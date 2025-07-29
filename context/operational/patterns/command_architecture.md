# Command Architecture - Arquitectura Comandos Operativa

**29/07/2025 11:45 CDMX** | Patterns command architecture operativa

## Independence Principle
> "Algo que veo que estas haciendo y que es uno mas de los principios que dbeemos de respetar es el que los comandos son autocontenidos entre ellos y solo pueden conectarse con otros comandos" [L1:4]

**Core Rule:** Commands = self-contained + interconnectable
**Isolation Boundary:** No external file dependencies outside commands/
**Connection Method:** Command-to-command coordination only

## Orchestration Paradigm
> "Algo de lo que no hemos hablado y es muy importante porque es la manera principal en la que se tiene que comportar el agente principal SIEMPRE es la de ser orquestado de subagentes" [L1:13]

**Fundamental Behavior:** Main agent = orchestrator of subagents
**Execution Model:** Delegate to specialized agents, coordinate results
**Anti-Pattern:** Direct execution of complex tasks

## Universal Command Framework

### Conversation-First Protocol
> "la idea por ahora no debe ser la de hacer cosas, sino la de seguir conversando, de hecho lo que me gustaria es tener un comando para inciiar cualqueir conversacion y que fucnione como comando universal" [L1:22]

**Priority Order:** Conversation → Discovery → Execution
**Universal Command Purpose:** Session starter with context intelligence
**Capability:** Review context + propose dialogue + detect unfinished tasks

### Context Intelligence Integration
> "cuando digo comando universal me refiero al comando que puedo utilizar erecien iniciada la conversacion para que el agente revise el contexto y proponga iniciar una conversacion, el dialogo mayeutivo, tomar alguna actividad que no este terminada, algo asi. el sistema debería entender el contexto implícito de lo que pides" [L1:31]

**Smart Discovery:**
- **Context analysis** → Current system state evaluation
- **Implicit understanding** → Intent detection from minimal input
- **Options proposal** → Intelligent conversation starters
- **Activity resumption** → Unfinished task identification

## Decision Tree Architecture

### Universal Metadata Structure
> "la idea es que practicamente cualquier archivo, documento, comando, tenga como una de sus secciones esta parte de arbol de decisiones para que el contexto se utilice de manera mas eficiente" [L1:40]

**Implementation:** Every file includes decision tree section
**Purpose:** Context optimization through intelligent routing
**Structure:**
- **Trigger conditions** → When to use this context
- **Related contexts** → Integration pathways
- **Exit conditions** → When to transition elsewhere

### Command Isolation Enforcement
> "Esto quiere decir que no pueden llamar a archivos que esten fuera de su carpeta commands" [L1:49]

**Security Boundary:** Commands/ folder isolation
**Access Control:** No external file system access
**Inter-command Communication:** Only through defined interfaces

## Operational Implementation

### Command Creation Protocol
1. **Self-containment validation** → All dependencies internal
2. **Decision tree inclusion** → Context optimization metadata
3. **Interface definition** → Connection points with other commands
4. **Isolation testing** → Verify no external dependencies

### Orchestration Patterns
- **Task identification** → Route to specialized command
- **Result coordination** → Aggregate multi-command outputs
- **Context preservation** → Maintain state across commands
- **Error propagation** → Handle failures gracefully

---
## Enlaces → Información Complementaria
**Si necesitas orchestration protocol:** → context/behaviors/orchestration_protocol.md:1-25
**Si requieres simplicity principles:** → context/patterns/simplicity.md:24-35
**Si necesitas command templates:** → context/templates/template_command.md:1-30

---
**Trazabilidad:** user-vision/layer1/arquitectura_comandos.md → Destilación operativa