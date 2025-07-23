# Track Performance

## Purpose
Performance tracking, benchmarking, and metrics collection for development workflows.

## Usage
`/track-performance [baseline|measure|compare|report] [parameters]`

## Implementation

### Notification System
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
```

### Tracking Protocol
```javascript
// 1. BASELINE ESTABLISHMENT (real execution)
Bash("if [[ -f tools/performance-tracker.json ]]; then cp tools/performance-tracker.json tools/performance-baseline-$(date +%Y%m%d).json; fi") // Backup current metrics
Read("tools/performance-tracker.json") // Read current performance data

// 2. SYSTEM METRICS COLLECTION (real execution)
Bash("echo '{\"timestamp\": \"$(date -Iseconds)\", \"metrics\": {' > /tmp/current-metrics.json") // Start metrics collection
Bash("echo '\"memory_usage\": \"$(ps aux | awk '{sum+=$6} END {print sum/1024\" MB\"}')\",'; echo '\"cpu_load\": \"$(uptime | awk -F'load average:' '{print $2}')\",'; echo '\"disk_usage\": \"$(df -h . | tail -1 | awk '{print $5}')\"'; echo '}}' >> /tmp/current-metrics.json") // Collect system metrics

// 3. DEVELOPMENT WORKFLOW TIMING (real execution)
Bash("start_time=$(date +%s); echo \"Workflow timing started at: $(date)\"") // Start workflow timer
Task("Performance measurement", "measure development workflow performance and collect detailed metrics")
```

### Benchmarking Integration
- **Command Execution Timing**: Track execution time for all workflow commands
- **Resource Utilization**: Monitor CPU, memory, and disk usage during operations
- **Throughput Metrics**: Measure operations per minute/hour
- **Quality Metrics**: Track error rates and success percentages

### Data Management
```javascript
// Performance data validation and management
Grep("\"timestamp\"|\"metrics\"|\"performance\"", {path: "tools/performance-tracker.json", output_mode: "count"}) // Validate metrics format
Bash("jq '.metrics | keys' tools/performance-tracker.json 2>/dev/null || echo 'Invalid JSON format'") // Validate JSON structure
```

### Reporting Framework
- **Trend Analysis**: Compare current metrics with historical baselines
- **Bottleneck Identification**: Highlight performance degradation areas
- **Optimization Tracking**: Measure improvement after optimizations
- **Threshold Alerting**: Warn when performance metrics exceed acceptable ranges

## Triggers

### Input Triggers
**Context**: Performance measurement, benchmarking, optimization validation
**Keywords**: performance, benchmark, metrics, measure, track, timing

### Output Triggers
**When**: Performance degradation detected → Alert and generate optimization recommendations
**When**: Baseline requested → Establish new performance baseline
**Chain**: track-performance → analyze-parallel (for optimization) → monitor-dev (for validation)

## Module Integration

### Command Dependencies
- `/analyze-parallel` → Optimization target identification and scoring
- `/monitor-dev` → Real-time performance monitoring during operations
- `/git-worktree` → Isolated performance testing in separate environments

### Success Indicators
**Tracking Success**: Consistent metrics collection with <5% measurement variance
**Baseline Success**: Reliable performance baseline established across key metrics
**Analysis Success**: Clear performance trend identification and actionable insights

## Execution Layer

### Tool Executions
```javascript
// 1. PERFORMANCE DATA VALIDATION (real execution)
Read("tools/performance-tracker.json") // Read current performance configuration
Bash("test -f tools/performance-tracker.json && echo 'Performance tracker exists' || echo 'Creating new tracker'") // Validate tracker existence

// 2. METRICS COLLECTION (real execution)
Bash("echo '{\"session_start\": \"$(date -Iseconds)\", \"command\": \"track-performance\", \"metrics\": {}}' >> tools/performance-session-$(date +%Y%m%d).json") // Log session start
Task("System metrics", "collect comprehensive system performance metrics and resource utilization data")

// 3. BASELINE MANAGEMENT (real execution)
Bash("if [[ ! -f tools/performance-baseline.json ]]; then cp tools/performance-tracker.json tools/performance-baseline.json; echo 'Baseline established'; fi") // Create baseline if needed
```

### Integration Protocol
```javascript
// Integration with other performance commands
Task("Performance integration", "coordinate with analyze-parallel and monitor-dev for comprehensive performance management")
```

---

**CRITICAL**: This command provides comprehensive performance tracking with real metrics collection, baseline management, and optimization coordination across the development workflow.