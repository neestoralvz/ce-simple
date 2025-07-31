# Risk Assessment Framework - Risk Classification & Priority Authority

**31/07/2025 15:30 CDMX** | Risk classification matrix and priority calculation methodology

## AUTORIDAD SUPREMA
← risk-stratified-migration-patterns.md → risk-assessment-framework.md implements risk classification per migration authority

## PRINCIPIO FUNDAMENTAL
**"Systematic risk classification enables evidence-based migration prioritization with quantifiable decision criteria"** - Risk Assessment Dimensions + Priority Formula = Objective migration sequencing.

## RISK CLASSIFICATION MATRIX

### Risk Assessment Dimensions
```
Risk Assessment Framework:
├── IMPACT LEVEL: LOW | MEDIUM | HIGH (system functionality change)
├── RISK LEVEL: LOW | MEDIUM | HIGH (probability of issues/rollback)
├── COMPLEXITY: LOW | MEDIUM | HIGH (implementation difficulty)
└── DEPENDENCIES: NONE | INTERNAL | EXTERNAL (cross-system impact)
```

### Migration Priority Formula
**Priority = (Impact × 3) + (Inverse Risk × 2) + (Inverse Complexity × 1)**

**Calculation Examples:**
- High Impact + Low Risk + Low Complexity = (3×3) + (3×2) + (3×1) = 18 = **Highest Priority**
- Medium Impact + Medium Risk + Low Complexity = (2×3) + (2×2) + (3×1) = 13 = **Medium Priority**  
- Low Impact + High Risk + High Complexity = (1×3) + (1×2) + (1×1) = 6 = **Lowest Priority**

## RISK CLASSIFICATION PROTOCOL

### Classification Evaluation Framework
**1. Impact Assessment**: Functionality change, user experience, system performance, authority chain modification
**2. Risk Evaluation**: Historical failure rates, complexity factors, dependency analysis, rollback complexity  
**3. Complexity Analysis**: Implementation steps, validation requirements, cross-reference updates, integration testing
**4. Dependency Mapping**: NONE (isolated) | INTERNAL (same system) | EXTERNAL (cross-system/APIs)

## PRACTICAL CLASSIFICATION TEMPLATES

### Component Risk Assessment Template
```markdown
## [Component Name] Risk Assessment
- **Component**: [Description and scope]
- **Impact Level**: [LOW|MEDIUM|HIGH] - [Functionality change justification]
- **Risk Level**: [LOW|MEDIUM|HIGH] - [Risk factors and failure probability]
- **Complexity**: [LOW|MEDIUM|HIGH] - [Implementation difficulty factors]
- **Dependencies**: [NONE|INTERNAL|EXTERNAL] - [Dependency list and impact]
- **Priority Score**: [Calculated using formula]
- **Recommended Phase**: [1|2|3|4] - [Phase assignment rationale]
- **Rollback Protocol**: [Specific rollback procedure description]
```

## INTEGRATION REFERENCES

### Authority Integration
**Pattern Authority**: ← ../README.md (risk assessment validation)
**Migration Authority**: ← risk-stratified-migration-patterns.md (framework application)

---

**RISK ASSESSMENT DECLARATION**: Systematic risk classification framework enabling evidence-based migration prioritization through quantifiable criteria and structured evaluation protocols.

**APPLICATION**: Risk classification → priority calculation → phase assignment → migration execution