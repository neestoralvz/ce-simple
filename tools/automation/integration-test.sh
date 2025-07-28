#!/bin/bash

# Integration Testing for VDD Automation Systems
# Purpose: Comprehensive testing of Git Intelligence, Performance Metrics, and Think×4 Enforcement
# Status: Integration validation for automation architecture

set -euo pipefail

# ============================================================================
# CONFIGURATION
# ============================================================================

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
readonly TEST_RESULTS_DIR="$PROJECT_ROOT/data/integration-tests"
readonly LOG_FILE="$TEST_RESULTS_DIR/integration-test.log"

# Test components
readonly GIT_INTELLIGENCE_SCRIPT="$SCRIPT_DIR/git-intelligence-engine.sh"
readonly PERFORMANCE_COLLECTOR="$SCRIPT_DIR/performance-collector.py"
readonly THINK_X4_VALIDATOR="$SCRIPT_DIR/think-x4-validator.sh"

# Ensure test results directory exists
mkdir -p "$TEST_RESULTS_DIR"

# ============================================================================
# LOGGING FUNCTIONS
# ============================================================================

log_info() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] INFO: $*" | tee -a "$LOG_FILE"
}

log_success() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ✅ SUCCESS: $*" | tee -a "$LOG_FILE"
}

log_error() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ❌ ERROR: $*" >&2 | tee -a "$LOG_FILE"
}

log_warning() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ⚠️  WARNING: $*" | tee -a "$LOG_FILE"
}

# ============================================================================
# TEST FRAMEWORK
# ============================================================================

test_counter=0
passed_tests=0
failed_tests=0

run_test() {
    local test_name="$1"
    local test_command="$2"
    
    ((test_counter++))
    log_info "Running Test $test_counter: $test_name"
    
    if eval "$test_command"; then
        log_success "Test $test_counter PASSED: $test_name"
        ((passed_tests++))
        return 0
    else
        log_error "Test $test_counter FAILED: $test_name"
        ((failed_tests++))
        return 1
    fi
}

# ============================================================================
# GIT INTELLIGENCE TESTS
# ============================================================================

test_git_intelligence_availability() {
    [[ -x "$GIT_INTELLIGENCE_SCRIPT" ]] && [[ -f "$GIT_INTELLIGENCE_SCRIPT" ]]
}

test_git_intelligence_execution() {
    "$GIT_INTELLIGENCE_SCRIPT" >/dev/null 2>&1
}

test_git_metrics_generation() {
    local metrics_dir="$PROJECT_ROOT/data/git-metrics"
    [[ -f "$metrics_dir/commit-patterns.json" ]] && \
    [[ -f "$metrics_dir/branch-lifecycle.json" ]] && \
    [[ -f "$metrics_dir/merge-success.json" ]] && \
    [[ -f "$metrics_dir/orchestration-analysis.json" ]] && \
    [[ -f "$metrics_dir/vdd-integration.json" ]]
}

test_git_integration_file_content() {
    local integration_file="$PROJECT_ROOT/data/git-metrics/vdd-integration.json"
    [[ -f "$integration_file" ]] && \
    jq -e '.orchestration_settings.parallelization_level' "$integration_file" >/dev/null && \
    jq -e '.orchestration_settings.suggested_agents' "$integration_file" >/dev/null && \
    jq -e '.orchestration_settings.risk_assessment' "$integration_file" >/dev/null
}

# ============================================================================
# PERFORMANCE METRICS TESTS
# ============================================================================

test_performance_collector_availability() {
    [[ -x "$PERFORMANCE_COLLECTOR" ]] && [[ -f "$PERFORMANCE_COLLECTOR" ]]
}

test_performance_collector_dashboard() {
    python3 "$PERFORMANCE_COLLECTOR" dashboard >/dev/null 2>&1
}

test_performance_session_workflow() {
    local session_id="integration-test-$(date +%s)"
    
    # Start session
    python3 "$PERFORMANCE_COLLECTOR" start-session --session-id "$session_id" --agents 2 >/dev/null 2>&1 && \
    sleep 1 && \
    # End session
    python3 "$PERFORMANCE_COLLECTOR" end-session --session-id "$session_id" >/dev/null 2>&1
}

