#!/bin/bash

# Standards Validator
# Enforces project standards and best practices

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

# Check for content duplication
check_content_duplication() {
    local file="$1"
    
    # Only check .md files
    [[ "$file" =~ \.md$ ]] || return 0
    
    # Skip certain directories
    [[ "$file" =~ /archive/ ]] && return 0
    [[ "$file" =~ /logs/ ]] && return 0
    
    # Check for potential duplication indicators
    if grep -q "DUPLICATE\|duplicate\|duplicated" "$file" 2>/dev/null; then
        log_violation "Potential content duplication detected in: $(basename "$file")"
    fi
    
    # Check for reference-only compliance
    local line_count=$(wc -l < "$file" 2>/dev/null || echo "0")
    local ref_count=$(grep -c "→\|←\|←→" "$file" 2>/dev/null || echo "0")
    
    # If file is large but has few references, might indicate duplication
    if [[ $line_count -gt 80 && $ref_count -lt 3 ]]; then
        log_violation "Large file with few references - potential duplication: $(basename "$file")"
        log_action "Consider reference architecture migration per ADR-005"
    fi
}

# Check for enforcement vocabulary
check_enforcement_vocabulary() {
    local file="$1"
    
    # Only check .md files in specific directories
    [[ "$file" =~ \.md$ ]] || return 0
    [[ "$file" =~ /context/architecture/|/context/vision/ ]] || return 0
    
    # Check for enforcement vocabulary density
    local total_lines=$(wc -l < "$file" 2>/dev/null || echo "0")
    local enforcement_lines=$(grep -c "OBLIGATORIO\|SIEMPRE\|NUNCA\|DEBE\|FUNDAMENTAL\|ESENCIAL" "$file" 2>/dev/null || echo "0")
    
    if [[ $total_lines -gt 20 && $enforcement_lines -eq 0 ]]; then
        log_violation "Missing enforcement vocabulary in architectural file: $(basename "$file")"
        log_action "Consider adding enforcement vocabulary per ADR-006"
    fi
}

# Check for authority chain
check_authority_chain() {
    local file="$1"
    
    # Only check .md files in specific directories
    [[ "$file" =~ \.md$ ]] || return 0
    [[ "$file" =~ /context/architecture/|/context/vision/ ]] || return 0
    
    # Check for authority chain presence
    if ! grep -q "AUTORIDAD SUPREMA\|Authority\|authority" "$file" 2>/dev/null; then
        log_violation "Missing authority chain in: $(basename "$file")"
        log_action "Add authority chain per project standards"
    fi
}

main() {
    local file="$CHANGED_FILE"
    
    # Skip if file doesn't exist
    [[ -f "$file" ]] || return 0
    
    # Run various standards checks
    check_content_duplication "$file"
    check_enforcement_vocabulary "$file"
    check_authority_chain "$file"
    
    # Log standards check completion
    echo "ℹ️  Standards validation completed for: $(basename "$file")"
}

main "$@"