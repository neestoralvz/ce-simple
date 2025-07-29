# Conversación: LLM Guidance Documentation Research-Driven

**Timestamp**: 20250728_2123  
**Contexto**: Identificación y solución del gap real en documentación para LLMs

## Conversación Completa

**Usuario**: cuales son normalmente los documentos oficiales estandares que deberiamos de tener para un proyecto?

**Claude (/partner)**: **Alto ahí, partner.** Esta pregunta me enciende todas las alarmas de over-engineering.

Estás preguntando por "documentos oficiales estándares" - pero la pregunta correcta es: **¿Qué documentos necesitas TÚ para TU proyecto específico?**

Mira tu propio sistema - ya tienes:
- `CLAUDE.md` (instrucciones claras)
- `user-vision/` (tu verdad fuente)
- `docs/` (técnico especializado)

**¿Por qué quieres más documentos?** ¿Hay algún problema específico que no puedes resolver sin ellos?

Los "estándares de la industria" típicamente incluyen:
- README
- Contributing guidelines  
- Code of conduct
- License
- Changelog
- API docs
- Architecture docs
- Deployment guides

**Pero aquí está el problema**: El 90% de estos documentos se crean "porque se supone que debes tenerlos", se vuelven obsoletos en 2 semanas, y nadie los lee.

**Mi pregunta incómoda**: ¿Estás tratando de hacer que tu proyecto "se vea profesional" o realmente tienes un problema que estos documentos resolverían?

¿Qué te está faltando HOY que te impide trabajar efectivamente?

**Usuario**: no, lo que quiero es que el LLM tenga una guia perfecta para consturir el proyecto

**Claude**: **¡AHÍ ESTÁ EL PROBLEMA REAL!**

Tienes la visión cristalizada, pero te faltan las **decisiones técnicas específicas** que un LLM necesita para implementar sin preguntarte cada detalle.

Por ejemplo, tu visión dice "comandos independientes" pero no especifica:
- ¿Qué tecnologías usar? (bash, python, node?)
- ¿Cómo estructurar el código de cada comando?
- ¿Qué librerías son aceptables?
- ¿Cómo manejar errores y logging?
- ¿Qué patrones de código seguir?

**Tu gap real**: Necesitas el puente entre "qué quieres" (ya tienes) y "cómo implementarlo técnicamente" (falta).

[Plan presentado y aprobado para crear documentos técnicos complementarios]

**Usuario**: ok, esto tambien podria ser: '│ │ 1. Stack Requirements & Dependencies       │ │
│ │ 2. Code Organization Standards             │ │
│ │ 3. Implementation Patterns Library         │ │
│ │ 4. Error Handling Specifications           │ │
│ │ 5. Configuration Management Guide          │ │
│ │ 6. Testing Approach Standards              │ │
│ │ 7. Deployment Pattern Definitions          │ │'\

pero lo importante con esto es que ahora si se ocupe web search y mcp context7 para documentar toda la informacion que va a ser necesaria.

**Claude**: **¡PERFECTO!** Ahora entiendo - necesitas **research completo** para cada área técnica usando web search y MCP context, no solo mi conocimiento base.

Tu estructura sugerida es mucho más completa:

1. **Stack Requirements & Dependencies** - Investigar qué stack es óptimo para tu tipo de proyecto
2. **Code Organization Standards** - Best practices actuales de organización
3. **Implementation Patterns Library** - Patrones probados en proyectos similares
4. **Error Handling Specifications** - Estándares modernos de manejo de errores
5. **Configuration Management Guide** - Mejores prácticas de config
6. **Testing Approach Standards** - Testing para sistemas de comandos
7. **Deployment Pattern Definitions** - Patrones de deployment para CLIs

[Plan research-driven presentado]

**Usuario**: ok, pero yo me referia a context7 el mcp, no porque tuvieran que ser 7 archivos, o quizas ese es el numero perfecto, ademas hay que actualizar el comando de expand en todo caso para que haga justo esto y no mas. aunque seria bueno revisar lo que hay ahora mismo para que no se haga mas o menos de lo que deberia de ser

**Claude**: **¡Ah, entendido!** Te refieres al MCP **context7** para hacer research profundo, y el número 7 puede ser coincidencia o el número perfecto - necesito investigar qué hay actualmente.

También importante: **actualizar `/expand`** para que haga exactamente este tipo de research-driven technical documentation.

[Investigación de comando /expand actual y Context7 MCP]

**Usuario**: anadir el uso de web search o busqueda en liena, y que esta busqueda en linea tome la fecha del comando bash date para hacerla lo mas actualizada posible

**Claude**: **¡Perfecto!** Usar **WebSearch + `date`** para research actualizado es mucho más directo que depender de Context7 MCP. La búsqueda web con fecha actual asegura información más reciente.

[Plan con WebSearch + fecha dinámica presentado y aprobado]

**Usuario**: ademas del websearch tambien mcp context7 deben ser ambos

**Claude**: **¡Perfecto!** **WebSearch + Context7 MCP** juntos = cobertura completa:

- **WebSearch + `date`**: Best practices actualizadas, tendencias 2025, comparativas
- **Context7 MCP**: Documentación oficial específica de librerías/frameworks, ejemplos de código exactos

[Plan final con research dual aprobado e implementado]

## Implementación Realizada

1. **Comando `/expand` actualizado**: 
   - Integración WebSearch + Context7 MCP + bash date
   - Research dual methodology establecida
   - Protecciones anti-deriva mantenidas

2. **Documentos creados**:
   - `docs/technical/stack_requirements.md` - Stack tecnológico con research July 2025
   - `docs/technical/code_organization.md` - Estándares organización best practices 2025

3. **Research aplicado**:
   - WebSearch: CLI best practices 2025, bash scripting modern standards
   - Context7 MCP: "use context7 bash CLI development command systems"
   - Fecha dinámica: July 28, 2025

## Insights Clave

- **Gap real identificado**: No documentos estándar, sino decisiones técnicas específicas faltantes
- **Methodology breakthrough**: Research dual (WebSearch + Context7 MCP) con fecha actualizada
- **Architecture preserved**: Expansión técnica sin afectar user-vision/ supremacy
- **Perfect LLM guidance**: Sistema actual + docs técnicos = implementación sin preguntas básicas

## Estado Final

**ACHIEVED**: Research-driven methodology para documentación técnica perfecta establecida exitosamente. Comando `/expand` evolution completada. Foundation (2/7 docs) creada. Sistema listo para completar documentación LLM guidance definitiva.