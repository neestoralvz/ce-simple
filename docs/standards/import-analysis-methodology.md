# Import Analysis Methodology Standard

**Updated**: 2025-07-24 | **Authority**: Context Economy Optimization | **Limit**: 100 lines  
**Navigation**: [System Hub](../navigation/index.md) | [Context Compaction](context-compaction-techniques.md) | [Import Criteria](import-vs-reference-criteria.md)

## Critical Understanding: @ Import Behavior

**CONFIRMED FACT**: @ imports work EXCLUSIVELY in CLAUDE.md files and load immediately when Claude Code starts, consuming token budget instantly. They do NOT work in regular documentation files.

## Rigorous Analysis Framework

### Five-Criteria Decision Matrix
**Apply systematically to every @ import with immediate loading reality**:

#### 1. Immediate Necessity Test
- **Question**: Absolutely essential for basic system function?
- **Reality**: This content loads EVERY session regardless of need
- **Pass**: Only truly universal content | **Fail**: Specialized or occasional content

#### 2. Session Frequency Analysis  
- **Question**: Used in 100% of sessions without exception?
- **Reality**: @ imports consume tokens even when unused
- **Pass**: Universal session content only | **Fail**: Any occasional-use content

#### 3. Context Economy Impact
- **Question**: Token cost justified for EVERY session?
- **Measurement**: Lines imported × session frequency = true cost
- **Pass**: <50 lines used every session | **Fail**: Any unused content

#### 4. Authority Hierarchy Validation
- **Question**: Represents single source requiring immediate access?
- **Reality**: Content loaded before any task context known
- **Pass**: Core system architecture only | **Fail**: Task-specific content

#### 5. Redundancy Elimination Check
- **Question**: Cannot be accessed via reference link?
- **Reality**: Reference links provide access without token cost
- **Pass**: Must be in memory immediately | **Fail**: Can wait for user request

## Classification System

### MANDATORY (@ Import - Always Load)
**Criteria**: ALL 5 tests pass + session failure without immediate access
**Examples**: EXTREMELY limited - possibly none
**Target**: ≤1 file, ≤50 total lines maximum

### REFERENCE (Link Without Import - Recommended)
**Criteria**: Any content not passing ALL 5 tests
**Examples**: Navigation hubs, documentation, standards, frameworks
**Format**: `[descriptive text](path/to/file.md)` - NO @ prefix
**Benefit**: Zero token cost until accessed

### INSTRUCTION (Conditional References - Alternative)
**Criteria**: Content needed conditionally based on task type
**Examples**: "When validating code, READ docs/core/pts-checklist.md"
**Format**: Reference links in conditional instructions (NO @ syntax)
**Benefit**: Claude loads only when instructed via reference links

### ELIMINATE (Remove Completely)
**Criteria**: Unnecessary for any workflow
**Examples**: Broken references, duplicate content, outdated information
**Action**: Delete reference completely

## Analysis Process

### Step 1: Inventory (5 minutes)
1. **Extract CLAUDE.md @ References**: Use grep search ONLY on CLAUDE.md files
2. **Calculate True Cost**: Every @ import = immediate token consumption (CLAUDE.md only)
3. **Measure Current Load**: Sum total lines of always-loaded content from CLAUDE.md

### Step 2: Ruthless Evaluation (10 minutes per import)
1. **Apply Five-Criteria Matrix**: ALL 5 must pass for @ import justification
2. **Measure Real Impact**: Lines imported × 100% session frequency = true cost
3. **Validate Necessity**: Can system function without immediate access?
4. **Test Reference Alternative**: Can link provide adequate access?

### Step 3: Optimization & Conversion (15 minutes)
1. **Eliminate @ Imports**: Convert non-essential CLAUDE.md @ imports to reference links
2. **Create Instructions**: Add conditional reading instructions using reference links (NO @)
3. **Validate References**: Ensure all links functional and accessible
4. **Measure Savings**: Calculate actual token reduction achieved

## Success Metrics

### Quantitative Targets
- **Context Reduction**: ≥95% reduction in always-loaded @ imports
- **Reference Accuracy**: 100% functional reference links
- **Loading Efficiency**: ≤50 lines always-loaded maximum
- **Token Economy**: Dramatic reduction in base session cost

### Qualitative Improvements
- **True Conditional Loading**: Content loaded only when needed
- **Authority Preservation**: Access maintained via reference links
- **System Responsiveness**: Minimal base context, maximum efficiency
- **User Control**: Content loaded based on actual task requirements

---

## See Also
- **[Claude.md Import Methodology](claude-md-import-methodology.md)** - Corrected @ import scope understanding
- **[Context Efficiency Optimization](context-efficiency-optimization.md)** - Systematic optimization process
- **[Context Economy Metrics](../validation/context-economy-metrics.md)** - Measurement framework
- **[System Navigation](../navigation/index.md)** - Complete system access

**Application**: Apply this methodology systematically to achieve measurable context economy improvements while maintaining system functionality and authority hierarchy integrity.