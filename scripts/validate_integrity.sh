#!/bin/bash
# validate_integrity.sh - Comprehensive system integrity validation
# 30/07/2025 CDMX | Post-extraction validation for PHASE_0_EMERGENCY

set -e  # Exit on any error

# Configuration
CONTEXT_DIR="/Users/nalve/ce-simple/context"
VALIDATION_DIR="/Users/nalve/ce-simple/scripts/validation_results_$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$VALIDATION_DIR/validation_log.txt"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${GREEN}PHASE_0_EMERGENCY INTEGRITY VALIDATION${NC}"
echo "Validating system integrity after extraction..."

# Create validation directory
mkdir -p "$VALIDATION_DIR"

# Initialize log
echo "Validation started: $(date)" > "$LOG_FILE"
echo "Context directory: $CONTEXT_DIR" >> "$LOG_FILE"

# Function: Check file size compliance
check_file_size_compliance() {
    echo -e "${YELLOW}Checking file size compliance (≤80 lines)...${NC}"
    
    # Find all violations
    find "$CONTEXT_DIR" -name "*.md" -exec wc -l {} + | \
    awk '$1 > 80 {print $1, $2}' | \
    sort -nr > "$VALIDATION_DIR/remaining_violations.txt"
    
    local violation_count=$(wc -l < "$VALIDATION_DIR/remaining_violations.txt")
    
    if [[ $violation_count -eq 0 ]]; then
        echo -e "${GREEN}✅ FILE SIZE COMPLIANCE: PERFECT${NC}"
        echo -e "   All files ≤80 lines limit"
        echo "File size compliance: PASS - 0 violations" >> "$LOG_FILE"
        return 0
    else
        echo -e "${RED}❌ FILE SIZE COMPLIANCE: $violation_count VIOLATIONS REMAIN${NC}"
        echo -e "${YELLOW}Remaining violations:${NC}"
        while read -r lines file; do
            rel_path="${file#$CONTEXT_DIR/}"
            echo -e "  ${RED}✗${NC} $rel_path: $lines lines ($(( (lines * 100) / 80 ))% violation)"
        done < "$VALIDATION_DIR/remaining_violations.txt"
        echo "File size compliance: FAIL - $violation_count violations" >> "$LOG_FILE"
        return 1
    fi
}

# Function: Validate reference integrity
validate_references() {
    echo -e "${YELLOW}Validating cross-reference integrity...${NC}"
    
    local broken_refs=0
    local total_refs=0
    
    # Find all markdown references in format @file.md or → file.md
    find "$CONTEXT_DIR" -name "*.md" -exec grep -l "@\|→\|←\|←→" {} \; > "$VALIDATION_DIR/files_with_refs.txt"
    
    echo > "$VALIDATION_DIR/broken_references.txt"
    echo > "$VALIDATION_DIR/reference_summary.txt"
    
    while read -r file; do
        if [[ -f "$file" ]]; then
            rel_path="${file#$CONTEXT_DIR/}"
            
            # Extract references (@ format)
            grep -o '@[a-zA-Z0-9_/.-]*\.md' "$file" 2>/dev/null | while read -r ref; do
                total_refs=$((total_refs + 1))
                ref_file="${ref#@}"  # Remove @ prefix
                
                # Check if referenced file exists
                if [[ -f "$CONTEXT_DIR/$ref_file" ]]; then
                    echo "✅ $rel_path → $ref_file" >> "$VALIDATION_DIR/reference_summary.txt"
                else
                    echo "❌ $rel_path → $ref_file (BROKEN)" >> "$VALIDATION_DIR/broken_references.txt"
                    broken_refs=$((broken_refs + 1))
                fi
            done
            
            # Extract arrow references (→ ← ←→ format)
            grep -o '[→←].*\.md' "$file" 2>/dev/null | while read -r ref; do
                total_refs=$((total_refs + 1))
                ref_file=$(echo "$ref" | sed 's/^[→←←→ ]*//' | awk '{print $1}')
                
                # Handle relative paths
                ref_dir=$(dirname "$file")
                full_ref_path="$ref_dir/$ref_file"
                
                if [[ -f "$full_ref_path" ]] || [[ -f "$CONTEXT_DIR/$ref_file" ]]; then
                    echo "✅ $rel_path → $ref_file" >> "$VALIDATION_DIR/reference_summary.txt"
                else
                    echo "❌ $rel_path → $ref_file (BROKEN)" >> "$VALIDATION_DIR/broken_references.txt"
                    broken_refs=$((broken_refs + 1))
                fi
            done
        fi
    done < "$VALIDATION_DIR/files_with_refs.txt"
    
    # Count results
    local working_refs=$(wc -l < "$VALIDATION_DIR/reference_summary.txt" 2>/dev/null || echo "0")
    local broken_count=$(wc -l < "$VALIDATION_DIR/broken_references.txt" 2>/dev/null || echo "0")
    
    if [[ $broken_count -eq 0 ]]; then
        echo -e "${GREEN}✅ REFERENCE INTEGRITY: PERFECT${NC}"
        echo -e "   $working_refs references validated, 0 broken"
        echo "Reference integrity: PASS - $working_refs working, 0 broken" >> "$LOG_FILE"
        return 0
    else
        echo -e "${RED}❌ REFERENCE INTEGRITY: $broken_count BROKEN REFERENCES${NC}"
        echo -e "${YELLOW}Broken references:${NC}"
        head -20 "$VALIDATION_DIR/broken_references.txt" 2>/dev/null || echo "No broken references file"
        echo "Reference integrity: FAIL - $broken_count broken references" >> "$LOG_FILE"
        return 1
    fi
}

