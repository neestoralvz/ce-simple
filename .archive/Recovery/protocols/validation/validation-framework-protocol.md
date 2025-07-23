# Validation Framework Protocol

## Purpose
Define health scoring and validation standards for system quality assessment.

## Health Score Calculation
100-point scale across 5 dimensions:
- **Structural Integrity**: 25 points (file organization, size compliance)
- **Content Quality**: 25 points (density, clarity, accuracy)
- **Reference Health**: 20 points (functional links, navigation efficiency)
- **Standards Compliance**: 15 points (format consistency, naming conventions)
- **Integration Quality**: 15 points (cross-command compatibility, workflow efficiency)

## Quality Thresholds
- **≥90**: Excellent (optimal system health)
- **75-89**: Good (minor optimization opportunities)
- **60-74**: Moderate (attention required)
- **<60**: Poor (systematic remediation needed)
- **<85**: Below threshold (triggers automatic optimization)

## Issue Classification

### Severity Levels
**CRITICAL** (immediate action):
- File size >200 lines
- Broken references >10%
- Content duplication >40%
- Core functionality failures

**WARNING** (review recommended):
- Files 180-200 lines
- Broken references 5-10%
- Duplication 20-40%
- Standards compliance gaps

**INFO** (optimization opportunities):
- Files >140 lines
- Reference issues <5%
- Duplication <20%
- Performance improvement potential

## Validation Commands
Automated checks:
- **File size**: `find . -name "*.md" -exec wc -l {} \;`
- **References**: `grep -r "\.md" --include="*.md" .`
- **Duplication**: `grep -r "[pattern]" --include="*.md" .`

## Quality Gates

### Pre-execution
- File structure validated
- Reference network functional
- Size compliance verified
- Content standards met

### Post-execution
- Health score ≥85%
- Critical issues resolved
- Warning issues addressed
- Integration compatibility confirmed

## Error Handling

### Detection Pattern
- Health score below 85% threshold
- Critical/warning/info issues count
- Failed dimension identification
- Primary focus area determination

### Recovery Process
- Deploy targeted optimization
- Apply corrections and re-validate
- Track progress and improvement
- Confirm threshold achievement

## Optimization Logic
1. **Validate**: Execute health assessment
2. **Evaluate**: Compare against 85% threshold
3. **Decide**: Success (≥85%) or retry (<85%, attempts<3) or escalate (attempts≥3)
4. **Execute**: Apply targeted corrections
5. **Re-validate**: Measure improvement and iterate

## Success Metrics

### Quantitative Targets
- File size compliance: ≥90% within limits
- Reference accuracy: ≥95% functional links
- Content efficiency: ≤20% duplication
- Navigation speed: ≤2.5 cognitive steps
- Integration quality: 100% compatibility

### Qualitative Indicators
- Clear information hierarchy
- Consistent formatting standards
- Efficient cognitive load distribution
- Seamless workflow transitions
- User confidence in system reliability

---

**IMPLEMENTATION**: Use this framework for systematic quality assessment and optimization.