#!/bin/bash
# quality-gate.sh - Quality assurance validation for /core protocol
# Validates task completion against quality standards

set -euo pipefail

# Configuration
TEMP_DIR=$(mktemp -d)
LOG_FILE="$TEMP_DIR/quality-gate.log"
QUALITY_REPORT="$TEMP_DIR/quality_report.md"

# Cleanup
cleanup() {
    rm -rf "$TEMP_DIR"
}
trap cleanup EXIT

# Log function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

# Quality checks
check_file_sizes() {
    log "Checking file size compliance (≤80 lines)"
    local violations=0
    
    echo "## File Size Violations" >> "$QUALITY_REPORT"
    
    while IFS= read -r file; do
        if [[ -f "$file" ]] && [[ "$file" == *.md ]]; then
            local lines=$(wc -l < "$file")
            if (( lines > 80 )); then
                echo "- $file: $lines lines (violation)" >> "$QUALITY_REPORT"
                ((violations++))
            fi
        fi
    done < <(find . -name "*.md" -not -path "./.git/*" -not -path "./scripts/*" 2>/dev/null)
    
    if (( violations == 0 )); then
        echo "✅ No file size violations" >> "$QUALITY_REPORT"
    else
        echo "❌ Found $violations file size violations" >> "$QUALITY_REPORT"
    fi
    
    log "File size check: $violations violations"
    return $violations
}

check_authority_chain() {
    log "Checking authority chain integrity"
    local violations=0
    
    echo "## Authority Chain Validation" >> "$QUALITY_REPORT"
    
    # Check for AUTORIDAD SUPREMA declarations
    local files_with_authority=0
    while IFS= read -r file; do
        if [[ -f "$file" ]] && grep -q "AUTORIDAD SUPREMA" "$file" 2>/dev/null; then
            ((files_with_authority++))
        fi
    done < <(find context/ -name "*.md" 2>/dev/null)
    
    echo "- Files with authority declarations: $files_with_authority" >> "$QUALITY_REPORT"
    
    # Check for broken references
    local broken_refs=0
    while IFS= read -r file; do
        if [[ -f "$file" ]]; then
            while IFS= read -r ref; do
                local target_file="${ref#@}"
                if [[ ! -f "$target_file" ]]; then
                    echo "- Broken reference in $file: $ref" >> "$QUALITY_REPORT"
                    ((broken_refs++))
                fi
            done < <(grep -o '@[^[:space:]]*\.md' "$file" 2>/dev/null || true)
        fi
    done < <(find . -name "*.md" -not -path "./.git/*" 2>/dev/null)
    
    if (( broken_refs == 0 )); then
        echo "✅ No broken references found" >> "$QUALITY_REPORT"
    else
        echo "❌ Found $broken_refs broken references" >> "$QUALITY_REPORT"
        violations=$broken_refs
    fi
    
    log "Authority chain check: $violations violations"
    return $violations
}

check_todo_completion() {
    log "Checking TodoWrite completion status"
    
    echo "## TodoWrite Status" >> "$QUALITY_REPORT"
    
    # This would integrate with TodoWrite tool results
    # For now, just document the requirement
    echo "- TodoWrite completion verification required" >> "$QUALITY_REPORT"
    echo "- All tasks should be marked as completed" >> "$QUALITY_REPORT"
    
    log "TodoWrite check: Manual verification required"
    return 0
}

check_git_state() {
    log "Checking git repository state"
    local violations=0
    
    echo "## Git Repository State" >> "$QUALITY_REPORT"
    
    # Check for uncommitted changes
    if ! git diff --quiet 2>/dev/null; then
        echo "❌ Uncommitted changes in working directory" >> "$QUALITY_REPORT"
        ((violations++))
    else
        echo "✅ Working directory clean" >> "$QUALITY_REPORT"
    fi
    
    # Check for staged changes
    if ! git diff --cached --quiet 2>/dev/null; then
        echo "⚠️ Staged changes present" >> "$QUALITY_REPORT"
    else
        echo "✅ No staged changes" >> "$QUALITY_REPORT"
    fi
    
    # Check current branch
    local current_branch=$(git branch --show-current 2>/dev/null || echo "unknown")
    echo "- Current branch: $current_branch" >> "$QUALITY_REPORT"
    
    log "Git state check: $violations violations"
    return $violations
}

generate_summary() {
    local total_violations=$1
    
    echo "# Quality Gate Report" > "$QUALITY_REPORT.tmp"
    echo "**Generated**: $(date)" >> "$QUALITY_REPORT.tmp"
    echo "" >> "$QUALITY_REPORT.tmp"
    
    if (( total_violations == 0 )); then
        echo "## ✅ QUALITY GATE PASSED" >> "$QUALITY_REPORT.tmp"
        echo "All quality checks completed successfully." >> "$QUALITY_REPORT.tmp"
    else
        echo "## ❌ QUALITY GATE FAILED" >> "$QUALITY_REPORT.tmp"
        echo "Found $total_violations total violations." >> "$QUALITY_REPORT.tmp"
    fi
    
    echo "" >> "$QUALITY_REPORT.tmp"
    cat "$QUALITY_REPORT" >> "$QUALITY_REPORT.tmp"
    mv "$QUALITY_REPORT.tmp" "$QUALITY_REPORT"
}

# Main execution
main() {
    local action="${1:-validate}"
    
    case "$action" in
        "validate")
            log "Starting quality gate validation"
            
            local total_violations=0
            
            check_file_sizes || total_violations=$((total_violations + $?))
            check_authority_chain || total_violations=$((total_violations + $?))
            check_todo_completion || total_violations=$((total_violations + $?))
            check_git_state || total_violations=$((total_violations + $?))
            
            generate_summary $total_violations
            
            log "Quality gate validation completed"
            log "Total violations: $total_violations"
            
            # Output summary
            cat "$QUALITY_REPORT"
            
            # Return exit code based on violations
            if (( total_violations == 0 )); then
                log "✅ QUALITY GATE PASSED"
                return 0
            else
                log "❌ QUALITY GATE FAILED"
                return 1
            fi
            ;;
        "help"|*)
            echo "Usage: $0 [validate|help]"
            echo ""
            echo "validate: Run all quality checks (default)"
            echo "help: Show this help"
            ;;
    esac
}

main "$@"