# Fundamentos y Arquitectura de Claude Code

## Tabla de Contenidos

1. [Arquitectura General](#arquitectura-general)
2. [Sistema de Comandos](#sistema-de-comandos)
3. [Gestión de Configuración](#gestión-de-configuración)
4. [Sistema de Memoria](#sistema-de-memoria)
5. [Herramientas Disponibles](#herramientas-disponibles)
6. [Integraciones y Protocolos](#integraciones-y-protocolos)

---

## Arquitectura General

### Componentes Principales

```
Claude Code Architecture
├── CLI Interface
│   ├── Interactive REPL
│   ├── Command Line Arguments
│   └── Keyboard Shortcuts
├── Configuration System
│   ├── Settings Files (JSON)
│   ├── Environment Variables
│   └── Hooks System
├── Memory Management
│   ├── Project Memory (CLAUDE.md)
│   ├── User Memory (~/.claude/CLAUDE.md)
│   └── Context Preservation
├── Tool System
│   ├── Built-in Tools
│   ├── Custom Commands
│   └── MCP Integrations
└── External Integrations
    ├── IDE Integrations
    ├── Version Control
    └── Cloud Providers
```

### Flujo de Ejecución

1. **Inicio de Sesión**
   - Carga configuración desde settings.json
   - Lee memoria desde CLAUDE.md files
   - Inicializa conexiones MCP
   - Configura hooks del sistema

2. **Procesamiento de Comandos**
   - Parse del input del usuario
   - Validación con hooks PreToolUse
   - Ejecución de herramientas
   - Hooks PostToolUse
   - Actualización de contexto

3. **Gestión de Estado**
   - Mantiene contexto de conversación
   - Persiste cambios en memoria
   - Actualiza configuraciones
   - Log de actividades

---

## Sistema de Comandos

### Tipos de Comandos

#### 1. Comandos Built-in
Comandos nativos de Claude Code:

```bash
# Comandos de sesión
/clear          # Limpiar historial
/help           # Mostrar ayuda
/exit           # Salir de la sesión

# Comandos de configuración
/config         # Gestionar configuración
/memory         # Editar archivos de memoria

# Comandos de análisis
/review         # Revisar código
/compact        # Compactar contexto
```

#### 2. Slash Commands Personalizados
Comandos definidos en archivos markdown:

**Ubicaciones:**
- `.claude/commands/` (proyecto)
- `~/.claude/commands/` (personal)

**Estructura del archivo:**
```markdown
---
description: "Descripción del comando"
allowedTools: ["Read", "Write", "Bash"]
extendedThinking: false
---

# Contenido del comando
Instrucciones y lógica del comando
```

#### 3. Comandos MCP
Comandos expuestos por servidores MCP:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-github"]
    }
  }
}
```

### Namespacing y Organización

#### Estructura Recomendada
```
.claude/commands/
├── analysis/
│   ├── code-review.md
│   ├── performance.md
│   └── security.md
├── automation/
│   ├── ci-setup.md
│   ├── deployment.md
│   └── testing.md
├── documentation/
│   ├── api-docs.md
│   └── readme-gen.md
└── utils/
    ├── cleanup.md
    └── setup.md
```

#### Convenciones de Nombres
- **Usar kebab-case**: `code-review.md`, `api-docs.md`
- **Ser descriptivos**: `generate-api-docs.md` mejor que `docs.md`
- **Agrupar por función**: análisis, automatización, documentación

---

## Gestión de Configuración

### Jerarquía de Configuración

Claude Code utiliza una jerarquía de configuración que permite granularidad:

```
1. ~/.claude/settings.json           (Global user)
2. .claude/settings.json             (Project shared)  
3. .claude/settings.local.json       (Project local)
4. Environment variables             (Runtime)
5. Command line flags                (Session)
```

### Archivo settings.json

#### Configuración Completa
```json
{
  "model": "claude-3-5-sonnet-20241022",
  "provider": "anthropic",
  "maxTurns": 10,
  "diffTool": "auto",
  "editor": "code",
  
  "permissions": {
    "allowBash": true,
    "allowFileWrite": true,
    "allowNetworking": true,
    "restrictedPaths": ["/etc", "/usr"]
  },
  
  "tools": {
    "enabled": ["Read", "Write", "Bash", "Grep", "Edit"],
    "disabled": ["WebSearch"]
  },
  
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-filesystem"],
      "env": {
        "ROOT_PATH": "/Users/dev/projects"
      }
    },
    "github": {
      "command": "npx", 
      "args": ["-y", "@anthropic-ai/mcp-server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  },
  
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "scripts/validate-write.sh",
            "outputMode": "json"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "scripts/log-bash.sh"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "scripts/enhance-prompt.sh"
          }
        ]
      }
    ]
  },
  
  "aliases": {
    "test": "npm test",
    "build": "npm run build",
    "deploy": "npm run deploy"
  }
}
```

### Variables de Entorno

#### Variables Principales
```bash
# Autenticación
ANTHROPIC_API_KEY="sk-ant-..."
CLAUDE_MODEL="claude-3-5-sonnet-20241022"

