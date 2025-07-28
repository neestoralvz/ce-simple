# Multi-Subagent Orchestration - Master Template

## Core Orchestration Principle
**El agente principal NUNCA ejecuta trabajo directo - SIEMPRE orquesta especialistas via Task tools.**

## Subagent Specialization Matrix

| Specialist | Primary Focus | Common Uses | Template |
|------------|---------------|-------------|----------|
| **Research** | Investigation + benchmarking | Best practices, case studies, anti-patterns | [research-specialist.md](./research-specialist.md) |
| **Architecture** | System consistency + integration | Validation, conflict detection, alignment | [architecture-validator.md](./architecture-validator.md) |
| **Content** | Token economy + optimization | Structure, density, efficiency | [content-optimizer.md](./content-optimizer.md) |
| **Voice Preservation** | User voice exactitude | Quote preservation, intent maintenance | [voice-preservation.md](./voice-preservation.md) |
| **Quality** | Final validation + standards | Quality gates, compliance, deployment | [quality-assurance.md](./quality-assurance.md) |

## Parallel Orchestration Pattern

### Single Task Deployment
```
Task: [Specialist Type]
Description: "[3-5 word objective]"  
Subagent: general-purpose
Prompt: "[Specialized template prompt from appropriate template file]"
```

### Concurrent Multi-Task Pattern
**SIEMPRE usar múltiples Task tools cuando posible para máxima eficiencia:**

```
// Example: Document creation workflow
Task 1: Research Specialist - "Investigate [topic] best practices"
Task 2: Architecture Validator - "Verify [component] system consistency"
Task 3: Content Optimizer - "Optimize [content] token economy"

// Then consolidate results for final processing
```

## Common Orchestration Scenarios

### Document Creation (3-step workflow)
1. **Content Specialist** → Create initial draft
2. **Architecture Validator** → Verify alignment 
3. **Quality Assurance** → Final validation

### Research + Analysis
1. **Research Specialist** → Investigate topic
2. **Architecture Validator** → Check integration implications
3. **Voice Preservation** → Ensure user intent maintained

### Content Optimization
1. **Content Optimizer** → Structure + token economy
2. **Quality Assurance** → Standards compliance
3. **Voice Preservation** → User voice validation

### Complex Multi-Phase Tasks
1. **Research Specialist** → Initial investigation (parallel)
2. **Architecture Validator** → System analysis (parallel)
3. **Content Optimizer** → Draft optimization (sequential)
4. **Voice Preservation** → User voice validation (sequential)
5. **Quality Assurance** → Final validation (sequential)

## Orchestration Best Practices

### Task Design
- **Specific objectives**: Clear 3-5 word descriptions
- **Appropriate specialization**: Match task to specialist strength
- **Context provision**: Load relevant system context
- **Output requirements**: Define expected format

### Parallel Execution
- **Independent tasks**: Can run concurrently
- **Dependent tasks**: Must run sequentially  
- **Resource efficiency**: Maximize parallel when possible
- **Result consolidation**: Integrate parallel outputs

### Quality Control
- **Specialist expertise**: Trust subagent specialization
- **Cross-validation**: Multiple specialists on critical tasks
- **Error handling**: Clear failure modes + recovery
- **Continuous improvement**: Learn from orchestration patterns

## Success Metrics

### Efficiency Metrics
- Tasks completed per session
- Parallel vs sequential ratio
- Time to completion improvement
- Resource utilization optimization

### Quality Metrics  
- Specialist accuracy scores
- Cross-validation agreement
- Error reduction over time
- User satisfaction maintenance

## Integration with ContextFlow

### Conversation Phase
- **Socratic exploration** mantiene focus en comprensión
- **Challenge proactivo** via research specialist input
- **Context loading** automático para specialists

### Execution Phase  
- **Task deployment** seamless tras validation conversacional
- **Parallel processing** optimizado para efficiency
- **Result consolidation** for user presentation

### Evolution Phase
- **Pattern learning** from orchestration success/failure
- **Template refinement** based on specialist performance
- **System improvement** via orchestration insights

---

**Remember**: La potencia está en la orquestación inteligente de especialistas, no en hacer todo uno mismo.