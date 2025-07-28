#!/bin/bash

# progress-update-handler.sh
# Implements real-time progress update notification for specialist→orchestrator communication
# Based on progress notification protocol design from 2025-07-28 15:02

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
PROGRESS_DIR="$PROJECT_ROOT/data/orchestration/progress_updates"
CONVERSATIONS_DB="$PROJECT_ROOT/data/orchestration/conversations.db"
COORDINATION_LOG="$PROJECT_ROOT/data/orchestration/coordination_logs/$(date +%Y-%m-%d)_coordination.log"
HEALTH_DAEMON_STATUS="$PROJECT_ROOT/data/monitoring/health_daemon_status.json"

# Environment variables
TASK_ID="${TASK_ID:-}"
SPECIALIST_SESSION="${SPECIALIST_SESSION:-$(basename "$0" .sh)-$(date +%s)}"
CONVERSATION_ID="${CONVERSATION_ID:-$SPECIALIST_SESSION}"
ORCHESTRATOR_HUB="${ORCHESTRATOR_HUB:-orchestrator-hub-coordinator}"

# Logging function
log_progress() {
    local level="$1"
    local message="$2"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    # Create log directory if it doesn't exist
    mkdir -p "$(dirname "$COORDINATION_LOG")"
    
    echo "[$timestamp] [$level] [PROGRESS_UPDATE] [$TASK_ID] $message" >> "$COORDINATION_LOG"
}

# Validate required parameters
validate_parameters() {
    if [[ -z "$TASK_ID" ]]; then
        log_progress "ERROR" "TASK_ID environment variable is required"
        return 1
    fi
    
    if [[ -z "$SPECIALIST_SESSION" ]]; then
        log_progress "ERROR" "SPECIALIST_SESSION environment variable is required"
        return 1
    fi
    
    return 0
}

# Verify task delegation exists
verify_task_delegation() {
    local task_id="$1"
    local delegation_file="$PROJECT_ROOT/data/orchestration/task_delegations/${task_id}_delegation.json"
    
    if [[ ! -f "$delegation_file" ]]; then
        log_progress "ERROR" "Task delegation not found: $delegation_file"
        return 1
    fi
    
    log_progress "INFO" "Task delegation verified: $delegation_file"
    return 0
}

# Calculate progress percentage from various indicators
calculate_progress_percentage() {
    local current_milestone="$1"
    local deliverables_status="$2"
    local manual_percentage="${3:-}"
    
    # If manual percentage provided, use it
    if [[ -n "$manual_percentage" ]] && [[ "$manual_percentage" =~ ^[0-9]+$ ]] && [[ "$manual_percentage" -le 100 ]]; then
        echo "$manual_percentage"
        return 0
    fi
    
    # Calculate based on milestone progression
    local progress=0
    case "$current_milestone" in
        "task_acknowledgment"|"started"|"beginning")
            progress=10
            ;;
        "research"|"analysis"|"planning")
            progress=25
            ;;
        "implementation"|"development"|"execution")
            progress=50
            ;;
        "testing"|"validation"|"review")
            progress=75
            ;;
        "completion"|"finalization"|"handoff")
            progress=90
            ;;
        "completed"|"done"|"finished")
            progress=100
            ;;
        *)
            # Analyze deliverables status if available
            if [[ "$deliverables_status" != "{}" ]] && command -v jq >/dev/null 2>&1; then
                local total_deliverables=$(echo "$deliverables_status" | jq 'length' 2>/dev/null || echo "1")
                local completed_deliverables=$(echo "$deliverables_status" | jq '[.[] | select(.status == "completed")] | length' 2>/dev/null || echo "0")
                
                if [[ "$total_deliverables" -gt 0 ]]; then
                    progress=$(( (completed_deliverables * 100) / total_deliverables ))
                else
                    progress=25  # Default progress if cannot determine
                fi
            else
                progress=25  # Default progress
            fi
            ;;
    esac
    
    echo "$progress"
}

