---
contextflow:
  purpose: "Final edit verification via Quality Assurance subagent"
  workflow-step: 3
  prev: ["align-edit"]
  requires-subagent: true
  auto-chain: false
  research-driven: true
  triggers: ["verify edit", "final validation", "edit completion"]
  communication-rules:
    - "NUNCA bash echo para comunicar con usuario"
    - "SIEMPRE Task tools → Main agent → Usuario"
    - "Parallel Task tools obligatorio en mismo mensaje"
    - "Subagents NUNCA comunican directamente"
  decision-tree:
    use-when:
      - "Final edit quality validation required"
      - "Production deployment preparation needed"
      - "Edit workflow completion validation"
    alternatives: ["align-edit"]
    semantic-triggers:
      - "verify edit" / "validate edit" / "final check"
      - "edit verification" / "quality gates"
      - "production ready" / "deployment ready"
---

# Comando `/verify-edit`

## Propósito Core
Verification final de ediciones documentales con quality gates, production readiness validation y deployment preparation.

## CONTEXT OBLIGATORIO - WORKFLOW COMPLETION

**PREREQUISITO**: Este comando SOLO ejecuta tras `/align-edit` completion. NO funciona standalone.
**ESTADO REQUERIDO**: workflow_state = "verifying" con alignment context completo.

## Final Quality Gates Framework

### Critical Verification Dimensions
- **Edit Quality Score**: ≥85/100 production readiness threshold
- **Voice Preservation Final**: ≥54/60 voice integrity confirmation
- **Change Verification**: Complete modification validation
- **Production Deployment**: System readiness for edited document

## Template-Based Final Verification

### Specialist Deployment (Production Ready)
```
Task: Quality Assurance (from ../templates/quality-assurance.md)
Focus: Final quality gates (≥85/100) + production readiness

Task: Voice Preservation (from ../templates/voice-preservation.md)
Focus: Voice integrity final confirmation (≥54/60)

Task: Change Impact Analyzer (from ../templates/change-impact-analyzer.md)
Focus: Edit completion + deployment validation
```

## Workflow State Completion

### Orchestrator-Managed Completion

**Reference**: ../utilities/edit-workflow-orchestrator.md completion patterns
**Context handoff**: Template specialists receive full workflow context
**Deployment logic**: Template-enforced production readiness validation

## Template-Driven Final Validation

**Quality gates**: Templates enforce ≥85/100 quality + ≥54/60 voice thresholds
**Production readiness**: Template-based deployment validation
**Change verification**: Template-enforced completion requirements
**Integration**: Template coordination ensures seamless deployment preparation

## Production Deployment (Template-Managed)

**Validation**: Template-enforced quality gates must pass
**Deployment**: Orchestrator executes template-validated deployment
**Finalization**: Template-based document and system updates

## Final Rollback (Template-Based)

**Triggers**: Template validation failures (quality <85/100, voice <54/60)
**Resolution**: Orchestrator determines rollback target with template guidance

## Completion Documentation (Template-Generated)

**Documentation**: Template-based completion reports
**Audit trail**: Orchestrator-managed change tracking
**Quality metrics**: Template-enforced score progression

## Performance (Template-Optimized)

**Efficiency**: Template-based concurrent validation
**Resource usage**: Template references minimize context consumption
**Quality assurance**: Template-enforced comprehensive validation

## User Communication

**Success**: "Edit verification completed. Quality: {score}/100, Voice: {score}/60. Document deployed."
**Issues**: "Verification detected issues: {details}. Template-based resolution required."
**Failure**: "Verification failed: {reason}. Template-guided rollback initiated."

## System Integration

**Template coordination**: Final verification via template specialists
**Orchestrator management**: Workflow completion and deployment
**Quality tracking**: Template-enforced metrics and documentation

---

**TEMPLATE-DRIVEN COMPLETION** of edit workflow with production deployment.
**WORKFLOW COMPLETE**: Document successfully verified and deployed.
**TEMPLATE-BASED AUDIT**: Complete change documentation preserved.