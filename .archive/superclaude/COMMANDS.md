# COMMANDS.md - SuperClaude Command Execution Framework

---
framework: "SuperClaude v3.0"
execution-engine: "Claude Code"
wave-compatibility: "Full"
---

Command execution framework for Claude Code SuperClaude integration.

## Command System Architecture

### Core Command Structure
- --
- **Command**: /{command-name}
- **Category**: Primary classification
- **Purpose**: Operational objective
- **Wave-Enabled**: true|false
- **Performance-Profile**: optimization|standard|complex
- --

### Command Processing Pipeline
1. **Input Parsing**: `$ARGUMENTS` with `@<path>`, `!<command>`, `--<flags>`
2. **Context Resolution**: Auto-persona activation and MCP server selection
3. **Wave Eligibility**: Complexity assessment and wave mode determination
4. **Execution Strategy**: Tool orchestration and resource allocation
5. **Quality Gates**: Validation checkpoints and error handling

### Integration Layers
- **Claude Code**: Native slash command compatibility
- **Persona System**: Auto-activation based on command context
- **MCP Servers**: Context7, Sequential, Magic, Playwright integration
- **Wave System**: Multi-stage orchestration for complex operations

## Wave System Integration

**Wave Orchestration Engine**: Multi-stage command execution with compound intelligence. Auto-activates on complexity ≥0.7 + files >20 + operation_types >2.

**Wave-Enabled Commands**:
- **Tier 1**: `/analyze`, `/build`, `/implement`, `/improve`
- **Tier 2**: `/design`, `/task`

### Development Commands

**`/build $ARGUMENTS`**
- --
- **Command**: /build
- **Category**: Development & Deployment
- **Purpose**: Project builder with framework detection
- **Wave-Enabled**: true
- **Performance-Profile**: optimization
- --
- **Auto-Persona**: Frontend, Backend, Architect, Scribe
- **MCP Integration**: Magic (UI builds), Context7 (patterns), Sequential (logic)
- **Tool Orchestration**: [Read, Grep, Glob, Bash, TodoWrite, Edit, MultiEdit]
- **Arguments**: `[target]`, `@<path>`, `!<command>`, `--<flags>`

**`/implement $ARGUMENTS`**
- --
- **Command**: /implement
- **Category**: Development & Implementation
- **Purpose**: Feature and code implementation with intelligent persona activation
- **Wave-Enabled**: true
- **Performance-Profile**: standard
- --
- **Auto-Persona**: Frontend, Backend, Architect, Security (context-dependent)
- **MCP Integration**: Magic (UI components), Context7 (patterns), Sequential (complex logic)
- **Tool Orchestration**: [Read, Write, Edit, MultiEdit, Bash, Glob, TodoWrite, Task]
- **Arguments**: `[feature-description]`, `--type component|api|service|feature`, `--framework <name>`, `--<flags>`


### Analysis Commands

**`/analyze $ARGUMENTS`**
- --
- **Command**: /analyze
- **Category**: Analysis & Investigation
- **Purpose**: Multi-dimensional code and system analysis
- **Wave-Enabled**: true
- **Performance-Profile**: complex
- --
- **Auto-Persona**: Analyzer, Architect, Security
- **MCP Integration**: Sequential (primary), Context7 (patterns), Magic (UI analysis)
- **Tool Orchestration**: [Read, Grep, Glob, Bash, TodoWrite]
- **Arguments**: `[target]`, `@<path>`, `!<command>`, `--<flags>`

**`/troubleshoot [symptoms] [flags]`** - Problem investigation | Auto-Persona: Analyzer, QA | MCP: Sequential, Playwright

**`/explain [topic] [flags]`** - Educational explanations | Auto-Persona: Mentor, Scribe | MCP: Context7, Sequential


### Quality Commands

**`/improve [target] [flags]`**
- --
- **Command**: /improve
- **Category**: Quality & Enhancement
- **Purpose**: Evidence-based code enhancement
- **Wave-Enabled**: true
- **Performance-Profile**: optimization
- --
- **Auto-Persona**: Refactorer, Performance, Architect, QA
- **MCP Integration**: Sequential (logic), Context7 (patterns), Magic (UI improvements)
- **Tool Orchestration**: [Read, Grep, Glob, Edit, MultiEdit, Bash]
- **Arguments**: `[target]`, `@<path>`, `!<command>`, `--<flags>`


**`/cleanup [target] [flags]`** - Project cleanup and technical debt reduction | Auto-Persona: Refactorer | MCP: Sequential

### Additional Commands

**`/document [target] [flags]`** - Documentation generation | Auto-Persona: Scribe, Mentor | MCP: Context7, Sequential

**`/estimate [target] [flags]`** - Evidence-based estimation | Auto-Persona: Analyzer, Architect | MCP: Sequential, Context7

**`/task [operation] [flags]`** - Long-term project management | Auto-Persona: Architect, Analyzer | MCP: Sequential

**`/test [type] [flags]`** - Testing workflows | Auto-Persona: QA | MCP: Playwright, Sequential

**`/git [operation] [flags]`** - Git workflow assistant | Auto-Persona: DevOps, Scribe, QA | MCP: Sequential

**`/design [domain] [flags]`** - Design orchestration | Auto-Persona: Architect, Frontend | MCP: Magic, Sequential, Context7

### Meta & Orchestration Commands

**`/index [query] [flags]`** - Command catalog browsing | Auto-Persona: Mentor, Analyzer | MCP: Sequential

**`/load [path] [flags]`** - Project context loading | Auto-Persona: Analyzer, Architect, Scribe | MCP: All servers

**Iterative Operations** - Use `--loop` flag with improvement commands for iterative refinement

**`/spawn [mode] [flags]`** - Task orchestration | Auto-Persona: Analyzer, Architect, DevOps | MCP: All servers

## Command Execution Matrix

### Performance Profiles
- **Optimization**: High-performance with caching and parallel execution
- **Standard**: Balanced performance with moderate resource usage
- **Complex**: Resource-intensive with comprehensive analysis

### Command Categories
- **Development**: build, implement, design
- **Analysis**: analyze, troubleshoot, explain
- **Quality**: improve, cleanup
- **Testing**: test
- **Documentation**: document
- **Planning**: estimate, task
- **Version-Control**: git
- **Meta**: index, load, spawn

### Wave-Enabled Commands
6 commands: `/analyze`, `/build`, `/design`, `/implement`, `/improve`, `/task`

