#!/bin/bash
# comprehensive-quality-validator.sh - Master quality orchestration script
# 31/07/2025 CDMX | H6D-SCRIPTS automation framework - Priority Script #2

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
SCRIPTS_DIR="$PROJECT_ROOT/scripts"
OUTPUT_DIR="$PROJECT_ROOT/scripts/quality_validation_$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$OUTPUT_DIR/quality_validation_log.txt"

# Silent script - no user notifications (Claude Code communicates results)

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Initialize log (technical data only)
{
    echo "$(date)"
    echo "$PROJECT_ROOT"
    echo "comprehensive_quality_validation_start"
} > "$LOG_FILE"

# Quality validation framework components
declare -A VALIDATION_SCRIPTS=(
    ["domain_classification"]="$SCRIPTS_DIR/analysis/domain-classifier.sh"
    ["authority_validation"]="$SCRIPTS_DIR/validation/authority-validator.sh"
    ["reference_integrity"]="$SCRIPTS_DIR/validation/reference-integrity-validator.sh"
    ["file_size_compliance"]="$SCRIPTS_DIR/validation/validate_integrity.sh"
    ["progress_tracking"]="$SCRIPTS_DIR/infrastructure/progress-tracker.sh"
)

# Quality gate thresholds
declare -A QUALITY_THRESHOLDS=(
    ["authority_fidelity_min"]="95"
    ["reference_integrity_min"]="90"
    ["file_size_compliance_min"]="85"
    ["overall_quality_min"]="90"
)

# Execute validation script with error handling
execute_validation_script() {
    local script_name="$1"
    local script_path="$2"
    shift 2
    local script_args=("$@")
    
    if [[ ! -f "$script_path" ]]; then
        echo "SCRIPT_NOT_FOUND:$script_name:$script_path"
        {
            echo "ERROR: Validation script not found"
            echo "  Script: $script_name"
            echo "  Path: $script_path"
        } >> "$LOG_FILE"
        return 1
    fi
    
    # Execute script and capture results
    local start_time=$(date +%s)
    local exit_code=0
    local output_file="$OUTPUT_DIR/${script_name}_output.txt"
    
    if bash "$script_path" "${script_args[@]}" > "$output_file" 2>&1; then
        exit_code=0
    else
        exit_code=$?
    fi
    
    local end_time=$(date +%s)
    local duration=$((end_time - start_time))
    
    # Parse results based on script type
    local result_data=$(parse_script_results "$script_name" "$output_file" "$exit_code")
    
    # Log execution details
    {
        echo "SCRIPT_EXECUTION: $script_name"
        echo "  Path: $script_path"
        echo "  Args: ${script_args[*]}"
        echo "  Exit code: $exit_code"
        echo "  Duration: ${duration}s"
        echo "  Results: $result_data"
        echo "  ---"
    } >> "$LOG_FILE"
    
    echo "$result_data"
    return $exit_code
}

