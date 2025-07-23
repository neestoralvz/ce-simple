#!/bin/bash

# Validation Suite
# Comprehensive system validation and migration failure detection
# Usage: ./validation-suite.sh [validation-type] [options]

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
LOG_DIR="$SCRIPT_DIR/logs"
VALIDATION_LOG="$LOG_DIR/validation-$(date +%Y%m%d_%H%M%S).log"

mkdir -p "$LOG_DIR"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

# Logging with file output
exec 1> >(tee -a "$VALIDATION_LOG")
exec 2> >(tee -a "$VALIDATION_LOG" >&2)

log_info() {
    echo -e "${BLUE}[INFO]${NC} $(date '+%H:%M:%S') - $1"
}

log_success() {
    echo -e "${GREEN}[PASS]${NC} $(date '+%H:%M:%S') - $1"
}

log_warning() {
    echo -e "${YELLOW}[WARN]${NC} $(date '+%H:%M:%S') - $1"
}

log_error() {
    echo -e "${RED}[FAIL]${NC} $(date '+%H:%M:%S') - $1"
}

log_section() {
    echo -e "${CYAN}[SECTION]${NC} $1"
    echo "=================================================="
}

# Global validation results
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0
WARNING_TESTS=0

# Test result tracking
record_test() {
    local result="$1"
    local test_name="$2"
    
    ((TOTAL_TESTS++))
    
    case "$result" in
        "PASS")
            ((PASSED_TESTS++))
            log_success "$test_name"
            ;;
        "FAIL")
            ((FAILED_TESTS++))
            log_error "$test_name"
            ;;
        "WARN")
            ((WARNING_TESTS++))
            log_warning "$test_name"
            ;;
    esac
}

# Core System Validation
validate_core_system() {
    log_section "Core System Validation"
    
    cd "$PROJECT_ROOT"
    
    # Test 1: Critical files exist
    local critical_files=("CLAUDE.md" "README.md")
    for file in "${critical_files[@]}"; do
        if [[ -f "$file" ]]; then
            record_test "PASS" "Critical file exists: $file"
        else
            record_test "FAIL" "Critical file missing: $file"
        fi
    done
    
    # Test 2: Commands directory structure
    if [[ -d "commands" ]]; then
        local cmd_count=$(find commands -name "*.md" -type f | wc -l)
        if [[ $cmd_count -gt 0 ]]; then
            record_test "PASS" "Commands directory has $cmd_count commands"
        else
            record_test "FAIL" "Commands directory is empty"
        fi
    else
        record_test "FAIL" "Commands directory missing"
    fi
    
    # Test 3: Documentation structure
    if [[ -d "docs" ]]; then
        local doc_count=$(find docs -name "*.md" -type f | wc -l)
        if [[ $doc_count -gt 0 ]]; then
            record_test "PASS" "Documentation has $doc_count files"
        else
            record_test "WARN" "Documentation directory is empty"
        fi
    else
        record_test "WARN" "Documentation directory missing"
    fi
    
    # Test 4: Essential command presence
    local essential_commands=("start.md" "explore-codebase.md" "capture-learnings.md")
    for cmd in "${essential_commands[@]}"; do
        if find commands -name "$cmd" -type f | grep -q .; then
            record_test "PASS" "Essential command found: $cmd"
        else
            record_test "FAIL" "Essential command missing: $cmd"
        fi
    done
}

# Git Repository Validation
validate_git_repository() {
    log_section "Git Repository Validation"
    
    cd "$PROJECT_ROOT"
    
    # Test 1: Git repository exists and is functional
    if git status >/dev/null 2>&1; then
        record_test "PASS" "Git repository is functional"
    else
        record_test "FAIL" "Git repository is corrupted or missing"
        return
    fi
    
    # Test 2: Git configuration
    if git config user.name >/dev/null 2>&1 && git config user.email >/dev/null 2>&1; then
        record_test "PASS" "Git user configuration present"
    else
        record_test "WARN" "Git user configuration missing"
    fi
    
    # Test 3: Working directory status
    local git_status_output=$(git status --porcelain 2>/dev/null || echo "")
    local modified_files=$(echo "$git_status_output" | grep -c "^ M" || echo "0")
    local deleted_files=$(echo "$git_status_output" | grep -c "^ D" || echo "0")
    local untracked_files=$(echo "$git_status_output" | grep -c "^??" || echo "0")
    
    if [[ $deleted_files -gt 100 ]]; then
        record_test "FAIL" "Excessive deleted files detected: $deleted_files (possible migration issue)"
    elif [[ $deleted_files -gt 0 ]]; then
        record_test "WARN" "Deleted files detected: $deleted_files"
    else
        record_test "PASS" "No deleted files detected"
    fi
    
    # Test 4: Recent commits integrity
    local recent_commits=$(git log --oneline -5 2>/dev/null | wc -l)
    if [[ $recent_commits -gt 0 ]]; then
        record_test "PASS" "Git history accessible ($recent_commits recent commits)"
    else
        record_test "FAIL" "Git history not accessible"
    fi
    
    # Test 5: Branch status
    local current_branch=$(git branch --show-current 2>/dev/null || echo "")
    if [[ -n "$current_branch" ]]; then
        record_test "PASS" "Currently on branch: $current_branch"
    else
        record_test "WARN" "Detached HEAD state detected"
    fi
}

