---
contextflow:
  purpose: "Workflow state tracking and auto-chaining coordination"
  type: "utility-system"
  integration: "workflow-commands"
---

# Workflow State Manager

## State Tracking System

### Workflow State Structure:
```json
{
  "workflow_id": "doc-{timestamp}",
  "current_step": 1,
  "document_path": "/path/to/document.md",
  "document_type": "command|rule|methodology|template",
  "user_context": "original user request",
  "step_history": [
    {
      "step": 1,
      "command": "create-doc",
      "status": "completed",
      "timestamp": "2025-07-28T12:00:00Z",
      "output_file": "/path/to/created-doc.md"
    }
  ],
  "auto_chain_enabled": true,
  "user_confirmation_required": false,
  "error_state": null
}
```

## Auto-Chaining Logic Implementation

### Step Progression Rules:
```markdown
CREATE-DOC (Step 1):
- ON SUCCESS → AUTO-EXECUTE align-doc with created document
- ON ERROR → PAUSE workflow, require user intervention

ALIGN-DOC (Step 2):  
- ON SUCCESS (no issues) → AUTO-EXECUTE verify-doc with aligned document
- ON SUCCESS (minor issues fixed) → AUTO-EXECUTE verify-doc with corrected document
- ON MAJOR-CONFLICTS → PAUSE workflow, require user decision

VERIFY-DOC (Step 3):
- ON SUCCESS → COMPLETE workflow, notify user of completion
- ON MINOR-ISSUES → AUTO-FIX and complete workflow
- ON MAJOR-ISSUES → RETURN to appropriate previous step
```

## Context Preservation Protocol

### Document Context Chain:
```markdown
Step 1 → Step 2:
- Document file path
- User voice quotes
- Creation metadata
- Content specialist outputs

Step 2 → Step 3:
- Aligned document path
- Architecture validation results
- Applied corrections log
- Integration status

Step 3 → Completion:
- Final document path
- Quality scores
- Optimization log
- Deployment readiness
```

## Error Handling & Rollback

### Error State Management:
```markdown
RECOVERABLE ERRORS:
- Minor validation issues → Auto-fix and continue
- Content optimization needs → Apply improvements and continue
- Missing metadata → Regenerate and continue

NON-RECOVERABLE ERRORS:
- Major architecture conflicts → Return to align-doc
- User voice distortion → Return to create-doc
- System integration failures → Full workflow restart
```

### Rollback Mechanisms:
```markdown
ROLLBACK TRIGGERS:
- Workflow step failure after 2 retry attempts
- User explicit rollback request
- Data corruption detection
- Integration conflict resolution failure

ROLLBACK ACTIONS:
- Restore previous step state
- Clear error conditions
- Preserve user context
- Reset auto-chain status
```

## Integration Instructions

### For Workflow Commands:
1. Import this state manager at command start
2. Initialize workflow state before subagent deployment
3. Update state after each successful operation
4. Check auto-chain conditions before triggering next step
5. Handle errors according to defined protocols

### State Persistence:
- Store workflow state in `/handoff/workflow-states/`
- Maintain state across command executions
- Clean up completed workflow states after 24 hours
- Log all state transitions for debugging

---
**Integration**: Import into all workflow commands for state management