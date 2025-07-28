#!/bin/bash

# orchestration-progress-reporter.sh
# Specialized hook for reporting real-time progress of conversations to orchestrator hub
# Integrates with health daemon PID 37803 and SQLite coordination system

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
HEALTH_DAEMON_STATUS="$PROJECT_ROOT/data/monitoring/health_daemon_status.json"
CONVERSATIONS_DB="$PROJECT_ROOT/data/orchestration/conversations.db"
PROGRESS_LOG="$PROJECT_ROOT/.claude/logs/orchestration-progress.log"

# Environment variables from Claude hooks system
TOOL_NAME="${1:-$CLAUDE_TOOL_NAME}"
TOOL_INPUT="${2:-$CLAUDE_TOOL_INPUT}"
TOOL_OUTPUT="${3:-$CLAUDE_TOOL_OUTPUT}"
CONVERSATION_ID="${CONVERSATION_ID:-hooks-integration-specialist-144944}"
TASK_ID="${TASK_ID:-582903d9-f10e-4da6-bc0b-78e4944a68c9}"
ORCHESTRATOR_HUB="${ORCHESTRATOR_HUB:-orchestrator-hub-coordinator}"

# Logging function
log_progress() {
    local level="$1"
    local message="$2"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$timestamp] [$level] [$CONVERSATION_ID] $message" >> "$PROGRESS_LOG"
}

# Verify health daemon is running
verify_health_daemon() {
    if [[ ! -f "$HEALTH_DAEMON_STATUS" ]]; then
        log_progress "WARNING" "Health daemon status file not found"
        return 1
    fi
    
    local daemon_pid=$(jq -r '.pid // empty' "$HEALTH_DAEMON_STATUS" 2>/dev/null || echo "")
    if [[ -z "$daemon_pid" ]] || ! ps -p "$daemon_pid" > /dev/null 2>&1; then
        log_progress "ERROR" "Health daemon not running (PID: $daemon_pid)"
        return 1
    fi
    
    log_progress "INFO" "Health daemon verified (PID: $daemon_pid)"
    return 0
}

# Extract progress metrics from tool usage
extract_progress_metrics() {
    local tool_name="$1"
    local tool_input="$2"
    local tool_output="$3"
    
    local progress_data="{}"
    
    # Tool-specific progress extraction
    case "$tool_name" in
        "Task")
            # Extract subagent deployment information
            local subagent_type=$(echo "$tool_input" | jq -r '.subagent_type // empty' 2>/dev/null || echo "")
            local description=$(echo "$tool_input" | jq -r '.description // empty' 2>/dev/null || echo "")
            if [[ -n "$subagent_type" ]]; then
                progress_data=$(jq -n \
                    --arg type "subagent_deployment" \
                    --arg subagent "$subagent_type" \
                    --arg desc "$description" \
                    '{
                        type: $type,
                        subagent_type: $subagent,
                        description: $desc,
                        timestamp: now
                    }')
            fi
            ;;
        "TodoWrite")
            # Extract todo status changes
            local todos=$(echo "$tool_input" | jq -r '.todos // empty' 2>/dev/null || echo "")
            if [[ -n "$todos" ]]; then
                local completed_count=$(echo "$todos" | jq '[.[] | select(.status == "completed")] | length' 2>/dev/null || echo "0")
                local in_progress_count=$(echo "$todos" | jq '[.[] | select(.status == "in_progress")] | length' 2>/dev/null || echo "0")
                local pending_count=$(echo "$todos" | jq '[.[] | select(.status == "pending")] | length' 2>/dev/null || echo "0")
                
                progress_data=$(jq -n \
                    --arg type "todo_status_update" \
                    --argjson completed "$completed_count" \
                    --argjson in_progress "$in_progress_count" \
                    --argjson pending "$pending_count" \
                    '{
                        type: $type,
                        completed: $completed,
                        in_progress: $in_progress,
                        pending: $pending,
                        timestamp: now
                    }')
            fi
            ;;
        "Read"|"Write"|"Edit"|"MultiEdit")
            # Extract file operations
            progress_data=$(jq -n \
                --arg type "file_operation" \
                --arg tool "$tool_name" \
                --arg file_count "1" \
                '{
                    type: $type,
                    operation: $tool,
                    file_count: ($file_count | tonumber),
                    timestamp: now
                }')
            ;;
        "Bash")
            # Extract command execution
            local command=$(echo "$tool_input" | jq -r '.command // empty' 2>/dev/null || echo "$tool_input")
            progress_data=$(jq -n \
                --arg type "command_execution" \
                --arg cmd "$command" \
                '{
                    type: $type,
                    command: $cmd,
                    timestamp: now
                }')
            ;;
        *)
            # Generic tool usage
            progress_data=$(jq -n \
                --arg type "tool_usage" \
                --arg tool "$tool_name" \
                '{
                    type: $type,
                    tool: $tool,
                    timestamp: now
                }')
            ;;
    esac
    
    echo "$progress_data"
}

