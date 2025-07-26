#!/bin/bash

# Implementation Verification Mandatory Script
# Based on user-input/technical-requirements/implementation-verification-mandatory-user.md
# Authority: MANDATORY - Cannot be bypassed

set -e

echo "=== VDD MANDATORY IMPLEMENTATION VERIFICATION ==="
echo "Authority: user-input/technical-requirements/implementation-verification-mandatory-user.md"
echo "Status: MANDATORY - Cannot be bypassed"
echo

# Function to check if verification type is needed
check_verification_type() {
    local verification_type=$1
    echo "🔍 Checking if $verification_type verification is needed..."
    
    case $verification_type in
        "pre-implementation")
            echo "ℹ️  Pre-Implementation verification requested"
            return 0
            ;;
        "during-implementation")
            echo "ℹ️  During-Implementation checkpoint requested"
            return 0
            ;;
        "post-implementation")
            echo "ℹ️  Post-Implementation validation requested"
            return 0
            ;;
        "handoff")
            echo "ℹ️  Handoff verification requested"
            return 0
            ;;
        *)
            echo "❌ Unknown verification type: $verification_type"
            return 1
            ;;
    esac
}

# Function to run coherence validation as part of verification
run_coherence_validation() {
    echo "🔍 Running System Coherence Validation..."
    if [ -f "./tools/scripts/validate-coherence.sh" ]; then
        ./tools/scripts/validate-coherence.sh
        if [ $? -eq 0 ]; then
            echo "✅ Coherence validation passed"
            return 0
        else
            echo "❌ Coherence validation FAILED"
            return 1
        fi
    else
        echo "⚠️  Coherence validation script not found"
        return 1
    fi
}

# Pre-Implementation Verification
verify_pre_implementation() {
    echo "=== PRE-IMPLEMENTATION VERIFICATION (MANDATORY) ==="
    echo "ALL items must be checked before implementation can proceed"
    echo
    
    local failures=0
    
    echo "A. Scope Definition Verification"
    echo "-------------------------------"
    
    # Check for clear objective definition
    echo "Checking for clear objective definition..."
    if [ -f "CLAUDE.md" ] && grep -q "Section" CLAUDE.md; then
        echo "✅ Clear objective definition found in CLAUDE.md"
    else
        echo "❌ Clear objective definition NOT FOUND"
        failures=$((failures + 1))
    fi
    
    # Check for success criteria
    echo "Checking for success criteria..."
    if find . -name "*.md" -exec grep -l "Success\|success\|criteria\|metric" {} \; | head -1 > /dev/null; then
        echo "✅ Success criteria defined in documentation"
    else
        echo "❌ Success criteria NOT DEFINED"
        failures=$((failures + 1))
    fi
    
    echo
    echo "B. Authority Alignment Verification"
    echo "-----------------------------------"
    
    # Check user vision compliance
    if [ -f "user-input/vision/core-mission-concept.md" ]; then
        echo "✅ User vision file exists for alignment check"
    else
        echo "❌ User vision file MISSING"
        failures=$((failures + 1))
    fi
    
    # Check technical requirements
    if [ -d "user-input/technical-requirements" ]; then
        echo "✅ Technical requirements directory exists"
    else
        echo "❌ Technical requirements MISSING"
        failures=$((failures + 1))
    fi
    
    # Check PTS Framework availability
    if [ -f "docs/core/pts-framework-consolidated.md" ]; then
        echo "✅ PTS Framework available for compliance"
    else
        echo "❌ PTS Framework NOT AVAILABLE"
        failures=$((failures + 1))
    fi
    
    echo
    echo "C. Implementation Plan Verification"
    echo "-----------------------------------"
    
    # Check for step-by-step breakdown (TodoWrite tool usage)
    if command -v git >/dev/null && git log --oneline -1 | grep -q "todo\|Todo\|step\|Step"; then
        echo "✅ Implementation steps tracking detected"
    else
        echo "⚠️  Implementation steps tracking not clearly evident"
    fi
    
    echo
    if [ $failures -eq 0 ]; then
        echo "🎉 PRE-IMPLEMENTATION VERIFICATION PASSED"
        echo "Implementation may proceed"
        return 0
    else
        echo "❌ PRE-IMPLEMENTATION VERIFICATION FAILED ($failures failures)"
        echo "❌ IMPLEMENTATION BLOCKED - Re-planning required"
        return 1
    fi
}

