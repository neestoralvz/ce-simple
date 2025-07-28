# ContextFlow - Semantic Context Retrieval Architecture

## Filosofía Core
Context loading basado en **análisis conversacional semántico** > pattern matching keywords. Sistema detecta intención actual + mapea a contexto histórico relevante.

## Detección Intención Semántica

### Triggers Conversacionales
```markdown
PERFORMANCE CONCERN:
- "lento", "se cuelga", "demora mucho"
- "optimizar", "mejorar velocidad"
→ RETRIEVE: Performance decisions, bottlenecks previos, optimization patterns

QUALITY/MAINTAINABILITY:
- "muy grande", "complicado", "difícil mantener"  
- "refactor", "reorganizar", "simplificar"
→ RETRIEVE: Refactoring patterns, code organization decisions, quality improvements

UNCERTAINTY PATTERNS:
- "no estoy seguro si...", "debería usar..."
- "qué opinas de...", "mejor approach..."
→ RETRIEVE: Decision rationales similares, alternatives evaluated, user preferences

FUNCTIONAL ISSUES:
- "no funciona", "bug", "error"
- "comportamiento extraño", "no hace lo esperado"  
→ RETRIEVE: Debugging approaches, similar issues resolved, testing patterns
```

### Análisis Evolutivo Conversación
```markdown
SHIFT DETECTION:
Usuario: "Tengo un bug en login" 
[técnico focus]
Usuario: "Usuarios se confunden con el flow"
[UX focus shift]

RESPONSE PATTERN:
"Veo que pasamos de concern técnico a experiencia usuario. 
¿Recontextualizo hacia UX patterns y usability decisions, 
o mantenemos ambos threads (técnico + UX)?"

WAIT FOR: Confirmación explícita usuario antes cambiar context loading
```

## Context Mapping Semántico

### Dominios Conceptuales
```markdown
AUTHENTICATION/SECURITY:
- login, logout, tokens, permissions, roles
- security decisions, auth patterns, access control
→ CONTEXT: Auth implementations, security reviews, permission models

STATE MANAGEMENT:
- estado, data flow, updates, synchronization
- Redux, Context API, state complexity  
→ CONTEXT: State architecture decisions, data flow patterns, complexity management

PERFORMANCE:
- velocidad, memoria, rendering, carga
- optimization, caching, lazy loading
→ CONTEXT: Performance analysis, optimization strategies, benchmarking results

TESTING/QUALITY:
- tests, coverage, CI/CD, quality gates
- debugging, validation, error handling
→ CONTEXT: Testing strategies, quality decisions, debugging approaches
```

### Relaciones Semánticas
```markdown
CAUSAL RELATIONSHIPS:
"Después de implementar X, Y se volvió lento"
→ RETRIEVE: Implementation X details + performance impact analysis

COMPARATIVE PATTERNS:  
"Como hicimos con Z pero para caso diferente"
→ RETRIEVE: Z implementation + adaptation patterns

EVOLUTIONARY CONCERNS:
"Esto funcionaba antes pero ahora..."
→ RETRIEVE: Timeline of changes + what worked previously
```

## Estrategias Context Loading

### 1. Automático (Invisible)
```markdown
TRIGGERS:
- Términos específicos con contexto histórico claro
- Patterns conversacionales reconocidos sin ambigüedad
- Dominios conceptuales bien establecidos

EJEMPLO:
Usuario: "OAuth setup para este proyecto"
→ AUTO-LOAD: OAuth configurations, auth patterns, security decisions
→ NO MENCIONAR: Context loading automático
```

### 2. Sugerencia Options (Múltiples Contextos)
```markdown
TRIGGERS:
- Términos generales con múltiples contexts posibles
- Primera mención concepto sin establecer scope

EJEMPLO:
Usuario: "Revisar la implementación anterior"
→ RESPONSE: "Veo implementaciones previas:
- OAuth authentication (proyecto-backend)
- Component architecture (proyecto-frontend)  
- Database schema (proyecto-data)
¿Cuál te interesa o examino todas?"
```

### 3. Validación Shifts (Cambios Intención)
```markdown
TRIGGERS:
- Shift detected de focus conversacional
- Ambigüedad sobre context relevance
- Conflicto entre intención actual vs histórico loaded

EJEMPLO:
Usuario shift técnico → UX
→ RESPONSE: "Detecté cambio de technical implementation a user experience.
¿Recontextualizo hacia UX patterns o mantienes technical + UX contexts?"
→ WAIT: Confirmación antes cambiar strategy
```

## Implementation Patterns

### Context Relevance Scoring
```markdown
ANÁLISIS CONVERSACIONAL:
1. Intención actual (weight: 40%)
2. Dominio conceptual (weight: 30%)  
3. Patterns históricos similares (weight: 20%)
4. User preferences established (weight: 10%)

THRESHOLD AUTOMÁTICO: >85% confidence
THRESHOLD SUGERENCIA: 50-85% confidence  
THRESHOLD VALIDACIÓN: <50% confidence o shift detected
```

### Conversation State Tracking
```markdown
CURRENT_INTENT: [detected semantic intention]
LOADED_CONTEXT: [what context currently active]
SHIFT_DETECTED: [boolean - conversation evolution]
CONFIDENCE_LEVEL: [context relevance confidence]
VALIDATION_PENDING: [waiting user confirmation]
```

## Validación Approach

### Response Templates
```markdown
SHIFT VALIDATION:
"Veo que [previous focus] evoluciona hacia [new focus].
¿Recontextualizo o mantengo ambos threads?"

MULTIPLE OPTIONS:
"Varios contexts relevantes:
- [option 1] - [brief relevance]
- [option 2] - [brief relevance]
¿Cuál prefieres o examino todos?"

CONFIDENCE CHECK:
"Para asegurar traigo context más útil:
¿Te refieres a [interpretation] o [alternative]?"
```

### User Confirmation Handling
```markdown
EXPLICIT CONFIRMATION REQUIRED:
- Shifts >70% cambio intención
- Multiple valid contexts (>3 options)
- Low confidence (<50%) en relevance

IMPLICIT CONFIRMATION ACCEPTABLE:
- High confidence (>85%) semantic match
- Single obvious context
- Continuation established conversation thread
```