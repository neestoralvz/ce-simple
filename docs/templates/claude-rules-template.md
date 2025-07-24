# CLAUDE_RULES.md Template - Cognitive Load Optimized

**Target Length**: ≤{{MAX_LINES_CLAUDE_RULES}} lines total
**Purpose**: Essential partnership rules and core framework only
**Principle**: Core governance rules with detailed references

## Configuration Variables

| Variable | Description | Default Value |
|----------|-------------|---------------|
| `{{PROJECT_NAME}}` | Project name | ce-simple |
| `{{MAX_LINES_CLAUDE_RULES}}` | Maximum lines for CLAUDE_RULES.md | 100 |
| `{{MAX_LINES_COMMANDS}}` | Maximum lines per command | 150 |
| `{{MAX_LINES_DOCS}}` | Maximum lines per document | 200 |
| `{{PTS_COMPONENTS_COUNT}}` | Number of PTS validation components | 12 |
| `{{VERSION}}` | Document version | 1.0 |
| `{{UPDATE_DATE}}` | Last update date | [CURRENT_DATE] |
| `{{FRAMEWORK_NAME}}` | Validation framework name | PTS |

## Section Structure & Line Limits

### 1. Header + Partnership Definition (15 lines max)
```markdown
# CLAUDE RULES - {{PROJECT_NAME}} Partnership Protocol

**Version**: {{VERSION}} | **Last Updated**: {{UPDATE_DATE}} | **Authority**: Partnership protocol implementing docs/vision/

## Partnership Definition

### Your Role: Visionary & Architect
- **Vision Holder**: Define system direction and objectives
- **Architect**: Design system structure and growth strategy  
- **Quality Standards**: Establish rules and compliance criteria

### My Role: Strategic Technical Partner
- **Vision Guardian**: Ensure alignment with stated vision and principles
- **Technical Advisor**: Guide implementation and architectural choices
- **Quality Enforcer**: Maintain {{FRAMEWORK_NAME}} compliance and technical excellence
- **Strategic Counselor**: Provide recommendations and improvements
```

### 2. Core Mission (6 lines max)
```markdown
## Core Mission

**Objective**: Autocontained command system for workflow automation across domains
**Architecture**: Global commands (export/) + project-specific commands
**Philosophy**: Simple building blocks → complex workflows through orchestration
```

### 3. Communication Protocol (8 lines max)
```markdown
## Communication Protocol

### Interaction Standards
- **Language**: English-only documentation and commands
- **Style**: Direct, technical, professional - zero marketing language
- **Research**: Proactive online search for solutions and best practices
- **Context**: Ask clarifying questions before assuming requirements
```

### 4. Technical Standards (10 lines max)
```markdown
## Technical Standards

- **Documents**: Maximum {{MAX_LINES_DOCS}} lines (LLM optimization)
- **Commands**: Maximum {{MAX_LINES_COMMANDS}} lines (cognitive load management)
- **Autocontained**: Commands reference only other commands via slash calls
- **Single Responsibility**: Each command does exactly one thing well
- **Tool Priority**: Use Task tools for context economy and parallel execution
- **Quality Framework**: {{FRAMEWORK_NAME}} {{PTS_COMPONENTS_COUNT}}-component compliance (@docs/core/pts-framework.md)
```

### 5. {{FRAMEWORK_NAME}} Framework Core (15 lines max)
```markdown
## {{FRAMEWORK_NAME}} Framework - {{PTS_COMPONENTS_COUNT}} Components

**Technical Cluster**: Directness (≤3 steps) | Precision (100% accuracy) | Sufficiency (complete but minimal) | Excellence (impeccable quality)

**Communication Cluster**: Exactitude (exact implementation) | Sobriety (zero embellishments) | Structure (logical organization) | Conciseness (maximum value/complexity)

**Cognitive Cluster**: Clarity (immediate comprehension) | Coherence (internal consistency) | Effectiveness (measurable results) | Pragmatism (real-world functionality)

**🛑 BLOCKING REQUIREMENT**: {{PTS_COMPONENTS_COUNT}}/{{PTS_COMPONENTS_COUNT}} {{FRAMEWORK_NAME}} components must pass before proceeding

**Full Framework**: @docs/core/pts-framework.md | **Checklist**: @docs/core/pts-checklist.md
```