# Estimate completion time based on progress and history
estimate_completion() {
    local progress_percentage="$1"
    local task_id="$2"
    
    local current_time=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
    
    # Simple estimation based on progress percentage
    if [[ "$progress_percentage" -ge 90 ]]; then
        # Almost done - estimate 15 minutes
        date -u -d "+15 minutes" '+%Y-%m-%dT%H:%M:%SZ' 2>/dev/null || echo "$current_time"
    elif [[ "$progress_percentage" -ge 75 ]]; then
        # Near completion - estimate 30 minutes
        date -u -d "+30 minutes" '+%Y-%m-%dT%H:%M:%SZ' 2>/dev/null || echo "$current_time"
    elif [[ "$progress_percentage" -ge 50 ]]; then
        # Halfway - estimate 1 hour
        date -u -d "+1 hour" '+%Y-%m-%dT%H:%M:%SZ' 2>/dev/null || echo "$current_time"
    elif [[ "$progress_percentage" -ge 25 ]]; then
        # Early stage - estimate 2 hours
        date -u -d "+2 hours" '+%Y-%m-%dT%H:%M:%SZ' 2>/dev/null || echo "$current_time"
    else
        # Just started - estimate 3 hours
        date -u -d "+3 hours" '+%Y-%m-%dT%H:%M:%SZ' 2>/dev/null || echo "$current_time"
    fi
}

# Create progress update record
create_progress_update() {
    local progress_percentage="$1"
    local current_milestone="$2"
    local deliverables_status="$3"
    local blocking_issues="$4"
    local message="${5:-Progress update}"
    
    local update_timestamp=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
    local estimated_completion=$(estimate_completion "$progress_percentage" "$TASK_ID")
    local progress_file="$PROGRESS_DIR/${TASK_ID}_progress_$(date +%s).json"
    
    # Ensure progress directory exists
    mkdir -p "$PROGRESS_DIR"
    
    # Create progress update record based on protocol design
    local progress_data=$(jq -n \
        --arg task_id "$TASK_ID" \
        --arg specialist_session "$SPECIALIST_SESSION" \
        --arg update_timestamp "$update_timestamp" \
        --argjson progress_percentage "$progress_percentage" \
        --arg current_milestone "$current_milestone" \
        --argjson deliverables_status "$deliverables_status" \
        --argjson blocking_issues "$blocking_issues" \
        --arg estimated_completion "$estimated_completion" \
        --arg message "$message" \
        --arg conversation_id "$CONVERSATION_ID" \
        '{
            progress_update: {
                task_id: $task_id,
                specialist_session: $specialist_session,
                update_timestamp: $update_timestamp,
                progress_percentage: $progress_percentage,
                current_milestone: $current_milestone,
                deliverables_status: $deliverables_status,
                blocking_issues: $blocking_issues,
                estimated_completion: $estimated_completion,
                message: $message,
                conversation_id: $conversation_id,
                update_sequence: null,
                created_by: "progress-update-handler"
            },
            protocol_version: "1.0",
            health_monitor_integration: {
                pid: null,
                cycle: null,
                coordination_metrics: true
            }
        }')
    
    # Add sequence number based on existing updates
    local sequence_number=$(ls -1 "$PROGRESS_DIR/${TASK_ID}_progress_"*.json 2>/dev/null | wc -l)
    sequence_number=$((sequence_number + 1))
    
    progress_data=$(echo "$progress_data" | jq \
        --argjson seq "$sequence_number" \
        '.progress_update.update_sequence = $seq')
    
    # Add health daemon info if available
    if [[ -f "$HEALTH_DAEMON_STATUS" ]]; then
        local daemon_pid=$(jq -r '.pid // null' "$HEALTH_DAEMON_STATUS" 2>/dev/null || echo "null")
        local cycle_count=$(jq -r '.cycle_count // null' "$HEALTH_DAEMON_STATUS" 2>/dev/null || echo "null")
        
        progress_data=$(echo "$progress_data" | jq \
            --argjson pid "$daemon_pid" \
            --argjson cycle "$cycle_count" \
            '.health_monitor_integration.pid = $pid | .health_monitor_integration.cycle = $cycle')
    fi
    
    # Write progress update record
    echo "$progress_data" > "$progress_file"
    
    log_progress "INFO" "Created progress update record: $progress_file"
    echo "$progress_file"
}

