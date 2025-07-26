# Context Compaction Checklist - Consolidated

**Updated**: 2025-07-26 | **Authority**: Core context optimization  
**Source**: Consolidated from validation/context-compaction-checklist.md  
**Purpose**: Validation criteria for context compaction techniques application

## Pre-Compaction Validation
- [ ] Component extraction criteria applied first
- [ ] Extractable content identified (checklists, templates, examples, procedures)  
- [ ] Reusability assessment completed for separable components
- [ ] Functional content protection evaluated

## Compaction Quality Validation
- [ ] Information preserved (no semantic loss)
- [ ] Clarity maintained (≤5 seconds comprehension time)
- [ ] References provided for extracted details
- [ ] Symbols universally understood
- [ ] Structure remains scannable

## Post-Compaction Verification
- [ ] Line limits respected (≤100 lines for docs, ≤80 lines for commands)
- [ ] Cross-references functional and accurate
- [ ] Extracted components accessible via references
- [ ] Original functionality preserved in all components
- [ ] English-only language compliance maintained

## Extraction Validation
- [ ] Extracted components serve clear standalone purpose
- [ ] Reference links use precise @path/file.md format
- [ ] Extracted files maintain original content quality
- [ ] Navigation between main file and extracted components intuitive
- [ ] No content duplication between main and extracted files

## Success Criteria
- **Density Ratio**: ≥2:1 compression without semantic loss
- **Comprehension Time**: ≤30% increase from original
- **Reference Efficiency**: ≤3 navigation hops to reach details
- **Maintenance Ease**: Updates remain straightforward
- **Functional Preservation**: All original capabilities maintained

---
**Authority References**: [Context Economy Metrics](context-economy-metrics.md) | [Context Architecture](context-architecture.md)