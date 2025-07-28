#!/bin/bash

# Permission Boundary Verification Hook
# Validates operations against established permission boundaries in settings.local.json
# Based on 2025 Claude Code hooks best practices

set -euo pipefail

# Configuration
HOOK_NAME="verify-permission-boundaries"
LOG_FILE="/Users/nalve/ce-simple/.claude/logs/hooks.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
SETTINGS_FILE="/Users/nalve/ce-simple/.claude/settings.local.json"

# Tool arguments from parameters
TOOL_ARGS="$1"

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
            echo "HOOK_ERROR: Permission boundary violation detected"
            echo "GUIDANCE: $error_message"
            echo "RESOLUTION: Check .claude/settings.local.json permissions configuration"
            echo "REFERENCE: Review allowed/denied tool patterns in settings"
            ;;
        2)
            echo "HOOK_WARNING: Permission boundary warning"
            echo "GUIDANCE: $error_message"
            ;;
        3)
            echo "HOOK_SKIP: Operation skipped due to permission restrictions"
            echo "GUIDANCE: $error_message"
            ;;
    esac
    
    exit "$exit_code"
}

# Load permission settings from settings.local.json
load_permission_settings() {
    if [[ ! -f "$SETTINGS_FILE" ]]; then
        log_message "WARN" "Settings file not found: $SETTINGS_FILE"
        return 1
    fi
    
    # Validate JSON structure
    if ! jq empty "$SETTINGS_FILE" 2>/dev/null; then
        handle_error 1 "Invalid JSON in settings file: $SETTINGS_FILE"
    fi
    
    log_message "INFO" "Permission settings loaded from: $SETTINGS_FILE"
    return 0
}

# Extract command from tool arguments
extract_command() {
    local args="$1"
    local command=""
    
    # Handle common command patterns
    if [[ "$args" =~ ^([a-zA-Z0-9_/-]+) ]]; then
        command="${BASH_REMATCH[1]}"
    else
        # Fallback - take first word
        command=$(echo "$args" | awk '{print $1}')
    fi
    
    echo "$command"
}

