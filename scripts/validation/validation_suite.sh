#!/bin/bash

# validation_suite.sh - Comprehensive Authority Preservation Validation
# Authority: @context/architecture/core/authority.md + @context/vision/simplicity.md
# Purpose: Systematic validation of user authority preservation and system compliance

set -euo pipefail

# Silent script - no user notifications (Claude Code communicates results)
# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
LOG_FILE="$PROJECT_ROOT/scripts/logs/validation_suite_$(date +%Y%m%d_%H%M%S).log"
REPORT_DIR="$PROJECT_ROOT/scripts/validation_results_$(date +%Y%m%d_%H%M%S)"

# Create necessary directories
mkdir -p "$(dirname "$LOG_FILE")"
mkdir -p "$REPORT_DIR"

# Logging function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Error handling
error_exit() {
    log "ERROR: $1"
    exit 1
}

# Banner
log "=========================================="
log "VALIDATION SUITE - COMPREHENSIVE AUTHORITY PRESERVATION"
log "Authority: User Authority Supremacy + 95% Fidelity Requirement"
log "=========================================="

# User quote extraction and analysis
validate_user_authority_preservation() {
    log "VALIDATING: User Authority Preservation (95%+ Fidelity Requirement)"
    
    local total_quotes=0
    local preserved_quotes=0
    local missing_quotes=0
    
    # Known critical user quotes for validation
    declare -a CRITICAL_USER_QUOTES=(
        "no estoy de acuerdo, creo que de esa manera se pierde mucha informacion"
        "Por supuesto que la belleza va a estar en la simplicidad"
        "Quiero que el sistema se sienta como una conversación natural"
        "los comandos son autocontenidos entre ellos y solo pueden conectarse con otros comandos"
        "no debemos de repetir contenido en ningun documento, solo se debe de referenciar"
        "lo más importante también es conservar mi visión, lo que yo estoy diciendo"
        "no me gusta que tú avances sin que tengamos un registro de la planeación"
        "Context como padre de todo"
        "hacerlo lo que tiene que ser"
        "prioriza el uso de scripts siempre que haya errores sistemicos"
    )
    
    log "Checking preservation of ${#CRITICAL_USER_QUOTES[@]} critical user quotes..."
    
    for quote in "${CRITICAL_USER_QUOTES[@]}"; do
        total_quotes=$((total_quotes + 1))
        
        # Search for quote in context directory
        if grep -r -l "$quote" "$PROJECT_ROOT/context" >/dev/null 2>&1; then
            preserved_quotes=$((preserved_quotes + 1))
            log "✅ PRESERVED: \"$quote\""
        else
            missing_quotes=$((missing_quotes + 1))
            log "❌ MISSING: \"$quote\""
            echo "MISSING_QUOTE: $quote" >> "$REPORT_DIR/missing_user_quotes.txt"
        fi
    done
    
    # Calculate fidelity percentage
    local fidelity_percentage=$((preserved_quotes * 100 / total_quotes))
    
    log "=========================================="
    log "USER AUTHORITY PRESERVATION SUMMARY"
    log "Total Critical Quotes: $total_quotes"
    log "Preserved Quotes: $preserved_quotes"
    log "Missing Quotes: $missing_quotes"
    log "Fidelity Percentage: ${fidelity_percentage}%"
    log "=========================================="
    
    # Validation against 95% threshold
    if [[ $fidelity_percentage -ge 95 ]]; then
        log "✅ SUCCESS: User authority preservation meets 95%+ requirement"
        echo "AUTHORITY_VALIDATION: PASS (${fidelity_percentage}%)" >> "$REPORT_DIR/validation_summary.txt"
        return 0
    else
        log "❌ FAILURE: User authority preservation below 95% requirement"
        echo "AUTHORITY_VALIDATION: FAIL (${fidelity_percentage}%)" >> "$REPORT_DIR/validation_summary.txt"
        return 1
    fi
}

