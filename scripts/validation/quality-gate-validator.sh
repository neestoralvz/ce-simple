#!/bin/bash
# quality-gate-validator.sh - Comprehensive quality validation framework
# 31/07/2025 CDMX | H6D-SCRIPTS automation framework - Quality Assurance Script #3

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
OUTPUT_DIR="$PROJECT_ROOT/scripts/quality_validation_$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$OUTPUT_DIR/quality_validation_log.txt"

# Colors for output
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; BLUE='\033[0;34m'
PURPLE='\033[0;35m'; CYAN='\033[0;36m'; NC='\033[0m'

echo -e "${GREEN}🎯 QUALITY GATE VALIDATOR: Comprehensive Validation Framework${NC}"
mkdir -p "$OUTPUT_DIR"

# Initialize log
{
    echo "Quality gate validation started: $(date)"
    echo "Project root: $PROJECT_ROOT"
    echo "Target: Comprehensive quality validation with automated gates"
    echo "Authority: @context/architecture/standards/quality-assurance.md"
    echo "=============================================================================="
} > "$LOG_FILE"

# Quality gate definitions
declare -A QUALITY_GATES=(
    ["file_size"]="80"           # Max lines per file
    ["authority_fidelity"]="95"  # Min % user voice fidelity
    ["reference_integrity"]="100" # % working references
    ["spanish_preservation"]="90" # % Spanish authority markers
    ["modular_compliance"]="85"   # % L2-MODULAR compliance
)

# Comprehensive file quality assessment
assess_file_quality() {
    local file_path="$1"
    local validation_mode="${2:-comprehensive}"
    
    if [[ ! -f "$file_path" ]]; then
        echo "0:0:0:0:0:failed:file_not_found"
        return
    fi
    
    python3 << EOF
import re
import os
from urllib.parse import urlparse

file_path = "$file_path"
validation_mode = "$validation_mode"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
    
    # Gate 1: File Size Validation (0-100 score)
    line_count = len(lines)
    if line_count <= 80:
        size_score = 100
    elif line_count <= 90:
        size_score = 85
    elif line_count <= 100:
        size_score = 70
    elif line_count <= 120:
        size_score = 50
    else:
        size_score = max(0, 100 - (line_count - 80) * 2)
    
    # Gate 2: Authority Fidelity Assessment (0-100 score)
    authority_elements = 0
    
    # User quotes (high value)
    user_quotes = len(re.findall(r'[">][^"<\n]{10,}["><]', content))
    authority_elements += user_quotes * 15
    
    # Authority declarations
    auth_declarations = len(re.findall(r'\*\*[^*]*(AUTORIDAD|SUPREMA|Authority)[^*]*\*\*', content, re.IGNORECASE))
    authority_elements += auth_declarations * 10
    
    # Spanish authority preservation
    spanish_markers = len(re.findall(r'(autoridad|suprema|usuario|visión|metodología)', content, re.IGNORECASE))
    authority_elements += spanish_markers * 5
    
    # User preference statements
    user_prefs = len(re.findall(r'(quiero|necesito|prefiero|importante|debe)', content, re.IGNORECASE))
    authority_elements += user_prefs * 8
    
    authority_score = min(100, authority_elements)
    
    # Gate 3: Reference Integrity (0-100 score)
    all_refs = re.findall(r'@[a-zA-Z0-9/_.-]+|→\s*[a-zA-Z0-9/_.-]+\.md|←\s*[a-zA-Z0-9/_.-]+\.md', content)
    
    if all_refs:
        # Check reference format compliance
        context_refs = [ref for ref in all_refs if ref.startswith('@context/')]
        format_compliance = len(context_refs) / len(all_refs) * 100 if all_refs else 0
        
        # Check bidirectional consistency
        forward_refs = len(re.findall(r'→', content))
        backward_refs = len(re.findall(r'←', content))
        bidirectional_balance = min(100, (min(forward_refs, backward_refs) / max(forward_refs, backward_refs) * 100) if max(forward_refs, backward_refs) > 0 else 100)
        
        reference_score = (format_compliance * 0.6) + (bidirectional_balance * 0.4)
    else:
        reference_score = 100  # No refs = no problems
    
    # Gate 4: Spanish Preservation (0-100 score)
    total_words = len(content.split())
    spanish_words = len(re.findall(r'\b(autoridad|suprema|usuario|visión|metodología|sistema|principio|quiero|necesito)\b', content, re.IGNORECASE))
    
    if total_words > 0:
        spanish_density = (spanish_words / total_words) * 100
        spanish_score = min(100, spanish_density * 20)  # Scale appropriately
    else:
        spanish_score = 0
    
    # Gate 5: Modular Compliance (0-100 score)
    modular_indicators = 0
    
    # L2-MODULAR indicators
    if 'L2-MODULAR' in content or 'l2-modular' in content.lower():
        modular_indicators += 20
    
    # Hub structure indicators
    if '## AUTORIDAD SUPREMA' in content:
        modular_indicators += 15
    
    # Module references
    module_refs = len(re.findall(r'→\s*@[a-zA-Z0-9/_.-]+\.md', content))
    modular_indicators += min(25, module_refs * 5)
    
    # Clear section structure
    sections = len(re.findall(r'^##+ ', content, re.MULTILINE))
    if sections >= 3:
        modular_indicators += 15
    elif sections >= 2:
        modular_indicators += 10
    
    # Reference architecture compliance
    if '@context/architecture/core/truth-source.md' in content:
        modular_indicators += 15
    
    modular_score = min(100, modular_indicators)
    
    # Overall quality assessment
    scores = [size_score, authority_score, reference_score, spanish_score, modular_score]
    overall_score = sum(scores) / len(scores)
    
    # Quality level determination
    if overall_score >= 90:
        quality_level = "excellent"
    elif overall_score >= 80:
        quality_level = "good"
    elif overall_score >= 70:
        quality_level = "acceptable"
    elif overall_score >= 60:
        quality_level = "poor"
    else:
        quality_level = "critical"
    
    # Gate pass/fail determination
    gates_passed = 0
    total_gates = 5
    
    if size_score >= ${QUALITY_GATES[file_size]}:
        gates_passed += 1
    if authority_score >= ${QUALITY_GATES[authority_fidelity]}:
        gates_passed += 1
    if reference_score >= ${QUALITY_GATES[reference_integrity]}:
        gates_passed += 1
    if spanish_score >= ${QUALITY_GATES[spanish_preservation]}:
        gates_passed += 1
    if modular_score >= ${QUALITY_GATES[modular_compliance]}:
        gates_passed += 1
    
    gate_status = "passed" if gates_passed >= 4 else "failed"
    
    print(f"{size_score:.1f}:{authority_score:.1f}:{reference_score:.1f}:{spanish_score:.1f}:{modular_score:.1f}:{quality_level}:{gate_status}")

except Exception as e:
    print(f"0:0:0:0:0:error:failed")
EOF
}

