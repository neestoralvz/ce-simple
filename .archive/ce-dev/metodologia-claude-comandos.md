# Metodología Completa para Crear Comandos Claude Code

## Tabla de Contenidos

1. [Fundamentos y Arquitectura](#1-fundamentos-y-arquitectura)
2. [Tipos de Comandos por Categoría](#2-tipos-de-comandos-por-categoría)
3. [Patrones de Implementación](#3-patrones-de-implementación)
4. [Integración Avanzada](#4-integración-avanzada)
5. [Documentación y Training](#5-documentación-y-training)

---

## 1. Fundamentos y Arquitectura

### 1.1 Estructura de Comandos

Claude Code utiliza dos ubicaciones principales para comandos personalizados:

#### Comandos de Proyecto (`.claude/commands/`)
- **Ubicación**: En la raíz del proyecto
- **Propósito**: Comandos específicos del proyecto compartidos con el equipo
- **Control de versiones**: Se incluyen en git
- **Ejemplos**: análisis de arquitectura específica, workflows de deployment

#### Comandos Personales (`~/.claude/commands/`)
- **Ubicación**: Directorio home del usuario
- **Propósito**: Comandos personales del desarrollador
- **Control de versiones**: No se incluyen en git
- **Ejemplos**: preferencias de código, shortcuts personales

### 1.2 Configuración del Sistema

#### Settings.json Hierarchy
```
~/.claude/settings.json          # Configuración global
.claude/settings.json            # Configuración del proyecto
.claude/settings.local.json      # Configuración local (no versionada)
```

#### Variables de Entorno Clave
```bash
ANTHROPIC_API_KEY              # API key de Anthropic
CLAUDE_MODEL                   # Modelo a usar
CLAUDE_CONFIG_PATH            # Path personalizado de configuración
```

### 1.3 Sistema de Memoria (CLAUDE.md)

#### Tipos de Memoria
- **Proyecto** (`./CLAUDE.md`): Instrucciones compartidas del equipo
- **Usuario** (`~/.claude/CLAUDE.md`): Preferencias personales globales
- **Importaciones**: Uso de `@path/to/import` para incluir otros archivos

#### Mejores Prácticas para CLAUDE.md
```markdown
# Proyecto X - Instrucciones Claude

## Arquitectura
- Framework: React + TypeScript
- Estado: Redux Toolkit
- Testing: Jest + React Testing Library

## Convenciones de Código
- ESLint configuración estricta
- Prettier para formateo
- Commits convencionales

## Comandos Comunes
- `npm run test` - Ejecutar tests
- `npm run lint` - Verificar linting
- `npm run build` - Build de producción
```

### 1.4 Model Context Protocol (MCP)

#### Configuración de Servidores MCP
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-filesystem"]
    }
  }
}
```

---

## 2. Tipos de Comandos por Categoría

### 2.1 Análisis y Calidad

#### Comando: Revisión de Código
```markdown
---
description: "Analiza la calidad del código y sugiere mejoras"
allowedTools: ["Read", "Grep", "Write"]
---

# Revisión de Código

Analiza los siguientes aspectos del código:

1. **Calidad general**: Legibilidad, mantenibilidad
2. **Rendimiento**: Identificar posibles cuellos de botella
3. **Seguridad**: Vulnerabilidades potenciales
4. **Best practices**: Adherencia a patrones establecidos

Archivos a analizar: $ARGUMENTS

## Acciones a realizar:
- Leer archivos especificados
- Buscar anti-patterns comunes
- Generar reporte con recomendaciones
- Proponer refactorings específicos
```

#### Comando: Análisis de Dependencias
```markdown
---
description: "Analiza dependencias del proyecto y detecta vulnerabilidades"
allowedTools: ["Bash", "Read", "Write"]
---

# Análisis de Dependencias

!npm audit --json > audit-results.json
!npm ls --json > dependency-tree.json

Analizar:
1. Vulnerabilidades conocidas
2. Dependencias obsoletas
3. Dependencias no utilizadas
4. Conflictos de versiones

Generar reporte con recomendaciones de actualización.
```

### 2.2 Automatización de Workflows

#### Comando: Setup CI/CD
```markdown
---
description: "Configura pipeline de CI/CD completo"
allowedTools: ["Write", "Read", "Bash"]
---

# Setup CI/CD Pipeline

Crear configuración completa de CI/CD:

1. **GitHub Actions workflows**
2. **Scripts de deployment**
3. **Configuración de testing**
4. **Hooks de pre-commit**

Parámetros: $ARGUMENTS (staging|production)

## Templates a crear:
- `.github/workflows/ci.yml`
- `.github/workflows/deploy.yml`
- `scripts/deploy.sh`
- `.pre-commit-config.yaml`
```

#### Comando: Release Automation
```markdown
---
description: "Automatiza proceso de release con changelog"
allowedTools: ["Bash", "Write", "Read"]
---

# Automatización de Release

Proceso automatizado:

1. !git log --oneline $(git describe --tags --abbrev=0)..HEAD
2. Generar changelog basado en commits
3. Actualizar version en package.json
4. Crear tag de git
5. Generar release notes

Tipo de release: $ARGUMENTS (major|minor|patch)
```

### 2.3 Documentación y Mantenimiento

#### Comando: Generación de Docs
```markdown
---
description: "Genera documentación automática del código"
allowedTools: ["Read", "Write", "Bash"]
---

# Generación de Documentación

Generar documentación completa:

1. **API Documentation**: JSDoc/TSDoc
2. **README actualizado**: Con ejemplos de uso
3. **Guías de desarrollo**: Setup y contribución
4. **Arquitectura**: Diagramas y explicaciones

Directorios a documentar: $ARGUMENTS
```

---

## 3. Patrones de Implementación

### 3.1 Plantillas Base

#### Template Mínimo
```markdown
---
description: "Descripción breve del comando"
allowedTools: ["Read", "Write"]
---

# Nombre del Comando

Descripción detallada de lo que hace el comando.

Parámetros: $ARGUMENTS

## Pasos:
1. Paso uno
2. Paso dos
3. Paso tres
```

#### Template Avanzado
```markdown
---
description: "Comando complejo con validaciones"
allowedTools: ["Read", "Write", "Bash", "Grep"]
extendedThinking: true
---

# Comando Avanzado

## Validaciones Previas
- Verificar que el proyecto esté inicializado
- Validar permisos necesarios
- Comprobar dependencias

## Lógica Principal
Parámetros recibidos: $ARGUMENTS

### Fase 1: Análisis
@package.json
Analizar configuración actual

### Fase 2: Implementación
Aplicar cambios necesarios

### Fase 3: Validación
!npm test
Verificar que todo funciona correctamente

## Resultado Esperado
Descripción del estado final deseado
```

### 3.2 Convenciones de Nomenclatura

#### Estructura de Nombres
```
categoria/subcategoria/accion.md

Ejemplos:
- analysis/code/review.md
- automation/ci/setup.md
- docs/api/generate.md
- maintenance/deps/update.md
```

#### Namespacing con Directorios
```
.claude/commands/
├── analysis/
│   ├── code/
│   ├── performance/
│   └── security/
├── automation/
│   ├── ci/
│   ├── deployment/
│   └── testing/
└── docs/
    ├── api/
    └── guides/
```

### 3.3 Manejo de Argumentos

#### Argumentos Simples
```markdown
# Uso básico
Archivo a procesar: $ARGUMENTS

# Con validación
!if [ -z "$ARGUMENTS" ]; then echo "Error: Se requiere especificar archivo"; exit 1; fi
```

#### Argumentos Múltiples
```markdown
# Separar argumentos
!IFS=' ' read -ra ARGS <<< "$ARGUMENTS"
!FILE="${ARGS[0]}"
!TYPE="${ARGS[1]:-default}"

Procesando archivo: ${FILE} con tipo: ${TYPE}
```

#### Argumentos Named
```markdown
# Parsing de argumentos con nombres
!while [[ $# -gt 0 ]]; do
  case $1 in
    --file=*) FILE="${1#*=}"; shift ;;
    --type=*) TYPE="${1#*=}"; shift ;;
    *) echo "Argumento desconocido: $1"; exit 1 ;;
  esac
done
```

### 3.4 Referencias y Contexto

#### Referencias a Archivos
```markdown
# Archivo específico
@src/components/Button.tsx

# Múltiples archivos
@src/components/*.tsx

# Directorio completo
@src/utils/
```

#### Referencias a Recursos MCP
```markdown
# GitHub issues
@github:issues

# Base de datos
@db:users table

# Servicios externos
@api:health-check
```

---

## 4. Integración Avanzada

### 4.1 Sistema de Hooks

#### Configuración de Hooks
```json
{
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
            "command": "scripts/log-command.sh"
          }
        ]
      }
    ]
  }
}
```

#### Hook de Validación
```bash
#!/bin/bash
# scripts/validate-write.sh

FILE_PATH="$1"
CONTENT="$2"

# Validar que no se escriban secretos
if echo "$CONTENT" | grep -i "password\|secret\|key\|token" > /dev/null; then
  echo '{"approved": false, "message": "Detectado posible secreto en el contenido"}'
  exit 1
fi

echo '{"approved": true}'
```

### 4.2 SDK Integration

#### TypeScript SDK
```typescript
import { query } from "@anthropic-ai/claude-code";

async function generateCommand(prompt: string) {
  for await (const message of query({
    prompt: `Crear comando Claude Code: ${prompt}`,
    options: { 
      maxTurns: 3,
      model: "claude-3-5-sonnet-20241022"
    }
  })) {
    if (message.type === 'text') {
      console.log(message.content);
    }
  }
}
```

#### Python SDK
```python
from anthropic_claude_code import query

async def analyze_codebase(project_path: str):
    async for message in query(
        prompt=f"Analizar estructura de proyecto en {project_path}",
        options={"max_turns": 5}
    ):
        if message.type == "text":
            print(message.content)
```

### 4.3 Enterprise Features

#### Configuración de Proxy Corporativo
```json
{
  "proxy": {
    "http": "http://proxy.empresa.com:8080",
    "https": "https://proxy.empresa.com:8080",
    "noProxy": ["localhost", "*.empresa.com"]
  }
}
```

#### LLM Gateway Integration
```json
{
  "llmGateway": {
    "endpoint": "https://llm-gateway.empresa.com",
    "apiKey": "${LLM_GATEWAY_API_KEY}",
    "department": "engineering",
    "project": "metodologia-comandos"
  }
}
```

#### Cloud Provider Integration
```json
{
  "provider": "bedrock",
  "region": "us-west-2",
  "model": "anthropic.claude-3-5-sonnet-20241022-v2:0",
  "credentials": {
    "type": "iam",
    "roleArn": "arn:aws:iam::123456789:role/ClaudeCodeRole"
  }
}
```

---

## 5. Documentación y Training

### 5.1 Guías por Tipo de Proyecto

#### Proyecto React/TypeScript
```markdown
# Comandos para Proyecto React

## Setup Inicial
- `/react/setup` - Configuración inicial completa
- `/react/component` - Generar componente con tests
- `/react/hook` - Crear custom hook

## Development
- `/react/analyze` - Análisis de rendimiento
- `/react/test` - Ejecutar tests con coverage
- `/react/lint` - Linting y formateo

## Deployment
- `/react/build` - Build optimizado
- `/react/deploy` - Deployment a diferentes envs
```

#### Proyecto Node.js/API
```markdown
# Comandos para API Node.js

## Desarrollo
- `/api/endpoint` - Generar nuevo endpoint
- `/api/middleware` - Crear middleware
- `/api/model` - Generar modelo de datos

## Testing
- `/api/test-integration` - Tests de integración
- `/api/load-test` - Tests de carga
- `/api/security-test` - Análisis de seguridad

## Deployment
- `/api/docker` - Containerización
- `/api/k8s` - Configuración Kubernetes
```

### 5.2 Training y Adopción

#### Programa de Onboarding
1. **Semana 1**: Conceptos básicos y comandos built-in
2. **Semana 2**: Crear primeros comandos personalizados
3. **Semana 3**: Comandos avanzados e integraciones
4. **Semana 4**: Best practices y optimización

#### Workshops Recomendados
- **Workshop 1**: "Fundamentos de Claude Code"
- **Workshop 2**: "Comandos Personalizados Efectivos"
- **Workshop 3**: "Integraciones Enterprise"
- **Workshop 4**: "Automatización de Workflows"

### 5.3 Casos de Uso Comunes

#### Migración de Legacy Code
```markdown
# Comando: Modernizar Codebase

Proceso step-by-step para migrar código legacy:

1. Análisis de dependencias obsoletas
2. Identificación de anti-patterns
3. Plan de migración gradual
4. Implementación por módulos
5. Testing de regresión
6. Documentación de cambios
```

#### Code Review Automatizado
```markdown
# Comando: Review Automático

Integración con GitHub para review automático:

1. Trigger en PR creation
2. Análisis estático del código
3. Verificación de tests
4. Comentarios automáticos
5. Scoring de calidad
6. Sugerencias de mejora
```

### 5.4 Métricas y Monitoreo

#### KPIs para Comandos
- **Uso**: Frecuencia de ejecución
- **Efectividad**: Tiempo ahorrado
- **Calidad**: Reducción de bugs
- **Adopción**: Usuarios activos

#### Dashboard de Métricas
```json
{
  "metrics": {
    "comandos_ejecutados": 1250,
    "tiempo_ahorrado_horas": 180,
    "errores_detectados": 45,
    "adoption_rate": "75%"
  }
}
```

---

## Conclusión

Esta metodología proporciona un framework completo para desarrollar comandos Claude Code efectivos, desde conceptos básicos hasta integraciones enterprise avanzadas. La implementación gradual y el enfoque en mejores prácticas garantizan adopción exitosa en equipos de desarrollo.

## Próximos Pasos

1. Implementar plantillas base
2. Crear comandos de ejemplo
3. Configurar integraciones
4. Establecer programa de training
5. Medir y optimizar resultados