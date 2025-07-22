# Get Template - Claude Code Slash Command

## 🎯 Purpose
Provide standardized command template structure for creating consistent, functional Claude Code slash commands with all required sections and variables.

## 🚀 Usage
Execute: `/get-template`

## 🔧 Implementation

### Instructions for Claude Code
When executing this command:

1. **Display Standard Command Template**: Show the complete template structure with all sections
2. **Include Template Variables**: List all available placeholder variables for customization
3. **Show Best Practices**: Display template creation guidelines and standards
4. **Provide Usage Guide**: Explain how to use the template with /create-command
5. **Output Persistence**: Analyze execution results for semantic patterns, discover natural groupings, and persist to `output/[discovered-pattern].md`

### Command Template Structure
```markdown
# [Name] - Claude Code Slash Command

## 🎯 Purpose
[Describe specific practical functionality]

## 🚀 Usage
Execute: `/[command-name]`

## 🔧 Implementation

### Instructions for Claude Code
When executing this command:

1. **[Primary Step]**: [Specific implementation instruction]
2. **[Secondary Step]**: [Additional implementation details]
3. **[Output Step]**: [Result formatting requirements]
4. **[Validation Step]**: [Error handling procedures]
5. **Output Persistence**: Analyze execution results for semantic patterns, discover natural groupings, and persist to `output/[discovered-pattern].md`

### Output Format
```
🎯 [[COMMAND-NAME]] [Result Summary]
📊 [Key metrics or status information]
📋 [Detailed information or findings]
💡 [Suggestions or next steps]
```

### Universal Rules (See CLAUDE.md)
- **File Rewriting Rule**: For files requiring >5 modifications, use complete rewrite
- **Output Persistence**: Analyze results, discover patterns, persist to output files
- **Anti-Bias Rule**: Never predetermine categories, all organization emerges from content

### ⚡ Triggers

#### Input Triggers (When to activate this command):
- **Context**: [Situation requiring this command]
- **Previous**: `/[previous-command]` → [condition leading here]
- **Keywords**: [contextual terms that suggest this command]

#### Output Triggers (What commands to suggest after):
- **When**: [Result condition] → `/[next-command]` for [reason]
- **Chain**: [command1] → [command2] → [command3]
- **Success Pattern**: [Success condition] → [Suggested next action]

---

*Claude Code slash command*
```

### Template Variables Available
- `[Name]` - Capitalized command name for header
- `[command-name]` - Lowercase command name with hyphens
- `[Primary Step]` - Main implementation step
- `[COMMAND-NAME]` - Uppercase command name for output format
- `[previous-command]` - Input trigger command
- `[next-command]` - Output trigger command

### Template Creation Best Practices
1. **Clear Purpose**: Single, specific functionality per command
2. **Self-Contained**: Only reference other commands, never external files
3. **Immediate Value**: Useful from first execution
4. **Standard Format**: Follow exact template structure
5. **Pragmatic Focus**: Practical functionality over theoretical perfection

### Output Format
```
📄 [GET-TEMPLATE] Template: ✅ READY
📋 Template Structure: Complete with all required sections
🔧 Variables: 6 placeholders available for customization
📊 Sections: Purpose, Usage, Implementation, Triggers
💡 Next Step: Use template with /create-command [name]
```

### Universal Rules (See CLAUDE.md)
- **File Rewriting Rule**: For files requiring >5 modifications, use complete rewrite
- **Output Persistence**: Analyze results, discover patterns, persist to output files
- **Anti-Bias Rule**: Never predetermine categories, all organization emerges from content


### ⚡ Triggers

#### Input Triggers (When to activate this command):
- **Context**: User needs command template structure or creation guidance
- **Previous**: Before `/create-command` → Get template structure first
- **Keywords**: template, structure, format, standard, example, create command

#### Output Triggers (What commands to suggest after):
- **When**: Template provided → `/create-command [name]` for implementation
- **Chain**: get-template → create-command → validate-file
- **Success Pattern**: Template displayed → Suggest command creation with specific name

---

*Claude Code slash command - standardized template provider for consistent command structure*