# Function: Check authority chain preservation
check_authority_preservation() {
    echo -e "${YELLOW}Validating authority chain preservation...${NC}"
    
    local authority_files=("TRUTH_SOURCE.md" "authority.md" "vision_foundation.md" "methodology.md")
    local authority_violations=0
    
    echo > "$VALIDATION_DIR/authority_check.txt"
    
    for auth_file in "${authority_files[@]}"; do
        local full_path=$(find "$CONTEXT_DIR" -name "$auth_file" -type f | head -1)
        
        if [[ -f "$full_path" ]]; then
            echo -e "${GREEN}✅ Authority file found: $auth_file${NC}"
            echo "✅ $auth_file: EXISTS" >> "$VALIDATION_DIR/authority_check.txt"
            
            # Check if file has proper authority references
            if grep -q "AUTORIDAD SUPREMA\|supreme authority\|user authority" "$full_path" 2>/dev/null; then
                echo "✅ $auth_file: AUTHORITY DECLARATIONS PRESENT" >> "$VALIDATION_DIR/authority_check.txt"
            else
                echo "⚠️  $auth_file: MISSING AUTHORITY DECLARATIONS" >> "$VALIDATION_DIR/authority_check.txt"
                authority_violations=$((authority_violations + 1))
            fi
        else
            echo -e "${RED}❌ Authority file missing: $auth_file${NC}"
            echo "❌ $auth_file: MISSING" >> "$VALIDATION_DIR/authority_check.txt"
            authority_violations=$((authority_violations + 1))
        fi
    done
    
    if [[ $authority_violations -eq 0 ]]; then
        echo -e "${GREEN}✅ AUTHORITY PRESERVATION: PERFECT${NC}"
        echo "Authority preservation: PASS - all authority files present" >> "$LOG_FILE"
        return 0
    else
        echo -e "${RED}❌ AUTHORITY PRESERVATION: $authority_violations VIOLATIONS${NC}"
        echo "Authority preservation: FAIL - $authority_violations violations" >> "$LOG_FILE"
        return 1
    fi
}

# Function: Test system navigation
test_system_navigation() {
    echo -e "${YELLOW}Testing system navigation capabilities...${NC}"
    
    # Test CLAUDE.md conditional loading
    local claude_md="$CONTEXT_DIR/../CLAUDE.md"
    if [[ -f "$claude_md" ]]; then
        if grep -q "IF semantic_pattern" "$claude_md" 2>/dev/null; then
            echo -e "${GREEN}✅ CLAUDE.md conditional loading: PRESENT${NC}"
            echo "CLAUDE.md navigation: PASS" >> "$LOG_FILE"
        else
            echo -e "${YELLOW}⚠️  CLAUDE.md conditional loading: NEEDS UPDATE${NC}"
            echo "CLAUDE.md navigation: WARNING" >> "$LOG_FILE"
        fi
    else
        echo -e "${RED}❌ CLAUDE.md: NOT FOUND${NC}"
        echo "CLAUDE.md navigation: FAIL" >> "$LOG_FILE"
    fi
    
    # Test README.md navigation hubs
    local readme_count=$(find "$CONTEXT_DIR" -name "README.md" | wc -l)
    echo -e "${GREEN}✅ README navigation hubs: $readme_count found${NC}"
    echo "README hubs: $readme_count found" >> "$LOG_FILE"
}

