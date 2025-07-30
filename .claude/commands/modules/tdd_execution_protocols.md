# TDD Execution Protocols Module

## Phase 1: Objective Establishment Template
**Behavior**: Clear goal definition + success criteria establishment
**Method**:
- **Objective establishment**: Define clear, measurable goal from planning phase
- **Success criteria definition**: Establish specific, testable completion metrics
- **Validation framework**: Create tests that verify objective achievement
- **Recursive strategy**: Define failure handling and retry methodology

## Phase 2: Git WorkTree Integration Template
**Behavior**: Safe experimentation with disposable branches
**Method**:
- **Conversation-level branching**: Each conversation starts in Git WorkTree
- **Experimental control**: Safe experimentation without main branch contamination
- **Granular change management**: Specific control of each implementation attempt
- **Disposable option**: WorkTree can be discarded if experiment fails

## Phase 3: TDD Implementation Loop Template
**Behavior**: Recursive implementation until success criteria met
**Method**:
1. **Implementation loop**: Agent/subagent systematic execution
2. **Validation cycle**: Test against established success criteria
3. **Recursive retry**: IF criteria not met → restart implementation process
4. **Success condition**: Continue until success OR declare impossible
5. **Quality gates**: Apply creation→alignment→verification throughout

## Task Tool Templates

### Implementation Template
```
Task(
  description: "Implementation execution",
  prompt: "Act as implementation specialist. Load context from @context/vision/simplicity.md. Execute development following quality gates and anti-pattern prevention. Apply TDD methodology with success criteria: [specific criteria]. Use Git WorkTree for safe experimentation.",
  subagent_type: "general-purpose"
)
```

### Validation Template
```
Task(
  description: "TDD validation",
  prompt: "Act as validation specialist. Load context from @context/architecture/core/truth-source.md. Test implementation against success criteria: [criteria]. Apply recursive validation protocol. Report success/failure with specific evidence.",
  subagent_type: "general-purpose"
)
```

## Git WorkTree Setup Template
```bash
git worktree add ../experiment-branch
cd ../experiment-branch
# Implementation work here
# If successful: merge changes
# If failed: remove worktree
```

## Recursive Validation Protocol Template

### Success Path
1. **Implementation complete** → Test against success criteria
2. **Criteria met** → Validate quality gates
3. **Quality approved** → Merge to main branch
4. **Documentation updated** → Session closure preparation

### Failure Path
1. **Implementation complete** → Test against success criteria  
2. **Criteria not met** → Analyze failure reasons
3. **Strategy adjustment** → Modify approach based on failure analysis
4. **Recursive retry** → Restart implementation with adjusted strategy
5. **Max iterations** → If repeated failures, escalate or declare impossible

## Success Criteria Examples Template
- **Functionality**: Feature works as specified in discovery phase
- **Quality**: Code passes linting, type checking, tests
- **Integration**: Changes don't break existing functionality
- **User validation**: Meets original user intent from discovery
- **Documentation**: Implementation properly documented

**Usage**: TDD workflow with Git WorkTree integration and recursive validation