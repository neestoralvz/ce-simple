# Monitor-Dev - Real-Time Development Environment Monitoring

## 🎯 Purpose
Provide comprehensive real-time monitoring of parallel development environments and AI agent activities.

## 🚀 Usage
Execute: `/monitor-dev [snapshot|continuous] [parameters]`

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
```

### Real-Time Monitoring Protocol
**Comprehensive Development Tracking**:
```javascript
// 1. SYSTEM RESOURCE MONITORING (real execution)
Bash("ps aux | grep -E '(node|python|git|code)' | grep -v grep") // Monitor development processes
Bash("df -h . && free -h 2>/dev/null || vm_stat") // Check disk and memory usage

// 2. DEVELOPMENT ACTIVITY TRACKING (real execution)
Bash("git log --oneline -10") // Recent git activity
Bash("find . -name '*.{js,ts,py,md}' -mtime -1 | head -20") // Recently modified files

// 3. WORKTREE AND BRANCH MONITORING (real execution)
Bash("git worktree list 2>/dev/null || echo 'No worktrees active'") // Monitor active worktrees
Bash("git branch -v") // Track branch status
```

### Performance Monitoring Integration
**Real-Time Metrics Collection**:
- **Resource Usage**: CPU, memory, disk usage monitoring
- **Development Activity**: File changes, git operations, build processes
- **Agent Coordination**: Track AI agent activities and coordination
- **Performance Alerts**: Detect and report performance bottlenecks

### Continuous Monitoring Framework
**Intelligent Monitoring Modes**:
```javascript
// Snapshot mode - single point-in-time analysis
Task("Development snapshot", "capture current development environment state and metrics")

// Continuous mode - ongoing monitoring with alerts
Task("Continuous monitoring", "establish ongoing monitoring with intelligent alerting")
```

### Integration with Performance Suite
**Cross-Command Coordination**:
- **Performance Tracking**: Coordinate with `/track-performance` for metrics
- **Optimization**: Work with `/analyze-parallel` for performance improvements
- **Worktree Management**: Monitor `/git-worktree` operations

## ⚡ Triggers

### Input Triggers
**Context**: Development monitoring, performance tracking, system health checks
**Keywords**: monitor, track, watch, status, health, performance

### Output Triggers
**When**: Performance threshold exceeded → Alert and recommend optimization
**When**: Resource contention detected → Suggest workload balancing
**Chain**: monitor-dev → track-performance → analyze-parallel (if optimization needed)

## 🔗 Module Integration

### Command Dependencies
**Development Monitoring Suite**:
- `/track-performance` → Detailed performance metrics and benchmarking
- `/analyze-parallel` → Performance optimization recommendations
- `/git-worktree` → Worktree activity and coordination monitoring

### Success Indicators
**Monitoring Success**: Real-time metrics collection with <1% overhead
**Alert Success**: Accurate threshold detection and timely notifications
**Integration Success**: Seamless coordination with performance and optimization commands

## ⚡ EXECUTION LAYER

### Mandatory Tool Executions
```javascript
// 1. ENVIRONMENT MONITORING (real execution)
Bash("echo 'Development monitoring session: $(date)' && uptime") // System status
Bash("git status --porcelain | wc -l") // Count uncommitted changes

// 2. RESOURCE TRACKING (real execution)
Task("Resource monitoring", "collect comprehensive development environment metrics and resource utilization")

// 3. ACTIVITY MONITORING (real execution)
Bash("lsof +D . 2>/dev/null | grep -E '\\.(js|ts|py|md)$' | wc -l || echo 'File activity check'") // Monitor file access
Bash("echo 'Active monitoring: $(date)' >> .development-monitoring.log") // Log monitoring session
```

### Alert Framework
**Intelligent Threshold Management**:
```javascript
// Performance threshold monitoring
Bash("if [[ $(ps aux | grep -c node) -gt 10 ]]; then echo 'HIGH: Multiple Node processes detected'; fi") // Process monitoring
```

---

**CRITICAL**: This command provides comprehensive real-time development environment monitoring with intelligent alerting and performance integration.