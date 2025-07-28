# CLAUDE.md Writing Standards

**Authority**: System architecture | **Purpose**: Mandatory standards for CLAUDE.md file creation and maintenance | **Limit**: ≤80 lines

## Core Requirements

### Mathematical Limits (Non-Negotiable)
**Maximum Lines**: ≤80 total lines (context economy enforcement)
**Essential @ Imports**: Exactly 2 files only: rules/CLAUDE_RULES.md and conditional-loading-protocols.md
**Combined Load**: CLAUDE.md + rules/CLAUDE_RULES.md + conditional-loading-protocols.md ≤150 lines total
**Validation**: `wc -l CLAUDE.md` must return ≤80

### Three-Section Architecture (Mandatory)
1. **Essential Context** - @ imports for critical system understanding and user authority reference
2. **Conditional Documentation Navigation** - READ syntax with line ranges for documentation access only
3. **Context Navigation** - Directory links for exploration

## Syntax Standards

### @ Import Usage (CLAUDE.md Only)
**Essential Context**: Only `@rules/CLAUDE_RULES.md` and `@rules/conditional-loading-protocols.md`
**Mandatory Language**: Must include **STRICT MANDATORY** for rules/CLAUDE_RULES.md and **CONDITIONAL MANDATORY** for conditional-loading-protocols.md
**Criteria**: Partnership protocol and conditional loading system only
**Limit**: Exactly 2 @ imports (no more, no less)

### Reference Syntax (All Other Content)
**README.md Reference**: `**System Information**: [README.md](README.md) - Description` (link format, not @ import)
**Conditional Instructions**: `READ docs/path/file.md:lines` (no @ prefix)
**Navigation Links**: `[Description](docs/path/)` for directories
**File References**: `[Title](docs/path/file.md)` for documents

## Content Rules

### Header Requirements
```markdown
# CLAUDE.md - Project Name

**REQUIRED**: READ rules/when/standards-claude-md-conditional.md BEFORE any modifications to this file
**Updated**: YYYY-MM-DD HH:MM (Mexico City) | **Authority**: user-input/ (Sacred User Space)
```

### Section Content Standards
**Essential Context**: 
- @ imports: Only rules/CLAUDE_RULES.md and conditional-loading-protocols.md with **STRICT MANDATORY** and **CONDITIONAL MANDATORY** enforcement language
- Reference: README.md as **System Information** link (not @ import) with comprehensive system description
- Authority: user-input/ as **SACRED ABSOLUTE AUTHORITY** with override specification
**Conditional Documentation Navigation**: Documentation-specific READ commands with line ranges (no rules references)
**Context Navigation**: Directory-level navigation using standard markdown links

### Prohibited Content
**No Implementation Details**: Reference external files only
**No Examples**: Link to example files instead
**No Redundancy**: Single source of truth principle
**No Mixed Language**: English only throughout

## Validation Framework

### Compliance Checklist
- [ ] Total lines ≤80 (mathematical requirement)
- [ ] Header references this rule file
- [ ] Three-section architecture implemented
- [ ] @ imports exactly 2: rules/CLAUDE_RULES.md and conditional-loading-protocols.md
- [ ] All conditional instructions use READ syntax
- [ ] Navigation uses standard markdown links
- [ ] No implementation details included
- [ ] English-only content
- [ ] Related files updated: rules/CLAUDE_RULES.md, conditional-loading-protocols.md, README.md consistent with changes

### Quality Gates
**Line Count**: `wc -l CLAUDE.md` ≤80
**@ Import Count**: `grep "^@" CLAUDE.md | wc -l` = 2
**Structure Validation**: All 3 sections present and properly labeled
**Reference Integrity**: All linked files exist and are accessible
**Related Files Consistency**: rules/CLAUDE_RULES.md, conditional-loading-protocols.md, and README.md reflect current CLAUDE.md structure

## Integration Requirements

### Template Compliance
**Base Template**: `tools/templates/claude-md-template.md`
**Rule Integration**: This file governs template usage for CLAUDE.md
**Authority Chain**: rules/ → templates/ → implementation

### System Integration
**Conditional Loading**: Must integrate with `rules/conditional-loading-protocols.md`
**Context Economy**: Must comply with `docs/core/05-per-performance/per-context-economy.md`
**Navigation System**: Must support `docs/core/06-inf-infrastructure/inf-navigation-system.md`

### Supporting Rules Integration
**Context Economy Validation**: Apply `rules/context-economy-enforcement.md:20-30` for file length thresholds
**Writing Standards Framework**: Follow `rules/writing-standards-protocols.md:18-35` for documentation quality
**Communication Standards**: Comply with `rules/communication-standards-protocols.md:12-20` for language requirements
**Template Compliance**: Validate against `rules/template-usage-protocols.md:10-25` for structural requirements
**Content Classification**: Apply `rules/nomenclature-rule.md:8-25` for proper content categorization

## Automatic Coherence Validation (🛑 MANDATORY)

### Auto-Validation Process
**TRIGGER**: ANY CLAUDE.md update request
**AUTO-EXECUTE**: Automatically read and validate all 4 core files:

1. **Auto-read CLAUDE.md** - Current structure and navigation patterns
2. **Auto-read rules/CLAUDE_RULES.md** - Authority hierarchy and partnership protocol  
3. **Auto-read rules/conditional-loading-protocols.md** - Conditional loading patterns
4. **Auto-read README.md** - Architecture descriptions and system overview

### Automatic Coherence Checkpoints (ALL Auto-Validated)
**Authority Hierarchy Alignment**: Auto-verify rules/CLAUDE_RULES.md authority chain ↔ CLAUDE.md Section 1 references
**Navigation Pattern Consistency**: Auto-verify conditional-loading-protocols.md patterns ↔ CLAUDE.md Section 2 READ commands
**Architecture Description Sync**: Auto-verify README.md "Three-Section CLAUDE.md Architecture" ↔ actual CLAUDE.md structure
**Version/Date Consistency**: Auto-verify updated dates align across all modified files
**Line Count Compliance**: Auto-verify combined CLAUDE.md + rules/CLAUDE_RULES.md + conditional-loading-protocols.md ≤150 lines

### Integrated Validation Framework
```markdown
## CLAUDE.md Update Protocol (Automatic)
1. Auto-execute: Read all 4 core files
2. Auto-validate: All coherence checkpoints
3. Auto-report: Alignment status and any issues
4. Proceed: Only if all validations pass automatically
```

**AUTOMATIC STANDARD**: All coherence checkpoints auto-validate before any CLAUDE.md modifications proceed.

## Related Files Update Requirements

### Mandatory Co-Updates
When CLAUDE.md is modified, these related files MUST also be updated for consistency:

**rules/CLAUDE_RULES.md Updates Required When:**
- Line limits or section counts change
- Authority hierarchy is modified
- Essential Context imports are altered
- Navigation structure changes

**rules/conditional-loading-protocols.md Updates Required When:**
- Conditional loading patterns change
- New documentation navigation paths are added
- READ syntax or reference patterns are modified

**README.md Updates Required When:**
- Architecture description needs updating (currently shows "Three-Section CLAUDE.md Architecture")
- Authority hierarchy changes
- System overview or navigation patterns are modified

### Consistency Validation
**Cross-Reference Check**: All files referencing CLAUDE.md structure must reflect current implementation
**Authority Alignment**: Hierarchy described in rules/CLAUDE_RULES.md must match CLAUDE.md structure
**Navigation Accuracy**: conditional-loading-protocols.md must align with CLAUDE.md Section 2 patterns

---

**Enforcement**: This rule is mandatory for all CLAUDE.md creation and maintenance activities