# w-execute - TDD Execution & Validation

**31/07/2025 00:00 CDMX** | Test-driven execution + recursive validation workflow

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

## Task Tool Integration
**When to delegate**: Complex implementations requiring specialized expertise
**Template**: Use systematic delegation with recursive validation patterns
**Quality gates**: All subagents must pass validation before completion

## Git WorkTree Setup
- **Branch creation**: Automatic experimental branch per conversation
- **Isolation**: Changes contained until success validation
- **Cleanup**: Automatic disposal if experiment fails
- **Integration**: Merge only on complete success

## Recursive Validation Protocol
1. **Attempt implementation** using planned methodology
2. **Test against success criteria** systematically
3. **IF failure detected** → analyze root cause + retry with improvements
4. **IF success achieved** → proceed to integration
5. **IF impossible** → escalate to user with recommendations

## Usage Pattern
```
w-execute
```
(Requires completed `w-plan` with success criteria)

TDD execution → Recursive validation → Success achievement → Ready for `w-close`

## Success Criteria
- **Objective achievement**: All planned goals successfully implemented
- **Quality validation**: All quality gates passed
- **Test compliance**: All tests pass successfully
- **Integration ready**: Safe for main branch integration