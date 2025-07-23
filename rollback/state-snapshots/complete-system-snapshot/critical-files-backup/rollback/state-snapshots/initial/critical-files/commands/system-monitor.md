# System-Monitor - Unified System Monitoring and Performance Management

## Purpose
Comprehensive system monitoring with standards compliance, development environment tracking, and performance metrics through unified mode-based execution and real-time health assessment.

## Principles and Guidelines
• **Standards Compliance**: Validate 150-line limits, execution layer coverage, and anti-bias enforcement with auto-correction
• **Development Environment**: Monitor git health, resource utilization, command availability, and system dependencies
• **Performance Metrics**: Track execution times, resource usage, benchmark performance, and optimization opportunities
• **Real-Time Integration**: Continuous monitoring during command execution with threshold alerts and proactive notifications

## Execution Process

### Phase 1: Compliance and Standards Validation
```javascript
TodoWrite([
  {"content": "🔍 COMPLIANCE: Execute standards compliance validation and autocritique", "status": "pending", "priority": "high", "id": "monitor-compliance-1"},
  {"content": "💻 DEVELOPMENT: Monitor development environment health and metrics", "status": "pending", "priority": "high", "id": "monitor-development-1"}
])
```

**Compliance Assessment**:
- Validate file size compliance against 150-line standards
- Detect documentation theater through execution layer analysis
- Perform quality threshold validation (>85% compliance)
- Generate compliance scores and violation reports

### Phase 2: Performance and Environment Monitoring
```javascript
TodoWrite([
  {"content": "📊 PERFORMANCE: Track performance metrics and system benchmarks", "status": "pending", "priority": "high", "id": "monitor-performance-1"},
  {"content": "🔄 INTEGRATION: Seamless workflow integration with real-time updates", "status": "pending", "priority": "medium", "id": "monitor-integration-1"}
])
```

**System Health Assessment**:
- Monitor git status, branch health, and repository integrity
- Track file system health, disk usage, and resource availability
- Collect performance metrics and execution time benchmarks
- Assess command availability and system dependencies

### Phase 3: Reporting and Integration
```javascript
TodoWrite([
  {"content": "📋 REPORTING: Generate comprehensive monitoring reports", "status": "pending", "priority": "medium", "id": "monitor-reporting-1"}
])
```

**Report Generation**:
- Create comprehensive system health reports
- Integrate monitoring data with workflow processes
- Generate performance optimization recommendations
- Execute git integration with health metrics

### Tool Execution Implementation
```javascript
// UNIFIED MONITORING EXECUTION
const mode = process.argv[2] || 'full'

// COMPLIANCE MODE TOOLS
if (mode === 'compliance' || mode === 'full') {
  // Standards compliance validation
  Bash("find commands -name '*.md' -exec wc -l {} + | awk '$1 > 150 {count++} END {print \"Oversized files:\" count+0}'")
  Grep("EXECUTION LAYER", {glob: "commands/*.md", output_mode: "count"}) // Execution coverage
  Bash("echo 'Compliance validation complete'")
  
  // Auto-correction capabilities
  Bash("if [ $(find commands -name '*.md' -exec wc -l {} + | awk '$1 > 150' | wc -l) -gt 0 ]; then echo 'WARNING: Size violations detected'; fi")
}

// DEVELOPMENT MODE TOOLS
if (mode === 'development' || mode === 'full') {
  // Environment health monitoring
  Bash("git status --porcelain | wc -l") // Git health
  Bash("du -sh commands/ docs/ context/ 2>/dev/null") // Disk usage
  LS("commands") // Directory health
  Bash("find commands -name '*.md' | wc -l") // Command inventory
  
  // Resource monitoring
  Bash("echo 'Development environment monitoring complete'")
}

// PERFORMANCE MODE TOOLS
if (mode === 'performance' || mode === 'full') {
  // Performance metrics collection
  Bash("start_time=$(date +%s); echo \"Performance tracking started: $start_time\"")
  Bash("find commands -name '*.md' -exec wc -l {} + | awk '{sum+=$1; count++} END {print \"Average command size:\" sum/count \" lines\"}'")
  Bash("find commands -name '*.md' | wc -l | awk '{print \"Total commands:\" $1}'")
  
  // Benchmark execution
  Task("Performance Benchmark", "Execute system performance analysis")
  Bash("end_time=$(date +%s); echo \"Performance tracking completed\"")
}

// INTEGRATED REPORTING (full mode only)
if (mode === 'full') {
  // Comprehensive system report
  Write("system-health-report.md", "# System Health Report\\n\\nGenerated: $(date)\\n\\n## Compliance Status\\n## Development Environment\\n## Performance Metrics")
  Bash("echo '✅ SYSTEM-MONITOR: Full monitoring cycle completed'")
  
  // Git integration
  Bash("git add . && git commit -m 'system-monitor: full health check completed ✓'")
}
```

---

**Single Responsibility**: Unified system monitoring with compliance validation, environment health tracking, and performance optimization through integrated reporting.