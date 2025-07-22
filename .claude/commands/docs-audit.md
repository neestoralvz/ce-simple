# Docs Audit - Documentation Structure and Health Analysis

## 🎯 Purpose
Systematically analyze documentation structure, identify content duplication, validate cross-references, and assess system health for markdown documentation ecosystem.

## 🚀 Usage
Execute: `/docs-audit [scope]`

## 🔧 Implementation

### Behavioral Reinforcement Protocol
**MANDATORY at audit initialization**:

```javascript
TodoWrite([
  {"content": "📋 MAPPING: Execute comprehensive structure and file inventory", "status": "pending", "priority": "high", "id": "audit-mapping-1"},
  {"content": "🔍 DUPLICATION: Identify content overlap and redundancy patterns", "status": "pending", "priority": "high", "id": "audit-duplication-1"},
  {"content": "🔗 REFERENCES: Validate cross-reference health and link integrity", "status": "pending", "priority": "high", "id": "audit-references-1"},
  {"content": "📊 HEALTH: Calculate system health score and compliance metrics", "status": "pending", "priority": "medium", "id": "audit-health-1"},
  {"content": "📝 REPORT: Generate comprehensive audit report with recommendations", "status": "pending", "priority": "medium", "id": "audit-report-1"}
])
```

**Issue-Driven Analysis**: Add priority todos based on critical issues discovered during audit

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
- `../docs/quality/docs-audit-metrics.md` - Complete metrics calculation and validation protocols

### Related Commands
- Execute `/docs-workflow` for complete automated documentation optimization
- Execute `/docs-consolidate` for targeted content unification and duplication resolution
- Execute `/docs-optimize` for specific CLAUDE.md optimization and standards compliance
- Execute `/docs-validate` for isolated cross-reference health verification

### Integration References
- `context/discoveries/documentation-workflow-discoveries.md` - Audit methodology basis
- `context/research/anthropic-claude-md-standards.md` - Compliance validation criteria
- `../docs/documentation/simplicity-principles.md` - Structural assessment framework
- `../docs/documentation/writing-standards.md` - Content quality evaluation standards

---

## ⚡ EXECUTION LAYER

### Mandatory Tool Executions
**CRITICAL**: Actual implementation of comprehensive documentation structure and health analysis

```javascript
// COMPREHENSIVE DOCUMENTATION AUDIT SYSTEM
// Execute systematic documentation health assessment

// 1. STRUCTURE MAPPING AND INVENTORY
// Complete file system analysis
Glob("**/*.md", {path: "."})                                    // All markdown files
Glob(".claude/**/*.md", {path: "."})                            // Command system files
Glob("docs/**/*.md", {path: "."})                               // Documentation files
Glob("context/**/*.md", {path: "."})                            // Context files

// File size analysis
Bash("find . -name '*.md' -exec wc -l {} + | sort -n")         // Line counts sorted
Bash("find . -name '*.md' -exec ls -la {} + | awk '{print $5, $9}' | sort -n") // File sizes

// 2. CONTENT DUPLICATION DETECTION
// Identify overlapping content patterns
Grep("## Purpose|## Usage|## Implementation", {glob: "**/*.md", output_mode: "content", -n: true}) // Header patterns
Grep("MANDATORY|CRITICAL|Execute:", {glob: "**/*.md", output_mode: "content", -n: true})           // Common phrases
Grep("TodoWrite|Task|Bash|Write|Read", {glob: "**/*.md", output_mode: "content", -n: true})        // Tool patterns

// 3. CROSS-REFERENCE VALIDATION
// Comprehensive link integrity analysis
Grep("\\[.*\\]\\(.*\\.md\\)", {glob: "**/*.md", output_mode: "content", -n: true})  // Markdown links
Grep("/[a-zA-Z-]+", {glob: "**/*.md", output_mode: "content", -n: true})             // Slash commands
Grep("docs/|context/|\\.claude/|standards/", {glob: "**/*.md", output_mode: "content", -n: true}) // Directory refs

// 4. STANDARDS COMPLIANCE CHECK
// File size and formatting validation
Bash("find . -name '*.md' -exec awk 'END{if(NR>200) print FILENAME \" exceeds 200 lines: \" NR}' {} +") // Size violations
Grep("Last Updated:|YYYY-MM-DD", {glob: "**/*.md", output_mode: "content"})        // Date maintenance
Grep("^# [A-Z]", {glob: "**/*.md", output_mode: "content"})                         // Header format

// 5. HEALTH ASSESSMENT CALCULATION
// Generate comprehensive audit report
Write("context/discoveries/documentation-audit-[timestamp].md", `# Documentation Audit Report

