#!/bin/bash

# Claude Code Hook: Standards Compliance Check
# Validates project standards during conversation workflow

set -euo pipefail

# Input parameters
PROJECT_ROOT="${1:-/Users/nalve/ce-simple}"
LOG_FILE="$PROJECT_ROOT/.claude/hooks/protection.log"

# Guardian enforcement logging
log_event() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] CLAUDE_HOOK: $1" >> "$LOG_FILE"
}

log_check() {
    echo "🔍 STANDARDS: $1"
    log_event "STANDARDS_CHECK: $1"
}

log_violation() {
    echo "⚠️ STANDARDS: $1"
    log_event "STANDARDS_VIOLATION: $1"
}

log_suggestion() {
    echo "💡 STANDARDS: $1"
    log_event "STANDARDS_SUGGESTION: $1"
}

# Check for content duplication patterns
check_content_duplication() {
    local violations=0
    
    # Look for potential duplication indicators in recent files
    local recent_files=$(find "$PROJECT_ROOT/context" -name "*.md" -type f -mtime -1 2>/dev/null || true)
    
    for file in $recent_files; do
        if [[ -f "$file" ]] && grep -q "DUPLICATE\|duplicate\|duplicated" "$file" 2>/dev/null; then
            log_violation "Potential content duplication detected in: $(basename "$file")"
            ((violations++))
        fi
        
        # Check for large files with few references (potential duplication)
        if [[ -f "$file" ]]; then
            local line_count=$(wc -l < "$file" 2>/dev/null || echo "0")
            local ref_count=$(grep -c "→\|←\|←→" "$file" 2>/dev/null || echo "0")
            
            if [[ $line_count -gt 80 && $ref_count -lt 3 ]] && [[ ! "$file" =~ /archive/ ]]; then
                log_suggestion "Large file with few references - consider reference architecture: $(basename "$file")"
            fi
        fi
    done
    
    return $violations
}

# Check for enforcement vocabulary in architectural files
check_enforcement_vocabulary() {
    local violations=0
    local arch_files=$(find "$PROJECT_ROOT/context/architecture" "$PROJECT_ROOT/context/vision" -name "*.md" -type f -mtime -1 2>/dev/null || true)
    
    for file in $arch_files; do
        if [[ -f "$file" ]]; then
            local total_lines=$(wc -l < "$file" 2>/dev/null || echo "0")
            local enforcement_lines=$(grep -c "OBLIGATORIO\|SIEMPRE\|NUNCA\|DEBE\|FUNDAMENTAL\|ESENCIAL" "$file" 2>/dev/null || echo "0")
            
            if [[ $total_lines -gt 20 && $enforcement_lines -eq 0 ]]; then
                log_suggestion "Consider adding enforcement vocabulary in: $(basename "$file")"
                log_suggestion "Reference ADR-006 for enforcement vocabulary standards"
            fi
        fi
    done
    
    return $violations
}

# Check for authority chain presence
check_authority_chains() {
    local violations=0
    local arch_files=$(find "$PROJECT_ROOT/context/architecture" "$PROJECT_ROOT/context/vision" -name "*.md" -type f -mtime -1 2>/dev/null || true)
    
    for file in $arch_files; do
        if [[ -f "$file" ]] && ! grep -q "AUTORIDAD SUPREMA\|Authority\|authority" "$file" 2>/dev/null; then
            log_suggestion "Consider adding authority chain in: $(basename "$file")"
            ((violations++))
        fi
    done
    
    return $violations
}

# Check reference architecture compliance
check_reference_architecture() {
    local violations=0
    
    # Check for potential DRY violations
    local potential_duplicates=$(find "$PROJECT_ROOT/context" -name "*.md" -type f -exec grep -l "# .*README\|# .*Template" {} \; 2>/dev/null | wc -l)
    
    if [[ $potential_duplicates -gt 10 ]]; then
        log_suggestion "Multiple files with similar headers - verify reference architecture compliance"
    fi
    
    return $violations
}

# Main standards check
main() {
    log_check "Starting pre-conversation standards validation"
    
    local total_violations=0
    
    # Run all checks
    check_content_duplication
    total_violations=$((total_violations + $?))
    
    check_enforcement_vocabulary
    total_violations=$((total_violations + $?))
    
    check_authority_chains
    total_violations=$((total_violations + $?))
    
    check_reference_architecture
    total_violations=$((total_violations + $?))
    
    # Summary
    if [[ $total_violations -eq 0 ]]; then
        log_check "Standards validation completed - no violations detected"
    else
        log_check "Standards validation completed - $total_violations suggestions provided"
        echo "📋 Review suggestions above for standards compliance optimization"
    fi
    
    log_event "STANDARDS_CHECK_COMPLETE: $total_violations suggestions generated"
}

# Only run if we have a valid project root
if [[ -d "$PROJECT_ROOT" ]]; then
    main
else
    log_event "Invalid project root: $PROJECT_ROOT"
    exit 0
fi

exit 0