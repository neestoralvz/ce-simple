# Planning Layers Templates Module

## Standard Display Template
```
📋 Project: [project-type] Construction Layers

Layer 1: [Foundation] ✅ COMPLETED
├─ [Key achievements list]
└─ Gate: [Completion criteria] ✅

Layer 2: [Development] 🔄 ACTIVE  
├─ [Current focus areas]
├─ Progress: [X/Y items completed]
└─ Gate: [Readiness criteria] ⏳

Layer 3: [Integration] ⏳ PENDING
├─ Dependencies: Layer 2 completion
└─ Gate: [Future criteria] 📋

Layer 4: [Distribution] ⏳ PENDING
├─ Dependencies: Layer 3 completion  
└─ Gate: [Final criteria] 📋
```

## Status Indicators Template
### Layer Status
- **✅ COMPLETED:** Layer finished, gate passed, ready for next
- **🔄 ACTIVE:** Currently working in this layer
- **⏳ PENDING:** Waiting for dependencies, not yet accessible
- **🚫 BLOCKED:** Dependencies failed, requires attention

### Gate Status  
- **✅ PASSED:** Requirements met, advancement available
- **⏳ PENDING:** Requirements in progress, advancement blocked
- **🚫 FAILED:** Requirements not met, requires resolution
- **📋 DEFINED:** Criteria established, evaluation not yet run

## Project Examples Templates

### Ce-Simple Current State Template
```
📋 Project: ce-simple (Context Engineering Framework)

Layer 1: Context Maturation ✅ COMPLETED
├─ @context/architecture/core/truth-source.md authority established
├─ Methodology protocols crystallized  
├─ Authority hierarchy defined
└─ Gate: Context stable + protocols proven ✅

Layer 2: System Crystallization 🔄 ACTIVE
├─ Commands system optimized
├─ Progress: 35/38 files need ≤80 line refactoring
├─ Templates consolidated
└─ Gate: File sizes compliant + commands functional ⏳

Layer 3: Distribution Readiness ⏳ PENDING
├─ Dependencies: Layer 2 completion
├─ dist/ system design needed
└─ Gate: Framework tested + distribution validated 📋
```

### Web-App Example Template
```
📋 Project: web-app Construction Layers

Layer 1: Database Foundation ✅ COMPLETED
├─ Schema design finalized
├─ Migrations functional
└─ Gate: CRUD operations working ✅

Layer 2: Backend Development 🔄 ACTIVE
├─ API endpoints: 12/18 completed
├─ Authentication: In progress
└─ Gate: Frontend can consume APIs ⏳

Layer 3: Frontend Development ⏳ PENDING
Layer 4: Integration & Deploy ⏳ PENDING
```

## Detail View Extensions Template
**Additional information for /planning:layers detail:**
- **Dependency explanations:** Why each layer depends on previous
- **Gate criteria details:** Specific requirements for advancement
- **Current blockers:** What's preventing layer advancement
- **Next actions:** Recommended focus within current layer

**Usage**: Construction layer display with dependencies, status indicators, and project-specific examples