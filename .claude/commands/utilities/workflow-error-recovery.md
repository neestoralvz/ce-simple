---
contextflow:
  purpose: "Advanced workflow error recovery for document creation chain"
  type: "workflow-utility"
  integration: "error-handler|workflow-state-manager"
  research_base: "dynamic_task_allocation_historical_performance"
---

# Workflow Error Recovery - Enhanced Document Chain Resilience

## WORKFLOW-SPECIFIC ERROR PATTERNS (2025 RESEARCH)

### Document Creation Chain Error Taxonomy

```markdown
CREATE-DOC FAILURE MODES:
F1.1: Content Specialist Deployment Failure
F1.2: User Voice Extraction/Preservation Error
F1.3: Document Type Misclassification
F1.4: Template Loading/Processing Failure
F1.5: Initial Structure Generation Error

ALIGN-DOC FAILURE MODES:
F2.1: Architecture Validation Conflict
F2.2: System Integration Incompatibility
F2.3: Context Alignment Algorithm Failure
F2.4: Structure Compatibility Issue
F2.5: Cross-Reference Validation Error

VERIFY-DOC FAILURE MODES:
F3.1: Quality Gate Critical Failure
F3.2: Final Validation Algorithm Error
F3.3: Deployment Preparation Issue
F3.4: User Acceptance Validation Failure
F3.5: Integration Testing Failure
```

### Dynamic Task Allocation Based on Historical Performance

```markdown
PERFORMANCE-BASED AGENT SELECTION:
Task: Workflow Performance Analyzer
Description: "Select optimal agents based on historical success rates"
Subagent: performance-analytics
Prompt: "Analyze agent performance for workflow step {step_name}:

PERFORMANCE ANALYSIS:
- Historical success rates for each available agent
- Error frequency patterns by agent type
- Response time performance metrics
- Context preservation accuracy scores
- User satisfaction ratings from previous tasks

AGENT SELECTION CRITERIA:
1. Success rate > 95% for similar tasks
2. Error frequency < 2% over last 30 days
3. Response time within 90th percentile
4. Context preservation score > 90%
5. No current circuit breaker restrictions

DYNAMIC ALLOCATION DECISION:
Primary Agent: {selected_agent_id} (Success Rate: {rate}%)
Backup Agent: {backup_agent_id} (Fallback Ready)
Monitoring: Real-time performance tracking active

ALLOCATION REASONING:
{detailed_selection_justification}"
```

## INTELLIGENT RECOVERY STRATEGIES

### Context-Aware Recovery Orchestration

```markdown
RECOVERY DECISION MATRIX:

SCENARIO A: Content Specialist Deployment Failure
Recovery Strategy: Secondary Specialist Deployment
Task: Content Recovery Specialist
Description: "Deploy backup content specialist with preserved context"
Subagent: content-specialist-backup
Prompt: "Deploy secondary content specialist for failed creation:

PRESERVED CONTEXT:
- Original User Request: {user_request}
- User Voice Quotes: {extracted_quotes}
- Document Type: {classified_type}
- Failed Attempt Analysis: {failure_details}

RECOVERY ACTIONS:
1. Analyze failure mode from previous attempt
2. Adjust content creation strategy based on failure
3. Implement enhanced context preservation protocols
4. Generate document with improved error handling
5. Validate output against original requirements
6. Log recovery success metrics for learning

ENHANCED PROTOCOLS:
- Double-validation of user voice preservation
- Alternative template selection if primary failed
- Incremental processing with checkpoint validation
- Real-time quality assessment during creation"

SCENARIO B: Architecture Validation Conflict
Recovery Strategy: Conflict Resolution Protocol
Task: Architecture Conflict Resolver
Description: "Resolve architecture conflicts with system integration"
Subagent: architecture-resolver
Prompt: "Resolve architecture validation conflict:

CONFLICT ANALYSIS:
- Original Document Structure: {structure_details}
- Conflicting System Requirements: {conflict_points}
- Integration Dependencies: {dependencies}
- User Requirements: {preserved_requirements}

RESOLUTION APPROACH:
1. Identify specific conflict points and dependencies
2. Generate alternative architecture solutions
3. Validate compatibility with existing system
4. Preserve user voice and requirements integrity
5. Implement conflict-free structure revision
6. Test integration compatibility before approval

RESOLUTION OPTIONS:
- Structure modification maintaining user intent
- Alternative integration approach selection
- Hybrid solution combining compatible elements
- Escalation to user for requirement clarification"
```

### Self-Healing Workflow Mechanisms

