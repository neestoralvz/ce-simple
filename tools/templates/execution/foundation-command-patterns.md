# Foundation Command Patterns

**Updated**: 2025-07-27 14:30 (Mexico City) | **Authority**: Template Compliance Rule
**Purpose**: Proven command patterns for high-quality implementations | **Status**: Active | **Lines**: ≤150
**MANDATORY**: Template compliance enforcement | **English-only**: Zero mixed languages

## When to Apply
**IF command creation** → Use proven patterns for PTS-compliant implementations
**IF quality improvement** → Apply foundation patterns to existing commands

## Proven Foundation Patterns

### Pattern 1: Simple Standalone Command (Gold Standard)
**Quality Score**: 8/10 PTS | **Source**: Root-level commands
**Structure**:
```markdown
# Command Name - Brief Description
## Purpose
Clear statement of single responsibility
## Principles and Guidelines
- Primary PTS components relevant to command
- Key behavioral principles  
- Integration guidelines
## Execution Process
Direct implementation steps without over-orchestration
```

### Pattern 2: Discovery Command Pattern
**Quality Score**: 7/10 PTS | **Purpose**: Information gathering and analysis
**Structure**:
```markdown
# Discovery Command
## Purpose
Specific discovery objective
## Discovery Process
Phase-based information gathering with clear outputs
## Results Documentation
Structured findings with actionable insights
```

### Pattern 3: Implementation Command Pattern  
**Quality Score**: 7/10 PTS | **Purpose**: Direct implementation tasks
**Structure**:
```markdown
# Implementation Command
## Purpose
Specific implementation objective
## Implementation Steps
Sequential execution with validation checkpoints
## Quality Validation
PTS compliance verification and success criteria
```

### Pattern 4: Validation Command Pattern
**Quality Score**: 8/10 PTS | **Purpose**: Quality assurance and verification
**Structure**:
```markdown
# Validation Command
## Purpose
Specific validation objective
## Validation Framework
Systematic quality checking with measurable criteria
## Results Reporting
Clear pass/fail status with improvement recommendations
```

## Anti-Patterns to Avoid

### Over-Orchestration Anti-Pattern
**Problem**: Commands that orchestrate multiple sub-commands
**Issues**: Complexity increase | Dependency management | Testing difficulty
**Solution**: Use simple standalone commands with clear single responsibility

### Numbered Directory Commands
**Problem**: Commands organized in complex hierarchical structures
**Issues**: Navigation complexity | Maintenance overhead | Discovery difficulty
**Solution**: Flat command structure with descriptive names

### Mixed Language Content
**Problem**: Commands containing non-English content
**Issues**: Template Compliance Rule violations | Communication inconsistency
**Solution**: English-only command content with clear terminology

## Implementation Standards

### Quality Requirements
- **PTS Compliance**: 12/12 components validation required
- **Line Limits**: ≤80 lines maximum per command
- **Self-Contained**: No external dependencies beyond slash calls
- **Single Responsibility**: Each command does exactly one thing well
- **Template Compliance Rule**: MANDATORY enforcement

### Command Structure Standards
- **Header**: Clear purpose statement and mandatory timestamp
- **Principles**: PTS components and behavioral guidelines
- **Process**: Direct implementation without over-orchestration
- **Validation**: Quality checkpoints and success criteria
- **English-Only**: Zero mixed language content

### Testing and Validation
- **Think×4 Analysis**: Required for command design decisions
- **Template Compliance**: MANDATORY rule enforcement
- **Quality Gates**: PTS validation before deployment
- **User Testing**: Validation of command effectiveness

## Success Criteria
**Command Quality**: ≥7/10 PTS score achievement
**Implementation Success**: ≥90% successful command executions
**Template Compliance**: 100% rule adherence
**User Satisfaction**: ≥85% effectiveness rating

---

**Foundation Authority**: Proven patterns ensuring high-quality command implementation with mandatory compliance enforcement