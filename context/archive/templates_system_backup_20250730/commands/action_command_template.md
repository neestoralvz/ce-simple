# Template: Action Commands

**Template última edición: 29/07/2025** | Template for /actions: direct execution commands

## Action Command Structure

```markdown
# /actions:name - [Action Function]

**DD/MM/YYYY** | [Action purpose]

## DO
- [Primary action execution 1]
- [Primary action execution 2]
- [When to EXECUTE /methodology:specific]
- [Quality/completion criteria]

## DON'T
- [Action scope violation 1]
- [Action scope violation 2]
- [Common execution mistakes to avoid]
- [Anti-patterns that compromise action quality]

## Context
- [Templates/patterns relevant to this action]
- [Authority sources for action requirements]
- [Related system components affected by action]

## Next Action
- **Automatic**: /next:command (when action completion triggers clear next step)
- **Recommended**: /suggested:command (when user choice optimal)
- **Context**: Orchestrator continuation vs direct user guidance
```

## Action Categories

### Creation Actions (docs, write)
**Purpose**: Generate content, documentation, or system components

**DO Pattern**:
- Apply appropriate templates and consistency standards
- Reference authority sources and maintain traceability
- Ensure output meets established quality criteria
- Validate content against system principles and user vision

**DON'T Pattern**:
- Create content without understanding target audience/purpose
- Duplicate existing information without adding clear value
- Skip template compliance or quality validation
- Generate content that contradicts system architecture

### Processing Actions (compact, expand, research)
**Purpose**: Transform, analyze, or gather information systematically

**DO Pattern**:  
- Preserve essential information during transformation
- Apply systematic methodology for processing
- Validate transformation quality and completeness
- Maintain clear traceability to source material

**DON'T Pattern**:
- Process without clear transformation criteria
- Lose critical information during processing operations
- Skip methodology when complexity requires systematic approach
- Create output disconnected from source context

### System Actions (git, maintain)
**Purpose**: Manage system state, commits, and infrastructure health

**DO Pattern**:
- Follow established system protocols and safety checks
- Validate system state before and after action execution
- Document changes appropriately for future reference
- Ensure action contributes to overall system health

**DON'T Pattern**:
- Execute system changes without proper validation
- Skip documentation of system modifications
- Compromise system integrity for convenience
- Perform actions that conflict with system architecture

## Context Section Guidelines

### For Creation Actions
```markdown
## Context
- context/templates/ (for content structure)
- context/patterns/documentation_style.md
- context/TRUTH_SOURCE.md (for authority alignment)
- Related existing content for consistency
```

### For Processing Actions
```markdown
## Context
- context/patterns/[relevant_methodology].md
- Source material location and format
- Transformation requirements and criteria
- Quality validation standards
```

### For System Actions
```markdown
## Context
- System state requirements and validation
- context/decisions/ (for system behavior)
- Safety protocols and rollback procedures
- Integration points with other system components
```

## Next Action Patterns

### Completion-Triggered Automatic
```markdown
## Next Action
- **Automatic**: /actions:git (after content/system changes)
- **Automatic**: /workflows:close (after session-ending actions)
- **Automatic**: /methodology:validation_protocol (after critical changes)
```

### User-Choice Recommended
```markdown
## Next Action
- **Recommended**: /workflows:continue (to build on completed action)
- **Recommended**: /roles:partner (for validation of action results)
- **Alternative**: /actions:related (for complementary actions)
```

### Context-Aware Routing
```markdown
## Next Action
- **If orchestrated**: Return to orchestrator with action results
- **If direct execution**: Suggest logical continuation based on action type
- **If error occurred**: /workflows:debug for issue resolution
```

## Template Usage Instructions

1. **Identify action category** (creation/processing/system)
2. **Copy appropriate structure** from template
3. **Customize DO/DON'T** sections for action's specific function
4. **Populate Context** section with relevant resources
5. **Define Next Action** logic based on action's workflow position

---
**Authority Source**: Action command analysis + execution pattern templates
**Template References**: context/templates/universal_do_dont_template.md