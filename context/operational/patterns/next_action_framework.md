# Next Action Framework - Core Logic Principles

**29/07/2025** | Workflow automation framework + progression logic categories

## Core Principles

### Framework Fundamentals
- **Workflow continuity**: Commands suggest logical next steps to prevent workflow breakage
- **Context awareness**: Next actions adapt based on execution environment (orchestrator vs direct)
- **User agency preservation**: Automatic only when clear, recommended when choice optimal
- **System integration**: Next actions consider system state and session context

## Logic Categories

### Automatic Progression
**Criteria**: When conditions are clear and progression is unambiguous
```markdown
## Next Action
- **Automatic**: /next:command (specific condition triggers this unambiguously)
```

**Examples**:
- `/actions:git` → **Automatic**: `/workflows:close` (after session changes committed)
- `/workflows:start` → **Automatic**: User choice based on planning state
- `/actions:build` → **Automatic**: `/actions:git` (after content creation)

### Recommended Progression  
**Criteria**: When user choice is optimal but clear suggestion exists
```markdown
## Next Action
- **Recommended**: /suggested:command (user choice optimal but clear suggestion)
- **Alternative**: /alternative:command (viable alternative path)
```

**Examples**:
- `/roles:partner` → **Recommended**: `/actions:git` (if decision validated)
- `/workflows:debug` → **Recommended**: `/workflows:continue` (if issue resolved)
- `/actions:research` → **Recommended**: `/actions:build` (to document findings)

### Context-Aware Routing
**Criteria**: Next action depends on execution environment and context
```markdown
## Next Action
- **Context**: Different actions based on orchestrator vs direct execution
- **If orchestrated**: Return results to orchestrator
- **If direct**: Suggest continuation command
```

**Examples**:
- `/roles:research` → **Context**: Return to orchestrator if delegated, /actions:build if direct
- `/methodology:thinkx4` → **Context**: Continue with original command or escalate if conflicts
- `/workflows:explore` → **Context**: Route based on findings (debug/continue/document)

## Decision Logic Framework

### Automatic vs Recommended Criteria
**Automatic triggers**:
- Unambiguous condition completion
- Single logical next step exists
- System state changes require immediate action

**Recommended triggers**:
- Multiple viable options exist
- User choice provides value
- Context adaptation beneficial

---
**Referencias:** → context/operational/patterns/next_action_command_patterns.md (implementation patterns)
→ context/operational/patterns/next_action_context_awareness.md (context detection)