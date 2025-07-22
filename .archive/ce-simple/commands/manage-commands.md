# Manage Commands - Claude Code Slash Command

## 🎯 Purpose
Comprehensive command management tool for exploring, analyzing, editing, and maintaining the entire commands ecosystem with automated optimization and quality assurance.

## 🚀 Usage
Execute: `/manage-commands [action] [target]`

## 🔧 Implementation

### Instructions for Claude Code
When executing this command:

1. **Parse Action**: Identify requested action (explore, analyze, edit, optimize, validate, reorganize)
2. **Discovery Phase**: Use Task tool deployment for pure discovery without assumptions
3. **Semantic Analysis**: Analyze discovered patterns for natural semantic groupings
4. **Execute Action**: Perform requested operation based on discovered data
5. **Output Persistence**: Analyze execution results for semantic patterns, discover natural groupings, and persist to `output/[discovered-pattern].md`

**ANTI-BIAS PRINCIPLE**: Every action uses pure discovery via exploration tools. ZERO predetermined assumptions about commands, categories, or patterns.

### Available Actions

**explore**: List and analyze all available commands
- Deploy `/explore-code` to discover command purposes
- Find command-to-command relationships dynamically
- Analyze current directory organization

**analyze [command-name]**: Deep analysis of specific command
- Examine command structure and compliance
- Identify optimization opportunities
- Check integration patterns

**edit [command-name]**: Interactive editing of command structure
- Apply template standardization
- Update to current standards
- Maintain functionality while improving structure

**optimize**: System-wide command optimization
- Identify redundancies and improvements
- Suggest consolidation opportunities
- Enhance performance patterns

**validate**: Validate all commands for standards compliance
- Check template adherence
- Verify Universal Rules implementation
- Identify non-compliant commands

**reorganize**: Organize commands into categorized subdirectories
- Discover natural command groupings
- Create semantic directory structure
- Maintain command accessibility

### Output Format
```
🎯 [MANAGE-COMMANDS] Action: [action] | Target: [target] | Status: ✅ COMPLETED
📊 Discovery: [discovered patterns and relationships]
📋 Analysis: [semantic analysis results]
🔧 Actions Taken: [specific operations performed]
💡 Recommendations: [optimization suggestions]
```

### Universal Rules (See CLAUDE.md)
- **File Rewriting Rule**: For files requiring >5 modifications, use complete rewrite
- **Output Persistence**: Analyze results, discover patterns, persist to output files
- **Anti-Bias Rule**: Never predetermine categories, all organization emerges from content

### ⚡ Triggers

#### Input Triggers (When to activate this command):
- **Context**: User needs comprehensive command management operations
- **Previous**: After `/list-commands` → Manage discovered commands
- **Keywords**: manage, organize, analyze, optimize, maintain, edit commands

#### Output Triggers (What commands to suggest after):
- **When**: Analysis completed → `/validate-file` for specific command validation
- **Chain**: manage-commands → validate-file → sync-docs
- **Success Pattern**: Management operation completed → Suggest system synchronization

---

*Claude Code slash command - comprehensive command ecosystem management with discovery-based optimization*