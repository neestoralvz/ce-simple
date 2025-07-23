# /filter-results - Result Filtering & Refinement

**Purpose**: Orchestrate intelligent filtering and ranking of search results with relevance scoring, multi-criteria analysis, and quality optimization for enhanced information discovery.

**Category**: 13-search  
**Complexity**: Medium  
**Prerequisites**: Search results from /search-advanced or /discover-information

## Core Principles

**Single Responsibility**: Focus exclusively on result filtering orchestration with intelligent ranking algorithms and comprehensive quality analytics.

**Natural Language Orchestration**: Use Task tool to coordinate filtering operations through clear, actionable instructions without embedded scripting.

**Progressive Disclosure**: Maintain core filtering logic in this command while referencing detailed algorithm specifications in supporting documentation.

**Quality-First**: Prioritize result relevance and user value through sophisticated scoring algorithms and multi-dimensional analysis.

## Phase 1: Input Analysis

**Instruction**: Use Task tool to analyze input sources and prepare filtering environment.

Execute these parallel tasks through Task tool:

1. **Input Source Detection**: Identify input format (search results file, discovery reports, or auto-generated directory analysis). Auto-detect from /tmp/search_results_*, .discovery/discovery_report.md, or generate from current directory.

2. **Data Structure Analysis**: Parse input format (JSON, markdown, text) and extract metadata including file size, line count, format type, and content preview for filtering preparation.

3. **Quality Assessment**: Validate input data completeness and identify any structural issues that could affect filtering accuracy.

4. **Workspace Initialization**: Create .filter directory structure with input, processing, output, and analytics subdirectories for organized result management.

## Phase 2: Criteria Application

**Instruction**: Apply filtering criteria through Task tool coordination with intelligent weighting algorithms.

Configure these filtering operations:

1. **Primary Filter Selection**: Apply user-specified criteria (relevance, date, size, category, or custom) with appropriate threshold settings and algorithm selection.

2. **Relevance Scoring Algorithm**: Calculate composite scores using TF-IDF with context weighting, content quality metrics (0-30 points), recency factors (0-25 points), cross-reference analysis (0-25 points), and context relevance (0-20 points).

3. **Multi-Criteria Ranking**: Execute intelligent ranking mode with adaptive algorithms that consider content structure, modification dates, cross-references, and user context patterns.

4. **Threshold Application**: Apply quality thresholds with high relevance (70+ points), medium relevance (40-69 points), and low relevance (<40 points) classifications.

## Phase 3: Result Optimization

**Instruction**: Optimize filtered results through Task tool orchestration of advanced processing operations.

Execute these optimization processes:

1. **Duplicate Removal**: Identify and eliminate duplicate or near-duplicate results using content similarity analysis and structural comparison.

2. **Intelligent Grouping**: Group related results by topic, category, or functional similarity to improve organization and user navigation.

3. **Quality Enhancement**: Apply final quality filters, optimize result presentation format, and ensure readability thresholds are met.

4. **Ranking Finalization**: Sort results by composite scores, apply maximum result limits (default 25), and prepare for structured output generation.

## Phase 4: Output Generation

**Instruction**: Generate comprehensive reports and analytics through Task tool coordination.

Create these deliverables:

1. **Filtered Results Report**: Generate structured report with filtering summary, high-relevance results, medium-relevance results, and filtering analytics including average scores and distribution patterns.

2. **Analytics Dashboard**: Create performance metrics analysis covering processing efficiency, content quality insights, improvement opportunities, and system recommendations.

3. **Actionable Recommendations**: Provide next steps including result review guidance, content enhancement suggestions, and integration points with other search commands.

4. **Integration Outputs**: Prepare filtered results in formats compatible with /search-advanced expansion, /discover-information enhancement, and content quality improvement workflows.

## Phase 5: Command Routing and Handoff

**Instruction**: Implement intelligent workflow continuation based on filtering results and user context.

Determine optimal next steps:

1. **Result Quality Assessment**: If high-quality results found (70+ score), route to immediate use. If medium quality (40-69), suggest refinement. If low quality (<40), recommend content improvement.

2. **Search Expansion**: For insufficient results, recommend /search-advanced with refined query parameters or /discover-information for broader context gathering.

3. **Content Enhancement**: For low-scoring content identified, suggest specific improvement actions and integration with documentation maintenance workflows.

4. **Performance Optimization**: Based on filtering analytics, recommend /index-content for search performance improvement or additional filtering iterations with different criteria.

## Integration Framework

**Input Sources**: Search results from /search-advanced, discovery reports from /discover-information, directory analysis, or custom data sources  
**Output Formats**: Structured filtered results, analytics reports, performance metrics, and actionable recommendations  
**Cross-Category Enhancement**: Integrates with all workflow categories through refined information delivery and quality optimization

## Usage Patterns

**Standard Filtering**: Auto-detect input source, apply relevance criteria, return top 25 results with intelligent ranking  
**Temporal Filtering**: Filter by modification dates and recency with priority on recently updated content  
**Category-Based**: Organize results by content type (commands, documentation, configuration) with appropriate weighting  
**Custom Criteria**: Apply user-defined filtering parameters with flexible threshold configuration

---

*Result filtering orchestration with intelligent ranking algorithms and comprehensive quality analytics for optimal information discovery and workflow enhancement*