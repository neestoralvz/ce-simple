# Nomenclature Decision: Rules vs Standards

**Decision Date**: 2025-07-24  
**Authority**: Architectural decision implementing PTS principles  
**Status**: Active

## Decision

**RULES**: Governance protocols for behavior  
**STANDARDS**: Technical specifications for implementation

## Definitions

### Rules
- **Purpose**: Behavior and interaction protocols
- **Location**: `/docs/rules/` (flat)
- **Template**: `/docs/templates/claude-rules-template.md`
- **Limit**: 100 lines maximum
- **Examples**: CLAUDE_RULES.md, communication protocols

### Standards  
- **Purpose**: Technical implementation criteria
- **Location**: `/docs/standards/` (flat, create when first needed)
- **Template**: `/docs/templates/standard-template.md` (to be created)
- **Limit**: 100 lines maximum
- **Examples**: CLAUDE.md Implementation Standard

## Directory Structure

```
docs/
├── rules/          # Existing, 11 files
├── standards/      # Create when first file needed
├── templates/      # Existing
└── governance/     # This file only
```

## Reference Requirements

**MUST consult this before**:
- Creating new documentation
- Choosing between "rule" vs "standard"
- Adding docs/ directories

**Process**:
1. What problem does this solve?
2. Rule (behavior) or Standard (technical)?
3. Does first file of type require new directory?
4. Will it be actively used?

**Prevention**: If purpose unclear → do not create

## Usage Guidelines

### Create Rule When
- Defines behavior protocols
- Governs interactions
- Sets partnership agreements

### Create Standard When  
- Defines technical criteria
- Specifies implementation requirements
- Sets quality thresholds

## Principles Applied

- **Flat structure**: Maximum 1 directory level
- **Create when needed**: No empty directories
- **Single purpose**: Each file solves specific problem
- **Active use**: Only create if actively referenced

---

**Implementation**: Consult before creating documentation to maintain organization and prevent file proliferation.