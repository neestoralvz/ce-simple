# /actions:setup - Project Context Structure Auto-Setup

**LOAD:** /modules:context_templates + /modules:setup_validation

You are the project initialization command. Your job is to create the complete context structure that allows global commands to work with local project context.

## Core Function

Detect if project has context structure, and if not, create it automatically with all required files and directories.

## Auto-Detection Logic → /modules:setup_validation

## Setup Process

### Phase 1: Directory Structure Creation
Create the complete directory structure:

```
context/
├── operational/
│   ├── patterns/
│   ├── behaviors/
│   ├── enforcement/
│   └── operations/
├── system/
│   └── templates/
└── archive/
user-vision/
├── raw/
└── processed/
planning/
sessions/
```

### Phase 2: Core Context Files Generation

**@context/architecture/core/truth-source.md** - Project Authority Dispatcher:
```markdown
# @context/architecture/core/truth-source.md - Project Authority Dispatcher

**PROJECT**: [Detect project name from directory/README.md]
**PURPOSE**: [Extract from README.md or prompt user]

## AUTORIDAD SUPREMA
@context/architecture/core/truth-source.md → sobrescribe → todo lo demás

## PROJECT VISION
[To be filled during project evolution]

## CORE PRINCIPLES
- Simplicity over complexity
- Working software over comprehensive documentation  
- User needs over technical elegance
- Conversation-first development

## DECISION FRAMEWORK
Authority hierarchy: User vision → Project requirements → Technical constraints → Implementation details

## CONTEXT ARCHITECTURE
This project uses global commands with local context awareness.
All decisions trace back to this authority source.

---
**Evolution**: This file grows through project conversations and decisions.
```

**Template Sources** → /modules:context_templates

### Phase 3: CLAUDE.md Integration

Copy the CLAUDE_LOCAL_TEMPLATE.md to ./CLAUDE.md with project-specific customizations:
- Replace [PROJECT_PURPOSE] with actual project purpose
- Ensure all @context/ references point to created structure
- Validate that global commands can access local context

### Phase 4: Validation → /modules:setup_validation

## Core Function
Seamless integration between global command system and local project context with automatic detection and structure creation

**Success Criteria**: All global commands work with local context + @context/ references resolve + authority hierarchy established