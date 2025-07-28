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

## Multi-Specialist Orchestration OBLIGATORIA

### 3 Task Tools Concurrentes (MISMO MENSAJE)
**EJECUTAR OBLIGATORIO**:
```
Task 1: Quality Assurance Specialist - "Final quality gates + production readiness"
Task 2: Voice Preservation Validator - "Voice integrity final confirmation"  
Task 3: Change Verification Specialist - "Edit completion + deployment validation"
```

## Workflow State Completion

### State Validation OBLIGATORIA
```yaml
workflow_completion:
  prerequisite_state: "aligning"
  required_context: ["alignment_results", "issue_resolution", "quality_metrics", "voice_validation"]
  completion_state: "verified"
  deployment_ready: true
```

### Final Context Requirements
- **Alignment Results**: Complete validation outcomes from `/align-edit`
- **Issue Resolution**: Any corrections applied during alignment
- **Quality Evolution**: Progressive quality scores through workflow
- **Voice Analysis**: Complete voice preservation tracking

## Specialist Deployment Specifications

### Quality Assurance Specialist (TASK 1) - ENHANCED FOR EDITS
**Mission**: Final quality gates + production readiness validation
**Edit Quality Specialization**:
- **Quality Score Validation**: Must achieve ≥85/100 for production deployment
- **Edit Integration Quality**: How well modifications integrate with existing content
- **Technical Accuracy**: Correctness of all modified content
- **Production Readiness**: Complete deployment preparation validation
- **Change Quality Assessment**: Quality of modifications vs original content

**Enhanced Quality Criteria**:
- **Content Accuracy**: Technical correctness of all edits
- **Integration Quality**: Seamless blending with existing content
- **Structure Integrity**: Document organization maintained
- **Performance Impact**: Edit efficiency and resource usage

**QUALITY THRESHOLDS**:
- **Minimum Score**: ≥85/100 (BLOCKING if below)
- **Integration Quality**: Seamless content blending required
- **Technical Accuracy**: 100% correctness required
- **Production Ready**: Complete deployment validation

**Deliverable**: Final quality assessment with production deployment approval

### Voice Preservation Validator (TASK 2) - FINAL CONFIRMATION
**Mission**: Voice integrity final confirmation + contamination final check
**Final Voice Validation**:
- **Voice Score Confirmation**: Final ≥54/60 verification
- **Edit Voice Integration**: New content voice consistency validation
- **Preservation Accuracy**: Complete voice element protection verification
- **Contamination Final Check**: Zero voice mixing tolerance verification
- **Attribution Integrity**: Complete source traceability confirmation

**Final Voice Analysis**:
- **Score Progression**: Pre-edit → Post-edit → Post-align → Final score
- **Integration Success**: New content voice synthesis quality
- **Preservation Success**: Existing voice element protection validation
- **Quality Maintenance**: Voice quality standards throughout entire workflow

**FINAL VOICE REQUIREMENTS**:
- **Final Score**: ≥54/60 (MANDATORY for deployment)
- **Zero Contamination**: Perfect voice preservation confirmed
- **Complete Attribution**: 100% source traceability maintained
- **Quality Consistency**: Voice quality maintained throughout edits

**Deliverable**: Final voice preservation certification with score confirmation

### Change Verification Specialist (TASK 3) - NEW SPECIALIST
**Mission**: Edit completion validation + deployment preparation
**Change Verification Specialization**:
- **Edit Completion**: All requested changes successfully implemented
- **Change Accuracy**: Modifications match user requirements exactly
- **Integration Success**: Changes properly integrated with existing content
- **Deployment Readiness**: Complete preparation for production deployment
- **Change Documentation**: Complete modification audit trail

**Critical Verification Areas**:
- **Requirement Fulfillment**: User edit requests completely satisfied
- **Implementation Accuracy**: Changes implemented correctly
- **System Integration**: Modified document system compatibility
- **Deployment Preparation**: Complete production readiness

**VERIFICATION REQUIREMENTS**:
- **Complete Implementation**: 100% of requested changes made
- **Accuracy Validation**: Changes match requirements exactly
- **Integration Success**: Seamless system compatibility
- **Deployment Ready**: Production deployment approved

**Deliverable**: Complete change verification with deployment authorization

