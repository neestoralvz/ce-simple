---
contextflow:
  purpose: "Alineamiento documento via Architecture Validator subagent"
  workflow-step: 2
  prev: ["create-doc"]
  next: ["verify-doc"]
  requires-subagent: true
  auto-chain: true
  research-driven: true
  factorized: true
  auxiliary-commands:
    - align-doc-architecture
    - align-doc-voice
    - align-doc-completion
---

# Comando `/align-doc` - Workflow Step 2

## Document Alignment Orchestration

**INSTRUCCIÓN**: Deploy alignment specialists via auxiliary commands

### Modular Alignment Flow
```python
# Step 1: Architecture Validation
architecture_results = EXECUTE("/align-doc-architecture", document_input)

# Step 2: Voice Preservation Validation
voice_results = EXECUTE("/align-doc-voice", architecture_results)

# Step 3: Alignment Completion
EXECUTE("/align-doc-completion", voice_results)
```

## Auxiliary Commands
- [@align-doc-architecture.md] - Architecture validation and consistency
- [@align-doc-voice.md] - Voice preservation validation
- [@align-doc-completion.md] - Alignment completion and auto-chain


## Alignment Verification (Modular)
- Consistency check: Principles, decisions, architecture
- Integration validation: No conflicts con sistema existente
- User voice preservation: Intent maintenance sin distorsión
- Standards compliance: Token economy + context loading

## Output Format
```markdown
## Alignment Complete
### ✅ Aligned: [corrections applied]
### ⚠️ Issues: [resolved]
---
**Status**: Ready for `/verify-doc`
```

## Auto-Chain Logic
```python
IF alignment_success AND no_major_issues:
    EXECUTE("/verify-doc", aligned_document)
ELSE:
    REQUIRE user intervention
```

## Success Criteria
- [ ] Architecture validation completed
- [ ] Voice preservation maintained ≥54/60
- [ ] Token economy compliance
- [ ] Auto-chain to verify-doc functional

## Factorization Benefits
- Token Economy: Main <80 lines, auxiliaries ~50-80 lines
- Functionality preserved via modular execution
- Self-contained ecosystem per user vision

---
**Workflow**: Create → ALIGN → Verify