# Project Governance

**Last Updated: 2025-07-23**
**Authority**: Structure and organization protocols implementing Partnership Protocol

## Directory Authority Hierarchy

### Project Structure Standards
```
ce-simple/
├── docs/vision/             # System direction (absolute authority)
├── docs/core/               # Technical implementation of vision
├── docs/rules/              # Partnership protocol rule modules
├── CLAUDE_RULES.md          # Master partnership protocol (deprecated → docs/rules/)
├── CLAUDE.md                # Project overview and navigation hub
├── commands/                # Essential local commands (3 core commands)
├── export/                  # Global commands + export CLAUDE.md
├── development/             # Development workspace (prototypes, testing)
├── templates/               # Master templates for development
└── automation/              # CI/CD and quality automation
```

### Authority Implementation
- **docs/vision/**: Absolute authority for all system direction decisions
- **docs/core/**: Technical implementation authority for architectural decisions  
- **docs/rules/**: Partnership protocol authority for collaboration standards
- **CLAUDE.md**: Navigation and overview authority for project structure
- **commands/**: Local execution authority for project-specific workflows

## File Management Rules

### Structure Maintenance Standards
- **Structure Integrity**: Keep all files in correct directories according to purpose
- **No File Displacement**: Zero tolerance for files out of designated locations
- **Directory Purpose Clarity**: Each directory maintains clear, focused purpose
- **Clean Organization**: Regular cleanup of temporary or misplaced files

### CLAUDE.md Update Protocol
**CLAUDE.md Update Rules**:
- **Structure Changes**: Update CLAUDE.md immediately when directory structure changes
- **New Component Addition**: Add references to new major components or documentation
- **Navigation Updates**: Ensure navigation paths remain current and functional
- **Cross-Reference Maintenance**: Keep links to related documentation current

### Context Documentation Standards
- **Achievement Documentation**: Document major achievements and milestones for future context
- **Error Learning Capture**: Record errors and their solutions for learning purposes
- **Decision Rationale**: Document reasoning behind major structural decisions
- **Evolution Tracking**: Maintain history of structural changes and their motivations

## Command System Architecture

### Command Boundary Enforcement
- **Global Commands** (export/): Core reusable commands for any project
- **Local Commands** (commands/): Project-specific commands that cannot modify global system
- **Interaction Rule**: Commands reference each other only via slash command calls
- **Self-Contained Principle**: Each command includes all necessary logic and patterns

### Command Reference Standards
- **Slash Command Only**: Commands can only invoke other commands via `/command-name` syntax
- **No File Dependencies**: Commands cannot reference files outside their designated scope
- **Embedded Logic**: All patterns, templates, and logic included inline within commands
- **Boundary Respect**: Local commands cannot modify global system components

## Integration and Cross-Reference Rules

### Documentation Integration Standards
- **No Fragmentation**: Create consolidated context, not scattered information
- **Cross-Reference Requirements**: All major documents must include references to related documents
- **Navigation Flow**: Each document should guide users to relevant next steps
- **Context Linking**: Technical concepts linked to their definitions and explanations

### Rule Update Protocol Implementation
**Continuous Rule Updates**:
- **Insight Capture**: Document new learnings and rules from each interaction
- **Module Integration**: Add new rules to appropriate rule modules based on content
- **Cross-Module Validation**: Ensure new rules don't conflict with existing rule modules
- **Evolution Documentation**: Track rule evolution with timestamp logging

## Quality Assurance and Compliance

### Structure Integrity Enforcement
- **Regular Audits**: Periodic validation of directory structure compliance
- **Automated Checks**: Where possible, implement automated structure validation
- **Violation Correction**: Immediate correction of structure violations when detected
- **Prevention Strategies**: Design workflows to prevent common structure violations

### Governance Metrics
- **Structure Compliance**: 100% of files in correct directories
- **Documentation Currency**: CLAUDE.md and navigation documents always current
- **Command Compliance**: 100% adherence to command boundary rules
- **Cross-Reference Coverage**: All major documents properly linked and referenced

---

**Application**: These governance rules ensure project structure integrity and organization standards. Reference when making structural changes or validating project organization.