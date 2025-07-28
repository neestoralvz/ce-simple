#!/bin/bash

# Process Notification Hook
# Handles Claude Code notifications and triggers appropriate responses
# Based on 2025 Claude Code hooks best practices

set -euo pipefail

# Configuration
HOOK_NAME="process-notification"
LOG_FILE="/Users/nalve/ce-simple/.claude/logs/hooks.log"
NOTIFICATION_LOG_FILE="/Users/nalve/ce-simple/.claude/logs/notifications.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Parameters
NOTIFICATION_TYPE="$1"  
NOTIFICATION_MESSAGE="$2"

# Logging function
log_message() {
    local level="$1"
    local message="$2"
    echo "[$TIMESTAMP] [$HOOK_NAME] [$level] $message" | tee -a "$LOG_FILE"
}

# Categorize notification type
categorize_notification() {
    local type="$1"
    local message="$2"
    
    case "$type" in
        "error"|"ERROR")
            echo "system_error"
            ;;
        "warning"|"WARNING"|"warn"|"WARN")
            echo "system_warning"
            ;;
        "info"|"INFO"|"information")
            echo "system_info"
            ;;
        "alert"|"ALERT")
            echo "system_alert"
            ;;
        "success"|"SUCCESS")
            echo "system_success"
            ;;
        *)
            # Analyze message content for categorization
            if echo "$message" | grep -qi "error\|failed\|exception\|crash"; then
                echo "content_error"
            elif echo "$message" | grep -qi "warning\|caution\|deprecated"; then
                echo "content_warning"
            elif echo "$message" | grep -qi "complete\|success\|finished\|done"; then
                echo "content_success"
            else
                echo "general"
            fi
            ;;
    esac
}

# Determine notification priority
determine_priority() {
    local category="$1"
    local message="$2"
    
    case "$category" in
        "system_error"|"content_error")
            echo "high"
            ;;
        "system_alert")
            echo "critical"
            ;;
        "system_warning"|"content_warning")
            echo "medium"
            ;;
        "system_success"|"content_success")
            echo "low"
            ;;
        "system_info")
            echo "low"
            ;;
        *)
            # Analyze message for priority indicators
            if echo "$message" | grep -qi "critical\|urgent\|immediate"; then
                echo "critical"
            elif echo "$message" | grep -qi "important\|significant"; then
                echo "high"
            else
                echo "medium"
            fi
            ;;
    esac
}

# Extract context information
extract_notification_context() {
    local context_info=""
    
    # Current session information
    context_info+=",session_id:${CLAUDE_SESSION_ID:-none}"
    context_info+=",workflow_context:${CLAUDE_WORKFLOW_CONTEXT:-none}"
    
    # System state
    if git rev-parse --git-dir >/dev/null 2>&1; then
        local branch
        branch=$(git branch --show-current 2>/dev/null || echo "detached")
        context_info+=",git_branch:$branch"
    fi
    
    # Active workflows
    if [[ -f ".claude-workflow-active" ]]; then
        context_info+=",active_workflow:true"
    else
        context_info+=",active_workflow:false"
    fi
    
    # System load
    local load_avg
    load_avg=$(uptime | awk -F'load average:' '{print $2}' | awk -F',' '{print $1}' | tr -d ' ')
    context_info+=",system_load:$load_avg"
    
    echo "$context_info"
}

# Process error notifications  
process_error_notification() {
    local message="$1"
    
    log_message "ERROR" "Processing error notification: $message"
    
    # Create error alert
    local alert_file="/Users/nalve/ce-simple/.claude/logs/alerts/error-$(date +%Y%m%d-%H%M%S).alert"
    mkdir -p "$(dirname "$alert_file")"
    
    cat > "$alert_file" << EOF
Alert Type: System Error
Message: $message
Timestamp: $TIMESTAMP
Priority: High
Source: Claude Code Notification
Context: $(extract_notification_context)
Requires Investigation: Yes
EOF
    
    # Check for specific error patterns that need immediate attention
    if echo "$message" | grep -qi "filesystem\|permission\|disk"; then
        log_message "CRITICAL" "Filesystem-related error detected - may require immediate attention"
        
        # Check disk space
        local disk_usage
        disk_usage=$(df -h . | tail -1 | awk '{print $5}' | tr -d '%')
        if [[ "$disk_usage" -gt 90 ]]; then
            log_message "CRITICAL" "Disk usage critical: ${disk_usage}%"
        fi
    fi
    
    if echo "$message" | grep -qi "git\|repository"; then
        log_message "WARN" "Git-related error detected - checking repository health"
        
        # Quick git health check
        if ! git fsck --no-progress >/dev/null 2>&1; then
            log_message "CRITICAL" "Git repository corruption detected"
        fi
    fi
}

