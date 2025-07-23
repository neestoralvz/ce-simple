# Agent Coordinate - Planning Command

## Purpose
High-level orchestration strategy development for agent coordination workflows. Defines coordination patterns, manages workflow dependencies, and handles coordination failures.

## Principles and Guidelines

**Single Responsibility**: Focus exclusively on coordination strategy without execution
**Granular Planning**: Break coordination into small, manageable planning steps  
**Dependency Management**: Clear workflow dependencies with explicit sequencing
**Error Recovery**: Built-in coordination failure handling and recovery protocols

## Execution Process

### Phase 1: Strategy Development
Update TodoWrite: Mark "Coordination strategy development" as in_progress

Analyze coordination requirements:
- Review agent types and capabilities needed
- Identify workflow dependencies between agents
- Assess coordination complexity and constraints
- Determine optimal coordination approach

Generate coordination strategy:
- Define agent interaction patterns
- Specify dependency resolution sequence
- Plan communication protocols between agents
- Document coordination decision points

### Phase 2: Workflow Planning
Update TodoWrite: Complete previous, mark "Workflow dependency planning" as in_progress

Plan execution sequence optimization:
- Map agent execution order and dependencies
- Identify parallel execution opportunities
- Define synchronization points and handoffs
- Plan coordination checkpoint validation

Create workflow specification:
- Document execution sequence requirements
- Specify inter-agent communication needs
- Define coordination monitoring points
- Plan dependency validation steps

### Phase 3: Coordination Implementation
Update TodoWrite: Complete previous, mark "Coordination implementation" as in_progress

Implement coordination strategy:
- Configure coordination mechanisms
- Set up dependency tracking systems
- Establish communication protocols
- Initialize coordination monitoring

Validate coordination setup:
- Test coordination mechanisms functionality
- Verify dependency tracking accuracy
- Confirm communication protocol operation
- Validate monitoring system readiness

### Phase 4: Error Handling Integration
Update TodoWrite: Complete previous, mark "Coordination error handling" as in_progress

Handle coordination failure scenarios:
- Define coordination failure detection methods
- Implement recovery strategy protocols
- Set up failure escalation procedures
- Test error recovery mechanisms

If coordination failures occur:
- Add TodoWrite task: "Resolve coordination failure: [specific issue]"
- Implement specific recovery strategy for failure type
- Validate recovery effectiveness before proceeding
- Document lessons learned for future coordination

Update TodoWrite: Complete all coordination planning tasks
Add follow-up: "Coordination strategy ready for agent deployment"

---

**Single Responsibility**: Planning focused exclusively on agent coordination strategy development and workflow dependency management.**