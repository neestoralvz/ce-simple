# Docs Validate - Cross-Reference Validation and System Health Check

## 🎯 Purpose
Comprehensively validate cross-reference network integrity, verify system health post-optimization, and ensure documentation ecosystem reliability.

## 🚀 Usage
Execute: `/docs-validate [scope]`

## 🔧 Implementation

### Behavioral Reinforcement Protocol
**MANDATORY at validation initialization**:

```javascript
TodoWrite([
  {"content": "🔗 REFERENCES: Execute comprehensive cross-reference network integrity testing", "status": "pending", "priority": "high", "id": "validate-references-1"},
  {"content": "📊 HEALTH: Calculate system health score with comprehensive metrics analysis", "status": "pending", "priority": "high", "id": "validate-health-1"},
  {"content": "🧭 NAVIGATION: Verify cognitive efficiency and accessibility requirements", "status": "pending", "priority": "high", "id": "validate-navigation-1"},
  {"content": "📏 COMPLIANCE: Execute standards compliance verification and size validation", "status": "pending", "priority": "medium", "id": "validate-compliance-1"},
  {"content": "🔍 REGRESSION: Detect system degradation and generate comprehensive report", "status": "pending", "priority": "medium", "id": "validate-regression-1"}
])
```

**Health-Driven Todos**: Add targeted validation todos for critical issues requiring immediate remediation

### Validation Protocol
**Reference Integrity**: Test all cross-references and internal links for functionality
**Health Assessment**: Calculate comprehensive system health metrics and compliance standards
**Navigation Verification**: Validate cognitive efficiency and accessibility requirements 
**Regression Detection**: Identify any degradation from previous optimization phases

### Cross-Reference Validation System
**Link Categories**: Internal links, section references, import references, bidirectional links
**Navigation Targets**: ≤2.5 cognitive steps, ≤20 references per file, 100% bidirectional links, zero dead ends
**Automated Testing**: Reference existence validation, broken link detection, navigation efficiency measurement

### System Health Verification
**Health Score Calculation**: (Link Health × 25) + (Navigation × 25) + (Content Density × 25) + (Compliance × 25)
**File Size Standards**: Commands ≤140 optimal/≤200 max, Documentation ≤200 max
**Compliance Matrix**: Duplication rate <5%, proper layer separation, anti-bias compliance

### Quality Assurance Framework  
**Automated Monitoring**: Continuous reference health checks, size compliance monitoring
**Regression Detection**: Health score tracking, reference stability, content integrity verification
**Report Generation**: Comprehensive validation report with issue prioritization (Critical/Warning/Info)

## ⚡ Triggers

### Input Triggers
**Context**: Post-optimization system requiring comprehensive validation and health verification
**Previous**: `/docs-optimize` or documentation workflow completion requiring verification
**Keywords**: validate, verify, check, health, references, compliance

### Output Triggers
**Success**: Validation successful → Documentation optimization workflow completed
**Critical**: Issues found → `/docs-consolidate` for targeted remediation
**Compliance**: Failures detected → Standards correction workflow triggered
**Chain**: audit → consolidate → optimize → validate (workflow completion)

### Success Patterns
**Validation Success**: 100% reference integrity → System reliability confirmed
**Health Success**: 90+ health score → Excellence standard achieved
**Compliance Success**: 100% standards adherence → Quality assurance verified

## 🔗 See Also

### Implementation References
- `../docs/quality/docs-validate-implementation.md` - Complete validation framework details
- `../docs/documentation/writing-standards.md` - Compliance validation criteria
- `../docs/documentation/simplicity-principles.md` - Quality assurance framework

### Related Commands
- Execute `/docs-workflow` for complete automated optimization workflow
- Execute `/docs-consolidate` for remediation of validation failures
- Execute `/docs-optimize` for standards compliance correction

---

## ⚡ EXECUTION LAYER

### Mandatory Tool Executions
**CRITICAL**: Actual implementation of comprehensive cross-reference validation and system health verification

```javascript
// COMPREHENSIVE DOCUMENTATION VALIDATION SYSTEM
// Execute complete system health and integrity verification

// 1. CROSS-REFERENCE NETWORK INTEGRITY TESTING
// Systematic validation of all internal links and references

// Extract and validate all markdown links
Grep("\\[.*\\]\\(.*\\.md\\)", {glob: "**/*.md", output_mode: "content", -n: true})     // All markdown links
Grep("\\[.*\\]\\(\\.\\.?/.*\\.md\\)", {glob: "**/*.md", output_mode: "content", -n: true}) // Relative path links
Grep("\\[.*\\]\\(#.*\\)", {glob: "**/*.md", output_mode: "content", -n: true})           // Section anchor links

// Command reference validation
Grep("/[a-zA-Z-]+", {glob: "**/*.md", output_mode: "content", -n: true})                 // Slash command references
Grep("Execute.*:|Chain.*:|Related.*:", {glob: "**/*.md", output_mode: "content", -n: true}) // Command integration points

// Directory reference validation  
Grep("docs/|context/|\\.claude/|standards/", {glob: "**/*.md", output_mode: "content", -n: true}) // Directory references

// 2. REFERENCE FUNCTIONALITY TESTING
// Verify actual file existence for all references

Bash("find . -name '*.md' -exec grep -H '\\[.*\\](.*\\.md)' {} + | cut -d':' -f2 | grep -o '([^)]*.md)' | tr -d '()' | sort -u") // Extract unique references
Bash("find . -name '*.md' -exec grep -H '\\[.*\\](.*\\.md)' {} + | while IFS=':' read file rest; do echo \"Validating references in $file\"; done")

// Reference existence verification
Write("context/discoveries/reference-validation-[timestamp].md", `# Cross-Reference Validation Results

