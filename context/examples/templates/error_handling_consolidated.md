# Error Handling Templates - Consolidated

**29/07/2025 11:35 CDMX** | Error handling templates for systematic error management

## Core Error Templates

### Template Error Recoverable
"Encontrado [ISSUE] en [SUBTAREA]. Intentando [WORKAROUND] automáticamente..."

### Template Error Crítico  
"ERROR CRÍTICO: [DESCRIPTION]. Ejecución pausada. Requiere intervención usuario para [RESOLUTION]."

## Error Response Framework

### Principio Fundamental
**PRINCIPIO:** Agotar opciones automáticas antes de pausar

### Error Classification System
**RECOVERABLE ERRORS:**
- Temporary file access issues
- Network connectivity problems
- Resource conflicts with workarounds available
- Parsing errors with fallback methods

**CRITICAL ERRORS:**
- Fundamental system corruption
- Required resources permanently unavailable
- Security violations
- Data integrity threats

## Exception Management

### Excepciones Válidas Para Detención
**ÚNICAMENTE detener ejecución cuando:**
- **Error crítico:** Imposibilidad técnica de continuar
- **Usuario solicita STOP:** Comando explícito de parada
- **Recurso bloqueado:** Dependencia externa no disponible
- **Clarificación requerida:** Ambigüedad que impide progreso
- **Scope change:** Usuario modifica objetivos mid-execution

### Error Recovery Protocol
1. **Detection**: Identify error type and scope
2. **Classification**: Determine if recoverable or critical
3. **Automatic Resolution**: Attempt workarounds for recoverable errors
4. **Escalation**: Only pause for critical errors requiring user intervention
5. **Documentation**: Log error and resolution for learning

## Advanced Error Templates

### Error Detection Framework Template
**DETECTION TRIGGERS:**
- System inconsistency patterns
- Performance degradation indicators
- Authority chain violations
- Template duplication detection

**RESPONSE PROTOCOL:**
- Immediate automatic correction when possible
- Escalation to specialized agents when required
- User notification for manual intervention needs
- System state preservation during error handling

### Recovery Procedures Template
**RECOVERY SEQUENCE:**
1. **Isolate**: Contain error scope to prevent propagation
2. **Analyze**: Determine root cause and impact assessment
3. **Restore**: Apply appropriate recovery mechanism
4. **Validate**: Verify system integrity post-recovery
5. **Document**: Record incident for prevention improvement

## Usage Guidelines

### Template Application
- **Usar Template Recoverable** para errores que permiten workarounds
- **Usar Template Crítico** solo cuando ejecución debe pausarse completamente
- **Siempre intentar** resolución automática antes de escalar
- **Proporcionar información específica** para resolución manual cuando necesario

### Error Communication
- **Be specific** about error location and nature
- **Suggest solutions** when possible
- **Maintain transparency** about attempted resolutions
- **Preserve execution momentum** whenever possible

### Prevention Integration
**PROACTIVE MEASURES:**
- Regular health monitoring integration
- Predictive error detection patterns
- Automatic system validation protocols
- Template compliance enforcement

## Integration Syntax
```markdown
**TEMPLATE:** /examples:error_handling_consolidated
```

---
**Authority Source**: context/operational/patterns/orchestrator_methodology.md + context/operational/enforcement/error_detection_framework.md
**Extracted from**: Error handling templates across orchestrator, enforcement, and recovery documentation
**Consolidation Date**: 29/07/2025 - Template deduplication initiative