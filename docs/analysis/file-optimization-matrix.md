# File Optimization Priority Matrix

**Updated**: 2025-07-24 | **Analysis**: 120 files, 22,025 lines total | **Crisis**: 95 files >80 lines

## Critical Statistics
- **Compliance Crisis**: 95/120 files (79%) exceed 80-line limit
- **Largest File**: 847 lines (tier-by-tier-validation.md)
- **Average File Size**: 184 lines (target: ≤80 lines)
- **Required Reduction**: ~16,000 lines system-wide

## Priority Classification

### **Tier 1: Massive Files (>400 lines) - URGENT**
1. `tier-by-tier-validation.md` - 847 lines → Target: 80 lines (90% reduction)
2. `principle-compliance-assessment.md` - 608 lines → Target: 80 lines (87% reduction)
3. `refactoring-guide.md` - 510 lines → Target: 80 lines (84% reduction)
4. `33-principle-validation-framework.md` - 510 lines → Target: 80 lines (84% reduction)
5. `composition-patterns-framework.md` - 492 lines → Target: 80 lines (84% reduction)

### **Tier 2: Large Files (200-400 lines) - HIGH**
- `stp-examples-library.md` - 462 lines
- `command-examples-by-tier.md` - 454 lines
- `progressive-disclosure-framework.md` - 437 lines
- `development-principles.md` - 431 lines
- `tier0-pragmatic-technical-simplicity.md` - 412 lines

### **Tier 3: Medium Files (100-200 lines) - MEDIUM**
- Files in 100-200 line range requiring standard compaction
- Apply Level 1-2 compaction techniques
- Convert duplicated content to references

### **Tier 4: Compliant Files (<80 lines) - MAINTAIN**
- 25 files already compliant
- Preserve as reference examples
- Minimal changes required

## Duplication Analysis Priority

### **High Duplication Concepts** (Target for @references)
1. **PTS Framework**: Referenced in 40+ files
2. **Context Economy**: Explained in 25+ files  
3. **Git Workflows**: Duplicated across 20+ files
4. **Agent Deployment**: Repeated in 15+ files
5. **Markdown Standards**: Replicated in 10+ files

### **Authority File Strategy**
- Create technical/* files for each major concept
- Convert duplications to @path/file.md:line-range references
- Establish single source of truth architecture

## Optimization Strategy by Directory

### **docs/frameworks/** (Highest line count)
- Convert to navigation hubs + technical detail files
- Reference-heavy architecture for complex frameworks
- Split large files into focused technical modules

### **docs/core/** (Essential authority)
- Aggressive compaction required
- Maintain authority while reducing redundancy
- Hub pattern: overview + precise technical references

### **docs/implementation/** (Practical guides)
- Convert examples to reference patterns
- Create reusable example library
- Focus on hub-and-spoke access pattern

## Success Metrics
- **File Compliance**: 100% files ≤80 lines (current: 21%)
- **Context Load**: ≤50 lines always-loaded (current: 510 lines)
- **Duplication**: <5% acceptable cross-references (current: ~60%)
- **Information**: Zero unique content loss during optimization

---
**Matrix Principle**: Systematic file classification enables targeted optimization with mathematical precision while preserving information integrity.