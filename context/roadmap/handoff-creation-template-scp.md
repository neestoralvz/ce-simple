# Handoff Creation Template with SCP Analysis

**31/07/2025 CDMX** | Template for creating handoffs with integrated SCP classification

## AUTORIDAD SUPREMA
@context/roadmap/scp-classification-framework.md → handoff-creation-template-scp.md implements SCP-guided handoff creation per classification authority

## PRINCIPIO FUNDAMENTAL
**"SCP-guided handoff creation ensures optimal design and resource planning from inception"** - Every handoff designed with systematic Scope-Coordination-Processing analysis for strategic execution.

## HANDOFF CREATION WORKFLOW

### **PHASE 1: SCP PRE-ANALYSIS**

#### **Step 1: Scope Analysis (S-Classification)**
```
SCOPE EVALUATION QUESTIONNAIRE:
□ How many components will be affected? (Count: ____)
  • ≤5 components → S1-FOCUSED
  • 6-15 components → S2-CROSS  
  • 15+ components → S3-SYSTEM

□ How many functional areas involved? (Count: ____)
  • 1 area → S1-FOCUSED
  • 2-3 areas → S2-CROSS
  • Entire system → S3-SYSTEM

□ What is the architectural impact?
  • Localized changes → S1-FOCUSED
  • Multi-area integration → S2-CROSS
  • System-wide structural → S3-SYSTEM

SCOPE CLASSIFICATION: S__ (FOCUSED/CROSS/SYSTEM)
```

#### **Step 2: Coordination Analysis (C-Classification)**
```
COORDINATION EVALUATION QUESTIONNAIRE:
□ How many other handoffs must complete first? (Count: ____)
  • 0 dependencies → C1-INDEPENDENT
  • 1-2 dependencies → C2-DEPENDENT
  • 3+ dependencies → C3-ORCHESTRATED

□ Can this handoff run in parallel with others?
  • Yes, completely parallel → C1-INDEPENDENT
  • Partially parallel → C2-DEPENDENT
  • Requires active coordination → C3-ORCHESTRATED

□ What level of synchronization is needed?
  • None required → C1-INDEPENDENT  
  • Basic sequencing → C2-DEPENDENT
  • Continuous coordination → C3-ORCHESTRATED

COORDINATION CLASSIFICATION: C__ (INDEPENDENT/DEPENDENT/ORCHESTRATED)
```

#### **Step 3: Processing Analysis (P-Classification)**
```
PROCESSING EVALUATION QUESTIONNAIRE:
□ What implementation approach is required?
  • Standard patterns → P1-DIRECT
  • Content extraction/modularization → P2-EXTRACTION
  • Complex orchestration → P3-COORDINATION

□ How many processing phases are needed?
  • Single phase → P1-DIRECT
  • Multi-phase with extraction → P2-EXTRACTION
  • Multi-phase with orchestration → P3-COORDINATION

□ What is the technical complexity level?
  • Low (known patterns) → P1-DIRECT
  • Medium (restructuring) → P2-EXTRACTION
  • High (complex coordination) → P3-COORDINATION

PROCESSING CLASSIFICATION: P__ (DIRECT/EXTRACTION/COORDINATION)
```

### **PHASE 2: SCP COMBINATION ANALYSIS**

#### **Step 4: SCP Profile Determination**
```
COMBINED SCP PROFILE: S__C__P__ (e.g., S2C2P2)

COMPLEXITY ASSESSMENT:
□ Low Complexity (S1C1P1, S1C2P1): 1-4 hours, single session
□ Medium Complexity (S2C1P2, S2C2P1, S1C1P3): 4-16 hours, 1-2 days
□ High Complexity (S2C2P2, S3C2P1, S2C3P2): 1-4 days, coordination required
□ Critical Complexity (S3C3P2, S3C3P3): 3-10 days, intensive orchestration

ESTIMATED EFFORT: ____ hours/days
RESOURCE REQUIREMENTS: ____
RISK LEVEL: ____ (Low/Medium/High/Critical)
```

### **PHASE 3: STRATEGY SELECTION**

#### **Step 5: Execution Strategy by SCP Profile**

