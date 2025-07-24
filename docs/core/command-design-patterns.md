# Command Design Patterns - ce-simple

**Last Updated: 2025-07-23**

## STP-Compliant Command Templates

### Template Estándar - 33 Principios Compliant

```markdown
# [comando]

## Propósito STP (Tier 0)
[Una línea técnica precisa - Directness + Precision + Exactitude]

## Responsabilidad Única (Tier 1 - SRP)
[Exactly one thing this command does - no exceptions]

## Ejecución KISS (Tier 1)
[≤3 pasos mínimos - Simplest solution that works]
1. [Paso específico con validation upfront - Fail Fast]
2. [Paso técnico con error handling claro - Technical Excellence]
3. [Paso final con resultado verificable - Effectiveness]

## Resultado Esperado (Tier 0 - Effectiveness + Pragmatism)
[Specific, measurable output que funciona en condiciones reales]

## Error Handling (Tier 2 + STP)
[Clear, actionable error messages - Fail Fast + Sobriety]

## Shared Pattern Integration (Tier 3 - Composition)
@./shared/validation.md - Input validation patterns (DRY + SSOT)
@./shared/error-handling.md - Error handling patterns (Convention)
@./shared/completion.md - Completion patterns (Least Surprise)

## Progressive Enhancement (Tier 5)
[References to advanced/specialized versions if applicable]

---
@./docs/core/shared-patterns.md (SSOT - Tier 5)
```

## Pattern Catalog por Tipo de Comando

### Core Command Pattern (init.md, start.md, explore.md)

#### STP Foundation Requirements:
- **Directness**: ≤3 steps from intent to execution
- **Precision**: 100% exact behavior specification
- **Sufficiency**: Exactly what's needed, complete
- **Technical Excellence**: Code quality ≥90%, complexity ≤15
- **Exactitude**: Implementation at exact required point
- **Sobriety**: 0 marketing language, pure technical content
- **Structure**: 100% pattern consistency
- **Conciseness**: ≥80% information density ratio
- **Clarity**: ≥90% new user comprehension without training
- **Coherence**: 0 integration conflicts with existing components
- **Effectiveness**: ≥95% objective completion rate
- **Pragmatism**: ≥80% active feature usage in real scenarios

#### Core Template:
```markdown
# [comando]

## Propósito
[Elevator pitch técnico - 30 segundos máximo]

## Prerrequisitos (Fail Fast)
[Validation checks upfront - specific error messages]

## Ejecución
1. [Direct step - no ambiguity]
2. [Technical step - with validation]
3. [Completion step - with verification]

## Resultado
[Measurable, verifiable output]

## Errors y Recovery
[Specific errors, clear recovery paths]

@./shared/validation.md
@./shared/error-handling.md
@./shared/completion.md
```

### Advanced Command Pattern (advanced/*)

#### Additional Requirements:
- **Progressive Disclosure**: Enhanced functionality clearly separated
- **Modular Design**: Composable components
- **Information Hiding**: Implementation complexity hidden
- **Orthogonality**: No side effects on core commands

#### Advanced Template:
```markdown
# [comando-advanced]

## Propósito STP
[Technical precision - advanced functionality specific]

## Core vs Advanced (Progressive Disclosure)
- **Core equivalent**: [reference to core command]
- **Advanced features**: [specific enhanced capabilities]
- **When to use**: [clear criteria for advanced vs core]

## Enhanced Execution (Modular Design)
### Phase 1: Core Functionality
[Compose from core patterns]

### Phase 2: Advanced Features  
[Additional capabilities with clear value]

### Phase 3: Integration
[Seamless integration with ecosystem]

## Advanced Error Handling (Graceful Degradation)
[Fallback to core functionality on advanced feature failure]

@./shared/orchestration.md
@./shared/validation.md  
@../core/[relevant-core-command].md
```

### Specialized Command Pattern (specialized/*)

#### Expert-Level Requirements:
- **Least Privilege**: Minimal access for maximum functionality
- **Technical Excellence**: Expert-level technical precision
- **Domain Abstraction**: Appropriate domain-specific abstractions
- **Graceful Degradation**: Multiple fallback strategies

#### Specialized Template:
```markdown
# [comando-specialized]

## Expert Purpose (Technical Excellence)
[Domain-specific technical precision - expert audience]

## Prerequisites & Privileges (Least Privilege)
[Minimal required access - security considerations]

## Domain Context (Appropriate Abstraction)
[Domain-specific context and terminology]

## Expert Execution (Technical Excellence)
[Sophisticated execution with expert-level precision]

## Multi-Level Fallbacks (Graceful Degradation)
1. **Specialized failure**: [fallback to advanced equivalent]
2. **Advanced failure**: [fallback to core equivalent]  
3. **Core failure**: [minimal viable outcome]

## Expert Error Handling
[Domain-specific errors with expert-level guidance]

@./shared/orchestration.md
@../advanced/[related-advanced-command].md
@../core/[related-core-command].md
```

## Shared Pattern Integration

### Validation Pattern Integration

