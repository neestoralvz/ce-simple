# System Monitor Agents - Meta Command

## Purpose
Agent health and status monitoring for orchestration systems. Provides real-time monitoring, performance degradation detection, and system health reporting.

## Principles and Guidelines

**Single Responsibility**: Focus exclusively on monitoring without agent control or deployment management
**Granular Monitoring**: Break health tracking into small, specific monitoring steps
**Status Management**: Clear health thresholds with explicit alerting requirements
**Error Recovery**: Built-in monitoring failure handling and data validation protocols

## Execution Process

### Phase 1: Agent Health Status Collection
Update TodoWrite: Mark "Agent health status collection" as in_progress

Collect current agent health data:
- Check agent responsiveness and availability status
- Monitor execution progress and completion rates
- Detect agent failures and performance issues
- Assess individual agent health metrics

Use Read tool to collect monitoring data:
- Read agent execution logs for status information
- Extract performance metrics from system outputs
- Identify health trend patterns and anomalies
- Validate monitoring data completeness and accuracy

Generate baseline health inventory:
- Document individual agent status and performance
- Record system-wide health indicators
- Calculate performance trend analysis
- Identify alert conditions and threshold violations

### Phase 2: Performance Degradation Analysis
Update TodoWrite: Complete previous, mark "Performance degradation analysis" as in_progress

Analyze performance degradation patterns:
- Monitor response time increases across agents
- Track resource utilization spikes and patterns
- Identify bottleneck formation in system components
- Detect potential cascade failure conditions

Perform degradation trend analysis:
- Compare current performance against baseline metrics
- Implement trend analysis for early warning detection
- Assess impact on overall system performance
- Provide root cause identification support data

### Phase 3: System Health Reporting
Update TodoWrite: Complete previous, mark "System health report generation" as in_progress

Generate comprehensive health reports:
- Compile agent availability and uptime statistics
- Document performance metrics and trend analysis
- Record error rates and failure pattern analysis
- Summarize resource utilization across system

Use Write tool for health documentation:
- Write detailed system health status report
- Generate real-time agent status indicators
- Create performance graphs and metrics summary
- Document alert notifications and system warnings

### Phase 4: Recovery Monitoring and Validation
Update TodoWrite: Complete previous, mark "Recovery monitoring validation" as in_progress

Monitor agent failure recovery processes:
- Detect failed agents and isolation requirements
- Track recovery progress and validation steps
- Monitor recovery strategy effectiveness
- Update health status after successful recovery

Validate recovery monitoring data:
- Confirm failure detection and classification accuracy
- Assess recovery time and success metrics
- Evaluate system resilience and stability
- Document recovery patterns for future reference

If monitoring issues detected:
- Add TodoWrite task: "Resolve monitoring issue: [specific problem]"
- Implement monitoring data validation and correction
- Restore monitoring functionality before proceeding
- Document resolution approach for system improvement

Update TodoWrite: Complete all agent monitoring tasks
Add follow-up: "Agent health monitoring data ready for coordination"

---

**Single Responsibility**: Meta-system monitoring focused exclusively on agent health tracking and system status reporting.**