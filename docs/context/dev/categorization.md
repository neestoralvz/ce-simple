# Semantic Categorization Framework

## Purpose
Three-tier semantic categorization system for context files with intelligent updating and consolidation.

## Framework Overview
Based on knowledge management systems, AI agent context organization, and technical documentation standards.

See [semantic-categorization-details.md](semantic-categorization-details.md) for complete research foundation and specifications.

## Research Foundation

### Key Principles
- AI-powered categorization with human oversight
- Semantic networks beyond hierarchical structures
- Content lifecycle management with freshness assessment
- Context engineering through iterative refinement

### Standards
- Semantic ladder: Glossaries → Taxonomies → Ontologies
- Content-based organization by semantic intent
- Optimal 2-3 hierarchical levels
- Strong cross-reference integration

## Three-Tier System

### Tier 1: Primary Categories

#### Development (`dev/`)
Coding, implementation, analysis, patterns, tools

#### Operations (`ops/`)
Maintenance, workflows, monitoring, validation

#### Learning (`learn/`)
Discoveries, experiences, insights, research

#### System (`sys/`)
Architecture, integration, governance, evolution

### Tier 2: Domain Modifiers

#### By Scope
- `micro/` - Component-level details
- `macro/` - System-level concerns
- `meta/` - Framework-level approaches

#### By Time
- `historical/` - Past decisions, legacy
- `current/` - Active development
- `future/` - Planning, roadmaps

#### By Complexity
- `simple/` - Basic patterns
- `complex/` - Advanced architectures  
- `critical/` - Mission-critical

### Tier 3: Content Types

#### Naming: `[type]-[theme]-[date].md`

**Analysis**: analysis-, assessment-, matrix-
**Learning**: discovery-, interview-, pattern-, insight-
**System**: protocol-, framework-, report-, validation-
**Research**: research-, comparison-, survey-

## Decision Rules

### File Management
**Create New**: Theme uniqueness, content type shift, line limit approach
**Update Existing**: Theme continuation, content evolution, capacity available
**Split File**: Exceeds 180 lines, multi-theme content, complexity divergence

### Consolidation
**Triggers**: >70% semantic overlap, theme redundancy, fragmentary content
**Process**: AI similarity assessment, theme mapping, hierarchy establishment

## Integration

### Command Applications
- **capture-learnings**: learn/discoveries/, discovery-/interview-/insight- types
- **explore-codebase**: dev/analysis/, analysis-/pattern-/assessment- types  
- **explore-web**: learn/research/, research-/comparison-/survey- types
- **matrix-maintenance**: sys/architecture/, protocol-/validation- types

See [semantic-categorization-integration.md](semantic-categorization-integration.md) for complete command specifications.

### Git Integration

#### Commit Standards
`[category]/[subcategory]: [action] [theme] [content-type]`

#### Branch Organization
- `feature/[category]-[theme]`
- `content/[category]-[subcategory]-update`
- `maintenance/categorization-framework-update`

## Line Limits

### Thresholds
- **Optimal**: 80-150 lines
- **Acceptable**: 150-180 lines
- **Warning**: 180-200 lines
- **Maximum**: 200 lines (mandatory split)

### Splitting Strategies
**Thematic**: Extract secondary themes with cross-references
**Temporal**: Separate historical, current, and future content
**Complexity**: Progressive disclosure with layered documentation

## Implementation

### Success Metrics
- Categorization accuracy: >95%
- File discovery time: <30 seconds
- Cross-reference integrity: >98%
- Line limit compliance: <5% files exceeding 200 lines

### Benefits
- Predictable organization with intuitive navigation
- Intelligent consolidation reducing fragmentation
- Context preservation through semantic grouping
- Progressive disclosure supporting different depth requirements

---

See [semantic-categorization-details.md](semantic-categorization-details.md) for complete implementation guidelines, quality controls, and technical specifications.