## Production Deployment Protocol

### Deployment Readiness Validation
**All Criteria Must Pass**:
- ✅ **Quality Score**: ≥85/100 achieved
- ✅ **Voice Preservation**: ≥54/60 maintained
- ✅ **Change Completion**: All edits implemented correctly
- ✅ **System Integration**: Full compatibility confirmed
- ✅ **Technical Accuracy**: 100% correctness verified

### Automatic Deployment Process
```
IF all_quality_gates_pass:
    finalize_edited_document()
    update_system_references()
    cleanup_workflow_state()
    generate_completion_report()
    deploy_to_production()
```

### Deployment Actions
- **Document Finalization**: Apply final edits to production document
- **Reference Updates**: Update all system cross-references
- **Metadata Synchronization**: Complete contextflow metadata updates
- **Audit Trail Completion**: Finalize complete change documentation

## Rollback Scenarios - FINAL OPPORTUNITY

### Critical Failure Rollback
**Triggers**: Unresolvable quality or voice issues
- **Quality Score <85**: Fundamental quality failure
- **Voice Score <54**: Voice preservation failure
- **Critical System Issues**: Unresolvable architecture conflicts
- **Implementation Failures**: Unable to complete requested changes

### Final Rollback Process
```
IF critical_failures_detected:
    preserve_verification_analysis()
    determine_rollback_target()
    IF voice_issues: rollback_to_edit_phase()
    IF quality_issues: rollback_to_alignment_phase()
    IF system_issues: complete_workflow_rollback()
    provide_comprehensive_failure_analysis()
```

## Workflow Completion & Documentation

### Completion Documentation
- **Edit Summary**: Complete change documentation
- **Quality Progression**: Quality scores throughout workflow
- **Voice Analysis**: Voice preservation success tracking
- **System Impact**: Final architecture impact assessment
- **Performance Metrics**: Workflow execution efficiency

### Change Audit Trail
```yaml
edit_completion_record:
  workflow_id: "{edit_workflow_id}"
  document_target: "{edited_document_path}"
  edit_requests: "{original_user_requests}"
  changes_implemented: "{detailed_change_log}"
  quality_progression: "{quality_scores_throughout}"
  voice_preservation: "{voice_scores_throughout}"
  completion_timestamp: "{deployment_timestamp}"
  specialist_validations: "{all_specialist_reports}"
```

## Performance Optimization

### Verification Efficiency
- **Parallel Processing**: 3 concurrent specialist deployment
- **Targeted Validation**: Focus on critical verification areas
- **Quick Deployment**: Streamlined production deployment process
- **Resource Optimization**: Efficient final validation resource usage

### Quality Assurance
- **Comprehensive Testing**: Complete edit validation
- **Performance Monitoring**: Verification phase timing optimization
- **Quality Metrics**: Detailed quality assessment documentation
- **Success Tracking**: Verification success rate monitoring

## User Communication Protocol

### Successful Verification Communication
```
"Edit verification completed successfully. Quality: {quality_score}/100, Voice: {voice_score}/60. Document deployed to production. Edit workflow complete."
```

### Quality Issues Communication
```
"Edit verification detected quality issues: {issue_details}. Current score: {quality_score}/100 (minimum 85 required). Workflow paused for resolution."
```

### Complete Failure Communication
```
"Edit verification failed: {failure_reason}. Rollback initiated to {rollback_target}. Analysis: {failure_analysis}. Recommended resolution: {guidance}"
```

## Integration with System Monitoring

### Success Metrics Tracking
- **Edit Success Rate**: Percentage of edits completing successfully
- **Quality Achievement**: Average quality scores for completed edits
- **Voice Preservation**: Voice score maintenance statistics
- **Workflow Efficiency**: Average time from edit to deployment

### System Evolution Input
- **Edit Pattern Analysis**: Common edit types and success patterns
- **Quality Improvement**: Trends in edit quality over time
- **Voice Preservation Trends**: Voice score evolution analysis
- **System Optimization**: Edit workflow performance improvements

---

**ESTE COMANDO COMPLETA** el edit workflow con production deployment.
**WORKFLOW FINALIZADO**: Document successfully edited and deployed.
**AUDIT TRAIL**: Complete change documentation preserved.