#!/bin/bash

# Start Performance Timer Hook  
# Initiates performance timing for expensive operations
# Based on 2025 Claude Code hooks best practices

set -euo pipefail

# Configuration
HOOK_NAME="start-performance-timer"
LOG_FILE="/Users/nalve/ce-simple/.claude/logs/hooks.log"
PERFORMANCE_LOG_FILE="/Users/nalve/ce-simple/.claude/logs/performance.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Parameters
TOOL_NAME="$1"

# Logging function
log_message() {
    local level="$1"
    local message="$2"
    echo "[$TIMESTAMP] [$HOOK_NAME] [$level] $message" | tee -a "$LOG_FILE"
}

# Get high precision timestamp
get_precision_timestamp() {
    # Use Python for high precision timing
    python3 -c "import time; print(f'{time.time():.6f}')" 2>/dev/null || date +%s
}

# Create timer data structure
create_timer_data() {
    local tool_name="$1"
    local start_timestamp="$2"
    local timer_id="$3"
    
    # Gather system context
    local system_load memory_usage disk_usage
    system_load=$(uptime | awk -F'load average:' '{print $2}' | awk -F',' '{print $1}' | tr -d ' ')
    memory_usage=$(free 2>/dev/null | grep '^Mem:' | awk '{print int($3/$2 * 100)}' || echo "unknown")
    disk_usage=$(df . | tail -1 | awk '{print $5}' | tr -d '%')
    
    # Git context
    local git_branch git_changes
    if git rev-parse --git-dir >/dev/null 2>&1; then
        git_branch=$(git branch --show-current 2>/dev/null || echo "detached")
        git_changes=$(git status --porcelain | wc -l)
    else
        git_branch="none"
        git_changes=0
    fi
    
    # Create timer data in JSON format
    python3 -c "
import json
import os
from datetime import datetime

timer_data = {
    'timer_id': '$timer_id',
    'tool_name': '$tool_name',
    'start_timestamp': float('$start_timestamp'),
    'start_time_human': datetime.fromtimestamp(float('$start_timestamp')).isoformat(),
    'session_id': '${CLAUDE_SESSION_ID:-unknown}',
    'workflow_context': '${CLAUDE_WORKFLOW_CONTEXT:-none}',
    'system_context': {
        'working_directory': '$(pwd)',
        'git_branch': '$git_branch',
        'git_changes': int('$git_changes'),
        'system_load': '$system_load',
        'memory_usage': '$memory_usage',
        'disk_usage': int('$disk_usage'),
        'process_id': os.getpid(),
        'parent_process_id': os.getppid()
    },
    'tool_context': {
        'tool_category': '$(categorize_tool "$tool_name")',
        'expected_duration': '$(estimate_duration "$tool_name")',
        'performance_critical': $(is_performance_critical "$tool_name" && echo 'true' || echo 'false')
    }
}

# Write timer data to file
timer_file = '/tmp/claude-performance-timer-$timer_id.json'
with open(timer_file, 'w') as f:
    json.dump(timer_data, f, indent=2)

print(f'Timer data created: {timer_file}')
"
}

# Categorize tool for performance analysis
categorize_tool() {
    local tool_name="$1"
    
    case "$tool_name" in
        "WebSearch")
            echo "network_operation"
            ;;
        "mcp__"*)
            echo "mcp_operation"
            ;;
        "Bash")
            echo "system_operation"
            ;;
        "Read"|"Write"|"Edit"|"MultiEdit")
            echo "file_operation"
            ;;
        "Glob"|"Grep")
            echo "search_operation"
            ;;
        *)
            echo "general_operation"
            ;;
    esac
}

# Estimate expected duration for different tools
estimate_duration() {
    local tool_name="$1"
    
    case "$tool_name" in
        "WebSearch")
            echo "2-5 seconds"
            ;;
        "mcp__ide__executeCode")
            echo "1-3 seconds"
            ;;
        "Bash")
            echo "0.5-2 seconds"
            ;;
        "Read")
            echo "0.1-0.5 seconds"
            ;;
        "Write"|"Edit"|"MultiEdit")
            echo "0.2-1 second"
            ;;
        "Glob"|"Grep")
            echo "0.5-2 seconds"
            ;;
        *)
            echo "1-3 seconds"
            ;;
    esac
}

# Check if tool is performance critical
is_performance_critical() {
    local tool_name="$1"
    
    case "$tool_name" in
        "WebSearch"|"mcp__"*|"Bash")
            return 0  # True - performance critical
            ;;
        *)
            return 1  # False - not performance critical
            ;;
    esac
}

# Generate unique timer ID
generate_timer_id() {
    local tool_name="$1"
    local timestamp="$2"
    
    # Create unique ID from tool name, timestamp, and process ID
    echo "${tool_name}-$(date +%s)-$$" | tr '[:upper:]' '[:lower:]' | tr -d ' ' | tr '_' '-'
}

# Log timer start
log_timer_start() {
    local tool_name="$1"
    local timer_id="$2"
    local start_timestamp="$3"
    
    # Log to performance log file
    cat >> "$PERFORMANCE_LOG_FILE" << EOF
[$TIMESTAMP] TIMER_START
Tool: $tool_name
Timer ID: $timer_id
Start Timestamp: $start_timestamp
Session: ${CLAUDE_SESSION_ID:-unknown}
Context: ${CLAUDE_WORKFLOW_CONTEXT:-none}
Expected Duration: $(estimate_duration "$tool_name")
Performance Critical: $(is_performance_critical "$tool_name" && echo "yes" || echo "no")
---
EOF
}

