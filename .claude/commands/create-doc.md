---
contextflow:
  purpose: "Creación documento via Content Specialist subagent"
  workflow-step: 1
  next: ["align-doc"]
  requires-subagent: true
  auto-chain: true
---

# Comando `/create-doc` - Workflow Step 1

## Subagent Orchestration OBLIGATORIA

**NUNCA crear contenido directamente** - SIEMPRE via Task tool con Content Specialist.

### Task Tools Deployment Paralelo:
```
EJECUTAR simultáneamente en mismo mensaje:

Task 1: Research Specialist - "Research best practices + existing patterns"
Task 2: Content Specialist - "Generate core document structure + content"
Task 3: Voice Preservation - "Ensure user voice quotes integration"
Task 4: Architecture Validator - "Validate structure + metadata compliance"
```

**Main agent consolida results y genera documento final.**

## Input Requirements:
- **Document type**: Command, rule, methodology, template
- **Core content**: User voice quotes + requirements
- **Context source**: Synthesis file o conversation reference

## Output Structure:
```markdown
---
contextflow:
  source: "[origen-synthesis-o-conversation]"
  user-voice: "[cita-decision-original]"
  created-by: "content-specialist-subagent"
---

# [Título]

## User Voice Original
> "[cita exacta usuario]"

## [Contenido optimizado por specialist]

---
**Ready for**: `/align-doc` - Architecture validation
```

## Auto-Chaining Implementation:

```markdown
IMPORT: @/.claude/commands/utilities/workflow-state-manager.md

WORKFLOW STATE INITIALIZATION:
1. Create workflow_id: "doc-{timestamp}"
2. Set current_step: 1
3. Store document_type from user input
4. Initialize step_history array
5. Enable auto_chain_enabled: true

POST-CREATION AUTO-CHAIN LOGIC:
IF subagent_deployment_success AND document_created:
  → UPDATE workflow state (step 1 completed)
  → STORE document_path in workflow state
  → AUTO-EXECUTE: Task tool with align-doc command
  → PASS: workflow_id + document_path + user_context
  
IF subagent_deployment_failed OR creation_errors:
  → SET error_state in workflow
  → PAUSE auto-chain progression
  → REQUIRE user intervention for error resolution
  
IF user_confirmation_required (complex documents):
  → PAUSE auto-chain temporarily
  → AWAIT user approval before align-doc trigger
  → RESUME auto-chain on user confirmation
```

### Auto-Chain Task Tool Implementation:
```markdown
POST-SUCCESS TRIGGER:
Task: Workflow Coordinator
Description: "Auto-chain to align-doc step"
Subagent: general-purpose
Prompt: "Execute /align-doc command with workflow state:
- workflow_id: {workflow_id}
- document_path: {created_document_path}
- user_context: {original_user_request}
- previous_step_output: {creation_results}

Auto-chain enabled - proceed immediately to alignment validation."
```

## Success Criteria + Auto-Chain Triggers:
- [ ] Subagent deployed via Task tool (no direct creation)
- [ ] User voice preserved in quotes
- [ ] Token economy optimized (50-80 líneas core)
- [ ] Context metadata complete
- [ ] Workflow state initialized and tracked
- [ ] Document path stored for chain progression
- [ ] Auto-chain to align-doc triggered successfully
- [ ] Next step receives complete context handoff

---
**Workflow**: CREATE → Align → Verify