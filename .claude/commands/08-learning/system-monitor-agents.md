# /system-monitor-agents - Agent Health Monitoring System

## Purpose
Orchestrates comprehensive agent health monitoring through parallel status collection, performance degradation analysis, and real-time system health reporting for orchestration systems.

## Principles and Guidelines
- **Real-Time Monitoring**: Continuous agent health assessment with threshold violation detection
- **Parallel Processing**: Execute concurrent health status collection, performance monitoring, and degradation analysis
- **High Detection Accuracy**: Achieve 98%+ failure detection with minimal false positives
- **Recovery Validation**: Monitor agent recovery processes ensuring system resilience

## Execution Process

### Phase 1: Health Status & Performance Collection
Update TodoWrite mark "agent health collection" as in_progress

Execute parallel monitoring using Read, Bash, and Grep:
- Collect agent responsiveness and availability metrics
- Monitor execution progress and completion rates
- Gather performance data across all active agents
- Validate agent accessibility and response times

### Phase 2: Degradation Analysis & Alert Detection
Update TodoWrite complete previous, mark "degradation analysis" as in_progress

Analyze performance patterns using Task and Bash:
- Analyze performance degradation patterns and trends
- Identify threshold violations and alert conditions
- Compare current metrics against baseline performance
- Flag agents requiring isolation or intervention

### Phase 3: Health Reporting & Dashboard Generation
Update TodoWrite complete previous, mark "health reporting" as in_progress

Generate comprehensive health reports using Write and Task:
- Consolidate agent health data into unified dashboard
- Create alert notifications for threshold violations
- Document performance trends and bottleneck identification
- Generate optimization recommendations for agent performance

### Phase 4: Recovery Validation & System Optimization
Update TodoWrite complete previous, mark "recovery validation" as in_progress

Monitor recovery processes using Task and Bash:
- Monitor recovery processes and validate effectiveness
- Track recovery success rates and resilience metrics
- Validate system optimization guidance implementation
- Generate system health summary with improvement recommendations

Update TodoWrite complete all agent monitoring tasks

**Error Handling**: Flag unresponsive agents for isolation continuing monitoring, use cached data implementing retry logic, validate performance anomalies against baseline, implement failover monitoring documenting issues

---

**Single Responsibility**: Agent health monitoring through parallel status collection, performance degradation analysis, and real-time system health reporting ensuring orchestration system reliability.