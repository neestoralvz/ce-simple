# Pragmatic Technical Simplicity (PTS) - System Checklist

**Updated**: 2025-07-24 12:54 (Mexico City)  
**Navigation**: [System Hub](../navigation/index.md) | [PTS Framework](pts-framework.md) | [Development Principles](development-principles.md)

## Tier 0 - PTS Foundation (MANDATORY)

**Apply BEFORE any development - primary filter determining viability**

### 📋 PTS Checklist - 12 Critical Components

**All elements MUST be fulfilled to proceed:**

#### 1. **Clear Purpose**
- [ ] **What specific problem does it solve?** - Precise problem definition
- [ ] **Why is it necessary?** - Clear need justification
- [ ] **What is the expected result?** - Specific and measurable output

#### 2. **Minimal Viable Implementation**  
- [ ] **What is the simplest version that works?** - Minimal effective solution
- [ ] **What can be eliminated without losing function?** - Unnecessary element identification
- [ ] **Is there a more direct solution?** - Simple alternative evaluation

#### 3. **Single Responsibility**
- [ ] **Does it do one thing well?** - SRP applied meticulously
- [ ] **Can it be described in one sentence?** - Unique purpose clarity
- [ ] **Does it avoid multiple reasons to change?** - Responsibility stability

#### 4. **Immediate Reusability**
- [ ] **Is it useful in multiple contexts?** - Broad applicability
- [ ] **Does it have a clear and stable interface?** - Consistent API
- [ ] **Does it compose naturally with other elements?** - Fluid composition

#### 5. **Evident Maintainability**
- [ ] **Does a new developer understand it quickly?** - Immediate clarity
- [ ] **Are changes localized and predictable?** - Controlled impact
- [ ] **Does the name describe exactly what it does?** - Precise nomenclature

#### 6. **Direct Verification**
- [ ] **Can it be tested simply?** - Straightforward testing
- [ ] **Is the result evident and immediate?** - Clear feedback
- [ ] **Are errors obvious and useful?** - Efficient debugging

#### 7. **Natural Integration**
- [ ] **Does it connect naturally with the ecosystem?** - Architectural fit
- [ ] **Does it respect existing conventions?** - System consistency
- [ ] **Does it improve without breaking?** - Compatibility preserved

#### 8. **Self-Evident Documentation**
- [ ] **Does the code/command self-document?** - Intrinsic clarity
- [ ] **Are examples trivial to understand?** - Minimal learning curve
- [ ] **Is documentation minimal but sufficient?** - Precise balance

#### 9. **Adequate Performance**
- [ ] **Is it fast enough for its purpose?** - Performance objective
- [ ] **Does it use resources reasonably?** - Appropriate efficiency
- [ ] **Does it scale appropriately for the use case?** - Scalability target

#### 10. **Clear Error Handling**
- [ ] **Are errors informative and actionable?** - Useful feedback
- [ ] **Does it fail fast with clear guidance?** - Fail fast applied
- [ ] **Is recovery obvious?** - Evident recovery path

#### 11. **Data Principles**
- [ ] **Does it have a single source of truth?** - SSOT applied
- [ ] **Does it avoid unnecessary duplication?** - DRY respected
- [ ] **Do data have consistent format?** - Uniform structure

#### 12. **Controlled Evolution**
- [ ] **Can it evolve without breaking dependencies?** - Backward compatibility
- [ ] **Does it have obvious extension points?** - Clear extension points
- [ ] **Does it preserve interface stability?** - API stability

## 🚫 PTS Blocking Criteria

**Any of these elements PREVENTS proceeding:**

### Critical Blocking
- **No clear purpose** - Cannot justify the need
- **Multiple responsibilities** - Fundamentally violates SRP
- **Unnecessary complexity** - Simpler solution exists
- **Not reusable** - Only useful in specific case
- **Not maintainable** - Requires specialized knowledge to modify

### Quality Blocking
- **No direct verification** - Cannot be tested effectively
- **Complex documentation** - Requires extensive explanation
- **Inadequate performance** - Doesn't meet basic requirements
- **Poor error handling** - Errors not informative or without recovery
- **Breaks conventions** - Inconsistent with ecosystem

### Architecture Blocking
- **No SSOT** - Data duplicated without justification
- **Forced integration** - No natural fit with system
- **Evolution blocked** - Future changes require major refactoring

## 🔄 PTS Validation Process

### Phase 1: Pre-evaluation (2 minutes)
1. **Elevator Pitch Test**: Can it be explained in 30 seconds?
2. **Single Purpose Test**: Does it do exactly one thing?
3. **Simplicity Test**: Is it the simplest possible solution?

**If any test fails → STOP → Redesign**

