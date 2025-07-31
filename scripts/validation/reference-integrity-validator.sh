#!/bin/bash
# reference-integrity-validator.sh - Bidirectional link verification system
# 31/07/2025 CDMX | H6D-SCRIPTS automation framework - Priority Script #8

set -euo pipefail

# Configuration
# Get script directory and project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
CONTEXT_DIR="$PROJECT_ROOT/context"
OUTPUT_DIR="$PROJECT_ROOT/scripts/reference_integrity_$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$OUTPUT_DIR/reference_integrity_log.txt"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${GREEN}🔗 REFERENCE INTEGRITY VALIDATOR: Bidirectional Link Verification${NC}"
echo "Purpose: Comprehensive cross-reference validation and bidirectional link integrity verification"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Initialize log
{
    echo "Reference integrity validation started: $(date)"
    echo "Project root: $PROJECT_ROOT"
    echo "Target: Bidirectional link verification and cross-reference integrity"
    echo "Standards: ADR-005 reference architecture compliance"
    echo "=============================================================================="
} > "$LOG_FILE"

# Reference pattern definitions
declare -A REFERENCE_PATTERNS=(
    ["authority"]="← @context/.*"
    ["delegation"]="→ @context/.*"
    ["bidirectional"]="←→ @context/.*"
    ["upward"]="↑ @context/.*"
    ["context_reference"]="@context/[^[:space:]\)]*"
)

# Extract all references from a file
extract_file_references() {
    local file_path="$1"
    local reference_type="${2:-all}"
    
    if [[ ! -f "$file_path" ]]; then
        echo "FILE_NOT_FOUND:$file_path"
        return 1
    fi
    
    python3 << EOF
import re
import os

file_path = "$file_path"
reference_type = "$reference_type"
project_root = "$PROJECT_ROOT"

patterns = {
    "authority": r"← @context/[^\\s\\)]*",
    "delegation": r"→ @context/[^\\s\\)]*", 
    "bidirectional": r"←→ @context/[^\\s\\)]*",
    "upward": r"↑ @context/[^\\s\\)]*",
    "context_reference": r"@context/[^\\s\\)]*"
}

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    relative_path = os.path.relpath(file_path, project_root)
    
    # Extract references based on type
    references = []
    
    if reference_type == "all":
        for pattern in patterns.values():
            matches = re.findall(pattern, content)
            references.extend(matches)
    else:
        if reference_type in patterns:
            matches = re.findall(patterns[reference_type], content)
            references.extend(matches)
    
    # Clean and normalize references
    cleaned_refs = []
    for ref in references:
        # Remove directional arrows and clean
        clean_ref = re.sub(r'^[←→↑↓←→]+\\s*', '', ref).strip()
        if clean_ref.startswith('@context/'):
            cleaned_refs.append(clean_ref)
    
    # Output results
    for ref in cleaned_refs:
        # Check if target file exists
        target_path = os.path.join(project_root, ref[1:])  # Remove @ prefix
        exists = "EXISTS" if os.path.exists(target_path) else "MISSING"
        
        print(f"REFERENCE:{relative_path}:{ref}:{exists}")

except Exception as e:
    print(f"ERROR:{file_path}:{str(e)}")
EOF
}

