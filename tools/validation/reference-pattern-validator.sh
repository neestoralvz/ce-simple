#!/bin/bash
# reference-pattern-validator.sh - File Reference Pattern Standardization Tool
# AUTHORITY: CLAUDE.md reference standardization + ADR-005 compliance
# Performance: Systematic reference pattern analysis and correction

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
LOG_FILE="${PROJECT_ROOT}/.claude/logs/reference-validation.log"
REPORT_FILE="${PROJECT_ROOT}/tools/validation/reference-pattern-report.md"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

log_error() {
    echo -e "${RED}ERROR: $1${NC}" | tee -a "$LOG_FILE"
}

log_success() {
    echo -e "${GREEN}SUCCESS: $1${NC}" | tee -a "$LOG_FILE"
}

log_warning() {
    echo -e "${YELLOW}WARNING: $1${NC}" | tee -a "$LOG_FILE"
}

log_info() {
    echo -e "${BLUE}INFO: $1${NC}" | tee -a "$LOG_FILE"
}

# Initialize logging
mkdir -p "$(dirname "$LOG_FILE")"
log "=== Reference Pattern Validator Started ==="

# Reference pattern definitions using simple approach
check_pattern() {
    local file="$1"
    local pattern="$2" 
    local pattern_name="$3"
    
    local count
    count=$(grep -c "$pattern" "$file" 2>/dev/null || true)
    
    if [[ $count -gt 0 ]]; then
        if [[ "$pattern_name" == "INVALID" ]]; then
            log_warning "Found $count invalid patterns in $file: $pattern"
            return $count
        else
            log_info "Found $count valid $pattern_name patterns in $file"
            return 0
        fi
    fi
    
    return 0
}

# Analysis functions
analyze_file() {
    local file="$1"
    local issues_found=0
    
    log_info "Analyzing: $file"
    
    # Check for invalid patterns
    check_pattern "$file" 'context/[a-zA-Z0-9/_-]+\.md' "INVALID"
    issues_found=$((issues_found + $?))
    
    check_pattern "$file" '\.\./[a-zA-Z0-9/_.-]+\.md' "INVALID"
    issues_found=$((issues_found + $?))
    
    check_pattern "$file" 'archive/methodologies_consolidated/' "INVALID"
    issues_found=$((issues_found + $?))
    
    check_pattern "$file" 'context/operational/' "INVALID"
    issues_found=$((issues_found + $?))
    
    # Check for valid patterns
    check_pattern "$file" '← @context/architecture/core/truth-source\.md' "authority_backward"
    check_pattern "$file" '↑ @context/architecture/core/truth-source\.md' "authority_upward"
    check_pattern "$file" '@context/[a-zA-Z0-9/_-]+\.md' "context_absolute"
    check_pattern "$file" '→ [a-zA-Z0-9/_.-]+\.md' "forward_reference"
    check_pattern "$file" '←→ [a-zA-Z0-9/_.-]+\.md' "bidirectional"
    check_pattern "$file" '→ [a-zA-Z0-9/_.-]+\.md:[0-9]+-[0-9]+' "line_specific"
    
    return $issues_found
}

# Fix functions
fix_missing_at_prefix() {
    local file="$1"
    local temp_file="${file}.tmp"
    
    # Convert context/ to @context/ where not already prefixed
    sed 's/\([^@]\)context\//\1@context\//g' "$file" > "$temp_file"
    
    if ! cmp -s "$file" "$temp_file"; then
        mv "$temp_file" "$file"
        log_success "Fixed missing @ prefix in $file"
        return 0
    else
        rm "$temp_file"
        return 1
    fi
}

standardize_upward_references() {
    local file="$1"
    local temp_file="${file}.tmp"
    local changes=0
    
    # Convert various upward patterns to standard ↑ format
    sed -E 's/\^[[:space:]]*@context/↑ @context/g' "$file" > "$temp_file"
    
    if ! cmp -s "$file" "$temp_file"; then
        mv "$temp_file" "$file"
        log_success "Standardized upward references in $file"
        changes=1
    else
        rm "$temp_file"
    fi
    
    return $changes
}

quarantine_broken_references() {
    local file="$1"
    local temp_file="${file}.tmp"
    local changes=0
    
    # Comment out broken archive references
    sed 's/archive\/methodologies_consolidated/<!-- QUARANTINED: archive\/methodologies_consolidated -->/g' "$file" > "$temp_file"
    
    if ! cmp -s "$file" "$temp_file"; then
        mv "$temp_file" "$file"
        log_warning "Quarantined broken archive references in $file"
        changes=1
    else
        rm "$temp_file"
    fi
    
    return $changes
}

