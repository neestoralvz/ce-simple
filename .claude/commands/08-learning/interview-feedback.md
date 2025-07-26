# interview-feedback

**Updated**: 2025-07-26 | **Category**: 08-learning | **Purpose**: Systematic user feedback capture via structured interview

## Purpose

Initiate systematic user feedback interview capturing insights about results, achievements, challenges, errors, obstacles, and learnings. Creates structured documentation in Sacred User Space preserving user voice and perspective.

## Principles

- **Sacred User Space**: All feedback captured in user-input/context/ preserving user's authentic voice
- **Structured Interview**: Systematic question framework ensuring comprehensive feedback collection
- **Context Preservation**: Links current session results to feedback for future reference
- **Learning Integration**: Connects feedback to system evolution and pattern recognition

## Execution Process

### Phase 1: Interview Preparation
Mark "Interview Setup and Context Preparation" as in_progress using TodoWrite

Prepare interview environment:
- Validate user-input/context/ directory exists (create if needed)
- Generate timestamp for feedback session: TZ='America/Mexico_City' date '+%Y-%m-%d-%H-%M'
- Identify current session context and results for reference
- Prepare structured interview questions framework

Use Write to create context directory if needed:
```bash
# Ensure docs/context/ exists for cross-reference
# Ensure user-input/context/ exists for Sacred User Space
```

Complete Phase 1, mark "Structured Interview Execution" as in_progress using TodoWrite

### Phase 2: Interview Execution
Mark "Structured Interview Execution" as in_progress using TodoWrite

Execute systematic interview using progressive questioning:

**Interview Framework**:
1. **Session Context**: "What was the main objective of this session?"
2. **Results Assessment**: "How do you evaluate the results achieved?"
3. **Achievements**: "What specific achievements or successes did you observe?"
4. **Challenges**: "What challenges or difficulties did you encounter?"
5. **Errors & Obstacles**: "What errors, obstacles, or blockers appeared?"
6. **Learning Insights**: "What key learnings or insights did you gain?"
7. **System Performance**: "How did the VDD framework perform during this session?"
8. **Improvement Areas**: "What areas need improvement or optimization?"
9. **Future Priorities**: "What should be prioritized in upcoming sessions?"
10. **Overall Satisfaction**: "Rate overall satisfaction and explain reasoning"

Conduct interview with natural conversation flow while covering all framework areas.

Complete Phase 2, mark "Feedback Documentation" as in_progress using TodoWrite

### Phase 3: Feedback Documentation
Mark "Feedback Documentation" as in_progress using TodoWrite

Document feedback in Sacred User Space:

Create comprehensive feedback file:
- **Filename**: user-input/context/feedback-YYYY-MM-DD-HH-MM-session.md
- **Structure**: Interview responses with user's exact language preserved
- **Categories**: logros, desafios, errores, obstaculos, aprendizajes (as requested by user)
- **Context Links**: Reference to session objectives and results
- **Metadata**: Session duration, tools used, complexity level

Use Write to create feedback documentation:
```markdown
# User Feedback Session - [Date/Time]

**Type**: Sacred User Space - User authentic voice preserved
**Session Context**: [Brief session description]
**Duration**: [Session length]
**Tools Used**: [List of tools/commands]

## Achievements (Logros)
[User responses about successes and achievements]

## Challenges (Desafios)
[User responses about challenges faced]

## Errors (Errores)
[User responses about errors encountered]

## Obstacles (Obstaculos)
[User responses about obstacles and blockers]

## Learnings (Aprendizajes)
[User responses about insights and learnings]

## VDD Framework Performance
[User assessment of framework effectiveness]

## Future Priorities
[User input on next priorities]

## Overall Session Assessment
**Satisfaction**: [Rating/assessment]
**Reasoning**: [User explanation]

---
**Preservation Note**: This feedback represents user's authentic perspective and should inform system evolution decisions.
```

Complete Phase 3, mark "Cross-Reference Integration" as in_progress using TodoWrite

### Phase 4: Integration & Follow-up
Mark "Cross-Reference Integration" as in_progress using TodoWrite

Integrate feedback with system:
- Create docs/context/ cross-reference linking to user feedback
- Update relevant handoff documents with feedback insights
- Identify actionable improvements for next session
- Generate TodoWrite tasks for high-priority improvements

Use Write to create cross-reference documentation:
```markdown
# Session Feedback Cross-Reference - [Date]

**User Feedback**: user-input/context/feedback-YYYY-MM-DD-HH-MM-session.md
**System Context**: [Current session tools and results]
**Action Items**: [Derived improvement tasks]

## Key Insights
- [Extracted patterns and insights]

## System Improvements
- [Identified optimization opportunities]

## Next Session Priorities
- [Priority tasks for upcoming work]
```

Complete interview process, mark all phases as completed using TodoWrite

## Error Recovery

**Interview Interruption**: Resume with last completed question, preserve partial responses
**Documentation Failure**: Retry with simplified format, ensure user voice preservation
**Context Loss**: Recreate interview framework, focus on critical feedback areas
**User Unavailability**: Schedule follow-up interview, maintain interview preparation

## Success Criteria

- Complete interview framework executed with user engagement
- Feedback documented in Sacred User Space preserving authentic user voice
- Cross-references created linking feedback to system context
- Actionable improvements identified and queued for implementation
- User satisfaction with feedback capture process

## Integration Points

**Connects to**: /capture-learnings (system-wide pattern extraction)
**Feeds into**: All categories (improvement input)
**References**: user-input/context/ (Sacred User Space)
**Updates**: docs/context/ (implementation tracking)

---

**Command Truth**: Systematic user feedback capture preserving authentic voice while enabling continuous VDD framework evolution.