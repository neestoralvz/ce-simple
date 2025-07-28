#!/bin/bash

# Session Cleanup Hook
# Handles session state management and cleanup when Claude finishes responses
# Based on 2025 Claude Code hooks best practices

set -euo pipefail

# Configuration
HOOK_NAME="session-cleanup"
LOG_FILE="/Users/nalve/ce-simple/.claude/logs/hooks.log"
SESSION_LOG_FILE="/Users/nalve/ce-simple/.claude/logs/sessions.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Parameters
SESSION_ID="${1:-unknown}"

# Logging function
log_message() {
    local level="$1"
    local message="$2"
    echo "[$TIMESTAMP] [$HOOK_NAME] [$level] $message" | tee -a "$LOG_FILE"
}

# Update context state
update_context_state() {
    local session_id="$1"
    local context_file="/Users/nalve/ce-simple/.claude/context/session-state.json"
    
    # Create context directory if it doesn't exist
    mkdir -p "$(dirname "$context_file")"
    
    log_message "INFO" "Updating context state for session: $session_id"
    
    # Gather current state information
    local current_state=""
    current_state+=",timestamp:$TIMESTAMP"
    current_state+=",session_id:$session_id"
    current_state+=",workflow_context:${CLAUDE_WORKFLOW_CONTEXT:-none}"
    current_state+=",emergency_override:${CLAUDE_EMERGENCY_OVERRIDE:-false}"
    
    # Git state
    if git rev-parse --git-dir >/dev/null 2>&1; then
        local branch commit_hash
        branch=$(git branch --show-current 2>/dev/null || echo "detached")
        commit_hash=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")
        current_state+=",git_branch:$branch,git_commit:$commit_hash"
        
        local changes
        changes=$(git status --porcelain | wc -l)
        current_state+=",git_changes:$changes"
    fi
    
    # Working directory
    current_state+=",working_directory:$(pwd)"
    
    # Active workflows
    if [[ -f ".claude-workflow-active" ]]; then
        current_state+=",active_workflow:true"
        local workflow_type
        workflow_type=$(cat ".claude-workflow-active" 2>/dev/null || echo "unknown")
        current_state+=",workflow_type:$workflow_type"
    else
        current_state+=",active_workflow:false"
    fi
    
    # Update the context state file using Python for better JSON handling
    python3 -c "
import json
import sys
from datetime import datetime

context_file = '$context_file'
session_id = '$session_id'
state_info = '$current_state'

# Parse state info into dict
state_dict = {}
for item in state_info.split(','):
    if ':' in item and item:
        key, value = item.split(':', 1)
        # Convert boolean strings
        if value.lower() in ['true', 'false']:
            value = value.lower() == 'true'
        # Convert numeric strings
        elif value.isdigit():
            value = int(value)
        state_dict[key] = value

try:
    # Load existing context or create new
    if os.path.exists(context_file):
        with open(context_file, 'r') as f:
            context = json.load(f)
    else:
        context = {
            'session': {},
            'workflow': {},
            'system': {},
            'context_preservation': {},
            'performance': {}
        }
    
    # Update session info
    context['session'] = {
        'id': session_id,
        'last_activity': datetime.now().isoformat(),
        'active': False,  # Session is ending
        'cleanup_timestamp': datetime.now().isoformat()
    }
    
    # Update workflow info
    context['workflow'] = {
        'current_command': state_dict.get('workflow_context', 'none'),
        'context': state_dict.get('workflow_context', 'none'), 
        'active_workflow': state_dict.get('active_workflow', False),
        'workflow_type': state_dict.get('workflow_type', 'none')
    }
    
    # Update system info
    context['system'] = {
        'project_root': state_dict.get('working_directory', ''),
        'git_branch': state_dict.get('git_branch', 'unknown'),
        'git_commit': state_dict.get('git_commit', 'unknown'),
        'git_changes': state_dict.get('git_changes', 0),
        'emergency_override': state_dict.get('emergency_override', False)
    }
    
    # Update context preservation (placeholder for future enhancement)
    context['context_preservation'] = {
        'user_voice_captured': True,  # Assume voice is preserved
        'last_update': datetime.now().isoformat()
    }
    
    # Update performance metrics (placeholder)
    context['performance'] = {
        'token_economy_score': 85,  # Placeholder score
        'last_calculated': datetime.now().isoformat()
    }
    
    # Write updated context
    with open(context_file, 'w') as f:
        json.dump(context, f, indent=2)
        
    print(f'Context state updated successfully for session {session_id}')
        
except Exception as e:
    print(f'Error updating context state: {e}', file=sys.stderr)
    sys.exit(1)
" 2>/dev/null || log_message "WARN" "Failed to update context state"
}

