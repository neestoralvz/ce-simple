---
contextflow:
  purpose: "Alineamiento documento via Architecture Validator subagent"
  workflow-step: 2
  prev: ["create-doc"]
  next: ["verify-doc"]
  requires-subagent: true
  auto-chain: true
---

# Comando `/align-doc` - Workflow Step 2

## Subagent Orchestration OBLIGATORIA

**NUNCA validar alignment directamente** - SIEMPRE via Task tool con Architecture Validator.

### Task Tools Deployment Paralelo (EJECUTAR INMEDIATAMENTE):

**DEPLOYMENT PATTERN**: 4 Task tools concurrentes para comprehensive alignment validation:

```python
# TASK 1: Architecture Validator (PRIMARY)
Task(
    description="Validate consistency with core system architecture",
    prompt="""Actúa como Architecture Validator. MISSION: Ensure document integrates seamlessly con sistema core.

DOCUMENT INPUT:
- Current document: {document_content}
- Document type: {document_type}
- Creation context: {create_doc_output}
- Workflow state: {workflow_context}

ARCHITECTURE CONSISTENCY VALIDATION:
1. System Integration: Check conflicts con commands/rules existentes
2. Contextflow Metadata: Verify complete + accurate headers
3. Decision Tree Logic: Validate semantic triggers, alternatives, next steps
4. Import References: Verify all @/ imports are valid
5. Navigation Structure: Ensure proper linking + cross-references
6. Naming Conventions: Validate consistency con sistema standards

CONFLICT DETECTION:
- Duplicate functionality identification
- Contradictory rule/command patterns
- Integration point failures
- Metadata inconsistencies

OUTPUT: Detailed alignment report con specific corrections needed.""",
    subagent_type="general-purpose"
)

# TASK 2: Research Specialist
Task(
    description="Benchmark alignment practices and anti-patterns",
    prompt="""Actúa como Research Specialist. BENCHMARK MISSION: Research alignment best practices.

RESEARCH SCOPE:
- Document type: {document_type}
- Current alignment issues: {preliminary_issues}
- System architecture: CE-Simple ecosystem patterns
- Integration context: Multi-subagent workflows

RESEARCH OBJECTIVES:
1. Alignment best practices para {document_type}
2. Common anti-patterns in document integration
3. Token economy optimization during alignment
4. Voice preservation during corrections methodology  
5. Workflow continuity patterns post-alignment

BENCHMARK ANALYSIS:
- Industry standards para document alignment
- System-specific optimization patterns
- Error prevention methodologies
- Quality assurance integration points

OUTPUT: Benchmarked recommendations para optimal alignment approach.""",
    subagent_type="general-purpose"
)

# TASK 3: Voice Preservation Specialist
Task(
    description="Verify user voice maintained through alignment",
    prompt="""Actúa como Voice Preservation Specialist. PRESERVATION MISSION: Maintain voice integrity during alignment.

VOICE INTEGRITY ANALYSIS:
- Original document: {original_document}
- Proposed changes: {architecture_validator_corrections}
- User voice elements: {extracted_user_quotes}
- Voice preservation score: {current_voice_score}

VOICE PRESERVATION VALIDATION:
1. Quote Integrity: Verify NO user quotes modified during alignment
2. Intent Preservation: Ensure user decisions remain unchanged
3. Source Attribution: Maintain complete source linkage
4. Immutability Protection: Verify crystallized decisions untouched
5. Separation Maintenance: User voice vs system analysis boundaries
6. Score Validation: Ensure voice score remains ≥54/60

ALIGNMENT IMPACT ASSESSMENT:
- Which corrections affect user voice content?
- How to apply corrections without voice contamination?
- Protection mechanisms for immutable user decisions
- Voice score impact of proposed changes

OUTPUT: Voice-safe alignment recommendations con preservation verification.""",
    subagent_type="general-purpose"
)

# TASK 4: Content Optimizer
Task(
    description="Check token economy and structure compliance",
    prompt="""Actúa como Content Optimizer. OPTIMIZATION MISSION: Maintain efficiency during alignment.

OPTIMIZATION SCOPE:
- Document content: {document_with_corrections}
- Token economy target: 50-80 líneas core máximo
- Structure requirements: Headers, sections, navigation
- Efficiency metrics: Information density per token

CONTENT OPTIMIZATION ANALYSIS:
1. Token Economy: Verify corrections don't exceed 80-line limit
2. Information Density: Ensure maximum utility per token maintained
3. Structure Clarity: Headers, sections properly organized post-corrections
4. Navigation Efficiency: Links, references optimized
5. Readability Balance: Clarity without losing information density
6. Context Loading: Metadata supports efficient context loading

OPTIMIZATION RECOMMENDATIONS:
- Token reduction opportunities without information loss
- Structure improvements for better navigation
- Efficiency gains through better organization
- Context loading optimizations

OUTPUT: Optimized document version con efficiency metrics validated.""",
    subagent_type="general-purpose"
)
```

**MAIN AGENT CONSOLIDATION**: Receive outputs from 4 specialists → Apply corrections while preserving voice → Generate aligned document ready for verification.

## Alignment Verification:
- **Consistency check**: Principles, decisions, architecture
- **Integration validation**: No conflicts con sistema existente
- **User voice preservation**: Intent maintenance sin distorsión
- **Standards compliance**: Token economy + context loading

## Output Format:
```markdown
## Alignment Validation Results

### ✅ Aligned Correctly:
- [aspecto 1 correcto]
- [aspecto 2 correcto]

### ⚠️ Alignment Issues:
- **Issue 1**: [descripción] → [correction needed]
- **Issue 2**: [descripción] → [correction needed]

### 🔄 Corrections Applied:
[Documento corregido con changes tracked]

---
**Status**: Ready for `/verify-doc` - Quality validation
```

