# Current Project Structure

**Updated**: 2025-07-26 | **Authority**: Live system structure | **Status**: Post ultra-simplification

## Core System Architecture

```
ce-simple/
├── CLAUDE_RULES.md               # Partnership protocol + Think×4 mandatory
├── CLAUDE.md                     # System navigation hub (≤50 lines)
├── .claude/                      # Claude Code integration
│   ├── commands/                # Executable commands (4 core commands)
│   │   ├── docs-audit.md       # Documentation system audit
│   │   ├── explore-codebase.md # Codebase exploration
│   │   ├── init-project.md     # Project initialization  
│   │   ├── start.md           # Project analysis and guidance
│   │   └── README.md          # Commands documentation
│   └── settings.local.json    # Claude Code settings
├── tools/                       # Development tools (moved from docs/)
│   ├── templates/              # Document + command templates
│   │   ├── claude-md-template.md
│   │   ├── command-template.md
│   │   └── ...
│   ├── vdd-config.json        # VDD configuration
│   ├── vdd-dashboard.sh       # Dashboard utilities
│   └── vdd-metrics-dashboard.py
├── docs/                       # Documentation system (3 core directories)
│   ├── core/                  # Technical authority (consolidated)
│   │   ├── pts-framework-consolidated.md # PTS framework authority
│   │   ├── command-governance-framework.md # Governance
│   │   ├── development-principles.md # Development standards
│   │   ├── performance-framework.md # Performance metrics
│   │   └── ... (70 consolidated files)
│   ├── context/               # System knowledge hub
│   │   ├── patterns/         # Validated patterns
│   │   ├── examples/         # Working examples
│   │   ├── implementation/   # Implementation guides
│   │   ├── methodologies/    # Research methods
│   │   └── README.md        # Context navigation
│   ├── decisions/            # Strategic direction
│   │   ├── vision/          # User vision (from docs/vision/)
│   │   ├── governance/      # Architectural decisions
│   │   └── README.md       # Decisions navigation
│   ├── .archive/            # Historical content (hidden)
│   └── README.md           # Documentation hub
├── user-input/              # Sacred User Space (unchanged)
│   ├── vision/             # Pure user conceptual input
│   ├── technical-requirements/ # User technical specifications
│   │   ├── think-by-four-mandatory.md # Think×4 requirement
│   │   └── ...
│   ├── evolution/          # User sessions and framework evolution
│   └── context/           # User feedback
├── export/                 # Global command system (86 commands)
│   ├── commands/          # 15 categories (00-14)
│   └── CLAUDE.md         # Export system overview
├── rules/                 # Conditional loading rules
└── scripts/              # Automation scripts
```

## Directory Functions

### Essential System Files
- **CLAUDE_RULES.md**: Partnership protocol + Think×4 mandates + authority hierarchy
- **CLAUDE.md**: Navigation entry point with @ imports + essential context

### Core Implementation (`.claude/`)
- **commands/**: Self-contained Task Tool commands using Claude Code convention
- **settings.local.json**: Claude Code local configuration

### Development Tools (`tools/`)
- **templates/**: Reusable patterns for commands, docs, rules (moved from docs/)
- **vdd-config.json**: VDD system configuration
- **Dashboard utilities**: System monitoring and metrics

### Documentation Architecture (`docs/`) - Ultra-Simplified
- **core/**: Consolidated technical authority (standards + rules + technical + protocols)
- **context/**: System knowledge (patterns + examples + implementation + methodologies) 
- **decisions/**: Strategic direction (vision + governance)
- **.archive/**: Historical content (hidden from navigation)

### Sacred User Space (`user-input/`)
- **vision/**: Pure user conceptual framework
- **technical-requirements/**: User technical specifications including Think×4 mandates
- **evolution/**: User sessions and framework development
- **context/**: User feedback and assessment

### Global Command System (`export/`)
- **commands/**: 86 commands organized in 15 categories for global deployment
- **CLAUDE.md**: Export system documentation

## Key Changes from Previous Structure

### Eliminated Directories (8 total)
- **docs/analysis/**: Content consolidated into core/
- **docs/frameworks/**: Merged into core/  
- **docs/validation/**: Integrated into core/
- **docs/standards/**: Moved to core/
- **docs/rules/**: Consolidated into core/
- **docs/technical/**: Merged into core/
- **docs/protocols/**: Moved to core/
- **docs/templates/**: Relocated to tools/

### Relocated Content
- **commands/** → **.claude/commands/** (Claude Code convention)
- **docs/templates/** → **tools/templates/** (tools in project root)
- **docs/vision/** → **docs/decisions/vision/** (strategic grouping)
- **docs/governance/** → **docs/decisions/governance/** (strategic grouping)
- **docs/archive/** → **docs/.archive/** (hidden from navigation)

### New Integrations
- **Think×4 perpetual analysis**: Mandatory in user-input/, CLAUDE_RULES.md, core/PTS framework
- **Unified technical authority**: All standards, rules, protocols in core/
- **Conceptual organization**: Context (learned) vs Decisions (strategic) vs Core (technical)

## Success Metrics

### Simplification Achievement
- **77% directory reduction**: 13 → 3 core docs/ directories
- **100% content preservation**: All unique content consolidated without loss
- **Authority consolidation**: Single source technical truth in core/
- **Navigation optimization**: ≤60 seconds to find any content

### Functional Integration
- **Claude Code compliance**: Commands in .claude/commands/
- **Think×4 integration**: Perpetual analysis mandated at all levels
- **Sacred User Space**: user-input/ completely preserved
- **Tools accessibility**: Direct access from project root

---

**Structure Principle**: Maximum simplicity with complete functionality - user focus on vision and execution, system handles complexity.