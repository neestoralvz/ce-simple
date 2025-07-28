# Claude.md Import Methodology Standard

**Updated**: 2025-07-24 | **Authority**: Claude Code @ import system understanding | **Limit**: 100 lines
**Navigation**: [System Hub](../navigation/index.md) | [Import Analysis](import-analysis-methodology.md) | [Context Efficiency](context-efficiency-optimization.md)

## Critical Understanding: @ Import Scope

**CONFIRMED FACT**: @ import syntax works EXCLUSIVELY in CLAUDE.md files. It does NOT work in regular markdown documentation files.

### @ Import Functionality
- **CLAUDE.md Files**: Special configuration files processed by Claude Code automatically
- **@ Import Syntax**: `@path/to/file.md` loads content immediately when Claude Code starts
- **Regular Markdown**: Standard documentation files do NOT support @ import syntax
- **Scope Limitation**: @ imports are Claude Code's memory system feature, not general markdown

## Four-Section CLAUDE.md Architecture

### Section 1: Essential @ Imports (Immediate Loading)
**Purpose**: Critical context that Claude needs from session start
**Syntax**: `@path/to/file.md` or `@path/to/file.md:15-30` for line ranges
**Criteria**: Architectural understanding, core navigation, essential protocols

```markdown
## Essential Context
@docs/core/project-structure-current.md
@rules/CLAUDE_RULES.md:1-25
```

### Section 2: Conditional Instructions (Reference Links)
**Purpose**: Task-based loading instructions using standard reference syntax
**Syntax**: Regular reference links - NO @ prefix
**Format**: `READ docs/path/file.md:15-30` or `[Description](docs/path/file.md)`

```markdown
## Conditional Loading Instructions
**Documentation Work** → READ docs/rules/documentation-standards-foundation.md:15-30
**Development Tasks** → READ docs/core/pts-framework.md:1-50
**Validation Work** → READ docs/core/pts-checklist.md:15-45
```

### Section 3: Context Navigation (Directory References)
**Purpose**: Guide Claude to context folders based on need type
**Syntax**: Standard markdown links to directories
**Format**: `[Description](docs/category/)` for directory access

```markdown
## Context Navigation
**Core Architecture** → [docs/core/](docs/core/)
**Rules & Standards** → [docs/rules/](docs/rules/)
**Technical Standards** → [docs/standards/](docs/standards/)
```

### Section 4: Practical Development (Context-Triggered)
**Purpose**: Anthropic CLAUDE.md best practices integration for practical workflow guidance
**Syntax**: Conditional READ instructions with line ranges
**Format**: `**Category** → READ docs/standards/filename.md:lines`

```markdown
## Practical Development (Context-Triggered)
**Basic Commands** → READ docs/standards/basic-commands.md:20-50
**Code Style** → READ docs/standards/code-style-preferences.md:15-40
**Development Workflow** → READ docs/standards/development-workflow.md:25-60
**Environment Setup** → READ docs/standards/environment-setup.md:15-35
**Known Issues** → READ docs/standards/known-issues-warnings.md:20-45
**AI Behavior** → READ docs/standards/behavioral-preferences.md:15-40
```

## Syntax Distinction Standards

### @ Import Syntax (CLAUDE.md Only)
```markdown
# Full file import
@docs/core/project-structure-current.md

# Line range import
@rules/CLAUDE_RULES.md:1-25

# Multiple range import
@docs/core/pts-framework.md:1-15,45-60
```

### Reference Links (All Documentation)
```markdown
# Conditional instruction
READ docs/rules/development-standards.md:20-40

# Directory navigation
[Core Architecture](docs/core/)

# Standard reference
[PTS Framework](docs/core/pts-framework.md)
```

## Reference Patterns in Regular Documentation

### Conditional Instructions Pattern
**Format**: `**IF [condition]** → READ docs/path/file.md:lines (description)`
**Usage**: Replace @ imports in regular documentation with conditional READ instructions

```markdown
# Standard conditional pattern
**IF documentation work** → READ docs/rules/markdown-standards.md:10-25 (format standards)
**IF development work** → READ docs/core/pts-framework.md:1-50 (PTS components)
**IF git operations** → READ docs/rules/git-workflow-protocols.md (workflow guide)
```

### Navigation Reference Pattern  
**Format**: `[Description](docs/path/)` or `[Title](docs/path/file.md)`
**Usage**: Standard markdown links for navigation and reference

```markdown
# Directory navigation
[Core Architecture](docs/core/) - System frameworks & principles
[Rules & Standards](docs/rules/) - Behavioral protocols

# File references
[PTS Framework](docs/core/pts-framework.md) - Technical validation system
```

## Common Errors to Avoid

### Incorrect Usage
```markdown
# WRONG - @ syntax in conditional instructions
**Documentation Work** → READ @docs/rules/markdown-standards.md:10-25

# WRONG - @ syntax in regular documentation files  
See @docs/core/pts-framework.md for details

# WRONG - @ syntax in authority hierarchy
1. @docs/vision/ - System direction
```

### Correct Usage
```markdown
# CORRECT - Conditional instructions without @
**Documentation Work** → READ docs/rules/markdown-standards.md:10-25

# CORRECT - Standard links in regular documentation
See [PTS Framework](docs/core/pts-framework.md) for details

# CORRECT - Navigation links in authority hierarchy
1. [docs/vision/](docs/vision/) - System direction
```

## Context Economy Principles

### Essential @ Imports (≤100 lines total)
- Project structure understanding (architectural necessity)
- Core partnership protocol (interaction requirements)
- Immediate navigation context (system operation)

### Conditional References (0 lines until needed)
- Task-specific standards and frameworks
- Detailed implementation procedures
- Validation and quality checklists

### Navigation Links (0 token cost)
- Directory organization guidance
- Secondary documentation access
- Extended context discovery

---

## See Also
- **[Import Analysis Methodology](import-analysis-methodology.md)** - General @ reference analysis
- **[Context Efficiency Optimization](context-efficiency-optimization.md)** - Systematic optimization
- **[Context Economy Metrics](../validation/context-economy-metrics.md)** - Measurement framework
- **[System Navigation](../navigation/index.md)** - Complete system access

**Application**: Use this methodology to properly implement Claude Code's @ import system exclusively in CLAUDE.md files while using standard reference links for all other documentation and conditional instructions.