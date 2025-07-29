# Architectural Principles

**Trazabilidad**: Derived from layer1_quotes.md [quotes 23,25,27,31,33] and layer2_relationships.md [lines 18-32, 49-50, 68-71]

## Core Design Philosophy

### Simplicity Imperative
"la estructura de carpetas del proyecto se esta volviendo muy compleja y eso no es bueno, es importante entender que nos debemos de mantener simples, pragmaticos, funcionales, lean, ligero" [Layer1:31]

**Beauty Standard**: "Por supuesto que la belleza va a estar en la simplicidad. Exacto. Quiero que el sistema se sienta como una conversación natural, que de esa conversación natural salga el resultado" [Layer1:59]

### Clean Slate Regeneration
"es importante eliminar archivos y crealos desde cero bajo los lineamientos que vamos actualizando, pues si solo vamos construyendo sobre los anteriores existe demasiado sesgo por la informacion que ya esta" [Layer1:45]

## Command Architecture

### Independence Principle
"Algo que veo que estas haciendo y que es uno mas de los principios que dbeemos de respetar es el que los comandos son autocontenidos entre ellos y solo pueden conectarse con otros comandos" [Layer1:25]

**Design Rule**: Each command = self-contained unit with explicit inter-command connections only

### Orchestration Model
"Algo de lo que no hemos hablado y es muy importante porque es la manera principal en la que se tiene que comportar el agente principal SIEMPRE es la de ser orquestado de subagentes" [Layer1:27]

**Implementation**: Main agent orchestrates → Specialized subagents execute → Coordination through command interfaces

## Authority Architecture

### Vision-Implementation Separation
"recuerda que yo no te debo de decir como hacer las cosas, yo debo de darte la vision y los comentarios qye veo pero tu eres quien debe de decidir como hacerlo" [Layer1:23]

**Decision Boundary**: User owns vision/requirements → AI owns implementation decisions → User validates outcomes

### Bias Prevention
"no me gusta la idea de que el hecho de que sea CEO sea algo que se mencione, quizas sea algo que debas de tomar en consideracion, pero no hacerlo presente" [Layer1:41]

## Information Architecture

### Layered Knowledge Structure
"me gustaria que la primer capa se capture en una carpeta que sea layer 1 o algo asi, luego la segunda capa en una layer 2, creo que de esa manera podemos tener mas control" [Layer1:33]

### Hierarchy Model
"para mí, por ejemplo, el archivo de claude.md se vuelve el pináculo de la pirámide y una de nuestras conversaciones en RAW es la base" [Layer1:37]

**Structure**: Raw conversations (base) → Layer distillation → CLAUDE.md (pinnacle)

### Reference-Only Content
"tambien con esta idea de que no debemos de repetir contenido en ningun documento, solo se debe de referenciar" [Layer1:61]

## Technical Constraints

### Token Economy Boundaries
"La economía de tokens no debería estar en la conversación, porque es en la conversación que a través de la mayéutica se puede obtener todo lo que quiere hacer el usuario" [Layer1:19]

### File Size Management
"Tambien deberiamos de empezar a habalr sobre el tamano de los archvios para mantenernos apegados a los lineamientos y la economia de tokens y eficiena de contexto" [Layer1:65]

## System Health Principles

### Over-Engineering Prevention
"necesitamos de alguna manera tambien definir esto como algo que no puede volver a pasar en nuestro sistema y ademas resolverlo" [Layer1:49]

### Aggressive Simplification Rejection
"no estoy seguro de lo que estas proponiendo, creo que es una simplificacion demasiado agresiva" [Layer1:47]

**Balance**: Maintain simplicity without losing essential functionality