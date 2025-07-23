# Learning Capture System

## Value Scoring

### Context Weight
- Days since interview: +1 (max +3)
- Simple executions: +1 per 3 consecutive
- Novel domains: +2

### Complexity Score
- Sequential commands (>2): +2
- Error resolution: +2
- New patterns: +2
- Alternative strategies: +1
- Unexpected timing: +1
- Novel tool combinations: +1
- Context switching: +1

## Interview Questions

### Core Questions
- Process effectiveness: "Did workflow follow expected sequence?"
- Result quality: "Do results match initial vision?"
- Friction points: "Any confusion or blocking moments?"
- Discovery value: "Learn anything unexpected?"
- Efficiency: "What would you change next time?"
- System evolution: "Does result suggest system improvements?"

### Selection Logic
Choose 3 highest-value questions based on execution patterns. Add extended questions only for multiple novel patterns.

## Storage Structure

### Patterns
- `execution-patterns-[domain].md` - Workflow execution
- `decision-patterns-[domain].md` - Choice reasoning
- `friction-patterns-[domain].md` - Obstacles and solutions
- `discovery-patterns-[domain].md` - Learning insights

### Experience
- `workflow-effectiveness-[month].md` - Process efficiency
- `expectation-reality-[month].md` - Outcome analysis
- `improvement-suggestions-[month].md` - Enhancement ideas

## Agent Integration

### Process Agent
1. Document decision reasoning
2. Classify discovery novelty
3. Record rejected options
4. Enhance context with meta-insights

### Results Agent
1. Analyze execution workflow
2. Generate dynamic questions
3. Conduct feedback interview
4. Validate system integrity
5. Integrate insights with patterns

## Integrity Validation

### Components
- Command existence in "See Also" sections
- Chain consistency (bidirectional)
- Cross-reference accessibility
- Trigger logic consistency

### Gap Classification
- **Critical**: Missing command breaks workflow
- **Reference**: Broken cross-reference reduces navigation
- **Chain**: Incomplete workflow progression
- **Documentation**: Inconsistent references

### Resolution Priority
1. **Immediate**: Critical workflow gaps
2. **High**: Reference gaps in frequent commands
3. **Medium**: Secondary workflow chains
4. **Low**: Rarely accessed documentation

## Notifications

### Integration Format
- INTEGRITY: System validation initiated
- VALIDATION: Commands verified, references checked
- DISCOVERY: Gaps identified with severity
- COMPLETION: Health documented, recommendations generated