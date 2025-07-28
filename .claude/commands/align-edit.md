---
contextflow:
  purpose: "Edit alignment validation via Architecture Validator subagent"
  workflow-step: 2
  prev: ["edit-doc"]
  next: ["verify-edit"]
  requires-subagent: true
  auto-chain: true
  research-driven: true
  triggers: ["edit alignment", "document validation", "edit consistency"]
  communication-rules:
    - "NUNCA bash echo para comunicar con usuario"
    - "SIEMPRE Task tools → Main agent → Usuario"
    - "Parallel Task tools obligatorio en mismo mensaje"
    - "Subagents NUNCA comunican directamente"
  decision-tree:
    use-when:
      - "Post-edit document alignment validation needed"
      - "Architecture consistency verification required"
      - "Voice preservation through edits validation"
    alternatives: ["edit-doc"]
    semantic-triggers:
      - "align edit" / "validate edit" / "check consistency"
      - "edit alignment" / "document alignment"
      - "edit validation" / "consistency check"
---

# Comando `/align-edit`

## Propósito Core
Validación de consistencia y alineación de ediciones documentales con system architecture y voice preservation standards.

## CONTEXT OBLIGATORIO - WORKFLOW CONTINUATION

**PREREQUISITO**: Este comando SOLO ejecuta tras `/edit-doc` completion. NO funciona standalone.
**ESTADO REQUERIDO**: workflow_state = "aligning" con edit context completo.

## Edit Alignment Validation Framework

### Critical Validation Dimensions
- **Architecture Consistency**: Edit impact on system integrity
- **Voice Preservation Continuity**: Voice score maintenance ≥54/60
- **Change Impact Assessment**: Downstream effects of modifications
- **Integration Validation**: System interoperability preservation

## Template-Based Alignment Validation

### Specialist Deployment (Conditional)
```
Task: Architecture Validator (from ../templates/architecture-validator.md)
Focus: Edit consistency + system impact validation

Task: Voice Preservation (from ../templates/voice-preservation.md)
Focus: Voice integrity + contamination detection (≥54/60)

Task: Change Impact Analyzer (from ../templates/change-impact-analyzer.md)
Focus: Downstream effects + dependency validation

Task: Integration Specialist (from ../templates/integration-specialist.md)
Focus: Cross-reference + integration validation
```

## Workflow State Continuation

### Orchestrator-Managed State Transition

**Reference**: ../utilities/edit-workflow-orchestrator.md state management
**Context handoff**: Template-based specialists receive editing context
**Auto-chain logic**: Conditional progression based on validation results

## Template-Driven Validation (Efficient)

**All specialists**: Use template references from /templates/ directory
**Validation logic**: Template-enforced quality gates and thresholds
**Documentation**: Template-based deliverable standardization
**Integration**: Orchestrator coordinates template specialist deployment

## Auto-Correction (Template-Based)

**Template protocols**: Each template includes auto-correction logic
**Minor issues**: Template-based automatic resolution
**Validation**: Template-enforced success criteria

## Major Issue Resolution (Orchestrator-Managed)

**Blocking conditions**: Template validation failures, voice <54/60, architecture violations
**Resolution**: Orchestrator manages rollback decisions and user guidance

## Quality Gates (Template-Enforced)

**Success criteria**: Template validation passes for all specialists
**Auto-chain logic**: Orchestrator-managed conditional progression
**Context preservation**: Template-based state handoff to verify-edit

## Rollback (Template-Based)

**Triggers**: Template validation failures requiring edit modification
**Process**: Orchestrator-managed rollback with template-based guidance

## Performance (Template-Optimized)

**Efficiency**: Template-based specialist deployment minimizes context usage
**Parallel processing**: Concurrent template validation
**Resource optimization**: Template references reduce token consumption

## User Communication

**Success**: "Edit alignment completed via template validation. Auto-chaining to verification."
**Issues**: "Alignment detected issues: {details}. Template-based resolution applied."
**Failure**: "Alignment validation failed. Template-guided rollback initiated."

## System Integration

**Template coordination**: All validation via template specialists
**Orchestrator management**: State progression and context handoff
**Quality tracking**: Template-enforced progressive validation

---

**TEMPLATE-DRIVEN VALIDATION** for edit consistency and system alignment.
**CONDITIONAL AUTO-CHAIN**: To `/verify-edit` based on validation results.
**TEMPLATE-BASED ROLLBACK**: Guided resolution for validation failures.