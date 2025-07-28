# System Architecture Governance Comprehensive Protocol

**Purpose**: Complete system design, naming, organization, and validation governance for optimal architecture coherence  
**Authority**: Unified architectural governance consolidating modular design, hierarchical naming, and central documents validation  
**Updated**: 2025-07-27 15:45 (Mexico City) | **Status**: Active | **Lines**: ≤80

## When to Apply
**IF modular architecture work** → System design tasks requiring structure & organization, component architecture
**IF hierarchical naming needed** → File/directory creation, renaming operations, organization/restructuring work
**IF content classification** → Creating documentation, organizing files, establishing structure
**IF central documents update** → Central documents modification, system changes requiring validation
**IF portability requirements** → Cross-system compatibility needs, Task Tool compatibility

## Hierarchical Naming Standards (MANDATORY)

### Directory Pattern (MANDATORY)
**Format**: `[number]-[code]-[purpose]/` | **Examples**: `01-fnd-foundations/`, `02-std-standards/`
**Purpose**: Clear ordering + category identification | Sequential numbering for logical hierarchy
**Implementation**: Consistent pattern application across all directory structures

### File Pattern (MANDATORY)  
**Format**: `[category-code]-[specific-purpose].md` | Code MUST match parent directory code  
**Examples**: `fnd-pts-framework.md`, `std-command-governance.md`
**Purpose**: Instant category recognition + hierarchical consistency maintenance

### Category Codes (STANDARDIZED)
**Core Categories**: `fnd` = Foundations | `std` = Standards | `com` = Communication
**Extended Categories**: `pro` = Protocols | `per` = Performance | `inf` = Infrastructure
**Scalability**: Pattern accommodates unlimited category expansion following same structure

## Modular Architecture Standards (MANDATORY)

### Design Principles (MANDATORY)
**Focused Responsibility**: Each module handles specific aspect | Clear boundaries reduce confusion | Single purpose per component
**Size Boundaries**: Commands ≤80 lines | Documentation ≤100 lines | Rules ≤80 lines | Modules ≤200 lines maximum
**Flat Structure Maximum**: ≤1 level deep | Create directories when first file needed | Active use only
**Dependency Management**: Clear explicit references | Avoid circular dependencies | Document integration points

### Self-Containment Standards (BLOCKING)
**Complete Independence**: No external file dependencies or references required for operation
**Embedded Logic**: All necessary logic included within single file or component
**Standalone Operation**: Functions independently without external configuration or dependencies
**Resource Isolation**: Self-manages all required resources and dependencies internally

## Content Distribution Framework (MANDATORY)

### Distribution Decision Criteria
**Consolidate When**: Content duplication >60% | No functional separation | User workflow requires simultaneous access | Maintenance burden exceeds benefit
**Distribute When**: Clear functional separation exists | Different workflows access different content | Authority hierarchy requires separation | Navigation supports distribution
**Test Methods**: If users always need A + B together → Consolidate | If A serves different purpose than B → Distribute

### Central Documents Validation (BLOCKING)
**Coherence Validation**: Auto-validate 4-file coherence (CLAUDE.md, rules/CLAUDE_RULES.md, conditional-loading-protocols.md, README.md)
**Cross-Reference Validation**: All internal links updated during changes | Reference integrity maintained
**Authority Hierarchy Preservation**: user-input/ → CLAUDE_RULES → docs/core/ → implementation flow maintained
**Navigation Pattern Maintenance**: Preserve established user discovery patterns and system clarity

## Implementation Standards (BLOCKING)

### Quality Gates (MANDATORY)
**Pre-Creation**: No creation without pattern compliance verification
**Auto-Correction**: Immediate rename when non-compliance discovered  
**Reference Updates**: All internal links updated during renaming operations
**Scalability Verification**: New categories follow established pattern requirements

### Architecture Verification (BLOCKING)
**Modular Design Review**: Verify clean component boundaries and minimal coupling
**Self-Containment Check**: Validate no external dependencies or file references
**Distribution Validation**: Confirm optimal organization based on decision criteria
**Integration Compatibility**: Ensure works with existing autocontained systems

### Central Documents Management
**CLAUDE.md Management**: Automatic execution sequence + 4-file coherence validation
**rules/CLAUDE_RULES.md Management**: Auto-validation protocol + rule separation integrity  
**Cross-Validation Protocol**: Verify orchestration compatibility + Apply comprehensive validation
**System Integrity Protection**: Architecture consistency maintained throughout

## Success Criteria
**Naming Consistency**: 100% compliance with hierarchical naming patterns across system
**Modular Excellence**: Clear boundaries, single responsibility, optimal cognitive load management
**Complete Self-Containment**: Zero external dependencies, standalone operation capability
**Distribution Optimization**: Content organized for optimal user workflow and system navigation
**System Coherence**: Unified architecture maintaining integrity across all components
**Central Documents Integrity**: 4-file coherence maintained with authority preservation

---

**Architecture Authority**: This comprehensive protocol ensures optimal system organization through unified hierarchical naming, modular design, self-containment, and central documents validation governance.