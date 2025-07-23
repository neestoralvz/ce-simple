# Mejores Prácticas para Claude Code - Guía Completa

Claude Code es una herramienta de línea de comandos para codificación agéntica que proporciona acceso directo al modelo sin imponer flujos de trabajo específicos. Esta flexibilidad la convierte en una herramienta poderosa pero requiere desarrollar mejores prácticas para maximizar su efectividad.

---

## 1. 🔧 Personaliza tu Configuración

### Crear archivos CLAUDE.md estratégicos

CLAUDE.md es un archivo especial que Claude lee automáticamente para obtener contexto. Úsalo para documentar:

```markdown
# Comandos bash comunes
- npm run build: Construir el proyecto
- npm run typecheck: Ejecutar verificador de tipos
- npm test: Ejecutar suite de pruebas

# Estilo de código
- Usar sintaxis ES modules (import/export), no CommonJS (require)
- Desestructurar imports cuando sea posible (ej. import { foo } from 'bar')
- Preferir const sobre let, let sobre var

# Flujo de trabajo
- Verificar tipos después de hacer cambios de código
- Ejecutar pruebas individuales, no toda la suite, para mejor rendimiento
- Commits atómicos con mensajes descriptivos

# Configuración del entorno
- Usar Node.js 18+ con npm 9+
- Variables de entorno en .env.local
- Base de datos local: PostgreSQL 14

# Comportamientos específicos del proyecto
- La API rate-limita en desarrollo, usar delays entre requests
- Tests de integración requieren base de datos limpia
- Build en Windows requiere configuración adicional de paths
```

### Ubicaciones estratégicas para CLAUDE.md

**Jerarquía de archivos CLAUDE.md (orden de prioridad):**

1. **Proyecto actual:** `./CLAUDE.md` (versionar en git para compartir con equipo)
2. **Proyecto local:** `./CLAUDE.local.md` (ignorar en git para configuración personal)
3. **Monorepo padre:** `../CLAUDE.md` (contexto compartido)
4. **Subdirectorios:** `./components/CLAUDE.md` (contexto específico)
5. **Global personal:** `~/.claude/CLAUDE.md` (aplica a todas las sesiones)

### Optimizar archivos CLAUDE.md

**Principios para CLAUDE.md efectivos:**

```markdown
# ✅ Buenas prácticas para CLAUDE.md

## Comandos más usados (ordenar por frecuencia)
- npm run dev: Servidor de desarrollo
- npm run test:watch: Tests en modo watch
- npm run lint:fix: Corregir issues de linting automáticamente

## Patrones críticos del proyecto
- IMPORTANTE: Siempre usar TypeScript strict mode
- OBLIGATORIO: Tests para toda nueva funcionalidad
- CRÍTICO: Validar permisos antes de operaciones de base de datos

## Archivos clave del sistema
- src/types/index.ts: Definiciones de tipos principales
- src/utils/validation.ts: Funciones de validación compartidas
- src/config/database.ts: Configuración de base de datos
```

**Usa la tecla `#` para documentar automáticamente:**
- Presiona `#` seguido de una instrucción
- Claude incorpora automáticamente el contenido al CLAUDE.md relevante
- Incluye cambios de CLAUDE.md en commits para beneficio del equipo

### Configurar lista de herramientas permitidas

**Cuatro métodos para gestionar permisos:**

1. **Durante sesión:** Seleccionar "Always allow" cuando se solicite
2. **Comando en sesión:** `/permissions` para agregar/remover herramientas
3. **Configuración manual:** Editar `.claude/settings.json` o `~/.claude.json`
4. **Flag CLI:** `--allowedTools` para permisos específicos de sesión

**Ejemplos de configuración de permisos:**
```bash
# Permitir edición de archivos siempre
/permissions add Edit

# Permitir commits de git específicos
/permissions add "Bash(git commit:*)"

# Permitir navegación con Puppeteer MCP
/permissions add mcp__puppeteer__puppeteer_navigate
```

### Instalar GitHub CLI

