# Next Action Command Patterns - Implementation Logic by Category

**29/07/2025** | Specific patterns for roles, actions, workflows commands

## Roles Commands Next Action Logic

### Consultation Roles
```markdown
## Next Action Logic for Consultation Roles
- **If analysis complete**: Return insights to user/orchestrator for decision
- **If additional validation needed**: /roles:challenge or /roles:partner  
- **If decision validated**: /actions:git (to commit validated changes)
- **Context**: Always preserve user authority in decision-making
```

### Execution Roles  
```markdown
## Next Action Logic for Execution Roles  
- **If delegation needed**: Deploy specialist via Task tool
- **If work complete**: /workflows:close (for session documentation)
- **If validation required**: /methodology:validation_protocol
- **Context**: Continue execution until completion or escalation
```

## Actions Commands Next Action Logic

### Creation Actions
```markdown
## Next Action Logic for Creation Actions
- **Automatic**: /actions:git (after content/system changes)
- **Recommended**: /roles:partner (for validation of created content)
- **Context**: Consider session state for appropriate continuation
```

### Processing Actions
```markdown
## Next Action Logic for Processing Actions
- **Automatic**: /methodology:validation_protocol (after processing completion)
- **Recommended**: /actions:build (to document processing results)
- **Context**: Route based on processing outcomes and user needs
```

### System Actions
```markdown
## Next Action Logic for System Actions
- **Automatic**: /workflows:close (after session-ending system actions)
- **Recommended**: /maintenance:validate (for system health verification)
- **Context**: Consider system state and integration requirements
```

## Workflows Commands Next Action Logic

### Session Management
```markdown
## Next Action Logic for Session Management
- **Automatic**: User choice presentation (start) or system state cleanup (close)
- **Recommended**: Related workflow based on session outcomes
- **Context**: Session lifecycle position determines next action logic
```

### Investigation/Analysis
```markdown
## Next Action Logic for Investigation/Analysis
- **Recommended**: /actions:build (to document findings)  
- **Alternative**: /workflows:debug (if issues discovered)
- **Context**: Investigation results determine appropriate continuation
```

---
**Referencias:** → context/operational/patterns/next_action_framework.md (core principles)
→ context/operational/patterns/next_action_methodology_integration.md (methodology patterns)