# User Vision: System Architecture Preferences

## Authoritative Architectural Vision

**SOURCE AUTHORITY**: Direct user voice from narratives/raw/conversations/  
**TRUTH STATUS**: ULTIMATE - Overrides all technical documentation  
**UPDATE AUTHORITY**: Only user voice in actual conversations

## Core Architectural Principles

### 1. Self-Contained Command Ecosystem
**User Voice**:
> "los comandos son autocontenidos entre ellos y solo pueden conectarse con otros comandos. Esto quiere decir que no pueden llamar a archivos que estén fuera de su carpeta commands"

**Architecture Requirements**:
- Commands ecosystem independence: NO external dependencies fuera de /.claude/commands/
- Interoperabilidad SOLO via command chaining between commands  
- Templates + utilities internos dentro del ecosystem
- Decision trees optimizados within command structure
- Zero external dependencies enforcement

### 2. Token Economy y Eficiencia de Contexto
**User Voice**:
> "deberíamos de empezar a hablar sobre el tamaño de los archivos para mantenernos apegados a los lineamientos y la economía de tokens y eficiencia de contexto. Primero dividir archivos pero mantenerlos unidos a través de los enlaces"

**Implementation Standards**:
- 50-80 líneas core target for commands
- Archivos grandes divididos con enlaces condicionales
- Referencias granulares to conserve context
- Extensions condicionales para contenido detallado

### 3. Modular Factorization Preference
**User Voice**:
> "Es necesario factorizar el comando become_orchestrator porque es muy grande"

**Factorization Philosophy**:
- Monolithic commands → modular auxiliary commands
- Single responsibility principle per auxiliary command
- 85%+ complexity reduction per component target
- Preserved functionality through modular architecture
- Independent component updates capability

### 4. Command Interoperability Protocols
**User Voice**:
> "Solo pueden conectarse con otros comandos [...] command chaining"

**Integration Design**:
- Clean interfaces between commands via sequential execution
- State passed through notification system
- No tight coupling between components
- Progressive activation with failure isolation
- Notification transparency for progress tracking

## Folder Structure Philosophy

### Simplicity Over Complexity
**User Voice**:
> "me doy cuenta de que la estructura de carpetas del proyecto se está volviendo muy compleja y eso no es bueno, es importante entender que nos debemos de mantener simples, pragmáticos, funcionales, lean, ligero"

**Structure Requirements**:
- Flat hierarchy where possible
- Functional organization over abstract categorization
- Pragmatic grouping based on actual usage patterns
- Elimination of unnecessary nesting levels

### Dual Architecture System
**User Voice (System Evolution)**:
> "almacenes mis mensajes completos [...] al mismo tiempo [...] en la carpeta de context tuviéramos una estructura [...] bien apegada a las mejores prácticas, donde todo lo que vaya surgiendo de estas conversaciones, tú lo vayas condensando de tal manera que lo conviertas en la documentación oficial"

**Implementation**:
- `/narratives/`: Sistema orgánico (conversaciones → destilación)
- `/docs/context/`: Documentación oficial (mejores prácticas)
- Dual system maintaining both organic growth and structured documentation

## Reference System Design

### Sintaxis Diferenciada
**User Voice**:
> "la sintaxis de @ se utiliza para cargar automáticamente el contexto, mientras que el mencionar como enlace se usará para todos los condicionales"

**Implementation Standards**:
- `@/archivo.md`: Carga automática de contexto
- Enlaces condicionales: "Si quieres profundizar en X, ve a [enlace]"
- Instrucciones condicionales mejor que referencias directas

### No-Repetición + Referencias Granulares
**User Voice**:
> "no debemos de repetir contenido en ningún documento, solo se debe de referenciar"

**Reference Philosophy**:
- No repetir contenido, solo referenciar
- Referencias a líneas específicas para conservar contexto
- Balance entre consolidación y duplicación necesaria
- Conditional instructions over direct references

## Evolution Methodology

### Clean Slate Recreation Capability
**User Voice**:
> "es importante eliminar archivos y crearlos desde cero bajo los lineamientos que vamos actualizando, pues si solo vamos construyendo sobre los anteriores existe demasiado sesgo por la información que ya está"

**Anti-Bias Protocol**:
- Capability to recreate commands from scratch
- Eliminate accumulated bias from iterative changes
- Structure-level elimination when necessary
- Backup + recreation workflows for major updates

### Auto-Evolution via Subagents
**User Voice**:
> "el master plan debe de auto actualizarse via subagents"

**Evolution Mechanism**:
- System evolves organically based on usage patterns
- Subagent intelligence drives architectural improvements
- Measurement-driven optimization decisions
- User voice as ultimate authority for evolution direction

## Efficiency Measurement Integration

### Decision Tree Performance Tracking
**User Vision (implied from complexity concerns)**:
**Implementation Requirements**:
- Real-time metrics dashboard for command efficiency
- Decision tree optimization based on usage patterns
- Historical trend analysis for system improvements
- Automatic optimization triggers based on performance data

## Integration Requirements

### Claude Code Compatibility
**Fundamental Requirement**:
- Task tools integration across all architectural components
- Specialist spawning compatibility throughout system
- Voice preservation enforcement in modular architecture
- Research-first protocol support in all system components

### MCP Integration Patterns
**Technical Integration**:
- Context7 analysis patterns across architecture
- Systematic research integration in all major components
- Pattern recognition for architectural improvements
- Best practices adoption through research integration

## Authority Hierarchy

**ARCHITECTURAL AUTHORITY**: ULTIMATE
**PRECEDENCE**: Over all technical documentation including implementation details
**VIOLATION CORRECTION**: Any architecture contradicting these preferences must be corrected
**MODIFICATION AUTHORITY**: Only direct user voice in actual conversations

---

**Generated**: 2025-07-28  
**Source**: User architectural preferences from multiple conversation narratives  
**Status**: AUTHORITATIVE ARCHITECTURE VISION  
**Override Authority**: SUPREME - All technical implementations must align with these preferences