# PTS Framework Placement - Architectural Decision Record

**Date**: 2025-07-26 | **Status**: Decided | **Context**: docs/ auditing and consolidation

## Decision Summary

**DECISION**: Maintain current functional distribution of PTS Framework content across existing file locations rather than creating new consolidated modules.

## Context

During docs/ auditing process, we discovered PTS Framework content distributed across 4 files with 60% duplication but 40% unique content. Initial plan was to create new consolidated modules, but Documentation First Rule analysis revealed optimal strategy.

## Analysis Process

### Documentation First Rule Applied
1. **ANALYZE**: Examined complete docs/ structure (15 directories, 125+ files)
2. **DECIDE**: Evaluated placement options based on existing organizational patterns
3. **DOCUMENT**: This architectural decision record
4. **CREATE**: Consolidate content in existing files (not create new ones)

### Current PTS Distribution
- `docs/core/pts-framework.md` (241 lines) - Navigation hub + foundational definitions
- `docs/technical/pts-framework-technical.md` (81 lines) - Technical authority specifications  
- `docs/validation/pts-checklist.md` (240 lines) - Practical validation checklists
- `docs/frameworks/stp-validation-framework.md` (363 lines) - Implementation methodology

## Options Considered

### Option A: Create New Consolidated Modules ❌
- **Pros**: Clean consolidation, reduced duplication
- **Cons**: Breaks existing navigation, disrupts user familiarity
- **Decision**: Rejected - too disruptive

### Option B: Consolidate Everything in core/ ❌  
- **Pros**: Single location for PTS content
- **Cons**: Violates functional separation, mixed content types
- **Decision**: Rejected - breaks organizational patterns

### Option C: Maintain Functional Distribution ✅
- **Pros**: Preserves navigation, maintains authority hierarchy, functional coherence
- **Cons**: Content remains distributed
- **Decision**: SELECTED - optimal for system

## Decision Rationale

### Organizational Consistency
**Current structure follows established patterns:**
- `core/` = navigation hubs + foundational concepts (21 files)
- `technical/` = complete technical authority (6 files)
- `validation/` = practical quality gates (6 files)  
- `frameworks/` = implementation methodologies (10 files)

### Authority Hierarchy Preservation
**Maintains established flow:**
- `vision/` → `core/` → `technical/` (authority hierarchy)
- Each location serves distinct function in system navigation

### User Navigation Optimization
**Current distribution supports user workflow:**
- **Start**: `core/pts-framework.md` (overview + navigation)
- **Reference**: `technical/pts-framework-technical.md` (complete specs)
- **Practice**: `validation/pts-checklist.md` (workflow tools)
- **Implementation**: `frameworks/stp-validation-framework.md` (methodology)

### Future Scalability
**Distribution supports growth:**
- Each directory can expand independently
- Import system handles distributed content effectively
- No structural changes required for future PTS enhancements

## Implementation Strategy

### Content Consolidation Plan
1. **Preserve unique content** from all 4 files
2. **Consolidate overlapping content** by incorporating into most appropriate file
3. **Establish clear cross-references** between related files
4. **Eliminate pure duplication** while maintaining content accessibility

### Specific Consolidation Actions
- **`core/pts-framework.md`** → Enhance with mathematical formulas + comprehensive navigation
- **`technical/pts-framework-technical.md`** → Consolidate all technical specifications
- **`validation/pts-checklist.md`** → Integrate all practical validation tools
- **`frameworks/stp-validation-framework.md`** → Consolidate implementation methodologies

## Success Criteria

- **100% unique content preserved** across all 4 files
- **60% duplication eliminated** through smart consolidation
- **Navigation patterns maintained** - users find content where expected
- **Authority hierarchy preserved** - core/ → technical/ flow intact
- **Cross-references optimized** - clear connections between related content

## Precedent Established

**Principle**: When consolidating distributed framework content, prioritize preservation of existing navigation patterns and functional separation over co-location convenience.

**Future Applications**: Apply same analysis for other distributed framework consolidations (Context Management, Validation Systems, etc.)

## Alternatives Rejected

- Creating new pts-modules/ directory - breaks existing patterns
- Moving all content to single file - violates functional separation  
- Reorganizing entire docs/ structure - too disruptive for current benefits

---

**Decision Authority**: Based on Documentation First Rule analysis + user vision for structure preservation + organizational consistency requirements**