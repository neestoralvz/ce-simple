# PTS Validation - Consolidated Authority

**Authority Level**: Validation Framework  
**Updated**: 2025-07-26  
**Status**: Consolidated validation procedures & blocking criteria  
**Module**: 2 of 4 PTS Authority Modules

## 3-Phase Validation Process

### Phase 1: Pre-evaluation (2 minutes)
```markdown
- [ ] What is the specific purpose? (Clarity test)
- [ ] Does it solve exactly one problem? (Sufficiency test)  
- [ ] Uses ≤3 steps to achieve objective? (Directness test)
- [ ] Does it work without additional configuration? (Pragmatism test)
```

### Phase 2: Complete Evaluation (10 minutes)
- Validate all 12 PTS components individually
- Verify absence of blocking criteria
- Measure quantitative metrics where applicable
- Document trade-offs and decisions

### Phase 3: Contextual Validation (5 minutes)  
- Coherence with Tier 1-5 principles
- Alignment with docs/vision/
- Integration with existing system
- Impact on maintainability

## 12-Point Practical Checklist

### Technical Cluster Validation

**1. Directness**
- [ ] What specific problem does it solve? - Precise problem definition
- [ ] Why is it necessary? - Clear need justification  
- [ ] What is the expected result? - Specific and measurable output

**2. Precision**
- [ ] What is the simplest version that works? - Minimal effective solution
- [ ] What can be eliminated without losing function? - Unnecessary element identification
- [ ] Is there a more direct solution? - Simple alternative evaluation

**3. Sufficiency**
- [ ] Does it cover all necessary use cases? - Complete coverage validation
- [ ] Are there any unused or unnecessary features? - Feature utilization audit
- [ ] Is the solution complete for its intended purpose? - Completeness verification

**4. Technical Excellence**
- [ ] Does it meet quality standards? - Technical quality assessment
- [ ] Is error handling comprehensive? - Error scenario coverage
- [ ] Is performance optimized? - Performance requirement validation

### Communication Cluster Validation

**5. Exactitude**
- [ ] Does it precisely match requirements? - Requirements alignment check
- [ ] Is there any objective drift? - Purpose consistency validation
- [ ] Is implementation at the exact point needed? - Implementation precision

**6. Sobriety**
- [ ] Is language direct and technical? - Marketing language elimination
- [ ] Are embellishments removed? - Superfluous content audit
- [ ] Is tone appropriate and professional? - Communication style validation

**7. Structure**
- [ ] Is organization logical and clear? - Structural coherence check
- [ ] Is navigation under 30 seconds? - Navigation efficiency test
- [ ] Are hierarchy levels ≤3? - Complexity management validation

**8. Conciseness**
- [ ] Is information density ≥80%? - Content efficiency measurement
- [ ] Is redundancy eliminated? - Duplication audit
- [ ] Is value/complexity ratio ≥2.0? - Efficiency validation

### Cognitive Cluster Validation

**9. Clarity**
- [ ] Can it be understood in <5 minutes? - Comprehension time test
- [ ] Are there any ambiguities? - Ambiguity elimination check
- [ ] Is first-reading comprehension ≥95%? - Understanding validation

**10. Coherence**
- [ ] Is internal consistency 100%? - Consistency audit
- [ ] Are there any contradictions? - Contradiction detection
- [ ] Does everything fit together logically? - Logical coherence check

**11. Effectiveness**
- [ ] Does it produce measurable results? - Results measurement validation
- [ ] Is success rate ≥90%? - Success rate verification
- [ ] Is user satisfaction ≥85%? - Satisfaction measurement

**12. Pragmatism**
- [ ] Does it function in real conditions? - Real-world testing
- [ ] Is production success rate ≥95%? - Production validation
- [ ] Is maintenance overhead ≤5%? - Maintenance efficiency check

## Blocking Criteria

### Critical Blocking (Stops development)
- **No clear purpose** - Cannot justify the need (Clarity failure)
- **Multiple responsibilities** - Fundamentally violates SRP (Sufficiency failure)  
- **Unnecessary complexity** - Simpler solution exists (Directness failure)
- **Not reusable** - Only useful in specific case (Pragmatism failure)
- **Not maintainable** - Requires specialized knowledge to modify (Technical Excellence failure)

### Quality Blocking (Requires correction)
- **No direct verification** - Cannot be tested effectively (Precision failure)
- **Complex documentation** - Requires extensive explanation (Clarity failure)
- **Inadequate performance** - Doesn't meet basic requirements (Effectiveness failure)
- **Poor error handling** - Errors not informative or without recovery (Exactitude failure)
- **Breaks conventions** - Inconsistent with ecosystem (Coherence failure)

### Architecture Blocking
- **No SSOT** - Data duplicated without justification (Structure failure)
- **Forced integration** - No natural fit with system (Coherence failure)
- **Evolution blocked** - Future changes require major refactoring (Pragmatism failure)

## Context-Specific Quick Tests

### PTS for Commands
```bash
# Quick PTS test for commands
- What workflow does it solve? (30 seconds)
- Does it work without configuration? (KISS)
- Is output evident? (Direct verification)
- Is it self-contained? (No external dependencies)
```

### PTS for Documentation
```bash
# Quick PTS test for docs
- What question does it answer? (Clear purpose)
- Is it understood without additional context? (Self-evident)
- Does it have practical examples? (Direct verification)
- Can it be applied immediately? (Pragmatism)
```

### PTS for Code
```bash
# Quick PTS test for code
- What exactly does it do? (Single responsibility)
- Does name fully describe function? (Self-evident)
- Can it be tested in isolation? (Direct verification)
- Is API stable? (Controlled evolution)
```

### PTS for Architecture
```bash
# Quick PTS test for architecture
- What fundamental principle does it establish? (Clear purpose)
- Does it facilitate or complicate development? (Technical simplicity)
- Is it evident how to use it? (Pragmatism)
- Does it scale naturally? (Controlled evolution)
```

## Success Metrics

- **Comprehension time**: <5 minutes to understand completely
- **Usage time**: <2 minutes to use effectively
- **Modification time**: <15 minutes for typical changes
- **Reusability**: Used in >3 different contexts
- **Maintenance**: <30 minutes/month average maintenance

---

## Module Integration

**Related Authority Modules:**
- **[pts-framework-consolidated.md](pts-framework-consolidated.md)** - Core 12-component definitions & metrics
- **[pts-governance-consolidated.md](pts-governance-consolidated.md)** - Tier integration & governance framework  
- **[pts-application-consolidated.md](pts-application-consolidated.md)** - Context-specific applications & examples

**Cross-References:**
- Validation procedures extracted from: docs/core/pts-checklist.md (@lines:85-189)
- Blocking criteria preserved from: docs/analysis/pts-content-extraction-analysis.md (@lines:101-121)
- Quick tests consolidated from: docs/core/pts-framework.md (@lines:267-305)