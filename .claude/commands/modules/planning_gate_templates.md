# Planning Gate Templates Module

## Gate Validation Templates

### Layer 1 → Layer 2 (Foundation → Development)
**Criteria:**
- Core architecture decisions crystallized ✅/❌
- Authority hierarchy established ✅/❌  
- Basic system functionality proven ✅/❌
- Foundation stability validated ✅/❌

### Layer 2 → Layer 3 (Development → Integration)  
**Criteria:**
- Core features implemented and tested ✅/❌
- Code quality standards met (≤80 lines, DRY, etc.) ✅/❌
- Cross-component dependencies resolved ✅/❌
- System coherence maintained ✅/❌

### Layer 3 → Layer 4 (Integration → Distribution)
**Criteria:**
- End-to-end functionality validated ✅/❌
- Performance requirements met ✅/❌
- Documentation completeness achieved ✅/❌
- Distribution preparation ready ✅/❌

## Advancement Decision Templates

### ✅ GATE PASSED Template
```
🎉 Layer [X] Complete - Ready for Layer [X+1]

✅ All criteria met:
  ✅ [Criterion 1] - [Status detail]
  ✅ [Criterion 2] - [Status detail]  
  ✅ [Criterion 3] - [Status detail]

🎯 Advancing to Layer [X+1]: [Next layer description]
📋 Next focus: [Specific next actions]
```

### ❌ GATE BLOCKED Template
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

## Project-Specific Gates Templates

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

**Usage**: Layer advancement validation with project-specific criteria and quality gate enforcement