Con `gh` CLI instalado, Claude puede:
- ✅ Crear issues y pull requests
- ✅ Leer comentarios de código
- ✅ Gestionar releases y milestones
- ✅ Interactuar con GitHub Actions

---

## 2. 🛠️ Amplía las Herramientas de Claude

### Usar Claude con herramientas bash

**Claude hereda tu entorno bash completo:**

```bash
# Documentar herramientas personalizadas en CLAUDE.md
# Ejemplo de funciones bash útiles para Claude

# Función para setup rápido de proyecto
setup_project() {
    npm install
    cp .env.example .env.local
    npm run db:migrate
    npm run dev
}

# Función para cleanup de ramas
cleanup_branches() {
    git branch --merged | grep -v master | xargs -n 1 git branch -d
}

# Función para análisis de bundle
analyze_bundle() {
    npm run build:analyze
    open dist/bundle-analyzer.html
}
```

**En CLAUDE.md, documenta:**
```markdown
# Herramientas personalizadas disponibles
- setup_project: Configuración completa de proyecto nuevo
- cleanup_branches: Eliminar ramas ya mergeadas
- analyze_bundle: Analizar tamaño de bundle y dependencias
- Para ver documentación: <comando> --help
```

### Usar Claude con MCP (Model Context Protocol)

**Tres formas de configurar MCP:**

1. **Configuración de proyecto** (`.mcp.json` en raíz del proyecto):
```json
{
  "mcpServers": {
    "puppeteer": {
      "command": "npx",
      "args": ["@anthropic-ai/mcp-server-puppeteer"]
    },
    "sentry": {
      "command": "npx", 
      "args": ["@sentry/mcp-server"],
      "env": {
        "SENTRY_ORG": "tu-org",
        "SENTRY_PROJECT": "tu-proyecto"
      }
    }
  }
}
```

2. **Configuración global** (`~/.claude/mcp.json`):
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["@anthropic-ai/mcp-server-filesystem", "/ruta/a/directorio"]
    }
  }
}
```

3. **Debug MCP:** Usar `--mcp-debug` para identificar problemas de configuración

### Crear comandos slash personalizados

**Estructura de comandos personalizados:**
```
.claude/
└── commands/
    ├── fix-github-issue.md
    ├── analyze-performance.md
    └── frontend/
        └── component-review.md
```

**Ejemplo de comando con argumentos:**
```markdown
<!-- .claude/commands/fix-github-issue.md -->
Analiza y corrige el issue de GitHub: $ARGUMENTS.

Sigue estos pasos:
1. Usar `gh issue view $ARGUMENTS` para obtener detalles
2. Entender el problema descrito
3. Buscar archivos relevantes en el codebase
4. Implementar cambios necesarios
5. Escribir y ejecutar tests de verificación
6. Asegurar que el código pase linting y type checking
7. Crear mensaje de commit descriptivo
8. Push y crear PR con descripción detallada

Recuerda usar GitHub CLI (`gh`) para todas las tareas relacionadas con GitHub.
```

**Uso:** `/fix-github-issue 1234` corrige automáticamente el issue #1234

---

## 3. 🔄 Flujos de Trabajo Comprobados

### A. Explorar → Planificar → Codificar → Commit

**Flujo paso a paso:**

```bash
# 1. Exploración (SIN codificar aún)
> lee los archivos que manejan autenticación y explica la arquitectura actual, pero NO escribas código todavía

# 2. Planificación con pensamiento extendido
> piensa profundamente sobre cómo implementar autenticación de dos factores. considera múltiples enfoques, evalúa tradeoffs, y crea un plan detallado

# 3. Verificación del plan
> crea un documento con tu plan en ./docs/2fa-implementation-plan.md para que pueda revisarlo antes de proceder

# 4. Implementación
> implementa la solución siguiendo exactamente el plan aprobado. verifica cada componente antes de continuar al siguiente

