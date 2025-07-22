# Docs Audit - Documentation Structure and Health Analysis

## 🎯 Purpose
Systematically analyze documentation structure, identify content duplication, validate cross-references, and assess system health for markdown documentation ecosystem.

## 🚀 Usage
Execute: `/docs-audit [scope]`

## 🔧 Implementation

### Documentation Audit Protocol
1. **STRUCTURE MAPPING**: Complete directory and file inventory with line counts
2. **DUPLICATION DETECTION**: Content overlap identification and impact assessment
3. **REFERENCE VALIDATION**: Cross-reference health and broken link analysis
4. **STANDARDS COMPLIANCE**: File size limits and formatting consistency check
5. **HEALTH ASSESSMENT**: Overall system coherence and navigation efficiency

### Parallel Analysis Framework

#### Core Audit Tasks (Parallel Execution)
**MANDATORY**: Deploy multiple Task Tools for comprehensive coverage

**Essential Analysis Operations**:
- **File Structure Analysis**: Map all .md files with sizes, modification dates, dependencies
- **Content Duplication Scan**: Identify overlapping content, redundant explanations, concept repetition
- **Cross-Reference Validation**: Test all internal links, identify broken references, map authority chains
- **Standards Compliance Check**: Validate file size limits, formatting consistency, naming conventions

### Analysis Output Standards
**Audit Report Generation**:
```
📊 DOCUMENTATION AUDIT REPORT
Structure: [X] files analyzed, [Y] total lines, [Z] directories
Duplication: [X]% content overlap detected across [Y] file pairs
References: [X]% functional links, [Y] broken references identified
Compliance: [X]% files within size limits, [Y] standard violations
Health Score: [X]/100 (Navigation: [Y], Density: [Z], Coherence: [W])
```

### Analysis Framework
**Issue Classification**: CRITICAL (>40% duplication, >10% broken links) → WARNING (20-40%, 5-10%) → INFO (<20%, <5%)

**Health Scoring**: Link integrity (25pts) + Navigation efficiency (10pts) + Content density (25pts) + Structure coherence (25pts) + Compliance (15pts) = 100pts total

**Quality Thresholds**: >90pts (Excellent) → 75-90pts (Good) → 60-75pts (Moderate) → <60pts (Poor)

## ⚡ Triggers

### Input Triggers
**Context**: Documentation maintenance needs, system health assessment requirements
**Previous**: `/start` → documentation workflow detection → `/docs-audit`
**Keywords**: documentation, audit, health, structure, references, duplication

### Output Triggers
**When**: Issues detected → `/docs-workflow maintain` for automated optimization
**When**: Quality score <85% → Auto-trigger recursive correction workflow  
**When**: System healthy → Regular health checks with `/docs-audit` + Git baseline
**When**: Todo plans detected → `/docs-workflow` (complete pipeline with generation)
**Chain**: audit → workflow (complete) OR audit → generate → optimize → validate (with plans)

### Git Integration Protocol
**BASELINE ESTABLISHMENT**: Automatic Git tracking for audit sessions with quality benchmarking

**Automated Commit Templates**: Generate standardized commit messages based on audit findings and system health status

### Success Patterns
**Audit Success**: >95% structure mapped → Comprehensive analysis complete
**Issue Identification**: Critical problems identified → Prioritized remediation plan
**Health Assessment**: Baseline established → Improvement targets defined

## 🔗 See Also

### Implementation Details
- `../../standards/docs-audit-metrics.md` - Complete metrics calculation and validation protocols

### Related Commands
- Execute `/docs-workflow` for complete automated documentation optimization
- Execute `/docs-consolidate` for targeted content unification and duplication resolution
- Execute `/docs-optimize` for specific CLAUDE.md optimization and standards compliance
- Execute `/docs-validate` for isolated cross-reference health verification

### Integration References
- `context/discoveries/documentation-workflow-discoveries.md` - Audit methodology basis
- `context/research/anthropic-claude-md-standards.md` - Compliance validation criteria
- `../../standards/simplicity-principles.md` - Structural assessment framework
- `../../standards/writing-standards.md` - Content quality evaluation standards

---

**CRITICAL**: This command provides comprehensive documentation health assessment and must maintain focus on actionable insights rather than exhaustive reporting. Audit findings should directly enable targeted remediation workflows.