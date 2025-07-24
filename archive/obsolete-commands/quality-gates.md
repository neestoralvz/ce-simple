# Quality Gates - Command and Documentation Standards

## Purpose
Automated quality gate system enforcing length limits, complexity scoring, and development standards. Prevents deployment of non-compliant components through systematic validation.

## Principles and Guidelines
- **Length Enforcement**: Strict 150-line limit for commands, 200-line limit for documentation
- **Complexity Scoring**: Objective complexity assessment with blocking thresholds
- **Automated Validation**: Pre-deployment gates preventing quality violations
- **Progressive Feedback**: Clear guidance for achieving compliance

## Execution Process

### Phase 1: Length Validation and Enforcement
Execute strict length compliance checking:

```bash
echo "=== Length Compliance Validation ==="
echo "Checking file: $FILE_PATH"

# Count lines excluding empty lines and comments
CONTENT_LINES=$(grep -v '^#' "$FILE_PATH" | grep -v '^$' | wc -l)
TOTAL_LINES=$(wc -l < "$FILE_PATH")

# Determine file type and limits
if [[ "$FILE_PATH" == *"/commands/"* ]]; then
    LIMIT=150
    TYPE="command"
elif [[ "$FILE_PATH" == *"/docs/"* ]]; then
    LIMIT=200
    TYPE="documentation"
else
    LIMIT=150
    TYPE="general"
fi

echo "File Type: $TYPE"
echo "Content Lines: $CONTENT_LINES"
echo "Total Lines: $TOTAL_LINES"
echo "Limit: $LIMIT lines"

# Length compliance check
if [ $TOTAL_LINES -gt $LIMIT ]; then
    echo "❌ LENGTH VIOLATION: $TOTAL_LINES lines exceeds $LIMIT limit"
    echo "REQUIRED ACTION: Reduce by $((TOTAL_LINES - LIMIT)) lines"
    echo "BLOCKING: Cannot proceed until compliant"
    exit 1
else
    echo "✅ LENGTH COMPLIANT: $TOTAL_LINES/$LIMIT lines"
fi
```

### Phase 2: Complexity Scoring and Assessment
Calculate objective complexity metrics:

```bash
echo "=== Complexity Assessment ==="

# Count complexity indicators
SECTIONS=$(grep -c '^#' "$FILE_PATH")
SUBSECTIONS=$(grep -c '^##' "$FILE_PATH")
CODE_BLOCKS=$(grep -c '```' "$FILE_PATH" | awk '{print $1/2}')
TODOWRITE_CALLS=$(grep -c 'TodoWrite' "$FILE_PATH")
TOOL_CALLS=$(grep -c -E '(Read|Write|Edit|Bash|Grep|LS|Task)' "$FILE_PATH")
PHASES=$(grep -c 'Phase [0-9]' "$FILE_PATH")

echo "Sections: $SECTIONS"
echo "Subsections: $SUBSECTIONS"
echo "Code Blocks: $CODE_BLOCKS"
echo "TodoWrite Calls: $TODOWRITE_CALLS"
echo "Tool Calls: $TOOL_CALLS"
echo "Phases: $PHASES"

# Calculate complexity score
COMPLEXITY_SCORE=0
COMPLEXITY_SCORE=$((COMPLEXITY_SCORE + SECTIONS * 2))
COMPLEXITY_SCORE=$((COMPLEXITY_SCORE + SUBSECTIONS * 1))
COMPLEXITY_SCORE=$((COMPLEXITY_SCORE + CODE_BLOCKS * 3))
COMPLEXITY_SCORE=$((COMPLEXITY_SCORE + TODOWRITE_CALLS * 5))
COMPLEXITY_SCORE=$((COMPLEXITY_SCORE + TOOL_CALLS * 2))
COMPLEXITY_SCORE=$((COMPLEXITY_SCORE + PHASES * 4))

echo "Raw Complexity Score: $COMPLEXITY_SCORE"

# Normalize by content length
NORMALIZED_COMPLEXITY=$((COMPLEXITY_SCORE * 100 / CONTENT_LINES))
echo "Normalized Complexity: $NORMALIZED_COMPLEXITY (per 100 lines)"

# Complexity thresholds
if [ $TYPE = "command" ]; then
    COMPLEXITY_LIMIT=60
elif [ $TYPE = "documentation" ]; then
    COMPLEXITY_LIMIT=40
else
    COMPLEXITY_LIMIT=50
fi

echo "Complexity Limit: $COMPLEXITY_LIMIT"