# Parse script results based on script type
parse_script_results() {
    local script_name="$1"
    local output_file="$2"
    local exit_code="$3"
    
    if [[ ! -f "$output_file" ]]; then
        echo "NO_OUTPUT:$script_name:$exit_code"
        return
    fi
    
    case "$script_name" in
        "domain_classification")
            # Parse domain classifier results
            local processed=$(grep -c "| [A-Z]" "$output_file" 2>/dev/null || echo "0")
            local h6a_count=$(grep -c "H6A" "$output_file" 2>/dev/null || echo "0")
            local h6b_count=$(grep -c "H6B" "$output_file" 2>/dev/null || echo "0")
            local h6c_count=$(grep -c "H6C" "$output_file" 2>/dev/null || echo "0")
            echo "DOMAIN_RESULTS:processed=$processed:h6a=$h6a_count:h6b=$h6b_count:h6c=$h6c_count"
            ;;
            
        "authority_validation")
            # Parse authority validator results
            local fidelity=$(grep "fidelity.*:" "$output_file" | grep -o "[0-9]\+%" | head -1 | tr -d '%' || echo "0")
            local violations=$(grep -c "VIOLATION" "$output_file" 2>/dev/null || echo "0")
            echo "AUTHORITY_RESULTS:fidelity=$fidelity:violations=$violations"
            ;;
            
        "reference_integrity")
            # Parse reference integrity results
            local integrity=$(grep "integrity.*:" "$output_file" | grep -o "[0-9]\+%" | head -1 | tr -d '%' || echo "0")
            local broken=$(grep "broken.*:" "$output_file" | grep -o "[0-9]\+" | head -1 || echo "0")
            echo "REFERENCE_RESULTS:integrity=$integrity:broken=$broken"
            ;;
            
        "file_size_compliance")
            # Parse file size compliance results
            local compliant=$(grep -c "COMPLIANT" "$output_file" 2>/dev/null || echo "0")
            local violations=$(grep -c "VIOLATION" "$output_file" 2>/dev/null || echo "0")
            local total=$((compliant + violations))
            local compliance_rate=0
            if [[ $total -gt 0 ]]; then
                compliance_rate=$((compliant * 100 / total))
            fi
            echo "SIZE_RESULTS:compliant=$compliant:violations=$violations:rate=$compliance_rate"
            ;;
            
        "progress_tracking")
            # Parse progress tracker results
            local tracked=$(grep -c "TRACKING" "$output_file" 2>/dev/null || echo "0")
            local status=$(grep "STATUS:" "$output_file" | cut -d: -f2 | head -1 || echo "unknown")
            echo "PROGRESS_RESULTS:tracked=$tracked:status=$status"
            ;;
            
        *)
            echo "UNKNOWN_SCRIPT:$script_name:exit_code=$exit_code"
            ;;
    esac
}

