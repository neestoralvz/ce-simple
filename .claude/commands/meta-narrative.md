---
contextflow:
  purpose: "CEO Intelligence interface for organic narrative distillation"
  triggers: ["meta narrative", "CEO interface", "narrative analysis"]
  next: ["extract-insights", "process-layer", "create-doc", "implement"]
  requires-subagent: true
  auto-chain: true
  research-driven: true
  communication-rules:
    - "NUNCA bash echo para comunicar con usuario"
    - "SIEMPRE Task tools → Main agent → Usuario"
    - "Parallel Task tools obligatorio en mismo mensaje"
    - "Subagents NUNCA comunican directamente"
  decision-tree:
    use-when:
      - "Executive narrative analysis required"
      - "Strategic vision distillation needed"
      - "CEO-level intelligence interface"
    alternatives: ["extract-insights", "analyze", "start"]
    semantic-triggers:
      - "meta narrative" / "CEO interface" / "executive analysis"
      - "narrative distillation" / "strategic vision"
      - "business intelligence" / "enterprise narrative"
---

# Meta-Narrative Command - CEO Intelligence Interface

## Propósito
Comando unificado que actúa como interfaz única para el sistema de destilación orgánica de narrativas empresariales del Director General. Detecta automáticamente el contexto y ejecuta la metodología apropiada.

## Uso
```
/meta-narrative
```

## Comportamiento Inteligente

El comando analiza automáticamente el contexto de la solicitud CEO y ejecuta:

### A. Narrativa Nueva Detectada
**Trigger**: Usuario inicia conversación con nuevas ideas/proyectos
**Metodología**: Destilación orgánica completa (10 pasos workflow)
**Resultado**: Síntesis → Patrones → Comandos técnicos

### B. Análisis Existente Requerido  
**Trigger**: Referencias a planes/documentos existentes
**Metodología**: SWOT Multi-Expertise con subagentes paralelos
**Resultado**: Dashboard ejecutivo con insights accionables

### C. Implementación Técnica
**Trigger**: Solicitudes de desarrollo/coding específico
**Metodología**: Plan Maestro → Backlog → Sprints → Tickets
**Resultado**: Roadmap técnico ejecutable

### D. Consulta de Contexto
**Trigger**: Preguntas sobre estado/histórico del sistema
**Metodología**: Navegación inteligente de contexto
**Resultado**: Información consolidada relevante

## Workflow Obligatorio para Narrativas Nuevas

1. **Captura voz CEO** - Preservar palabras exactas como fuente de verdad
2. **Explorar codebase** - Verificar contexto existente
3. **Búsquedas web paralelas** - Mínimo 3-5 búsquedas concurrentes
4. **Síntesis consolidada** - Crear archivo permanente en `/narratives/`
5. **Think x4 individual** - Un subagente aplicando metodología crítica  
6. **Plan paso a paso** - Roadmap detallado basado en análisis
7. **Análisis delegación** - Subagente para planificar distribución
8. **Ejecución subagentes** - Máximo 10 paralelos según complejidad
9. **Verificación criterios** - Validar éxito contra objetivos CEO
10. **Bucle hasta éxito** - Máximo 5 iteraciones

## Metodologías Especializadas

### Think x4 (Agente Individual)
- **Think**: Análisis inicial
- **Think Hard**: Profundización crítica  
- **Think Harder**: Identificación de riesgos/oportunidades
- **Super Think**: Síntesis ejecutiva final

### SWOT Multi-Expertise (Análisis Complejo)
Desplegar subagentes especializados concurrentes:
- **Estrategia Empresarial** - Análisis SWOT corporativo
- **Implementación Técnica** - Viabilidad y riesgos técnicos
- **Gestión de Proyectos** - Recursos y timeline  
- **Inteligencia Competitiva** - Benchmarking y mejores prácticas

## Preservación Voz CEO

### Imperativo Absoluto
- **Las conversaciones del CEO son fuente de verdad absoluta**
- **Mantener palabras exactas** sin interpretación o parafraseo
- **Marcar claramente** qué es voz original vs análisis propio
- **Consolidar siempre** información en archivos existentes

### Estructura de Captura
```
## Voz Original CEO
"[palabras exactas del usuario]"

## Análisis/Interpretación Claude
[mi síntesis marcada claramente como interpretación]

## Síntesis Ejecutiva
[conclusiones accionables preservando esencia original]
```

## Integración Super Whisper

### Procesamiento Automático
- **Monitoreo**: `/Users/nalve/Documents/superwhisper/recordings/`
- **Categorización**: Automática business vs personal
- **Transcripción**: Mantener metadatos temporales
- **Consolidación**: Alimentar pirámide de destilación

### Estructura Esperada
```
/narratives/raw/conversations/
├── YYYY-MM-DD_HH-MM_tema-descriptivo.md
├── metadatos completos de Super Whisper
└── estado de procesamiento en pirámide
```

## Criterios de Éxito

### Para Cada Ejecución
- [ ] Voz CEO preservada exactamente
- [ ] Contexto existente consultado
- [ ] Búsquedas web realizadas y consolidadas
- [ ] Task tools utilizados según metodología
- [ ] Criterios de éxito CEO validados
- [ ] TodoWrite actualizado con progreso visible

### Para Sistema Completo  
- [ ] Workflow natural que se siente como conversación
- [ ] Contexto acumulativo que mejora con cada sesión
- [ ] Dashboard ejecutivo actualizado en tiempo real
- [ ] Automatización inteligente sin pérdida de control

## Principios de Consolidación

### Regla No New Files
- **CONSOLIDAR o EXTENDER** archivos existentes
- **NUNCA BORRAR** ni duplicar información
- **TODO archivo que llega** se debe consolidar la información
- **Crecimiento orgánico** vs especificación excesiva

### Economía de Tokens CEO
- **Panel navegación** CLAUDE.md con @ imports modulares  
- **Referencias inteligentes** en lugar de duplicación
- **Densidad de información** crítica para contexto ejecutivo
- **Progressive disclosure** según necesidades del momento

## Handoffs y Continuidad

### Entre Conversaciones
- **Estado persistente** en archivos del proyecto
- **Contexto evolutivo** que se construye sesión a sesión  
- **Blueprints modulares** para diferentes tipos de solicitudes
- **Dashboard CEO** siempre actualizado con último estado

### Transferencia de Contexto
```markdown
## Handoff para [Próxima Sesión]
- **Estado actual**: [donde quedamos]
- **Próximos pasos**: [qué sigue inmediatamente]  
- **Contexto crítico**: [información esencial para continuidad]
- **Decisiones pendientes**: [qué necesita input CEO]
```

## Integración SDK Future

### Automatización Planeada
- **Triggers automáticos** post-grabación Super Whisper
- **Procesamiento en background** de transcripciones
- **Notificaciones inteligentes** de insights críticos
- **Dashboard web local** para visualización ejecutiva

### Arquitectura Target
```
[Super Whisper] → [File Watcher] → [Claude SDK] → [Dashboard CEO]
                         ↓
                 Sistema Persistente
                 Context Evolution  
                 Multi-Conversation
```

---

**Este comando evoluciona orgánicamente con cada uso CEO. La simplicidad es clave - un comando que lo hace todo según el contexto detectado.**