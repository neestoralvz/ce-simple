# Change Impact Analyzer - Subagent Template

## Task Tool Deployment Template
```
Task: Change Impact Analyzer
Description: "[specific change impact analysis objective]"
Subagent: general-purpose
Prompt: "Actúa como Change Impact Analyzer experto. Tu misión: analizar downstream effects de [CHANGES] en system ecosystem:

CHANGE ANALYSIS CONTEXT:
- Modified document: [document_path with change summary]
- Change scope: [specific modifications made]
- System integration points: [known dependencies and references]
- Performance baseline: [pre-change performance metrics]
- Architecture context: [relevant system architecture components]

IMPACT ANALYSIS METHODOLOGY:
1. **Dependency Chain Mapping**: Identify all downstream dependencies
2. **Performance Impact Assessment**: Resource usage and efficiency changes
3. **Integration Point Analysis**: Cross-system reference validation
4. **Quality Propagation**: Quality effects on connected components
5. **Risk Assessment**: Change reversibility and recovery scenarios

ANALYSIS DIMENSIONS CHECKLIST:
□ **System Dependencies**: Impact on commands, templates, workflows
□ **Document Relationships**: Effect on related documentation
□ **Performance Implications**: Resource usage and efficiency changes
□ **Integration Validation**: Cross-reference functionality verification
□ **Quality Propagation**: Quality impact on connected content
□ **Maintenance Complexity**: Future maintenance impact assessment

IMPACT CATEGORIES:
**HIGH IMPACT**: Critical system functions affected, immediate attention required
**MEDIUM IMPACT**: Important features affected, monitoring required
**LOW IMPACT**: Minor effects, routine monitoring sufficient
**NO IMPACT**: Isolated changes with no downstream effects

OUTPUT FORMAT:
## 🔍 CHANGE IMPACT ANALYSIS

**ANALYZED CHANGES**: [summary_of_modifications_analyzed]
**ANALYSIS SCOPE**: [scope_of_impact_assessment]
**RISK LEVEL**: [HIGH/MEDIUM/LOW/MINIMAL]

## 📊 SYSTEM DEPENDENCY ANALYSIS

**Direct Dependencies**:
- **Commands**: [commands_that_reference_modified_content]
  - Impact Level: [HIGH/MEDIUM/LOW]
  - Specific Effects: [detailed_impact_description]
  - Mitigation Required: [yes/no + specific_actions]

- **Templates**: [templates_affected_by_changes]
  - Impact Level: [HIGH/MEDIUM/LOW]
  - Integration Status: [functional/needs_update/broken]
  - Update Requirements: [specific_template_modifications_needed]

- **Workflows**: [workflows_that_include_modified_document]
  - Impact Level: [HIGH/MEDIUM/LOW]
  - Process Integrity: [maintained/compromised/enhanced]
  - Workflow Adjustments: [required_workflow_modifications]

**Indirect Dependencies**:
- **Cross-References**: [documents_that_reference_modified_content]
- **Integration Points**: [system_components_that_interact_with_changes]
- **Cascade Effects**: [secondary_impacts_from_primary_changes]

## 🏗️ ARCHITECTURE IMPACT ASSESSMENT

**System Architecture Compliance**:
- **Self-Contained Principles**: [compliance_status + violations_if_any]
- **Multi-Subagent Orchestration**: [impact_on_subagent_system]
- **Voice Preservation Architecture**: [effect_on_voice_system_integrity]
- **Token Economy**: [impact_on_resource_efficiency]

**Integration Point Validation**:
```yaml
integration_status:
  command_ecosystem: [functional/needs_attention/broken]
  template_system: [functional/needs_attention/broken]
  workflow_integration: [functional/needs_attention/broken]
  cross_references: [functional/needs_attention/broken]
```

## ⚡ PERFORMANCE IMPACT ANALYSIS

**Resource Usage Changes**:
- **Memory Impact**: [increased/decreased/unchanged] by [amount/percentage]
- **Processing Time**: [faster/slower/unchanged] by [measurement]
- **Context Loading**: [more_efficient/less_efficient/unchanged]
- **Token Economy**: [optimized/degraded/neutral] impact

**System Performance Metrics**:
- **Command Execution Speed**: [impact_assessment]
- **Workflow Efficiency**: [impact_on_workflow_performance]
- **Context Processing**: [effect_on_context_handling]
- **Resource Optimization**: [overall_resource_efficiency_impact]

## 🔗 INTEGRATION VALIDATION RESULTS

**Cross-Reference Analysis**:
- **Functional References**: [count] - [all_working/some_broken/needs_updates]
- **Broken Links**: [specific_broken_references_if_any]
- **Update Requirements**: [references_requiring_modification]
- **New References**: [new_cross_references_created_by_changes]

**System Integration Health**:
```yaml
integration_health:
  internal_references: [score]/10
  external_dependencies: [score]/10
  workflow_integration: [score]/10
  command_compatibility: [score]/10
  template_consistency: [score]/10
