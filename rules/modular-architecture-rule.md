# Modular Architecture Rule

**Purpose**: When and how to apply modular system design  
**Authority**: Extracted from docs/decisions/governance/modular-rules-adr.md  
**Trigger**: System design tasks requiring structure & organization  
**Status**: Active | **Lines**: ≤80

## When to Apply Modular Architecture

**Triggers**:
- File exceeds cognitive limits (≤80 lines commands, ≤100 lines docs)
- Mixed content types in single file
- Multiple responsibilities in one component
- Maintenance requires touching unrelated content

**Test**: If changes to A require understanding B → Modularize

## Modular Design Principles

### Focused Responsibility
- Each module handles specific aspect of system
- Clear boundaries reduce confusion & conflicts
- Single purpose per file/component

### Flat Structure Maximum
- Maximum 1 directory level (avoid deep nesting)
- Create directories when first file needed (no empty dirs)
- Active use only (don't create unused structure)

### Size Boundaries
- Commands: ≤80 lines maximum
- Documentation: ≤100 lines maximum  
- Rules: ≤80 lines maximum
- Individual modules: ≤200 lines maximum

## Cross-Module Integration Protocols

### Dependency Management
- Clear, explicit references between modules
- Avoid circular dependencies
- Document integration points

### Authority Hierarchy
- Foundation modules establish principles
- Implementation modules extend principles  
- All modules align with foundation authority

### Integration Testing
- Validate module interactions
- Test in real development scenarios
- Ensure no gaps or contradictions
- Verify complete coverage

## Implementation Strategy

**Phase 1**: Identify module boundaries (responsibility separation)  
**Phase 2**: Extract content into focused modules  
**Phase 3**: Establish cross-references & integration points  
**Phase 4**: Test & validate modular system functionality

## Quality Gates

- Each module serves single, clear purpose
- Integration points documented & tested
- No content duplication across modules
- Maintained cognitive load optimization

---

**🤖 IMPLEMENTATION AGENT**: Apply modular design when system complexity exceeds limits  
**🔍 VALIDATION AGENT**: Verify module boundaries & integration protocols