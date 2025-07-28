# ContextFlow - Consolidation Strategies

## Filosofía
Densificar información inteligentemente preservando valor semántico. Optimizar token economy + carga cognitiva.

## Capas de Consolidación

### Capa 1: Sesión Activa
**Propósito**: Fidelidad completa conversación actual  
**Contenido**: Intercambios completos, decisiones tentativas, código desarrollo  
**Vida**: Durante sesión activa

### Capa 2: Insights Sesión  
**Propósito**: Extraer patrones + decisiones clave  
**Contenido**: Decisiones arquitectónicas, patrones exitosos, preferencias usuario  
**Vida**: Entre sesiones (días/semanas)

**Template**:
```markdown
## Contexto Sesión
Objetivo inicial → final

## Decisiones Clave  
[Decisión] → [Rationale] → [Implicaciones]

## Patrones Emergentes
[Pattern] → [Contexto aplicable]

## User Profile
Preferencias reveladas + antipatterns
```

### Capa 3: Conocimiento Proyecto
**Propósito**: Modelo mental consolidado proyecto + usuario  
**Contenido**: Arquitectura estable, convenciones, competencias usuario  
**Vida**: Duración proyecto (meses)

**Template**:
```markdown
## Stack Estable
[Tech] → [Uso] → [ADR ref]

## User Competencias
[Área] → [Nivel] → [Evidencia]

## Decisiones Consolidadas  
[ADR] → [Estado] → [Impacto]
```

### Capa 4: Metapatterns
**Propósito**: Conocimiento transferible entre proyectos  
**Contenido**: Patrones conversacionales, estrategias resolución, heurísticas  
**Vida**: Permanente, evolución lenta

## Estrategias Densificación

### Semantic Compression
```markdown
❌ ANTES (verboso):
Usuario: "No estoy seguro si usar Redux..."
[15 intercambios exploratorios]

✅ DESPUÉS (densificado):
USER PATTERN: State management → Context API + useReducer
AVOID: Redux si <5 componentes complejos  
TRIGGER: "state complexity" → suggest Context API
```

### Pattern Abstraction
```markdown
# Casos observados:
API timeout → timeout + retry
DB connection → pooling + health checks
Cache miss → invalidation strategy

# Pattern abstraído:
DEBUG PATTERN: (1) diagnose root (2) fix immediate (3) prevent recurrence
COMMANDS: /debug-analyze → /fix-immediate → /prevent-recurrence
```

### Context Layering
```markdown
QUICK ACCESS (diario):
- Commands frecuentes
- Preferencias críticas  
- Antipatterns comunes

PROJECT CONTEXT (semanal):
- Arquitectura sistema
- Decisiones técnicas
- Workflows establecidos

DEEP CONTEXT (mensual):
- Historial decisiones
- Experimentos fallidos
- Evolución proyecto
```

## Detección Cambios

### Indicators Shift Conceptual
- **Contradicciones**: Usuario sugiere opuesto decisiones previas
- **Nuevas prioridades**: Cambio criterios evaluación  
- **Scope expansion**: Problemas evolucionan significativamente
- **Tool adoption**: Nuevas herramientas cambian posibilidades

### Proceso Remapping
1. **Detectar** inconsistencia modelo actual
2. **Validar** cambio temporal vs fundamental
3. **Explorar** implicaciones  
4. **Actualizar** modelo + propagar
5. **Documentar** evolución

## Métricas Efectividad

**Cuantitativos**:
- Tokens promedio/sesión (objetivo: reducción gradual)
- Tiempo primera sugerencia útil (<2 intercambios)
- Comandos sugeridos vs utilizados (>60%)

**Cualitativos**:
- Relevancia sugerencias
- Sensación comprensión sistema
- Reducción explicaciones repetitivas

## Implementación

### Scripts Consolidación
```bash
/consolidate-session - Final cada sesión
/consolidate-project - Semanal
/consolidate-patterns - Mensual
```

### Triggers Automáticos
- Sesión >50 intercambios → sugerir consolidación
- Context >10KB → reorganización
- 5+ sesiones sin consolidación → alertar pérdida