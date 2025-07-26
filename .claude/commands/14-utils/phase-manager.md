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

### Phase 5 Routing Template
```
Update TodoWrite: Complete previous, mark "Phase 5: Route to specialized commands" as in_progress

Execute context analysis workflow:
- Analyze current workflow results and outcomes
- Extract key context indicators and patterns
- Assess task complexity and domain requirements
- Identify optimal command category for continuation

Generate routing decision:
- Apply decision matrix patterns for 15-category routing
- Match context patterns to specialized command capabilities
- Generate specific command recommendations with rationale
- Prepare standardized handoff message with context preservation

Execute intelligent routing:
- Format handoff message with complete context transfer
- Include workflow history and key decision points
- Specify next-phase requirements and success criteria
- Transfer execution to recommended specialized command
```

## Decision Matrix Patterns

### 15-Category Routing Decision Matrix

#### Foundation Layer (00-core)
```javascript
route_to_core(context_indicators) {
  if (context_indicators.includes('project_initialization')) return '/init-project'
  if (context_indicators.includes('context_management')) return '/context-engine'
  if (context_indicators.includes('notification_required')) return '/notify-manager'
  if (context_indicators.includes('session_transition')) return '/handoff-manager'
  if (context_indicators.includes('workflow_start')) return '/start'
  if (context_indicators.includes('advanced_discovery')) return '/enhanced-start'
  return null
}
```

#### Discovery & Analysis (01-discovery, 03-analysis)
```javascript
route_to_discovery_analysis(context_indicators, complexity_level) {
  // Discovery routing
  if (context_indicators.includes('codebase_analysis')) return '/explore-codebase'
  if (context_indicators.includes('external_research')) return '/explore-web'
  if (context_indicators.includes('deep_thinking') || complexity_level > 7) return '/think-layers'
  
  // Analysis routing
  if (context_indicators.includes('parallel_processing')) return '/analyze-parallel'
  if (context_indicators.includes('parallel_implementation')) return '/analyze-parallel-implementation'
  if (context_indicators.includes('complexity_assessment')) return '/complexity-assess'
  if (context_indicators.includes('load_balancing')) return '/load-balance'
  if (context_indicators.includes('problem_decomposition')) return '/problem-solving'
  
  return null
}
```

#### Planning & Strategy (02-planning)
```javascript
route_to_planning(context_indicators, project_phase) {
  if (context_indicators.includes('solution_architecture')) return '/architect-solution'
  if (context_indicators.includes('vision_feedback')) return '/feedback-vision'
  if (context_indicators.includes('phase_planning')) return '/plan-phases'
  if (context_indicators.includes('resource_planning')) return '/resource-plan'
  if (context_indicators.includes('risk_assessment')) return '/risk-assess'
  if (context_indicators.includes('strategy_optimization')) return '/strategy-optimize'
  if (context_indicators.includes('vision_propagation')) return '/vision-propagate'
  return null
}
```

#### Execution & Orchestration (04-execution)
```javascript
route_to_execution(context_indicators, execution_scope) {
  if (context_indicators.includes('agent_coordination')) return '/agent-coordinate'
  if (context_indicators.includes('agent_deployment')) return '/agent-deploy'
  if (context_indicators.includes('advanced_orchestration')) return '/agent-orchestration'
  if (context_indicators.includes('result_consolidation')) return '/result-consolidate'
  return null
}
```

#### Quality Assurance (05-validation)
```javascript
route_to_validation(context_indicators, validation_domains) {
  if (validation_domains.includes('performance')) return '/performance-validate'
  if (validation_domains.includes('quality_gates')) return '/quality-gates'
  if (validation_domains.includes('test_orchestration')) return '/test-orchestrate'
  if (validation_domains.includes('code')) return '/validate-code'
  if (validation_domains.includes('completion')) return '/validate-complete'
  if (validation_domains.includes('creative')) return '/validate-creative'
  if (validation_domains.includes('visual')) return '/validate-visual'
  return null
}
```

