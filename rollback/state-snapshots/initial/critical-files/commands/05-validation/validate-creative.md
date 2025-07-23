# validate-creative.md

**Purpose**: LLM-based validation for creative outputs measuring originality, engagement, and user satisfaction through qualitative assessment metrics.

## Command Structure

### Phase 1: Creative Assessment Setup
- Define creativity domains (content, design, narrative, innovation)
- Establish baseline metrics (originality score, engagement potential, emotional impact)
- Set evaluation criteria specific to creative output type
- Initialize feedback collection mechanisms

### Phase 2: Multi-Dimensional Analysis
- **Originality Scoring**: Assess uniqueness against common patterns
- **Engagement Metrics**: Evaluate user interaction potential and appeal
- **Emotional Resonance**: Measure emotional impact and connection strength  
- **Innovation Factor**: Rate creative problem-solving and novel approaches

### Phase 3: Validation Execution
- Run parallel creative assessments across defined dimensions
- Generate quantifiable scores for each creativity metric
- Cross-validate results through multiple evaluation perspectives
- Document specific strengths and improvement opportunities

### Phase 4: Feedback Integration
- Compile comprehensive creativity assessment report
- Identify specific enhancement recommendations
- Trigger iteration cycle if scores below threshold (70%)
- Archive successful validations with pattern documentation

## Implementation

Execute through Claude Code Task Tool with parallel creative evaluation:

```bash
# Creative validation workflow
validate_creative() {
    # Creativity domain assessment
    assess_originality_score()
    assess_engagement_potential() 
    assess_emotional_impact()
    assess_innovation_factor()
    
    # Multi-perspective validation
    cross_validate_creativity()
    generate_improvement_recommendations()
    
    # Results processing
    compile_creative_assessment()
    trigger_feedback_loop_if_needed()
}
```

## Success Criteria

**Validation Thresholds**:
- Originality Score: ≥75/100
- Engagement Potential: ≥70/100  
- Emotional Impact: ≥65/100
- Innovation Factor: ≥70/100
- Overall Creative Score: ≥70/100

**Feedback Triggers**: Any metric below threshold initiates targeted improvement cycle with specific enhancement recommendations and re-validation protocol.