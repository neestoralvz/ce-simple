---
contextflow:
  purpose: "Complete integration guide for auto-chaining workflow system"
  type: "integration-documentation"
  scope: "system-wide"
---

# Auto-Chaining Integration Guide

## System Architecture Overview

### Component Integration Map:
```markdown
WORKFLOW COMMANDS:
├── create-doc.md (Step 1) 
│   ├── Import: workflow-state-manager.md
│   ├── Import: context-preservation-framework.md
│   └── Auto-chain: → align-doc
├── align-doc.md (Step 2)
│   ├── Import: workflow-state-manager.md
│   ├── Import: workflow-error-handler.md
│   └── Auto-chain: → verify-doc
└── verify-doc.md (Step 3)
    ├── Import: workflow-state-manager.md
    ├── Import: workflow-error-handler.md
    └── Complete: workflow + cleanup

UTILITY SYSTEMS:
├── workflow-state-manager.md (State tracking)
├── workflow-error-handler.md (Error handling + rollback)
├── context-preservation-framework.md (Context continuity)
└── auto-chaining-integration-guide.md (This guide)
```

## Complete Workflow Execution Flow

### Step 1: CREATE-DOC Auto-Chain Sequence:
```markdown
1. INITIALIZE WORKFLOW:
   - Generate workflow_id: "doc-{timestamp}"
   - Create workflow state with user context
   - Set current_step: 1, auto_chain_enabled: true

2. DEPLOY SUBAGENTS (Parallel Task Tools):
   - Research Specialist
   - Content Specialist  
   - Voice Preservation Validator
   - Architecture Validator

3. CONTEXT PRESERVATION:
   - Store original user request exactly
   - Preserve user voice quotes with attribution
   - Maintain document type and target specifications

4. SUCCESS VALIDATION:
   - Document created successfully
   - User voice preserved in quotes
   - Token economy optimized (50-80 lines core)
   - Metadata structure complete

5. AUTO-CHAIN TRIGGER:
   - Update workflow state (step 1 completed)
   - Store document_path for next step
   - AUTO-EXECUTE align-doc via Task tool
   - Pass complete context package

ERROR HANDLING:
- Minor issues: Auto-fix and continue
- Major issues: Pause auto-chain, require user intervention
```

### Step 2: ALIGN-DOC Auto-Chain Sequence:
```markdown
1. RECEIVE CONTEXT HANDOFF:
   - Load workflow_id from create-doc
   - Validate context package integrity
   - Update current_step: 2

2. DEPLOY SUBAGENTS (Parallel Task Tools):
   - Architecture Validator
   - Research Specialist (benchmarking)
   - Voice Preservation Validator
   - Content Optimizer

3. ALIGNMENT VALIDATION:
   - System consistency check
   - Integration conflict detection
   - User voice preservation verification
   - Standards compliance validation

4. CORRECTION PROCESSING:
   - Minor issues: Auto-apply corrections
   - Moderate issues: Apply fixes and log changes
   - Major conflicts: Pause for user decision

5. AUTO-CHAIN TRIGGER:
   - Update workflow state (step 2 completed)
   - Store aligned document + validation results  
   - AUTO-EXECUTE verify-doc via Task tool
   - Pass context + alignment results

ROLLBACK CONDITIONS:
- Major architecture conflicts → User decision required
- User voice distortion → Rollback to create-doc
- Integration breaking changes → Pause workflow
```

### Step 3: VERIFY-DOC Completion Sequence:
```markdown
1. RECEIVE CONTEXT HANDOFF:
   - Load complete workflow state
   - Validate document progression chain
   - Update current_step: 3 (final)

2. DEPLOY SUBAGENTS (Primary + Concurrent):
   - Quality Assurance Specialist (primary)
   - Content Optimizer (concurrent)
   - Voice Preservation Validator (concurrent)

3. QUALITY VALIDATION:
   - Token economy final check (≤80 lines core)
   - Context metadata completion
   - No duplication vs existing docs
   - Technical accuracy validation
   - Readability optimization

4. COMPLETION PROCESSING:
   - Quality gates passed: Deploy and complete
   - Minor issues: Auto-fix and deploy
   - Major issues: Rollback to appropriate step

5. WORKFLOW COMPLETION:
   - Update workflow state: "completed"
   - Deploy document to target location
   - Update handoff with new document
   - Notify user of completion
   - Schedule state cleanup (24h)

ROLLBACK CONDITIONS:
- Quality gate critical failures → Rollback to align-doc
- Content corruption detected → Rollback to create-doc
- User requested final review → Pause for confirmation
```

