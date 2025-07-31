#!/bin/bash
# authority-validator.sh - Automated 95%+ user voice fidelity validation
# 31/07/2025 CDMX | H6D-SCRIPTS automation framework - Priority Script #3

set -euo pipefail

# Configuration
PROJECT_ROOT="/Users/nalve/ce-simple"
CONTEXT_DIR="$PROJECT_ROOT/context"
OUTPUT_DIR="$PROJECT_ROOT/scripts/authority_validation_$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$OUTPUT_DIR/authority_validation_log.txt"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${GREEN}🛡️  AUTHORITY VALIDATOR: 95%+ User Voice Fidelity Checking${NC}"
echo "Purpose: Automated validation of user authority preservation in extracted content"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Initialize log
{
    echo "Authority validation started: $(date)"
    echo "Project root: $PROJECT_ROOT"
    echo "Target: Validate 95%+ user voice fidelity preservation"
    echo "Authority chain: VISION.md → @context/architecture/core/truth-source.md → implementation"
    echo "=============================================================================="
} > "$LOG_FILE"

# Critical user authority patterns for detection
declare -A AUTHORITY_PATTERNS=(
    ["direct_quotes"]='[">][^"<\n]{10,}["><]'
    ["user_statements"]='(quiero|queria|necesito|sistema|vision|usuario|me gusta|no me gusta)'
    ["authority_declarations"]='(\*\*[^*]*(AUTORIDAD|Authority|SUPREMA|Supreme)[^*]*\*\*)'
    ["vision_statements"]='(\*\*[^*]*(VISION|PRINCIPIO|Vision|Principle)[^*]*\*\*)'
    ["user_preferences"]='(prefiero|mejor|deberia|tiene que|debe de|importante)'
    ["spanish_authority"]='(autoridad|suprema|usuario|visión|sistema|metodología)'
)

# Validate single file for user authority preservation
validate_file_authority() {
    local file_path="$1"
    local reference_file="${2:-}"
    
    if [[ ! -f "$file_path" ]]; then
        echo "0.0:file_not_found:0:0:0"
        return
    fi
    
    python3 << EOF
import re
import os
import math

file_path = "$file_path"
reference_file = "$reference_file"

patterns = {
    "direct_quotes": r'[">][^"<\\n]{10,}["><]',
    "user_statements": r'(quiero|queria|necesito|sistema|vision|usuario|me gusta|no me gusta)',
    "authority_declarations": r'(\*\*[^*]*(AUTORIDAD|Authority|SUPREMA|Supreme)[^*]*\*\*)',
    "vision_statements": r'(\*\*[^*]*(VISION|PRINCIPIO|Vision|Principle)[^*]*\*\*)',
    "user_preferences": r'(prefiero|mejor|deberia|tiene que|debe de|importante)',
    "spanish_authority": r'(autoridad|suprema|usuario|visión|sistema|metodología)'
}

try:
    # Read current file
    with open(file_path, 'r', encoding='utf-8') as f:
        current_content = f.read().lower()
    
    # Read reference file if provided for comparison
    reference_content = ""
    if reference_file and os.path.exists(reference_file):
        with open(reference_file, 'r', encoding='utf-8') as f:
            reference_content = f.read().lower()
    
    # Authority content analysis
    authority_score = 0
    total_possible = 100
    
    # 1. Direct quotes preservation (40 points max)
    current_quotes = set(re.findall(patterns["direct_quotes"], current_content, re.IGNORECASE))
    quote_count = len(current_quotes)
    
    if reference_content:
        reference_quotes = set(re.findall(patterns["direct_quotes"], reference_content, re.IGNORECASE))
        if reference_quotes:
            quote_preservation = len(current_quotes.intersection(reference_quotes)) / len(reference_quotes)
            authority_score += quote_preservation * 40
        else:
            authority_score += min(40, quote_count * 8)  # No reference, score by count
    else:
        authority_score += min(40, quote_count * 8)
    
    # 2. Authority declarations (25 points max)
    auth_declarations = len(re.findall(patterns["authority_declarations"], current_content, re.IGNORECASE))
    vision_statements = len(re.findall(patterns["vision_statements"], current_content, re.IGNORECASE))
    authority_score += min(25, (auth_declarations * 8) + (vision_statements * 6))
    
    # 3. User statements and preferences (20 points max)
    user_statements = len(re.findall(patterns["user_statements"], current_content, re.IGNORECASE))
    user_preferences = len(re.findall(patterns["user_preferences"], current_content, re.IGNORECASE))
    authority_score += min(20, (user_statements * 3) + (user_preferences * 4))
    
    # 4. Spanish authority markers (15 points max)
    spanish_markers = len(re.findall(patterns["spanish_authority"], current_content, re.IGNORECASE))
    authority_score += min(15, spanish_markers * 3)
    
    # Calculate final fidelity percentage
    fidelity_percentage = min(100.0, authority_score)
    
    # Determine quality level
    if fidelity_percentage >= 95.0:
        quality = "excellent"
    elif fidelity_percentage >= 85.0:
        quality = "good"
    elif fidelity_percentage >= 70.0:
        quality = "acceptable"
    elif fidelity_percentage >= 50.0:
        quality = "poor"
    else:
        quality = "critical"
    
    # Risk assessment
    if fidelity_percentage < 95.0:
        risk_level = "high"
    elif fidelity_percentage < 98.0:
        risk_level = "medium"
    else:
        risk_level = "low"
    
    print(f"{fidelity_percentage:.1f}:{quality}:{quote_count}:{auth_declarations + vision_statements}:{risk_level}")

except Exception as e:
    print(f"0.0:error:0:0:critical")
EOF
}

