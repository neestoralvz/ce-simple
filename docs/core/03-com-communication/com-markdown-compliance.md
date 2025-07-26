# Markdown Compliance - Technical Authority

**Updated**: 2025-07-24 | **Authority**: Complete markdown standards & line limits | **Limit**: 80 lines
**Purpose**: Single source of truth for markdown compliance across system

## Line Limit Standards (Lines 5-20)
### **Strict Limits (Non-negotiable)**
- **Documentation Files**: ≤80 lines maximum
- **CLAUDE.md**: ≤50 lines maximum  
- **Command Files**: ≤80 lines maximum
- **Technical Authority Files**: ≤80 lines (this file demonstrates)

### **Three-Layer Architecture**
- **Foundation Layer**: ≤50 lines (core concepts only)
- **Implementation Layer**: ≤100 lines (conditional loading)
- **Validation Layer**: ≤100 lines (quality gates)

### **Enforcement Protocol**
- Pre-commit validation required
- Automated line count checking
- Quality gate blocking for violations
- No exceptions without vision-level approval

## Compaction Techniques (Lines 21-45)
### **Level 1: Basic Compaction**
- **Pipe Headers**: `## Overview | Purpose | Scope`
- **Dense Lists**: Multiple concepts per line with `|` separation
- **Arrow Notation**: `Input → Process → Output` patterns
- **Reference Format**: `@file.md:15-30` for precision linking

### **Level 2: Advanced Compaction**  
- **Inline Examples**: Code/examples within text lines
- **YAML-style**: Structured data in compact format
- **Mathematical Notation**: Formulas and symbolic representation
- **Abbreviated Headers**: `###` reduced to essential keywords

### **Level 3: Extreme Compaction**
- **Multi-concept Lines**: 2-3 related concepts per line
- **Context Compression**: Maximum information density
- **Symbol Heavy**: Unicode symbols for common concepts
- **Strategic Elimination**: Remove non-essential elaborations

## Structure Standards (Lines 46-65)
### **Required Elements**
- **Header**: Title + metadata (Updated, Authority, Limit)
- **Purpose Statement**: Clear objective within first 5 lines
- **Hierarchical Organization**: Logical section progression
- **Authority Footer**: Reference to source authority if applicable

### **Forbidden Elements**
- **Marketing Language**: No "amazing", "incredible", "revolutionary"
- **Spanish Content**: English-only documentation
- **Redundant Explanations**: Single source of truth principle
- **Excessive Examples**: One example maximum per concept

### **Formatting Rules**
- **Bold Emphasis**: `**Key Terms**` for important concepts  
- **Code Blocks**: Minimal, essential examples only
- **Reference Links**: `[descriptive text](path/file.md)` format
- **Line Numbers**: Stable organization for @file.md:line referencing

## Validation Criteria (Lines 66-80)
### **Automated Checks**
```bash
validate_markdown() {
    lines=$(wc -l < "$file")  
    if [ $lines -gt 80 ]; then echo "❌ Exceeds limit: $lines"; fi
    if grep -q "amazing\|incredible" "$file"; then echo "❌ Marketing language"; fi
    if ! head -5 "$file" | grep -q "**Updated**"; then echo "⚠️ Missing metadata"; fi
}
```

### **Manual Review**
- **Information Density**: Maximum value per line
- **Clarity**: Immediate comprehension possible
- **Completeness**: All necessary information present
- **Consistency**: Follows established patterns

### **Quality Gates**
- Line count validation (blocking)
- Language compliance check (blocking)  
- Structure validation (warning)
- Content density assessment (advisory)

---
**Authority**: This file is the single source of truth for markdown compliance across entire system.