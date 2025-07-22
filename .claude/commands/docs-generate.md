# Docs Generate - Todo Plans to Documentation Creation

## 🎯 Purpose
Convert todo list plans into structured Markdown documentation through parallel agent deployment and 3-wave execution strategy.

## 🚀 Usage
Execute: `/docs-generate [scope]`

## 🔧 Implementation

### Behavioral Reinforcement Protocol
**MANDATORY at generation initialization**:

```javascript
TodoWrite([
  {"content": "📋 ANALYSIS: Analyze todo plans and validate documentation requirements", "status": "pending", "priority": "high", "id": "generate-analysis-1"},
  {"content": "🚀 WAVE1: Execute parallel agent deployment for document creation", "status": "pending", "priority": "high", "id": "generate-wave1-1"},
  {"content": "🔗 WAVE2: Build comprehensive cross-reference integration network", "status": "pending", "priority": "high", "id": "generate-wave2-1"},
  {"content": "✅ WAVE3: Execute quality validation with comprehensive audit", "status": "pending", "priority": "medium", "id": "generate-wave3-1"},
  {"content": "🔄 RECOVERY: Monitor and execute error recovery with targeted corrections", "status": "pending", "priority": "medium", "id": "generate-recovery-1"}
])
```

**Wave-Progressive Todos**: Add stage-specific todos as each wave completes with quality gate validation

### Execution Framework
**3-Wave Strategy**: Parallel creation → Cross-reference integration → Quality validation

**Core Protocol**:
1. **WAVE 1**: Deploy specialized agents per document (parallel execution)
2. **WAVE 2**: Build bidirectional cross-reference network
3. **WAVE 3**: Execute comprehensive quality validation with `/docs-audit`

**Progress Tracking**: Real-time notifications with agent status, completion metrics, and quality gates

**Error Recovery**: Automatic failure detection with targeted correction agents and retry logic

## ⚡ Triggers

### Input Triggers
**Context**: Todo lists containing documentation creation plans
**Previous**: `/start` → documentation workflow detection → `/docs-generate`
**Keywords**: generate, create, documentation, todo, plans

### Output Triggers
**When**: Generation complete → `/docs-audit` for quality validation
**When**: Quality issues → Recursive correction with targeted agents
**When**: Success achieved → Documentation ready for integration
**Chain**: generate → validate → (correct if needed) → complete

### Success Patterns
**Generation Success**: All documents created with template compliance
**Integration Success**: Cross-reference network established with >99% accuracy
**Quality Success**: Combined score ≥85% with no critical failures

## 🔗 See Also

### Implementation Details
- `../docs/implementation/docs-generate-implementation.md` - Complete 3-wave execution framework and integration protocols

### Related Commands
- Execute `/docs-workflow` for complete documentation optimization pipeline
- Execute `/docs-audit` for comprehensive quality assessment and validation
- Execute `/start` for discovery workflow and systematic analysis
- Execute `/think-layers` for complex plan analysis and optimization strategies

### System Integration
- Integrates with `/docs-workflow` as Phase 0 generation step
- Uses `/docs-audit` for quality validation and metrics assessment
- Follows standards for LLM-optimized documentation creation
- Implements anti-bias protocols for neutral content generation

---

## ⚡ EXECUTION LAYER

### Mandatory Tool Executions
**CRITICAL**: Actual implementation of 3-wave documentation generation system

```javascript
// 3-WAVE DOCUMENTATION GENERATION SYSTEM
// Convert todo plans to structured documentation

// WAVE 1: PARALLEL DOCUMENT CREATION
// Deploy specialized agents for document generation

// Todo plan analysis and validation
Grep("TODO|todo|plan|create|generate", {glob: "context/**/*.md", output_mode: "content", -C: 2}) // Find todo plans
Bash("find context/ -name '*todo*' -o -name '*plan*' | head -10")                             // Locate plan files

// Document structure template preparation
Write("context/discoveries/generation-templates-[timestamp].md", `# Document Generation Templates

## Standard Document Structure
\`\`\`markdown
# [Title] - [Subtitle]

## 🎯 Purpose
[Clear purpose statement]

## 🚀 Usage
Execute: \`/command-name [parameters]\`

## 🔧 Implementation
[Implementation details]

## ⚡ Triggers
[Input/output triggers]

## 🔗 See Also
[Related references]

---
**CRITICAL**: [Closing statement]
\`\`\`

## Agent Deployment Strategy
[Parallel agent assignments]
`)

// WAVE 1: PARALLEL AGENT DEPLOYMENT
// Deploy multiple agents for concurrent document creation
Task("Document Generator 1", "Generate [document-type-1] based on todo requirements with standard template compliance")
Task("Document Generator 2", "Generate [document-type-2] based on todo requirements with standard template compliance") 
Task("Document Generator 3", "Generate [document-type-3] based on todo requirements with standard template compliance")
Task("Document Generator 4", "Generate [document-type-4] based on todo requirements with standard template compliance")

// WAVE 2: CROSS-REFERENCE INTEGRATION NETWORK
// Build comprehensive bidirectional reference system