# File Integrity Validation
validate_file_integrity() {
    log_section "File Integrity Validation"
    
    cd "$PROJECT_ROOT"
    
    # Test 1: File permissions
    local permission_issues=0
    while IFS= read -r file; do
        if [[ -f "$file" && ! -r "$file" ]]; then
            log_error "File not readable: $file"
            ((permission_issues++))
        fi
    done < <(find . -name "*.md" -o -name "*.sh" -o -name "*.json" | grep -v ".git/")
    
    if [[ $permission_issues -eq 0 ]]; then
        record_test "PASS" "All files have correct permissions"
    else
        record_test "FAIL" "$permission_issues files have permission issues"
    fi
    
    # Test 2: File encoding validation (UTF-8)
    local encoding_issues=0
    while IFS= read -r file; do
        if [[ -f "$file" ]]; then
            if ! file "$file" | grep -q "UTF-8"; then
                local encoding=$(file "$file" | cut -d: -f2)
                log_warning "Non-UTF-8 encoding detected: $file ($encoding)"
                ((encoding_issues++))
            fi
        fi
    done < <(find . -name "*.md" | head -20)  # Sample check
    
    if [[ $encoding_issues -eq 0 ]]; then
        record_test "PASS" "File encoding validation passed"
    else
        record_test "WARN" "$encoding_issues files have encoding issues"
    fi
    
    # Test 3: Large file detection
    local large_files=0
    while IFS= read -r file; do
        if [[ -f "$file" ]]; then
            local size=$(wc -c < "$file" 2>/dev/null || echo "0")
            if [[ $size -gt 100000 ]]; then  # >100KB
                log_warning "Large file detected: $file ($(($size/1024))KB)"
                ((large_files++))
            fi
        fi
    done < <(find . -name "*.md" -o -name "*.sh" | grep -v ".git/")
    
    if [[ $large_files -eq 0 ]]; then
        record_test "PASS" "No unusually large files detected"
    else
        record_test "WARN" "$large_files large files detected"
    fi
}

# Command System Validation
validate_command_system() {
    log_section "Command System Validation"
    
    cd "$PROJECT_ROOT"
    
    if [[ ! -d "commands" ]]; then
        record_test "FAIL" "Commands directory missing"
        return
    fi
    
    # Test 1: Command file structure
    local malformed_commands=0
    while IFS= read -r cmd_file; do
        if [[ -f "$cmd_file" ]]; then
            # Check for basic markdown structure
            if ! grep -q "^# " "$cmd_file" 2>/dev/null; then
                log_warning "Command missing title: $cmd_file"
                ((malformed_commands++))
            fi
            
            # Check file size (should be reasonable)
            local lines=$(wc -l < "$cmd_file" 2>/dev/null || echo "0")
            if [[ $lines -gt 200 ]]; then
                log_warning "Command file very large: $cmd_file ($lines lines)"
                ((malformed_commands++))
            elif [[ $lines -lt 10 ]]; then
                log_warning "Command file very small: $cmd_file ($lines lines)"
                ((malformed_commands++))
            fi
        fi
    done < <(find commands -name "*.md" -type f)
    
    if [[ $malformed_commands -eq 0 ]]; then
        record_test "PASS" "All command files well-formed"
    else
        record_test "WARN" "$malformed_commands command files have issues"
    fi
    
    # Test 2: Core commands presence
    local core_dir="commands/00-core"
    if [[ -d "$core_dir" ]]; then
        local core_commands=("init-project.md" "context-engine.md" "notify-manager.md" "handoff-manager.md")
        local missing_core=0
        
        for core_cmd in "${core_commands[@]}"; do
            if [[ -f "$core_dir/$core_cmd" ]]; then
                record_test "PASS" "Core command exists: $core_cmd"
            else
                record_test "FAIL" "Core command missing: $core_cmd"
                ((missing_core++))
            fi
        done
    else
        record_test "FAIL" "Core commands directory missing"
    fi
    
    # Test 3: Command accessibility
    local inaccessible_commands=0
    while IFS= read -r cmd_file; do
        if [[ -f "$cmd_file" && ! -r "$cmd_file" ]]; then
            log_error "Command not accessible: $cmd_file"
            ((inaccessible_commands++))
        fi
    done < <(find commands -name "*.md" -type f)
    
    if [[ $inaccessible_commands -eq 0 ]]; then
        record_test "PASS" "All commands accessible"
    else
        record_test "FAIL" "$inaccessible_commands commands not accessible"
    fi
}