# Update task status in SQLite database
update_task_status() {
    local progress_percentage="$1"
    local current_milestone="$2"
    local message="$3"
    
    if [[ ! -f "$CONVERSATIONS_DB" ]]; then
        log_progress "ERROR" "Conversations database not found: $CONVERSATIONS_DB"
        return 1
    fi
    
    local update_timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    local status="in_progress"
    
    # Determine status based on progress
    if [[ "$progress_percentage" -ge 100 ]]; then
        status="completed"
    elif [[ "$progress_percentage" -ge 90 ]]; then
        status="finalizing"
    elif [[ "$progress_percentage" -ge 10 ]]; then
        status="in_progress"
    else
        status="starting"
    fi
    
    # Update task metadata with progress information
    local progress_metadata=$(jq -n \
        --argjson progress "$progress_percentage" \
        --arg milestone "$current_milestone" \
        --arg last_update "$update_timestamp" \
        --arg update_message "$message" \
        '{
            progress_percentage: $progress,
            current_milestone: $milestone,
            last_progress_update: $last_update,
            update_message: $update_message,
            specialist_session: "'"$SPECIALIST_SESSION"'"
        }')
    
    # Update task in database
    sqlite3 "$CONVERSATIONS_DB" "
        UPDATE conversation_tasks 
        SET 
            status = '$status',
            metadata = json_patch(COALESCE(metadata, '{}'), '$progress_metadata'),
            updated_at = '$update_timestamp'
        WHERE task_id = '$TASK_ID';
    " 2>/dev/null || {
        log_progress "ERROR" "Failed to update task status in database"
        return 1
    }
    
    # Update specialist conversation registry
    sqlite3 "$CONVERSATIONS_DB" "
        UPDATE conversation_registry 
        SET 
            last_seen = '$update_timestamp',
            metadata = json_patch(COALESCE(metadata, '{}'), '$progress_metadata')
        WHERE conversation_id = '$CONVERSATION_ID';
    " 2>/dev/null || {
        log_progress "WARNING" "Failed to update conversation registry"
    }
    
    log_progress "INFO" "Updated task status to '$status' with $progress_percentage% progress"
}

# Send progress notification to orchestrator
send_progress_notification() {
    local progress_file="$1"
    
    if [[ ! -f "$progress_file" ]]; then
        log_progress "ERROR" "Progress file not found: $progress_file"
        return 1
    fi
    
    local message_id="msg-$(date +%s)-$(uuidgen | tr '[:upper:]' '[:lower:]' | head -c 8 2>/dev/null || echo "$(( RANDOM % 10000 ))")"
    local progress_content=$(cat "$progress_file")
    local created_timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    # Insert progress message into coordination system
    sqlite3 "$CONVERSATIONS_DB" "
        INSERT INTO conversation_messages (
            message_id, from_conversation, to_conversation, 
            message_type, content, created_at
        ) VALUES (
            '$message_id',
            '$CONVERSATION_ID',
            '$ORCHESTRATOR_HUB',
            'progress_update',
            '$progress_content',
            '$created_timestamp'
        );
    " 2>/dev/null || {
        log_progress "ERROR" "Failed to send progress notification"
        return 1
    }
    
    log_progress "INFO" "Sent progress notification to orchestrator: $message_id"
    echo "$message_id"
}

# Update health daemon with progress metrics
update_health_metrics() {
    local progress_percentage="$1"
    local current_milestone="$2"
    
    local health_update_file="$PROJECT_ROOT/data/monitoring/orchestration-update-$(date +%s).json"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    jq -n \
        --arg source "progress-update-handler" \
        --arg task_id "$TASK_ID" \
        --arg conversation_id "$CONVERSATION_ID" \
        --arg specialist_session "$SPECIALIST_SESSION" \
        --arg metric_type "progress_update" \
        --argjson progress "$progress_percentage" \
        --arg milestone "$current_milestone" \
        --arg timestamp "$timestamp" \
        '{
            source: $source,
            task_id: $task_id,
            conversation_id: $conversation_id,
            specialist_session: $specialist_session,
            metric_type: $metric_type,
            progress_data: {
                progress_percentage: $progress,
                current_milestone: $milestone,
                protocol_version: "1.0"
            },
            timestamp: $timestamp
        }' > "$health_update_file"
    
    log_progress "INFO" "Created health daemon update: $health_update_file"
}