# Post-Implementation Validation
verify_post_implementation() {
    echo "=== POST-IMPLEMENTATION VALIDATION (MANDATORY) ==="
    echo "ALL items must pass before work can be considered complete"
    echo
    
    local failures=0
    
    echo "A. Completeness Verification"
    echo "----------------------------"
    
    # Run coherence validation
    echo "Running coherence validation as part of completeness check..."
    if run_coherence_validation; then
        echo "✅ System coherence maintained"
    else
        echo "❌ System coherence BROKEN"
        failures=$((failures + 1))
    fi
    
    echo
    echo "B. System Integrity Verification"
    echo "--------------------------------"
    
    # Check PTS compliance in commands
    if [ -d "commands" ]; then
        pts_failures=0
        for cmd in commands/*.md; do
            if [ -f "$cmd" ]; then
                # Check for Task Tool references
                if ! grep -q "Task Tool" "$cmd"; then
                    echo "❌ $cmd missing Task Tool parallelization"
                    pts_failures=$((pts_failures + 1))
                fi
                
                # Check for external references
                if grep -q "\.\./\|@.*\.md" "$cmd"; then
                    echo "❌ $cmd contains external references"
                    pts_failures=$((pts_failures + 1))
                fi
                
                # Check for step count (Directness)
                step_count=$(grep -c "### Step [0-9]" "$cmd" || echo "0")
                if [ "$step_count" -gt 3 ]; then
                    echo "❌ $cmd violates Directness (>3 steps)"
                    pts_failures=$((pts_failures + 1))
                fi
            fi
        done
        
        if [ $pts_failures -eq 0 ]; then
            echo "✅ All commands pass PTS compliance"
        else
            echo "❌ PTS compliance failures detected ($pts_failures)"
            failures=$((failures + 1))
        fi
    fi
    
    echo
    echo "C. Documentation & Knowledge Transfer"
    echo "------------------------------------"
    
    # Check for git commit (knowledge capture)
    if command -v git >/dev/null && git status --porcelain | grep -q "^[MADRCU]"; then
        echo "⚠️  Uncommitted changes detected - commit to capture knowledge"
    else
        echo "✅ Working directory clean - changes committed"
    fi
    
    echo
    if [ $failures -eq 0 ]; then
        echo "🎉 POST-IMPLEMENTATION VALIDATION PASSED"
        echo "Work is COMPLETE and verified"
        return 0
    else
        echo "❌ POST-IMPLEMENTATION VALIDATION FAILED ($failures failures)"
        echo "❌ WORK IS NOT COMPLETE - Return to implementation phase"
        return 1
    fi
}

# Handoff Verification Protocol
verify_handoff() {
    echo "=== HANDOFF VERIFICATION PROTOCOL (MANDATORY) ==="
    echo "ALL items must be verified before handoff can proceed"
    echo
    
    local failures=0
    
    echo "A. State Transfer Verification"
    echo "------------------------------"
    
    # Check for current state documentation
    if [ -f "CLAUDE.md" ]; then
        echo "✅ CLAUDE.md exists for state documentation"
    else
        echo "❌ CLAUDE.md MISSING for state transfer"
        failures=$((failures + 1))
    fi
    
    # Check for work documentation in git
    if command -v git >/dev/null; then
        recent_commits=$(git log --oneline -5 | wc -l)
        if [ "$recent_commits" -gt 0 ]; then
            echo "✅ Recent work documented in git history ($recent_commits commits)"
        else
            echo "❌ No recent work documentation found"
            failures=$((failures + 1))
        fi
    fi
    
    echo
    echo "B. Knowledge Transfer Verification"
    echo "----------------------------------"
    
    # Check for technical details in documentation
    if find . -name "*.md" -exec grep -l "implementation\|technical\|decision" {} \; | head -1 > /dev/null; then
        echo "✅ Technical details documented"
    else
        echo "❌ Technical details NOT DOCUMENTED"
        failures=$((failures + 1))
    fi
    
    echo
    if [ $failures -eq 0 ]; then
        echo "🎉 HANDOFF VERIFICATION PASSED"
        echo "Handoff may proceed safely"
        return 0
    else
        echo "❌ HANDOFF VERIFICATION FAILED ($failures failures)"
        echo "❌ HANDOFF BLOCKED - Resolve gaps before transition"
        return 1
    fi
}

# Main execution
main() {
    local verification_type=${1:-"post-implementation"}
    
    if ! check_verification_type "$verification_type"; then
        echo "Usage: $0 [pre-implementation|during-implementation|post-implementation|handoff]"
        exit 1
    fi
    
    case $verification_type in
        "pre-implementation")
            verify_pre_implementation
            ;;
        "post-implementation")
            verify_post_implementation
            ;;
        "handoff")
            verify_handoff
            ;;
        "during-implementation")
            echo "During-implementation checkpoints should be run as part of development workflow"
            echo "Running basic coherence validation as checkpoint..."
            run_coherence_validation
            ;;
        *)
            echo "❌ Unknown verification type"
            exit 1
            ;;
    esac
    
    verification_result=$?
    
    if [ $verification_result -eq 0 ]; then
        echo
        echo "✅ MANDATORY VERIFICATION SUCCESSFUL"
        echo "Authority: implementation-verification-mandatory-user.md"
    else
        echo
        echo "❌ MANDATORY VERIFICATION FAILED"
        echo "❌ GAP DETECTION TRIGGERED"
        echo "❌ AUTOMATIC RE-PLANNING REQUIRED"
        echo "Authority: implementation-verification-mandatory-user.md"
        exit 1
    fi
}

# Execute main function with all arguments
main "$@"