# Explore Code - Claude Code Slash Command

## 🎯 Purpose
Specialized tool for exploring and finding relevant information in the codebase based on user queries.

## 🚀 Usage
Execute: `/explore-code [search-description]`

## 🔧 Implementation

### Instructions for Claude Code
When executing this command:

1. **Analyze User Request**: Extract main keywords from description and identify relevant file types
2. **Execute Search Strategy**: Use Glob and Grep tools to discover relevant files and patterns
3. **Content Analysis**: Examine discovered files for contextual relevance to user query
4. **Pattern Recognition**: Identify relationships and connections between discovered elements
5. **Output Persistence**: Analyze execution results for semantic patterns, discover natural groupings, and persist to `output/[discovered-pattern].md`

### Search Strategy Process
1. **Keyword Extraction**: Parse search description for technical terms and concepts
2. **File Type Identification**: Determine appropriate file extensions and directories to search
3. **Multi-Level Search**: Combine filename patterns with content searches for comprehensive coverage
4. **Context Discovery**: Read relevant files to understand implementation patterns and relationships
5. **Result Synthesis**: Organize findings into coherent summary with actionable insights

### Search Examples
- **Configuration**: "database config" → Find config files, environment variables, database connections
- **Authentication**: "auth functions" → Locate authentication logic, user management, security patterns
- **UI Components**: "UI components" → Discover React/Vue components, styling, component architecture
- **Error Handling**: "error handling" → Find error classes, exception handling, logging patterns

### Analysis Approach
- **Discovery-Based**: Use exploration tools to find patterns without predetermined assumptions
- **Contextual**: Provide relevant code snippets and file locations
- **Comprehensive**: Search both filenames and file contents for complete coverage
- **Structured**: Organize results by logical groupings (files, patterns, relationships)

### Output Format
```
🎯 [EXPLORE-CODE] Query: [search-description] | Results: [count] files found
📂 Locations: [relevant directories and files]
📋 Patterns: [discovered implementation patterns]
🔗 Relationships: [connections between components]
💡 Insights: [key findings and recommendations]
```

### Universal Rules (See CLAUDE.md)
- **File Rewriting Rule**: For files requiring >5 modifications, use complete rewrite
- **Output Persistence**: Analyze results, discover patterns, persist to output files
- **Anti-Bias Rule**: Never predetermine categories, all organization emerges from content

### ⚡ Triggers

#### Input Triggers (When to activate this command):
- **Context**: User needs to find specific functionality or patterns in codebase
- **Previous**: Before `/validate-file` → Explore codebase to find files for validation
- **Keywords**: find, search, explore, discover, locate, where is, how does

#### Output Triggers (What commands to suggest after):
- **When**: Files discovered → `/validate-file` for specific file analysis
- **Chain**: explore-code → validate-file → manage-commands
- **Success Pattern**: Relevant code found → Suggest deeper analysis or validation of discovered files

---

*Claude Code slash command - intelligent codebase exploration with discovery-based search and contextual analysis*