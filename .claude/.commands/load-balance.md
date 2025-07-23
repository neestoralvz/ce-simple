# Load Balance - Analysis Command

## Purpose
Resource distribution analysis and optimization for agent workload management. Analyzes current utilization and generates load balancing recommendations.

## Principles and Guidelines

**Single Responsibility**: Focus exclusively on load analysis without agent deployment or coordination
**Granular Analysis**: Break utilization assessment into small, measurable analysis steps
**Resource Management**: Clear capacity thresholds with explicit optimization requirements
**Error Recovery**: Built-in analysis failure handling and data validation protocols

## Execution Process

### Phase 1: Resource Utilization Assessment
Update TodoWrite: Mark "Resource utilization assessment" as in_progress

Analyze current agent resource utilization:
- Assess cognitive load across all active agents
- Monitor processing capacity for each agent type
- Identify bottlenecks in resource allocation
- Calculate utilization percentages for system components

Generate utilization baseline:
- Document current agent count and active status
- Record individual agent workload distribution
- Calculate resource utilization percentages
- Identify performance degradation indicators

### Phase 2: Load Distribution Analysis
Update TodoWrite: Complete previous, mark "Load distribution analysis" as in_progress

Analyze workload distribution patterns:
- Examine workload characteristics and requirements
- Assess current agent assignment effectiveness
- Evaluate agent capabilities and specializations
- Identify distribution inefficiencies and imbalances

Calculate optimal distribution strategy:
- Balance workload across available agents
- Minimize cognitive overload risks for agents
- Maximize parallel execution efficiency opportunities
- Account for task dependencies and sequencing requirements

### Phase 3: Capacity Management Analysis
Update TodoWrite: Complete previous, mark "Agent capacity analysis" as in_progress

Monitor and analyze agent capacity:
- Track maximum sustainable workload per agent
- Detect when capacity thresholds are approaching
- Calculate remaining available capacity in system
- Assess capacity utilization trends and patterns

Use Read tool to analyze performance data:
- Read existing agent performance logs
- Extract capacity utilization metrics
- Identify capacity constraint patterns
- Validate capacity calculations against historical data

### Phase 4: Optimization Recommendations
Update TodoWrite: Complete previous, mark "Load balancing recommendations" as in_progress

Generate specific load balancing recommendations:
- Create workload redistribution suggestions
- Propose agent reassignment strategies
- Recommend capacity scaling adjustments
- Develop performance optimization strategies

Use Write tool to document recommendations:
- Write comprehensive load balancing analysis report
- Document specific optimization strategies with priorities
- Include utilization metrics and trend analysis
- Provide implementation guidance for recommendations

If analysis issues detected:
- Add TodoWrite task: "Address load balancing issue: [specific problem]"
- Implement data validation and correction procedures
- Validate analysis accuracy before recommendations
- Document resolution approach for future reference

Update TodoWrite: Complete all load balancing analysis tasks
Add follow-up: "Load balancing recommendations ready for implementation"

---

**Single Responsibility**: Analysis focused exclusively on resource distribution and agent workload optimization.**