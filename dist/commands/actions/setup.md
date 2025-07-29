# /actions:setup - Project Context Structure Auto-Setup

You are the project initialization command. Your job is to create the complete context structure that allows global commands to work with local project context.

## Core Function

Detect if project has context structure, and if not, create it automatically with all required files and directories.

## Auto-Detection Logic

### Check Current State
```bash
# Primary detection
if [ ! -d "./context" ]; then
    echo "No context structure detected - initializing project"
    setup_required=true
else
    echo "Context structure exists - validating completeness"
    setup_required=false
fi

# Secondary validation
required_files=(
    "./context/TRUTH_SOURCE.md"
    "./context/operational/patterns/socratic_methodology.md"
    "./context/operational/patterns/authority_framework.md"
    "./context/operational/patterns/simplicity_principles.md"
    "./context/operational/behaviors/orchestration_protocol.md"
)

missing_files=()
for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        missing_files+=("$file")
        setup_required=true
    fi
done
```

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
├── conversations/
└── processed/
planning/
sessions/
```

### Phase 2: Core Context Files Generation

**context/TRUTH_SOURCE.md** - Project Authority Dispatcher:
```markdown
# TRUTH_SOURCE.md - Project Authority Dispatcher

**PROJECT**: [Detect project name from directory/README.md]
**PURPOSE**: [Extract from README.md or prompt user]

## AUTORIDAD SUPREMA
context/TRUTH_SOURCE.md → sobrescribe → todo lo demás

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

**context/operational/patterns/socratic_methodology.md** - Basic version:
```markdown
# Socratic Methodology - Project Discovery

## Core Principle
Conversation-first discovery → Command execution
Deep dialogue before implementation decisions

## Discovery Triggers
- Intent ambiguity detected → Activate socratic questioning
- User story unclear → Deep conversational exploration  
- Requirements fuzzy → Mayeutic dialogue mandatory
- Complex decisions → Challenge methodology activation

## Application
Use this when requirements are unclear or decisions need validation.
Always explore "why" before "how".
```

### Phase 3: CLAUDE.md Integration

Copy the CLAUDE_LOCAL_TEMPLATE.md to ./CLAUDE.md with project-specific customizations:
- Replace [PROJECT_PURPOSE] with actual project purpose
- Ensure all @context/ references point to created structure
- Validate that global commands can access local context

### Phase 4: Validation

After setup, verify:
1. All required directories exist
2. Core context files are readable
3. CLAUDE.md references resolve correctly
4. Global commands can access local context structure

## Command Integration

### Auto-Setup Triggers
This command should be called automatically by other commands when they detect missing context structure.

**Example integration in other commands:**
```markdown
## Context Validation
if [ ! -f "./context/TRUTH_SOURCE.md" ]; then
    echo "Project context missing - running auto-setup"
    # Call /actions:setup
    # Continue with original command after setup
fi
```

### Manual Setup
User can also run `/actions:setup` explicitly to:
- Initialize new project
- Repair missing context structure
- Upgrade existing context to latest standards

## Success Criteria

**Perfect setup when:**
- All global commands work seamlessly with local context
- @context/ references in CLAUDE.md resolve correctly
- Project has working authority hierarchy
- Commands can read/write to appropriate local directories

**Setup validates that:**
- CLAUDE.md loads without errors
- /roles:orchestrator can access context/TRUTH_SOURCE.md
- /actions:build can write to appropriate directories
- Project maintains separation between global commands and local context

Your objective is seamless integration between global command system and local project context, creating a working environment where sophisticated project intelligence operates through portable commands.