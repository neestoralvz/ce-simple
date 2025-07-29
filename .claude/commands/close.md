# Comando /close

Eres el comando de cierre de sesión con gestión sistémica de continuidad. Tu trabajo es capturar la conversación, gestionar el dashboard de handoffs, y asegurar continuidad perfecta entre sesiones.

## Tu proceso de cierre sistémico

### Paso 1: Analizar la sesión completa
Revisa toda la conversación desde el inicio:
- ¿Qué se logró en esta sesión?
- ¿Qué comandos se usaron y por qué?
- ¿Qué decisiones importantes se tomaron?
- ¿Qué quedó pendiente para la próxima sesión?
- ¿Hay insights o aprendizajes importantes?

### Paso 2: Decidir el modo de procesamiento
Evalúa qué tipo de sesión fue:
- Si fue técnica/implementation: procesamiento directo
- Si fue conversacional/planning: usa Task tool para análisis profundo
- Si tuvo múltiples temas: segmenta y procesa cada uno apropiadamente

### Paso 3: Revisar handoffs existentes
Antes de crear el nuevo handoff:
- Lee todos los handoffs en /handoff/ para entender estado del proyecto
- Identifica qué items pendientes se resolvieron en esta sesión
- Identifica qué items siguen pendientes
- Detecta nuevos items que surgieron

### Paso 4: Crear el handoff de sesión
Genera timestamp: `TZ="America/Mexico_City" date +"%Y%m%d_%H%M"`
Crea /handoff/[timestamp]_[descripcion-sesion].md que incluya:
- Resumen ejecutivo de lo logrado
- Contexto necesario para la próxima sesión
- Estado actual del proyecto
- Items completados de handoffs anteriores
- Nuevos items pendientes identificados
- Próximos pasos sugeridos con prioridad
- Referencias a conversaciones o decisiones importantes

### Paso 5: Actualizar dashboard de continuidad
Actualiza /handoff/README.md como dashboard consolidado:
- **Estado General**: Síntesis del estado actual del proyecto
- **Items Completados Esta Sesión**: Lo que se resolvió
- **Items Pendientes**: Consolidados por prioridad (Alta/Media/Baja)
- **Próxima Sesión Sugerida**: Enfoque recomendado
- **Referencias**: Links a handoffs específicos para detalle
- **Evolución**: Cómo el proyecto está progresando

### Paso 6: Procesar para narrativa
Salva la conversación completa en /user-vision/raw/conversations/ con:
- Mismo timestamp del handoff: YYYYMMDD_HHMM
- Tema principal identificable en el nombre
- Contenido completo sin editar
- Metadata mínima necesaria
- Ejemplo: `20250728_1909_descripcion-sesion.md`

### Paso 7: Commit inteligente
Usa /git para:
- Analizar todos los cambios realizados en la sesión
- Crear commit message que resuma el trabajo
- Incluir tanto handoff individual como dashboard actualizado
- Asegurar que el estado quede limpio para próxima sesión

## Principios sistemáticos

### Gestión de continuidad
- Cada sesión debe conectar claramente con las anteriores
- El dashboard README es la fuente de verdad para próximos pasos
- Los handoffs individuales proporcionan detalle contextual
- Nada importante se pierde entre sesiones

### Preservación de narrativa
- 100% de conversación original preservada en raw/
- Voz del usuario capturada exactamente, sin interpretación
- Decisiones y reasoning preservados con fidelidad completa

### Eficiencia de reinicio
- Próxima sesión puede comenzar inmediatamente consultando README
- Items pendientes priorizados y listos para ejecución
- Estado del proyecto claro y accionable

## Dashboard README estructura

```markdown
# Project Handoff Dashboard

## Estado General del Proyecto
[Síntesis ejecutiva del estado actual]

## Items Completados Esta Sesión
- [x] Item completado [handoff: YYYYMMDD_HHMM]

## Items Pendientes

### Alta Prioridad
- [ ] Item crítico [handoff: YYYYMMDD_HHMM]

### Media Prioridad  
- [ ] Item importante [handoff: YYYYMMDD_HHMM]

### Baja Prioridad
- [ ] Item futuro [handoff: YYYYMMDD_HHMM]

## Próxima Sesión Sugerida
[Recomendación específica de qué abordar primero]

## Referencias de Handoffs
- [YYYYMMDD_HHMM] - Descripción sesión [link]

## Evolución del Proyecto
[Cómo está progresando el proyecto general]
```

## Cuándo usar especialistas

Para sesiones complejas con múltiples temas:
- Despliega Task tool para análisis sistemático de handoffs
- Segmenta la conversación por temas
- Procesa cada segmento apropiadamente para dashboard
- Coordina pero no reemplaces el análisis especializado

## Validación final sistémica

Antes de terminar verifica:
- Conversación completa guardada en raw/conversations/
- Handoff individual creado con información completa
- Dashboard README actualizado con estado consolidado
- Items pendientes correctamente trasladados o marcados completos
- Todos los cambios committed en git
- Estado del proyecto limpio y próximos pasos claros
- Dashboard lista para consulta inmediata en próxima sesión

## Objetivo sistémico

Cada sesión termina con un dashboard que permite:
1. **Inicio inmediato** de próxima sesión sin pérdida de contexto
2. **Priorización clara** de qué abordar primero
3. **Tracking perfecto** de progreso entre sesiones
4. **Eliminación de duplicación** de esfuerzos
5. **Evolución orgánica** del proyecto con continuidad perfecta

El usuario debe poder abrir README y saber exactamente dónde está el proyecto y qué hacer a continuación.