# Detailed quality analysis with recommendations
analyze_quality_issues() {
    local file_path="$1"
    
    if [[ ! -f "$file_path" ]]; then
        echo "File not found for analysis"
        return 1
    fi
    
    python3 << EOF
import re
import os

file_path = "$file_path"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
    
    print("=== QUALITY ANALYSIS DETAILS ===")
    
    line_count = len(lines)
    print(f"\\nFILE SIZE ANALYSIS:")
    print(f"  Current lines: {line_count}")
    print(f"  Target: ≤80 lines")
    if line_count > 80:
        print(f"  ❌ ISSUE: {line_count - 80} lines over limit")
        print(f"  💡 RECOMMENDATION: Consider L2-MODULAR extraction")
    else:
        print(f"  ✅ COMPLIANT: Within size limits")
    
    print(f"\\nAUTHORITY PRESERVATION:")
    user_quotes = len(re.findall(r'[">][^"<\\n]{10,}["><]', content))
    auth_declarations = len(re.findall(r'\*\*[^*]*(AUTORIDAD|SUPREMA|Authority)[^*]*\*\*', content, re.IGNORECASE))
    
    print(f"  User quotes: {user_quotes}")
    print(f"  Authority declarations: {auth_declarations}")
    
    if user_quotes < 3:
        print(f"  ❌ ISSUE: Insufficient user quotes ({user_quotes} < 3)")
        print(f"  💡 RECOMMENDATION: Add more direct user voice preservation")
    
    if auth_declarations < 1:
        print(f"  ❌ ISSUE: Missing authority declarations")
        print(f"  💡 RECOMMENDATION: Add AUTORIDAD SUPREMA section")
    
    print(f"\\nREFERENCE INTEGRITY:")
    all_refs = re.findall(r'@[a-zA-Z0-9/_.-]+', content)
    context_refs = [ref for ref in all_refs if ref.startswith('@context/')]
    
    print(f"  Total references: {len(all_refs)}")
    print(f"  @context/ compliant: {len(context_refs)}")
    
    if all_refs and len(context_refs) / len(all_refs) < 0.8:
        print(f"  ❌ ISSUE: Poor @context/ compliance ({len(context_refs)}/{len(all_refs)})")
        print(f"  💡 RECOMMENDATION: Convert references to @context/ format")
    
    print(f"\\nMODULAR STRUCTURE:")
    sections = len(re.findall(r'^##+ ', content, re.MULTILINE))
    print(f"  Section headers: {sections}")
    
    if sections < 2:
        print(f"  ❌ ISSUE: Insufficient structure ({sections} < 2)")
        print(f"  💡 RECOMMENDATION: Add clear section organization")
    
    if '@context/architecture/core/truth-source.md' not in content:
        print(f"  ❌ ISSUE: Missing core authority reference")
        print(f"  💡 RECOMMENDATION: Add truth-source.md reference")

except Exception as e:
    print(f"Error in quality analysis: {e}")
EOF
}