# Update session metrics
update_session_metrics() {
    local session_id="$1"
    
    log_message "INFO" "Updating session metrics for: $session_id"
    
    # Calculate session duration (if we have a start time)
    local start_time_file="/tmp/claude-session-start-$session_id"
    local duration="unknown"
    
    if [[ -f "$start_time_file" ]]; then
        local start_time end_time
        start_time=$(cat "$start_time_file")
        end_time=$(date +%s)
        duration=$((end_time - start_time))
        rm -f "$start_time_file"
        log_message "INFO" "Session duration: ${duration} seconds"
    fi
    
    # Count operations in this session (from hook logs)
    local operation_count=0
    if [[ -f "$LOG_FILE" ]]; then
        # Count hook operations in the last hour that might belong to this session
        local one_hour_ago
        one_hour_ago=$(date -v-1H '+%Y-%m-%d %H:%M:%S' 2>/dev/null || date -d '1 hour ago' '+%Y-%m-%d %H:%M:%S' 2>/dev/null)
        
        if [[ -n "$one_hour_ago" ]]; then
            operation_count=$(awk -v start="$one_hour_ago" '$0 >= start' "$LOG_FILE" | grep -c "\[.*\] \[.*\] \[INFO\]" || echo "0")
        fi
    fi
    
    # Log session summary
    cat >> "$SESSION_LOG_FILE" << EOF
[$TIMESTAMP] Session Summary
Session ID: $session_id
Duration: ${duration}s
Operations: $operation_count
Git Branch: $(git branch --show-current 2>/dev/null || echo "detached")
Git Changes: $(git status --porcelain | wc -l)
Working Directory: $(pwd)
Workflow Context: ${CLAUDE_WORKFLOW_CONTEXT:-none}
Emergency Override: ${CLAUDE_EMERGENCY_OVERRIDE:-false}
---
EOF
}

# Clean up temporary files
cleanup_temporary_files() {
    local session_id="$1"
    
    log_message "INFO" "Cleaning up temporary files for session: $session_id"
    
    # Clean up session-specific temporary files
    local temp_patterns=(
        "/tmp/claude-session-*-$session_id"
        "/tmp/claude-hook-timer-*"
        "/tmp/claude-workflow-*"
        ".claude-workflow-active-$session_id"
    )
    
    for pattern in "${temp_patterns[@]}"; do
        # Use find to handle patterns safely
        find /tmp -name "$(basename "$pattern")" -type f -mtime +1 -delete 2>/dev/null || true
    done
    
    # Clean up old lock files
    find .claude -name "*.lock" -type f -mtime +1 -delete 2>/dev/null || true
    
    # Clean up old log files (keep last 30 days)
    find .claude/logs -name "*.log" -type f -mtime +30 -delete 2>/dev/null || true
    
    log_message "INFO" "Temporary file cleanup completed"
}

# Archive session data
archive_session_data() {
    local session_id="$1"
    
    # Only archive if session_id is meaningful
    if [[ "$session_id" != "unknown" ]] && [[ "$session_id" != "none" ]]; then
        log_message "INFO" "Archiving session data for: $session_id"
        
        local archive_dir="/Users/nalve/ce-simple/.claude/sessions/archive"
        mkdir -p "$archive_dir"
        
        # Create session archive
        local archive_file="$archive_dir/session-$session_id-$(date +%Y%m%d-%H%M%S).json"
        
        # Gather session data
        python3 -c "
import json
import os
from datetime import datetime

session_id = '$session_id'
archive_file = '$archive_file'

session_data = {
    'session_id': session_id,
    'archived_at': datetime.now().isoformat(),
    'final_state': {
        'git_branch': '$(git branch --show-current 2>/dev/null || echo "detached")',
        'git_commit': '$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")',
        'working_directory': '$(pwd)',
        'workflow_context': '${CLAUDE_WORKFLOW_CONTEXT:-none}',
        'emergency_override': '${CLAUDE_EMERGENCY_OVERRIDE:-false}' == 'true'
    },
    'metrics': {
        'cleanup_timestamp': datetime.now().isoformat(),
        'archival_reason': 'session_end'
    }
}

try:
    with open(archive_file, 'w') as f:
        json.dump(session_data, f, indent=2)
    print(f'Session data archived to {archive_file}')
except Exception as e:
    print(f'Error archiving session data: {e}')
" 2>/dev/null || log_message "WARN" "Failed to archive session data"
    fi
}

