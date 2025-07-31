# Think x4 Analysis Template - Architectural Pattern Evaluation Framework

**31/07/2025 00:15 CDMX** | Systematic architectural decision methodology per Think x4 authority

## AUTORIDAD SUPREMA
← templates/quality/ → think-x4-analysis.md implements systematic architectural pattern evaluation per ADR-024 Think x4 methodology authority

## PRINCIPIO FUNDAMENTAL
**"Four-perspective systematic analysis eliminates assumption-based architectural decisions"** - Evidence-based architectural pattern evaluation through structured analysis framework.

## ARCHITECTURAL PATTERN EVALUATION FRAMEWORK

### **Think x4 Analysis Structure**
```
ARCHITECTURAL DECISION: [Decision Name]
CONTEXT: [Background + Problem Statement]

**THINK 1: Context Overlap Analysis**
- Compare proposed solution against existing system components
- Measure overlap percentage with current architecture
- Assessment: [0-100%] overlap → [Novel/Optimization/Redundant]

**THINK 2: Incremental Value Assessment** 
- Quantify genuine technical value vs existing solutions
- Identify unique capabilities and functionality gaps
- Assessment: [High/Medium/Low] incremental value → [Justified/Questionable/Unjustified]

**THINK 3: Pattern Classification Analysis**
- Distinguish novel architectural patterns vs optimization
- Evaluate architectural significance and system impact
- Assessment: [Novel Pattern/Optimization/Documentation] → [ADR/Enhancement/Documentation]

**THINK 4: Evidence-Based Decision Rationale**
- Systematic justification based on previous three perspectives
- Resource investment validation through evidence synthesis
- Assessment: [Recommended/Conditional/Not Recommended] → [Implementation/Review/Archive]
```

### **Evidence-Based ADR Decision Methodology**

#### **Novel vs Optimization Distinction Criteria**
- **Novel Pattern Indicators**: <5% overlap + High incremental value + Architectural significance
- **Optimization Indicators**: 30-70% overlap + Medium incremental value + Performance improvement  
- **Documentation Indicators**: >70% overlap + Low incremental value + Clarification only

#### **Decision Matrix Framework**
| Think 1 Overlap | Think 2 Value | Think 3 Pattern | Think 4 Decision | Recommendation |
|-----------------|---------------|-----------------|------------------|----------------|
| 0-20%          | High          | Novel           | Recommended      | **CREATE ADR** |
| 20-50%         | Medium        | Novel           | Conditional      | **ENHANCE EXISTING** |
| 50-80%         | Low           | Optimization    | Not Recommended  | **DOCUMENT ONLY** |
| 80-100%        | Negligible    | Documentation   | Not Recommended  | **ARCHIVE** |

## SYSTEMATIC ANALYSIS APPROACH FOR ARCHITECTURE DECISIONS

### **Pre-Analysis Preparation**
1. **Context Loading**: Load relevant system components and authority sources
2. **Stakeholder Identification**: Identify affected components and authority chains
3. **Success Criteria Definition**: Define measurable outcomes for decision validation

### **Analysis Execution Protocol**
1. **Think 1 Execution**: Systematic comparison with existing system components
2. **Think 2 Execution**: Quantitative value assessment with specific metrics  
3. **Think 3 Execution**: Pattern classification with architectural impact analysis
4. **Think 4 Execution**: Evidence synthesis and recommendation generation

### **Post-Analysis Validation**
1. **Authority Alignment**: Validate decision against user vision supremacy
2. **Resource Assessment**: Confirm resource investment justification
3. **Implementation Pathway**: Define systematic implementation approach
4. **Success Metrics**: Establish measurable validation criteria

## TEMPLATE APPLICATION EXAMPLES

### **Example 1: Novel Architectural Pattern (ADR Creation)**
```
DECISION: Unified File Naming Convention System
THINK 1: 0% overlap with existing conventions → Novel
THINK 2: High value (system coherence + automation) → Justified  
THINK 3: Novel pattern (systematic standardization) → ADR
THINK 4: Evidence-based recommendation → CREATE ADR-030
```

### **Example 2: System Optimization (Enhancement)**
```  
DECISION: Performance Improvement Protocol
THINK 1: 40% overlap with existing monitoring → Optimization
THINK 2: Medium value (specific improvement) → Conditional
THINK 3: Optimization pattern (performance focus) → Enhancement
THINK 4: Conditional recommendation → ENHANCE EXISTING
```

## INTEGRATION REFERENCES

### **Authority Sources**
- **Methodology Authority**: ← @context/architecture/core/methodology.md (Think x4 framework)
- **ADR Integration**: ← ADR-024-think-x4-methodology-universal-integration.md (systematic analysis)
- **Quality Framework**: ← @context/architecture/templates/quality/ (quality template authority)

### **Usage Integration**
- **Pattern Evaluation**: Use for all architectural pattern decisions
- **ADR Creation**: Apply before creating new architectural decisions
- **System Enhancement**: Apply before modifying existing components

---

**TEMPLATE DECLARATION**: This Think x4 analysis template provides systematic architectural pattern evaluation eliminating assumption-based decisions through evidence-based four-perspective methodology.

**EVOLUTION PATHWAY**: Template evolves through usage → validation → methodology refinement cycle.