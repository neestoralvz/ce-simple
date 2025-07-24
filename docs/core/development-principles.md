# Development Principles - ce-simple

**Last Updated: 2025-07-23**

## Quick Reference

**PTS + 20 principles in 6 tiers** - Use this checklist for all development decisions:

### Tier 0 - PRAGMATIC TECHNICAL SIMPLICITY (PTS) - ABSOLUTE GOVERNING PRINCIPLE

**Definition**: The meta-principle governing all other principles. Direct, forceful, and technically precise solutions that say exactly what's necessary at the exact point, with sober, concise, clear, coherent, effective, and pragmatic structure.

**Authority**: PTS is the mandatory primary filter. The other 20 principles apply ONLY after PTS has been meticulously and exhaustively fulfilled.

#### The 12 PTS Components (ALL MANDATORY)

**Technical Cluster:**
- **Directness**: Most direct path to objective without detours
- **Precision**: Forceful and specific technical accuracy
- **Sufficiency**: Exactly what's necessary, no more, no less, but complete
- **Technical Excellence**: Impeccable technical quality in simple solution

**Communication Cluster:**
- **Exactitude**: Implementation at exact required point
- **Sobriety**: Sober approach without unnecessary embellishments
- **Structure**: Logical, clear, well-structured organization
- **Conciseness**: Maximum value per unit of complexity

**Cognitive Cluster:**
- **Clarity**: Immediate comprehension without ambiguity
- **Coherence**: Absolute internal consistency
- **Effectiveness**: Produces measurable and successful results
- **Pragmatism**: Works effectively under real conditions

**PTS Application**: Each component is applied meticulously and exhaustively in every line of code, document, command, and architectural decision. NO EXCEPTIONS.
- [ ] **Sobriety**: 0 marketing language in technical content
- [ ] **Structure**: 100% pattern consistency across similar components
- [ ] **Conciseness**: ≥ 80% information density ratio

**Cognitive Optimization:**
- [ ] **Clarity**: ≥ 90% new user comprehension without training
- [ ] **Coherence**: 0 integration conflicts with existing components
- [ ] **Effectiveness**: ≥ 95% objective completion rate
- [ ] **Pragmatism**: ≥ 80% active feature usage in real scenarios

**🛑 BLOCKING REQUIREMENT**: 12/12 PTS components must pass for any development to proceed.

**📋 Complete Framework**: [Tier 0 PTS Framework](tier0-pragmatic-technical-simplicity.md) | **🔧 Validation Tools**: [PTS Validation Framework](../frameworks/pts-validation-framework.md)

### Tier 1 - Fundamentals
- **KISS**: Simplest solution that works
- **SOLID**: SRP, OCP, LSP, ISP, DIP  
- **DRY**: Single source of truth
- **YAGNI**: Only implement what's needed

### Tier 2 - Critical  
- **Separation of Concerns**: Distinct responsibilities
- **Fail Fast**: Early error detection
- **Convention over Configuration**: Sensible defaults
- **Least Surprise**: Predictable behavior

### Tier 3 - Important
- **Composition over Inheritance**: Flexible design
- **Loose Coupling/High Cohesion**: Independent modules
- **Immutability**: Stable foundations

### Tier 4 - Modularization
- **Modular Design**: Reusable components
- **Information Hiding**: Clean interfaces
- **Progressive Disclosure**: Gradual complexity
- **Orthogonality**: Independent changes
- **Abstraction**: Appropriate layers

### Tier 5 - Architecture
- **Single Source of Truth**: One authority
- **Least Privilege**: Minimal access
- **Graceful Degradation**: Fault tolerance
- **Progressive Enhancement**: Incremental improvement

## Core Philosophy

Simple implementation of proven principles that solve real problems without over-engineering.

**Priority when principles conflict:**
1. **PTS Foundation** (Tier 0 - absolute priority)
2. KISS (simplicity)
3. SSOT (single truth)
4. SRP (clear responsibility)  
5. Fail Fast (early detection)

## Principle Details

### Tier 0 - PTS Foundation (Pragmatic Technical Simplicity)

**OBLIGATORY PRE-FILTER** - Must pass before applying any other principles.