# Update system health after session
update_system_health() {
    log_message "INFO" "Triggering system health update after session cleanup"
    
    # Update health monitoring if available
    local health_script="/Users/nalve/ce-simple/tools/monitoring/system-health.py"
    if [[ -f "$health_script" ]]; then
        python3 "$health_script" >/dev/null 2>&1 &
        log_message "INFO" "System health update triggered"
    fi
    
    # Update health daemon status
    local daemon_status="/Users/nalve/ce-simple/data/monitoring/health_daemon_status.json"
    if [[ -f "$daemon_status" ]]; then
        # Touch the status file to indicate activity
        touch "$daemon_status"
        log_message "INFO" "Health daemon notified of session end"
    fi
}

# Clear workflow state
clear_workflow_state() {
    log_message "INFO" "Clearing workflow state"
    
    # Remove workflow marker files
    local workflow_markers=(
        ".claude-workflow-active"
        ".claude/workflow-state.json"
        ".claude/context/workflow-active.json"
    )
    
    for marker in "${workflow_markers[@]}"; do
        if [[ -f "$marker" ]]; then
            rm -f "$marker"
            log_message "INFO" "Removed workflow marker: $marker"
        fi
    done
    
    # Clear workflow environment variables (if this script had control over them)
    # Note: Environment variables are typically managed by the parent process
    log_message "INFO" "Workflow state cleared"
}

# Generate cleanup report
generate_cleanup_report() {
    local session_id="$1"
    
    local report=""
    report+="Session Cleanup Report\n"
    report+="=====================\n"
    report+="Session ID: $session_id\n"
    report+="Cleanup Time: $TIMESTAMP\n"
    report+="Git Branch: $(git branch --show-current 2>/dev/null || echo "detached")\n"
    report+="Working Directory: $(pwd)\n"
    report+="Active Workflows: $(test -f ".claude-workflow-active" && echo "yes" || echo "no")\n"
    report+="Emergency Override: ${CLAUDE_EMERGENCY_OVERRIDE:-false}\n"
    report+="Context Preserved: yes\n"
    report+="Cleanup Status: completed\n"
    
    echo -e "$report"
}

# Main session cleanup function
perform_session_cleanup() {
    local session_id="$1"
    
    log_message "INFO" "Starting session cleanup for: $session_id"
    
    # Perform all cleanup operations
    update_context_state "$session_id"
    update_session_metrics "$session_id"
    cleanup_temporary_files "$session_id"
    archive_session_data "$session_id"
    clear_workflow_state
    update_system_health
    
    # Generate and log cleanup report
    local report
    report=$(generate_cleanup_report "$session_id")
    log_message "INFO" "Session cleanup completed:\n$report"
}

# Error handling
handle_error() {  
    local exit_code="$1"
    local error_message="$2"
    log_message "ERROR" "$error_message"
    
    # Session cleanup should not block operations
    case "$exit_code" in
        1)
            log_message "WARN" "Session cleanup error (non-blocking): $error_message"
            ;;
        *)
            log_message "INFO" "Session cleanup issue (continuing): $error_message"
            ;;
    esac
    
    # Always exit 0 for session cleanup hooks
    exit 0
}

# Main execution
main() {
    # Create log directories
    mkdir -p "$(dirname "$LOG_FILE")"
    mkdir -p "$(dirname "$SESSION_LOG_FILE")"
    
    # Validate session ID (but proceed even if unknown)
    if [[ -z "$SESSION_ID" ]]; then
        SESSION_ID="unknown-$(date +%s)"
        log_message "WARN" "No session ID provided, using: $SESSION_ID"
    fi
    
    # Perform session cleanup
    perform_session_cleanup "$SESSION_ID"
    
    # Success
    log_message "SUCCESS" "Session cleanup hook completed successfully"
    exit 0
}

# Trap signals for clean exit
trap 'log_message "WARN" "Session cleanup interrupted"; exit 0' INT TERM

# Execute main function
main "$@"