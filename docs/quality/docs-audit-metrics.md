# Docs Audit Metrics and Validation Protocols

## Issue Categorization Matrix

### CRITICAL Issues (Immediate attention required)
- Duplicate content >40% overlap between files
- Broken references >10% of total links
- File size violations >200 lines
- Authority conflicts (multiple files claiming same domain)

### WARNING Issues (Review recommended)
- Moderate duplication 20-40% overlap
- Broken references 5-10% of total links
- File size approaching limits 180-200 lines
- Cross-reference gaps in navigation chain

### INFO Issues (Optimization opportunities)
- Minor duplication <20% overlap
- Isolated broken references <5%
- Suboptimal file organization
- Navigation efficiency improvements available

## Health Metrics Calculation

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

## Automated Validation Protocols

**Quick Health Check Commands**:
```bash
# File size validation
find . -name "*.md" -exec wc -l {} \; | awk '$1 > 200'

# Cross-reference validation
grep -r "\.md" --include="*.md" . | grep -v "archive"

# Duplication detection pattern
grep -r "CRITICAL|MANDATORY|REQUIRED" --include="*.md" .
```

## Git Integration Protocol

**Audit Tracking**: Uses standardized git integration templates for baseline establishment and health monitoring

**Reference**: See `../../docs/workflow/git-integration.md` for audit-specific commit templates