---
contextflow:
  purpose: "Architecture validation and consistency checking for document alignment"
  parent-command: "align-doc"
  auxiliary: true
  input-format: "document-input"
  output-format: "architecture-results"
  research-driven: false
---

# Auxiliary Command `/align-doc-architecture`

## Purpose
Execute comprehensive architecture validation and consistency checking for document alignment workflow.

## Architecture Validation Framework

### Core Architecture Functions
```python
def execute_architecture_validation(document_input):
    return {
        'consistency_check': validate_system_consistency(document_input),
        'integration_validation': validate_system_integration(document_input),
        'metadata_verification': validate_contextflow_metadata(document_input),
        'conflict_detection': detect_system_conflicts(document_input),
        'standards_compliance': validate_standards_compliance(document_input)
    }
```

### System Consistency Validation
```python
def validate_system_consistency(document):
    return {
        'principles_alignment': check_principles_consistency(document),
        'decisions_coherence': validate_decision_coherence(document),
        'architecture_integrity': verify_architecture_integrity(document),
        'methodology_compliance': check_methodology_compliance(document)
    }
```

### Integration Validation
```python
def validate_system_integration(document):
    return {
        'no_conflicts_detected': scan_for_system_conflicts(document),
        'command_ecosystem_compatibility': validate_command_compatibility(document),
        'workflow_integration': validate_workflow_integration(document),
        'reference_integrity': validate_reference_integrity(document)
    }
```

### Task Tools Deployment
```python
# Architecture Validator Specialist
Task(
    description="Comprehensive architecture validation and consistency analysis",
    prompt="""Actúa como Architecture Validator. ARCHITECTURE VALIDATION MISSION: Validate system integration.

DOCUMENT INPUT:
- Document content: {document_input.content}
- Document metadata: {document_input.metadata}
- System context: {document_input.system_context}
- Integration points: {document_input.integration_points}

VALIDATION SCOPE:
1. System Consistency Analysis:
   - Principles alignment with established architecture
   - Decision coherence across system components
   - Architecture integrity maintenance
   - Methodology compliance verification

2. Integration Validation:
   - Conflict detection with existing system components
   - Command ecosystem compatibility assessment
   - Workflow integration verification
   - Cross-reference integrity validation

3. Metadata Verification:
   - Contextflow metadata completeness
   - Purpose definition accuracy
   - Trigger specification correctness
   - Workflow step integration validity

4. Standards Compliance:
   - Token economy adherence (50-80 lines core)
   - Context loading optimization
   - Reference structure compliance
   - Decision tree completeness

ARCHITECTURE SCORING:
- System Consistency: /25 points
- Integration Compatibility: /25 points
- Metadata Compliance: /25 points
- Standards Adherence: /25 points
- TOTAL: /100 points (80+ required for approval)

OUTPUT: Comprehensive architecture validation report with alignment recommendations.""",
    subagent_type="general-purpose"
)
```

## Architecture Issue Detection

### Conflict Detection Logic
```python
def detect_system_conflicts(document):
    conflicts = {
        'principle_conflicts': scan_for_principle_conflicts(document),
        'decision_contradictions': scan_for_decision_contradictions(document),
        'workflow_conflicts': scan_for_workflow_conflicts(document),
        'reference_conflicts': scan_for_reference_conflicts(document)
    }
    
    return {
        'conflicts_detected': any(conflicts.values()),
        'conflict_details': conflicts,
        'severity_assessment': assess_conflict_severity(conflicts)
    }
```

### Correction Recommendations
```python
def generate_correction_recommendations(validation_results):
    recommendations = []
    
    if validation_results.consistency_issues:
        recommendations.extend(generate_consistency_corrections(validation_results))
    
    if validation_results.integration_conflicts:
        recommendations.extend(generate_integration_corrections(validation_results))
        
    if validation_results.metadata_issues:
        recommendations.extend(generate_metadata_corrections(validation_results))
    
    return {
        'correction_recommendations': recommendations,
        'priority_order': prioritize_corrections(recommendations),
        'auto_fixable': identify_auto_fixable_issues(recommendations)
    }
```

## Architecture Scoring System

### Scoring Criteria
```python
architecture_scoring = {
    'system_consistency': {
        'weight': 25,
        'criteria': [
            'principles_alignment',
            'decisions_coherence',
            'architecture_integrity',
            'methodology_compliance'
        ]
    },
    'integration_compatibility': {
        'weight': 25,
        'criteria': [
            'no_conflicts_detected',
            'command_ecosystem_compatibility',
            'workflow_integration',
            'reference_integrity'
        ]
    },
    'metadata_compliance': {
        'weight': 25,
        'criteria': [
            'contextflow_completeness',
            'purpose_accuracy',
            'trigger_correctness',
            'workflow_validity'
        ]
    },
    'standards_adherence': {
        'weight': 25,
        'criteria': [
            'token_economy_compliance',
            'context_loading_optimization',
            'reference_structure',
            'decision_tree_completeness'
        ]
    }
}
```

## Output Structure
```json
{
  "architecture_validation_complete": true,
  "architecture_score": 83,
  "validation_status": "PASSED",
  "system_consistency": {
    "principles_aligned": true,
    "decisions_coherent": true,
    "architecture_intact": true,
    "methodology_compliant": true
  },
  "integration_validation": {
    "conflicts_detected": false,
    "ecosystem_compatible": true,
    "workflow_integrated": true,
    "references_valid": true
  },
  "correction_recommendations": [...],
  "ready_for_voice_validation": true
}
```

## Integration Points
- **INPUT**: Document input from align-doc orchestrator
- **OUTPUT**: Architecture validation results for align-doc-voice
- **THRESHOLD**: Architecture score ≥80/100 required for workflow continuation

---
**Function**: Comprehensive architecture validation for document alignment workflow