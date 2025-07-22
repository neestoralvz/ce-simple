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

### Issue Categorization Matrix
**CRITICAL Issues** (Immediate attention required):
- Duplicate content >40% overlap between files
- Broken references >10% of total links
- File size violations >200 lines
- Authority conflicts (multiple files claiming same domain)

**WARNING Issues** (Review recommended):
- Moderate duplication 20-40% overlap
- Broken references 5-10% of total links
- File size approaching limits 180-200 lines
- Cross-reference gaps in navigation chain

**INFO Issues** (Optimization opportunities):
- Minor duplication <20% overlap
- Isolated broken references <5%
- Suboptimal file organization
- Navigation efficiency improvements available

### Health Metrics Calculation
**Documentation Effectiveness Scoring**:
- **Link Health**: Functional references / Total references × 25 points
- **Navigation Efficiency**: (3.0 - Average cognitive steps) × 10 points
- **Content Density**: Value per cognitive unit × 25 points
- **Structural Coherence**: Logical organization assessment × 25 points
- **Standards Compliance**: Files within limits / Total files × 15 points

**Target Thresholds**:
- >90 points: Excellent documentation health
- 75-90 points: Good health with minor optimization opportunities
- 60-75 points: Moderate health requiring attention
- <60 points: Poor health requiring systematic remediation

### Automated Validation Protocols
**Quick Health Check Commands**:
```bash
# File size validation
find . -name "*.md" -exec wc -l {} \; | awk '$1 > 200'

# Cross-reference validation
grep -r "\.md" --include="*.md" . | grep -v "archive"

# Duplication detection pattern
grep -r "CRITICAL\|MANDATORY\|REQUIRED" --include="*.md" .
```

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
**BASELINE ESTABLISHMENT**: Automatic Git tracking for audit sessions establishing quality baselines

**Audit Completion Commit** (when significant findings):
```bash
git add . && git commit -m "docs-audit: System health assessment completed

📊 AUDIT RESULTS:
- Files analyzed: [N]
- Health score: [X]%
- Issues identified: [N] critical, [N] warning, [N] info
- Analysis duration: [X] minutes

🔍 SYSTEM STATUS:
- Reference integrity: [X]%
- Template compliance: [X]%
- Cross-reference health: [X]%
- Content quality: [X]%

🎯 RECOMMENDATIONS:
- Priority actions: [list]
- Workflow triggers: [triggered/not-triggered]
- Next audit recommended: [timeframe]
- System trend: [improving/stable/declining]

📈 BASELINE ESTABLISHED:
- Quality benchmark: [X]% for future comparisons
- Issue tracking: [patterns identified]
- Performance baseline: [metrics captured]

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"
```

**Health Check Commit** (for regular maintenance audits):
```bash
git add . && git commit -m "docs-audit: Regular health check completed

📊 HEALTH CHECK: [Date] system maintenance validation
✅ Status: [Healthy/Attention-Needed/Critical]
📈 Quality: [X]% (trend: [direction])
🔧 Actions: [none-required/maintenance-scheduled/immediate-attention]

🤖 Generated with Claude Code - Health Check
Co-Authored-By: Claude <noreply@anthropic.com>"
```

### Success Patterns
**Audit Success**: >95% structure mapped → Comprehensive analysis complete
**Issue Identification**: Critical problems identified → Prioritized remediation plan
**Health Assessment**: Baseline established → Improvement targets defined

## 🔗 See Also

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