PTS represents the synthesis of technical excellence with pragmatic value. Every element must be simultaneously:
- **Simple**: Minimal complexity for maximum effect
- **Technical**: Architecturally sound and well-engineered  
- **Pragmatic**: Immediately useful and valuable

**ce-simple application:**
- 3 essential commands vs 111+ archived (PTS filter applied)
- Each command solves specific problem pragmatically
- Self-contained architecture enables practical reuse
- Clear purpose and immediate value

**Example:** `commands/init-project.md` passes all 12 PTS components - clear purpose (project setup), minimal implementation (essential steps only), single responsibility (initialization), immediate reuse (any project), evident maintainability (straightforward logic), direct verification (visible results), natural integration (standard conventions), self-evident documentation (clear steps), adequate performance (fast execution), clear error handling (informative failures), data principles (SSOT project structure), controlled evolution (extensible without breaking).

**Critical Integration:** PTS modifies how we apply traditional principles:
- **SOLID + PTS**: Architecture must be sound AND pragmatically valuable
- **DRY + PTS**: Eliminate duplication only if it reduces practical complexity
- **YAGNI + PTS**: Implement only what has proven pragmatic value

**Blocking Enforcement:** Any component failing PTS validation cannot proceed to other principle evaluation. This prevents over-engineering and ensures every element delivers practical value.

**Complete Framework:** See [PTS Checklist](pts-checklist.md) for comprehensive validation process, context-specific matrices, and integration guidelines.

### Tier 1 - Fundamentals

#### KISS (Keep It Simple)
Simplest solution that works.

**ce-simple application:**
- 3 essential commands vs 111+ complex ones
- Clear, single-purpose functions
- Minimal abstraction layers

**Example:** `commands/init-project.md` - straightforward setup without options

#### SOLID Principles
Complete framework for maintainable code.

**Single Responsibility (SRP):** One reason to change
**Open/Closed (OCP):** Open for extension, closed for modification
**Liskov Substitution (LSP):** Replaceable subtypes
**Interface Segregation (ISP):** Specific interfaces
**Dependency Inversion (DIP):** Depend on abstractions

**ce-simple application:**
- Each command handles one workflow (SRP)
- Commands extend without modification (OCP)
- Command interfaces are substitutable (LSP)
- Specific vs general interfaces (ISP)
- Reference abstractions not implementations (DIP)

**Example:** Commands reference `docs/vision/` (abstraction) not hard-coded requirements

#### DRY (Don't Repeat Yourself)
Every piece of knowledge has single representation.

**ce-simple application:**
- `docs/vision/` as single source for system direction
- Shared templates in `docs/templates/`
- Common patterns in `docs/frameworks/`

**Example:** All commands reference same vision documents

#### YAGNI (You Aren't Gonna Need It)
Don't implement until actually needed.

**ce-simple application:**
- Archived 111 unused commands
- Focus on 3 proven commands
- No speculative features

**Example:** Complex orchestration archived until needed

### Tier 2 - Critical

#### Separation of Concerns
Different aspects in distinct sections.

**ce-simple application:**
- Clear separation: `commands/`, `docs/`, `templates/`
- Vision separate from implementation
- Standards separate from execution

**Example:** `docs/vision/` defines WHAT, `docs/core/` defines HOW

#### Fail Fast
Detect errors early with clear guidance.

**ce-simple application:**
- Input validation before execution
- Clear error messages
- Upfront requirement checks

#### Convention over Configuration
Sensible defaults reduce configuration.

**ce-simple application:**
- Standard project structure
- Conventional locations (CLAUDE.md, docs/, commands/)
- Default workflows work immediately

#### Principle of Least Surprise
Predictable, expected behavior.

**ce-simple application:**
- Consistent naming and structure
- Commands behave as names suggest
- Predictable file organization

### Tier 3 - Important

#### Composition over Inheritance
Favor composition for flexibility.

**ce-simple application:**
- Commands compose from core documents
- Modular documentation
- Flexible architecture

#### Loose Coupling, High Cohesion
Independent modules, internal coherence.

**ce-simple application:**
- Independent, self-contained commands
- Clear interfaces between sections
- Focused, cohesive documents

#### Immutability
Preserve stability where possible.

