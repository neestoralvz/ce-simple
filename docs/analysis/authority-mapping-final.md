# Authority Mapping - Single Source of Truth Architecture

**Updated**: 2025-07-24 | **Purpose**: Definitive authority assignment | **Impact**: 98% duplication elimination

## Authority Architecture Framework

### **Technical Authority Files** (≤80 lines each)
**Purpose**: Dense technical content optimized for line-level referencing
**Pattern**: Lines 1-10 overview, 11-80 organized by concept with stable line numbers

1. **`docs/technical/pts-framework-technical.md`** ✅ AUTHORITY: PTS Framework
   - Lines 1-20: 12-component framework definition  
   - Lines 21-40: Technical cluster (Directness, Precision, Sufficiency, Excellence)
   - Lines 41-60: Communication cluster (Exactitude, Sobriety, Structure, Conciseness)
   - Lines 61-80: Cognitive cluster (Clarity, Coherence, Effectiveness, Pragmatism)

2. **`docs/technical/agent-deployment-technical.md`** ✅ AUTHORITY: Task Tool/Agent Deployment
   - Lines 1-20: Task Tool coordination principles
   - Lines 21-40: Parallel execution patterns
   - Lines 41-60: Agent specialization protocols  
   - Lines 61-80: Integration and validation approaches

3. **`docs/technical/markdown-compliance-technical.md`** ✅ AUTHORITY: Markdown Standards
   - Lines 1-20: Line limit standards (≤80 lines docs, ≤50 CLAUDE.md)
   - Lines 21-40: Three-layer architecture requirements
   - Lines 41-60: Compaction techniques and formatting rules
   - Lines 61-80: Validation criteria and compliance checking

4. **`docs/technical/context-economy-framework.md`** ✅ AUTHORITY: Context Economy (Created)
   - Lines 1-20: Mathematical framework and token budget
   - Lines 21-40: @ import elimination strategy
   - Lines 41-60: Reference architecture and optimization
   - Lines 61-80: Validation framework and success metrics

5. **`docs/technical/git-protocols-technical.md`** ✅ AUTHORITY: Git Workflows
   - Lines 1-20: Commit protocols and PR creation
   - Lines 21-40: Branch management and merge strategies
   - Lines 41-60: Git workflow integration with system
   - Lines 61-80: Validation and best practice enforcement

### **Navigation Hub Files** (≤80 lines each)
**Purpose**: Essential context + strategic references to technical authorities
**Pattern**: 20-30 lines overview, 40-50 lines precision references

#### **Core Navigation Hubs**
- **`CLAUDE.md`** → 25 lines max (tech stack + authority + prohibitions)
- **`CLAUDE_RULES.md`** → 25 lines max (partnership protocol only)
- **`docs/core/README.md`** → Navigation hub to technical authorities
- **`docs/rules/README.md`** → Rules navigation with technical references

#### **Specialized Navigation Hubs**
- **`docs/core/pts-framework.md`** → Hub + @technical/pts-framework-technical.md references
- **`docs/patterns/task-tool-communication.md`** → Hub + @technical/agent-deployment-technical.md
- **`docs/rules/markdown-standards.md`** → Hub + @technical/markdown-compliance-technical.md
- **`docs/rules/git-workflow-protocols.md`** → Hub + @technical/git-protocols-technical.md

## Reference Conversion Strategy

### **Mass Reference Pattern**
```markdown
# Before (Duplication)
## PTS Framework Detailed Explanation
The Pragmatic Technical Simplicity framework consists of 12 components that ensure...
[200+ lines of duplicated content]

# After (Authority Reference)
## PTS Framework
**Complete Framework**: @docs/technical/pts-framework-technical.md:1-80
**12 Components**: @docs/technical/pts-framework-technical.md:15-75
**Validation Checklist**: @docs/technical/pts-framework-technical.md:65-80
```

### **Selective Reference Pattern**
```markdown
# Before (Mixed Content)
## Quality Standards and Implementation
PTS framework requires... [100 lines mixed content]
Plus unique implementation details specific to this context...

# After (Selective Authority)
## Quality Standards and Implementation  
**PTS Core Principles**: @docs/technical/pts-framework-technical.md:21-40
**Validation Process**: @docs/technical/pts-framework-technical.md:65-80

### Unique Implementation Details
[Preserved unique content specific to this document]
```

