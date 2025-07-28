# ContextFlow v3

**Sistema prompts conversacional para Claude Code: slash commands auto-organizados + metodología socrática + economía tokens extrema.**

## Visión Core
Transforma Claude Code en agente que evoluciona comprensión usuario mediante diálogo natural sin estructuras predefinidas. Máxima densidad informacional, cero redundancia.

## Arquitectura

### Context Engineering Dinámico
- **Slash commands modulares**: Prompts markdown auto-contenidos con $ARGUMENTS
- **Auto-sugerencia contextual**: Comandos sugieren próximos pasos vía metadata
- **Consolidación progresiva**: Densificación conocimiento sin pérdida nuances
- **Mapeo adaptativo**: Reinterpretación automática sesiones pasadas

### Metodología Socrática + Token Economy
- **Extracción imperativa**: Preguntas precisas revelan intención  
- **Validación concisa**: Confirmación antes ejecución
- **Construcción incremental**: Descubrimiento conversacional guiado
- **Vocabulario reforzado**: Comandos específicos fuerzan acciones LLM

### Workflows Auto-Contenidos
```markdown
# Ejemplo: .claude/commands/analyze.md
Analyze codebase: $ARGUMENTS

EXECUTE:
1. Scan files
2. Identify patterns
3. Generate insights  

OUTPUT: Max 5 findings + 3 recommendations

SUGGEST: Use /visualize or /export next
```

## Casos Uso
- **Desarrollo software**: Construcción apps mediante exploración conversacional
- **Investigación**: Análisis datos con contexto acumulativo  
- **Context management**: Preservación conocimiento entre sesiones

## Diferenciadores
1. **Evolución conceptual**: Mejora comprensión usuario cada interacción
2. **Token economy**: Máxima eficiencia costo-beneficio
3. **No-prescriptivo**: Descubrimiento natural sin imposición frameworks
4. **Portabilidad inteligente**: Patrones adaptativos entre proyectos

## Estado: Diseño arquitectónico - definiendo grafo conceptual + auto-sugerencia