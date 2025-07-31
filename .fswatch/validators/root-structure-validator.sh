#!/bin/bash

# Root Structure Validator
# Protects project root from unauthorized files

set -euo pipefail

CHANGED_FILE="$1"
PROJECT_ROOT="/Users/nalve/ce-simple"

# Guardian enforcement logging
log_violation() {
    echo "🛡️ GUARDIAN ENFORCEMENT: $1"
}

log_action() {
    echo "✅ GUARDIAN ACTION: $1"
}

# Allowed files in project root
is_allowed_in_root() {
    local file="$1"
    local basename=$(basename "$file")
    
    # Allowed files in root
    case "$basename" in
        "CLAUDE.md"|"README.md"|".gitignore"|".gitattributes")
            return 0
            ;;
        *)
            # Check if it's an allowed directory
            if [[ -d "$file" ]]; then
                case "$basename" in
                    "context"|"scripts"|".git"|".fswatch")
                        return 0
                        ;;
                esac
            fi
            return 1
            ;;
    esac
}

# Auto-move files to appropriate locations
auto_relocate() {
    local file="$1"
    local basename=$(basename "$file")
    local target_dir=""
    
    # Determine target directory based on file type
    case "$basename" in
        *"REPORT"*|*"report"*)
            target_dir="$PROJECT_ROOT/context/archive/processing_reports"
            ;;
        *"VALIDATION"*|*"validation"*)
            target_dir="$PROJECT_ROOT/context/archive/processing_reports"
            ;;
        *"ANALYSIS"*|*"analysis"*)
            target_dir="$PROJECT_ROOT/context/archive/processing_reports"
            ;;
        *.md)
            # Generic markdown files go to archive
            target_dir="$PROJECT_ROOT/context/archive"
            ;;
        *.log)
            target_dir="$PROJECT_ROOT/.fswatch/logs"
            ;;
        *)
            # Default to archive
            target_dir="$PROJECT_ROOT/context/archive"
            ;;
    esac
    
    # Ensure target directory exists
    mkdir -p "$target_dir"
    
    # Move the file
    if [[ -f "$file" ]]; then
        mv "$file" "$target_dir/"
        log_action "Auto-relocated: $basename → $(basename "$target_dir")/"
        return 0
    fi
    
    return 1
}

main() {
    local file="$CHANGED_FILE"
    
    # Skip if file doesn't exist (might have been deleted)
    [[ -e "$file" ]] || return 0
    
    # Get relative path for reporting
    local relative_path="${file#$PROJECT_ROOT/}"
    
    # Check if file is in project root (not in subdirectory)
    if [[ "$relative_path" != */* ]]; then
        
        if ! is_allowed_in_root "$file"; then
            log_violation "ROOT POLLUTION: Unauthorized file in project root - $relative_path"
            
            # Attempt auto-relocation
            if auto_relocate "$file"; then
                log_action "Guardian auto-cleanup successful"
                
                # Log the action
                echo "$(date '+%Y-%m-%d %H:%M:%S') - ROOT_VIOLATION_CORRECTED: $relative_path" >> "$PROJECT_ROOT/.fswatch/logs/violations.log"
            else
                log_violation "Auto-relocation failed for: $relative_path"
                echo "$(date '+%Y-%m-%d %H:%M:%S') - ROOT_VIOLATION_UNCORRECTED: $relative_path" >> "$PROJECT_ROOT/.fswatch/logs/violations.log"
            fi
        else
            # File is allowed in root
            echo "ℹ️  Authorized root file: $relative_path"
        fi
    fi
}

main "$@"