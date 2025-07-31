#!/bin/bash

# Claude Code Hook: Root Structure Protection
# Prevents unauthorized files in project root with intelligent auto-remediation

set -euo pipefail

# Input parameters
FILE_PATH="${1:-}"
PROJECT_ROOT="/Users/nalve/ce-simple"
LOG_FILE="$PROJECT_ROOT/.claude/hooks/protection.log"

# Guardian enforcement logging
log_event() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] CLAUDE_HOOK: $1" >> "$LOG_FILE"
}

log_violation() {
    echo "🛡️ GUARDIAN: $1"
    log_event "VIOLATION: $1"
}

log_action() {
    echo "✅ GUARDIAN: $1"
    log_event "ACTION: $1"
}

# Check if file path is provided
if [[ -z "$FILE_PATH" ]]; then
    log_event "root-protection.sh called without file path"
    exit 0
fi

# Skip if file doesn't exist or is not a real file
if [[ ! -f "$FILE_PATH" ]]; then
    exit 0
fi

# Get relative path and filename
RELATIVE_PATH="${FILE_PATH#$PROJECT_ROOT/}"
FILENAME=$(basename "$FILE_PATH")
DIRNAME=$(dirname "$FILE_PATH")

# Check if file is in project root (not in subdirectory)
if [[ "$DIRNAME" == "$PROJECT_ROOT" ]]; then
    
    # Define allowed files in root
    case "$FILENAME" in
        "CLAUDE.md"|"README.md"|".gitignore"|".gitattributes")
            log_event "Authorized root file: $FILENAME"
            exit 0
            ;;
        *)
            # Unauthorized file in root detected
            log_violation "ROOT POLLUTION: Unauthorized file in project root - $FILENAME"
            
            # Determine target directory based on file type and name
            TARGET_DIR=""
            case "$FILENAME" in
                *"REPORT"*|*"report"*|*"VALIDATION"*|*"validation"*|*"ANALYSIS"*|*"analysis"*)
                    TARGET_DIR="$PROJECT_ROOT/context/archive/processing_reports"
                    ;;
                *.md)
                    TARGET_DIR="$PROJECT_ROOT/context/archive"
                    ;;
                *.log)
                    TARGET_DIR="$PROJECT_ROOT/.claude/hooks"
                    ;;
                *.json|*.js|*.py|*.sh)
                    TARGET_DIR="$PROJECT_ROOT/scripts"
                    ;;
                *)
                    TARGET_DIR="$PROJECT_ROOT/context/archive"
                    ;;
            esac
            
            # Ensure target directory exists
            mkdir -p "$TARGET_DIR"
            
            # Attempt auto-relocation
            if mv "$FILE_PATH" "$TARGET_DIR/"; then
                log_action "Auto-relocated: $FILENAME → $(basename "$TARGET_DIR")/"
                echo "📁 File automatically moved to appropriate location: $(basename "$TARGET_DIR")/"
                log_event "ROOT_VIOLATION_CORRECTED: $FILENAME relocated to $(basename "$TARGET_DIR")"
            else
                log_violation "Auto-relocation failed for: $FILENAME"
                echo "⚠️ Could not auto-relocate file. Please move manually to appropriate directory."
                log_event "ROOT_VIOLATION_UNCORRECTED: $FILENAME - manual intervention required"
                exit 1
            fi
            ;;
    esac
else
    # File is in subdirectory - log for monitoring but allow
    log_event "File operation in subdirectory: $RELATIVE_PATH"
fi

exit 0