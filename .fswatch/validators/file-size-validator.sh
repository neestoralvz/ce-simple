#!/bin/bash

# File Size Validator
# Enforces 80-line maximum per structural standards

set -euo pipefail

CHANGED_FILE="$1"
LINE_COUNT="$2"
PROJECT_ROOT="/Users/nalve/ce-simple"

# Guardian enforcement logging
log_violation() {
    echo "🛡️ GUARDIAN ENFORCEMENT: $1"
}

log_action() {
    echo "✅ GUARDIAN ACTION: $1"
}

# Check if file should be excluded from size limits
is_excluded() {
    local file="$1"
    
    # Exclude certain file types and locations
    [[ "$file" =~ \.git/ ]] && return 0
    [[ "$file" =~ /logs/ ]] && return 0
    [[ "$file" =~ /archive/ ]] && return 0
    [[ "$file" =~ /scripts/.*analysis_results/ ]] && return 0
    [[ "$file" =~ README\.md$ ]] && return 0
    [[ "$file" =~ CLAUDE\.md$ ]] && return 0
    
    return 1
}

# Check if file needs factorization
needs_factorization() {
    local file="$1"
    local lines="$2"
    
    # Only apply to .md files in specific directories
    [[ "$file" =~ \.md$ ]] || return 1
    [[ "$file" =~ /context/architecture/ ]] && return 0
    [[ "$file" =~ /context/vision/ ]] && return 0
    [[ "$file" =~ /context/handoffs/ ]] && return 0
    
    return 1
}

main() {
    local file="$CHANGED_FILE"
    local lines="$LINE_COUNT"
    
    # Skip if file is excluded
    if is_excluded "$file"; then
        return 0
    fi
    
    # Check if file exceeds 80 lines and needs enforcement
    if [[ $lines -gt 80 ]] && needs_factorization "$file"; then
        log_violation "File exceeds 80-line limit: $file ($lines lines)"
        
        # Create notification for user
        relative_path="${file#$PROJECT_ROOT/}"
        log_violation "STRUCTURAL VIOLATION: $relative_path requires L2-MODULAR factorization"
        log_action "Recommended: Factor into specialized modules per ADR-004 protocol"
        
        # Log to guardian activity
        echo "$(date '+%Y-%m-%d %H:%M:%S') - SIZE_VIOLATION: $relative_path ($lines lines)" >> "$PROJECT_ROOT/.fswatch/logs/violations.log"
        
        # Future enhancement: Could trigger automatic factorization
        # For now, we log and notify
        log_action "Guardian enforcement: User notification generated for manual factorization"
        
    elif [[ $lines -gt 80 ]]; then
        # File exceeds limit but is in excluded category
        echo "ℹ️  File exceeds 80 lines but is excluded from enforcement: $file ($lines lines)"
    fi
}

main "$@"