# Update SQLite coordination database
update_coordination_db() {
    local progress_data="$1"
    
    if [[ ! -f "$CONVERSATIONS_DB" ]]; then
        log_progress "ERROR" "Conversations database not found: $CONVERSATIONS_DB"
        return 1
    fi
    
    # Update task status with progress metadata
    local metadata=$(echo "$progress_data" | jq -c '.')
    local update_timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    sqlite3 "$CONVERSATIONS_DB" "
        UPDATE conversation_tasks 
        SET 
            status = 'in_progress',
            metadata = json_patch(COALESCE(metadata, '{}'), '$metadata'),
            updated_at = '$update_timestamp'
        WHERE task_id = '$TASK_ID';
        
        INSERT OR IGNORE INTO conversation_registry (conversation_id, status, capabilities, last_seen)
        VALUES ('$CONVERSATION_ID', 'active', '[\"hooks-integration\", \"real-time-monitoring\"]', '$update_timestamp');
        
        UPDATE conversation_registry 
        SET last_seen = '$update_timestamp'
        WHERE conversation_id = '$CONVERSATION_ID';
    " 2>/dev/null || {
        log_progress "ERROR" "Failed to update coordination database"
        return 1
    }
    
    log_progress "INFO" "Updated coordination database with progress: $metadata"
}

# Send progress report to orchestrator hub
send_progress_report() {
    local progress_data="$1"
    
    # Create progress message for orchestrator
    local message_content=$(jq -n \
        --arg conv_id "$CONVERSATION_ID" \
        --arg task_id "$TASK_ID" \
        --argjson progress "$progress_data" \
        '{
            conversation_id: $conv_id,
            task_id: $task_id,
            progress: $progress,
            reported_at: now
        }')
    
    local message_id="msg-$(date +%s)-$(uuidgen | tr '[:upper:]' '[:lower:]' | head -c 8)"
    
    # Insert message into coordination system
    sqlite3 "$CONVERSATIONS_DB" "
        INSERT INTO conversation_messages 
        (message_id, from_conversation, to_conversation, message_type, content, created_at)
        VALUES (
            '$message_id',
            '$CONVERSATION_ID',
            '$ORCHESTRATOR_HUB',
            'progress_report',
            '$message_content',
            datetime('now')
        );
    " 2>/dev/null || {
        log_progress "ERROR" "Failed to send progress report to orchestrator"
        return 1
    }
    
    log_progress "INFO" "Sent progress report to orchestrator: $message_id"
}

# Update health daemon with orchestration metrics
update_health_daemon() {
    local progress_data="$1"
    
    # Extract metrics for health daemon
    local metric_type=$(echo "$progress_data" | jq -r '.type // "unknown"')
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    # Create health update file for daemon to pick up
    local health_update_file="$PROJECT_ROOT/data/monitoring/orchestration-update-$(date +%s).json"
    
    jq -n \
        --arg conv_id "$CONVERSATION_ID" \
        --arg task_id "$TASK_ID" \
        --arg metric_type "$metric_type" \
        --argjson progress "$progress_data" \
        --arg timestamp "$timestamp" \
        '{
            source: "orchestration-hooks",
            conversation_id: $conv_id,
            task_id: $task_id,
            metric_type: $metric_type,
            progress: $progress,
            timestamp: $timestamp
        }' > "$health_update_file"
    
    log_progress "INFO" "Created health daemon update: $health_update_file"
}

# Main execution
main() {
    # Create log directory if it doesn't exist
    mkdir -p "$(dirname "$PROGRESS_LOG")"
    
    log_progress "INFO" "Starting orchestration progress report for tool: $TOOL_NAME"
    
    # Verify health daemon is running
    if ! verify_health_daemon; then
        log_progress "WARNING" "Proceeding without health daemon verification"
    fi
    
    # Extract progress metrics from tool usage
    local progress_data
    progress_data=$(extract_progress_metrics "$TOOL_NAME" "$TOOL_INPUT" "$TOOL_OUTPUT")
    
    if [[ "$progress_data" == "{}" ]]; then
        log_progress "DEBUG" "No significant progress metrics extracted for tool: $TOOL_NAME"
        exit 0
    fi
    
    # Update coordination database
    if update_coordination_db "$progress_data"; then
        log_progress "INFO" "Successfully updated coordination database"
    else
        log_progress "ERROR" "Failed to update coordination database"
    fi
    
    # Send progress report to orchestrator
    if send_progress_report "$progress_data"; then
        log_progress "INFO" "Successfully sent progress report to orchestrator"
    else
        log_progress "ERROR" "Failed to send progress report to orchestrator"
    fi
    
    # Update health daemon
    update_health_daemon "$progress_data"
    
    log_progress "INFO" "Orchestration progress reporting completed"
}

# Execute main function if script is run directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi