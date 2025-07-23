# Capture Learnings - Documentation Command

## Purpose
Dual-phase learning capture system for automatic pattern documentation during workflows and intelligent post-execution interviews based on learning value assessment.

## Principles and Guidelines

**Single Responsibility**: Focus exclusively on learning capture and documentation without execution or analysis
**Granular Learning**: Break learning capture into small, specific documentation steps
**Knowledge Management**: Clear learning thresholds with explicit validation requirements
**Error Recovery**: Built-in learning capture failure handling and interview adjustment protocols

## Execution Process

### Phase 1: Learning Value Assessment
Update TodoWrite: Mark "Learning value assessment" as in_progress

Calculate learning value using assessment framework:
- Assess progressive disclosure mastery and application (+2 points)
- Evaluate system health optimization contributions (+2 points)
- Document alternative strategies evaluated (+1 point)
- Identify cross-domain insights generated (+1 point)
- Record workflow complexity indicators (+1 point)

Determine learning capture threshold:
- Calculate total learning value score from assessment
- Apply threshold evaluation (≥4 points for interview activation)
- Determine appropriate learning capture approach
- Validate learning value calculation accuracy

Prepare learning capture strategy:
- If score ≥4: Prepare for dynamic interview execution
- If score <4: Prepare for basic pattern documentation
- Identify specific learning areas and focus topics
- Plan documentation approach and target files

### Phase 2: Dynamic Learning Interview
Update TodoWrite: Complete previous, mark "Learning interview execution" as in_progress

Conduct intelligent learning interview (if threshold met):
- Generate 3-6 context-driven questions based on workflow
- Focus questions on just-executed commands and patterns
- Gather insights about decision points and alternatives
- Document user responses and learning insights

Extract learning patterns from interview:
- Identify successful approaches and decision criteria
- Document alternative strategies and evaluation methods
- Record workflow optimization opportunities
- Capture cross-domain insights and applications

### Phase 3: Pattern Documentation and Integration
Update TodoWrite: Complete previous, mark "Pattern documentation" as in_progress

Document discovered patterns systematically:
- Update existing context/patterns/ files with validated patterns
- Enhance context/workflows/ files with workflow insights
- Apply progressive disclosure principles to documentation
- Maintain file size limits (≤200 lines maximum)

Use Read tool to review existing documentation:
- Read current pattern documentation for context
- Identify integration points for new learning
- Validate consistency with existing patterns
- Prepare updates without creating new files

Use Write tool for learning documentation:
- Update universal-problem-solving-patterns.md with validated patterns
- Enhance workflow-notifications.md with insights
- Integrate learning into existing documentation structure
- Apply evidence-based documentation standards

### Phase 4: System Integration Validation
Update TodoWrite: Complete previous, mark "Learning integration validation" as in_progress

Validate learning integration with system:
- Verify pattern consistency across documentation
- Check cross-reference integrity with existing content
- Confirm learning enhances rather than contradicts system
- Validate documentation quality and clarity

Assess system evolution opportunities:
- Identify command system enhancement opportunities
- Document workflow optimization recommendations
- Record system health improvement suggestions
- Plan integration of learning into future workflows

If learning capture issues detected:
- Add TodoWrite task: "Resolve learning capture issue: [specific problem]"
- Adjust interview approach or documentation strategy
- Validate learning accuracy and system integration
- Document resolution approach for future improvements

Update TodoWrite: Complete all learning capture tasks
Add follow-up: "Learning capture complete with patterns documented and integrated"

---

**Single Responsibility**: Documentation focused exclusively on learning capture, pattern extraction, and knowledge integration.**