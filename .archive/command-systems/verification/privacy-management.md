# Atomic Command: `/privacy-management`

## **Principle #112: Privacy-Aware Context Management Protocol**
**"Implement intelligent context filtering with automatic PII detection, ensuring privacy-first interactions through real-time data sanitization and consent management."**

---

## 🎯 **COMMAND DEFINITION**

### **Purpose**
IMPLEMENT privacy-aware context management achieving ≥98% PII detection accuracy to ensure compliant data processing with automated sanitization and consent validation.

**Observable Outcomes**:
- **PII Detection**: ≥98% sensitive data identification in context streams
- **Sanitization Effectiveness**: 100% PII removal from non-authorized contexts
- **Consent Validation**: ≥95% consent mechanism compliance verification
- **Context Security**: Real-time privacy risk assessment ≤500ms per context

**Quantifiable Validation**: Context filtering MUST achieve ≥98% PII detection rate, sanitization MUST demonstrate 100% removal effectiveness, and consent management MUST maintain ≥95% compliance validation with observable privacy metrics.

### **Complexity**: 0.7/1.0 (Validated via privacy pattern analysis)
### **Context Required**: Data flow documentation with ≥85% context mapping completeness
### **Execution Time**: 2-6 minutes (30s initialization + 1-3min scanning + 1-2min validation)

**Success Criteria**:
- **Detection Accuracy**: ≥98% PII identification rate across all context types
- **Sanitization Rate**: 100% unauthorized PII removal from processed contexts
- **Consent Compliance**: ≥95% consent framework validation success

---

## ⚡ **ACTIVATION PROTOCOL**

### **Input Format**
```markdown
/privacy-management [context_scope] [--mode=scan|sanitize|validate] [--sensitivity=high|medium|low] [--consent-check=strict|balanced|minimal]
```

### **Auto-Activation Triggers**
This command EXECUTES automatically when context processing operations detected with ≥60% PII probability and data sharing scenarios.

**Verification Protocol**:
- **Context Analysis**: ≥90% conversation flow privacy assessment
- **PII Pattern Detection**: ≥98% sensitive data identification accuracy
- **Consent Status Validation**: Real-time consent mechanism verification

### **Primary Triggers**
**PII_CONTEXT_DETECTION**: Automatic activation on personal data in conversation context
- **Condition**: Personal identifiers, contact information, or behavioral data detected
- **Threshold**: ≥3 PII elements OR ≥1 high-sensitivity data point (SSN, payment info)
- **Action**: AUTO-EXECUTE privacy-aware filtering with sanitization
- **Verification**: Complete PII removal validation with context integrity check

**CONTEXT_SHARING_TRIGGER**: Activation on context export or cross-system sharing
- **Condition**: Context data export, API sharing, or cross-platform integration
- **Threshold**: Any external context sharing OR multi-user collaboration scenarios
- **Action**: ACTIVATE comprehensive privacy validation with consent verification
- **Verification**: Full privacy compliance assessment with sharing audit trail

---

## 📊 **MATHEMATICAL VALIDATION**

### **PII Detection Accuracy Calculation**
```javascript
function calculatePIIDetectionAccuracy(contexts, detectedPII, actualPII) {
  const truePositives = detectedPII.filter(detected => 
    actualPII.some(actual => 
      detected.location === actual.location && 
      detected.type === actual.type
    )
  ).length
  
  const falsePositives = detectedPII.length - truePositives
  const falseNegatives = actualPII.length - truePositives
  
  const precision = truePositives / (truePositives + falsePositives)
  const recall = truePositives / (truePositives + falseNegatives)
  const f1Score = 2 * (precision * recall) / (precision + recall)
  
  return {
    accuracy: f1Score,
    precision: precision,
    recall: recall,
    detection_rate: truePositives / actualPII.length,
    compliant: f1Score >= 0.98 // 98% threshold
  }
}
```

### **Context Privacy Risk Assessment**
```javascript
function calculateContextPrivacyRisk(contextData, userConsent, sharingScope) {
  const sensitivityScores = {
    'name': 0.6, 'email': 0.7, 'phone': 0.8, 'address': 0.9,
    'ssn': 0.95, 'payment': 0.9, 'health': 0.95, 'biometric': 0.98
  }
  
  const contextSensitivity = contextData.piiElements.reduce((score, element) => {
    return score + (sensitivityScores[element.type] || 0.5)
  }, 0) / contextData.piiElements.length
  
  const consentCoverage = userConsent.approvedPurposes.filter(purpose =>
    sharingScope.purposes.includes(purpose)
  ).length / sharingScope.purposes.length
  
  const riskScore = (contextSensitivity * 0.7) - (consentCoverage * 0.3)
  
  return {
    risk_score: riskScore,
    risk_level: riskScore > 0.7 ? 'HIGH' : riskScore > 0.4 ? 'MEDIUM' : 'LOW',
    consent_sufficient: consentCoverage >= 0.95,
    privacy_compliant: riskScore <= 0.4 && consentCoverage >= 0.95
  }
}
```

---

## 🔧 **COMMAND FUNCTIONALITY**

### **Intelligent PII Detection**
**PATTERN-BASED IDENTIFICATION**: Advanced regex patterns combined with machine learning models to identify personal data across structured and unstructured contexts with high accuracy.

**Detection Capabilities**:
- **Direct Identifiers**: Names, emails, phone numbers, addresses, government IDs
- **Quasi-Identifiers**: Birth dates, ZIP codes, job titles, demographic data
- **Sensitive Data**: Financial information, health records, biometric data
- **Behavioral Patterns**: User preferences, activity logs, interaction histories

