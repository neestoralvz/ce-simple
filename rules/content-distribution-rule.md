# Content Distribution Rule

**Purpose**: Consolidation vs distribution decision criteria for optimal organization  
**Authority**: Extracted from docs/decisions/governance/pts-placement-decision.md  
**Trigger**: Content organization, system restructuring, architectural decisions  
**Status**: Active | **Lines**: ≤80

## When to Consolidate vs Distribute

### Consolidate When
**Criteria**:
- Content duplication >60% across files
- No functional separation between content types
- User workflow requires all content simultaneously
- Maintenance burden exceeds organizational benefit

**Test**: If users always need A + B together → Consolidate

### Distribute When  
**Criteria**:
- Clear functional separation exists
- Different user workflows access different content
- Authority hierarchy requires separation
- Navigation patterns support distribution

**Test**: If A serves different purpose than B → Distribute

## Distribution Decision Framework

### Documentation First Rule
1. **ANALYZE**: Examine complete system structure & patterns
2. **DECIDE**: Evaluate options based on organizational consistency  
3. **DOCUMENT**: Record architectural decision with rationale
4. **CREATE**: Implement optimal structure (consolidate or distribute)

### Organizational Consistency Priority
- Preserve existing navigation patterns
- Maintain established authority hierarchy  
- Support user workflow optimization
- Ensure functional coherence

### Authority Hierarchy Preservation
**Maintain established flow**:
- `user-input/` → `CLAUDE_RULES` → `docs/core/` → implementation
- Each location serves distinct function in system navigation
- Clear precedence prevents conflicts

## Quality Gates

### Content Analysis
- **100% unique content preserved** across all files
- **Duplication eliminated** through smart distribution
- **Navigation patterns maintained** - users find content where expected
- **Cross-references optimized** - clear connections between related content

### Future Scalability
- Each directory can expand independently
- System handles distributed content effectively  
- No structural changes required for growth
- Clean integration & maintenance protocols

## Implementation Strategy

**Phase 1**: Analyze current distribution & identify optimization opportunities  
**Phase 2**: Apply decision criteria to determine optimal structure  
**Phase 3**: Preserve unique content while eliminating pure duplication  
**Phase 4**: Establish clear cross-references & integration points

## Precedent Established

**Principle**: When consolidating distributed content, prioritize preservation of existing navigation patterns and functional separation over co-location convenience.

---

**🤖 IMPLEMENTATION AGENT**: Apply distribution analysis when restructuring content organization  
**🔍 VALIDATION AGENT**: Verify distribution decisions preserve navigation & authority hierarchy