# Check for existing timers
check_existing_timers() {
    local tool_name="$1"
    
    # Check for orphaned timer files (older than 1 hour)
    local orphaned_count
    orphaned_count=$(find /tmp -name "claude-performance-timer-*.json" -type f -mmin +60 2>/dev/null | wc -l)
    
    if [[ "$orphaned_count" -gt 0 ]]; then
        log_message "WARN" "Found $orphaned_count orphaned timer files - cleaning up"
        find /tmp -name "claude-performance-timer-*.json" -type f -mmin +60 -delete 2>/dev/null
    fi
    
    # Check for concurrent timers for the same tool
    local concurrent_count
    concurrent_count=$(find /tmp -name "claude-performance-timer-${tool_name,,}-*.json" -type f 2>/dev/null | wc -l)
    
    if [[ "$concurrent_count" -gt 0 ]]; then
        log_message "INFO" "Found $concurrent_count existing timers for $tool_name"
    fi
}

# Set performance monitoring environment
setup_performance_environment() {
    local timer_id="$1"
    
    # Export timer ID for use by end-timer hook
    export CLAUDE_PERFORMANCE_TIMER_ID="$timer_id"
    
    # Create performance monitoring directory
    mkdir -p "/Users/nalve/ce-simple/.claude/logs/performance"
    
    # Set high-resolution timer flag
    export CLAUDE_HIGH_PRECISION_TIMING="true"
    
    log_message "INFO" "Performance monitoring environment configured"
}

# Initialize performance baseline
capture_performance_baseline() {
    local timer_id="$1"
    local baseline_file="/tmp/claude-performance-baseline-$timer_id.json"
    
    # Capture system performance baseline
    python3 -c "
import json
import psutil
import time
from datetime import datetime

try:
    baseline = {
        'timestamp': time.time(),
        'cpu_percent': psutil.cpu_percent(interval=0.1),
        'memory_percent': psutil.virtual_memory().percent,
        'disk_io': dict(psutil.disk_io_counters()._asdict()) if psutil.disk_io_counters() else {},
        'network_io': dict(psutil.net_io_counters()._asdict()) if psutil.net_io_counters() else {},
        'process_count': len(psutil.pids()),
        'load_average': psutil.getloadavg() if hasattr(psutil, 'getloadavg') else [0, 0, 0]
    }
    
    with open('$baseline_file', 'w') as f:
        json.dump(baseline, f, indent=2)
        
    print('Performance baseline captured')
    
except ImportError:
    # Fallback if psutil is not available
    baseline = {
        'timestamp': time.time(),
        'fallback': True,
        'message': 'psutil not available - using basic metrics'
    }
    
    with open('$baseline_file', 'w') as f:
        json.dump(baseline, f, indent=2)
        
    print('Basic performance baseline captured')
    
except Exception as e:
    print(f'Error capturing baseline: {e}')
" 2>/dev/null || log_message "WARN" "Failed to capture performance baseline"
}

# Main performance timer start function
start_performance_timer() {
    local tool_name="$1"
    
    log_message "INFO" "Starting performance timer for: $tool_name"
    
    # Get high precision start timestamp
    local start_timestamp
    start_timestamp=$(get_precision_timestamp)
    
    # Generate unique timer ID
    local timer_id
    timer_id=$(generate_timer_id "$tool_name" "$start_timestamp")
    
    log_message "INFO" "Generated timer ID: $timer_id"
    
    # Check for existing timers and cleanup
    check_existing_timers "$tool_name"
    
    # Create timer data structure
    create_timer_data "$tool_name" "$start_timestamp" "$timer_id"
    
    # Log timer start
    log_timer_start "$tool_name" "$timer_id" "$start_timestamp"
    
    # Setup performance monitoring environment
    setup_performance_environment "$timer_id"
    
    # Capture performance baseline
    capture_performance_baseline "$timer_id"
    
    log_message "SUCCESS" "Performance timer started successfully: $timer_id"
}

# Error handling
handle_error() {
    local exit_code="$1"
    local error_message="$2"
    log_message "ERROR" "$error_message"
    
    # Performance timer should not block operations
    case "$exit_code" in
        1)
            log_message "WARN" "Performance timer error (non-blocking): $error_message"
            ;;
        *)
            log_message "INFO" "Performance timer issue (continuing): $error_message"
            ;;
    esac
    
    # Always exit 0 for performance hooks
    exit 0
}

# Main execution
main() {
    # Create log directories
    mkdir -p "$(dirname "$LOG_FILE")"
    mkdir -p "$(dirname "$PERFORMANCE_LOG_FILE")"
    
    # Validate input
    if [[ -z "$TOOL_NAME" ]]; then
        handle_error 1 "No tool name provided for performance timing"
    fi
    
    # Only start timer for performance-critical tools by default
    # But allow all tools if explicit performance monitoring is enabled
    if is_performance_critical "$TOOL_NAME" || [[ "${CLAUDE_PERFORMANCE_MONITORING:-false}" == "true" ]]; then
        start_performance_timer "$TOOL_NAME"
    else
        log_message "INFO" "Tool $TOOL_NAME not flagged as performance-critical, skipping timer"
    fi
    
    # Success
    log_message "SUCCESS" "Performance timer hook completed successfully"
    exit 0
}

# Trap signals for clean exit
trap 'log_message "WARN" "Performance timer interrupted"; exit 0' INT TERM

# Execute main function
main "$@"