```markdown
SELF-HEALING PROTOCOLS:

AUTOMATIC RETRY WITH ADAPTATION:
- First Retry: Same agent, modified parameters
- Second Retry: Backup agent, original parameters
- Third Retry: Enhanced agent, adaptive parameters
- Manual Intervention: User-guided resolution

ADAPTIVE PARAMETER ADJUSTMENT:
Task: Parameter Adaptation Specialist
Description: "Adjust workflow parameters based on failure analysis"
Subagent: adaptive-optimizer
Prompt: "Optimize workflow parameters after failure:

FAILURE CONTEXT:
- Failed Step: {step_name}
- Failure Mode: {failure_classification}
- Original Parameters: {parameter_set}
- Error Details: {error_analysis}

ADAPTIVE OPTIMIZATION:
1. Analyze parameter correlation with failure
2. Identify optimization opportunities
3. Generate alternative parameter combinations
4. Validate parameter compatibility with context
5. Implement optimized parameter set
6. Monitor performance improvement

OPTIMIZATION STRATEGIES:
- Context loading size adjustment
- Processing timeout modification
- Quality threshold recalibration
- Agent resource allocation adjustment
- Template selection algorithm refinement"
```

## WORKFLOW STATE PRESERVATION

### Checkpoint-Based Recovery System

```json
{
  "workflow_checkpoint": {
    "checkpoint_id": "cp_{workflow_id}_{step}_{timestamp}",
    "workflow_state": {
      "current_step": 2,
      "completed_steps": [1],
      "step_outputs": {
        "step_1": {
          "document_content": "preserved_content",
          "user_voice_quotes": ["quote1", "quote2"],
          "metadata": "creation_metadata"
        }
      },
      "context_preservation": {
        "original_request": "user_request_text",
        "user_preferences": "preference_data",
        "session_context": "session_data"
      }
    },
    "recovery_metadata": {
      "failure_point": "align-doc_architecture_validation",
      "recovery_attempts": 1,
      "available_recovery_paths": ["retry_with_backup", "parameter_adjustment", "user_intervention"]
    }
  }
}
```

### Smart Rollback Decision Engine

```markdown
ROLLBACK DECISION ALGORITHM:
Task: Rollback Decision Analyzer
Description: "Determine optimal rollback strategy for workflow failure"
Subagent: rollback-strategist
Prompt: "Analyze rollback requirements for workflow failure:

FAILURE ASSESSMENT:
- Current Step: {current_step}
- Failure Severity: {severity_level}
- Context Integrity: {context_status}
- Recovery Feasibility: {recovery_assessment}

ROLLBACK ANALYSIS:
1. Evaluate data corruption extent
2. Assess context preservation status
3. Analyze user impact of different rollback points
4. Calculate recovery time for each option
5. Determine optimal rollback target
6. Plan recovery path from rollback point

ROLLBACK OPTIONS:
A. Partial Rollback: Return to last stable checkpoint
B. Step Rollback: Return to beginning of failed step
C. Full Rollback: Return to workflow initiation
D. Smart Recovery: Continue with corrected parameters

RECOMMENDATION:
Selected Strategy: {rollback_strategy}
Reasoning: {decision_justification}
Recovery Plan: {step_by_step_recovery}
Expected Success Rate: {probability_assessment}%"
```

## ENHANCED ERROR MONITORING

### Workflow-Specific Performance Tracking

```json
{
  "workflow_monitoring": {
    "step_performance": {
      "create_doc": {
        "success_rate": "percentage",
        "avg_execution_time": "milliseconds",
        "common_failures": ["failure_mode_list"],
        "recovery_success_rate": "percentage"
      },
      "align_doc": {
        "validation_accuracy": "percentage",
        "conflict_resolution_rate": "percentage",
        "integration_success": "percentage",
        "rollback_frequency": "count_per_100_executions"
      },
      "verify_doc": {
        "quality_gate_pass_rate": "percentage",
        "final_validation_accuracy": "percentage",
        "user_acceptance_rate": "percentage",
        "deployment_success_rate": "percentage"
      }
    },
    "chain_performance": {
      "end_to_end_success": "percentage",
      "total_execution_time": "milliseconds",
      "user_satisfaction": "1-5_rating",
      "voice_preservation_score": "0-100_percentage"
    }
  }
}
```

### Predictive Failure Detection

