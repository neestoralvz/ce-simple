# Command Structure Standard

**Updated**: 2025-07-24 12:54 (Mexico City)  
**Authority**: Core Development Framework

## 4-Section Command Architecture

**Template**: Purpose(3-5L) | Principles(8-12L) | Execution(120-130L) | Footer(2-3L) = ≤150L total

1. **Purpose**: "Executes [function] through [method] providing [outcome] with [criteria]"
2. **Principles**: Single Responsibility | Granular Execution | Resource Management | Error Recovery
3. **Execution**: 5-Phase TodoWrite pattern with Phase 5 routing/handoff (MANDATORY)
4. **Footer**: @./docs/core/README.md architectural context links

## Writing Standards

**Word Economy**: ≤15 words/instruction | Action verbs only | Remove: should/might/perhaps/utilize
**Natural Language**: "Search TypeScript files" ✓ | `Grep('*.ts')` ✗ | Direct instructions only
**Anti-Patterns**: No code syntax | tool syntax | meta-commentary | theoretical explanations

## 5-Phase Execution Template

### Phases 1-4: Standard Task Execution
```
Phase N: [Descriptive Name]
1. TodoWrite: Mark Phase N as in_progress
2. Execute: [Specific verb] [object] [criteria]
3. Use [Tool]: [parameters] → [expected outcome]
4. Validate: [success criteria]
5. TodoWrite: Mark Phase N complete, mark Phase N+1 pending
```

### Phase 5: Routing/Handoff (MANDATORY)
```
Phase 5: Analysis and Routing
1. TodoWrite: Mark Phase 5 in_progress
2. Analyze: Current context and completed achievements
3. Review: Overall success against original objectives
4. Identify: Next logical steps in workflow progression
5. Recommend: 2-3 specific commands for continuation
6. Handoff: Prepare transition message with context summary
7. TodoWrite: Mark Phase 5 complete
```

## Tool Integration

**TodoWrite Points**: Phase start | Phase end | Phase 5 complete | Error tasks
**Tool Pattern**: Use [Tool] to [action]: [parameters] → [outcome] with [validation]

**Examples**:
✓ Use Grep to search TypeScript files: pattern="interface" → List interface definitions
✓ Use Read to examine configuration: file="/path/config.json" → Extract settings
✗ Utilize the Grep functionality to search for patterns

## Quality Validation

### Structure Compliance
- [ ] 4 sections | ≤150L total | Single responsibility | 5-phase execution | Phase 5 routing

### Writing Quality  
- [ ] ≤15 words/instruction | Action verbs only | Natural language | No meta-commentary

### Execution Readiness
- [ ] TodoWrite integration | Tool parameter→outcome pattern | Error recovery | Command recommendations

## Error Recovery

**Pattern**: If [condition] → TodoWrite: "Resolve [error]" → Recovery action → Validate → Continue

**Scenarios**: Tool failure (retry with alternative) | Dependency missing (add resolution task) | Validation failure (create debugging task) | Context loss (add recovery task)

## Command Template

```
# [Command Name]

Executes [function] through [method] providing [outcome] with [criteria].

## Principles
Single Responsibility: [task] without [exclusions] | Granular: [process]→[units] | Resource: [deps] with [reqs] | Error: [validation] and recovery

## Execution
[5-phase workflow with TodoWrite integration including mandatory Phase 5 routing]

## Footer
@./docs/core/README.md - Complete architectural context
```

---

**Core Standard**: Commands use natural language instructions with TodoWrite orchestration for reliable, trackable execution across all development workflows.