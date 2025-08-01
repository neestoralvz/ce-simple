# ADR-005: Reference Architecture Migration Protocol

**Date**: 2025-07-30  
**Status**: ACCEPTED  
**Authority**: User simplicity supremacy → @context/architecture/core/truth-source.md → ADR-005

## Context

System requires transition from monolithic content duplication to reference-only architecture per user authority "no debemos de repetir contenido en ningun documento, solo se debe de referenciar". Current fragmentation creates authority contamination risk and violates "one fact in one place" principle.

**Problem Statement**: 
- Content duplication across files violates DRY compliance
- Authority chain integrity compromised by scattered information
- Token economy inefficiency from redundant content
- Migration paralysis due to lack of systematic protocol

## Decision

**SYSTEMATIC REFERENCE ARCHITECTURE MIGRATION OBLIGATORIO** with zero information loss and bidirectional consistency enforcement.

### Migration Protocol Framework:
1. **Content Consolidation**: Single authoritative source per domain with 95%+ user voice fidelity
2. **Reference Implementation**: Bidirectional cross-reference system per CROSS_REFERENCE_SYSTEM.md
3. **Authority Preservation**: Supreme authority chain integrity throughout migration process
4. **Quality Gates Protocol**: Pre/mid/post-migration validation with rollback capability

### Reference Architecture Standards:
- **Source of Truth**: One authoritative location per content domain
- **Reference-Only Files**: Secondary locations contain only forward references
- **Authority References**: ← symbol for authority sources, ↑ symbol for upward authority chain
- **Directional References**: → symbol for forward delegation, ←→ for bidirectional relationships
- **Absolute Path Requirement**: @context/ prefix MANDATORY for all cross-file references
- **Conditional Loading**: Smart context loading based on conversation patterns

### Integration Requirements:
- **MIGRATION_RULES.md**: Phase-based migration with authority validation
- **COMPONENT_DECISION_MATRIX.md**: Integration pathway optimization
- **CROSS_REFERENCE_SYSTEM.md**: Reference syntax and linking standards

## Consequences

### Positive:
- **Zero Duplication**: DRY compliance through single source of truth architecture
- **Authority Integrity**: User voice preservation through systematic consolidation
- **Token Economy**: Efficiency improvement through reference-only architecture
- **System Coherence**: Bidirectional consistency eliminates fragmentation

### Negative:
- **Migration Complexity**: Systematic migration requires careful authority preservation
- **Reference Overhead**: Additional cross-reference maintenance responsibility

### Risk Mitigation:
- **Rollback Protocol**: Complete migration reversal capability if authority compromised
- **Quality Gates**: 95%+ user voice fidelity monitoring throughout process

## Compliance Monitoring

**Enforcement Protocol**: Guardian role OBLIGATORIO validates zero duplication compliance
**Quality Gates**: Authority chain integrity DEBE be preserved during all migrations
**Standards Integration**: Reference architecture FUNDAMENTAL for system evolution
**Automated Validation**: tools/validation/reference-pattern-validator.sh OBLIGATORIO for syntax compliance
**Crisis Resolution**: Archive quarantine protocols for broken reference containment

## References

- **Authority Source**: @context/architecture/core/truth-source.md (supreme architecture authority)
- **Migration Protocol**: @context/architecture/adr/ADR-005-reference-architecture-migration-protocol.md (systematic migration authority)  
- **Reference System**: @context/architecture/reference/README.md (bidirectional linking)
- **Integration Matrix**: @context/architecture/ux/component-decision-flowchart.md (pathway optimization)
- **Technical Standards**: TOGAF ADM migration planning + OAIS preservation frameworks

---
**EVOLUTION**: Reference architecture evolves through migration → validation → optimization cycle preserving user authority supremacy and zero information loss.