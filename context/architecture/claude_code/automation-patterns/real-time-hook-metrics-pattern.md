# Real-Time Hook Metrics Pattern

**31/07/2025 CDMX** | Performance monitoring pattern for automation systems

## AUTORIDAD SUPREMA
@context/architecture/core/truth-source.md → claude_code/automation-patterns/ → real-time-hook-metrics-pattern.md implements metrics pattern per session insights

## PATTERN DEFINITION

**"Real-Time Hook Metrics Pattern"** - Comprehensive automation performance tracking with JSON-based metrics storage, intelligent reporting, and system health monitoring for automation systems.

## ARCHITECTURAL INNOVATION

### JSON-Based Metrics Architecture
```json
{
  "hook_performance": {
    "hook_name": {
      "total_executions": 0,
      "successful_executions": 0,
      "failed_executions": 0,
      "average_execution_time": 0,
      "success_rate": 0,
      "last_execution": "timestamp"
    }
  },
  "system_health": {
    "total_hook_executions": 0,
    "overall_success_rate": 0,
    "monitoring_active": true
  }
}
```

### Real-Time Recording Implementation
```bash
record_hook_execution() {
    local hook_name="$1" success="$2" execution_time="$3"
    
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
         (.hook_performance[$hook].successful_executions / 
          .hook_performance[$hook].total_executions * 100) |
       .system_health.overall_success_rate = 
         (total_successful / .system_health.total_hook_executions * 100)
    ' "$METRICS_FILE"
}
```

## PERFORMANCE MONITORING FRAMEWORK

### Multi-Dimensional Tracking
- **Execution Count Tracking**: Total, successful, failed execution counters
- **Performance Analysis**: Average execution time calculation and trending
- **Success Rate Monitoring**: Individual hook and system-wide success rates
- **Temporal Analysis**: Last execution timestamps and frequency patterns

### Intelligent Reporting System
```bash
generate_report() {
    echo "🚀 Hook Performance Report - $(date)"
    echo "📊 System Health: Overall Success Rate: ${overall_success_rate}%"
    
    for hook in hook_list; do
        local success_rate=$(jq -r ".hook_performance.$hook.success_rate" "$METRICS_FILE")
        local avg_time=$(jq -r ".hook_performance.$hook.average_execution_time" "$METRICS_FILE")
        echo "🔧 $hook: Success: ${success_rate}%, Avg Time: ${avg_time}ms"
    done
}
```

### Real-Time Health Monitoring
- **Live Performance Dashboard**: Instant visibility into system performance
- **Trend Analysis**: Performance degradation detection and alerting
- **Resource Usage Tracking**: Execution time and resource consumption monitoring
- **System Health Indicators**: Overall automation system reliability metrics

## PATTERN APPLICATIONS

### Hook Integration Monitoring
- **PostToolUse Performance**: File operation automation success tracking
- **Stop Event Monitoring**: Conversation completion automation metrics
- **PreToolUse Validation**: Pre-operation validation performance analysis
- **Cross-Hook Analysis**: System-wide automation performance correlation

### Metrics Collection Strategy
```bash
# Before hook execution
start_time=$(date +%s%3N)

# After hook execution
end_time=$(date +%s%3N)
execution_time=$((end_time - start_time))
success=$([ $? -eq 0 ] && echo "true" || echo "false")

# Record metrics
record_hook_execution "$hook_name" "$success" "$execution_time"
```

### Performance Optimization Framework
- **Bottleneck Identification**: Slow-performing hook detection
- **Success Rate Analysis**: Failure pattern identification and resolution
- **Resource Optimization**: Execution time optimization opportunities
- **System Capacity Planning**: Load analysis and scaling recommendations

## MONITORING BENEFITS

### Operational Visibility
- **Real-Time Performance**: Live system performance monitoring
- **Historical Analysis**: Long-term performance trend tracking
- **Failure Analysis**: Detailed failure pattern identification
- **Resource Planning**: Capacity planning based on actual usage data

### System Reliability
- **Proactive Issue Detection**: Performance degradation early warning
- **Failure Rate Monitoring**: System reliability trend analysis
- **Performance Benchmarking**: Baseline establishment and comparison
- **Optimization Guidance**: Data-driven performance improvement recommendations

## REUSABILITY FRAMEWORK

### Pattern Templates
- **Metrics Collection Template**: Standard performance data collection
- **JSON Schema Template**: Structured metrics storage format
- **Reporting Template**: Standardized performance reporting
- **Health Monitoring Template**: System health assessment framework

### Integration Points
- **Automation Systems**: Any hook-based or event-driven automation
- **CI/CD Pipelines**: Build and deployment performance monitoring
- **Monitoring Systems**: Integration with existing monitoring infrastructure
- **Performance Dashboards**: Real-time performance visualization

## TECHNICAL IMPLEMENTATION

### Atomic Metrics Updates
```bash
# Thread-safe metrics updating using temporary files
temp_file=$(mktemp)
jq 'update_operations' "$METRICS_FILE" > "$temp_file" && mv "$temp_file" "$METRICS_FILE"
```

### Error Handling and Recovery
- **Metrics File Corruption Recovery**: Automatic metrics file recreation
- **Missing Data Handling**: Graceful degradation when metrics unavailable
- **Performance Impact Minimization**: Low-overhead metrics collection
- **Storage Management**: Automatic log rotation and cleanup

## INTEGRATION REFERENCES

**Pattern Authority**: ← H-HOOK-INTEGRATION hook-metrics-tracker.sh implementation
**Performance Monitoring**: ←→ @context/architecture/patterns/ (system monitoring patterns)
**Automation Integration**: ←→ @context/architecture/claude_code/ (automation framework)

---

**REAL-TIME METRICS DECLARATION**: This pattern enables comprehensive automation performance monitoring with minimal overhead, providing operational visibility and system health insights for reliable automation systems.

**EVOLUTION PATHWAY**: Pattern evolves through application → optimization → dashboard integration → predictive analysis enhancement cycle.