## Task Tool Implementation Patterns

### Standard Auto-Chain Task Pattern:
```markdown
TASK TEMPLATE FOR AUTO-CHAINING:
Task: Workflow Coordinator
Description: "Auto-chain from {current_step} to {next_step}"
Subagent: general-purpose
Prompt: "Execute auto-chain workflow progression:

SOURCE STEP: {current_step}
TARGET STEP: {next_step}
WORKFLOW ID: {workflow_id}

CONTEXT HANDOFF:
- Document Path: {current_document_path}
- User Context: {preserved_user_context}
- Step Results: {current_step_outputs}
- Context Validation: {context_integrity_status}

EXECUTION:
1. Validate context handoff complete
2. Execute /{next_step_command} with full context
3. Maintain auto-chain progression
4. Handle any errors per error-handler protocols"
```

### Error Recovery Task Pattern:
```markdown
ERROR RECOVERY TASK TEMPLATE:
Task: Error Recovery Specialist
Description: "Recover from {error_type} in step {step_number}"
Subagent: general-purpose
Prompt: "Error recovery required:

ERROR DETAILS:
- Type: {error_classification}
- Step: {current_step}
- Description: {error_description}

RECOVERY PROTOCOL:
1. Assess error severity and recovery approach
2. Apply appropriate auto-fix or rollback
3. Preserve all user context during recovery
4. Update workflow state with recovery actions
5. Continue or pause auto-chain as appropriate
6. Notify user of recovery actions taken"
```

## State Persistence Implementation

### Workflow State Directory Structure:
```markdown
/handoff/workflow-states/
├── active/
│   ├── doc-{timestamp}.json (active workflow states)
│   └── error-{workflow_id}.json (error state backups)
├── completed/
│   └── doc-{timestamp}.json (completed workflow logs)
└── cleanup/
    └── scheduled-{date}.json (cleanup schedule)

STATE PERSISTENCE RULES:
- Save state after each successful step
- Backup state before error recovery attempts
- Preserve state during rollback operations
- Clean up completed states after 24 hours
- Maintain error logs for debugging
```

## User Experience Guidelines

### Seamless Auto-Chain Experience:
```markdown
USER INTERACTION PRINCIPLES:
1. INVISIBLE AUTOMATION: Auto-chain works behind the scenes
2. CONTEXT PRESERVATION: User never repeats information
3. CLEAR COMMUNICATION: User informed of progress without overwhelm
4. ERROR TRANSPARENCY: Clear explanation when manual intervention needed
5. ROLLBACK SAFETY: User work never lost during errors

NOTIFICATION STRATEGY:
- Progress updates: Brief, non-intrusive
- Success completion: Clear summary of deliverables
- Error states: Specific, actionable guidance
- Rollback situations: Reassurance that work is preserved
```

## System Monitoring & Maintenance

### Auto-Chain Health Monitoring:
```markdown
MONITORING CHECKPOINTS:
- Workflow initiation success rate
- Auto-chain progression reliability  
- Context preservation accuracy
- Error recovery effectiveness
- User intervention frequency
- Completion time metrics

MAINTENANCE PROTOCOLS:
- Weekly auto-chain performance review
- Monthly error pattern analysis
- Quarterly context preservation audit
- Continuous workflow optimization
```

---
**Status**: ✅ Complete auto-chaining system implemented and integrated
**Next Steps**: Deploy with enforcement mechanism for production workflow