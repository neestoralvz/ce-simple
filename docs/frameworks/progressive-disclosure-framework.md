# Progressive Disclosure Framework - ce-simple

**Last Updated: 2025-07-23**

## STP-Compliant Progressive Disclosure

### Propósito STP

Framework para implementación meticulosa de Progressive Disclosure que cumple Simplicidad Técnica Pragmática, permitiendo revelación gradual de complejidad manteniendo directness, precision y clarity en cada nivel.

## Tier-Based Disclosure Architecture

### Level 1: Core Commands (Essential)

#### STP Foundation for Core Level:
- **Directness**: Acceso inmediato a funcionalidad esencial
- **Clarity**: ≥90% comprensión sin training previo
- **Sufficiency**: 100% funcionalidad independiente
- **Pragmatism**: ≥80% usage rate en scenarios reales

#### Core Command Characteristics:
```yaml
Audience: Todos los usuarios (new user friendly)
Complexity: Minimal (≤15 cyclomatic complexity)
Functionality: Essential operations only
Independence: 100% self-contained
Documentation: Self-evident (≤30 lines effective documentation)
Learning Curve: <5 minutes to productive use
Success Rate: ≥95% first-time success
```

#### Core Commands Implementation:

**`init.md` - Project Initialization:**
```yaml
Purpose: Create functional ce-simple project
Disclosure Level: Essential project setup only
Hidden Complexity: 
  - Advanced git configuration
  - Comprehensive template deployment  
  - Specialized environment setup
Revealed Functionality:
  - Basic git initialization
  - Minimal directory structure
  - Essential CLAUDE.md creation
Progressive Path: → advanced/init-complete.md when needed
```

**`start.md` - Context Analysis:**
```yaml
Purpose: Analyze current context, suggest next step
Disclosure Level: Quick assessment + clear recommendation
Hidden Complexity:
  - Deep architectural analysis
  - Comprehensive project metrics
  - Multi-factor decision matrices
Revealed Functionality:
  - Basic project structure scan
  - Simple recommendation logic
  - Clear next-step guidance  
Progressive Path: → advanced/analyze-deep.md for detailed analysis
```

**`explore.md` - Structure Exploration:**
```yaml
Purpose: Understand project organization quickly
Disclosure Level: Structure overview + key patterns
Hidden Complexity:
  - Architectural pattern analysis
  - Dependency graph mapping
  - Code quality metrics
Revealed Functionality:
  - Directory structure display
  - Basic file organization
  - Simple pattern identification
Progressive Path: → advanced/explore-architecture.md for deep analysis
```

### Level 2: Advanced Commands (Enhanced)

#### STP Compliance for Advanced Level:
- **Technical Excellence**: Higher technical sophistication while maintaining simplicity
- **Precision**: More specific technical capabilities
- **Structure**: Clear enhancement over core functionality
- **Effectiveness**: Measurably enhanced results

#### Advanced Command Characteristics:
```yaml
Audience: Users with basic ce-simple experience
Complexity: Moderate (≤25 cyclomatic complexity)
Functionality: Enhanced operations with clear added value
Independence: Self-contained with optional core composition
Documentation: Clear enhancement explanation (≤50 lines)
Learning Curve: <15 minutes additional learning
Success Rate: ≥90% for experienced users
```

#### Advanced Commands Implementation:

**`advanced/init-complete.md` - Enhanced Initialization:**
```yaml
Core Enhancement: Extends init.md with comprehensive setup
Additional Disclosure:
  - Template system deployment
  - Advanced git configuration
  - Documentation scaffolding
  - Development environment setup
Hidden Complexity:
  - Custom template creation
  - Environment-specific configurations
  - Specialized deployment options
Composition Pattern: Uses shared/orchestration.md for coordination
Progressive Path: → specialized/init-enterprise.md for complex environments
```

**`advanced/analyze-deep.md` - Comprehensive Analysis:**
```yaml
Core Enhancement: Extends start.md with detailed assessment
Additional Disclosure:
  - Multi-dimensional project analysis
  - Technical debt assessment
  - Architecture quality metrics
  - Development pathway recommendations
Hidden Complexity:
  - Complex metric calculations
  - Multi-factor optimization algorithms
  - Predictive analysis models
Composition Pattern: Uses shared/validation.md for thorough checks
Progressive Path: → specialized/audit-compliance.md for full audit
```