#### Specialized Categories (06-14)
```javascript
route_to_specialized(context_indicators, domain_type) {
  // Documentation (06)
  if (context_indicators.includes('documentation_maintenance')) return '/docs-maintain'
  
  // Maintenance (07)
  if (context_indicators.includes('context_optimization')) return '/context-optimize'
  
  // Learning (08)
  if (context_indicators.includes('pattern_extraction')) return '/capture-learnings'
  if (context_indicators.includes('performance_tracking')) return '/performance-track'
  if (context_indicators.includes('system_monitoring')) return '/system-monitor'
  if (context_indicators.includes('agent_monitoring')) return '/system-monitor-agents'
  
  // Git Workflows (09)
  if (context_indicators.includes('parallel_development')) return '/git-worktree'
  if (context_indicators.includes('worktree_initialization')) return '/worktree-start'
  if (context_indicators.includes('session_completion')) return '/worktree-close'
  if (context_indicators.includes('maintenance_cleanup')) return '/worktree-cleanup'
  
  // Standards (10)
  if (context_indicators.includes('naming_conventions')) return '/standard-naming'
  if (context_indicators.includes('writing_standards')) return '/standard-writing'
  if (context_indicators.includes('command_templates')) return '/template-command'
  if (context_indicators.includes('documentation_templates')) return '/template-docs'
  
  // Meta-system (11)
  if (context_indicators.includes('command_creation')) return '/command-create'
  if (context_indicators.includes('command_framework')) return '/command-creation'
  if (context_indicators.includes('command_maintenance')) return '/command-maintain'
  if (context_indicators.includes('cross_reference_validation')) return '/matrix-maintenance'
  
  // Mathematical (12)
  if (context_indicators.includes('metrics_analysis')) return '/analyze-metrics'
  if (context_indicators.includes('complexity_calculation')) return '/calculate-complexity'
  if (context_indicators.includes('optimization_calculation')) return '/optimize-calculate'
  if (context_indicators.includes('predictive_modeling')) return '/predictive-model'
  if (context_indicators.includes('statistical_analysis')) return '/statistical-analyze'
  
  // Search (13)
  if (context_indicators.includes('information_discovery')) return '/discover-information'
  if (context_indicators.includes('result_filtering')) return '/filter-results'
  if (context_indicators.includes('content_indexing')) return '/index-content'
  if (context_indicators.includes('advanced_search')) return '/search-advanced'
  
  // Utilities (14)
  if (context_indicators.includes('agent_lifecycle')) return '/agent-lifecycle'
  if (context_indicators.includes('calculation_engine')) return '/calc-engine'
  if (context_indicators.includes('deployment_core')) return '/deploy-core'
  if (context_indicators.includes('monitoring_core')) return '/monitor-core'
  if (context_indicators.includes('phase_management')) return '/phase-manager'
  if (context_indicators.includes('task_management')) return '/todo-manager'
  if (context_indicators.includes('validation_engine')) return '/validation-engine'
  if (context_indicators.includes('validator_core')) return '/validator-core'
  
  return null
}
```

### Context Analysis Patterns

#### Context Indicator Extraction
```javascript
extract_context_indicators(workflow_results, task_history) {
  const indicators = []
  
  // Technical indicators
  if (workflow_results.includes('code') || workflow_results.includes('implementation')) {
    indicators.push('code_analysis', 'technical_validation')
  }
  
  // Complexity indicators  
  if (task_history.length > 5 || workflow_results.includes('complex')) {
    indicators.push('complexity_assessment', 'deep_thinking')
  }
  
  // Parallel processing indicators
  if (workflow_results.includes('parallel') || task_history.includes('concurrent')) {
    indicators.push('parallel_processing', 'load_balancing')
  }
  
  // Quality indicators
  if (workflow_results.includes('validation') || workflow_results.includes('testing')) {
    indicators.push('quality_gates', 'validation_required')
  }
  
  // Documentation indicators
  if (workflow_results.includes('document') || workflow_results.includes('readme')) {
    indicators.push('documentation_maintenance', 'writing_standards')
  }
  
  return indicators
}
```

