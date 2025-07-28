#!/bin/bash

# validate-orchestration-integration.sh
# Comprehensive validation of orchestration hooks integration
# Tests all components: hooks, health daemon, SQLite coordination, real-time reporting

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
VALIDATION_LOG="$PROJECT_ROOT/.claude/logs/validation-$(date +%s).log"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging function
log() {
    local level="$1"
    local message="$2"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    local color=""
    
    case "$level" in
        "ERROR") color="$RED" ;;
        "SUCCESS") color="$GREEN" ;;
        "WARNING") color="$YELLOW" ;;
        "INFO") color="$BLUE" ;;
    esac
    
    echo -e "${color}[$timestamp] [$level] $message${NC}"
    echo "[$timestamp] [$level] $message" >> "$VALIDATION_LOG"
}

# Test functions
test_health_daemon() {
    log "INFO" "Testing health daemon integration..."
    
    local health_status_file="$PROJECT_ROOT/data/monitoring/health_daemon_status.json"
    
    if [[ ! -f "$health_status_file" ]]; then
        log "ERROR" "Health daemon status file not found"
        return 1
    fi
    
    local daemon_pid=$(jq -r '.pid // empty' "$health_status_file" 2>/dev/null || echo "")
    if [[ -z "$daemon_pid" ]]; then
        log "ERROR" "Cannot read daemon PID from status file"
        return 1
    fi
    
    if ! ps -p "$daemon_pid" > /dev/null 2>&1; then
        log "ERROR" "Health daemon not running (PID: $daemon_pid)"
        return 1
    fi
    
    local daemon_status=$(jq -r '.status // empty' "$health_status_file" 2>/dev/null || echo "")
    if [[ "$daemon_status" != "running" ]]; then
        log "ERROR" "Health daemon status is not 'running': $daemon_status"
        return 1
    fi
    
    log "SUCCESS" "Health daemon verified (PID: $daemon_pid, Status: $daemon_status)"
    return 0
}

test_sqlite_database() {
    log "INFO" "Testing SQLite coordination database..."
    
    local db_file="$PROJECT_ROOT/data/orchestration/conversations.db"
    
    if [[ ! -f "$db_file" ]]; then
        log "ERROR" "Conversations database not found: $db_file"
        return 1
    fi
    
    # Test database accessibility
    local table_count=$(sqlite3 "$db_file" "SELECT COUNT(*) FROM sqlite_master WHERE type='table';" 2>/dev/null || echo "0")
    if [[ "$table_count" -lt 3 ]]; then
        log "ERROR" "Database missing required tables (found: $table_count)"
        return 1
    fi
    
    # Test conversation registry
    local active_conversations=$(sqlite3 "$db_file" "SELECT COUNT(*) FROM conversation_registry WHERE status = 'active';" 2>/dev/null || echo "0")
    log "SUCCESS" "Database verified ($table_count tables, $active_conversations active conversations)"
    
    return 0
}

test_hooks_configuration() {
    log "INFO" "Testing hooks configuration..."
    
    local settings_file="$PROJECT_ROOT/.claude/settings.toml"
    
    if [[ ! -f "$settings_file" ]]; then
        log "ERROR" "Settings file not found: $settings_file"
        return 1
    fi
    
    # Count orchestration hooks
    local orchestration_hooks=$(grep -c "orchestration-progress-reporter.sh" "$settings_file" || echo "0")
    if [[ "$orchestration_hooks" -lt 6 ]]; then
        log "ERROR" "Missing orchestration hooks in configuration (found: $orchestration_hooks)"
        return 1
    fi
    
    # Verify hook script exists and is executable
    local hook_script="$PROJECT_ROOT/.claude/hooks/orchestration-progress-reporter.sh"
    if [[ ! -x "$hook_script" ]]; then
        log "ERROR" "Orchestration progress reporter not executable: $hook_script"
        return 1
    fi
    
    log "SUCCESS" "Hooks configuration verified ($orchestration_hooks orchestration hooks configured)"
    return 0
}

test_orchestrator_interface() {
    log "INFO" "Testing orchestrator interface..."
    
    local interface_script="$PROJECT_ROOT/.claude/hooks/orchestrator-interface.sh"
    
    if [[ ! -x "$interface_script" ]]; then
        log "ERROR" "Orchestrator interface not executable: $interface_script"
        return 1
    fi
    
    # Test system status command
    local status_output
    if ! status_output=$("$interface_script" status 2>&1); then
        log "ERROR" "Orchestrator interface status command failed: $status_output"
        return 1
    fi
    
    # Verify JSON output
    if ! echo "$status_output" | jq . > /dev/null 2>&1; then
        log "ERROR" "Orchestrator interface returned invalid JSON"
        return 1
    fi
    
    # Test list command
    local list_output
    if ! list_output=$("$interface_script" list 2>&1); then
        log "ERROR" "Orchestrator interface list command failed: $list_output"
        return 1
    fi
    
    log "SUCCESS" "Orchestrator interface verified (status and list commands working)"
    return 0
}

