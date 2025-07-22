# Create Command - Claude Code Slash Command

## 🎯 Purpose
Create structured automation templates with standardized format, automatic documentation updates, and advanced intent-based trigger system.

## 🚀 Usage
Execute: `/create-command [command-name]`

## 🔧 Implementation

### Instructions for Claude Code
When executing this command:

1. **Validate Command Name**: Verify name format (letters, numbers, hyphens only) and uniqueness
2. **Create Command File**: Generate `.claude/commands/[name].md` using standardized template from `/get-template`
3. **Update CLAUDE.md**: Add new command to "Functional Commands" section with status "✅ READY"
4. **System Synchronization**: Update command counters and lists via `/list-commands`
5. **Output Persistence**: Analyze execution results for semantic patterns, discover natural groupings, and persist to `output/[discovered-pattern].md`

**ANTI-BIAS REQUIREMENT**: New commands MUST use discovery-based logic via exploration tools. NEVER include predetermined assumptions, hardcoded categories, or fixed patterns in command implementations.

### Template Application Process
1. **Get Template**: Use `/get-template` for current standardized structure
2. **Replace Variables**: Substitute all placeholder variables with actual content
3. **Validate Structure**: Ensure all required sections are present and properly formatted
4. **Test Functionality**: Verify command works as expected

### Output Format
```
📊 [CREATE-COMMAND] Command: /[name] | Status: ✅ CREATED
📁 File: [name].md created successfully
📋 CLAUDE.md: Updated with new entry
📄 /list-commands: Counters and lists updated
🧠 Intent System: Smart triggers configured
🔧 System synchronized: Available commands updated
🚀 Next step: Implement specific functionality
```

### Universal Rules (See CLAUDE.md)
- **File Rewriting Rule**: For files requiring >5 modifications, use complete rewrite
- **Output Persistence**: Analyze results, discover patterns, persist to output files
- **Anti-Bias Rule**: Never predetermine categories, all organization emerges from content

### ⚡ Triggers

#### Input Triggers (When to activate this command):
- **Context**: User needs to create new automation command
- **Previous**: `/get-template` → Get template structure first
- **Keywords**: create, generate, new, make, build, automate, command, tool

#### Output Triggers (What commands to suggest after):
- **When**: Command created successfully → `/sync-docs` for documentation update
- **Chain**: create-command → sync-docs → validate-file
- **Success Pattern**: Template applied → Suggest command implementation and testing

---

*Claude Code slash command - standardized automation template creation with intelligent intent recognition*