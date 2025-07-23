# Architectural Principles

## Purpose
Core principles guiding ce-simple's Living Command System architecture and design decisions.

## Core Identity
ce-simple creates self-contained slash commands that orchestrate parallel task execution via Claude Code's Task Tool to transform user vision into reality.

## Foundation Principles

### Interview-Driven Development (IDD)
- Start with deep understanding of user vision
- Focus on possibilities over technical specifications
- Define clear success metrics from beginning
- Continuously adapt based on user insights

### Test-Driven Everything (TDE)
- Vision testing: Does result match user imagination?
- Quality testing: Do outputs meet success criteria?
- Workflow testing: Are objectives met efficiently?
- Evolution testing: Is system improving over time?

## Task Orchestration Architecture

### Command Hierarchy
1. **Slash Commands**: Orchestrate entire workflows
2. **Sub-agents**: Execute specific work via Task Tool
3. **Task Patterns**: Reusable orchestration strategies
4. **Result Processing**: Combine and synthesize outputs

### Core Patterns
- **7-Parallel-Tasks**: Component development pattern
- **Wave Deployment**: Sequential task phases
- **Git WorkTree**: Isolated parallel development
- **Batch Processing**: Group similar operations

## Strategic Deployment

### When to Use Parallel
- Independent operations (different files, searches)
- Multiple perspectives on same problem
- Time-sensitive work requiring speed
- Resource abundance situations

### When to Use Sequential
- Critical dependencies between tasks
- Resource constraints or limitations
- Shared state modifications required
- Quality gates requiring validation

## Living System Qualities

### Self-Healing
- Automatic error detection and correction
- Quality threshold maintenance
- Continuous improvement from failures
- Hallucination detection and prevention

### Transparency
- Real-time progress notifications
- Clear decision rationale
- Expected completion estimates
- Success metrics tracking

### Evolution
- Pattern library growth from usage
- Strategy optimization based on results
- User preference learning and adaptation
- System-wide architectural improvements

## Success Vision

### For Users
- Effortless power through simple interface
- Ideas become reality naturally
- Continuous support as needs evolve
- Complete transparency in operations

### For System
- Growing intelligence with each interaction
- Self-healing and self-optimizing operation
- Graceful handling of any complexity
- Sustainable growth without unwieldiness

---

**Core Commitment**: ce-simple remains simple to use, powerful in capability, transparent in operation, and sustainable in growth.

See principles-details.md for detailed specifications and implementation examples.