# Foundation Command Patterns - ce-simple

**Last Updated: 2025-07-23**

## Purpose

Extract and document proven command patterns from export/commands analysis for building high-quality, PTS-compliant commands. Based on analysis of 86 existing commands with focus on salvageable foundation elements.

## Quality Analysis Summary

From export/commands analysis:
- **✅ High Quality**: ~15% (e.g., root-level `explore-codebase.md`, `init-project.md`)
- **⚠️ Medium Quality**: ~25% (some 00-core commands with good structure)  
- **❌ Low Quality**: ~60% (over-orchestrated numbered directory commands)

## Proven Foundation Patterns

### Pattern 1: Simple Standalone Command (GOLD STANDARD)
**Source**: `/explore-codebase.md` (root level) - **Score: 8/10 PTS**

```markdown
# Command Name - Brief Description

## Purpose
Clear statement of single responsibility

## Principles and Guidelines  
- Primary PTS components relevant to command
- Key behavioral principles
- Integration guidelines

## Execution Process
Sequential phases with clear objectives
Each phase focused on specific outcome

## Implementation Standards
- Single Responsibility definition
- Tool usage specifications  
- Error handling approach
- Success criteria
```

**Key Success Elements**:
- Direct tool usage without orchestration overhead
- Specific error handling with recovery steps
- Clear 3-phase approach
- Practical scope limitation

### Pattern 2: Enhanced Structured Command
**Source**: `/init-project.md` (root level) - **Score: 9/10 PTS**

```markdown
# Command Name - Enhanced Description

## Purpose
Extended capability statement

## Principles and Guidelines
- Core PTS components + specific enhancements
- Behavioral principles for complexity management
- Clear integration boundaries

## Execution Process

### Phase 1: Validation and Setup
[Specific validation steps]

### Phase 2: Core Implementation  
[Primary functionality execution]

### Phase 3: Verification and Completion
[Success confirmation and cleanup]

## Error Handling Framework
ERROR: [Specific error description]
CAUSE: [Root cause identification]  
IMPACT: [Effect on workflow]
RECOVERY: [Specific recovery steps]
CONTINUE: [How to proceed]

## Implementation Standards
- Single Responsibility: [Specific definition]
- Tool Usage: [Exact tool specifications]
- Validation: [Success criteria]
- Authority: [Reference to governing documents]
```

**Key Success Elements**:
- Comprehensive error handling with specific recovery
- Clear phase separation without over-orchestration
- Direct tool integration
- Authority references

### Pattern 3: Balanced Multi-Phase Command
**Source**: `/start.md` (root level) - **Score: 7/10 PTS**

```markdown
# Command Name - Progressive Enhancement

## Purpose
Core capability with progressive enhancement options

## Prerequisites
- Basic requirements (keep minimal)
- Context assumptions

## Principles and Guidelines
- Progressive enhancement approach
- Fallback strategies built-in
- User choice preservation

## Execution Process

### Core Workflow (Always Execute)
[Essential functionality]

### Enhanced Workflow (When Applicable)  
[Extended features based on detection]

### Expert Options (When Requested)
[Advanced capabilities]

## Implementation Standards
- Graceful degradation maintained
- User control preserved
- Clear capability communication
```

**Key Success Elements**:
- Progressive enhancement without complexity explosion
- User agency maintained
- Clear capability communication
- Practical fallback strategies

## Anti-Patterns to Avoid

### Anti-Pattern 1: Over-Orchestration (60% of existing commands)
**Problems**:
- Excessive TodoWrite usage creating noise
- Multiple redundant validation phases  
- Meta-descriptions without practical value
- Complex phase transitions

**Example of BAD pattern**:
```markdown
TodoWrite([
  {"content": "Execute comprehensive synthesis with mathematical assessment", "status": "pending", "priority": "high"},
  {"content": "Coordinate multi-dimensional validation through orchestration layers", "status": "pending", "priority": "high"}
])
```

**Replacement with GOOD pattern**:
```markdown
## Phase 1: Analysis
Execute codebase analysis using Read and Grep tools
Generate project structure assessment

## Phase 2: Recommendations  
Create actionable guidance based on analysis
Present clear next steps to user
```

