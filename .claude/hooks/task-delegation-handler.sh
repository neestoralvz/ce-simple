#!/bin/bash

# task-delegation-handler.sh
# Implements task delegation protocol for orchestrator-specialist coordination
# Based on progress notification protocol design from 2025-07-28 15:02

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
DELEGATIONS_DIR="$PROJECT_ROOT/data/orchestration/task_delegations"
CONVERSATIONS_DB="$PROJECT_ROOT/data/orchestration/conversations.db"
COORDINATION_LOG="$PROJECT_ROOT/data/orchestration/coordination_logs/$(date +%Y-%m-%d)_coordination.log"
HEALTH_DAEMON_STATUS="$PROJECT_ROOT/data/monitoring/health_daemon_status.json"

# Environment variables
TASK_ID="${TASK_ID:-$(uuidgen | tr '[:upper:]' '[:lower:]')}"
SPECIALIST_TYPE="${SPECIALIST_TYPE:-generic}"
ORCHESTRATOR_SESSION="${ORCHESTRATOR_SESSION:-orchestrator-hub-coordinator}"
CONVERSATION_ID="${CONVERSATION_ID:-$(basename "$0" .sh)-$(date +%s)}"

# Logging function
log_coordination() {
    local level="$1"
    local message="$2"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    # Create log directory if it doesn't exist
    mkdir -p "$(dirname "$COORDINATION_LOG")"
    
    echo "[$timestamp] [$level] [TASK_DELEGATION] [$TASK_ID] $message" >> "$COORDINATION_LOG"
}

# Generate UUID v4 if needed
generate_task_id() {
    if command -v uuidgen >/dev/null 2>&1; then
        uuidgen | tr '[:upper:]' '[:lower:]'
    else
        # Fallback UUID generation
        python3 -c "import uuid; print(str(uuid.uuid4()))" 2>/dev/null || \
        echo "task-$(date +%s)-$(( RANDOM % 10000 ))"
    fi
}

# Verify health daemon status
verify_health_daemon() {
    if [[ ! -f "$HEALTH_DAEMON_STATUS" ]]; then
        log_coordination "WARNING" "Health daemon status file not found"
        return 1
    fi
    
    local daemon_pid=$(jq -r '.pid // empty' "$HEALTH_DAEMON_STATUS" 2>/dev/null || echo "")
    if [[ -z "$daemon_pid" ]] || ! ps -p "$daemon_pid" > /dev/null 2>&1; then
        log_coordination "ERROR" "Health daemon not running (PID: $daemon_pid)"
        return 1
    fi
    
    log_coordination "INFO" "Health daemon verified (PID: $daemon_pid)"
    return 0
}

# Create task delegation record
create_delegation_record() {
    local specialist_type="$1"
    local expected_deliverables="$2"
    local progress_checkpoints="$3"
    local completion_criteria="$4"
    local description="${5:-Task delegation for $specialist_type}"
    
    local delegation_timestamp=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
    local delegation_file="$DELEGATIONS_DIR/${TASK_ID}_delegation.json"
    
    # Ensure delegation directory exists
    mkdir -p "$DELEGATIONS_DIR"
    
    # Create delegation record based on protocol design
    local delegation_data=$(jq -n \
        --arg task_id "$TASK_ID" \
        --arg specialist_type "$specialist_type" \
        --arg orchestrator_session "$ORCHESTRATOR_SESSION" \
        --arg delegation_timestamp "$delegation_timestamp" \
        --argjson expected_deliverables "$expected_deliverables" \
        --argjson progress_checkpoints "$progress_checkpoints" \
        --argjson completion_criteria "$completion_criteria" \
        --arg description "$description" \
        --arg conversation_id "$CONVERSATION_ID" \
        '{
            task_delegation: {
                task_id: $task_id,
                specialist_type: $specialist_type,
                orchestrator_session: $orchestrator_session,
                delegation_timestamp: $delegation_timestamp,
                expected_deliverables: $expected_deliverables,
                progress_checkpoints: $progress_checkpoints,
                completion_criteria: $completion_criteria,
                description: $description,
                conversation_id: $conversation_id,
                status: "delegated",
                created_by: "task-delegation-handler"
            },
            protocol_version: "1.0",
            health_monitor_integration: {
                pid: null,
                cycle: null,
                coordination_metrics: true
            }
        }')
    
    # Add health daemon info if available
    if [[ -f "$HEALTH_DAEMON_STATUS" ]]; then
        local daemon_pid=$(jq -r '.pid // null' "$HEALTH_DAEMON_STATUS" 2>/dev/null || echo "null")
        local cycle_count=$(jq -r '.cycle_count // null' "$HEALTH_DAEMON_STATUS" 2>/dev/null || echo "null")
        
        delegation_data=$(echo "$delegation_data" | jq \
            --argjson pid "$daemon_pid" \
            --argjson cycle "$cycle_count" \
            '.health_monitor_integration.pid = $pid | .health_monitor_integration.cycle = $cycle')
    fi
    
    # Write delegation record
    echo "$delegation_data" > "$delegation_file"
    
    log_coordination "INFO" "Created delegation record: $delegation_file"
    echo "$delegation_file"
}