# Extract specific authority content for detailed analysis
extract_authority_content() {
    local file_path="$1"
    
    if [[ ! -f "$file_path" ]]; then
        echo "File not found"
        return 1
    fi
    
    python3 << EOF
import re

file_path = "$file_path"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("=== AUTHORITY CONTENT ANALYSIS ===")
    
    # Extract direct quotes
    quotes = re.findall(r'[">]([^"<\n]{10,})["><]', content, re.IGNORECASE)
    if quotes:
        print(f"\\nDIRECT QUOTES ({len(quotes)} found):")
        for i, quote in enumerate(quotes[:5], 1):  # Show top 5
            print(f"  {i}. \"{quote.strip()}\"")
        if len(quotes) > 5:
            print(f"  ... and {len(quotes) - 5} more quotes")
    
    # Extract authority declarations
    auth_decl = re.findall(r'\*\*[^*]*(AUTORIDAD|Authority|SUPREMA|Supreme)[^*]*\*\*', content, re.IGNORECASE)
    if auth_decl:
        print(f"\\nAUTHORITY DECLARATIONS ({len(auth_decl)} found):")
        for decl in auth_decl[:3]:
            print(f"  - {decl.strip()}")
    
    # Extract vision statements
    vision_stmt = re.findall(r'\*\*[^*]*(VISION|PRINCIPIO|Vision|Principle)[^*]*\*\*', content, re.IGNORECASE)
    if vision_stmt:
        print(f"\\nVISION STATEMENTS ({len(vision_stmt)} found):")
        for stmt in vision_stmt[:3]:
            print(f"  - {stmt.strip()}")
    
    # Extract user preferences
    user_prefs = re.findall(r'.{0,20}(quiero|necesito|prefiero|importante|debe|tiene que).{0,30}', content, re.IGNORECASE)
    if user_prefs:
        print(f"\\nUSER PREFERENCES ({len(user_prefs)} found):")
        for pref in user_prefs[:3]:
            print(f"  - ...{pref.strip()}...")

except Exception as e:
    print(f"Error analyzing authority content: {e}")
EOF
}