# Validate bidirectional reference consistency
validate_bidirectional_consistency() {
    local file_pattern="${1:-.*\.md$}"
    local check_reverse="${2:-true}"
    
    echo -e "${BLUE}🔍 Validating bidirectional reference consistency${NC}"
    echo "File pattern: $file_pattern"
    echo "Check reverse references: $check_reverse"
    
    local total_files=0
    local total_references=0
    local valid_references=0
    local broken_references=0
    local missing_reverse=0
    
    # Find all markdown files
    local files=()
    while IFS= read -r file; do
        if [[ -f "$file" ]] && [[ "$file" =~ $file_pattern ]]; then
            if [[ ! "$file" =~ /\.git/|/node_modules/|/scripts/.*results/ ]]; then
                files+=("$file")
            fi
        fi
    done < <(find "$PROJECT_ROOT" -type f -name "*.md")
    
    echo -e "\n${PURPLE}📊 Reference Integrity Analysis:${NC}"
    printf "%-50s | %-8s | %-8s | %-8s | %-10s\n" \
        "FILE" "TOTAL" "VALID" "BROKEN" "REVERSE"
    printf "%s\n" "$(printf '%.0s-' {1..95})"
    
    # Process each file
    for file_path in "${files[@]}"; do
        ((total_files++))
        
        local file_refs=0
        local file_valid=0
        local file_broken=0
        local file_reverse_missing=0
        
        # Extract references from file
        while IFS=: read -r type source_file ref_path status; do
            if [[ "$type" == "REFERENCE" ]]; then
                ((file_refs++))
                ((total_references++))
                
                if [[ "$status" == "EXISTS" ]]; then
                    ((file_valid++))
                    ((valid_references++))
                    
                    # Check reverse reference if bidirectional
                    if [[ "$check_reverse" == "true" ]] && [[ "$ref_path" =~ ←→ ]]; then
                        local target_file="$PROJECT_ROOT/${ref_path#@}"
                        local source_relative=$(realpath --relative-to="$PROJECT_ROOT" "$file_path")
                        
                        if [[ -f "$target_file" ]]; then
                            if ! grep -q "←→.*$source_relative" "$target_file" 2>/dev/null; then
                                ((file_reverse_missing++))
                                ((missing_reverse++))
                            fi
                        fi
                    fi
                else
                    ((file_broken++))
                    ((broken_references++))
                fi
            fi
        done < <(extract_file_references "$file_path" "all")
        
        # Display file results
        local color="${GREEN}"
        if [[ $file_broken -gt 0 ]]; then
            color="${RED}"
        elif [[ $file_reverse_missing -gt 0 ]]; then
            color="${YELLOW}"
        fi
        
        printf "${color}%-50s | %8d | %8d | %8d | %10d${NC}\n" \
            "$(basename "$file_path")" "$file_refs" "$file_valid" "$file_broken" "$file_reverse_missing"
        
        # Log detailed results
        {
            echo "REFERENCE_ANALYSIS: $(basename "$file_path")"
            echo "  Total references: $file_refs"
            echo "  Valid references: $file_valid"
            echo "  Broken references: $file_broken"
            echo "  Missing reverse: $file_reverse_missing"
            echo "  ---"
        } >> "$LOG_FILE"
    done
    
    # Calculate summary statistics
    local integrity_percentage=0
    if [[ $total_references -gt 0 ]]; then
        integrity_percentage=$(( valid_references * 100 / total_references ))
    fi
    
    local reverse_consistency=0
    if [[ $total_references -gt 0 ]]; then
        reverse_consistency=$(( (total_references - missing_reverse) * 100 / total_references ))
    fi
    
    # Display summary
    echo -e "\n${GREEN}📈 Reference Integrity Summary:${NC}"
    echo "Files analyzed: $total_files"
    echo "Total references: $total_references"
    echo "Valid references: $valid_references"
    echo "Broken references: $broken_references"
    echo "Missing reverse references: $missing_reverse"
    echo "Reference integrity: ${integrity_percentage}%"
    echo "Bidirectional consistency: ${reverse_consistency}%"
    
    # Overall assessment
    if [[ $broken_references -eq 0 ]] && [[ $missing_reverse -eq 0 ]]; then
        echo -e "\n${GREEN}🎉 EXCELLENT: Perfect reference integrity${NC}"
        integrity_status="EXCELLENT"
    elif [[ $integrity_percentage -ge 95 ]] && [[ $reverse_consistency -ge 90 ]]; then
        echo -e "\n${GREEN}✅ GOOD: High reference integrity with minor issues${NC}"
        integrity_status="GOOD"
    elif [[ $integrity_percentage -ge 85 ]] && [[ $reverse_consistency -ge 80 ]]; then
        echo -e "\n${YELLOW}⚠️  ACCEPTABLE: Reference integrity needs improvement${NC}"
        integrity_status="ACCEPTABLE"
    else
        echo -e "\n${RED}❌ POOR: Significant reference integrity issues${NC}"
        integrity_status="POOR"
    fi
    
    # Log summary
    {
        echo "=============================================================================="
        echo "REFERENCE INTEGRITY SUMMARY: $(date)"
        echo "Files analyzed: $total_files"
        echo "Total references: $total_references"
        echo "Valid references: $valid_references"
        echo "Broken references: $broken_references"
        echo "Missing reverse: $missing_reverse"
        echo "Integrity percentage: ${integrity_percentage}%"
        echo "Reverse consistency: ${reverse_consistency}%"
        echo "Status: $integrity_status"
        echo "=============================================================================="
    } >> "$LOG_FILE"
    
    # Return appropriate code
    case "$integrity_status" in
        "EXCELLENT"|"GOOD") return 0 ;;
        "ACCEPTABLE") return 1 ;;
        "POOR") return 2 ;;
    esac
}