# Configuración
CLAUDE_CONFIG_PATH="/custom/path/.claude"
CLAUDE_SETTINGS_FILE="custom-settings.json"

# Proveedores cloud
AWS_REGION="us-west-2"
AWS_PROFILE="claude-code"
GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account.json"

# Integraciones
GITHUB_TOKEN="ghp_..."
SLACK_TOKEN="xoxb-..."
JIRA_API_TOKEN="..."

# Proxy corporativo
HTTP_PROXY="http://proxy.company.com:8080"
HTTPS_PROXY="https://proxy.company.com:8080"
NO_PROXY="localhost,*.company.com"
```

---

## Sistema de Memoria

### Tipos de Memoria

#### 1. Project Memory (`./CLAUDE.md`)
Instrucciones compartidas del proyecto:

```markdown
# Proyecto E-commerce - Instrucciones Claude

## Arquitectura
- **Frontend**: React 18 + TypeScript + Vite
- **Backend**: Node.js + Express + PostgreSQL
- **Estado**: Redux Toolkit + RTK Query
- **Testing**: Jest + React Testing Library + Cypress

## Convenciones
- **Commits**: Conventional Commits (feat:, fix:, docs:)
- **Branches**: feature/*, bugfix/*, release/*
- **Code Style**: ESLint + Prettier + Husky hooks

## Estructura de Directorios
```
src/
├── components/      # Componentes reutilizables
├── pages/          # Páginas de la aplicación
├── hooks/          # Custom hooks
├── services/       # API calls y servicios
├── store/          # Redux store y slices
├── utils/          # Funciones utilitarias
└── types/          # Definiciones TypeScript
```

## Comandos del Proyecto
- `npm run dev` - Desarrollo local
- `npm run test` - Tests unitarios
- `npm run e2e` - Tests end-to-end
- `npm run lint` - Linting y formateo
- `npm run build` - Build de producción

## Base de Datos
- **ORM**: Prisma
- **Migraciones**: `npx prisma migrate dev`
- **Seed**: `npx prisma db seed`

## APIs Externas
- **Payments**: Stripe API
- **Email**: SendGrid
- **Storage**: AWS S3
```

#### 2. User Memory (`~/.claude/CLAUDE.md`)
Preferencias personales del desarrollador:

```markdown
# Preferencias Personales - Claude Code

## Estilo de Código
- Preferir const sobre let
- Usar arrow functions para callbacks
- Destructuring cuando sea posible
- Comentarios JSDoc para funciones públicas

## Testing
- Tests unitarios para toda lógica de negocio
- Mocks para APIs externas
- Tests de integración para flujos críticos

## Git Workflow
- Commits frecuentes y descriptivos
- Rebase sobre merge para branches feature
- Tags semánticos para releases

## Herramientas Favoritas
- **Editor**: VS Code con extensiones TypeScript, ESLint, Prettier
- **Terminal**: iTerm2 con Oh My Zsh
- **Diff Tool**: code --diff
```

### Importación de Archivos

#### Syntax de Importación
```markdown
# Importar configuración base
@../shared/base-config.md

# Importar reglas específicas
@./rules/typescript-rules.md
@./rules/react-rules.md

# Importar desde directorio home
@~/.claude/personal-preferences.md
```

#### Ejemplo de Estructura Modular
```
.claude/
├── CLAUDE.md                    # Archivo principal
├── shared/
│   ├── base-config.md          # Configuración base
│   └── common-patterns.md      # Patrones comunes
├── frontend/
│   ├── react-rules.md          # Reglas React
│   └── styling-guide.md        # Guía de estilos
└── backend/
    ├── api-conventions.md      # Convenciones API
    └── database-patterns.md    # Patrones DB
```

---

## Herramientas Disponibles

### Herramientas Built-in

#### 1. File Operations
```markdown
Read        # Leer archivos
Write       # Crear/sobrescribir archivos
Edit        # Editar archivos existentes
MultiEdit   # Múltiples edits en un archivo
LS          # Listar directorios
Glob        # Búsqueda por patrones
```

#### 2. Search and Analysis
```markdown
Grep        # Búsqueda en contenido (ripgrep)
Task        # Delegación a agentes especializados
```

#### 3. Execution
```markdown
Bash        # Ejecutar comandos shell
```

#### 4. Web and External
```markdown
WebFetch    # Obtener contenido web
WebSearch   # Búsqueda en internet
```

#### 5. Specialized
```markdown
NotebookRead   # Leer Jupyter notebooks
NotebookEdit   # Editar Jupyter notebooks
TodoWrite      # Gestión de tareas
```

### Configuración de Herramientas

#### Restricciones de Permisos
```json
{
  "permissions": {
    "allowBash": true,
    "allowFileWrite": true,
    "allowNetworking": false,
    "restrictedPaths": [
      "/etc",
      "/usr/bin", 
      "/System"
    ],
    "allowedCommands": [
      "npm",
      "git",
      "docker",
      "kubectl"
    ],
    "blockedCommands": [
      "rm -rf",
      "sudo",
      "chmod 777"
    ]
  }
}
```

#### Tool-specific Configuration
```json
{
  "tools": {
    "Bash": {
      "timeout": 120000,
      "workingDirectory": "/Users/dev/projects",
      "environment": {
        "NODE_ENV": "development",
        "DEBUG": "app:*"
      }
    },
    "Read": {
      "maxFileSize": "10MB",
      "allowedExtensions": [".js", ".ts", ".md", ".json"],
      "encoding": "utf8"
    },
    "WebFetch": {
      "timeout": 30000,
      "maxResponseSize": "5MB",
      "allowedDomains": ["docs.example.com", "api.example.com"]
    }
  }
}
```

---

## Integraciones y Protocolos

### Model Context Protocol (MCP)

#### Arquitectura MCP
```
Claude Code ←→ MCP Client ←→ MCP Server ←→ External Resource
                    ↑
               JSON-RPC over stdio/HTTP
```

#### Tipos de Transporte
1. **stdio**: Proceso hijo con comunicación por stdin/stdout
2. **HTTP**: Servidor HTTP remoto
3. **SSE**: Server-Sent Events para streaming

#### Configuración de Servidores

##### Filesystem Server
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-filesystem"],
      "env": {
        "ROOT_PATH": "/Users/dev/projects"
      }
    }
  }
}
```

##### GitHub Server
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

##### Database Server
```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-postgres"],
      "env": {
        "DATABASE_URL": "${DATABASE_URL}"
      }
    }
  }
}
```

### IDE Integrations

#### VS Code Integration
```json
{
  "ide": {
    "vscode": {
      "enabled": true,
      "keyboardShortcut": "cmd+esc",
      "diffTool": "code --diff",
      "openInEditor": true,
      "shareSelection": true,
      "shareDiagnostics": true
    }
  }
}
```

#### JetBrains Integration
```json
{
  "ide": {
    "jetbrains": {
      "enabled": true,
      "product": "IntelliJ",
      "keyboardShortcut": "ctrl+alt+c",
      "diffTool": "idea diff",
      "openInEditor": true
    }
  }
}
```

### Cloud Provider Integration

#### AWS Bedrock
```json
{
  "provider": "bedrock",
  "region": "us-west-2", 
  "model": "anthropic.claude-3-5-sonnet-20241022-v2:0",
  "credentials": {
    "type": "profile",
    "profile": "claude-code"
  },
  "promptCaching": true
}
```

#### Google Vertex AI
```json
{
  "provider": "vertex",
  "project": "my-project-id",
  "location": "us-central1",
  "model": "claude-3-5-sonnet@20241022",
  "credentials": {
    "type": "service-account",
    "path": "/path/to/service-account.json"
  }
}
```

### Monitoring y Observabilidad

#### OpenTelemetry Integration
```json
{
  "telemetry": {
    "enabled": true,
    "endpoint": "http://localhost:4317",
    "serviceName": "claude-code",
    "attributes": {
      "team": "engineering",
      "project": "metodologia-comandos"
    }
  }
}
```

#### Logging Configuration
```json
{
  "logging": {
    "level": "info",
    "format": "json",
    "outputs": [
      {
        "type": "file",
        "path": "/var/log/claude-code/app.log",
        "rotation": "daily"
      },
      {
        "type": "stdout",
        "format": "pretty"
      }
    ]
  }
}
```

---

## Seguridad y Governance

### Configuración de Seguridad

#### Restricted Execution
```json
{
  "security": {
    "sandbox": true,
    "restrictedPaths": [
      "/etc",
      "/usr/bin",
      "/System",
      "~/.ssh",
      "~/.aws"
    ],
    "allowedCommands": [
      "npm", "yarn", "pnpm",
      "git",
      "docker", "docker-compose",
      "kubectl",
      "terraform"
    ],
    "blockedPatterns": [
      "rm -rf /",
      "sudo.*",
      "chmod 777",
      ">/etc/",
      "curl.*|.*sh"
    ]
  }
}
```

#### Enterprise Policies
```json
{
  "enterprisePolicy": {
    "managedBy": "IT-Security",
    "version": "1.2.0",
    "enforced": true,
    "policies": {
      "dataRetention": "30days",
      "allowedProviders": ["bedrock", "vertex"],
      "requiredMFA": true,
      "auditLogging": true,
      "networkRestrictions": {
        "allowedDomains": ["*.company.com", "api.anthropic.com"],
        "blockedDomains": ["*"]
      }
    }
  }
}
```

Esta documentación proporciona una base sólida para entender la arquitectura completa de Claude Code y sus capacidades de configuración avanzada.