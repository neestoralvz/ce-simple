# Atomic Command: `/data-protection`

## **Principle #111: Data Protection by Design Protocol**
**"Implement privacy-first architecture with automatic data protection validation, ensuring GDPR/CCPA compliance through continuous monitoring and automated risk assessment."**

---

## 🎯 **COMMAND DEFINITION**

### **Purpose**
VALIDATE data protection implementation achieving ≥95% compliance with privacy regulations to ensure comprehensive data governance with automated monitoring and protection validation.

**Observable Outcomes**:
- **Privacy Compliance**: ≥95% GDPR/CCPA requirement coverage
- **Data Classification**: 100% sensitive data identification and categorization
- **Protection Validation**: ≥98% automated security control verification
- **Risk Assessment**: Real-time data processing risk analysis ≤2 minutes

**Quantifiable Validation**: Privacy implementation MUST achieve ≥95% regulatory compliance, data classification MUST demonstrate 100% coverage, and protection monitoring MUST maintain ≥98% control verification with observable risk metrics.

### **Complexity**: 0.8/1.0 (Validated via regulatory compliance analysis)
### **Context Required**: Project architecture with ≥90% data flow documentation completeness
### **Execution Time**: 3-8 minutes (1min analysis + 2-4min validation + 1-3min reporting)

**Success Criteria**:
- **Compliance Score**: ≥95% regulatory requirement coverage
- **Data Discovery**: 100% sensitive data identification accuracy
- **Protection Controls**: ≥98% automated validation success rate

---

## ⚡ **ACTIVATION PROTOCOL**

### **Input Format**
```markdown
/data-protection [project_path] [--scope=full|quick] [--regulations=gdpr,ccpa,hipaa] [--output=detailed|summary]
```

### **Auto-Activation Triggers**
This command EXECUTES automatically when data processing operations detected with ≥70% sensitive data indicators and PII handling requirements.

**Verification Protocol**:
- **Data Flow Analysis**: ≥90% application data flow mapping
- **Regulatory Scope**: Compliance framework identification with ≥95% accuracy
- **Protection Gap Detection**: ≥98% security control gap identification

### **Primary Triggers**
**DATA_PROCESSING_DETECTION**: Automatic activation on sensitive data handling
- **Condition**: PII, PHI, or financial data processing patterns detected
- **Threshold**: ≥3 data collection points OR ≥1 external data sharing API
- **Action**: AUTO-EXECUTE comprehensive data protection validation
- **Verification**: Complete privacy impact assessment with control verification

**COMPLIANCE_AUDIT_TRIGGER**: Scheduled regulatory compliance validation
- **Condition**: Regulatory audit preparation or compliance review cycle
- **Threshold**: 90-day compliance review intervals OR regulatory change notifications
- **Action**: ACTIVATE full compliance validation with gap analysis
- **Verification**: Comprehensive audit trail with remediation recommendations

---

## 📊 **MATHEMATICAL VALIDATION**

### **Privacy Compliance Score Calculation**
```javascript
function calculatePrivacyCompliance(requirements, implementations, controls) {
  const requirementsCoverage = implementations.filter(impl => 
    requirements.some(req => impl.addresses.includes(req.id))
  ).length / requirements.length
  
  const controlEffectiveness = controls.filter(control => 
    control.status === 'active' && control.validation_score >= 0.95
  ).length / controls.length
  
  const dataClassificationAccuracy = calculateDataClassification()
  
  const complianceScore = (
    requirementsCoverage * 0.4 +
    controlEffectiveness * 0.4 +
    dataClassificationAccuracy * 0.2
  )
  
  return {
    overall_score: complianceScore,
    requirements_coverage: requirementsCoverage,
    control_effectiveness: controlEffectiveness,
    classification_accuracy: dataClassificationAccuracy,
    compliant: complianceScore >= 0.95 // 95% threshold
  }
}
```