test_progress_reporting() {
    log "INFO" "Testing progress reporting functionality..."
    
    # Test with sample data
    local reporter_script="$PROJECT_ROOT/.claude/hooks/orchestration-progress-reporter.sh"
    local test_tool="Test"
    local test_input='{"test": "data"}'
    local test_output='{"result": "success"}'
    
    # Run progress reporter
    if ! "$reporter_script" "$test_tool" "$test_input" "$test_output" 2>&1; then
        log "ERROR" "Progress reporter failed with test data"
        return 1
    fi
    
    # Check if progress was logged
    local progress_log="$PROJECT_ROOT/.claude/logs/orchestration-progress.log"
    if [[ ! -f "$progress_log" ]]; then
        log "ERROR" "Progress log file not created"
        return 1
    fi
    
    # Check for recent log entry
    local recent_entries=$(tail -n 5 "$progress_log" | grep -c "Test" || echo "0")
    if [[ "$recent_entries" -eq 0 ]]; then
        log "ERROR" "No recent progress entries found in log"
        return 1
    fi
    
    log "SUCCESS" "Progress reporting verified (test data processed and logged)"
    return 0
}

test_real_time_monitoring() {
    log "INFO" "Testing real-time monitoring capabilities..."
    
    local interface_script="$PROJECT_ROOT/.claude/hooks/orchestrator-interface.sh"
    
    # Test metrics command
    local metrics_output
    if ! metrics_output=$("$interface_script" metrics 2>&1); then
        log "ERROR" "Real-time metrics command failed: $metrics_output"
        return 1
    fi
    
    # Verify metrics contain health daemon info
    if ! echo "$metrics_output" | jq -e '.health_daemon.pid' > /dev/null 2>&1; then
        log "ERROR" "Metrics output missing health daemon information"
        return 1
    fi
    
    # Verify recent activity is included
    if ! echo "$metrics_output" | jq -e '.recent_activity' > /dev/null 2>&1; then
        log "ERROR" "Metrics output missing recent activity"
        return 1
    fi
    
    log "SUCCESS" "Real-time monitoring verified (metrics and activity tracking working)"
    return 0
}

# Integration test
test_end_to_end_integration() {
    log "INFO" "Testing end-to-end integration..."
    
    local conversation_id="hooks-integration-specialist-144944"
    local interface_script="$PROJECT_ROOT/.claude/hooks/orchestrator-interface.sh"
    
    # Get conversation progress
    local progress_output
    if ! progress_output=$("$interface_script" progress "$conversation_id" 2>&1); then
        log "ERROR" "Failed to get conversation progress: $progress_output"
        return 1
    fi
    
    # Verify progress structure
    if ! echo "$progress_output" | jq -e '.conversation_id' > /dev/null 2>&1; then
        log "ERROR" "Progress output missing conversation_id"
        return 1
    fi
    
    if ! echo "$progress_output" | jq -e '.tasks' > /dev/null 2>&1; then
        log "ERROR" "Progress output missing tasks array"
        return 1
    fi
    
    # Check for integration completeness
    local task_count=$(echo "$progress_output" | jq '.tasks | length')
    local message_count=$(echo "$progress_output" | jq '.recent_messages | length')
    
    log "SUCCESS" "End-to-end integration verified ($task_count tasks, $message_count messages tracked)"
    return 0
}

# Performance test
test_performance() {
    log "INFO" "Testing system performance..."
    
    local reporter_script="$PROJECT_ROOT/.claude/hooks/orchestration-progress-reporter.sh"
    local start_time=$(date +%s.%N)
    
    # Run multiple progress reports
    for i in {1..5}; do
        "$reporter_script" "PerformanceTest$i" '{"iteration": '$i'}' '{"status": "completed"}' >/dev/null 2>&1 || {
            log "ERROR" "Performance test iteration $i failed"
            return 1
        }
    done
    
    local end_time=$(date +%s.%N)
    local duration=$(echo "$end_time - $start_time" | bc)
    local threshold="2.0"
    
    if (( $(echo "$duration > $threshold" | bc -l) )); then
        log "WARNING" "Performance test took ${duration}s (threshold: ${threshold}s)"
    else
        log "SUCCESS" "Performance test completed in ${duration}s"
    fi
    
    return 0
}

# Main validation function
run_validation() {
    log "INFO" "Starting orchestration hooks integration validation..."
    mkdir -p "$(dirname "$VALIDATION_LOG")"
    
    local tests=(
        "test_health_daemon"
        "test_sqlite_database"
        "test_hooks_configuration"
        "test_orchestrator_interface"
        "test_progress_reporting"
        "test_real_time_monitoring"
        "test_end_to_end_integration"
        "test_performance"
    )
    
    local passed=0
    local failed=0
    
    for test in "${tests[@]}"; do
        if $test; then
            ((passed++))
        else
            ((failed++))
        fi
        echo # Add spacing between tests
    done
    
    # Summary
    echo
    log "INFO" "=== VALIDATION SUMMARY ==="
    log "INFO" "Tests passed: $passed"
    log "INFO" "Tests failed: $failed"
    log "INFO" "Total tests: $((passed + failed))"
    log "INFO" "Validation log: $VALIDATION_LOG"
    
    if [[ $failed -eq 0 ]]; then
        log "SUCCESS" "ALL TESTS PASSED - Orchestration hooks integration is operational"
        return 0
    else
        log "ERROR" "$failed TEST(S) FAILED - Integration needs attention"
        return 1
    fi
}

# Execute validation if run directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    run_validation "$@"
fi