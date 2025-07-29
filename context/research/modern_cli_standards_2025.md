# Modern CLI Standards Research 2025

**Fuente:** Migrado de docs/technical/stack_requirements.md (contenido investigativo)
**29/07/2025 - Context Research**

## Industry Best Practices Research (July 28, 2025)

### CLI Design Evolution
**CLI design has evolved from machine-first to human-first interfaces**, updating traditional UNIX principles for the modern day. Today's command line is human-first: a text-based UI that affords access to all kinds of tools, systems and platforms.

### Core Requirements for 2025
- Functionality first with proper error handling
- Authentication via OAuth patterns with browser launch
- Layered validation starting with format progressing to semantic
- Support for commonly used output modifiers and color/no-color options
- Keep output lines under 80 characters where possible

### Bash Scripting Modern Standards (2025)
- **Shebang**: Use `#!/usr/bin/env bash` over direct paths for better portability
- **Strict Mode**: Always start scripts with strict mode settings for early error detection
- **Google Style Influence**: Scripts under 50 lines, emphasizing simplicity and maintainability
- **Variable Naming**: ALLCAPS format with underscores only for readability
- **Arrays**: Use `"${array[@]}"` quoted expansion to avoid quoting issues

### Stack Tecnológico Research

#### Authorized Languages & Tools
- **Bash**: Para comandos del sistema y orchestración
- **Markdown**: Para toda documentación
- **JSON**: Para configuración y data interchange
- **YAML**: Solo para configs Claude Code específicas

#### Core Tools Validated
- **Claude Code CLI**: Interface principal
- **Git**: Control de versiones y coordinación
- **ripgrep (rg)**: Para búsquedas en código
- **find/ls**: Para navegación de archivos

#### Deprecated/Prohibited
- Frameworks complejos (React, Vue, Angular para este proyecto)
- Bases de datos pesadas (PostgreSQL, MySQL para comandos simples)
- Microservicios architecture
- Docker containers (mantener simplicidad)

---
**Trazabilidad:** Research extraído de docs/technical/stack_requirements.md durante simplificación estructural