# 5. Commit y PR
> commit los cambios con mensaje descriptivo y crea un PR explicando la implementación
```

**Niveles de pensamiento extendido:**
- `"piensa"` → pensamiento básico
- `"piensa fuerte"` → análisis más profundo  
- `"piensa más fuerte"` → evaluación exhaustiva
- `"ultrapiensa"` → máximo presupuesto de análisis

### B. Tests Primero → Código → Iteración

**Flujo TDD optimizado:**

```bash
# 1. Escribir tests (desarrollo dirigido por tests)
> escribe tests completos para la funcionalidad de autenticación 2FA basándote en estos requisitos. esto es TDD, así que NO implementes la funcionalidad aún, solo los tests

# 2. Verificar que fallan
> ejecuta los tests y confirma que fallan como se esperaba. NO escribas código de implementación todavía

# 3. Commit de tests
> commit los tests con mensaje "Add tests for 2FA authentication"

# 4. Implementar hasta pasar tests
> ahora implementa el código para que todos los tests pasen. NO modifiques los tests. sigue iterando hasta que todos pasen

# 5. Verificación independiente
> usa un subagente para verificar que la implementación no está sobreajustada a los tests específicos

# 6. Commit de implementación
> commit la implementación final con mensaje descriptivo
```

### C. Código → Screenshot → Iteración Visual

**Para desarrollo de UI:**

```bash
# 1. Configurar captura de pantalla
> configura Puppeteer MCP para tomar screenshots del navegador

# 2. Implementar diseño inicial
> implementa este mockup (arrastra imagen aquí) en React. después toma un screenshot del resultado

# 3. Iterar hasta perfección
> compara tu implementación con el mockup original. itera hasta que coincidan exactamente. toma screenshots después de cada cambio

# 4. Commit final
> cuando estés satisfecho con el resultado visual, commit los cambios
```

### D. Modo YOLO Seguro

**Para tareas de bajo riesgo:**
```bash
# Modo sin supervisión (usar con precaución)
claude --dangerously-skip-permissions

# Solo en contenedores sin acceso a internet
docker run --rm -it -v $(pwd):/workspace claude-container
```

**Casos de uso seguros:**
- ✅ Corregir errores de linting
- ✅ Generar código boilerplate
- ✅ Refactoring automático
- ❌ Operaciones de base de datos
- ❌ Deployment a producción

### E. Q&A de Codebase

**Preguntas efectivas para onboarding:**

```bash
# Arquitectura general
> ¿cómo funciona el sistema de logging en este proyecto?
> ¿cuál es el flujo completo de una request HTTP desde router hasta response?

# Implementación específica
> ¿qué hace este async move { ... } en la línea 134 de foo.rs?
> ¿por qué estamos llamando foo() en lugar de bar() en la línea 333?

# Casos edge y diseño
> ¿qué casos edge maneja CustomerOnboardingFlowImpl?
> ¿cuál sería el equivalente en Java de la línea 334 de baz.py?

# Debugging e historia
> ¿qué cambios causaron el bug en el endpoint /api/users?
> ¿quién diseñó esta API y cuál fue la justificación?
```

### F. Gestión Avanzada de Git

**Claude maneja operaciones complejas de git:**

```bash
# Análisis de historial
> busca en el historial de git qué cambios se incluyeron en v1.2.3
> ¿quién es el owner de la funcionalidad de pagos?
> ¿por qué se diseñó esta API de esta manera? busca en commits y PRs

# Operaciones complejas
> resuelve estos conflictos de rebase manteniendo ambas implementaciones
> revierte solo los cambios del archivo auth.js del último commit
> compara y aplica este patch del branch feature/new-auth
```

### G. Integración con GitHub

**Automatización de workflows de GitHub:**

```bash
# Crear PRs inteligentes
> crear un pr # Claude analiza diff y contexto automáticamente

# Resolver comentarios de code review
> corrige todos los comentarios del PR #123 y push los cambios

# Triage de issues
> categoriza y asigna labels a todos los issues abiertos del último mes

