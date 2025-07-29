# Implementation Anti-Patterns Prevention

Prevention of architectural violations and quality issues.

## Architecture Violations
**Prohibited Patterns:**
- **Authority hierarchy bypass** → Skip user-vision consultation
- **Single-conversation limitation** → Force complex tasks into one conversation
- **Background process avoidance** → Fail to use persistent monitoring
- **Git worktree omission** → Not using branch-per-conversation for complex tasks

## Implementation Quality Violations
**Mandatory Requirements:**
- **Authority consultation** for all systemic changes
- **Challenge system integration** for problem/solution detection  
- **User feedback priority** over AI optimization recommendations
- **Multi-conversation capability** for complex orchestration needs

---

**Prevention principle**: Systematic violation detection maintains architectural integrity and quality standards.

**Trazabilidad:** user-vision/layer3/architecture_principles.md → Operations distillation
**Execution:** Apply to ALL architectural decisions and implementations
**Integration:** → behaviors/orchestration_protocol.md, patterns/command_architecture.md