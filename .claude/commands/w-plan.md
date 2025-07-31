# w-plan - Investigation & Planning with Think x4

**31/07/2025 00:00 CDMX** | Investigation + systematic planning workflow

## Command Purpose
Execute investigation workflow (online research + MCP integration) + planning workflow (Think x4 analysis + step-by-step design) to create actionable execution plans.

**LOAD:** @context/architecture/core/methodology.md

## Execution Protocol

### Phase 1: Investigation Activation
**Authority**: `discovery_execution_flow.md:36-49`
**Behavior**: Research external solutions + best practices
**Method**:
- **Parallel WebSearch OBLIGATORIO**: Multiple concurrent searches for solutions, best practices, success cases
- **MCP TextEven integration**: Use specialized search when available
- **Solution synthesis**: Compile options and evidence-based recommendations
- **Research-informed guidance**: Continue conversation with external knowledge integration

### Phase 2: Think x4 Planning
**Authority**: `discovery_execution_flow.md:51-64`
**Behavior**: Systematic analysis + structured plan design
**Method**:
- **Information analysis**: Think x4 OBLIGATORIO systematic analysis on all gathered information
- **4 perspectives required**: Analyze from 4 different viewpoints before decisions
- **Evidence-based methodology**: All planning decisions backed by research + discovery
- **Step-by-step design**: Create detailed plan with specific, measurable steps

### Phase 3: Multi-Conversation Analysis
**Authority**: `discovery_execution_flow.md:66-80`
**Behavior**: Conversation division for parallel execution
**Method**:
- **Conversation breakdown**: Analyze which parts can be parallel vs sequential
- **Prompt crafting**: Generate specific conversation starters for each execution thread
- **Orchestrator consideration**: Identify where each conversation can deploy orchestrators
- **Power multiplication**: Design for Conversation → Orchestrator → Subagents hierarchy

## Think x4 Integration Protocol
**OBLIGATORIO**: Apply 4-perspective analysis to:
1. **Perspective 1**: Technical feasibility and implementation complexity
2. **Perspective 2**: User value and business impact
3. **Perspective 3**: Resource requirements and timeline considerations  
4. **Perspective 4**: Risk assessment and failure modes

## Task Tool Integration
**When to delegate**: If investigation requires specialized research domains or complex analysis
**Research Template**:
```
Task(
  description: "Research investigation",
  prompt: "Act as research specialist. Load context from @context/architecture/claude_code/orchestration_protocols.md. Conduct systematic investigation using Think x4 methodology. Focus on [specific domain]. Provide insights and recommendations.",
  subagent_type: "general-purpose"
)
```

## Output Structure
### Investigation Results
- **Solutions found**: Documented options with sources
- **Best practices identified**: Industry standards and recommendations
- **Success cases**: Real-world implementation examples
- **Risk factors**: Potential challenges and mitigation strategies

### Planning Results  
- **Think x4 Analysis**: 4-perspective systematic analysis
- **Step-by-step plan**: Detailed, measurable implementation steps
- **Conversation breakdown**: Parallel vs sequential execution threads
- **Conversation starters**: Ready-to-use prompts for execution phase

## Usage Pattern
```
w-plan
```
(Requires completed `w-start` for context)

Investigation + Think x4 analysis → Structured plan → Conversation division → Ready for `w-execute`

## Success Criteria
- **Evidence-based plan**: All decisions backed by research + systematic analysis
- **Think x4 compliance**: 4-perspective analysis applied to all major decisions
- **Parallel execution ready**: Clear conversation breakdown for maximum efficiency
- **Measurable steps**: Each plan element has specific success criteria