### Anti-Pattern 2: Vague Language and Marketing Speak
**Problems**:
- "Intelligent orchestration" without specifics
- "Comprehensive synthesis" without clear definition
- "Advanced optimization" without metrics

**Good replacements**:
- "Execute parallel Read operations on project files"
- "Combine results from 3 analysis tools"  
- "Reduce execution time from 2 minutes to 30 seconds"

### Anti-Pattern 3: Complex Error Handling
**Problems**:
- Generic error messages
- No specific recovery guidance
- Multiple error handling layers

**Good replacement**:
```markdown
ERROR: Git repository not found
CAUSE: No .git directory in current or parent directories
RECOVERY: Run 'git init' to initialize repository, or navigate to project root
CONTINUE: Command will proceed with local file analysis only
```

## Command Quality Checklist

### Pre-Development Validation (2 minutes)
```bash
- [ ] Clear purpose in 30 seconds?
- [ ] Single responsibility only?  
- [ ] Simplest solution that works?
- [ ] Works without configuration?
```

### PTS Component Validation (10 minutes)
```bash
Technical Cluster:
- [ ] Directness: ≤3 steps to objective?
- [ ] Precision: 100% specific instructions?
- [ ] Sufficiency: Complete but minimal?
- [ ] Technical Excellence: Error handling included?

Communication Cluster:  
- [ ] Exactitude: Exact implementation points?
- [ ] Sobriety: Zero marketing language?
- [ ] Structure: Logical organization?
- [ ] Conciseness: Maximum value/complexity ratio?

Cognitive Cluster:
- [ ] Clarity: Immediate comprehension?
- [ ] Coherence: Internal consistency?
- [ ] Effectiveness: Measurable results?
- [ ] Pragmatism: Real-world functionality?
```

### Length and Complexity Validation
```bash
- [ ] ≤150 lines total length?
- [ ] ≤3 main phases?
- [ ] ≤5 tools used?
- [ ] ≤10 TodoWrite items (if any)?
```

## Tool Usage Best Practices

### Direct Tool Integration (GOOD)
```markdown
## Phase 1: Project Analysis
Use Read tool to examine package.json and README.md
Use Grep tool to identify main entry points
Use LS tool to understand directory structure
```

### Avoid Orchestration Overhead (BAD)
```markdown
## Phase 1: Comprehensive Analysis Orchestration
TodoWrite([
  {"content": "Execute multi-layered project analysis with comprehensive validation", "status": "pending"}
])
```

### Error Handling Integration
```markdown
# Tool usage with error handling
Read package.json
→ If file not found: "No package.json detected - Node.js project structure assumed"
→ If malformed JSON: "Package.json syntax error - manual review required"
→ Continue with available information
```

## Template Usage Guide

### For Core Commands (Essential Functionality)
Use **Pattern 1: Simple Standalone Command**
- Focus on single, clear responsibility
- Direct tool usage
- Minimal phases (≤3)
- Essential error handling

### For Enhanced Commands (Extended Features)  
Use **Pattern 2: Enhanced Structured Command**
- Add comprehensive error handling framework
- Include authority references
- Maintain clear phase separation
- Add specific recovery guidance

### For Progressive Commands (Adaptive Behavior)
Use **Pattern 3: Balanced Multi-Phase Command**  
- Implement progressive enhancement
- Maintain user control
- Provide clear capability communication
- Include graceful degradation

## Success Metrics by Pattern

### Pattern 1 Success Indicators
- Execution time <30 seconds
- User understanding <10 seconds
- Error rate <5%
- Reuse rate >80%

### Pattern 2 Success Indicators  
- Complex workflow completion >90%
- Error recovery success >95%
- User satisfaction >85%
- Maintenance time <15 minutes/month

### Pattern 3 Success Indicators
- Progressive enhancement adoption >60%
- Fallback usage success >90%
- User choice satisfaction >95%
- Capability communication clarity >85%

---

**Foundation Principle**: Build commands using proven patterns that deliver immediate practical value while maintaining technical excellence and user clarity.