# Main progress update function
update_progress() {
    local current_milestone="$1"
    local message="${2:-Progress update}"
    local deliverables_status="${3:-{}}"
    local blocking_issues="${4:-[]}"
    local manual_percentage="${5:-}"
    
    log_progress "INFO" "Starting progress update for milestone: $current_milestone"
    
    # Validate required parameters
    if ! validate_parameters; then
        return 1
    fi
    
    # Verify task delegation exists
    if ! verify_task_delegation "$TASK_ID"; then
        return 1
    fi
    
    # Calculate progress percentage
    local progress_percentage
    progress_percentage=$(calculate_progress_percentage "$current_milestone" "$deliverables_status" "$manual_percentage")
    
    log_progress "INFO" "Calculated progress: $progress_percentage%"
    
    # Create progress update record
    local progress_file
    progress_file=$(create_progress_update \
        "$progress_percentage" \
        "$current_milestone" \
        "$deliverables_status" \
        "$blocking_issues" \
        "$message")
    
    if [[ $? -ne 0 ]] || [[ ! -f "$progress_file" ]]; then
        log_progress "ERROR" "Failed to create progress update record"
        return 1
    fi
    
    # Update task status in database
    if update_task_status "$progress_percentage" "$current_milestone" "$message"; then
        log_progress "INFO" "Task status updated in coordination database"
    else
        log_progress "ERROR" "Failed to update task status in database"
        return 1
    fi
    
    # Send progress notification to orchestrator
    local message_id
    message_id=$(send_progress_notification "$progress_file")
    if [[ $? -ne 0 ]]; then
        log_progress "ERROR" "Failed to send progress notification"
        return 1
    fi
    
    # Update health metrics
    update_health_metrics "$progress_percentage" "$current_milestone"
    
    log_progress "INFO" "Progress update completed successfully"
    
    # Output progress summary
    cat << EOF
PROGRESS UPDATE SUMMARY
======================
Task ID: $TASK_ID
Specialist Session: $SPECIALIST_SESSION
Progress: $progress_percentage%
Current Milestone: $current_milestone
Update File: $progress_file
Message ID: $message_id
Message: $message

Status: Progress update sent to orchestrator
Next: Continue with task execution or send completion confirmation
EOF
}

# Command line interface
main() {
    local action="${1:-update}"
    
    case "$action" in
        "update")
            local current_milestone="${2:-in_progress}"
            local message="${3:-Progress update}"
            local deliverables_status="${4:-{}}"
            local blocking_issues="${5:-[]}"
            local manual_percentage="${6:-}"
            
            update_progress "$current_milestone" "$message" "$deliverables_status" \
                           "$blocking_issues" "$manual_percentage"
            ;;
        "status")
            local task_id="${2:-$TASK_ID}"
            if [[ -n "$task_id" ]]; then
                echo "Progress updates for task: $task_id"
                ls -la "$PROGRESS_DIR/${task_id}_progress_"*.json 2>/dev/null | tail -5 || echo "No progress updates found"
                
                # Show latest update
                local latest_update=$(ls -t "$PROGRESS_DIR/${task_id}_progress_"*.json 2>/dev/null | head -1)
                if [[ -n "$latest_update" ]]; then
                    echo -e "\nLatest update:"
                    cat "$latest_update" | jq '.progress_update'
                fi
            else
                echo "TASK_ID environment variable required for status check"
            fi
            ;;
        "list")
            echo "All progress updates:"
            find "$PROGRESS_DIR" -name "*.json" -exec basename {} \; 2>/dev/null | sort || echo "No progress updates found"
            ;;
        *)
            cat << EOF
Usage: $0 [action] [parameters]

Actions:
  update [milestone] [message] [deliverables] [blocking_issues] [percentage] - Send progress update
  status [task_id] - Check progress status for task
  list - List all progress updates

Environment Variables:
  TASK_ID - Unique task identifier (required)
  SPECIALIST_SESSION - Specialist session identifier
  CONVERSATION_ID - Conversation identifier
  ORCHESTRATOR_HUB - Orchestrator session to notify

Examples:
  TASK_ID=550e8400-e29b-41d4-a716-446655440000 $0 update "implementation" "Working on core features"
  TASK_ID=550e8400-e29b-41d4-a716-446655440000 $0 update "testing" "Running validation tests" '{}' '[]' 75
  TASK_ID=550e8400-e29b-41d4-a716-446655440000 $0 status
EOF
            ;;
    esac
}

# Execute main function if script is run directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi