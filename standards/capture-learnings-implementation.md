# Capture-Learnings Implementation Standards

## Learning Value Scoring Framework

### Historical Context Weighting
- Days since last interview: +1 point (max +3)
- Consecutive simple executions: +1 point per 3 executions
- Novel domain interactions: +2 points

### Execution Complexity Scoring
```
Sequential commands (>2): +2 points
Error resolution occurred: +2 points  
New patterns discovered: +2 points
Alternative strategies evaluated: +1 point
Unexpected execution time: +1 point
Novel tool combinations: +1 point
Context switching required: +1 point
```

## Dynamic Interview Question Pools

### Context-Driven Questions
- **Process Effectiveness**: "¿El workflow siguió la secuencia que esperabas?"
- **Result Quality**: "¿Los resultados coinciden con tu visión inicial?"
- **Friction Points**: "¿Hubo algún momento donde te sentiste perdido o confundido?"
- **Discovery Value**: "¿Aprendiste algo inesperado sobre tu código/dominio?"
- **Efficiency Assessment**: "¿Qué cambiarías del proceso para la próxima vez?"
- **System Evolution**: "¿El resultado sugiere mejoras al sistema mismo?"

### Adaptive Selection Logic
- Select 3 highest-value questions based on execution patterns detected
- Add extended questions only when multiple novel patterns found
- Prioritize density over quantity for cognitive load optimization

## Documentation Framework Structure

### Pattern Storage Architecture
```
context/patterns/
├── execution-patterns-[domain].md      # How workflows typically execute
├── decision-patterns-[domain].md       # Why certain choices made repeatedly  
├── friction-patterns-[domain].md       # Common obstacles and solutions
└── discovery-patterns-[domain].md      # Learning insights and breakthroughs
```

### Experience Integration Structure
```
context/experience/
├── workflow-effectiveness-[month].md   # Process efficiency insights
├── expectation-reality-[month].md      # Outcome vs prediction analysis
└── improvement-suggestions-[month].md  # User-driven enhancement ideas
```

## Agent Integration Protocols

### Process Learning Agent Objectives
1. **Decision Documentation**: Record why specific approaches chosen
2. **Pattern Classification**: Identify if discoveries are novel vs familiar
3. **Alternative Assessment**: Document considered but rejected options
4. **Context Enhancement**: Enrich existing context with meta-insights

### Results Learning Agent Workflow
1. **Execution Analysis**: Review full workflow trace and outcomes
2. **Interview Generation**: Create dynamic questions based on execution patterns
3. **User Engagement**: Conduct structured feedback interview
4. **System Integrity Validation**: Verify command system coherence and reference integrity
5. **Insight Integration**: Enhance existing patterns with experience data

## System Integrity Validation

### Validation Components
**Reference Integrity Check**:
- Command existence verification in "See Also" sections
- Chain consistency validation (bidirectional and complete)
- Cross-reference health (accessible files and sections)
- Trigger logic consistency across commands

### Gap Discovery Notification System
```
🔍 INTEGRITY: Scanning command references from executed workflow
📊 ANALYSIS: [X] commands checked, [Y] references validated
⚠️  GAPS: [N] missing references detected → [list of gaps]
🔧 RECOMMENDATIONS: [Specific actions to resolve gaps]
```

### Gap Classification System
- **Critical Gap**: Missing command breaks workflow execution
- **Reference Gap**: Broken cross-reference reduces navigation efficiency  
- **Chain Gap**: Incomplete workflow progression creates user confusion
- **Documentation Gap**: Inconsistent or outdated references

### Resolution Priority Framework
1. **Immediate**: Critical gaps affecting workflow functionality
2. **High**: Reference gaps in frequently used commands
3. **Medium**: Chain gaps in secondary workflows
4. **Low**: Documentation gaps in rarely accessed sections

### Recommendation Engine Format
```
🎯 RESOLUTION RECOMMENDATIONS:
├── Create missing command: [command-name] referenced in [N] locations
├── Update references: Replace [old-ref] with [new-ref] in [files]
├── Complete chain: Add [missing-link] to connect [workflow-a] → [workflow-b]  
└── Validate architecture: Review [command-set] for consistency
```

## Notification Standards

### Validation Integration Notifications
```
🔍 INTEGRITY: System validation initiated → Workflow context analysis
📊 VALIDATION: [X] commands verified, [Y] references checked
⚠️  DISCOVERY: [N] gaps identified → [severity breakdown]
✅ COMPLETION: System health documented → Recommendations generated
```