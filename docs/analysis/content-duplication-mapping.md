# Content Duplication Mapping - Authority Consolidation Plan

**Updated**: 2025-07-24 | **Crisis Level**: 60%+ duplication across system | **Target**: <5% residual

## Duplication Crisis Analysis

### **Critical Duplication Categories**

#### **1. PTS Framework - MASSIVE (212 occurrences, 43 files)**
**Authority Source**: `docs/technical/pts-framework-technical.md` (to be created)
**Impact**: Most duplicated content in system
**Conversion Strategy**: @docs/technical/pts-framework-technical.md:line-range references

**Major Duplicate Locations**:
- `docs/core/pts-framework.md` (32 refs) - Keep as authority, optimize to 80 lines
- `docs/core/pts-checklist.md` (34 refs) - Convert to navigation hub + references
- `docs/core/development-principles.md` (29 refs) - Aggressive reference conversion
- `docs/core/tier0-pragmatic-technical-simplicity.md` (3 refs) - Reference conversion

#### **2. Task Tool/Agent Deployment - MASSIVE (214 occurrences, 52 files)**
**Authority Source**: `docs/technical/agent-deployment-technical.md` (to be created)
**Impact**: Highest duplication count in system
**Conversion Strategy**: Create comprehensive technical authority file

**Major Duplicate Locations**:
- `docs/patterns/task-tool-communication.md` (10 refs) - Convert to hub + references
- `docs/governance/architecture-decision-record-three-layer-system.md` (13 refs)
- `docs/vision/overview.md` (12 refs) - Keep minimal, reference technical details
- `docs/core/task-orchestration.md` (9 refs) - Hub pattern conversion

#### **3. Markdown Standards/Line Limits - HIGH (141 occurrences, 46 files)**
**Authority Source**: `docs/technical/markdown-compliance-technical.md` (to be created)
**Impact**: Standards scattered across entire system
**Conversion Strategy**: Single technical standards file + line-level references

**Major Duplicate Locations**:
- `docs/rules/markdown-standards.md` (2 refs) - Keep as navigation hub
- `docs/templates/claude-md-template.md` (5 refs) - Reference technical authority
- `docs/rules/documentation-standards-foundation.md` (7 refs) - Hub conversion
- `docs/commands/command-modularization-standards.md` (9 refs) - Reference conversion

#### **4. Context Economy - HIGH (83 occurrences, 38 files)**
**Authority Source**: `docs/technical/context-economy-framework.md` (✅ created)
**Impact**: Core architectural concept duplicated across system
**Conversion Strategy**: Reference existing technical authority file

**Major Duplicate Locations**:
- `docs/templates/cognitive-load-guidelines.md` (6 refs) - Convert to references
- `docs/standards/context-efficiency-optimization.md` (6 refs) - Reference conversion
- `docs/governance/architecture-decision-record-three-layer-system.md` (5 refs)

#### **5. Git Workflows - SIGNIFICANT (43 occurrences, 26 files)**
**Authority Source**: `docs/technical/git-protocols-technical.md` (to be created)
**Impact**: Development workflow duplication
**Conversion Strategy**: Comprehensive git technical authority

**Major Duplicate Locations**:
- `docs/rules/git-workflow-protocols.md` (8 refs) - Keep as navigation hub
- `docs/commands/command-index.md` (3 refs) - Reference conversion
- `docs/core/context-architecture.md` (3 refs) - Reference conversion

## Authority File Creation Plan

### **Technical Authority Files** (≤80 lines each)
1. `docs/technical/pts-framework-technical.md` - Complete PTS 12-component framework
2. `docs/technical/agent-deployment-technical.md` - Task Tool coordination patterns  
3. `docs/technical/markdown-compliance-technical.md` - Complete markdown standards
4. `docs/technical/context-economy-framework.md` - ✅ Already created
5. `docs/technical/git-protocols-technical.md` - Comprehensive git workflows

### **Navigation Hub Conversion** (≤80 lines each)
- Convert current authority files to navigation hubs
- Essential context + strategic references to technical files
- Line-level precision: @file.md:15-30 format

## Conversion Impact Calculation

### **Line Reduction Potential**
- **PTS Framework**: 212 occurrences → 1 authority file (≤80 lines) = ~8,000 line reduction
- **Agent Deployment**: 214 occurrences → 1 authority file (≤80 lines) = ~8,500 line reduction  
- **Markdown Standards**: 141 occurrences → 1 authority file (≤80 lines) = ~5,500 line reduction
- **Context Economy**: 83 occurrences → Reference to existing file = ~3,000 line reduction
- **Git Workflows**: 43 occurrences → 1 authority file (≤80 lines) = ~1,500 line reduction

**Total Potential Reduction**: ~26,500 lines → ~400 lines = **98.5% duplication elimination**

### **Reference Conversion Strategy**

#### **Level 1: Direct Replacement**
```markdown
# Before (duplicated content)
## PTS Framework
The Pragmatic Technical Simplicity framework consists of 12 components...
[Full explanation - 200+ lines]

# After (reference)
## PTS Framework  
Complete framework: @docs/technical/pts-framework-technical.md:1-80
Quick reference: @docs/technical/pts-framework-technical.md:65-80
```

#### **Level 2: Selective References**
```markdown
# Before (partial duplication)
## Quality Standards
PTS compliance requires... [100 lines of mixed content]

# After (selective references)
## Quality Standards
Core principles: @docs/technical/pts-framework-technical.md:15-30
Validation: @docs/technical/pts-framework-technical.md:45-60
[Unique content specific to this document]
```

## Implementation Priority

### **Phase 1: Authority File Creation** (60 minutes)
1. Create 4 new technical authority files (PTS, Agent, Markdown, Git)
2. Consolidate all authoritative content into ≤80 line files
3. Organize for optimal line-level referencing

### **Phase 2: Mass Reference Conversion** (90 minutes)
1. Convert highest-impact duplications first (PTS, Agent Deployment)
2. Apply systematic @file.md:line-range replacements
3. Validate reference accuracy and information preservation

### **Phase 3: Validation & Cleanup** (30 minutes)
1. Test all reference links for functionality
2. Verify zero unique content loss
3. Measure actual line reduction achieved

## Success Metrics

### **Quantitative Targets**
- **Duplication Reduction**: 98%+ of identified duplications eliminated
- **Line Reduction**: ~26,500 → ~400 lines (system-wide impact)
- **Authority Files**: 5 technical files, each ≤80 lines
- **Reference Accuracy**: 100% functional line-level references

### **Quality Validation**
- **Information Preservation**: Zero unique content loss
- **Authority Maintenance**: Single source of truth per concept
- **Navigation Excellence**: Clear hub-to-technical progression
- **System Coherence**: Consistent reference patterns throughout

---
**Consolidation Principle**: Transform massive content duplication into precise reference architecture while preserving 100% information value and establishing single source authority.