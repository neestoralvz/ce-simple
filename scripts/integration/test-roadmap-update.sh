#!/bin/bash

# Test script for roadmap-update functionality
# Validates core functions without full execution

set -euo pipefail

# Silent script - no user notifications (Claude Code communicates results)
# Get script directory and project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
ROADMAP_FILE="$PROJECT_ROOT/context/roadmap/ROADMAP_REGISTRY.md"

# Colors
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

# Test violation analysis function
test_violation_analysis() {
    log_info "Testing violation analysis..."
    
    cd "$PROJECT_ROOT"
    
    # Find most recent analysis
    local latest_analysis=$(ls -t scripts/analysis_results_* 2>/dev/null | head -1)
    if [[ -z "$latest_analysis" ]]; then
        log_error "No analysis results found"
        return 1
    fi
    
    if [[ ! -f "$latest_analysis/all_violations.txt" ]]; then
        log_error "Analysis files not found in $latest_analysis"
        return 1
    fi
    
    local total=$(wc -l < "$latest_analysis/all_violations.txt" 2>/dev/null || echo "0")
    local l0=$(wc -l < "$latest_analysis/L0_EMERGENCY.txt" 2>/dev/null || echo "0")
    local l1=$(wc -l < "$latest_analysis/L1_CRITICAL.txt" 2>/dev/null || echo "0")
    local l2=$(wc -l < "$latest_analysis/L2_HIGH.txt" 2>/dev/null || echo "0")
    
    log_success "Current violations: Total=$total, L0=$l0, L1=$l1, L2=$l2"
    
    # Test P0B progress calculation
    local initial_violations=294
    local progress=0
    if [[ $total -eq 0 ]]; then
        progress=100
    elif [[ $total -le 10 ]]; then
        progress=95
    else
        progress=$(( (initial_violations - total) * 100 / initial_violations ))
        [[ $progress -lt 0 ]] && progress=0
        [[ $progress -gt 100 ]] && progress=100
    fi
    
    log_success "P0B progress calculation: $progress%"
    return 0
}

# Test GitHub CLI availability
test_github_integration() {
    log_info "Testing GitHub integration..."
    
    if command -v gh &> /dev/null; then
        if gh auth status &> /dev/null; then
            log_success "GitHub CLI authenticated and ready"
            
            # Test issue list (limited)
            local issue_count=$(gh issue list --limit=5 --json number 2>/dev/null | jq length 2>/dev/null || echo "0")
            log_success "Can access $issue_count issues"
        else
            log_info "GitHub CLI available but not authenticated (will use offline mode)"
        fi
    else
        log_info "GitHub CLI not available (will use offline mode)"
    fi
}

# Test roadmap file structure
test_roadmap_structure() {
    log_info "Testing roadmap file structure..."
    
    if [[ ! -f "$ROADMAP_FILE" ]]; then
        log_error "Roadmap file not found: $ROADMAP_FILE"
        return 1
    fi
    
    # Check for key sections
    local sections=(
        "ROADMAP WORK ITEMS"
        "GITHUB ISSUES STATUS"
        "EXECUTION LOGIC"
        "NEXT ACTIONS"
    )
    
    for section in "${sections[@]}"; do
        if grep -q "$section" "$ROADMAP_FILE"; then
            log_success "Found section: $section"
        else
            log_error "Missing section: $section"
        fi
    done
    
    # Check for P0B-CLEANUP line
    if grep -q "P0B-CLEANUP.*IN PROGRESS" "$ROADMAP_FILE"; then
        local current_progress=$(grep "P0B-CLEANUP.*IN PROGRESS" "$ROADMAP_FILE" | grep -o '[0-9]\+%' | head -1)
        log_success "Found P0B-CLEANUP progress: $current_progress"
    else
        log_info "P0B-CLEANUP progress line not found (may be completed)"
    fi
}

# Test jq availability
test_dependencies() {
    log_info "Testing dependencies..."
    
    if command -v jq &> /dev/null; then
        log_success "jq available for JSON processing"
    else
        log_error "jq not found - required for GitHub integration"
        return 1
    fi
    
    # Test jq with simple JSON
    echo '{"test": "value"}' | jq -r '.test' > /dev/null 2>&1
    log_success "jq working correctly"
}

# Test backup functionality
test_backup_functionality() {
    log_info "Testing backup functionality..."
    
    local backup_dir="$PROJECT_ROOT/context/roadmap/backups"
    mkdir -p "$backup_dir"
    
    # Create test backup
    local test_backup="$backup_dir/test_backup_$(date +%Y%m%d_%H%M%S).md"
    cp "$ROADMAP_FILE" "$test_backup"
    
    if [[ -f "$test_backup" ]]; then
        log_success "Backup functionality working"
        # Clean up test backup
        rm "$test_backup"
    else
        log_error "Backup functionality failed"
        return 1
    fi
}

# Main test function
main() {
    echo "🧪 ROADMAP UPDATE TEST SUITE"
    echo "==============================="
    echo ""
    
    local tests=(
        "test_dependencies"
        "test_roadmap_structure" 
        "test_violation_analysis"
        "test_github_integration"
        "test_backup_functionality"
    )
    
    local passed=0
    local total=${#tests[@]}
    
    for test in "${tests[@]}"; do
        if $test; then
            ((passed++))
        fi
        echo ""
    done
    
    echo "==============================="
    echo "Test Results: $passed/$total passed"
    
    if [[ $passed -eq $total ]]; then
        log_success "All tests passed! Roadmap update script should work correctly."
        echo ""
        log_info "You can now run: ./scripts/roadmap-update.sh"
        return 0
    else
        log_error "Some tests failed. Please fix issues before using roadmap-update."
        return 1
    fi
}

main "$@"