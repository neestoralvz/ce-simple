---
contextflow:
  purpose: "Verificación final via Quality Assurance subagent"
  workflow-step: 3
  prev: ["align-doc"]
  workflow-complete: true
  requires-subagent: true
  research-driven: true
---

# Comando `/verify-doc` - Workflow Step 3 (Final)

## Subagent Orchestration OBLIGATORIA

**NUNCA hacer quality verification directamente** - SIEMPRE via Task tool con Quality Assurance specialist.

### Task Tools Deployment Paralelo (EJECUTAR INMEDIATAMENTE):

**DEPLOYMENT PATTERN**: 3 Task tools concurrentes para comprehensive final verification:

```python
# TASK 1: Quality Assurance Specialist (PRIMARY)
Task(
    description="Final quality verification and optimization",
    prompt="""Actúa como Quality Assurance Specialist. FINAL QUALITY MISSION: Complete document verification.

DOCUMENT INPUT:
- Aligned document: {aligned_document_content}
- Workflow context: {complete_workflow_state}
- Previous corrections: {alignment_corrections_log}
- Voice preservation status: {voice_integrity_status}

QUALITY VERIFICATION CHECKLIST:
1. Token Economy: Verify 50-80 líneas core máximo maintained
2. Context Loading: Metadata árbol decisiones complete + functional
3. Duplication Check: Verify uniqueness vs existing system documents
4. Structure Optimization: Headers, sections, navigation properly organized
5. Technical Accuracy: Syntax, references, imports fully validated
6. Readability Balance: Clarity maintained without losing information density
7. Integration Readiness: Document ready for production deployment
8. User Experience: Navigation, accessibility, findability optimized

FINAL QUALITY GATES:
- Overall Quality Score: [X/100] (minimum 85 required)
- Technical Compliance: All syntax, references validated
- Information Architecture: Optimal structure for user navigation
- Production Readiness: No blocking issues detected

OUTPUT: Complete quality assessment con final optimization recommendations.""",
    subagent_type="general-purpose"
)

# TASK 2: Voice Preservation Validator (MANDATORY ENFORCEMENT)
Task(
    description="MANDATORY final voice preservation validation with scoring",
    prompt="""Actúa como Voice Preservation Validator. ENFORCEMENT MISSION: Final voice preservation compliance.

VOICE PRESERVATION IMPERATIVES:
- Voice preservation score MUST be ≥54/60 (90% compliance)
- User voice and system analysis MUST be completely separated
- All user quotes MUST be exact with source attribution  
- Crystallized decisions MUST be marked as immutable
- ZERO voice contamination tolerance

FINAL VALIDATION INPUT:
- Document for validation: {final_document_content}
- Original user voice: {original_user_quotes}
- Voice tracking history: {voice_preservation_log}
- Previous voice score: {previous_voice_score}

SCORING MATRIX (MANDATORY - FINAL VALIDATION):
- Quote Accuracy [X/10]: Zero paraphrasing - exact user words only
- Intent Fidelity [X/10]: Original meaning maintained without interpretation
- Context Completeness [X/10]: Full situational context preserved
- Source Traceability [X/10]: Perfect links to original sources
- Attribution Clarity [X/10]: Complete separation user/system content
- Immutability Status [X/10]: Crystallized decisions protected

REJECTION CRITERIA (ZERO TOLERANCE):
- Score <54/60: AUTOMATIC REJECTION for voice contamination
- Missing source attribution: IMMEDIATE CORRECTION REQUIRED
- Mixed user/system content: SEPARATION VIOLATION - REJECT
- Paraphrased user quotes: VOICE CONTAMINATION - REJECT
- Modified crystallized decisions: IMMUTABILITY VIOLATION - REJECT

OUTPUT: Final voice preservation score + pass/fail determination + corrections needed (if any).""",
    subagent_type="general-purpose"
)

# TASK 3: Content Optimizer (FINAL OPTIMIZATION)
Task(
    description="Final token economy and structure optimization",
    prompt="""Actúa como Content Optimizer. FINAL OPTIMIZATION MISSION: Maximum efficiency for production.

OPTIMIZATION INPUT:
- Quality-verified document: {quality_validated_document}
- Token economy status: {current_token_count}
- Structure analysis: {current_structure_assessment}
- User experience requirements: Navigation, accessibility standards

FINAL OPTIMIZATION OBJECTIVES:
1. Token Economy: Achieve optimal density within 50-80 líneas core limit
2. Information Architecture: Maximum utility per token without losing clarity
3. Navigation Efficiency: Optimal headers, sections, cross-references
4. Context Loading: Metadata structure supports efficient loading
5. Production Polish: Final formatting, consistency, professional presentation
6. User Experience: Optimal readability + information accessibility

OPTIMIZATION TECHNIQUES:
- Density improvements without information loss
- Structure refinements for better navigation
- Metadata optimization for context loading
- Professional presentation polish
- Cross-reference optimization

OUTPUT: Final optimized document ready for production deployment.""",
    subagent_type="general-purpose"
)
```

