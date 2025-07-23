# Project Organization Protocol - Structural Intelligence Framework

## 🎯 Purpose
Define canonical project structure and automated maintenance protocols for optimal organization, accessibility, and system intelligence integration.

## 🏗️ CANONICAL STRUCTURE

### Root Directory Organization
```
/project-root/
├── docs/               # Framework definitions and protocols
│   ├── structure/      # Project organization standards (THIS FILE)
│   ├── command/        # Command development standards  
│   ├── documentation/  # Writing and content standards
│   ├── implementation/ # Technical implementation guides
│   ├── quality/        # Validation and metrics frameworks
│   └── workflow/       # Process and automation standards
├── context/            # Learning and discovery documentation  
│   ├── discoveries/    # Session findings and results
│   ├── experience/     # Implementation learnings and feedback
│   ├── patterns/       # Validated behavioral and architectural patterns
│   ├── research/       # External pattern validation and discovery
│   └── workflows/      # Process templates and integration protocols
└── .claude/            # ONLY Claude Code specific configuration
    ├── commands/       # Executable slash commands
    └── settings.local.json  # Personal Claude Code settings
```

## 📋 DIRECTORY RESPONSIBILITIES

### Standards/ - Framework Governance
**Purpose**: System-wide standards, protocols, and rules
**Content**: Normative documentation for consistent system operation
**Access**: Visible, discoverable, team-accessible

#### Subdirectories:
- **structure/**: Project organization and file placement standards
- **command/**: Command development templates and protocols  
- **documentation/**: Writing standards, style guides, content optimization
- **implementation/**: Technical implementation guides and methodologies
- **quality/**: Validation frameworks, metrics, anti-bias protocols
- **workflow/**: Process automation, Git integration, notification standards

### Context/ - Knowledge Repository
**Purpose**: Generated knowledge, patterns, and learning documentation
**Content**: Discovery results, patterns, research consolidation
**Access**: Visible, version-controlled, searchable

#### Subdirectories:
- **discoveries/**: Session results and finding documentation
- **experience/**: User feedback, implementation experience, lessons learned
- **patterns/**: Identified patterns, architectural decisions, solution templates
- **research/**: External research, standards, and reference consolidation
- **workflows/**: Process examples, automation patterns, integration guides

### .claude/ - Tool Configuration
**Purpose**: Claude Code specific configuration and commands
**Content**: Executable commands and tool settings only
**Access**: Hidden directory, tool-specific

#### Contents:
- **commands/**: Slash commands as Markdown files (executable)
- **settings.local.json**: Personal Claude Code configuration

## 🔧 FILE PLACEMENT DECISION TREE

### For New Files:

#### Documentation and Standards:
```
Is it a standard, protocol, or framework?
├─ YES → docs/[category]/
└─ NO → Continue...

Is it learning, discovery, or research?
├─ YES → context/[category]/
└─ NO → Continue...

Is it an executable command?
├─ YES → .claude/commands/
└─ NO → Root directory or project-specific location
```

#### Content Categories:
- **Normative Content** (rules, standards, protocols) → `docs/`
- **Learning Content** (discoveries, patterns, research) → `context/`
- **Tool Configuration** (commands, settings) → `.claude/`

## ⚡ STRUCTURAL VALIDATION FRAMEWORK

### Pre-Command Validation Protocol
**MANDATORY for all commands**:
1. 🏗️ **STRUCTURE-CHECK**: Validate project organization compliance
2. 🔗 **REFERENCE-VERIFY**: Check cross-reference integrity
3. 📏 **SIZE-VALIDATE**: Enforce file size limits (140-200 lines)
4. ⚡ **AUTO-CORRECT**: Fix structural violations automatically

### Validation Levels:

#### Level 1 - Silent Auto-Correction:
- Broken relative path references
- File size compliance (auto-extraction)
- Cross-reference validation and repair

#### Level 2 - Notification + Auto-Correction:
- File placement optimization
- Structural anti-pattern detection
- Progressive disclosure violations

#### Level 3 - User Notification + Recommendation:
- Major structural reorganization needs
- Architecture evolution requirements

## 📊 REFERENCE INTEGRITY STANDARDS

### Cross-Reference Format:
```markdown
- `../docs/[category]/file.md` - Description
- `../context/[category]/file.md` - Description
```

### Validation Requirements:
- **100% Reference Accuracy**: All cross-references must be functional
- **Bidirectional Navigation**: Two-way reference relationships maintained
- **Authority Hierarchy**: Clear source-of-truth designation

## 🎯 COMMAND INTEGRATION PROTOCOLS

### Enhanced Command Pattern:
```markdown
### Structural Validation Protocol
**MANDATORY PRE-EXECUTION**:
1. 🏗️ STRUCTURE-CHECK: Validate project organization
2. 🔗 REFERENCE-VERIFY: Check cross-reference integrity
3. 📏 SIZE-VALIDATE: Enforce size limits  
4. ⚡ AUTO-CORRECT: Fix violations automatically
```

### Commands with Structural Intelligence:
- **`/start`**: Master structural orchestrator
- **`/docs-workflow`**: Documentation structure guardian
- **`/explore-codebase`**: Internal structure analyzer
- **`/capture-learnings`**: Pattern-based structure evolution

## 🚫 PROHIBITED PATTERNS

### File Organization Anti-Patterns:
- **Configuration-Documentation Mixing**: No documentation in `.claude/`
- **Hidden Critical Information**: No team documentation in hidden directories
- **Flat Structure Overload**: No more than 10 files per directory without categorization
- **Reference Fragmentation**: No broken or circular reference chains

### Maintenance Anti-Patterns:
- **Manual Structure Management**: All structure maintenance must be automated
- **Assumption-Based Organization**: All placement decisions must follow decision tree
- **Silent Structural Debt**: All structural issues must trigger automatic correction

## 🔄 EVOLUTION PROTOCOLS

### Structure Evolution Framework:
**Pattern Recognition**: Automatic detection of successful structural patterns
**Standards Update**: Regular evolution of organizational standards based on usage patterns
**Migration Support**: Automated tools for structure transitions

### Migration Procedures:
1. **Analysis**: Identify structural improvements needed
2. **Planning**: Design migration path with minimal disruption
3. **Implementation**: Execute migrations with reference updates
4. **Validation**: Confirm structural integrity post-migration

## 📋 SUCCESS METRICS

### Structural Health Indicators:
- **File Organization Compliance**: 100% files in correct directories
- **Reference Integrity**: 100% working cross-references
- **Size Compliance**: 100% files within limits with auto-extraction
- **Zero Configuration Pollution**: No documentation in `.claude/` outside commands

### Automation Success Metrics:
- **Pre-execution Validation**: 100% commands validate structure
- **Auto-correction Rate**: ≥95% structural issues resolved automatically
- **User Intervention**: <5% issues require manual resolution
- **Structure Evolution**: Quarterly improvements based on usage patterns

---

**CRITICAL**: This organizational protocol MUST be enforced automatically by all commands. Manual structural management is prohibited - all maintenance must be integrated into command workflows for sustainable system health.