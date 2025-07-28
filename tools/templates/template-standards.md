# Template Standards - Core Requirements

**Purpose**: Essential template compliance and structural standards
**Authority**: Level 3 - Core Operations | **Updated**: 2025-07-27 16:35 (Mexico City)
**Lines**: ≤80

## When to Apply (MANDATORY)
**TRIGGER**: File creation, documentation updates, command development, structure modifications
**UNIVERSAL**: All content creation and modification operations

## Core Template Requirements (BLOCKING)

### Header Standards (MANDATORY)
**Required Elements**:
- Title with descriptive purpose
- **Purpose**: Brief functionality description
- **Authority**: Level + category (e.g., "Level 3 - Core Operations")
- **Updated**: YYYY-MM-DD HH:MM (Mexico City)
- **Lines**: Limit specification (≤80 for commands, ≤150 for documents)

### Structure Requirements (MANDATORY)
**Line Limits**: Commands ≤80 lines | Documents ≤100-150 lines | Context economy optimization
**Progressive Disclosure**: Logical hierarchy with clear section breaks
**Information Density**: ≥80% information density | <20% redundancy
**Cross-Reference**: Clear linking to related files and authorities

### Content Standards (MANDATORY)
**English-Only**: Zero tolerance for mixed languages
**Technical Precision**: Actionable content only | Consistent terminology
**Self-Containment**: Complete information within file boundaries
**Authority Traceability**: Clear connection to user-input/ or system authorities

## File Type Specific Standards

### Commands (.md files in export/commands/)
**Length**: ≤80 lines maximum
**Structure**: Purpose → Context → Implementation → Success Criteria
**Self-Contained**: All necessary patterns and logic embedded
**Single Responsibility**: One clear function per command

### Documentation (docs/, rules/)
**Length**: ≤100-150 lines maximum  
**Template**: Header → When to Apply → Core Framework → Implementation → Success Criteria
**Authority Integration**: Clear references to source authorities
**Context Economy**: Optimized information architecture

### Rules (rules/ directory)
**Authority Hierarchy**: Clear level designation and superior authorities
**Enforcement Clarity**: BLOCKING, MANDATORY, REQUIRED levels specified
**Application Scope**: When and how rule applies
**Integration Standards**: How rule connects to broader system

## Quality Gates (BLOCKING)

### Template Compliance Checklist
☐ Header with all required elements present
☐ Line limits respected (≤80 commands, ≤150 documents)
☐ Information density ≥80% achieved
☐ English-only compliance verified
☐ Authority traceability established
☐ Progressive disclosure structure implemented

### Validation Requirements
**BLOCKING**: Template violations prevent file progression
**MANDATORY**: Compliance verification before system integration
**QUALITY**: Consistency checking across related files

## Integration with System

### Authority Chain Compliance
**user-input/PRINCIPLES.md** → **rules/CLAUDE_RULES.md** → **rules/core/** → **implementation**
**Template Enforcement**: All files must align with authority hierarchy

### Cross-System Standards
**Naming Convention**: Apply rules/rules-naming-convention.md
**Context Economy**: Optimize for minimal cognitive load
**User Authority**: Respect Sacred User Space protection protocols

---
**Template Truth**: Essential structural standards ensuring consistent, efficient, and authoritative content creation across all system components.