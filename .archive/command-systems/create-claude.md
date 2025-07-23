# Comando: /create-claude

> **Ubicación:** `.claude/commands/create-claude.md`

Inicia el proyecto capturando la visión y generando CLAUDE.md completo con todos los protocolos

## PROTOCOLO DE EJECUCIÓN

### FASE 1: CAPTURA DE VISIÓN (2-3 minutos máximo)

HACER estas preguntas en orden, esperando respuesta breve:

```markdown
🎯 **¿Qué estás construyendo?**
   (Describe en 1-2 líneas la idea principal)

👥 **¿Para quién es?** 
   (Usuario final o cliente target)

💡 **¿Qué problema resuelve?**
   (El valor principal que aporta)

📏 **¿Cómo lo imaginas?**
   - [ ] MVP simple (pocas features core)
   - [ ] Sistema mediano (múltiples módulos)
   - [ ] Plataforma compleja (muchos usuarios/roles)

🛠️ **¿Tienes preferencias técnicas?**
   (Stack, lenguaje, framework - o "sugiéreme")
```

### FASE 2: EXPLORACIÓN INTELIGENTE

Con las respuestas, EXPLORAR:

1. **Si existe código**:
   - Analizar estructura actual
   - Identificar patrones existentes
   - Detectar stack real vs preferido

2. **Si es proyecto nuevo**:
   - BUSCAR mejores prácticas para el dominio
   - INVESTIGAR arquitecturas similares exitosas
   - PROPONER estructura inicial

3. **Determinar scope real**:
   ```
   MVP → 3-5 features core
   Mediano → 8-12 features
   Complejo → Diseño modular escalable
   ```

### FASE 3: PENSAMIENTO PROFUNDO

PENSAR MUCHO MÁS sobre:
- Arquitectura óptima para el dominio
- Features core vs nice-to-have
- Decisiones técnicas fundamentales
- Estructura que permita crecimiento
- Protocolos necesarios desde el inicio

### FASE 4: GENERACIÓN DE CLAUDE.md COMPLETO

GENERAR el siguiente CLAUDE.md adaptado pero COMPLETO:

```markdown
# CLAUDE.md - [Nombre del Proyecto]

## 🎯 VISIÓN
[Expandir la respuesta de "qué estás construyendo"]

## 👥 USUARIOS
[Detallar para quién es y qué esperan]

## 💡 PROPUESTA DE VALOR
[Qué problema resuelve y cómo específicamente]

## 🧠 PROTOCOLO DE PENSAMIENTO OBLIGATORIO

**REGLA FUNDAMENTAL**: NUNCA actuar sin pensar primero.

### Niveles de Pensamiento
- `PENSAR`: Tareas simples, cambios menores (10-15 segundos)
- `PENSAR MÁS`: Features medianas, decisiones importantes (30-45 segundos)
- `PENSAR MUCHO MÁS`: Arquitectura, sistemas complejos (1-2 minutos)
- `ULTRAPENSAR`: Migraciones, cambios críticos (3-5 minutos)

### Protocolo
1. Analizar la complejidad de la tarea
2. Elegir nivel de pensamiento apropiado
3. Reflexionar sobre approach, riesgos, trade-offs
4. Solo entonces proceder con implementación

## 🔍 HERRAMIENTAS DE INVESTIGACIÓN

### Cuándo Buscar Información Externa
- Tecnología o patrón desconocido
- Necesidad de mejores prácticas actuales
- Problema sin solución obvia
- Integración con servicio externo nuevo

### Protocolo de Búsqueda
1. **MCP Context7**: Para documentación técnica profunda
2. **Web Search**: Para ejemplos y casos reales
3. **Documentar en**: `examples/research/[tema].md`

## 🏗️ ARQUITECTURA
- **Frontend**: [Stack decidido o propuesto]
- **Backend**: [Stack decidido o propuesto]
- **Base de datos**: [Tipo y justificación]
- **Infraestructura**: [Local/Cloud, estrategia]

## 📁 ESTRUCTURA Y REFERENCIAS

### Estructura del Proyecto
```
[nombre-proyecto]/
├── src/                    # Código fuente
├── tests/                  # Tests (TDD obligatorio)
├── examples/              # Crear después del primer código
│   ├── patterns/          # Patrones a seguir
│   ├── anti-patterns/     # Qué evitar
│   └── research/          # Conocimiento adquirido
├── PRPs/                  # Blueprints detallados
│   └── templates/         # Para nuevas features
├── docs/                  # Documentación técnica
└── .claude/
    └── commands/          # Comandos personalizados
