#!/bin/bash

# orchestrator-interface.sh
# Interface for orchestrator hub to query real-time progress of specialized conversations
# Provides API-like functionality for conversation monitoring

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
CONVERSATIONS_DB="$PROJECT_ROOT/data/orchestration/conversations.db"
PROGRESS_LOG="$PROJECT_ROOT/.claude/logs/orchestration-progress.log"
HEALTH_DAEMON_STATUS="$PROJECT_ROOT/data/monitoring/health_daemon_status.json"

# Command functions
cmd_list_active_conversations() {
    sqlite3 "$CONVERSATIONS_DB" -header -json "
        SELECT 
            conversation_id,
            status,
            capabilities,
            last_seen,
            datetime(last_seen, 'localtime') as last_seen_local
        FROM conversation_registry 
        WHERE status = 'active'
        ORDER BY last_seen DESC;
    "
}

cmd_get_conversation_progress() {
    local conversation_id="$1"
    
    # Get task progress
    local tasks=$(sqlite3 "$CONVERSATIONS_DB" -header -json "
        SELECT 
            task_id,
            status,
            task_type,
            title,
            description,
            assigned_to,
            metadata,
            datetime(created_at, 'localtime') as created_at,
            datetime(updated_at, 'localtime') as updated_at
        FROM conversation_tasks 
        WHERE conversation_id = '$conversation_id'
        ORDER BY priority ASC, created_at ASC;
    ")
    
    # Get recent messages
    local messages=$(sqlite3 "$CONVERSATIONS_DB" -header -json "
        SELECT 
            message_id,
            from_conversation,
            message_type,
            content,
            datetime(created_at, 'localtime') as created_at
        FROM conversation_messages 
        WHERE from_conversation = '$conversation_id' OR to_conversation = '$conversation_id'
        ORDER BY created_at DESC
        LIMIT 10;
    ")
    
    # Combine into progress report
    jq -n \
        --arg conv_id "$conversation_id" \
        --argjson tasks "$tasks" \
        --argjson messages "$messages" \
        '{
            conversation_id: $conv_id,
            tasks: $tasks,
            recent_messages: $messages,
            generated_at: now
        }'
}

cmd_get_real_time_metrics() {
    local conversation_id="${1:-}"
    
    # Get health daemon status
    local health_status="{}"
    if [[ -f "$HEALTH_DAEMON_STATUS" ]]; then
        health_status=$(cat "$HEALTH_DAEMON_STATUS")
    fi
    
    # Get recent progress log entries
    local recent_logs="[]"
    if [[ -f "$PROGRESS_LOG" ]]; then
        recent_logs=$(tail -n 50 "$PROGRESS_LOG" | jq -Rs '
            split("\n") | 
            map(select(length > 0)) |
            map(
                capture("\\[(?<timestamp>[^\\]]+)\\] \\[(?<level>[^\\]]+)\\] \\[(?<conv_id>[^\\]]+)\\] (?<message>.*)") //
                {timestamp: "", level: "", conv_id: "", message: .}
            ) |
            if $conv_id != "" then 
                map(select(.conv_id == $conv_id))
            else 
                .
            end |
            reverse
        ' --arg conv_id "$conversation_id")
    fi
    
    # Combine metrics
    jq -n \
        --argjson health "$health_status" \
        --argjson logs "$recent_logs" \
        --arg conv_filter "$conversation_id" \
        '{
            health_daemon: $health,
            recent_activity: $logs,
            conversation_filter: $conv_filter,
            generated_at: now
        }'
}

cmd_send_orchestrator_command() {
    local target_conversation="$1"
    local command_type="$2"
    local command_data="$3"
    
    local message_id="cmd-$(date +%s)-$(uuidgen | tr '[:upper:]' '[:lower:]' | head -c 8)"
    local orchestrator_id="orchestrator-hub-coordinator"
    
    # Create command message
    local message_content=$(jq -n \
        --arg cmd_type "$command_type" \
        --arg cmd_data "$command_data" \
        '{
            command_type: $cmd_type,
            command_data: $cmd_data,
            sent_at: now
        }')
    
    # Insert command message
    sqlite3 "$CONVERSATIONS_DB" "
        INSERT INTO conversation_messages 
        (message_id, from_conversation, to_conversation, message_type, content, created_at)
        VALUES (
            '$message_id',
            '$orchestrator_id',
            '$target_conversation',
            'orchestrator_command',
            '$message_content',
            datetime('now')
        );
    "
    
    echo "{\"message_id\": \"$message_id\", \"status\": \"sent\", \"target\": \"$target_conversation\"}"
}

cmd_get_system_status() {
    # Database status
    local db_size=$(stat -f%z "$CONVERSATIONS_DB" 2>/dev/null || echo "0")
    local db_last_modified=$(stat -f%m "$CONVERSATIONS_DB" 2>/dev/null || echo "0")
    
    # Active conversations count
    local active_count=$(sqlite3 "$CONVERSATIONS_DB" "SELECT COUNT(*) FROM conversation_registry WHERE status = 'active';" 2>/dev/null || echo "0")
    
    # Pending tasks count
    local pending_tasks=$(sqlite3 "$CONVERSATIONS_DB" "SELECT COUNT(*) FROM conversation_tasks WHERE status = 'pending';" 2>/dev/null || echo "0")
    
    # Health daemon status
    local health_status="{}"
    if [[ -f "$HEALTH_DAEMON_STATUS" ]]; then
        health_status=$(cat "$HEALTH_DAEMON_STATUS")
    fi
    
    jq -n \
        --argjson db_size "$db_size" \
        --argjson db_modified "$db_last_modified" \
        --argjson active_conversations "$active_count" \
        --argjson pending_tasks "$pending_tasks" \
        --argjson health "$health_status" \
        '{
            database: {
                size_bytes: $db_size,
                last_modified: $db_modified
            },
            orchestration: {
                active_conversations: $active_conversations,
                pending_tasks: $pending_tasks
            },
            health_daemon: $health,
            generated_at: now
        }'
}

# Main command dispatcher
main() {
    local command="${1:-help}"
    
    case "$command" in
        "list"|"list-conversations")
            cmd_list_active_conversations
            ;;
        "progress")
            if [[ $# -lt 2 ]]; then
                echo "Error: conversation_id required" >&2
                exit 1
            fi
            cmd_get_conversation_progress "$2"
            ;;
        "metrics")
            cmd_get_real_time_metrics "${2:-}"
            ;;
        "command"|"send-command")
            if [[ $# -lt 4 ]]; then
                echo "Error: target_conversation, command_type, and command_data required" >&2
                exit 1
            fi
            cmd_send_orchestrator_command "$2" "$3" "$4"
            ;;
        "status"|"system-status")
            cmd_get_system_status
            ;;
        "help"|*)
            cat << EOF
Orchestrator Interface Commands:

  list                           List active conversations
  progress <conversation_id>     Get progress for specific conversation
  metrics [conversation_id]      Get real-time metrics (optionally filtered)
  command <target> <type> <data> Send command to conversation
  status                         Get overall system status
  help                          Show this help

Examples:
  $0 list
  $0 progress hooks-integration-specialist-144944
  $0 metrics hooks-integration-specialist-144944
  $0 command hooks-integration-specialist-144944 priority-update high
  $0 status

EOF
            ;;
    esac
}

# Execute if run directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi