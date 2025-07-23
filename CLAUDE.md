# CLAUDE.md - ce-simple Command System

**Last Updated: 2025-07-23**

## System Overview

**ce-simple** creates self-contained slash commands that orchestrate parallel task execution through Claude Code's Task Tool to transform user vision into reality.

**Core Philosophy**: Interview-Driven Development with intelligent task orchestration for 10x productivity gains.

**Complete Vision**: See [docs/vision/overview.md](docs/vision/overview.md) for full system philosophy and evolution roadmap.

## Core Architecture

**Foundation Documentation**: [docs/core/README.md](docs/core/README.md) - Complete architectural overview with reading path.

### Reading Order
1. **[Principles](docs/core/principles.md)** - System foundation and architectural principles
2. **[Orchestration](docs/core/orchestration.md)** - Task coordination patterns and strategies  
3. **[Context System](docs/core/context-system.md)** - Distributed memory architecture
4. **[Evolution](docs/core/evolution.md)** - Learning and adaptation protocols

Each core document includes references to detailed implementations.

## Project Structure

```
ce-simple/
├── .archive/                 # Legacy system archive
├── commands/                 # Executable slash commands
├── docs/
│   ├── commands/            # Command implementations
│   ├── context/             # Context system documentation
│   ├── core/                # Core architecture documentation
│   ├── matrix/              # Cross-reference framework
│   ├── notes/               # Session notes and discoveries
│   ├── patterns/            # Reusable patterns
│   ├── standards/           # Development standards
│   ├── templates/           # Document templates
│   └── vision/              # System philosophy
├── CLAUDE.md                # System overview (this file)
└── README.md                # Project introduction
```

## Command System

**Executable Commands**: `commands/` - Self-contained slash commands for Claude Code execution  
**Implementation Docs**: `docs/commands/` - Detailed implementation guides and system documentation

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
- **[Document Template](docs/standards/document-template.md)** - Consistent structure patterns

### Key Requirements
- Commands: ≤150 lines with full self-containment
- Documentation: ≤200 lines using progressive disclosure
- Default parallel execution with intelligent orchestration
- Natural language instructions for Claude Code execution

## Quick Start

### Entry Point
Execute `/start` with your request for intelligent discovery workflow.

### Learning Path  
Begin with [docs/core/principles.md](docs/core/principles.md) to understand system foundation.

### Complete Guide
See [docs/core/README.md](docs/core/README.md) for full documentation navigation.

---

**System Principle**: Simple interface, powerful orchestration, transparent operation, continuous evolution.