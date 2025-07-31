#!/bin/bash

# Claude Code Hook: File Size Validation
# Enforces 80-line maximum with context-aware intelligence

set -euo pipefail

# Input parameters
FILE_PATH="${1:-}"
PROJECT_ROOT="/Users/nalve/ce-simple"
LOG_FILE="$PROJECT_ROOT/.claude/hooks/protection.log"
MAX_LINES=80

# Guardian enforcement logging
log_event() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] CLAUDE_HOOK: $1" >> "$LOG_FILE"
}

log_violation() {
    echo "🛡️ GUARDIAN: $1"
    log_event "SIZE_VIOLATION: $1"
}

log_suggestion() {
    echo "💡 SUGGESTION: $1"
    log_event "SUGGESTION: $1"
}

# Check if file path is provided and exists
if [[ -z "$FILE_PATH" || ! -f "$FILE_PATH" ]]; then
    log_event "size-validation.sh: No valid file path provided"
    exit 0
fi

# Only check .md files
if [[ ! "$FILE_PATH" =~ \.md$ ]]; then
    exit 0
fi

# Get file info
RELATIVE_PATH="${FILE_PATH#$PROJECT_ROOT/}"
FILENAME=$(basename "$FILE_PATH")
LINE_COUNT=$(wc -l < "$FILE_PATH" 2>/dev/null || echo "0")

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
    [[ "$file" =~ \.fswatch/ ]] && return 0
    
    return 1
}

# Check if file needs factorization enforcement
needs_enforcement() {
    local file="$1"
    
    # Apply enforcement to architecture and vision files
    [[ "$file" =~ /context/architecture/ ]] && return 0
    [[ "$file" =~ /context/vision/ ]] && return 0
    [[ "$file" =~ /context/handoffs/ ]] && return 0
    
    return 1
}

# Generate context-aware suggestions
generate_suggestions() {
    local file="$1"
    local lines="$2"
    
    echo ""
    echo "📋 FACTORIZATION SUGGESTIONS:"
    
    if [[ "$file" =~ /context/architecture/ ]]; then
        echo "   • Consider L2-MODULAR factorization per ADR-004 protocol"
        echo "   • Extract specialized modules with reference-only architecture"
        echo "   • Use @context/architecture/templates/specialized_directory_template.md"
    elif [[ "$file" =~ /context/vision/ ]]; then
        echo "   • Extract specific vision components to specialized files"
        echo "   • Use reference architecture to maintain authority chain"
        echo "   • Consider vision-specific templates for organization"
    else
        echo "   • Break into logical modules ≤80 lines each"
        echo "   • Use reference-only architecture for cross-references"
        echo "   • Maintain authority chain integrity"
    fi
    
    echo "   • Current size: $lines lines (target: ≤$MAX_LINES lines)"
    echo ""
}

# Main validation logic
if is_excluded "$FILE_PATH"; then
    log_event "File excluded from size validation: $RELATIVE_PATH ($LINE_COUNT lines)"
    exit 0
fi

if [[ $LINE_COUNT -gt $MAX_LINES ]]; then
    if needs_enforcement "$FILE_PATH"; then
        log_violation "File exceeds $MAX_LINES-line limit: $RELATIVE_PATH ($LINE_COUNT lines)"
        
        echo "⚠️ SIZE VIOLATION: $FILENAME exceeds $MAX_LINES-line structural standard"
        generate_suggestions "$FILE_PATH" "$LINE_COUNT"
        
        log_event "SIZE_ENFORCEMENT: $RELATIVE_PATH ($LINE_COUNT lines) - suggestions provided"
        
        # For conversation workflow, we warn but don't block
        # The user can choose to address or continue
        exit 0
        
    else
        log_event "File exceeds limit but not enforced: $RELATIVE_PATH ($LINE_COUNT lines)"
        exit 0
    fi
else
    # File is within limits
    if [[ $LINE_COUNT -gt 60 ]]; then
        log_suggestion "File approaching size limit: $RELATIVE_PATH ($LINE_COUNT/$MAX_LINES lines)"
        echo "ℹ️ Notice: $FILENAME is approaching the $MAX_LINES-line limit ($LINE_COUNT lines)"
    fi
    
    log_event "Size validation passed: $RELATIVE_PATH ($LINE_COUNT lines)"
fi

exit 0