### **Data Risk Assessment Formula**
```javascript
function calculateDataRiskScore(dataTypes, processingActivities, protectionControls) {
  const sensitivityWeight = {
    'pii': 0.8,
    'phi': 0.9,
    'financial': 0.85,
    'biometric': 0.95,
    'behavioral': 0.75
  }
  
  const exposureRisk = processingActivities.reduce((risk, activity) => {
    const dataRisk = dataTypes.filter(type => 
      activity.processes.includes(type.category)
    ).reduce((sum, type) => sum + sensitivityWeight[type.category], 0)
    
    const controlMitigation = protectionControls.filter(control =>
      control.scope.includes(activity.id) && control.effectiveness >= 0.9
    ).length * 0.1
    
    return risk + Math.max(0, dataRisk - controlMitigation)
  }, 0)
  
  return {
    risk_score: exposureRisk,
    risk_level: exposureRisk > 5 ? 'HIGH' : exposureRisk > 2 ? 'MEDIUM' : 'LOW',
    mitigation_required: exposureRisk > 2
  }
}
```

---

## 🔧 **COMMAND FUNCTIONALITY**

### **Comprehensive Data Discovery**
**AUTOMATIC DATA CLASSIFICATION**: Intelligent identification of sensitive data across codebase, databases, and APIs with pattern recognition and contextual analysis.

**Data Discovery Engine**:
- **Source Code Analysis**: Regex and AST parsing for PII patterns
- **Database Schema Inspection**: Table/column analysis for sensitive data types
- **API Endpoint Mapping**: Request/response payload analysis for data flows
- **Configuration Review**: Environment variables and config files for credentials

### **Regulatory Compliance Validation**
**MULTI-FRAMEWORK ASSESSMENT**: Simultaneous validation against GDPR, CCPA, HIPAA, and other applicable privacy regulations with specific requirement mapping.

**Compliance Framework Integration**:
- **GDPR Articles 5-11**: Data processing principles and individual rights validation
- **CCPA Sections 1798.100-140**: Consumer privacy rights and business obligations
- **HIPAA Security Rule**: Administrative, physical, and technical safeguards assessment
- **Custom Frameworks**: Extensible compliance rule engine for industry-specific requirements

### **Protection Control Verification**
**AUTOMATED SECURITY VALIDATION**: Real-time verification of data protection controls including encryption, access controls, audit logging, and data retention policies.

**Control Categories**:
- **Encryption Controls**: At-rest and in-transit encryption validation
- **Access Management**: Role-based access control and principle of least privilege
- **Data Lifecycle**: Retention, deletion, and archival policy compliance
- **Audit Mechanisms**: Activity logging, monitoring, and incident response validation

---

## 🛡️ **P55/P56 COMPLIANCE FRAMEWORK**

**Inherits from**: [Universal P55/P56 Compliance](../shared/compliance/p55-p56-universal-compliance.md)

