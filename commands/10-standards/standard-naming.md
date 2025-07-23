# Naming Standards - Consistent Conventions

**Purpose**: Standardized naming conventions ensuring system-wide consistency

## Core Principles

**Verbo-Sustantivo Pattern**: Use verb-noun structure for all commands and functions
- Format: `action-target` (e.g., analyze-performance, create-component)
- Clarity: Immediately conveys what action is performed on what target
- Consistency: Uniform pattern across entire system

**Type-Based Consistency**: Apply consistent naming within each category
- Commands: verb-noun with hyphens
- Files: lowercase with hyphens  
- Directories: lowercase with hyphens
- Variables: camelCase for code, kebab-case for configs

## Command Naming

### Format: `/verb-noun`
**Structure**: Action verb + target noun, connected by hyphen

**Examples**:
- `/analyze-performance` - Analyze system performance
- `/create-component` - Create new component
- `/optimize-context` - Optimize context usage
- `/maintain-commands` - Maintain command system

### Verb Selection
**Discovery Actions**: explore, analyze, assess, investigate
**Creation Actions**: create, generate, build, develop  
**Maintenance Actions**: maintain, optimize, update, cleanup
**Management Actions**: monitor, track, coordinate, orchestrate

### Noun Selection
**System Targets**: commands, context, system, matrix
**Code Targets**: components, functions, modules, patterns
**Process Targets**: workflow, tasks, operations, sessions

## File Naming

### Documentation Files
**Format**: `topic-type.md`
- `command-standards.md` - Standards for commands
- `context-system.md` - Context system documentation
- `orchestration-details.md` - Detailed orchestration guide

### Template Files  
**Format**: `template-purpose.md`
- `template-command.md` - Command creation template
- `template-docs.md` - Documentation template

### Implementation Files
**Format**: `verb-noun.md` (matching command names)
- `analyze-performance.md` - Performance analysis implementation
- `create-component.md` - Component creation implementation

## Directory Naming

### Organizational Structure
**Format**: `##-category/` (numbered for ordering)
- `00-core/` - Core system components
- `10-standards/` - Standards and templates
- `14-utils/` - Utility functions

### Content-Based Structure
**Format**: `category/` (descriptive grouping)
- `commands/` - Executable commands
- `docs/` - Documentation files
- `templates/` - Template files

## Variable Naming

### Code Variables
**camelCase**: For internal code variables
- `taskManager`, `contextEngine`, `orchestrationStrategy`

### Configuration Variables
**kebab-case**: For configuration and parameter names
- `max-parallel-tasks`, `context-timeout`, `validation-mode`

## Validation Examples

### Correct Naming
```
Commands: /analyze-codebase, /create-workflow, /optimize-performance
Files: command-standards.md, context-system.md, template-docs.md
Directories: 10-standards/, commands/, docs/templates/
Variables: taskOrchestrator (code), max-task-limit (config)
```

### Incorrect Naming
```
Commands: /analyzeCodebase, /CreateWorkflow, /optimize_performance
Files: CommandStandards.md, context_system.md, templateDocs.md
Directories: Standards/, Commands/, Docs/Templates/
Variables: task_orchestrator (code), maxTaskLimit (config)
```

## Validation Checklist

- [ ] Commands use verb-noun pattern with hyphens
- [ ] Files use lowercase with hyphens
- [ ] Directories use consistent organizational scheme
- [ ] Variables follow camelCase (code) or kebab-case (config)
- [ ] Names clearly indicate purpose and scope
- [ ] Consistent patterns within each category