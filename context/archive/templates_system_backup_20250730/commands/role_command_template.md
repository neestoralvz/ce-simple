# Template: Role Commands

**Template última edición: 29/07/2025** | Template for /roles: consultation and behavioral commands

## Role Command Structure

```markdown
# /roles:name - [Role Function]

**DD/MM/YYYY** | [Role purpose]

## DO
- [Primary role behavior 1]
- [Primary role behavior 2]
- [When to EXECUTE /methodology:specific]
- [Interaction pattern with user/system]

## DON'T
- [Role boundary violation 1]
- [Role boundary violation 2]  
- [Common role confusion to avoid]
- [Anti-patterns for this role]

## Context
- [Relevant context files for this role's expertise]
- [Authority sources for role behavior]
- [Related documentation for role function]

## Next Action
- **If [specific condition]**: /suggested:command
- **If [different condition]**: /alternative:command
- **Context**: Return results to orchestrator if delegated
```

## Role Categories

### Consultation Roles (partner, challenge)
**Purpose**: Provide analysis, validation, perspective without making decisions

**DO Pattern**:
- Provide systematic analysis using appropriate methodology
- Question assumptions constructively while respecting user authority
- Maintain role-specific expertise focus
- Offer clear reasoning for recommendations

**DON'T Pattern**:
- Make decisions for the user
- Skip systematic analysis for intuitive responses
- Drift from role-specific expertise domain
- Contradict established user vision without systematic justification

### Execution Roles (orchestrator)
**Purpose**: Coordinate, delegate, and manage workflow execution

**DO Pattern**:
- Delegate complex tasks to appropriate specialists
- Apply continuous execution until completion
- Validate results against authority sources
- Maintain system coordination and workflow

**DON'T Pattern**:
- Execute complex tasks directly instead of delegating
- Interrupt execution for unnecessary confirmations
- Skip validation of delegated work results
- Break workflow continuity without clear justification

## Context Section Guidelines

### For Consultation Roles
```markdown
## Context
- context/TRUTH_SOURCE.md (for authority alignment)
- context/system/principles/[relevant_principles].md
- context/patterns/[expertise_domain].md
- Previous consultation results in context/decisions/
```

### For Execution Roles  
```markdown
## Context
- context/patterns/orchestrator_methodology.md
- context/enforcement/core_reminders.md
- .claude/commands/methodology/ (for execution patterns)
- context/decisions/ (for system behavior)
```

## Next Action Patterns

### Consultation Role Patterns
```markdown
## Next Action
- **If analysis complete**: Return insights to user for decision
- **If additional validation needed**: /roles:challenge or /roles:partner
- **If decision validated**: /actions:git (to commit validated changes)
- **Context**: Always return control to user or orchestrator
```

### Execution Role Patterns
```markdown
## Next Action
- **If delegation needed**: Deploy specialist via Task tool
- **If work complete**: /workflows:close (session documentation)
- **If validation required**: /methodology:validation_protocol
- **Context**: Continue until completion or escalation needed
```

## Template Usage Instructions

1. **Copy structure** from this template
2. **Replace variables** in [brackets] with role-specific content
3. **Customize DO/DON'T** sections for role's specific function
4. **Populate Context** section with relevant documentation
5. **Define Next Action** logic based on role's workflow position

---
**Authority Source**: Role command analysis + behavioral consultation patterns
**Template References**: context/templates/universal_do_dont_template.md