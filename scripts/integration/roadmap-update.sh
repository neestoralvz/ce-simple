#!/bin/bash

# Roadmap Update Script - Enhanced Version
# Actualización inteligente y automática del ROADMAP_REGISTRY.md
# Integra con GitHub CLI, análisis de violaciones y progreso real
# 31/07/2025 CDMX | Enhanced with comprehensive automation

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="/Users/nalve/ce-simple"
ROADMAP_FILE="$PROJECT_ROOT/context/roadmap/ROADMAP_REGISTRY.md"
TEMP_DIR=$(mktemp -d)
trap 'rm -rf "$TEMP_DIR"' EXIT

# Enhanced configuration
SCRIPT_VERSION="2.0"
GITHUB_RATE_LIMIT_DELAY=1
MAX_RETRIES=3

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log_info() { echo -e "${BLUE}ℹ${NC} $1"; }
log_success() { echo -e "${GREEN}✅${NC} $1"; }
log_warning() { echo -e "${YELLOW}⚠${NC} $1"; }
log_error() { echo -e "${RED}❌${NC} $1"; }

# Source analysis functions
source_analysis_functions() {
    # Embed key analysis functions directly
    
    analyze_current_violations() {
        cd "$PROJECT_ROOT"
        
        # Run fresh violation analysis
        log_info "Running violation analysis..."
        if ! ./scripts/analyze_violations.sh > /dev/null 2>&1; then
            log_warning "Violation analysis failed, using cached results"
        fi
        
        # Find latest analysis results
        local latest_analysis=$(ls -td scripts/analysis_results_* 2>/dev/null | head -1)
        if [[ ! -d "$latest_analysis" ]]; then
            log_warning "No analysis results found, assuming zero violations"
            echo "0 0 0 0"
            return
        fi
        
        # Extract violation counts with error handling
        local total=$(wc -l < "$latest_analysis/all_violations.txt" 2>/dev/null || echo "0")
        local l0=$(wc -l < "$latest_analysis/L0_EMERGENCY.txt" 2>/dev/null || echo "0")
        local l1=$(wc -l < "$latest_analysis/L1_CRITICAL.txt" 2>/dev/null || echo "0")
        local l2=$(wc -l < "$latest_analysis/L2_HIGH.txt" 2>/dev/null || echo "0")
        
        log_info "Violations found: Total=$total, L0=$l0, L1=$l1, L2=$l2"
        echo "$total $l0 $l1 $l2"
    }
    
    # Silent version for command substitution (no log output)
    get_current_violations_silent() {
        cd "$PROJECT_ROOT"
        
        # Find latest analysis results
        local latest_analysis=$(ls -td scripts/analysis_results_* 2>/dev/null | head -1)
        if [[ ! -d "$latest_analysis" ]]; then
            echo "0 0 0 0"
            return
        fi
        
        # Extract violation counts with error handling and strip whitespace
        local total=$(wc -l < "$latest_analysis/all_violations.txt" 2>/dev/null | tr -d ' ' || echo "0")
        local l0=$(wc -l < "$latest_analysis/L0_EMERGENCY.txt" 2>/dev/null | tr -d ' ' || echo "0")
        local l1=$(wc -l < "$latest_analysis/L1_CRITICAL.txt" 2>/dev/null | tr -d ' ' || echo "0")
        local l2=$(wc -l < "$latest_analysis/L2_HIGH.txt" 2>/dev/null | tr -d ' ' || echo "0")
        
        echo "$total $l0 $l1 $l2"
    }
    
    analyze_work_item_completions() {
        local roadmap_file="$1"
        local completions=()
        
        # Check for completed handoff markers in git history
        local recent_commits=$(git log --oneline --since="24 hours ago" --grep="HANDOFF.*COMPLETED\|✅.*COMPLETED" || echo "")
        
        # Analyze repository state for completion indicators
        while IFS= read -r line; do
            if [[ $line =~ \*\*🔄([^*]+)\*\*.*🔄.*READY ]]; then
                local work_item="${BASH_REMATCH[1]}"
                # Check if work item directory exists and has completion markers
                if check_work_item_completion "$work_item"; then
                    completions+=("$work_item")
                fi
            fi
        done < "$roadmap_file"
        
        printf '%s\n' "${completions[@]}"
    }
    
    check_work_item_completion() {
        local work_item="$1"
        
        # Define completion criteria for different work items
        case "$work_item" in
            "P0B-CLEANUP")
                # P0B is complete when violations drop below threshold
                local violation_data=$(get_current_violations_silent)
                local total_violations=$(echo "$violation_data" | cut -d' ' -f1)
                [[ "$total_violations" -le 10 ]]
                ;;
            "H"*|"P"[1-9]*)
                # Handoffs and Phases require manual validation - NEVER auto-complete
                return 1
                ;;
            *)
                return 1  # Unknown work item - require manual validation
                ;;
        esac
    }
    
    calculate_p0b_progress() {
        local current_violations="$1"
        local initial_violations=294  # P0B initial count from dashboard
        
        if [[ "$current_violations" -eq 0 ]]; then
            echo "100"
        elif [[ "$current_violations" -le 10 ]]; then
            echo "95"  # Near completion threshold
        else
            local progress=$(( (initial_violations - current_violations) * 100 / initial_violations ))
            [[ $progress -lt 0 ]] && progress=0
            [[ $progress -gt 100 ]] && progress=100
            echo "$progress"
        fi
    }
    
    sync_github_issues() {
        local temp_file="$TEMP_DIR/github_issues.json"
        if command -v gh &> /dev/null && gh auth status &> /dev/null; then
            gh issue list --state=all --limit=100 --json number,title,state > "$temp_file" 2>/dev/null || {
                log_warning "Failed to sync with GitHub, using offline mode"
                echo "[]" > "$temp_file"
            }
        else
            log_warning "GitHub CLI not available, using offline mode"
            echo "[]" > "$temp_file"
        fi
        echo "$temp_file"
    }
}

