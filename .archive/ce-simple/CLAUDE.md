# CLAUDE.md - Pragmatic Commands System

## 🎯 PRAGMATIC SYSTEM

An **executable commands system for Claude Code** that operates with **pragmatic principles: practical effectiveness over theoretical perfection**.

**🤖 YOUR OBJECTIVE**: Create and use simple, functional, and testable commands that provide immediate value.

### Pragmatic Principles:
- **Executable commands** in `.claude/commands/` that work with `/command-name`
- **Self-contained** - commands only reference and call other commands
- **Anti-bias discovery** - commands NEVER predetermine results, ALL patterns discovered dynamically
- **Constant MVP** - each command works in minimum version from day 1
- **Immediate testing** - verifiable in less than 5 minutes
- **Immediate value** - useful from first use
- **Weekly iteration** - one improvement per command per week

## 🚀 PRAGMATIC ARCHITECTURE

### Simple Structure
```
ce-simple/
├── CLAUDE.md                    # Main instructions (this file)
├── system/                     # Pragmatic documentation (3 files)
│   ├── pragmatic-foundation.md # Fundamental principle
│   ├── quick-start.md         # Start in 5 minutes
│   └── working-components.md  # Working commands
├── .claude/commands/          # Executable commands
│   ├── validate-file.md      # /validate-file
│   ├── create-command.md     # /create-command
│   ├── ss.md                 # /ss (start-system)
│   ├── list-commands.md      # /list-commands
│   ├── explore-code.md       # /explore-code
│   ├── writing-standards.md  # /writing-standards
│   ├── sync-docs.md          # /sync-docs
│   ├── manage-commands.md    # /manage-commands
│   ├── validate-principles.md # /validate-principles
│   └── get-template.md       # /get-template
└── .archive/                 # Historical reference (hidden)
    ├── system-original/     # Previous theoretical system
    └── components-original/ # 88 components as reference
```

## 🎯 AVAILABLE COMMANDS

### Functional Commands (Use with `/command-name`)

#### `/validate-file` - ✅ READY
- **Purpose**: Validate file structure and content
- **Usage**: `/validate-file [file-name]`
- **Test**: Execute on any file, response in <5 seconds

#### `/create-command` - ✅ READY
- **Purpose**: Create new commands with standardized template
- **Usage**: `/create-command [command-name]`
- **Test**: Create test command, file generated in <10 seconds

#### `/ss` - ✅ READY
- **Purpose**: Activate and begin using the commands system
- **Usage**: `/ss`
- **Test**: Show complete system status in <5 seconds

#### `/list-commands` - ✅ READY
- **Purpose**: List all available commands with counters
- **Usage**: `/list-commands`
- **Test**: Show complete list in <3 seconds

#### `/explore-code` - ✅ READY
- **Purpose**: Explore and search relevant information in codebase
- **Usage**: `/explore-code [search-description]`
- **Test**: Search for configuration files, response in <10 seconds

#### `/writing-standards` - ✅ READY
- **Purpose**: Establish and verify consistent writing standards
- **Usage**: `/writing-standards [file]`
- **Test**: Execute on any file, analysis in <5 seconds

#### `/sync-docs` - ✅ READY
- **Purpose**: Maintain system documentation synchronized and coherent
- **Usage**: `/sync-docs`
- **Test**: Execute and verify complete synchronization in <10 seconds

#### `/manage-commands` - ✅ READY
- **Purpose**: Comprehensive command management tool for exploring, analyzing, editing commands
- **Usage**: `/manage-commands [action] [target]`
- **Test**: Execute `/manage-commands explore`, complete command inventory in <5 seconds

#### `/validate-principles` - ✅ READY
- **Purpose**: Validate adherence to project principles and guidelines defined in CLAUDE.md
- **Usage**: `/validate-principles [target]`
- **Test**: Execute `/validate-principles CLAUDE.md`, principle alignment analysis in <5 seconds

#### `/get-template` - ✅ READY
- **Purpose**: Provide standardized command template structure for consistent command creation
- **Usage**: `/get-template`
- **Test**: Execute `/get-template`, complete template displayed in <5 seconds

### Planned Commands (Next weeks)
- `/analyze-simple` - Basic content analysis
- `/quick-fix` - Common automatic repairs

