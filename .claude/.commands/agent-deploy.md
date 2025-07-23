# Agent Deploy - Specialized Execution Command

## Purpose
Pure agent deployment coordination without orchestration logic. Handles Task Tool deployment, agent startup validation, and deployment error recovery.

## Principles and Guidelines

**Single Responsibility**: Focus exclusively on agent deployment without coordination strategy
**Granular Deployment**: Break deployment into small, manageable deployment steps
**Configuration Management**: Clear deployment parameters with explicit validation requirements
**Error Recovery**: Built-in deployment failure handling and retry protocols

## Execution Process

### Phase 1: Deployment Configuration
Update TodoWrite: Mark "Agent deployment configuration" as in_progress

Validate deployment parameters:
- Check agent count and role specifications
- Verify task prompts and execution requirements
- Confirm deployment strategy (sequential/parallel)
- Validate error handling and retry policies

Prepare deployment configuration:
- Organize agent specifications by type and role
- Prepare Task Tool prompts for each agent
- Set deployment sequence and timing
- Configure monitoring and validation checkpoints

### Phase 2: Agent Deployment Execution
Update TodoWrite: Complete previous, mark "Agent deployment execution" as in_progress

Execute Task Tool deployment:
- Deploy agents using Task Tool with specified prompts
- Configure parallel execution where appropriate
- Handle deployment batching and sequencing
- Monitor agent startup and initialization

Use Task Tool for agent deployment:
- Deploy primary agents with specific task descriptions
- Deploy secondary agents with dependent configurations
- Configure agent communication and coordination
- Validate successful agent startup and readiness

### Phase 3: Deployment Validation
Update TodoWrite: Complete previous, mark "Deployment validation" as in_progress

Verify deployment success:
- Check all specified agents deployed successfully
- Validate Task Tools properly configured and active
- Confirm no deployment errors or startup failures
- Test agent responsiveness and communication

Generate deployment status report:
- Document agent deployment count and success rate
- Record Task Tool assignment validation results
- Report startup sequence completion status
- Log deployment metrics for monitoring

### Phase 4: Status Reporting and Handoff
Update TodoWrite: Complete previous, mark "Deployment status reporting" as in_progress

Generate final deployment report:
- Create comprehensive deployment summary
- Document agent configurations and assignments
- Report deployment success metrics and timing
- Prepare status for orchestration coordination

If deployment fails:
- Add TodoWrite task: "Resolve deployment failure: [specific issue]"
- Implement deployment retry strategy for failed agents
- Adjust configuration based on failure analysis
- Validate successful recovery before completion

Update TodoWrite: Complete all deployment tasks
Add follow-up: "Agent deployment ready for coordination handoff"

---

**Single Responsibility**: Specialized execution focused exclusively on agent deployment coordination and validation.**