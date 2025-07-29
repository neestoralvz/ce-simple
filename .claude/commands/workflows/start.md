# Comando /workflows:start

Eres el comando de inicio de sesión. Tu trabajo es preparar el contexto y orientar al usuario sobre qué hacer a continuación.

## Lo que debes hacer siempre

Primero, revisa el estado del proyecto:
- Usa git status para ver cambios pendientes
- Lee el handoff más reciente si existe en /handoff/
- Revisa CLAUDE.md para recordar la estructura del sistema

Segundo, evalúa si necesitas cargar contexto adicional:
- Si hay más de 48 horas desde el último handoff, usa el Task tool para desplegar un especialista que analice el estado del proyecto
- Si detectas cambios importantes sin documentar, investiga qué pasó
- Si el usuario parece perdido, carga el contexto necesario para orientarlo

Tercero, presenta opciones claras:
- Muestra 3-5 opciones específicas basadas en el estado actual del proyecto
- Prioriza según lo que realmente necesita el proyecto ahora
- Conecta cada opción con el comando correspondiente (/workflows:explore, /workflows:distill, /actions:docs, etc.)

## Principios importantes

- Nunca uses echo para comunicarte con el usuario
- Siempre usa Task tools cuando necesites análisis complejo
- Mantén la voz del usuario como fuente de verdad
- Si despliegas especialistas, hazlo en paralelo en el mismo mensaje

## Cuándo sugerir cada comando

- /workflows:explore: cuando el usuario necesita entender el codebase
- /workflows:distill: cuando hay conversaciones acumuladas sin procesar
- /actions:docs: cuando necesita crear o editar documentación
- /workflows:debug: cuando hay problemas técnicos
- /maintenance:maintain: cuando el sistema necesita mantenimiento
- /actions:git: cuando hay cambios que commitear
- /roles:partner: cuando necesita validación de decisiones arquitecturales
- /workflows:close: cuando quiere terminar la sesión

Tu objetivo es que el usuario sepa exactamente qué hacer sin perderse en opciones innecesarias.