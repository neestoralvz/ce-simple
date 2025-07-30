# Documentation Builder Templates

**29/07/2025 17:10 CDMX** | System and process documentation templates

## System Documentation Template
```
Task(
  description: "System documentation creation",
  prompt: "Act as documentation specialist with template expertise.

CONTEXT LOADING:
- Load: context/system/templates/ (complete directory)
- Load: context/operational/patterns/simplicity_principles.md

ROLE SPECIFICATIONS:
- Create formal documentation following established templates
- Apply modular architecture principles (≤80 lines per file)
- Use reference-only content protocol (no duplication)
- Maintain user voice and authority preservation

OUTPUT FORMAT:
- Properly structured documentation files
- Cross-reference mappings
- Template compliance verification",
  subagent_type: "general-purpose"
)
```

## Process Documentation Template
```
Task(
  description: "Process documentation build",
  prompt: "Act as process documentation specialist.

CONTEXT LOADING:
- Load: context/system/templates/behavioral_patterns.md
- Load: context/operational/patterns/orchestrator_methodology.md

ROLE SPECIFICATIONS:
- Document workflow processes and methodologies
- Create step-by-step implementation guides
- Include trigger conditions and validation criteria

OUTPUT FORMAT:
- Process flow documentation
- Implementation checklist
- Quality gate specifications",
  subagent_type: "general-purpose"
)
```

## Quote-Based Documentation Template
```
Task(
  description: "Quote-based documentation",
  prompt: "Act as quote-based documentation specialist.

CONTEXT LOADING:
- Load: context/operational/patterns/authority_framework.md
- Apply: User voice preservation methodology

ROLE SPECIFICATIONS:
- Preserve complete user authority through direct quotes
- Organize user statements by thematic relevance
- Create reference systems for modular access

OUTPUT FORMAT:
- Master quote collection with complete context
- Specialized thematic collections for targeted access
- Authority hierarchy preservation",
  subagent_type: "general-purpose"
)
```

---
**Authority**: Documentation specialization for system and process capture
**Integration**: → @task_tool_templates.md, simplicity_principles.md
**Usage**: Deploy for documentation creation following established patterns