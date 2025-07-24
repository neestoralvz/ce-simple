# Validate PTS - Systematic Compliance Checker

## Purpose
Systematic validation tool for PTS (Pragmatic Technical Simplicity) compliance checking across commands, documentation, and system components. Implements 12-component framework with blocking criteria enforcement.

## Principles and Guidelines
- **Systematic Validation**: Complete 12-component PTS framework assessment
- **Blocking Enforcement**: Stop development when critical criteria fail
- **Objective Metrics**: Quantifiable compliance scoring where applicable
- **Actionable Feedback**: Specific recommendations for compliance improvement

## Execution Process

### Phase 1: Pre-Validation Assessment
Execute rapid pre-evaluation to determine if full validation is warranted:

```bash
# 2-minute pre-evaluation checklist
echo "=== PTS Pre-Validation Assessment ==="
echo "1. Clear Purpose Test: Can purpose be explained in 30 seconds?"
echo "2. Single Responsibility Test: Does it do exactly one thing?"
echo "3. Simplicity Test: Is this the simplest solution that works?"
echo "4. Zero-Config Test: Works without additional configuration?"
echo ""
echo "If ANY test fails → STOP → Redesign required"
```

### Phase 2: Complete PTS Component Validation
Systematic evaluation of all 12 PTS components:

**Technical Cluster Validation:**
```bash
echo "=== Technical Cluster Assessment ==="
echo "1. DIRECTNESS: Path to objective (≤3 steps required)"
echo "   - Count steps to primary objective"
echo "   - Identify unnecessary detours"
echo "   - Score: Direct=3, Minimal=2, Complex=1, Convoluted=0"

echo "2. PRECISION: Technical accuracy (100% specificity required)"
echo "   - Check for vague language or ambiguous instructions"
echo "   - Validate all technical specifications"
echo "   - Score: Specific=3, Mostly=2, Some=1, Vague=0"

echo "3. SUFFICIENCY: Complete but minimal (100% coverage, 0% bloat)"
echo "   - Verify all use cases covered"
echo "   - Identify unnecessary features"
echo "   - Score: Perfect=3, Minor gaps=2, Missing key=1, Incomplete=0"

echo "4. TECHNICAL EXCELLENCE: Impeccable quality in simple solution"
echo "   - Error handling completeness"
echo "   - Performance optimization"
echo "   - Score: Excellent=3, Good=2, Adequate=1, Poor=0"
```

**Communication Cluster Validation:**
```bash
echo "=== Communication Cluster Assessment ==="
echo "5. EXACTITUDE: Implementation at exact required point"
echo "   - Verify requirements alignment"
echo "   - Check for scope drift"
echo "   - Score: Exact=3, Close=2, Drift=1, Misaligned=0"

echo "6. SOBRIETY: Zero marketing language, pure technical content"
echo "   - Count marketing terms ('intelligent', 'comprehensive', 'advanced')"
echo "   - Verify professional tone maintained"
echo "   - Score: Pure=3, Minimal=2, Some=1, Heavy=0"

echo "7. STRUCTURE: Logical, clear, well-organized (≤3 hierarchy levels)"
echo "   - Check hierarchy depth"
echo "   - Validate navigation clarity"
echo "   - Score: Excellent=3, Good=2, Adequate=1, Confusing=0"

echo "8. CONCISENESS: Maximum value per complexity unit"
echo "   - Calculate information density ratio"
echo "   - Identify redundant content"
echo "   - Score: Dense=3, Efficient=2, Average=1, Verbose=0"
```

**Cognitive Cluster Validation:**
```bash
echo "=== Cognitive Cluster Assessment ==="
echo "9. CLARITY: Immediate comprehension without ambiguity"
echo "   - Test understanding time (≤5 minutes target)"
echo "   - Check for ambiguous language"
echo "   - Score: Immediate=3, Quick=2, Slow=1, Confusing=0"

echo "10. COHERENCE: Absolute internal consistency"
echo "    - Check for contradictions"
echo "    - Validate conceptual alignment"
echo "    - Score: Consistent=3, Minor=2, Some=1, Contradictory=0"

echo "11. EFFECTIVENESS: Produces measurable successful results"
echo "    - Verify success criteria definition"
echo "    - Check measurable outcomes"
echo "    - Score: Measurable=3, Mostly=2, Partial=1, Unclear=0"

echo "12. PRAGMATISM: Works effectively in real conditions"
echo "    - Test real-world applicability"
echo "    - Verify production readiness"
echo "    - Score: Production=3, Stable=2, Limited=1, Theoretical=0"
```

