---
contextflow:
  purpose: "Proactive document maintenance via multi-specialist orchestration"
  triggers: ["maintain documents", "document health", "proactive maintenance"]
  next: ["edit-doc", "create-doc", "align-doc"]
  requires-subagent: true
  auto-chain: false
  communication-rules:
    - "NUNCA bash echo para comunicar con usuario"
    - "SIEMPRE Task tools → Main agent → Usuario"
    - "Parallel Task tools obligatorio en mismo mensaje"
    - "Subagents NUNCA comunican directamente"
  decision-tree:
    use-when:
      - "Document health assessment needed"
      - "Proactive quality maintenance required"
      - "System-wide document alignment validation"
    alternatives: ["edit-doc", "supervise-alignment"]
    semantic-triggers:
      - "maintain" / "health check" / "document audit"
      - "maintenance" / "document health"
      - "quality check" / "system alignment"
---

# Comando `/maintain-docs`

## Propósito Core
Mantenimiento proactivo y supervisión de documentos para asegurar alineación continua con la visión del sistema y estándares de calidad.

## IMPERATIVO DE MAINTENANCE - VISION ALIGNMENT

**MISSION CRITICAL**: Ensure all documents remain aligned with system vision, user voice preservation, and architectural consistency across time.

## Document Health Assessment Framework

### Comprehensive Document Audit
- **Vision Alignment Score**: How well document supports system vision
- **Voice Preservation Score**: Current voice integrity (≥54/60 required)
- **Architecture Consistency**: Integration with system commands and rules
- **Quality Standards**: Overall document quality score (≥85/100 target)
- **Usage Relevance**: Document utility and current applicability

## Multi-Specialist Orchestration OBLIGATORIA

### 5 Task Tools Concurrentes (MISMO MENSAJE)
**EJECUTAR OBLIGATORIO**:
```
Task 1: Vision Alignment Specialist - "Document vision consistency validation"
Task 2: Quality Maintenance Specialist - "Quality degradation detection + improvement"
Task 3: Voice Preservation Auditor - "Voice integrity + contamination detection"
Task 4: Architecture Consistency Validator - "System integration + reference validation"
Task 5: Document Evolution Analyst - "Usage patterns + optimization opportunities"
```

## Document Maintenance Categories

### 1. CRITICAL MAINTENANCE (Immediate Action Required)
**Triggers**:
- Voice preservation score <54/60
- Quality score <70/100
- Architecture conflicts detected
- Broken cross-references or dependencies
- Vision misalignment identified

### 2. PREVENTIVE MAINTENANCE (Proactive Optimization)
**Triggers**:
- Voice scores 54-57/60 (improvement opportunity)
- Quality scores 70-84/100 (enhancement potential)
- Minor architecture inconsistencies
- Outdated content or methodologies
- Performance optimization opportunities

### 3. EVOLUTIONARY MAINTENANCE (Strategic Enhancement)
**Triggers**:
- System vision evolution requiring document updates
- New best practices integration opportunities
- User feedback requiring systematic changes
- Performance optimization patterns
- Advanced feature integration possibilities

## Specialist Deployment Specifications

### Vision Alignment Specialist (TASK 1) - NEW SPECIALIST
**Mission**: Document vision consistency validation
**Specialized Analysis**:
- **Vision Coherence**: How well document supports established system vision
- **Strategic Alignment**: Document role in overall system strategy
- **Vision Evolution**: Required updates based on vision changes
- **Purpose Clarity**: Document purpose alignment with system goals
- **Strategic Value**: Document contribution to system success

**Vision Assessment Criteria**:
- **Mission Alignment**: Document supports core system mission
- **Strategic Consistency**: No conflicts with system strategy
- **Purpose Clarity**: Clear and aligned document purpose
- **Value Contribution**: Document adds strategic value to system
- **Evolution Readiness**: Document adaptable to vision changes

