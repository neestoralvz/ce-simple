# Context Management Framework

**Purpose**: Standards for line-level references and selective imports
**Authority**: Context economy and precision requirements
**Usage**: Apply when creating references or importing content

## Line-Level Reference Standards

### Precision Requirements
**Exact Line Targeting**: Use `@docs/path/file.md:15-23` format for specific content
**Single Concept Rule**: One reference per distinct concept or procedure
**Context Boundaries**: Reference complete logical units (full procedures, complete examples)
**Range Specifications**: Use ranges (15-23) for multi-line concepts, single lines (42) for specific points

### Reference Granularity Guidelines
**Micro-References (1-3 lines)**: Specific definitions, single criteria, brief examples
**Macro-References (4-15 lines)**: Complete procedures, validation checklists, implementation steps
**Section References (16+ lines)**: Major concepts requiring full context understanding

## Import Decision Matrix

### Full Document Import Criteria
**Apply When**:
- Daily use tools requiring complete understanding
- Core methodology creation needing full framework context
- Complex interdependent concepts where partial import loses meaning
- Framework understanding requiring complete mental model

### Selective Line Import Criteria  
**Apply When**:
- Specific procedures can function independently
- Technical specifications are self-contained
- Validation criteria are clearly bounded
- Implementation details don't require broader context

### Reference-Only Criteria
**Apply When**:
- Content used infrequently (monthly or less)
- Historical documentation for context only
- Extended examples serving illustrative purpose only
- Complex technical details supporting but not essential

## Context Economy Optimization

### Token Efficiency Rules
**Minimize Imports**: Import smallest functional unit that preserves comprehension
**Batch Related Lines**: Group related concepts in single reference ranges
**Avoid Duplication**: Never import same content through multiple references
**Strategic Placement**: Place imports at decision points where content is immediately needed

### Import Timing Guidelines
**Session Start**: Core decision support framework (always loaded)
**Task Triggered**: Conditional imports based on specific work type
**Just-in-Time**: Import specific procedures when about to execute
**Validation Phase**: Import quality criteria when validating work

## Reference Format Standards

### Syntax Requirements
**File References**: `@docs/category/filename.md` (full file)
**Line References**: `@docs/category/filename.md:42` (single line)
**Range References**: `@docs/category/filename.md:15-23` (line range)
**Section References**: `@docs/category/filename.md#section-name` (markdown section)

### Context Preservation
**Sufficient Context**: Ensure referenced lines make sense without broader file context
**Logical Boundaries**: Respect conceptual boundaries when defining line ranges
**Cross-Reference Integrity**: Maintain reference accuracy when files are modified
**Update Responsibility**: Verify line references remain accurate after edits

## Implementation Guidelines

### Decision Workflow
1. **Identify Content Need**: What specific information is required?
2. **Assess Scope**: Single concept, procedure, or framework understanding?
3. **Apply Decision Matrix**: Full import, selective lines, or reference-only?
4. **Format Reference**: Apply precise line-level syntax
5. **Validate Context**: Ensure imported content maintains comprehension

### Quality Validation
**Reference Accuracy**: Line numbers point to correct content
**Context Sufficiency**: Imported lines provide adequate understanding
**Economy Efficiency**: No unnecessary content imported
**Maintenance Feasibility**: References remain manageable during file updates

---

**Core Principle**: Import precisely what's needed, when it's needed, in the smallest functional unit that preserves understanding and enables effective action.