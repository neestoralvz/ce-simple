# Claude Code Integration Component

**30/07/2025 11:30 CDMX** | Claude Code-specific methodologies and patterns

## Component Purpose

Specialized integration layer for Claude Code CLI capabilities, methodologies, and operational patterns. This component bridges user vision with Claude Code's specific tools, behaviors, and execution patterns.

**Core Function**: Translate user vision into Claude Code-optimized workflows while preserving conversation-first development philosophy.

## Content Categorization

### `/roles/`
**Purpose**: Claude Code-specific role definitions and behavioral patterns
**Content**: Role templates, behavioral specifications, execution protocols
**Example**: Partner constructor for Claude Code environments, Guardian patterns for CLI contexts

### `/methodology/`
**Purpose**: Claude Code-optimized execution methodologies
**Content**: Tool orchestration patterns, CLI-specific workflows, execution optimization techniques
**Example**: Multi-tool parallel execution, WebSearch + MCP integration patterns

### `/actions/`
**Purpose**: Atomic Claude Code action definitions
**Content**: Specific tool invocations, parameter patterns, execution sequences
**Example**: Research actions, file manipulation patterns, git workflow actions

### `/command-creation/`
**Purpose**: Methodology for creating Claude Code-optimized commands
**Content**: Command structure patterns, tool integration guidelines, validation protocols
**Example**: Command templates that leverage Claude Code's concurrent capabilities

### `/orchestration/`
**Purpose**: Multi-conversation and parallel execution orchestration
**Content**: Coordination patterns, state management, inter-conversation communication
**Example**: Git worktree-based parallel execution, background process management

### `/conversation-patterns/`
**Purpose**: Claude Code conversation flow optimization
**Content**: Dialogue patterns, user interaction optimization, natural conversation preservation
**Example**: Socratic discovery adapted for Claude Code capabilities

## Integration Points

### ↑ TRUTH_SOURCE.md
**Authority Source**: Supreme authority context drives all Claude Code methodologies
**Connection**: All Claude Code methodologies validate against supreme authority context
**Protocol**: Claude Code optimizations must preserve user vision and authority hierarchy

### ←→ /methodology.md
**Connection**: Claude Code-specific implementations of core methodology patterns
**Protocol**: Specialized adaptations of Think x4, Research-First, Continuous Execution

### ←→ /patterns.md
**Connection**: Claude Code tool usage patterns and orchestration frameworks
**Protocol**: Tool-specific implementations of architectural and behavioral patterns

### → /.claude/commands/
**Connection**: Implementation target for Claude Code methodologies
**Protocol**: Methodologies inform command creation and optimization

### → architecture/standards/
**Connection**: Claude Code tool compliance and technical standards alignment
**Protocol**: Tool usage patterns must comply with architectural standards and quality gates

## Evolution Guidelines

### Organic Growth Triggers
- **User feedback on Claude Code performance** → methodology refinement
- **New Claude Code capabilities** → integration pattern development
- **Efficiency discoveries** → pattern documentation
- **Multi-conversation usage** → orchestration pattern evolution

### Content Addition Criteria
1. **Claude Code Specificity**: Content must leverage Claude Code unique capabilities
2. **User Vision Alignment**: All methodologies serve conversation-first development
3. **Practical Application**: Patterns must emerge from actual usage, not theoretical design
4. **Authority Preservation**: User authority supremacy maintained in all Claude Code adaptations

### Semantic Placement Decision Tree
**Is it Claude Code-specific?** → Yes: Place in claude_code/
**Does it involve tool orchestration?** → orchestration/ or methodology/
**Is it a reusable action pattern?** → actions/
**Does it define behavioral roles?** → roles/
**Is it about command creation?** → command-creation/
**Does it optimize conversation flow?** → conversation-patterns/

---

**Authority Chain**: VISION.md → TRUTH_SOURCE.md → claude_code/ component → specialized implementations
**Evolution Protocol**: Empirical discovery → pattern documentation → methodology integration → command optimization