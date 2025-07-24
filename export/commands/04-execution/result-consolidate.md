# Result Consolidate - Execution Command

## Purpose
Integrates and synthesizes outputs from multiple agents through parallel collection, analysis, and documentation generation with quality validation and comprehensive reporting capabilities.

## Principles and Guidelines

- **Single Responsibility**: Focus exclusively on result consolidation without handling agent deployment or monitoring tasks
- **Granular Consolidation**: Break consolidation workflows into small, manageable synthesis phases with clear validation steps
- **Documentation Management**: Clear result dependencies with explicit integration requirements and quality checkpoints
- **Error Recovery**: Built-in consolidation failure handling and recovery protocols with partial result processing

## Execution Process

### Phase 1: Agent Result Collection
Update TodoWrite: Mark "Agent result collection" as in_progress

Collect results from multiple agents:
- Gather all agent outputs with complete metadata tagging
- Organize results by agent type and execution phase
- Validate result completeness against expected outputs
- Handle missing or incomplete agent outputs with fallbacks

Use Read tool for result collection:
- Read agent output files and execution logs
- Extract key findings and data points
- Organize results by agent type and responsibility
- Validate data integrity and completeness

Generate collection inventory:
- Document agent result count and completion status
- Record result quality assessment scores
- Identify missing data and incomplete outputs
- Confirm collection validation and readiness

### Phase 2: Result Analysis and Synthesis
Update TodoWrite: Complete previous, mark "Result synthesis and analysis" as in_progress

Analyze result relationships and patterns:
- Examine connections between agent findings
- Identify recurring themes and patterns
- Resolve conflicts and inconsistencies between agents
- Generate unified insights from distributed findings

Synthesize findings into coherent narrative:
- Apply thematic organization to agent findings
- Implement cross-reference validation between results
- Resolve conflicts through evidence weighting
- Ensure narrative coherence and logical flow

### Phase 3: Documentation Generation
Update TodoWrite: Complete previous, mark "Consolidated documentation generation" as in_progress

Generate structured results documentation:
- Create executive summary of consolidated findings
- Develop detailed agent contribution breakdown
- Build cross-referenced insights and pattern analysis
- Prepare appendices with organized raw agent outputs

Use Write tool for documentation creation:
- Write comprehensive consolidation report
- Generate summary with key findings and recommendations
- Create detailed analysis section with synthesis insights
- Document sources with agent contributions and metadata

### Phase 4: Quality Assurance and Validation
Update TodoWrite: Complete previous, mark "Documentation quality validation" as in_progress

Validate consolidated documentation:
- Verify result accuracy against source agent data
- Check cross-reference integrity and consistency
- Confirm narrative coherence and logical flow
- Validate source attribution and metadata accuracy

Perform final quality checks:
- Review documentation completeness and coverage
- Validate synthesis quality and insight generation
- Confirm adherence to documentation standards
- Test cross-references and validation links

If consolidation issues detected:
- Add TodoWrite task: "Resolve consolidation issue: [specific problem]"
- Implement data recovery or synthesis correction
- Validate resolution before final documentation
- Document issue resolution for future reference

Update TodoWrite: Complete all result consolidation tasks
Add follow-up: "Consolidated documentation ready for delivery"

**Single Responsibility**: Result consolidator focused exclusively on multi-agent output integration without deployment or monitoring responsibilities.