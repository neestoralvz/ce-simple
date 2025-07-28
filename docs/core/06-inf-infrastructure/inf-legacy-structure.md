# Project Structure - ce-simple VDD Framework

**Generated with**: `tree . -I '.git|node_modules|.DS_Store|backups|planning|handoffs' -L 3 -a`  
**Updated**: 2025-07-26 | **Status**: Post ultra-simplification structure

## Complete Directory Structure

```
ce-simple/
├── .claude/                      # Claude Code Integration
│   ├── commands/                # Core executable commands (4 commands)
│   │   ├── docs-audit.md       # Documentation system audit & validation
│   │   ├── explore-codebase.md # Intelligent codebase exploration
│   │   ├── init-project.md     # Project initialization with git setup
│   │   ├── README.md          # Commands system documentation
│   │   └── start.md           # Project analysis and guidance
│   └── settings.local.json    # Claude Code local configuration
├── .github/                     # GitHub integration
│   ├── README.md              # GitHub documentation
│   └── workflows/             # CI/CD workflows
│       ├── deploy-docs.yml    # Documentation deployment
│       └── docs.yml          # Documentation building
├── .githooks/                   # Git hooks
│   └── pre-commit             # Pre-commit validation
├── rules/CLAUDE_RULES.md             # Partnership protocol + Think×4 mandates
├── CLAUDE.md                   # System navigation hub (≤80 lines)
├── docs/                       # Documentation system (ultra-simplified)
│   ├── .archive/              # Historical content (hidden)
│   │   └── pts-original/      # Original PTS framework files
│   ├── context/               # System knowledge hub
│   │   ├── examples/          # Working examples and applications
│   │   ├── implementation/    # Implementation guides and real usage
│   │   ├── methodologies/     # Research methods and analysis frameworks
│   │   ├── patterns/          # Validated patterns and communication protocols
│   │   └── README.md         # Context navigation hub
│   ├── core/                  # Technical authority (consolidated)
│   │   ├── pts-framework-consolidated.md    # PTS framework authority
│   │   ├── command-governance-framework.md  # Command governance
│   │   ├── development-principles.md        # Development standards
│   │   ├── performance-framework.md         # Performance metrics
│   │   ├── context-economy-metrics.md       # Context optimization
│   │   ├── progressive-disclosure-framework.md # UI/UX patterns
│   │   └── ... (70 consolidated authority files)
│   ├── decisions/             # Strategic direction
│   │   ├── governance/        # Architectural decisions and records
│   │   ├── README.md         # Decisions navigation
│   │   └── vision/           # Complete user vision and philosophy
│   └── README.md             # Documentation hub navigation
├── export/                     # Global command system (86 commands)
│   ├── CLAUDE.md             # Export system overview
│   └── commands/             # Global commands in 15 categories
│       ├── 00-core/          # Foundation operations
│       ├── 01-discovery/     # Discovery and exploration
│       ├── 02-planning/      # Planning and strategy
│       ├── 03-analysis/      # Analysis and assessment
│       ├── 04-execution/     # Execution and implementation
│       ├── 05-validation/    # Validation and testing
│       ├── 06-documentation/ # Documentation creation
│       ├── 07-maintenance/   # Maintenance and optimization
│       ├── 08-learning/      # Learning and knowledge capture
│       ├── 09-git/          # Git workflow automation
│       ├── 10-standards/    # Standards and quality
│       ├── 11-meta/         # Meta-operations
│       ├── 12-math/         # Mathematical operations
│       ├── 13-search/       # Search and discovery
│       └── 14-utils/        # Utility operations
├── mkdocs.yml                 # Documentation site configuration
├── README.md                  # Project overview and entry point
├── rules/                     # Conditional loading rules (rules/CLAUDE_RULES.md)
│   ├── architecture-decision-protocols.md
│   ├── content-auditing-methodology.md
│   ├── development-workflow-protocols.md
│   ├── orchestration-protocols.md
│   ├── planning-methodology.md
│   ├── README.md            # Rules system navigation
│   ├── transparency-requirements.md
│   └── validation-protocols.md
├── scripts/                   # Automation and validation scripts
│   ├── setup-hooks.sh       # Git hooks setup
│   ├── validate-coherence.sh # System coherence validation
│   └── validate-implementation-mandatory.sh # Implementation validation
├── site/                      # Generated documentation site (MkDocs)
│   ├── index.html           # Site entry point
│   ├── core/                # Core documentation pages
│   ├── context/             # Context documentation
│   ├── decisions/           # Decisions documentation
│   └── ... (generated content)
├── tools/                     # Development tools and utilities
│   ├── scripts/             # Utility scripts and automation
│   ├── templates/           # Development templates (moved from docs/)
│   │   ├── claude-md-template.md      # CLAUDE.md template
│   │   ├── claude-rules-template.md   # rules/CLAUDE_RULES.md template
│   │   ├── cognitive-load-guidelines.md # Information density guidelines
│   │   ├── command-template.md        # Command structure template
│   │   ├── foundation-command-patterns.md # Common command patterns
│   │   ├── README.md                  # Templates navigation
│   │   └── three-layer-methodology-template.md # Methodology template
│   ├── config/              # Configuration files
│   │   └── vdd-config.json  # VDD system configuration
│   ├── dashboards/          # Monitoring and metrics tools
│   │   ├── vdd-dashboard.sh # System dashboard utilities
│   │   └── vdd-metrics-dashboard.py # Performance metrics dashboard
└── user-input/               # Sacred User Space (protected)
    ├── context/             # User feedback and assessment
    │   └── README.md       # Context feedback system
    ├── evolution/           # User sessions and framework development
    │   ├── 2025-07-25-23-39-vdd-migration-vision.md
    │   └── 2025-07-26-00-25-framework-refinements-complete.md
    ├── README.md           # Sacred User Space authority
    ├── technical-requirements/ # User technical specifications
    │   ├── coherence-validation-methodology-user.md
    │   ├── command-review-methodology-user.md
    │   ├── content-auditing-methodology-user.md
    │   ├── documentation-first-methodology-user.md
    │   ├── execution-strategies-user.md
    │   ├── implementation-verification-mandatory-user.md
    │   ├── README.md       # Technical requirements navigation
    │   ├── root-directory-auditing-methodology-user.md
    │   ├── technical-architecture-user.md
    │   ├── think-by-four-mandatory.md  # Think×4 perpetual requirement
    │   └── transparency-requirements-user.md
    └── vision/              # Pure user conceptual input
        ├── application-evolution-user.md
        ├── autonomous-systems-user.md
        ├── command-philosophy-user.md
        ├── communication-documentation-user.md
        ├── core-mission-concept.md
        ├── development-methodology-user.md
        ├── global-system-user.md
        └── README.md       # Vision navigation
```