#### Complexity Assessment Logic
```javascript
assess_task_complexity(task_description, resource_requirements, dependencies) {
  let complexity_score = 1
  
  // Factor in task description complexity
  if (task_description.length > 500) complexity_score += 2
  if (task_description.includes('integrate') || task_description.includes('orchestrate')) complexity_score += 3
  
  // Factor in resource requirements
  if (resource_requirements.includes('multiple_agents')) complexity_score += 3
  if (resource_requirements.includes('external_apis')) complexity_score += 2
  
  // Factor in dependencies
  complexity_score += dependencies.length * 0.5
  
  return Math.min(complexity_score, 10) // Cap at 10
}
```

## Routing Intelligence Patterns

### Standard Handoff Message Formats

#### Context Preservation Format
```
==== PHASE 5 ROUTING HANDOFF ====

**Previous Workflow Summary:**
- Phase completed: [phase_name]
- Key outcomes: [outcome_summary]
- Artifacts generated: [artifact_list]
- Context indicators: [indicator_list]

**Routing Decision:**
- Recommended command: [command_path]
- Category: [category_name] 
- Rationale: [routing_reasoning]
- Complexity level: [1-10]

**Next Phase Requirements:**
- Primary objective: [objective_description]
- Success criteria: [criteria_list]
- Resource requirements: [resource_list]
- Quality gates: [quality_requirements]

**Context Transfer:**
[Complete context dump with preserved state]

**Execution Instruction:**
Please execute [recommended_command] with the provided context to continue the workflow. The routing decision was based on [decision_factors] and complexity assessment of [complexity_score]/10.
```

#### Emergency Routing Format
```
==== CRITICAL ROUTING REQUIRED ====

**Critical Issue:** [issue_description]
**Immediate Action Required:** [action_needed]
**Recommended Command:** [emergency_command]
**Context:** [minimal_essential_context]

This is an emergency routing due to [critical_condition]. Standard workflow suspended pending resolution.
```

### Intelligent Routing Logic

#### Multi-Factor Decision Engine
```javascript
generate_routing_recommendation(context_analysis, complexity_assessment, resource_availability) {
  // Priority matrix: Foundation > Critical > Specialized
  const routing_priorities = [
    () => route_to_core(context_analysis.indicators),
    () => route_to_validation(context_analysis.indicators, context_analysis.validation_domains),
    () => route_to_execution(context_analysis.indicators, context_analysis.execution_scope),
    () => route_to_discovery_analysis(context_analysis.indicators, complexity_assessment.score),
    () => route_to_planning(context_analysis.indicators, context_analysis.project_phase),
    () => route_to_specialized(context_analysis.indicators, context_analysis.domain_type)
  ]
  
  // Execute priority routing
  for (const route_function of routing_priorities) {
    const recommendation = route_function()
    if (recommendation) {
      return {
        command: recommendation,
        confidence: calculate_confidence(context_analysis, recommendation),
        rationale: generate_rationale(context_analysis, recommendation)
      }
    }
  }
  
  // Fallback to /start for unclear routing
  return {
    command: '/start',
    confidence: 0.3,
    rationale: 'Context unclear, routing to primary entry point for re-assessment'
  }
}
```