# Complexity compliance check
if [ $NORMALIZED_COMPLEXITY -gt $COMPLEXITY_LIMIT ]; then
    echo "❌ COMPLEXITY VIOLATION: $NORMALIZED_COMPLEXITY exceeds $COMPLEXITY_LIMIT limit"
    echo "REQUIRED ACTION: Simplify structure or reduce orchestration"
    echo "BLOCKING: Cannot proceed until simplified"
    exit 1
else
    echo "✅ COMPLEXITY COMPLIANT: $NORMALIZED_COMPLEXITY/$COMPLEXITY_LIMIT"
fi
```

### Phase 3: Content Quality Assessment
Evaluate content quality indicators:

```bash
echo "=== Content Quality Assessment ==="

# Marketing language detection
MARKETING_TERMS=("intelligent" "comprehensive" "advanced" "sophisticated" "cutting-edge" "revolutionary" "innovative")
MARKETING_COUNT=0

for term in "${MARKETING_TERMS[@]}"; do
    COUNT=$(grep -i -c "$term" "$FILE_PATH")
    MARKETING_COUNT=$((MARKETING_COUNT + COUNT))
    if [ $COUNT -gt 0 ]; then
        echo "Marketing term '$term' found $COUNT times"
    fi
done

echo "Total Marketing Terms: $MARKETING_COUNT"

# Technical precision indicators
VAGUE_TERMS=("various" "multiple" "several" "many" "some" "etc")
VAGUE_COUNT=0

for term in "${VAGUE_TERMS[@]}"; do
    COUNT=$(grep -i -c "$term" "$FILE_PATH")
    VAGUE_COUNT=$((VAGUE_COUNT + COUNT))
done

echo "Vague Language Count: $VAGUE_COUNT"

# Information density calculation
WORDS=$(wc -w < "$FILE_PATH")
DENSITY=$((WORDS / TOTAL_LINES))
echo "Information Density: $DENSITY words per line"

# Quality compliance checks
QUALITY_VIOLATIONS=0

if [ $MARKETING_COUNT -gt 0 ]; then
    echo "❌ SOBRIETY VIOLATION: $MARKETING_COUNT marketing terms detected"
    QUALITY_VIOLATIONS=$((QUALITY_VIOLATIONS + 1))
fi

if [ $VAGUE_COUNT -gt 3 ]; then
    echo "❌ PRECISION VIOLATION: $VAGUE_COUNT vague terms (>3 limit)"
    QUALITY_VIOLATIONS=$((QUALITY_VIOLATIONS + 1))
fi

if [ $DENSITY -lt 8 ]; then
    echo "❌ CONCISENESS VIOLATION: $DENSITY words/line (<8 minimum)"
    QUALITY_VIOLATIONS=$((QUALITY_VIOLATIONS + 1))
fi

if [ $QUALITY_VIOLATIONS -eq 0 ]; then
    echo "✅ CONTENT QUALITY COMPLIANT"
else
    echo "❌ QUALITY VIOLATIONS: $QUALITY_VIOLATIONS issues detected"
    echo "BLOCKING: Cannot proceed until quality issues resolved"
    exit 1
fi
```

### Phase 4: PTS Framework Integration
Integrate with PTS validation for complete assessment:

```bash
echo "=== PTS Framework Validation ==="

# Quick PTS assessment
echo "Executing PTS pre-validation..."

# Call PTS validation if available
if command -v validate-pts >/dev/null 2>&1; then
    validate-pts "$FILE_PATH" --quick
    PTS_RESULT=$?
    
    if [ $PTS_RESULT -eq 0 ]; then
        echo "✅ PTS VALIDATION PASSED"
    else
        echo "❌ PTS VALIDATION FAILED"
        echo "BLOCKING: PTS compliance required before deployment"
        exit 1
    fi
else
    echo "⚠️ PTS validator not found - manual validation required"
fi
```

## Quality Gate Thresholds

### Length Limits (BLOCKING)
- **Commands**: 150 lines maximum (strict enforcement)
- **Documentation**: 200 lines maximum (optimize for token efficiency)
- **Templates**: 100 lines maximum (brevity for reuse)
- **Configuration**: 50 lines maximum (simplicity focus)

### Complexity Limits (BLOCKING)
- **Commands**: Normalized complexity ≤60 (moderate structure allowed)
- **Documentation**: Normalized complexity ≤40 (emphasis on clarity)
- **Templates**: Normalized complexity ≤30 (simple patterns only)

### Content Quality Standards (BLOCKING)
- **Marketing Language**: 0 terms allowed (sobriety principle)
- **Vague Language**: ≤3 terms allowed (precision requirement)
- **Information Density**: ≥8 words/line (conciseness standard)
- **Technical Accuracy**: 100% requirement (no ambiguous instructions)

## Scoring Matrix

### Overall Quality Score Calculation
```bash
# Component scoring weights
LENGTH_WEIGHT=30      # 30% of total score
COMPLEXITY_WEIGHT=25  # 25% of total score  
CONTENT_WEIGHT=25     # 25% of total score
PTS_WEIGHT=20         # 20% of total score

