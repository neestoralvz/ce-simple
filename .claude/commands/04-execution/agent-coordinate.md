# Agent Coordinate - Execution Command

## Purpose
Orchestrates distributed agent coordination through Task Tool deployment, managing workflow dependencies, communication protocols, and failure recovery patterns to enable synchronized parallel execution across multiple agents.

## Principles and Guidelines

- **Single Responsibility**: Focus exclusively on agent coordination orchestration without handling deployment or validation tasks
- **Granular Coordination**: Break coordination workflows into small, manageable dependency chains with clear sequencing
- **Workflow Management**: Clear agent interaction dependencies with explicit communication protocols and validation checkpoints
- **Error Recovery**: Built-in coordination failure handling and recovery protocols with automated re-establishment mechanisms

## Execution Process

### Phase 1: Coordination Strategy Development
Update TodoWrite: Mark "Agent coordination strategy development" as in_progress

Analyze coordination requirements:
- Review agent types and required capabilities
- Identify workflow dependencies between agents
- Assess coordination complexity and constraints
- Determine optimal coordination approach

Develop coordination strategy:
- Define agent interaction patterns and protocols
- Specify dependency resolution sequence
- Plan communication channels between agents
- Document coordination decision points

### Phase 2: Workflow Dependency Planning
Update TodoWrite: Complete previous, mark "Workflow dependency planning" as in_progress

Map execution dependencies:
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

Implement coordination mechanisms:
- Configure coordination systems and protocols
- Set up dependency tracking mechanisms
- Establish communication channels between agents
- Initialize coordination monitoring systems

Validate coordination setup:
- Test coordination mechanisms functionality
- Verify dependency tracking accuracy
- Confirm communication protocol operation
- Validate monitoring system readiness

### Phase 4: Error Handling and Recovery
Update TodoWrite: Complete previous, mark "Coordination error handling" as in_progress

Setup coordination failure protocols:
- Define coordination failure detection methods
- Implement recovery strategy protocols
- Set up failure escalation procedures
- Test error recovery mechanisms

If coordination failures occur:
- Add TodoWrite task: "Resolve coordination failure: [specific issue]"
- Implement specific recovery strategy for failure type
- Validate recovery effectiveness before proceeding
- Document lessons learned for future coordination

Update TodoWrite: Complete all coordination tasks
Add follow-up: "Agent coordination strategy ready for deployment"

**Single Responsibility**: Coordination orchestrator focused exclusively on agent workflow coordination without deployment or validation responsibilities.