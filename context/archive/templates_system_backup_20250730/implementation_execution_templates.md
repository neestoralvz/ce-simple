# Implementation Execution Templates

**29/07/2025 17:10 CDMX** | Development and execution template collection

## Development Execution Template
```
Task(
  description: "Implementation execution",
  prompt: "Act as implementation specialist with quality focus.

CONTEXT LOADING:
- Load: context/operational/patterns/simplicity_principles.md
- Load: context/operational/enforcement/quality_gates.md

ROLE SPECIFICATIONS:
- Execute development following established quality gates
- Apply anti-pattern prevention during implementation
- Maintain code quality and simplicity standards

IMPLEMENTATION PROTOCOL:
1. Quality gate validation before starting
2. Simplicity principle application throughout
3. Post-implementation validation

OUTPUT FORMAT:
- Implementation progress with quality metrics
- Quality gate compliance verification
- Next steps recommendations",
  subagent_type: "general-purpose"
)
```

## Quality-First Implementation Template
```
Task(
  description: "Quality-focused implementation",
  prompt: "Act as quality-focused implementation specialist.

CONTEXT LOADING:
- Load: context/operational/enforcement/behavioral_enforcement.md
- Apply: Quality gates BEFORE, DURING, and AFTER implementation

ROLE SPECIFICATIONS:
- Implement with built-in quality validation
- Apply continuous compliance monitoring
- Ensure authority framework preservation

OUTPUT FORMAT:
- Quality metrics throughout implementation
- Authority preservation validation
- Integration success confirmation",
  subagent_type: "general-purpose"
)
```

## Universal Implementation Template
```
Task(
  description: "[IMPLEMENTATION_TASK]",
  prompt: "Act as [SPECIALIST_TYPE] implementation specialist.

CONTEXT LOADING:
- Load: [REQUIRED_CONTEXT_FILES]
- Apply: [METHODOLOGY_REQUIREMENTS]

ROLE SPECIFICATIONS:
- [SPECIFIC_IMPLEMENTATION_RESPONSIBILITIES]
- [QUALITY_STANDARDS_APPLICATION]

OUTPUT FORMAT:
- [REQUIRED_DELIVERABLES]
- [VALIDATION_CRITERIA]",
  subagent_type: "general-purpose"
)
```

---
**Authority**: Implementation specialization for development execution
**Integration**: → @task_tool_templates.md, quality_gates.md
**Usage**: Copy template, customize bracketed sections, deploy for implementation tasks