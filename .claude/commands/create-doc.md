---
contextflow:
  purpose: "Creación documento via Content Specialist subagent"
  workflow-step: 1
  next: ["align-doc"]
  requires-subagent: true
  auto-chain: true
  research-driven: true
---

# Comando `/create-doc` - Workflow Step 1

## Document Creation Orchestration

**INSTRUCCIÓN**: Deploy document creation specialists using template references

### Specialist Deployment (Condicional)
**SI documento requiere research → Deploy Research Specialist**
**SI documento complejo → Deploy full specialist suite**
**SI documento básico → Deploy Content + Voice Preservation only**

### Template References
```
Task: Research Specialist (from ../templates/research-specialist.md)
Description: "Document type best practices research"
Focus: {document_type} structure + optimization patterns

Task: Content Optimizer (from ../templates/content-optimizer.md)  
Description: "Generate core document using research"
Focus: User voice integration + token economy + metadata

Task: Voice Preservation (from ../templates/voice-preservation.md)
Description: "MANDATORY voice separation compliance"
Focus: synthesis-voice-separation.md template enforcement

Task: Architecture Validator (from ../templates/architecture-validator.md)
Description: "System integration validation"
Focus: Contextflow metadata + conflict detection
```

### Voice Preservation Requirements
**Template**: synthesis-voice-separation.md (enforced via template)
**Score minimum**: ≥54/60 (validated by Voice Preservation specialist)
**Separation**: User voice vs system analysis (template-enforced)
**Attribution**: Source linking (automatic via specialist)

**Main Agent**: Consolidate specialist outputs → Generate final document

## Input Requirements:
- **Document type**: Command, rule, methodology, template
- **Core content**: User voice quotes + requirements
- **Context source**: Synthesis file o conversation reference

## Output Structure:
```markdown
---
contextflow:
  source: "[origen-synthesis-o-conversation]"
  user-voice-score: "[X/60 - must be ≥54 for approval]"
  voice-separation: "ENFORCED"
  created-by: "content-specialist-subagent"
  template-used: "synthesis-voice-separation.md"
---

# [Título]

## 👤 USER VOICE - FUENTE DE VERDAD ABSOLUTA (IMMUTABLE)
> "[cita exacta usuario 1]" - Source: [/path/to/source.md:line-X]
> "[cita exacta usuario 2]" - Source: [/path/to/source.md:line-Y]

**CRYSTALLIZED DECISIONS (NO EVOLUTION ALLOWED):**
- Decision: "[exact user words]"
- Status: IMMUTABLE

## 📊 SYSTEM ANALYSIS (INTERPRETATION - SEPARATE FROM USER VOICE)
[System analysis and implementation guidance]

## 🔗 VOICE PRESERVATION AUDIT
**TOTAL VOICE PRESERVATION SCORE: [X/60]** - Must be ≥54

---
**Ready for**: `/align-doc` - Architecture validation with voice preservation verified
```

## Auto-Chain Logic (Condicional)

**Workflow progression**: create-doc → align-doc (si documento complejo)
**State management**: Via ../utilities/document-workflow-orchestrator.md
**Trigger conditions**: Document quality > basic threshold

### Auto-Chain Implementation
```
IF document_creation_success AND complexity > basic:
  → Execute /align-doc con workflow context
  → Pass document_path + user_context + specialist_results
  
IF creation_errors OR user_intervention_required:
  → Pause auto-chain
  → Require manual continuation
```

## Success Criteria
- [ ] Specialists deployed via template references
- [ ] Voice preservation score ≥54/60
- [ ] Document structure compliant
- [ ] Auto-chain logic functional
- [ ] Token economy optimized (50-80 lines)

---
**Workflow**: CREATE → Align → Verify