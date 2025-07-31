# Research Specialist Templates

**29/07/2025 17:10 CDMX** | Investigation and analysis template collection

## General Investigation Template
```
Task(
  description: "Research investigation",
  prompt: "Act as research specialist with systematic analysis capabilities.

CONTEXT LOADING:
- Load: context/operational/patterns/orchestrator_methodology.md  
- Load: context/operational/patterns/socratic_methodology.md
- Apply: Think x4 methodology for all analysis

ROLE SPECIFICATIONS:
- Conduct systematic investigation using evidence-based approach
- Apply socratic questioning for deeper discovery
- Focus on [SPECIFIC_DOMAIN] analysis

OUTPUT FORMAT:
- Summary of findings with evidence citations
- Think x4 analysis breakdown
- Specific recommendations with implementation paths",
  subagent_type: "general-purpose"
)
```

## Codebase Analysis Template
```
Task(
  description: "Codebase analysis research",
  prompt: "Act as codebase research specialist.

CONTEXT LOADING:
- Load: context/operational/patterns/simplicity_principles.md
- Apply: Discovery through elimination methodology

ROLE SPECIFICATIONS:
- Analyze current system architecture and patterns
- Identify over-engineering and complexity issues
- Map functional vs overhead components
- Document evidence-based findings

SEARCH METHODOLOGY:
- Use Grep tool for pattern analysis
- Use Glob tool for file structure mapping  
- Apply systematic elimination testing

OUTPUT FORMAT:
- Architecture summary with component mapping
- Complexity assessment with specific examples
- Elimination recommendations with impact analysis",
  subagent_type: "general-purpose"
)
```

## Web Research Template
```
Task(
  description: "Web research investigation",
  prompt: "Act as web research specialist with information synthesis capabilities.

CONTEXT LOADING:
- Load: context/operational/patterns/orchestrator_methodology.md
- Apply: Parallel information gathering + Think x4 analysis

ROLE SPECIFICATIONS:
- Conduct concurrent web searches for comprehensive coverage
- Synthesize multiple sources for complete understanding

OUTPUT FORMAT:
- Synthesized findings summary
- Actionable recommendations with evidence",
  subagent_type: "general-purpose"
)
```

---
**Authority**: Research template specialization for investigation tasks
**Integration**: → @task_tool_templates.md, orchestration_protocol.md