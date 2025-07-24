# Import vs Reference Criteria

**Updated**: 2025-07-24 | **Authority**: Claude Code context strategy | **Limit**: 100 lines
**Navigation**: [System Hub](../navigation/index.md) | **Related**: [Agent Deployment Footer Standard](agent-deployment-footer-standard.md)

## Decision Framework

### Full File Import Strategy (@file.md)
**Use when ALL criteria met**:
- **Usage Frequency**: ≥70% of sessions require this content
- **File Size**: ≤100 lines for complete context justification
- **Core Workflow**: Essential for daily development operations
- **Standalone Context**: Complete concepts without external dependencies

### Line-Level Import Strategy (@file.md:15-30)
**Use when ALL criteria met**:
- **Specific Sections**: Precise procedures/concepts needed
- **Large Files**: >100 lines with focused content requirements
- **Context Efficiency**: 50-85% token reduction achievable
- **Semantic Completeness**: Target lines form complete, understandable units

### Reference Strategy ([Link](file.md))
**Use when ANY criterion met**:
- **Occasional Access**: <30% session usage frequency
- **Navigation Purpose**: Access pathway rather than working context
- **Comprehensive Content**: Full exploration preferred over partial context
- **Variable Usage**: Different sections needed in different sessions

### Decision-Triggered Loading
**Use for conditional context**:
- **Task-Specific**: Only needed for specific activities (writing, debugging)
- **Standards Enforcement**: Documentation/markdown standards when creating content
- **Advanced Features**: Complex frameworks for specialized workflows

## Application Matrix

### Full File Import (Core Context)
| File | Lines | Justification | Usage |
|------|-------|---------------|--------|
| CLAUDE_RULES.md | 100 | Partnership protocol | 100% sessions |
| project-structure-current.md | 82 | Navigation foundation | 90% sessions |
| command-index.md | 60 | Daily workflow | 85% sessions |
| decision-navigation-system.md | 88 | Decision support | 80% sessions |

### Line-Level Import (Precision Context)
| File | Target Lines | Content | Usage Pattern |
|------|-------------|---------|---------------|
| documentation-standards.md | :15-30 | Core principles only | Writing sessions |
| markdown-standards.md | :10-25 | Format standards | Markdown editing |
| pts-framework.md | :42-67 | 12 PTS components | Validation work |
| development-principles.md | :15-40 | Core tier principles | Development sessions |
| context-compaction-techniques.md | :51-70 | Compaction methods | Optimization work |

### Reference Only (On-Demand)
| File | Lines | Justification | Access Pattern |
|------|-------|---------------|----------------|
| navigation/index.md | ~150 | Comprehensive navigation | 30% sessions |
| templates/ | Variable | Development templates | 20% sessions |
| handoffs/ | Variable | Historical context | 10% sessions |
| line-level-import-standards.md | 100 | Complete methodology | Rare reference |

## Evaluation Protocol

### Assessment Protocol
**Quantitative**: Session tracking (10 sessions) | Usage percentage | Token cost analysis | Line-level precision impact  
**Qualitative**: Workflow criticality | Context dependency | Semantic completeness | Line boundary stability

## Implementation Standards

### Full File Import Implementation
```markdown
## Section Title
@path/to/file.md
```

### Line-Level Import Implementation
```markdown
## Section Title
**Context**: Core implementation procedures from methodology guide
@docs/implementation/methodology-implementation.md:45-75
```

### Multiple Range Import Implementation
```markdown
## Section Title
**Context**: Definition + implementation patterns
@docs/core/pts-framework.md:1-15,45-60
```

### Reference Implementation  
```markdown  
## Section Title
**Navigation**: [Comprehensive Index](docs/navigation/index.md)
**Templates**: [Command Templates](docs/templates/)
**Standards**: [Documentation Standards](docs/rules/documentation-standards.md) (load when writing)
```

## Optimization Guidelines

### Token Economy Framework
**Full Files**: ≤300 lines always-loaded | Core workflow justification required
**Line-Level**: Target 50-85% token reduction | Semantic completeness mandatory
**Reference**: 2-click max navigation | Clear conditional triggers
**Maintenance**: Line stability monitoring | Reference validation | Usage tracking

### Decision Optimization Matrix
| Content Size | Usage Frequency | Strategy | Token Impact |
|-------------|-----------------|----------|--------------|
| ≤100 lines | >70% sessions | Full Import | High value |
| >100 lines | >50% sessions | Line-Level | Optimal efficiency |
| >100 lines | <50% sessions | Reference | Maximum economy |
| Variable | Task-specific | Conditional | Precise loading |

## Authority Integration

**Decision Priority**: Semantic completeness (primary) | Usage frequency | Token efficiency | Line stability
**Line-Level Standards**: Complete reference → @docs/standards/line-level-import-standards.md
**Override Cases**: Full import (core architecture) | Line-level (precision context) | Reference (navigation access)

---

**Principle**: Full import for core workflow, Line-level for precision context, Reference for navigation access - optimizing semantic completeness with maximum token economy through intelligent loading strategies