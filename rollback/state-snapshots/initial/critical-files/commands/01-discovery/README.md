# 01-discovery - Discovery & Research Commands

## Purpose
Intelligent information gathering and context discovery. These commands explore codebases, web resources, and problem spaces to build comprehensive understanding before planning or execution.

## Commands
- `/explore-codebase` - Internal project analysis and mapping
- `/explore-web` - External research and information gathering
- `/context-scan` - Rapid context assessment and profiling
- `/dependency-map` - Dependency analysis and visualization
- `/requirement-extract` - Automatic requirement identification

## Category Relations
- **Triggered by**: 00-core (start commands)
- **Feeds into**: 02-planning, 03-analysis
- **Uses**: 13-search for information retrieval
- **Coordinates with**: 14-utils for data processing

## Usage Patterns
```
00-core/start → 01-discovery/explore → 02-planning/architect
13-search/query → 01-discovery/context-scan → 03-analysis/assess
01-discovery/dependency-map → 05-validation/check → 04-execution/implement
```

## Discovery Methodology
- **Phase 0**: Initial context assessment
- **Phase 1**: Deep exploration and mapping
- **Phase 2**: Requirement extraction and validation
- **Phase 3**: Integration with planning systems

## Information Sources
- Internal: Codebase, documentation, configuration
- External: Web research, API documentation, standards
- Dynamic: User interaction, clarification questions
- Historical: Previous sessions, learned patterns

## Output Formats
- Structured context maps
- Dependency graphs
- Requirement matrices
- Discovery reports with actionable insights

---
*Category 01: Foundation for informed decision-making*