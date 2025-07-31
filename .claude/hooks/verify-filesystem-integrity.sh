#!/bin/bash

# verify-filesystem-integrity.sh - File Operation Validation Hook
# AUTHORITY: CLAUDE.md READ-BEFORE-EDIT enforcement
# Performance: <100ms for PreToolUse hook compliance

set -euo pipefail

# Logging setup
HOOK_LOG="/Users/nalve/ce-simple/.claude/logs/hooks.log"
mkdir -p "$(dirname "$HOOK_LOG")"

# Function to log messages
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [verify-filesystem-integrity] $1" >> "$HOOK_LOG"
}

# Function to extract file path from tool input
extract_file_path() {
    local tool_input="$1"
    
    # Extract file_path from JSON-like input (Edit/Write/MultiEdit tools)
    if echo "$tool_input" | grep -q "file_path"; then
        echo "$tool_input" | grep -o '"file_path":\s*"[^"]*"' | sed 's/"file_path":\s*"//; s/"//'
    else
        # Return empty if no file_path found
        echo ""
    fi
}

# Function to validate READ-BEFORE-EDIT compliance
validate_read_compliance() {
    local file_path="$1"
    local session_log="/tmp/claude_session_tools.log"
    
    # Check if Read tool was used for this file in current session
    if [[ -f "$session_log" ]]; then
        if grep -q "Read.*$file_path" "$session_log" 2>/dev/null; then
            log_message "✅ Read compliance validated for: $file_path"
            return 0
        fi
    fi
    
    # Log READ-BEFORE-EDIT violation
    log_message "❌ READ-BEFORE-EDIT violation: $file_path (no Read tool usage detected)"
    echo "⚠️ ENFORCEMENT VIOLATION: OBLIGATORIO Read tool antes de Edit/Write/MultiEdit operations"
    echo "File: $file_path"
    echo "CLAUDE.md requirement: READ-BEFORE-EDIT OBLIGATORIO"
    return 1
}

# Function to validate file location accuracy
validate_location_accuracy() {
    local file_path="$1"
    
    # Convert relative paths to absolute
    if [[ ! "$file_path" = /* ]]; then
        file_path="/Users/nalve/ce-simple/$file_path"
    fi
    
    # Check if file exists (for Edit operations)
    if [[ "$CLAUDE_TOOL_NAME" == "Edit" ]] && [[ ! -f "$file_path" ]]; then
        log_message "❌ File not found for Edit: $file_path"
        echo "❌ FILE LOCATION ERROR: File does not exist for Edit operation"
        echo "File: $file_path"
        echo "Suggestion: Verify file path or use Write tool for new files"
        return 1
    fi
    
    # Check parent directory exists (for Write operations)
    local parent_dir="$(dirname "$file_path")"
    if [[ ! -d "$parent_dir" ]]; then
        log_message "❌ Parent directory not found: $parent_dir"
        echo "❌ DIRECTORY ERROR: Parent directory does not exist"
        echo "Directory: $parent_dir"
        echo "File: $file_path"
        return 1
    fi
    
    log_message "✅ File location validated: $file_path"
    return 0
}

# Main validation logic
main() {
    local tool_input="${1:-}"
    
    log_message "Validating filesystem integrity for tool: $CLAUDE_TOOL_NAME"
    
    # Extract file path from tool input
    local file_path
    file_path=$(extract_file_path "$tool_input")
    
    if [[ -z "$file_path" ]]; then
        log_message "⚠️ No file_path found in tool input, skipping validation"
        exit 0
    fi
    
    # Validate location accuracy
    if ! validate_location_accuracy "$file_path"; then
        exit 1
    fi
    
    # Validate READ-BEFORE-EDIT compliance (only for Edit operations)
    if [[ "$CLAUDE_TOOL_NAME" == "Edit" ]] || [[ "$CLAUDE_TOOL_NAME" == "MultiEdit" ]]; then
        if ! validate_read_compliance "$file_path"; then
            exit 1
        fi
    fi
    
    # Log tool usage for session tracking
    echo "$(date '+%Y-%m-%d %H:%M:%S') $CLAUDE_TOOL_NAME $file_path" >> "/tmp/claude_session_tools.log"
    
    log_message "✅ Filesystem integrity validation passed for: $file_path"
    exit 0
}

# Execute main function
main "$@"