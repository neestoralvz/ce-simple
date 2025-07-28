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

### Task Tools Deployment (EJECUTAR INMEDIATAMENTE):

**DEPLOYMENT PATTERN**: 4 Task tools concurrentes en mismo mensaje para máxima efficiency:

```python
# TASK 1: Research Specialist
Task(
    description="Research best practices documentation patterns",
    prompt="""Actúa como Research Specialist. Tu misión: Identificar best practices para el tipo de documento solicitado.

DOCUMENT TYPE: {document_type}
USER REQUEST: {user_request}
CONTEXT SOURCE: {context_source}

RESEARCH OBJECTIVES:
1. Best practices para {document_type} structure
2. Token economy optimization patterns
3. Context loading methodologies
4. Anti-patterns a evitar
5. Integration patterns con sistema existente

OUTPUT: Structured research findings con recommendations específicas.""",
    subagent_type="general-purpose"
)

# TASK 2: Content Specialist  
Task(
    description="Generate core document structure and content",
    prompt="""Actúa como Content Specialist. MISSION CRITICAL: Generar documento core usando research findings.

INPUT CONTEXT:
- Document type: {document_type}
- User requirements: {user_voice_quotes}
- Research findings: {research_output}
- Context source: {context_source}

CONTENT GENERATION REQUIREMENTS:
- Token economy: 50-80 líneas core máximo
- Context metadata: Complete decision tree
- User voice integration: Exact quotes preserved
- Structure optimization: Headers, sections, navigation
- Technical accuracy: Syntax, references, imports validated

OUTPUT: Complete document draft con metadata + context árbol.""",
    subagent_type="general-purpose"
)

# TASK 3: Voice Preservation Specialist (MANDATORY)
Task(
    description="MANDATORY voice separation compliance validation",
    prompt="""Actúa como Voice Preservation Specialist. ENFORCEMENT MISSION: Absolute user voice preservation.

VOICE PRESERVATION IMPERATIVES:
- Template: synthesis-voice-separation.md (MANDATORY)
- Separation: User voice vs system analysis (COMPLETE)
- Scoring: Voice preservation ≥54/60 (90%+ compliance)
- Immutability: Crystallized user decisions (PROTECTED)
- Attribution: Every quote linked to source (EXACT)

INPUT FOR ANALYSIS:
- User voice quotes: {user_voice_content}
- Context source: {source_location}
- Content draft: {content_specialist_output}

VOICE PRESERVATION VALIDATION:
1. Extract exact user quotes (ZERO paraphrasing)
2. Verify complete source attribution
3. Ensure user/system content separation
4. Mark crystallized decisions as immutable
5. Calculate voice preservation score
6. Enforce synthesis-voice-separation.md template

OUTPUT: Voice-validated document con scoring matrix + compliance verification.""",
    subagent_type="general-purpose"
)

# TASK 4: Architecture Validator
Task(
    description="Validate structure and metadata compliance",
    prompt="""Actúa como Architecture Validator. SYSTEM INTEGRATION MISSION: Ensure document integrates perfectly.

ARCHITECTURE VALIDATION SCOPE:
- Content draft: {content_with_voice_preservation}
- System context: Current architecture patterns
- Integration points: Command ecosystem, rules system
- Metadata compliance: Contextflow headers, decision trees

VALIDATION CHECKLIST:
1. Contextflow metadata: Complete y accurate
2. Decision tree: Semantic triggers, alternatives, next steps
3. System integration: No conflicts con commands/rules existentes
4. Token economy: Optimization sin perder functionality
5. Navigation structure: Clear headers, sections, links
6. Technical accuracy: Syntax validation, import references

OUTPUT: Architecture-validated document con integration compliance verified.""",
    subagent_type="general-purpose"
)
```

### VOICE PRESERVATION ENFORCEMENT:
**MANDATORY TEMPLATE**: synthesis-voice-separation.md automáticamente enforced por Voice Preservation Specialist
**SEPARATION PROTOCOL**: User voice vs system analysis completely separated via specialist validation
**SCORING ENFORCEMENT**: Voice preservation score ≥54/60 automatically validated
**IMMUTABILITY PROTECTION**: Crystallized user decisions automatically marked unchangeable
**SOURCE ATTRIBUTION**: Every user quote automatically linked to original source

**MAIN AGENT CONSOLIDATION**: Receive outputs from 4 specialists → Generate final document combining research, content, voice preservation, and architecture validation.

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

### Auto-Chain Task Tool Implementation (EXECUTABLE):

```python
# POST-SUCCESS AUTO-CHAIN EXECUTION
if subagent_deployment_success and document_created:
    # Update workflow state
    workflow_state.update({
        "current_step": 1,
        "status": "completed",
        "document_path": created_document_path,
        "timestamp": current_timestamp
    })
    
    # AUTO-CHAIN TO ALIGN-DOC
    Task(
        description="Auto-chain workflow to align-doc step",
        prompt="""Execute /align-doc command con workflow state continuation.

WORKFLOW STATE HANDOFF:
- workflow_id: {workflow_id}
- document_path: {created_document_path}
- document_type: {document_type}
- user_context: {original_user_request}
- voice_preservation_score: {voice_score}
- creation_results: {specialist_outputs_summary}
- research_findings: {research_specialist_output}
- auto_chain_enabled: true

EXECUTE: /align-doc command immediately con complete context preservation.

ALIGNMENT MISSION: Validate architecture consistency while preserving user voice and research findings.""",
        subagent_type="general-purpose"
    )
else:
    # ERROR HANDLING - PAUSE AUTO-CHAIN
    workflow_state.update({
        "status": "error",
        "error_details": error_summary,
        "auto_chain_paused": true
    })
    # Require user intervention
```

## Success Criteria + Auto-Chain Triggers (AUTOMATED VALIDATION):

**SPECIALIST DEPLOYMENT VALIDATION**:
- [x] 4 Task tools deployed concurrently (Research, Content, Voice Preservation, Architecture)
- [x] Voice Preservation Specialist deployment (MANDATORY - auto-enforced)
- [x] synthesis-voice-separation.md template usage (AUTO-ENFORCED by specialist)

**VOICE PRESERVATION VALIDATION** (Auto-verified by Voice Preservation Specialist):
- [x] User voice completely separated from system analysis
- [x] Voice preservation score ≥54/60 (AUTOMATICALLY calculated)
- [x] All user quotes exact with source attribution (ZERO paraphrasing tolerance)
- [x] Crystallized decisions marked immutable (AUTO-PROTECTION enabled)

**CONTENT & ARCHITECTURE VALIDATION** (Auto-verified by specialists):
- [x] Token economy optimized (50-80 líneas core - Content Specialist enforced)
- [x] Context metadata complete (Architecture Validator enforced)
- [x] System integration validated (NO conflicts detected)
- [x] Technical accuracy verified (Syntax, references, imports validated)

**WORKFLOW ORCHESTRATION** (Auto-managed):
- [x] Workflow state initialized and tracked (workflow_id generated)
- [x] Document path stored for chain progression
- [x] Auto-chain to align-doc triggered (CONDITIONAL on success)
- [x] Complete context handoff prepared (All specialist outputs preserved)
- [x] Voice preservation verification completed (Ready for next step)

**AUTO-CHAIN EXECUTION LOGIC**:
```python
if all_specialists_successful and voice_score >= 54:
    trigger_auto_chain_to_align_doc()
else:
    pause_workflow_for_user_intervention()
```

---
**Workflow**: CREATE → Align → Verify