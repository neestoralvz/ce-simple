# Command Management Comprehensive Protocol

**Purpose**: Complete command creation, review, and placement governance ensuring strategic value and Claude Code compatibility  
**Authority**: Unified command governance combining review methodology and placement protocols  
**Updated**: 2025-07-27 14:30 (Mexico City) | **Status**: Active | **Lines**: ≤80

## When to Apply
**IF command creation/management** → New command development, modification, library expansion, workflow automation
**IF creating/managing commands** → ALL executable commands placement and location governance
**IF command not recognized** → Command discovery and system arsenal scanning protocols

## Command Review Protocol (MANDATORY)

### 4-Phase Review: INVENTORY → ANALYZE → JUSTIFY → APPROVE
#### Phase 1: INVENTORY
**Complete analysis**: Comprehensive scan of export/commands/ directory structure (86+ commands, 15 categories)
**Functional mapping**: Existing command capabilities | Workflow coverage analysis | Gap identification
**Overlap prevention**: Zero tolerance for functional duplication across command library

#### Phase 2: ANALYZE  
**Automated similarity detection**: Command descriptions and functionality comparison
**Manual strategic analysis**: Command purpose and user workflow integration assessment
**Efficiency assessment**: Proposed vs existing solutions with duplicate prevention protocols

#### Phase 3: JUSTIFY
**Unique value proposition**: No existing command provides equivalent functionality
**Clear workflow gap**: Creates user friction or inefficiency without solution
**Strategic necessity**: Command library completeness with measurable user benefit quantification

#### Phase 4: APPROVE
**Technical review**: Implementation feasibility with strategic library coherence
**User experience review**: Workflow integration assessment | Final governance authority approval
**Blocking enforcement**: No command creation without full review approval completion

## Command Placement Standards (MANDATORY)

### Location Framework (BLOCKING)
**Executable Commands**: MUST be in `.claude/commands/` for Claude Code recognition and direct execution
**Library Commands**: MAY exist in `export/commands/` as reference library and template repository
**No Duplication**: Commands cannot exist in both locations simultaneously | Clear authority designation
**Migration Path**: Commands move from export library to active directory for deployment

### Directory Architecture (MANDATORY)
**`.claude/commands/` (Active)**:
- Executable commands recognized by Claude Code with direct Task Tool integration
- Maximum 10-15 commands for context economy optimization
- Self-contained with embedded logic and patterns for standalone operation

**`export/commands/` (Library)**:
- Reference library (86+ commands in 15 categories) for templates and development patterns
- Historical command versions with cross-project command sharing capability

## Implementation Standards (BLOCKING)

### Activation Process (MANDATORY)
1. **Review Completion**: Pass all 4 phases of review protocol before creation
2. **Select/Create Command**: Choose from export library or create following review approval
3. **Place in Active**: Copy to `.claude/commands/` with project-specific customization
4. **Validate Recognition**: Ensure Claude Code recognition via `/command-name` testing
5. **Library Management**: Remove from export if no longer needed as template

### Quality Requirements (BLOCKING)
**Recognition Test**: Command must be callable via `/command-name` without errors
**Self-Containment**: All logic embedded inline (sub-agents cannot access external files)
**Strategic Value**: Measurable user benefit with clear workflow gap resolution
**Context Economy**: Active directory ≤80 lines per command with maximum efficiency

## Success Criteria
**Review Excellence**: All new commands pass complete 4-phase review protocol
**Placement Compliance**: 100% executable commands in correct locations with clear authority
**Strategic Value**: Zero functional duplication with demonstrated unique workflow benefits
**System Integration**: Claude Code recognition with seamless Task Tool integration

---

**Command Authority**: This comprehensive protocol ensures strategic command development through unified review and placement governance.