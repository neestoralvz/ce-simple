# /workflows:execute - TDD Execution + Validation

**29/07/2025 23:00 CDMX** | Test-driven execution + recursive validation workflow

## Command Purpose
Execute TDD workflow (recursive validation until success) with Git WorkTree integration for safe experimentation and systematic implementation.

**LOAD:** @context/architecture/core/methodology.md

## Execution Protocol

### Phase 1: Objective Establishment
**Authority**: @context/architecture/core/methodology.md
**Behavior**: Clear goal definition + success criteria establishment
**Method**:
- **Objective establishment**: Define clear, measurable goal from planning phase
- **Success criteria definition**: Establish specific, testable completion metrics
- **Validation framework**: Create tests that verify objective achievement
- **Recursive strategy**: Define failure handling and retry methodology

### Phase 2: Git WorkTree Integration
**Authority**: @context/architecture/core/methodology.md
**Behavior**: Safe experimentation with disposable branches
**Method**:
- **Conversation-level branching**: Each conversation starts in Git WorkTree
- **Experimental control**: Safe experimentation without main branch contamination
- **Granular change management**: Specific control of each implementation attempt
- **Disposable option**: WorkTree can be discarded if experiment fails

### Phase 3: TDD Implementation Loop
**Authority**: `discovery_execution_flow.md:87-91`
**Behavior**: Recursive implementation until success criteria met
**Method**:
1. **Implementation loop**: Agent/subagent systematic execution
2. **Validation cycle**: Test against established success criteria
3. **Recursive retry**: IF criteria not met → restart implementation process
4. **Success condition**: Continue until success OR declare impossible
5. **Quality gates**: Apply creation→alignment→verification throughout

## Multi-Conversation Orchestration → /modules:tdd_execution_protocols

## Task Tool Integration → /modules:tdd_execution_protocols

## Git WorkTree Setup → /modules:tdd_execution_protocols

## Recursive Validation Protocol → /modules:tdd_execution_protocols

## Success Criteria Examples → /modules:tdd_execution_protocols

## Core Function
TDD workflow execution with Git WorkTree integration and recursive validation until success criteria met

**Features**: Multi-conversation orchestration + Task tool integration + Anti-patterns prevention + Quality gates enforcement

**Usage**: `/workflows:execute` (requires completed `/workflows:plan` with success criteria)

---
**Authority**: @context/architecture/core/methodology.md
**Integration**: `/workflows:start` → `/workflows:plan` → `/workflows:execute`
**Dependencies**: Git WorkTree, task_tool_methodology.md, simplicity_principles.md