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
Task 3: Voice Preservation Specialist - "MANDATORY voice separation compliance using synthesis-voice-separation.md template"
Task 4: Architecture Validator - "Validate structure + metadata compliance"
```

### VOICE PRESERVATION ENFORCEMENT:
**MANDATORY TEMPLATE**: Must use synthesis-voice-separation.md template for ALL document creation
**SEPARATION REQUIRED**: User voice and system analysis completely separated
**SCORING THRESHOLD**: Voice preservation score ≥90% required for approval
**IMMUTABILITY**: Crystallized user decisions marked as unchangeable
**SOURCE ATTRIBUTION**: Every user quote linked to original source

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
  user-voice-score: "[X/60 - must be ≥54 for approval]"
  voice-separation: "ENFORCED"
  created-by: "content-specialist-subagent"
  template-used: "synthesis-voice-separation.md"
---

# [Título]

## 👤 USER VOICE - FUENTE DE VERDAD ABSOLUTA (IMMUTABLE)
> "[cita exacta usuario 1]" - Source: [/path/to/source.md:line-X]
> "[cita exacta usuario 2]" - Source: [/path/to/source.md:line-Y]

**CRYSTALLIZED DECISIONS (NO EVOLUTION ALLOWED):**
- Decision: "[exact user words]"
- Status: IMMUTABLE

## 📊 SYSTEM ANALYSIS (INTERPRETATION - SEPARATE FROM USER VOICE)
[System analysis and implementation guidance]

## 🔗 VOICE PRESERVATION AUDIT
**TOTAL VOICE PRESERVATION SCORE: [X/60]** - Must be ≥54

---
**Ready for**: `/align-doc` - Architecture validation with voice preservation verified
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
- [ ] Voice Preservation Specialist deployed (MANDATORY)
- [ ] synthesis-voice-separation.md template used (ENFORCED)
- [ ] User voice completely separated from system analysis
- [ ] Voice preservation score ≥54/60 (90%+ compliance)
- [ ] All user quotes exact with source attribution
- [ ] Crystallized decisions marked as immutable
- [ ] Token economy optimized (50-80 líneas core)
- [ ] Context metadata complete
- [ ] Workflow state initialized and tracked
- [ ] Document path stored for chain progression
- [ ] Auto-chain to align-doc triggered successfully
- [ ] Next step receives complete context handoff with voice preservation verified

---
**Workflow**: CREATE → Align → Verify