```

### Referencias (se llenarán conforme crezca)
- **Patrones**: Ver `examples/patterns/` (crear con `/generate-examples`)
- **Features**: Consultar `roadmap-features.md` (crear con `/extract-features`)
- **Blueprints**: PRPs en `PRPs/` (crear con `/generate-prp`)

## 📋 CONVENCIONES Y REGLAS

### Desarrollo
- **TDD es obligatorio**: Tests primero, código después
- **Commits atómicos**: Un cambio lógico por commit
- **Paralelización**: Maximizar tareas simultáneas

### Estilo de Código
[Inferir del stack o dejar para definir]
- Usar [convención detectada o estándar]
- Nomenclatura: [camelCase/snake_case según lenguaje]
- Estructura: [modular/por features/por capas]

## 🚀 FEATURES CORE (MVP)
[Listar 3-5 features esenciales basadas en la visión]
1. [Feature 1 esencial]
2. [Feature 2 esencial]
3. [Feature 3 esencial]

## 🗺️ ROADMAP INICIAL
[Próximas features después del MVP]
- [ ] [Feature siguiente prioridad]
- [ ] [Feature nice-to-have]
- [ ] [Optimización/mejora]

## 🛠️ COMANDOS

### Desarrollo
```bash
# [Adaptar según stack]
npm run dev          # Servidor desarrollo
npm test            # Ejecutar tests
npm run build       # Build producción
```

### Comandos Claude
- `/update-core`: Actualizar CLAUDE.md y examples
- `/extract-features`: Generar roadmap detallado
- `/generate-prp [feature]`: Crear blueprint
- `/execute-prp`: Implementar blueprint
- `/debug-parallel`: Debug complejo
- `/refactor-smart`: Mejorar código
- `/generate-examples`: Crear patterns

## 🔧 CONFIGURACIÓN

### Setup Inicial
1. [Pasos específicos según stack]
2. Instalar dependencias
3. Configurar entorno
4. Verificar que funciona

### Variables de Entorno
```bash
# Crear .env.local con:
[Variables necesarias según arquitectura]
```

## 💡 WORKFLOW RECOMENDADO

### Para Empezar
1. Implementar primera feature core
2. `/generate-examples` después del primer código
3. `/extract-features` para roadmap detallado

### Desarrollo Continuo
1. Para features nuevas: `/generate-prp`
2. Para bugs: descripción directa o `/debug-parallel`
3. Para mejorar: `/refactor-smart`
4. Periódicamente: `/update-core`

## 🚨 NOTAS
[Cualquier consideración especial del dominio]

---

> **Siguiente paso**: Implementar primera feature core. El sistema evolucionará orgánicamente desde esta base.
```

### FASE 5: CREAR ESTRUCTURA INICIAL

GENERAR estructura de directorios:

```bash
mkdir -p src tests docs examples/{patterns,anti-patterns,research} PRPs/templates .claude/commands
touch .gitignore README.md
```

### FASE 6: PROPUESTA DE SIGUIENTE PASO

```markdown
✅ CLAUDE.md creado con:
- Visión clara del proyecto
- Protocolos establecidos
- Estructura lista para crecer
- Comandos disponibles

📁 Estructura creada:
[mostrar árbol de directorios]

🎯 Siguiente paso recomendado:
1. Revisar CLAUDE.md generado
2. Implementar: [primera feature core más simple]
3. Después: `/generate-examples` para establecer patrones

¿Comenzamos con [primera feature]?
```

## CRITERIOS DE ÉXITO

- CLAUDE.md completo con TODOS los protocolos desde el inicio
- Estructura que guía su propia evolución
- Usuario puede empezar inmediatamente
- Sistema listo para crecer orgánicamente

## NOTAS IMPORTANTES

- El CLAUDE.md inicial tiene toda la estructura pero contenido mínimo
- Las secciones vacías tienen indicaciones de cuándo/cómo llenarlas
- Los protocolos (pensamiento, TDD, etc.) están desde el día 1
- La evolución es natural siguiendo los comandos indicados