# Register task in SQLite coordination database
register_task_in_db() {
    local specialist_type="$1"
    local description="$2"
    local priority="${3:-3}"
    
    if [[ ! -f "$CONVERSATIONS_DB" ]]; then
        log_coordination "ERROR" "Conversations database not found: $CONVERSATIONS_DB"
        return 1
    fi
    
    local created_timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    local metadata=$(jq -n \
        --arg specialist_type "$specialist_type" \
        --arg orchestrator_session "$ORCHESTRATOR_SESSION" \
        --arg delegation_method "task-delegation-handler" \
        '{
            specialist_type: $specialist_type,
            orchestrator_session: $orchestrator_session,
            delegation_method: $delegation_method,
            protocol_version: "1.0"
        }')
    
    # Insert task into conversation_tasks table
    sqlite3 "$CONVERSATIONS_DB" "
        INSERT INTO conversation_tasks (
            task_id, conversation_id, priority, status, task_type, 
            title, description, created_at, updated_at, metadata
        ) VALUES (
            '$TASK_ID',
            '$CONVERSATION_ID',
            $priority,
            'delegated',
            'specialist_task',
            'Specialist Task: $specialist_type',
            '$description',
            '$created_timestamp',
            '$created_timestamp',
            '$metadata'
        );
    " 2>/dev/null || {
        log_coordination "ERROR" "Failed to register task in coordination database"
        return 1
    }
    
    # Register conversation in registry if not exists
    sqlite3 "$CONVERSATIONS_DB" "
        INSERT OR IGNORE INTO conversation_registry (conversation_id, status, capabilities, last_seen, metadata)
        VALUES (
            '$CONVERSATION_ID', 
            'active', 
            '[\"task_delegation\", \"coordination\"]',
            '$created_timestamp',
            '{\"role\": \"specialist\", \"delegated_by\": \"$ORCHESTRATOR_SESSION\"}'
        );
        
        UPDATE conversation_registry 
        SET last_seen = '$created_timestamp'
        WHERE conversation_id = '$CONVERSATION_ID';
    " 2>/dev/null || {
        log_coordination "WARNING" "Failed to update conversation registry"
    }
    
    log_coordination "INFO" "Registered task in coordination database"
}

# Send delegation notification to specialist
send_delegation_notification() {
    local delegation_file="$1"
    
    if [[ ! -f "$delegation_file" ]]; then
        log_coordination "ERROR" "Delegation file not found: $delegation_file"
        return 1
    fi
    
    local message_id="msg-$(date +%s)-$(uuidgen | tr '[:upper:]' '[:lower:]' | head -c 8)"
    local delegation_content=$(cat "$delegation_file")
    local created_timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    # Insert delegation message into coordination system
    sqlite3 "$CONVERSATIONS_DB" "
        INSERT INTO conversation_messages (
            message_id, from_conversation, to_conversation, 
            message_type, content, created_at
        ) VALUES (
            '$message_id',
            '$ORCHESTRATOR_SESSION',
            '$CONVERSATION_ID',
            'task_delegation',
            '$delegation_content',
            '$created_timestamp'
        );
    " 2>/dev/null || {
        log_coordination "ERROR" "Failed to send delegation notification"
        return 1
    }
    
    log_coordination "INFO" "Sent delegation notification: $message_id"
    echo "$message_id"
}

# Update health daemon with delegation metrics
update_health_metrics() {
    local specialist_type="$1"
    
    local health_update_file="$PROJECT_ROOT/data/monitoring/orchestration-update-$(date +%s).json"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    jq -n \
        --arg source "task-delegation-handler" \
        --arg task_id "$TASK_ID" \
        --arg conversation_id "$CONVERSATION_ID" \
        --arg specialist_type "$specialist_type" \
        --arg metric_type "task_delegation" \
        --arg timestamp "$timestamp" \
        '{
            source: $source,
            task_id: $task_id,
            conversation_id: $conversation_id,
            metric_type: $metric_type,
            delegation_data: {
                specialist_type: $specialist_type,
                orchestrator_session: "'"$ORCHESTRATOR_SESSION"'",
                protocol_version: "1.0"
            },
            timestamp: $timestamp
        }' > "$health_update_file"
    
    log_coordination "INFO" "Created health daemon update: $health_update_file"
}