# Documentation Validation
validate_documentation() {
    log_section "Documentation Validation"
    
    cd "$PROJECT_ROOT"
    
    # Test 1: Core documentation exists
    local core_docs=("docs/core/README.md" "docs/core/principles.md" "docs/standards/command-standards.md")
    for doc in "${core_docs[@]}"; do
        if [[ -f "$doc" ]]; then
            record_test "PASS" "Core documentation exists: $doc"
        else
            record_test "FAIL" "Core documentation missing: $doc"
        fi
    done
    
    # Test 2: Documentation structure
    if [[ -d "docs" ]]; then
        local doc_dirs=("core" "standards" "templates")
        for dir in "${doc_dirs[@]}"; do
            if [[ -d "docs/$dir" ]]; then
                record_test "PASS" "Documentation directory exists: docs/$dir"
            else
                record_test "WARN" "Documentation directory missing: docs/$dir"
            fi
        done
    else
        record_test "FAIL" "Documentation directory missing"
    fi
    
    # Test 3: Documentation consistency
    local broken_links=0
    if command -v grep >/dev/null 2>&1; then
        while IFS= read -r doc_file; do
            if [[ -f "$doc_file" ]]; then
                # Check for broken internal links (basic check)
                grep -o '\[.*\](.*\.md)' "$doc_file" 2>/dev/null | while IFS= read -r link; do
                    local file_ref=$(echo "$link" | sed 's/.*](\(.*\))/\1/')
                    local full_path="$(dirname "$doc_file")/$file_ref"
                    if [[ ! -f "$full_path" ]]; then
                        log_warning "Possible broken link in $doc_file: $link"
                        ((broken_links++))
                    fi
                done
            fi
        done < <(find docs -name "*.md" -type f 2>/dev/null | head -10)  # Sample check
    fi
    
    if [[ $broken_links -eq 0 ]]; then
        record_test "PASS" "No broken documentation links detected"
    else
        record_test "WARN" "$broken_links potential broken links detected"
    fi
}

# Performance Validation
validate_performance() {
    log_section "Performance Validation"
    
    cd "$PROJECT_ROOT"
    
    # Test 1: File system performance
    local start_time=$(date +%s.%N)
    find . -name "*.md" > /dev/null 2>&1
    local end_time=$(date +%s.%N)
    local find_time=$(echo "$end_time - $start_time" | bc 2>/dev/null || echo "0")
    
    if [[ $(echo "$find_time < 5.0" | bc 2>/dev/null || echo "1") -eq 1 ]]; then
        record_test "PASS" "File system performance acceptable (${find_time}s)"
    else
        record_test "WARN" "File system performance slow (${find_time}s)"
    fi
    
    # Test 2: Git performance
    start_time=$(date +%s.%N)
    git status >/dev/null 2>&1
    end_time=$(date +%s.%N)
    local git_time=$(echo "$end_time - $start_time" | bc 2>/dev/null || echo "0")
    
    if [[ $(echo "$git_time < 2.0" | bc 2>/dev/null || echo "1") -eq 1 ]]; then
        record_test "PASS" "Git performance acceptable (${git_time}s)"
    else
        record_test "WARN" "Git performance slow (${git_time}s)"
    fi
    
    # Test 3: Disk space
    local available_space=$(df . | tail -1 | awk '{print $4}')
    local space_mb=$((available_space / 1024))
    
    if [[ $space_mb -gt 1000 ]]; then  # >1GB
        record_test "PASS" "Sufficient disk space available (${space_mb}MB)"
    elif [[ $space_mb -gt 100 ]]; then  # >100MB
        record_test "WARN" "Limited disk space available (${space_mb}MB)"
    else
        record_test "FAIL" "Insufficient disk space (${space_mb}MB)"
    fi
}

