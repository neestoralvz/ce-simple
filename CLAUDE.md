# CLAUDE.md - ce-simple Command System

**Last Updated: 2025-07-23**

## System Overview

**ce-simple** creates self-contained slash commands that orchestrate parallel task execution through Claude Code's Task Tool to transform user vision into reality.

**Core Philosophy**: Interview-Driven Development with intelligent task orchestration for 10x productivity gains.

**Dynamic Questioning Principle**: Question dynamically for clarification throughout all phases when requirements unclear. This continuous principle applies across all commands and workflows to ensure accuracy and prevent assumptions.

**Complete Vision**: See [docs/vision/overview.md](docs/vision/overview.md) for full system philosophy and evolution roadmap.

## Vision-Driven Development

**Absolute Authority**: The `docs/vision/` directory contains the **single source of truth** for all system direction, user intent, and project evolution. Every component of ce-simple exists to serve and implement the user's vision as captured in these documents.

**Authority Hierarchy**: 
1. **`docs/vision/`** - User intent and system direction (absolute authority)
2. **`docs/core/`** - Technical implementation of vision principles  
3. **`commands/`** - Executable manifestation of vision workflows
4. **`CLAUDE.md`** - System documentation reflecting current vision state

**Vision-First Principle**: All system changes, updates, and evolution must originate from and align with `docs/vision/`. No component may contradict or override user vision as captured in these foundational documents.

**Feedback Integration**: Use `/feedback-vision` to capture user feedback through dynamic interviews and automatically update vision documents. Use `/vision-propagate` to ensure all system components reflect the latest vision state.

## Core Architecture

**Foundation Documentation**: [docs/core/README.md](docs/core/README.md) - Complete architectural overview with reading path.

### 00-core Foundation

**System Foundation Layer**: Six essential commands providing core infrastructure for project initialization, context management, notifications, and primary entry points.

- **`/init-project`** - Complete project initialization with git, structure, and core documentation
- **`/context-engine`** - Automated context updating and synchronization across distributed memory architecture  
- **`/notify-manager`** - Centralized notification management for transparent delegation and state tracking
- **`/handoff-manager`** - Seamless agent and session transitions with complete state preservation
- **`/start`** - Primary entry point with dynamic questioning and mathematical assessment
- **`/enhanced-start`** - Advanced discovery with Phase 0 assessment and autotrigger execution

**Integration**: Foundation commands integrate with all workflow phases and provide essential infrastructure for system operation.

### Reading Order
1. **[System Principles](docs/core/system-principles.md)** - System foundation and architectural principles
2. **[Task Orchestration](docs/core/task-orchestration.md)** - Task coordination patterns and strategies  
3. **[Context Architecture](docs/core/context-architecture.md)** - Distributed memory architecture
4. **[Performance](docs/frameworks/performance-framework.md)** - Performance monitoring and optimization
5. **[Patterns](docs/frameworks/execution-patterns.md)** - Comprehensive execution pattern library
6. **[Validation](docs/frameworks/validation-framework.md)** - Quality assurance and validation framework
7. **[Evolution and Learning](docs/core/evolution-learning.md)** - Comprehensive learning and adaptation protocols

Each core document includes references to detailed implementations.

## Project Structure

