# ContextFlow - Prompt Engineering Guide

## Principios Fundamentales

ContextFlow = **prompt engineering efectivo para LLMs**. Todo funciona como instrucciones sofisticadas que Claude Code interpreta vía lenguaje natural.

## Token Economy & Optimization

### Imperativo: Concisión Máxima
Prompts concisos mejoran calidad respuesta + reducen costos. Eliminar palabras innecesarias manteniendo claridad.

```markdown
❌ VERBOSO:
"Could you help by providing detailed analysis of this dataset, covering important aspects while keeping understandable?"

✅ OPTIMIZADO:  
"Analyze dataset: $ARGUMENTS. Output: Key patterns only."
```

### Vocabulario Reforzado
Frases imperativas, estructuradas, orientadas objetivos. Incluir formato deseado, alcance, longitud.

**Comandos ContextFlow:**
- **EXECUTE:** - Instrucción directa acción
- **OUTPUT:** - Formato exacto esperado  
- **SUGGEST:** - Próximos pasos recomendados
- **TRIGGER:** - Condiciones auto-sugerencia

## Estructura Slash Commands

### Template Base Optimizado
```markdown
---
# .claude/commands/[nombre].md
contextflow:
  next: ["cmd1", "cmd2", "cmd3"]
  prev: ["prep-cmd"]  
  triggers: ["completion phrase", "success indicator"]
---

[Descripción concisa]: $ARGUMENTS

EXECUTE:
1. [Acción específica]
2. [Validación]
3. [Output generación]

OUTPUT: [Formato exacto - máximo X palabras/items]
SUGGEST: Use /[next-command] for [specific-reason]
```

### Ejemplos Optimizados

#### Comando Análisis
```markdown
---
contextflow:
  next: ["visualize", "export", "document"]
  triggers: ["analysis complete", "patterns identified"]
---

Analyze codebase: $ARGUMENTS

EXECUTE:
1. Scan target files
2. Identify patterns/issues
3. Generate actionable insights

OUTPUT: 
- Issue count: X
- Priority items: [max 5]
- Recommendations: [max 3]

SUGGEST: Use /visualize charts or /export report
```

#### Comando Refactoring
```markdown
---
contextflow:
  next: ["test", "commit", "document"]
  prev: ["analyze"]
  triggers: ["refactoring complete"]
---

Refactor code: $ARGUMENTS  

EXECUTE:
1. Identify improvements
2. Apply best practices
3. Verify functionality

OUTPUT:
- Changes: [max 50 words]
- Performance impact: [measure]
- Next steps: [max 2]

SUGGEST: Use /test validate changes
```

## Auto-Sugerencia Estrategias

### Triggers Contextuales
Slash commands = cambio tratar AI como socio conversacional → herramienta automatización programable.

```markdown
# Después comando exitoso:
✅ [Command] complete.

NEXT RECOMMENDED:
- /[logical-next] - [specific reason]
- /[alternative] - [different approach needed]  
- /[finalize] - [ready conclude]

Type /[command] or describe intent.
```

### Cadenas Workflow
```markdown
# Secuencias comunes:
explore → analyze → design → implement → test → document

# Auto-sugerencia inteligente:
WORKFLOW DETECTED: Research phase
SUGGEST: Continue /analyze or /design next?

WORKFLOW DETECTED: Implementation complete  
SUGGEST: /test validate or /document handoff?
```

## Integración Metodología Socrática

### Preguntas Token-Eficientes
```markdown
❌ VERBOSO:
"I'd like to understand better what you're trying to accomplish with this feature so I can provide targeted assistance."

✅ OPTIMIZADO:
"Core goal?"
"Primary user or internal tool?"  
"Performance critical?"
```

### Validación Antes Ejecución
```markdown
# Template confirmación
UNDERSTANDING CHECK:
- Goal: [restate intent]
- Approach: [planned method]  
- Output: [expected result]

Correct? Type 'go' proceed or clarify.
```

## Best Practices

### DO:
- Usar verbos imperativos
- Especificar límites exactos (palabras, items, tiempo)
- Incluir triggers específicos auto-sugerencia
- Testear prompts optimización continua

### DON'T:
- Lenguaje indirecto o cortés innecesario
- Asumir contexto sin validación
- Outputs largos sin límites
- Repetir información establecida
- Ignorar señales cambio patterns usuario

## Métricas Efectividad

### Token Efficiency KPIs
- Promedio tokens/sesión: [reducción 20% mes-a-mes]
- Tiempo primera sugerencia útil: [<2 intercambios]
- Precisión auto-sugerencia: [>70% uptake rate]

### Quality Indicators  
- Reduced re-explanations needed
- Faster task completion
- Higher user satisfaction suggestions

## Evolución Sistema

ContextFlow mejora prompt engineering vía:

1. **A/B testing prompts** - Identificar formulaciones efectivas
2. **Pattern recognition** - Detectar estructuras mejores resultados  
3. **User feedback integration** - Adaptar basándose uptake sugerencias
4. **Token optimization** - Refinamiento continuo máxima eficiencia

**Objetivo**: Enseñar Claude Code pensar como usuario específico, menor tokens posible, máxima precisión + utilidad.