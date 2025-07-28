---
contextflow:
  purpose: "Document editing via multi-specialist orchestration"
  workflow-step: 1
  next: ["align-edit"]
  requires-subagent: true
  auto-chain: true
  research-driven: true
  triggers: ["edit document", "modify document", "update document"]
  communication-rules:
    - "NUNCA bash echo para comunicar con usuario"
    - "SIEMPRE Task tools → Main agent → Usuario"
    - "Parallel Task tools obligatorio en mismo mensaje"
    - "Subagents NUNCA comunican directamente"
  decision-tree:
    use-when:
      - "Existing document modification required"
      - "Content updates needed while preserving voice"
      - "Controlled document editing workflow"
    alternatives: ["create-doc", "maintain-docs"]
    semantic-triggers:
      - "edit" / "modify" / "update document"
      - "change document" / "alter content"
      - "document modification" / "content edit"
---

# Comando `/edit-doc`

## Propósito Core
Modificación controlada de documentos existentes via multi-specialist orchestration manteniendo voice preservation y system integrity.

## IMPERATIVO OBLIGATORIO - NUNCA EDITAR DIRECTAMENTE

**WORKFLOW ENFORCEMENT**: NUNCA usar Edit/MultiEdit para documentos .md fuera de este workflow. SIEMPRE iniciar con `/edit-doc` → auto-chain a `/align-edit` → `/verify-edit`.

## Pre-Edit Validation OBLIGATORIA

### Validaciones Críticas (BLOCKING)
```
IF documento_no_existe OR voice_score < 54 OR conflicts_detected:
    BLOCK_EDIT_OPERATION()
    RETURN error_guidance_message
    EXIT_WORKFLOW()
```

### Document Requirements
- **Document Existence**: Target file must exist with valid content
- **Voice Score Minimum**: Existing document must have ≥54/60 voice preservation score
- **Architecture Consistency**: No conflicts with system rules or commands
- **Edit Permission**: Document type must be editable (not system-critical files)

## Multi-Specialist Orchestration OBLIGATORIA

### Template-Based Specialist Deployment
**Deploy when**: Document modification required
```
Task: Edit Specialist (from ../templates/edit-specialist.md)
Focus: Surgical document modification + voice preservation

Task: Change Impact Analyzer (from ../templates/change-impact-analyzer.md)
Focus: Change scope assessment + dependency validation

Task: Voice Preservation (from ../templates/voice-preservation.md)
Focus: Voice integrity validation (≥54/60 requirement)

Task: Architecture Validator (from ../templates/architecture-validator.md)
Focus: System impact + conflict detection
```

## Workflow State Management (via Orchestrator)

**Reference**: ../utilities/edit-workflow-orchestrator.md patterns

### Conditional Deployment Logic
```
IF minor_edit: Deploy Edit + Voice templates only
IF major_edit: Deploy full template suite
IF critical_edit: Deploy enhanced validation suite
```

### Auto-Chain Progression (Conditional)
- **Minor**: skip alignment → direct verification
- **Major**: full edit → align → verify progression  
- **Critical**: enhanced validation at each step

## Change Classification & Specialist Deployment

### Minor Edits (Streamlined Processing)
- **Triggers**: Typo corrections, format adjustments, simple content additions
- **Specialists**: Edit Specialist + Voice Preservation (from templates)
- **Auto-chain**: Direct to verification if quality gates met

### Major Edits (Full Workflow)
- **Triggers**: Structural changes, logic modifications, voice preservation updates
- **Specialists**: All 4 template-based specialists deployed
- **Auto-chain**: Full edit → align → verify progression

### Critical Edits (Enhanced Validation)
- **Triggers**: Architecture changes, system integration modifications
- **Specialists**: Enhanced template deployment + additional validation
- **Auto-chain**: Full workflow with rollback checkpoints

## Auto-Chain Logic (Orchestrator-Managed)

**Reference**: ../utilities/edit-workflow-orchestrator.md conditional progression
**Success criteria**: Template validation passes + quality gates met
**Context preservation**: Orchestrator maintains state between workflow steps

## Rollback (Template-Based)

**Triggers**: Template validation failures, voice score <54/60, system conflicts
**Process**: Orchestrator-managed restoration with template-based guidance

## Token Economy (Template-Driven)

**Template optimization**: All specialists follow template efficiency patterns
**Scope limits**: 50-80 lines maximum (enforced via change classification)
**Context efficiency**: Template references minimize token usage
**Parallel processing**: Concurrent template-based deployment

## Quality Gates (Template-Enforced)

**Template validation**: All templates include quality thresholds
**Voice preservation**: ≥54/60 (enforced by voice-preservation.md template)
**System integrity**: Architecture-validator.md template ensures compliance
**Change accuracy**: Edit-specialist.md template ensures precision

**Auto-chain logic**: Orchestrator handles conditional progression based on change complexity

## User Communication

**Success**: "Edit workflow initiated via template-based specialists. Change complexity: {classification}. Auto-chaining based on validation results."
**Issues**: "Edit workflow auto-correcting via template protocols. Enhanced monitoring enabled."
**Failure**: "Edit workflow failed: {reason}. Template-based rollback initiated."

## System Integration

**Template enforcement**: All specialists use validated templates from /templates/
**Orchestrator coordination**: ../utilities/edit-workflow-orchestrator.md manages progression
**Workflow continuity**: Conditional auto-chain based on change classification
**Quality tracking**: Template-based validation ensures consistency

---

**TEMPLATE-DRIVEN WORKFLOW** for all document edits.
**CONDITIONAL AUTO-CHAIN**: Based on change complexity classification.
**ROLLBACK**: Template-based restoration protocols.