## Key Architecture Components

### Command Execution System
- **.claude/commands/**: 4 core local commands using Claude Code convention
- **export/commands/**: 86 global commands organized in 15 categories
- **Rules integration**: Conditional loading through rules/CLAUDE_RULES.md

### Documentation Architecture (Ultra-Simplified)
- **docs/core/**: Technical authority (70 consolidated files)
- **docs/context/**: System knowledge (patterns, examples, implementation)
- **docs/decisions/**: Strategic direction (vision + governance)
- **Total reduction**: 13 → 3 core directories (77% simplification)

### Development Infrastructure
- **tools/**: Development utilities and templates (moved from docs/)
- **scripts/**: Automation and validation utilities
- **rules/**: Conditional loading protocols
- **Git integration**: Hooks, workflows, and automation

### Sacred User Space Protection
- **user-input/**: Complete user authority preservation
- **Think×4 integration**: Perpetual analysis requirement established
- **Vision authority**: Original user conceptual framework maintained

## System Integration Points

### Think×4 Perpetual Analysis
- **user-input/technical-requirements/think-by-four-mandatory.md**: User requirement
- **rules/CLAUDE_RULES.md**: Agent mandate (🧠 MANDATORY section)
- **docs/core/pts-framework-consolidated.md**: Technical integration

### Authority Hierarchy
1. **user-input/**: Sacred User Space (absolute authority)
2. **rules/CLAUDE_RULES.md**: Partnership protocol + Think×4 mandates
3. **docs/core/**: Technical implementation authority
4. **.claude/commands/**: Executable implementation

### Quality Assurance Integration
- **PTS Framework**: 12-component validation in core/
- **Documentation standards**: Consolidated in core/
- **Performance monitoring**: Metrics and dashboards in tools/
- **Git validation**: Pre-commit hooks and scripts

---

**Architecture Principle**: Maximum simplicity with sophisticated parallel execution - user focuses on vision and objectives while system handles technical complexity through intelligent orchestration.