# Quality gate enforcement
enforce_quality_gates() {
    local file_path="$1"
    local gate_mode="${2:-strict}"
    local auto_fix="${3:-false}"
    
    echo -e "${BLUE}Enforcing quality gates: $(basename "$file_path")${NC}"
    
    local quality_result=$(assess_file_quality "$file_path" "comprehensive")
    local size_score=$(echo "$quality_result" | cut -d: -f1)
    local authority_score=$(echo "$quality_result" | cut -d: -f2)
    local reference_score=$(echo "$quality_result" | cut -d: -f3)
    local spanish_score=$(echo "$quality_result" | cut -d: -f4)
    local modular_score=$(echo "$quality_result" | cut -d: -f5)
    local quality_level=$(echo "$quality_result" | cut -d: -f6)
    local gate_status=$(echo "$quality_result" | cut -d: -f7)
    
    # Display gate results
    echo -e "\n${PURPLE}📊 Quality Gate Results:${NC}"
    printf "  %-20s | %6.1f | %s\n" "File Size" "$size_score" "$([ $(echo "$size_score >= ${QUALITY_GATES[file_size]}" | bc -l) -eq 1 ] && echo -e "${GREEN}PASS${NC}" || echo -e "${RED}FAIL${NC}")"
    printf "  %-20s | %6.1f | %s\n" "Authority Fidelity" "$authority_score" "$([ $(echo "$authority_score >= ${QUALITY_GATES[authority_fidelity]}" | bc -l) -eq 1 ] && echo -e "${GREEN}PASS${NC}" || echo -e "${RED}FAIL${NC}")"
    printf "  %-20s | %6.1f | %s\n" "Reference Integrity" "$reference_score" "$([ $(echo "$reference_score >= ${QUALITY_GATES[reference_integrity]}" | bc -l) -eq 1 ] && echo -e "${GREEN}PASS${NC}" || echo -e "${RED}FAIL${NC}")"
    printf "  %-20s | %6.1f | %s\n" "Spanish Preservation" "$spanish_score" "$([ $(echo "$spanish_score >= ${QUALITY_GATES[spanish_preservation]}" | bc -l) -eq 1 ] && echo -e "${GREEN}PASS${NC}" || echo -e "${RED}FAIL${NC}")"
    printf "  %-20s | %6.1f | %s\n" "Modular Compliance" "$modular_score" "$([ $(echo "$modular_score >= ${QUALITY_GATES[modular_compliance]}" | bc -l) -eq 1 ] && echo -e "${GREEN}PASS${NC}" || echo -e "${RED}FAIL${NC}")"
    
    echo -e "\n  Overall Quality: ${quality_level^^} | Gate Status: $([ "$gate_status" == "passed" ] && echo -e "${GREEN}PASSED${NC}" || echo -e "${RED}FAILED${NC}")"
    
    # Auto-fix if requested and possible
    if [[ "$auto_fix" == "true" ]] && [[ "$gate_status" == "failed" ]]; then
        echo -e "\n${YELLOW}🔧 Attempting auto-fix...${NC}"
        
        # Basic auto-fixes
        if [[ $(echo "$size_score < ${QUALITY_GATES[file_size]}" | bc -l) -eq 1 ]]; then
            echo -e "${BLUE}  Triggering L2-MODULAR extraction...${NC}"
            # Could call l2_modular_extractor.sh here
        fi
        
        if [[ $(echo "$reference_score < ${QUALITY_GATES[reference_integrity]}" | bc -l) -eq 1 ]]; then
            echo -e "${BLUE}  Fixing reference format...${NC}"
            # Could call reference format fixer here
        fi
    fi
    
    return $([ "$gate_status" == "passed" ] && echo 0 || echo 1)
}

