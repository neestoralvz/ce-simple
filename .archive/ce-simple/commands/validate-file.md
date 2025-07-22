# Validate File - Claude Code Slash Command

## 🎯 Purpose
Validate file structure and content against practical quality criteria.

## 🚀 Usage
Execute: `/validate-file`

The command will validate:
1. **Basic structure** - File exists and is readable
2. **Pragmatic size** - <200 lines (cognitive limit)
3. **Useful content** - No empty files or comment-only files
4. **Basic format** - Appropriate extension for content

## 🔧 Implementation

### Instructions for Claude Code
When executing this command:

1. **Read specified file** using Read tool
2. **Verify basic criteria**:
   - File exists and is accessible
   - Size ≤200 lines 
   - Non-empty content (>10 useful characters)
   - Extension matches apparent content

3. **Report result**:
   - ✅ **VALID**: File meets pragmatic criteria
   - ⚠️ **WARNING**: Minor issues identified  
   - ❌ **INVALID**: Critical problems found

4. **Include metrics**: Lines, characters, problems found

### Validation Criteria
- **Cognitive size**: ≤200 lines
- **Useful content**: >10 non-whitespace characters
- **Basic structure**: Recognizable format
- **Accessibility**: Readable and processable

### Output Format
```
📊 [VALIDATE-FILE] File: [name] | Lines: [X] | Status: [VALID/WARNING/INVALID]
📋 Details: [problem description/confirmation]
💡 Suggestion: For files with >5 problems, consider complete rewrite
```

### Universal Rules (See CLAUDE.md)
- **File Rewriting Rule**: For files requiring >5 modifications, use complete rewrite
- **Output Persistence**: Analyze results, discover patterns, persist to output files
- **Anti-Bias Rule**: Never predetermine categories, all organization emerges from content

### ⚡ Triggers
Claude Code slash command integration patterns

#### Input Triggers (When to activate this command):
- **Context**: User needs to verify quality of specific file
- **Previous**: `/explore-code` → Found files require validation
- **Keywords**: validate, verify, review, check, assess

#### Output Triggers (What commands to suggest after):
- **When**: Problems detected in file
- **Suggest**: [Future `/quick-fix` for repairs]
- **Chain**: explore-code → validate-file → quick-fix

---

*Claude Code slash command - rapid file validation and quality assessment*