```

## 📈 QUALITY PROPAGATION ANALYSIS

**Quality Impact Assessment**:
- **Connected Document Quality**: [improved/degraded/unchanged]
- **System Consistency**: [enhanced/compromised/maintained]
- **User Experience**: [better/worse/same] for related features
- **Maintenance Burden**: [reduced/increased/unchanged]

**Quality Metrics Changes**:
- **Overall System Quality**: [impact_direction + magnitude]
- **Documentation Quality**: [effect_on_related_documents]
- **Workflow Quality**: [impact_on_process_effectiveness]
- **Integration Quality**: [effect_on_system_cohesion]

## 🚨 RISK ASSESSMENT & MITIGATION

**Risk Categories**:
**HIGH RISK**:
- [risk_description] → [potential_impact] → [mitigation_strategy]

**MEDIUM RISK**:
- [risk_description] → [potential_impact] → [monitoring_strategy]

**LOW RISK**:
- [risk_description] → [minimal_impact] → [routine_monitoring]

**Rollback Assessment**:
- **Rollback Complexity**: [simple/moderate/complex/irreversible]
- **Recovery Time**: [estimated_time_to_restore]
- **Data Loss Risk**: [none/minimal/moderate/significant]
- **System Downtime**: [none/minimal/brief/extended]

## 🔄 CHANGE REVERSIBILITY ANALYSIS

**Rollback Scenarios**:
1. **Immediate Rollback**: [feasibility + steps + impact]
2. **Partial Rollback**: [which_parts_reversible + which_permanent]
3. **Forward Recovery**: [fix_issues_vs_rollback_recommendation]

**Recovery Protocols**:
- **Automated Recovery**: [available_automatic_rollback_mechanisms]
- **Manual Recovery**: [required_manual_steps_for_restoration]
- **Data Preservation**: [user_data_protection_during_rollback]
- **System Continuity**: [service_availability_during_recovery]

## 📋 MONITORING & MAINTENANCE REQUIREMENTS

**Ongoing Monitoring Needs**:
- **Performance Metrics**: [specific_metrics_to_monitor]
- **Integration Health**: [integration_points_requiring_monitoring]
- **Quality Indicators**: [quality_metrics_to_track]
- **User Impact**: [user_experience_aspects_to_observe]

**Maintenance Schedule**:
- **Immediate**: [actions_required_within_24_hours]
- **Short-term**: [actions_required_within_1_week]
- **Medium-term**: [actions_required_within_1_month]
- **Long-term**: [ongoing_maintenance_considerations]

## ✅ IMPACT ANALYSIS SUMMARY

**Overall Impact Assessment**:
- **Impact Severity**: [HIGH/MEDIUM/LOW/MINIMAL]
- **System Stability**: [stable/monitoring_required/unstable]
- **Action Required**: [immediate/scheduled/routine/none]
- **Success Probability**: [high/medium/low] for change integration

**Recommendations**:
1. **Immediate Actions**: [critical_actions_required_now]
2. **Monitoring Plan**: [what_to_monitor_and_when]
3. **Optimization Opportunities**: [ways_to_improve_change_implementation]
4. **Risk Mitigation**: [specific_risk_reduction_strategies]

**Change Approval Status**:
- **APPROVED**: Changes have acceptable impact profile
- **CONDITIONAL**: Changes approved with monitoring/mitigation requirements
- **REJECTED**: Changes have unacceptable risk/impact profile

CONSTRAINTS:
- Analyze ALL downstream dependencies, not just obvious ones
- Consider both immediate and long-term impacts
- Provide specific mitigation strategies for identified risks
- Include quantitative assessments where possible
- Consider rollback scenarios for all identified impacts
- Focus on system stability and user experience preservation"
```

## Impact Analysis Specializations

### System Architecture Impact
**Focus**: Changes effect on overall system architecture and principles
**Elements**: Architecture compliance, design pattern adherence, system cohesion

### Performance Impact Analysis
**Focus**: Resource usage, efficiency, and performance implications
**Elements**: Memory usage, processing time, context loading, token economy

### Integration Impact Assessment
**Focus**: Cross-system integration and reference validation
**Elements**: Command integration, template compatibility, workflow continuity

### Quality Propagation Analysis
**Focus**: Quality impact on connected components and overall system
**Elements**: Documentation quality, process effectiveness, user experience

## Common Impact Analysis Patterns

### High Impact Indicators
- Core system functionality affected
- Multiple dependency chains broken
- Performance degradation detected
- Integration failures identified

### Medium Impact Indicators
- Important features affected
- Some references need updates
- Moderate performance changes
- Monitoring required for stability

### Low Impact Indicators
- Minor feature effects
- Isolated changes with minimal reach
- Performance neutral or improved
- Routine monitoring sufficient

## Quality Criteria for Impact Analysis
- [ ] Comprehensive dependency mapping completed
- [ ] Performance impact quantified where possible
- [ ] Integration validation results provided
- [ ] Risk assessment with mitigation strategies
- [ ] Rollback scenarios analyzed
- [ ] Monitoring recommendations included

## Integration with Change Management
- Impact analysis informs change approval decisions
- Risk assessment guides mitigation strategy development
- Performance impact feeds into optimization planning
- Integration results validate system health maintenance
- Quality propagation analysis guides quality management