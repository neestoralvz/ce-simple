---
contextflow:
  next: ["commit", "deploy", "document"]
  prev: ["refactor", "implement"]
  triggers: ["tests passing", "coverage complete"]
  research-driven: true
---

Test implementation: $ARGUMENTS

## Testing Orchestration via Specialists
**EJECUTAR comprehensive testing workflow**:
```
Task 1: Research Specialist - "Research $ARGUMENTS testing strategies + coverage standards"
Task 2: Architecture Validator - "Analyze $ARGUMENTS test architecture + integration points"
Task 3: Content Optimizer - "Run tests + add missing coverage for $ARGUMENTS"
Task 4: Quality Assurance - "Validate $ARGUMENTS functionality + performance criteria"
```

**Main agent orchestrates testing pipeline ensuring comprehensive validation**

OUTPUT:
- Test status: X passed, Y failed
- Coverage: Z%
- New tests added: N

SUGGEST: Use /commit if all green or /debug if failures