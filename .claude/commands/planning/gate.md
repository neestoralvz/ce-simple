# /planning:gate - Layer Advancement Validation

**29/07/2025 16:25 CDMX** | Validate readiness for next construction layer

## Function
Validate current layer completion and authorize advancement to next layer.

## Usage
```bash
/planning:gate              # Validate current layer readiness
/planning:gate check        # Check without advancing
/planning:gate force        # Override validation (caution!)
```

## Validation Process

### 1. Current Layer Assessment
**Completion criteria check:** Verify all layer requirements met
**Quality validation:** Ensure standards maintained (file sizes, references, etc.)
**Dependency verification:** Confirm foundational elements stable

### 2. Readiness Gate Criteria

#### Layer 1 → Layer 2 (Foundation → Development)
**Criteria:**
- Core architecture decisions crystallized ✅/❌
- Authority hierarchy established ✅/❌  
- Basic system functionality proven ✅/❌
- Foundation stability validated ✅/❌

#### Layer 2 → Layer 3 (Development → Integration)  
**Criteria:**
- Core features implemented and tested ✅/❌
- Code quality standards met (≤80 lines, DRY, etc.) ✅/❌
- Cross-component dependencies resolved ✅/❌
- System coherence maintained ✅/❌

#### Layer 3 → Layer 4 (Integration → Distribution)
**Criteria:**
- End-to-end functionality validated ✅/❌
- Performance requirements met ✅/❌
- Documentation completeness achieved ✅/❌
- Distribution preparation ready ✅/❌

### 3. Advancement Decision

#### ✅ GATE PASSED
```
🎉 Layer [X] Complete - Ready for Layer [X+1]

✅ All criteria met:
  ✅ [Criterion 1] - [Status detail]
  ✅ [Criterion 2] - [Status detail]  
  ✅ [Criterion 3] - [Status detail]

🎯 Advancing to Layer [X+1]: [Next layer description]
📋 Next focus: [Specific next actions]
```

#### ❌ GATE BLOCKED
```
🚫 Layer [X] Incomplete - Advancement Blocked

❌ Unmet criteria:
  ❌ [Failed criterion] - [Issue description]
  ⏳ [Pending criterion] - [What's needed]
  ✅ [Met criterion] - [Confirmed]

🔧 Required actions:
  1. [Specific action for failed criterion]
  2. [Specific action for pending criterion]
  
📋 Run /planning:gate when criteria resolved
```

## Project-Specific Gates

### Ce-Simple Gates
**Layer 1 → 2:** Context/TRUTH_SOURCE stable + methodology proven ✅
**Layer 2 → 3:** File sizes ≤80 lines + commands functional ⏳
**Layer 3 → Complete:** Framework tested + dist/ ready 📋

### Web-App Gates  
**Layer 1 → 2:** Database schema stable + CRUD working
**Layer 2 → 3:** APIs complete + authentication functional
**Layer 3 → 4:** Frontend connected + user flows working
**Layer 4 → Complete:** Testing passed + deployment ready

### CLI-Tool Gates
**Layer 1 → 2:** Core logic proven + data structures stable
**Layer 2 → 3:** Commands working + help system complete
**Layer 3 → 4:** Configuration validated + packaging ready
**Layer 4 → Complete:** Installation tested + documentation complete

## Override Options

### /planning:gate force
**Use case:** Exceptional circumstances requiring gate bypass
**Warning:** Displays risks of advancing with incomplete foundation
**Confirmation:** Requires explicit user confirmation before proceeding
**Logging:** Records forced advancement for future reference

### /planning:gate check  
**Use case:** Assessment without automatic advancement
**Output:** Shows gate status but doesn't change current layer
**Purpose:** Planning and preparation for upcoming advancement

## Integration Points

### Status Update
**Current layer advancement:** Update project tracking in context/planning/current.md
**Focus shift:** Automatically update /planning:focus to new layer
**Progress recording:** Log advancement in project history

### Cross-Command Coordination
**Layer visibility:** Update /planning:layers display with new status
**Status consistency:** Sync with /planning:status overall view
**Focus alignment:** Coordinate with /planning:focus layer setting

## Error States
- **No project initialized:** Prompt to run `/planning:init [type]`
- **Already at final layer:** Congratulate completion, suggest next steps
- **Invalid layer state:** Suggest `/planning:status` for diagnosis

---
**Authority:** Dependency layers methodology + quality gate enforcement
**Integration:** → /planning:layers, /planning:focus, /planning:status