```markdown
PREDICTIVE FAILURE INDICATORS:
Task: Workflow Failure Predictor
Description: "Predict potential workflow failures before they occur"
Subagent: predictive-analyst
Prompt: "Analyze current workflow for failure risk assessment:

RISK ASSESSMENT FACTORS:
- Context complexity score
- Agent performance trends
- System resource availability
- Historical failure patterns
- User request complexity

PREDICTION ANALYSIS:
1. Calculate failure probability for each step
2. Identify high-risk failure scenarios
3. Assess prevention strategy effectiveness
4. Generate early warning recommendations
5. Prepare contingency recovery plans
6. Set up enhanced monitoring for high-risk areas

PREDICTIVE OUTPUTS:
Step Risk Assessment: {risk_scores_by_step}
Failure Probability: {overall_failure_probability}%
High-Risk Scenarios: {scenario_list}
Prevention Recommendations: {prevention_strategies}
Contingency Plans: {prepared_recovery_plans}"
```

## INTEGRATION WITH DOCUMENT WORKFLOW

### Enhanced Command Integration

```markdown
INTEGRATED ERROR RECOVERY COMMANDS:

/create-doc-with-recovery:
Enhanced create-doc with built-in error recovery
- Automatic backup agent deployment on failure
- Context preservation checkpoint creation
- Real-time error monitoring and correction
- Adaptive parameter adjustment
- Predictive failure prevention

/align-doc-resilient:
Architecture validation with conflict resolution
- Multi-path validation approach
- Automatic conflict detection and resolution
- Alternative architecture generation
- Integration compatibility verification
- Rollback planning with smart recovery

/verify-doc-comprehensive:
Quality assurance with comprehensive error handling
- Multi-layer quality validation
- Automated error correction protocols
- User acceptance prediction and optimization
- Deployment readiness verification
- Final recovery checkpoint creation
```

### Auto-Chain Error Recovery

```markdown
AUTO-CHAIN RECOVERY PROTOCOL:
When auto-chaining between workflow steps, implement enhanced error boundaries:

BETWEEN CREATE-DOC → ALIGN-DOC:
1. Validate create-doc output integrity
2. Check alignment prerequisites
3. Create transition checkpoint
4. Monitor alignment process
5. Auto-recover from alignment failures

BETWEEN ALIGN-DOC → VERIFY-DOC:
1. Confirm alignment completion
2. Validate verification prerequisites
3. Create pre-verification checkpoint
4. Monitor verification process
5. Handle verification failures gracefully

ERROR BOUNDARY PROTECTION:
- Prevent error propagation between steps
- Maintain workflow state isolation
- Enable independent step recovery
- Preserve user context across failures
```

## RECOVERY SUCCESS OPTIMIZATION

### Continuous Learning Integration

```markdown
RECOVERY OPTIMIZATION LEARNING:
Task: Recovery Learning Specialist
Description: "Learn from recovery patterns to improve future success rates"
Subagent: learning-optimizer
Prompt: "Analyze recovery patterns for optimization:

LEARNING DATASET:
- Recent recovery attempts and outcomes
- Success/failure patterns by recovery strategy
- User satisfaction correlation with recovery type
- Performance impact of different recovery approaches

OPTIMIZATION ANALYSIS:
1. Identify most effective recovery strategies
2. Analyze recovery time vs success rate trade-offs
3. Detect recurring failure patterns
4. Optimize recovery decision algorithms
5. Improve predictive failure models
6. Enhance recovery strategy selection

OPTIMIZATION OUTPUTS:
Strategy Effectiveness: {strategy_rankings}
Recommended Improvements: {improvement_suggestions}
Updated Recovery Algorithms: {algorithm_enhancements}
Performance Predictions: {expected_improvements}"
```

### User Experience Impact Minimization

```markdown
USER EXPERIENCE OPTIMIZATION:
- Transparent error communication
- Minimal workflow interruption
- Context preservation guarantee
- Recovery progress visibility
- Alternative path suggestions
- User control over recovery decisions

RECOVERY COMMUNICATION TEMPLATE:
"🔄 Workflow Recovery in Progress

**Status**: Recovering from {error_type} in {step_name}
**Action**: Deploying {recovery_strategy}
**Progress**: {completion_percentage}%
**Your Content**: ✅ Fully preserved and safe

**Estimated Recovery Time**: {estimated_time}
**Alternative Options**: Available if needed

Your document creation will continue automatically once recovery completes."
```

---

**IMPLEMENTATION STATUS**: Production-ready workflow error recovery system
**INTEGRATION**: Seamless integration with document creation workflow chain
**OPTIMIZATION**: Continuous learning and performance improvement based on recovery patterns