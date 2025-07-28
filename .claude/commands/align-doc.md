---
contextflow:
  purpose: "Alineamiento documento via Architecture Validator subagent"
  workflow-step: 2
  prev: ["create-doc"]
  next: ["verify-doc"]
  requires-subagent: true
  auto-chain: true
---

# Comando `/align-doc` - Workflow Step 2

## Subagent Orchestration OBLIGATORIA

**NUNCA validar alignment directamente** - SIEMPRE via Task tool con Architecture Validator.

### Task Tools Deployment Paralelo:
```
EJECUTAR simultáneamente en mismo mensaje:

Task 1: Architecture Validator - "Validar consistency con sistema core"
Task 2: Research Specialist - "Benchmark alignment practices + anti-patterns"
Task 3: Voice Preservation - "Verify user voice maintained through changes"
Task 4: Content Optimizer - "Check token economy + structure compliance"
```

**Main agent consolida validation results y aplica corrections necesarias.**

## Alignment Verification:
- **Consistency check**: Principles, decisions, architecture
- **Integration validation**: No conflicts con sistema existente
- **User voice preservation**: Intent maintenance sin distorsión
- **Standards compliance**: Token economy + context loading

## Output Format:
```markdown
## Alignment Validation Results

### ✅ Aligned Correctly:
- [aspecto 1 correcto]
- [aspecto 2 correcto]

### ⚠️ Alignment Issues:
- **Issue 1**: [descripción] → [correction needed]
- **Issue 2**: [descripción] → [correction needed]

### 🔄 Corrections Applied:
[Documento corregido con changes tracked]

---
**Status**: Ready for `/verify-doc` - Quality validation
```

## Auto-Chaining Implementation:

```markdown
IMPORT: @/.claude/commands/utilities/workflow-state-manager.md

WORKFLOW STATE CONTINUATION:
1. RECEIVE workflow_id from create-doc step
2. LOAD existing workflow state
3. UPDATE current_step: 2
4. VALIDATE document_path continuity
5. PRESERVE user_context throughout alignment

POST-ALIGNMENT AUTO-CHAIN LOGIC:
IF alignment_validation_success AND no_major_issues:
  → UPDATE workflow state (step 2 completed)
  → STORE aligned_document_path
  → STORE validation_results for next step
  → AUTO-EXECUTE: Task tool with verify-doc command
  → PASS: workflow_id + aligned_document + validation_context
  
IF minor_issues_found:
  → AUTO-APPLY corrections via subagent
  → UPDATE document with corrections
  → LOG corrections in workflow state
  → CONTINUE auto-chain to verify-doc with corrected document
  
IF major_conflicts_detected:
  → SET error_state: "major_alignment_conflict"
  → PAUSE auto-chain progression
  → REQUIRE user decision for conflict resolution
  → PRESERVE state for potential rollback to create-doc
```

### Auto-Chain Task Tool Implementation:
```markdown
SUCCESS SCENARIO TRIGGER:
Task: Workflow Coordinator
Description: "Auto-chain to verify-doc step"
Subagent: general-purpose
Prompt: "Execute /verify-doc command with workflow state:
- workflow_id: {workflow_id}
- document_path: {aligned_document_path}
- alignment_results: {validation_summary}
- corrections_applied: {corrections_log}
- user_context: {preserved_original_context}

Auto-chain enabled - proceed immediately to quality verification."

MINOR ISSUES SCENARIO:
Task: Auto-Correction Specialist
Description: "Apply minor corrections and continue chain"
Subagent: general-purpose  
Prompt: "Apply these minor corrections: {issues_list}
Then auto-chain to verify-doc with corrected document."
```

## Success Criteria + Auto-Chain Triggers:
- [ ] Architecture Validator deployed via Task tool
- [ ] System consistency verified
- [ ] Integration conflicts resolved (or flagged for user decision)
- [ ] User voice preserved through corrections
- [ ] Workflow state updated with alignment results
- [ ] Document corrections logged for traceability
- [ ] Auto-chain to verify-doc triggered (or paused if major conflicts)
- [ ] Context handoff to final verification step complete

---
**Workflow**: Create → ALIGN → Verify