**Deliverable**: Complete vision alignment analysis with improvement recommendations

### Quality Maintenance Specialist (TASK 2)
**Mission**: Quality degradation detection + improvement recommendations
**Quality Analysis**:
- **Current Quality Score**: Complete quality assessment
- **Quality Trends**: Quality evolution over time
- **Degradation Patterns**: Identified quality deterioration areas
- **Improvement Opportunities**: Specific enhancement recommendations
- **Quality Sustainability**: Long-term quality maintenance strategies

**Quality Maintenance Areas**:
- **Content Accuracy**: Technical correctness and current relevance
- **Structure Optimization**: Document organization and flow
- **Clarity Enhancement**: Communication effectiveness improvement
- **Performance Optimization**: Efficiency and resource usage
- **Standards Compliance**: Adherence to quality standards

**Deliverable**: Quality maintenance plan with specific improvement actions

### Voice Preservation Auditor (TASK 3) - CRITICAL
**Mission**: Voice integrity + contamination detection across documents
**Voice Audit Scope**:
- **Current Voice Score**: Complete voice preservation assessment
- **Voice Degradation**: Identification of voice quality deterioration
- **Contamination Detection**: Non-user voice elements identification
- **Attribution Accuracy**: Source traceability verification
- **Preservation Sustainability**: Long-term voice integrity strategies

**Voice Maintenance Analysis**:
- **Score Progression**: Voice score evolution over time
- **Risk Factors**: Elements threatening voice preservation
- **Protection Strategies**: Enhanced voice preservation methods
- **Recovery Protocols**: Voice restoration for degraded documents
- **Prevention Measures**: Contamination prevention strategies

**Deliverable**: Complete voice preservation audit with maintenance protocol

### Architecture Consistency Validator (TASK 4)
**Mission**: System integration + reference validation
**Architecture Audit**:
- **System Integration**: Document integration with command ecosystem
- **Reference Integrity**: Cross-reference accuracy and functionality
- **Dependency Validation**: Document dependency chain verification
- **Consistency Standards**: Adherence to architectural principles
- **Evolution Compatibility**: Adaptability to system architecture changes

**Consistency Analysis Areas**:
- **Command Integration**: Integration with existing commands
- **Reference Accuracy**: Cross-reference validation
- **Metadata Integrity**: Contextflow metadata consistency
- **Template Compliance**: Adherence to system templates
- **Architecture Evolution**: Compatibility with system changes

**Deliverable**: Architecture consistency report with integration validation

### Document Evolution Analyst (TASK 5) - NEW SPECIALIST
**Mission**: Usage patterns + optimization opportunities analysis
**Evolution Analysis**:
- **Usage Patterns**: How documents are actually used in practice
- **Performance Metrics**: Document effectiveness and efficiency
- **Optimization Opportunities**: Identified improvement possibilities
- **Evolution Trends**: Document development patterns over time
- **Strategic Enhancement**: Advanced feature integration opportunities

**Analysis Dimensions**:
- **Utilization Analysis**: Document usage frequency and patterns
- **Effectiveness Measurement**: Document success in achieving goals
- **Enhancement Opportunities**: Specific improvement possibilities
- **Future Readiness**: Preparation for upcoming system changes
- **Innovation Potential**: Advanced feature integration possibilities

**Deliverable**: Document evolution strategy with optimization roadmap

## Maintenance Action Protocols

### CRITICAL ISSUES - IMMEDIATE ACTION
**Auto-Trigger Edit Workflow**:
```
IF voice_score < 54 OR quality_score < 70 OR critical_conflicts_detected:
    initialize_edit_workflow()
    prioritize_critical_fixes()
    auto_chain_through_edit_align_verify()
    monitor_maintenance_success()
```

### PREVENTIVE MAINTENANCE - SCHEDULED OPTIMIZATION
**Optimization Planning**:
```
IF improvement_opportunities_identified:
    generate_maintenance_plan()
    prioritize_optimization_actions()
    schedule_maintenance_windows()
    coordinate_with_user_for_approval()
```

