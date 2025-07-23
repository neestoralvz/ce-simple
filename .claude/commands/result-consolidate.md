# Result Consolidate - Documentation Command

## Purpose
Results integration and reporting for agent orchestration. Collects outputs from multiple agents, synthesizes findings, and generates consolidated documentation.

## Principles and Guidelines

**Single Responsibility**: Focus exclusively on result consolidation without agent management or deployment
**Granular Synthesis**: Break consolidation into small, manageable synthesis steps
**Documentation Management**: Clear quality standards with explicit validation requirements
**Error Recovery**: Built-in consolidation failure handling and data validation protocols

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

---

**Single Responsibility**: Documentation focused exclusively on result consolidation and synthesis from multiple agent sources.**