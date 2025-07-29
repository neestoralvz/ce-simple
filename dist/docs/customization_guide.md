# Customization Guide

How to adapt the command system for your specific project needs.

## Essential Customizations

### 1. Project Vision (context/TRUTH_SOURCE.md)
This is the most critical file to customize:

```markdown
# [Your Project] Truth Source

## Core Vision
[Define your project's purpose and objectives]

## Authority Framework  
[Define who decides what and how decisions are made]

## Architectural Principles
[Your project's technical and design principles]

## Quality Standards
[What constitutes quality work in your project]
```

### 2. Context Structure
Organize your context directory to match your project needs:

```
context/
├── TRUTH_SOURCE.md           # Your project vision
├── patterns/                 # Your methodology patterns
├── principles/               # Your decision principles  
├── templates/                # Your document templates
└── enforcement/              # Your quality rules
```

### 3. Command Triggers
Customize semantic triggers in CLAUDE.md for your domain:

```markdown
### [Your Domain] Pattern
**Semantic triggers**: [Your specific keywords and contexts]
**Execute**: Task tool → [Your preferred command sequence]
**Validate**: Task tool → [Your validation criteria]
```

## Advanced Customizations

### Command Modification
Edit command files in `.claude/commands/` to:
- Change context references
- Modify methodology steps
- Adjust validation criteria
- Add domain-specific patterns

### New Command Creation
Create new commands by:
1. Adding `.md` file in appropriate category
2. Following existing command structure
3. Defining clear methodology and objectives
4. Adding appropriate context references

### Integration Patterns
Customize how commands integrate:
- Modify context loading patterns
- Adjust validation sequences
- Change delegation strategies
- Update orchestration logic

## Domain-Specific Adaptations

### Software Development
- Emphasize code quality patterns
- Add testing and deployment workflows
- Include architecture validation
- Focus on technical documentation

### Content Creation
- Emphasize style and voice consistency
- Add editorial workflows
- Include publication processes
- Focus on audience-appropriate output

### Research Projects
- Emphasize validation and sourcing
- Add peer review processes
- Include methodology documentation
- Focus on reproducible results

### Business Operations
- Emphasize process optimization
- Add stakeholder communication
- Include decision documentation
- Focus on measurable outcomes

## Quality Assurance

### Validation Checklist
- [ ] All context references point to existing files
- [ ] Command objectives align with project goals
- [ ] Methodology steps are clear and actionable
- [ ] Enforcement rules match project standards
- [ ] Integration patterns work smoothly

### Testing Your Setup
1. Run `/workflows:start` to test basic functionality
2. Try a research task with `/actions:research`
3. Test orchestration with a complex multi-step task
4. Validate quality with `/roles:challenge`
5. Complete a full session with `/workflows:close`

## Maintenance

### Regular Updates
- Review and update TRUTH_SOURCE.md as project evolves
- Adjust command patterns based on usage experience
- Update enforcement rules based on lessons learned
- Refine integration patterns for better efficiency

### Performance Optimization
- Monitor command execution patterns
- Identify frequently used sequences
- Create shortcuts for common workflows
- Optimize context loading for speed

## Support

If you encounter issues:
1. Check that all context files exist and are properly formatted
2. Verify command syntax matches the reference
3. Ensure CLAUDE.md triggers are properly configured
4. Test individual commands before complex workflows

Remember: The system is designed to be organic and adaptive. Start with basic customizations and evolve based on your actual usage patterns.