## System Overview
- Total Files: [total_files]
- Commands: [command_count]
- Documentation: [docs_count]
- Context Files: [context_count]
- Total Lines: [total_lines]

## Structure Analysis
- Average File Size: [avg_size] lines
- Size Violations: [violations] files >200 lines
- Directory Distribution: [distribution_breakdown]

## Content Duplication Assessment
- Duplicate Header Patterns: [header_duplicates]
- Common Phrase Overlap: [phrase_overlap]%
- Tool Pattern Repetition: [tool_pattern_overlap]%
- **Overall Duplication**: [duplication_percentage]%

## Cross-Reference Health
- Total References: [total_references]
- Functional Links: [functional_links]
- Broken References: [broken_count]
- **Link Integrity**: [link_percentage]%

## Standards Compliance
- Size Compliance: [compliant_files]/[total_files] files
- Date Maintenance: [dated_files] files with timestamps
- Header Standards: [standard_headers] compliant
- **Compliance Score**: [compliance_percentage]%

## Health Score Calculation
- Link Integrity (25pts): [link_score]/25
- Content Density (25pts): [density_score]/25
- Structure Coherence (25pts): [structure_score]/25
- Standards Compliance (25pts): [compliance_score]/25
- **TOTAL HEALTH SCORE**: [total_score]/100

## Issue Classification
- **CRITICAL**: [critical_issues] (>40% duplication, >10% broken links)
- **WARNING**: [warning_issues] (20-40% duplication, 5-10% broken)
- **INFO**: [info_issues] (<20% duplication, <5% broken)

## Recommendations
[Prioritized action items based on findings]
`)

// Optimized health metrics calculations (3 → 1 authorization)  
Bash("echo 'scale=1;
link_integrity_pct = ([functional_links] * 100) / [total_references];
compliance_pct = ([compliant_files] * 100) / [total_files];
content_density_pct = (100 - [duplication_percentage]);
print \"Link Integrity: \", link_integrity_pct, \"%\";
print \"Size Compliance: \", compliance_pct, \"%\";
print \"Content Density: \", content_density_pct, \"%\"' | bc")

// 7. DECISION LOGIC FOR NEXT STEPS
// Auto-trigger workflow based on health score
Bash("echo 'Health assessment complete: [total_score]/100'")
Bash("echo 'Critical issues: [critical_count] | Warning issues: [warning_count]'")
Bash("echo 'Recommendation: [WORKFLOW_MAINTAIN|CONSOLIDATE_FIRST|AUDIT_ONLY]'")
```

### Audit Assessment Logic
**HEALTH SCORING COMPONENTS**:
- **Link Integrity** (25pts): Functional references / Total references × 25
- **Content Density** (25pts): (100 - Duplication percentage) × 0.25
- **Structure Coherence** (25pts): Compliance score × 0.25  
- **Standards Compliance** (25pts): Size + format compliance × 0.25

### Issue Classification Framework
**CRITICAL THRESHOLDS**:
- Duplication >40% OR Broken links >10% OR Health <60
- **Action**: Immediate remediation required

**WARNING THRESHOLDS**:
- Duplication 20-40% OR Broken links 5-10% OR Health 60-85
- **Action**: Optimization recommended

### Session Completion Protocol
**MANDATORY WORKFLOW END**:
```javascript
// Git automation with audit metrics
Bash("git add . && git commit -m \"docs-audit: health [score]/100 | issues: [critical]/[warning]/[info] ✓session-[N]\"")
```

### Execution Verification
**TOOL CALL AUDIT**:
- **Structure mapping**: 4 Glob + 2 Bash operations for inventory
- **Duplication detection**: 3 Grep operations for content analysis
- **Reference validation**: 3 Grep operations for link testing
- **Compliance checking**: 1 Bash + 3 Grep operations for standards
- **Health assessment**: 1 Write operation for report generation
- **Metrics calculation**: 3 Bash operations using bc
- **Decision tracking**: 3 Bash operations for recommendations
- **Ratio**: 20 tool calls to ~100 documentation lines = 20% (HEALTHY)

---

**CRITICAL**: This command provides comprehensive documentation health assessment and must maintain focus on actionable insights rather than exhaustive reporting. Audit findings should directly enable targeted remediation workflows.

**EXECUTION COMMITMENT**: Comprehensive documentation audit with structure mapping, duplication detection, reference validation, and health scoring are NOW implemented with actual tool calls.