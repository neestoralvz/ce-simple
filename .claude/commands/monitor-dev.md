# Monitor-Dev - Real-Time Development Environment Monitoring

## 🎯 Purpose
Provide comprehensive real-time monitoring of parallel development environments and AI agent activities

## 🚀 Usage  
Execute: `/monitor-dev [snapshot|continuous] [parameters]`

## 🔧 Implementation

### Real-Time Monitoring Protocol
1. **WORKTREE-STATUS**: Check git branch status, modifications, and activity for each environment
2. **RESOURCE-TRACKING**: Monitor memory, CPU, and disk usage across development streams
3. **PROCESS-DETECTION**: Identify active AI agents and development processes
4. **ACTIVITY-SUMMARY**: Generate comprehensive development state overview
5. **CONTINUOUS-MODE**: Optional real-time monitoring with periodic updates

### System Intelligence Framework
**Snapshot Monitoring**:
```bash
Bash("./tools/parallel-monitoring.sh") // Single comprehensive report
```

**Continuous Monitoring**:
```bash
Bash("./tools/parallel-monitoring.sh --watch") // Real-time updates every 10 seconds
```

### Data Collection Framework
**WorkTree Analysis**: Branch status, file modifications, last commit activity
**Resource Metrics**: Memory utilization, CPU load, disk usage by worktrees
**Process Intelligence**: Claude instances, node processes, development tools

### Alert and Notification Integration
**High Resource Usage**: Alert when system utilization exceeds thresholds
**Development Conflicts**: Detect potential merge conflicts across worktrees
**Process Anomalies**: Identify stuck or failed development processes

## ⚡ Triggers

### Input Triggers
**Context**: Active parallel development requiring oversight and coordination
**Previous**: `/git-worktree` → environments created, monitoring needed
**Keywords**: monitor, status, resources, activity, development

### Output Triggers
**When**: Performance issues detected → `/analyze-parallel` for optimization
**When**: Resource limits approached → `/track-performance` for historical analysis
**Chain**: monitor-dev → analyze-parallel → track-performance → git-worktree

### Success Patterns
**Monitoring Success**: Real-time visibility into all development streams achieved
**Resource Success**: System utilization optimized without bottlenecks
**Coordination Success**: Development conflicts prevented through early detection

---

**CRITICAL**: Provides essential oversight for aggressive parallelization workflows with intelligent resource monitoring and conflict prevention