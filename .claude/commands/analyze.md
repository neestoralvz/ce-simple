---
contextflow:
  next: ["visualize", "refactor", "document"]
  prev: ["explore"]
  triggers: ["analysis complete", "patterns identified", "issues found"]
---

Analyze codebase: $ARGUMENTS

## Specialized Subagent Orchestration
**EJECUTAR simultáneamente en mismo mensaje**:
```
Task 1: Research Specialist - "Investigate $ARGUMENTS best practices + patterns"
Task 2: Architecture Validator - "Analyze $ARGUMENTS system consistency + issues"
Task 3: Content Optimizer - "Identify $ARGUMENTS optimization opportunities"
```

**Main agent consolidates subagent analysis y genera insights integrados**

OUTPUT: 
- Issue count: X critical, Y warnings
- Top 3 patterns detected
- Max 3 priority recommendations

SUGGEST: Use /visualize for charts or /refactor for improvements