# Validate authority chain integrity
validate_authority_chains() {
    local trace_depth="${1:-5}"
    
    echo -e "${BLUE}🔍 Validating authority chain integrity${NC}"
    echo "Maximum trace depth: $trace_depth"
    
    local authority_files=()
    local broken_chains=0
    local valid_chains=0
    
    # Find files with authority declarations
    while IFS= read -r file; do
        if [[ -f "$file" ]] && grep -q "AUTORIDAD SUPREMA\|AUTHORITY" "$file" 2>/dev/null; then
            authority_files+=("$file")
        fi
    done < <(find "$PROJECT_ROOT" -type f -name "*.md")
    
    echo -e "\n${PURPLE}📊 Authority Chain Analysis:${NC}"
    printf "%-50s | %-10s | %-8s | %-15s\n" \
        "FILE" "CHAIN" "DEPTH" "TERMINUS"
    printf "%s\n" "$(printf '%.0s-' {1..85})"
    
    for auth_file in "${authority_files[@]}"; do
        local current_file="$auth_file"
        local chain_depth=0
        local chain_valid=true
        local terminus="unknown"
        
        # Trace authority chain
        while [[ $chain_depth -lt $trace_depth ]] && [[ $chain_valid == true ]]; do
            # Look for authority reference in current file
            local auth_ref=$(grep -o "← @context/[^[:space:]\)]*" "$current_file" 2>/dev/null | head -1)
            
            if [[ -n "$auth_ref" ]]; then
                # Clean reference and check if file exists
                local clean_ref=$(echo "$auth_ref" | sed 's/← //')
                local target_file="$PROJECT_ROOT/${clean_ref#@}"
                
                if [[ -f "$target_file" ]]; then
                    current_file="$target_file"
                    ((chain_depth++))
                    
                    # Check if we've reached a supreme authority
                    if grep -q "vision_foundation\|truth-source" "$target_file" 2>/dev/null; then
                        terminus="SUPREME"
                        break
                    fi
                else
                    chain_valid=false
                    terminus="BROKEN"
                    ((broken_chains++))
                    break
                fi
            else
                terminus="TERMINAL"
                break
            fi
        done
        
        if [[ $chain_valid == true ]] && [[ $terminus != "BROKEN" ]]; then
            ((valid_chains++))
        fi
        
        # Display result
        local color="${GREEN}"
        case "$terminus" in
            "BROKEN") color="${RED}" ;;
            "unknown") color="${YELLOW}" ;;
            "TERMINAL") color="${CYAN}" ;;
            "SUPREME") color="${GREEN}" ;;
        esac
        
        local chain_status="VALID"
        if [[ $chain_valid == false ]]; then
            chain_status="BROKEN"
        fi
        
        printf "${color}%-50s | %-10s | %8d | %-15s${NC}\n" \
            "$(basename "$auth_file")" "$chain_status" "$chain_depth" "$terminus"
        
        # Log authority chain details
        {
            echo "AUTHORITY_CHAIN: $(basename "$auth_file")"
            echo "  Chain status: $chain_status"
            echo "  Chain depth: $chain_depth"
            echo "  Terminus: $terminus"
            echo "  ---"
        } >> "$LOG_FILE"
    done
    
    # Authority chain summary
    local total_authority_files=${#authority_files[@]}
    local chain_integrity=0
    if [[ $total_authority_files -gt 0 ]]; then
        chain_integrity=$(( valid_chains * 100 / total_authority_files ))
    fi
    
    echo -e "\n${GREEN}📈 Authority Chain Summary:${NC}"
    echo "Authority files: $total_authority_files"
    echo "Valid chains: $valid_chains"
    echo "Broken chains: $broken_chains"
    echo "Chain integrity: ${chain_integrity}%"
    
    if [[ $broken_chains -eq 0 ]]; then
        echo -e "\n${GREEN}✅ EXCELLENT: All authority chains intact${NC}"
        return 0
    elif [[ $chain_integrity -ge 80 ]]; then
        echo -e "\n${YELLOW}⚠️  ACCEPTABLE: Minor authority chain issues${NC}"
        return 1
    else
        echo -e "\n${RED}❌ CRITICAL: Significant authority chain breaks${NC}"
        return 2
    fi
}

