# ADR-030: Unified File Naming Convention System

**Date**: 2025-07-31  
**Status**: ACCEPTED  
**Authority**: User vision supremacy → @context/architecture/core/truth-source.md → ADR-030

## Context

System exhibits inconsistent file naming patterns creating navigation complexity and automation barriers. Analysis reveals Spanish/English mixing, inconsistent separator conventions, and massive temporary file accumulation requiring systematic standardization.

**Problem Statement**:
- **Language Inconsistency**: Spanish filenames violate user authority "English naming for all files and directories"
- **Convention Fragmentation**: Mixed kebab-case/snake_case usage without file-type rationale
- **Temporary File Accumulation**: 200+ backup files creating system bloat and navigation difficulty
- **Automation Barriers**: Inconsistent patterns prevent effective tooling and validation

## Decision

**SYSTEMATIC FILE NAMING CONVENTION ARCHITECTURE OBLIGATORIO** with file-type-specific standards and risk-stratified migration methodology.

### Unified Naming System Framework:
1. **Language Standardization**: English-only naming across all files and directories
2. **File-Type-Specific Conventions**: Technical rationale-based separator standards
3. **Risk-Stratified Migration**: 4-phase approach with safety protocols and rollback capability
4. **Automated Validation**: Continuous compliance monitoring and enforcement tools

### File-Type Convention Standards:
```
File Type               Convention          Technical Rationale
-----------------------------------------------------------------
Markdown Files         kebab-case.md       Web-friendly, readable URLs
Python Scripts         snake_case.py       PEP 8 compliance, Python convention
Shell Scripts          kebab-case.sh       Unix tradition, dash-friendly
Directories           kebab-case/         Consistent with web standards
JSON/Config           kebab-case.json     Web API compatibility
Text Files            kebab-case.txt      General readability
```

### Migration Phase Architecture:
- **Phase 1 (IMMEDIATE)**: Temporary file cleanup - 80%+ file reduction, zero risk
- **Phase 2 (HIGH PRIORITY)**: Spanish→English core files - requires cross-reference updates
- **Phase 3 (MEDIUM PRIORITY)**: Directory standardization - path reference updates
- **Phase 4 (LOW PRIORITY)**: Tool script standardization - cosmetic improvements

## Consequences

### Positive:
- **System Coherence**: Unified naming eliminates cognitive overhead and navigation confusion
- **Automation Enablement**: Consistent patterns enable effective tooling and validation scripts
- **Authority Compliance**: English-only naming serves user vision supremacy
- **Maintenance Reduction**: Systematic cleanup eliminates accumulated temporary files
- **Developer Experience**: Predictable naming patterns improve development workflow

### Negative:
- **Migration Complexity**: Cross-reference updates required for renamed files
- **Temporary Disruption**: Migration process requires careful coordination

### Risk Mitigation:
- **Phase-Based Approach**: Risk stratification minimizes impact of each migration phase
- **Rollback Protocol**: Complete backup and rollback capability for all phases
- **Cross-Reference Mapping**: Systematic documentation of all references before changes
- **Automated Validation**: Tools ensure compliance and detect reference breaks

## Technical Implementation

### Validation Tool Architecture:
- **Pattern Detection**: Automated identification of naming convention violations
- **Reference Mapping**: Cross-reference analysis before file operations
- **Migration Safety**: Batch reference updates synchronized with file renames
- **Compliance Monitoring**: Continuous validation preventing future violations

### Integration with Existing Systems:
- **ADR-005 Enhancement**: Extends reference architecture with naming standardization
- **Hook System Integration**: Claude Code hooks enforce ongoing compliance
- **Authority Preservation**: 95%+ user voice fidelity maintained throughout migration

## Compliance Monitoring

**Enforcement Protocol**: Guardian role OBLIGATORIO validates naming convention compliance
**Quality Gates**: Authority chain integrity DEBE be preserved during all migrations  
**Standards Integration**: Naming conventions FUNDAMENTAL for system evolution
**Automated Validation**: tools/validation/naming-convention-validator.sh OBLIGATORIO
**Continuous Monitoring**: Pre-commit hooks prevent future violations

## Success Metrics

### Quantitative Targets:
- **File Reduction**: 80%+ temporary file elimination (Phase 1)
- **Language Compliance**: 100% English naming across system (Phase 2)
- **Convention Compliance**: 100% file-type convention adherence (Phases 3-4)
- **Reference Integrity**: 100% functional cross-references post-migration

### Qualitative Outcomes:
- **Navigation Improvement**: Predictable file location and naming patterns
- **Developer Experience**: Reduced cognitive load from consistent conventions
- **System Maintainability**: Automated tooling enabled by consistent patterns
- **Authority Alignment**: Technical standards serving user vision supremacy

## References

- **Authority Source**: @context/architecture/core/truth-source.md (supreme architecture authority)
- **User Vision**: @context/vision/vision_foundation.md (English naming requirement)
- **Migration Enhancement**: ADR-005-reference-architecture-migration-protocol.md (reference migration patterns)
- **Implementation Details**: NAMING_CONVENTIONS.md + NAMING_MIGRATION_PLAN.md (technical specifications)
- **Validation Tools**: tools/validation/naming-convention-validator.sh (automated compliance)

---

**EVOLUTION**: Naming convention architecture evolves through migration → validation → continuous compliance monitoring cycle preserving user authority supremacy and enabling systematic quality enhancement.