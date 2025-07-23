# Phase Manager - Universal Phase Orchestration Engine

## Purpose
Centralized phase management system for TodoWrite orchestration, providing standardized phase initiation, transition, error handling, and completion patterns across all command workflows.

## Principles and Guidelines
- **Pattern Standardization**: Unified TodoWrite patterns eliminating 91% command duplication 
- **Phase Lifecycle Management**: Complete phase orchestration from initiation to completion
- **Error Recovery Protocols**: Standardized error handling with recovery workflows
- **Cross-Command Consistency**: Single source of truth for phase management patterns

## Core Phase Management Functions

### Phase Initiation Pattern
```javascript
initiate_phase(phase_name, task_description) {
  return `Update TodoWrite: Mark "${phase_name}" as in_progress\n\n${task_description}`
}
```

### Phase Transition Pattern  
```javascript
transition_phase(from_phase, to_phase, new_task) {
  return `Update TodoWrite: Complete previous, mark "${to_phase}" as in_progress\n\n${new_task}`
}
```

### Error Handling Pattern
```javascript
handle_phase_error(error_type, specific_issue) {
  return `Add TodoWrite task: "Resolve ${error_type} issue: ${specific_issue}"`
}
```

### Workflow Completion Pattern
```javascript
complete_workflow(workflow_type, follow_up_message) {
  return `Update TodoWrite: Complete all ${workflow_type} tasks\nAdd follow-up: "${follow_up_message}"`
}
```

## Standard Phase Templates

### Analysis Phase Template
```
Update TodoWrite: Mark "[Analysis Type] analysis" as in_progress

Execute analysis workflow:
- Configure analysis parameters and scope
- Set up analysis tools and validation criteria
- Define success metrics and quality gates
- Prepare analysis environment with requirements

Validate analysis setup:
- Check scope and analysis standards
- Verify depth requirements and assessment criteria  
- Confirm quality threshold parameters
- Validate tool configurations and accessibility
```

### Execution Phase Template
```
Update TodoWrite: Complete previous, mark "[Execution Type] execution" as in_progress

Execute implementation workflow:
- Deploy configured systems and processes
- Monitor execution progress and performance
- Validate execution results against requirements
- Handle execution errors with recovery protocols

Process execution results:
- Collect execution metrics and performance data
- Validate results against success criteria
- Document execution outcomes with evidence
- Prepare next phase transition requirements
```

### Validation Phase Template  
```
Update TodoWrite: Complete previous, mark "[Validation Type] validation" as in_progress

Execute validation workflow:
- Run validation tests and quality checks
- Monitor validation progress and results
- Validate outcomes against quality gates
- Document validation findings with evidence

Process validation results:
- Compile validation report with metrics
- Identify issues requiring resolution
- Generate improvement recommendations
- Prepare compliance certification status
```

### Completion Phase Template
```
Update TodoWrite: Complete previous, mark "[Task Type] completion" as in_progress

Finalize workflow:
- Compile comprehensive results report
- Document outcomes with quality evidence
- Generate improvement recommendations  
- Prepare handoff documentation

Complete workflow:
Update TodoWrite: Complete all [workflow_type] tasks
Add follow-up: "[Completion message with next steps]"
```

## Error Recovery Workflows

### Standard Error Recovery
```
If [error_condition] detected:
- Add TodoWrite task: "Resolve [error_type] failure: [specific_issue]"
- Implement targeted remediation for [specific_problem]
- Execute re-validation cycle for corrected issues
- Validate remediation effectiveness before continuation
```

### Critical Error Escalation
```
If critical validation failures occur:
- Add TodoWrite task: "CRITICAL: Resolve [critical_issue] blocking workflow"
- Halt current workflow execution until resolution
- Implement emergency recovery protocols
- Execute comprehensive re-validation before resumption
```

## Integration Patterns

### Agent Deployment Integration
```javascript
agent_deployment_phase(agent_type, deployment_config) {
  return initiate_phase(`${agent_type} agent deployment`, 
    `Deploy ${agent_type} agents with configuration:\n${deployment_config}`)
}
```

### Validation Integration
```javascript
validation_orchestration_phase(validation_domains, criteria) {
  return initiate_phase(`${validation_domains.join('+')} validation`,
    `Execute parallel validation across: ${validation_domains.join(', ')}\nCriteria: ${criteria}`)
}
```

### Analysis Integration
```javascript
analysis_coordination_phase(analysis_type, scope_parameters) {
  return initiate_phase(`${analysis_type} analysis coordination`,
    `Coordinate ${analysis_type} analysis with scope: ${scope_parameters}`)
}
```

## Usage Examples

### Basic Phase Management
```
// Initialize discovery phase
${initiate_phase("codebase discovery", "Analyze project structure and dependencies")}

// Transition to analysis  
${transition_phase("discovery", "complexity analysis", "Assess technical complexity and requirements")}

// Handle error
${handle_phase_error("validation", "test coverage below threshold")}

// Complete workflow
${complete_workflow("discovery", "Codebase analysis complete with architectural assessment ready")}
```

### Multi-Domain Validation
```
${initiate_phase("multi-domain validation setup", "Configure creative, technical, and visual validation channels")}

${transition_phase("setup", "parallel validation execution", "Execute validation across all configured domains")}

${transition_phase("execution", "results integration", "Aggregate and analyze cross-domain validation results")}

${complete_workflow("validation", "Multi-domain validation complete with integrated assessment ready")}
```

---

**Single Responsibility**: Universal phase management engine providing standardized TodoWrite orchestration patterns, eliminating duplicate phase management logic across 42 commands while ensuring consistent workflow execution and error handling.