# Migration-Specific Validation
validate_migration_state() {
    log_section "Migration State Validation"
    
    cd "$PROJECT_ROOT"
    
    # Test 1: Archive directory analysis
    if [[ -d ".archive" ]]; then
        local archive_size=$(du -sh .archive 2>/dev/null | cut -f1)
        local archive_files=$(find .archive -type f | wc -l)
        
        if [[ $archive_files -gt 1000 ]]; then
            record_test "WARN" "Large archive detected: $archive_files files ($archive_size)"
        else
            record_test "PASS" "Archive size reasonable: $archive_files files ($archive_size)"
        fi
        
        # Check for migration patterns
        local recovery_files=$(find .archive -name "*Recovery*" -type f | wc -l)
        if [[ $recovery_files -gt 0 ]]; then
            record_test "PASS" "Migration archive structure detected ($recovery_files recovery files)"
        fi
    else
        record_test "PASS" "No archive directory (clean state)"
    fi
    
    # Test 2: Git staging area
    local staged_files=$(git diff --cached --name-only 2>/dev/null | wc -l)
    local deleted_staged=$(git diff --cached --name-only --diff-filter=D 2>/dev/null | wc -l)
    
    if [[ $deleted_staged -gt 50 ]]; then
        record_test "WARN" "Many deleted files staged: $deleted_staged (possible migration in progress)"
    elif [[ $staged_files -gt 0 ]]; then
        record_test "PASS" "Staged changes detected: $staged_files files"
    else
        record_test "PASS" "No staged changes"
    fi
    
    # Test 3: Rollback system presence
    if [[ -d "rollback" ]]; then
        local rollback_scripts=$(find rollback -name "*.sh" -type f | wc -l)
        if [[ $rollback_scripts -gt 0 ]]; then
            record_test "PASS" "Rollback system detected ($rollback_scripts scripts)"
        else
            record_test "WARN" "Rollback directory exists but no scripts found"
        fi
    else
        record_test "WARN" "No rollback system detected"
    fi
}

# Emergency Detection
detect_emergencies() {
    log_section "Emergency Condition Detection"
    
    cd "$PROJECT_ROOT"
    
    local emergency_detected=false
    
    # Emergency 1: Critical system files missing
    local critical_missing=0
    local critical_files=("CLAUDE.md" "commands")
    for file in "${critical_files[@]}"; do
        if [[ ! -e "$file" ]]; then
            log_error "EMERGENCY: Critical component missing: $file"
            ((critical_missing++))
            emergency_detected=true
        fi
    done
    
    # Emergency 2: Git repository corruption
    if ! git rev-parse --git-dir >/dev/null 2>&1; then
        log_error "EMERGENCY: Git repository corruption detected"
        emergency_detected=true
    fi
    
    # Emergency 3: Massive file deletion
    local deleted_count=$(git status --porcelain 2>/dev/null | grep -c "^ D" || echo "0")
    if [[ $deleted_count -gt 500 ]]; then
        log_error "EMERGENCY: Massive file deletion detected: $deleted_count files"
        emergency_detected=true
    fi
    
    # Emergency 4: Command system destruction
    local command_count=$(find commands -name "*.md" -type f 2>/dev/null | wc -l)
    if [[ $command_count -eq 0 ]]; then
        log_error "EMERGENCY: Command system appears to be destroyed"
        emergency_detected=true
    fi
    
    if [[ "$emergency_detected" == "true" ]]; then
        record_test "FAIL" "EMERGENCY CONDITIONS DETECTED - IMMEDIATE ROLLBACK RECOMMENDED"
        return 1
    else
        record_test "PASS" "No emergency conditions detected"
        return 0
    fi
}

