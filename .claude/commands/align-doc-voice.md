---
contextflow:
  purpose: "Voice preservation validation during document alignment process"
  parent-command: "align-doc"
  auxiliary: true
  input-format: "architecture-results"
  output-format: "voice-results"
  research-driven: false
---

# Auxiliary Command `/align-doc-voice`

## Purpose
Validate user voice preservation during document alignment process ensuring no distortion occurs.

## Voice Preservation Framework

### Core Voice Functions
```python
def execute_alignment_voice_validation(architecture_results):
    return {
        'voice_integrity_check': validate_voice_integrity(architecture_results.document),
        'alignment_impact_assessment': assess_alignment_voice_impact(architecture_results),
        'distortion_detection': detect_voice_distortion(architecture_results.document),
        'score_preservation': validate_score_preservation(architecture_results.document),
        'correction_compatibility': validate_correction_voice_compatibility(architecture_results)
    }
```

### Voice Integrity Validation
```python
def validate_voice_integrity(document):
    return {
        'user_voice_unchanged': verify_voice_unchanged(document),
        'quote_accuracy_maintained': verify_quotes_intact(document),
        'intent_preservation': verify_intent_preserved(document),
        'context_maintained': verify_context_intact(document)
    }
```

### Alignment Impact Assessment
```python
def assess_alignment_voice_impact(architecture_results):
    return {
        'corrections_impact_on_voice': assess_correction_voice_impact(architecture_results.corrections),
        'architecture_changes_voice_safe': verify_architecture_changes_safe(architecture_results),
        'metadata_changes_voice_neutral': verify_metadata_changes_neutral(architecture_results),
        'voice_score_trajectory': predict_voice_score_impact(architecture_results)
    }
```

### Task Tools Deployment
```python
# Voice Preservation Validator
Task(
    description="Validate user voice preservation during alignment corrections",
    prompt="""Actúa como Voice Preservation Validator. ALIGNMENT VOICE MISSION: Ensure voice integrity.

ALIGNMENT CONTEXT:
- Document content: {architecture_results.document}
- Architecture corrections: {architecture_results.corrections}
- Validation results: {architecture_results.validation}
- Proposed changes: {architecture_results.changes}

VOICE PRESERVATION VALIDATION:
1. Voice Integrity Analysis:
   - User voice sections unchanged by alignment
   - Quote accuracy maintained through corrections
   - Intent preservation despite architectural changes
   - Context completeness maintained

2. Alignment Impact Assessment:
   - Architecture corrections don't affect user voice
   - Metadata changes are voice-neutral
   - System improvements preserve voice integrity
   - Score trajectory remains ≥54/60

3. Distortion Detection:
   - No voice contamination from system changes
   - No interpretation injection during alignment
   - No paraphrasing introduced by corrections
   - No context modification affecting voice

4. Correction Compatibility:
   - All proposed corrections are voice-safe
   - Architecture improvements don't distort voice
   - Integration changes preserve voice separation
   - Standards compliance maintains voice integrity

VOICE SCORING VALIDATION:
- Voice Integrity: /15 points
- Alignment Impact: /15 points
- Distortion Prevention: /15 points
- Correction Compatibility: /15 points
- TOTAL: /60 points (54+ maintained required)

OUTPUT: Voice preservation validation with alignment compatibility assessment.""",
    subagent_type="general-purpose"
)
```

## Voice Distortion Detection

### Distortion Scanning
```python
def detect_voice_distortion(document):
    distortion_checks = {
        'alignment_induced_contamination': scan_alignment_contamination(document),
        'correction_voice_impact': scan_correction_voice_impact(document),
        'metadata_voice_interference': scan_metadata_interference(document),
        'integration_voice_pollution': scan_integration_pollution(document)
    }
    
    return {
        'distortion_detected': any(distortion_checks.values()),
        'distortion_sources': distortion_checks,
        'voice_purity_maintained': calculate_voice_purity_post_alignment(distortion_checks)
    }
```

### Score Preservation Validation
```python
def validate_score_preservation(document):
    current_score = calculate_current_voice_score(document)
    
    return {
        'current_voice_score': current_score,
        'score_threshold_met': current_score >= 54,
        'score_trajectory': predict_score_after_alignment(document),
        'preservation_assured': current_score >= 54 and predict_score_after_alignment(document) >= 54
    }
```

## Correction Voice Compatibility

### Voice-Safe Corrections
```python
def validate_correction_voice_compatibility(architecture_results):
    voice_safe_corrections = []
    voice_risky_corrections = []
    
    for correction in architecture_results.corrections:
        if is_voice_safe_correction(correction):
            voice_safe_corrections.append(correction)
        else:
            voice_risky_corrections.append(correction)
    
    return {
        'voice_safe_corrections': voice_safe_corrections,
        'voice_risky_corrections': voice_risky_corrections,
        'all_corrections_voice_safe': len(voice_risky_corrections) == 0,
        'voice_protection_recommendations': generate_voice_protection_recommendations(voice_risky_corrections)
    }
```

## Voice Scoring During Alignment

### Alignment Voice Scoring
```python
alignment_voice_scoring = {
    'voice_integrity': {
        'weight': 15,
        'criteria': [
            'user_voice_unchanged',
            'quote_accuracy_maintained',
            'intent_preservation',
            'context_maintained'
        ]
    },
    'alignment_impact': {
        'weight': 15,
        'criteria': [
            'corrections_voice_neutral',
            'architecture_changes_safe',
            'metadata_changes_neutral',
            'score_trajectory_positive'
        ]
    },
    'distortion_prevention': {
        'weight': 15,
        'criteria': [
            'no_contamination_detected',
            'no_interpretation_injection',
            'no_paraphrasing_introduced',
            'no_context_modification'
        ]
    },
    'correction_compatibility': {
        'weight': 15,
        'criteria': [
            'corrections_voice_safe',
            'improvements_preserve_voice',
            'integration_maintains_separation',
            'standards_preserve_integrity'
        ]
    }
}
```

## Output Structure
```json
{
  "voice_validation_complete": true,
  "voice_preservation_score": 56,
  "voice_status": "PRESERVED",
  "voice_integrity": {
    "user_voice_unchanged": true,
    "quotes_intact": true,
    "intent_preserved": true,
    "context_maintained": true
  },
  "alignment_impact": {
    "corrections_voice_safe": true,
    "score_trajectory": "stable",
    "distortion_prevented": true
  },
  "correction_compatibility": {
    "all_corrections_voice_safe": true,
    "voice_protection_applied": true
  },
  "ready_for_completion": true
}
```

## Integration Points
- **INPUT**: Architecture validation results from align-doc-architecture
- **OUTPUT**: Voice validation results for align-doc-completion
- **THRESHOLD**: Voice preservation score ≥54/60 maintained

---
**Function**: Voice preservation validation ensuring alignment process maintains voice integrity