**MAIN AGENT CONSOLIDATION**: Receive outputs from 3 specialists → Apply final optimizations → Generate production-ready document with complete quality + voice + optimization validation.

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
# WORKFLOW STATE MANAGER - EMBEDDED

**Self-Contained Workflow Management**:
- workflow_id finalization
- Complete state validation
- Deployment logic with rollback capability
- Success/failure handling

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

### Workflow Completion Task Implementation (EXECUTABLE):

```python
# SUCCESS COMPLETION SCENARIO
if quality_gates_passed and voice_score >= 54 and no_major_issues:
    # Update workflow state to completion
    workflow_state.update({
        "current_step": 3,
        "status": "completed",
        "final_document_path": verified_document_path,
        "quality_score": final_quality_score,
        "voice_preservation_score": final_voice_score,
        "completion_timestamp": current_timestamp
    })
    
    # WORKFLOW COMPLETION TASK
    Task(
        description="Finalize document workflow and deploy to production",
        prompt="""WORKFLOW COMPLETION MISSION: Deploy document and finalize workflow.

COMPLETION CONTEXT:
- workflow_id: {workflow_id}
- final_document: {verified_document_path}
- quality_score: {final_quality_score} (threshold: 85+)
- voice_preservation_score: {final_voice_score} (threshold: 54+)
- optimizations_applied: {final_optimization_log}
- deployment_target: {target_location}
- workflow_duration: {total_workflow_time}

COMPLETION ACTIONS:
1. Deploy document to target location
2. Update handoff with new document availability
3. Log workflow success metrics
4. Generate completion summary for user
5. Schedule workflow state cleanup (24h)
6. Update system documentation index

USER NOTIFICATION: Generate success summary with:
- Document deployed location
- Quality metrics achieved
- Voice preservation verification
- Next steps recommendations

EXECUTE: Complete workflow deployment and user notification.""",
        subagent_type="general-purpose"
    )

# MINOR ISSUES AUTO-FIX SCENARIO
elif minor_issues_detected and voice_score >= 54:
    Task(
        description="Auto-fix minor issues and complete workflow",
        prompt="""AUTO-FIX MISSION: Resolve minor issues and complete workflow.

MINOR ISSUES TO RESOLVE:
{minor_issues_list}

AUTO-FIX REQUIREMENTS:
- Maintain voice preservation score ≥54/60
- Preserve all user voice integrity
- Keep quality score ≥85/100
- Log all fixes for traceability

POST-FIX ACTION:
Complete workflow deployment with fixes applied + comprehensive fix log.

WORKFLOW CONTINUATION: Deploy corrected document and notify user of completion.""",
        subagent_type="general-purpose"
    )

# ROLLBACK SCENARIO - MAJOR ISSUES
else:
    rollback_target = determine_rollback_target(major_issues_summary)
    workflow_state.update({
        "status": "rolling_back",
        "rollback_target": rollback_target,
        "rollback_reason": major_issues_summary,
        "user_intervention_required": true
    })
    
    Task(
        description="Handle workflow rollback to previous step",
        prompt="""ROLLBACK MISSION: Return workflow to previous step for correction.

ROLLBACK CONTEXT:
- workflow_id: {workflow_id}
- rollback_target: /{rollback_target}
- rollback_reason: {major_issues_summary}
- preserved_context: {complete_workflow_history}
- quality_issues: {quality_failure_details}
- voice_issues: {voice_preservation_failures}

ROLLBACK ACTIONS:
1. Preserve all user context and previous work
2. Reset workflow state to target step
3. Prepare detailed issue summary for user
4. Maintain voice preservation throughout rollback
5. Clear error conditions for fresh step execution

USER COMMUNICATION: Explain:
- Why rollback was necessary
- What will be preserved
- What corrections are needed
- How to proceed

EXECUTE: Rollback to /{rollback_target} with complete context preservation.""",
        subagent_type="general-purpose"
    )
```

