# Communication Protocols

## Purpose
Define agent communication patterns for nested orchestration systems.

## Agent Hierarchy

### Level 1: Coordinators
- **Code Analysis**: Manages 16-32 language specialists
- **Documentation**: Manages 12-24 content specialists  
- **Configuration**: Manages 8-16 format specialists
- **Testing**: Manages 12-20 test specialists

### Level 2: Specialists
- **JavaScript/TypeScript**: React, Node.js, build systems, dependencies
- **Python**: Frameworks, data science, packages, testing
- **Go/Java**: Language-specific patterns and structures

### Level 3: Micro-Agents
- **Component Analysis**: Individual files, patterns, relationships
- **Function Analysis**: Single operations with specific focus
- **Pattern Recognition**: Targeted searches and validations

### Level 4: Nano-Agents
- **Atomic Operations**: Single file/function analysis
- **Immediate Results**: No further delegation
- **Specific Tasks**: Grep, Read, extract, process

## Load Balancing

### Distribution Strategies
- **Horizontal**: Work queue across peer agents
- **Vertical**: Task breakdown across levels
- **Adaptive**: Real-time performance adjustment

### Resource Management
- **Monitor**: I/O, memory, CPU, network usage
- **Prioritize**: Critical path operations first
- **Adjust**: Real-time reallocation and balancing

## Context Flow

### Information Direction
- **Bottom-Up**: Atomic results → system understanding
- **Top-Down**: Strategic goals → operation parameters
- **Lateral**: Peer sharing and correlation

### Consistency Rules
- **Critical Updates**: Immediate propagation
- **Routine Updates**: Batched processing
- **Validation**: Cross-level consistency checks

## Communication Patterns

### Message Flow
- **Master-Coordinator**: Strategic directives, resource allocation
- **Coordinator-Specialist**: Domain tasks, technology focus
- **Specialist-Micro**: File operations, pattern matching
- **Micro-Nano**: Atomic operations, immediate results

## Message Types

### Command Messages
- Task assignment, resource allocation, priority changes
- Strategy modification, emergency controls

### Status Messages  
- Progress reports, resource usage, performance metrics
- Error notifications, completion confirmations

### Data Messages
- Results, context updates, pattern discoveries
- Cross-references, metadata, summaries

### Coordination Messages
- Synchronization, conflict resolution, load balancing
- Quality validation, optimization suggestions

---

**IMPLEMENTATION**: Use this protocol for nested agent orchestration with clear hierarchy and communication patterns.