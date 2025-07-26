# Progressive Disclosure Framework - Consolidated

**Updated**: 2025-07-26 | **Authority**: Core UI/UX framework  
**Source**: Consolidated from frameworks/progressive-disclosure-framework.md  
**Purpose**: Framework para revelación gradual de complejidad manteniendo STP compliance

## Tier-Based Disclosure Architecture

### Level 1: Core Commands (Essential)

#### STP Foundation for Core Level
- **Directness**: Acceso inmediato a funcionalidad esencial
- **Clarity**: ≥90% comprensión sin training previo
- **Sufficiency**: 100% funcionalidad independiente
- **Pragmatism**: ≥80% usage rate en scenarios reales

#### Core Command Characteristics
```yaml
Audience: Todos los usuarios (new user friendly)
Complexity: Minimal (≤15 cyclomatic complexity)
Functionality: Essential operations only
Independence: 100% self-contained
Documentation: Self-evident (≤30 lines effective documentation)
Learning Curve: <5 minutes to productive use
Success Rate: ≥95% first-time success
```

### Level 2: Advanced Commands (Enhanced)

#### Enhanced Characteristics
```yaml
Audience: Experienced users + specific domain needs
Complexity: Moderate (≤30 cyclomatic complexity)
Functionality: Specialized operations + customization
Prerequisites: Core command mastery assumed
Documentation: Detailed but structured (≤80 lines)
Learning Curve: <15 minutes additional learning
Success Rate: ≥85% with prior core experience
```

### Level 3: Expert Commands (Specialized)

#### Expert Characteristics
```yaml
Audience: Domain experts + advanced customization
Complexity: High (≤50 cyclomatic complexity)
Functionality: Full power + edge cases
Prerequisites: Advanced command experience
Documentation: Comprehensive (≤150 lines)
Learning Curve: <30 minutes domain-specific learning
Success Rate: ≥75% for target expert audience
```

## Progressive Path Design

### Disclosure Triggers
- **User Competency**: Automatic progression based on usage patterns
- **Task Complexity**: Context-sensitive feature revelation
- **Error Recovery**: Advanced options revealed when needed
- **Performance Needs**: Optimization features disclosed based on usage

### Implementation Standards
- **Clear Entry Points**: Each level has obvious starting commands
- **Natural Progression**: Logical flow from basic to advanced
- **Escape Hatches**: Quick access to simpler alternatives
- **Context Preservation**: State maintained across complexity levels

---
**Authority References**: [Command Design Patterns](command-design-patterns.md) | [Task Orchestration](task-orchestration.md)