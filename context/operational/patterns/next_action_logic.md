# Next Action Logic - Workflow Automation Patterns

**29/07/2025 11:55 CDMX** | Next Action automation logic for command workflow continuity

## Next Action Logic Framework

### Core Principles
- **Workflow continuity**: Commands suggest logical next steps to prevent workflow breakage
- **Context awareness**: Next actions adapt based on execution environment (orchestrator vs direct)
- **User agency preservation**: Automatic only when clear, recommended when choice optimal
- **System integration**: Next actions consider system state and session context

### Logic Categories

#### Automatic Progression
**Criteria**: When conditions are clear and progression is unambiguous
```markdown
## Next Action
- **Automatic**: /next:command (specific condition triggers this unambiguously)
```

**Examples**:
- `/actions:git` → **Automatic**: `/workflows:close` (after session changes committed)
- `/workflows:start` → **Automatic**: User choice based on planning state
- `/actions:docs` → **Automatic**: `/actions:git` (after content creation)

#### Recommended Progression  
**Criteria**: When user choice is optimal but clear suggestion exists
```markdown
## Next Action
- **Recommended**: /suggested:command (user choice optimal but clear suggestion)
- **Alternative**: /alternative:command (viable alternative path)
```

**Examples**:
- `/roles:partner` → **Recommended**: `/actions:git` (if decision validated)
- `/workflows:debug` → **Recommended**: `/workflows:continue` (if issue resolved)
- `/actions:research` → **Recommended**: `/actions:docs` (to document findings)

#### Context-Aware Routing
**Criteria**: Next action depends on execution environment and context
```markdown
## Next Action
- **Context**: Different actions based on orchestrator vs direct execution
- **If orchestrated**: Return results to orchestrator
- **If direct**: Suggest continuation command
```

**Examples**:
- `/roles:research` → **Context**: Return to orchestrator if delegated, /actions:docs if direct
- `/methodology:thinkx4` → **Context**: Continue with original command or escalate if conflicts
- `/workflows:explore` → **Context**: Route based on findings (debug/continue/document)

## Implementation Patterns

### Command Category Next Action Patterns

#### Roles Commands
```markdown
## Next Action Logic for Consultation Roles
- **If analysis complete**: Return insights to user/orchestrator for decision
- **If additional validation needed**: /roles:challenge or /roles:partner  
- **If decision validated**: /actions:git (to commit validated changes)
- **Context**: Always preserve user authority in decision-making
```

```markdown
## Next Action Logic for Execution Roles  
- **If delegation needed**: Deploy specialist via Task tool
- **If work complete**: /workflows:close (for session documentation)
- **If validation required**: /methodology:validation_protocol
- **Context**: Continue execution until completion or escalation
```

#### Actions Commands
```markdown
## Next Action Logic for Creation Actions
- **Automatic**: /actions:git (after content/system changes)
- **Recommended**: /roles:partner (for validation of created content)
- **Context**: Consider session state for appropriate continuation
```

```markdown
## Next Action Logic for Processing Actions
- **Automatic**: /methodology:validation_protocol (after processing completion)
- **Recommended**: /actions:docs (to document processing results)
- **Context**: Route based on processing outcomes and user needs
```

```markdown
## Next Action Logic for System Actions
- **Automatic**: /workflows:close (after session-ending system actions)
- **Recommended**: /maintenance:validate (for system health verification)
- **Context**: Consider system state and integration requirements
```

#### Workflows Commands
```markdown
## Next Action Logic for Session Management
- **Automatic**: User choice presentation (start) or system state cleanup (close)
- **Recommended**: Related workflow based on session outcomes
- **Context**: Session lifecycle position determines next action logic
```

```markdown
## Next Action Logic for Investigation/Analysis
- **Recommended**: /actions:docs (to document findings)  
- **Alternative**: /workflows:debug (if issues discovered)
- **Context**: Investigation results determine appropriate continuation
```

### Methodology Next Action Integration

#### Analysis Methodologies
**Pattern**: Return to original command with analysis insights
```markdown
## Next Action
- **Context**: Continue with command that invoked methodology
- **If conflicts**: Escalate to /roles:partner for resolution
- **If additional analysis needed**: Chain to related methodology
```

#### Execution Methodologies
**Pattern**: Enhance execution of calling command
```markdown
## Next Action
- **Context**: Continue execution with methodology applied
- **If optimization available**: Suggest efficiency improvements
- **If conflicts detected**: Route to conflict resolution
```

#### Validation Methodologies
**Pattern**: Route based on validation results
```markdown
## Next Action
- **If validation passed**: Continue with original workflow
- **If validation failed**: Route to /workflows:debug or /roles:partner
- **If authority conflict**: Escalate to user for resolution
```

## Context-Aware Logic Implementation

### Orchestrator Context Detection
```markdown
## Context Detection Logic
- **If Task tool invocation**: Command was delegated by orchestrator
- **Action**: Return results to orchestrator for integration
- **Format**: Structured results ready for orchestrator processing
```

### Direct Execution Context Detection
```markdown
## Context Detection Logic  
- **If direct user invocation**: User executed command directly
- **Action**: Suggest logical next command for continued productivity
- **Format**: User-friendly next step recommendations
```

### Session Context Integration
```markdown
## Session Context Logic
- **Session beginning**: Route to workflow initiation commands
- **Session middle**: Route to continuation/building commands  
- **Session ending**: Route to documentation/commit/close commands
```

### Error Context Handling
```markdown
## Error Context Logic
- **Recoverable errors**: Suggest retry or alternative approach
- **System errors**: Route to /workflows:debug for resolution
- **Authority conflicts**: Escalate to /roles:partner or user decision
```

## Workflow Continuity Validation

### Next Action Chain Testing
**Validation criteria**:
- **No dead ends**: Every command has appropriate next action
- **No infinite loops**: Next action chains eventually reach completion
- **Context consistency**: Next actions respect execution environment
- **User agency**: Automatic progression only when unambiguous

### Integration Validation
**System integration points**:
- **Git integration**: Commands affecting system state route to /actions:git
- **Documentation integration**: Commands creating content route to documentation commands
- **Session integration**: Commands consider session lifecycle position
- **Planning integration**: Commands integrate with planning and progress tracking

## Next Action Logic Evolution

### Pattern Recognition
- Monitor next action effectiveness for workflow optimization
- Identify common next action sequences for potential automation
- Detect workflow friction points for logic refinement
- Track user override patterns for logic adjustment

### Logic Refinement
- Update next action logic based on usage patterns and user feedback
- Optimize automatic progression criteria for better user experience
- Refine context-aware routing for improved workflow continuity
- Enhance recommendation quality based on outcome tracking

---
**Authority Source**: Command workflow analysis + automation pattern design
**Template References**: All command templates + universal_do_dont_template.md

## Enlaces → Información Complementaria
**Si necesitas command templates:** → [context/templates/commands/template_index.md](../templates/commands/template_index.md)
**Si requieres workflow patterns:** → [context/patterns/orchestrator_methodology.md](./orchestrator_methodology.md)
**Si buscas automation principles:** → [context/enforcement/core_reminders.md](../enforcement/core_reminders.md)