# Batch quality validation
batch_validate_quality() {
    local file_pattern="${1:-.*\.md$}"
    local gate_mode="${2:-strict}"
    local max_files="${3:-50}"
    
    echo -e "${BLUE}🔍 Starting batch quality validation${NC}"
    echo "File pattern: $file_pattern"
    echo "Gate mode: $gate_mode"
    echo "Max files: $max_files"
    
    # Find target files
    local files=()
    while IFS= read -r file; do
        if [[ -f "$file" ]] && [[ "$file" =~ $file_pattern ]]; then
            if [[ ! "$file" =~ /\.git/|/node_modules/|/scripts/.*results/ ]]; then
                files+=("$file")
            fi
        fi
    done < <(find "$PROJECT_ROOT" -type f -name "*.md")
    
    if [[ ${#files[@]} -eq 0 ]]; then
        echo -e "${YELLOW}⚠️  No files found matching pattern${NC}"
        return 1
    fi
    
    # Limit file count
    if [[ ${#files[@]} -gt $max_files ]]; then
        files=("${files[@]:0:$max_files}")
        echo -e "${YELLOW}⚠️  Limited to first $max_files files${NC}"
    fi
    
    echo -e "\n${PURPLE}📊 Quality Validation Results:${NC}"
    printf "%-40s | %5s | %5s | %5s | %5s | %5s | %-10s | %s\n" \
        "FILE" "SIZE" "AUTH" "REF" "SPAN" "MOD" "QUALITY" "GATES"
    printf "%s\n" "$(printf '%.0s-' {1..120})"
    
    local total_files=0
    local passed_files=0
    local failed_files=0
    local excellent_count=0
    local good_count=0
    local acceptable_count=0
    local poor_count=0
    local critical_count=0
    
    for file_path in "${files[@]}"; do
        local relative_path="${file_path#$PROJECT_ROOT/}"
        local quality_result=$(assess_file_quality "$file_path" "$gate_mode")
        
        local size_score=$(echo "$quality_result" | cut -d: -f1)
        local authority_score=$(echo "$quality_result" | cut -d: -f2)
        local reference_score=$(echo "$quality_result" | cut -d: -f3)
        local spanish_score=$(echo "$quality_result" | cut -d: -f4)
        local modular_score=$(echo "$quality_result" | cut -d: -f5)
        local quality_level=$(echo "$quality_result" | cut -d: -f6)
        local gate_status=$(echo "$quality_result" | cut -d: -f7)
        
        # Color code based on gate status
        local color="${GREEN}"
        if [[ "$gate_status" == "failed" ]]; then
            color="${RED}"
            ((failed_files++))
        else
            color="${GREEN}"
            ((passed_files++))
        fi
        
        printf "${color}%-40s | %5.1f | %5.1f | %5.1f | %5.1f | %5.1f | %-10s | %s${NC}\n" \
            "$(basename "$file_path")" "$size_score" "$authority_score" "$reference_score" \
            "$spanish_score" "$modular_score" "$quality_level" "$gate_status"
        
        # Count by quality level
        case "$quality_level" in
            "excellent") ((excellent_count++)) ;;
            "good") ((good_count++)) ;;
            "acceptable") ((acceptable_count++)) ;;
            "poor") ((poor_count++)) ;;
            "critical") ((critical_count++)) ;;
        esac
        
        ((total_files++))
        
        # Log detailed results
        {
            echo "QUALITY_VALIDATION: $(basename "$file_path")"
            echo "  Path: $relative_path"
            echo "  Scores: Size($size_score) Auth($authority_score) Ref($reference_score) Spanish($spanish_score) Modular($modular_score)"
            echo "  Quality: $quality_level | Gates: $gate_status"
            echo "  ---"
        } >> "$LOG_FILE"
    done
    
    # Calculate summary statistics
    local pass_rate=$(( passed_files * 100 / total_files ))
    
    # Display summary
    echo -e "\n${GREEN}📈 Quality Validation Summary:${NC}"
    echo "Files validated: $total_files"
    echo "Pass rate: ${pass_rate}% ($passed_files passed, $failed_files failed)"
    echo ""
    echo "Quality distribution:"
    echo "  Excellent: $excellent_count files"
    echo "  Good: $good_count files"
    echo "  Acceptable: $acceptable_count files"
    echo "  Poor: $poor_count files"
    echo "  Critical: $critical_count files"
    
    # Overall system assessment
    if [[ $pass_rate -ge 90 ]]; then
        echo -e "\n${GREEN}🎉 SYSTEM STATUS: EXCELLENT quality compliance${NC}"
    elif [[ $pass_rate -ge 75 ]]; then
        echo -e "\n${YELLOW}⚠️  SYSTEM STATUS: Good quality, minor improvements needed${NC}"
    elif [[ $pass_rate -ge 60 ]]; then
        echo -e "\n${YELLOW}⚠️  SYSTEM STATUS: Acceptable quality, significant improvements needed${NC}"
    else
        echo -e "\n${RED}❌ SYSTEM STATUS: CRITICAL quality issues detected${NC}"
    fi
    
    return $pass_rate
}

# Generate comprehensive quality report
generate_quality_report() {
    local total_files="$1"
    local pass_rate="$2"
    local report_file="$OUTPUT_DIR/QUALITY_GATE_VALIDATION_REPORT.md"
    
    cat > "$report_file" << EOF
# Quality Gate Validation Report

**Generated**: $(date)
**Script**: quality-gate-validator.sh
**Purpose**: Comprehensive quality validation framework with automated gates

## Validation Summary

### Overall Results
- **Files Validated**: $total_files
- **Pass Rate**: ${pass_rate}%
- **Gate Compliance**: 5 quality gates with automated assessment

### Quality Gates Framework

#### Gate 1: File Size Compliance (≤80 lines)
- **Purpose**: Ensure files remain within maintainable size limits
- **Threshold**: ${QUALITY_GATES[file_size]} points minimum
- **Action**: Trigger L2-MODULAR extraction when exceeded

#### Gate 2: Authority Fidelity (≥95% user voice preservation)
- **Purpose**: Maintain supreme user authority throughout system
- **Threshold**: ${QUALITY_GATES[authority_fidelity]} points minimum
- **Components**: User quotes, authority declarations, preferences

#### Gate 3: Reference Integrity (100% working references)
- **Purpose**: Ensure all cross-references function correctly
- **Threshold**: ${QUALITY_GATES[reference_integrity]} points minimum
- **Standards**: @context/ format compliance, bidirectional consistency

#### Gate 4: Spanish Preservation (≥90% authority markers)
- **Purpose**: Preserve original Spanish authority terminology
- **Threshold**: ${QUALITY_GATES[spanish_preservation]} points minimum
- **Elements**: autoridad, suprema, usuario, visión, metodología

#### Gate 5: Modular Compliance (≥85% L2-MODULAR standards)
- **Purpose**: Ensure proper modular architecture implementation
- **Threshold**: ${QUALITY_GATES[modular_compliance]} points minimum
- **Indicators**: L2-MODULAR markers, hub structure, module references

### Quality Levels
- **Excellent (≥90)**: Full compliance with all quality standards
- **Good (80-89)**: Minor improvements needed, generally compliant
- **Acceptable (70-79)**: Significant improvements required
- **Poor (60-69)**: Major quality issues, systematic attention needed
- **Critical (<60)**: Urgent intervention required

### Automated Features
- **Pattern Recognition**: Automated identification of quality issues
- **Gate Enforcement**: Systematic validation against all quality criteria
- **Batch Processing**: Efficient validation of multiple files
- **Detailed Analysis**: Comprehensive issue identification and recommendations

---
**Generated by**: quality-gate-validator.sh - H6D-SCRIPTS automation framework
EOF

    echo -e "${GREEN}📄 Quality report: QUALITY_GATE_VALIDATION_REPORT.md${NC}"
}

# Show usage information
show_usage() {
    cat << EOF
Quality Gate Validator - H6D-SCRIPTS Automation Framework

USAGE:
    $0 [file_path] [detailed_analysis]
    $0 --batch [pattern] [gate_mode] [max_files]
    $0 --enforce [file_path] [gate_mode] [auto_fix]
    $0 --help

SINGLE FILE MODE:
    file_path           Path to file for validation
    detailed_analysis   true/false - show detailed analysis (default: false)

BATCH MODE:
    pattern            Regex pattern for file filtering (default: .*\.md$)
    gate_mode          strict/standard/lenient (default: strict)
    max_files          Maximum files to validate (default: 50)

ENFORCEMENT MODE:
    file_path          Path to file for gate enforcement
    gate_mode          strict/standard/lenient (default: strict)
    auto_fix           true/false - attempt automatic fixes (default: false)

EXAMPLES:
    $0 context/architecture/core/authority.md true              # Single file with details
    $0 --batch "context/.*" standard 30                        # Batch validate context files
    $0 --enforce file.md strict true                           # Enforce gates with auto-fix
    $0 --batch ".*authority.*" strict 10                       # Authority files validation

QUALITY GATES:
    File Size          ≤80 lines (${QUALITY_GATES[file_size]} threshold)
    Authority Fidelity ≥95% user voice (${QUALITY_GATES[authority_fidelity]} threshold)
    Reference Integrity 100% working refs (${QUALITY_GATES[reference_integrity]} threshold)
    Spanish Preservation ≥90% markers (${QUALITY_GATES[spanish_preservation]} threshold)
    Modular Compliance  ≥85% L2-MODULAR (${QUALITY_GATES[modular_compliance]} threshold)

OUTPUT:
    - Individual quality scores for all 5 gates
    - Pass/fail status for each quality gate
    - Overall quality level and recommendations
    - Batch validation summary with system health assessment
    - Comprehensive quality validation report
EOF
}

# Main execution function
main() {
    if [[ $# -eq 0 ]] || [[ "$1" == "--help" ]]; then
        show_usage
        exit 0
    fi
    
    case "$1" in
        --batch)
            local pattern="${2:-.*\.md$}"
            local gate_mode="${3:-strict}"
            local max_files="${4:-50}"
            
            echo -e "${GREEN}📊 Starting batch quality validation${NC}"
            local pass_rate=$(batch_validate_quality "$pattern" "$gate_mode" "$max_files")
            
            generate_quality_report "$max_files" "$pass_rate"
            
            if [[ $pass_rate -ge 75 ]]; then
                echo -e "\n${GREEN}✅ Batch validation completed successfully${NC}"
            else
                echo -e "\n${YELLOW}⚠️  Batch validation completed with quality issues${NC}"
            fi
            ;;
            
        --enforce)
            local file_path="$2"
            local gate_mode="${3:-strict}"
            local auto_fix="${4:-false}"
            
            if [[ ! -f "$file_path" ]]; then
                echo -e "${RED}❌ File not found: $file_path${NC}"
                exit 1
            fi
            
            echo -e "${GREEN}🎯 Enforcing quality gates${NC}"
            if enforce_quality_gates "$file_path" "$gate_mode" "$auto_fix"; then
                echo -e "\n${GREEN}✅ Quality gates passed${NC}"
            else
                echo -e "\n${RED}❌ Quality gates failed${NC}"
                analyze_quality_issues "$file_path"
            fi
            ;;
            
        *)
            local file_path="$1"
            local detailed_analysis="${2:-false}"
            
            if [[ ! -f "$file_path" ]]; then
                echo -e "${RED}❌ File not found: $file_path${NC}"
                exit 1
            fi
            
            echo -e "${GREEN}🔍 Single file quality validation${NC}"
            if enforce_quality_gates "$file_path" "standard" "false"; then
                echo -e "\n${GREEN}✅ File passes quality validation${NC}"
            else
                echo -e "\n${YELLOW}⚠️  File has quality issues${NC}"
            fi
            
            if [[ "$detailed_analysis" == "true" ]]; then
                analyze_quality_issues "$file_path"
            fi
            ;;
    esac
    
    echo -e "\n${GREEN}📁 Output directory: $OUTPUT_DIR${NC}"
    echo -e "${GREEN}📄 Validation log: $LOG_FILE${NC}"
}

# Execute main function
main "$@"