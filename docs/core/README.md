# ce-simple: Core Architecture

## Purpose
Core documentation for ce-simple's living command system using progressive disclosure principles.

## System Overview
ce-simple creates **self-contained slash commands** that orchestrate **parallel task execution** through Claude Code's Task Tool to transform **user vision into reality**.

## Core Documentation

### [Principles](principles.md) 
System foundation and architectural principles.
- Interview-Driven Development
- Task Orchestration philosophy  
- Living System qualities
- [See details →](principles-details.md)

### [Orchestration](orchestration.md)
Task orchestration patterns and strategies.
- 7-Parallel-Tasks method
- Wave deployment patterns
- Parallelization guidelines
- [See details →](orchestration-details.md)

### [Context System](context-system.md)
Distributed context and memory architecture.
- Minimal conductor context
- Dynamic context loading  
- Git-based persistence
- [See details →](context-system-details.md)

### [Evolution](evolution.md)
Learning and adaptation protocols.
- Per-session learning cycles
- Pattern extraction methods
- Adaptive behaviors
- [See details →](evolution-details.md)

## Documentation Standards
All core documents follow progressive disclosure:
- **Core files** (≤200 lines): Essential concepts and practices
- **Detail files** (unlimited): Advanced specifications and implementation

## Reading Order
1. Start with **principles.md** for system foundation
2. Continue with **orchestration.md** for execution patterns
3. Review **context-system.md** for memory architecture
4. Complete with **evolution.md** for learning protocols

Each core document ends with a reference to its detail file for deeper exploration.

## Integration
Core documentation integrates with:
- Command templates in `/standards/`
- Implementation patterns in `/patterns/`
- System overview in `/vision/`

---

**Next Step**: Begin with [principles.md](principles.md) to understand the system foundation.