// Reference mapping and integration
Grep("See Also|Related|Integration|Chain", {glob: "**/*.md", output_mode: "content", -n: true}) // Existing references
Task("Reference Integrator 1", "Build cross-reference network between generated documents and existing system")
Task("Reference Integrator 2", "Validate bidirectional links and ensure navigation completeness")

// Cross-reference validation
Write("context/discoveries/cross-reference-network-[timestamp].md", `# Cross-Reference Network Integration

## Generated Documents
[List of newly created documents]

## Integration Points
[Connection points with existing system]

## Bidirectional Link Validation
[Verification of two-way navigation]

## Navigation Efficiency Assessment
[Cognitive steps and accessibility metrics]
`)

// WAVE 3: QUALITY VALIDATION AND AUDIT
// Comprehensive quality assurance through audit

// Deploy docs-audit for quality assessment
Task("Quality Validator", "Execute /docs-audit on generated documents for comprehensive quality assessment")

// Generation quality metrics
Bash("find . -name '*.md' -newer context/discoveries/generation-templates-[timestamp].md | wc -l") // Count new files
Bash("find . -name '*.md' -newer context/discoveries/generation-templates-[timestamp].md -exec wc -l {} + | tail -1") // Total lines

// ERROR RECOVERY AND CORRECTION
// Monitor generation quality and deploy corrections

Grep("ERROR|BROKEN|INCOMPLETE|FIXME", {glob: "**/*.md", output_mode: "files_with_matches", head_limit: 10}) // Error detection
Task("Error Recovery Agent", "Identify and correct any generation errors or quality issues in created documents")

// GENERATION RESULTS DOCUMENTATION
Write("context/discoveries/generation-results-[timestamp].md", `# Documentation Generation Results

## Wave 1: Document Creation
- Documents Generated: [generated_count]
- Template Compliance: [compliance_percentage]%
- Agent Deployment: [agent_count] parallel agents
- Creation Efficiency: [creation_time]

## Wave 2: Cross-Reference Integration
- References Created: [reference_count]
- Bidirectional Links: [bidirectional_count]
- Navigation Paths: [navigation_paths]
- Integration Success: [integration_percentage]%

## Wave 3: Quality Validation
- Audit Score: [audit_score]/100
- Quality Gates Passed: [gates_passed]/[total_gates]
- Error Recovery Actions: [recovery_actions]
- Final Quality Score: [final_quality_score]%

## Generation Metrics
- Todo Conversion Rate: [conversion_percentage]%
- Standards Compliance: [standards_compliance]%
- System Integration: [system_integration]%
- Overall Success: [overall_success]%

## Error Recovery Summary
[Details of any corrections applied]

## Recommendations
[Suggestions for process improvement]
`)

// LEARNING VALUE ASSESSMENT
// Evaluate generation complexity for learning capture
Bash("echo 'scale=1; ([generation_complexity] + [agent_count] + [quality_issues]) / 3' | bc") // Learning value calculation
Task("Learning Assessment", "Evaluate generation learning value: if complexity ≥4 points, trigger /capture-learnings")
```

### 3-Wave Execution Strategy
**WAVE 1 - CREATION**: Parallel document generation with template compliance
**WAVE 2 - INTEGRATION**: Cross-reference network building with bidirectional validation
**WAVE 3 - VALIDATION**: Quality audit with error recovery and correction

### Agent Deployment Logic
**PARALLEL EFFICIENCY**:
- Deploy 4 specialized document generators simultaneously
- Deploy 2 reference integrators for network building
- Deploy 1 quality validator + 1 error recovery agent
- **Total**: 8 agents with coordinated execution

### Quality Gate Framework
**VALIDATION CRITERIA**:
- Template compliance >95%
- Cross-reference integrity 100%
- Audit score ≥85
- Error recovery success 100%

### Session Completion Protocol
**MANDATORY WORKFLOW END**:
```javascript
// Git automation with generation metrics
Bash("git add . && git commit -m \"docs-generate: 3-wave | docs: [N] | quality: [score]% ✓session-[N]\"")
```

### Execution Verification
**TOOL CALL AUDIT**:
- **Planning**: 2 Grep + 1 Bash + 1 Write operations for setup
- **Wave 1**: 4 Task operations for parallel document creation
- **Wave 2**: 1 Grep + 2 Task + 1 Write operations for integration
- **Wave 3**: 1 Task + 2 Bash operations for validation
- **Recovery**: 1 Grep + 1 Task operations for error correction
- **Documentation**: 1 Write operation for results
- **Learning**: 1 Bash + 1 Task operations for assessment
- **Ratio**: 18 tool calls to ~75 documentation lines = 24% (HEALTHY)

---

**CRITICAL**: This command specializes in todo-to-docs conversion and integrates seamlessly with existing documentation workflow for complete optimization pipeline.

**EXECUTION COMMITMENT**: 3-wave documentation generation with parallel creation, cross-reference integration, and quality validation are NOW implemented with actual tool calls.