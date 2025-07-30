# Template: Methodology Modules

**Template última edición: 29/07/2025** | Template for /methodology: reusable behavioral patterns

## Methodology Module Structure

```markdown
# /methodology:name - [Methodology Function]

**DD/MM/YYYY** | [Methodology purpose]

## DO
- [Primary methodology behavior 1]
- [Primary methodology behavior 2]
- [Application requirements and conditions]
- [Integration patterns with other methodologies]

## DON'T
- [Methodology violations 1]
- [Methodology violations 2]
- [Common application mistakes to avoid]
- [Anti-patterns that compromise methodology effectiveness]

## Context
- [Integration requirements with commands]
- [Dependencies on other methodologies]
- [Authority sources for methodology standards]
- [Application domains and use cases]

## Integration Pattern
```markdown
## When to EXECUTE this methodology
**EXECUTE:** /methodology:name
[Apply methodology instructions here]
```
```

## Methodology Categories

### Analysis Methodologies (thinkx4)
**Purpose**: Provide systematic frameworks for analysis and decision-making

**DO Pattern**:
- Require explicit application of all methodology components
- Maintain systematic approach throughout analysis process
- Document reasoning and insights from methodology application
- Integrate findings into actionable conclusions

**DON'T Pattern**:
- Skip methodology components for convenience or speed
- Apply methodology superficially without genuine systematic analysis
- Use methodology as checklist without understanding underlying principles
- Conclude without proper synthesis of methodology insights

### Execution Methodologies (parallel_execution, continuous_flow)
**Purpose**: Optimize execution patterns and workflow efficiency

**DO Pattern**:
- Enforce consistent execution patterns across similar contexts
- Provide clear criteria for when methodology should be applied
- Maintain execution quality while optimizing efficiency
- Integrate seamlessly with command and workflow execution

**DON'T Pattern**:
- Apply execution methodology inappropriately to context
- Compromise quality for efficiency gains
- Skip methodology when execution complexity requires systematic approach
- Create conflicts with other execution methodologies

### Validation Methodologies (validation_protocol, research_first)
**Purpose**: Ensure quality, accuracy, and authority compliance

**DO Pattern**:
- Apply systematic validation criteria consistently
- Reference appropriate authority sources for validation standards
- Document validation process and results clearly
- Escalate validation conflicts appropriately

**DON'T Pattern**:
- Skip validation when methodology requires systematic checking
- Apply validation superficially without genuine verification
- Ignore validation failures or conflicts
- Compromise validation standards for expedience

## Context Section Guidelines

### For Analysis Methodologies
```markdown
## Context
- Application domains where methodology is required
- Integration with command execution patterns
- Authority sources for analysis standards
- Quality criteria for methodology application
```

### For Execution Methodologies
```markdown
## Context
- Execution contexts where methodology applies
- Integration requirements with other execution patterns
- Performance and quality standards
- Conflict resolution with competing methodologies
```

### For Validation Methodologies
```markdown
## Context
- Validation criteria and authority sources
- Integration with system authority hierarchy
- Escalation procedures for validation conflicts
- Quality gates and compliance requirements
```

## Integration Patterns

### Command Integration
```markdown
## Integration Pattern
Commands reference methodology via:
**EXECUTE:** /methodology:name
[Apply methodology at appropriate execution point]
```

### Methodology Chaining
```markdown
## Integration Pattern
When multiple methodologies required:
**EXECUTE:** /methodology:first + /methodology:second
[Apply methodologies in appropriate sequence]
```

### Conditional Application
```markdown
## Integration Pattern
Context-sensitive methodology application:
**If [condition]**: EXECUTE /methodology:specific
**If [different condition]**: EXECUTE /methodology:alternative
```

## Template Usage Instructions

1. **Identify methodology category** (analysis/execution/validation)
2. **Define clear application conditions** and requirements
3. **Specify integration patterns** with commands and other methodologies
4. **Document DO/DON'T patterns** specific to methodology function
5. **Provide clear EXECUTE instructions** for consistent application

---
**Authority Source**: Methodology module analysis + systematic behavioral patterns
**Template References**: context/templates/universal_do_dont_template.md