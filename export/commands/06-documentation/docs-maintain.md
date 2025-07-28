# /docs-maintain - Documentation Maintenance System

## Purpose
Orchestrates comprehensive documentation maintenance through parallel analysis, consolidation, optimization, and validation with automated quality assurance protocols.

## Principles and Guidelines
- **Parallel Execution**: Deploy concurrent analysis, consolidation, optimization, and validation tasks
- **Quality Assurance**: Automated error detection, broken link resolution, and content validation
- **Progressive Disclosure**: Split oversized files while maintaining coherent structure
- **Self-Validation**: Built-in integrity checks ensuring maintenance quality standards

## Execution Process

### Phase 1: Structure Analysis
Update TodoWrite mark "documentation structure analysis" as in_progress

Analyze documentation directory structure using LS and Bash:
- Map file relationships and cross-references
- Identify oversized files requiring progressive disclosure
- Detect broken links and missing dependencies
- Generate structure health metrics

### Phase 2: Content Consolidation
Update TodoWrite complete previous, mark "content consolidation" as in_progress

Consolidate duplicate content using Grep and Edit:
- Merge redundant documentation sections
- Repair cross-reference links during consolidation
- Preserve chronological information and context
- Update file references across system

### Phase 3: Optimization & Validation
Update TodoWrite complete previous, mark "optimization validation" as in_progress

Optimize documentation structure using parallel validation:
- Implement progressive disclosure for oversized files
- Validate cross-references and internal links
- Check documentation standards compliance
- Generate comprehensive health report

### Phase 4: Quality Reporting
Update TodoWrite complete previous, mark "quality reporting" as in_progress

Generate maintenance summary using Write and Bash:
- Create system health report with metrics
- Document improvements and optimizations performed
- Provide actionable recommendations for future maintenance
- Commit changes with detailed improvement summary

### Phase 5: Command Routing and Handoff
Update TodoWrite complete previous, mark "command routing and handoff" as in_progress

**Context Analysis**: Review documentation maintenance outcomes and identify integration opportunities
- Analyze documentation structure changes and validation requirements
- Assess need for validation commands based on structural modifications
- Evaluate learning capture opportunities from maintenance patterns
- Consider matrix validation requirements for cross-reference updates

**Intelligent Routing**: Route to 4-6 related commands based on documentation outcomes
- **Documentation validation flow**: /validate-complete (high) - verify documentation integrity post-maintenance
- **Learning extraction**: /capture-learnings (medium) - extract maintenance patterns for future optimization
- **System monitoring**: /system-monitor (medium) - track documentation health metrics over time
- **Matrix validation**: /matrix-maintenance (low) - validate cross-reference consistency after structural changes
- **Context optimization**: /context-optimize (low) - consolidate documentation context for performance
- **Performance tracking**: /performance-track (low) - measure documentation maintenance efficiency

**Handoff Protocol**: Format: "Next: /command (priority) - rationale"

Update TodoWrite complete all documentation maintenance tasks

**Error Handling**: Automatically detect broken references, generate merge recommendations, implement progressive disclosure, create placeholder files with proper structure

---

docs/core/README.md
docs/core/system-principles.md