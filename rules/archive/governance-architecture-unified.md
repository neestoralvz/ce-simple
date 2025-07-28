# Architecture Governance Unified Protocol (CONDITIONAL-MANDATORY)

**Authority**: System architecture principles | **Purpose**: CONDITIONAL-MANDATORY modular design and system architecture enforcement
**TRIGGER**: Architecture decisions, system design, component creation, naming operations | **Status**: Active | **Lines**: ≤80
**Updated**: 2025-07-27 17:00 (Mexico City)

## Enhanced Conditional Enforcement

**CONDITIONAL-MANDATORY**: When triggered, blocks architecture decisions until modular compliance verified
**DOMAIN-UNIVERSAL**: Applies to ALL architecture and design work when activated
**AUTO-EXECUTE-VALIDATION**: Automatic architecture validation with blocking capability
**PROGRESSIVE-ESCALATION**: Architecture violations escalate from warning to blocking

## Modular Architecture Principles (CONDITIONAL-MANDATORY)

### Autocontained Principle (CONDITIONAL-MANDATORY)
**TRIGGER**: Component creation, module design, system architecture
**ENFORCEMENT**: Complete self-containment required

**Self-Containment Requirements**:
- **Embedded Logic**: All necessary logic contained within component
- **Minimal Dependencies**: External dependencies minimized and explicit
- **Single Responsibility**: Clear, focused purpose and functionality
- **Interface Definition**: Well-defined inputs, outputs, and interactions

### Component Design Framework (CONDITIONAL-MANDATORY)
**Design Principles**:
- **Separation of Concerns**: Clear functional boundaries
- **Loose Coupling**: Minimal interdependence between modules
- **High Cohesion**: Related functionality grouped together
- **Explicit Interfaces**: Clear communication protocols

## Hierarchical Naming Standards (MANDATORY)

### Directory Pattern (MANDATORY)
**Format**: `[number]-[code]-[purpose]/` | **Examples**: `01-fnd-foundations/`, `02-std-standards/`
**Purpose**: Clear ordering + category identification | Sequential numbering for logical hierarchy

### File Pattern (MANDATORY)  
**Format**: `[category-code]-[specific-purpose].md` | Code MUST match parent directory code  
**Examples**: `fnd-pts-framework.md`, `std-command-governance.md`
**Purpose**: Instant category recognition + hierarchical consistency maintenance

### Category Codes (STANDARDIZED)
**Core Categories**: `fnd` = Foundations | `std` = Standards | `com` = Communication
**Extended Categories**: `pro` = Protocols | `per` = Performance | `inf` = Infrastructure

## Architecture Standards (CONDITIONAL-BLOCKING)

### Module Structure Requirements
**File Organization**: Logical structure with clear hierarchy
**Size Boundaries**: Commands ≤80 lines | Documentation ≤100 lines | Rules ≤80 lines | Modules ≤200 lines maximum
**Documentation Standards**: Complete module documentation required
**Testing Framework**: Comprehensive test coverage for each module

### Self-Containment Standards (BLOCKING)
**Complete Independence**: No external file dependencies or references required for operation
**Embedded Logic**: All necessary logic included within single file or component
**Standalone Operation**: Functions independently without external configuration or dependencies
**Resource Isolation**: Self-manages all required resources and dependencies internally

## Content Distribution Framework (MANDATORY)

### Distribution Decision Criteria
**Consolidate When**: Content duplication >60% | No functional separation | User workflow requires simultaneous access
**Distribute When**: Clear functional separation exists | Different workflows access different content | Authority hierarchy requires separation
**Test Methods**: If users always need A + B together → Consolidate | If A serves different purpose than B → Distribute

### Central Documents Validation (BLOCKING)
**Coherence Validation**: Auto-validate 4-file coherence (CLAUDE.md, rules/CLAUDE_RULES.md, conditional-loading-protocols.md, README.md)
**Cross-Reference Validation**: All internal links updated during changes | Reference integrity maintained
**Authority Hierarchy Preservation**: user-input/ → CLAUDE_RULES → docs/core/ → implementation flow maintained

## Quality Gates (CONDITIONAL-BLOCKING)

### Architecture Validation Checkpoints
**Design Review**: Architecture decision documentation and validation
**Interface Verification**: API and interface contract validation
**Dependency Analysis**: Dependency mapping and minimization verification
**Integration Testing**: Cross-module integration and compatibility testing

### Progressive Enforcement
**Phase 1: CONDITIONAL-ADVISORY**: Architecture guidance and best practices
**Phase 2: CONDITIONAL-REQUIRED**: Design compliance verification
**Phase 3: CONDITIONAL-MANDATORY**: Blocking until architecture standards met
**Phase 4: CONDITIONAL-BLOCKING**: System halt for critical architecture violations

## Success Criteria
**Modularity Achievement**: Clear separation of concerns and minimal coupling
**Naming Consistency**: 100% compliance with hierarchical naming patterns across system
**Complete Self-Containment**: Zero external dependencies, standalone operation capability
**System Integration**: Seamless component integration and communication
**Central Documents Integrity**: 4-file coherence maintained with authority preservation

---

**Architecture Authority**: Unified architecture governance achieves comprehensive modular design and systematic organization through conditional enforcement and progressive validation.