#### Confidence Scoring
```javascript
calculate_confidence(context_analysis, recommendation) {
  let confidence = 0.5 // Base confidence
  
  // Boost confidence for clear indicators
  if (context_analysis.indicators.length > 3) confidence += 0.2
  if (context_analysis.complexity_clear) confidence += 0.2
  if (context_analysis.domain_specific) confidence += 0.3
  
  // Reduce confidence for ambiguous contexts
  if (context_analysis.mixed_signals) confidence -= 0.2
  if (context_analysis.incomplete_information) confidence -= 0.3
  
  return Math.max(0.1, Math.min(1.0, confidence))
}
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

### Phase 5 Routing Integration
```javascript
phase5_routing_integration(workflow_results, task_context, complexity_metrics) {
  return initiate_phase("Phase 5: Intelligent routing analysis",
    `Execute routing workflow:
    - Analyze workflow results: ${workflow_results.summary}
    - Extract context indicators from task history
    - Assess complexity level: ${complexity_metrics.score}/10
    - Generate routing recommendations using decision matrix
    - Format standardized handoff message with context preservation
    - Execute intelligent routing to optimal specialized command`)
}
```

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

### Context Engine Integration
```javascript
context_engine_phase(context_operation, synchronization_requirements) {
  return initiate_phase(`Context engine: ${context_operation}`,
    `Execute context management:
    - Operation type: ${context_operation}
    - Synchronization requirements: ${synchronization_requirements}
    - Prepare for Phase 5 routing with enhanced context preservation`)
}
```

### Handoff Manager Integration
```javascript
handoff_preparation_phase(target_command, context_package) {
  return initiate_phase("Handoff preparation for routing",
    `Prepare seamless transition:
    - Target command: ${target_command}
    - Context package: ${context_package.size} elements
    - Format Phase 5 routing handoff message
    - Validate context completeness before transfer`)
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

### Phase 5 Routing Workflow
```
// Context analysis and routing decision
${phase5_routing_integration(
  { summary: "Complex codebase analysis completed with parallel processing requirements identified" },
  { task_history: ["discovery", "analysis", "complexity_assessment"], indicators: ["parallel_processing", "load_balancing"] },
  { score: 8, factors: ["multiple_dependencies", "concurrent_operations"] }
)}

// Generate routing recommendation
Context analysis complete. Routing decision:
- Recommended command: /agent-orchestration
- Category: 04-execution
- Rationale: High complexity (8/10) with parallel processing requirements
- Confidence: 0.85

==== PHASE 5 ROUTING HANDOFF ====

**Previous Workflow Summary:**
- Phase completed: Complex codebase analysis
- Key outcomes: Identified 12 parallel processing opportunities
- Artifacts generated: Analysis report, dependency map, performance metrics
- Context indicators: parallel_processing, load_balancing, advanced_orchestration

**Routing Decision:**
- Recommended command: /agent-orchestration
- Category: 04-execution
- Rationale: High complexity parallel workload requiring advanced coordination
- Complexity level: 8

**Next Phase Requirements:**
- Primary objective: Execute parallel processing implementation
- Success criteria: 12 concurrent operations, <2s latency, 95% success rate
- Resource requirements: 4-6 parallel agents, load balancing, monitoring
- Quality gates: Performance validation, error handling, result consolidation

**Context Transfer:**
[Complete analysis context with dependency mappings, performance requirements, and orchestration parameters]

**Execution Instruction:**
Please execute /agent-orchestration with the provided context to continue the workflow. The routing decision was based on complexity assessment and parallel processing requirements with confidence score of 0.85.
```

### Emergency Routing Example
```
// Critical issue detected during validation
${handle_phase_error("validation", "critical performance degradation in parallel operations")}

// Emergency routing protocol
==== CRITICAL ROUTING REQUIRED ====

**Critical Issue:** Performance degradation causing system instability
**Immediate Action Required:** Load balancing reconfiguration and performance optimization
**Recommended Command:** /load-balance
**Context:** Parallel operations experiencing 400% latency increase, 15% failure rate

This is an emergency routing due to critical performance degradation. Standard workflow suspended pending resolution.
```

### Cross-Category Integration Example
```
// Foundation layer integration
${initiate_phase("Enhanced discovery with context management", "Execute /enhanced-start with /context-engine integration")}

// Discovery phase completion leading to routing
${transition_phase("discovery", "Phase 5 routing analysis", "Analyze discovery results for specialized command routing")}

// Generated routing: Discovery → Analysis → Execution → Validation
Context analysis indicates: codebase_analysis + complexity_assessment + parallel_processing
Routing sequence:
1. /explore-codebase (01-discovery) ✓ Complete
2. /complexity-assess (03-analysis) → Route based on complexity score
3. /agent-orchestration (04-execution) → If complexity > 7
4. /validate-complete (05-validation) → Final quality assurance

// Context preservation across routing chain
Each handoff maintains complete context with progressive enhancement
```

---

**Single Responsibility**: Universal phase management engine providing standardized TodoWrite orchestration patterns with Phase 5 intelligent routing capabilities, eliminating duplicate phase management logic across all commands while ensuring consistent workflow execution, context preservation, and intelligent command routing across the 15-category system architecture.