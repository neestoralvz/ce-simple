# Enhanced Start - Discovery Command

## Purpose
Discovery command with structural validation, conditional agent deployment, and parallel orchestration for comprehensive investigation and maximum efficiency.

## Principles and Guidelines

**Single Responsibility**: Focus exclusively on enhanced discovery without execution or implementation
**Granular Discovery**: Break investigation into small, manageable discovery steps
**Assessment Management**: Clear complexity thresholds with explicit deployment requirements
**Error Recovery**: Built-in discovery failure handling and re-assessment protocols

## Execution Process

### Phase 1: Structure Validation and Assessment
Update TodoWrite: Mark "Enhanced discovery structure validation" as in_progress

Validate system structure and readiness:
- Use LS tool to check docs/ directory exists and is accessible
- Use LS tool to verify commands/ directory structure and contents
- Use LS tool to confirm context/ directory presence and organization
- Validate system integrity before proceeding with discovery

Calculate discovery complexity using embedded formula:
```bash
scope=$(analyze_request_scope)
breadth=$(count_domains) 
interdep=$(analyze_dependencies)
complexity=$(echo "scale=1; ($scope + $breadth + $interdep) / 3" | bc)
```

Assess discovery requirements:
- Determine scope depth and investigation breadth
- Identify domain expertise requirements
- Evaluate interdependency complexity factors
- Calculate deployment strategy based on complexity score

### Phase 2: Conditional Agent Deployment
Update TodoWrite: Complete previous, mark "Conditional agent deployment" as in_progress

Deploy agents based on complexity assessment:
- If complexity ≥6: Use Task Tool executing `/worktree-start` for isolation setup
- If learning value ≥4: Use Task Tool executing `/capture-learnings` for knowledge extraction
- If multi-domain detected: Use Task Tool executing `/explore-codebase` for internal analysis
- If multi-domain detected: Use Task Tool executing `/explore-web` for external research

Execute parallel deployment coordination:
- Deploy Task Tools simultaneously for maximum efficiency
- Monitor agent startup and initialization status
- Validate successful deployment before proceeding
- Handle deployment failures with retry mechanisms

### Phase 3: Discovery Coordination and Monitoring
Update TodoWrite: Complete previous, mark "Discovery coordination and monitoring" as in_progress

Coordinate parallel discovery execution:
- Monitor Task Tool agent progress and status
- Track discovery completion across deployed agents
- Coordinate inter-agent communication and dependencies
- Handle agent coordination issues and bottlenecks

Collect intermediate discovery results:
- Gather partial findings from active agents
- Validate discovery quality and completeness
- Identify gaps requiring additional investigation
- Adjust discovery strategy based on intermediate results

### Phase 4: Result Aggregation and Validation
Update TodoWrite: Complete previous, mark "Discovery result aggregation" as in_progress

Aggregate discovery findings:
- Collect outputs from all deployed Task Tool agents
- Synthesize findings with pattern extraction and analysis
- Resolve conflicts between different agent discoveries
- Generate comprehensive discovery summary

Validate discovery completion using systematic checks:
```bash
total_scope=$(calculate_total_scope)
covered_scope=$(get_covered_scope)
completeness=$(echo "scale=1; $covered_scope * 100 / $total_scope" | bc)
```

Perform completion validation:
- Verify request fulfilled completely (≥95% scope coverage)
- Confirm all Task Tool agents completed successfully
- Validate learning patterns captured and documented
- Check system integrity maintained (completeness ≥85%)

If discovery validation fails:
- Add TodoWrite task: "Resolve discovery gap: [specific issue]"
- Re-deploy agents with enhanced discovery protocols
- Recalculate complexity using refined assessment parameters
- Re-execute discovery phases with adjusted scope and strategy

Update TodoWrite: Complete all enhanced discovery tasks
Add follow-up: "Enhanced discovery complete with comprehensive findings ready"

---

**Single Responsibility**: Discovery focused exclusively on enhanced investigation with conditional agent deployment and parallel orchestration optimization.**