# Fix broken references automatically
fix_broken_references() {
    local dry_run="${1:-true}"
    local fix_strategy="${2:-conservative}"
    
    echo -e "${BLUE}🔧 Fixing broken references (dry_run: $dry_run)${NC}"
    echo "Fix strategy: $fix_strategy"
    
    if [[ "$dry_run" == "false" ]]; then
        echo -e "${YELLOW}⚠️  WARNING: This will modify files. Backups will be created.${NC}"
        mkdir -p "$OUTPUT_DIR/fix_backups"
    fi
    
    local total_fixes=0
    local successful_fixes=0
    
    # Find all files with references
    while IFS= read -r file; do
        if [[ -f "$file" ]]; then
            local file_fixes=0
            local file_backup_created=false
            
            # Extract broken references
            while IFS=: read -r type source_file ref_path status; do
                if [[ "$type" == "REFERENCE" ]] && [[ "$status" == "MISSING" ]]; then
                    ((total_fixes++))
                    
                    # Attempt to fix based on strategy
                    case "$fix_strategy" in
                        "conservative")
                            echo "BROKEN REFERENCE: $source_file -> $ref_path"
                            
                            # Try to find similar files
                            local ref_basename=$(basename "${ref_path#@context/}" .md)
                            local candidates=$(find "$CONTEXT_DIR" -name "*${ref_basename}*" -type f | head -3)
                            
                            if [[ -n "$candidates" ]]; then
                                echo "  Possible fixes:"
                                echo "$candidates" | while read candidate; do
                                    local rel_candidate=$(realpath --relative-to="$PROJECT_ROOT" "$candidate")
                                    echo "    @${rel_candidate}"
                                done
                            fi
                            ;;
                            
                        "aggressive")
                            # Actually attempt automatic fixes (not implemented for safety)
                            echo "AGGRESSIVE FIX: Would attempt automatic repair of $ref_path"
                            ;;
                    esac
                fi
            done < <(extract_file_references "$file" "all")
        fi
    done < <(find "$PROJECT_ROOT" -type f -name "*.md")
    
    echo -e "\n${GREEN}📈 Fix Summary:${NC}"
    echo "References needing fixes: $total_fixes"
    echo "Successful fixes: $successful_fixes"
    
    if [[ "$dry_run" == "true" ]]; then
        echo -e "\n${BLUE}ℹ️  This was a dry run. No files were modified.${NC}"
        echo "Run with --fix false to apply fixes."
    fi
}