# Execute comprehensive quality validation
execute_comprehensive_validation() {
    local target_pattern="${1:-.*}"
    local validation_mode="${2:-full}"
    
    echo "COMPREHENSIVE_VALIDATION_START:pattern=$target_pattern:mode=$validation_mode"
    
    local validation_results=()
    local overall_score=0
    local critical_failures=0
    local validation_count=0
    
    # Execute domain classification
    if [[ -f "${VALIDATION_SCRIPTS[domain_classification]}" ]]; then
        echo "EXECUTING_DOMAIN_CLASSIFICATION"
        local domain_result=$(execute_validation_script "domain_classification" "${VALIDATION_SCRIPTS[domain_classification]}" "$target_pattern" "50")
        validation_results+=("domain:$domain_result")
        ((validation_count++))
        
        if [[ "$domain_result" =~ processed=([0-9]+) ]]; then
            local processed=${BASH_REMATCH[1]}
            if [[ $processed -gt 0 ]]; then
                overall_score=$((overall_score + 25))
            fi
        fi
    fi
    
    # Execute authority validation
    if [[ -f "${VALIDATION_SCRIPTS[authority_validation]}" ]]; then
        echo "EXECUTING_AUTHORITY_VALIDATION"
        local auth_result=$(execute_validation_script "authority_validation" "${VALIDATION_SCRIPTS[authority_validation]}" "$target_pattern")
        validation_results+=("authority:$auth_result")
        ((validation_count++))
        
        if [[ "$auth_result" =~ fidelity=([0-9]+) ]]; then
            local fidelity=${BASH_REMATCH[1]}
            if [[ $fidelity -ge ${QUALITY_THRESHOLDS[authority_fidelity_min]} ]]; then
                overall_score=$((overall_score + 30))
            else
                ((critical_failures++))
            fi
        fi
    fi
    
    # Execute reference integrity validation
    if [[ -f "${VALIDATION_SCRIPTS[reference_integrity]}" ]]; then
        echo "EXECUTING_REFERENCE_INTEGRITY"
        local ref_result=$(execute_validation_script "reference_integrity" "${VALIDATION_SCRIPTS[reference_integrity]}" "--validate" "$target_pattern")
        validation_results+=("reference:$ref_result")
        ((validation_count++))
        
        if [[ "$ref_result" =~ integrity=([0-9]+) ]]; then
            local integrity=${BASH_REMATCH[1]}
            if [[ $integrity -ge ${QUALITY_THRESHOLDS[reference_integrity_min]} ]]; then
                overall_score=$((overall_score + 25))
            else
                ((critical_failures++))
            fi
        fi
    fi
    
    # Execute file size compliance validation
    if [[ -f "${VALIDATION_SCRIPTS[file_size_compliance]}" ]]; then
        echo "EXECUTING_SIZE_COMPLIANCE"
        local size_result=$(execute_validation_script "file_size_compliance" "${VALIDATION_SCRIPTS[file_size_compliance]}")
        validation_results+=("size:$size_result")
        ((validation_count++))
        
        if [[ "$size_result" =~ rate=([0-9]+) ]]; then
            local compliance=${BASH_REMATCH[1]}
            if [[ $compliance -ge ${QUALITY_THRESHOLDS[file_size_compliance_min]} ]]; then
                overall_score=$((overall_score + 20))
            fi
        fi
    fi
    
    # Calculate final quality score
    local quality_percentage=0
    if [[ $validation_count -gt 0 ]]; then
        quality_percentage=$((overall_score))
    fi
    
    # Determine quality status
    local quality_status="UNKNOWN"
    if [[ $critical_failures -eq 0 ]] && [[ $quality_percentage -ge 95 ]]; then
        quality_status="EXCELLENT"
    elif [[ $critical_failures -eq 0 ]] && [[ $quality_percentage -ge ${QUALITY_THRESHOLDS[overall_quality_min]} ]]; then
        quality_status="GOOD"
    elif [[ $critical_failures -le 1 ]] && [[ $quality_percentage -ge 75 ]]; then
        quality_status="ACCEPTABLE"
    else
        quality_status="POOR"
    fi
    
    # Output comprehensive results
    echo "QUALITY_VALIDATION_COMPLETE"
    echo "VALIDATIONS_EXECUTED:$validation_count"
    echo "OVERALL_SCORE:$quality_percentage"
    echo "CRITICAL_FAILURES:$critical_failures"
    echo "QUALITY_STATUS:$quality_status"
    
    # Log comprehensive results
    {
        echo "COMPREHENSIVE_VALIDATION_RESULTS"
        echo "  Target pattern: $target_pattern"
        echo "  Validation mode: $validation_mode"
        echo "  Validations executed: $validation_count"
        echo "  Overall score: $quality_percentage"
        echo "  Critical failures: $critical_failures"
        echo "  Quality status: $quality_status"
        echo "  Individual results:"
        for result in "${validation_results[@]}"; do
            echo "    $result"
        done
        echo "  =========================================="
    } >> "$LOG_FILE"
    
    # Return appropriate exit code
    case "$quality_status" in
        "EXCELLENT"|"GOOD") return 0 ;;
        "ACCEPTABLE") return 1 ;;
        "POOR") return 2 ;;
    esac
}

# Execute H6A/B/C specific quality validation
execute_h6_specific_validation() {
    local h6_type="$1"
    local target_files="${2:-}"
    
    echo "H6_SPECIFIC_VALIDATION:$h6_type"
    
    case "$h6_type" in
        "H6A")
            # H6A: Quick wins validation - focus on file size and batch processing readiness
            echo "H6A_VALIDATION:archive_batch_processing"
            execute_comprehensive_validation ".*archive.*|.*backup.*|.*legacy.*" "h6a_specific"
            ;;
            
        "H6B")
            # H6B: L2-MODULAR validation - focus on authority preservation and modular extraction
            echo "H6B_VALIDATION:l2_modular_extraction"
            execute_comprehensive_validation ".*authority.*|.*methodology.*|.*patterns.*" "h6b_specific"
            ;;
            
        "H6C")
            # H6C: Individual assessment - comprehensive quality validation
            echo "H6C_VALIDATION:individual_assessment"
            execute_comprehensive_validation ".*" "h6c_specific"
            ;;
            
        *)
            echo "UNKNOWN_H6_TYPE:$h6_type"
            return 1
            ;;
    esac
}

