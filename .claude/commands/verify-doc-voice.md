---
contextflow:
  purpose: "Voice preservation validation and scoring for document verification"
  parent-command: "verify-doc"
  auxiliary: true
  input-format: "quality-results"
  output-format: "voice-results"
  research-driven: false
---

# Auxiliary Command `/verify-doc-voice`

## Purpose
Execute mandatory voice preservation validation and scoring with zero contamination tolerance.

## Voice Preservation Framework

### Voice Validation Core Functions
```python
def execute_voice_preservation_validation(quality_results):
    return {
        'voice_separation': validate_voice_separation(quality_results.document),
        'quote_accuracy': validate_quote_accuracy(quality_results.document),
        'source_attribution': validate_source_attribution(quality_results.document),
        'contamination_detection': detect_voice_contamination(quality_results.document),
        'scoring_compliance': calculate_voice_score(quality_results.document)
    }
```

### Voice Separation Validation
```python
def validate_voice_separation(document):
    return {
        'user_voice_identified': identify_user_voice_sections(document),
        'system_analysis_separated': identify_system_sections(document),
        'complete_separation': verify_zero_mixing(document),
        'contamination_detected': scan_for_contamination(document)
    }
```

### Quote Accuracy Validation
```python
def validate_quote_accuracy(document):
    return {
        'exact_quotes_only': verify_no_paraphrasing(document),
        'source_attribution_complete': verify_complete_attribution(document),
        'context_preservation': verify_context_maintained(document),
        'zero_interpretation': verify_no_interpretation_added(document)
    }
```

### Task Tools Deployment
```python
# Voice Preservation Validator
Task(
    description="MANDATORY voice preservation validation with comprehensive scoring",
    prompt="""Actúa como Voice Preservation Validator. VOICE PRESERVATION MISSION: Validate user voice integrity.

DOCUMENT INPUT:
- Document content: {quality_results.document}
- Quality validation: {quality_results.validation}
- Context: {quality_results.context}

VOICE PRESERVATION VALIDATION:
1. Voice Separation Analysis:
   - Complete separation user voice vs system analysis
   - Zero contamination detection (MANDATORY)
   - Clear attribution boundaries
   - Immutability marking verification

2. Quote Accuracy Verification:
   - Exact user words preserved (NO paraphrasing)
   - Complete source attribution for every quote
   - Context preservation without interpretation
   - Intent clarity without system interpretation

3. Source Traceability:
   - Perfect links to original sources
   - Complete conversation references
   - Timestamp accuracy where applicable
   - Navigational integrity maintained

4. Contamination Detection:
   - System voice infiltration scanning
   - AI interpretation elimination
   - Bias injection prevention
   - Voice purity enforcement

VOICE SCORING SYSTEM (60 points total):
- Quote Accuracy: /10 points
- Intent Fidelity: /10 points
- Context Completeness: /10 points
- Source Traceability: /10 points
- Attribution Clarity: /10 points
- Immutability Status: /10 points

MINIMUM THRESHOLD: ≥54/60 (90%+ required for approval)

OUTPUT: Comprehensive voice preservation report with detailed scoring.""",
    subagent_type="general-purpose"
)
```

## Voice Scoring System

### Scoring Criteria
```python
voice_scoring = {
    'quote_accuracy': {
        'weight': 10,
        'criteria': [
            'exact_words_preserved',
            'zero_paraphrasing_detected',
            'original_formatting_maintained',
            'punctuation_accuracy'
        ]
    },
    'intent_fidelity': {
        'weight': 10,
        'criteria': [
            'original_meaning_maintained',
            'no_interpretation_added',
            'context_clarity_preserved',
            'user_intention_accuracy'
        ]
    },
    'context_completeness': {
        'weight': 10,
        'criteria': [
            'full_context_preserved',
            'conversation_flow_maintained',
            'decision_context_included',
            'background_information_complete'
        ]
    },
    'source_traceability': {
        'weight': 10,
        'criteria': [
            'perfect_source_links',
            'conversation_references_accurate',
            'timestamp_precision',
            'navigational_integrity'
        ]
    },
    'attribution_clarity': {
        'weight': 10,
        'criteria': [
            'complete_user_system_separation',
            'clear_attribution_boundaries',
            'voice_ownership_clarity',
            'responsibility_attribution'
        ]
    },
    'immutability_status': {
        'weight': 10,
        'criteria': [
            'crystallized_decisions_protected',
            'evolution_protection_marked',
            'user_authority_preserved',
            'modification_restrictions_clear'
        ]
    }
}
```

## Contamination Detection

### Zero Tolerance Protocol
```python
def detect_voice_contamination(document):
    contamination_checks = {
        'system_voice_infiltration': scan_for_ai_voice(document),
        'interpretation_injection': scan_for_interpretations(document),
        'bias_contamination': scan_for_bias_injection(document),
        'paraphrasing_detection': scan_for_paraphrasing(document),
        'context_modification': scan_for_context_changes(document)
    }
    
    return {
        'contamination_detected': any(contamination_checks.values()),
        'contamination_details': contamination_checks,
        'purity_score': calculate_voice_purity(contamination_checks)
    }
```

## Output Structure
```json
{
  "voice_validation_complete": true,
  "voice_preservation_score": 56,
  "voice_gate_status": "PASSED",
  "voice_breakdown": {
    "quote_accuracy": 10,
    "intent_fidelity": 9,
    "context_completeness": 10,
    "source_traceability": 9,
    "attribution_clarity": 9,
    "immutability_status": 9
  },
  "contamination_detection": {
    "contamination_detected": false,
    "voice_purity_score": 98,
    "zero_contamination_verified": true
  },
  "voice_separation_audit": {
    "complete_separation": true,
    "clear_boundaries": true,
    "attribution_accuracy": true
  },
  "ready_for_completion": true
}
```

## Integration Points
- **INPUT**: Quality validation results from verify-doc-quality
- **OUTPUT**: Voice validation results for verify-doc-completion
- **THRESHOLD**: Voice preservation score ≥54/60 (90%+ required)

---
**Function**: Mandatory voice preservation validation with zero contamination tolerance