# Main delegation function
delegate_task() {
    local specialist_type="$1"
    local description="$2"
    local expected_deliverables="${3:-[\"completion_confirmation\"]}"
    local progress_checkpoints="${4:-[\"task_acknowledgment\", \"progress_update\", \"completion\"]}"
    local completion_criteria="${5:-{\"explicit_confirmation\": true, \"deliverables_validated\": true}}"
    local priority="${6:-3}"
    
    log_coordination "INFO" "Starting task delegation to $specialist_type"
    
    # Verify health daemon if available
    verify_health_daemon || log_coordination "WARNING" "Proceeding without health daemon verification"
    
    # Generate task ID if not provided
    if [[ -z "$TASK_ID" ]] || [[ "$TASK_ID" == "$(basename "$0" .sh)-$(date +%s)" ]]; then
        TASK_ID=$(generate_task_id)
        log_coordination "INFO" "Generated task ID: $TASK_ID"
    fi
    
    # Create delegation record
    local delegation_file
    delegation_file=$(create_delegation_record \
        "$specialist_type" \
        "$expected_deliverables" \
        "$progress_checkpoints" \
        "$completion_criteria" \
        "$description")
    
    if [[ $? -ne 0 ]] || [[ ! -f "$delegation_file" ]]; then
        log_coordination "ERROR" "Failed to create delegation record"
        return 1
    fi
    
    # Register task in coordination database
    if register_task_in_db "$specialist_type" "$description" "$priority"; then
        log_coordination "INFO" "Task registered in coordination database"
    else
        log_coordination "ERROR" "Failed to register task in database"
        return 1
    fi
    
    # Send delegation notification
    local message_id
    message_id=$(send_delegation_notification "$delegation_file")
    if [[ $? -ne 0 ]]; then
        log_coordination "ERROR" "Failed to send delegation notification"
        return 1
    fi
    
    # Update health metrics
    update_health_metrics "$specialist_type"
    
    log_coordination "INFO" "Task delegation completed successfully"
    
    # Output delegation summary
    cat << EOF
TASK DELEGATION SUMMARY
======================
Task ID: $TASK_ID
Specialist Type: $specialist_type
Conversation ID: $CONVERSATION_ID
Orchestrator Session: $ORCHESTRATOR_SESSION
Delegation File: $delegation_file
Message ID: $message_id
Status: Successfully delegated

Next Steps:
1. Specialist will receive delegation notification
2. Progress updates expected via progress-update-handler
3. Completion confirmation required via completion-handler
EOF
}

# Command line interface
main() {
    local action="${1:-delegate}"
    
    case "$action" in
        "delegate")
            local specialist_type="${2:-generic}"
            local description="${3:-Specialist task delegation}"
            local expected_deliverables="${4:-[\"completion_confirmation\"]}"
            local progress_checkpoints="${5:-[\"task_acknowledgment\", \"progress_update\", \"completion\"]}"
            local completion_criteria="${6:-{\"explicit_confirmation\": true, \"deliverables_validated\": true}}"
            local priority="${7:-3}"
            
            delegate_task "$specialist_type" "$description" "$expected_deliverables" \
                         "$progress_checkpoints" "$completion_criteria" "$priority"
            ;;
        "status")
            local task_id="${2:-$TASK_ID}"
            if [[ -f "$DELEGATIONS_DIR/${task_id}_delegation.json" ]]; then
                echo "Delegation record found:"
                cat "$DELEGATIONS_DIR/${task_id}_delegation.json" | jq '.'
            else
                echo "No delegation record found for task ID: $task_id"
            fi
            ;;
        "list")
            echo "Active delegations:"
            ls -la "$DELEGATIONS_DIR"/*.json 2>/dev/null || echo "No delegations found"
            ;;
        *)
            cat << EOF
Usage: $0 [action] [parameters]

Actions:
  delegate [specialist_type] [description] - Delegate task to specialist
  status [task_id] - Check delegation status
  list - List all active delegations

Environment Variables:
  TASK_ID - Unique task identifier (auto-generated if not provided)
  SPECIALIST_TYPE - Type of specialist for delegation
  ORCHESTRATOR_SESSION - Orchestrator session identifier
  CONVERSATION_ID - Conversation identifier

Examples:
  $0 delegate "Research Specialist" "Analyze system architecture"
  $0 status 550e8400-e29b-41d4-a716-446655440000
  $0 list
EOF
            ;;
    esac
}

# Execute main function if script is run directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi