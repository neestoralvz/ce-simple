# Patrones de Implementación y Mejores Prácticas

## Tabla de Contenidos

1. [Patrones de Comandos](#patrones-de-comandos)
2. [Mejores Prácticas de Desarrollo](#mejores-prácticas-de-desarrollo)
3. [Gestión de Argumentos y Parámetros](#gestión-de-argumentos-y-parámetros)
4. [Manejo de Errores y Validaciones](#manejo-de-errores-y-validaciones)
5. [Optimización y Performance](#optimización-y-performance)
6. [Testing de Comandos](#testing-de-comandos)
7. [Seguridad y Validación](#seguridad-y-validación)
8. [Documentación y Mantenimiento](#documentación-y-mantenimiento)

---

## Patrones de Comandos

### 1. Patrón de Comando Simple

#### Estructura Base
```markdown
---
description: "Descripción clara y concisa"
allowedTools: ["Read", "Write"]
---

# Nombre del Comando

Descripción detallada de lo que hace el comando.

## Entrada
Parámetros esperados: $ARGUMENTS

## Procesamiento
Lógica principal del comando

## Salida
Resultado esperado del comando
```

#### Ejemplo: Comando de Análisis
```markdown
---
description: "Analiza la estructura de un archivo JavaScript"
allowedTools: ["Read", "Grep"]
---

# Análisis de Archivo JavaScript

Analiza la estructura y complejidad de un archivo JavaScript.

Archivo a analizar: $ARGUMENTS

## Análisis de Estructura
@$ARGUMENTS

## Métricas del Archivo
!wc -l "$ARGUMENTS"
!grep -c "function\|=>" "$ARGUMENTS"
!grep -c "class " "$ARGUMENTS"

## Reporte
Generar reporte con:
- Líneas de código
- Número de funciones
- Número de clases
- Nivel de complejidad estimado
```

### 2. Patrón de Comando Complejo

#### Template Avanzado
```markdown
---
description: "Comando complejo con múltiples fases"
allowedTools: ["Read", "Write", "Bash", "Grep", "Edit"]
extendedThinking: true
---

# Comando Complejo Multi-fase

## Validaciones Previas
Verificar precondiciones antes de ejecutar

## Fase 1: Análisis
Analizar el estado actual

## Fase 2: Planificación  
Crear plan de ejecución

## Fase 3: Implementación
Ejecutar cambios planificados

## Fase 4: Validación
Verificar resultados y calidad

## Fase 5: Cleanup
Limpiar archivos temporales y finalizar
```

#### Ejemplo: Migración de Componente
```markdown
---
description: "Migra componente React de clase a funcional"
allowedTools: ["Read", "Write", "Edit", "Bash"]
extendedThinking: true
---

# Migración de Componente React

Migra un componente React de clase a componente funcional con hooks.

Archivo del componente: $ARGUMENTS

## Fase 1: Análisis del Componente Actual
@$ARGUMENTS

Identificar:
- Estado local usado
- Lifecycle methods
- Props recibidas
- Métodos de instancia

## Fase 2: Validaciones Previas
!grep -n "componentDidMount\|componentWillUnmount\|shouldComponentUpdate" "$ARGUMENTS"

## Fase 3: Backup del Original
!cp "$ARGUMENTS" "$ARGUMENTS.backup"

## Fase 4: Transformación
Convertir:
- `class` a `function`
- `this.state` a `useState`
- `componentDidMount` a `useEffect`
- `this.props` a parámetros de función

## Fase 5: Testing
!npm test -- --testPathPattern="$(basename "$ARGUMENTS" .jsx).test"

## Fase 6: Cleanup
Si los tests pasan, eliminar backup
```

### 3. Patrón de Comando Modular

#### Comandos Reutilizables
```markdown
---
description: "Comando que utiliza otros comandos"
allowedTools: ["Task"]
---

# Comando Modular Principal

## Sub-comandos
Ejecutar comandos especializados:

!claude /analyze/code "$ARGUMENTS"
!claude /docs/generate "$ARGUMENTS"  
!claude /test/run "$ARGUMENTS"

## Consolidación
Combinar resultados de todos los sub-comandos
```

### 4. Patrón de Pipeline

#### Comando de Pipeline de Datos
```markdown
---
description: "Procesa datos a través de múltiples etapas"
allowedTools: ["Read", "Write", "Bash"]
---

# Pipeline de Procesamiento

Datos de entrada: $ARGUMENTS

## Etapa 1: Extracción
@$ARGUMENTS

## Etapa 2: Transformación
!cat "$ARGUMENTS" | jq '.data[] | {id, name, email}'

## Etapa 3: Validación
Verificar integridad de datos

## Etapa 4: Carga
Guardar datos procesados en formato final
```

---

## Mejores Prácticas de Desarrollo

### 1. Estructura y Organización

#### Convenciones de Nomenclatura
```bash
# ✅ Buenos nombres
analysis/code-quality.md
automation/ci-setup.md
docs/api-generate.md
utils/project-cleanup.md

# ❌ Nombres poco descriptivos
utils/stuff.md
misc/things.md
temp/test.md
```

#### Organización de Directorios
```
.claude/commands/
├── analysis/           # Comandos de análisis
│   ├── code/          
│   ├── performance/   
│   └── security/      
├── automation/        # Comandos de automatización
│   ├── ci-cd/         
│   ├── deployment/    
│   └── testing/       
├── development/       # Comandos de desarrollo
│   ├── setup/         
│   ├── debugging/     
│   └── refactoring/   
├── documentation/     # Comandos de documentación
│   ├── api/           
│   ├── guides/        
│   └── readme/        
└── utils/            # Utilidades generales
    ├── cleanup/       
    ├── backup/        
    └── migration/     
```

### 2. Documentación en Comandos

#### YAML Frontmatter Completo
```yaml
---
description: "Descripción clara del propósito del comando"
allowedTools: ["Read", "Write", "Bash", "Grep"]
extendedThinking: true
author: "nombre-del-autor"
version: "1.2.0"
tags: ["analysis", "javascript", "performance"]
prerequisites: ["node.js", "npm"]
estimatedTime: "5-10 minutes"
---
```

#### Documentación Interna
```markdown
# Comando de Análisis

## Propósito
Este comando analiza la calidad del código JavaScript y proporciona métricas detalladas.

## Requisitos Previos
- Node.js v16+
- Proyecto con package.json
- ESLint configurado

## Entrada Esperada
- Archivo JavaScript (.js, .jsx, .ts, .tsx)
- O directorio con archivos JavaScript

## Salida Esperada
- Reporte de métricas de calidad
- Lista de problemas encontrados
- Sugerencias de mejora

## Ejemplos de Uso
```bash
claude /analysis/code-quality src/components/Button.jsx
claude /analysis/code-quality src/
```

## Notas
- El comando creará archivos temporales en .tmp/
- Los resultados se guardan en reports/code-quality-{timestamp}.md
```

### 3. Modularidad y Reutilización

#### Comandos Base Reutilizables
```markdown
# commands/utils/file-backup.md
---
description: "Crea backup de archivo con timestamp"
allowedTools: ["Bash"]
---

# Backup de Archivo

!timestamp=$(date +"%Y%m%d_%H%M%S")
!cp "$ARGUMENTS" "$ARGUMENTS.backup.$timestamp"
echo "✅ Backup creado: $ARGUMENTS.backup.$timestamp"
```

#### Importación de Comandos Base
```markdown
---
description: "Comando que usa utilidades base"
allowedTools: ["Task", "Read", "Write"]
---

# Comando Principal

## Backup Previo
!claude /utils/file-backup "$ARGUMENTS"

## Procesamiento Principal
Lógica principal del comando...

## Validación Final
!claude /utils/validate-changes "$ARGUMENTS"
```

---

## Gestión de Argumentos y Parámetros

### 1. Parsing de Argumentos Simple

#### Argumentos Posicionales
```bash
# En el comando markdown
!IFS=' ' read -ra ARGS <<< "$ARGUMENTS"
!FILE="${ARGS[0]}"
!TYPE="${ARGS[1]:-default}"
!OUTPUT="${ARGS[2]:-output.txt}"

echo "Procesando archivo: $FILE"
echo "Tipo: $TYPE"
echo "Salida: $OUTPUT"
```

#### Validación de Argumentos
```bash
# Verificar argumentos requeridos
!if [ -z "$ARGUMENTS" ]; then
  echo "❌ Error: Se requiere especificar un archivo"
  echo "Uso: claude /comando archivo.js [tipo] [salida]"
  exit 1
fi

!if [ ! -f "$FILE" ]; then
  echo "❌ Error: El archivo '$FILE' no existe"
  exit 1
fi
```

### 2. Argumentos con Nombres (Named Arguments)

#### Parser de Argumentos Avanzado
```bash
# Función para parsing de argumentos con nombres
!parse_args() {
  local file=""
  local type="default"
  local output=""
  local verbose=false
  
  while [[ $# -gt 0 ]]; do
    case $1 in
      --file=*) file="${1#*=}"; shift ;;
      --type=*) type="${1#*=}"; shift ;;
      --output=*) output="${1#*=}"; shift ;;
      --verbose) verbose=true; shift ;;
      -*) echo "Argumento desconocido: $1"; exit 1 ;;
      *) file="$1"; shift ;;
    esac
  done
  
  echo "file=$file"
  echo "type=$type" 
  echo "output=$output"
  echo "verbose=$verbose"
}

!eval $(parse_args $ARGUMENTS)
```

#### Ejemplo de Uso
```markdown
# El usuario puede llamar el comando así:
claude /analyze --file=src/app.js --type=performance --verbose
claude /analyze src/app.js --output=report.md
claude /analyze --type=security src/utils.js
```

### 3. Configuración Flexible

#### Archivo de Configuración
```bash
# Cargar configuración desde archivo
!CONFIG_FILE=".claude-config.json"
!if [ -f "$CONFIG_FILE" ]; then
  echo "📋 Cargando configuración desde $CONFIG_FILE"
  # Parsear JSON config file
fi

# Variables de entorno como fallback
!OUTPUT_DIR="${CLAUDE_OUTPUT_DIR:-./reports}"
!LOG_LEVEL="${CLAUDE_LOG_LEVEL:-info}"
```

#### Configuración en CLAUDE.md
```markdown
# En CLAUDE.md del proyecto
## Configuración de Comandos

### Análisis de Código
- Directorio de salida: `reports/`
- Formato por defecto: `markdown`
- Incluir métricas: `true`

### CI/CD
- Entorno por defecto: `staging`
- Auto-deploy: `false`
- Notificaciones: `slack`
```

---

## Manejo de Errores y Validaciones

### 1. Validaciones Previas

#### Checklist de Validaciones
```bash
# Validar herramientas requeridas
!check_requirements() {
  local missing=()
  
  if ! command -v node &> /dev/null; then
    missing+=("node.js")
  fi
  
  if ! command -v npm &> /dev/null; then
    missing+=("npm")
  fi
  
  if [ ${#missing[@]} -ne 0 ]; then
    echo "❌ Herramientas faltantes: ${missing[*]}"
    echo "Instala las herramientas requeridas antes de continuar"
    exit 1
  fi
  
  echo "✅ Todas las herramientas requeridas están disponibles"
}

!check_requirements
```

#### Validación de Estructura de Proyecto
```bash
# Verificar estructura de proyecto
!validate_project() {
  if [ ! -f "package.json" ]; then
    echo "❌ Error: No se encontró package.json"
    echo "Este comando requiere un proyecto Node.js válido"
    exit 1
  fi
  
  if [ ! -d "src" ]; then
    echo "⚠️  Advertencia: No se encontró directorio src/"
    echo "Procediendo con la estructura actual..."
  fi
  
  echo "✅ Estructura de proyecto válida"
}

!validate_project
```

### 2. Manejo de Errores Graceful

#### Try-Catch Pattern
```bash
# Manejo de errores con recuperación
!execute_with_recovery() {
  local command="$1"
  local recovery_action="$2"
  
  echo "🔄 Ejecutando: $command"
  
  if ! eval "$command"; then
    echo "❌ Error ejecutando: $command"
    
    if [ -n "$recovery_action" ]; then
      echo "🔧 Intentando recuperación: $recovery_action"
      eval "$recovery_action"
    fi
    
    return 1
  fi
  
  echo "✅ Comando ejecutado exitosamente"
  return 0
}

# Ejemplo de uso
!execute_with_recovery "npm test" "npm install && npm test"
```

#### Logging Estructurado
```bash
# Sistema de logging
!log() {
  local level="$1"
  local message="$2"
  local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
  
  case $level in
    ERROR) echo "[$timestamp] ❌ ERROR: $message" ;;
    WARN)  echo "[$timestamp] ⚠️  WARN:  $message" ;;
    INFO)  echo "[$timestamp] ℹ️  INFO:  $message" ;;
    DEBUG) [ "$DEBUG" = "true" ] && echo "[$timestamp] 🐛 DEBUG: $message" ;;
  esac
}

# Uso del logger
!log "INFO" "Iniciando análisis de código"
!log "WARN" "Archivo no encontrado, usando valores por defecto"
!log "ERROR" "Fallo crítico en el procesamiento"
```

### 3. Rollback y Cleanup

#### Sistema de Rollback
```bash
# Crear punto de restauración
!create_restore_point() {
  local backup_dir=".claude-backup-$(date +%s)"
  mkdir -p "$backup_dir"
  
  # Backup de archivos que se van a modificar
  find . -name "*.js" -o -name "*.json" | while read file; do
    cp "$file" "$backup_dir/"
  done
  
  echo "$backup_dir" > .claude-restore-point
  echo "📦 Punto de restauración creado: $backup_dir"
}

# Función de rollback
!rollback() {
  if [ -f ".claude-restore-point" ]; then
    local backup_dir=$(cat .claude-restore-point)
    
    echo "🔄 Restaurando desde: $backup_dir"
    cp -r "$backup_dir"/* ./
    
    rm -rf "$backup_dir"
    rm .claude-restore-point
    
    echo "✅ Rollback completado"
  else
    echo "❌ No hay punto de restauración disponible"
  fi
}
```

#### Cleanup Automático
```bash
# Cleanup al finalizar comando
!cleanup() {
  echo "🧹 Limpiando archivos temporales..."
  
  # Remover archivos temporales
  rm -f .tmp-*
  rm -rf .claude-temp/
  
  # Remover backup si todo salió bien
  if [ "$CLEANUP_BACKUP" = "true" ] && [ -f ".claude-restore-point" ]; then
    local backup_dir=$(cat .claude-restore-point)
    rm -rf "$backup_dir"
    rm .claude-restore-point
  fi
  
  echo "✅ Cleanup completado"
}

# Asegurar cleanup al salir
!trap cleanup EXIT
```

---

## Optimización y Performance

### 1. Comandos Eficientes

#### Evitar Operaciones Costosas
```bash
# ❌ Ineficiente: múltiples llamadas a find
!find . -name "*.js" | wc -l
!find . -name "*.ts" | wc -l  
!find . -name "*.jsx" | wc -l

# ✅ Eficiente: una sola llamada
!find . \( -name "*.js" -o -name "*.ts" -o -name "*.jsx" \) | wc -l
```

#### Cache de Resultados
```bash
# Sistema de cache simple
!get_cached_result() {
  local cache_key="$1"
  local cache_file=".claude-cache/$cache_key"
  
  if [ -f "$cache_file" ]; then
    local cache_age=$(($(date +%s) - $(stat -c %Y "$cache_file")))
    
    # Cache válido por 1 hora
    if [ $cache_age -lt 3600 ]; then
      cat "$cache_file"
      return 0
    fi
  fi
  
  return 1
}

!set_cached_result() {
  local cache_key="$1"
  local result="$2"
  
  mkdir -p ".claude-cache"
  echo "$result" > ".claude-cache/$cache_key"
}
```

#### Paralelización de Tareas
```bash
# Procesamiento en paralelo
!process_files_parallel() {
  local files=("$@")
  local max_jobs=4
  
  for file in "${files[@]}"; do
    # Limitar trabajos concurrentes
    while [ $(jobs -r | wc -l) -ge $max_jobs ]; do
      sleep 0.1
    done
    
    # Procesar archivo en background
    process_single_file "$file" &
  done
  
  # Esperar a que terminen todos los trabajos
  wait
}
```

### 2. Monitoring de Performance

#### Medición de Tiempo
```bash
# Timer para medir performance
!start_timer() {
  export TIMER_START=$(date +%s.%N)
}

!end_timer() {
  local end_time=$(date +%s.%N)
  local duration=$(echo "$end_time - $TIMER_START" | bc)
  echo "⏱️  Tiempo transcurrido: ${duration}s"
}

# Uso
!start_timer
# ... operaciones ...
!end_timer
```

#### Métricas de Recursos
```bash
# Monitoreo de memoria y CPU
!monitor_resources() {
  echo "💾 Uso de memoria: $(free -h | awk '/^Mem:/ {print $3 "/" $2}')"
  echo "🖥️  Carga de CPU: $(uptime | awk -F'load average:' '{print $2}')"
}
```

---

## Testing de Comandos

### 1. Testing Unitario de Comandos

#### Framework de Testing
```bash
# test-command.sh
#!/bin/bash

# Configuración de test
TEST_DIR="test-temp"
COMMAND_DIR="../commands"

setup() {
  mkdir -p "$TEST_DIR"
  cd "$TEST_DIR"
}

teardown() {
  cd ..
  rm -rf "$TEST_DIR"
}

# Test individual
test_code_analysis() {
  local test_file="sample.js"
  
  # Crear archivo de prueba
  cat > "$test_file" << 'EOF'
function hello() {
  console.log("Hello World");
}
EOF
  
  # Ejecutar comando
  local result=$(claude /analysis/code "$test_file")
  
  # Verificar resultado
  if echo "$result" | grep -q "Hello World"; then
    echo "✅ Test code_analysis: PASS"
  else
    echo "❌ Test code_analysis: FAIL"
    return 1
  fi
}

# Ejecutar tests
run_tests() {
  setup
  
  local failed=0
  
  test_code_analysis || ((failed++))
  # Agregar más tests...
  
  teardown
  
  if [ $failed -eq 0 ]; then
    echo "🎉 Todos los tests pasaron"
  else
    echo "💥 $failed tests fallaron"
    exit 1
  fi
}

run_tests
```

### 2. Testing de Integración

#### Test de Workflow Completo
```bash
# integration-test.sh
test_full_workflow() {
  echo "🧪 Testing workflow completo..."
  
  # Setup proyecto de prueba
  mkdir -p test-project/src
  cat > test-project/package.json << 'EOF'
{
  "name": "test-project",
  "version": "1.0.0",
  "scripts": {
    "test": "echo 'test'"
  }
}
EOF
  
  cd test-project
  
  # Test 1: Análisis inicial
  local analysis_result=$(claude /analysis/project .)
  assert_contains "$analysis_result" "package.json"
  
  # Test 2: Setup CI/CD
  claude /automation/ci-setup github-actions
  assert_file_exists ".github/workflows/ci.yml"
  
  # Test 3: Generar documentación
  claude /docs/generate api
  assert_file_exists "docs/api.md"
  
  cd ..
  rm -rf test-project
  
  echo "✅ Workflow completo: PASS"
}
```

### 3. Mocking y Stubs

#### Mock de Herramientas Externas
```bash
# mock-tools.sh
# Mock para npm cuando no está disponible
npm() {
  case "$1" in
    "test") echo "mock: tests passed" ;;
    "install") echo "mock: packages installed" ;;
    "audit") echo '{"vulnerabilities": 0}' ;;
    *) echo "mock: npm $*" ;;
  esac
}

# Mock para git
git() {
  case "$1" in
    "status") echo "On branch main" ;;
    "diff") echo "no changes" ;;
    *) echo "mock: git $*" ;;
  esac
}

export -f npm git
```

---

## Seguridad y Validación

### 1. Validación de Input

#### Sanitización de Argumentos
```bash
# Sanitizar input del usuario
!sanitize_input() {
  local input="$1"
  
  # Remover caracteres peligrosos
  input=$(echo "$input" | tr -d ';&|`$')
  
  # Validar path (no permitir ../)
  if echo "$input" | grep -q '\.\./'; then
    echo "❌ Path inseguro detectado"
    exit 1
  fi
  
  # Validar longitud
  if [ ${#input} -gt 200 ]; then
    echo "❌ Input demasiado largo"
    exit 1
  fi
  
  echo "$input"
}

# Uso
!SAFE_ARGS=$(sanitize_input "$ARGUMENTS")
```

#### Whitelist de Comandos
```bash
# Solo permitir comandos seguros
!safe_command() {
  local cmd="$1"
  local allowed_commands=("ls" "cat" "grep" "find" "wc" "head" "tail")
  
  local cmd_name=$(echo "$cmd" | awk '{print $1}')
  
  if [[ " ${allowed_commands[@]} " =~ " $cmd_name " ]]; then
    eval "$cmd"
  else
    echo "❌ Comando no permitido: $cmd_name"
    exit 1
  fi
}
```

### 2. Protección de Archivos Sensibles

#### Blacklist de Archivos
```bash
# Archivos que nunca deben ser modificados
!check_protected_files() {
  local file="$1"
  local protected_patterns=(
    "\.ssh/"
    "\.aws/"
    "/etc/passwd"
    "/etc/shadow"
    "\.env"
    "\.secret"
  )
  
  for pattern in "${protected_patterns[@]}"; do
    if echo "$file" | grep -q "$pattern"; then
      echo "❌ Archivo protegido: $file"
      exit 1
    fi
  done
}
```

#### Verificación de Permisos
```bash
# Verificar permisos antes de escribir
!check_write_permissions() {
  local file="$1"
  
  if [ -f "$file" ] && [ ! -w "$file" ]; then
    echo "❌ Sin permisos de escritura en: $file"
    exit 1
  fi
  
  local dir=$(dirname "$file")
  if [ ! -w "$dir" ]; then
    echo "❌ Sin permisos de escritura en directorio: $dir"
    exit 1
  fi
}
```

### 3. Auditoria y Logging

#### Log de Seguridad
```bash
# Logging de acciones sensibles
!security_log() {
  local action="$1"
  local file="$2"
  local user=$(whoami)
  local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
  
  echo "[$timestamp] $user: $action on $file" >> .claude-security.log
}

# Uso
!security_log "FILE_WRITE" "$target_file"
!security_log "COMMAND_EXEC" "$command"
```

---

## Documentación y Mantenimiento

### 1. Versionado de Comandos

#### Semantic Versioning
```yaml
---
description: "Comando con versionado"
version: "2.1.0"
changelog:
  - "2.1.0": "Agregar soporte para TypeScript"
  - "2.0.0": "Refactor completo de la lógica"
  - "1.5.2": "Fix en manejo de errores"
  - "1.5.1": "Mejorar documentación"
  - "1.5.0": "Agregar validaciones adicionales"
deprecated: false
---
```

#### Migration Guides
```markdown
## Migración de v1.x a v2.x

### Cambios Breaking
- El parámetro `--output` ahora es requerido
- La estructura del output JSON cambió

### Antes (v1.x)
```bash
claude /analysis/code src/app.js
```

### Después (v2.x)
```bash
claude /analysis/code --file=src/app.js --output=report.json
```

### Compatibilidad
Para mantener compatibilidad temporal, usar:
```bash
claude /analysis/code-legacy src/app.js
```
```

### 2. Documentación Automática

#### Generación de Docs
```bash
# generate-docs.sh
#!/bin/bash

echo "# Comandos Disponibles" > COMMANDS.md
echo "" >> COMMANDS.md

find .claude/commands -name "*.md" | while read cmd_file; do
  # Extraer metadata
  description=$(grep "description:" "$cmd_file" | sed 's/description: *"\(.*\)"/\1/')
  version=$(grep "version:" "$cmd_file" | sed 's/version: *"\(.*\)"/\1/')
  
  # Extraer ruta relativa
  cmd_path=$(echo "$cmd_file" | sed 's/.claude\/commands\///' | sed 's/\.md$//')
  
  # Agregar entrada a documentación
  echo "## /$cmd_path" >> COMMANDS.md
  echo "$description" >> COMMANDS.md
  echo "**Versión:** $version" >> COMMANDS.md
  echo "" >> COMMANDS.md
done
```

### 3. Health Checks para Comandos

#### Validación de Comandos
```bash
# health-check.sh
#!/bin/bash

check_command_health() {
  local cmd_file="$1"
  local issues=()
  
  # Verificar metadata requerida
  if ! grep -q "description:" "$cmd_file"; then
    issues+=("Falta descripción")
  fi
  
  if ! grep -q "allowedTools:" "$cmd_file"; then
    issues+=("Falta definición de herramientas")
  fi
  
  # Verificar sintaxis markdown
  if ! markdown-lint "$cmd_file" &>/dev/null; then
    issues+=("Errores de sintaxis markdown")
  fi
  
  # Reportar problemas
  if [ ${#issues[@]} -gt 0 ]; then
    echo "⚠️  $cmd_file:"
    printf "  - %s\n" "${issues[@]}"
    return 1
  fi
  
  return 0
}

# Verificar todos los comandos
find .claude/commands -name "*.md" | while read cmd; do
  check_command_health "$cmd"
done
```

Esta documentación de patrones y mejores prácticas proporciona una base sólida para desarrollar comandos de Claude Code de alta calidad, mantenibles y seguros.