# Check if command matches allowed patterns
check_allowed_patterns() {
    local command="$1"
    local full_args="$2"
    
    log_message "INFO" "Checking allowed patterns for command: $command"
    
    # Get allowed patterns from settings
    local allowed_patterns
    if ! allowed_patterns=$(jq -r '.permissions.allow[]?' "$SETTINGS_FILE" 2>/dev/null); then
        log_message "WARN" "Could not read allowed patterns from settings"
        return 0  # Allow by default if we can't read settings
    fi
    
    # Check each allowed pattern
    while IFS= read -r pattern; do
        [[ -z "$pattern" ]] && continue
        
        # Handle different pattern types
        if [[ "$pattern" =~ ^Bash\((.*)\)$ ]]; then
            local bash_pattern="${BASH_REMATCH[1]}"
            
            # Handle wildcard patterns
            if [[ "$bash_pattern" == "*" ]]; then
                log_message "INFO" "Command allowed by wildcard pattern: Bash(*)"
                return 0
            fi
            
            # Handle specific command patterns
            if [[ "$bash_pattern" == "$command:*" ]] || [[ "$bash_pattern" == "$command" ]]; then
                log_message "INFO" "Command allowed by pattern: $pattern"
                return 0
            fi
            
            # Handle regex-like patterns
            if [[ "$full_args" =~ $bash_pattern ]]; then
                log_message "INFO" "Command allowed by regex pattern: $pattern"
                return 0
            fi
        fi
        
        # Handle other tool patterns
        if [[ "$pattern" =~ ^([^(]+)\((.*)\)$ ]]; then
            local tool_name="${BASH_REMATCH[1]}"
            local tool_pattern="${BASH_REMATCH[2]}"
            
            # This is for non-Bash tools, skip for Bash command checking
            continue
        fi
        
        # Direct pattern matching
        if [[ "$command" == "$pattern" ]] || [[ "$full_args" =~ $pattern ]]; then
            log_message "INFO" "Command allowed by direct pattern: $pattern"
            return 0
        fi
        
    done <<< "$allowed_patterns"
    
    return 1  # Not found in allowed patterns
}

# Check if command matches denied patterns
check_denied_patterns() {
    local command="$1"
    local full_args="$2"
    
    log_message "INFO" "Checking denied patterns for command: $command"
    
    # Get denied patterns from settings
    local denied_patterns
    if ! denied_patterns=$(jq -r '.permissions.deny[]?' "$SETTINGS_FILE" 2>/dev/null); then
        log_message "INFO" "No denied patterns found in settings"
        return 1  # Not denied if no patterns exist
    fi
    
    # Check each denied pattern
    while IFS= read -r pattern; do
        [[ -z "$pattern" ]] && continue
        
        # Handle Write patterns for specific paths
        if [[ "$pattern" =~ ^Write\((.*)\)$ ]]; then
            local write_pattern="${BASH_REMATCH[1]}"
            # This applies to Write tool, not Bash commands
            continue
        fi
        
        # Handle MultiEdit patterns
        if [[ "$pattern" =~ ^MultiEdit\((.*)\)$ ]]; then
            local edit_pattern="${BASH_REMATCH[1]}"
            # This applies to MultiEdit tool, not Bash commands
            continue
        fi
        
        # Direct pattern matching for bash commands
        if [[ "$command" == "$pattern" ]] || [[ "$full_args" =~ $pattern ]]; then
            log_message "ERROR" "Command denied by pattern: $pattern"
            return 0  # Found in denied patterns
        fi
        
    done <<< "$denied_patterns"
    
    return 1  # Not found in denied patterns
}

# Check for dangerous command patterns
check_dangerous_commands() {
    local command="$1"
    local full_args="$2"
    
    log_message "INFO" "Checking for dangerous command patterns"
    
    # Define dangerous patterns
    local dangerous_patterns=(
        "rm -rf /"
        "rm -rf /usr"
        "rm -rf /var"
        "rm -rf /etc"
        ":(){ :|:& };:"  # Fork bomb
        "chmod -R 777 /"
        "dd if=/dev/zero of="
        "mkfs\."
        "fdisk"
        "cfdisk"
        "parted"
        "> /dev/sda"
        "> /dev/hda"
    )
    
    for pattern in "${dangerous_patterns[@]}"; do
        if [[ "$full_args" =~ $pattern ]]; then
            handle_error 1 "Dangerous command pattern detected: $pattern"
        fi
    done
    
    # Check for suspicious sudo usage
    if [[ "$full_args" =~ sudo.*rm.*-rf ]] || [[ "$full_args" =~ sudo.*chmod.*-R ]]; then
        handle_error 1 "Suspicious sudo command detected: $full_args"
    fi
    
    log_message "INFO" "No dangerous command patterns detected"
}

# Verify file access permissions
verify_file_access_permissions() {
    local full_args="$1"
    
    # Extract file paths from common commands
    local file_paths=()
    
    # Handle common file operations
    if [[ "$full_args" =~ (cp|mv|rm|chmod|chown).*([[:space:]]/)([^[:space:]]+) ]]; then
        # Extract paths that start with /
        while [[ "$full_args" =~ [[:space:]](/[^[:space:]]+) ]]; do
            file_paths+=("${BASH_REMATCH[1]}")
            full_args="${full_args/${BASH_REMATCH[0]}/ }"
        done
    fi
    
    # Check each file path
    for file_path in "${file_paths[@]}"; do
        # Check for access to sensitive system directories
        if [[ "$file_path" =~ ^/(etc|usr/bin|usr/sbin|var/log|boot|sys|proc)(/|$) ]]; then
            handle_error 1 "Access to sensitive system directory: $file_path"
        fi
        
        # Check for access outside project directory
        local project_dir="/Users/nalve/ce-simple"
        if [[ "$file_path" = /* ]] && [[ ! "$file_path" =~ ^$project_dir ]]; then
            log_message "WARN" "Access to file outside project directory: $file_path"
            # Don't block, but log for monitoring
        fi
    done
}

# Check resource consumption limits
check_resource_limits() {
    local full_args="$1"
    
    log_message "INFO" "Checking resource consumption limits"
    
    # Check for potentially resource-intensive commands
    local resource_heavy_commands=(
        "find / "
        "grep -r / "
        "dd "
        "tar czf "
        "gzip "
        "python.*-c.*while True"
        "while true"
        "for.*in.*{1..1000000}"
    )
    
    for pattern in "${resource_heavy_commands[@]}"; do
        if [[ "$full_args" =~ $pattern ]]; then
            log_message "WARN" "Resource-intensive command detected: $pattern"
            handle_error 2 "Resource-intensive operation - monitor system resources"
        fi
    done
    
    log_message "INFO" "Resource consumption check completed"
}

# Enhanced verification with debugging support
debug_permission_state() {
    if [[ "${CLAUDE_DEBUG_HOOKS:-false}" == "true" ]]; then
        log_message "DEBUG" "=== Permission State Debug Information ==="
        log_message "DEBUG" "Tool arguments: $TOOL_ARGS"
        log_message "DEBUG" "Settings file: $SETTINGS_FILE"
        log_message "DEBUG" "Settings file exists: $(test -f "$SETTINGS_FILE" && echo "yes" || echo "no")"
        
        # Show permission summary
        if [[ -f "$SETTINGS_FILE" ]]; then
            log_message "DEBUG" "Allowed patterns count: $(jq '.permissions.allow | length' "$SETTINGS_FILE" 2>/dev/null || echo "unknown")"
            log_message "DEBUG" "Denied patterns count: $(jq '.permissions.deny | length' "$SETTINGS_FILE" 2>/dev/null || echo "unknown")"
        fi
        
        log_message "DEBUG" "Current user: $(whoami)"
        log_message "DEBUG" "Current directory: $(pwd)"
        log_message "DEBUG" "=== End Debug Information ==="
    fi
}

# Emergency override check
check_emergency_override() {
    if [[ "${CLAUDE_EMERGENCY_OVERRIDE:-false}" == "true" ]]; then
        log_message "WARN" "Emergency override activated - bypassing permission boundary verification"
        return 0
    fi
    return 1
}

# Main verification function
verify_permission_boundaries() {
    log_message "INFO" "Starting permission boundary verification"
    
    # Load permission settings
    if ! load_permission_settings; then
        log_message "WARN" "Proceeding without permission settings validation"
        return 0
    fi
    
    # Extract command from arguments
    local command
    command=$(extract_command "$TOOL_ARGS")
    
    log_message "INFO" "Verifying permissions for command: $command"
    
    # Run verification steps
    check_dangerous_commands "$command" "$TOOL_ARGS"
    verify_file_access_permissions "$TOOL_ARGS"
    check_resource_limits "$TOOL_ARGS"
    
    # Check against permission patterns
    if check_denied_patterns "$command" "$TOOL_ARGS"; then
        handle_error 1 "Command matches denied pattern: $command"
    fi
    
    if ! check_allowed_patterns "$command" "$TOOL_ARGS"; then
        handle_error 1 "Command not found in allowed patterns: $command"
    fi
    
    log_message "INFO" "Permission boundary verification completed successfully for: $command"
}

# Main execution
main() {
    # Create log directory if it doesn't exist
    mkdir -p "$(dirname "$LOG_FILE")"
    
    # Validate input
    if [[ -z "$TOOL_ARGS" ]]; then
        handle_error 1 "No tool arguments provided for verification"
    fi
    
    # Check for emergency override first
    if check_emergency_override; then
        exit 0
    fi
    
    # Run debug logging if enabled
    debug_permission_state
    
    # Perform main verification
    verify_permission_boundaries
    
    # If we get here, verification passed
    log_message "SUCCESS" "Permission boundary verification passed"
    exit 0
}

# Trap signals for clean exit
trap 'log_message "ERROR" "Script interrupted"; exit 130' INT TERM

# Execute main function
main "$@"