# Process warning notifications
process_warning_notification() {
    local message="$1"
    
    log_message "WARN" "Processing warning notification: $message"
    
    # Log warning with context
    cat >> "$NOTIFICATION_LOG_FILE" << EOF
[$TIMESTAMP] WARNING: $message
Context: $(extract_notification_context)
---
EOF
    
    # Check for patterns that might indicate upcoming issues
    if echo "$message" | grep -qi "memory\|resource\|performance"; then
        log_message "INFO" "Resource-related warning - monitoring system health"
        
        # Basic resource check
        local memory_usage
        memory_usage=$(free 2>/dev/null | grep '^Mem:' | awk '{print int($3/$2 * 100)}' || echo "unknown")
        if [[ "$memory_usage" != "unknown" ]] && [[ "$memory_usage" -gt 80 ]]; then
            log_message "WARN" "High memory usage detected: ${memory_usage}%"
        fi
    fi
}

# Process success notifications
process_success_notification() {
    local message="$1"
    
    log_message "SUCCESS" "Processing success notification: $message"
    
    # Log success for tracking
    cat >> "$NOTIFICATION_LOG_FILE" << EOF
[$TIMESTAMP] SUCCESS: $message
Context: $(extract_notification_context)
---
EOF
    
    # Check for completion of critical operations
    if echo "$message" | grep -qi "commit\|push\|deploy"; then
        log_message "INFO" "Critical operation completed successfully: $message"
    fi
}

# Process info notifications
process_info_notification() {
    local message="$1"
    
    log_message "INFO" "Processing info notification: $message"
    
    # Simple logging for informational messages
    cat >> "$NOTIFICATION_LOG_FILE" << EOF
[$TIMESTAMP] INFO: $message
---
EOF
}

# Trigger system health update
trigger_health_update() {
    local priority="$1"
    
    # For high priority notifications, trigger immediate health check
    if [[ "$priority" == "critical" ]] || [[ "$priority" == "high" ]]; then
        log_message "INFO" "Triggering system health update due to high priority notification"
        
        # Update health daemon if it exists
        if [[ -f "/Users/nalve/ce-simple/data/monitoring/health_daemon_status.json" ]]; then
            # Touch the health monitoring script to trigger immediate check
            if [[ -f "/Users/nalve/ce-simple/tools/monitoring/system-health.py" ]]; then
                python3 "/Users/nalve/ce-simple/tools/monitoring/system-health.py" >/dev/null 2>&1 &
            fi
        fi
    fi
}

# Generate notification summary
generate_notification_summary() {
    local type="$1"
    local category="$2"
    local priority="$3"
    local message="$4"
    
    local summary="Type: $type | Category: $category | Priority: $priority"
    summary+="\nMessage: $message"
    summary+="\nTimestamp: $TIMESTAMP"
    summary+="\nContext: $(extract_notification_context)"
    
    echo -e "$summary"
}

