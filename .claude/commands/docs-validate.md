# Docs Validate - Cross-Reference Validation and System Health Check

## 🎯 Purpose
Comprehensively validate cross-reference network integrity, verify system health post-optimization, and ensure documentation ecosystem reliability.

## 🚀 Usage
Execute: `/docs-validate [scope]`

## 🔧 Implementation

### Validation Protocol
1. **REFERENCE INTEGRITY**: Test all cross-references and internal links for functionality
2. **HEALTH ASSESSMENT**: Calculate comprehensive system health metrics and compliance
3. **NAVIGATION VERIFICATION**: Validate cognitive efficiency and accessibility requirements
4. **COMPLIANCE CONFIRMATION**: Verify adherence to all established standards and policies
5. **REGRESSION DETECTION**: Identify any degradation from previous optimization phases

### Cross-Reference Validation Framework

#### Link Integrity Testing
**Comprehensive Reference Analysis**:
```bash
# Extract all internal references
grep -r "\.md\b" --include="*.md" . | grep -v "archive"

# Validate file existence
find . -name "*.md" -exec basename {} \; | sort | uniq

# Check for broken reference patterns
grep -r "@[a-zA-Z]" --include="*.md" . | grep -v "archive"
```

**Reference Categories**:
- **Internal Links**: File-to-file references within system
- **Section References**: Specific section linking within documents
- **Import References**: @path/to/import style references
- **Bidirectional Links**: Reverse navigation capabilities

#### Navigation Efficiency Assessment

**Cognitive Load Measurement**:
- **Path Analysis**: Calculate steps required to reach any information
- **Hub Efficiency**: Evaluate strategic navigation point effectiveness
- **Dead End Detection**: Identify files lacking outbound references
- **Circular Reference**: Detect and resolve navigation loops

**Target Validation**:
- **≤2.5 Cognitive Steps**: Maximum path length to any essential information
- **≤20 References**: Optimal cross-reference density per file
- **100% Bidirectional**: Complete reverse navigation capabilities
- **Zero Dead Ends**: All files connected to navigation network

### System Health Verification

#### Comprehensive Health Scoring
**Health Metrics Calculation**:
```
Health Score = (Link Health × 25) + (Navigation Efficiency × 25) + 
               (Content Density × 25) + (Standards Compliance × 25)
```

**Component Assessments**:
- **Link Health**: Functional references / Total references × 25
- **Navigation Efficiency**: (3.0 - Average cognitive steps) × 10
- **Content Density**: Value per cognitive unit assessment × 25
- **Standards Compliance**: Compliant files / Total files × 25

#### Compliance Verification Matrix

**File Size Standards**:
- **Commands**: ≤140 lines optimal, ≤200 maximum
- **Documentation**: ≤200 lines maximum
- **Violation Detection**: Automated identification and reporting
- **Trend Analysis**: Size evolution tracking and early warning

**Content Quality Standards**:
- **Duplication Rate**: <5% content overlap target
- **Reference Density**: Optimal linking without redundancy
- **Information Architecture**: Proper layer separation (commands/standards/context)
- **Anti-Bias Compliance**: Neutral content and discovery-based logic

### Regression Detection System

#### Change Impact Analysis
**Pre/Post Comparison**:
- **Health Score Tracking**: Monitor improvements and degradations
- **Reference Stability**: Detect broken links introduced during optimization
- **Content Integrity**: Verify no information loss during consolidation
- **Performance Impact**: Assess navigation and accessibility changes

**Regression Alerts**:
- **Health Score Decline**: >5 point reduction triggers investigation
- **Broken References**: Any new non-functional links flagged immediately
- **Size Violations**: New compliance violations identified and reported
- **Navigation Degradation**: Increased cognitive steps detected and analyzed

### Automated Validation Tools

#### Continuous Monitoring Scripts
**Reference Health Check**:
```bash
#!/bin/bash
# Automated reference validation
for file in $(find . -name "*.md" -not -path "./archive/*"); do
    echo "Validating: $file"
    grep -o '[a-zA-Z0-9_-]*\.md' "$file" | while read ref; do
        if [ ! -f "$ref" ] && [ ! -f "./$ref" ]; then
            echo "BROKEN: $file -> $ref"
        fi
    done
done
```

**Size Compliance Monitor**:
```bash
#!/bin/bash
# File size compliance checking
echo "Commands exceeding 140 lines (optimal):"
find .claude/commands -name "*.md" -exec wc -l {} \; | awk '$1 > 140 {print $2 ": " $1 " lines"}'

echo "Files exceeding 200 lines (maximum):"
find . -name "*.md" -not -path "./archive/*" -exec wc -l {} \; | awk '$1 > 200 {print $2 ": " $1 " lines"}'
```

### Quality Assurance Reporting

#### Validation Report Generation
**Comprehensive Assessment Output**:
```
📊 VALIDATION REPORT
Reference Health: [X]% functional links ([Y] broken, [Z] total)
Navigation Efficiency: [X] cognitive steps average (target: ≤2.5)
Standards Compliance: [X]% files compliant ([Y] violations detected)
System Health Score: [X]/100 (trend: [improvement/decline])

CRITICAL ISSUES: [X] items requiring immediate attention
WARNING ISSUES: [X] items for review and optimization
SUCCESS METRICS: [X] validation targets achieved
```

**Issue Prioritization**:
- **CRITICAL**: Broken references, major compliance violations
- **WARNING**: Size limit approaches, navigation inefficiency
- **INFO**: Optimization opportunities, minor improvements

## ⚡ Triggers

### Input Triggers
**Context**: Post-optimization system requiring comprehensive validation
**Previous**: `/docs-optimize` → standards applied, validation needed
**Keywords**: validate, verify, check, health, references, compliance

### Output Triggers
**When**: Validation successful → Documentation optimization complete
**When**: Complete workflow → `/docs-workflow` for automated full optimization  
**When**: Critical issues found → `/docs-consolidate` for targeted remediation
**When**: Compliance failures → `/docs-optimize` for standards correction
**Chain**: audit → consolidate → optimize → validate (granular) OR audit → workflow (complete)

### Success Patterns
**Validation Success**: 100% reference integrity → System reliability confirmed
**Health Success**: 90+ health score → Excellence standard achieved
**Compliance Success**: 100% standards adherence → Quality assurance verified

## 🔗 See Also

### Related Commands
- Execute `/docs-workflow` for complete automated documentation optimization workflow
- Execute `/docs-audit` for initial system analysis and baseline establishment
- Execute `/docs-consolidate` for remediation of validation failures
- Execute `/docs-optimize` for standards compliance correction

### Integration References
- `context/discoveries/documentation-workflow-discoveries.md` - Validation methodology
- `standards/writing-standards.md` - Compliance validation criteria
- `standards/simplicity-principles.md` - Quality assurance framework
- `context/patterns/command-complexity-management.md` - System integrity patterns

---

**CRITICAL**: This command ensures complete system reliability through comprehensive validation and provides continuous quality assurance for documentation ecosystem integrity.