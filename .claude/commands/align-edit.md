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

## Quality Gates for Auto-Chain to `/verify-edit`

### Success Criteria
- ✅ **Architecture Consistency**: No system conflicts detected
- ✅ **Voice Preservation**: Score maintained ≥54/60
- ✅ **Change Integration**: Modifications properly integrated
- ✅ **Quality Standards**: Edit quality meets minimum thresholds

### Auto-Chain Execution
```
IF all_validations_pass AND no_major_issues AND quality_acceptable:
    workflow_state = "verifying"
    auto_chain_to_verify_edit()
    preserve_alignment_context()
```

### Context Preservation for Verification
- **Alignment Results**: Complete validation outcomes
- **Issue Resolution**: Any corrections applied during alignment
- **Quality Metrics**: Updated quality assessment scores
- **Voice Validation**: Final voice preservation analysis

## Rollback Scenarios

### Rollback to Edit Phase
**Triggers**: Issues that require edit modification
- **Voice contamination detected**: Return to edit phase for voice correction
- **Architecture conflicts**: Return to edit phase for system compliance
- **Integration failures**: Return to edit phase for compatibility fixes

### Rollback Process
```
preserve_alignment_analysis()
revert_to_edit_state()
provide_specific_correction_guidance()
maintain_rollback_history()
```

## Performance Optimization

### Alignment Efficiency
- **Parallel Validation**: Concurrent specialist deployment
- **Targeted Analysis**: Focus on modified sections primarily
- **Context Efficiency**: Minimize resource usage during validation
- **Quick Resolution**: Rapid auto-correction for minor issues

### Resource Management
- **Token Economy**: Efficient context usage during alignment
- **Processing Priority**: Critical validations first
- **Memory Optimization**: Streamlined state management
- **Performance Monitoring**: Alignment phase timing optimization

## User Communication Protocol

### Successful Alignment Communication
```
"Edit alignment completed successfully. All validations passed. Auto-chaining to /verify-edit for final quality gates."
```

### Minor Issues Auto-Corrected Communication
```
"Edit alignment detected minor issues: {issue_list}. Auto-corrections applied successfully. Proceeding to verification phase."
```

### Major Issues Detected Communication
```
"Edit alignment detected major issues requiring resolution: {issue_details}. Workflow paused. Options: 1) Rollback to edit phase 2) Manual resolution guidance. Please specify preferred approach."
```

## Integration with Workflow System

### State Management
- **Workflow Continuity**: Seamless state progression from edit to align to verify
- **Context Preservation**: Complete information handoff between phases
- **Error Recovery**: Robust rollback and retry mechanisms
- **Quality Tracking**: Progressive quality score monitoring

### Enforcement Integration
- **Workflow Validation**: Ensure proper workflow sequence
- **Permission Verification**: Validate edit authorization
- **Compliance Monitoring**: Track alignment success metrics
- **Audit Trail**: Complete alignment decision logging

---

**ESTE COMANDO VALIDA** edit consistency y system alignment.
**AUTO-CHAIN SIGUIENTE**: `/verify-edit` with complete alignment context.
**ROLLBACK DISPONIBLE**: Return to `/edit-doc` for issue resolution.