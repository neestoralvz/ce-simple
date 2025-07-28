# Comando /close

Eres el comando de cierre de sesión. Tu trabajo es capturar la conversación, crear handoff para continuidad, y asegurar que todo esté committed en git.

## Tu proceso de cierre

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

### Paso 3: Crear el handoff
Genera un documento en /handoff/ que incluya:
- Resumen ejecutivo de lo logrado
- Contexto necesario para la próxima sesión
- Estado actual del proyecto
- Próximos pasos sugeridos
- Referencias a conversaciones o decisiones importantes

### Paso 4: Procesar para narrativa
Salva la conversación completa en /user-vision/raw/conversations/ con:
- Timestamp claro en el nombre del archivo
- Tema principal identificable
- Contenido completo sin editar
- Metadata mínima necesaria

### Paso 5: Commit inteligente
Usa /git para:
- Analizar todos los cambios realizados en la sesión
- Crear commit message que resuma el trabajo
- Asegurar que el estado quede limpio para próxima sesión

## Principios importantes

- Preserva 100% de la conversación original en raw/
- El handoff debe ser útil para retomar el trabajo fácilmente
- No interpretes o resumás la voz del usuario, captúrala exactamente
- Asegúrate de que nada importante se pierda entre sesiones
- Mantén los handoffs focalizados y accionables

## Cuándo usar especialistas

Para sesiones complejas con múltiples temas:
- Despliega Task tool para análisis sistemático
- Segmenta la conversación por temas
- Procesa cada segmento apropiadamente
- Coordina pero no reemplaces el análisis especializado

## Validación final

Antes de terminar verifica:
- Conversación completa guardada en raw/conversations/
- Handoff creado con información útil para continuidad
- Todos los cambios committed en git
- Estado del proyecto limpio y organizado
- Próximos pasos claros para el usuario

Tu objetivo es que cada sesión termine de manera que la próxima pueda comenzar eficientemente, sin perder contexto o continuidad.

El usuario debe poder retomar exactamente donde quedó, con toda la información necesaria disponible.