# CLAUDE.md - ce-simple Command System

**Last Updated: 2025-07-23**

## System Overview

**ce-simple** creates self-contained slash commands that orchestrate parallel task execution through Claude Code's Task Tool to transform user vision into reality.

**Core Philosophy**: Interview-Driven Development with intelligent task orchestration for 10x productivity gains.

**Dynamic Questioning Principle**: Question dynamically for clarification throughout all phases when requirements unclear. This continuous principle applies across all commands and workflows to ensure accuracy and prevent assumptions.

**Complete Vision**: See [docs/vision/overview.md](docs/vision/overview.md) for full system philosophy and evolution roadmap.

## Core Architecture

**Foundation Documentation**: [docs/core/README.md](docs/core/README.md) - Complete architectural overview with reading path.

### 00-core Foundation

**System Foundation Layer**: Four essential commands providing core infrastructure for project initialization, context management, notifications, and seamless handoffs.

- **`/init-project`** - Complete project initialization with git, structure, and core documentation
- **`/context-engine`** - Automated context updating and synchronization across distributed memory architecture  
- **`/notify-manager`** - Centralized notification management for transparent delegation and state tracking
- **`/handoff-manager`** - Seamless agent and session transitions with complete state preservation

**Integration**: Foundation commands integrate with all workflow phases and provide essential infrastructure for system operation.

### Reading Order
1. **[Principles](docs/core/principles.md)** - System foundation and architectural principles
2. **[Orchestration](docs/core/orchestration.md)** - Task coordination patterns and strategies  
3. **[Context System](docs/core/context-system.md)** - Distributed memory architecture
4. **[Performance](docs/frameworks/performance-framework.md)** - Performance monitoring and optimization
5. **[Patterns](docs/frameworks/execution-patterns.md)** - Comprehensive execution pattern library
6. **[Validation](docs/frameworks/validation-framework.md)** - Quality assurance and validation framework
7. **[Evolution](docs/core/evolution.md)** - Learning and adaptation protocols

Each core document includes references to detailed implementations.

## Project Structure

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
│   ├── enhanced-start.md        # Enhanced discovery
│   ├── explore-codebase.md      # Codebase exploration
│   ├── explore-web.md           # Web research
│   ├── load-balance.md          # Load balancing
│   ├── matrix-maintenance.md    # Cross-reference validation
│   ├── performance-track.md     # Performance tracking
│   ├── start.md                 # Primary entry point
│   ├── system-monitor.md        # System monitoring
│   ├── think-layers.md          # Progressive analysis
│   ├── worktree-cleanup.md      # Worktree cleanup
│   ├── worktree-close.md        # Worktree completion
│   └── worktree-start.md        # Isolated development
├── docs/                   # Documentation framework
│   ├── commands/          # Command implementation details
│   ├── context/           # Context system documentation
│   ├── core/              # Core architecture
│   │   ├── architecture-v2-overview.md # Architecture overview
│   │   ├── context-system.md           # Distributed memory
│   │   ├── evolution.md                # System evolution
│   │   ├── orchestration.md            # Task coordination
│   │   ├── principles.md               # Design principles
│   │   └── README.md                   # Core documentation
│   ├── frameworks/        # System frameworks
│   │   ├── execution-patterns.md       # Execution patterns
│   │   ├── performance-framework.md    # Performance monitoring
│   │   ├── task-orchestration-framework.md # Task coordination
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

## Command System

**Executable Commands**: `commands/` - Self-contained slash commands for Claude Code execution  
**Implementation Docs**: `docs/commands/` - Detailed implementation guides and system documentation

### System Foundation (00-core)
- **`/init-project`** - Entry point for new project initialization with complete foundation setup
- **`/context-engine`** - Automated context synchronization and distributed memory management  
- **`/notify-manager`** - Centralized notifications for transparent delegation and system state tracking
- **`/handoff-manager`** - Seamless transitions between agents, sessions, and workflow phases

### Discovery & Analysis
- **`/start`** - Primary entry point with dynamic questioning
- **`/enhanced-start`** - Advanced discovery with Phase 0 assessment and autotrigger execution
- **`/explore-codebase`** - Internal project analysis
- **`/explore-web`** - External research and information gathering  
- **`/think-layers`** - Progressive analysis for complex problems

### Workflow Management
- **`/worktree-start`** - Initialize isolated development environment
- **`/worktree-close`** - Complete session with merge decisions
- **`/worktree-cleanup`** - Automated maintenance and cleanup

### System Maintenance
- **`/matrix-maintenance`** - Cross-reference validation and integrity
- **`/context-optimize`** - Intelligent context consolidation
- **`/command-create`** - Systematic command development
- **`/command-maintain`** - Command maintenance and optimization

### Learning & Development
- **`/capture-learnings`** - Pattern extraction and documentation
- **`/system-monitor`** - Performance tracking and optimization
- **`/agent-orchestration`** - Advanced parallel task coordination

## Development Standards

**All Standards**: [docs/standards/](docs/standards/) directory contains complete development guidelines.

### Core Standards
- **[Documentation Standards](docs/standards/documentation-standards.md)** - Writing principles and clarity requirements
- **[Command Standards](docs/standards/command-standards.md)** - Self-contained orchestration requirements  
- **[Document Template](docs/templates/documentation-template.md)** - Consistent structure patterns

### Key Requirements
- Commands: ≤150 lines with full self-containment
- Documentation: ≤200 lines using progressive disclosure
- Default parallel execution with intelligent orchestration
- Natural language instructions for Claude Code execution

## Quick Start

### Entry Points
- **New Projects**: Execute `/init-project` to establish complete foundation with git, structure, and documentation
- **Existing Projects**: Execute `/start` with your request for intelligent discovery workflow

### Learning Path  
Begin with [docs/core/principles.md](docs/core/principles.md) to understand system foundation.

### Complete Guide
See [docs/core/README.md](docs/core/README.md) for full documentation navigation.

---

**System Principle**: Simple interface, powerful orchestration, transparent operation, continuous evolution.