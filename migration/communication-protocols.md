# VDD Sub-Agent Communication Protocols

**Updated**: 2025-07-26 | **Purpose**: Comprehensive inter-agent communication specifications | **Authority**: Communication architecture design

## Communication Architecture Overview

VDD framework implements structured communication protocols enabling efficient coordination between 4 specialized sub-agent types through standardized message formats, coordination patterns, and error handling mechanisms.

## Communication Model

### Architecture Pattern
**Model**: Hub-and-Spoke with Publish-Subscribe capabilities  
**Central Hub**: Planning Agent serves as primary coordination hub  
**Communication Flow**: Bidirectional with structured message passing  
**Message Security**: Validated formats with authentication and error handling  
**Scalability**: Designed for high-frequency coordination with minimal overhead

### Message Types
- **Task Assignment**: Planning Agent → Specialized Agents
- **Status Update**: All Agents → Planning Agent  
- **Result Publication**: Completing Agent → All Interested Agents
- **Error Notification**: Any Agent → Planning Agent + Affected Agents
- **Resource Request**: Any Agent → Planning Agent
- **Quality Gate**: Validation Agent → All Agents
- **Knowledge Share**: Discovery Agent → Knowledge Base → All Agents

---

## Message Interface Specifications

### Task Assignment Protocol

**Purpose**: Planning Agent distributes specialized tasks to appropriate agents  
**Direction**: Planning Agent → Target Agent  
**Frequency**: Per task initiation  
**Priority**: High (system coordination critical)

```json
{
  "protocol_version": "2.0",
  "message_type": "task_assignment",
  "message_id": "unique_uuid_v4",
  "timestamp": "2025-07-26T12:00:00Z",
  "from_agent": {
    "agent_type": "planning_agent",
    "agent_instance_id": "planning_001",
    "session_id": "session_uuid"
  },
  "to_agent": {
    "agent_type": "discovery_agent|execution_agent|validation_agent",
    "agent_instance_id": "target_agent_id",
    "specialization_required": "specific_capability_needed"
  },
  "task_specification": {
    "task_id": "unique_task_identifier",
    "task_type": "exploration|implementation|validation|coordination",
    "priority": "critical|high|medium|low",
    "deadline": "2025-07-26T15:00:00Z",
    "estimated_duration": "duration_in_minutes",
    "complexity_level": "simple|moderate|complex|expert"
  },
  "context": {
    "project_state": "current_vdd_project_context",
    "dependencies": [
      {
        "dependency_id": "prerequisite_task_id",
        "dependency_type": "blocking|informational|resource",
        "status": "pending|in_progress|completed"
      }
    ],
    "resources": {
      "token_allocation": "allocated_token_count",
      "tool_permissions": ["Read", "Write", "Edit", "Bash"],
      "file_access_scope": "directory_or_file_patterns",
      "external_access": "web_search|none"
    },
    "constraints": {
      "time_limit": "maximum_execution_time",
      "quality_requirements": "pts_compliance_level",
      "coordination_requirements": "agent_coordination_needs"
    }
  },
  "task_details": {
    "objective": "specific_measurable_task_objective",
    "deliverables": [
      {
        "deliverable_type": "file|analysis|report|implementation",
        "specification": "detailed_deliverable_requirements",
        "quality_criteria": "validation_requirements"
      }
    ],
    "success_criteria": [
      "measurable_success_metric_1",
      "measurable_success_metric_2"
    ],
    "validation_requirements": {
      "self_validation": "agent_self_check_requirements",
      "peer_validation": "validation_agent_requirements",
      "quality_gates": "pts_compliance_checks"
    }
  },
  "coordination": {
    "communication_frequency": "milestone|continuous|completion",
    "progress_reporting": "detailed|summary|minimal",
    "collaboration_agents": ["list_of_collaborating_agents"],
    "escalation_path": "conflict_resolution_procedure"
  }
}
```

### Status Update Protocol

**Purpose**: Continuous progress tracking and coordination  
**Direction**: Any Agent → Planning Agent  
**Frequency**: Periodic during task execution  
**Priority**: Medium (coordination optimization)