# CI/CD debugging  
> analiza por qué falló el último build y propón soluciones
```

### H. Trabajo con Jupyter Notebooks

**Para investigadores y data scientists:**

```bash
# Análisis de notebooks
> analiza este notebook y explica qué hace cada celda
> optimiza las visualizaciones para que sean más aesthetically pleasing

# Limpieza y mejora
> limpia este notebook antes de compartirlo con colegas. mejora comentarios, organiza código, y haz las visualizaciones más professional
```

---

## 4. ⚡ Optimización de Flujo de Trabajo

### Ser específico en las instrucciones

**Transformar instrucciones vagas en específicas:**

| ❌ Vago | ✅ Específico |
|---------|---------------|
| `agregar tests para foo.py` | `escribir tests unitarios para foo.py cubriendo el caso edge donde el usuario no está logueado. evitar mocks, usar datos reales de test` |
| `¿por qué ExecutionFactory tiene una API tan rara?` | `busca en el historial de git de ExecutionFactory y resume cómo evolucionó su API, incluyendo decisiones de diseño y refactorings principales` |
| `agregar widget de calendario` | `estudia cómo están implementados los widgets existentes en la home page, especialmente HotDogWidget.php. luego sigue ese patrón para implementar un widget de calendario que permita seleccionar mes y paginar años. construir desde cero sin librerías externas` |

### Proporcionar imágenes a Claude

**Métodos para compartir imágenes:**

1. **Screenshot directo:** `cmd+ctrl+shift+4` (macOS) → `ctrl+v` para pegar
2. **Arrastrar y soltar:** Directamente al input de prompt
3. **Rutas de archivo:** `analiza esta imagen: /path/to/mockup.png`

**Casos de uso efectivos:**
- 🎨 Mockups de diseño como referencia para desarrollo UI
- 📊 Charts y gráficos para análisis de datos
- 🐛 Screenshots de errores para debugging
- 📱 Screenshots de apps móviles para replicar funcionalidad

### Mencionar archivos específicos

**Usar tab-completion para referencias exactas:**
```bash
# Tab-completion ayuda a encontrar archivos rápidamente
> optimiza el rendimiento de src/components/UserDash[TAB]
# Se completa a: src/components/UserDashboard.tsx

> revisa la lógica en utils/auth[TAB] y tests/unit/auth[TAB]
# Referencias múltiples para contexto completo
```

### Proporcionar URLs

**URLs para contexto adicional:**
```bash
# Documentación externa
> implementa esta funcionalidad siguiendo la documentación en https://docs.stripe.com/payments/intents

# Para evitar prompts de permisos repetidos
/permissions add domain:docs.stripe.com
/permissions add domain:api.github.com
```

### Corrección de curso temprana y frecuente

**Herramientas de corrección:**

1. **Planificación previa:**
```bash
> crea un plan detallado para implementar webhooks de Stripe. NO codes hasta que confirme que el plan se ve bien
```

2. **Interrumpir con Escape:**
   - `Escape` → interrumpe cualquier operación preservando contexto
   - `Escape + Escape` → salta atrás en historial para editar prompts previos

3. **Deshacer cambios:**
```bash
> deshaz los últimos cambios al archivo auth.js y toma un enfoque diferente usando JWT en lugar de sessions
```

### Usar /clear para mantener contexto enfocado

**Cuándo limpiar contexto:**
- ✅ Entre tareas no relacionadas
- ✅ Cuando el contexto tiene >50 archivos cargados
- ✅ Después de completar features grandes
- ✅ Cuando Claude parece "distraído" por conversación previa

```bash
# Ejemplo de sesión limpia
> /clear
Contexto limpiado. ¿En qué puedo ayudarte?

> implementa autenticación OAuth para la aplicación React
```

### Usar checklists para workflows complejos

**Para tareas grandes o complejas:**

```bash
# 1. Crear checklist inicial
> ejecuta eslint y crea un checklist en ./fix-lint-issues.md con todos los errores encontrados, incluyendo archivos y números de línea

# 2. Trabajo sistemático
> trabaja a través del checklist en fix-lint-issues.md. corrige cada issue uno por uno, verifica la corrección, y marca como completado antes de continuar al siguiente
```

**Ejemplo de checklist generado:**
```markdown
# Lint Issues - Fix Checklist