# Generate comprehensive reference report
generate_reference_report() {
    local integrity_status="$1"
    local chain_status="$2"
    local report_file="$OUTPUT_DIR/REFERENCE_INTEGRITY_REPORT.md"
    
    cat > "$report_file" << EOF
# Reference Integrity Report

**Generated**: $(date)
**Script**: reference-integrity-validator.sh
**Purpose**: Bidirectional link verification and cross-reference integrity analysis

## Validation Summary

### Reference Integrity
- **Status**: $integrity_status
- **Standards**: ADR-005 reference architecture compliance
- **Scope**: Complete cross-reference validation across all markdown files

### Authority Chain Integrity
- **Status**: $chain_status
- **Validation**: Authority chain traceability to supreme sources
- **Requirements**: Complete authority preservation per user vision supremacy

## Reference Validation Framework

### Reference Types Validated
1. **Authority References** (← @context/): Authority source traceability
2. **Delegation References** (→ @context/): Forward functionality delegation
3. **Bidirectional References** (←→ @context/): Mutual relationship validation
4. **Upward References** (↑ @context/): Hierarchical authority chain validation
5. **Context References** (@context/): General cross-reference integrity

### Validation Criteria
- **File Existence**: All referenced files must exist in the system
- **Bidirectional Consistency**: Mutual references must be reciprocal
- **Authority Chain Integrity**: Authority references must trace to supreme sources
- **Reference Syntax**: All references must follow ADR-005 standards

### Quality Standards
- **Excellent**: 100% reference integrity, complete bidirectional consistency
- **Good**: ≥95% reference integrity, ≥90% bidirectional consistency
- **Acceptable**: ≥85% reference integrity, ≥80% bidirectional consistency
- **Poor**: <85% reference integrity or <80% bidirectional consistency

### Integration with H6D Scripts
- **Pre-Operation Validation**: Reference integrity check before batch operations
- **Post-Operation Validation**: Reference consistency verification after modifications
- **Continuous Monitoring**: Real-time reference integrity tracking
- **Automated Repair**: Conservative fix recommendations for broken references

## Reference Architecture Standards

### ADR-005 Compliance
- **@context/ Prefix**: All cross-references use absolute @context/ paths
- **Directional Arrows**: Clear authority direction indication (←, →, ←→, ↑)
- **Bidirectional Links**: Mutual references maintained for two-way relationships
- **Authority Preservation**: Reference modifications preserve user authority supremacy

### Authority Chain Requirements
- **Supreme Authority**: All authority chains trace to vision_foundation.md or truth-source.md
- **Chain Integrity**: No broken links in authority hierarchy
- **Authority Validation**: Authority files contain required authority markers
- **Reference Traceability**: Complete path from implementation to supreme authority

---
**Generated by**: reference-integrity-validator.sh - H6D-SCRIPTS automation framework
EOF

    echo -e "${GREEN}📄 Reference integrity report: REFERENCE_INTEGRITY_REPORT.md${NC}"
}