# Calculate component scores (0-100 scale)
LENGTH_SCORE=$((100 - (TOTAL_LINES - LIMIT) * 100 / LIMIT))
COMPLEXITY_SCORE=$((100 - (NORMALIZED_COMPLEXITY - COMPLEXITY_LIMIT) * 100 / COMPLEXITY_LIMIT))
CONTENT_SCORE=$((100 - QUALITY_VIOLATIONS * 25))  # 25 point deduction per violation
PTS_SCORE=85  # Placeholder - from actual PTS validation

# Weighted overall score
OVERALL_SCORE=$(((LENGTH_SCORE * LENGTH_WEIGHT + COMPLEXITY_SCORE * COMPLEXITY_WEIGHT + CONTENT_SCORE * CONTENT_WEIGHT + PTS_SCORE * PTS_WEIGHT) / 100))

echo "=== Quality Score Summary ==="
echo "Length Score: $LENGTH_SCORE/100 (Weight: $LENGTH_WEIGHT%)"
echo "Complexity Score: $COMPLEXITY_SCORE/100 (Weight: $COMPLEXITY_WEIGHT%)"
echo "Content Score: $CONTENT_SCORE/100 (Weight: $CONTENT_WEIGHT%)"
echo "PTS Score: $PTS_SCORE/100 (Weight: $PTS_WEIGHT%)"
echo "Overall Score: $OVERALL_SCORE/100"
```

### Deployment Thresholds
- **Production Ready**: ≥90 overall score (all components excellent)
- **Development Ready**: ≥80 overall score (minor improvements needed)
- **Requires Improvement**: ≥70 overall score (significant work needed)
- **Major Rework**: <70 overall score (fundamental issues)

## Integration Examples

### Pre-Commit Validation
```bash
#!/bin/bash
# .git/hooks/pre-commit
echo "Running quality gates validation..."

# Check all staged files
for file in $(git diff --cached --name-only --diff-filter=ACM); do
    if [[ "$file" =~ \.(md)$ ]]; then
        echo "Validating: $file"
        quality-gates "$file"
        if [ $? -ne 0 ]; then
            echo "Quality gate failed for $file"
            exit 1
        fi
    fi
done

echo "All quality gates passed ✅"
```

### CI/CD Integration
```yaml
# GitHub Actions example
quality_gates:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v3
    - name: Run Quality Gates
      run: |
        find . -name "*.md" -exec quality-gates {} \;
    - name: Generate Quality Report
      run: |
        quality-gates --batch --report > quality-report.md
```

### Development Workflow
```bash
# Before command development
quality-gates --check-limits --file="new-command.md"

# During development  
quality-gates --live-monitor --file="new-command.md"

# Before deployment
quality-gates --full-validation --file="new-command.md"
```

## Error Recovery Guidance

### Length Violations
```bash
ERROR: Length limit exceeded
CURRENT: 165 lines
LIMIT: 150 lines
REDUCTION_NEEDED: 15 lines

STRATEGIES:
1. Remove redundant explanations
2. Consolidate similar phases
3. Eliminate marketing language
4. Use more concise tool calls
5. Reference external docs instead of inline content
```

### Complexity Violations
```bash
ERROR: Complexity limit exceeded
CURRENT: 75 normalized complexity
LIMIT: 60 normalized complexity

STRATEGIES:
1. Reduce TodoWrite calls (5 points each)
2. Combine similar phases (4 points each)
3. Simplify tool orchestration (2 points per call)
4. Reduce nested sections (1-2 points each)
```

### Content Quality Issues
```bash
ERROR: Marketing language detected
TERMS: "comprehensive", "intelligent", "advanced"
REPLACEMENTS:
- "comprehensive" → "complete" or specific description
- "intelligent" → "automated" or specific capability
- "advanced" → specific feature description
```

---

**Single Responsibility**: Automated quality gate enforcement providing length limits, complexity scoring, content validation, and deployment readiness assessment for maintaining system standards.