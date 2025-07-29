# Stack Requirements & Dependencies

## Derivación de Principios Establecidos
Basado en user-vision/TRUTH_SOURCE.md: "no te voy a decir como hacer las cosas, tu debes de decidirlo de acuerdo a mi vision y lo que te digo" [L1:67] y "Solo usar herramientas que ya están en el sistema o que Claude Code provee" [Sistema Simple].

## Research Actualizado (July 28, 2025)

### Industry Best Practices
**CLI Design Evolution**: CLI design has evolved from machine-first to human-first interfaces, updating traditional UNIX principles for the modern day. Today's command line is human-first: a text-based UI that affords access to all kinds of tools, systems and platforms.

**Core Requirements for 2025**:
- Functionality first with proper error handling
- Authentication via OAuth patterns with browser launch
- Layered validation starting with format progressing to semantic
- Support for commonly used output modifiers and color/no-color options
- Keep output lines under 80 characters where possible

### Official Implementation Standards
**Bash Scripting Modern Standards (2025)**:
- **Shebang**: Use `#!/usr/bin/env bash` over direct paths for better portability
- **Strict Mode**: Always start scripts with strict mode settings for early error detection
- **Google Style Influence**: Scripts under 50 lines, emphasizing simplicity and maintainability
- **Variable Naming**: ALLCAPS format with underscores only for readability
- **Arrays**: Use `"${array[@]}"` quoted expansion to avoid quoting issues

## Implementación Técnica Sintetizada

### Stack Tecnológico Autorizado

#### Core Languages & Tools
```bash
# Primary Stack
- Bash 5.3+ (latest 2025 standards)
- Markdown (documentation)
- JSON (configuration/data)
- YAML (Claude Code configs only)

# System Tools (already available)
- Claude Code CLI (primary interface)
- Git (version control + coordination)
- ripgrep/rg (code search)
- find/ls (file navigation)
```

#### Bash Standards Implementation
```bash
#!/usr/bin/env bash
# Script header with strict mode
set -euo pipefail  # Error handling, undefined vars, pipe failures
IFS=$'\n\t'        # Safe Internal Field Separator

# Variables: ALLCAPS with underscores
COMMAND_NAME="example"
OUTPUT_PATH="/path/to/output"

# Functions: no 'function' keyword for compatibility
validate_input() {
    [[ -n "$1" ]] || { echo "Parameter required" >&2; exit 1; }
}

# Array usage with proper quoting
COMMANDS=("start" "distill" "docs" "explore")
for cmd in "${COMMANDS[@]}"; do
    echo "Processing: $cmd"
done
```

### Dependency Management

#### Zero External Dependencies
- **Principle**: Only tools already in system or provided by Claude Code
- **Rationale**: Maintain system simplicity and avoid dependency hell
- **Exception Handling**: If external tool needed, justify in TRUTH_SOURCE.md first

#### Approved System Dependencies
```bash
# Always available in target systems
- bash (5.0+)
- git 
- grep/rg (prefer rg when available)
- find
- sed/awk (basic text processing)
- curl (for WebSearch/MCP integration)
```

### File Structure Standards

#### Command Structure
```
.claude/commands/[command_name].md
├── Header with purpose (1 line)
├── Authority reference (TRUTH_SOURCE.md)
├── Implementation logic (<100 lines)
└── Minimal dependencies only if absolutely necessary
```

#### Size Limitations
- **CLAUDE.md**: ≤200 lines (currently 79)
- **Individual commands**: ≤100 lines  
- **Technical docs**: ≤150 lines
- **user-vision/ layers**: No limit (preserve complete voice)

### Error Handling & Output Standards

#### Error Patterns
```bash
# Specific, actionable error messages
validate_file() {
    local file="$1"
    [[ -f "$file" ]] || {
        echo "ERROR: File not found: $file" >&2
        echo "SOLUTION: Check path or create file first" >&2
        exit 1
    }
}

# Debug information only when requested
debug_log() {
    [[ "${DEBUG:-}" == "true" ]] && echo "DEBUG: $*" >&2
}
```

#### Output Guidelines
- **Interactive commands**: Maximum 4 lines explanatory output
- **Progress**: Only for operations >5 seconds
- **Logs**: stdout/stderr only, never automatic file logging
- **Formatting**: Use markdown for CLI readability

### Performance & Resource Guidelines

#### Token Economy Implementation
```bash
# Conversation phase: No restrictions
# Implementation phase: Optimize for context efficiency

# Read specific files vs loading directories
read_specific_file() {
    # GOOD: Direct file read
    cat "/specific/path/file.txt"
}

avoid_directory_scan() {
    # AVOID: Loading entire directories
    # find . -name "*.md" -exec cat {} \;
}
```

#### Batch Operations
```bash
# Group related operations
batch_git_operations() {
    git status
    git diff --staged
    git log --oneline -5
}
```

### Integration Requirements

#### Claude Code Tool Preferences
```bash
# Tool hierarchy (prefer → avoid)
Read tool        → bash cat
Glob tool        → bash find  
Edit tool        → manual file editing
WebSearch        → manual web lookup
Context7 MCP     → guessing implementation details
```

#### Git Integration Standards
```bash
# Commit message format
git_commit_with_context() {
    local message="$1"
    git commit -m "$message

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>

References: user-vision/TRUTH_SOURCE.md"
}
```

### Security & Access Control

#### Path Safety
```bash
# Always use absolute paths in scripts
SAFE_PATH="/Users/nalve/ce-simple/docs"
UNSAFE_PATH="./docs"  # AVOID: relative paths

# Validate paths before use
validate_path() {
    local path="$1"
    [[ "$path" =~ ^/Users/nalve/ce-simple/ ]] || {
        echo "ERROR: Path outside project scope" >&2
        exit 1
    }
}
```

#### Input Validation
```bash
# Validate all external input
sanitize_input() {
    local input="$1"
    # Remove potentially dangerous characters
    echo "$input" | sed 's/[;&|`$(){}*?]//_/g'
}
```

## Referencias a Autoridad
- user-vision/TRUTH_SOURCE.md líneas 109-127: Golden Authority Rule - AI decides implementation
- user-vision/TRUTH_SOURCE.md líneas 44-51: Metodología sin restricciones para conversación
- user-vision/TRUTH_SOURCE.md líneas 62-64: Simplicidad as beauty principle
- docs/core/principles.md: Simplicidad rector y anti-over-engineering
- Industry Research: CLI Guidelines (clig.dev), Google Shell Style Guide, Bash 5.3 standards