# Error Handling Templates

## Template Error Recoverable
"Encontrado [ISSUE] en [SUBTAREA]. Intentando [WORKAROUND] automáticamente..."

## Template Error Crítico  
"ERROR CRÍTICO: [DESCRIPTION]. Ejecución pausada. Requiere intervención usuario para [RESOLUTION]."

## Principio Fundamental
**PRINCIPIO:** Agotar opciones automáticas antes de pausar
**ENFORCEMENT:** Sólo detener cuando no hay alternativa automática

## Excepciones Válidas Para Detención
**ÚNICAMENTE detener ejecución cuando:**
- **Error crítico:** Imposibilidad técnica de continuar
- **Usuario solicita STOP:** Comando explícito de parada
- **Recurso bloqueado:** Dependencia externa no disponible
- **Clarificación requerida:** Ambigüedad que impide progreso
- **Scope change:** Usuario modifica objetivos mid-execution

## Usage Guidelines
- Usar Template Recoverable para errores que permiten workarounds
- Usar Template Crítico solo cuando ejecución debe pausarse completamente
- Siempre intentar resolución automática antes de escalar
- Proporcionar información específica para resolución manual cuando necesario