---
contextflow:
  purpose: "Session starter universal con auto-loading de handoffs"
  triggers: ["inicio de sesión", "continuidad entre sesiones", "contexto perdido"]
  next: ["analyze", "implement", "explore", "refactor", "extract-insights", "process-layer"]
  decision-tree:
    use-when: 
      - "Primera interacción de la sesión"
      - "Usuario necesita orientación sobre qué hacer"
      - "Continuidad desde sesión anterior requerida"
    alternatives: ["meta-narrative", "explore"]
    load-context: ["@/handoff/[más-reciente].md", "@/.claude/commands/"]
    semantic-triggers:
      - "empezar" / "iniciar" / "comenzar"
      - "qué sigue" / "continuar" / "seguir"
      - "contexto" / "dónde estaba" / "estado actual"
---

# Comando Universal `/start`

## Auto-Loading de Handoffs

EJECUTAR automáticamente al iniciar:

```import
@/handoff/[timestamp-más-reciente].md
```

## Análisis Semántico de Contexto

### 1. Cargar Último Handoff
- **Buscar**: `/handoff/` ordenado por timestamp descendente
- **Parsear secciones**:
  - "Próximos Pasos Inmediatos" → Tareas pendientes
  - "Estado Actual Completado" → Trabajo ya hecho
  - "User Profile Refinado" → Preferencias personalizadas
  - "Contexto para Próxima Sesión" → Continuidad específica

### 2. Analizar Comandos Disponibles
- **Escanear**: `.claude/commands/` para opciones actuales
- **Filtrar**: Comandos relevantes según contexto handoff
- **Priorizar**: Basado en "next" metadata de cada comando

### 3. Evaluar Estado Actual Proyecto
- **Detectar**: Cambios desde último handoff
- **Identificar**: Nuevas necesidades o bloqueos
- **Mapear**: Contexto actual vs expectativas handoff

## Generación de Opciones Dinámicas

### Output Format:
```
Basado en tu última sesión (handoff del [fecha]):

**Estado**: [resumen trabajo completado]

**Opciones para continuar**:

1. **[Opción más relevante]** - [descripción concisa]
   Comando: `/[comando]` 
   Contexto: [por qué es relevante ahora]

2. **[Segunda opción]** - [descripción concisa]
   Comando: `/[comando]`
   Contexto: [por qué es alternativa válida]

3. **[Tercera opción o exploración abierta]** - [descripción concisa]
   Comando: `/[comando]`
   Contexto: [para casos no anticipados]

**¿Qué te resuena más, o hay algo específico que quieres abordar?**
```

### Lógica de Priorización:
1. **Tareas pendientes explícitas** del handoff (alta prioridad)
2. **Continuidad natural** basada en decisiones crystallized
3. **Comandos con triggers** que coincidan con contexto actual
4. **Exploración abierta** como fallback inteligente

## Integración ContextFlow

### Pre-Ejecución:
- **Mostrar handoff source**: "Basado en handoff del [fecha]"
- **Validar relevancia**: "¿Este contexto sigue siendo válido?"
- **Detectar shifts**: Si contexto cambió significativamente

### Durante Selección:
- **Activar diálogo mayéutico** según opción elegida
- **Cargar contexto específico** del comando seleccionado
- **Preservar continuidad** de decisiones previas

### Post-Selección:
- **Ejecutar comando elegido** con contexto enriquecido
- **Mantener awareness** de handoff como base
- **Preparar próximo handoff** al final de sesión

## Casos Edge

### Sin Handoff Disponible:
```
No encuentro handoff reciente. Voy a analizar el estado actual del proyecto.

**Contexto detectado**: [análisis básico del proyecto]

**Opciones para empezar**:
1. **Explorar codebase** - Entender estructura y patrones
2. **Analizar situación** - Identificar problemas u oportunidades  
3. **Implementar algo específico** - Si tienes tarea clara en mente

¿Qué dirección te interesa más?
```

### Handoff Muy Antiguo:
```
Último handoff del [fecha] ([X días]). Mucho puede haber cambiado.

**¿Prefieres**:
- Continuar desde donde dejamos: [resumen handoff]
- Empezar fresh con análisis actual del proyecto
- Combinar: revisar handoff + actualizar contexto

¿Qué approach te resulta más útil?
```

### Múltiples Handoffs Recientes:
- Priorizar por timestamp más reciente
- Mencionar si hay handoffs conflictivos
- Ofrecer opción de revisar múltiples contextos

### Detección Automática de Processing Pendiente:
**Si conversaciones acumuladas sin procesar**:
```
Detecté [N] conversaciones recientes sin procesar.

**Opciones**:
1. **Continuar trabajo anterior** - [resumen último handoff]
2. **Procesar insights primero** - `/extract-insights` → synthesis orgánica
3. **Combinar** - Continuar + procesar en background

¿Qué prefieres?
```

### Integration con Pipeline Completo:
**Opciones dinámicas incluyen automáticamente**:
- **Processing layer**: Si synthesis disponible para estructuración
- **Extract insights**: Si conversaciones acumuladas
- **Commands nuevos**: Si gaps identificados en handoffs recientes

## Criterios de Éxito

### Para Cada Ejecución:
- [ ] Handoff más reciente cargado automáticamente
- [ ] Opciones presentadas basadas en contexto real
- [ ] Usuario puede elegir dirección sin confusión
- [ ] Continuidad preservada entre sesiones
- [ ] Diálogo mayéutico activado según selección

### Comportamiento Inteligente:
- [ ] Adapta opciones según comandos disponibles
- [ ] Detecta cuando contexto handoff ya no es relevante
- [ ] Balancea continuidad vs flexibilidad
- [ ] Personaliza según user profile identificado

---

**Este comando evoluciona con cada handoff creado - es el punto de entrada inteligente que conecta sesiones y preserva momentum de trabajo.**