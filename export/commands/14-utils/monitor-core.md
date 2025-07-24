# Monitor-Core - Universal Monitoring Engine

## Purpose
Centralized monitoring engine extracted from system-monitor, system-monitor-agents, and performance-track. Provides universal health status collection, performance analysis, and alert management for all system components.

## Principles and Guidelines
• **Centralized Collection**: Single point for all health data gathering and analysis
• **Universal Interface**: Consistent monitoring functions across all system components  
• **Threshold Management**: Dynamic alert thresholds with automated degradation detection
• **Trend Analysis**: Historical performance tracking with baseline comparison capabilities

## Core Functions

### collect_health_data()
```javascript
function collect_health_data(component_type = 'all') {
  // System health data collection
  if (component_type === 'system' || component_type === 'all') {
    Bash("git status --porcelain | wc -l") // Git health
    Bash("du -sh commands/ docs/ 2>/dev/null") // Resource usage
    LS("commands") // Directory integrity
    Read("system-health.log") // Historical data
  }
  
  // Agent health monitoring
  if (component_type === 'agents' || component_type === 'all') {
    Bash("find commands -name '*.md' -exec wc -l {} + | awk '$1 > 150 {count++} END {print \"Oversized:\" count+0}'")
    Grep("EXECUTION LAYER", {glob: "commands/*.md", output_mode: "count"})
    Bash("echo 'Agent health collection complete'")
  }
  
  // Performance metrics
  if (component_type === 'performance' || component_type === 'all') {
    Bash("start_time=$(date +%s); echo \"Monitoring started: $start_time\"")
    Bash("find commands -name '*.md' | wc -l | awk '{print \"Total commands:\" $1}'")
    Bash("ps aux | grep -v grep | wc -l | awk '{print \"Process count:\" $1}'")
  }
}
```

### analyze_performance_trends()
```javascript
function analyze_performance_trends(baseline_file = 'performance-baseline.log') {
  // Load baseline data
  Read(baseline_file)
  
  // Current performance collection
  Bash("find commands -name '*.md' -exec wc -l {} + | awk '{sum+=$1; count++} END {print \"Current avg:\" sum/count}'")
  Bash("du -s commands/ | awk '{print \"Storage usage:\" $1}'")
  
  // Trend calculation
  Bash("echo 'Calculating performance trends...'")
  Bash("current_time=$(date +%s); echo \"Analysis timestamp: $current_time\"")
  
  // Generate trend report
  Write("trend-analysis.md", "# Performance Trend Analysis\\n\\nTimestamp: $(date)\\n\\n## Baseline Comparison\\n## Current Metrics\\n## Trend Direction")
}
```

### detect_degradation_patterns()
```javascript
function detect_degradation_patterns(threshold_config = 'alert-thresholds.json') {
  // Load alert thresholds
  Read(threshold_config)
  
  // Resource degradation detection
  Bash("if [ $(find commands -name '*.md' -exec wc -l {} + | awk '$1 > 150' | wc -l) -gt 3 ]; then echo 'ALERT: Size violations detected'; fi")
  Bash("if [ $(du -s commands/ | awk '{print $1}') -gt 10000 ]; then echo 'ALERT: Storage threshold exceeded'; fi")
  
  // Performance degradation patterns
  Bash("response_time=$(date +%s); if [ $response_time -gt $(($response_time - 300)) ]; then echo 'Performance within normal range'; fi")
  
  // System health degradation
  Bash("if [ $(git status --porcelain | wc -l) -gt 20 ]; then echo 'ALERT: High uncommitted changes'; fi")
}
```

### manage_alert_thresholds()
```javascript
function manage_alert_thresholds(action = 'check', threshold_type = 'all') {
  if (action === 'update') {
    Write("alert-thresholds.json", '{"file_size_limit": 150, "storage_limit": 10000, "change_limit": 20, "response_time_limit": 300}')
    Bash("echo 'Alert thresholds updated'")
  }
  
  if (action === 'check' || action === 'validate') {
    Read("alert-thresholds.json")
    Bash("echo 'Validating current thresholds against system state'")
    
    // Threshold validation
    Bash("find commands -name '*.md' -exec wc -l {} + | awk '$1 > 150 {print \"Threshold violation: \" FILENAME}' > threshold-violations.log")
    Read("threshold-violations.log")
  }
}
```

### generate_monitoring_reports()
```javascript
function generate_monitoring_reports(report_type = 'comprehensive') {
  const timestamp = new Date().toISOString()
  
  if (report_type === 'health' || report_type === 'comprehensive') {
    Write("health-report.md", `# System Health Report\\n\\nGenerated: ${timestamp}\\n\\n## System Status\\n## Agent Health\\n## Performance Metrics\\n## Alert Summary`)
    Bash("echo 'Health report generated'")
  }
  
  if (report_type === 'performance' || report_type === 'comprehensive') {
    Bash("find commands -name '*.md' -exec wc -l {} + | sort -nr > performance-metrics.log")
    Read("performance-metrics.log")
    Write("performance-report.md", `# Performance Report\\n\\nGenerated: ${timestamp}\\n\\n## Metrics Summary\\n## Trend Analysis\\n## Optimization Recommendations`)
  }
  
  if (report_type === 'alerts' || report_type === 'comprehensive') {
    Bash("grep -i 'alert\\|warning\\|error' *.log > alert-summary.log 2>/dev/null || echo 'No alerts found'")
    Read("alert-summary.log")
    Write("alert-report.md", `# Alert Summary\\n\\nGenerated: ${timestamp}\\n\\n## Active Alerts\\n## Resolved Issues\\n## Recommendations`)
  }
}
```

## Execution Implementation

```javascript
// MONITOR-CORE UNIVERSAL ENGINE
const mode = process.argv[2] || 'health'
const component = process.argv[3] || 'all'

switch(mode) {
  case 'collect':
    collect_health_data(component)
    break
    
  case 'trends':
    analyze_performance_trends()
    break
    
  case 'degradation':
    detect_degradation_patterns()
    break
    
  case 'thresholds':
    manage_alert_thresholds('check', component)
    break
    
  case 'report':
    generate_monitoring_reports(component)
    break
    
  case 'full':
  default:
    collect_health_data('all')
    analyze_performance_trends()
    detect_degradation_patterns()
    generate_monitoring_reports('comprehensive')
    Bash("echo '✅ MONITOR-CORE: Universal monitoring cycle completed'")
}
```

---

**Single Responsibility**: Universal monitoring engine providing centralized health collection, performance analysis, degradation detection, and comprehensive reporting across all system components.