# File size compliance validation
validate_file_size_compliance() {
    log "VALIDATING: File Size Compliance (≤80 lines enforcement)"
    
    local total_files=0
    local compliant_files=0
    local violation_files=0
    
    # Check all markdown files in context directory
    while IFS= read -r -d '' file; do
        total_files=$((total_files + 1))
        local line_count=$(wc -l < "$file")
        
        if [[ $line_count -le 80 ]]; then
            compliant_files=$((compliant_files + 1))
            log "✅ COMPLIANT: $file ($line_count lines)"
        else
            violation_files=$((violation_files + 1))
            log "❌ VIOLATION: $file ($line_count lines)"
            echo "SIZE_VIOLATION: $file ($line_count lines)" >> "$REPORT_DIR/file_size_violations.txt"
        fi
        
    done < <(find "$PROJECT_ROOT/context" -name "*.md" -type f -print0)
    
    # Calculate compliance percentage
    local compliance_percentage=$((compliant_files * 100 / total_files))
    
    log "=========================================="
    log "FILE SIZE COMPLIANCE SUMMARY"
    log "Total Files: $total_files"
    log "Compliant Files: $compliant_files"
    log "Violation Files: $violation_files"
    log "Compliance Percentage: ${compliance_percentage}%"
    log "=========================================="
    
    echo "SIZE_COMPLIANCE: $compliance_percentage% ($compliant_files/$total_files)" >> "$REPORT_DIR/validation_summary.txt"
    
    if [[ $violation_files -eq 0 ]]; then
        log "✅ SUCCESS: All files comply with ≤80 lines requirement"
        return 0
    else
        log "⚠️  WARNING: $violation_files files exceed 80-line limit"
        return 1
    fi
}

# Authority chain integrity validation
validate_authority_chain_integrity() {
    log "VALIDATING: Authority Chain Integrity"
    
    local total_files=0
    local files_with_authority=0
    local broken_chains=0
    
    # Check for authority chain declarations in all files
    while IFS= read -r -d '' file; do
        total_files=$((total_files + 1))
        
        # Check for authority declarations
        if grep -q "AUTORIDAD SUPREMA\|## AUTORIDAD\|AUTHORITY" "$file"; then
            files_with_authority=$((files_with_authority + 1))
            
            # Validate authority chain references
            if grep -q "@context/vision/vision_foundation.md\|@context/architecture/core/truth-source.md" "$file"; then
                log "✅ VALID CHAIN: $file"
            else
                broken_chains=$((broken_chains + 1))
                log "❌ BROKEN CHAIN: $file (missing supreme authority reference)"
                echo "BROKEN_AUTHORITY_CHAIN: $file" >> "$REPORT_DIR/broken_authority_chains.txt"
            fi
        fi
        
    done < <(find "$PROJECT_ROOT/context" -name "*.md" -type f -print0)
    
    log "=========================================="
    log "AUTHORITY CHAIN INTEGRITY SUMMARY"
    log "Total Files: $total_files"
    log "Files with Authority Declarations: $files_with_authority"
    log "Broken Authority Chains: $broken_chains"
    log "=========================================="
    
    echo "AUTHORITY_CHAIN_INTEGRITY: $broken_chains broken chains" >> "$REPORT_DIR/validation_summary.txt"
    
    if [[ $broken_chains -eq 0 ]]; then
        log "✅ SUCCESS: All authority chains are intact"
        return 0
    else
        log "❌ FAILURE: $broken_chains broken authority chains detected"
        return 1
    fi
}

