#!/bin/bash

# Git Repository State Validation Hook
# Prevents git operation failures due to repository health issues
# Based on 2025 Claude Code hooks best practices

set -euo pipefail

# Configuration
HOOK_NAME="verify-git-state"
LOG_FILE="/Users/nalve/ce-simple/.claude/logs/hooks.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Git command from arguments
GIT_COMMAND="$1"

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
            echo "HOOK_ERROR: Git repository validation failed"
            echo "GUIDANCE: $error_message"
            echo "SUGGESTED_ACTIONS:"
            echo "  - Check repository integrity with 'git fsck'"
            echo "  - Verify working directory is clean"
            echo "  - Ensure proper git configuration"
            ;;
        2)
            echo "HOOK_WARNING: Git repository state warning"
            echo "GUIDANCE: $error_message"
            ;;
        3)
            echo "HOOK_SKIP: Git operation skipped due to precondition"
            echo "GUIDANCE: $error_message"
            ;;
    esac
    
    exit "$exit_code"
}

# Check if we're in a git repository
verify_git_repository() {
    if ! git rev-parse --git-dir >/dev/null 2>&1; then
        handle_error 1 "Not in a git repository"
    fi
    
    log_message "INFO" "Confirmed we are in a git repository"
}

# Verify repository integrity
verify_repository_integrity() {
    log_message "INFO" "Checking repository integrity"
    
    # Check for repository corruption
    if ! git fsck --no-progress --no-dangling >/dev/null 2>&1; then
        handle_error 1 "Repository integrity check failed - corruption detected"
    fi
    
    # Check if .git directory is accessible
    local git_dir
    git_dir=$(git rev-parse --git-dir)
    if [[ ! -d "$git_dir" ]] || [[ ! -r "$git_dir" ]]; then
        handle_error 1 "Git directory is not accessible: $git_dir"
    fi
    
    log_message "INFO" "Repository integrity verified"
}

# Check working directory state
verify_working_directory() {
    log_message "INFO" "Checking working directory state"
    
    # Check if working directory is readable/writable
    if [[ ! -w "$(pwd)" ]]; then
        handle_error 1 "Working directory is not writable"
    fi
    
    # For operations that require clean working directory
    if [[ "$GIT_COMMAND" =~ (merge|rebase|checkout.*-b) ]]; then
        local status_output
        status_output=$(git status --porcelain)
        if [[ -n "$status_output" ]]; then
            log_message "WARN" "Working directory is not clean for operation: $GIT_COMMAND"
            handle_error 2 "Working directory has uncommitted changes"
        fi
    fi
    
    log_message "INFO" "Working directory state verified"
}

# Verify git configuration
verify_git_configuration() {
    log_message "INFO" "Checking git configuration"
    
    # Check for basic configuration
    local user_name user_email
    user_name=$(git config user.name 2>/dev/null || echo "")
    user_email=$(git config user.email 2>/dev/null || echo "")
    
    if [[ -z "$user_name" ]] || [[ -z "$user_email" ]]; then
        if [[ "$GIT_COMMAND" =~ commit ]]; then
            handle_error 1 "Git user.name and user.email must be configured for commits"
        else
            log_message "WARN" "Git user configuration incomplete"
        fi
    fi
    
    log_message "INFO" "Git configuration verified"
}

# Check remote connectivity (for push/pull operations)
verify_remote_connectivity() {
    if [[ "$GIT_COMMAND" =~ (push|pull|fetch) ]]; then
        log_message "INFO" "Checking remote connectivity for: $GIT_COMMAND"
        
        # Get current branch and its remote
        local current_branch remote_name
        current_branch=$(git branch --show-current 2>/dev/null || echo "")
        
        if [[ -n "$current_branch" ]]; then
            remote_name=$(git config "branch.$current_branch.remote" 2>/dev/null || echo "origin")
            
            # Check if remote exists
            if ! git remote get-url "$remote_name" >/dev/null 2>&1; then
                if [[ "$GIT_COMMAND" =~ push ]]; then
                    handle_error 1 "Remote '$remote_name' not configured for push operation"
                else
                    log_message "WARN" "Remote '$remote_name' not found"
                fi
            fi
            
            # Test connectivity (lightweight check)
            if ! timeout 5 git ls-remote --heads "$remote_name" >/dev/null 2>&1; then
                if [[ "$GIT_COMMAND" =~ push ]]; then
                    handle_error 2 "Cannot connect to remote '$remote_name' - network or authentication issue"
                else
                    log_message "WARN" "Remote connectivity test failed for '$remote_name'"
                fi
            fi
        else
            log_message "WARN" "No current branch detected"
        fi
        
        log_message "INFO" "Remote connectivity verified"
    fi
}

