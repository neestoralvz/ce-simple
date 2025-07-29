# Quick Reference - Documentación Oficial

**Fuente:** Síntesis práctica desde todos los layers + conversación directa

## Command Quick Reference

### Core Commands
- **`/start`** - Universal entry point, context-intelligent session starter  
- **`/distill`** - Iterative conversation processing: raw → núcleos → síntesis → docs
- **`/challenge`** - External validation agent for alignment and over-engineering detection
- **`/partner`** - Consultor constructor for simplicity and focus maintenance
- **`/docs`** - Document creation/editing with vision alignment
- **`/git`** - Version control integration with intelligent commit messages

### Workflow Commands  
- **`/explore`** - Codebase navigation and understanding
- **`/debug`** - Systematic problem resolution
- **`/maintain`** - System maintenance and consistency checks
- **`/close`** - Session capture and change commit

## Key Principles Quick Reference

### Methodology Principles
1. **Two-Phase**: Unrestricted discovery → Structured execution
2. **Socratic**: Conversation sin restricciones para verdadero descubrimiento  
3. **Story-Driven**: Narrative humana → Reality manifestation
4. **Human-Centric**: "Una nueva forma de trabajar con IA que sea más humana"

### Architecture Principles
1. **Command Independence**: Autocontenidos pero coordinables
2. **Universal Orchestration**: `/start` como entry point inteligente
3. **State-Based Communication**: Via file system, no direct coupling
4. **Layered Authority**: TRUTH_SOURCE.md → CLAUDE.md → commands/

### Quality Principles
1. **Simplicity-First**: "la belleza va a estar en la simplicidad"
2. **Vision Preservation**: 100% fidelidad a voz del usuario
3. **Anti-Bias**: Zero contaminación AI en insights
4. **Challenge-Driven**: Validación externa automática

## Authority Hierarchy Quick Reference

```
user-vision/TRUTH_SOURCE.md     [AUTORIDAD SUPREMA]
        ↓
CLAUDE.md                       [Sistema base]
        ↓  
.claude/commands/               [Workflows ejecutables]
        ↓
System files                    [Implementación]
```

## Workflow Patterns Quick Reference

### Standard Request Pattern
1. **Discovery**: Conversación socrática sin restricciones
2. **Planning**: Documentación obligatoria antes de ejecución  
3. **Execution**: Comandos coordinados con token optimization
4. **Validation**: `/challenge` para verificar alineación

### Quality Gates Pattern  
**3-Stage:** Creación → Alineamiento → Verificación

### Evolution Pattern
1. **Metrics-Driven**: Crecimiento justificado por eficiencia
2. **Vision-Anchored**: Evolución preservando esencia
3. **Clean Slate**: Regeneración periódica anti-sesgo

## File Structure Quick Reference

```
/
├── CLAUDE.md                   # Sistema base
├── .claude/commands/           # 9 comandos independientes
├── user-vision/               # AUTORIDAD SUPREMA
│   ├── TRUTH_SOURCE.md        # Visión consolidada
│   ├── layer1/                # Núcleos temáticos con quotes
│   ├── layer2/                # Síntesis de relaciones  
│   ├── layer3/                # Documentación oficial
│   └── raw/conversations/     # Conversaciones originales
└── handoff/                   # Continuidad entre sesiones
```

## Troubleshooting Quick Reference

### Si el sistema se siente complejo:
- Ejecutar `/challenge` para detectar over-engineering
- Verificar alineación con principios de simplicidad
- Considerar clean slate regeneration

### Si hay pérdida de contexto:
- Revisar `handoff/` para continuidad
- Ejecutar `/start` para context recovery
- Validar autoridad hierarchy

### Si hay conflicto de información:
- TRUTH_SOURCE.md siempre gana sobre otros documentos
- Regenerar desde fuentes puras si hay contaminación
- Usar trazabilidad exacta para verificar origen

## Success Metrics Quick Reference

### Conversation Quality
- Se siente natural y humana
- Discovery phase without token anxiety
- Proactive suggestions and challenges

### Implementation Quality  
- Execution aligned with vision
- Simplicity maintained over time
- Anti-bias protection working

### System Quality
- Commands coordinate smoothly
- Context intelligence functioning
- Organic evolution vs feature creep

---

**Remember:** "no te ovy a decir como hacer las cosas, tu debes de decidirlo de acuero a mi vision y lo que te digo, enteinde esto como una de las maximas de este proyecto"