```
ce-simple/
├── commands/                 # Executable slash commands (15 categories, 54 commands)
│   ├── 00-core/             # System foundation layer (6 commands)
│   │   ├── context-engine.md    # Distributed memory management
│   │   ├── enhanced-start.md     # Advanced discovery with Phase 0 assessment
│   │   ├── handoff-manager.md    # Session transitions
│   │   ├── init-project.md       # Project initialization
│   │   ├── notify-manager.md     # Centralized notifications
│   │   └── start.md              # Primary entry point
│   ├── 01-discovery/        # Discovery and exploration (3 commands)
│   │   ├── explore-codebase.md   # Internal project analysis
│   │   ├── explore-web.md        # External research
│   │   └── think-layers.md       # Progressive analysis
│   ├── 02-planning/         # Strategic planning (2 commands)
│   │   ├── feedback-vision.md    # User feedback collection and vision update
│   │   └── vision-propagate.md   # Vision-driven system propagation
│   ├── 03-analysis/         # Analysis and assessment (5 commands)
│   │   ├── analyze-parallel.md   # Parallel processing analysis
│   │   ├── analyze-parallel-implementation.md # Implementation details
│   │   ├── complexity-assess.md  # Technical complexity evaluation
│   │   ├── load-balance.md       # Load balancing strategies
│   │   └── problem-solving.md    # Systematic problem decomposition
│   ├── 04-execution/        # Implementation and execution (5 commands)
│   │   ├── agent-coordinate.md   # Agent coordination
│   │   ├── agent-deploy.md       # Agent deployment
│   │   ├── agent-orchestration.md # Advanced parallel coordination
│   │   ├── load-balance.md       # Distributed workload management
│   │   └── result-consolidate.md # Result aggregation
│   ├── 05-validation/       # Quality assurance (4 commands)
│   │   ├── validate-code.md      # Code validation
│   │   ├── validate-complete.md  # Completion validation
│   │   ├── validate-creative.md  # Creative output validation
│   │   └── validate-visual.md    # Visual content validation
│   ├── 06-documentation/    # Documentation management (1 command)
│   │   └── docs-maintain.md      # Documentation maintenance
│   ├── 07-maintenance/      # System maintenance (1 command)
│   │   └── context-optimize.md   # Context consolidation
│   ├── 08-learning/         # Learning and development (4 commands)
│   │   ├── capture-learnings.md  # Pattern extraction
│   │   ├── performance-track.md  # Performance metrics
│   │   ├── system-monitor.md     # System monitoring
│   │   └── system-monitor-agents.md # Agent health monitoring
│   ├── 09-git/              # Git workflow management (4 commands)
│   │   ├── git-worktree.md       # Parallel development manager
│   │   ├── worktree-cleanup.md   # Automated maintenance
│   │   ├── worktree-close.md     # Session completion
│   │   └── worktree-start.md     # Isolated development
│   ├── 10-standards/        # Standards and templates (4 commands)
│   │   ├── standard-naming.md    # Naming conventions
│   │   ├── standard-writing.md   # Writing standards
│   │   ├── template-command.md   # Command templates
│   │   └── template-docs.md      # Documentation templates
│   ├── 11-meta/             # Meta-system commands (4 commands)
│   │   ├── command-create.md     # Command development
│   │   ├── command-creation.md   # Creation framework
│   │   ├── command-maintain.md   # Command maintenance
│   │   └── matrix-maintenance.md # Cross-reference validation
│   ├── 12-math/             # Mathematical operations (0 commands)
│   ├── 13-search/           # Information discovery & retrieval (4 commands)
│   │   ├── search-advanced.md   # Complex search operations
│   │   ├── index-content.md     # Content indexing with metadata
│   │   ├── discover-information.md # Intelligent information retrieval
│   │   └── filter-results.md    # Result filtering and refinement
│   └── 14-utils/            # Utility engines (8 commands)
│       ├── phase-manager.md      # Universal TodoWrite orchestration
│       ├── validation-engine.md  # Multi-domain validation coordination
│       ├── agent-lifecycle.md    # Agent deployment and management
│       ├── calc-engine.md        # Calculation engine
│       ├── deploy-core.md        # Deployment engine
│       ├── monitor-core.md       # Monitoring infrastructure
│       ├── todo-manager.md       # Task management
│       └── validator-core.md     # Validation framework
├── docs/
│   ├── commands/            # Command implementation documentation
│   ├── context/             # Context system documentation
│   ├── core/                # Core architecture documentation
│   │   ├── README.md           # Complete architectural overview
│   │   ├── system-principles.md # System foundation and principles
│   │   ├── task-orchestration.md # Task orchestration patterns
│   │   ├── context-architecture.md # Distributed memory architecture
│   │   └── evolution-learning.md # Learning and adaptation protocols
│   ├── frameworks/          # System frameworks
│   │   ├── execution-patterns.md     # Execution pattern library
│   │   ├── performance-framework.md  # Performance monitoring
│   │   └── validation-framework.md   # Quality assurance
│   ├── standards/           # Development standards
│   │   ├── command-standards.md      # Command specifications
│   │   └── documentation-standards.md # Documentation requirements
│   ├── templates/           # Document templates
│   │   └── command-template.md       # Command development template
│   └── vision/              # System philosophy
│       └── overview.md      # Complete system philosophy
├── CLAUDE.md                # System overview (this file)
└── README.md                # Project introduction
```

## Command System

