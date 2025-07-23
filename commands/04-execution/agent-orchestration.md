# Agent Orchestration - Planning Command

## Purpose
Master orchestrator for intelligent agent deployment and coordination. Coordinates specialized commands for complexity assessment, deployment, monitoring, and result consolidation.

## Principles and Guidelines

**Single Responsibility**: Focus exclusively on orchestration coordination without direct agent management
**Granular Orchestration**: Break coordination into small, manageable orchestration steps
**Command Management**: Clear command sequencing with explicit dependency requirements
**Error Recovery**: Built-in orchestration failure handling and command coordination protocols

## Execution Process

### Phase 1: Complexity Assessment and Strategy
Update TodoWrite: Mark "Agent orchestration complexity assessment" as in_progress

Execute complexity analysis for orchestration strategy:
- Execute `/complexity-assess` for workload complexity calculation
- Validate complexity score and strategy recommendation
- Determine optimal orchestration approach based on assessment
- Prepare orchestration parameters for deployment coordination

Execute strategy coordination planning:
- Execute `/agent-coordinate` for coordination strategy development
- Validate workflow dependencies and sequencing requirements
- Confirm coordination mechanisms and communication protocols
- Prepare coordination strategy for deployment execution

### Phase 2: Agent Deployment and Load Management
Update TodoWrite: Complete previous, mark "Agent deployment coordination" as in_progress

Coordinate agent deployment process:
- Execute `/agent-deploy` for specialized agent deployment coordination
- Validate successful agent deployment and startup
- Confirm Task Tool configurations and agent readiness
- Monitor deployment status and handle deployment issues

Implement load balancing optimization:
- Execute `/load-balance` for resource distribution analysis
- Apply load balancing recommendations to deployment
- Optimize workload distribution across deployed agents
- Validate balanced resource allocation and utilization

### Phase 3: System Monitoring and Performance Tracking
Update TodoWrite: Complete previous, mark "Agent monitoring and performance" as in_progress

Initiate comprehensive monitoring:
- Execute `/system-monitor-agents` for health and status monitoring
- Monitor agent execution and performance metrics
- Track system health indicators and alert conditions
- Validate monitoring data accuracy and completeness

Implement performance analysis:
- Execute `/performance-track` for efficiency analysis and optimization
- Collect performance metrics and trend analysis
- Generate optimization recommendations for system improvement
- Validate performance analysis and improvement opportunities

### Phase 4: Result Consolidation and Final Reporting
Update TodoWrite: Complete previous, mark "Result consolidation and reporting" as in_progress

Consolidate orchestration results:
- Execute `/result-consolidate` for comprehensive result integration
- Synthesize findings from all orchestrated agents
- Generate consolidated documentation and reports
- Validate result accuracy and completeness

Generate final orchestration report:
- Document orchestration strategy and execution results
- Record performance metrics and system health status
- Report deployment success and optimization achievements
- Provide comprehensive orchestration summary

If orchestration failures occur:
- Add TodoWrite task: "Resolve orchestration failure: [specific command/issue]"
- Implement recovery strategy for failed command coordination
- Re-execute failed orchestration components with adjustments
- Validate recovery success before proceeding to next phase

Update TodoWrite: Complete all agent orchestration tasks
Add follow-up: "Agent orchestration complete with consolidated results ready"

---

**Single Responsibility**: Planning focused exclusively on coordinating specialized agent management commands through orchestrated workflow execution.**