# Universal DO/DON'T Template - System-Wide Behavioral Standards

**29/07/2025 11:45 CDMX** | Universal behavioral template for all system components

## Universal Template Structure

### For Any System Component
→ Ver context/examples/templates/do_dont_structure.md

## Application Domains

### Commands (/.claude/commands/)
**DO Section Focus**: 
- Clear execution instructions
- When to EXECUTE methodology
- Behavioral constraints for role/function
- Expected interaction patterns

**DON'T Section Focus**:
- Prohibited behaviors that violate command purpose
- Common execution mistakes
- Anti-patterns that break system coherence
- Boundary violations

### Documentation (context/)
**DO Section Focus**:
- Information accuracy requirements
- Authority source referencing  
- Template compliance expectations
- Trazabilidad maintenance

**DON'T Section Focus**:
- Information duplication prohibition
- Authority violation prevention
- Template inconsistency avoidance
- Reference accuracy requirements

### Methodology (/.claude/commands/methodology/)
**DO Section Focus**:
- Systematic application requirements
- Integration with other methodologies
- Output quality standards
- Behavioral consistency enforcement

**DON'T Section Focus**:
- Shortcuts that compromise methodology
- Integration conflicts with other methodologies
- Quality degradation patterns
- Behavioral drift prevention

## Next Action Logic Patterns

### Automatic Progression Criteria
```markdown
- **Clear workflow sequence**: When logical next step is obvious
- **Completion triggers**: When current component finished successfully  
- **Error recovery**: When specific error requires specific next action
- **State transitions**: When system state determines next component
```

### Recommended Progression Criteria
```markdown
- **User choice optimal**: When multiple valid next steps exist
- **Context dependent**: When next step depends on user goals/preferences
- **Validation needed**: When user should confirm before proceeding
- **Alternative paths**: When different workflows possible
```

### Context-Aware Patterns
```markdown
- **Orchestrator context**: Return control to orchestrator with results
- **Direct execution**: Suggest logical next command for user
- **Error context**: Route to appropriate debugging/recovery command  
- **Session context**: Consider session state for appropriate next action
```

## Behavioral Consistency Standards

### Language Patterns
**DO use**: DEBE, SIEMPRE, NUNCA, OBLIGATORIO for critical requirements
**DON'T use**: Weak language for behavioral boundaries
**DO maintain**: Consistent terminology across all components
**DON'T allow**: Behavioral drift between similar components

### Structure Consistency  
**DO follow**: Same DO/DON'T template structure everywhere
**DON'T vary**: Template structure based on component type
**DO maintain**: Next Action logic patterns universally
**DON'T skip**: Any section of universal template

### Integration Standards
**DO ensure**: Components work together seamlessly
**DON'T create**: Conflicting behavioral requirements
**DO validate**: Next Action chains work correctly
**DON'T break**: Workflow continuity between components

## Template Variable Guide

### [COMPONENT_NAME]
- Commands: /category:command format
- Documentation: Descriptive title format  
- Methodology: /methodology:name format

### [Function]
- Brief description of component purpose
- Single line, action-oriented
- Clear value proposition

### [Brief purpose]
- One line description of why component exists
- Focused on user/system benefit
- Complements function description

---
**Authority Source**: Universal behavioral standards + DO/DON'T system design
**Next Action**: 
- **Automatic**: Create category-specific templates using this universal structure
- **Recommended**: Apply to existing system components for consistency validation