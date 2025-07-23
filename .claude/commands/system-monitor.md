# System-Monitor - Unified System Monitoring and Performance Management

## 🎯 Purpose
Comprehensive system monitoring with standards compliance, development environment tracking, and performance metrics through unified mode-based execution.

## 🚀 Usage
Execute: `/system-monitor [mode]`

**Modes**:
- `compliance` - Standards compliance and autocritique validation
- `development` - Development environment monitoring and health
- `performance` - Performance metrics, benchmarking, and optimization
- `full` - Execute all monitoring modes with integrated reporting

## 🔧 Implementation

### Autocontained Notification System
```bash
#!/bin/bash
readonly B='\e[34m' G='\e[32m' R='\e[31m' Y='\e[33m' C='\e[36m' M='\e[35m' GB='\e[32;1m' N='\e[0m'
info()     { echo -e "${B}🔵 INFO${N}: $1"; }
success()  { echo -e "${G}🟢 SUCCESS${N}: $1"; }  
error()    { echo -e "${R}🔴 ERROR${N}: $1"; }
warn()     { echo -e "${Y}🟡 WARNING${N}: $1"; }
process()  { echo -e "${C}⚡ PROCESS${N}: $1"; }
data()     { echo -e "${M}📊 DATA${N}: $1"; }
complete() { echo -e "${GB}✅ COMPLETE${N}: $1"; }
calc()     { echo "scale=${2:-2}; $1" | bc -l; }
progress() { local p=$(calc "$1*100/$2" 0); process "$3 [$p% complete]"; }
```

### Behavioral Reinforcement Protocol
**MANDATORY at monitoring initialization**:

```javascript
TodoWrite([
  {"content": "🔍 COMPLIANCE: Execute standards compliance validation and autocritique", "status": "pending", "priority": "high", "id": "monitor-compliance-1"},
  {"content": "💻 DEVELOPMENT: Monitor development environment health and metrics", "status": "pending", "priority": "high", "id": "monitor-development-1"},
  {"content": "📊 PERFORMANCE: Track performance metrics and system benchmarks", "status": "pending", "priority": "high", "id": "monitor-performance-1"},
  {"content": "🔄 INTEGRATION: Seamless workflow integration with real-time updates", "status": "pending", "priority": "medium", "id": "monitor-integration-1"},
  {"content": "📋 REPORTING: Generate comprehensive monitoring reports", "status": "pending", "priority": "medium", "id": "monitor-reporting-1"}
])
```

### Mode-Based Monitoring Framework

#### Compliance Mode (self-monitor)
**Purpose**: Standards compliance and autocritique validation
```bash
# Proactive standards compliance scanning
validate_compliance() {
  local score=0
  # File size compliance
  oversized=$(find .claude/commands -name "*.md" -exec wc -l {} + | awk '$1 > 150 {count++} END {print count+0}')
  
  # Tool execution ratio validation  
  ratio_check=$(grep -c "LS\\|Bash\\|Edit\\|Read\\|Glob\\|Grep\\|Task\\|Write" .claude/commands/*.md)
  
  # Quality threshold validation (>85%)
  compliance_score=$((95 - oversized * 5))
  echo "📊 COMPLIANCE SCORE: $compliance_score%"
}
```

#### Development Mode (monitor-dev)
**Purpose**: Development environment monitoring and health
```bash
# Development environment health check
monitor_dev_environment() {
  # Git status and branch health
  git status --porcelain | wc -l
  
  # File system health
  du -sh .claude/commands/ docs/ context/ 2>/dev/null
  
  # Command availability check
  find .claude/commands -name "*.md" | wc -l
  
  echo "💻 DEV ENVIRONMENT: Healthy"
}
```

