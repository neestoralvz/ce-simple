# Technical Architecture

**Updated**: 2025-07-26 12:00 (Mexico City) | **Authority**: Complete technical vision | **Lines**: ≤80  
**Core**: [Central Concept](concept-vision.md) | [Command Philosophy](commands-vision.md) | [Execution Strategies](execution-vision.md)  
**Implementation**: [Core Architecture](../core/README.md) | [Agent Deployment](../protocols/agent-deployment-protocols.md) | [Parallelization System](../core/04-parallelization-system.md)

## Core Execution Mechanism

**Task Tool Integration**: Claude Code's Task Tool provides core execution foundation:
- Parallel execution of up to 10 sub-agents per command
- Each sub-agent has access to Read/Write/Edit/Bash tools  
- Sub-agents cannot spawn additional tasks or invoke slash commands
- Clear output formats & graceful error handling

**Execution Flow**: User Request → Command Analysis → Sub-agent Deployment → Parallel Execution → Result Synthesis → User Delivery

## Technical Constraints & Solutions

**Autocontainment Requirement**: Commands MUST be self-contained due to technical limitations:
- Sub-agents have no access to other commands or external files
- All logic, patterns, templates must be embedded inline
- Context & instructions passed explicitly to sub-agents
- No external dependencies or configuration requirements

**Git WorkTrees for Parallel Development**: Enable conflict-free parallel operations:
- Isolated file operations preventing merge conflicts
- Multiple agents working on same codebase simultaneously  
- Clean integration & session management
- Automated cleanup & maintenance protocols

## Quality Assurance Architecture

**PTS Framework**: 12-component technical validation system:
- **Technical Cluster**: Directness, Precision, Sufficiency, Excellence
- **Communication Cluster**: Exactitude, Sobriety, Structure, Conciseness
- **Cognitive Cluster**: Clarity, Coherence, Effectiveness, Pragmatism

**Error Recovery Framework**: Built-in fault tolerance:
- Phase-level recovery with rollback to stable checkpoints
- Command-level recovery with alternative routing
- System-level recovery with comprehensive failure analysis
- 95%+ automatic recovery without human intervention

## Performance Architecture

**Git-Based Intelligence**: Orchestration driven by Git metrics:
- Commit patterns & success indicators for decision making
- Branch lifecycle & merge success rates optimization
- Performance timeline data from Git history analysis
- Autonomous resource allocation based on historical data

**Parallelization Levels**: Optimized parallel execution:
- Search tasks: 8-16 parallel (20x speedup)
- File operations: 5-10 parallel (10x speedup)  
- Analysis tasks: 4-8 parallel (4x speedup)
- Validation operations: distributed testing (minutes vs hours)

---

**Technical Vision**: Sophisticated parallel architecture with simple user interface, powered by intelligent Git-based decision making.