**Executable Commands**: `commands/` - Self-contained slash commands organized in 15 functional categories  
**Implementation Docs**: `docs/commands/` - Detailed implementation guides and system documentation

### Information Discovery & Retrieval (13-search) - 4 Commands
Advanced search capabilities with intelligent filtering, content indexing, and context-aware information discovery.

- **`/search-advanced`** - Complex search operations with multi-criteria filtering and boolean logic
- **`/index-content`** - Content indexing and organization with metadata management and relationship mapping
- **`/discover-information`** - Intelligent information retrieval with context awareness and gap detection
- **`/filter-results`** - Result filtering and refinement with relevance scoring and ranking algorithms

### System Foundation (00-core) - 6 Commands
Essential infrastructure commands providing core functionality for all operations.

- **`/init-project`** - Complete project initialization with git, structure, and core documentation
- **`/context-engine`** - Automated context synchronization and distributed memory management  
- **`/notify-manager`** - Centralized notifications for transparent delegation and system state tracking
- **`/handoff-manager`** - Seamless transitions between agents, sessions, and workflow phases
- **`/start`** - Primary entry point with dynamic questioning and mathematical assessment
- **`/enhanced-start`** - Advanced discovery with Phase 0 assessment and autotrigger execution

### Discovery & Analysis (01-discovery, 03-analysis) - 7 Commands
Commands for understanding requirements, context, and technical analysis.

- **`/explore-codebase`** - Internal project analysis and code understanding
- **`/explore-web`** - External research and information gathering from web sources
- **`/think-layers`** - Progressive analysis for complex problems requiring deep thinking
- **`/analyze-parallel`** - Parallel processing analysis and optimization strategies
- **`/analyze-parallel-implementation`** - Implementation details for parallel analysis
- **`/complexity-assess`** - Technical complexity evaluation and assessment methodology
- **`/load-balance`** - Load balancing strategies for distributed workloads (consolidated from execution)
- **`/problem-solving`** - Systematic problem decomposition and solution frameworks

### Execution & Orchestration (04-execution) - 4 Commands
Commands for active development, implementation, and parallel coordination.

- **`/agent-coordinate`** - Agent coordination and task distribution
- **`/agent-deploy`** - Agent deployment and orchestration setup
- **`/agent-orchestration`** - Advanced parallel task coordination and management
- **`/result-consolidate`** - Result aggregation and synthesis from parallel operations

### Quality Assurance (05-validation) - 4 Commands
Comprehensive validation commands ensuring quality and correctness.

- **`/validate-code`** - Code validation and quality assurance
- **`/validate-complete`** - Completion validation and requirement verification
- **`/validate-creative`** - Creative output validation and assessment
- **`/validate-visual`** - Visual content validation and standards compliance

### Git Workflow Management (09-git) - 4 Commands
Advanced Git operations and version control orchestration.

- **`/git-worktree`** - Parallel development environment manager with lifecycle tracking
- **`/worktree-start`** - Initialize isolated development environment with session metadata
- **`/worktree-close`** - Complete session with enhanced auto-decision matrix and merge orchestration
- **`/worktree-cleanup`** - Automated maintenance with intelligent orphan detection and safety protocols

### System Management (06-documentation, 07-maintenance, 08-learning, 11-meta) - 10 Commands
Commands for system health, documentation, learning, and maintenance operations.

- **`/docs-maintain`** - Documentation maintenance and consistency validation
- **`/context-optimize`** - Intelligent context consolidation and optimization
- **`/capture-learnings`** - Pattern extraction and documentation with interview-driven learning
- **`/performance-track`** - Performance metrics collection and optimization analysis
- **`/system-monitor`** - Unified system monitoring with compliance validation and performance metrics
- **`/system-monitor-agents`** - Agent health monitoring and status tracking for orchestration systems
- **`/command-create`** - Systematic command development and creation
- **`/command-creation`** - Command creation framework and methodology
- **`/command-maintain`** - Command maintenance and optimization procedures
- **`/matrix-maintenance`** - Cross-reference validation and integrity checking

### Development Standards (10-standards) - 4 Commands
Standards, templates, and development guidelines.

- **`/standard-naming`** - Naming conventions and consistency guidelines
- **`/standard-writing`** - Writing standards and documentation requirements
- **`/template-command`** - Command development templates and structures
- **`/template-docs`** - Documentation templates and formatting standards