### Phase 3: Compliance Scoring and Blocking Assessment
Calculate overall compliance and identify blocking issues:

```bash
echo "=== Compliance Scoring ==="
echo "Total PTS Score: [Sum of all component scores] / 36 possible"
echo "Percentage: [Score/36 * 100]%"
echo ""
echo "=== Blocking Criteria Assessment ==="
echo "CRITICAL BLOCKING (Stops development immediately):"
echo "- Purpose unclear in <30 seconds"
echo "- Multiple responsibilities detected"
echo "- Unnecessary complexity evident"
echo "- Configuration dependencies required"

echo "QUALITY BLOCKING (Requires correction before proceeding):"
echo "- Technical metrics <90%"
echo "- Information redundancy >20%"
echo "- Non-intuitive navigation"
echo "- Requirements drift >5%"

echo "ARCHITECTURE BLOCKING (System integration issues):"
echo "- No single source of truth"
echo "- Forced integration detected"
echo "- Evolution path blocked"
```

### Phase 4: Actionable Recommendations
Generate specific improvement recommendations:

```bash
echo "=== Improvement Recommendations ==="
echo "For each failing component, provide:"
echo "1. Specific issue description"
echo "2. Root cause analysis"
echo "3. Exact remediation steps"
echo "4. Validation criteria for fix"
echo "5. Prevention strategies"
```

## Compliance Thresholds

### Minimum Passing Scores
- **Perfect Compliance**: 36/36 (100%) - All components excellent
- **Production Ready**: 32/36 (89%) - Minor improvements needed
- **Development Continue**: 28/36 (78%) - Acceptable with fixes
- **Major Rework Required**: <28/36 (78%) - Fundamental issues

### Blocking Criteria (Any failure = STOP)
- **Critical Function**: Purpose, Single Responsibility, Simplicity, Pragmatism
- **Quality Gates**: Technical Excellence, Sobriety, Coherence, Effectiveness
- **Architecture**: Structure, Exactitude, Clarity, Sufficiency

## Tool Integration Examples

### Command Validation
```bash
# Validate existing command
./validate-pts.sh /path/to/command.md

# Expected output:
# PTS Validation Report - command.md
# Technical Cluster: 11/12 (92%)
# Communication Cluster: 10/12 (83%)  
# Cognitive Cluster: 12/12 (100%)
# Overall Score: 33/36 (92%) - PRODUCTION READY
```

### Documentation Validation  
```bash
# Validate documentation file
./validate-pts.sh /path/to/doc.md --type=documentation

# Additional checks for documentation:
# - Reference accuracy
# - Example quality
# - Learning curve assessment
```

### Batch Validation
```bash
# Validate entire system
./validate-pts.sh --batch --directory=commands/
./validate-pts.sh --batch --directory=docs/core/

# Generate compliance dashboard
./validate-pts.sh --report --output=pts-compliance-report.md
```

## Error Handling Framework

### Validation Failures
```bash
ERROR: PTS Component failure detected
COMPONENT: [Specific component name]
CURRENT_SCORE: [Score/3]
ISSUE: [Specific problem description]
IMPACT: [Effect on overall system quality]
RECOVERY: [Exact steps to achieve compliance]
VALIDATION: [How to verify fix is successful]
```

### Blocking Criteria Triggered
```bash
BLOCKING_ERROR: Critical PTS violation detected
CATEGORY: [Critical/Quality/Architecture]
VIOLATION: [Specific violation description]
SYSTEM_IMPACT: [Effect on overall system]
MANDATORY_FIX: [Required action before proceeding]
VERIFICATION: [Compliance re-check procedure]
```

## Implementation Standards

### Automated Integration
- Integrate with command development lifecycle
- Pre-commit hook validation for critical files
- Continuous compliance monitoring for system health
- Dashboard reporting for compliance trends

### Manual Validation Protocol
- Use for new command development
- Apply during refactoring processes
- Validate during system updates
- Check compliance during reviews

### Learning Integration
- Capture common failure patterns
- Build improved validation criteria
- Update thresholds based on experience
- Share compliance learnings across team

---

**Single Responsibility**: Systematic PTS compliance validation providing objective assessment, blocking criteria enforcement, and actionable improvement recommendations for maintaining system quality.