```json
{
  "protocol_version": "2.0",
  "message_type": "status_update",
  "message_id": "unique_uuid_v4",
  "timestamp": "2025-07-26T12:30:00Z",
  "from_agent": {
    "agent_type": "discovery_agent|execution_agent|validation_agent",
    "agent_instance_id": "reporting_agent_id",
    "session_id": "session_uuid"
  },
  "to_coordinator": {
    "agent_type": "planning_agent",
    "coordination_session": "coordination_session_id"
  },
  "task_reference": {
    "task_id": "assigned_task_identifier",
    "task_type": "exploration|implementation|validation",
    "original_assignment": "task_assignment_message_id"
  },
  "status": {
    "execution_status": "not_started|initializing|in_progress|completing|completed|failed|blocked|paused",
    "progress_percentage": 0-100,
    "estimated_completion": "2025-07-26T14:30:00Z",
    "confidence_level": 0.0-1.0,
    "quality_score": 0.0-1.0
  },
  "current_activity": {
    "activity_description": "specific_current_work_description",
    "tools_in_use": ["currently_active_tools"],
    "current_focus": "specific_task_component_being_worked",
    "next_planned_action": "immediate_next_step"
  },
  "resource_utilization": {
    "tokens_consumed": "current_token_usage",
    "tokens_remaining": "remaining_token_allocation",
    "tools_active": ["list_of_active_tools"],
    "memory_usage": "current_memory_consumption",
    "performance_metrics": {
      "execution_speed": "operations_per_minute",
      "error_rate": "percentage_of_failed_operations",
      "efficiency_score": 0.0-1.0
    }
  },
  "issues_and_blockers": [
    {
      "issue_type": "blocker|warning|information",
      "severity": "critical|high|medium|low",
      "description": "specific_issue_description",
      "impact": "impact_on_task_completion",
      "suggested_resolution": "proposed_solution",
      "escalation_needed": "true|false"
    }
  ],
  "intermediate_results": [
    {
      "result_type": "discovery|partial_implementation|validation_finding",
      "description": "intermediate_result_description",
      "confidence": 0.0-1.0,
      "actionable": "true|false"
    }
  ],
  "coordination_requests": [
    {
      "request_type": "resource|assistance|clarification|escalation",
      "urgency": "immediate|high|medium|low",
      "description": "specific_request_details",
      "preferred_resolution": "suggested_approach"
    }
  ]
}
```

### Result Publication Protocol

**Purpose**: Share completed work and discoveries across agent network  
**Direction**: Completing Agent → Planning Agent + Interested Agents  
**Frequency**: Upon task completion or major milestone  
**Priority**: High (system knowledge integration)

```json
{
  "protocol_version": "2.0",
  "message_type": "result_publication",
  "message_id": "unique_uuid_v4",
  "timestamp": "2025-07-26T14:00:00Z",
  "from_agent": {
    "agent_type": "discovery_agent|execution_agent|validation_agent",
    "agent_instance_id": "completing_agent_id",
    "session_id": "session_uuid"
  },
  "task_reference": {
    "task_id": "completed_task_identifier",
    "original_assignment": "task_assignment_message_id",
    "execution_duration": "actual_execution_time_minutes"
  },
  "completion_status": {
    "status": "full_success|partial_success|completed_with_issues|failed",
    "success_percentage": 0-100,
    "quality_score": 0.0-1.0,
    "confidence_level": 0.0-1.0
  },
  "primary_deliverables": [
    {
      "deliverable_id": "unique_deliverable_id",
      "deliverable_type": "file|analysis|report|implementation|discovery",
      "location": "file_path_or_reference",
      "description": "deliverable_description",
      "quality_metrics": {
        "pts_compliance": "12/12_or_score",
        "validation_status": "validated|pending|failed",
        "performance_impact": "positive|neutral|negative"
      }
    }
  ],
  "secondary_outputs": [
    {
      "output_type": "insight|pattern|recommendation|warning",
      "description": "secondary_output_description",
      "relevance": "high|medium|low",
      "actionable": "true|false"
    }
  ],
  "artifacts_created": [
    {
      "artifact_type": "file|data_structure|configuration|documentation",
      "location": "artifact_location_reference",
      "purpose": "artifact_purpose_description",
      "maintenance_requirements": "ongoing_maintenance_needs"
    }
  ],
  "knowledge_gained": [
    {
      "knowledge_type": "pattern|insight|best_practice|anti_pattern|optimization",
      "description": "knowledge_description",
      "applicability": "project_specific|domain_general|system_wide",
      "confidence": 0.0-1.0,
      "supporting_evidence": "evidence_references"
    }
  ],
  "quality_assessment": {
    "self_validation": {
      "passed": "true|false",
      "validation_details": "self_validation_results",
      "identified_issues": ["list_of_self_identified_issues"]
    },
    "validation_required": {
      "validation_agent_review": "required|optional|not_needed",
      "peer_review": "required|optional|not_needed",
      "user_review": "required|optional|not_needed"
    },
    "performance_metrics": {
      "execution_efficiency": 0.0-1.0,
      "resource_utilization": 0.0-1.0,
      "output_quality": 0.0-1.0,
      "coordination_effectiveness": 0.0-1.0
    }
  },
  "follow_up_recommendations": [
    {
      "recommendation_type": "immediate_action|future_task|optimization|investigation",
      "priority": "critical|high|medium|low",
      "description": "recommendation_description",
      "estimated_effort": "effort_estimation",
      "suggested_agent": "optimal_agent_for_task"
    }
  ],
  "lessons_learned": [
    {
      "lesson_type": "process_improvement|technical_insight|coordination_optimization",
      "description": "lesson_description",
      "impact": "system_wide|domain_specific|agent_specific",
      "implementation_suggestion": "how_to_apply_lesson"
    }
  ]
}
```