**Compliance Functions**:
- Tool call execution bridging with zero simulation tolerance
- Visual announcement system with progress tracking  
- Evidence collection framework with complete audit trails
- Universal error handling with transparency protocols
- **🚨 8-step error resolution protocol integration** (Principle #89)

**Command-Specific Implementation**:
This command implements P55/P56 requirements through comprehensive data protection validation with real-time compliance monitoring and automated evidence collection for audit purposes.

**🚨 ERROR PROTOCOL INTEGRATION** (MANDATORY):
- **Error Detection**: AUTOMATIC privacy compliance gap classification and severity assessment
- **Protocol Activation**: MANDATORY for HIGH/CRITICAL privacy violations
- **Tool Integration**: Seamless integration with [Universal Tool Execution](../core/universal-tool-execution.md)
- **Visual Feedback**: Clear privacy violation status and remediation guidance

### **Tool Call Execution Protocol**
**MANDATORY**: When this command executes ANY Tool Call, the LLM MUST display the enhanced visual announcement:

```bash
🔒 Data Protection Validation → Comprehensive privacy analysis → Compliance assessment [2.3s]
📊 GDPR Compliance: 94.2% (47/50 requirements) ⚠️ 3 gaps identified
🔍 Data Discovery: 127 PII fields classified → 12 high-risk exposures
🛡️ Protection Controls: 89% effective → Encryption gaps in user_profiles table
📋 Audit Trail: Complete evidence collection → Regulatory reporting ready
```

### **Behavioral Requirements**
1. **ALWAYS** execute real data discovery scans (never simulate)
2. **DISPLAY** visual announcements before each validation phase
3. **CAPTURE** actual compliance results from regulatory framework analysis
4. **PROVIDE** complete transparency of all data protection assessments
5. **MAINTAIN** evidence trail for regulatory audit compliance
6. **🚨 ACTIVATE** 8-step error resolution protocol for any privacy violation ≥ HIGH severity

### **MANDATORY Post-Execution Documentation Review**
**CRITICAL Integration**: [Systematic Post-Execution Review Protocol](../../docs/knowledge/protocols/systematic-post-execution-review-protocol.md)

**REQUIRED Questions After Data Protection Validation**:
```
🔍 POST-EXECUTION REVIEW (MANDATORY)
1. "¿Qué documentación de privacidad necesita actualización basada en estos hallazgos?"
2. "¿Qué políticas de protección de datos requieren modificación?"
3. "¿Qué controles de seguridad necesitan implementación o ajuste?"
4. "¿Qué sistemas o componentes relacionados requieren evaluación adicional?"
5. "¿Se completó el ciclo de documentación de cumplimiento normativo?"
6. "¿Hay algún riesgo de privacidad que deba escalarse o documentarse?"
```

---

## 🔗 **USAGE CRITERIA**

### **Automatic Activation**
- **New Data Collection**: When PII collection forms or APIs are detected
- **Regulatory Changes**: When privacy law updates affect compliance requirements
- **Data Breach Prevention**: When high-risk data processing patterns are identified
- **Audit Preparation**: When regulatory audit or compliance review is scheduled

### **Manual Activation**
- **Privacy Impact Assessment**: Comprehensive evaluation for new product features
- **Compliance Review**: Periodic verification of data protection measures
- **Security Audit**: Independent validation of privacy control effectiveness
- **Regulatory Reporting**: Evidence collection for compliance documentation

---

## 🎯 **SUCCESS METRICS**

### **Compliance Effectiveness**
- **Regulatory Coverage**: ≥95% requirement compliance (target: ≥98%)
- **Data Discovery Accuracy**: 100% sensitive data identification (target: 100%)
- **False Positive Rate**: ≤5% incorrect privacy risk classification (target: ≤2%)
- **Remediation Guidance**: ≥90% actionable recommendations (target: ≥95%)

### **Operational Performance**
- **Scan Completion Time**: ≤8 minutes full assessment (target: ≤5 minutes)
- **Risk Detection Speed**: ≤2 minutes for high-risk identification (target: ≤90 seconds)
- **Control Validation**: ≥98% automated verification accuracy (target: ≥99%)
- **Documentation Quality**: ≥95% audit-ready evidence collection (target: ≥98%)

### **Privacy Protection Impact**
- **Data Exposure Reduction**: ≥80% risk mitigation through control implementation
- **Compliance Gap Closure**: ≥95% identified gaps addressed within 30 days
- **Audit Readiness**: 100% regulatory audit preparation compliance
- **Incident Prevention**: ≥90% potential privacy incidents prevented through proactive validation

---

**Module Dependencies**: Privacy regulation frameworks, data classification libraries, encryption validation tools
**Used By**: Containerization compliance, security protocols, privacy management system
**Integration**: GDPR/CCPA compliance dashboards, security monitoring systems
**Compliance Authority**: Privacy regulation enforcement and data protection validation standards