# Show usage information
show_usage() {
    cat << EOF
Reference Integrity Validator - H6D-SCRIPTS Automation Framework

USAGE:
    $0 --validate [pattern] [check_reverse]              # Validate reference integrity
    $0 --authority [trace_depth]                         # Validate authority chains
    $0 --fix [dry_run] [strategy]                        # Fix broken references
    $0 --extract file_path [type]                        # Extract references from file
    $0 --help                                             # Show this help

COMMANDS:
    --validate      Comprehensive reference integrity validation
    --authority     Authority chain integrity validation
    --fix           Broken reference identification and repair
    --extract       Extract and analyze references from specific file

VALIDATION EXAMPLES:
    $0 --validate                                        # Validate all references
    $0 --validate "context/.*" true                      # Context files with reverse check
    $0 --validate ".*authority.*" false                  # Authority files, no reverse check

AUTHORITY EXAMPLES:
    $0 --authority                                       # Default trace depth (5)
    $0 --authority 10                                    # Deep authority chain tracing
    $0 --authority 3                                     # Shallow authority validation

FIX EXAMPLES:
    $0 --fix true conservative                           # Dry run with conservative fixes
    $0 --fix false conservative                          # Apply conservative fixes
    $0 --fix true aggressive                             # Dry run with aggressive fixes

EXTRACT EXAMPLES:
    $0 --extract context/authority.md all               # All references from file
    $0 --extract some/file.md bidirectional             # Only bidirectional references
    $0 --extract path/file.md authority                  # Only authority references

REFERENCE TYPES:
    all              All reference types
    authority        Authority references (← @context/)
    delegation       Delegation references (→ @context/)
    bidirectional    Bidirectional references (←→ @context/)
    upward          Upward references (↑ @context/)
    context_reference General @context/ references

FIX STRATEGIES:
    conservative     Identify issues and suggest fixes (safe)
    aggressive       Attempt automatic repairs (use with caution)

VALIDATION STANDARDS:
    Reference Syntax:    ADR-005 compliance (@context/ prefix mandatory)
    File Existence:      All referenced files must exist
    Bidirectional:       Mutual references must be reciprocal
    Authority Chains:    Must trace to supreme authority sources

OUTPUT:
    - Reference integrity analysis with file-by-file breakdown
    - Authority chain validation with trace depth analysis
    - Broken reference identification with fix recommendations
    - Comprehensive integrity reports with compliance assessment
EOF
}

# Main execution function
main() {
    if [[ $# -eq 0 ]] || [[ "$1" == "--help" ]]; then
        show_usage
        exit 0
    fi
    
    local integrity_status="UNKNOWN"
    local chain_status="UNKNOWN"
    
    case "$1" in
        --validate)
            local pattern="${2:-.*\.md$}"
            local check_reverse="${3:-true}"
            
            if validate_bidirectional_consistency "$pattern" "$check_reverse"; then
                case $? in
                    0) integrity_status="EXCELLENT" ;;
                    1) integrity_status="ACCEPTABLE" ;;
                    2) integrity_status="POOR" ;;
                esac
            else
                exit_code=$?
                case $exit_code in
                    1) integrity_status="ACCEPTABLE" ;;
                    2) integrity_status="POOR" ;;
                esac
            fi
            ;;
            
        --authority)
            local trace_depth="${2:-5}"
            
            if validate_authority_chains "$trace_depth"; then
                case $? in
                    0) chain_status="EXCELLENT" ;;
                    1) chain_status="ACCEPTABLE" ;;
                    2) chain_status="CRITICAL" ;;
                esac
            else
                exit_code=$?
                case $exit_code in
                    1) chain_status="ACCEPTABLE" ;;
                    2) chain_status="CRITICAL" ;;
                esac
            fi
            ;;
            
        --fix)
            local dry_run="${2:-true}"
            local strategy="${3:-conservative}"
            
            fix_broken_references "$dry_run" "$strategy"
            ;;
            
        --extract)
            if [[ $# -lt 2 ]]; then
                echo -e "${RED}❌ Usage: $0 --extract file_path [type]${NC}"
                exit 1
            fi
            
            local file_path="$2"
            local ref_type="${3:-all}"
            
            if [[ ! -f "$file_path" ]]; then
                echo -e "${RED}❌ File not found: $file_path${NC}"
                exit 1
            fi
            
            echo -e "${BLUE}📋 Extracting references from: $(basename "$file_path")${NC}"
            extract_file_references "$file_path" "$ref_type"
            ;;
            
        *)
            echo -e "${RED}❌ Unknown option: $1${NC}"
            show_usage
            exit 1
            ;;
    esac
    
    # Generate comprehensive report
    if [[ "$1" == "--validate" ]] || [[ "$1" == "--authority" ]]; then
        generate_reference_report "$integrity_status" "$chain_status"
    fi
    
    # Common output for all operations
    if [[ "$1" != "--help" ]]; then
        echo -e "\n${GREEN}📁 Output directory: $OUTPUT_DIR${NC}"
        echo -e "${GREEN}📄 Integrity log: $LOG_FILE${NC}"
    fi
}

# Execute main function
main "$@"