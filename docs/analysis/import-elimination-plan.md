# @ Import Elimination Implementation Plan

**Updated**: 2025-07-24 | **Target**: 95%+ elimination (107 → ≤10 lines) | **Critical**: Foundation task

## Current @ Import Analysis

### **CLAUDE.md @ Imports** (Total: 107 lines always-loaded)
1. `@docs/core/project-structure-current.md` - 82 lines
2. `@CLAUDE_RULES.md:1-25` - 25 lines

### **5-Criteria Decision Matrix Evaluation**

#### **Import 1: @docs/core/project-structure-current.md (82 lines)**
- **Immediate Necessity**: ❌ Project structure not needed every session
- **Session Frequency**: ❌ <50% of sessions reference project structure
- **Context Economy**: ❌ 82 lines far exceeds budget for this content
- **Authority Hierarchy**: ❌ Not single-source authority requiring immediate access
- **Redundancy Elimination**: ❌ Can be accessed via reference link when needed

**Decision**: ❌ ELIMINATE - Convert to conditional READ instruction

#### **Import 2: @CLAUDE_RULES.md:1-25 (25 lines)**
- **Immediate Necessity**: ⚠️ Partnership protocol arguably essential
- **Session Frequency**: ✅ Referenced in 100% of sessions  
- **Context Economy**: ⚠️ 25 lines significant but manageable
- **Authority Hierarchy**: ✅ Core operational authority requiring immediate access
- **Redundancy Elimination**: ⚠️ Could be accessed via reference but creates friction

**Decision**: ⚠️ EVALUATE - Consider retention vs conditional loading

## Elimination Strategy

### **Phase A: Complete @ Import Elimination** (Target: 0 @ imports)
Convert all @ imports to conditional READ instructions in CLAUDE_RULES.md

**Optimized CLAUDE.md Structure** (Target: 25 lines):
```markdown
# CLAUDE.md - ce-simple

**Updated**: 2025-07-24 | **Partnership**: [CLAUDE_RULES.md](CLAUDE_RULES.md) | **Navigation**: [System Hub](docs/navigation/index.md) | **Limit**: 25 lines

## Tech Stack
- **Platform**: Claude Code slash commands
- **Architecture**: Self-contained commands with Task Tool parallel execution
- **Validation**: UltraThink x4 + PTS framework (conditional on validation tasks)

## Project Structure
[Project Structure](docs/core/project-structure-current.md) - Live system architecture

## Commands
[Command Index](docs/core/command-index.md) - Local + global command reference

## Development Standards
- **Commands**: ≤80 lines, self-contained | **Docs**: ≤100 lines (conditional standards)
- **Context**: Conditional loading based on task type | **UltraThink x4 + PTS**: Universal cognitive + 12/12 technical (conditional)
- **Authority**: docs/vision/ → CLAUDE_RULES → docs/core/ → CLAUDE

## Quick References
### Core Access
- **Partnership Protocol**: [CLAUDE_RULES.md](CLAUDE_RULES.md) - Authority & conditional loading
- **Navigation Hub**: [Complete System Index](docs/navigation/index.md) - 2-click access

### Conditional Loading System
- **Documentation Work**: Standards & markdown compliance triggered
- **Validation Tasks**: PTS framework & checklist triggered
- **Development Work**: Principles & templates triggered

### Prohibitions
No Spanish | No marketing | No PTS bypass | No vision override | No limit violations

---

**Navigation Hub**: [Complete System Index](docs/navigation/index.md) | **Core**: Simple building blocks → complex workflows via parallel execution
```

### **Phase B: CLAUDE_RULES.md Conditional Enhancement**
Add project structure to conditional loading system:

```markdown
## Conditional Context Instructions (True Conditional Loading)
**IF session start** → READ docs/core/README.md (core architecture) + READ docs/core/decision-navigation-system.md (decision trees) + READ docs/core/command-index.md (available commands) + READ docs/core/project-structure-current.md (current structure)
**IF project understanding** → READ docs/core/project-structure-current.md:1-82 (complete architecture)
[... existing conditional instructions ...]
```

## Implementation Execution

### **Step 1: Create Optimized CLAUDE.md** (Zero @ imports)
- Remove both @ import lines
- Create reference-based navigation structure
- Maintain essential context in ≤25 lines
- Add clear pathway to all major system components

### **Step 2: Enhanced Conditional Loading**
- Ensure CLAUDE_RULES.md conditional system covers all eliminated @ imports
- Add project structure to "IF session start" or dedicated conditional
- Test that all essential information remains accessible

### **Step 3: Validation Testing**
- Verify zero @ imports in CLAUDE.md
- Test conditional loading provides equivalent functionality
- Confirm context economy target achieved

## Expected Impact

### **Context Load Reduction**
- **Before**: CLAUDE.md (31) + @ imports (107) = 138 lines always-loaded
- **After**: CLAUDE.md (25) + CLAUDE_RULES.md (unchanged conditional system) = 25 lines always-loaded from CLAUDE.md
- **Reduction**: 138 → 25 = **82% reduction in CLAUDE.md always-loaded content**

### **Total System Context Economy**
- **Previous Analysis**: 510 lines total always-loaded (including CLAUDE_RULES.md imports)
- **After CLAUDE.md Optimization**: Approximately 400 lines total (510 - 110 eliminated)
- **Progress Toward Target**: 400 lines (target: ≤50 lines overall)

### **Information Access Preservation**
- **Project Structure**: Available via conditional READ or direct reference link
- **Partnership Protocol**: Immediate access via CLAUDE_RULES.md reference
- **Navigation**: Enhanced through reference-based system
- **Authority Hierarchy**: Maintained through clear reference structure

## Success Validation

### **Quantitative Targets**
- **@ Imports**: 2 → 0 (100% elimination)
- **CLAUDE.md Lines**: 31 → 25 (19% reduction)
- **Always-Loaded from CLAUDE.md**: 138 → 25 (82% reduction)
- **Reference Functionality**: 100% equivalent access maintained

### **Quality Standards**
- **Information Preservation**: Zero loss of essential functionality
- **Navigation Excellence**: Clear pathways to all system components
- **Authority Maintenance**: Hierarchy preserved through reference system
- **Context Economy**: Significant progress toward ≤50 line target

---
**Elimination Principle**: Remove all @ imports while preserving 100% information access through optimized reference architecture and conditional loading system.