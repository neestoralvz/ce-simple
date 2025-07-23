# Task Orchestration

## Purpose
Patterns and strategies for orchestrating parallel task execution via Claude Code's Task Tool.

## Task Tool Architecture

### Command Hierarchy
- **Slash Commands**: Primary orchestrators that deploy sub-agents
- **Sub-Agents**: Workers created via Task Tool (up to 10 concurrent)
- **Task Patterns**: Proven orchestration strategies
- **Result Aggregation**: Combining outputs from parallel tasks

### Key Constraints
- Slash commands must be completely self-contained
- Sub-agents cannot spawn additional tasks
- Sub-agents cannot invoke other slash commands
- All task instructions must include complete context

## Core Orchestration Patterns

### 7-Parallel-Tasks Pattern
Optimal for component development:
1. Component logic
2. Styles/CSS
3. Tests
4. Type definitions
5. Utilities/hooks
6. Integration points
7. Documentation

Result: 7x speedup vs sequential development.

### Search Pattern
For information gathering:
- Deploy multiple search strategies in parallel
- Each sub-agent explores different areas
- Aggregate and synthesize results
- Remove duplicates and rank by relevance

### Analysis Pattern
For complex problem solving:
- Apply think layers concurrently
- Multiple perspectives on same problem
- Parallel hypothesis testing
- Synthesize insights from all analyses

### Wave Deployment
For multi-stage workflows:
1. **Discovery Wave**: Parallel exploration
2. **Analysis Wave**: Process findings
3. **Creation Wave**: Generate solutions
4. **Validation Wave**: Verify results

## Parallelization Guidelines

### When to Use Parallel
- Independent operations (different files, searches)
- Multiple perspectives needed
- Time-sensitive work
- Abundant resources available

### When to Use Sequential
- Tasks have critical dependencies
- Resource constraints exist
- Shared state modifications required
- Quality gates need validation checkpoints

## Result Processing

### Aggregation Strategies
- **Merge Similar**: Combine compatible outputs
- **Resolve Conflicts**: Handle contradictory results
- **Extract Patterns**: Identify successful approaches
- **Synthesize Insights**: Create unified understanding

### Quality Assurance
- Validate all task completions
- Check for contradictions
- Verify success criteria met
- Handle partial failures gracefully

## Success Metrics

### Performance Targets
- **7-Parallel-Tasks**: ~6x speedup vs sequential
- **Search Operations**: 10x faster information gathering
- **Analysis Tasks**: 4x more comprehensive insights
- **Overall Efficiency**: 85% improvement in workflow completion

### Quality Standards
- All tasks complete successfully
- Results are coherent and usable
- No information loss in aggregation
- Conflicts resolved intelligently

---

**Key Principle**: Task orchestration transforms single-threaded work into parallel execution while maintaining quality and coherence.

See orchestration-details.md for advanced techniques and implementation specifications.