## Success Criteria + Workflow Completion (AUTOMATED VALIDATION):

**SPECIALIST DEPLOYMENT VALIDATION**:
- [x] 3 Task tools deployed concurrently (Quality Assurance, Voice Preservation Validator, Content Optimizer)
- [x] Quality Assurance Specialist deployment (PRIMARY - comprehensive verification)
- [x] Voice Preservation Validator deployment (MANDATORY - final enforcement)
- [x] Content Optimizer deployment (Final polish + production readiness)

**QUALITY VERIFICATION** (Auto-verified by Quality Assurance Specialist):
- [x] Quality score ≥85/100 (Production readiness threshold)
- [x] Token economy compliance (50-80 líneas core maintained)
- [x] Technical accuracy verified (Syntax, references, imports validated)
- [x] Structure optimization complete (Headers, sections, navigation)
- [x] No duplication detected (Uniqueness vs existing documents verified)
- [x] Context loading optimized (Metadata supports efficient loading)

**VOICE PRESERVATION FINAL ENFORCEMENT** (Auto-verified by Voice Preservation Validator):
- [x] Voice preservation score ≥54/60 (MANDATORY 90%+ compliance)
- [x] User voice completely separated (ZERO contamination detected)
- [x] All user quotes exact with source attribution (NO paraphrasing)
- [x] Crystallized decisions marked immutable (PROTECTED status verified)
- [x] Source traceability complete (Perfect links to original sources)
- [x] Attribution clarity maintained (Complete user/system separation)

**FINAL OPTIMIZATION** (Auto-verified by Content Optimizer):
- [x] Token efficiency maximized (Optimal density without information loss)
- [x] Information architecture optimized (Maximum utility per token)
- [x] Navigation efficiency achieved (Optimal structure for user experience)
- [x] Production polish applied (Professional presentation + consistency)
- [x] Cross-reference optimization complete (Functional linking throughout)

**WORKFLOW COMPLETION** (Auto-managed):
- [x] Document deployed to target location (Production ready)
- [x] Workflow state marked as completed (Success metrics logged)
- [x] Handoff updated with new document availability (System index updated)
- [x] User notified of successful completion (Comprehensive summary provided)
- [x] Workflow cleanup scheduled (24h automatic cleanup)
- [x] Rollback executed if major issues detected (Context preservation maintained)

**COMPLETION EXECUTION LOGIC**:
```python
if quality_score >= 85 and voice_score >= 54 and no_major_issues:
    deploy_document_and_complete_workflow()
elif minor_issues_only and voice_score >= 54:
    auto_fix_issues_and_complete_workflow()
else:
    execute_rollback_to_appropriate_step()
```

---
**Workflow**: Create → Align → VERIFY ✅