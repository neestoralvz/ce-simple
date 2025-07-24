# feedback-vision

## Purpose

Captures user feedback through dynamic interviews and integrates with research to update docs/vision/ as the absolute source of truth for system direction.

## Principles

- **Vision Authority**: docs/vision/ directory is the ultimate authority for user intent
- **Dynamic Questioning**: Generate contextual questions based on current project state
- **Research Integration**: Combine user responses with web/codebase searches for enhanced context
- **Intelligent Filing**: Automatically identify and update the correct vision document

## Execution Process

### Phase 1: Context Analysis
Mark "Context Analysis and Question Generation" as in_progress using TodoWrite

Execute parallel context gathering:
- Agent 1: Use Read tool to analyze all docs/vision/ files and identify current focus areas
- Agent 2: Use Grep to search recent project changes and modifications
- Agent 3: Use WebSearch to gather external context on current project topics
- Agent 4: Use Glob to identify recently modified files for context

Synthesize context into dynamic question framework:
- Identify gaps in current vision documentation
- Generate specific questions about user intentions and preferences
- Prepare contextual follow-up questions based on project state

### Phase 2: User Interview
Mark "Dynamic User Interview and Feedback Collection" as in_progress using TodoWrite

Execute dynamic interview process:
- Present initial contextual questions to user based on Phase 1 analysis
- Collect user responses and identify areas requiring deeper exploration
- Generate follow-up questions dynamically based on user responses
- Continue interview until comprehensive feedback is captured

For each significant user response:
- Execute parallel research: WebSearch for external insights + Grep for codebase alignment
- Synthesize research findings with user input for enhanced understanding
- Validate user intent against existing vision documents

### Phase 3: Research Enhancement
Mark "Research Integration and Context Enhancement" as in_progress using TodoWrite

Execute parallel research based on user responses:
- Agent 1: WebSearch using user response keywords for external insights and best practices
- Agent 2: Grep codebase for related implementations and patterns
- Agent 3: Read relevant documentation for alignment validation
- Agent 4: Analyze vision documents for consistency requirements

Synthesize research findings:
- Combine external insights with user feedback
- Identify enhancement opportunities for vision documents
- Validate research alignment with user intentions

### Phase 4: Vision Update
Mark "Vision Document Update and Integration" as in_progress using TodoWrite

Execute intelligent vision document updates with consolidation:
- Analyze existing vision documents for related content before creating new files
- Consolidate information into existing documents when concepts overlap (≤200 line limit)
- Create new vision documents only when content requires separate treatment
- Use Edit tool to update identified vision documents following documentation standards
- Apply progressive disclosure principles extracting details to separate files when needed
- Ensure updates maintain document structure, consistency, and ≤200 line limits
- Validate updates preserve user intent without LLM modifications

Execute vision document validation and standards compliance:
- Cross-reference updates against all other vision documents for consistency
- Ensure user feedback is accurately represented without interpretation bias
- Validate adherence to documentation standards (natural language, word economy, clarity)
- Confirm document length limits and progressive disclosure implementation
- Validate document integrity, readability, and immediate actionability

Complete all tasks using TodoWrite

---

**Vision-driven feedback system ensuring docs/vision/ reflects pure user intent enhanced with intelligent research.**