# Content duplication detection
validate_content_duplication() {
    log "VALIDATING: Content Duplication (DRY Compliance)"
    
    local duplicate_blocks=0
    local total_blocks_checked=0
    
    # Create temporary file for analysis
    local temp_analysis="$REPORT_DIR/duplication_analysis.txt"
    
    # Extract significant content blocks (>3 lines) from all files
    while IFS= read -r -d '' file; do
        # Extract blocks of 4+ consecutive lines
        awk 'NF>0{lines[NR]=$0} END{
            for(i=1; i<=NR-3; i++) {
                if(lines[i] && lines[i+1] && lines[i+2] && lines[i+3]) {
                    block = lines[i] "\n" lines[i+1] "\n" lines[i+2] "\n" lines[i+3]
                    print "BLOCK:" FILENAME ":" i ":" block
                }
            }
        }' "$file" >> "$temp_analysis"
        
    done < <(find "$PROJECT_ROOT/context" -name "*.md" -type f -print0)
    
    # Analyze for duplicates
    while IFS=: read -r marker file1 line1 content; do
        if [[ "$marker" == "BLOCK" ]]; then
            total_blocks_checked=$((total_blocks_checked + 1))
            
            # Search for same content in other files
            while IFS=: read -r marker2 file2 line2 content2; do
                if [[ "$marker2" == "BLOCK" && "$file1" != "$file2" && "$content" == "$content2" ]]; then
                    duplicate_blocks=$((duplicate_blocks + 1))
                    log "❌ DUPLICATE CONTENT: $file1:$line1 and $file2:$line2"
                    echo "DUPLICATE: $file1:$line1 <-> $file2:$line2" >> "$REPORT_DIR/content_duplicates.txt"
                    break
                fi
            done < "$temp_analysis"
        fi
    done < "$temp_analysis"
    
    log "=========================================="
    log "CONTENT DUPLICATION SUMMARY"
    log "Total Blocks Analyzed: $total_blocks_checked"
    log "Duplicate Blocks Found: $duplicate_blocks"
    log "=========================================="
    
    echo "CONTENT_DUPLICATION: $duplicate_blocks duplicates found" >> "$REPORT_DIR/validation_summary.txt"
    
    if [[ $duplicate_blocks -eq 0 ]]; then
        log "✅ SUCCESS: No content duplication detected"
        return 0
    else
        log "⚠️  WARNING: $duplicate_blocks duplicate content blocks found"
        return 1
    fi
}

# Reference architecture compliance
validate_reference_architecture() {
    log "VALIDATING: Reference Architecture Compliance"
    
    local total_references=0
    local valid_references=0
    local invalid_references=0
    
    # Check reference syntax compliance
    while IFS= read -r -d '' file; do
        while IFS=: read -r line_num content; do
            # Extract references
            while read -r reference; do
                total_references=$((total_references + 1))
                
                # Validate @context/ prefix compliance
                if [[ "$reference" =~ ^@context/ ]]; then
                    # Check if target file exists
                    local target_file="${reference#@}"
                    if [[ -f "$PROJECT_ROOT/$target_file" ]]; then
                        valid_references=$((valid_references + 1))
                    else
                        invalid_references=$((invalid_references + 1))
                        log "❌ INVALID REF: $file:$line_num -> $reference (file not found)"
                        echo "INVALID_REFERENCE: $file:$line_num -> $reference" >> "$REPORT_DIR/invalid_references.txt"
                    fi
                else
                    # Check for missing @context/ prefix
                    if [[ "$reference" =~ ^context/ ]]; then
                        invalid_references=$((invalid_references + 1))
                        log "❌ MISSING PREFIX: $file:$line_num -> $reference (should be @$reference)"
                        echo "MISSING_PREFIX: $file:$line_num -> $reference" >> "$REPORT_DIR/missing_prefixes.txt"
                    else
                        valid_references=$((valid_references + 1))
                    fi
                fi
            done < <(echo "$content" | grep -oE "(→|←|↑|↓|←→) @?context/[^[:space:]\)]*" | sed 's/^[→←↑↓←→] //' || true)
            
        done < <(grep -n -E "(→|←|↑|↓|←→)" "$file" 2>/dev/null || true)
        
    done < <(find "$PROJECT_ROOT/context" -name "*.md" -type f -print0)
    
    # Calculate compliance percentage
    local reference_compliance=100
    if [[ $total_references -gt 0 ]]; then
        reference_compliance=$((valid_references * 100 / total_references))
    fi
    
    log "=========================================="
    log "REFERENCE ARCHITECTURE SUMMARY"
    log "Total References: $total_references"
    log "Valid References: $valid_references"
    log "Invalid References: $invalid_references"
    log "Compliance Percentage: ${reference_compliance}%"
    log "=========================================="
    
    echo "REFERENCE_COMPLIANCE: ${reference_compliance}% ($valid_references/$total_references)" >> "$REPORT_DIR/validation_summary.txt"
    
    if [[ $invalid_references -eq 0 ]]; then
        log "✅ SUCCESS: All references comply with architecture standards"
        return 0
    else
        log "❌ FAILURE: $invalid_references invalid references detected"
        return 1
    fi
}

