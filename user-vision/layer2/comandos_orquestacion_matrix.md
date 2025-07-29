# Síntesis: Comandos ↔ Orquestación Matrix

## Matrix Core
Los comandos mantienen independencia pero se coordinan inteligentemente según contexto y necesidades.

## Relaciones de Coordinación

### Independencia + Coordinación
**Núcleo base:** `arquitectura_comandos.md`

**Principio fundamental:**
- "los comandos son autocontenidos entre ellos y solo pueden conectarse con otros comandos"
- "Esto quiere decir que no pueden llamar a archivos que esten fuera de su carpeta commands"

**Coordinación emergente:**
- "Algo de lo que no hemos hablado y es muy importante porque es la manera principal en la que se tiene que comportar el agente principal SIEMPRE es la de ser orquestado de subagentes"

### Command Starter: Universal Orchestrator
**Relación especial:**
- "comando para inciiar cualqueir conversacion y que fucnione como comando universal"
- "cuando digo comando universal me refiero al comando que puedo utilizar erecien iniciada la conversacion para que el agente revise el contexto y proponga iniciar una conversacion"

**Función:** Punto de entrada que determina qué comandos activar según contexto

### Workflow Integration: Command Chains
**Núcleo flujos:** `flujos_trabajo.md` → `arquitectura_comandos.md`

**Pattern Chain:**
1. "lo que quiero construir es un sistema de comandos que represente el workflow que quiero"
2. "a mí no me gusta que tú avances sin que tengamos un registro de la planeación"
3. "Ahora, tambien me gustaria que una de las cosas que siempre siempre se haga al momento de crear un documento es pasarlo por el workflow siguiente: creacion, alineamiento y verificacion"

**Implicación:** Comandos se encadenan según workflows establecidos

## Matrix de Interacciones

### /start → Other Commands
- **Función:** Orchestration entry point
- **Conecta con:** Cualquier comando según contexto detectado
- **Criterio:** "las opciones que vienen tendran que estar cambiando constantemente de acuerdo a los comandos que tengamos disponibles"

### /distill → /docs → /git
- **Chain pattern:** Destilación → Documentación → Versionado
- **Trigger:** Nuevas conversaciones raw requieren procesamiento completo

### /challenge → Any Command
- **Relationship:** Validation overlay para cualquier comando
- **Activation:** Post-ejecución para validar alineación con visión

### /partner → Decision Points
- **Function:** Consultation agent para decisiones arquitecturales
- **Trigger:** Cuando hay tensiones vision ↔ simplicidad

## Coordinación Sin Acoplamiento

### Principle: Message Passing
Comandos se comunican a través de artefactos (archivos, estados) no referencias directas

### Principle: State-Based Triggers  
Comandos se activan según estado del sistema, no llamadas explícitas

### Principle: Context Intelligence
"el sistema debería entender el contexto implícito de lo que pides" - Orquestación inteligente automática