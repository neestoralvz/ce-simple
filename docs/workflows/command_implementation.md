# Implementación Técnica de Comandos

## Derivación de Principios Establecidos
Basado en TRUTH_SOURCE.md: "Los comandos son solo la ejecución después del descubrimiento conversacional" [L1:17] y "los comandos son autocontenidos entre ellos y solo pueden conectarse con otros comandos" [L1:25].

## Patrones de Implementación por Comando

### /start - Activación Técnica
**Responsabilidad Técnica Específica**: Carga contextual y orientación inicial
**Implementación**:
- Auto-importar TRUTH_SOURCE.md (siempre)
- Importar user-vision/layer3/ si contexto requiere
- Activar modo conversación libre sin restricciones token
- Establecer estado de sesión para coordinación posterior

**Anti-Patrón Prevención**: NO hacer trabajo de otros comandos, solo orientar

### /distill - Engine de Destilación
**Responsabilidad Técnica Específica**: Procesamiento raw → visión consolidada
**Implementación de 5 Capas**:
1. **Raw Processing**: Extracción de conversaciones user-vision/raw/
2. **Layer 1**: Quote extraction 100% fidelidad
3. **Layer 2**: Relationship mapping entre insights
4. **Layer 3**: Documentation synthesis técnica
5. **CLAUDE.md Update**: Regeneración automática bajo validation.md

**Anti-Patrón Prevención**: NO interpretar usuario, solo destilar voice preservation

### /expand - Motor Técnico Complementario
**Responsabilidad Técnica Específica**: Expansión técnica implementacional SOLO
**Implementación**:
- Análisis gaps en docs/ para complementariedad
- Generación contenido técnico basado en principios establecidos
- PROHIBIDO: Tocar user-vision/ o crear nueva filosofía
- Validación obligatoria: Cada expansión justificada con TRUTH_SOURCE.md

**Anti-Patrón Prevención**: NO expandir visión, solo implementación técnica

### /partner - Challenger Automático
**Responsabilidad Técnica Específica**: Validación decisiones + simplicidad enforcement
**Implementación**:
- Challenge obligatorio para cambios sistémicos
- Validación responsabilidad única por comando
- Balance checker: esencial vs over-engineering
- Enforcement de separación de responsabilidades

**Anti-Patrón Prevención**: NO decidir por usuario, solo validar simplicidad

### /git - Integración Versionado
**Responsabilidad Técnica Específica**: Manejo inteligente git workflow
**Implementación**:
- Commits contextuales basados en comando coordinado
- Branch management para multi-conversación
- Integration con todos comandos para commits automáticos
- Mensajes commit que reflejan visión preservada

**Anti-Patrón Prevención**: NO manejar contenido, solo versionado

## Coordinación Técnica Entre Comandos

### Patrón Orquestación Master-Subagent
Basado en TRUTH_SOURCE.md: "la manera principal en la que se tiene que comportar el agente principal SIEMPRE es la de ser orquestado de subagentes" [L1:27].

**Implementación de Orquestación**:
- Agente principal = dispatcher inteligente
- Cada comando = subagente especializado
- Coordinación explícita sin dependencias complejas
- State sharing mínimo necesario

### Flujo de Coordinación Técnica
```
Session Start → /start (context loading)
             → comando específico (task execution)
             → /partner (validation si sistémico)
             → /git (versioning si cambios)
             → /close (session wrap + capture)
```

### Integration Patterns Anti-Complexity
- **No Circular Dependencies**: Comandos referencian, no dependen
- **Minimal State Sharing**: Solo data esencial entre comandos
- **Async Coordination**: Comandos coordinan sin blocking
- **Failure Isolation**: Error en comando no afecta otros

## Enforcement de Responsabilidad Única

### Validation Técnica Pre-Ejecución
**Criterios Automáticos**:
- Comando mantiene scope original definido
- No invasión de responsabilidades de otros comandos
- Límites claros de qué hace vs qué NO hace
- Composabilidad sin conflicto

### Challenger Integration
**Proceso Técnico**:
1. Detección change request sistémico
2. Auto-activación /partner challenger
3. Validación scope + simplicidad + necesidad real
4. Aprobación/rechazo con justificación
5. Implementation si aprobado

### Anti-Patrón Detection System
**Patrones Técnicos Prohibidos**:
- "Solo una funcionalidad más" → Auto-rechazo
- Funciones mezcladas → Separación forzada
- Scope creep acumulativo → Reset a responsabilidad original
- Interdependencias complejas → Refactoring independencia

## State Management Minimalista

### Session State Pattern
**Mínimo Estado Necesario**:
- Current command context
- Coordination flags entre comandos
- User vision authority references
- Anti-complexity metrics tracking

### Persistence Pattern
**Qué Persiste Entre Sesiones**:
- user-vision/ structure (autoridad suprema)
- docs/ technical modules (implementation)
- .claude/commands/ (executable workflows)
- handoff/ continuity data

**Qué NO Persiste**:
- Session temporary state
- Command internal processing data
- Validation intermediate results

## Referencias a Autoridad
- user-vision/TRUTH_SOURCE.md líneas 66-71: Command independence architecture
- user-vision/TRUTH_SOURCE.md líneas 69-71: Orchestration model técnico
- docs/workflows/commands.md: Filosofía comandos independientes
- docs/workflows/coordination.md: Patterns coordinación
- docs/core/principles.md: Separación responsabilidades enforcement