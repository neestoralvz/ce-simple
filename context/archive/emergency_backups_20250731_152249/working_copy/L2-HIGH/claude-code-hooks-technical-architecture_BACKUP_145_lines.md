# Claude Code Hooks - Technical Architecture Implementation

**30/07/2025 - CDMX** | Technical implementation architecture and configuration authority

## AUTORIDAD SUPREMA
claude-code-hooks-implementation-notes.md → claude-code-hooks-technical-architecture.md implements complete technical architecture per implementation authority

## SISTEMA DE CONFIGURACIÓN COMPLETA

### Archivo Principal de Configuración
**Ubicación**: `.claude/hooks/project-protection.json`
```json
{
  "hooks": {
    "file-write": {
      "command": "bash",
      "args": [".claude/hooks/root-protection.sh", "${CLAUDE_FILE_PATH}"],
      "description": "Root structure protection and file validation",
      "timeout": 5000
    },
    "user-prompt-submit": {
      "command": "bash",
      "args": [".claude/hooks/standards-check.sh", "${CLAUDE_PROJECT_ROOT}"],
      "description": "Pre-conversation standards validation",
      "timeout": 3000
    }
  },
  "project": {
    "max_file_lines": 80,
    "enforcement_level": "warn",
    "allowed_root_files": ["CLAUDE.md", "README.md", ".gitignore"]
  }
}
```

## SCRIPTS DE PROTECCIÓN MODULAR

### 1. root-protection.sh - Auto-reubicación Inteligente
**Función**: Detecta y reubica archivos no autorizados en raíz del proyecto
**Características**:
- Detecta archivos en raíz del proyecto
- Determina ubicación apropiada según tipo/nombre
- Ejecuta movimiento automático con logging
- Maneja casos edge con fallback manual

### 2. size-validation.sh - Enforcement Límite 80 Líneas
**Función**: Valida límite de líneas con contexto y sugerencias
**Características**:
- Valida solo archivos .md
- Proporciona sugerencias factorización específicas
- Context-aware recommendations basadas en contenido
- Logging detallado para tracking violations

### 3. standards-check.sh - Monitoreo Compliance Estándares
**Función**: Pre-conversación validation checks y monitoreo continuo
**Características**:
- Pre-conversación validation checks
- Detecta drift autoridad en archivos core
- Valida integridad estructural
- Sugerencias proactivas mantenimiento

### 4. authority-validation.sh - Validación Cadena Autoridad
**Función**: Session-start integrity checks y detección contamination
**Características**:
- Session-start integrity checks
- Detección contamination authority
- Validation hierarchy VISION.md → truth-source.md → components
- Alert system para authority drift

## EVENTOS HOOK Y TIMING DETALLADO

| Hook Event | Script | Timing | Función Principal |
|------------|--------|--------|-------------------|
| `session-start` | authority-validation.sh | 2s timeout | Authority integrity check |
| `user-prompt-submit` | standards-check.sh | 3s timeout | Pre-conversation validation |
| `file-write` | root-protection.sh | 5s timeout | Root protection + auto-fix |
| `tool-call-complete` | size-validation.sh | 4s timeout | Post-action compliance |

## TEMPLATE CONFIGURACIÓN HOOK

### Hook Configuration Template Genérico
```json
{
  "hooks": {
    "[trigger-event]": {
      "command": "bash",
      "args": [".claude/hooks/[protection-script].sh", "${CLAUDE_VARIABLE}"],
      "description": "[Clear description of protection function]",
      "timeout": [appropriate_timeout_ms]
    }
  },
  "project": {
    "[project_specific_config]": "[values]",
    "enforcement_level": "[info|warn|error]",
    "fail_on_error": [true|false]
  }
}
```

### Bash Script Protection Template
```bash
#!/bin/bash
set -euo pipefail

# Configuration
PARAM="${1:-}"
PROJECT_ROOT="[project_root_path]"
LOG_FILE="$PROJECT_ROOT/.claude/hooks/protection.log"

# Logging functions
log_event() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] CLAUDE_HOOK: $1" >> "$LOG_FILE"; }
log_violation() { echo "🛡️ GUARDIAN: $1"; log_event "VIOLATION: $1"; }
log_action() { echo "✅ GUARDIAN: $1"; log_event "ACTION: $1"; }

# Validation logic
[validation_logic_here]

# Auto-remediation if appropriate
[auto_fix_logic_here]

exit 0
```

## ARQUITECTURA SISTEMA PROTECCIÓN

### Protection System Architecture Pattern
```
/project-root/.claude/hooks/
├── configuration.json          // Declarative hook definitions
├── protection-scripts/         // Modular bash scripts
│   ├── [concern]-protection.sh // Single responsibility scripts
│   └── logging-functions.sh    // Shared utilities
├── protection.log             // Centralized logging
└── README.md                  // Complete documentation
```

### Características Técnicas Clave
- **Variable Integration**: ${CLAUDE_FILE_PATH}, ${CLAUDE_PROJECT_ROOT} proporcionan context perfect
- **Event Timing Granular**: Precise workflow integration timing
- **Error Handling Graceful**: Mantiene user experience quality
- **Cross-platform Compatibility**: Sin dependencies additional
- **Lightweight Resource Usage**: Excellent performance characteristics

---

**TECHNICAL ARCHITECTURE DECLARATION**: Complete technical implementation architecture preserving all configuration details and implementation specifications with 100% fidelity per L0-EMERGENCY extraction requirements.