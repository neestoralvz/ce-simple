# Nomenclature Rule

**Purpose**: Naming and categorization standards for consistent system organization  
**Authority**: Extracted from docs/decisions/governance/nomenclature-decision.md  
**Trigger**: Creating documentation, organizing files, establishing structure  
**Status**: Active | **Lines**: ≤80

## Content Classification Standards

### Rules (Governance Protocols)
**Purpose**: Behavior and interaction protocols
**Location**: `rules/` (flat structure)
**Format**: `topic-rule.md`
**Limit**: ≤80 lines maximum
**Examples**: partnership-protocol, communication-rules, modular-architecture-rule

### Standards (Technical Specifications)  
**Purpose**: Technical implementation criteria
**Location**: `docs/standards/` (create when first needed)
**Format**: `topic-standard.md`
**Limit**: ≤100 lines maximum
**Examples**: CLAUDE.md implementation standard, command development standard

### Templates (Reusable Patterns)
**Purpose**: Consistent structure and format guides
**Location**: `docs/templates/`
**Format**: `topic-template.md`
**Examples**: rule-template, command-template, documentation-template

## Naming Convention Standards

### File Naming: topic-type.md
**Pattern**: `[topic]-[type].md` (lowercase, hyphenated)
**Examples**:
- `modular-architecture-rule.md`
- `documentation-standard.md`
- `command-template.md`

### Directory Structure
**Principle**: Flat structure maximum (≤1 level deep)
**Create**: Only when first file needed (no empty directories)
**Organization**: By function, not arbitrary categorization

## Decision Process

**Before creating documentation**:
1. What problem does this solve?
2. Rule (behavior) or Standard (technical) or Template (pattern)?
3. Does first file of type require new directory?
4. Will it be actively used?

**Prevention**: If purpose unclear → do not create

## Quality Standards

### Active Use Only
- Only create files that will be actively referenced
- Remove unused or outdated files
- Maintain clear purpose for each file

### Single Purpose
- Each file solves specific problem
- Avoid mixed content types
- Clear scope boundaries

### Cognitive Optimization
- Respect line limits (rules ≤80, standards ≤100)
- Direct, technical language only
- Maximum value density

---

**🤖 IMPLEMENTATION AGENT**: Apply nomenclature standards when creating new documentation  
**🔍 VALIDATION AGENT**: Verify naming compliance & content classification accuracy