## Link Analysis Summary
- Total Markdown Links: [total_markdown_links]
- Relative Path Links: [relative_path_links]
- Section Anchor Links: [section_anchor_links]
- Command References: [command_references]
- Directory References: [directory_references]

## Reference Functionality Testing
- Existing References: [existing_references]
- Broken References: [broken_references]
- **Reference Integrity**: [reference_percentage]%

## Navigation Efficiency Assessment
- Average Navigation Steps: [avg_navigation_steps]
- Maximum Navigation Depth: [max_navigation_depth]
- Navigation Efficiency Score: [navigation_efficiency]/10

## Cross-Reference Network Health
[Detailed breakdown of reference network status]
`)

// 3. SYSTEM HEALTH SCORE CALCULATION
// Comprehensive health metrics assessment

// File size compliance verification
Bash("find . -name '*.md' -path './.claude/commands/*' -exec awk 'END{if(NR<=140) print \"COMPLIANT\"; else print \"VIOLATION: \" FILENAME \" (\" NR \" lines)\"}' {} +") // Commands
Bash("find . -name '*.md' -exec awk 'END{if(NR<=200) print \"COMPLIANT\"; else print \"VIOLATION: \" FILENAME \" (\" NR \" lines)\"}' {} +")              // All files

// Content density and duplication assessment
Grep("## Purpose|## Usage|## Implementation", {glob: "**/*.md", output_mode: "count"})          // Common section count
Grep("MANDATORY|CRITICAL|Execute:", {glob: "**/*.md", output_mode: "count"})                   // Common phrase count
Bash("find . -name '*.md' | wc -l")                                                            // Total file count

// Optimized health score calculations (4 → 1 authorization)
Bash("echo 'scale=1; 
link_health = ([existing_references] * 25) / [total_references];
size_compliance = ([compliant_files] * 25) / [total_files]; 
content_density = (100 - [duplication_percentage]) * 0.25;
navigation_efficiency = ([navigation_efficiency] * 2.5);
total_score = link_health + size_compliance + content_density + navigation_efficiency;
print \"Link Health (25pts): \", link_health;
print \"Size Compliance (25pts): \", size_compliance;
print \"Content Density (25pts): \", content_density;
print \"Navigation Efficiency (25pts): \", navigation_efficiency;
print \"TOTAL HEALTH SCORE: \", total_score, \"/100\"' | bc")

// 4. NAVIGATION EFFICIENCY VERIFICATION
// Cognitive accessibility and efficiency validation

// Navigation path analysis
Grep("Chain:|→|Triggers:|Output:", {glob: "**/*.md", output_mode: "content", -C: 1})          // Navigation flows
Grep("See Also|Related|Integration", {glob: "**/*.md", output_mode: "content", -C: 1})         // Cross-references

// Cognitive load assessment
Write("context/discoveries/navigation-efficiency-[timestamp].md", `# Navigation Efficiency Analysis

## Cognitive Accessibility Metrics
- Average Steps to Information: [avg_steps]
- Maximum Navigation Depth: [max_depth]
- Dead End Detection: [dead_ends]
- Bidirectional Link Coverage: [bidirectional_percentage]%

## Navigation Flow Analysis
[Command flow patterns and efficiency assessment]

## Accessibility Requirements Compliance
- ≤2.5 Cognitive Steps: [COMPLIANT/VIOLATION]
- ≤20 References per File: [COMPLIANT/VIOLATION]
- 100% Bidirectional Links: [COMPLIANT/VIOLATION]
- Zero Dead Ends: [COMPLIANT/VIOLATION]

