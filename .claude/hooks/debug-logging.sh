#!/bin/bash

# Debug Logging Hook
# Provides detailed troubleshooting information for hook system debugging
# Based on 2025 Claude Code hooks best practices

set -euo pipefail

# Configuration
HOOK_NAME="debug-logging"
LOG_FILE="/Users/nalve/ce-simple/.claude/logs/hooks.log"
DEBUG_LOG_FILE="/Users/nalve/ce-simple/.claude/logs/debug-hooks.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Parameters
DEBUG_PHASE="$1"  # 'PRE' or 'POST'
TOOL_NAME="$2"
TOOL_DATA="$3"    # INPUT for PRE, OUTPUT for POST

# Logging function
log_message() {
    local level="$1"
    local message="$2"
    echo "[$TIMESTAMP] [$HOOK_NAME] [$level] $message" | tee -a "$LOG_FILE"
}

# Debug logging function
debug_log() {
    local message="$1"
    echo "[$TIMESTAMP] [DEBUG] [$DEBUG_PHASE] $message" >> "$DEBUG_LOG_FILE"
}

# Check if debug logging is enabled
is_debug_enabled() {
    [[ "${CLAUDE_DEBUG_HOOKS:-false}" == "true" ]]
}

# Log system state information
log_system_state() {
    debug_log "=== SYSTEM STATE DEBUG ==="
    debug_log "Tool: $TOOL_NAME"
    debug_log "Phase: $DEBUG_PHASE"
    debug_log "PID: $$"
    debug_log "Working Directory: $(pwd)"
    debug_log "User: $(whoami)"
    debug_log "Shell: $SHELL"
    debug_log "PATH: $PATH"
    
    # Environment variables
    debug_log "=== CLAUDE ENVIRONMENT ==="
    env | grep -E "^CLAUDE_" | while read -r var; do
        debug_log "  $var"
    done
    
    # Git state if in git repo
    if git rev-parse --git-dir >/dev/null 2>&1; then
        debug_log "=== GIT STATE ==="
        debug_log "  Repository: $(git rev-parse --show-toplevel 2>/dev/null || echo 'N/A')"
        debug_log "  Branch: $(git branch --show-current 2>/dev/null || echo 'detached')"
        debug_log "  Commit: $(git rev-parse --short HEAD 2>/dev/null || echo 'N/A')"
        debug_log "  Status: $(git status --porcelain | wc -l) changes"
    fi
    
    # System resources
    debug_log "=== SYSTEM RESOURCES ==="
    debug_log "  Load Average: $(uptime | awk -F'load average:' '{print $2}')"
    debug_log "  Memory: $(free -h 2>/dev/null | grep '^Mem:' || echo 'N/A')"
    debug_log "  Disk Space: $(df -h . | tail -1 | awk '{print $4 " available"}')"
}

# Log tool-specific information
log_tool_information() {
    debug_log "=== TOOL INFORMATION ==="
    debug_log "Tool Name: $TOOL_NAME"
    debug_log "Execution Phase: $DEBUG_PHASE"
    
    if [[ "$DEBUG_PHASE" == "PRE" ]]; then
        debug_log "Tool Input: $TOOL_DATA"
        
        # Parse tool input if it's JSON
        if echo "$TOOL_DATA" | jq . >/dev/null 2>&1; then
            debug_log "=== PARSED TOOL INPUT ==="
            echo "$TOOL_DATA" | jq -r 'to_entries[] | "  \(.key): \(.value)"' 2>/dev/null | while read -r line; do
                debug_log "$line"
            done
        fi
        
    elif [[ "$DEBUG_PHASE" == "POST" ]]; then
        debug_log "Tool Output Length: ${#TOOL_DATA} characters"
        debug_log "Tool Output Preview: $(echo "$TOOL_DATA" | head -c 200)..."
        
        # Check for common error patterns
        if echo "$TOOL_DATA" | grep -qi "error\|failed\|exception"; then
            debug_log "⚠️  ERROR PATTERNS DETECTED in tool output"
        fi
    fi
}

# Log hook execution chain
log_hook_chain() {
    debug_log "=== HOOK EXECUTION CHAIN ==="
    
    # Find other active hooks
    local active_hooks
    active_hooks=$(ps aux | grep -E "\.claude/hooks" | grep -v grep | head -5)
    if [[ -n "$active_hooks" ]]; then
        debug_log "Active hooks:"
        echo "$active_hooks" | while read -r line; do
            debug_log "  $line"
        done
    else
        debug_log "No other active hooks detected"
    fi
    
    # Check recent hook logs
    if [[ -f "$LOG_FILE" ]]; then
        debug_log "Recent hook executions:"
        tail -5 "$LOG_FILE" | while read -r line; do
            debug_log "  $line"
        done
    fi
}