### Error Notification Protocol

**Purpose**: Immediate notification of errors and system issues  
**Direction**: Any Agent → Planning Agent + Affected Agents  
**Frequency**: Immediate upon error detection  
**Priority**: Critical (system stability)

```json
{
  "protocol_version": "2.0",
  "message_type": "error_notification",
  "message_id": "unique_uuid_v4",
  "timestamp": "2025-07-26T12:45:00Z",
  "from_agent": {
    "agent_type": "any_agent_type",
    "agent_instance_id": "error_reporting_agent_id",
    "session_id": "session_uuid"
  },
  "error_details": {
    "error_id": "unique_error_identifier",
    "error_type": "system|coordination|task_execution|validation|communication",
    "severity": "critical|high|medium|low|informational",
    "error_category": "recoverable|escalatable|critical|informational",
    "error_description": "detailed_error_description",
    "error_context": "circumstances_and_context_of_error"
  },
  "task_impact": {
    "affected_task_id": "task_identifier_if_applicable",
    "impact_severity": "blocking|degrading|warning|informational",
    "estimated_delay": "estimated_delay_in_minutes",
    "cascade_risk": "high|medium|low|none"
  },
  "system_impact": {
    "affected_agents": ["list_of_affected_agent_types"],
    "affected_operations": ["list_of_affected_operations"],
    "system_stability": "stable|degraded|unstable|critical",
    "data_integrity": "intact|questionable|compromised|unknown"
  },
  "error_analysis": {
    "root_cause": "identified_root_cause_if_known",
    "contributing_factors": ["list_of_contributing_factors"],
    "error_pattern": "new|recurring|known_issue|system_pattern",
    "reproduction_steps": "steps_to_reproduce_error_if_applicable"
  },
  "recovery_status": {
    "recovery_attempted": "true|false",
    "recovery_success": "successful|partial|failed|not_attempted",
    "recovery_actions": ["list_of_recovery_actions_taken"],
    "current_status": "recovered|recovering|degraded|failed"
  },
  "escalation_requirements": {
    "immediate_escalation": "true|false",
    "escalation_target": "planning_agent|user|system_admin|none",
    "escalation_reason": "escalation_justification",
    "recommended_actions": ["list_of_recommended_actions"]
  },
  "prevention_analysis": {
    "preventable": "true|false|unknown",
    "prevention_measures": ["suggested_prevention_measures"],
    "system_improvements": ["suggested_system_improvements"],
    "monitoring_enhancements": ["suggested_monitoring_improvements"]
  }
}
```

---

## Coordination Protocols

### Task Distribution Algorithm

**Phase 1: Request Analysis**
1. Planning Agent receives user request or system trigger
2. Decompose request into specialized sub-tasks using domain expertise mapping
3. Identify task dependencies and execution order requirements
4. Assess resource requirements and agent availability

**Phase 2: Agent Selection**
1. Match sub-tasks to appropriate agent specializations based on capability matrix
2. Consider agent availability, current workload, and performance history
3. Optimize for parallel execution while respecting dependencies
4. Reserve resources and schedule execution timeline