## 📋 UNIVERSAL COMMAND RULES

### File Rewriting Rule
**When to apply**: For files requiring >5 modifications, use complete rewrite for optimal structure and comprehensive improvement.

### Output Persistence
**File Creation**: Create/update `output/[discovered-pattern].md` based on dynamic content analysis
**Pattern Discovery**: Analyze execution results to discover natural semantic groupings without predetermined categories
**Implementation Steps**:
1. **Content Analysis**: Extract keywords, context, and semantic patterns from execution results
2. **Dynamic Discovery**: Compare with existing output files to identify similar content patterns
3. **File Organization**: Group results by discovered patterns, create new pattern file if no match found
4. **Timestamp Consolidation**: Append results with execution timestamp and maintain historical context

### Anti-Bias Rule
**CRITICAL**: Commands MUST use discovery-based logic via exploration tools. NEVER predetermine file categories or patterns - all organization emerges from actual content analysis.

## 📝 UNIVERSAL WRITING REQUIREMENT

**CRITICAL**: ALWAYS execute `/writing-standards` mentally before creating or modifying ANY file. Apply ALL standards automatically:
- **English language ONLY** - ALL documentation MUST be in English
- **Optimize density and maximum value** - Every element serves specific purpose
- **Use imperative tone** for instructions - Direct, commanding voice
- **Apply technical precision** - Detailed specifications when accuracy required
- **Use CAPITALS for critical instructions** (ALWAYS, NEVER, MUST)
- **Implement import system syntax** when needed (@import[LAZY], @import[LINES])
- **Structure for LLM processing** with clear hierarchy
- **ELIMINATE redundancy** while preserving function

**NO EXCEPTIONS**: Every file creation/modification MUST comply with these standards without asking for permission.

## 📋 FUNDAMENTAL PRINCIPLE

See: `system/pragmatic-foundation.md`

**"Practical effectiveness over theoretical perfection"**

### Decision Filters:
- **Is it needed NOW?** → If not, do not do it
- **Does it work with minimum?** → If not, simplify
- **Can it be tested easily?** → If not, redesign
- **Does it provide immediate value?** → If not, eliminate
- **Does it discover dynamically?** → If not, remove predetermined assumptions

## 🚀 START NOW

### For Users (3 steps):
1. **Read principle**: `system/pragmatic-foundation.md` (2 minutes)
2. **View commands**: `system/working-components.md` (2 minutes)  
3. **Test command**: `/ss` then `/validate-file CLAUDE.md` (1 minute)

### For Developers:
1. **Create command**: File `[name].md` for command `/[name]`
2. **Follow template**: Purpose + Usage + Test + Implementation + Triggers
3. **Test immediately**: MUST work in <5 minutes
4. **Iterate weekly**: One improvement per week

### CENTRAL RULES:
1. **Nomenclature**: File name = command name (without slash)
2. **Self-containment**: Commands only reference other commands (`/command-name`)
3. **Closed ecosystem**: Commands call each other, never external files
4. **Triggers system**: Commands define dynamic connections between them

## ⚡ TRIGGERS SYSTEM

### Universal Structure for Commands Connection
Each command includes **Triggers** section that defines:

#### Input Triggers (When to activate):
- **Context**: Situation requiring this command
- **Previous**: Previous command → condition leading here
- **Keywords**: Flexible contextual terms

#### Output Triggers (What to suggest next):
- **When**: Specific result condition
- **Suggest**: Next command with contextual parameters
- **Chain**: Typical workflow (command1 → command2 → command3)

### System Benefits:
- **Dynamic**: Each command defines its own connections
- **Contextual**: Suggestions based on real results
- **Scalable**: Easy to add new connections
- **Natural flows**: Automated work chains

## 📊 REFERENCES

### Historical Knowledge (Reference only)
- **Previous system**: `.archive/system-original/` - Complete theoretical system
- **Historical components**: `.archive/components-original/` - 88 components as inspiration
- **Use as reference**, NOT as direct implementation
- **Principle**: Executable functionality before elegant theory

### Current Documentation
- **Principle**: `system/pragmatic-foundation.md`
- **Quick start**: `system/quick-start.md`
- **Active commands**: `system/working-components.md`
- **Implemented commands**: `.claude/commands/`

---

**Pragmatic system: simple, functional, executable, iterative**