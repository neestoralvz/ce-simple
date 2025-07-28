---
contextflow:
  purpose: "Verificación final via Quality Assurance subagent"
  workflow-step: 3
  prev: ["align-doc"]
  workflow-complete: true
  requires-subagent: true
  research-driven: true
  factorized: true
  auxiliary-commands:
    - verify-doc-quality
    - verify-doc-voice
    - verify-doc-completion
---

# Comando `/verify-doc` - Workflow Step 3 (Final)

## Document Verification Orchestration

**INSTRUCCIÓN**: Deploy verification specialists via auxiliary commands

### Modular Verification Flow
```python
# Step 1: Quality Gates Verification
quality_results = EXECUTE("/verify-doc-quality", document_input)

# Step 2: Voice Preservation Validation  
voice_results = EXECUTE("/verify-doc-voice", quality_results)

# Step 3: Workflow Completion
EXECUTE("/verify-doc-completion", voice_results)
```

## Auxiliary Commands
- [@verify-doc-quality.md] - Quality gates and technical validation
- [@verify-doc-voice.md] - Voice preservation scoring and validation
- [@verify-doc-completion.md] - Workflow completion and deployment


## Quality Gates (Modular)

### Technical Validation
- Token economy: Core file ≤80 líneas
- Context metadata: Complete decision tree
- No duplication: Unique vs existing docs
- Links structure: Conditional links vs imports

### Voice Preservation (MANDATORY)
- Voice separation: Complete user voice vs system analysis separation
- Quote accuracy: Zero paraphrasing - exact user words only
- Source attribution: Every quote linked to original source
- Scoring compliance: Voice preservation score ≥54/60 (90%+ required)

## Verification Output
```markdown
## 🎯 Document Verification Complete

### Quality Score: [X/100]
### Voice Preservation Score: [X/60] - MUST BE ≥54

### ✅ Quality Gates Passed:
- Token economy: [X lines] ✓
- Voice preservation: [X/60] ✓
- No duplication: ✓
- Structure optimized: ✓

### 🎁 Final Document:
[Production-ready document]

---
**STATUS**: ✅ WORKFLOW COMPLETE
```

## Factorization Benefits
- Token Economy: Main <80 lines, auxiliaries ~50-80 lines
- Functionality preserved via modular execution
- Self-contained ecosystem per user vision
- Workflow completion maintained

---
**Workflow**: Create → Align → VERIFY ✅
**Ready for**: Immediate usage with identical functionality via modular execution