**ce-simple application:**
- Vision documents are stable authority
- Command templates provide consistent patterns
- Core principles remain consistent

### Tier 4 - Modularization

#### Modular Design
Independent, reusable components.

**ce-simple application:**
- Self-contained commands
- Modular documentation sections
- Archive preserves reusable components

#### Information Hiding/Encapsulation
Hide implementation, expose interfaces.

**ce-simple application:**
- Commands hide orchestration complexity
- `docs/core/` encapsulates architecture
- Simple interfaces for complex operations

#### Progressive Disclosure
Present information gradually.

**ce-simple application:**
- CLAUDE.md overview → detailed docs
- Simple commands → archived advanced features
- Layered documentation depth

#### Orthogonality
Independent components without side effects.

**ce-simple application:**
- Commands operate independently
- Documentation sections update independently
- Archive preserves orthogonal functionality

#### Principle of Abstraction
Appropriate abstraction layers.

**ce-simple application:**
- `docs/vision/` - high-level abstractions
- `docs/core/` - architectural abstractions  
- Commands - workflow abstractions

### Tier 5 - Architecture

#### Single Source of Truth (SSOT)
Exactly one authoritative representation.

**ce-simple application:**
- `docs/vision/` is absolute authority
- CLAUDE.md is single system overview
- No conflicting documentation

#### Principle of Least Privilege
Minimum necessary access.

**ce-simple application:**
- Commands access only required files
- Clear scope boundaries
- Minimal system impact

#### Graceful Degradation
Continue functioning when components fail.

**ce-simple application:**
- Commands work independently
- Core functionality preserved
- Clear fallback strategies

#### Progressive Enhancement
Basic functionality first, advanced features incrementally.

**ce-simple application:**
- 3 essential commands provide core functionality
- 111 archived commands for advanced needs
- Basic workflows work immediately

## Implementation Checklist

When creating or modifying components:

**Tier 0 - PTS Foundation (OBLIGATORY):**
- [ ] **Clear Purpose**: What specific problem does it solve?
- [ ] **Minimal Implementation**: Simplest version that works?
- [ ] **Single Responsibility**: Does exactly one thing well?
- [ ] **Immediate Reusability**: Useful in multiple contexts?
- [ ] **Evident Maintainability**: New developer understands quickly?
- [ ] **Direct Verification**: Can be tested simply?
- [ ] **Natural Integration**: Fits naturally with ecosystem?
- [ ] **Self-Evident Documentation**: Code/command self-documents?
- [ ] **Adequate Performance**: Fast enough for its purpose?
- [ ] **Clear Error Handling**: Errors are informative and actionable?
- [ ] **Data Principles**: Single source of truth, avoids duplication?
- [ ] **Controlled Evolution**: Can evolve without breaking dependencies?

**⚠️ STOP if any PTS component fails - Return to design phase**

**Tier 1 - Fundamentals:**
- [ ] Simplest solution? (KISS + PTS)
- [ ] SOLID principles followed? (Architecture + PTS)
- [ ] No duplication? (DRY + PTS pragmatism)
- [ ] Only needed features? (YAGNI + PTS value)

**Tier 2 - Critical:**
- [ ] Concerns separated?
- [ ] Fast failure with guidance?
- [ ] Sensible defaults?
- [ ] Predictable behavior?

**Tier 3 - Important:**
- [ ] Composition used?
- [ ] Loose coupling, high cohesion?
- [ ] Immutability preserved?

**Tier 4 - Modularization:**
- [ ] Modular design?
- [ ] Implementation hidden?
- [ ] Progressive disclosure?
- [ ] Orthogonal components?
- [ ] Appropriate abstraction?

**Tier 5 - Architecture:**
- [ ] Single source of truth?
- [ ] Minimal access granted?
- [ ] Graceful degradation?
- [ ] Progressive enhancement?

**📋 Complete PTS Validation**: Use [PTS Checklist](pts-checklist.md) for detailed validation process with context-specific matrices and blocking criteria.

## Evolution

Principles evolve through:
- Assessment against usage patterns
- Refinement from experience
- Integration with learning protocols  
- Alignment with `docs/vision/`

---

**Next:** [System Principles](system-principles.md) for architectural implementation