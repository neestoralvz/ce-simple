# CLAUDE.md - Simplified Commands System

**Last Updated: 2025-07-22**

## 🎯 SYSTEM OVERVIEW

**ce-simple**: Streamlined command system for Claude Code enabling efficient context engineering through intelligent workflow orchestration and agent deployment.

**Core Philosophy**: Pragmatic effectiveness, autocontained commands, LLM optimized, anti-bias processing → `docs/system/architectural-principles.md`

## 🚫 FILE CREATION RESTRICTIONS

**CRITICAL**: Anti-proliferation protocol to prevent documentation bloat

### Prohibited File Creation:
- ❌ **NO context/ file generation** - System must NOT create files in context/ directories
- ❌ **NO date-stamped files** - Ban automatic date-based file naming (YYYY-MM-DD patterns)
- ❌ **NO meta-documentation** - No files documenting the documentation system itself
- ❌ **NO "health reports"** or "matrix analysis" files
- ❌ **NO behavioral pattern documentation** - System self-analysis forbidden

### Required Behavior:
- ✅ **UPDATE existing files** instead of creating new ones
- ✅ **User value threshold** - Files must serve direct user needs only
- ✅ **Consolidation over creation** - Merge related content into existing files

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

### System Maintenance
- **`/matrix-maintenance`** - Cross-reference matrix validation and system integrity monitoring

### System Standards
Commands follow integrated standards → `docs/documentation/writing-standards.md`, `docs/workflow/workflow-notifications.md`, `docs/quality/anti-bias-rules.md`, `docs/command/command-template.md`

## 🔧 WORKFLOW INTEGRATION

### Primary Discovery Flow
```
⟳ /start → dynamic questions → /explore-codebase + /explore-web → /think-layers → execution plan → /capture-learnings
├─ /matrix-maintenance → Cross-reference validation (periodic)
```

**Complete workflow details**: `docs/workflow/primary-discovery-flow.md`

### Intelligence Parallelization Protocol
**MANDATORY**: Autocontained analysis → optimization → aggressive execution
- **Dynamic WebSearches** (4-16 based on topic complexity)
- **Adaptive codebase operations** (12-52 based on project size)
- **Message-level optimization** - maximize efficiency through intelligent batching

**Detailed specifications**: `docs/implementation/aggressive-parallelization-protocol.md`

## 🎯 IMPLEMENTATION READY

### System Status
- ✓ **Command Structure**: Core commands implemented and cross-referenced
- ✓ **Standards Framework**: Writing, notification, and anti-bias protocols established
- ✓ **Workflow Integration**: Discovery-to-execution pipeline operational
- ✓ **Context Architecture**: Structured documentation and pattern storage

### Usage Instructions
1. **Initialize**: Execute `/start` with initial request
2. **Respond**: Answer dynamic discovery questions for context clarification
3. **Monitor**: Track progress through real-time notifications
4. **Review**: Evaluate generated context and analysis results
5. **Execute**: Implement recommendations from workflow

**Complete operation guide**: `docs/system/usage-instructions.md`

---

**CRITICAL**: This system operates through slash command execution only. All functionality accessed via `/command-name` with autocontained cross-command integration.