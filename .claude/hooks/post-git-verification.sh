#!/bin/bash

# Post-Git Operation Verification Hook
# Logs git operations and verifies repository state after completion
# Based on 2025 Claude Code hooks best practices

set -euo pipefail

# Configuration
HOOK_NAME="post-git-verification"
LOG_FILE="/Users/nalve/ce-simple/.claude/logs/hooks.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
GIT_LOG_FILE="/Users/nalve/ce-simple/.claude/logs/git-operations.log"

# Parameters
GIT_COMMAND="$1"
TOOL_OUTPUT="$2"

# Logging function
log_message() {
    local level="$1"
    local message="$2"
    echo "[$TIMESTAMP] [$HOOK_NAME] [$level] $message" | tee -a "$LOG_FILE"
}

# Log git operation
log_git_operation() {
    local command="$1"
    local output="$2"
    
    # Create git log entry
    cat >> "$GIT_LOG_FILE" << EOF
[$TIMESTAMP] Git Operation: $command
Output: $output
Repository State After:
  Branch: $(git branch --show-current 2>/dev/null || echo "detached")
  Commit: $(git rev-parse --short HEAD 2>/dev/null || echo "unknown")
  Status: $(git status --porcelain | wc -l) changes
---
EOF
}

# Main execution
main() {
    # Create log directories
    mkdir -p "$(dirname "$LOG_FILE")"
    mkdir -p "$(dirname "$GIT_LOG_FILE")"
    
    log_message "INFO" "Post-git verification for: $GIT_COMMAND"
    
    # Log the operation
    log_git_operation "$GIT_COMMAND" "$TOOL_OUTPUT"
    
    # Verify repository state
    if git rev-parse --git-dir >/dev/null 2>&1; then
        log_message "SUCCESS" "Git repository state verified"
    else
        log_message "ERROR" "Git repository verification failed"
    fi
    
    exit 0
}

main "$@"