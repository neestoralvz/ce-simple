---
contextflow:
  purpose: "Comprehensive error handling and rollback system for document workflow"
  type: "utility-system"
  integration: "workflow-state-manager"
---

# Workflow Error Handler & Rollback System

## Error Classification System

### Error Severity Levels:
```markdown
LEVEL 1 - MINOR ERRORS (Auto-Recoverable):
- Token economy optimization needed
- Minor formatting issues
- Missing non-critical metadata
- Simple content improvements

LEVEL 2 - MODERATE ERRORS (Auto-Fixable):
- Structure alignment issues
- Non-critical voice preservation problems
- Integration warnings (non-breaking)
- Quality gate minor failures

LEVEL 3 - MAJOR ERRORS (User Decision Required):
- Architecture conflicts with existing system
- User voice distortion detected
- Major integration breaking changes
- Quality gate critical failures

LEVEL 4 - CRITICAL ERRORS (Workflow Restart):
- System corruption detected
- Unrecoverable data loss
- Security violations
- Multiple cascade failures
```

## Auto-Recovery Mechanisms

### Level 1 & 2 Auto-Fix Protocol:
```markdown
DETECTION TRIGGER:
Task: Error Recovery Specialist
Description: "Auto-fix minor/moderate workflow errors"
Subagent: general-purpose
Prompt: "Detected {error_level} errors in workflow step {current_step}:

ERROR DETAILS:
{error_list_with_details}

AUTO-FIX PROTOCOL:
1. Analyze error impact on workflow progression
2. Apply appropriate fixes maintaining user voice
3. Validate fixes don't introduce new issues
4. Update workflow state with fix log
5. Continue auto-chain progression
6. Report fixes applied to user (non-blocking)

CONSTRAINTS:
- Never modify user voice quotes
- Preserve original intent
- Maintain document quality standards
- Log all changes for audit trail"
```

## Rollback Decision Matrix

### Rollback Target Determination:
```markdown
ROLLBACK TO CREATE-DOC (Step 1):
- User voice severely distorted
- Document type fundamentally wrong
- Content specialist deployment failed
- Original requirements misunderstood

ROLLBACK TO ALIGN-DOC (Step 2):
- Architecture validation failures
- System integration conflicts
- Alignment corrections corrupted document
- Structure incompatibility detected

ROLLBACK TO VERIFY-DOC (Step 3):
- Quality gate recalibration needed
- Final optimization corrupted content
- Deployment target requirements changed
- User requested final review
```

## Rollback Execution Protocol

### State Preservation During Rollback:
```json
{
  "rollback_state": {
    "triggered_from_step": 3,
    "rollback_target_step": 2,
    "rollback_reason": "major_architecture_conflict",
    "preserved_context": {
      "original_user_request": "...",
      "user_voice_quotes": ["..."],
      "work_completed": {
        "step_1_outputs": "...",
        "step_2_partial": "..."
      },
      "lessons_learned": ["..."]
    },
    "rollback_timestamp": "2025-07-28T12:30:00Z"
  }
}
```

### Rollback Task Implementation:
```markdown
ROLLBACK EXECUTION:
Task: Workflow Rollback Manager
Description: "Execute safe rollback to {target_step}"
Subagent: general-purpose
Prompt: "Execute workflow rollback:

ROLLBACK DETAILS:
- From Step: {current_step}
- To Step: {target_step}  
- Reason: {rollback_reason}
- Preserved Context: {context_summary}

ROLLBACK ACTIONS:
1. Restore workflow state to step {target_step}
2. Preserve all user context and voice quotes
3. Maintain work completed up to rollback point
4. Clear error states from failed progression
5. Prepare clean environment for step restart
6. Log rollback execution for debugging
7. Notify user with clear rollback explanation

RESTART PREPARATION:
Execute /{target_step_command} with preserved context."
```

## Error Prevention & Early Detection

### Pre-Step Validation:
```markdown
BEFORE EACH WORKFLOW STEP:
Task: Pre-Step Validator
Description: "Validate readiness for {next_step}"
Subagent: general-purpose
Prompt: "Pre-step validation for {next_step}:

VALIDATION CHECKLIST:
- Previous step completed successfully
- Required inputs available and valid
- Context preservation verified
- No error states in workflow
- Auto-chain conditions met
- User confirmation obtained (if required)

OUTPUT: 
- PROCEED: Continue to {next_step}
- PAUSE: Issue details + resolution needed
- ROLLBACK: Target step + reason"
```

## Error Logging & Audit Trail

### Comprehensive Error Logging:
```markdown
ERROR LOG STRUCTURE:
{
  "workflow_id": "doc-{timestamp}",
  "error_log": [
    {
      "step": 2,
      "error_type": "moderate",
      "error_code": "ARCH_CONFLICT_001",
      "description": "Architecture validator detected conflict with existing rule system",
      "auto_fix_attempted": true,
      "auto_fix_success": false,
      "user_intervention_required": true,
      "resolution_action": "rollback_to_step_1",
      "timestamp": "2025-07-28T12:15:00Z"
    }
  ]
}
```

## User Communication Protocol

### Error Notification Format:
```markdown
🚨 WORKFLOW ISSUE DETECTED

**Step**: {current_step} ({step_name})
**Severity**: {error_level}
**Issue**: {user_friendly_description}

**Auto-Recovery**: {attempted_fixes}
**Status**: {current_status}

**Next Steps**:
{user_action_required_or_auto_continuation}

**Context Preserved**: ✅ All your work is safe
**Rollback Available**: ✅ Can return to previous steps if needed
```

---
**Integration**: Auto-imported by workflow-state-manager for error handling