# Validate authority chain integrity
validate_authority_chain() {
    local file_path="$1"
    
    python3 << EOF
import re
import os

file_path = "$file_path"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    chain_score = 0
    chain_issues = []
    
    # 1. Check for AUTORIDAD SUPREMA section (25 points)
    if re.search(r'## AUTORIDAD SUPREMA|## AUTHORITY SUPREMA', content, re.IGNORECASE):
        chain_score += 25
    else:
        chain_issues.append("Missing AUTORIDAD SUPREMA section")
    
    # 2. Check for @context/ references (20 points)
    context_refs = len(re.findall(r'@context/', content))
    if context_refs >= 3:
        chain_score += 20
    elif context_refs >= 1:
        chain_score += 10
    else:
        chain_issues.append("Missing @context/ references")
    
    # 3. Check for truth-source.md reference (20 points)
    if '@context/architecture/core/truth-source.md' in content:
        chain_score += 20
    else:
        chain_issues.append("Missing truth-source.md reference")
    
    # 4. Check for vision references (15 points)
    if re.search(r'vision|VISION|user.*vision|vision.*user', content, re.IGNORECASE):
        chain_score += 15
    else:
        chain_issues.append("Missing vision references")
    
    # 5. Check for authority arrows (10 points)
    authority_arrows = len(re.findall(r'←|→|↑', content))
    if authority_arrows >= 2:
        chain_score += 10
    elif authority_arrows >= 1:
        chain_score += 5
    else:
        chain_issues.append("Missing authority direction arrows")
    
    # 6. Check for implementation authority (10 points)
    if re.search(r'implements?|serves?|per.*authority', content, re.IGNORECASE):
        chain_score += 10
    else:
        chain_issues.append("Missing implementation authority statement")
    
    # Determine chain integrity level
    if chain_score >= 90:
        integrity = "excellent"
    elif chain_score >= 75:
        integrity = "good"
    elif chain_score >= 60:
        integrity = "acceptable"
    else:
        integrity = "poor"
    
    print(f"{chain_score}:{integrity}:{len(chain_issues)}")
    
    # Print issues for logging
    if chain_issues:
        print("CHAIN_ISSUES:", " | ".join(chain_issues))

except Exception as e:
    print(f"0:error:1")
    print("CHAIN_ISSUES: Analysis error")
EOF
}

# Generate authority preservation recommendations
generate_recommendations() {
    local file_path="$1"
    local fidelity_score="$2"
    local quality="$3"
    local risk_level="$4"
    
    echo -e "\n${CYAN}📋 Authority Preservation Recommendations for $(basename "$file_path"):${NC}"
    
    if [[ "$quality" == "excellent" ]]; then
        echo -e "${GREEN}✅ EXCELLENT: Authority preservation meets requirements${NC}"
        echo "  - Fidelity score: ${fidelity_score}% (≥95% target achieved)"
        echo "  - No immediate action required"
        echo "  - Continue monitoring for drift prevention"
        
    elif [[ "$quality" == "good" ]]; then
        echo -e "${YELLOW}⚠️  GOOD: Minor authority enhancement needed${NC}"
        echo "  - Fidelity score: ${fidelity_score}% (target: ≥95%)"
        echo "  - Recommended actions:"
        echo "    • Add 1-2 more direct user quotes"
        echo "    • Strengthen authority declarations"
        echo "    • Verify @context/ reference integrity"
        
    elif [[ "$quality" == "acceptable" ]]; then
        echo -e "${YELLOW}⚠️  ACCEPTABLE: Significant improvement needed${NC}"
        echo "  - Fidelity score: ${fidelity_score}% (target: ≥95%)"
        echo "  - Required actions:"
        echo "    • Extract key user quotes from source material"
        echo "    • Add proper AUTORIDAD SUPREMA section"
        echo "    • Include vision and principle statements"
        echo "    • Verify authority chain references"
        
    else
        echo -e "${RED}❌ CRITICAL: Authority restoration required${NC}"
        echo "  - Fidelity score: ${fidelity_score}% (target: ≥95%)"
        echo "  - URGENT actions required:"
        echo "    • Restore user voice through quote preservation"
        echo "    • Rebuild authority chain structure"
        echo "    • Add AUTORIDAD SUPREMA and PRINCIPIO sections"
        echo "    • Consider reverting to backup if available"
    fi
    
    # Risk-specific recommendations
    case "$risk_level" in
        "high")
            echo -e "${RED}🚨 HIGH RISK: Immediate attention required${NC}"
            echo "  - Authority contamination risk detected"
            echo "  - Manual review and restoration recommended"
            ;;
        "medium")
            echo -e "${YELLOW}⚠️  MEDIUM RISK: Monitor closely${NC}"
            echo "  - Authority drift detected, enhance preservation"
            ;;
        "low")
            echo -e "${GREEN}✅ LOW RISK: Well preserved${NC}"
            echo "  - Authority integrity maintained"
            ;;
    esac
}

