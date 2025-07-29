# Essential Customizations

How to configure core system components for your project.

## 1. Project Vision (context/TRUTH_SOURCE.md)
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

## 2. Context Structure
Organize your context directory to match your project needs:

```
context/
├── TRUTH_SOURCE.md           # Your project vision
├── patterns/                 # Your methodology patterns
├── principles/               # Your decision principles  
├── templates/                # Your document templates
└── enforcement/              # Your quality rules
```

## 3. Command Triggers
Customize semantic triggers in CLAUDE.md for your domain:

```markdown
### [Your Domain] Pattern
**Semantic triggers**: [Your specific keywords and contexts]
**Execute**: Task tool → [Your preferred command sequence]
**Validate**: Task tool → [Your validation criteria]
```

---

**Next**: See advanced_customizations.md for command modification and domain-specific adaptations.