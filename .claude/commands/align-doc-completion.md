---
contextflow:
  purpose: "Alignment completion and auto-chain logic for document alignment workflow"
  parent-command: "align-doc"
  auxiliary: true
  input-format: "voice-results"
  output-format: "completion-results"
  research-driven: false
---

# Auxiliary Command `/align-doc-completion`

## Purpose
Execute alignment completion, apply corrections, and manage auto-chain logic for document alignment workflow.

## Completion Logic Framework

### Alignment Completion Functions
```python
def execute_alignment_completion(voice_results):
    if voice_results.alignment_success and voice_results.voice_preserved:
        return execute_successful_alignment(voice_results)
    elif voice_results.minor_issues_only and voice_results.voice_score >= 54:
        return execute_auto_correction_alignment(voice_results)
    else:
        return execute_alignment_pause_for_intervention(voice_results)
```

### Successful Alignment Path
```python
def execute_successful_alignment(voice_results):
    return {
        'alignment_status': 'completed',
        'corrections_applied': apply_voice_safe_corrections(voice_results.corrections),
        'document_ready': prepare_aligned_document(voice_results.document),
        'auto_chain_ready': True,
        'next_step': 'verify-doc'
    }
```

### Auto-Correction Path
```python
def execute_auto_correction_alignment(voice_results):
    return {
        'alignment_status': 'auto_corrected',
        'minor_corrections_applied': apply_minor_corrections(voice_results.minor_issues),
        'voice_integrity_maintained': voice_results.voice_score >= 54,
        'document_corrected': generate_corrected_document(voice_results),
        'auto_chain_ready': True,
        'next_step': 'verify-doc'
    }
```

### Task Tools Deployment

#### Successful Alignment Task
```python
Task(
    description="Apply alignment corrections and prepare document for verification",
    prompt="""Actúa como Alignment Completion Specialist. COMPLETION MISSION: Finalize document alignment.

ALIGNMENT CONTEXT:
- Document: {voice_results.document}
- Architecture validation: {voice_results.architecture_validation}
- Voice preservation: {voice_results.voice_validation}
- Corrections needed: {voice_results.corrections}
- Voice score: {voice_results.voice_score} (≥54 maintained)

COMPLETION ACTIONS:
1. Apply Voice-Safe Corrections:
   - Implement architecture improvements while preserving voice
   - Apply metadata corrections without affecting user content
   - Optimize token economy while maintaining voice integrity
   - Ensure all corrections are voice-compatible

2. Document Finalization:
   - Generate aligned document with corrections applied
   - Maintain voice preservation score ≥54/60
   - Ensure architecture compliance achieved
   - Prepare document for verification workflow step

3. Auto-Chain Preparation:
   - Validate document ready for /verify-doc
   - Prepare workflow context for next step
   - Ensure seamless transition to verification
   - Document alignment success metrics

ALIGNMENT SUCCESS CRITERIA:
- Architecture validation score ≥80/100
- Voice preservation score ≥54/60 maintained
- All corrections applied successfully
- Document ready for verification

EXECUTE: Complete alignment with voice-safe corrections and prepare for verification.""",
    subagent_type="general-purpose"
)
```

#### Auto-Correction Task
```python
Task(
    description="Auto-fix minor alignment issues while preserving voice integrity",
    prompt="""Actúa como Auto-Correction Specialist. AUTO-FIX MISSION: Fix minor issues preserving voice.

AUTO-CORRECTION CONTEXT:
- Minor issues: {voice_results.minor_issues}
- Voice score: {voice_results.voice_score} (≥54 to maintain)
- Architecture score: {voice_results.architecture_score}
- Auto-fixable items: {voice_results.auto_fixable}

AUTO-CORRECTION REQUIREMENTS:
- Maintain voice preservation score ≥54/60 (MANDATORY)
- Preserve all user voice content exactly
- Apply only voice-safe corrections
- Log all fixes for transparency

MINOR FIXES APPLICATION:
1. Token economy optimizations (structure only)
2. Metadata completeness improvements
3. Reference integrity corrections
4. Context loading optimizations

POST-FIX VALIDATION:
- Verify voice score maintained ≥54/60
- Confirm architecture improvements applied
- Validate document ready for verification
- Prepare auto-chain to /verify-doc

EXECUTE: Auto-fix minor issues and prepare corrected document for verification.""",
    subagent_type="general-purpose"
)
```

#### Intervention Required Task
```python
Task(
    description="Handle major alignment issues requiring user intervention",
    prompt="""Actúa como Intervention Coordinator. INTERVENTION MISSION: Pause alignment for user guidance.

INTERVENTION CONTEXT:
- Major issues: {voice_results.major_issues}
- Voice preservation status: {voice_results.voice_status}
- Architecture conflicts: {voice_results.architecture_conflicts}
- User intervention points: {voice_results.intervention_needed}

INTERVENTION PREPARATION:
1. Preserve all user work and context
2. Document specific issues requiring resolution
3. Prepare clear guidance for user corrections
4. Maintain workflow state for resumption

USER COMMUNICATION REQUIREMENTS:
- Clear explanation of alignment issues detected
- Specific corrections needed before proceeding
- Impact on voice preservation (if any)
- Step-by-step resolution guidance
- Workflow resumption instructions

WORKFLOW PAUSE LOGIC:
- Set workflow state to "awaiting_user_intervention"
- Preserve complete document context
- Maintain alignment progress achieved
- Prepare for workflow resumption post-correction

EXECUTE: Pause alignment workflow with comprehensive user guidance.""",
    subagent_type="general-purpose"
)
```

## Auto-Chain Logic

### Auto-Chain Decision Tree
```python
def execute_auto_chain_logic(completion_results):
    if (completion_results.alignment_status == 'completed' and 
        completion_results.voice_score >= 54 and
        completion_results.architecture_score >= 80):
        
        return {
            'auto_chain_execute': True,
            'next_command': '/verify-doc',
            'workflow_context': prepare_verification_context(completion_results),
            'seamless_transition': True
        }
    else:
        return {
            'auto_chain_execute': False,
            'intervention_required': True,
            'pause_reason': determine_pause_reason(completion_results),
            'user_guidance': generate_user_guidance(completion_results)
        }
```

### Workflow Context Preparation
```python
def prepare_verification_context(completion_results):
    return {
        'aligned_document': completion_results.aligned_document,
        'alignment_corrections_log': completion_results.corrections_applied,
        'voice_preservation_verified': completion_results.voice_score >= 54,
        'architecture_validation_passed': completion_results.architecture_score >= 80,
        'workflow_step': 3,
        'ready_for_verification': True
    }
```

## Output Structure
```json
{
  "alignment_completion_status": "SUCCESS|AUTO_CORRECTED|INTERVENTION_REQUIRED",
  "completion_details": {
    "corrections_applied": [...],
    "voice_score_maintained": 56,
    "architecture_score_achieved": 83,
    "document_ready": true
  },
  "auto_chain_decision": {
    "execute_auto_chain": true,
    "next_command": "/verify-doc",
    "workflow_context": {...},
    "seamless_transition": true
  },
  "alignment_finalization": {
    "document_path": "...",
    "corrections_log": [...],
    "voice_integrity_verified": true,
    "ready_for_verification": true
  }
}
```

## Integration Points
- **INPUT**: Voice validation results from align-doc-voice
- **OUTPUT**: Alignment completion results with auto-chain decision
- **NEXT**: Auto-chain to /verify-doc if successful, or user intervention if issues

---
**Function**: Alignment completion with auto-chain logic and intervention handling