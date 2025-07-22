# Dual Self-Contained Architecture

## 🎯 ARQUITECTURA DUAL AUTOCONTENIDA

**PRINCIPIO FUNDAMENTAL**: 
- **`system/`** = Autocontenido para documentación, arquitectura, protocolos, templates
- **`components/`** = Autocontenido para ejecución (orchestrators, agents, behaviors)

### Separación de Responsabilidades
```
system/          # DOCUMENTACIÓN Y DISEÑO
├── Todo el diseño del sistema, protocolos, arquitectura
├── Templates, guías, especificaciones
├── Solo referencias internas a system/
└── No ejecución, solo documentación

components/      # EJECUCIÓN Y OPERACIÓN  
├── orchestrators/  # Coordinadores ejecutables
├── agents/         # Agentes especializados ejecutables
├── behaviors/      # Comportamientos aplicables
└── Solo referencias internas a components/
```

### Autocontención Independiente
```
system/
├── Toda la documentación, arquitectura, protocolos
├── Solo puede referenciar otros archivos en system/
├── Diseño completo del sistema de componentes
└── Especificaciones de cómo deben funcionar los componentes

components/
├── orchestrators/  # Solo pueden referenciar otros components/
├── agents/         # Solo pueden referenciar otros components/  
├── behaviors/      # Solo pueden referenciar otros components/
└── Implementación ejecutable del sistema diseñado en system/
```

## 🚫 REGLAS DE DOBLE AUTOCONTENCIÓN

### Para system/ (Documentación)
```markdown
✅ PERMITIDO: system/protocols/anything
✅ PERMITIDO: system/architecture/anything
✅ PERMITIDO: system/templates/anything
❌ PROHIBIDO: components/anything
❌ PROHIBIDO: handoffs/anything  
❌ PROHIBIDO: CLAUDE.md (debe estar autocontenido también)
```

### Para components/ (Ejecución)
```markdown
✅ PERMITIDO: components/orchestrators/anything
✅ PERMITIDO: components/agents/anything
✅ PERMITIDO: components/behaviors/anything
❌ PROHIBIDO: system/anything
❌ PROHIBIDO: handoffs/anything
❌ PROHIBIDO: archivos externos
```

## 📋 IMPLEMENTACIÓN DE DOBLE AUTOCONTENCIÓN

### components/ - Ejecución Pura
**Estructura final:**
```
components/
├── orchestrators/    # Coordinadores que solo referencian components/
├── agents/          # Agentes que solo referencian components/
├── behaviors/       # Behaviors que solo referencian components/
├── shared/         # Información compartida SOLO entre components/
└── interfaces/     # Interfaces para operaciones externas (Claude Code tools)
```

### system/ - Documentación Pura  
**Debe contener:**
```
system/
├── architecture/    # Diseño completo del sistema
├── protocols/       # Todos los protocolos del sistema
├── templates/       # Templates para crear componentes
├── guides/         # Guías de uso y operación
└── Toda la documentación necesaria para entender el sistema
```

### Separación Total de Responsabilidades
```
system/     → DISEÑA cómo deben funcionar los components/
components/ → EJECUTA lo que está diseñado en system/
```

**NO HAY COMUNICACIÓN CRUZADA** - Cada carpeta es completamente autocontenida

## 🔧 MIGRATION TO DUAL AUTOCONTENCIÓN

### Para components/ (Ejecución)
**Eliminar referencias externas:**
- ❌ Remover todas las referencias a `../system/`
- ❌ Remover todas las referencias a `../handoffs/`  
- ✅ Solo mantener referencias internas a `components/`
- ✅ Crear información mínima necesaria dentro de `components/shared/`

### Para system/ (Documentación)  
**Asegurar autocontención:**
- ✅ Todo el diseño del sistema debe estar en system/
- ✅ Protocolos completos para cómo funcionan los components/
- ✅ Templates y guías para crear components/
- ❌ No referencias a components/ (no necesita saber de implementación)

### Información Duplicada Necesaria
Cierta información crítica debe existir en ambos lugares:
- **system/**: Como documentación y especificación
- **components/shared/**: Como información operacional mínima

**Ejemplo**: Cognitive load limits
- `system/protocols/cognitive-load-limits.md` - Especificación completa
- `components/shared/cognitive-load-limits.md` - Límites operacionales básicos

## ⚡ INTERFACE RULES

### External System Interface
```markdown
# components/interfaces/external-system-interface.md
## 🎯 PURPOSE
Define cómo components/ interactúa con sistema externo

## 📋 AVAILABLE OPERATIONS
- Task() deployment → External agent coordination
- File operations → Read/Write outside components/
- Web operations → WebFetch, WebSearch
- System operations → Bash, LS, Glob, Grep

## 🔧 USAGE PROTOCOL
Components solo pueden usar external interface para operaciones fuera de components/
```

### Handoff Interface  
```markdown
# components/interfaces/handoff-interface.md
## 🎯 PURPOSE
Define cómo components/ maneja handoffs sin acceso directo a handoffs/

## 📋 HANDOFF OPERATIONS
- Create handoff → Via external interface
- Read handoff status → Via external interface  
- Update handoff → Via external interface
- Archive handoff → Via external interface
```

## 📊 VALIDATION RULES

### Self-Containment Validation
```bash
# Comando de validación (para ejecutar externamente)
find components/ -name "*.md" -exec grep -l "\.\./\." {} \; | wc -l
# Resultado esperado: 0 (cero archivos con referencias externas)
```

### Link Integrity Check
```bash
# Validar que todos los links apunten dentro de components/
grep -r "\[.*\](" components/ | grep -v "components/" | grep -v "http"
# Resultado esperado: vacío (sin links externos)
```

### Dependency Audit
```bash  
# Verificar imports externos
grep -r "@import\[" components/ | grep -v "components/"
# Resultado esperado: vacío (sin imports externos)
```

## 🎯 IMPLEMENTATION STRATEGY

### Phase 1: Critical Dependencies (Immediate)
- Copy VVP protocol to components/protocols/
- Copy orchestrator rules to components/protocols/
- Update 3 affected components to use internal copies

### Phase 2: Templates & Standards (Short-term)
- Create components/templates/ directory
- Copy verification templates
- Create communication standards
- Update template-dependent components

### Phase 3: Interfaces & Abstractions (Medium-term)  
- Create components/interfaces/ directory
- Implement external system interface
- Create handoff abstraction interface
- Update components to use interfaces

### Phase 4: Complete Self-Containment (Long-term)
- Create components/shared/ directory  
- Extract and summarize architecture information
- Implement full self-containment validation
- Remove all external dependencies

## ✅ SUCCESS CRITERIA

### Metrics for Complete Self-Containment
- **External references**: 0 files with external links
- **Import compliance**: 100% internal imports only
- **Interface usage**: 100% external operations via interfaces
- **Validation passing**: All validation commands return empty results

### Benefits Achieved
- **Portability**: components/ directory fully portable
- **Independence**: Zero external file dependencies
- **Modularity**: True modular architecture
- **Reliability**: No broken external link risk
- **Testing**: Complete isolated testing capability

---

**Esta arquitectura autocontenida permite que components/ funcione como un ecosistema completamente independiente donde cada componente solo puede interactuar con otros componentes internos o con sistemas externos a través de interfaces definidas.**