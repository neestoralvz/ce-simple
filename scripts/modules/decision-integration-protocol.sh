#!/bin/bash
# Decision Integration Protocol - Enhanced Validation and Integration
# Integration layer for intelligent-decision-matrix.sh with handoff-init.sh

# Integration function to replace analyze_complexity in handoff-init.sh
enhanced_complexity_analysis() {
    local conversation_context="$1"
    local debug_mode="${2:-false}"
    
    # Source the intelligent decision matrix
    local script_dir="$(dirname "${BASH_SOURCE[0]}")"
    if [[ -f "$script_dir/intelligent-decision-matrix.sh" ]]; then
        source "$script_dir/intelligent-decision-matrix.sh"
    else
        source scripts/modules/intelligent-decision-matrix.sh
    fi
    
    # Run enhanced analysis
    local analysis_result=$(intelligent_decision_analysis "$conversation_context" "$debug_mode")
    IFS=':' read -r decision confidence level task timeline domain method auth <<< "$analysis_result"
    
    # Authority validation
    local validation_result=$(validate_decision_authority "$decision" "$confidence" "$conversation_context")
    IFS=':' read -r authority_valid validation_msg <<< "$validation_result"
    
    # Enhanced decision refinement based on validation
    if [[ "$authority_valid" == "false" ]]; then
        log_warning "Authority validation failed: $validation_msg"
        # Downgrade decision if authority validation fails
        case "$decision" in
            "phase") decision="handoff" ;;
            "handoff") decision="issue" ;;
            "emergency") 
                if [[ $confidence -lt 85 ]]; then
                    decision="handoff"
                fi
                ;;
        esac
        confidence=$((confidence - 15))  # Reduce confidence for failed validation
    fi
    
    # Apply transformation decision matrix patterns per @context/architecture/patterns/
    if [[ $confidence -gt 85 ]] && [[ "$decision" == "handoff" ]]; then
        # Check for phase promotion based on methodology score
        if [[ $method -gt 70 ]] && [[ $domain -gt 60 ]]; then
            decision="phase"
            log_info "Promoted to phase based on methodology requirements"
        fi
    fi
    
    # Log decision with systematic trace
    log_decision "$analysis_result" "$(echo "$conversation_context" | head -c 200)..."
    
    # Return enhanced result compatible with original format
    echo "$decision:$task:$domain:$((timeline * confidence / 100)):$authority_valid:$(( method > 50 ))"
    
    # Debug output for validation
    if [[ "$debug_mode" == "true" ]]; then
        echo "ENHANCED_ANALYSIS: Decision=$decision, Confidence=$confidence%, Authority=$authority_valid" >&2
        echo "CRITERIA_BREAKDOWN: T=$task, TL=$timeline, D=$domain, M=$method, A=$auth" >&2
    fi
}

# Validation protocol for decision accuracy
validate_decision_accuracy() {
    local decision="$1"
    local confidence="$2"
    local conversation_context="$3"
    local expected_decision="${4:-}"  # Optional for testing
    
    local accuracy_score=0
    local validation_passed=true
    local issues=()
    
    # Validation Rule 1: Confidence threshold alignment
    case "$decision" in
        "emergency")
            if [[ $confidence -lt 85 ]]; then
                issues+=("Emergency decision with low confidence: $confidence%")
                validation_passed=false
            fi
            ;;
        "phase")
            if [[ $confidence -lt 70 ]]; then
                issues+=("Phase decision with insufficient confidence: $confidence%")
                validation_passed=false
            fi
            ;;
        "handoff")
            if [[ $confidence -lt 55 ]]; then
                issues+=("Handoff decision with low confidence: $confidence%")
                validation_passed=false
            fi
            ;;
    esac
    
    # Validation Rule 2: Context alignment check
    if [[ "$decision" == "issue" ]] && echo "$conversation_context" | grep -i -q -E "(system|architecture|framework|methodology)"; then
        issues+=("Issue classification but contains architectural indicators")
        accuracy_score=$((accuracy_score - 10))
    fi
    
    # Validation Rule 3: Emergency override verification
    if [[ "$decision" == "emergency" ]] && ! echo "$conversation_context" | grep -i -q -E "(critical|urgent|emergency|blocking)"; then
        issues+=("Emergency classification without explicit urgency indicators")
        validation_passed=false
    fi
    
    # Calculate accuracy score
    if [[ $validation_passed == true ]]; then
        accuracy_score=$((confidence > 85 ? 95 : confidence + 10))
    else
        accuracy_score=$((confidence - 20))
    fi
    
    # Output validation result
    echo "$validation_passed:$accuracy_score:$(IFS=';'; echo "${issues[*]}")"
}

# Integration test function
test_decision_integration() {
    local test_cases=(
        "emergency:Urgent security vulnerability in authentication system requires immediate fix:85"
        "phase:Complete system architecture migration with multiple frameworks and systematic methodology:75"
        "handoff:Implement user dashboard with backend API and frontend components:65"
        "issue:Fix small CSS styling issue in header component:35"
    )
    
    local total_tests=0
    local passed_tests=0
    
    echo "🧪 Testing Decision Integration Protocol..."
    echo "=========================================="
    
    for test_case in "${test_cases[@]}"; do
        IFS=':' read -r expected context min_confidence <<< "$test_case"
        total_tests=$((total_tests + 1))
        
        # Run enhanced analysis
        local result=$(enhanced_complexity_analysis "$context" true)
        IFS=':' read -r actual_decision task domain timeline authority methodology <<< "$result"
        
        # Extract confidence from detailed analysis
        local detailed_result=$(intelligent_decision_analysis "$context" false)
        local actual_confidence=$(echo "$detailed_result" | cut -d: -f2)
        
        # Validate accuracy
        local validation=$(validate_decision_accuracy "$actual_decision" "$actual_confidence" "$context" "$expected")
        IFS=':' read -r validation_passed accuracy_score validation_issues <<< "$validation"
        
        # Test result
        if [[ "$actual_decision" == "$expected" ]] && [[ $actual_confidence -ge $min_confidence ]]; then
            echo "✅ Test $total_tests: $expected - PASSED (confidence: $actual_confidence%, accuracy: $accuracy_score%)"
            passed_tests=$((passed_tests + 1))
        else
            echo "❌ Test $total_tests: Expected $expected, got $actual_decision (confidence: $actual_confidence%)"
            [[ -n "$validation_issues" ]] && echo "   Issues: $validation_issues"
        fi
    done
    
    local success_rate=$((passed_tests * 100 / total_tests))
    echo "=========================================="
    echo "📊 Test Results: $passed_tests/$total_tests passed ($success_rate% success rate)"
    
    if [[ $success_rate -ge 85 ]]; then
        echo "✅ Integration test PASSED - Meeting >85% accuracy requirement"
        return 0
    else
        echo "❌ Integration test FAILED - Below 85% accuracy requirement"
        return 1
    fi
}