# Generate comprehensive validation report
generate_validation_report() {
    log "Generating comprehensive validation report..."
    
    local report_file="$REPORT_DIR/VALIDATION_REPORT.md"
    
    cat > "$report_file" << EOF
# System Validation Report

**Generated**: $(date '+%Y-%m-%d %H:%M:%S')
**Authority**: User Authority Supremacy + System Compliance Standards

## Validation Summary

$(cat "$REPORT_DIR/validation_summary.txt" 2>/dev/null || echo "No summary data available")

## Critical Findings

### User Authority Preservation
- **Requirement**: ≥95% user voice fidelity
- **Status**: $(grep "AUTHORITY_VALIDATION" "$REPORT_DIR/validation_summary.txt" 2>/dev/null || echo "Not tested")

### File Size Compliance  
- **Requirement**: ≤80 lines per file
- **Status**: $(grep "SIZE_COMPLIANCE" "$REPORT_DIR/validation_summary.txt" 2>/dev/null || echo "Not tested")

### Authority Chain Integrity
- **Requirement**: Complete traceability to supreme authority
- **Status**: $(grep "AUTHORITY_CHAIN_INTEGRITY" "$REPORT_DIR/validation_summary.txt" 2>/dev/null || echo "Not tested")

### Content Duplication
- **Requirement**: Zero content duplication (DRY compliance)
- **Status**: $(grep "CONTENT_DUPLICATION" "$REPORT_DIR/validation_summary.txt" 2>/dev/null || echo "Not tested")

### Reference Architecture
- **Requirement**: 100% reference syntax compliance
- **Status**: $(grep "REFERENCE_COMPLIANCE" "$REPORT_DIR/validation_summary.txt" 2>/dev/null || echo "Not tested")

## Detailed Reports

- **Missing User Quotes**: missing_user_quotes.txt
- **File Size Violations**: file_size_violations.txt  
- **Broken Authority Chains**: broken_authority_chains.txt
- **Content Duplicates**: content_duplicates.txt
- **Invalid References**: invalid_references.txt
- **Missing Prefixes**: missing_prefixes.txt

## Recommendations

1. **User Authority**: Restore any missing critical user quotes
2. **File Size**: Apply L2-MODULAR extraction to oversized files
3. **Authority Chains**: Fix broken authority references
4. **Duplication**: Implement reference-only architecture for duplicates
5. **References**: Add @context/ prefixes and fix dead links

---
**VALIDATION AUTHORITY**: System compliance with user authority supremacy standards
EOF

    log "Validation report generated: $report_file"
}

# Main execution function
main() {
    local operation="${1:-full}"
    local overall_success=0
    
    case "$operation" in
        "authority")
            validate_user_authority_preservation
            ;;
        "size")
            validate_file_size_compliance
            ;;
        "chains")
            validate_authority_chain_integrity
            ;;
        "duplication")
            validate_content_duplication
            ;;
        "references")
            validate_reference_architecture
            ;;
        "full")
            log "Running comprehensive validation suite..."
            
            # Run all validations and track results
            validate_user_authority_preservation && ((overall_success++)) || true
            validate_file_size_compliance && ((overall_success++)) || true
            validate_authority_chain_integrity && ((overall_success++)) || true
            validate_content_duplication && ((overall_success++)) || true
            validate_reference_architecture && ((overall_success++)) || true
            
            # Generate report
            generate_validation_report
            
            log "=========================================="
            log "COMPREHENSIVE VALIDATION RESULTS"
            log "Passed Validations: $overall_success/5"
            log "Report Directory: $REPORT_DIR"
            log "=========================================="
            
            if [[ $overall_success -eq 5 ]]; then
                log "✅ SUCCESS: All validations passed"
                return 0
            else
                log "⚠️  WARNING: $(( 5 - overall_success )) validation(s) failed"
                return 1
            fi
            ;;
        *)
            echo "Usage: $0 {authority|size|chains|duplication|references|full}"
            echo ""
            echo "Validations:"
            echo "  authority    - User authority preservation (95%+ fidelity)"
            echo "  size         - File size compliance (≤80 lines)"
            echo "  chains       - Authority chain integrity"
            echo "  duplication  - Content duplication detection"
            echo "  references   - Reference architecture compliance"
            echo "  full         - Run all validations and generate report"
            exit 1
            ;;
    esac
}

# Execute main function
main "$@"

log "Validation suite completed. Results: $REPORT_DIR"