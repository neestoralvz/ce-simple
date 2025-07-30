# Template: Workflow Commands

**Template última edición: 29/07/2025** | Template for /workflows: process and sequence commands

## Workflow Command Structure

```markdown
# /workflows:name - [Workflow Function]

**DD/MM/YYYY** | [Workflow purpose]

## DO
- [Primary workflow coordination 1]
- [Primary workflow coordination 2]
- [When to EXECUTE /methodology:specific]
- [Process completion criteria]

## DON'T
- [Workflow scope violation 1]
- [Workflow scope violation 2]
- [Common process mistakes to avoid]
- [Anti-patterns that break workflow continuity]

## Context
- [Process state requirements and tracking]
- [Integration points with other workflows]
- [Authority sources for workflow behavior]
- [Dependencies and prerequisites]

## Next Action
- **Automatic**: /next:workflow (when process completion triggers clear next workflow)
- **Recommended**: /suggested:action (when user choice optimal for continuation)
- **Context**: Session state vs individual task completion
```

## Workflow Categories

### Session Management (start, close)
**Purpose**: Manage session lifecycle, continuity, and state transitions

**DO Pattern**:
- Maintain session state and context continuity
- Apply systematic handoff and documentation protocols
- Integrate with planning and progress tracking systems
- Ensure smooth transitions between sessions

**DON'T Pattern**:
- Start or close sessions without proper state management
- Skip documentation of session progress and outcomes
- Break continuity between session boundaries
- Ignore planning integration requirements

### Investigation/Analysis (explore, debug)
**Purpose**: Systematic investigation, problem-solving, and analysis processes

**DO Pattern**:
- Apply systematic methodology for investigation
- Use appropriate tools and techniques for analysis
- Document findings and maintain investigation traceability
- Provide actionable insights and recommendations

**DON'T Pattern**:
- Investigate without systematic approach or methodology
- Skip documentation of investigation process and findings
- Provide analysis without clear actionable outcomes
- Lose context or fail to maintain investigation continuity

### Content Processing (distill)
**Purpose**: Transform, synthesize, and process information systematically

**DO Pattern**:
- Preserve essential information during processing
- Apply appropriate methodology for content transformation
- Maintain traceability between source and processed content
- Validate processing quality and completeness

**DON'T Pattern**:
- Process content without clear transformation criteria
- Lose critical information during processing operations
- Skip quality validation of processed content
- Create output that lacks clear relationship to source

## Context Section Guidelines

### For Session Management
```markdown
## Context
- context/planning/current.md (for session state)
- Previous session handoffs and documentation
- System state and configuration requirements
- Integration with git and documentation systems
```

### For Investigation/Analysis
```markdown
## Context
- Investigation target and scope definition
- Available analysis tools and methodologies
- Previous investigation results and patterns
- System knowledge base and documentation
```

### For Content Processing
```markdown
## Context
- Source content location and characteristics
- Processing methodology and quality criteria
- Output requirements and format specifications
- Integration with documentation and filing systems
```

## Next Action Patterns

### Process-Completion Automatic
```markdown
## Next Action
- **Automatic**: /workflows:close (after completing session work)
- **Automatic**: /actions:git (after generating content requiring commit)
- **Automatic**: /workflows:related (when process triggers related workflow)
```

### Investigation-Result Recommended
```markdown
## Next Action
- **Recommended**: /actions:build (to document investigation findings)
- **Recommended**: /roles:partner (for validation of analysis results)
- **Alternative**: /workflows:debug (if issues discovered during investigation)
```

### Context-Sensitive Routing
```markdown
## Next Action
- **If session workflow**: Continue with session management sequence
- **If investigation complete**: Route to appropriate action based on findings
- **If processing complete**: Route to validation or continuation workflow
```

## Template Usage Instructions

1. **Identify workflow category** (session/investigation/processing)
2. **Define process boundaries** and completion criteria clearly
3. **Customize DO/DON'T** sections for workflow's specific coordination needs
4. **Map Context dependencies** and integration requirements
5. **Design Next Action** logic for smooth workflow transitions

---
**Authority Source**: Workflow command analysis + process coordination patterns
**Template References**: context/templates/universal_do_dont_template.md