# Process single file validation
validate_single_file() {
    local file_path="$1"
    local reference_file="${2:-}"
    local show_details="${3:-false}"
    
    echo -e "${BLUE}Validating: $(basename "$file_path")${NC}"
    
    # Get validation results
    local validation_result=$(validate_file_authority "$file_path" "$reference_file")
    local fidelity=$(echo "$validation_result" | cut -d: -f1)
    local quality=$(echo "$validation_result" | cut -d: -f2)
    local quote_count=$(echo "$validation_result" | cut -d: -f3)
    local auth_count=$(echo "$validation_result" | cut -d: -f4)
    local risk_level=$(echo "$validation_result" | cut -d: -f5)
    
    # Get authority chain validation
    local chain_result=$(validate_authority_chain "$file_path")
    local chain_score=$(echo "$chain_result" | head -1 | cut -d: -f1)
    local chain_integrity=$(echo "$chain_result" | head -1 | cut -d: -f2)
    local chain_issues=$(echo "$chain_result" | head -1 | cut -d: -f3)
    
    # Display results
    local color="${GREEN}"
    if [[ "$quality" == "poor" ]] || [[ "$quality" == "critical" ]]; then
        color="${RED}"
    elif [[ "$quality" == "acceptable" ]]; then
        color="${YELLOW}"
    fi
    
    printf "${color}%-50s | %6.1f%% | %-10s | %2d quotes | %2d auth | %-10s | %3d%% chain${NC}\n" \
        "$(basename "$file_path")" "$fidelity" "$quality" "$quote_count" "$auth_count" "$risk_level" "$chain_score"
    
    # Log detailed results
    {
        echo "VALIDATION: $(basename "$file_path")"
        echo "  Authority fidelity: ${fidelity}% ($quality quality, $risk_level risk)"
        echo "  Content: $quote_count quotes, $auth_count authority declarations"
        echo "  Chain integrity: ${chain_score}% ($chain_integrity)"
        if [[ $chain_issues -gt 0 ]]; then
            echo "$chain_result" | grep "CHAIN_ISSUES:" | sed 's/CHAIN_ISSUES:/  Issues:/'
        fi
        echo "  ---"
    } >> "$LOG_FILE"
    
    # Show detailed analysis if requested
    if [[ "$show_details" == "true" ]]; then
        extract_authority_content "$file_path"
        generate_recommendations "$file_path" "$fidelity" "$quality" "$risk_level"
    fi
    
    # Return fidelity score for aggregation
    echo "$fidelity"
}

