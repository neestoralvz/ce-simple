#!/bin/bash

# Hook Metrics Tracker - Performance and Success Rate Monitoring
# Tracks hook execution performance, success rates, and system health

set -euo pipefail

# Configuration
PROJECT_ROOT="/Users/nalve/ce-simple"
METRICS_FILE="$PROJECT_ROOT/.claude/hooks/logs/hook-metrics.json"
LOG_FILE="$PROJECT_ROOT/.claude/hooks/logs/metrics-tracker.log"

# Logging functions
log_info() { echo "[$(date '+%H:%M:%S')] 📊 $1" | tee -a "$LOG_FILE"; }
log_success() { echo "[$(date '+%H:%M:%S')] ✅ $1" | tee -a "$LOG_FILE"; }
log_warning() { echo "[$(date '+%H:%M:%S')] ⚠️ $1" | tee -a "$LOG_FILE"; }
log_error() { echo "[$(date '+%H:%M:%S')] ❌ $1" | tee -a "$LOG_FILE"; }

# Ensure directories exist
mkdir -p "$(dirname "$METRICS_FILE")"
mkdir -p "$(dirname "$LOG_FILE")"

# Initialize metrics file if it doesn't exist
initialize_metrics() {
    if [[ ! -f "$METRICS_FILE" ]]; then
        cat > "$METRICS_FILE" <<EOF
{
  "hook_performance": {
    "auto_git_commit": {
      "total_executions": 0,
      "successful_executions": 0,
      "failed_executions": 0,
      "average_execution_time": 0,
      "last_execution": "",
      "success_rate": 0
    },
    "auto_roadmap_update": {
      "total_executions": 0,
      "successful_executions": 0,
      "failed_executions": 0,
      "average_execution_time": 0,
      "last_execution": "",
      "success_rate": 0
    },
    "auto_validation": {
      "total_executions": 0,
      "successful_executions": 0,
      "failed_executions": 0,
      "average_execution_time": 0,
      "last_execution": "",
      "success_rate": 0
    }
  },
  "system_health": {
    "total_hook_executions": 0,
    "overall_success_rate": 0,
    "last_updated": "$(date -Iseconds)",
    "monitoring_active": true
  }
}
EOF
        log_info "Metrics file initialized"
    fi
}

# Record hook execution
record_hook_execution() {
    local hook_name="$1"
    local success="$2"
    local execution_time="$3"
    
    # Validate inputs
    if [[ ! "$hook_name" =~ ^(auto_git_commit|auto_roadmap_update|auto_validation)$ ]]; then
        log_error "Invalid hook name: $hook_name"
        return 1
    fi
    
    if [[ ! "$success" =~ ^(true|false)$ ]]; then
        log_error "Invalid success value: $success"
        return 1
    fi
    
    if ! [[ "$execution_time" =~ ^[0-9]+$ ]]; then
        log_error "Invalid execution time: $execution_time"
        return 1
    fi
    
    log_info "Recording execution for $hook_name: success=$success, time=${execution_time}ms"
    
    # Use jq to update metrics safely
    local temp_file
    temp_file=$(mktemp)
    
    jq --arg hook "$hook_name" \
       --arg success "$success" \
       --arg exec_time "$execution_time" \
       --arg timestamp "$(date -Iseconds)" '
       .hook_performance[$hook].total_executions += 1 |
       .hook_performance[$hook].last_execution = $timestamp |
       if $success == "true" then
         .hook_performance[$hook].successful_executions += 1
       else
         .hook_performance[$hook].failed_executions += 1
       end |
       .hook_performance[$hook].success_rate = 
         (.hook_performance[$hook].successful_executions / .hook_performance[$hook].total_executions * 100) |
       .hook_performance[$hook].average_execution_time = 
         ((.hook_performance[$hook].average_execution_time * (.hook_performance[$hook].total_executions - 1) + ($exec_time | tonumber)) / .hook_performance[$hook].total_executions) |
       .system_health.total_hook_executions += 1 |
       .system_health.last_updated = $timestamp |
       .system_health.overall_success_rate = 
         ((.hook_performance.auto_git_commit.successful_executions + 
           .hook_performance.auto_roadmap_update.successful_executions + 
           .hook_performance.auto_validation.successful_executions) / 
          .system_health.total_hook_executions * 100)
    ' "$METRICS_FILE" > "$temp_file" && mv "$temp_file" "$METRICS_FILE"
    
    log_success "Metrics updated for $hook_name"
}

# Generate performance report
generate_report() {
    log_info "Generating hook performance report"
    
    if [[ ! -f "$METRICS_FILE" ]]; then
        log_error "Metrics file not found: $METRICS_FILE"
        return 1
    fi
    
    echo "🚀 Hook Performance Report - $(date)"
    echo "======================================="
    echo
    
    # Overall system health
    local overall_success_rate
    overall_success_rate=$(jq -r '.system_health.overall_success_rate // 0' "$METRICS_FILE")
    local total_executions
    total_executions=$(jq -r '.system_health.total_hook_executions // 0' "$METRICS_FILE")
    
    echo "📊 System Health:"
    echo "  Overall Success Rate: ${overall_success_rate}%"
    echo "  Total Hook Executions: $total_executions"
    echo
    
    # Individual hook performance
    for hook in auto_git_commit auto_roadmap_update auto_validation; do
        local success_rate
        success_rate=$(jq -r ".hook_performance.$hook.success_rate // 0" "$METRICS_FILE")
        local total
        total=$(jq -r ".hook_performance.$hook.total_executions // 0" "$METRICS_FILE")
        local successful
        successful=$(jq -r ".hook_performance.$hook.successful_executions // 0" "$METRICS_FILE")
        local failed
        failed=$(jq -r ".hook_performance.$hook.failed_executions // 0" "$METRICS_FILE")
        local avg_time
        avg_time=$(jq -r ".hook_performance.$hook.average_execution_time // 0" "$METRICS_FILE")
        local last_exec
        last_exec=$(jq -r ".hook_performance.$hook.last_execution // \"Never\"" "$METRICS_FILE")
        
        echo "🔧 $hook:"
        echo "  Success Rate: ${success_rate}%"
        echo "  Executions: $total (✅ $successful, ❌ $failed)"
        echo "  Average Time: ${avg_time}ms"
        echo "  Last Execution: $last_exec"
        echo
    done
    
    log_success "Performance report generated"
}

# Main function
main() {
    local command="${1:-report}"
    
    case "$command" in
        "init")
            initialize_metrics
            ;;
        "record")
            local hook_name="${2:-}"
            local success="${3:-}"
            local execution_time="${4:-}"
            
            if [[ -z "$hook_name" || -z "$success" || -z "$execution_time" ]]; then
                log_error "Usage: $0 record <hook_name> <success> <execution_time>"
                exit 1
            fi
            
            initialize_metrics
            record_hook_execution "$hook_name" "$success" "$execution_time"
            ;;
        "report")
            initialize_metrics
            generate_report
            ;;
        "reset")
            log_warning "Resetting all metrics"
            rm -f "$METRICS_FILE"
            initialize_metrics
            log_success "Metrics reset completed"
            ;;
        *)
            echo "Usage: $0 {init|record <hook> <success> <time>|report|reset}"
            exit 1
            ;;
    esac
}

# Execute main function
main "$@"