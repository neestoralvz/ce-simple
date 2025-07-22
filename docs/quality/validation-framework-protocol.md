# Validation Framework Protocol

## Health Scoring Standards

### Universal Health Score Calculation
**Base Formula**: 100-point scale across 5 core dimensions
- **Structural Integrity**: 25 points (file organization, size compliance)
- **Content Quality**: 25 points (density, clarity, accuracy)
- **Reference Health**: 20 points (functional links, navigation efficiency)
- **Standards Compliance**: 15 points (format consistency, naming conventions)
- **Integration Quality**: 15 points (cross-command compatibility, workflow efficiency)

### Quality Thresholds
- **≥90 points**: Excellent - Optimal system health
- **75-89 points**: Good - Minor optimization opportunities
- **60-74 points**: Moderate - Attention required
- **<60 points**: Poor - Systematic remediation needed
- **<85 points**: Below threshold - Triggers automatic optimization

## Issue Classification Matrix

### Severity Levels
**CRITICAL** (Immediate action required):
- File size violations >200 lines
- Broken references >10% of total
- Content duplication >40% overlap
- Core functionality failures

**WARNING** (Review recommended):
- Files approaching size limits (180-200 lines)
- Broken references 5-10% of total
- Moderate duplication (20-40% overlap)
- Standards compliance gaps

**INFO** (Optimization opportunities):
- Files approaching optimization targets (140+ lines)
- Minor reference issues <5%
- Low-impact duplication <20%
- Performance improvement potential

## Validation Protocols

### Automated Validation Commands
```bash
# File size compliance check
find . -name "*.md" -exec wc -l {} \; | awk '$1 > [limit]' | sort -nr

# Reference integrity validation
grep -r "\.md" --include="*.md" . | grep -v "archive" | wc -l

# Content duplication detection
grep -r "[pattern]" --include="*.md" . | sort | uniq -c | sort -nr
```

### Quality Gate Standards
**Pre-execution Gates**:
- [ ] File structure validated
- [ ] Reference network functional
- [ ] Size compliance verified
- [ ] Content standards met

**Post-execution Gates**:
- [ ] Health score ≥85%
- [ ] Critical issues resolved
- [ ] Warning issues addressed
- [ ] Integration compatibility confirmed

## Error Handling Framework

### Failure Detection Patterns
```
⚠️ THRESHOLD: Health score [X]% below 85% minimum
🔍 ANALYSIS: [N] critical, [N] warning, [N] info issues detected
📊 METRICS: [Failed dimension]: [Score]/[Max] ([Gap] points below standard)
🎯 FOCUS: [Primary area] requires immediate attention
```

### Recovery Protocols
```
🔄 CORRECTION: Deploying targeted optimization → Focus: [specific issues]
⚡ RETRY: [Correction type] applied → Re-validation triggered
📈 PROGRESS: [Previous]% → [Current]% ([+/-X] point change)
✅ SUCCESS: Threshold achieved → System health restored
```

### Recursive Optimization Logic
1. **Validate**: Execute comprehensive health assessment
2. **Evaluate**: Compare score against 85% threshold
3. **Decide**: SUCCESS (≥85%) → Complete | RETRY (<85% + attempts<3) → Optimize | ESCALATE (attempts≥3) → Manual
4. **Execute**: Apply targeted corrections with error context
5. **Re-validate**: Measure improvement and iterate

## Success Metrics

### Quantitative Targets
- **File Size Compliance**: ≥90% files within optimal limits
- **Reference Accuracy**: ≥95% functional links
- **Content Efficiency**: ≤20% duplication across system
- **Navigation Speed**: ≤2.5 cognitive steps to information
- **Integration Quality**: 100% cross-command compatibility

### Qualitative Indicators
- Clear information hierarchy and logical organization
- Consistent formatting and presentation standards
- Efficient cognitive load distribution
- Seamless workflow transitions between commands
- User confidence in system reliability and completeness