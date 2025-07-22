# Validate Principles - Claude Code Slash Command

## 🎯 Purpose
Validate adherence to project principles and guidelines defined in CLAUDE.md, ensuring alignment with core project values and methodologies for any project.

## 🚀 Usage
Execute: `/validate-principles [target]`

## 🔧 Implementation

### Instructions for Claude Code
When executing this command:

1. **Read CLAUDE.md Dynamically**: Extract current principles without predetermined assumptions
2. **Principle Discovery**: Identify key principle categories through content analysis
3. **Target Analysis**: Analyze specified target against discovered principles
4. **Alignment Assessment**: Check adherence to extracted decision filters and operational criteria
5. **Output Persistence**: Analyze execution results for semantic patterns, discover natural groupings, and persist to `output/[discovered-pattern].md`

### Principle Categories to Validate
- **Pragmatic Principles**: Practical effectiveness over theoretical perfection
- **Decision Filters**: "Is it needed NOW?", "Does it work with minimum?", testability criteria
- **Architectural Rules**: Self-contained commands, anti-bias discovery, executable focus
- **Universal Standards**: Writing requirements, quality standards, iteration methodology
- **Development Methodology**: MVP approach, immediate testing, weekly iteration

### Target Types
- **No parameter**: Validates current working context
- **"project"**: Full project validation against all principles
- **File path**: Specific file validation (e.g., "file.md")
- **Directory path**: Directory validation (e.g., ".claude/commands/")

### Analysis Process
1. **Dynamic Principle Extraction**: Parse CLAUDE.md for current principle definitions
2. **Content Alignment Check**: Validate target content against discovered principles
3. **Methodology Verification**: Ensure adherence to pragmatic development approach
4. **Quality Assessment**: Check compliance with universal standards
5. **Recommendation Generation**: Provide actionable alignment improvements

### Output Format
```
🎯 [VALIDATE-PRINCIPLES] Target: [target] | Status: ✅ ANALYZED
📊 Principle Alignment: [percentage] | Issues Found: [count]
📋 Adherence: [specific principle compliance results]
⚠️ Violations: [identified misalignments with recommendations]
💡 Improvements: [actionable steps for better alignment]
```

### Universal Rules (See CLAUDE.md)
- **File Rewriting Rule**: For files requiring >5 modifications, use complete rewrite
- **Output Persistence**: Analyze results, discover patterns, persist to output files
- **Anti-Bias Rule**: Never predetermine categories, all organization emerges from content

### ⚡ Triggers

#### Input Triggers (When to activate this command):
- **Context**: User needs to verify project principle adherence
- **Previous**: After `/create-command` → Validate new command follows principles
- **Keywords**: validate, principles, adherence, alignment, compliance, guidelines

#### Output Triggers (What commands to suggest after):
- **When**: Violations found → `/writing-standards` for standard compliance
- **Chain**: validate-principles → writing-standards → validate-file
- **Success Pattern**: Alignment verified → Suggest continued development with principle adherence

---

*Claude Code slash command - dynamic principle validation ensuring project alignment and methodology adherence*