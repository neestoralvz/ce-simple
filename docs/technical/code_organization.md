# Code Organization Standards

## Derivación de Principios Establecidos  
Basado en user-vision/TRUTH_SOURCE.md: "la estructura de carpetas del proyecto se esta volviendo muy compleja y eso no es bueno, es importante entender que nos debemos de mantener simples, pragmaticos, funcionales, lean, ligero" [L1:31] y "Algo que veo que estas haciendo y que es uno mas de los principios que dbeemos de respetar es el que los comandos son autocontenidos entre ellos y solo pueden conectarse con otros comandos" [L1:25].

## Research Actualizado (July 28, 2025)

### Industry Best Practices
**Core Organization Principles for 2025**:
- **Outcome-driven rules**: Function names should clearly explain intention with consistent naming conventions
- **Single Responsibility**: Ideally, a single function should carry out a single task - avoid lengthy functions
- **DRY Principle**: Don't repeat yourself - automate repetitive tasks, same code should not be repeated
- **Avoid Deep Nesting**: Too many nesting levels make code harder to read and follow
- **Meaningful Names**: Choose names that convey purpose of variable or function for clarity and maintainability

**Directory Structure Standards**:
- Organize code into blocks or functions separated by whitespace with comments clarifying purpose
- Group related code into modules or packages for better organization and maintainability  
- Proper organization of files and folders is crucial for maintenance and readability
- Organize code into folders that reflect different components or modules

### Official Implementation Standards
**Command Line Tool Organization Patterns (2025)**:
- **CLI Tool File Organization**: Python CLI tools organize files by extension over 27+ file type categories
- **Directory Navigation**: Focus on automation, pattern recognition, and efficient navigation for large file collections
- **Pattern-Based Searching**: Modern tools emphasize fuzzy finding, recursive directory searching, and regex pattern matching
- **Clean Architecture**: For larger applications, adopt layered architecture separating concerns for easier testing and maintenance

## Implementación Técnica Sintetizada

### Project Structure Autorizada

#### Root Level Organization
```
ce-simple/
├── .claude/                    # Claude Code configuration
│   └── commands/               # 9 independent command workflows
├── user-vision/                # TRUTH_SOURCE authority + layers
│   ├── raw/conversations/      # Raw conversation history
│   ├── layer1/                 # Theme cores with direct quotes
│   ├── layer2/                 # Relationship synthesis
│   ├── layer3/                 # Official documentation
│   └── TRUTH_SOURCE.md         # Supreme consolidated authority
├── docs/                       # Technical complementary modules
│   ├── core/                   # Core methodology & architecture
│   ├── workflows/              # Command coordination & patterns
│   ├── maintenance/            # System health & updates
│   └── technical/              # LLM implementation guidance
├── handoff/                    # Cross-session continuity
├── CLAUDE.md                   # Ultra-dense dispatcher (≤200 lines)
└── [project-specific files]
```

#### Principios de Organización

**Jerarquía de Autoridad**:
```
TRUTH_SOURCE.md → CLAUDE.md → docs/ → commands/ → system files
```