### Utility Engines (14-utils) - 8 Commands
Core utility engines providing specialized functionality and eliminating duplicate logic across commands.

- **`/phase-manager`** - Universal TodoWrite orchestration eliminating 91% command duplication
- **`/validation-engine`** - Multi-domain validation orchestration with parallel execution
- **`/agent-lifecycle`** - Comprehensive agent deployment, monitoring, and recovery management
- **`/calc-engine`** - Mathematical calculation and computation engine
- **`/deploy-core`** - Universal deployment engine for system components
- **`/monitor-core`** - Core monitoring infrastructure and metrics collection
- **`/todo-manager`** - Advanced task management and tracking system
- **`/validator-core`** - Core validation framework and quality assurance

### Strategic Planning (02-planning) - 2 Commands
Vision-driven development commands ensuring user intent drives all system evolution.

- **`/feedback-vision`** - User feedback collection through dynamic interviews with integrated research
- **`/vision-propagate`** - Vision-driven system propagation maintaining docs/vision/ as absolute authority

### Expansion Categories (12-math) - 0 Commands
Reserved categories for future system expansion and specialized functionality.

## Development Standards

**All Standards**: [docs/standards/](docs/standards/) directory contains complete development guidelines.

### Core Standards
- **[Command Standards](docs/standards/command-standards.md)** - Self-contained orchestration requirements with 15-category organization
- **[Documentation Standards](docs/standards/documentation-standards.md)** - Writing principles and clarity requirements  
- **[Command Template](docs/templates/command-template.md)** - Consistent structure patterns for new command development

### Key Requirements
- **Commands**: ≤150 lines with full self-containment and categorical organization
- **Documentation**: ≤200 lines using progressive disclosure principles
- **Default parallel execution** with intelligent orchestration through Task Tool
- **Natural language instructions** for Claude Code execution
- **Categorical Structure**: Commands organized in 15 functional categories (00-14)

### Command Organization
- **00-core**: Foundation infrastructure (6 commands)
- **01-14**: Specialized categories with focused functionality
- **Empty categories** (12-math) reserved for future expansion

## Quick Start

### Entry Points
- **New Projects**: Execute `/init-project` (00-core) for complete foundation setup with git, structure, and documentation
- **Existing Projects**: Execute `/start` (00-core) for intelligent discovery workflow with mathematical assessment
- **Advanced Discovery**: Use `/enhanced-start` (00-core) for Phase 0 assessment and autotrigger execution
- **Complex Problems**: Deploy `/think-layers` (01-discovery) for progressive analysis and deep thinking
- **Research Tasks**: Combine `/explore-codebase` (01-discovery) with `/explore-web` (01-discovery)
- **User Feedback**: Use `/feedback-vision` (02-planning) to capture feedback and update vision documents
- **System Updates**: Execute `/vision-propagate` (02-planning) to align entire system with current vision

### Workflow Integration
- **Vision Authority**: All workflows respect docs/vision/ as absolute source of truth
- **Foundation Layer**: All commands use 00-core infrastructure (context-engine, notify-manager, handoff-manager)
- **Parallel Execution**: Commands designed for parallel execution through Task Tool orchestration
- **Quality Assurance**: 05-validation commands ensure quality throughout all phases
- **Learning Loop**: 08-learning commands capture patterns for continuous improvement
- **Feedback Integration**: System continuously aligns with user vision through feedback-vision and vision-propagate

### Command Path Examples
```bash
# Foundation commands (always available)
/init-project          # commands/00-core/init-project.md
/start                 # commands/00-core/start.md
/context-engine        # commands/00-core/context-engine.md

# Specialized workflow commands
/explore-codebase      # commands/01-discovery/explore-codebase.md
/feedback-vision       # commands/02-planning/feedback-vision.md
/vision-propagate      # commands/02-planning/vision-propagate.md
/agent-orchestration   # commands/04-execution/agent-orchestration.md
/validate-complete     # commands/05-validation/validate-complete.md
/worktree-start        # commands/09-git/worktree-start.md
```

### Learning Path  
Begin with [docs/core/system-principles.md](docs/core/system-principles.md) to understand system foundation, then see [docs/core/README.md](docs/core/README.md) for complete navigation guide.

---

**System Principle**: Simple interface, powerful orchestration, transparent operation, continuous evolution.