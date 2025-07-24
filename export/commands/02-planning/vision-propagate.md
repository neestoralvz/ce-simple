# vision-propagate

## Purpose

Propagates changes from docs/vision/ throughout the entire system ensuring docs/core/, commands/, and CLAUDE.md reflect the absolute authority of user vision without LLM interpretation.

## Principles

- **Vision Authority**: docs/vision/ is the single source of truth for all system direction
- **Cascade Updates**: Changes flow vision → core → commands → CLAUDE.md
- **Preservation Integrity**: User intent preserved exactly without LLM modifications
- **System Consistency**: All system components align with current vision state

## Execution Process

### Phase 1: Vision Analysis
Mark "Vision Document Analysis and Change Detection" as in_progress using TodoWrite

Execute comprehensive vision analysis:
- Agent 1: Read all docs/vision/ files and identify current vision state
- Agent 2: Compare vision content against docs/core/ for alignment gaps
- Agent 3: Analyze commands/ directory for vision inconsistencies  
- Agent 4: Review CLAUDE.md for vision representation accuracy

Generate change propagation matrix:
- Identify which core documents need updates based on vision changes
- Map vision concepts to affected command categories
- Determine CLAUDE.md sections requiring updates

### Phase 2: Core Documentation Update
Mark "Core Documentation Propagation" as in_progress using TodoWrite

Execute core documentation updates:
- Agent 1: Update docs/core/system-principles.md based on vision principles
- Agent 2: Update docs/core/task-orchestration.md with vision workflow requirements
- Agent 3: Update docs/core/context-architecture.md with vision-driven patterns
- Agent 4: Update docs/core/evolution-learning.md with vision adaptation protocols

Validate core updates:
- Ensure core documents accurately reflect vision without interpretation
- Cross-reference core updates for internal consistency
- Verify core documents maintain technical accuracy while following vision

### Phase 3: Command System Update
Mark "Command System Vision Alignment" as in_progress using TodoWrite

Execute command system propagation:
- Agent 1: Identify commands requiring updates based on vision changes
- Agent 2: Update affected commands in relevant categories (00-core, 01-discovery, etc.)
- Agent 3: Validate command purposes align with vision priorities
- Agent 4: Ensure command execution patterns follow vision-driven principles

Execute command validation:
- Verify commands maintain ≤150 line limit while incorporating vision updates
- Ensure command orchestration follows vision-defined workflows
- Validate command descriptions accurately reflect vision priorities

### Phase 4: CLAUDE.md Integration
Mark "CLAUDE.md Vision Integration and System Update" as in_progress using TodoWrite

Execute CLAUDE.md comprehensive update:
- Update system overview to prioritize vision authority
- Add Vision-Driven Development section establishing docs/vision/ supremacy
- Update command descriptions to reflect vision-aligned priorities
- Ensure all system documentation references flow from vision authority

Execute final system validation:
- Cross-reference entire system for vision consistency
- Validate that all components point to docs/vision/ as authority
- Ensure user intent is preserved throughout all system levels
- Confirm no LLM interpretations override user vision

Complete all tasks using TodoWrite

---

**Vision-driven system propagation ensuring complete alignment from user intent to system implementation.**