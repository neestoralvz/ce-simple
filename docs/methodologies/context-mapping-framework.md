# Context Mapping Methodology Framework

**Updated**: 2025-07-24 | **Authority**: Context architecture foundation | **Limit**: 100 lines
**Navigation**: [System Hub](../navigation/index.md) | [Import Analysis](../standards/import-analysis-methodology.md) | [Context Metrics](../validation/context-economy-metrics.md)

## Framework Definition

**Purpose**: Systematic methodology for mapping, analyzing, and optimizing context flow throughout ce-simple system architecture
**Authority**: docs/vision/ → CLAUDE_RULES.md → docs/core/ → CLAUDE.md (REAL hierarchy)
**Reality**: Context = immediate token cost vs. on-demand access cost vs. user workflow efficiency

## Context Discovery Protocol

### Phase 1: Context Inventory (15 minutes)
**Execute Systematic Analysis**:
1. **@ Import Extraction**: 4 always-loaded files = 353 lines immediate cost
2. **Reference Link Audit**: `grep -r "\[.*\](.*\.md)" docs/` → Map all reference links
3. **File Dependency Graph**: Map which files reference which other files
4. **Usage Pattern Analysis**: Which contexts triggered in different workflow types

### Phase 2: Context Classification (20 minutes)
**Apply Rigorous Criteria**:
- **MANDATORY**: ≤3 files total, used 100% sessions, <50 lines total, system fails without immediate access
- **CONDITIONAL**: Triggered by specific task types, loaded via READ instructions in CLAUDE_RULES.md
- **REFERENCE**: Accessible via links, zero token cost until accessed
- **ELIMINATE**: Unused, redundant, or broken references

### Phase 3: Context Flow Mapping (25 minutes)
**Map Information Pathways**:
1. **Authority Flow**: docs/vision/ → CLAUDE_RULES.md → docs/core/ → CLAUDE.md → implementation
2. **Decision Triggers**: Session start → Documentation work → Development → Architecture → Validation
3. **Cross-Reference Network**: Hub files → Technical files → Line-level precision
4. **Circular Dependencies**: Identify and eliminate reference loops

## Context Architecture Patterns

### Pattern 1: Hub-and-Spoke (Navigation)
**Structure**: Central navigation hub → Specialized technical areas
**Example**: docs/navigation/index.md → docs/core/, docs/rules/, docs/standards/
**Token Impact**: Single reference point, zero @ import cost

### Pattern 2: Conditional Loading (Task-Based)
**Structure**: IF task type → READ specific context
**Example**: IF documentation work → READ @docs/rules/documentation-standards-foundation.md
**Token Impact**: Context loaded only when actually needed

### Pattern 3: Line-Level Precision (Optimization)
**Structure**: @file.md:15-30 for specific sections
**Example**: @docs/core/pts-framework.md:1-50 (core components only)
**Token Impact**: 60-90% reduction vs. full file imports

### Pattern 4: Authority Cascade (Hierarchy)
**Structure**: High authority → Low authority with reference preservation
**Example**: docs/vision/ references → CLAUDE_RULES references → docs/core/ implementation
**Token Impact**: Preserves authority while minimizing always-loaded content

## Folder Structure Growth Rules

### Core Stability Principles
**Permanent Anchors**: CLAUDE.md, CLAUDE_RULES.md, docs/core/, export/commands/
**Expandable Zones**: docs/rules/, docs/standards/, docs/templates/, docs/validation/
**Growth Strategy**: Add files within existing directories before creating new directories

### Directory Function Definitions
- **docs/core/**: System architecture + frameworks (≤20 files, stable)
- **docs/rules/**: Behavioral protocols (expandable, authority-driven)
- **docs/standards/**: Technical implementation criteria (expandable, conditional) 
- **docs/templates/**: Reusable patterns (expandable, self-contained)
- **docs/governance/**: Decision records (append-only, permanent)
- **docs/validation/**: Quality frameworks (specialized, expandable)

### Growth Decision Matrix
**New File in Existing Directory**: Default choice, maintains organization
**New Directory**: Only when >15 files in category or fundamentally different function
**Directory Reorganization**: Only with vision-level approval, preserve all references

## Context Economy Optimization

### Token Budget Management
**Base Budget**: ≤200 tokens always-loaded (CLAUDE.md + essential imports)
**Conditional Budget**: ≤500 tokens per task-specific context loading
**Reference Budget**: Unlimited (zero cost until accessed)

### Optimization Strategies
1. **@ Import Elimination**: Convert 95%+ to reference links
2. **Line-Level Precision**: @file.md:15-30 instead of full files
3. **Conditional Instructions**: READ commands in CLAUDE_RULES.md
4. **Hub Navigation**: Central access points reduce redundant references

### Success Metrics
- **Context Reduction**: ≥90% reduction in always-loaded content
- **Functionality Preservation**: 100% workflows accessible via references
- **Reference Integrity**: Zero broken links after optimization
- **Authority Maintenance**: Hierarchy preserved without @ imports

## Integration Protocol

### Three-Layer Architecture Compatibility
**Layer 1 (Foundation)**: Core concepts ≤50 lines
**Layer 2 (Implementation)**: Detailed procedures ≤100 lines (NOT 150 as some docs state)
**Layer 3 (Validation)**: Quality gates ≤100 lines

### UltraThink x4 + PTS Integration
**UltraThink Analysis**: Apply progressive thinking to context architecture decisions
**PTS Validation**: All context changes must pass 12/12 PTS components
**Authority Compliance**: Changes align with docs/vision/ → CLAUDE_RULES hierarchy

---

## See Also
- **[Import Analysis Methodology](../standards/import-analysis-methodology.md)** - Rigorous analysis criteria
- **[Context Efficiency Optimization](../standards/context-efficiency-optimization.md)** - Systematic process
- **[Context Economy Metrics](../validation/context-economy-metrics.md)** - Measurement framework
- **[Folder Architecture Standards](../standards/folder-architecture-standards.md)** - Growth rules (coming)

**Application**: Apply this framework systematically to understand, map, and optimize context flow while maintaining system functionality and authority hierarchy integrity.