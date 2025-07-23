# CLAUDE.md - [Project Name]

**Purpose**: Spanish-language CLAUDE.md template for project documentation and development protocols.

**Authority**: Template for project-specific CLAUDE.md files with integrated thinking protocols and research guidelines.

---

## 🎯 VISIÓN
[Descripción concisa del proyecto y su propósito]

---

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

---

## 🔍 HERRAMIENTAS DE INVESTIGACIÓN

### Cuándo Buscar Información Externa
Si encuentras:
- Tecnología o patrón desconocido
- Necesidad de mejores prácticas actuales
- Problema sin solución obvia en el código base
- Integración con servicio externo

### Protocolo de Búsqueda
1. **MCP Context7**: Para documentación técnica profunda
   ```
   Buscar: "[tecnología] best practices 2024"
   Buscar: "[problema específico] solution patterns"
   ```

2. **Web Search**: Para ejemplos y casos reales
   ```
   Buscar: "[error específico] [tecnología]"
   Buscar: "[librería] production examples"
   ```

3. **Documentar Hallazgos**:
   - Crear/actualizar `examples/research/[tema].md`
   - Agregar patrones descubiertos a `examples/patterns/`
   - Actualizar este archivo si es conocimiento core

---

## 🏗️ ARQUITECTURA
- **Frontend**: [Stack y decisiones clave]
- **Backend**: [Stack y configuración]
- **Base de datos**: [Tipo y consideraciones]
- **Infraestructura**: [Deploy y servicios]

---

## 📁 ESTRUCTURA Y REFERENCIAS

### Estructura Core
```
proyecto/
├── src/                    # Código fuente
├── tests/                  # Tests (TDD obligatorio)
├── examples/              # ← VER: examples/README.md
│   ├── patterns/          # Patrones a seguir
│   ├── anti-patterns/     # Qué evitar
│   └── research/          # Conocimiento adquirido
├── PRPs/                  # ← VER: PRPs/README.md
│   ├── completed/         # Features implementadas
│   └── templates/         # Para nuevas features
├── docs/                  # Documentación técnica
└── .claude/
    └── commands/          # Comandos personalizados
```

### Referencias Importantes
- **Patrones de código**: Ver `examples/patterns/`
- **Anti-patrones**: EVITAR lo documentado en `examples/anti-patterns/`
- **Features planeadas**: Consultar roadmap en `roadmap-features.md`
- **Blueprints detallados**: PRPs en `PRPs/[feature-name].md`

---

## 📋 CONVENCIONES Y REGLAS

### Desarrollo
- **TDD es obligatorio**: Tests primero, código después
- **Commits atómicos**: Un cambio lógico por commit
- **Code review**: Via `/debug-parallel` o segunda terminal

### Estilo de Código
- [Convenciones específicas del proyecto]
- Ver ejemplos en `examples/patterns/`

### Manejo de Errores
- Siempre con tipos específicos
- Logging estructurado
- Ver patrón en `examples/patterns/error-handling.ts`

---

## 🚀 FEATURES IMPLEMENTADAS
- ✅ [Feature 1]: Ver detalles en `PRPs/completed/feature-1.md`
- ✅ [Feature 2]: Documentación en `docs/feature-2.md`
- ✅ [Feature 3]: Ejemplos en `examples/patterns/feature-3-usage.ts`

---

## 🗺️ ROADMAP
Consultar `roadmap-features.md` generado con `/extract-features`

---

## 🛠️ COMANDOS FRECUENTES

### Desarrollo
```bash
npm run dev          # Servidor de desarrollo
npm test -- --watch  # Tests en modo watch
npm run build       # Build de producción
```

### Comandos Claude
- `/create-claude`: Actualizar este archivo
- `/update-core`: Mantener proyecto sincronizado
- `/extract-features`: Generar roadmap
- `/generate-prp [feature]`: Crear blueprint
- `/debug-parallel [error]`: Debug complejo
- `/refactor-smart [componente]`: Mejorar código

---

## 🔧 CONFIGURACIÓN

### Variables de Entorno
```bash
# Ver .env.example para todas las variables
DATABASE_URL=
API_KEY=
```

### Setup Inicial
1. `npm install`
2. Copiar `.env.example` a `.env.local`
3. Configurar base de datos
4. `npm run migrate`

---

## 🔗 INTEGRACIONES EXTERNAS
- **[Servicio 1]**: Docs en [URL], ejemplos en `examples/integrations/servicio1.ts`
- **[Servicio 2]**: API key requerida, ver `.env.example`

---

## 📊 MODELOS DE DATOS
- **Esquema principal**: `prisma/schema.prisma`
- **Tipos TypeScript**: Generados con `npx prisma generate`
- **Factories para tests**: `examples/testing/factories.ts`

---

## 💡 WORKFLOW RECOMENDADO

### Para Nueva Feature
1. `/extract-features` - Ver roadmap actual
2. `/generate-prp [feature]` - Crear blueprint
3. Pensar al nivel apropiado
4. `/execute-prp PRPs/[feature].md` - Implementar
5. Actualizar `examples/` con nuevos patrones

### Para Debugging
1. Describir el problema
2. Si es complejo: `/debug-parallel`
3. Documentar solución en `examples/research/`

### Para Mejorar Código
1. `/refactor-smart [componente]`
2. Actualizar examples si surgen mejores patrones
3. `/update-core` para sincronizar documentación

---

## 🚨 NOTAS CRÍTICAS
- [Gotchas específicos del proyecto]
- [Decisiones importantes y por qué]
- [Limitaciones conocidas]

---

## 📝 CUSTOMIZACIÓN DEL TEMPLATE

### Variables a Reemplazar
- `[Project Name]`: Nombre del proyecto
- `[Stack y decisiones clave]`: Tecnologías específicas del proyecto
- `[Convenciones específicas del proyecto]`: Reglas de código específicas
- `[Feature N]`: Features implementadas específicas
- `[Servicio N]`: Integraciones externas específicas

### Secciones Opcionales
- Eliminar secciones no aplicables al proyecto
- Agregar secciones específicas del dominio
- Personalizar comandos según necesidades del proyecto

---

> **Recuerda**: Este archivo es la fuente de verdad. Mantenlo actualizado con `/update-core`.

**Template Type**: Spanish-language CLAUDE.md project template
**Used By**: Spanish-speaking development projects
**Language**: Spanish
**Integration**: Compatible with Claude Code development workflows