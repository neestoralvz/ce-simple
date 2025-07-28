---
contextflow:
  purpose: "Verificación final via Quality Assurance subagent"
  workflow-step: 3
  prev: ["align-doc"]
  workflow-complete: true
  requires-subagent: true
---

# Comando `/verify-doc` - Workflow Step 3 (Final)

## Subagent Orchestration OBLIGATORIA

**NUNCA hacer quality verification directamente** - SIEMPRE via Task tool con Quality Assurance specialist.

### Primary Task Tool Deployment:
```
Task: Quality Assurance Specialist
Description: "Verificación calidad final documento"
Subagent: general-purpose
Prompt: "Actúa como Quality Assurance Specialist. Verificación final documento:

QUALITY CHECKLIST:
- Token economy: 50-80 líneas core máximo
- Context loading: metadata árbol decisiones completo
- No duplicación: verificar vs documentos existentes
- Structure optimization: headers, sections, links
- Technical accuracy: syntax, references, imports
- Readability: clarity sin perder información densa

OUTPUT: Quality score + specific improvements needed + final optimized version"
```

### Concurrent Verification Tasks:
```
Task: Content Optimizer
Description: "Token economy final optimization"
Subagent: general-purpose
Prompt: "Optimizar documento para máxima token efficiency manteniendo información completa. Focus en densidad sin perder clarity."

Task: Voice Preservation Validator  
Description: "MANDATORY final voice preservation validation with scoring"
Subagent: general-purpose
Prompt: "Actúa como Voice Preservation Validator. ENFORCEMENT MISSION: Verificar voice preservation compliance usando scoring system.

VALIDATION IMPERATIVES:
- Voice preservation score MUST be ≥54/60 (90% compliance)
- User voice and system analysis MUST be completely separated
- All user quotes MUST be exact with source attribution
- Crystallized decisions MUST be marked as immutable
- ZERO voice contamination tolerance

SCORING MATRIX (MANDATORY):
- Quote Accuracy [X/10]: Zero paraphrasing - exact user words only
- Intent Fidelity [X/10]: Original meaning maintained without interpretation
- Context Completeness [X/10]: Full situational context preserved  
- Source Traceability [X/10]: Perfect links to original sources
- Attribution Clarity [X/10]: Complete separation user/system content
- Immutability Status [X/10]: Crystallized decisions protected

REJECTION CRITERIA:
- Score <54/60: AUTOMATIC REJECTION for voice contamination
- Missing source attribution: IMMEDIATE CORRECTION REQUIRED
- Mixed user/system content: SEPARATION VIOLATION - REJECT
- Paraphrased user quotes: VOICE CONTAMINATION - REJECT

OUTPUT: Detailed scoring + pass/fail determination + specific corrections needed"
```

## Final Quality Gates:

### Technical Validation:
- **Token economy**: Core file ≤80 líneas
- **Context metadata**: Complete decision tree
- **No duplication**: Unique vs existing docs
- **Links structure**: Conditional links vs imports

### Voice Preservation Validation (MANDATORY):
- **Voice separation**: Complete separation user voice vs system analysis
- **Quote accuracy**: Zero paraphrasing - exact user words only
- **Source attribution**: Every quote linked to original source
- **Immutability marking**: Crystallized decisions protected from evolution
- **Scoring compliance**: Voice preservation score ≥54/60 (90%+ required)
- **Contamination detection**: Zero voice contamination tolerance

### Content Validation:
- **User voice**: Exact quotes preserved with complete separation
- **Intent maintenance**: Original meaning intact without interpretation
- **Information density**: Maximum utility per token
- **Accessibility**: Clear navigation + structure

## Output Format:
```markdown
## 🎯 Document Verification Complete

### Quality Score: [X/100]
### Voice Preservation Score: [X/60] - MUST BE ≥54 FOR APPROVAL

### ✅ Passed Quality Gates:
- Token economy: [X lines] ✓
- Voice preservation: [X/60] ✓ (≥54 required)
- User voice separation: ✓ (Complete separation maintained)
- Quote accuracy: ✓ (Zero paraphrasing detected)
- Source attribution: ✓ (All quotes linked to sources)
- Immutability marking: ✓ (Crystallized decisions protected)
- No duplication: ✓
- Structure optimized: ✓

### 🔍 Voice Preservation Audit:
- **Quote Accuracy**: [X/10] - Exact words preserved
- **Intent Fidelity**: [X/10] - Original meaning maintained  
- **Context Completeness**: [X/10] - Full context preserved
- **Source Traceability**: [X/10] - Perfect source links
- **Attribution Clarity**: [X/10] - Complete user/system separation
- **Immutability Status**: [X/10] - Crystallized decisions protected

### 📊 Final Optimizations Applied:
- [optimization 1 applied]
- [optimization 2 applied]

### 🎁 Final Document:
[Documento final optimizado ready for production]

---
**STATUS**: ✅ WORKFLOW COMPLETE - Ready for deployment
```

## Workflow Completion Implementation:

```markdown
IMPORT: @/.claude/commands/utilities/workflow-state-manager.md

WORKFLOW STATE FINALIZATION:
1. RECEIVE workflow_id from align-doc step
2. LOAD complete workflow state
3. UPDATE current_step: 3 (final)
4. VALIDATE document progression chain
5. PREPARE for workflow completion

POST-VERIFICATION COMPLETION LOGIC:
IF quality_gates_passed AND no_major_issues:
  → UPDATE workflow state: "completed"
  → STORE final_document_path
  → LOG quality_scores and optimizations
  → DEPLOY document to target location
  → UPDATE handoff with new document available
  → NOTIFY user of successful workflow completion
  → CLEANUP workflow state (schedule for 24h deletion)
  
IF minor_issues_detected:
  → AUTO-FIX via Quality Assurance specialist
  → APPLY final optimizations
  → LOG fixes in workflow completion summary
  → PROCEED with deployment and completion
  
IF major_issues_require_rollback:
  → DETERMINE rollback target (align-doc or create-doc)
  → SET workflow state: "rolling_back_to_{target}"
  → PRESERVE all context for rollback step
  → AUTO-TRIGGER rollback to appropriate step
  → NOTIFY user of rollback with detailed reasoning
```

### Workflow Completion Task Implementation:
```markdown
SUCCESS COMPLETION TRIGGER:
Task: Workflow Completion Manager
Description: "Finalize document workflow and deploy"
Subagent: general-purpose
Prompt: "Complete document workflow:
- workflow_id: {workflow_id}
- final_document: {verified_document_path}
- quality_score: {final_quality_score}
- optimizations_applied: {optimization_log}
- deployment_target: {target_location}

Execute deployment, update handoff, notify user of completion."

ROLLBACK SCENARIO TRIGGER:
Task: Workflow Rollback Coordinator
Description: "Handle workflow rollback to previous step"
Subagent: general-purpose
Prompt: "Execute rollback to {target_step}:
- workflow_id: {workflow_id}
- rollback_reason: {major_issues_summary}
- preserved_context: {all_previous_work}
- target_command: /{target_step}

Maintain all user context and previous work."
```

## Success Criteria + Workflow Completion:
- [ ] Quality Assurance deployed via Task tool
- [ ] All quality gates passed (or minor issues auto-fixed)
- [ ] Final optimizations applied and logged
- [ ] Document deployed to target location
- [ ] Workflow state marked as completed
- [ ] Handoff updated with new document availability
- [ ] User notified of successful completion
- [ ] Workflow cleanup scheduled
- [ ] Rollback executed if major issues detected

---
**Workflow**: Create → Align → VERIFY ✅