## Critical Issues (must fix first)
- [ ] src/auth.js:23 - unused variable 'token'
- [ ] src/api/users.js:45 - missing return statement
- [ ] src/components/Header.jsx:12 - missing prop validation

## Style Issues 
- [ ] src/utils/format.js:8 - inconsistent spacing
- [ ] src/hooks/useApi.js:34 - prefer const over let
- [ ] src/types/index.ts:67 - missing semicolon

## Total: 6 issues | Fixed: 0 | Remaining: 6
```

### Métodos para pasar datos a Claude

**Opciones ordenadas por frecuencia de uso:**

1. **Copy/paste directo** (más común)
2. **Pipe de entrada:** `cat error.log | claude`
3. **Comandos bash:** `> ejecuta grep "ERROR" /var/log/app.log y analiza los patrones`
4. **Lectura de archivos:** `> lee y analiza data/sales-2024.csv`
5. **URLs y fetch:** `> analiza los datos de https://api.example.com/metrics`

---

## 5. 🤖 Modo Headless para Automatización

### Automatización de infraestructura

**Sintaxis básica:**
```bash
# Modo headless con prompt
claude -p "analiza este log y reporta errores críticos" < error.log

# Con formato JSON estructurado
claude -p "categoriza estos issues por severidad" --output-format stream-json < issues.txt

# Con herramientas específicas permitidas
claude -p "corrige errores de linting" --allowedTools Edit,Bash
```

### Triage automático de issues

**Script para automation de GitHub:**
```bash
#!/bin/bash
# .github/scripts/auto-triage.sh

gh api repos/$GITHUB_REPOSITORY/issues | claude -p "
analiza estos issues de GitHub y asigna labels apropiados:
- 'bug' para reportes de bugs
- 'feature' para requests de funcionalidad  
- 'documentation' para mejoras de docs
- 'good first issue' para issues apropiados para nuevos contribuidores

retorna solo los comandos gh necesarios para aplicar los labels
" --output-format json
```

### Claude como linter avanzado

**Linting subjetivo y contextual:**
```bash
# En package.json
{
  "scripts": {
    "lint:claude": "claude -p 'revisa este código en busca de: typos, comentarios obsoletos, nombres de variables misleading, y oportunidades de refactoring. reporta cada issue con archivo:línea y descripción' --allowedTools Edit"
  }
}

# En pre-commit hook
#!/bin/sh
git diff --cached --name-only '*.js' '*.ts' | claude -p "revisa estos archivos modificados por problemas de calidad de código" --output-format text
```

---

## 6. 🚀 Flujos Multi-Claude Avanzados

### Un Claude codifica, otro verifica

**Workflow de verificación cruzada:**

```bash
# Terminal 1: Claude principal
> implementa sistema de caching Redis para la API

# Terminal 2: Claude revisor (después de /clear)
> revisa la implementación de caching en src/cache/ y identifica problemas potenciales de performance, seguridad, o bugs

# Terminal 3: Claude integrador
> lee tanto el código original como el feedback del revisor. implementa las mejoras sugeridas manteniendo la funcionalidad original
```

### Múltiples checkouts de repositorio

**Para trabajo paralelo intensivo:**
```bash
# Configuración inicial
mkdir -p ~/projects/myapp-{main,feature-a,feature-b,hotfix}
cd ~/projects/myapp-main && git clone git@github.com:user/myapp.git .
cd ~/projects/myapp-feature-a && git clone git@github.com:user/myapp.git . && git checkout -b feature-a
cd ~/projects/myapp-feature-b && git clone git@github.com:user/myapp.git . && git checkout -b feature-b
cd ~/projects/myapp-hotfix && git clone git@github.com:user/myapp.git . && git checkout -b hotfix-auth

# Terminal tabs
# Tab 1: Main branch para reviews y merges
cd ~/projects/myapp-main && claude

# Tab 2: Desarrollo de feature A
cd ~/projects/myapp-feature-a && claude

# Tab 3: Desarrollo de feature B  
cd ~/projects/myapp-feature-b && claude

# Tab 4: Hotfix crítico
cd ~/projects/myapp-hotfix && claude
```