**`advanced/explore-architecture.md` - Architectural Exploration:**
```yaml
Core Enhancement: Extends explore.md with architectural insight
Additional Disclosure:
  - Architectural pattern identification
  - Component relationship mapping
  - Design principle compliance assessment
  - Refactoring opportunity identification
Hidden Complexity:
  - Complex dependency analysis
  - Pattern recognition algorithms
  - Quality assessment matrices
Composition Pattern: Uses shared/error-handling.md for robust analysis
Progressive Path: → specialized/optimize-performance.md for optimization
```

### Level 3: Specialized Commands (Expert)

#### STP Compliance for Specialized Level:
- **Technical Excellence**: Expert-level technical precision
- **Exactitude**: Domain-specific implementation precision
- **Sobriety**: Pure technical communication for experts
- **Coherence**: Consistent with expert domain knowledge

#### Specialized Command Characteristics:
```yaml
Audience: Expert users with domain expertise
Complexity: High (≤40 cyclomatic complexity) but well-structured
Functionality: Domain-specific expert operations
Independence: May require advanced prerequisites
Documentation: Expert-level precision (≤100 lines)
Learning Curve: Domain expertise assumed
Success Rate: ≥85% for domain experts
```

#### Specialized Commands Implementation:

**`specialized/audit-compliance.md` - Compliance Auditing:**
```yaml
Domain: Comprehensive system compliance validation
Expert Disclosure:
  - 33-principle comprehensive audit
  - Regulatory compliance checking
  - Quality assurance validation
  - Risk assessment analysis
Expert Complexity:  
  - Multi-tier compliance matrices
  - Regulatory framework integration
  - Complex scoring algorithms
Prerequisites: Understanding of compliance frameworks
Composition: Advanced composition from all shared patterns
```

**`specialized/optimize-performance.md` - Performance Optimization:**
```yaml
Domain: System performance optimization
Expert Disclosure:
  - Performance bottleneck identification
  - Optimization strategy development
  - Resource utilization analysis
  - Scalability assessment
Expert Complexity:
  - Performance profiling algorithms
  - Multi-dimensional optimization
  - Resource allocation strategies
Prerequisites: Performance engineering knowledge
Composition: Technical patterns + performance frameworks
```

**`specialized/trace-dependencies.md` - Dependency Analysis:**
```yaml
Domain: Complex dependency relationship analysis
Expert Disclosure:
  - Dependency graph construction
  - Circular dependency detection
  - Impact analysis calculation
  - Refactoring strategy development
Expert Complexity:
  - Graph analysis algorithms
  - Complex relationship modeling
  - Multi-level impact calculation
Prerequisites: Software architecture expertise  
Composition: Analysis patterns + graph algorithms
```

## Progressive Enhancement Implementation

### Disclosure Transition Patterns

#### Core → Advanced Transition:
```yaml
Trigger Conditions:
  - User explicitly requests enhanced functionality
  - Core command suggests advanced option
  - Context analysis indicates advanced need

Transition Method:
  - Clear explanation of enhanced capabilities
  - Explicit opt-in mechanism
  - Graceful fallback to core if advanced fails

Information Architecture:
  - Core functionality always accessible  
  - Advanced features clearly additional
  - No hidden complexity in core interface
```

#### Advanced → Specialized Transition:
```yaml
Trigger Conditions:
  - Expert knowledge demonstrated
  - Complex domain requirements identified
  - Advanced functionality insufficient

Transition Method:
  - Expert prerequisite validation
  - Domain-specific capability assessment
  - Clear expert mode activation

Information Architecture:
  - Domain expertise assumed
  - Specialized terminology appropriate
  - Expert-level precision expected
```

### Disclosure Interface Patterns

#### Core Interface Pattern:
```markdown
# [core-command]

## What This Does (STP Clarity)
[One sentence - immediate comprehension]

## Quick Start (STP Directness)  
[≤3 steps to success]

## Expected Result (STP Effectiveness)
[Specific, measurable outcome]

## When You Need More (Progressive Disclosure)
- **Enhanced version**: [link to advanced command] - for [specific enhanced capability]
- **Expert version**: [link to specialized command] - for [specific expert capability]
```

#### Advanced Interface Pattern:
```markdown
# [advanced-command]

## Enhanced Capabilities (STP Precision)
[Specific enhancements over core version]

## Core vs Advanced (Progressive Disclosure)
- **Core equivalent**: [link] - basic functionality
- **This version adds**: [specific enhancements]
- **When to use**: [clear criteria]

## Enhanced Execution (STP Technical Excellence)
[More sophisticated execution with clear value]

## Expert Path Available (Progressive Disclosure)
- **Expert version**: [link to specialized] - for [expert scenarios]
```