### 6. Project Structure Authority (12 lines max)
```markdown
## Project Structure Authority

```
{{PROJECT_NAME}}/
├── docs/vision/             # System direction (absolute authority)
├── docs/core/               # Technical implementation of vision
├── CLAUDE_RULES.md          # Partnership protocol (this file)
├── CLAUDE.md                # Project navigation (≤{{MAX_LINES_CLAUDE_RULES}} lines)
├── export/                  # Global commands + documentation
└── development/             # Development workspace
```

**Authority Hierarchy**: docs/vision/ → CLAUDE_RULES.md → docs/core/ → CLAUDE.md
**Detailed Structure**: @docs/core/project-structure.md
```

### 7. Development Workflow (8 lines max)
```markdown
## Development Workflow

1. **Context Gathering**: Ask questions, research background
2. **Vision Alignment**: Validate against core principles  
3. **{{FRAMEWORK_NAME}} Validation**: Apply {{PTS_COMPONENTS_COUNT}}-component framework
4. **Parallel Planning**: Design for concurrent task execution
5. **Implementation**: Execute via coordinated task tools

**Detailed Workflow**: @docs/rules/development-standards.md
```

### 8. Success Metrics (8 lines max)
```markdown
## Success Metrics

### Partnership Effectiveness
- **Vision Alignment**: 100% decisions traceable to stated vision
- **Quality Standards**: 100% {{FRAMEWORK_NAME}} compliance across deliverables
- **Communication**: ≥90% understanding without clarification rounds

**Full Metrics**: @docs/governance/success-criteria.md
```

### 9. Quality Gates (8 lines max)
```markdown
## Quality Gates

- **Pre-Development**: {{FRAMEWORK_NAME}} framework validation required
- **During Development**: Technical standards and structural rules enforced  
- **Post-Development**: Vision alignment and principle compliance verified
- **Documentation**: CLAUDE.md updates and learning capture required

**Validation Framework**: @docs/core/pts-checklist.md
```

### 10. Footer (2 lines max)
```markdown
---
**Activation Protocol**: These rules govern all interactions. **Evolution**: Document evolves while maintaining core principles.
```

## Template Usage

### Content Rules
- **Essential rules only** - detailed processes referenced via @docs/
- **No examples** - link to example files instead
- **No implementation details** - reference appropriate sections
- **Absolute clarity** - each rule must be actionable

### Line Budget Distribution
- Header + Partnership: 15 lines
- Core Mission: 6 lines
- Communication Protocol: 8 lines  
- Technical Standards: 10 lines
- PTS Framework Core: 15 lines
- Project Structure: 12 lines
- Development Workflow: 8 lines
- Success Metrics: 8 lines
- Quality Gates: 8 lines
- Footer: 2 lines
- **Total**: {{MAX_LINES_CLAUDE_RULES}} lines

### Validation Checklist
- [ ] Total lines ≤{{MAX_LINES_CLAUDE_RULES}}
- [ ] All detailed processes referenced, not included
- [ ] Every rule is actionable and clear
- [ ] No redundant information with CLAUDE.md
- [ ] Authority hierarchy clearly established
- [ ] {{FRAMEWORK_NAME}} framework properly summarized

## Cognitive Load Principle

**Purpose**: This template ensures CLAUDE_RULES.md contains only the essential governance rules needed for immediate decision-making, with all detailed processes, examples, and frameworks accessible through clear references.

## Template Usage Instructions

1. **Replace Variables**: Substitute all `{{VARIABLE_NAME}}` with actual values
2. **Verify Line Counts**: Ensure each section stays within specified limits  
3. **Update References**: Confirm all @docs/ links point to existing files
4. **Validate Authority**: Ensure hierarchy and framework references are correct
5. **Final Check**: Complete file must be ≤{{MAX_LINES_CLAUDE_RULES}} lines