# List Commands - Claude Code Slash Command

## 🎯 Purpose
List all available automation tools in the pragmatic system with current status and counters.

## 🚀 Usage
Execute: `/list-commands`

## 🔧 Implementation

### Instructions for Claude Code
When executing this command:

1. **Discover Available Commands**: Use Glob tool to find all .md files in .claude/commands/ directory
2. **Analyze Command Status**: Read each command file to determine functionality and readiness
3. **Generate Counters**: Count functional vs development commands dynamically
4. **Status Assessment**: Verify system integrity and command availability
5. **Output Persistence**: Analyze execution results for semantic patterns, discover natural groupings, and persist to `output/[discovered-pattern].md`

### Discovery Process
1. **File Discovery**: Scan .claude/commands/ directory for all command files
2. **Content Analysis**: Read each command to extract purpose and functionality status
3. **Status Classification**: Categorize commands as functional, in-development, or planned
4. **Integration Check**: Verify commands follow template structure and standards
5. **Counter Generation**: Provide accurate counts based on discovered data

### System Status Categories
- **Functional Commands**: Ready to use, fully tested, following template structure
- **Commands in Development**: Under construction, partial functionality
- **Planned Commands**: Documented but not yet implemented
- **System Counters**: General status and metrics

### Output Content
1. **Current Status Summary**: Overview of system state and command availability
2. **Functional Commands List**: Commands ready for immediate use
3. **Development Pipeline**: Commands currently under construction
4. **System Metrics**: Counters and statistics
5. **Next Steps**: Planned command development

### Output Format
```
🎯 [LIST-COMMANDS] System Status: ✅ OPERATIONAL
📊 Commands Functional: [count] | In Development: [count] | Planned: [count]
📋 Active Commands: [list of functional commands]
🚧 Development: [commands under construction]
📅 Planned: [next commands in pipeline]
💡 System Health: [overall system status and recommendations]
```

### Universal Rules (See CLAUDE.md)
- **File Rewriting Rule**: For files requiring >5 modifications, use complete rewrite
- **Output Persistence**: Analyze results, discover patterns, persist to output files
- **Anti-Bias Rule**: Never predetermine categories, all organization emerges from content

### ⚡ Triggers

#### Input Triggers (When to activate this command):
- **Context**: User needs overview of available automation tools
- **Previous**: After `/ss` → Show system status and available commands
- **Keywords**: list, show, commands, available, status, overview

#### Output Triggers (What commands to suggest after):
- **When**: Commands listed → `/manage-commands` for detailed command management
- **Chain**: ss → list-commands → manage-commands
- **Success Pattern**: System overview provided → Suggest specific command usage or management

---

*Claude Code slash command - dynamic system status and command availability overview*