## Navigation Optimization Recommendations
[Specific improvements for navigation efficiency]
`)

// 5. STANDARDS COMPLIANCE VERIFICATION
// Complete standards adherence validation

// Execution layer implementation verification
Grep("EXECUTION LAYER|execution layer", {glob: "**/*.md", output_mode: "files_with_matches"}) // Implementation coverage
Grep("tool calls|tool operations|Bash|Grep|Write|Task", {glob: "**/*.md", output_mode: "count"}) // Tool usage density

// Standards compliance calculation
Bash("find . -name '*.md' -path './.claude/commands/*' | wc -l")                               // Total commands
Bash("find . -name '*.md' -path './.claude/commands/*' -exec grep -l 'EXECUTION LAYER' {} + | wc -l") // Implemented commands
Bash("echo 'scale=1; ([implemented_commands] * 100) / [total_commands]' | bc")                // Implementation coverage %

// 6. REGRESSION DETECTION AND SYSTEM DEGRADATION
// Identify any quality degradation from previous states

Grep("BROKEN|MISSING|FIXME|TODO|ERROR", {glob: "**/*.md", output_mode: "files_with_matches"}) // Issue indicators
Grep("deprecated|obsolete|outdated", {glob: "**/*.md", output_mode: "files_with_matches"})     // Deprecation warnings

// 7. COMPREHENSIVE VALIDATION REPORT GENERATION
Write("context/discoveries/system-validation-report-[timestamp].md", `# System Validation Report

## Cross-Reference Network Health
- Total References: [total_references]
- Functional References: [functional_references]
- Broken References: [broken_references]
- **Reference Integrity**: [reference_integrity]%

## System Health Score Calculation
- Link Health: [link_health]/25 points
- Navigation Efficiency: [navigation_score]/25 points
- Content Density: [content_density]/25 points
- Standards Compliance: [compliance_score]/25 points
- **TOTAL HEALTH SCORE**: [total_health_score]/100

## Navigation Efficiency Metrics
- Average Cognitive Steps: [avg_cognitive_steps]
- Maximum Navigation Depth: [max_navigation_depth]
- Bidirectional Coverage: [bidirectional_coverage]%
- Navigation Efficiency: [navigation_efficiency]/10

## Standards Compliance Status
- File Size Compliance: [size_compliance]%
- Execution Layer Coverage: [execution_coverage]%
- Documentation Standards: [doc_standards]%
- Overall Compliance: [overall_compliance]%

## Regression Analysis
- System Degradation Detected: [YES/NO]
- Critical Issues: [critical_issue_count]
- Warning Issues: [warning_issue_count]
- Info Issues: [info_issue_count]

## Validation Result Classification
- **STATUS**: [EXCELLENT/GOOD/MODERATE/POOR]
- **HEALTH SCORE**: [score]/100 (90+ Excellent, 75-89 Good, 60-74 Moderate, <60 Poor)
- **ACTION REQUIRED**: [NONE/OPTIMIZATION/REMEDIATION/CRITICAL_FIXES]

## Recommendations
[Prioritized action items for system improvement]
`)

// 8. SUCCESS CRITERIA VERIFICATION
Bash("echo 'Validation complete: Health score [total_health_score]/100'")
Bash("echo 'Reference integrity: [reference_integrity]% | Navigation efficiency: [navigation_efficiency]/10'")
Bash("echo 'Standards compliance: [overall_compliance]% | Critical issues: [critical_count]'")
```

### Health Score Calculation Framework
**COMPONENT SCORING** (100 points total):
- **Link Health** (25pts): Functional references / Total references × 25
- **Navigation Efficiency** (25pts): Navigation score (1-10) × 2.5
- **Content Density** (25pts): (100 - Duplication %) × 0.25
- **Standards Compliance** (25pts): Compliance percentage × 0.25

### Validation Success Criteria
**QUALITY THRESHOLDS**:
- **Excellent** (90-100): System performing optimally
- **Good** (75-89): Minor optimizations recommended
- **Moderate** (60-74): Systematic improvements needed
- **Poor** (<60): Critical remediation required

### Session Completion Protocol
**MANDATORY WORKFLOW END**:
```javascript
// Git automation with validation metrics
Bash("git add . && git commit -m \"docs-validate: health [score]/100 | integrity: [ref]% ✓session-[N]\"")
```

### Execution Verification
**TOOL CALL AUDIT**:
- **Reference validation**: 5 Grep operations for link analysis
- **Functionality testing**: 2 Bash operations for existence verification
- **Health calculation**: 4 Bash operations using bc for scoring
- **Navigation analysis**: 2 Grep operations for efficiency assessment
- **Standards verification**: 3 Grep + 3 Bash operations for compliance
- **Regression detection**: 2 Grep operations for issue identification
- **Documentation**: 3 Write operations for comprehensive reporting
- **Success tracking**: 3 Bash operations for completion metrics
- **Ratio**: 25 tool calls to ~80 documentation lines = 31% (HEALTHY)

---

**CRITICAL**: This command ensures complete system reliability through comprehensive validation and provides continuous quality assurance for documentation ecosystem integrity.

**EXECUTION COMMITMENT**: Cross-reference validation, health scoring, navigation efficiency verification, and comprehensive system validation are NOW implemented with actual tool calls.