# Core Prevention Principles - Foundation Framework

**31/07/2025 CDMX** | Core principles for auto-completion bug prevention

## AUTORIDAD SUPREMA
prevention-framework-hub.md → core-prevention-principles.md implements foundation principles per hub authority

## CORE PREVENTION PRINCIPLES

### **Fundamental Principles Framework**
1. **Never Auto-Complete Complex Work**: Handoffs, phases, and complex tasks require manual validation
2. **Objective Criteria Only**: Auto-completion limited to measurable, binary criteria
3. **Explicit Pattern Matching**: Use specific patterns, avoid broad wildcards
4. **Default to Manual**: Unknown or ambiguous patterns default to manual validation
5. **Comprehensive Logging**: All auto-completion decisions must be logged with evidence

### **Implementation Safety Guidelines**
```bash
# Guidelines for safe auto-completion implementation
implement_safe_auto_completion() {
    # Guideline 1: Define explicit criteria
    define_objective_completion_criteria "$work_item"
    
    # Guideline 2: Implement explicit rejection for complex items
    if is_complex_work_item "$work_item"; then
        require_manual_validation "$work_item"
        return 1
    fi
    
    # Guideline 3: Use whitelist approach
    if ! is_whitelisted_for_auto_completion "$work_item"; then
        log_completion_decision "$work_item" "NOT_WHITELISTED" "Manual validation required"
        return 1
    fi
    
    # Guideline 4: Collect and validate evidence
    local evidence=$(collect_completion_evidence "$work_item")
    if ! validate_evidence "$evidence"; then
        log_completion_decision "$work_item" "INSUFFICIENT_EVIDENCE" "$evidence"
        return 1
    fi
    
    # Guideline 5: Log successful completion
    log_completion_decision "$work_item" "APPROVED" "All criteria satisfied: $evidence"
    return 0
}
```

### **Anti-Pattern Prevention**
```bash
# Patterns to avoid in auto-completion logic
avoid_dangerous_patterns() {
    # NEVER use broad wildcards
    # BAD: case "$item" in "H"*) return 0 ;;
    # GOOD: Explicit whitelist with objective criteria
    
    # NEVER assume completion without evidence
    # BAD: return 0  # Assume complete
    # GOOD: validate_objective_evidence "$item"
    
    # NEVER auto-complete unknown items
    # BAD: *) return 0 ;;  # Default to complete
    # GOOD: *) require_manual_validation ;;
}
```

## INTEGRATION REFERENCES
**Authority Source**: ← prevention-framework-hub.md (core principles authority)
**Implementation**: → implementation-guidelines.md (detailed implementation)
**Quality Gates**: → quality-gates.md (validation framework)

---
**CORE PRINCIPLES DECLARATION**: Foundation prevention principles providing systematic safety framework for auto-completion implementation with comprehensive guidelines and anti-pattern prevention.