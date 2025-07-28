---
contextflow:
  purpose: "Token economy + context loading optimization strategies"
  type: "context"
  related: ["system-architecture.md", "methodology-core.md"]
---

# Token Economy + Context Loading

## FILE SIZE OPTIMIZATION

### Core Files Target
- **Core files**: 50-80 líneas máximo
- **Extensions**: Enlaces condicionales cuando necesario
- **Division inteligente**: Core principles + detailed extensions
- **NO imports automáticos** para extensions

### Context Loading Strategy
- **`@/archivo.md`**: Carga automática context (imperativa)
- **[enlaces condicionales]**: "Si necesitas X, ve a Y" (opcional)
- **Decision trees**: Metadata para usage optimization
- **Efficiency measurement**: Auto-tracking performance

## CLEAN SLATE RECREATION

### Principio Anti-Bias
**Problem**: Actualizaciones incrementales acumulan bias información antigua.
**Solution**: Recreación completa desde principios + decisiones recientes.

### Recreation Triggers
- **Staleness detectada**: Files unchanged + system evolved
- **Architecture shift**: Fundamental principles changed  
- **Bias accumulation**: Incremental changes sin coherence
- **User explicit request**: "Recreate desde cero"

### Recreation Scope
- **Individual files**: Component específico
- **Structure-level**: Carpetas/ecosystems completos  
- **System-wide**: Multiple components coordinado

## EFFICIENCY MEASUREMENT

### Decision Tree Performance
- **Context loading optimization**: Speed + accuracy metrics
- **Command count vs efficiency**: Balance monitoring  
- **Usage pattern analysis**: Most/least effective paths
- **Auto-optimization**: Subagent suggestions para improvement

### System Health Indicators
- **Token economy compliance**: File size distribution
- **Voice preservation accuracy**: User intent maintenance
- **Integration coherence**: System consistency scores
- **Evolution velocity**: Adaptation speed + quality

---

**Tools**: 
- [Clean slate recreation command](../clean-slate-recreation.md)
- [Efficiency tracker utility](../utilities/efficiency-tracker.md)