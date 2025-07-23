# Project Structure - ce-simple Command System

**Generated with:** `tree -I '.git|node_modules|.DS_Store' -L 3`  
**Last Updated:** 2025-07-23

## Complete Directory Structure

```
ce-simple/
├── 10-standards/            # Development standards and templates
│   ├── standard-naming.md   # Naming conventions
│   ├── standard-writing.md  # Writing standards
│   ├── template-command.md  # Command template
│   └── template-docs.md     # Documentation template
├── CLAUDE.md               # System overview (this file)
├── commands/               # Executable slash commands
│   ├── 00-core/           # Foundation infrastructure
│   │   ├── context-engine.md    # Distributed memory management
│   │   ├── handoff-manager.md   # Session transitions
│   │   ├── init-project.md      # Project initialization
│   │   └── notify-manager.md    # Centralized notifications
│   ├── 01-discovery/      # Discovery commands
│   │   ├── explore-codebase.md  # Codebase exploration
│   │   ├── explore-web.md       # Web research
│   │   ├── exploration-patterns.md # Discovery methodology
│   │   └── think-layers.md      # Progressive analysis
│   ├── 02-planning/       # Planning commands
│   ├── 03-analysis/       # Analysis commands
│   ├── 04-execution/      # Execution commands
│   ├── 05-validation/     # Validation commands
│   │   ├── validate-code.md     # Code validation
│   │   ├── validate-complete.md # Completion validation
│   │   ├── validate-creative.md # Creative validation
│   │   └── validate-visual.md   # Visual validation
│   ├── 06-documentation/  # Documentation commands
│   ├── 07-maintenance/    # Maintenance commands
│   ├── 08-learning/       # Learning commands
│   ├── 09-git/           # Git workflow commands
│   ├── 10-standards/     # Standards commands
│   ├── 11-meta/          # Meta commands
│   ├── 12-math/          # Mathematical commands
│   ├── 13-search/        # Search commands
│   ├── 14-utils/         # Utility commands
│   │   ├── calc-engine.md       # Calculation engine
│   │   ├── deploy-core.md       # Deployment engine
│   │   ├── monitor-core.md      # Monitoring core
│   │   ├── todo-manager.md      # Task management
│   │   └── validator-core.md    # Validation framework
│   ├── agent-coordinate.md      # Agent coordination
│   ├── agent-deploy.md          # Agent deployment
│   ├── agent-orchestration.md   # Parallel orchestration
│   ├── analyze-parallel.md      # Parallel analysis
│   ├── capture-learnings.md     # Learning capture
│   ├── command-create.md        # Command creation
│   ├── command-maintain.md      # Command maintenance
│   ├── complexity-assess.md     # Complexity assessment
│   ├── context-optimize.md      # Context optimization
│   ├── 00-core/
│   │   ├── enhanced-start.md   # Enhanced discovery
│   ├── load-balance.md          # Load balancing
│   ├── matrix-maintenance.md    # Cross-reference validation
│   ├── performance-track.md     # Performance tracking
│   │   ├── start.md            # Primary entry point
│   ├── system-monitor.md        # System monitoring
│   ├── worktree-cleanup.md      # Worktree cleanup
│   ├── worktree-close.md        # Worktree completion
│   └── worktree-start.md        # Isolated development
├── docs/                   # Documentation framework
│   ├── commands/          # Command implementation details
│   ├── context/           # Context system documentation
│   ├── core/              # Core architecture
│   │   ├── context-architecture.md     # Distributed memory and context management
│   │   ├── evolution-learning.md       # System evolution and learning protocols
│   │   ├── system-principles.md        # Design principles and architecture overview
│   │   ├── task-orchestration.md       # Task coordination and orchestration
│   │   └── README.md                   # Core documentation navigation hub
│   ├── frameworks/        # System frameworks
│   │   ├── execution-patterns.md       # Execution patterns
│   │   ├── performance-framework.md    # Performance monitoring
│   │   └── validation-framework.md     # Quality assurance
│   ├── standards/         # Development standards
│   │   ├── command-standards.md        # Command specifications
│   │   ├── command-structure-standard.md # Structure standards
│   │   └── documentation-standards.md  # Documentation requirements
│   ├── templates/         # Document templates
│   │   ├── command-template.md         # Command template
│   │   └── documentation-template.md   # Documentation template
│   └── vision/            # System philosophy
│       ├── command-philosophy.md       # Command philosophy
│       ├── overview.md                 # System vision
│       ├── parallelization-strategy.md # Parallel execution
│       └── task-orchestration-details.md # Task orchestration
└── rollback/              # Disaster recovery
    ├── rollback-manager.sh            # Automated rollback
    └── rollback-strategy.md           # Recovery procedures
```

## Directory Statistics

- **Total Files**: 98
- **Total Directories**: 33
- **Command Categories**: 15 (00-core through 14-utils)
- **Core Commands**: 4 (foundation infrastructure)
- **Executable Commands**: 57 (includes categorized and root-level commands)

## Key Structural Elements

### Foundation Layer (00-core/)
Essential infrastructure commands providing the system foundation for all operations.

### Command Categories (01-15/)
Organized functional groupings with specialized commands for specific workflow phases.

### Documentation Framework (docs/)
Comprehensive documentation system using progressive disclosure and reference patterns.

### Standards and Templates (10-standards/, docs/standards/, docs/templates/)
Development guidelines and structural templates ensuring consistency across the system.

### Disaster Recovery (rollback/)
Automated recovery mechanisms for system reliability and data protection.

---

**Architecture Principle**: Hierarchical organization with clear separation of concerns and comprehensive documentation coverage for maximum maintainability and scalability.