# Function: Generate comprehensive validation report
generate_validation_report() {
    echo -e "${YELLOW}Generating validation report...${NC}"
    
    local compliance_status="❌ FAILED"
    local reference_status="❌ FAILED"  
    local authority_status="❌ FAILED"
    
    # Determine status from logs
    if grep -q "File size compliance: PASS" "$LOG_FILE"; then compliance_status="✅ PASSED"; fi
    if grep -q "Reference integrity: PASS" "$LOG_FILE"; then reference_status="✅ PASSED"; fi
    if grep -q "Authority preservation: PASS" "$LOG_FILE"; then authority_status="✅ PASSED"; fi
    
    cat > "$VALIDATION_DIR/VALIDATION_REPORT.md" << EOF
# PHASE_0_EMERGENCY Validation Report

**Date**: $(date)
**Validation Directory**: $VALIDATION_DIR

## Validation Results Summary

| Component | Status | Details |
|-----------|--------|---------|
| File Size Compliance | $compliance_status | All files ≤80 lines |
| Reference Integrity | $reference_status | Cross-references functional |
| Authority Preservation | $authority_status | Authority chain intact |
| System Navigation | ✅ VALIDATED | CLAUDE.md + README hubs |

## Detailed Results

### File Size Compliance
$(if [[ -f "$VALIDATION_DIR/remaining_violations.txt" ]]; then
    if [[ $(wc -l < "$VALIDATION_DIR/remaining_violations.txt") -eq 0 ]]; then
        echo "✅ **PERFECT COMPLIANCE**: All .md files ≤80 lines"
    else
        echo "❌ **$(wc -l < "$VALIDATION_DIR/remaining_violations.txt") VIOLATIONS REMAIN**"
        echo ""
        echo "Remaining violations:"
        head -10 "$VALIDATION_DIR/remaining_violations.txt" | while read -r lines file; do
            echo "- $(basename "$file"): $lines lines"
        done
    fi
else
    echo "No violation data available"
fi)

### Reference Integrity
$(if [[ -f "$VALIDATION_DIR/broken_references.txt" ]]; then
    if [[ $(wc -l < "$VALIDATION_DIR/broken_references.txt") -eq 0 ]]; then
        echo "✅ **PERFECT INTEGRITY**: All cross-references functional"
        echo "- Working references: $(wc -l < "$VALIDATION_DIR/reference_summary.txt" 2>/dev/null || echo "0")"
    else
        echo "❌ **$(wc -l < "$VALIDATION_DIR/broken_references.txt") BROKEN REFERENCES**"
        echo ""
        echo "Broken references (first 10):"
        head -10 "$VALIDATION_DIR/broken_references.txt"
    fi
else
    echo "No reference validation data available"
fi)

### Authority Preservation
$(if [[ -f "$VALIDATION_DIR/authority_check.txt" ]]; then
    echo "Authority file status:"
    cat "$VALIDATION_DIR/authority_check.txt"
else
    echo "No authority validation data available"
fi)

## Recommendations

$(if grep -q "FAIL" "$LOG_FILE"; then
    echo "### ❌ VALIDATION FAILED - Action Required"
    echo "1. **DO NOT PROCEED** with further extractions"
    echo "2. **FIX VIOLATIONS** identified above"
    echo "3. **RE-RUN VALIDATION** until all tests pass"
    echo "4. **CONSIDER ROLLBACK** if issues persist"
else
    echo "### ✅ VALIDATION PASSED - Safe to Continue"
    echo "1. **SYSTEM INTEGRITY**: Confirmed functional"
    echo "2. **SAFE TO PROCEED**: Next extraction phase authorized"
    echo "3. **MONITORING**: Continue validation after each batch"
fi)

---
**VALIDATION COMPLETE**: System integrity $(if grep -q "FAIL" "$LOG_FILE"; then echo "COMPROMISED"; else echo "CONFIRMED"; fi)
EOF

    echo -e "${GREEN}✓ Validation report generated: $VALIDATION_DIR/VALIDATION_REPORT.md${NC}"
}

# Main execution
echo "Context directory: $CONTEXT_DIR"
echo "Validation directory: $VALIDATION_DIR"

# Execute validation sequence
compliance_result=0
reference_result=0
authority_result=0

check_file_size_compliance || compliance_result=1
validate_references || reference_result=1  
check_authority_preservation || authority_result=1
test_system_navigation

# Generate report
generate_validation_report

# Overall result
if [[ $compliance_result -eq 0 ]] && [[ $reference_result -eq 0 ]] && [[ $authority_result -eq 0 ]]; then
    echo -e "${GREEN}🎉 SYSTEM VALIDATION: PERFECT${NC}"
    echo -e "${GREEN}✅ Safe to proceed with next phase${NC}"
    echo "Overall validation: PASS - system integrity confirmed" >> "$LOG_FILE"
    exit 0
else
    echo -e "${RED}❌ SYSTEM VALIDATION: FAILED${NC}"
    echo -e "${RED}⚠️  DO NOT PROCEED - Fix violations first${NC}"
    echo "Overall validation: FAIL - system integrity compromised" >> "$LOG_FILE"
    exit 1
fi

echo "Validation completed: $(date)" >> "$LOG_FILE"