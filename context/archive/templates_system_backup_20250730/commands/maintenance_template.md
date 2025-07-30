# Template: Maintenance Commands

**Template última edición: 29/07/2025** | Template for /maintenance: system management commands

## Maintenance Command Structure

```markdown
# /maintenance:name - [Maintenance Function]

**DD/MM/YYYY** | [Maintenance purpose]

## DO
- [Primary maintenance operation 1]
- [Primary maintenance operation 2]
- [System health validation requirements]
- [Safety and backup protocols]

## DON'T
- [System integrity violations 1]
- [System integrity violations 2]
- [Common maintenance mistakes to avoid]
- [Anti-patterns that compromise system stability]

## Context
- [System components affected by maintenance]
- [Dependencies and integration requirements]
- [Safety protocols and rollback procedures]
- [Validation criteria for maintenance success]

## Next Action
- **Automatic**: /actions:git (after system changes requiring commit)
- **Recommended**: /maintenance:validate (for system health verification)
- **Context**: Return to normal operations vs escalate issues
```

## Maintenance Categories

### System Health (maintain, cleanup)
**Purpose**: Monitor, optimize, and maintain overall system health and performance

**DO Pattern**:
- Perform systematic health checks before and after operations
- Apply established protocols for system optimization
- Document maintenance activities and results
- Validate system integrity after maintenance operations

**DON'T Pattern**:
- Perform maintenance without proper system backup or safety measures
- Skip validation of maintenance operation results
- Ignore system dependencies when making changes
- Eliminate archive/conversations/ without processing verification
- Delete conversation content without user confirmation
- Compromise system stability for performance gains

### Content Management (archive, organize)
**Purpose**: Manage information architecture, organization, and lifecycle

**DO Pattern**:
- Follow established information architecture principles
- Maintain content relationships and linking integrity
- Preserve content traceability and historical context
- Apply consistent organization standards
- Verify conversation processing status before elimination
- Obtain user confirmation for archive operations

**DON'T Pattern**:
- Reorganize content without preserving existing references and links
- Archive content without proper metadata and accessibility
- Break content relationships during organization activities
- Apply inconsistent organization standards across similar content
- Eliminate conversations without processing verification
- Delete archive content without user authority

### Configuration Management (update, configure)
**Purpose**: Manage system configuration, settings, and environmental consistency

**DO Pattern**:
- Follow change management protocols for configuration updates
- Validate configuration changes against system requirements
- Document configuration changes and rationale
- Test configuration changes in appropriate environments

**DON'T Pattern**:
- Make configuration changes without proper validation
- Skip documentation of configuration modifications
- Apply configuration changes that conflict with system architecture
- Ignore configuration dependencies and integration requirements

## Context Section Guidelines

### For System Health
```markdown
## Context
- System monitoring and diagnostic tools
- Health check criteria and performance baselines
- Backup and recovery procedures
- Integration with system architecture components
```

### For Content Management
```markdown
## Context
- Information architecture principles and standards
- Content lifecycle management policies
- Linking and reference integrity requirements
- Archive and retrieval system integration
```

### For Configuration Management
```markdown
## Context
- Configuration management protocols and standards
- Environment consistency requirements
- Dependency mapping and impact analysis
- Change validation and rollback procedures
```

## Next Action Patterns

### System Health Patterns
```markdown
## Next Action
- **Automatic**: /actions:git (after system changes)
- **Recommended**: /maintenance:validate (for health verification)
- **If issues found**: /workflows:debug (for problem resolution)
```

### Content Management Patterns
```markdown
## Next Action
- **Automatic**: Update documentation links after reorganization
- **Recommended**: /maintenance:validate (for link integrity check)
- **If content conflicts**: /roles:partner (for organization decision)
```

### Configuration Management Patterns
```markdown
## Next Action
- **Automatic**: /maintenance:validate (after configuration changes)
- **Recommended**: /workflows:test (for configuration validation)
- **If conflicts detected**: /workflows:debug (for resolution)
```

## Template Usage Instructions

1. **Identify maintenance category** (system health/content/configuration)
2. **Define safety protocols** and validation requirements
3. **Specify system impact** and dependency considerations
4. **Document rollback procedures** for maintenance operations
5. **Design validation logic** for maintenance success verification

---
**Authority Source**: Maintenance command analysis + system management patterns
**Template References**: context/architecture/templates/README.mduniversal_do_dont_template.md