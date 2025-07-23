# ce-simple: Core Architecture

## Purpose
Core documentation for ce-simple's living command system using progressive disclosure principles.

## System Overview
ce-simple creates **self-contained slash commands** that orchestrate **parallel task execution** through Claude Code's Task Tool to transform **user vision into reality**.

### Foundation Layer Integration
The system includes a **00-core foundation layer** providing essential infrastructure:
- **Project initialization** with complete setup and git integration
- **Automated context management** with distributed memory synchronization
- **Centralized notifications** for transparent delegation and state tracking  
- **Seamless handoff management** between agents, sessions, and workflow phases

## Core Documentation

### [System Principles](system-principles.md) 
System foundation and architectural principles.
- Interview-Driven Development
- Task Orchestration philosophy  
- Living System qualities
- Complete architectural overview with embedded detail patterns

### [Task Orchestration](task-orchestration.md)
Task orchestration patterns and strategies.
- 7-Parallel-Tasks method
- Wave deployment patterns
- Parallelization guidelines
- Complete Task Tool specifications

### [Context Architecture](context-architecture.md)
Distributed context and memory architecture.
- Minimal conductor context
- Dynamic context loading  
- Git-based persistence
- Complete distributed memory framework with implementation details

### [Evolution and Learning](evolution-learning.md)
Comprehensive learning and adaptation protocols.
- Multi-level learning architecture
- Sophisticated adaptation mechanisms
- Quality-controlled evolution cycles
- Cross-domain knowledge transfer

### [Performance](../frameworks/performance-framework.md)
Performance monitoring, benchmarks, and optimization.
- Scale-based performance standards
- Concurrent operations framework
- Resource utilization monitoring
- Mathematical performance models

### [Patterns](../frameworks/execution-patterns.md)
Comprehensive execution pattern library.
- Creation patterns (Seven-Parallel-Tasks)
- Discovery patterns (Four-Phase approach)
- Transformation patterns (Safety-first)
- Problem-solving patterns (Universal framework)

### [Validation](../frameworks/validation-framework.md)
Unified validation and quality assurance framework.
- Three-layer verification protocol
- Cross-reference analysis
- Quality assurance standards
- Anti-bias enforcement

## Documentation Standards
All core documents follow progressive disclosure:
- **Core files** (≤200 lines): Essential concepts and practices
- **Detail files** (unlimited): Advanced specifications and implementation

## Reading Order
1. Start with **system-principles.md** for system foundation
2. Continue with **task-orchestration.md** for execution patterns
3. Review **context-architecture.md** for memory architecture
4. Study **[performance-framework.md](../frameworks/performance-framework.md)** for optimization guidelines
5. Explore **[execution-patterns.md](../frameworks/execution-patterns.md)** for execution strategies
6. Complete with **[validation-framework.md](../frameworks/validation-framework.md)** for quality standards
7. Finish with **evolution-learning.md** for comprehensive learning and adaptation protocols

Each core document ends with a reference to its detail file for deeper exploration.

## Integration
Core documentation integrates with:
- **Foundation layer** in `/commands/00-core/` - Essential infrastructure commands
- Command templates in `/standards/`
- System overview in `/vision/`
- Context patterns in `/context/`

### Foundation Command Integration
- **init-project** integrates with system-principles.md for project architecture
- **context-engine** implements context-architecture.md distributed memory patterns
- **notify-manager** supports task-orchestration.md transparency requirements
- **handoff-manager** enables evolution-learning.md learning and adaptation protocols

---

**Next Step**: Begin with [system-principles.md](system-principles.md) to understand the system foundation.