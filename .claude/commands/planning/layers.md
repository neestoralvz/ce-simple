# /planning:layers - Display Construction Dependencies

**29/07/2025 16:20 CDMX** | Show current project construction layers and dependencies

## Function
Display project construction layers, current status, and dependency relationships.

## Usage
```bash
/planning:layers           # Show current project layers
/planning:layers detail    # Show with dependency explanations
```

## Display Format

### Standard View
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

### Detail View  
```bash
/planning:layers detail
```
**Additional information:**
- **Dependency explanations:** Why each layer depends on previous
- **Gate criteria details:** Specific requirements for advancement
- **Current blockers:** What's preventing layer advancement
- **Next actions:** Recommended focus within current layer

## Status Indicators

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

## Context Integration

### Project State Loading
**Source:** context/planning/current.md project tracking
**Fallback:** If no project initialized, suggest `/planning:init`
**Authority:** Reference to project template for layer definitions

### Cross-Command Integration
**Status sync:** Consistent with /planning:status and /planning:focus
**Gate integration:** Connect to /planning:gate for advancement validation
**Focus integration:** Highlight current focus layer from /planning:focus

## Output Examples

### Ce-Simple Current State
```
📋 Project: ce-simple (Context Engineering Framework)

Layer 1: Context Maturation ✅ COMPLETED
├─ TRUTH_SOURCE.md authority established
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

### Web-App Example
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

## Error States
- **No project initialized:** Prompt to run `/planning:init [type]`
- **Invalid project state:** Suggest running `/planning:status` for diagnosis
- **Missing template:** Reference to available project types

---
**Authority:** Dependency layers methodology + project template system
**Integration:** → /planning:init, /planning:gate, /planning:focus, /planning:status