#### Specialized Interface Pattern:
```markdown
# [specialized-command]  

## Expert Domain (STP Exactitude)
[Domain-specific technical precision]

## Prerequisites (STP Sobriety)
[Required expertise - no embellishment]

## Expert Execution (STP Technical Excellence)
[Sophisticated execution for domain experts]

## Fallback Path (Graceful Degradation)
- **If too complex**: [link to advanced] - enhanced but simpler
- **If still too complex**: [link to core] - basic functionality
```

## Usage Context Framework

### Context-Driven Disclosure

#### New User Journey:
```yaml
Entry Point: Core commands only
Disclosure Strategy: Hide all complexity initially
Progressive Revelation:
  1. Master core functionality (≥3 successful uses)
  2. Introduce advanced options contextually
  3. Expert level only on explicit request + validation
Success Metrics: ≥90% new user success with core commands
```

#### Experienced User Journey:
```yaml
Entry Point: Core or Advanced based on context
Disclosure Strategy: Reveal relevant enhanced capabilities
Progressive Revelation:
  1. Assess user experience level
  2. Suggest appropriate command level
  3. Provide pathway to specialized when applicable
Success Metrics: ≥85% experienced user efficiency gains
```

#### Expert User Journey:
```yaml
Entry Point: Any level appropriate for task
Disclosure Strategy: Full capability access with clear navigation
Progressive Revelation:
  1. Expert validation if accessing specialized
  2. Full disclosure of domain-specific capabilities
  3. Clear fallback paths for accessibility
Success Metrics: ≥80% expert user task completion efficiency
```

### Contextual Disclosure Rules

#### Automatic Disclosure Triggers:
```yaml
Core → Advanced:
  - User demonstrates proficiency (≥5 successful core uses)
  - Task complexity exceeds core capabilities
  - User explicitly requests "more options"

Advanced → Specialized:
  - Domain expertise demonstrated
  - Complex requirements identified  
  - User explicitly requests expert mode

Disclosure Suppression:
  - User explicitly requests simple mode
  - Error rate increases with complexity
  - Context analysis suggests over-complexity
```

## Implementation Guidelines

### STP-Compliant Disclosure Development

#### Design Phase:
1. **STP Validation First**: Ensure each level passes all 12 STP components
2. **Clear Level Boundaries**: Define exact functionality per level
3. **Transition Criteria**: Specify when/how users move between levels
4. **Fallback Strategy**: Define graceful degradation paths

#### Implementation Phase:
1. **Core First**: Implement and validate core functionality
2. **Advanced Enhancement**: Add capabilities without core modification
3. **Specialized Domain**: Expert-level without compromising lower levels
4. **Integration Testing**: Validate smooth transitions between levels

#### Validation Phase:
1. **Per-Level STP**: Each level must pass STP independently
2. **Transition Smoothness**: Validate user journey between levels
3. **Fallback Effectiveness**: Test degradation scenarios
4. **Overall Coherence**: Ensure system-wide consistency

### Quality Assurance Framework

#### Disclosure Effectiveness Metrics:
```yaml
Core Level Success:
  - New user comprehension: ≥90%
  - First-time success rate: ≥95%
  - Time to productivity: <5 minutes

Advanced Level Success:
  - Enhanced value delivery: ≥85%
  - Transition smoothness: ≥90%
  - Feature utilization: ≥70%

Specialized Level Success:
  - Expert task completion: ≥80%
  - Domain precision: ≥95%
  - Expert satisfaction: ≥85%
```

#### Progressive Disclosure Validation:
```yaml
Information Architecture:
  - Complexity graduation clarity: ≥90%
  - Level transition logic: 100% clear
  - Fallback path availability: 100%

User Experience:
  - Learning curve smoothness: ≥85%
  - Cognitive load management: ≥90%
  - User confidence maintenance: ≥90%

Technical Implementation:
  - Code complexity management: Each level ≤ specified limits
  - Modular isolation: 100% level independence
  - Shared pattern usage: Consistent across levels
```

---

**Authority References:**
- [Development Principles](../core/development-principles.md) - Progressive Disclosure principle authority
- [Command Architecture](../command-architecture/README.md) - Implementation architecture
- [33-Principle Validation](33-principle-validation-framework.md) - Validation framework

**Next:** [Composition Patterns Framework](composition-patterns-framework.md) para modular design patterns