## Auto-Chaining Implementation:

```markdown
IMPORT: @/.claude/commands/utilities/workflow-state-manager.md

WORKFLOW STATE CONTINUATION:
1. RECEIVE workflow_id from create-doc step
2. LOAD existing workflow state
3. UPDATE current_step: 2
4. VALIDATE document_path continuity
5. PRESERVE user_context throughout alignment

POST-ALIGNMENT AUTO-CHAIN LOGIC:
IF alignment_validation_success AND no_major_issues:
  → UPDATE workflow state (step 2 completed)
  → STORE aligned_document_path
  → STORE validation_results for next step
  → AUTO-EXECUTE: Task tool with verify-doc command
  → PASS: workflow_id + aligned_document + validation_context
  
IF minor_issues_found:
  → AUTO-APPLY corrections via subagent
  → UPDATE document with corrections
  → LOG corrections in workflow state
  → CONTINUE auto-chain to verify-doc with corrected document
  
IF major_conflicts_detected:
  → SET error_state: "major_alignment_conflict"
  → PAUSE auto-chain progression
  → REQUIRE user decision for conflict resolution
  → PRESERVE state for potential rollback to create-doc
```

### Auto-Chain Task Tool Implementation (EXECUTABLE):

```python
# ALIGNMENT SUCCESS AUTO-CHAIN
if alignment_validation_success and no_major_issues:
    # Update workflow state
    workflow_state.update({
        "current_step": 2,
        "status": "completed", 
        "aligned_document_path": aligned_document_path,
        "validation_results": validation_summary,
        "corrections_applied": corrections_log
    })
    
    # AUTO-CHAIN TO VERIFY-DOC
    Task(
        description="Auto-chain workflow to verify-doc step",
        prompt="""Execute /verify-doc command con complete workflow context.

WORKFLOW STATE HANDOFF:
- workflow_id: {workflow_id}
- document_path: {aligned_document_path}
- alignment_results: {validation_summary}
- corrections_applied: {corrections_log}
- voice_preservation_status: {voice_integrity_maintained}
- optimization_results: {content_optimizer_output}
- user_context: {preserved_original_context}
- auto_chain_enabled: true

EXECUTE: /verify-doc command for final quality validation.

QUALITY MISSION: Apply final quality gates while maintaining alignment and voice preservation.""",
        subagent_type="general-purpose"
    )

# MINOR ISSUES AUTO-CORRECTION
elif minor_issues_found:
    Task(
        description="Apply minor corrections and continue workflow",
        prompt="""Apply minor alignment corrections and continue auto-chain.

MINOR CORRECTIONS TO APPLY:
{minor_issues_list}

CORRECTION REQUIREMENTS:
- Preserve user voice integrity (NO quote modifications)
- Maintain token economy efficiency  
- Keep architecture validation compliance
- Log all corrections for traceability

POST-CORRECTION ACTION:
Auto-chain to /verify-doc with corrected document + correction log.

WORKFLOW CONTINUATION: Maintain all context for seamless verification step.""",
        subagent_type="general-purpose"
    )
    
# MAJOR CONFLICTS - PAUSE WORKFLOW
else:
    workflow_state.update({
        "status": "major_alignment_conflict",
        "conflict_details": major_issues_summary,
        "auto_chain_paused": true,
        "user_intervention_required": true
    })
    # Pause auto-chain for user decision
```

## Success Criteria + Auto-Chain Triggers (AUTOMATED VALIDATION):

**SPECIALIST DEPLOYMENT VALIDATION**:
- [x] 4 Task tools deployed concurrently (Architecture, Research, Voice Preservation, Content Optimizer)
- [x] Architecture Validator deployment (PRIMARY - system integration focus)
- [x] Voice Preservation Specialist deployment (MANDATORY - maintain voice integrity)
- [x] Content Optimizer deployment (Token economy + structure maintenance)

**ALIGNMENT VALIDATION** (Auto-verified by Architecture Validator):
- [x] System consistency verified (NO conflicts detected)
- [x] Contextflow metadata validated (Complete + accurate)
- [x] Decision tree logic verified (Semantic triggers, alternatives, next steps)
- [x] Import references validated (All @/ imports functional)
- [x] Navigation structure optimized (Proper linking + cross-references)

**VOICE PRESERVATION DURING ALIGNMENT** (Auto-verified by Voice Preservation Specialist):
- [x] User voice preserved through corrections (ZERO quote modifications)
- [x] Intent preservation verified (User decisions unchanged)
- [x] Source attribution maintained (Complete linkage preserved)
- [x] Immutability protection verified (Crystallized decisions untouched)
- [x] Voice score maintained ≥54/60 (Post-alignment verification)

**OPTIMIZATION VALIDATION** (Auto-verified by Content Optimizer):
- [x] Token economy maintained (50-80 líneas core limit)
- [x] Information density preserved (Maximum utility per token)
- [x] Structure clarity maintained (Headers, sections, navigation)
- [x] Context loading optimized (Efficient metadata structure)

**WORKFLOW ORCHESTRATION** (Auto-managed):
- [x] Workflow state updated with alignment results
- [x] Document corrections logged for traceability  
- [x] Auto-chain to verify-doc triggered (CONDITIONAL on success)
- [x] Context handoff prepared (All specialist outputs + corrections preserved)

**AUTO-CHAIN EXECUTION LOGIC**:
```python
if alignment_success and no_major_conflicts and voice_preserved:
    trigger_auto_chain_to_verify_doc()
elif minor_issues_only:
    auto_correct_and_continue_chain()
else:
    pause_workflow_for_user_intervention()
```

---
**Workflow**: Create → ALIGN → Verify