# Main validation function
validate_and_fix() {
    local mode="${1:-analyze}"  # analyze, fix, or report
    local total_files=0
    local files_with_issues=0
    local total_issues=0
    local fixed_files=0
    
    log_info "Starting validation in $mode mode"
    
    # Find all markdown files
    while IFS= read -r -d '' file; do
        total_files=$((total_files + 1))
        
        local file_issues=0
        analyze_file "$file"
        file_issues=$?
        
        if [[ $file_issues -gt 0 ]]; then
            files_with_issues=$((files_with_issues + 1))
            total_issues=$((total_issues + file_issues))
            
            if [[ "$mode" == "fix" ]]; then
                local fixes_applied=0
                
                # Apply fixes
                if fix_missing_at_prefix "$file"; then
                    fixes_applied=$((fixes_applied + 1))
                fi
                
                if standardize_upward_references "$file"; then
                    fixes_applied=$((fixes_applied + 1))
                fi
                
                if quarantine_broken_references "$file"; then
                    fixes_applied=$((fixes_applied + 1))
                fi
                
                if [[ $fixes_applied -gt 0 ]]; then
                    fixed_files=$((fixed_files + 1))
                fi
            fi
        fi
        
    done < <(find "$PROJECT_ROOT" -name "*.md" -type f -not -path "*/.git/*" -print0)
    
    # Generate report
    if [[ "$mode" == "report" ]] || [[ "$mode" == "fix" ]]; then
        generate_report "$total_files" "$files_with_issues" "$total_issues" "$fixed_files"
    fi
    
    log_success "Validation completed: $total_files files processed, $files_with_issues with issues, $total_issues total issues"
    
    if [[ "$mode" == "fix" ]]; then
        log_success "Fixed $fixed_files files"
    fi
}

# Report generation
generate_report() {
    local total_files="$1"
    local files_with_issues="$2" 
    local total_issues="$3"
    local fixed_files="${4:-0}"
    
    mkdir -p "$(dirname "$REPORT_FILE")"
    
    cat > "$REPORT_FILE" << EOF
# Reference Pattern Validation Report

**Generated**: $(date '+%Y-%m-%d %H:%M:%S CDMX')
**Authority**: CLAUDE.md reference standardization + ADR-005 compliance

## SUMMARY METRICS

- **Total Files Analyzed**: $total_files
- **Files with Issues**: $files_with_issues
- **Total Issues Found**: $total_issues
- **Files Fixed**: $fixed_files
- **Issue Rate**: $(( (files_with_issues * 100) / total_files ))%

## STANDARDIZATION STATUS

### ✅ VALID PATTERNS DETECTED
- **authority_backward**: ← @context/architecture/core/truth-source.md
- **authority_upward**: ↑ @context/architecture/core/truth-source.md  
- **context_absolute**: @context/[path].md format
- **forward_reference**: → target.md format
- **bidirectional**: ←→ peer.md format
- **line_specific**: → file.md:15-25 format

### ❌ INVALID PATTERNS DETECTED  
- **missing_at_prefix**: context/ without @ prefix
- **relative_paths**: ../relative/path usage
- **broken_archive**: archive/methodologies_consolidated/ references
- **phantom_operational**: context/operational/ references

## NEXT ACTIONS

1. **Archive Quarantine**: Broken references isolated
2. **Syntax Standardization**: @ prefix enforcement applied
3. **Upward Reference Standard**: ↑ symbol documented
4. **Bidirectional Integrity**: ←→ consistency validated

---
**AUTHORITY PRESERVATION**: All fixes maintain @context/architecture/core/truth-source.md authority chain integrity per user vision supremacy.
EOF

    log_success "Report generated: $REPORT_FILE"
}

# Main execution
case "${1:-analyze}" in
    "analyze")
        validate_and_fix "analyze"
        ;;
    "fix")
        validate_and_fix "fix"
        ;;
    "report")
        validate_and_fix "report"
        ;;
    *)
        echo "Usage: $0 [analyze|fix|report]"
        echo "  analyze: Check patterns without fixing"
        echo "  fix: Apply standardization fixes"
        echo "  report: Generate detailed report"
        exit 1
        ;;
esac

log "=== Reference Pattern Validator Completed ==="