**Separación de Responsabilidades**:
- **user-vision/**: User voice preservation + vision distillation
- **docs/**: Technical implementation guidance
- **.claude/commands/**: Pure executable workflows
- **handoff/**: Session state management

### File Naming Conventions

#### Consistent Naming Standards
```bash
# Files: lowercase with underscores
implementation_standards.md
error_handling.md
stack_requirements.md

# Directories: lowercase with hyphens when multi-word
user-vision/
.claude/
docs/

# Commands: lowercase single words
start.md
distill.md
maintain.md

# Variables in bash: ALLCAPS with underscores
COMMAND_NAME="example"
OUTPUT_PATH="/path/to/file"
PROJECT_ROOT="/Users/nalve/ce-simple"
```

#### File Size Guidelines
```bash
# Size limits based on TRUTH_SOURCE principles
CLAUDE_MD_LIMIT=200          # Ultra-dense dispatcher
COMMAND_LIMIT=100            # Individual workflows  
TECHNICAL_DOC_LIMIT=150      # Implementation guides
USER_VISION_NO_LIMIT=true    # Preserve complete voice
```

### Directory Access Patterns

#### Safe Path Management
```bash
# Always use absolute paths in scripts
PROJECT_ROOT="/Users/nalve/ce-simple"
DOCS_PATH="$PROJECT_ROOT/docs"
COMMANDS_PATH="$PROJECT_ROOT/.claude/commands"
USER_VISION_PATH="$PROJECT_ROOT/user-vision"

# Path validation function
validate_project_path() {
    local path="$1"
    [[ "$path" =~ ^/Users/nalve/ce-simple/ ]] || {
        echo "ERROR: Path outside project scope: $path" >&2
        exit 1
    }
}

# Safe directory operations
create_docs_structure() {
    local base_path="$PROJECT_ROOT/docs"
    mkdir -p "$base_path"/{core,workflows,maintenance,technical}
}
```

### Module Organization Standards

#### Command Independence Architecture
```bash
# Each command is self-contained
# .claude/commands/example.md structure:

#!/usr/bin/env bash
# Command: example
# Purpose: [single line description]
# Authority: user-vision/TRUTH_SOURCE.md

# 1. Authority validation
validate_authority() {
    [[ -f "$PROJECT_ROOT/user-vision/TRUTH_SOURCE.md" ]] || exit 1
}

# 2. Single responsibility logic
execute_main_task() {
    # Implementation focused on ONE specific task
    echo "Executing single responsibility task"
}

# 3. Clean output
main() {
    validate_authority
    execute_main_task
}
```

#### Dependency Management
```bash
# Zero external dependencies principle
check_system_dependencies() {
    local required_tools=("bash" "git" "rg" "find")
    for tool in "${required_tools[@]}"; do
        command -v "$tool" >/dev/null || {
            echo "ERROR: Required tool not found: $tool" >&2
            exit 1
        }
    done
}

# Internal dependency pattern
source_internal_utilities() {
    # Only source from within project
    local util_file="$PROJECT_ROOT/docs/technical/common_utils.sh"
    [[ -f "$util_file" ]] && source "$util_file"
}
```

### Content Organization Rules

#### Information Hierarchy
```markdown
# Document structure standard

## Authority Reference
[Required TRUTH_SOURCE.md citation]

## Research Section (when applicable)
[WebSearch + Context7 MCP findings]

## Implementation Details
[Technical specifics aligned with vision]

## References
[Internal project references only]
```

#### Anti-Duplication Pattern
```bash
# Reference, don't repeat content
create_reference_link() {
    local target_file="$1"
    local reference_text="→ Ver $target_file para detalles completos"
    echo "$reference_text"
}

# Avoid content duplication
avoid_duplication() {
    # GOOD: Reference existing content
    echo "→ Ver docs/core/principles.md línea 15-20"
    
    # BAD: Copy content from other files
    # Don't repeat existing content
}
```

### File Maintenance Standards

#### Clean Regeneration Process
```bash
# Based on TRUTH_SOURCE principle of clean slate regeneration
regenerate_clean_file() {
    local file_path="$1"
    local temp_file="${file_path}.tmp"
    
    # Generate completely new content
    generate_from_vision > "$temp_file"
    
    # Replace only if generation successful
    [[ -s "$temp_file" ]] && mv "$temp_file" "$file_path"
}

# Prevent incremental bias accumulation
detect_bias_accumulation() {
    local file="$1"
    local line_count=$(wc -l < "$file")
    local complexity_score=$(grep -c "TODO\|FIXME\|HACK" "$file")
    
    [[ $((line_count + complexity_score)) -gt 200 ]] && {
        echo "WARNING: File may need clean regeneration: $file" >&2
    }
}
```

#### Version Control Integration
```bash
# Git workflow for organized structure
maintain_clean_history() {
    # Stage by logical groups
    git add user-vision/
    git commit -m "Vision: [specific change]"
    
    git add docs/
    git commit -m "Docs: [technical update]"
    
    git add .claude/commands/
    git commit -m "Commands: [workflow update]"
}
```

### Access Control Patterns

#### Read/Write Permissions
```bash
# Different directories have different access patterns
USER_VISION_WRITE=false      # Only through conversation distillation
DOCS_WRITE=true             # Technical implementation updates
COMMANDS_WRITE=true         # Workflow modifications
CLAUDE_MD_WRITE=limited     # Only through validation process

# Permission validation
validate_write_access() {
    local file_path="$1"
    case "$file_path" in
        */user-vision/*)
            [[ "$CONTEXT" == "distillation" ]] || {
                echo "ERROR: user-vision/ only writable during distillation" >&2
                exit 1
            }
            ;;
        */CLAUDE.md)
            [[ "$CONTEXT" == "validation" ]] || {
                echo "ERROR: CLAUDE.md requires validation context" >&2
                exit 1
            }
            ;;
    esac
}
```

## Referencias a Autoridad
- user-vision/TRUTH_SOURCE.md líneas 64-65: Complejidad estructural warning
- user-vision/TRUTH_SOURCE.md líneas 66-67: Comandos autocontenidos principle  
- user-vision/TRUTH_SOURCE.md líneas 72-74: Clean slate regeneration methodology
- user-vision/TRUTH_SOURCE.md líneas 147-149: Anti-duplication reference-only principle
- docs/core/architecture.md: Estructura modular minimalista
- Industry Research: 2025 code organization standards emphasizing outcome-driven rules and clean architecture