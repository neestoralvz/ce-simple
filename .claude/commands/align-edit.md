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

## Multi-Specialist Orchestration OBLIGATORIA

### 4 Task Tools Concurrentes (MISMO MENSAJE)
**EJECUTAR OBLIGATORIO**:
```
Task 1: Architecture Validator - "Edit consistency + system impact validation"
Task 2: Research Specialist - "Edit alignment best practices + optimization"  
Task 3: Voice Preservation Validator - "Voice integrity + contamination detection"
Task 4: Change Impact Analyzer - "Downstream effects + dependency validation"
```

## Workflow State Continuation

### State Validation OBLIGATORIA
```yaml
workflow_validation:
  prerequisite_state: "editing"
  required_context: ["edit_changes", "voice_analysis", "system_impact", "quality_metrics"]
  continuation_state: "aligning"
  auto_chain_target: "/verify-edit"
```

### Context Requirements
- **Edit Documentation**: Complete change log from `/edit-doc`
- **Voice Analysis**: Pre/post-edit voice scores
- **System Impact**: Architecture validation results
- **Quality Baseline**: Initial edit quality assessment

## Specialist Deployment Specifications

### Architecture Validator (TASK 1) - ENHANCED FOR EDITS
**Mission**: Edit consistency with system architecture validation
**Edit-Specific Specialization**:
- Modified content system integration validation
- Edit impact on command ecosystem assessment
- Cross-reference consistency after modifications
- Self-contained architecture compliance verification
- Integration point functionality validation

**Enhanced Validation Criteria**:
- **Command Ecosystem**: No disruption to existing commands
- **Reference Integrity**: All internal references remain functional
- **Metadata Consistency**: Contextflow and system metadata preserved
- **Architecture Standards**: Self-contained principles maintained

**Deliverable**: Complete architecture consistency report with conflict resolution

### Research Specialist (TASK 2)
**Mission**: Edit alignment best practices + optimization research
**Specialization**:
- Edit alignment methodology research (current date: $(date))
- Change management best practices for document workflows
- Post-edit optimization patterns and standards
- Quality improvement techniques for modified content
- Industry standards for edit validation processes

**Research Focus**:
- **Edit Quality Standards**: Current industry benchmarks
- **Alignment Methodologies**: Proven edit validation approaches
- **Optimization Techniques**: Performance and quality improvements
- **Best Practice Integration**: Modern edit workflow standards

**Deliverable**: Research-driven optimization recommendations for edit quality

### Voice Preservation Validator (TASK 3) - CRITICAL
**Mission**: Voice integrity validation + contamination detection
**Critical Validation**:
- **Voice Score Verification**: Must maintain ≥54/60 threshold
- **Edit Impact Assessment**: How modifications affected voice elements
- **Contamination Detection**: New content voice consistency validation
- **Immutable Element Protection**: Crystallized decisions preservation check
- **Source Attribution Integrity**: Complete traceability maintenance

**Enhanced Edit Validation**:
- **Voice Delta Analysis**: Pre/post-edit voice score comparison
- **Content Integration**: New content voice synthesis validation
- **Preservation Accuracy**: Existing voice element protection verification
- **Quality Maintenance**: Voice quality standards throughout modifications

**CRITICAL THRESHOLDS**:
- **Minimum Voice Score**: ≥54/60 (BLOCKING if below)
- **Voice Contamination**: Zero tolerance for voice mixing
- **Attribution Accuracy**: 100% source traceability required

**Deliverable**: Comprehensive voice preservation validation with score analysis

### Change Impact Analyzer (TASK 4) - NEW SPECIALIST
**Mission**: Downstream effects + dependency validation
**Specialized Analysis**:
- **Dependency Chain Impact**: How edits affect related documents/commands
- **Performance Impact Assessment**: Modifications effect on system performance
- **Integration Point Analysis**: Impact on cross-system references
- **Rollback Requirement Evaluation**: Change reversibility assessment
- **Quality Propagation**: How edits affect connected content quality

**Critical Analysis Areas**:
- **System Dependencies**: Impact on commands, templates, workflows
- **Document Relationships**: Effect on related documentation
- **Performance Implications**: Resource usage and efficiency changes
- **Maintenance Impact**: Future maintenance complexity assessment

**Deliverable**: Complete change impact analysis with risk assessment

## Auto-Correction Protocol

### Minor Issue Auto-Correction
**Triggers**: Non-critical issues that don't affect core functionality
- **Formatting inconsistencies**: Auto-correct to system standards
- **Minor reference updates**: Automatic cross-reference alignment
- **Metadata synchronization**: Contextflow metadata updates
- **Performance optimizations**: Automatic efficiency improvements

### Auto-Correction Process
```
detect_minor_issues()
apply_automatic_corrections()
validate_correction_success()
continue_workflow_chain()
log_auto_corrections_applied()
```

## Major Issue Resolution Protocol

### Major Issue Detection
**Blocking Conditions**:
- **Voice Score Drop**: Below 54/60 threshold
- **Architecture Violations**: System integrity compromised
- **Critical Dependencies**: Essential functionality broken
- **Quality Degradation**: Fundamental quality standards not met

### Resolution Process
```
IF major_issues_detected:
    pause_workflow()
    generate_issue_report()
    provide_resolution_options()
    await_user_decision()
    IF user_chooses_rollback:
        execute_rollback_to_edit_phase()
    ELIF user_chooses_manual_fix:
        provide_specific_guidance()
        resume_workflow_after_fixes()
```

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