# Docs Optimize - CLAUDE.md and Standards Compliance Optimization

## 🎯 Purpose
Optimize CLAUDE.md according to official Anthropic standards, maintain date accuracy for temporal context, and ensure comprehensive compliance across documentation system.

## 🚀 Usage
Execute: `/docs-optimize [target]`

## 🔧 Implementation

### Optimization Protocol
1. **CLAUDE.MD ANALYSIS**: Evaluate against official Anthropic standards and token efficiency
2. **DATE MAINTENANCE**: Verify and update "Last Updated: YYYY-MM-DD" for temporal context accuracy
3. **STANDARDS COMPLIANCE**: Validate system-wide adherence to established policies
4. **TOKEN OPTIMIZATION**: Reduce cognitive load while maintaining information completeness
5. **STRUCTURE REFINEMENT**: Implement progressive disclosure and navigation optimization
6. **INTEGRATION VALIDATION**: Ensure compatibility with Claude Code workflows

### CLAUDE.md Optimization Framework

#### Anthropic Standards Compliance
**Official Requirements Validation**:
- **File Hierarchy**: Verify project root placement and structure compliance
- **Content Sections**: Validate tech stack, bash commands, code style, project structure
- **Import System**: Test @path/to/import functionality and avoid circular references
- **Token Efficiency**: Optimize content density and context window usage

#### Date Maintenance Framework
**Temporal Context Management**:
- **Current Date Verification**: Check if "Last Updated: YYYY-MM-DD" exists in CLAUDE.md header
- **Date Accuracy**: Validate date reflects actual last modification date
- **Discovery Context**: Ensure all exploration and discovery operations can reference accurate temporal context
- **Standards Enforcement**: Apply date maintenance requirements from writing standards

#### Content Structure Analysis
**Current CLAUDE.md Assessment**:
```bash
# Line count and density analysis
wc -l CLAUDE.md
grep -c "^#" CLAUDE.md  # Header count
grep -c "@" CLAUDE.md   # Import reference count
```

**Optimization Targets**:
- **Token Efficiency**: Reduce redundant content and optimize information density
- **Navigation Structure**: Implement clear hierarchy and strategic cross-references
- **Progressive Disclosure**: Move complex details to referenced files
- **Essential Focus**: Maintain only mission-critical project information

### System-Wide Standards Compliance

#### File Size Policy Enforcement
**Compliance Validation**:
```bash
# Commands size compliance (≤140 optimal, 200 max)
find .claude/commands -name "*.md" -exec wc -l {} \; | awk '$1 > 140'

# Documentation size compliance (≤200 max)
find standards context -name "*.md" -exec wc -l {} \; | awk '$1 > 200'
```

**Optimization Strategies**:
- **Size Violations**: Apply progressive disclosure extraction
- **Content Optimization**: Eliminate redundancy and improve density
- **Structural Refinement**: Maintain functionality within size constraints
- **Reference Implementation**: Replace inline content with external links

#### Cross-Reference Network Optimization

#### Reference Density Management
**CLAUDE.md Cross-Reference Analysis**:
- **Current State**: Evaluate internal link density and navigation efficiency
- **Optimization Target**: Reduce to ≤20 essential references
- **Strategic Linking**: Implement hub-based navigation architecture
- **Bidirectional Flow**: Ensure reverse navigation capabilities

**Reference Quality Improvement**:
- **Authority Clarification**: Establish clear primary sources for each concept
- **Link Validation**: Verify all references functional and accurate
- **Navigation Efficiency**: Optimize cognitive steps to information access
- **Hub Implementation**: Create strategic navigation entry points

### Token Efficiency Optimization

#### Content Density Enhancement
**Information Value Maximization**:
- **Redundancy Elimination**: Remove duplicate explanations across files
- **Concept Consolidation**: Unify related information in appropriate locations
- **Essential Focus**: Prioritize high-impact, frequently-accessed information
- **Progressive Detail**: Layer information complexity appropriately

#### Claude Code Integration
**Workflow Optimization**:
- **Memory Management**: Optimize for Claude Code's context handling
- **Command Integration**: Ensure seamless interaction with slash commands
- **Session Efficiency**: Minimize context loading overhead
- **Performance Focus**: Enhance Claude's operational effectiveness

### Quality Assurance Validation

#### Optimization Success Metrics
**Performance Indicators**:
- **Token Efficiency**: 30% reduction in redundant content
- **Navigation Speed**: ≤2.5 cognitive steps to any information
- **Compliance Rate**: 100% adherence to size and structure standards
- **Integration Quality**: Seamless Claude Code workflow operation

#### Post-Optimization Validation
**Systematic Verification**:
- [ ] CLAUDE.md complies with all Anthropic official standards
- [ ] "Last Updated: YYYY-MM-DD" header exists and reflects current date
- [ ] Date maintenance enables accurate discovery and exploration temporal references
- [ ] System-wide file size compliance achieved
- [ ] Cross-reference network optimized and functional
- [ ] Token efficiency targets met without information loss
- [ ] Claude Code integration verified and optimized

## ⚡ Triggers

### Input Triggers
**Context**: Post-consolidation system requiring standards optimization
**Previous**: `/docs-consolidate` → content unified, optimization needed
**Keywords**: optimize, CLAUDE.md, standards, compliance, token, efficiency

### Output Triggers
**When**: Optimization complete → `/docs-validate` for comprehensive verification
**When**: Complete workflow → `/docs-workflow` for automated full optimization
**When**: Complex issues discovered → `/docs-consolidate` for additional unification
**Chain**: audit → consolidate → optimize → validate (granular) OR audit → workflow (complete)

### Success Patterns
**CLAUDE.md Success**: Anthropic compliance achieved → Enhanced Claude Code integration
**Standards Success**: 100% system compliance → Automated validation enabled
**Efficiency Success**: Token optimization achieved → Improved operational performance

## 🔗 See Also

### Related Commands
- Execute `/docs-workflow` for complete automated documentation optimization workflow
- Execute `/docs-audit` for comprehensive system analysis before optimization
- Execute `/docs-consolidate` for content unification prior to optimization
- Execute `/docs-validate` for post-optimization system verification

### Integration References
- `context/research/anthropic-claude-md-standards.md` - Official optimization criteria
- `standards/writing-standards.md` - System compliance requirements
- `standards/simplicity-principles.md` - Optimization implementation guidelines
- `context/discoveries/documentation-workflow-discoveries.md` - Optimization methodology

---

**CRITICAL**: This command ensures maximum system effectiveness through standards compliance and token optimization while maintaining complete functional integrity and Claude Code compatibility.