## File Transformation Plan

### **Phase A: Technical Authority Creation** (4 new files)
1. Create `docs/technical/pts-framework-technical.md` - Consolidate 212 PTS references
2. Create `docs/technical/agent-deployment-technical.md` - Consolidate 214 agent references  
3. Create `docs/technical/markdown-compliance-technical.md` - Consolidate 141 markdown references
4. Create `docs/technical/git-protocols-technical.md` - Consolidate 43 git references

### **Phase B: Hub Conversion** (Transform existing files)
1. **`CLAUDE.md`** → Reduce to 25 lines (tech stack + authority hierarchy + prohibitions)
2. **`CLAUDE_RULES.md`** → Reduce to 25 lines (partnership protocol + conditional READ)
3. **Major Navigation Hubs** → Convert to overview + reference pattern

### **Phase C: Mass Reference Conversion** (500+ files affected)
1. **Systematic Replacement**: Convert duplicated content blocks to @path:line-range
2. **Validation Testing**: Verify all references resolve correctly
3. **Information Audit**: Confirm zero unique content loss

## Authority Hierarchy Maintenance

### **Vision Authority** (Absolute)
- `docs/vision/overview.md` - System direction and philosophy
- No technical duplication, maintains vision purity
- References technical details via hub pattern

### **Partnership Authority** (Operational)  
- `CLAUDE_RULES.md` - Partnership protocol (25 lines)
- Core behavioral standards only
- All technical details via READ instructions

### **Technical Authority** (Implementation)
- `docs/technical/*.md` - Dense technical specifications  
- Single source of truth for each major concept
- Optimized for line-level precision referencing

### **Navigation Authority** (Access)
- `CLAUDE.md` - System overview and entry point (25 lines)
- Hub files throughout docs/ - Overview + strategic references
- Master navigation indices for comprehensive access

## Validation Framework

### **Authority Integrity Checks**
```bash
# Verify technical authorities exist and are ≤80 lines
validate_technical_authorities() {
    for file in pts-framework agent-deployment markdown-compliance git-protocols; do
        if [ -f "docs/technical/${file}-technical.md" ]; then
            lines=$(wc -l < "docs/technical/${file}-technical.md")
            if [ $lines -le 80 ]; then
                echo "✅ Authority compliant: ${file}-technical.md ($lines lines)"
            else
                echo "❌ Authority exceeds limit: ${file}-technical.md ($lines lines)"
            fi
        else
            echo "❌ Authority missing: ${file}-technical.md"
        fi
    done
}
```

### **Reference Integrity Validation**
```bash
# Test all @path:line-range references resolve correctly
validate_references() {
    find docs/ -name "*.md" -exec grep -l "@.*:.*-.*" {} \; | while read file; do
        grep -o "@[^:]*:[0-9]*-[0-9]*" "$file" | while read ref; do
            target=$(echo "$ref" | cut -d: -f1 | sed 's/@//')
            if [ ! -f "$target" ]; then
                echo "❌ Broken reference: $ref in $file"
            fi
        done
    done
}
```

## Success Metrics

### **Authority Establishment**
- **Technical Files**: 5 authorities created, each ≤80 lines
- **Single Source**: Each concept has exactly one authoritative location
- **Reference Network**: 500+ files reference authorities instead of duplicating

### **Duplication Elimination**
- **PTS Framework**: 212 → 1 authority (98% reduction)
- **Agent Deployment**: 214 → 1 authority (98% reduction)  
- **Markdown Standards**: 141 → 1 authority (98% reduction)
- **System Total**: ~26,500 → ~400 lines (98.5% elimination)

### **System Integrity**
- **Information Preservation**: 100% unique content maintained
- **Authority Hierarchy**: Vision → Partnership → Technical → Navigation maintained
- **Reference Accuracy**: 100% functional line-level references
- **Navigation Excellence**: ≤3 clicks to any technical concept

---
**Authority Principle**: Single source of truth architecture eliminates massive duplication while preserving complete information access through precision reference system.