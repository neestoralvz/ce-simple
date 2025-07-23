# 06-documentation - Documentation & Knowledge Commands

## Purpose
Intelligent documentation generation and knowledge management. These commands create, maintain, and optimize documentation with automatic updates, cross-references, and knowledge extraction.

## Commands
- `/docs-maintain` - Comprehensive documentation maintenance system with audit, consolidation, optimization, validation, and generation capabilities
- `/doc-generate` - Intelligent documentation generation
- `/knowledge-extract` - Knowledge extraction from implementations
- `/doc-optimize` - Documentation optimization and maintenance  
- `/cross-reference` - Automatic cross-reference management
- `/doc-validate` - Documentation quality and accuracy validation

## Category Relations
- **Triggered by**: 04-execution, 05-validation after completion
- **Uses**: 08-learning for pattern documentation
- **Coordinates with**: 10-standards for compliance
- **Feeds into**: 01-discovery for future context

## Usage Patterns
```
04-execution/complete → 06-documentation/docs-maintain → 10-standards/validate
08-learning/capture → 06-documentation/extract → 01-discovery/context
06-documentation/docs-maintain → 10-standards/comply → 07-maintenance/maintain
```

## Documentation Types
- **Implementation Documentation**: Code, architecture, and design decisions
- **Process Documentation**: Workflows, procedures, and methodologies
- **Knowledge Documentation**: Patterns, learnings, and best practices
- **User Documentation**: Guides, tutorials, and reference materials

## Generation Features
- **Mode-based Execution**: Audit, consolidate, optimize, validate, generate, and workflow modes
- **Automatic code documentation extraction** with cross-reference validation
- **Cross-reference generation and maintenance** with broken link detection
- **Template-based consistency enforcement** following progressive disclosure
- **Content consolidation** with duplicate detection and unified source establishment
- **Performance optimization** for oversized documentation (>200 lines)
- **Multi-format output support** with dynamic health reporting

## Quality Standards
- **Structural Integrity**: Comprehensive cross-reference validation and broken link repair
- **Content Optimization**: Progressive disclosure for files >200 lines with implementation extraction
- **Consistency Enforcement**: Unified content sources with duplicate elimination
- **Performance Standards**: Optimized documentation structure with health monitoring
- **Cross-reference Networks**: Automated reference mapping and integrity maintenance
- **Error Handling**: Built-in detection and resolution of missing references and structural violations

---
*Category 06: Knowledge preservation and accessibility system*