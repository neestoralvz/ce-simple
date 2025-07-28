---
contextflow:
  next: ["test", "commit", "document"]
  prev: ["analyze"]
  triggers: ["refactoring complete", "code improved"]
  research-driven: true
---

Refactor code: $ARGUMENTS

## Refactoring Orchestration with Safety Checks
**EJECUTAR staged approach con validation**:
```
Task 1: Research Specialist - "Research $ARGUMENTS refactoring patterns + best practices"
Task 2: Architecture Validator - "Assess $ARGUMENTS improvement opportunities + risk analysis"
Task 3: Content Optimizer - "Apply refactoring maintaining functionality + performance"
Task 4: Quality Assurance - "Verify $ARGUMENTS changes correctness + test validation"
```

**Main agent ensures safe refactoring workflow con comprehensive validation**

OUTPUT:
- Changes summary (max 50 words)
- Performance impact estimate
- Breaking changes: none/minor/major

SUGGEST: Use /test to validate or /commit to save progress