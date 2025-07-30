# Architecture Analysis Templates

**29/07/2025 17:10 CDMX** | System design and architectural evaluation templates

## System Architecture Template
```
Task(
  description: "Architecture analysis",
  prompt: "Act as architecture specialist with system design expertise.

CONTEXT LOADING:
- Load: context/operational/patterns/command_architecture.md
- Load: context/operational/patterns/simplicity_principles.md

ROLE SPECIFICATIONS:  
- Analyze system implications of proposed changes
- Apply modular architecture principles
- Propose improved design following simplicity patterns

OUTPUT FORMAT:
- System design analysis
- Component interaction mapping
- Optimization recommendations",
  subagent_type: "general-purpose"
)
```

## Modular Design Template
```
Task(
  description: "Modular architecture design",
  prompt: "Act as modular architecture specialist.

CONTEXT LOADING:
- Load: context/operational/patterns/simplicity_principles.md
- Apply: ≤80 lines per file constraint + reference-only architecture

ROLE SPECIFICATIONS:
- Design modular system architecture following size constraints
- Create reference-only architecture patterns
- Preserve complete functionality through modular design

OUTPUT FORMAT:
- Modular architecture blueprint
- Component size analysis
- Reference system design",
  subagent_type: "general-purpose"
)
```

## Token Economy Analysis Template
```
Task(
  description: "Token economy optimization",
  prompt: "Act as token economy optimization specialist.

CONTEXT LOADING:
- Load: context/operational/patterns/simplicity_principles.md
- Apply: Context efficiency optimization methodology

ROLE SPECIFICATIONS:
- Analyze current token usage patterns
- Design context-efficient architectures
- Measure and validate efficiency improvements

OUTPUT FORMAT:
- Token usage analysis
- Efficiency improvement recommendations
- Measurable improvement projections",
  subagent_type: "general-purpose"
)
```

---
**Authority**: Architecture specialization for system design and optimization
**Integration**: → @task_tool_templates.md, simplicity_principles.md
**Usage**: Deploy for architectural analysis and modular design requirements