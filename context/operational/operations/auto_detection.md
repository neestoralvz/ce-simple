# Auto-Detection Module - State Detection Utilities

**29/07/2025 10:45 CDMX** | Auto-detection utilities for distillation state management

## Core Function
Hybrid auto-detection methodology for conversation processing state without file-based tracking.

## State Detection Methodology

### Hybrid Detection Strategy
**Primary detection**: Compare timestamps
```
newest_conversation=$(ls -t /conversations/*.md | head -1)
newest_nuclei=$(ls -t /layer1/*.md | head -1)
```

**Secondary detection**: Check processed lists in núcleos
```
grep -h "^- " /layer1/*/## Conversations Processed | sort -u > processed.tmp
ls /conversations/*.md | basename -s .md > available.tmp
comm -23 available.tmp processed.tmp = pending_conversations
```

**Tertiary validation**: Sample validation if timestamps match (2-3 recent conversations sampling)

## Layer Detection Logic

### Layer 1 State
**Detection criteria**: All conversations in raw/ reviewed by timestamp
- Cross-reference conversation timestamps with núcleos updates
- Verify "Conversations Processed" lists in núcleos footers
- Sample validation for recent conversations when timestamps indicate completeness

### Layer 2 State  
**Detection criteria**: All relationships between núcleos synthesized in thematic files
- Check existence of concentration synthesis files
- Validate 10+ quote consolidation in insights
- Verify evidence base references to Layer 1 sources

### Layer 3 State
**Detection criteria**: Official documentation completely reflects synthesis
- Verify methodology_guide.md, architecture_principles.md, implementation_guide.md, quick_reference.md existence
- Validate ultra-dense content quality (maximum value/token ratio)
- Check @-imports optimization readiness

## Convergence Detection

### Completion Criteria by Layer
**Layer 1 complete**: All raw/ conversations timestamp-verified + processed lists complete
**Layer 2 complete**: All núcleos relationships synthesized + concentration quality validated
**Layer 3 complete**: Ultra-dense documentation complete + @-imports ready
**TRUTH_SOURCE complete**: Supreme authority integrates all layers

### Auto-Termination Logic
**Completion message**: "Destilación completa - Todo el corpus conversacional procesado y sintetizado"
**Convergence validation**: Multi-method state verification before completion declaration

## Progress Reporting

### Conversational Progress Only
**Durante cada iteración**:
- "Procesando conversación [timestamp]..."
- "Núcleos actualizados: metodologia_socratica.md (+3 insights)"
- "Revisando hasta: 20250729 (2 conversaciones pendientes)"

**PROHIBITED**: Create tracking files, reports, or permanent state files
**STATE MANAGEMENT**: Conversational only - no persistent tracking beyond núcleos footers

---
**Integration:** Referenced by /workflows:distill orchestrator for state management
**Dependencies:** Conversations directory, existing núcleos structure
**Output:** State assessment without persistent tracking file creation