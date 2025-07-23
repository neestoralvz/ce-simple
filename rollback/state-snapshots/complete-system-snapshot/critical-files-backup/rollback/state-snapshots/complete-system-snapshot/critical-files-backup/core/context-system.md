# Context & Memory System

## Purpose
Distributed context architecture using minimal central storage, dynamic loading, and Git as persistent memory.

## Context Philosophy

### Cognitive Load Optimization
- Conductor holds only critical decisions
- Sub-agents load context on-demand
- Context files store reusable knowledge
- Git preserves everything permanently

### Asynchronous State Management
Every execution rebuilds state from Git since there's no persistent runtime between invocations.

## Context Layers

### Conductor Context (Minimal Core)
- Current workflow state
- Active task registry
- Critical decisions made
- Next actions queued

Target: <1000 tokens, updated at decision points.

### Task Working Context
- Search results and patterns
- Analysis findings
- Creation progress tracking
- Validation outcomes

Dynamic loading based on task needs.

### Persistent Context Files
- Discovered patterns and insights
- Successful strategies and approaches
- Project-specific knowledge
- Cross-session learnings

Organized in context/ directory structure.

### Git Memory Layer
- Complete execution history
- Decision audit trails
- Pattern evolution tracking
- Performance metrics over time

## Context Organization

### Directory Structure
```
context/
├── discoveries/     # Found patterns and insights
├── patterns/        # Successful approaches  
├── research/        # External knowledge
├── workflows/       # Process documentation
└── notes/          # Miscellaneous learnings
```

### File Naming Patterns
- Session-based: `topic-YYYYMMDD.md`
- Discovery-based: `discovery-description.md`
- Pattern-based: `pattern-name.md`
- Research-based: `research-topic.md`

## Context Flow Patterns

### Discovery to Context
1. Execute search/analysis tasks
2. Extract patterns from results
3. Create context files for reuse
4. Commit to Git for persistence

### Context to Action
1. Load relevant context files
2. Apply patterns to current situation
3. Make informed decisions
4. Update context with new learnings

### Cross-Session Continuity
1. Git history provides complete context
2. Context files enable quick restoration
3. TodoWrite maintains workflow state
4. Patterns guide consistent approaches

## Memory Optimization

### Selective Loading
Load only context relevant to current task:
- Recent discoveries for similar problems
- Successful patterns for current domain
- Project-specific accumulated knowledge
- User preferences and customizations

### Context Synthesis
Combine multiple context sources:
- Merge related discoveries
- Extract common patterns
- Identify successful strategies
- Build comprehensive understanding

### Garbage Collection
Regularly clean up context:
- Archive old discoveries
- Consolidate similar patterns
- Remove obsolete information
- Maintain optimal context density

## Success Indicators

### Context Effectiveness
- Faster problem resolution with accumulated knowledge
- Consistent application of successful patterns
- Reduced repetition of previous mistakes
- Improved decision quality over time

### Memory Efficiency
- Minimal conductor context load
- Fast context file loading
- Effective pattern reuse
- Clean Git history navigation

---

**Key Principle**: Context system balances minimal cognitive load with maximum available knowledge, using Git as perfect recall mechanism.

See context-system-details.md for advanced techniques and implementation specifications.