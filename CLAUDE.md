# CLAUDE.md - Simplified Commands System

**Last Updated: 2025-07-22**

**CRITICAL**: MANDATORY exploration of ALL `docs/core/` documentation BEFORE any content creation or system interaction.

## 🎯 SYSTEM OVERVIEW

**ce-simple**: Streamlined command system for Claude Code enabling efficient context engineering through intelligent workflow orchestration and agent deployment.

**Core Philosophy**: Pragmatic effectiveness, autocontained commands, LLM optimized, anti-bias processing → `docs/core/architectural-principles.md`

**Standard Operation**: ALL commands use exhaustive verification by default → `docs/matrix/validation-protocols.md`

**File Management Rules**: All file creation restrictions and maintenance rules → `docs/core/anti-bias-enforcement.md`

## 🔧 EXECUTION PROTOCOLS

### Mandatory Validation
- **3x Verification**: Structural → Content → Functional validation layers required
- **Exploration-First**: Use LS/Glob/Grep/Read tools BEFORE existence claims
- **Tool Ratio**: Minimum 3:1 tool calls to documentation lines
- **Quality Gates**: 85% health score threshold maintenance → `docs/matrix/validation-protocols.md`

### File Creation Controls
- **Session Limits**: Maximum 2-3 context files per session
- **Prohibited**: Meta-documentation, auto-timestamped, duplicate content
- **Required Structure**: Use subdirectories (discoveries/, patterns/, research/, workflows/)
- **Standards Compliance**: ≤150 lines commands, ≤200 lines documentation

### LLM Optimization Requirements
- **Behavioral Language**: CRITICAL/MANDATORY for high-priority instructions
- **Density Standards**: Maximum cognitive value per line
- **Context Engineering**: Progressive disclosure for complex workflows
- **Template Compliance**: All commands follow standardized structure → `docs/commands/command-template.md`

## 🚀 COMMAND DIRECTORY

### Commands Location: `.claude/commands/`

### Master Workflow
- **`/start`** - Discovery workflow with dynamic questioning and agent orchestration
- **Automation Tools** - Git WorkTrees, monitoring, and performance tracking (`tools/`)

### Core Operations  
- **`/explore-codebase`** - Internal discovery [Complexity: 3-8] [Tools: 12-52] → `docs/commands/explore-codebase-implementation.md`
- **`/explore-web`** - External research [Complexity: 2-6] [Searches: 4-16] → `docs/commands/explore-web-implementation.md`
- **`/think-layers`** - Progressive analysis [Auto-trigger: complex analysis] → `docs/commands/think-layers-implementation.md`
- **`/capture-learnings`** - Pattern detection [Auto-trigger: post-execution] → `docs/commands/capture-learnings-implementation.md`

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
├─ /context-optimize → Automated context + docs maintenance (post-command)
├─ /command-create → Systematic command development → /matrix-maintenance → /context-optimize
├─ /worktree-cleanup → Automated work tree maintenance (weekly)
```

**Enhanced Workflow Features**:
- **Real-time notifications**: Slash command execution tracking with TodoWrite integration
- **Auto-trigger transparency**: Clear visibility of command chain execution
- **Comprehensive maintenance**: Context + docs optimization with single source of truth
- **Meticulous integration**: All commands follow systematic integration protocols

**Complete workflow details**: Integrated in command implementations

### Intelligence Parallelization Protocol
**MANDATORY**: Autocontained analysis → optimization → aggressive execution
- **Dynamic WebSearches** (4-16 based on topic complexity)
- **Adaptive codebase operations** (12-52 based on project size)
- **Message-level optimization** - maximize efficiency through intelligent batching

**Detailed specifications**: `docs/core/parallelization-system.md`

## 📋 COMPLIANCE QUICK REFERENCE

### Pre-Execution Checklist
- [ ] Exploration tools used before claims
- [ ] File creation justified and limited
- [ ] Command complexity assessed
- [ ] Cross-references validated

### Standards Compliance
- [ ] 130-line command limit adherence
- [ ] CRITICAL/MANDATORY language for instructions
- [ ] 85% quality threshold maintenance
- [ ] Anti-bias protocol activation

### Performance Standards
- **Scale-Based Timing**: 30s <1000 files, 3min 1000-10000 files
- **Concurrent Operations**: 3-8 Task Tools, 2-5 WebSearch parallel
- **Auto-Optimization**: Real-time performance adaptation
- **Reference**: `docs/core/performance-system.md`

## 🎯 IMPLEMENTATION READY

### System Status
- ✓ **Command Structure**: Core commands implemented and cross-referenced
- ✓ **Standards Framework**: Writing, notification, and anti-bias protocols established
- ✓ **Workflow Integration**: Discovery-to-execution pipeline operational
- ✓ **Context Architecture**: Organized subdirectories (discoveries/, patterns/, research/, workflows/) + docs/notes/ with intelligent file creation controls

### Usage Instructions
1. **Initialize**: Execute `/start` with initial request
2. **Respond**: Answer dynamic discovery questions for context clarification
3. **Monitor**: Track progress through real-time notifications
4. **Review**: Evaluate generated context and analysis results
5. **Execute**: Implement recommendations from workflow

**Complete operation guide**: `docs/core/usage-instructions.md`

### Enhanced Integration Features
- **TodoWrite Behavioral System**: Automatic validation and workflow memory → `docs/commands/todowrite-system.md`
- **User Customization Engine**: Adaptive personalization system → `docs/core/user-customization.md`
- **Cross-reference FMEA**: Risk assessment with RPN scoring → `docs/matrix/cross-reference-framework.md`

---

**CRITICAL**: This system operates through slash command execution only. All functionality accessed via `/command-name` with autocontained cross-command integration.