# Check for conflicting processes
verify_no_conflicting_processes() {
    log_message "INFO" "Checking for conflicting git processes"
    
    # Check for git index lock
    local git_dir
    git_dir=$(git rev-parse --git-dir)
    
    if [[ -f "$git_dir/index.lock" ]]; then
        handle_error 1 "Git index is locked - another git process may be running"
    fi
    
    # Check for other git lock files
    if find "$git_dir" -name "*.lock" -type f 2>/dev/null | grep -q .; then
        handle_error 1 "Git lock files detected - repository may be in use by another process"
    fi
    
    log_message "INFO" "No conflicting processes detected"
}

# Verify branch state for specific operations
verify_branch_state() {
    if [[ "$GIT_COMMAND" =~ (merge|rebase|checkout) ]]; then
        log_message "INFO" "Checking branch state for: $GIT_COMMAND"
        
        local current_branch
        current_branch=$(git branch --show-current 2>/dev/null || echo "")
        
        if [[ -z "$current_branch" ]]; then
            if [[ "$GIT_COMMAND" =~ (merge|rebase) ]]; then
                handle_error 1 "Cannot perform $GIT_COMMAND in detached HEAD state"
            fi
        fi
        
        # Check for unmerged paths (indicating ongoing merge/rebase)
        if git ls-files --unmerged | grep -q .; then
            handle_error 1 "Repository has unmerged paths - resolve conflicts first"
        fi
        
        log_message "INFO" "Branch state verified"
    fi
}

# Check disk space
verify_disk_space() {
    log_message "INFO" "Checking available disk space"
    
    local available_space
    # Get available space in KB
    available_space=$(df "$(pwd)" | awk 'NR==2 {print $4}')
    
    # Require at least 100MB free space for git operations
    if [[ "$available_space" -lt 102400 ]]; then
        handle_error 1 "Insufficient disk space (less than 100MB available)"
    fi
    
    log_message "INFO" "Sufficient disk space available"
}

# Enhanced verification with debugging support
debug_git_state() {
    if [[ "${CLAUDE_DEBUG_HOOKS:-false}" == "true" ]]; then
        log_message "DEBUG" "=== Git State Debug Information ==="
        log_message "DEBUG" "Git version: $(git --version)"
        log_message "DEBUG" "Repository root: $(git rev-parse --show-toplevel 2>/dev/null || echo 'N/A')"
        log_message "DEBUG" "Current branch: $(git branch --show-current 2>/dev/null || echo 'N/A')"
        log_message "DEBUG" "Remote branches:"
        git branch -r 2>/dev/null | head -5 | while read -r line; do
            log_message "DEBUG" "  $line"
        done
        log_message "DEBUG" "Recent commits:"
        git log --oneline -3 2>/dev/null | while read -r line; do
            log_message "DEBUG" "  $line"
        done
        log_message "DEBUG" "Git command to execute: $GIT_COMMAND"
        log_message "DEBUG" "=== End Debug Information ==="
    fi
}

# Emergency override check
check_emergency_override() {
    if [[ "${CLAUDE_EMERGENCY_OVERRIDE:-false}" == "true" ]]; then
        log_message "WARN" "Emergency override activated - bypassing git verification"
        return 0
    fi
    return 1
}

# Main verification function
verify_git_state() {
    log_message "INFO" "Starting git state verification for command: $GIT_COMMAND"
    
    # Run all verification steps
    verify_git_repository
    verify_repository_integrity
    verify_working_directory
    verify_git_configuration
    verify_remote_connectivity
    verify_no_conflicting_processes
    verify_branch_state
    verify_disk_space
    
    log_message "INFO" "Git state verification completed successfully"
}

# Main execution
main() {
    # Create log directory if it doesn't exist
    mkdir -p "$(dirname "$LOG_FILE")"
    
    # Validate input
    if [[ -z "$GIT_COMMAND" ]]; then
        handle_error 1 "No git command provided for verification"
    fi
    
    # Check for emergency override first
    if check_emergency_override; then
        exit 0
    fi
    
    # Run debug logging if enabled
    debug_git_state
    
    # Perform main verification
    verify_git_state
    
    # If we get here, verification passed
    log_message "SUCCESS" "Git state verification passed - proceeding with: $GIT_COMMAND"
    exit 0
}

# Trap signals for clean exit
trap 'log_message "ERROR" "Script interrupted"; exit 130' INT TERM

# Execute main function
main "$@"