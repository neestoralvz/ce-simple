---
contextflow:
  purpose: "Workflow completion and deployment for document verification"
  parent-command: "verify-doc"
  auxiliary: true
  input-format: "voice-results"
  output-format: "completion-results"
  research-driven: false
---

# Auxiliary Command `/verify-doc-completion`

## Purpose
Execute workflow completion, deployment logic, and rollback handling for document verification workflow.

## Completion Logic Framework

### Workflow State Management
```python
def execute_workflow_completion(voice_results):
    if voice_results.quality_score >= 85 and voice_results.voice_score >= 54:
        return execute_success_completion(voice_results)
    elif voice_results.minor_issues_only and voice_results.voice_score >= 54:
        return execute_auto_fix_completion(voice_results)
    else:
        return execute_rollback_protocol(voice_results)
```

### Success Completion Path
```python
def execute_success_completion(voice_results):
    return {
        'workflow_status': 'completed',
        'deployment_executed': deploy_document_to_production(voice_results.document),
        'handoff_updated': update_handoff_with_new_document(voice_results),
        'user_notification': generate_success_summary(voice_results),
        'cleanup_scheduled': schedule_workflow_cleanup(voice_results.workflow_id)
    }
```

### Task Tools Deployment

#### Success Completion Task
```python
Task(
    description="Deploy document and finalize successful workflow completion",
    prompt="""Actúa como Workflow Completion Specialist. COMPLETION MISSION: Deploy and finalize workflow.

COMPLETION CONTEXT:
- workflow_id: {voice_results.workflow_id}
- final_document: {voice_results.document_path}
- quality_score: {voice_results.quality_score} (threshold: 85+)
- voice_preservation_score: {voice_results.voice_score} (threshold: 54+)
- validation_results: {voice_results.validation_summary}

COMPLETION ACTIONS:
1. Deploy document to target location
2. Update handoff with new document availability
3. Log workflow success metrics
4. Generate comprehensive completion summary
5. Schedule workflow state cleanup (24h)
6. Update system documentation index

USER NOTIFICATION REQUIREMENTS:
- Document deployed location and access instructions
- Quality metrics achieved (both quality and voice scores)
- Voice preservation verification confirmation
- Next steps recommendations for user
- System integration status

EXECUTE: Complete workflow deployment with comprehensive user notification.""",
    subagent_type="general-purpose"
)
```

#### Auto-Fix Minor Issues Task
```python
Task(
    description="Auto-fix minor issues and complete workflow deployment",
    prompt="""Actúa como Auto-Fix Specialist. AUTO-FIX MISSION: Resolve minor issues and deploy.

MINOR ISSUES CONTEXT:
- minor_issues: {voice_results.minor_issues}
- voice_score: {voice_results.voice_score} (≥54 maintained)
- quality_score: {voice_results.quality_score}
- auto_fix_capability: {voice_results.fixable_issues}

AUTO-FIX REQUIREMENTS:
- Maintain voice preservation score ≥54/60 (MANDATORY)
- Preserve all user voice integrity during fixes
- Keep quality score ≥85/100 
- Log all fixes for complete traceability

POST-FIX DEPLOYMENT:
1. Apply fixes while preserving voice integrity
2. Validate fixes don't impact voice preservation
3. Deploy corrected document to production
4. Generate fix log for user transparency
5. Complete workflow with comprehensive summary

EXECUTE: Auto-fix issues and deploy with complete fix documentation.""",
    subagent_type="general-purpose"
)
```

#### Rollback Protocol Task
```python
Task(
    description="Execute workflow rollback to appropriate previous step",
    prompt="""Actúa como Rollback Coordinator. ROLLBACK MISSION: Return workflow to previous step.

ROLLBACK CONTEXT:
- workflow_id: {voice_results.workflow_id}
- major_issues: {voice_results.major_issues}
- rollback_target: {determine_rollback_target(voice_results.issues)}
- preserved_context: {voice_results.workflow_history}
- quality_failures: {voice_results.quality_failures}
- voice_failures: {voice_results.voice_failures}

ROLLBACK EXECUTION:
1. Preserve all user context and previous work
2. Reset workflow state to appropriate target step
3. Prepare detailed issue summary for user
4. Maintain voice preservation throughout rollback
5. Clear error conditions for fresh step execution

USER COMMUNICATION REQUIREMENTS:
- Clear explanation of why rollback was necessary
- What user work will be preserved during rollback
- Specific corrections needed before proceeding
- Step-by-step guidance for resolution
- Timeline expectations for resolution

EXECUTE: Rollback to appropriate step with complete context preservation.""",
    subagent_type="general-purpose"
)
```

## Rollback Target Determination

### Rollback Logic
```python
def determine_rollback_target(issues_summary):
    if issues_summary.voice_preservation_failures:
        if issues_summary.source_attribution_errors:
            return "create-doc"  # Fundamental voice issues
        else:
            return "align-doc"   # Voice separation issues
    elif issues_summary.quality_failures:
        if issues_summary.structural_issues:
            return "align-doc"   # Architecture problems
        else:
            return "verify-doc"  # Minor quality issues
    else:
        return "verify-doc"      # Default minor issues
```

## Completion Validation

### Success Criteria Validation
```python
completion_validation = {
    'quality_threshold': quality_score >= 85,
    'voice_threshold': voice_score >= 54,
    'no_major_issues': len(major_issues) == 0,
    'deployment_ready': all_validations_passed,
    'user_notification_ready': summary_generated,
    'workflow_state_clean': cleanup_scheduled
}
```

## Output Structure
```json
{
  "workflow_completion_status": "SUCCESS|AUTO_FIXED|ROLLBACK",
  "completion_details": {
    "final_quality_score": 87,
    "final_voice_score": 56,
    "deployment_location": "...",
    "completion_timestamp": "...",
    "workflow_duration": "..."
  },
  "user_notification": {
    "success_summary": "...",
    "document_location": "...",
    "next_steps": [...],
    "metrics_achieved": {...}
  },
  "workflow_finalization": {
    "handoff_updated": true,
    "cleanup_scheduled": true,
    "documentation_indexed": true,
    "workflow_state_archived": true
  }
}
```

## Integration Points
- **INPUT**: Voice validation results from verify-doc-voice
- **OUTPUT**: Final workflow completion results
- **NEXT**: Workflow complete - document deployed and ready for use

---
**Function**: Comprehensive workflow completion with deployment and rollback capabilities