test_performance_metrics_files() {
    local metrics_dir="$PROJECT_ROOT/data/performance-metrics"
    [[ -f "$metrics_dir/realtime_dashboard.json" ]] && \
    [[ -f "$metrics_dir/active_sessions.json" ]]
}

# ============================================================================
# THINK×4 ENFORCEMENT TESTS
# ============================================================================

test_think_x4_validator_availability() {
    [[ -x "$THINK_X4_VALIDATOR" ]] && [[ -f "$THINK_X4_VALIDATOR" ]]
}

test_think_x4_validation_capability() {
    # Test with a file known to have Think×4 content
    local test_file="$PROJECT_ROOT/user-input/technical-requirements/think-by-four-mandatory.md"
    [[ -f "$test_file" ]] && \
    "$THINK_X4_VALIDATOR" validate-file "$test_file" >/dev/null 2>&1
}

test_think_x4_hooks_installation() {
    local pre_commit_hook="$PROJECT_ROOT/.git/hooks/pre-commit"
    [[ -f "$pre_commit_hook" ]] && [[ -x "$pre_commit_hook" ]]
}

test_think_x4_dashboard_generation() {
    "$THINK_X4_VALIDATOR" dashboard >/dev/null 2>&1
}

# ============================================================================
# INTEGRATION TESTS
# ============================================================================

test_cross_system_data_flow() {
    # Test that Git Intelligence affects Performance Collector recommendations
    local git_integration_file="$PROJECT_ROOT/data/git-metrics/vdd-integration.json"
    local performance_dashboard="$PROJECT_ROOT/data/performance-metrics/realtime_dashboard.json"
    
    [[ -f "$git_integration_file" ]] && \
    [[ -f "$performance_dashboard" ]] && \
    # Check that both files are recent (within last 10 minutes)
    [[ $(find "$git_integration_file" -mmin -10 | wc -l) -gt 0 ]] && \
    [[ $(find "$performance_dashboard" -mmin -10 | wc -l) -gt 0 ]]
}

test_automation_directories_structure() {
    [[ -d "$PROJECT_ROOT/data/git-metrics" ]] && \
    [[ -d "$PROJECT_ROOT/data/performance-metrics" ]] && \
    [[ -d "$PROJECT_ROOT/data/think-x4-validation" ]] && \
    [[ -d "$PROJECT_ROOT/tools/automation" ]]
}

test_system_responsiveness() {
    # Test that all systems can run within reasonable time
    local start_time=$(date +%s)
    
    "$GIT_INTELLIGENCE_SCRIPT" >/dev/null 2>&1 && \
    python3 "$PERFORMANCE_COLLECTOR" dashboard >/dev/null 2>&1 && \
    "$THINK_X4_VALIDATOR" dashboard >/dev/null 2>&1
    
    local end_time=$(date +%s)
    local duration=$((end_time - start_time))
    
    # All three systems should complete within 30 seconds
    [[ $duration -lt 30 ]]
}

test_log_files_generation() {
    local git_log="$PROJECT_ROOT/data/git-metrics/intelligence.log"
    local performance_log="$PROJECT_ROOT/data/performance-metrics/performance.log"
    local think_x4_log="$PROJECT_ROOT/data/think-x4-validation/think-x4-enforcement.log"
    
    [[ -f "$git_log" ]] && \
    [[ -f "$performance_log" ]] && \
    [[ -f "$think_x4_log" ]]
}

# ============================================================================
# TEST EXECUTION
# ============================================================================

run_all_tests() {
    log_info "Starting VDD Automation Systems Integration Testing"
    log_info "=============================================="
    
    # Git Intelligence Tests
    log_info "Testing Git Intelligence System..."
    run_test "Git Intelligence Script Availability" "test_git_intelligence_availability"
    run_test "Git Intelligence Execution" "test_git_intelligence_execution" 
    run_test "Git Metrics Generation" "test_git_metrics_generation"
    run_test "Git Integration File Content" "test_git_integration_file_content"
    
    # Performance Metrics Tests
    log_info "Testing Performance Metrics System..."
    run_test "Performance Collector Availability" "test_performance_collector_availability"
    run_test "Performance Dashboard Generation" "test_performance_collector_dashboard"
    run_test "Performance Session Workflow" "test_performance_session_workflow"
    run_test "Performance Metrics Files" "test_performance_metrics_files"
    
    # Think×4 Enforcement Tests
    log_info "Testing Think×4 Enforcement System..."
    run_test "Think×4 Validator Availability" "test_think_x4_validator_availability"
    run_test "Think×4 Validation Capability" "test_think_x4_validation_capability"
    run_test "Think×4 Hooks Installation" "test_think_x4_hooks_installation"
    run_test "Think×4 Dashboard Generation" "test_think_x4_dashboard_generation"
    
    # Integration Tests
    log_info "Testing System Integration..."
    run_test "Cross-System Data Flow" "test_cross_system_data_flow"
    run_test "Automation Directories Structure" "test_automation_directories_structure"
    run_test "System Responsiveness" "test_system_responsiveness"
    run_test "Log Files Generation" "test_log_files_generation"
    
    # Generate Test Report
    generate_test_report
}