**Phase 3: Task Assignment**
1. Generate detailed task assignments with complete context and specifications
2. Distribute tasks using Task Assignment Protocol with coordination requirements
3. Establish monitoring schedule and progress reporting expectations
4. Activate task execution monitoring and coordination oversight

**Phase 4: Execution Coordination**
1. Monitor task progress through Status Update Protocol
2. Coordinate dependencies and resource allocation dynamically
3. Handle escalations and coordination conflicts through resolution protocols
4. Manage task completion and result integration

**Phase 5: Result Integration**
1. Collect results through Result Publication Protocol
2. Validate completion against original request requirements
3. Integrate results and coordinate final delivery
4. Capture lessons learned and system improvement opportunities

### Conflict Resolution Protocols

**Resource Conflicts**
- **Detection**: Automatic detection of resource allocation conflicts
- **Mediation**: Planning Agent mediates resource disputes with optimization algorithms
- **Resolution**: Dynamic resource reallocation based on priority and efficiency
- **Prevention**: Proactive resource planning and reservation system

**Priority Conflicts**
- **Hierarchy**: User requests > Critical system issues > High priority > Medium/Low priority
- **Escalation**: Unresolvable priority conflicts escalate to user consultation
- **Coordination**: Planning Agent coordinates priority resolution with affected agents
- **Documentation**: All priority decisions documented for future reference

**Quality Conflicts**
- **Authority**: Validation Agent has final authority on quality and compliance issues
- **Standards**: PTS framework compliance is non-negotiable requirement
- **Resolution**: Quality issues block completion until resolution
- **Improvement**: Quality conflicts trigger system improvement analysis

**Technical Conflicts**
- **Expertise**: Agent with relevant domain expertise provides technical resolution
- **Collaboration**: Multiple agents collaborate on complex technical issues
- **Escalation**: Unresolvable technical conflicts escalate to user consultation
- **Learning**: Technical resolutions feed into system knowledge base

### Error Handling Protocols

**Error Detection**
- **Self-Monitoring**: Each agent continuously monitors its own operations
- **Peer Monitoring**: Agents monitor peer agent status and coordination health
- **System Monitoring**: Planning Agent monitors overall system health and coordination
- **Proactive Detection**: Pattern analysis for early error detection and prevention

**Error Classification**
- **Recoverable**: Errors that can be resolved through automatic recovery procedures
- **Escalatable**: Errors requiring Planning Agent intervention and coordination
- **Critical**: Errors threatening system stability requiring immediate attention
- **Informational**: Non-blocking issues for awareness and improvement opportunities

**Recovery Procedures**
- **Automatic Recovery**: Immediate automatic recovery for known recoverable errors
- **Coordinated Recovery**: Planning Agent coordinates recovery for complex errors
- **Fallback Procedures**: Graceful degradation to ensure continued operation
- **System Restart**: Last resort system restart for critical unrecoverable errors

**Learning Integration**
- **Error Analysis**: Comprehensive analysis of all errors for pattern identification
- **Prevention Enhancement**: System improvements based on error analysis
- **Recovery Optimization**: Continuous improvement of recovery procedures
- **Knowledge Integration**: Error patterns integrated into system knowledge base

---

## Performance Optimization

### Communication Efficiency
- **Message Batching**: Multiple related messages batched for efficient transmission
- **Compression**: Large message content compressed for bandwidth optimization
- **Prioritization**: Message priority queue ensuring critical communications are processed first
- **Caching**: Frequently accessed information cached for rapid retrieval

### Coordination Optimization
- **Parallel Coordination**: Multiple coordination threads for simultaneous task management
- **Dependency Optimization**: Intelligent dependency resolution for maximum parallelism
- **Resource Pooling**: Shared resource pools for efficient utilization across agents
- **Load Balancing**: Dynamic load balancing based on agent capacity and specialization

### Scalability Features
- **Agent Scaling**: Dynamic agent instance creation based on workload requirements
- **Communication Scaling**: Communication infrastructure scales with agent count
- **Resource Scaling**: Automatic resource allocation scaling for system demands
- **Performance Monitoring**: Continuous performance monitoring with automatic optimization

---

**Communication Protocol Principle**: Structured, efficient, and reliable communication enables optimal coordination between specialized agents while maintaining system stability and performance.**