### Git worktrees optimizados

**Método ligero para múltiples tareas:**
```bash
# Crear worktrees
git worktree add ../myapp-auth feature/auth-system
git worktree add ../myapp-ui feature/new-dashboard  
git worktree add ../myapp-api feature/api-v2

# Lanzar Claude en cada worktree
cd ../myapp-auth && claude &
cd ../myapp-ui && claude &
cd ../myapp-api && claude &

# Gestión de worktrees
git worktree list                    # Listar todos los worktrees
git worktree remove ../myapp-auth    # Remover cuando termine
```

**Consejos para worktrees:**
- ✅ Usar convenciones de nombres consistentes
- ✅ Una tab de terminal por worktree
- ✅ Configurar notificaciones (iTerm2) cuando Claude necesite atención
- ✅ Ventanas IDE separadas por worktree
- ✅ Cleanup al terminar: `git worktree remove`

### Modo headless con harness personalizado

**Pattern 1: Fan-out para migraciones masivas**
```bash
#!/bin/bash
# migrate-components.sh

# 1. Generar lista de tareas
claude -p "genera una lista de todos los archivos .jsx que necesitan migrar de React a Vue" > tasks.txt

# 2. Procesar cada tarea
while IFS= read -r file; do
    echo "Migrando $file..."
    result=$(claude -p "migra $file de React a Vue. retorna 'OK' si exitoso, 'FAIL' si falló" --allowedTools Edit,Bash 2>&1)
    
    if [[ $result == *"OK"* ]]; then
        echo "✅ $file migrado exitosamente"
        git add "$file" && git commit -m "Migrate $file from React to Vue"
    else
        echo "❌ Error migrando $file: $result"
        echo "$file" >> failed-migrations.txt
    fi
done < tasks.txt
```

**Pattern 2: Pipeline de procesamiento**
```bash
# Pipeline de análisis de logs
tail -f /var/log/app.log | \
claude -p "analiza estos logs en tiempo real y alerta sobre errores críticos. retorna JSON con timestamp, level, y mensaje" --output-format stream-json | \
jq -r 'select(.level == "CRITICAL") | "\(.timestamp): \(.message)"' | \
while read alert; do
    echo "$alert" | mail -s "Alert Crítico" devops@company.com
done
```

---

## 🎯 Métricas de Éxito y KPIs

### Indicadores de productividad
- **⏱️ Tiempo de onboarding:** Reducción del 60-80% con Q&A de codebase
- **🐛 Resolución de bugs:** 3-5x más rápido con análisis automático
- **✅ Calidad de código:** 90%+ de tests de primera pasada
- **🔄 Velocidad de iteración:** 2-3x ciclos más rápidos de development

### Señales de uso efectivo
- ✅ Instrucciones específicas → resultados precisos en primer intento
- ✅ CLAUDE.md actualizado → Claude entiende contexto del proyecto
- ✅ Workflows automatizados → menos tareas manuales repetitivas
- ✅ Múltiples instancias Claude → paralelización efectiva de trabajo

---

## 📚 Recursos y Referencias

- **📖 Documentación completa:** [claude.ai/code](https://claude.ai/code)
- **🔧 Implementación de referencia:** [Claude Code Docker Dev Container](https://github.com/anthropics/claude-code/tree/main/.devcontainer)
- **🤝 Comunidad:** Tag [@AnthropicAI](https://twitter.com/AnthropicAI) para compartir experiencias
- **📝 MCP Documentation:** [Model Context Protocol](https://docs.anthropic.com/claude/docs/mcp)

---

> **💡 Consejo final:** Claude Code es más efectivo cuando se trata como un ingeniero experimentado en tu equipo. Dale contexto, sé específico con las instrucciones, y no dudes en iterar hasta obtener el resultado perfecto.