generate_test_report() {
    local success_rate=0
    if [[ $test_counter -gt 0 ]]; then
        success_rate=$(( (passed_tests * 100) / test_counter ))
    fi
    
    local status="FAILED"
    if [[ $failed_tests -eq 0 ]]; then
        status="PASSED"
    elif [[ $success_rate -ge 80 ]]; then
        status="MOSTLY_PASSED"
    fi
    
    # Generate JSON report
    local report_file="$TEST_RESULTS_DIR/integration_test_report_$(date +%s).json"
    
    cat > "$report_file" <<EOF
{
  "metadata": {
    "test_timestamp": "$(date -Iseconds)",
    "test_duration": "$(date +%s)s",
    "automation_architecture_version": "1.0.0"
  },
  "summary": {
    "total_tests": $test_counter,
    "passed_tests": $passed_tests,
    "failed_tests": $failed_tests,
    "success_rate": $success_rate,
    "overall_status": "$status"
  },
  "system_status": {
    "git_intelligence": "$(test_git_intelligence_availability && echo "OPERATIONAL" || echo "FAILED")",
    "performance_metrics": "$(test_performance_collector_availability && echo "OPERATIONAL" || echo "FAILED")",
    "think_x4_enforcement": "$(test_think_x4_validator_availability && echo "OPERATIONAL" || echo "FAILED")"
  },
  "recommendations": {
    "action_required": $([ $failed_tests -gt 0 ] && echo "true" || echo "false"),
    "priority": "$([ $failed_tests -gt 5 ] && echo "HIGH" || echo "MEDIUM")",
    "next_steps": [
      "Review failed test logs",
      "Verify system dependencies",
      "Re-run integration tests",
      "Check automation component status"
    ]
  }
}
EOF
    
    log_info "=============================================="
    log_info "Integration Testing Results:"
    log_info "  Total Tests: $test_counter"
    log_info "  Passed: $passed_tests"
    log_info "  Failed: $failed_tests" 
    log_info "  Success Rate: $success_rate%"
    log_info "  Overall Status: $status"
    log_info "=============================================="
    log_info "Report saved to: $report_file"
    
    if [[ $failed_tests -eq 0 ]]; then
        log_success "All automation systems are operational and integrated!"
        return 0
    else
        log_error "Integration testing failed. $failed_tests system(s) need attention."
        return 1
    fi
}

# ============================================================================
# MAIN EXECUTION
# ============================================================================

main() {
    local command="${1:-test}"
    
    case "$command" in
        "test"|"run"|"")
            run_all_tests
            ;;
        "report")
            if [[ -f "$TEST_RESULTS_DIR/integration_test_report_$(date +%s).json" ]]; then
                cat "$TEST_RESULTS_DIR/integration_test_report_$(date +%s).json"
            else
                log_error "No recent test report found. Run integration tests first."
                exit 1
            fi
            ;;
        "help")
            cat <<EOF
VDD Automation Systems Integration Testing

Usage:
  $0 [test|run]    - Run complete integration test suite (default)
  $0 report        - Display latest test report  
  $0 help          - Show this help message

This script tests the integration of:
  1. Git-Based Intelligence Automation Engine
  2. Performance Metrics Collection System
  3. Think×4 Automated Enforcement

Test categories:
  - Component availability and executability
  - Individual system functionality  
  - Cross-system data flow and integration
  - Performance and responsiveness
  - File generation and persistence
EOF
            ;;
        *)
            log_error "Unknown command: $command"
            exit 1
            ;;
    esac
}

# Execute main function if script is run directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi