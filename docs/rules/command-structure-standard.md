# Command Structure Standard

## Purpose
Define executable command structure for Claude Code using simple, direct instructions with maximum clarity and immediate actionability.

## Core Requirements

### Structure Pattern
All commands follow 4-section structure:
1. **Purpose** - Single responsibility statement
2. **Principles** - 4 execution guidelines  
3. **Execution Process** - 5-phase workflow
4. **Core Import Footer** - Automatic architectural context loading

### Length Limits
- Total command: ≤150 lines
- Purpose: 1 paragraph (3-5 lines)
- Principles: 4 bullets (8-12 lines)
- Execution: 5 phases (120-130 lines)
- Core Import Footer: 2-3 lines

## Writing Standards

### Word Economy
- ≤15 words per instruction
- Action verbs only: Execute, Create, Deploy, Monitor, Validate
- Remove: "should", "might", "perhaps", "comprehensive", "utilize"
- Essential words only, no fluff

### Natural Language Instructions
```
GOOD: "Search TypeScript files for function definitions"
BAD: "Use Grep tool with pattern to locate function declarations"

GOOD: "Mark task as in_progress using TodoWrite" 
BAD: "TodoWrite([{"status": "in_progress"}])"

GOOD: "Analyze current context and recommend next command"
BAD: "Execute context analysis algorithm to determine optimal routing"
```

### Anti-Patterns
Never include:
- Programming syntax or code blocks
- Tool syntax: `Grep('*.ts')` → "Search TypeScript files"
- Meta-commentary: "This phase will..." → Direct instruction
- Theoretical explanations → Executable actions only

## Section Templates

### Purpose Template
```
Executes [primary function] through [method] providing [outcome] with [quality criteria].
```

### Principles Template
```
- **Single Responsibility**: Focus on [primary task] without [excluded areas]
- **Granular Approach**: Break [process] into manageable [units] with clear [criteria]
- **Resource Management**: Handle [dependencies] with explicit [requirements]
- **Error Recovery**: Built-in [failure handling] and recovery protocols
```

### Phase Template
```
### Phase N: [Phase Name]
Mark "[specific task]" as in_progress using TodoWrite

Execute [task group]:
- [Action verb] [specific object] [outcome criteria]
- [Action verb] [specific object] [validation step]
- [Action verb] [specific object] [documentation step]

Use [Tool] to [specific action]:
- [Parameter 1] for [specific purpose]
- [Parameter 2] with [validation criteria]

Complete current phase, mark "[next phase]" as in_progress using TodoWrite
```

### Error Handling Pattern
```
If [specific condition]:
- Add TodoWrite task: "Resolve [error type]: [specific issue]"
- [Specific recovery action]
- [Validation step]
- [Continue instruction]
```

## Phase 5: Command Routing and Handoff

### Mandatory Elements
All commands must include Phase 5 with:
- **Context Analysis**: Assess current state and achievements
- **Next Command Recommendations**: Suggest logical follow-up commands
- **Handoff Protocol**: Provide clear transition message

### Phase 5 Template
```
### Phase 5: Command Routing and Handoff
Mark "Command routing and handoff" as in_progress using TodoWrite

Analyze current context:
- Review [completed objectives] and [key outcomes]
- Identify [remaining requirements] or [next logical steps]
- Assess [system state] and [available resources]

Recommend next commands:
- [Command category/name]: [Specific use case scenario]
- [Command category/name]: [Alternative workflow option]
- [Command category/name]: [Advanced capability need]

Provide handoff message:
"[Summary of completion] - Ready for [next phase] via [recommended command]"

Complete all tasks using TodoWrite
```

## Tool Integration

### TodoWrite Requirements
Must appear at:
- Phase start: Mark new phase as in_progress
- Phase end: Complete current, mark next as in_progress  
- Phase 5: Context analysis, recommendations, and completion
- Errors: Add specific resolution tasks

### Tool Usage Pattern
```
Use [ToolName] to [action]:
- [Specific parameter] achieving [outcome]
- [Validation criteria] ensuring [quality]
```

## Quality Gates

### Structure Compliance
- [ ] 4 sections present and properly formatted
- [ ] ≤150 lines total length
- [ ] Single responsibility clearly defined
- [ ] 5-phase execution with TodoWrite integration
- [ ] Phase 5 routing and handoff included

### Writing Compliance  
- [ ] ≤15 words per instruction
- [ ] Action verbs used throughout
- [ ] No programming syntax or meta-commentary
- [ ] Natural language instructions only

### Execution Compliance
- [ ] Immediately actionable instructions
- [ ] Clear validation criteria per step
- [ ] Error handling integrated within phases
- [ ] Tool usage explicit with parameters

## Validation Checklist

**Structure**:
- Purpose defines single responsibility
- 4 principles follow template pattern
- 5 execution phases with TodoWrite
- Phase 5 includes routing and handoff
- Core Import Footer provides automatic architectural context

**Writing**:
- Instructions use ≤15 words
- Action verbs throughout
- No code syntax or theoretical explanations
- Natural language tool usage

**Execution**:
- Each instruction immediately executable
- Validation built into every step
- Error recovery protocols included
- Tool calls explicit with outcomes

## Core Import Footer

### Template
```
---

@./docs/core/README.md
@./docs/core/system-principles.md
```

### Purpose
Automatic loading of architectural foundation ensuring:
- **Compliance Automation**: Core principles automatically available
- **Educational Integration**: System architecture context in every command
- **Consistency Enforcement**: Unified foundation across all interactions

---

**All commands follow simple, direct structure using natural language instructions for immediate Claude Code execution success.**