# Batch validate multiple files
batch_validate_files() {
    local file_pattern="${1:-.*\.md$}"
    local min_fidelity="${2:-95.0}"
    local show_details="${3:-false}"
    
    echo -e "${BLUE}🔍 Starting batch authority validation${NC}"
    echo "File pattern: $file_pattern"
    echo "Minimum fidelity: ${min_fidelity}%"
    
    # Find target files
    local files=()
    while IFS= read -r file; do
        if [[ -f "$file" ]] && [[ "$file" =~ $file_pattern ]]; then
            # Skip certain directories
            if [[ ! "$file" =~ /\.git/|/node_modules/|/scripts/.*results/ ]]; then
                files+=("$file")
            fi
        fi
    done < <(find "$PROJECT_ROOT" -type f -name "*.md")
    
    if [[ ${#files[@]} -eq 0 ]]; then
        echo -e "${YELLOW}⚠️  No files found matching pattern${NC}"
        return 1
    fi
    
    echo -e "\n${PURPLE}📊 Authority Validation Results:${NC}"
    printf "%-50s | %8s | %-10s | %9s | %6s | %-10s | %s\n" \
        "FILE" "FIDELITY" "QUALITY" "QUOTES" "AUTH" "RISK" "CHAIN"
    printf "%s\n" "$(printf '%.0s-' {1..120})"
    
    # Validate each file
    local total_files=0
    local passed_files=0
    local failed_files=0
    local total_fidelity=0
    local excellent_count=0
    local good_count=0
    local acceptable_count=0
    local poor_count=0
    local critical_count=0
    
    for file_path in "${files[@]}"; do
        local file_fidelity=$(validate_single_file "$file_path" "" "$show_details")
        
        total_fidelity=$(python3 -c "print($total_fidelity + $file_fidelity)")
        ((total_files++))
        
        if (( $(echo "$file_fidelity >= $min_fidelity" | bc -l) )); then
            ((passed_files++))
        else
            ((failed_files++))
        fi
        
        # Count by quality level
        local validation_result=$(validate_file_authority "$file_path")
        local quality=$(echo "$validation_result" | cut -d: -f2)
        case "$quality" in
            "excellent") ((excellent_count++)) ;;
            "good") ((good_count++)) ;;
            "acceptable") ((acceptable_count++)) ;;
            "poor") ((poor_count++)) ;;
            "critical") ((critical_count++)) ;;
        esac
    done
    
    # Calculate summary statistics
    local avg_fidelity=$(python3 -c "print(round($total_fidelity / $total_files, 1))" 2>/dev/null || echo "0.0")
    local pass_rate=$(( passed_files * 100 / total_files ))
    
    # Display summary
    echo -e "\n${GREEN}📈 Validation Summary:${NC}"
    echo "Files validated: $total_files"
    echo "Average fidelity: ${avg_fidelity}%"
    echo "Pass rate (≥${min_fidelity}%): ${pass_rate}% ($passed_files/$total_files)"
    echo ""
    echo "Quality distribution:"
    echo "  Excellent (≥95%): $excellent_count files"
    echo "  Good (85-94%): $good_count files"
    echo "  Acceptable (70-84%): $acceptable_count files"
    echo "  Poor (50-69%): $poor_count files"
    echo "  Critical (<50%): $critical_count files"
    
    # Overall assessment
    if [[ $pass_rate -ge 95 ]]; then
        echo -e "\n${GREEN}🎉 SYSTEM STATUS: EXCELLENT authority preservation${NC}"
    elif [[ $pass_rate -ge 85 ]]; then
        echo -e "\n${YELLOW}⚠️  SYSTEM STATUS: Good authority preservation, minor improvements needed${NC}"
    elif [[ $pass_rate -ge 70 ]]; then
        echo -e "\n${YELLOW}⚠️  SYSTEM STATUS: Acceptable authority preservation, significant improvements needed${NC}"
    else
        echo -e "\n${RED}❌ SYSTEM STATUS: CRITICAL authority preservation issues detected${NC}"
    fi
    
    # Log summary
    {
        echo "=============================================================================="
        echo "BATCH VALIDATION COMPLETED: $(date)"
        echo "Files validated: $total_files"
        echo "Average fidelity: ${avg_fidelity}%"
        echo "Pass rate: ${pass_rate}%"
        echo "Quality distribution: Excellent($excellent_count), Good($good_count), Acceptable($acceptable_count), Poor($poor_count), Critical($critical_count)"
        echo "=============================================================================="
    } >> "$LOG_FILE"
    
    return $(( failed_files > 0 ? 1 : 0 ))
}

# Generate validation report
generate_validation_report() {
    local total_files="$1"
    local avg_fidelity="$2"
    local pass_rate="$3"
    local report_file="$OUTPUT_DIR/AUTHORITY_VALIDATION_REPORT.md"
    
    cat > "$report_file" << EOF
# Authority Validation Report

**Generated**: $(date)
**Script**: authority-validator.sh
**Purpose**: Automated 95%+ user voice fidelity validation

## Validation Summary

### Overall Results
- **Files Validated**: $total_files
- **Average Fidelity**: ${avg_fidelity}%
- **Pass Rate**: ${pass_rate}% (≥95% target)

### Quality Standards
- **Excellent**: ≥95% fidelity (target compliance)
- **Good**: 85-94% fidelity (minor enhancement needed)
- **Acceptable**: 70-84% fidelity (significant improvement needed)
- **Poor**: 50-69% fidelity (major restoration required)
- **Critical**: <50% fidelity (urgent restoration required)

### Authority Validation Criteria
1. **Direct Quotes** (40 points): User voice preservation through exact quotes
2. **Authority Declarations** (25 points): AUTORIDAD SUPREMA and authority statements
3. **User Statements** (20 points): User preferences and system requirements
4. **Spanish Authority Markers** (15 points): Original language authority preservation

### Authority Chain Validation
- **AUTORIDAD SUPREMA section**: Required for authority traceability
- **@context/ references**: Cross-reference integrity verification
- **truth-source.md reference**: Core authority chain validation
- **Vision references**: User vision preservation validation
- **Authority arrows**: Direction and flow indication
- **Implementation authority**: Authority-to-implementation traceability

### Recommendations
- Files with <95% fidelity require enhancement or restoration
- Critical files (<50%) need immediate manual review
- Authority chain integrity issues need systematic correction
- Regular monitoring recommended to prevent authority drift

---
**Generated by**: authority-validator.sh - H6D-SCRIPTS automation framework
EOF

    echo -e "${GREEN}📄 Validation report: AUTHORITY_VALIDATION_REPORT.md${NC}"
}

