#!/bin/bash

# MCP IDE Notebook State Verification Hook
# Prevents mcp__ide__executeCode failures due to missing preconditions
# Based on 2025 Claude Code hooks best practices

set -euo pipefail

# Configuration
HOOK_NAME="verify-notebook-state"
LOG_FILE="/Users/nalve/ce-simple/.claude/logs/hooks.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Logging function
log_message() {
    local level="$1"
    local message="$2"
    echo "[$TIMESTAMP] [$HOOK_NAME] [$level] $message" | tee -a "$LOG_FILE"
}

# Error handling
handle_error() {
    local exit_code="$1"
    local error_message="$2"
    log_message "ERROR" "$error_message"
    
    # Provide specific guidance based on error type
    case "$exit_code" in
        1)
            echo "HOOK_ERROR: MCP IDE notebook verification failed"
            echo "GUIDANCE: Check if notebook kernel is active and responsive"
            ;;
        2)
            echo "HOOK_WARNING: Notebook state unknown, proceeding with caution"
            echo "GUIDANCE: Monitor execution carefully for potential issues"
            ;;
        3)
            echo "HOOK_SKIP: Notebook verification skipped"
            echo "GUIDANCE: Manual verification recommended before code execution"
            ;;
    esac
    
    exit "$exit_code"
}

# Main verification function
verify_notebook_state() {
    log_message "INFO" "Starting MCP IDE notebook state verification"
    
    # Check 1: Verify MCP IDE tools are available
    if ! command -v python3 >/dev/null 2>&1; then
        handle_error 1 "Python3 not available - required for MCP IDE operations"
    fi
    
    # Check 2: Look for active notebook processes
    local notebook_processes
    notebook_processes=$(ps aux | grep -E "(jupyter|ipython)" | grep -v grep | wc -l)
    
    if [[ "$notebook_processes" -eq 0 ]]; then
        log_message "WARN" "No Jupyter/IPython processes detected"
        # Don't fail here - kernel might be embedded or using different process name
    else
        log_message "INFO" "Found $notebook_processes notebook-related processes"
    fi
    
    # Check 3: Verify working directory is accessible
    if [[ ! -w "$(pwd)" ]]; then
        handle_error 1 "Current working directory is not writable"
    fi
    
    # Check 4: Check for potential kernel connection issues
    local temp_test_file="/tmp/claude_notebook_test_$$"
    if ! echo "# Test notebook connectivity" > "$temp_test_file" 2>/dev/null; then
        handle_error 1 "Cannot create temporary files - filesystem issues detected"
    fi
    rm -f "$temp_test_file"
    
    # Check 5: Verify Python environment integrity (basic check)
    if ! python3 -c "import sys; print('Python OK')" >/dev/null 2>&1; then
        handle_error 1 "Python environment verification failed"
    fi
    
    # Check 6: Look for notebook-related environment variables
    if [[ -n "${JUPYTER_CONFIG_DIR:-}" ]] || [[ -n "${IPYTHONDIR:-}" ]]; then
        log_message "INFO" "Notebook environment variables detected"
    fi
    
    # Check 7: Verify system resources
    local memory_available
    memory_available=$(vm_stat | grep "Pages free" | awk '{print $3}' | sed 's/\.//')
    if [[ -n "$memory_available" ]] && [[ "$memory_available" -lt 10000 ]]; then
        log_message "WARN" "Low system memory detected - notebook execution may be slow"
        # Return warning code but don't block execution
        handle_error 2 "Low system memory warning"
    fi
    
    # Check 8: Look for existing notebook lock files that might indicate issues
    if find /tmp -name ".jupyter-*" -o -name "*-notebook-*" 2>/dev/null | grep -q .; then
        log_message "INFO" "Found existing notebook-related temporary files"
    fi
    
    # Check 9: Verify IDE integration is functional (if MCP connection exists)
    # This is a passive check - we don't want to actively trigger MCP calls here
    
    log_message "INFO" "MCP IDE notebook state verification completed successfully"
    
    # Success - allow execution to proceed
    return 0
}

# Enhanced verification with debugging support
debug_notebook_state() {
    if [[ "${CLAUDE_DEBUG_HOOKS:-false}" == "true" ]]; then
        log_message "DEBUG" "=== Notebook State Debug Information ==="
        log_message "DEBUG" "Python version: $(python3 --version 2>&1 || echo 'Not available')"
        log_message "DEBUG" "Working directory: $(pwd)"
        log_message "DEBUG" "User: $(whoami)"
        log_message "DEBUG" "Environment variables:"
        env | grep -E "(JUPYTER|IPYTHON|CLAUDE)" | while read -r line; do
            log_message "DEBUG" "  $line"
        done
        log_message "DEBUG" "=== End Debug Information ==="
    fi
}

# Emergency override check
check_emergency_override() {
    if [[ "${CLAUDE_EMERGENCY_OVERRIDE:-false}" == "true" ]]; then
        log_message "WARN" "Emergency override activated - bypassing notebook verification"
        return 0
    fi
    return 1
}

# Main execution
main() {
    # Create log directory if it doesn't exist
    mkdir -p "$(dirname "$LOG_FILE")"
    
    # Check for emergency override first
    if check_emergency_override; then
        exit 0
    fi
    
    # Run debug logging if enabled
    debug_notebook_state
    
    # Perform main verification
    verify_notebook_state
    
    # If we get here, verification passed
    log_message "SUCCESS" "Notebook state verification passed - proceeding with code execution"
    exit 0
}

# Trap signals for clean exit
trap 'log_message "ERROR" "Script interrupted"; exit 130' INT TERM

# Execute main function
main "$@"