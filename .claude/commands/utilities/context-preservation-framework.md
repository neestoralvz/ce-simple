---
contextflow:
  purpose: "Context preservation framework for seamless workflow progression"
  type: "utility-system"
  integration: "workflow-state-manager"
---

# Context Preservation Framework

## Context Data Structure

### Complete Context Package:
```json
{
  "context_id": "ctx-{workflow_id}",
  "preservation_timestamp": "2025-07-28T12:00:00Z",
  "user_context": {
    "original_request": "exact user input",
    "user_voice_quotes": [
      "quote 1 with attribution",
      "quote 2 with attribution"
    ],
    "user_intent": "distilled core intent",
    "context_source": "synthesis file | conversation reference"
  },
  "document_context": {
    "document_type": "command|rule|methodology|template",
    "target_location": "/intended/deployment/path",
    "file_naming": "determined naming convention",
    "metadata_requirements": {
      "contextflow_fields": ["purpose", "workflow-step", "etc"],
      "integration_points": ["command references", "imports"]
    }
  },
  "workflow_context": {
    "step_progression": [
      {
        "step": 1,
        "command": "create-doc",
        "specialist_outputs": {
          "research_findings": "...",
          "content_structure": "...",
          "voice_preservation": "...",
          "architecture_validation": "..."
        },
        "document_state": "file path and content snapshot"
      }
    ],
    "decision_points": [
      {
        "decision": "token economy optimization approach",
        "chosen_path": "dense information preservation",
        "rationale": "user preference for comprehensive coverage"
      }
    ]
  }
}
```

## Context Handoff Protocol

### Step-to-Step Context Transfer:
```markdown
CREATE-DOC → ALIGN-DOC HANDOFF:

PRESERVED ELEMENTS:
- Original user request (exact wording)
- User voice quotes with context
- Document type and target location
- Content specialist outputs
- Research findings and patterns
- Token economy decisions made
- Metadata structure established

HANDOFF PACKAGE:
Task: Context Handoff Manager
Description: "Transfer context from create-doc to align-doc"
Subagent: general-purpose
Prompt: "Preserve complete context for align-doc step:

CONTEXT PACKAGE:
- User Request: {original_request}
- Voice Quotes: {preserved_quotes}
- Created Document: {document_path_and_content}
- Specialist Insights: {research_and_content_outputs}
- Decisions Made: {token_economy_and_structure_choices}

ALIGNMENT TARGET:
Execute /align-doc with this complete context package."
```

### Context Validation Checkpoints:
```markdown
PRE-STEP CONTEXT VALIDATION:
Task: Context Integrity Validator
Description: "Validate context preservation before {next_step}"
Subagent: general-purpose
Prompt: "Validate context integrity:

VALIDATION REQUIREMENTS:
✓ User voice quotes exactly preserved
✓ Original intent maintained through transformations
✓ Document progression logically consistent
✓ No context loss during specialist handoffs
✓ Metadata continuity maintained
✓ Decision rationale preserved

VALIDATION OUTPUT:
- PASS: Context integrity confirmed
- WARN: Minor context drift detected (with corrections)
- FAIL: Major context loss (require rollback)"
```

## User Voice Preservation Protocol

### Voice Preservation Standards:
```markdown
VOICE PRESERVATION RULES:
1. EXACT QUOTES: Never paraphrase user decisions
2. CONTEXT ATTRIBUTION: Maintain quote source and timing
3. INTENT PRESERVATION: Core meaning unchanged through workflow
4. DECISION INTEGRITY: User choices preserved through optimizations
5. LANGUAGE CONSISTENCY: Maintain user's terminology preferences

VOICE VALIDATION CHECKPOINTS:
- After content specialist processing
- Before alignment validator changes
- Post architecture validation corrections
- Final quality assurance review
```

### Voice Preservation Task Implementation:
```markdown
VOICE PRESERVATION VALIDATOR:
Task: Voice Preservation Specialist
Description: "Validate user voice preservation in {current_step}"
Subagent: general-purpose
Prompt: "Voice preservation validation:

ORIGINAL USER VOICE:
{exact_user_quotes_with_context}

CURRENT DOCUMENT STATE:
{document_after_processing}

VALIDATION CHECKLIST:
✓ User quotes exactly preserved in document
✓ Original decisions maintained in implementation
✓ User terminology consistently used
✓ Intent clarity preserved through optimizations
✓ No distortion from specialist processing

OUTPUT:
- Voice integrity score (1-100)
- Specific preservation violations (if any)
- Recommended corrections (if needed)"
```

## Decision Context Tracking

### Decision Preservation System:
```markdown
DECISION TRACKING STRUCTURE:
{
  "decisions_made": [
    {
      "decision_point": "document structure approach",
      "user_input": "I want this to be comprehensive but concise",
      "interpretation": "dense information with token economy optimization",
      "implementation": "50-80 line core with detailed sections",
      "step_applied": 1,
      "preserved_through": [2, 3]
    }
  ]
}

DECISION CONTINUITY VALIDATION:
- Track each decision through workflow steps
- Ensure implementation consistency
- Validate no decision contradictions introduced
- Maintain decision rationale accessibility
```

## Context Recovery Mechanisms

### Context Loss Recovery:
```markdown
CONTEXT RECOVERY PROTOCOL:
IF context_validation_failed:
  
RECOVERY ACTIONS:
1. RETRIEVE original context from workflow state
2. IDENTIFY specific context loss points
3. RESTORE lost context elements
4. VALIDATE recovery completeness
5. CONTINUE workflow with restored context

RECOVERY TASK IMPLEMENTATION:
Task: Context Recovery Specialist
Description: "Recover lost context for workflow continuation"
Subagent: general-purpose
Prompt: "Context recovery required:

DETECTED LOSS:
{specific_context_elements_lost}

ORIGINAL CONTEXT:
{complete_preserved_context_package}

RECOVERY ACTIONS:
1. Restore lost elements to current document
2. Re-establish context continuity
3. Validate no additional loss occurred
4. Update workflow state with recovery log
5. Continue auto-chain progression with full context"
```

## Integration with Auto-Chaining

### Context-Aware Auto-Chain Triggers:
```markdown
AUTO-CHAIN CONTEXT REQUIREMENTS:
BEFORE auto-chain trigger:
1. Context preservation validated ✓
2. User voice integrity confirmed ✓
3. Decision continuity maintained ✓
4. Document state consistent ✓
5. Next step context package prepared ✓

CONTEXT PACKAGE FOR NEXT STEP:
- Complete preserved context
- Current step outputs
- Context validation results
- Any context corrections applied
- Next step specific requirements
```

---
**Integration**: Auto-imported by all workflow commands for context continuity