#!/bin/bash

# Emergency Override Hook
# Allows bypassing normal verification in critical situations
# Based on 2025 Claude Code hooks best practices

set -euo pipefail

# Configuration
HOOK_NAME="emergency-override"
LOG_FILE="/Users/nalve/ce-simple/.claude/logs/hooks.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Parameters
TOOL_NAME="$1"
TOOL_INPUT="$2"

# Logging function
log_message() {
    local level="$1"
    local message="$2"
    echo "[$TIMESTAMP] [$HOOK_NAME] [$level] $message" | tee -a "$LOG_FILE"
}

# Main execution
main() {
    # Create log directory
    mkdir -p "$(dirname "$LOG_FILE")"
    
    # Check if emergency override is actually enabled
    if [[ "${CLAUDE_EMERGENCY_OVERRIDE:-false}" != "true" ]]; then
        # Not in emergency mode - this hook should not be active
        exit 0
    fi
    
    log_message "WARN" "EMERGENCY OVERRIDE ACTIVE for tool: $TOOL_NAME"
    log_message "WARN" "Tool input: $TOOL_INPUT"
    log_message "WARN" "All normal verification bypassed"
    
    # Allow operation to proceed
    exit 0
}

main "$@"