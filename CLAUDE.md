# CLAUDE.md - Simplified Commands System

**Last Updated: 2025-07-22**

## 🎯 SYSTEM OVERVIEW

**ce-simple**: Streamlined command system for Claude Code enabling efficient context engineering through intelligent workflow orchestration and agent deployment.

**Core Philosophy**: Pragmatic effectiveness, autocontained commands, LLM optimized, anti-bias processing → `docs/core/architectural-principles.md`

**Standard Operation**: ALL commands use exhaustive verification by default → `docs/matrix/validation-protocols.md`

**File Management Rules**: All file creation restrictions and maintenance rules → `docs/core/anti-bias-enforcement.md`

## 🚀 COMMAND DIRECTORY

### Commands Location: `.claude/commands/`

### Master Workflow
- **`/start`** - Discovery workflow with dynamic questioning and agent orchestration
- **Automation Tools** - Git WorkTrees, monitoring, and performance tracking (`tools/`)

### Core Operations  
- **`/explore-codebase`** - Internal knowledge discovery with parallel Task Tool deployment
- **`/explore-web`** - External research and pattern validation with parallel WebSearch
- **`/think-layers`** - Progressive analysis: think → think-hard → think-harder → ultra-think
- **`/capture-learnings`** - Pattern detection and post-execution learning with dynamic interviews

### Work Tree Lifecycle
- **`/worktree-start`** - Initialize session work tree with automated isolation for complex workflows
- **`/worktree-close`** - Intelligent session completion with merge/abandon decision framework
- **`/worktree-cleanup`** - Automated maintenance and orphan work tree management

### System Maintenance
- **`/matrix-maintenance`** - Cross-reference matrix validation and system integrity monitoring
- **`/context-optimize`** - Intelligent context maintenance with consolidation and density optimization
- **`/command-create`** - Systematic command development with complete integration lifecycle

### System Standards
Commands follow integrated standards → `docs/core/writing-standards.md`, `docs/matrix/validation-protocols.md`, `docs/core/anti-bias-enforcement.md`, `docs/commands/command-template.md`

## 🔧 WORKFLOW INTEGRATION

### Primary Discovery Flow
```
⟳ /start → [complexity ≥6: /worktree-start] → dynamic questions → /explore-codebase + /explore-web → /think-layers → execution plan → /capture-learnings → /context-optimize → [session end: /worktree-close]
├─ /matrix-maintenance → Cross-reference validation → /context-optimize (periodic)
├─ /context-optimize → Automated context maintenance (post-command)
├─ /worktree-cleanup → Automated work tree maintenance (weekly)
```

**Complete workflow details**: Integrated in command implementations

### Intelligence Parallelization Protocol
**MANDATORY**: Autocontained analysis → optimization → aggressive execution
- **Dynamic WebSearches** (4-16 based on topic complexity)
- **Adaptive codebase operations** (12-52 based on project size)
- **Message-level optimization** - maximize efficiency through intelligent batching

**Detailed specifications**: `docs/core/parallelization-system.md`

## 🎯 IMPLEMENTATION READY

### System Status
- ✓ **Command Structure**: Core commands implemented and cross-referenced
- ✓ **Standards Framework**: Writing, notification, and anti-bias protocols established
- ✓ **Workflow Integration**: Discovery-to-execution pipeline operational
- ✓ **Context Architecture**: Organized subdirectories (discoveries/, patterns/, research/, workflows/) with intelligent file creation controls

### Usage Instructions
1. **Initialize**: Execute `/start` with initial request
2. **Respond**: Answer dynamic discovery questions for context clarification
3. **Monitor**: Track progress through real-time notifications
4. **Review**: Evaluate generated context and analysis results
5. **Execute**: Implement recommendations from workflow

**Complete operation guide**: `docs/core/usage-instructions.md`

---

**CRITICAL**: This system operates through slash command execution only. All functionality accessed via `/command-name` with autocontained cross-command integration.