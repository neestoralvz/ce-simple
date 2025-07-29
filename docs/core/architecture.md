# Arquitectura Minimalista del Sistema

## Estructura Esencial

### Directorio Principal
```
/.claude/commands/              (9 WORKFLOWS INDEPENDIENTES)
/user-vision/raw/conversations/ (CONVERSACIONES RAW)
/user-vision/                   (FUENTE DE VERDAD USUARIO)
/handoff/                       (CONTINUIDAD ENTRE SESIONES)
/actions:docs/                          (MÓDULOS TÉCNICOS ESPECIALIZADOS)
```

### Jerarquía de Autoridad
```
user-vision/TRUTH_SOURCE.md     (AUTORIDAD SUPREMA)
    ↓
user-vision/layer3/             (DOCUMENTACIÓN OFICIAL)
    ↓  
CLAUDE.md                       (DISPATCHER ULTRA-DENSO)
    ↓
docs/                           (MÓDULOS TÉCNICOS)
    ↓
/.claude/commands/              (WORKFLOWS EJECUTABLES)
```

## Árbol de Decisiones Contextual

### Core Auto-Imports (Contenido Ultra-Denso)
- `@user-vision/TRUTH_SOURCE.md` - Autoridad suprema siempre cargada
- `@user-vision/layer3/architecture_principles.md` - Si contexto arquitectural

### Imports Condicionales
- SI menciona "metodología/socratico" → `@user-vision/layer3/methodology_guide.md`
- SI debugging/problemas → `@user-vision/layer3/implementation_guide.md`  
- SI necesita referencia rápida → `@user-vision/layer3/quick_reference.md`

### Exclusiones Absolutas
**NUNCA importar**: Layer1 (quotes dispersos) o Layer2 (síntesis intermedia)

## Principios Arquitecturales

### Independencia de Comandos
"Algo que veo que estas haciendo y que es uno mas de los principios que dbeemos de respetar es el que los comandos son autocontenidos entre ellos y solo pueden conectarse con otros comandos"

### Modelo de Orquestación
"Algo de lo que no hemos hablado y es muy importante porque es la manera principal en la que se tiene que comportar el agente principal SIEMPRE es la de ser orquestado de subagentes"

### Regeneración Limpia
"es importante eliminar archivos y crealos desde cero bajo los lineamientos que vamos actualizando, pues si solo vamos construyendo sobre los anteriores existe demasiado sesgo por la informacion que ya esta"

## Diseño Modular

### /actions:docs/ como Complemento Técnico
- **docs/core/**: Principios fundamentales inmutables
- **docs/workflows/**: Documentación detallada de comandos
- **docs/maintenance/**: Reglas y validaciones del sistema

### CLAUDE.md como Dispatcher
- **Ultra-denso**: Máximo 200 líneas efectivas
- **Referencias modulares**: Apunta a docs/ vs duplicar contenido
- **Esencia pura**: Solo principios fundamentales y coordinación

### user-vision/ como Fuente de Verdad
- **Intocable**: Nunca se modifica automáticamente  
- **Autoridad suprema**: Sobrescribe cualquier conflicto
- **Preservación total**: Voz del usuario sin contaminación

## Flujos de Información

### Captura de Conversaciones
```
Conversación → user-vision/raw/conversations/ 
           → /workflows:distill → Layer 1, 2, 3
           → TRUTH_SOURCE.md actualización
           → CLAUDE.md regeneración automática
```

### Coordinación Entre Comandos
```
/workflows:start → orienta y carga contexto
otros comandos → ejecutan tareas específicas  
/actions:git → integra con todos para commits inteligentes
/roles:partner → valida decisiones arquitecturales
/workflows:close → captura conversación y commit cambios
```

### Evolución del Sistema
```
Conversación natural → raw/ storage
                   → /workflows:distill processing  
                   → Layer distillation
                   → TRUTH_SOURCE.md crystallization
                   → System adaptation
```

## Prevención de Complejidad

### Anti-Bloat Sistémico
- **Modularización forzada**: Contenido técnico en docs/ no en CLAUDE.md
- **Referencias vs duplicación**: Una fuente de verdad por concepto
- **Regeneración periódica**: Previene sesgo acumulativo
- **Validación automática**: Previene deriva de principios

### Restricciones de Crecimiento
- **CLAUDE.md**: ≤ 200 líneas efectivas máximo
- **docs/ módulos**: Especializados y enfocados  
- **user-vision/**: Solo crece por decisiones del usuario
- **comandos**: Independientes, no interdependencias complejas

---

**ARQUITECTURA RECTOR**: Estructura mínima que maximiza simplicidad, preserva autoridad del usuario, y habilita evolución orgánica controlada.