# Initialize analysis functions
source_analysis_functions

# Backup roadmap before modifications
backup_roadmap() {
    local backup_dir="$PROJECT_ROOT/context/roadmap/backups"
    mkdir -p "$backup_dir"
    local backup_file="$backup_dir/ROADMAP_REGISTRY_$(date +%Y%m%d_%H%M%S).md"
    cp "$ROADMAP_FILE" "$backup_file"
    log_info "Backup created: $(basename "$backup_file")"
}

# Update work item progress in roadmap
update_work_item_progress() {
    local roadmap_file="$1"
    local temp_file="$TEMP_DIR/roadmap_temp.md"
    local changes=()
    
    # Get current violation metrics
    local violation_data=$(get_current_violations_silent)
    local total_violations=$(echo "$violation_data" | cut -d' ' -f1)
    local p0b_progress=$(calculate_p0b_progress "$total_violations")
    
    log_info "Current violations: $total_violations, P0B progress: $p0b_progress%"
    
    # Update P0B-CLEANUP progress in simplified structure
    while IFS= read -r line; do
        if [[ $line =~ \|\s*\*\*🔄P0B-CLEANUP\*\*.*\|\s*🔄\s*([0-9]+)%\s*IN\s*PROGRESS ]]; then
            local old_progress="${BASH_REMATCH[1]}"
            if [[ "$old_progress" != "$p0b_progress" ]]; then
                line=$(echo "$line" | sed "s/🔄 ${old_progress}% IN PROGRESS/🔄 ${p0b_progress}% IN PROGRESS/")
                changes+=("P0B-CLEANUP progress updated: ${old_progress}% → ${p0b_progress}%")
            fi
        fi
        
        # Update violations count in summary section
        if [[ $line =~ "Violations.*([0-9]+)\s*remaining" ]]; then
            local old_violations="${BASH_REMATCH[1]}"
            if [[ "$old_violations" != "$total_violations" ]]; then
                line=$(echo "$line" | sed "s/Violations.*[0-9]*\s*remaining/Violations**: $total_violations remaining/")
                changes+=("Violation count updated: $old_violations → $total_violations")
            fi
        fi
        
        echo "$line" >> "$temp_file"
    done < "$roadmap_file"
    
    mv "$temp_file" "$roadmap_file"
    [[ ${#changes[@]} -gt 0 ]] && printf '%s\n' "${changes[@]}"
}

# Update GitHub issue states
update_github_issues() {
    local roadmap_file="$1"
    local github_data="$2"
    local temp_file="$TEMP_DIR/roadmap_github.md"
    local changes=()
    
    if [[ ! -f "$github_data" ]] || [[ "$(cat "$github_data")" == "[]" ]]; then
        log_warning "No GitHub data available, skipping issue updates"
        return
    fi
    
    while IFS= read -r line; do
        # Update GitHub issues in simplified CRITICAL ISSUES section
        if [[ $line =~ \|\s*\*\*#([0-9]+)\*\*.*\|\s*(🟡\s*OPEN|✅\s*CLOSED) ]]; then
            local issue_number="${BASH_REMATCH[1]}"
            local current_status="${BASH_REMATCH[2]}"
            local github_state=$(jq -r ".[] | select(.number==$issue_number) | .state" "$github_data" 2>/dev/null || echo "null")
            
            if [[ "$github_state" == "CLOSED" && "$current_status" =~ "OPEN" ]]; then
                line=$(echo "$line" | sed 's/🟡 OPEN/✅ CLOSED/')
                changes+=("Issue #$issue_number closed")
            elif [[ "$github_state" == "OPEN" && "$current_status" =~ "CLOSED" ]]; then
                line=$(echo "$line" | sed 's/✅ CLOSED/🟡 OPEN/')
                changes+=("Issue #$issue_number reopened")
            fi
        fi
        echo "$line" >> "$temp_file"
    done < "$roadmap_file"
    
    mv "$temp_file" "$roadmap_file"
    [[ ${#changes[@]} -gt 0 ]] && printf '%s\n' "${changes[@]}"
}

# Update dependency states based on progress
update_dependency_states() {
    local roadmap_file="$1"
    local temp_file="$TEMP_DIR/roadmap_deps.md"
    local changes=()
    
    # Check P0B completion status
    local violation_data=$(get_current_violations_silent)
    local total_violations=$(echo "$violation_data" | cut -d' ' -f1)
    local p0b_ready=$([[ $total_violations -le 10 ]] && echo "true" || echo "false")
    
    while IFS= read -r line; do
        if [[ "$p0b_ready" == "true" ]]; then
            # Unblock items waiting for P0B
            if [[ $line =~ "⏸️ BLOCKED by P0B" ]]; then
                line=$(echo "$line" | sed 's/⏸️ BLOCKED by P0B/🟡 READY/')
                changes+=("Unblocked by P0B completion: $(echo "$line" | grep -o '\*\*[^*]*\*\*' | head -1)")
            fi
            if [[ $line =~ "⏸️ Blocked by P0B" ]]; then
                line=$(echo "$line" | sed 's/⏸️ Blocked by P0B/🟡 READY/')
                changes+=("Issue unblocked by P0B completion: $(echo "$line" | grep -o '#[0-9]*' | head -1)")
            fi
        fi
        
        echo "$line" >> "$temp_file"
    done < "$roadmap_file"
    
    mv "$temp_file" "$roadmap_file"
    [[ ${#changes[@]} -gt 0 ]] && printf '%s\n' "${changes[@]}"
}

# Generate comprehensive change report
generate_change_report() {
    local all_changes=("$@")
    local report_file="$TEMP_DIR/update_report.md"
    
    cat > "$report_file" << EOF
# 🔄 ROADMAP UPDATE REPORT
**Date**: $(date)
**Script**: roadmap-update.sh

## 📊 Current Metrics
EOF
    
    # Add current metrics
    local violation_data=$(get_current_violations_silent)
    local total_violations=$(echo "$violation_data" | cut -d' ' -f1)
    local p0b_progress=$(calculate_p0b_progress "$total_violations")
    
    cat >> "$report_file" << EOF
- **Total Violations**: $total_violations files
- **P0B Progress**: $p0b_progress%
- **Analysis Time**: $(date)

## 🔄 Changes Detected
EOF
    
    if [[ ${#all_changes[@]} -eq 0 ]]; then
        echo "✅ No changes detected - roadmap is up to date" >> "$report_file"
    else
        echo "📋 The following changes were applied:" >> "$report_file"
        for change in "${all_changes[@]}"; do
            [[ -n "$change" ]] && echo "- $change" >> "$report_file"
        done
    fi
    
    # Add unblocking opportunities
    if [[ $total_violations -le 10 ]]; then
        cat >> "$report_file" << EOF

## 🚀 Unblocking Opportunities
- ✅ P0B-CLEANUP near completion enables:
  - P1-UX-FIX can start
  - Critical Issues (#35, #34, #20) can be worked on
  - 6 blocked issues can proceed
EOF
    fi
    
    cat >> "$report_file" << EOF

---
**Dashboard Status**: Updated and synchronized
**Next Update**: Run \`roadmap-update\` anytime for fresh status
EOF
    
    # Display report
    echo ""
    log_success "UPDATE COMPLETE"
    echo ""
    cat "$report_file"
    
    # Save report to roadmap directory
    cp "$report_file" "$PROJECT_ROOT/context/roadmap/last_update_report.md"
}

# Main update function
main() {
    log_info "Starting roadmap update..."
    
    # Verify roadmap file exists
    if [[ ! -f "$ROADMAP_FILE" ]]; then
        log_error "Roadmap file not found: $ROADMAP_FILE"
        exit 1
    fi
    
    # Create backup
    backup_roadmap
    
    # Collect all changes
    local all_changes=()
    
    # Sync with GitHub
    log_info "Syncing with GitHub issues..."
    local github_data=$(sync_github_issues)
    # Collect changes from each update step
    local github_changes_output=$(update_github_issues "$ROADMAP_FILE" "$github_data" 2>/dev/null || true)
    [[ -n "$github_changes_output" ]] && all_changes+=("$github_changes_output")
    
    # Update work item progress
    log_info "Analyzing work item progress..."
    local progress_changes_output=$(update_work_item_progress "$ROADMAP_FILE" 2>/dev/null || true)
    [[ -n "$progress_changes_output" ]] && all_changes+=("$progress_changes_output")
    
    # Update dependencies
    log_info "Updating dependency states..."
    local dependency_changes_output=$(update_dependency_states "$ROADMAP_FILE" 2>/dev/null || true)
    [[ -n "$dependency_changes_output" ]] && all_changes+=("$dependency_changes_output")
    
    # Generate and display report
    generate_change_report "${all_changes[@]}"
}

# Show usage if requested
if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
    cat << EOF
Roadmap Update Script

USAGE:
    $0                  Update roadmap with current status
    $0 --help          Show this help message

DESCRIPTION:
    Automatically synchronizes ROADMAP_REGISTRY.md with:
    - GitHub issue states (open/closed)
    - File violation metrics from analyze_violations.sh
    - Work item progress calculations
    - Dependency state updates

OUTPUT:
    - Updated ROADMAP_REGISTRY.md
    - Backup in context/roadmap/backups/
    - Update report in context/roadmap/last_update_report.md

REQUIREMENTS:
    - GitHub CLI (gh) for issue synchronization (optional)
    - analyze_violations.sh script in scripts/
    - jq for JSON processing
EOF
    exit 0
fi

# Check dependencies
if ! command -v jq &> /dev/null; then
    log_error "jq is required for JSON processing"
    exit 1
fi

# Run main function
cd "$PROJECT_ROOT"
main "$@"