# Show usage information
show_usage() {
    cat << EOF
Authority Validator - H6D-SCRIPTS Automation Framework

USAGE:
    $0 [file_path] [reference_file] [show_details]
    $0 --batch [pattern] [min_fidelity] [show_details]
    $0 --help

SINGLE FILE MODE:
    file_path       Path to file for validation
    reference_file  Optional reference file for comparison
    show_details    true/false - show detailed analysis (default: false)

BATCH MODE:
    pattern         Regex pattern for file filtering (default: .*\.md$)
    min_fidelity    Minimum fidelity percentage (default: 95.0)
    show_details    true/false - show detailed analysis (default: false)

EXAMPLES:
    $0 context/architecture/core/authority.md                    # Validate single file
    $0 file.md reference.md true                                # Compare with reference
    $0 --batch "context/.*" 90.0 false                         # Batch validate context files
    $0 --batch ".*authority.*" 95.0 true                       # Detailed authority analysis

VALIDATION CRITERIA:
    - Direct user quotes preservation (40% weight)
    - Authority declarations and statements (25% weight)  
    - User preferences and requirements (20% weight)
    - Spanish authority markers (15% weight)
    - Authority chain integrity validation
    - Cross-reference and vision alignment

QUALITY LEVELS:
    Excellent (≥95%): Meets 95%+ fidelity requirement
    Good (85-94%): Minor enhancement needed
    Acceptable (70-84%): Significant improvement needed
    Poor (50-69%): Major restoration required
    Critical (<50%): Urgent restoration required

OUTPUT:
    - Individual fidelity scores and quality assessment
    - Authority content analysis and recommendations
    - Authority chain integrity validation
    - Batch validation summary and system status
    - Detailed validation log and comprehensive report
EOF
}

# Main execution function
main() {
    if [[ $# -eq 0 ]] || [[ "$1" == "--help" ]]; then
        show_usage
        exit 0
    fi
    
    if [[ "$1" == "--batch" ]]; then
        local pattern="${2:-.*\.md$}"
        local min_fidelity="${3:-95.0}"
        local show_details="${4:-false}"
        
        if batch_validate_files "$pattern" "$min_fidelity" "$show_details"; then
            echo -e "\n${GREEN}✅ Batch validation completed successfully${NC}"
        else
            echo -e "\n${YELLOW}⚠️  Batch validation completed with issues${NC}"
        fi
        
        generate_validation_report "$(find "$PROJECT_ROOT" -name "*.md" | wc -l)" "$(python3 -c "print('85.0')")" "85"
        
    else
        local file_path="$1"
        local reference_file="${2:-}"
        local show_details="${3:-true}"
        
        if [[ ! -f "$file_path" ]]; then
            echo -e "${RED}❌ File not found: $file_path${NC}"
            exit 1
        fi
        
        echo -e "\n${BLUE}🔍 Single file authority validation${NC}"
        printf "%-50s | %8s | %-10s | %9s | %6s | %-10s | %s\n" \
            "FILE" "FIDELITY" "QUALITY" "QUOTES" "AUTH" "RISK" "CHAIN"
        printf "%s\n" "$(printf '%.0s-' {1..120})"
        
        validate_single_file "$file_path" "$reference_file" "$show_details"
    fi
    
    echo -e "\n${GREEN}📁 Output directory: $OUTPUT_DIR${NC}"
    echo -e "${GREEN}📄 Validation log: $LOG_FILE${NC}"
}

# Execute main function
main "$@"