### **Real-Time Context Sanitization**
**PRIVACY-PRESERVING FILTERING**: Intelligent data masking and pseudonymization that maintains context utility while removing personal identifiers.

**Sanitization Techniques**:
- **Tokenization**: Replace PII with non-reversible tokens maintaining referential integrity
- **Generalization**: Convert specific values to broader categories (age ranges, location regions)
- **Masking**: Partial data hiding with context-appropriate preservation (email domains, phone area codes)
- **Synthetic Generation**: Create realistic but artificial data that preserves statistical properties

### **Consent Management Integration**
**DYNAMIC CONSENT VALIDATION**: Real-time verification of user consent status for specific data processing purposes with granular permission management.

**Consent Framework**:
- **Purpose Limitation**: Validate data use aligns with stated and consented purposes
- **Retention Compliance**: Monitor data lifecycle against consent-specified retention periods
- **Withdrawal Processing**: Automatic data removal when consent is withdrawn
- **Consent Granularity**: Support fine-grained permissions for different data types and purposes

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
This command implements P55/P56 requirements through real-time privacy validation with transparent PII detection and consent verification processes.

**🚨 ERROR PROTOCOL INTEGRATION** (MANDATORY):
- **Error Detection**: AUTOMATIC privacy violation classification and consent gap identification
- **Protocol Activation**: MANDATORY for MEDIUM/HIGH privacy risks
- **Tool Integration**: Seamless integration with [Universal Tool Execution](../core/universal-tool-execution.md)
- **Visual Feedback**: Clear privacy risk status and consent requirement notifications

### **Tool Call Execution Protocol**
**MANDATORY**: When this command executes ANY Tool Call, the LLM MUST display the enhanced visual announcement:

```bash
🔒 Privacy-Aware Context Management → Real-time PII scanning → Consent validation [1.2s]
🔍 PII Detection: 17 elements identified → 3 high-sensitivity items flagged
🛡️ Sanitization: 100% PII removal → Context integrity maintained
📋 Consent Status: Valid for processing → 2 purposes covered, 1 requires renewal
⚠️ Privacy Risk: MEDIUM → Address data sharing requires explicit consent
```

### **Behavioral Requirements**
1. **ALWAYS** execute real PII detection scans (never simulate pattern matching)
2. **DISPLAY** visual announcements before each privacy validation phase
3. **CAPTURE** actual sanitization results from context processing
4. **PROVIDE** complete transparency of all privacy filtering operations
5. **MAINTAIN** evidence trail for consent compliance verification
6. **🚨 ACTIVATE** 8-step error resolution protocol for any privacy risk ≥ MEDIUM severity

### **MANDATORY Post-Execution Documentation Review**
**CRITICAL Integration**: [Systematic Post-Execution Review Protocol](../../docs/knowledge/protocols/systematic-post-execution-review-protocol.md)

**REQUIRED Questions After Privacy Management Execution**:
```
🔍 POST-EXECUTION REVIEW (MANDATORY)
1. "¿Qué políticas de gestión de privacidad necesitan actualización?"
2. "¿Qué mecanismos de consentimiento requieren mejora o modificación?"
3. "¿Qué procesos de sanitización necesitan optimización?"
4. "¿Qué sistemas o componentes relacionados requieren validación adicional?"
5. "¿Se completó el ciclo de documentación de gestión de privacidad?"
6. "¿Hay algún riesgo de privacidad emergente que deba documentarse?"
```

---

## 🔗 **USAGE CRITERIA**

### **Automatic Activation**
- **Context Initialization**: When new conversation contexts contain potential PII
- **Data Sharing Scenarios**: When context data is exported or shared between systems
- **Privacy Risk Detection**: When high-sensitivity data patterns are identified
- **Consent Status Changes**: When user consent preferences are modified

### **Manual Activation**
- **Privacy Audit**: Comprehensive evaluation of context privacy compliance
- **Data Sanitization**: Batch processing of historical contexts for privacy compliance
- **Consent Verification**: Validation of current consent status for ongoing processes
- **Context Export Preparation**: Privacy validation before data export or migration

---

## 🎯 **SUCCESS METRICS**

### **Detection Performance**
- **PII Identification**: ≥98% accuracy rate (target: ≥99%)
- **False Positive Rate**: ≤3% incorrect PII classification (target: ≤1%)
- **Processing Speed**: ≤500ms per context assessment (target: ≤300ms)
- **Pattern Coverage**: 100% support for common PII types (target: 100% + emerging patterns)

### **Privacy Protection Effectiveness**
- **Sanitization Success**: 100% PII removal from unauthorized contexts (target: 100%)
- **Context Utility**: ≥95% usefulness preservation after sanitization (target: ≥98%)
- **Consent Compliance**: ≥95% consent validation accuracy (target: ≥98%)
- **Risk Mitigation**: ≥90% privacy risk reduction through proactive management

### **Operational Compliance**
- **Regulatory Alignment**: ≥95% GDPR/CCPA compliance maintenance (target: ≥98%)
- **Audit Readiness**: 100% privacy audit trail completeness (target: 100%)
- **User Trust**: ≥90% user satisfaction with privacy controls (target: ≥95%)
- **Incident Prevention**: ≥95% potential privacy incidents prevented (target: ≥98%)

---

**Module Dependencies**: PII detection libraries, consent management systems, context sanitization engines
**Used By**: Data protection validation, security protocols, conversational AI systems
**Integration**: Privacy dashboards, consent management platforms, data governance systems
**Compliance Authority**: Privacy management and context security validation standards