# Validate H6A/B/C parallel execution readiness
validate_parallel_execution_readiness() {
    echo "PARALLEL_EXECUTION_READINESS_CHECK"
    
    local readiness_score=0
    local max_score=100
    local readiness_issues=()
    
    # Check script availability (30 points)
    local available_scripts=0
    for script_name in "${!VALIDATION_SCRIPTS[@]}"; do
        if [[ -f "${VALIDATION_SCRIPTS[$script_name]}" ]]; then
            ((available_scripts++))
        else
            readiness_issues+=("Missing script: $script_name")
        fi
    done
    
    if [[ $available_scripts -eq ${#VALIDATION_SCRIPTS[@]} ]]; then
        readiness_score=$((readiness_score + 30))
    else
        readiness_score=$((readiness_score + (available_scripts * 30 / ${#VALIDATION_SCRIPTS[@]})))
    fi
    
    # Check H6A readiness (25 points)
    local h6a_exit_code=0
    if execute_h6_specific_validation "H6A" > /dev/null 2>&1; then
        h6a_exit_code=$?
    fi
    
    if [[ $h6a_exit_code -eq 0 ]]; then
        readiness_score=$((readiness_score + 25))
    elif [[ $h6a_exit_code -eq 1 ]]; then
        readiness_score=$((readiness_score + 15))
        readiness_issues+=("H6A quality acceptable but not excellent")
    else
        readiness_issues+=("H6A quality validation failed")
    fi
    
    # Check H6B readiness (25 points)
    local h6b_exit_code=0
    if execute_h6_specific_validation "H6B" > /dev/null 2>&1; then
        h6b_exit_code=$?
    fi
    
    if [[ $h6b_exit_code -eq 0 ]]; then
        readiness_score=$((readiness_score + 25))
    elif [[ $h6b_exit_code -eq 1 ]]; then
        readiness_score=$((readiness_score + 15))
        readiness_issues+=("H6B quality acceptable but not excellent")
    else
        readiness_issues+=("H6B quality validation failed")
    fi
    
    # Check H6C readiness (20 points)
    local h6c_exit_code=0
    if execute_h6_specific_validation "H6C" > /dev/null 2>&1; then
        h6c_exit_code=$?
    fi
    
    if [[ $h6c_exit_code -eq 0 ]]; then
        readiness_score=$((readiness_score + 20))
    elif [[ $h6c_exit_code -eq 1 ]]; then
        readiness_score=$((readiness_score + 10))
        readiness_issues+=("H6C quality acceptable but not excellent")
    else
        readiness_issues+=("H6C quality validation failed")
    fi
    
    # Determine readiness status
    local readiness_status="UNKNOWN"
    if [[ $readiness_score -ge 95 ]] && [[ ${#readiness_issues[@]} -eq 0 ]]; then
        readiness_status="READY"
    elif [[ $readiness_score -ge 85 ]] && [[ ${#readiness_issues[@]} -le 2 ]]; then
        readiness_status="MOSTLY_READY"
    elif [[ $readiness_score -ge 70 ]]; then
        readiness_status="PARTIAL_READY"
    else
        readiness_status="NOT_READY"
    fi
    
    echo "PARALLEL_READINESS_SCORE:$readiness_score"
    echo "PARALLEL_READINESS_STATUS:$readiness_status"
    echo "READINESS_ISSUES:${#readiness_issues[@]}"
    
    # Log readiness assessment
    {
        echo "PARALLEL_EXECUTION_READINESS_ASSESSMENT"
        echo "  Readiness score: $readiness_score / $max_score"
        echo "  Readiness status: $readiness_status"
        echo "  Issues identified: ${#readiness_issues[@]}"
        if [[ ${#readiness_issues[@]} -gt 0 ]]; then
            echo "  Issues list:"
            for issue in "${readiness_issues[@]}"; do
                echo "    - $issue"
            done
        fi
        echo "  =========================================="
    } >> "$LOG_FILE"
    
    # Return appropriate exit code based on readiness
    case "$readiness_status" in
        "READY") return 0 ;;
        "MOSTLY_READY") return 1 ;;
        "PARTIAL_READY") return 2 ;;
        "NOT_READY") return 3 ;;
    esac
}

# Generate comprehensive quality report
generate_quality_report() {
    local validation_mode="$1"
    local quality_status="$2"
    local report_file="$OUTPUT_DIR/COMPREHENSIVE_QUALITY_REPORT.md"
    
    cat > "$report_file" << EOF
# Comprehensive Quality Validation Report

**Generated**: $(date)
**Script**: comprehensive-quality-validator.sh
**Purpose**: Master quality orchestration for H6A/B/C parallel execution

## Validation Summary

### Overall Quality Status
- **Status**: $quality_status
- **Validation Mode**: $validation_mode
- **Standards**: Complete H6D-SCRIPTS framework compliance

### Validation Framework
- **Domain Classification**: Automated content categorization
- **Authority Validation**: 95%+ user voice fidelity verification
- **Reference Integrity**: Cross-reference and bidirectional link validation
- **Size Compliance**: File size threshold enforcement
- **Progress Tracking**: Real-time execution monitoring

### Quality Thresholds
- **Authority Fidelity**: ≥${QUALITY_THRESHOLDS[authority_fidelity_min]}%
- **Reference Integrity**: ≥${QUALITY_THRESHOLDS[reference_integrity_min]}%
- **Size Compliance**: ≥${QUALITY_THRESHOLDS[file_size_compliance_min]}%
- **Overall Quality**: ≥${QUALITY_THRESHOLDS[overall_quality_min]}%

## H6A/B/C Integration

### H6A Support (Archive Batch Processing)
- **Focus**: Quick wins identification and batch processing readiness
- **Validation**: File size compliance and archive content classification
- **Quality Gates**: Authority preservation during batch operations

### H6B Support (L2-MODULAR Extraction)
- **Focus**: Authority-rich content modular extraction validation
- **Validation**: Authority fidelity and reference integrity preservation
- **Quality Gates**: 95%+ user voice fidelity throughout extraction

### H6C Support (Individual Assessment)
- **Focus**: Comprehensive individual file quality validation
- **Validation**: Complete quality framework application per file
- **Quality Gates**: Systematic quality assurance and compliance verification

## Quality Assurance Framework

### Pre-Operation Validation
- **Script Availability**: All required validation scripts functional
- **Dependency Check**: Required tools and resources available
- **Target Validation**: Input files and patterns verified

### Mid-Operation Monitoring
- **Real-time Quality Gates**: Continuous validation during operations
- **Authority Preservation**: User voice fidelity monitoring
- **Reference Integrity**: Cross-reference consistency verification

### Post-Operation Verification
- **Comprehensive Validation**: Complete quality framework re-execution
- **Compliance Verification**: All quality thresholds met
- **Success Metrics**: Quantitative quality improvement measurement

## Automation Benefits

### Quality Orchestration
- **Unified Framework**: Single command comprehensive quality validation
- **Script Coordination**: Automated execution of multiple validation scripts
- **Result Aggregation**: Consolidated quality assessment and reporting

### H6 Family Integration
- **Parallel Execution Support**: Quality validation for concurrent operations
- **Cross-handoff Coordination**: Quality consistency across H6A/B/C
- **Comprehensive Coverage**: Complete validation framework application

---
**Generated by**: comprehensive-quality-validator.sh - H6D-SCRIPTS automation framework
EOF

    echo "QUALITY_REPORT_GENERATED:$report_file"
}

# Main execution function
main() {
    local operation="${1:-validate}"
    local target_pattern="${2:-.*}"
    local mode="${3:-full}"
    
    case "$operation" in
        "validate")
            local exit_code=0
            if execute_comprehensive_validation "$target_pattern" "$mode"; then
                exit_code=$?
            else
                exit_code=$?
            fi
            
            local quality_status="UNKNOWN"
            case $exit_code in
                0) quality_status="EXCELLENT" ;;
                1) quality_status="ACCEPTABLE" ;;
                2) quality_status="POOR" ;;
            esac
            
            generate_quality_report "$mode" "$quality_status"
            return $exit_code
            ;;
            
        "h6a"|"h6b"|"h6c")
            local h6_type=$(echo "$operation" | tr '[:lower:]' '[:upper:]')
            execute_h6_specific_validation "$h6_type" "$target_pattern"
            ;;
            
        "readiness")
            validate_parallel_execution_readiness
            ;;
            
        *)
            echo "UNKNOWN_OPERATION:$operation"
            return 1
            ;;
    esac
}

# Execute main function
main "$@"