#!/bin/bash

# Post-Document Operation Verification Hook
# Logs document operations and verifies integrity after completion
# Based on 2025 Claude Code hooks best practices

set -euo pipefail

# Configuration
HOOK_NAME="post-document-verification"
LOG_FILE="/Users/nalve/ce-simple/.claude/logs/hooks.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
DOC_LOG_FILE="/Users/nalve/ce-simple/.claude/logs/document-operations.log"

# Parameters
FILE_PATHS="$1"
TOOL_OUTPUT="$2"

# Logging function
log_message() {
    local level="$1"
    local message="$2"
    echo "[$TIMESTAMP] [$HOOK_NAME] [$level] $message" | tee -a "$LOG_FILE"
}

# Log document operation
log_document_operation() {
    local file_paths="$1"
    local output="$2"
    
    # Create document log entry
    cat >> "$DOC_LOG_FILE" << EOF
[$TIMESTAMP] Document Operation
Files: $file_paths
Output: $output
File Status After:
EOF
    
    # Check each file
    for file_path in $file_paths; do
        if [[ -f "$file_path" ]]; then
            local size=$(wc -c < "$file_path" 2>/dev/null || echo "0")
            local lines=$(wc -l < "$file_path" 2>/dev/null || echo "0")
            echo "  $file_path: exists, $size bytes, $lines lines" >> "$DOC_LOG_FILE"
        else
            echo "  $file_path: does not exist" >> "$DOC_LOG_FILE"
        fi
    done
    
    echo "---" >> "$DOC_LOG_FILE"
}

# Main execution
main() {
    # Create log directories
    mkdir -p "$(dirname "$LOG_FILE")"
    mkdir -p "$(dirname "$DOC_LOG_FILE")"
    
    log_message "INFO" "Post-document verification for: $FILE_PATHS"
    
    # Log the operation
    log_document_operation "$FILE_PATHS" "$TOOL_OUTPUT"
    
    log_message "SUCCESS" "Document operation logged"
    exit 0
}

main "$@"