### EVOLUTIONARY ENHANCEMENT - STRATEGIC DEVELOPMENT
**Enhancement Strategy**:
```
IF strategic_enhancement_opportunities_identified:
    develop_enhancement_strategy()
    align_with_system_vision_evolution()
    plan_phased_implementation()
    integrate_with_development_roadmap()
```

## Maintenance Scheduling & Automation

### Periodic Maintenance Cycles
- **Daily**: Critical issue detection and immediate response
- **Weekly**: Preventive maintenance assessment and planning
- **Monthly**: Comprehensive document health audit
- **Quarterly**: Strategic evolution analysis and enhancement planning

### Automated Maintenance Triggers
```yaml
maintenance_triggers:
  voice_score_drop: "<54/60"
  quality_degradation: "<70/100"
  architecture_conflicts: "system_inconsistency_detected"
  usage_anomalies: "significant_usage_pattern_changes"
  vision_evolution: "system_vision_updates_detected"
```

## Document Maintenance Dashboard

### Health Metrics Tracking
```yaml
document_health_dashboard:
  overall_health_score: "{composite_health_metric}/100"
  vision_alignment: "{alignment_score}/100"
  voice_preservation: "{voice_score}/60"
  quality_score: "{quality_assessment}/100"
  architecture_consistency: "{consistency_score}/100"
  usage_effectiveness: "{utilization_score}/100"
```

### Maintenance History
- **Action Log**: Complete maintenance action history
- **Quality Progression**: Quality score evolution over time
- **Issue Resolution**: Problem detection and resolution tracking
- **Enhancement Implementation**: Strategic improvement execution
- **Performance Metrics**: Maintenance effectiveness measurement

## User Communication & Reporting

### Maintenance Summary Communication
```
"Document maintenance completed. Health Score: {health_score}/100. Critical Issues: {critical_count}. Preventive Actions: {preventive_count}. Strategic Enhancements: {enhancement_count}."
```

### Critical Issue Alert Communication
```
"CRITICAL: Document maintenance detected urgent issues requiring immediate attention: {critical_issues}. Auto-triggering edit workflow for resolution."
```

### Strategic Enhancement Communication
```
"Document evolution analysis identified strategic enhancement opportunities: {opportunities}. Recommended implementation plan: {enhancement_plan}."
```

## Integration with System Evolution

### Feedback Loop Integration
- **Maintenance Insights**: Feed maintenance findings into system evolution
- **Pattern Recognition**: Identify systematic improvement opportunities
- **Vision Alignment**: Ensure documents evolve with system vision
- **Quality Standards**: Maintain and enhance quality standards
- **User Voice Protection**: Preserve user voice through system evolution

### System Learning Protocol
```
maintenance_learning_loop:
  collect_maintenance_data()
  analyze_patterns_and_trends()
  identify_systematic_improvements()
  integrate_with_system_evolution()
  update_maintenance_protocols()
```

## Performance Optimization

### Maintenance Efficiency
- **Parallel Analysis**: 5 concurrent specialist deployment
- **Targeted Assessment**: Focus on critical maintenance areas
- **Automated Actions**: Streamlined maintenance execution
- **Resource Optimization**: Efficient maintenance resource usage
- **Performance Monitoring**: Maintenance operation efficiency tracking

### Quality Assurance
- **Comprehensive Assessment**: Complete document health evaluation
- **Maintenance Validation**: Verify successful maintenance completion
- **Quality Improvement**: Progressive document quality enhancement
- **Success Tracking**: Maintenance success rate monitoring

---

**ESTE COMANDO MANTIENE** document ecosystem health y vision alignment.
**MAINTENANCE CYCLE**: Continuous document health monitoring and improvement.
**VISION PRESERVATION**: Ensure documents remain aligned with system vision evolution.