#### shared/validation.md Template:
```markdown
# Shared Validation Patterns

## STP Validation Framework
[Direct, precise validation with technical excellence]

## Standard Validations (DRY Compliance)
### Input Validation
[Reusable input validation patterns]

### Environment Validation  
[System prerequisites validation]

### Context Validation
[Project context validation patterns]

## Usage in Commands (SSOT)
[How commands integrate these patterns]

## Error Integration (Fail Fast)
[How validation integrates with error handling]
```

### Error Handling Pattern Integration

#### shared/error-handling.md Template:
```markdown
# Shared Error Handling Patterns

## STP Error Framework
[Sober, clear, pragmatic error handling]

## Standard Error Types (Convention over Configuration)
### Validation Errors
[Consistent validation error format]

### Execution Errors
[Standard execution error patterns]

### System Errors  
[System-level error handling]

## Recovery Patterns (Graceful Degradation)
[Standard recovery strategies]

## Error Message Standards (Least Surprise)
[Consistent error message format and tone]
```

### Completion Pattern Integration

#### shared/completion.md Template:
```markdown
# Shared Completion Patterns

## STP Completion Framework  
[Effective, pragmatic completion indicators]

## Success Indicators (Effectiveness)
### Immediate Confirmation
[Instant success feedback patterns]

### Progress Tracking
[Standard progress indication]

### Result Verification
[Verification of successful completion]

## Next Steps Integration (Progressive Enhancement)
[How completion connects to next logical steps]

## Reporting Standards (Structure + Conciseness)
[Consistent completion reporting format]
```

### Orchestration Pattern Integration

#### shared/orchestration.md Template:
```markdown
# Shared Orchestration Patterns

## STP Orchestration Framework
[Direct, coherent command coordination]

## Command Coordination (Composition over Inheritance)
### Sequential Patterns
[Standard sequential execution patterns]

### Parallel Patterns  
[Parallel execution coordination]

### Conditional Patterns
[Conditional execution based on context]

## Context Passing (Loose Coupling)
[How context flows between commands]

## State Management (Immutability)
[Consistent state management across commands]

## Integration Standards (SSOT)
[How orchestration maintains single source of truth]
```

## Quality Assurance Patterns

### Code Quality Standards

#### STP Code Quality:
- **Technical Excellence**: Code quality ≥90%
- **Precision**: 100% absolute paths, specific references
- **Sufficiency**: Complete functionality, no gaps
- **Clarity**: Self-documenting code structure

#### Implementation Standards:
```markdown
## Code Structure (STP Structure)
[Logical organization - clear and well-structured]

## Naming Conventions (STP Clarity)  
[Names that provide immediate comprehension]

## Error Handling (STP Technical Excellence)
[Impeccable error handling in simple solution]

## Documentation (STP Sobriety)
[Sober technical documentation without embellishments]
```

### Performance Standards

#### STP Performance Requirements:
- **Pragmatism**: Performance adequate for purpose
- **Effectiveness**: Achieves objectives efficiently
- **Technical Excellence**: Optimized simple solutions

#### Performance Patterns:
```markdown
## Performance Targets
- **Core Commands**: <2 seconds execution
- **Advanced Commands**: <10 seconds execution  
- **Specialized Commands**: <30 seconds execution

## Optimization Patterns (Technical Excellence)
[Simple optimization techniques - no over-engineering]

## Resource Management (Least Privilege)
[Minimal resource usage patterns]

## Scalability Considerations (Progressive Enhancement)
[How commands scale with complexity]
```

## Integration Testing Patterns

### Tier Integration Testing

#### Cross-Tier Validation:
```markdown
## STP Integration Testing
[Direct testing of STP components across tiers]

## Tier Progression Testing
[Validation that tier 1-5 build properly on STP foundation]

## Cross-Command Integration
[Testing interaction between commands]

## Shared Pattern Integration Testing
[Validation of shared pattern usage]
```

### Automated Testing Patterns:
```markdown
## STP Automated Validation
[Automated checking of 12 STP components]

## Principle Compliance Testing
[Automated validation of 33 principles]

## Integration Testing Framework
[Automated cross-command integration testing]

## Performance Testing Automation
[Automated performance validation]
```

## Evolution Patterns

### Command Evolution Protocol

#### STP Evolution Standards:
- **Controlled Evolution**: Changes don't break STP compliance
- **Technical Excellence**: Evolution maintains quality standards
- **Pragmatism**: Evolution based on real usage patterns

#### Evolution Template:
```markdown
## Evolution Requirements (STP)
[How command evolution maintains STP compliance]

## Backward Compatibility (Immutability)
[How changes preserve existing interfaces]

## Progressive Enhancement Evolution
[How commands evolve from core → advanced → specialized]

## Integration Impact Assessment
[How evolution affects shared patterns and other commands]
```

---

**Authority References:**
- [Development Principles](../core/development-principles.md) - 33 principios authority
- [STP Checklist](../core/stp-checklist.md) - STP validation authority
- [Tier Compliance Matrix](tier-compliance-matrix.md) - Compliance reference

**Next:** [33-Principle Validation Framework](../frameworks/33-principle-validation-framework.md) para validation tools