```
STRATEGY TEMPLATES BY SCP PROFILE:

S1C1P1 (Minimal): 
- ✅ Direct implementation
- ✅ Single-session execution
- ✅ Minimal validation
- ✅ Simple rollback

S2C2P2 (Standard Complex):
- ✅ L2-MODULAR extraction patterns
- ✅ Multi-phase execution 
- ✅ Coordination protocols
- ✅ Quality gates validation

S3C3P3 (Maximum Complex):
- ✅ Full orchestration framework
- ✅ Intensive coordination
- ✅ Comprehensive validation
- ✅ Complex rollback procedures

SELECTED STRATEGY: ____
```

### **PHASE 4: HANDOFF DESIGN**

#### **Step 6: Template Application**

```markdown
# HANDOFF [ID]: [Title] - SCP Profile: [S_C_P_]

**[Date] CDMX** | [Brief description with SCP classification]

## AUTORIDAD SUPREMA
@context/architecture/core/truth-source.md → HANDOFF_[ID] implements [objective] per [authority]

## SCP CLASSIFICATION ANALYSIS

### **Scope: S_-[CLASSIFICATION]**
- **Components Affected**: [count] components
- **Functional Areas**: [list areas]
- **Impact Level**: [Localized/Multi-area/System-wide]

### **Coordination: C_-[CLASSIFICATION]** 
- **Dependencies**: [list dependencies]
- **Parallelization**: [Yes/Partial/No]
- **Coordination Level**: [Independent/Basic/Active]

### **Processing: P_-[CLASSIFICATION]**
- **Approach**: [Direct/Extraction/Orchestration]
- **Phases**: [count] phases
- **Technical Complexity**: [Low/Medium/High]

### **Combined Profile: [S_C_P_]**
- **Estimated Effort**: [hours/days]
- **Risk Level**: [Low/Medium/High/Critical]
- **Resource Requirements**: [description]

## [Continue with standard handoff content based on SCP strategy...]
```

### **PHASE 5: VALIDATION & OPTIMIZATION**

#### **Step 7: SCP Validation Checklist**
```
SCP ACCURACY VALIDATION:
□ Scope classification matches actual component impact
□ Coordination classification reflects true dependencies  
□ Processing classification aligns with technical complexity
□ Combined profile suggests appropriate execution strategy
□ Resource estimation aligns with historical SCP patterns
□ Risk assessment reflects true complexity level

OPTIMIZATION OPPORTUNITIES:
□ Can scope be reduced without losing value?
□ Can dependencies be eliminated or simplified?
□ Can processing be simplified through pattern reuse?
□ Can handoff be split for better SCP profile?

FINAL SCP CLASSIFICATION: S__C__P__
```

## SCP TEMPLATE LIBRARY

### **Quick Templates by Common Profiles**

#### **S1C1P1 Template** (Minimal Handoffs)
```markdown
# HANDOFF [ID]: [Title] - SCP Profile: S1C1P1

**Single-session focused implementation**
- Target: ≤5 components, 1 area, direct execution
- Timeline: 1-4 hours
- Resources: Single developer
- Strategy: Direct implementation with minimal validation
```

#### **S2C2P2 Template** (Standard Complex)
```markdown  
# HANDOFF [ID]: [Title] - SCP Profile: S2C2P2

**Multi-component extraction with coordination**
- Target: 6-15 components, 2-3 areas, L2-MODULAR required
- Timeline: 1-2 days
- Resources: Coordination + specialized processing
- Strategy: L2-MODULAR patterns with quality gates
```

#### **S3C3P3 Template** (Maximum Complexity)
```markdown
# HANDOFF [ID]: [Title] - SCP Profile: S3C3P3

**System-wide orchestrated transformation**
- Target: 15+ components, system architecture, full orchestration
- Timeline: 5-10 days  
- Resources: Full orchestration + specialized coordination
- Strategy: Comprehensive orchestration with extensive validation
```

## INTEGRATION REFERENCES

**SCP Framework**: ← @context/roadmap/scp-classification-framework.md (classification authority)
**Handoff Templates**: → handoff templates by SCP profile
**Pattern Database**: ←→ @context/roadmap/scp-patterns-database.md (historical patterns)
**Dashboard Integration**: ←→ @context/roadmap/dashboard/ (SCP tracking)

---

**TEMPLATE DECLARATION**: Complete handoff creation template with integrated SCP analysis ensuring optimal design, accurate resource planning, and strategic execution from handoff inception.

**EVOLUTION PATHWAY**: Template evolves through usage → pattern refinement → optimization → creation excellence cycle.