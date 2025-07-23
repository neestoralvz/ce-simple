# Active Documentation

**Purpose**: Current specifications and working procedures (≤150 lines per file).

## Content Guidelines

**File Size Limit**: ≤150 lines using progressive disclosure principles
**Content Type**: Active specifications, current procedures, working standards
**Update Frequency**: Regular updates as system evolves

## Organization Patterns

**Naming Convention**: `{topic}-{type}.md`
**Examples**:
- `system-architecture.md` - Current system architecture
- `command-standards.md` - Active command development standards
- `workflow-procedures.md` - Current workflow procedures
- `performance-metrics.md` - Active performance standards

## Progressive Disclosure

**Structure**:
1. **Overview** (≤20 lines) - Essential information
2. **Core Details** (≤80 lines) - Key implementation details  
3. **References** (≤30 lines) - Links to detailed implementation guides
4. **Updates** (≤20 lines) - Recent changes and evolution

**Detail Referencing**:
- Link to `/implementation/` for comprehensive guides
- Reference `/standards/` for authoritative requirements
- Point to `/reference/` for navigation and relationships

## Integration Points

- **Implementation Guides**: `../implementation/{topic}-implementation.md`
- **Standards**: `../standards/{domain}-standards.md`
- **References**: `../reference/{topic}-index.md`
- **Commands**: `../../commands/{category}/{command}.md`

## Quality Criteria

- **Clarity**: Information immediately actionable
- **Currency**: Updated within current development cycle
- **Completeness**: Covers essential aspects within size limit
- **Connectivity**: Clear references to detailed documentation