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

### 4 Task Tools Concurrentes (MISMO MENSAJE)
**EJECUTAR OBLIGATORIO**:
```
Task 1: Research Specialist - "Edit best practices + change impact analysis"  
Task 2: Edit Specialist - "Document modification with voice preservation"
Task 3: Voice Preservation Specialist - "Pre/post-edit voice integrity validation"
Task 4: Architecture Reviewer - "System impact assessment + conflict detection"
```

## Edit Workflow State Management

### State Initialization
```yaml
workflow_id: "edit-{timestamp}"  
workflow_type: "document_edit"
target_document: "{file_path}"
original_voice_score: "{pre_edit_score}/60"
edit_requests: "{user_modifications_requested}"
rollback_point: "{original_document_backup}"
state: "editing"
```

### Change Tracking OBLIGATORIO
- **Pre-Edit Snapshot**: Complete document backup before any changes
- **Diff Generation**: Line-by-line change tracking with attribution
- **Voice Delta Analysis**: Voice score impact assessment
- **System Impact Log**: Architecture consistency validation results

## Specialist Deployment Specifications

### Research Specialist (TASK 1)
**Mission**: Edit methodology research + impact analysis
**Specialization**:
- Document edit best practices for {document_type}
- Change impact assessment methodology  
- Voice preservation during modification techniques
- Edit validation standards research
- System integration impact analysis

**Deliverable**: Comprehensive edit strategy with methodology recommendations

### Edit Specialist (TASK 2) - NEW SPECIALIST TYPE
**Mission**: Surgical document modification with voice preservation priority
**Specialization**:
- Document diff analysis and surgical editing
- User request interpretation while preserving existing voice
- Content modification maintaining structure and flow
- Change integration without voice contamination
- Technical accuracy during modifications

**CRITICAL REQUIREMENTS**:
- **Voice Preservation**: Maintain all existing user quotes EXACTLY
- **Surgical Precision**: Modify only requested sections
- **Structure Maintenance**: Preserve document organization
- **Integration Accuracy**: Ensure changes integrate seamlessly

**Deliverable**: Modified document with complete change documentation

### Voice Preservation Specialist (TASK 3) - MANDATORY
**Mission**: Voice integrity validation throughout edit process
**Specialization**:
- Pre-edit voice score validation (≥54/60 requirement)
- User voice element identification and protection
- Immutable decision preservation during edits
- Post-edit voice integrity verification
- Voice contamination detection and prevention

**CRITICAL VALIDATION**:
- **Immutable Elements**: Crystallized user decisions NEVER modified
- **Quote Preservation**: User quotes maintained EXACTLY
- **Source Attribution**: Complete traceability preserved
- **Voice Score Maintenance**: Score must remain ≥54/60

**Deliverable**: Voice preservation validation report with pre/post scores

### Architecture Reviewer (TASK 4)
**Mission**: System impact validation + conflict prevention
**Specialization**:
- Edit impact on command ecosystem analysis
- Integration point validation post-modification
- Conflict detection with existing rules/commands
- Metadata consistency maintenance
- Self-contained architecture compliance

**CRITICAL VALIDATION**:
- **System Consistency**: No conflicts with existing commands
- **Integration Points**: All references remain functional
- **Metadata Integrity**: Complete contextflow preservation
- **Architecture Compliance**: Self-contained principles maintained

**Deliverable**: System impact assessment with conflict resolution

## Auto-Chain Logic to `/align-edit`

### Success Criteria for Auto-Chain
```
IF edit_successful AND voice_preserved AND no_system_conflicts AND quality_acceptable:
    workflow_state = "aligning"  
    auto_chain_to_align_edit()
    preserve_edit_context()
```

### Conditional Logic
```
IF minor_issues_detected:
    auto_correct_issues()
    continue_to_align_edit()
ELIF major_issues_detected:
    execute_rollback()
    provide_user_guidance()
    pause_workflow_for_resolution()
```

### Context Preservation for Chain
- **Edit Changes**: Complete modification documentation
- **Voice Analysis**: Pre/post-edit voice scores
- **System Impact**: Architecture validation results
- **Quality Metrics**: Initial quality assessment scores

## Rollback Mechanism

### Automatic Rollback Triggers
- **Voice Score Drop**: Below 54/60 threshold
- **System Conflicts**: Architecture violations detected
- **Edit Failures**: Technical errors during modification
- **Quality Issues**: Major quality degradation

### Rollback Process
```
restore_from_rollback_point()
preserve_user_intent_for_retry()
generate_failure_analysis_report()
provide_corrective_guidance()
```

## Token Economy Enforcement

### Edit Scope Limits
- **Core Changes**: 50-80 lines maximum modification scope
- **Structure Preservation**: Maintain existing document organization
- **Voice Economy**: Preserve existing voice content, modify only necessary sections
- **Quality Focus**: Surgical precision over comprehensive rewrites

### Performance Optimization
- **Targeted Editing**: Focus modifications on requested sections only
- **Context Efficiency**: Minimize context usage during edits
- **Parallel Processing**: Leverage concurrent specialist deployment
- **Change Minimization**: Smallest possible modifications achieving goals

## Quality Gates for Auto-Chain

### Minimum Requirements
- ✅ **Voice Preservation**: Score ≥54/60 maintained
- ✅ **Edit Accuracy**: Requested changes successfully implemented
- ✅ **System Integrity**: No architecture conflicts introduced
- ✅ **Technical Quality**: Modified content meets quality standards

### Warning Thresholds
- ⚠️ **Voice Score 54-56**: Proceed with enhanced monitoring
- ⚠️ **Minor Conflicts**: Auto-correct and continue
- ⚠️ **Quality 70-84**: Flag for alignment phase attention

### Blocking Thresholds
- 🚫 **Voice Score <54**: Immediate rollback required
- 🚫 **Major Conflicts**: System integrity violations
- 🚫 **Quality <70**: Fundamental quality failure

## User Communication Protocol

### Success Path Communication
```
"Edit workflow iniciado para {document}. Specialists deployed for modification analysis and voice preservation validation. Auto-chaining to /align-edit upon completion."
```

### Issue Detection Communication  
```
"Edit workflow detectó {issue_type}. Applying auto-correction. Workflow will continue to alignment phase with enhanced monitoring."
```

### Failure Communication
```
"Edit workflow failed: {failure_reason}. Document restored to original state. User guidance: {corrective_steps}"
```

## Integration with Existing System

### Enforcement Mechanism Extension
- **Edit Blocking**: Direct Edit/MultiEdit operations redirected to this workflow
- **Violation Logging**: Edit bypass attempts logged in `/data/workflow-violations/`
- **User Guidance**: Clear redirection messages for direct edit attempts

### Workflow Continuity
- **State Management**: Complete edit workflow state preservation
- **Context Handoff**: Seamless transition to `/align-edit`
- **Quality Tracking**: Progressive quality score validation
- **Voice Monitoring**: Continuous voice preservation verification

---

**ESTE COMANDO INICIA** el workflow obligatorio para ALL document edits.
**AUTO-CHAIN SIGUIENTE**: `/align-edit` with complete context preservation.
**ROLLBACK AVAILABLE**: Automatic restoration on any critical failures.