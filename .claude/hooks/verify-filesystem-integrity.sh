#!/bin/bash

# File System Integrity Verification Hook
# Prevents Write/Edit/MultiEdit failures due to file system issues
# Based on 2025 Claude Code hooks best practices

set -euo pipefail

# Configuration
HOOK_NAME="verify-filesystem-integrity"
LOG_FILE="/Users/nalve/ce-simple/.claude/logs/hooks.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Tool input from arguments
TOOL_INPUT="$1"

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
            echo "HOOK_ERROR: File system integrity verification failed"
            echo "GUIDANCE: $error_message"
            echo "SUGGESTED_ACTIONS:"
            echo "  - Check file/directory permissions"
            echo "  - Verify parent directories exist"
            echo "  - Ensure sufficient disk space"
            echo "  - Check for file locks or processes using the file"
            ;;
        2)
            echo "HOOK_WARNING: File system warning"
            echo "GUIDANCE: $error_message"
            ;;
        3)
            echo "HOOK_SKIP: File operation skipped due to precondition"
            echo "GUIDANCE: $error_message"
            ;;
    esac
    
    exit "$exit_code"
}

# Extract file path from tool input (handles JSON and direct paths)
extract_file_path() {
    local input="$1"
    local file_path=""
    
    # Try to extract file_path from JSON input
    if echo "$input" | jq -e '.file_path' >/dev/null 2>&1; then
        file_path=$(echo "$input" | jq -r '.file_path')
    elif echo "$input" | grep -q '"file_path"'; then
        # Simple regex extraction if jq fails
        file_path=$(echo "$input" | sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')
    else
        # Assume input is the file path directly
        file_path="$input"
    fi
    
    # Clean up the path
    file_path=$(echo "$file_path" | tr -d '"' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
    
    echo "$file_path"
}

# Verify file path is valid and safe
verify_file_path_safety() {
    local file_path="$1"
    
    # Check for empty path
    if [[ -z "$file_path" ]]; then
        handle_error 1 "File path is empty or could not be extracted"
    fi
    
    # Check for potentially dangerous paths
    if [[ "$file_path" =~ \.\./|\.\.\\ ]]; then
        handle_error 1 "File path contains directory traversal: $file_path"
    fi
    
    # Check for absolute vs relative paths
    if [[ "$file_path" = /* ]]; then
        log_message "INFO" "Using absolute path: $file_path"
    else
        log_message "INFO" "Using relative path: $file_path"
        # Convert to absolute path for further checks
        file_path="$(pwd)/$file_path"
    fi
    
    # Check path length (some filesystems have limits)
    if [[ ${#file_path} -gt 1024 ]]; then
        handle_error 1 "File path too long (>1024 characters): $file_path"
    fi
    
    # Check for invalid characters (basic check)
    if [[ "$file_path" =~ [[:cntrl:]] ]]; then
        handle_error 1 "File path contains control characters: $file_path"
    fi
    
    log_message "INFO" "File path safety verified: $file_path"
    echo "$file_path"
}

# Verify parent directory exists and is accessible
verify_parent_directory() {
    local file_path="$1"
    local parent_dir
    
    parent_dir=$(dirname "$file_path")
    
    log_message "INFO" "Checking parent directory: $parent_dir"
    
    # Check if parent directory exists
    if [[ ! -d "$parent_dir" ]]; then
        # Try to create parent directories
        if mkdir -p "$parent_dir" 2>/dev/null; then
            log_message "INFO" "Created parent directory: $parent_dir"
        else
            handle_error 1 "Parent directory does not exist and cannot be created: $parent_dir"
        fi
    fi
    
    # Check if parent directory is writable
    if [[ ! -w "$parent_dir" ]]; then
        handle_error 1 "Parent directory is not writable: $parent_dir"
    fi
    
    log_message "INFO" "Parent directory verified: $parent_dir"
}

# Verify file accessibility for existing files
verify_existing_file() {
    local file_path="$1"
    
    if [[ -e "$file_path" ]]; then
        log_message "INFO" "File exists, checking accessibility: $file_path"
        
        # Check if file is readable (for Edit operations)
        if [[ ! -r "$file_path" ]]; then
            handle_error 1 "Existing file is not readable: $file_path"
        fi
        
        # Check if file is writable
        if [[ ! -w "$file_path" ]]; then
            handle_error 1 "Existing file is not writable: $file_path"
        fi
        
        # Check if file is locked (basic check)
        if lsof "$file_path" >/dev/null 2>&1; then
            log_message "WARN" "File appears to be in use by another process: $file_path"
            handle_error 2 "File may be locked by another process"
        fi
        
        # Check file type
        if [[ -d "$file_path" ]]; then
            handle_error 1 "Target path is a directory, not a file: $file_path"
        fi
        
        # Check for symbolic links
        if [[ -L "$file_path" ]]; then
            local target
            target=$(readlink "$file_path")
            log_message "INFO" "File is a symbolic link to: $target"
            
            # Verify the link target exists and is accessible
            if [[ ! -e "$file_path" ]]; then
                handle_error 1 "Symbolic link target does not exist: $file_path -> $target"
            fi
        fi
        
        log_message "INFO" "Existing file accessibility verified: $file_path"
    else
        log_message "INFO" "File does not exist (will be created): $file_path"
    fi
}

# Check disk space availability
verify_disk_space() {
    local file_path="$1"
    local parent_dir
    
    parent_dir=$(dirname "$file_path")
    
    log_message "INFO" "Checking disk space for: $parent_dir"
    
    # Get available space in KB
    local available_space
    available_space=$(df "$parent_dir" | awk 'NR==2 {print $4}')
    
    # Require at least 10MB free space for file operations
    if [[ "$available_space" -lt 10240 ]]; then
        handle_error 1 "Insufficient disk space (less than 10MB available) in: $parent_dir"
    fi
    
    # For large operations, check for more space
    if [[ "$available_space" -lt 102400 ]]; then
        log_message "WARN" "Low disk space (<100MB) in: $parent_dir"
    fi
    
    log_message "INFO" "Sufficient disk space available: ${available_space}KB"
}

# Verify file system type and limitations
verify_filesystem_type() {
    local file_path="$1"
    local parent_dir
    
    parent_dir=$(dirname "$file_path")
    
    # Get filesystem type
    local fs_type
    fs_type=$(df -T "$parent_dir" 2>/dev/null | awk 'NR==2 {print $2}' || echo "unknown")
    
    log_message "INFO" "Filesystem type: $fs_type"
    
    # Check for known problematic filesystems
    case "$fs_type" in
        "vfat"|"msdos")
            # FAT filesystems have limitations
            local filename
            filename=$(basename "$file_path")
            if [[ ${#filename} -gt 255 ]]; then
                handle_error 1 "Filename too long for FAT filesystem: $filename"
            fi
            if [[ "$filename" =~ [<>\|:\*\?\"\\] ]]; then
                handle_error 1 "Filename contains characters invalid for FAT filesystem: $filename"
            fi
            ;;
        "ntfs")
            # NTFS has some restrictions
            local filename
            filename=$(basename "$file_path")
            if [[ "$filename" =~ [<>\|:\*\?\"\\] ]]; then
                handle_error 1 "Filename contains characters invalid for NTFS filesystem: $filename"
            fi
            ;;
    esac
    
    log_message "INFO" "Filesystem compatibility verified"
}

# Check for backup/version control considerations
verify_backup_considerations() {
    local file_path="$1"
    
    # Check if file is in a git repository
    if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
        # Check if file is ignored
        if git check-ignore "$file_path" >/dev/null 2>&1; then
            log_message "INFO" "File is git-ignored: $file_path"
        else
            log_message "INFO" "File is tracked by git: $file_path"
        fi
    fi
    
    # Check for existing backup files
    if [[ -e "$file_path.bak" ]] || [[ -e "$file_path~" ]]; then
        log_message "INFO" "Backup files detected for: $file_path"
    fi
}

# Enhanced verification with debugging support
debug_filesystem_state() {
    if [[ "${CLAUDE_DEBUG_HOOKS:-false}" == "true" ]]; then
        log_message "DEBUG" "=== Filesystem State Debug Information ==="
        log_message "DEBUG" "Current working directory: $(pwd)"
        log_message "DEBUG" "User: $(whoami)"
        log_message "DEBUG" "Umask: $(umask)"
        log_message "DEBUG" "Tool input: $TOOL_INPUT"
        
        # Show filesystem information
        log_message "DEBUG" "Filesystem information:"
        df -h "$(pwd)" | while read -r line; do
            log_message "DEBUG" "  $line"
        done
        
        log_message "DEBUG" "=== End Debug Information ==="
    fi
}

# Emergency override check
check_emergency_override() {
    if [[ "${CLAUDE_EMERGENCY_OVERRIDE:-false}" == "true" ]]; then
        log_message "WARN" "Emergency override activated - bypassing filesystem verification"
        return 0
    fi
    return 1
}

# Main verification function
verify_filesystem_integrity() {
    log_message "INFO" "Starting filesystem integrity verification"
    
    # Extract file path from tool input
    local file_path
    file_path=$(extract_file_path "$TOOL_INPUT")
    
    # Verify file path safety
    file_path=$(verify_file_path_safety "$file_path")
    
    # Run all verification steps
    verify_parent_directory "$file_path"
    verify_existing_file "$file_path"
    verify_disk_space "$file_path"
    verify_filesystem_type "$file_path"
    verify_backup_considerations "$file_path"
    
    log_message "INFO" "Filesystem integrity verification completed successfully for: $file_path"
}

# Main execution
main() {
    # Create log directory if it doesn't exist
    mkdir -p "$(dirname "$LOG_FILE")"
    
    # Validate input
    if [[ -z "$TOOL_INPUT" ]]; then
        handle_error 1 "No tool input provided for verification"
    fi
    
    # Check for emergency override first
    if check_emergency_override; then
        exit 0
    fi
    
    # Run debug logging if enabled
    debug_filesystem_state
    
    # Perform main verification
    verify_filesystem_integrity
    
    # If we get here, verification passed
    log_message "SUCCESS" "Filesystem integrity verification passed"
    exit 0
}

# Trap signals for clean exit
trap 'log_message "ERROR" "Script interrupted"; exit 130' INT TERM

# Execute main function
main "$@"