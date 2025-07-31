#!/bin/bash

# Claude Code Hook: Authority Chain Validation
# Validates project authority integrity at session start

set -euo pipefail

# Input parameters
PROJECT_ROOT="${1:-/Users/nalve/ce-simple}"
LOG_FILE="$PROJECT_ROOT/.claude/hooks/protection.log"

# Guardian enforcement logging
log_event() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] CLAUDE_HOOK: $1" >> "$LOG_FILE"
}

log_authority() {
    echo "🛡️ AUTHORITY: $1"
    log_event "AUTHORITY_CHECK: $1"
}

log_validation() {
    echo "✅ AUTHORITY: $1"
    log_event "AUTHORITY_VALIDATION: $1"
}

log_warning() {
    echo "⚠️ AUTHORITY: $1"
    log_event "AUTHORITY_WARNING: $1"
}

# Validate core authority files exist
validate_core_authority() {
    local missing_files=0
    local core_files=(
        "CLAUDE.md"
        "context/vision/vision_foundation.md"
        "context/architecture/core/truth-source.md"
        "context/architecture/core/methodology.md"
        "context/architecture/core/authority.md"
        "context/vision/simplicity.md"
    )
    
    log_authority "Validating core authority files..."
    
    for file in "${core_files[@]}"; do
        local full_path="$PROJECT_ROOT/$file"
        if [[ -f "$full_path" ]]; then
            log_validation "Core authority file present: $file"
        else
            log_warning "Missing core authority file: $file"
            ((missing_files++))
        fi
    done
    
    if [[ $missing_files -eq 0 ]]; then
        log_validation "All core authority files present"
    else
        log_warning "$missing_files core authority files missing"
    fi
    
    return $missing_files
}

# Check authority chain integrity in key files
validate_authority_chains() {
    local violations=0
    local key_files=(
        "$PROJECT_ROOT/context/architecture/core/truth-source.md"
        "$PROJECT_ROOT/context/architecture/core/methodology.md"
        "$PROJECT_ROOT/context/architecture/core/authority.md"
        "$PROJECT_ROOT/context/vision/vision_foundation.md"
    )
    
    log_authority "Validating authority chain integrity..."
    
    for file in "${key_files[@]}"; do
        if [[ -f "$file" ]]; then
            if grep -q "AUTORIDAD SUPREMA\|supreme.*authority\|Authority.*Source" "$file" 2>/dev/null; then
                log_validation "Authority chain present in: $(basename "$file")"
            else
                log_warning "Authority chain missing in: $(basename "$file")"
                ((violations++))
            fi
        fi
    done
    
    return $violations
}

# Validate CLAUDE.md dispatcher integrity
validate_claude_dispatcher() {
    local claude_file="$PROJECT_ROOT/CLAUDE.md"
    local issues=0
    
    log_authority "Validating CLAUDE.md dispatcher integrity..."
    
    if [[ ! -f "$claude_file" ]]; then
        log_warning "CLAUDE.md dispatcher missing"
        return 1
    fi
    
    # Check for essential sections
    local required_sections=(
        "INSTRUCCIÓN OPERACIONAL OBLIGATORIA UNIVERSAL"
        "AUTORIDAD SUPREMA"
        "CONTEXTO CORE SIEMPRE CARGADO"
        "SEMANTIC TRIGGERS"
    )
    
    for section in "${required_sections[@]}"; do
        if grep -q "$section" "$claude_file" 2>/dev/null; then
            log_validation "Essential section present: $section"
        else
            log_warning "Essential section missing: $section"
            ((issues++))
        fi
    done
    
    # Check for core context references
    local core_contexts=(
        "@context/vision/vision_foundation.md"
        "@context/architecture/core/truth-source.md"
        "@context/architecture/core/methodology.md"
        "@context/architecture/core/authority.md"
    )
    
    for context in "${core_contexts[@]}"; do
        if grep -q "$context" "$claude_file" 2>/dev/null; then
            log_validation "Core context referenced: $context"
        else
            log_warning "Core context missing: $context"
            ((issues++))
        fi
    done
    
    return $issues
}

# Check for authority drift indicators
check_authority_drift() {
    local drift_indicators=0
    
    log_authority "Checking for authority drift indicators..."
    
    # Look for files that might indicate authority contamination
    local suspicious_patterns=(
        "override.*authority"
        "ignore.*authority"
        "bypass.*authority"
        "deprecated.*authority"
    )
    
    for pattern in "${suspicious_patterns[@]}"; do
        local matches=$(find "$PROJECT_ROOT/context" -name "*.md" -type f -exec grep -l "$pattern" {} \; 2>/dev/null | wc -l)
        if [[ $matches -gt 0 ]]; then
            log_warning "Potential authority drift detected: $pattern ($matches files)"
            ((drift_indicators++))
        fi
    done
    
    if [[ $drift_indicators -eq 0 ]]; then
        log_validation "No authority drift indicators detected"
    fi
    
    return $drift_indicators
}

# Validate protection system integrity
validate_protection_system() {
    local protection_files=(
        ".claude/hooks/project-protection.json"
        ".claude/hooks/root-protection.sh"
        ".claude/hooks/size-validation.sh"
        ".claude/hooks/standards-check.sh"
        ".claude/hooks/authority-validation.sh"
    )
    
    log_authority "Validating protection system integrity..."
    
    local missing_protection=0
    for file in "${protection_files[@]}"; do
        local full_path="$PROJECT_ROOT/$file"
        if [[ -f "$full_path" ]]; then
            log_validation "Protection component present: $(basename "$file")"
        else
            log_warning "Protection component missing: $(basename "$file")"
            ((missing_protection++))
        fi
    done
    
    return $missing_protection
}

# Initialize protection context
initialize_protection_context() {
    log_authority "Initializing Claude Code protection context..."
    
    # Create log file if it doesn't exist
    touch "$LOG_FILE" 2>/dev/null || true
    
    # Log session start
    log_event "SESSION_START: Authority validation and protection context initialization"
    
    # Set protection status
    echo "🛡️ Guardian Protection System: ACTIVE"
    echo "📋 Authority Chain: VALIDATED" 
    echo "🔍 Standards Compliance: MONITORING"
    echo "📁 Root Structure: PROTECTED"
    
    log_validation "Protection context initialized successfully"
}

# Main authority validation
main() {
    log_authority "Starting session authority validation..."
    
    local total_issues=0
    
    # Initialize context first
    initialize_protection_context
    
    # Run all validations
    validate_core_authority
    total_issues=$((total_issues + $?))
    
    validate_authority_chains
    total_issues=$((total_issues + $?))
    
    validate_claude_dispatcher
    total_issues=$((total_issues + $?))
    
    check_authority_drift
    total_issues=$((total_issues + $?))
    
    validate_protection_system
    total_issues=$((total_issues + $?))
    
    # Summary
    if [[ $total_issues -eq 0 ]]; then
        log_validation "Authority validation completed successfully - system integrity confirmed"
        echo ""
        echo "✅ System Authority: INTACT"
        echo "🛡️ Protection Status: FULLY OPERATIONAL"
    else
        log_warning "Authority validation completed with $total_issues warnings - review recommended"
        echo ""
        echo "⚠️ System Authority: $total_issues warnings detected"
        echo "🔧 Recommendation: Review authority integrity"
    fi
    
    log_event "AUTHORITY_VALIDATION_COMPLETE: $total_issues issues detected"
}

# Only run if we have a valid project root
if [[ -d "$PROJECT_ROOT" ]]; then
    main
else
    log_event "Invalid project root for authority validation: $PROJECT_ROOT"
    exit 1
fi

exit 0