# Log file system state
log_filesystem_state() {
    if [[ "$TOOL_NAME" =~ ^(Write|Edit|MultiEdit|Read)$ ]]; then
        debug_log "=== FILESYSTEM STATE ==="
        
        # Try to extract file path from tool data
        local file_path=""
        if echo "$TOOL_DATA" | jq -e '.file_path' >/dev/null 2>&1; then
            file_path=$(echo "$TOOL_DATA" | jq -r '.file_path')
        elif [[ "$TOOL_DATA" =~ file_path.*:.*\"([^\"]+)\" ]]; then
            file_path="${BASH_REMATCH[1]}"
        fi
        
        if [[ -n "$file_path" ]]; then
            debug_log "Target File: $file_path"
            debug_log "File Exists: $(test -f "$file_path" && echo "yes" || echo "no")"
            if [[ -f "$file_path" ]]; then
                debug_log "File Size: $(stat -f%z "$file_path" 2>/dev/null || echo "unknown") bytes"
                debug_log "File Permissions: $(ls -la "$file_path" | awk '{print $1, $3, $4}')"
                debug_log "Last Modified: $(stat -f%Sm "$file_path" 2>/dev/null || echo "unknown")"
            fi
            
            # Check parent directory
            local parent_dir
            parent_dir=$(dirname "$file_path")
            debug_log "Parent Directory: $parent_dir"
            debug_log "Parent Exists: $(test -d "$parent_dir" && echo "yes" || echo "no")"
            debug_log "Parent Writable: $(test -w "$parent_dir" && echo "yes" || echo "no")"
        fi
    fi
}

# Log performance metrics
log_performance_metrics() {
    debug_log "=== PERFORMANCE METRICS ==="
    debug_log "Hook Start Time: $TIMESTAMP"
    debug_log "Process ID: $$"
    debug_log "Parent Process: $(ps -o ppid= -p $$ 2>/dev/null || echo "unknown")"
    
    # Execution time tracking
    if [[ "$DEBUG_PHASE" == "PRE" ]]; then
        echo "$TIMESTAMP" > "/tmp/claude-hook-timer-$$"
        debug_log "Timer Started: $TIMESTAMP"
    elif [[ "$DEBUG_PHASE" == "POST" ]] && [[ -f "/tmp/claude-hook-timer-$$" ]]; then
        local start_time
        start_time=$(cat "/tmp/claude-hook-timer-$$")
        local start_epoch end_epoch duration
        start_epoch=$(date -j -f "%Y-%m-%d %H:%M:%S" "$start_time" "+%s" 2>/dev/null || echo "0")
        end_epoch=$(date "+%s")
        duration=$((end_epoch - start_epoch))
        debug_log "Execution Duration: ${duration}s"
        rm -f "/tmp/claude-hook-timer-$$"
    fi
}

# Log context state
log_context_state() {
    debug_log "=== CONTEXT STATE ==="
    
    # Check for context files
    local context_files=(
        ".claude-workflow-active"
        ".claude/context/current-session.json"
        ".claude/context/workflow-state.json"
    )
    
    for context_file in "${context_files[@]}"; do
        if [[ -f "$context_file" ]]; then
            debug_log "Context File: $context_file (exists)"
            if [[ "$context_file" =~ \.json$ ]] && [[ -r "$context_file" ]]; then
                debug_log "  Content: $(cat "$context_file" 2>/dev/null | head -c 200)..."
            fi
        else
            debug_log "Context File: $context_file (missing)"
        fi
    done
    
    # Check workflow context
    debug_log "Workflow Context: ${CLAUDE_WORKFLOW_CONTEXT:-none}"
    debug_log "Emergency Override: ${CLAUDE_EMERGENCY_OVERRIDE:-false}"
    debug_log "Session ID: ${CLAUDE_SESSION_ID:-none}"
}

# Main debug logging function
perform_debug_logging() {
    # Only log if debug is enabled
    if ! is_debug_enabled; then
        return 0
    fi
    
    log_message "INFO" "Debug logging enabled for $TOOL_NAME ($DEBUG_PHASE phase)"
    
    # Create debug log directory
    mkdir -p "$(dirname "$DEBUG_LOG_FILE")"
    
    # Log all debug information
    debug_log ""
    debug_log "=========================================="
    debug_log "DEBUG SESSION START: $TOOL_NAME ($DEBUG_PHASE)"
    debug_log "=========================================="
    
    log_system_state
    log_tool_information
    log_hook_chain
    log_filesystem_state
    log_performance_metrics
    log_context_state
    
    debug_log "=========================================="
    debug_log "DEBUG SESSION END: $TOOL_NAME ($DEBUG_PHASE)"
    debug_log "=========================================="
    debug_log ""
    
    log_message "INFO" "Debug logging completed for $TOOL_NAME ($DEBUG_PHASE phase)"
}

# Error handling
handle_error() {
    local exit_code="$1"
    local error_message="$2"
    log_message "ERROR" "$error_message"
    
    # Debug logging should not block operations
    case "$exit_code" in
        1)
            log_message "WARN" "Debug logging error (non-blocking): $error_message"
            ;;
        *)
            log_message "INFO" "Debug logging issue (continuing): $error_message"
            ;;
    esac
    
    # Always exit 0 for debug hooks to not block operations
    exit 0
}

# Main execution
main() {
    # Create log directory if it doesn't exist
    mkdir -p "$(dirname "$LOG_FILE")"
    
    # Validate input
    if [[ -z "$DEBUG_PHASE" ]] || [[ -z "$TOOL_NAME" ]]; then
        handle_error 1 "Invalid debug logging parameters"
    fi
    
    # Validate debug phase
    if [[ "$DEBUG_PHASE" != "PRE" ]] && [[ "$DEBUG_PHASE" != "POST" ]]; then
        handle_error 1 "Invalid debug phase: $DEBUG_PHASE (must be PRE or POST)"
    fi
    
    # Perform debug logging
    perform_debug_logging
    
    # Success
    log_message "SUCCESS" "Debug logging hook completed successfully"
    exit 0
}

# Trap signals for clean exit
trap 'log_message "WARN" "Debug logging interrupted"; exit 0' INT TERM

# Execute main function
main "$@"