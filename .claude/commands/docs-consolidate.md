# Docs Consolidate - Content Unification and Reference Repair

## 🎯 Purpose
Systematically unify duplicated content, repair broken references, and consolidate fragmented information while maintaining system architectural integrity.

## 🚀 Usage
Execute: `/docs-consolidate [scope]`

## 🔧 Implementation

### Consolidation Protocol
1. **DUPLICATION RESOLUTION**: Identify and merge overlapping content across files
2. **REFERENCE REPAIR**: Fix broken cross-references and create missing target files
3. **CONTENT UNIFICATION**: Consolidate fragmented concepts into authoritative sources
4. **PROGRESSIVE DISCLOSURE**: Extract verbose content to appropriate architectural layers
5. **INTEGRITY VALIDATION**: Ensure consolidation maintains system coherence

### Parallel Consolidation Framework

#### Core Consolidation Tasks (Sequential Execution)
**MANDATORY**: Execute in dependency order to prevent reference breaks

**Essential Operations**:
- **Content Overlap Analysis**: Identify duplicate concepts and determine authoritative sources
- **Reference Chain Mapping**: Trace all cross-references and identify repair requirements
- **Progressive Extraction**: Move detailed content from commands to standards/context layers
- **Authority Establishment**: Designate single sources of truth for each concept domain

### Consolidation Strategies

#### Duplication Resolution Matrix
**HIGH Priority** (>40% overlap):
- Merge files with substantial content duplication
- Establish single authoritative source
- Create reference links from eliminated locations
- Preserve unique value-adding content

**MEDIUM Priority** (20-40% overlap):
- Consolidate overlapping sections within files
- Standardize terminology and explanations
- Cross-reference shared concepts
- Eliminate redundant examples

**LOW Priority** (<20% overlap):
- Optimize cross-reference patterns
- Standardize formatting and structure
- Unify symbol usage and conventions
- Streamline navigation paths

#### Reference Repair Operations
**Broken Reference Patterns**:
```bash
# Identify broken internal links
grep -r "\.md\b" --include="*.md" . | grep -v "archive"

# Validate file existence for references
find . -name "*.md" -exec basename {} \; | sort
```

**Repair Strategies**:
- **Create Missing Files**: Generate referenced files with appropriate content
- **Update References**: Modify links to point to consolidated locations
- **Bidirectional Linking**: Ensure reverse navigation capabilities
- **Authority Chain**: Establish clear hierarchy for cross-references

### Content Extraction Guidelines

#### Progressive Disclosure Implementation
**Commands** (≤140 lines optimal):
- Extract educational content → Move to context layer
- Extract detailed criteria → Move to standards layer
- Extract examples → Move to pattern documentation
- Maintain execution focus and coordination instructions

**Standards** (≤200 lines):
- Consolidate framework documentation
- Unify criteria and metrics
- Establish authoritative guidelines
- Cross-reference related concepts

**Context** (≤200 lines):
- Consolidate learning patterns
- Document discovered relationships
- Capture implementation examples
- Preserve historical decisions

### File Size Optimization

#### Size Violation Resolution
**Commands Exceeding Limits**:
- Apply progressive disclosure principles
- Extract verbose sections to external files
- Optimize redundant explanations
- Maintain coordination functionality

**Documentation Exceeding Limits**:
- Identify consolidation opportunities
- Merge related concept files
- Eliminate redundant sections
- Preserve information completeness

### Quality Assurance Protocols

#### Consolidation Validation
**Post-Consolidation Checklist**:
- [ ] All references functional and verified
- [ ] No information loss during consolidation
- [ ] File size compliance achieved
- [ ] Architectural boundaries maintained
- [ ] Navigation efficiency improved

**Success Metrics**:
- Content duplication reduced to <5%
- 100% functional cross-references
- File size compliance achieved
- Navigation steps ≤2.5 cognitive units
- System coherence maintained

## ⚡ Triggers

### Input Triggers
**Context**: Post-audit identification of duplication and reference issues
**Previous**: `/docs-audit` → identified consolidation requirements
**Keywords**: consolidate, unify, merge, repair, references, duplication

### Output Triggers
**When**: Content unified → `/docs-optimize` for standards compliance
**When**: Complete workflow → `/docs-workflow` for automated optimization
**When**: Complex size violations → `/docs-validate` for architecture verification
**Chain**: audit → consolidate → optimize → validate (granular) OR audit → workflow (complete)

### Success Patterns
**Consolidation Success**: <5% content duplication → Architectural integrity achieved
**Reference Success**: 100% functional links → Navigation completeness verified
**Size Success**: All files compliant → Progressive disclosure effective

## 🔗 See Also

### Related Commands
- Execute `/docs-workflow` for complete automated documentation optimization workflow
- Execute `/docs-audit` for comprehensive system analysis and issue identification
- Execute `/docs-optimize` for CLAUDE.md optimization and standards compliance
- Execute `/docs-validate` for post-consolidation system health verification

### Integration References
- `context/discoveries/documentation-workflow-discoveries.md` - Consolidation methodology
- `standards/simplicity-principles.md` - Progressive disclosure implementation
- `standards/writing-standards.md` - Content unification standards
- `context/patterns/command-complexity-management.md` - Architectural integrity patterns

---

**CRITICAL**: This command transforms system architecture through consolidation while maintaining information completeness and functional integrity. All consolidation operations must preserve essential content value.