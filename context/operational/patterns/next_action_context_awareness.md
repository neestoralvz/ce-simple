# Next Action Context Awareness - Context Detection & Workflow Continuity

**29/07/2025** | Environment-aware routing + workflow validation patterns

## Context Detection Logic

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

## Error Context Handling

### Error Type Routing
```markdown
## Error Context Logic
- **Recoverable errors**: Suggest retry or alternative approach
- **System errors**: Route to /workflows:debug for resolution
- **Authority conflicts**: Escalate to /roles:partner or user decision
```

### Context-Aware Error Recovery
- **Orchestrator context errors**: Return error status with recovery suggestions
- **Direct execution errors**: Provide user-friendly error resolution guidance
- **Methodology errors**: Route to appropriate validation or correction methodology

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
- **Monitor effectiveness**: Next action success rates for workflow optimization
- **Identify automation**: Common sequences for potential automatic progression
- **Detect friction**: Workflow interruption points for logic refinement
- **Track overrides**: User pattern changes for logic adjustment

### Logic Refinement Strategy
- **Update based on patterns**: Usage analytics drive next action improvements
- **Optimize criteria**: Automatic progression thresholds refined by effectiveness
- **Enhance routing**: Context-aware logic improved through user feedback
- **Quality improvement**: Recommendation accuracy enhanced by outcome tracking

## Context Environment Detection

### Technical Context Indicators
- **Git status**: Working directory state affects next action routing
- **Session state**: Planning documents inform appropriate next steps
- **System health**: Error conditions modify next action logic
- **User patterns**: Historical usage informs context-aware suggestions

### Adaptive Context Response
- **High-confidence routing**: Clear context → automatic progression
- **Medium-confidence routing**: Probable context → recommended progression  
- **Low-confidence routing**: Unclear context → user choice presentation
- **Context conflicts**: Multiple valid contexts → escalate to user decision

---
**Authority Source**: Command workflow analysis + automation pattern design
**Referencias:** → context/operational/patterns/next_action_framework.md (core principles)
→ context/system/templates/commands/template_index.md (command templates)