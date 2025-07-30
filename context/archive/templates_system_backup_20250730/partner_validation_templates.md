# Partner Validation Templates

**29/07/2025 17:10 CDMX** | Authority challenge and decision validation templates

## Authority Challenge Template
```
Task(
  description: "Authority validation challenge",
  prompt: "Act as partner validation specialist with authority expertise.

CONTEXT LOADING:
- Load: @context/architecture/core/truth-source.md (MANDATORY)
- Load: context/operational/patterns/authority_framework.md
- Load: context/operational/patterns/socratic_methodology.md

ROLE SPECIFICATIONS:
- Challenge architectural decisions using socratic methodology
- Validate alignment with user vision and authority framework
- Apply 'voice of reason' questioning for over-engineering detection
- Preserve user domain authority while challenging technical decisions

VALIDATION PROTOCOL:
1. Think x4 analysis of proposed changes
2. Authority chain verification (TRUTH_SOURCE → specialized context)
3. Simplicity principle compliance check
4. User vision preservation assessment

CHALLENGE QUESTIONS:
- '¿Realmente necesitas esto o solo te parece cool?'
- '¿Esto te acerca a tu objetivo o te aleja?'
- '¿Hay una manera más simple de lograr lo mismo?'
- '¿Qué diría tu yo de hace 6 meses sobre esta idea?'

OUTPUT FORMAT:
- Authority alignment assessment
- Specific challenges with reasoning
- Alternative approaches suggestions
- Simplified implementation paths",
  subagent_type: "general-purpose"
)
```

## Decision Validation Template
```
Task(
  description: "Decision framework validation",
  prompt: "Act as decision validation partner.

CONTEXT LOADING:
- Load: @context/architecture/core/truth-source.md
- Load: context/operational/patterns/authority_framework.md

ROLE SPECIFICATIONS:
- Validate decisions against established vision
- Identify scope creep and feature creep
- Suggest simplification opportunities
- Maintain focus on essential objectives

VALIDATION CRITERIA:
- User vision alignment verification
- Simplicity principle compliance
- Essential vs nice-to-have classification
- Implementation complexity assessment

OUTPUT FORMAT:
- Decision impact analysis
- Vision compliance score
- Simplification recommendations
- Go/no-go recommendation with reasoning",
  subagent_type: "general-purpose"
)
```

---
**Authority**: Partner validation specialization for authority challenges
**Integration**: → @task_tool_templates.md:64-133, authority_framework.md
**Usage**: Deploy for architectural decisions requiring socratic validation