# Generate validation report
generate_report() {
    local report_file="$LOG_DIR/validation-report-$(date +%Y%m%d_%H%M%S).json"
    
    cat > "$report_file" << EOF
{
  "validation_timestamp": "$(date -Iseconds)",
  "project_root": "$PROJECT_ROOT",
  "validator_version": "1.0.0",
  "results": {
    "total_tests": $TOTAL_TESTS,
    "passed_tests": $PASSED_TESTS,
    "failed_tests": $FAILED_TESTS,
    "warning_tests": $WARNING_TESTS,
    "success_rate": "$(( (PASSED_TESTS * 100) / TOTAL_TESTS ))%"
  },
  "overall_status": "$([ $FAILED_TESTS -eq 0 ] && echo "PASS" || echo "FAIL")",
  "rollback_recommended": $([ $FAILED_TESTS -gt 5 ] && echo "true" || echo "false"),
  "log_file": "$VALIDATION_LOG",
  "git_status": {
    "commit": "$(git rev-parse HEAD 2>/dev/null || echo 'no-git')",
    "branch": "$(git branch --show-current 2>/dev/null || echo 'no-branch')",
    "modified_files": $(git status --porcelain 2>/dev/null | wc -l),
    "deleted_files": $(git status --porcelain 2>/dev/null | grep -c "^ D" || echo "0")
  }
}
EOF
    
    echo "$report_file"
}

# Main validation orchestrator
run_full_validation() {
    log_section "Starting Comprehensive System Validation"
    
    validate_core_system
    validate_git_repository
    validate_file_integrity
    validate_command_system
    validate_documentation
    validate_performance
    validate_migration_state
    
    # Check for emergencies
    if ! detect_emergencies; then
        log_error "CRITICAL: Emergency conditions detected - validation terminated"
        generate_report
        return 2  # Emergency exit code
    fi
    
    log_section "Validation Summary"
    log_info "Total Tests: $TOTAL_TESTS"
    log_info "Passed: $PASSED_TESTS"
    log_info "Failed: $FAILED_TESTS"
    log_info "Warnings: $WARNING_TESTS"
    
    local success_rate=$(( (PASSED_TESTS * 100) / TOTAL_TESTS ))
    log_info "Success Rate: ${success_rate}%"
    
    local report_file=$(generate_report)
    log_info "Detailed report: $report_file"
    
    if [[ $FAILED_TESTS -eq 0 ]]; then
        log_success "VALIDATION PASSED - System appears healthy"
        return 0
    elif [[ $FAILED_TESTS -le 2 ]]; then
        log_warning "VALIDATION COMPLETED WITH MINOR ISSUES - Monitor closely"
        return 1
    else
        log_error "VALIDATION FAILED - Consider rollback ($FAILED_TESTS failures)"
        return 1
    fi
}

# Quick validation for runtime checks
run_quick_validation() {
    log_section "Quick Validation Check"
    
    # Essential checks only
    local quick_failures=0
    
    # Check critical files
    local critical_files=("CLAUDE.md" "commands")
    for file in "${critical_files[@]}"; do
        if [[ ! -e "$file" ]]; then
            log_error "Critical file missing: $file"
            ((quick_failures++))
        fi
    done
    
    # Check git functionality
    if ! git status >/dev/null 2>&1; then
        log_error "Git repository not functional"
        ((quick_failures++))
    fi
    
    # Check command count
    local cmd_count=$(find commands -name "*.md" -type f 2>/dev/null | wc -l)
    if [[ $cmd_count -eq 0 ]]; then
        log_error "No commands found"
        ((quick_failures++))
    fi
    
    if [[ $quick_failures -eq 0 ]]; then
        log_success "Quick validation passed"
        return 0
    else
        log_error "Quick validation failed ($quick_failures issues)"
        return 1
    fi
}

# Main dispatcher
main() {
    case "${1:-full}" in
        "full"|"complete")
            run_full_validation
            ;;
        "quick"|"fast")
            run_quick_validation
            ;;
        "emergency"|"critical")
            detect_emergencies
            ;;
        "report")
            generate_report
            ;;
        "help"|"-h"|"--help")
            cat << 'EOF'
Validation Suite - System Health and Migration Safety

Usage: ./validation-suite.sh [type] [options]

Validation Types:
  full        Complete system validation (default)
  quick       Fast essential checks only
  emergency   Emergency condition detection
  report      Generate validation report

Exit Codes:
  0 - All validations passed
  1 - Some validations failed (warnings)
  2 - Emergency conditions detected

Examples:
  ./validation-suite.sh full
  ./validation-suite.sh quick
  ./validation-suite.sh emergency
EOF
            ;;
        *)
            log_error "Unknown validation type: $1"
            echo "Use './validation-suite.sh help' for usage information"
            exit 1
            ;;
    esac
}

# Execute main function
main "$@"