### Phase 2: Complete Evaluation (10 minutes)
1. **Execute complete 12-component checklist**
2. **Verify absence of blocking criteria**
3. **Document decisions and trade-offs**

**If any component fails → STOP → Document reason → Redesign**

### Phase 3: Contextual Validation (5 minutes)
1. **Verify fit with tier 1-5 principles**
2. **Confirm alignment with docs/vision/**
3. **Validate consistency with existing system**

**If contextual validation fails → STOP → Evaluate systemic impact**

## 📊 Context-Specific Application Matrix

### PTS for Commands
**Specific focus:**
- Purpose: Unique and clear workflow
- Implementation: Self-contained logic
- Reusability: Applicable to multiple projects
- Verification: Predictable and measurable output

**Command validation:**
```bash
# Quick PTS test for commands
- What workflow does it solve? (30 seconds)
- Does it work without configuration? (KISS)
- Is output evident? (Direct verification)
- Is it self-contained? (No external dependencies)
```

### PTS for Documentation
**Specific focus:**
- Purpose: Specific and actionable information
- Implementation: Clear and navigable structure
- Reusability: Applicable patterns
- Verification: Immediately evident utility

**Documentation validation:**
```bash
# Quick PTS test for docs
- What question does it answer? (Clear purpose)
- Is it understood without additional context? (Self-evident)
- Does it have practical examples? (Direct verification)
- Can it be applied immediately? (Pragmatism)
```

### PTS for Code
**Specific focus:**
- Purpose: Well-defined specific function
- Implementation: Clean and direct code
- Reusability: Composable modules
- Verification: Simple and obvious tests

**Code validation:**
```bash
# Quick PTS test for code
- What exactly does it do? (Single responsibility)
- Does name fully describe function? (Self-evident)
- Can it be tested in isolation? (Direct verification)
- Is API stable? (Controlled evolution)
```

### PTS for Architecture
**Specific focus:**
- Purpose: Structure that facilitates development
- Implementation: Clear separation of responsibilities
- Reusability: Stable architectural patterns
- Verification: Evident quality metrics

**Architecture validation:**
```bash
# Quick PTS test for architecture
- What fundamental principle does it establish? (Clear purpose)
- Does it facilitate or complicate development? (Technical simplicity)
- Is it evident how to use it? (Pragmatism)
- Does it scale naturally? (Controlled evolution)
```

## 🔗 Integration with Existing Principles

### PTS modifies SOLID application:
- **SRP + PTS**: One clear responsibility AND pragmatically useful
- **OCP + PTS**: Extensible in simple and evident way
- **LSP + PTS**: Substitution without additional complexity
- **ISP + PTS**: Specific interfaces AND easy to use
- **DIP + PTS**: Pragmatic abstractions, not theoretical

### PTS modifies DRY application:
- **Classic DRY**: Don't repeat code
- **DRY + PTS**: Don't repeat knowledge, with pragmatism
- **Criteria**: If eliminating duplication adds significant complexity, evaluate trade-off

### PTS modifies YAGNI application:
- **Classic YAGNI**: Don't implement until necessary
- **YAGNI + PTS**: Don't implement until pragmatically valuable
- **Criteria**: Need must be evident and immediate, not speculative

## 🎯 System Implementation

### Application Order
1. **PTS Tier 0** - Mandatory primary filter
2. **Tier 1-5 Principles** - Applied only if passes PTS
3. **Specific context** - Final validation

### Development Flow
```yaml
Idea/Requirement:
  -> PTS Pre-evaluation (2 min)
  -> If passes: PTS Complete Evaluation (10 min)  
  -> If passes: PTS Contextual Validation (5 min)
  -> If passes: Apply Tier 1-5 principles
  -> Implement
```

### PTS Success Metrics
- **Comprehension time**: <5 minutes to understand completely
- **Usage time**: <2 minutes to use effectively
- **Modification time**: <15 minutes for typical changes
- **Reusability**: Used in >3 different contexts
- **Maintenance**: <30 minutes/month average maintenance

---

**Fundamental Principle**: PTS is the mandatory filter that ensures we only develop solutions that are simultaneously simple, technically sound, and pragmatically valuable.

**Application**: Every system element must pass PTS before any other consideration - it's the foundation that enables architectural excellence without over-engineering.

## See Also
- **[PTS Framework](pts-framework.md)** - Complete technical framework definition
- **[Development Principles](development-principles.md)** - Tier 0-5 principle hierarchy
- **[Development Standards](../rules/development-standards.md)** - Implementation requirements
- **[CLAUDE_RULES.md](../../CLAUDE_RULES.md)** - Partnership protocol with PTS mandates
- **[System Navigation](../navigation/index.md)** - Complete system access hub