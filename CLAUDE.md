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

@docs/core/project-structure.md

## Command System

@docs/commands/command-index.md

## Development Standards

@docs/standards/command-standards.md

## Quick Start

### Entry Points
- **New Projects**: Execute `/init-project` for complete foundation setup
- **Existing Projects**: Execute `/start` for intelligent discovery workflow
- **Complex Problems**: Use `/think-layers` for progressive analysis

### Learning Path
[Ver guía completa de navegación →](docs/core/README.md)

---

**System Principle**: Simple interface, powerful orchestration, transparent operation, continuous evolution.