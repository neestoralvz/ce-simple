---
contextflow:
  purpose: "Quality gates and technical validation for document verification"
  parent-command: "verify-doc"
  auxiliary: true
  input-format: "document-input"
  output-format: "quality-results"
  research-driven: false
---

# Auxiliary Command `/verify-doc-quality`

## Purpose
Execute comprehensive quality gates and technical validation for document verification workflow.

## Quality Validation Framework

### Technical Quality Gates
```python
def execute_technical_validation(document_input):
    return {
        'token_economy': validate_token_economy(document_input),
        'context_metadata': validate_context_metadata(document_input),
        'duplication_check': validate_uniqueness(document_input),
        'links_structure': validate_link_structure(document_input),
        'technical_accuracy': validate_technical_accuracy(document_input)
    }
```

### Token Economy Validation
```python
def validate_token_economy(document):
    line_count = count_document_lines(document)
    
    return {
        'compliant': line_count <= 80,
        'current_lines': line_count,
        'target_range': '50-80 lines',
        'optimization_needed': line_count > 80
    }
```

### Context Metadata Validation
```python
def validate_context_metadata(document):
    return {
        'contextflow_present': check_contextflow_metadata(document),
        'decision_tree_complete': validate_decision_tree(document),
        'purpose_defined': validate_purpose_definition(document),
        'triggers_specified': validate_triggers(document)
    }
```

### Task Tools Deployment
```python
# Quality Assurance Specialist
Task(
    description="Comprehensive quality verification and scoring",
    prompt="""Actúa como Quality Assurance Specialist. QUALITY VERIFICATION MISSION: Complete quality analysis.

DOCUMENT INPUT:
- Document content: {document_input.content}
- Metadata: {document_input.metadata}
- Context: {document_input.context}

QUALITY ANALYSIS SCOPE:
1. Technical Accuracy:
   - Syntax validation and correctness
   - Reference integrity and accuracy
   - Import statements and dependencies
   - Code blocks and examples

2. Structure Optimization:
   - Header hierarchy and navigation
   - Section organization and flow
   - Information architecture efficiency
   - Cross-reference functionality

3. Token Economy Compliance:
   - Line count within 50-80 range
   - Information density optimization
   - Redundancy elimination
   - Context loading efficiency

4. Production Readiness:
   - Professional presentation quality
   - Consistency with system standards
   - User experience optimization
   - Accessibility and clarity

QUALITY SCORING:
- Technical Accuracy: /25 points
- Structure Optimization: /25 points  
- Token Economy: /25 points
- Production Readiness: /25 points
- TOTAL: /100 points (85+ required for approval)

OUTPUT: Comprehensive quality report with score and recommendations.""",
    subagent_type="general-purpose"
)
```

## Quality Scoring System

### Scoring Criteria
```python
quality_scoring = {
    'technical_accuracy': {
        'weight': 25,
        'criteria': [
            'syntax_correctness',
            'reference_integrity', 
            'code_validation',
            'dependency_accuracy'
        ]
    },
    'structure_optimization': {
        'weight': 25,
        'criteria': [
            'header_hierarchy',
            'section_organization',
            'navigation_efficiency',
            'cross_reference_functionality'
        ]
    },
    'token_economy': {
        'weight': 25,
        'criteria': [
            'line_count_compliance',
            'information_density',
            'redundancy_elimination',
            'context_loading_efficiency'
        ]
    },
    'production_readiness': {
        'weight': 25,
        'criteria': [
            'professional_presentation',
            'system_consistency',
            'user_experience',
            'accessibility_clarity'
        ]
    }
}
```

## Output Structure
```json
{
  "quality_validation_complete": true,
  "overall_quality_score": 87,
  "quality_gate_status": "PASSED",
  "technical_validation": {
    "token_economy": {"compliant": true, "lines": 72},
    "context_metadata": {"complete": true},
    "duplication_check": {"unique": true},
    "links_structure": {"valid": true}
  },
  "quality_breakdown": {
    "technical_accuracy": 22,
    "structure_optimization": 23, 
    "token_economy": 21,
    "production_readiness": 21
  },
  "recommendations": [...],
  "ready_for_voice_validation": true
}
```

## Integration Points
- **INPUT**: Document input from verify-doc orchestrator
- **OUTPUT**: Quality validation results for verify-doc-voice
- **THRESHOLD**: Quality score ≥85/100 required for workflow continuation

---
**Function**: Comprehensive quality gates validation for document verification workflow