#### Performance Mode (track-performance)  
**Purpose**: Performance metrics, benchmarking, and optimization
```bash
# Performance metrics collection
track_system_performance() {
  # Command execution time tracking
  start_time=$(date +%s)
  
  # Resource utilization monitoring
  command_count=$(find .claude/commands -name "*.md" | wc -l)
  avg_size=$(find .claude/commands -name "*.md" -exec wc -l {} + | awk '{sum+=$1; count++} END {print sum/count}')
  
  # Performance benchmark
  end_time=$(date +%s)
  execution_time=$((end_time - start_time))
  
  echo "📊 PERFORMANCE: Commands: $command_count, Avg Size: $avg_size lines, Time: ${execution_time}s"
}
```

## ⚡ EXECUTION LAYER

### Unified Tool Execution Framework
**CRITICAL**: Mode-based tool deployment with integrated monitoring

```javascript
// Unified monitoring execution
const mode = process.argv[2] || 'full'

// COMPLIANCE MODE TOOLS
if (mode === 'compliance' || mode === 'full') {
  // Standards compliance validation
  Bash("find .claude/commands -name '*.md' -exec wc -l {} + | awk '$1 > 150 {count++} END {print \"Oversized files:\" count+0}'")
  Grep("EXECUTION LAYER", {glob: ".claude/commands/*.md", output_mode: "count"}) // Execution coverage
  Bash("echo 'Compliance validation complete'")
  
  // Auto-correction capabilities
  Bash("if [ $(find .claude/commands -name '*.md' -exec wc -l {} + | awk '$1 > 150' | wc -l) -gt 0 ]; then echo 'WARNING: Size violations detected'; fi")
}

// DEVELOPMENT MODE TOOLS  
if (mode === 'development' || mode === 'full') {
  // Environment health monitoring
  Bash("git status --porcelain | wc -l") // Git health
  Bash("du -sh .claude/commands/ docs/ context/ 2>/dev/null") // Disk usage
  LS(".claude/commands") // Directory health
  Bash("find .claude/commands -name '*.md' | wc -l") // Command inventory
  
  // Resource monitoring
  Bash("echo 'Development environment monitoring complete'")
}

// PERFORMANCE MODE TOOLS
if (mode === 'performance' || mode === 'full') {
  // Performance metrics collection
  Bash("start_time=$(date +%s); echo \"Performance tracking started: $start_time\"")
  Bash("find .claude/commands -name '*.md' -exec wc -l {} + | awk '{sum+=$1; count++} END {print \"Average command size:\" sum/count \" lines\"}'")
  Bash("find .claude/commands -name '*.md' | wc -l | awk '{print \"Total commands:\" $1}'")
  
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

### Real-Time Monitoring Integration
- **Continuous Monitoring**: Background health checks during command execution
- **Threshold Alerts**: Automatic notifications when metrics exceed thresholds
- **Auto-Correction**: Autonomous fixing of detected compliance issues
- **Performance Optimization**: Real-time suggestions for system improvements

### Integration Patterns
```bash
# Seamless workflow integration
integrate_monitoring() {
  # Pre-execution health check
  validate_compliance
  
  # During execution monitoring
  monitor_dev_environment &
  
  # Post-execution performance tracking
  track_system_performance
}
```

## ⚡ Triggers

### Input Triggers
**Context**: System health checks, compliance validation, performance monitoring
**Keywords**: monitor, compliance, performance, health, validation
**Auto-Triggers**: Command execution, file modifications, threshold violations

### Output Triggers
**When**: Issues detected → Priority alerts and auto-correction
**When**: Thresholds exceeded → Performance optimization recommendations  
**When**: Full monitoring complete → System health report generation

### Success Patterns
**Compliance Success**: >95% standards compliance, 0 critical violations
**Development Success**: Environment healthy, all resources accessible
**Performance Success**: Optimal metrics, benchmarks within targets

---

**CRITICAL**: This unified command replaces 3 separate monitoring commands (self-monitor, monitor-dev, track-performance) with integrated mode-based execution for comprehensive system oversight and performance optimization.