# Update notification statistics
update_notification_stats() {
    local category="$1"
    local priority="$2"
    local stats_file="/Users/nalve/ce-simple/.claude/logs/notification-statistics.json"
    
    # Create stats file if it doesn't exist
    if [[ ! -f "$stats_file" ]]; then
        cat > "$stats_file" << 'EOF'
{
    "last_updated": "",
    "total_notifications": 0,
    "categories": {},
    "priorities": {
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0
    },
    "recent_trends": []
}
EOF
    fi
    
    # Update statistics using Python
    python3 -c "
import json
import sys
from datetime import datetime

stats_file = '$stats_file'
category = '$category'
priority = '$priority'

try:
    with open(stats_file, 'r') as f:
        stats = json.load(f)
    
    # Update general stats
    stats['last_updated'] = datetime.now().isoformat()
    stats['total_notifications'] += 1
    
    # Update category stats
    if category not in stats['categories']:
        stats['categories'][category] = 0
    stats['categories'][category] += 1
    
    # Update priority stats
    if priority in stats['priorities']:
        stats['priorities'][priority] += 1
    
    # Add to recent trends (keep last 100)
    trend_entry = {
        'timestamp': datetime.now().isoformat(),
        'category': category,
        'priority': priority
    }
    stats['recent_trends'].append(trend_entry)
    if len(stats['recent_trends']) > 100:
        stats['recent_trends'] = stats['recent_trends'][-100:]
    
    # Write updated stats
    with open(stats_file, 'w') as f:
        json.dump(stats, f, indent=2)
        
except Exception as e:
    print(f'Error updating notification statistics: {e}', file=sys.stderr)
" 2>/dev/null || log_message "WARN" "Failed to update notification statistics"
}

# Main notification processing function
process_notification() {
    log_message "INFO" "Processing Claude Code notification"
    
    # Categorize and prioritize the notification
    local category
    category=$(categorize_notification "$NOTIFICATION_TYPE" "$NOTIFICATION_MESSAGE")
    
    local priority
    priority=$(determine_priority "$category" "$NOTIFICATION_MESSAGE")
    
    log_message "INFO" "Notification categorized as: $category (priority: $priority)"
    
    # Process based on category
    case "$category" in
        "system_error"|"content_error")
            process_error_notification "$NOTIFICATION_MESSAGE"
            ;;
        "system_warning"|"content_warning")
            process_warning_notification "$NOTIFICATION_MESSAGE"
            ;;
        "system_success"|"content_success")
            process_success_notification "$NOTIFICATION_MESSAGE"
            ;;
        "system_info"|"general")
            process_info_notification "$NOTIFICATION_MESSAGE"
            ;;
        "system_alert")
            # Treat alerts as errors for processing
            process_error_notification "$NOTIFICATION_MESSAGE"
            ;;
        *)
            log_message "WARN" "Unknown notification category: $category"
            process_info_notification "$NOTIFICATION_MESSAGE"
            ;;
    esac
    
    # Update statistics and trigger health checks
    update_notification_stats "$category" "$priority"
    trigger_health_update "$priority"
    
    # Generate summary for logging
    local summary
    summary=$(generate_notification_summary "$NOTIFICATION_TYPE" "$category" "$priority" "$NOTIFICATION_MESSAGE")
    log_message "INFO" "Notification processing completed:\n$summary"
}

# Error handling
handle_error() {
    local exit_code="$1"
    local error_message="$2"
    log_message "ERROR" "$error_message"
    
    # Notification hooks should not block operations
    case "$exit_code" in
        1)
            log_message "WARN" "Notification processing error (non-blocking): $error_message"
            ;;
        *)
            log_message "INFO" "Notification processing issue (continuing): $error_message"
            ;;
    esac
    
    # Always exit 0 for notification hooks
    exit 0
}

# Main execution
main() {
    # Create log directories
    mkdir -p "$(dirname "$LOG_FILE")"
    mkdir -p "$(dirname "$NOTIFICATION_LOG_FILE")"
    
    # Validate input
    if [[ -z "$NOTIFICATION_TYPE" ]] || [[ -z "$NOTIFICATION_MESSAGE" ]]; then
        handle_error 1 "Missing notification type or message"
    fi
    
    # Process the notification
    process_notification
    
    # Success
    log_message "SUCCESS" "Notification processing hook completed successfully"
    exit 0
}

# Trap signals for clean exit
trap 'log_message "WARN" "Notification processing interrupted"; exit 0' INT TERM

# Execute main function
main "$@"