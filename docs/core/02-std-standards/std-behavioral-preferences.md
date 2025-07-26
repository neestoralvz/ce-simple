# Behavioral Preferences Standard

**Updated**: 2025-07-24 | **Authority**: Anthropic CLAUDE.md best practices | **Limit**: 100 lines

## Purpose

This file should document how Claude should behave when working on this project - communication style, decision-making preferences, error handling approaches, and interaction patterns. Based on official Anthropic recommendations, this customizes AI assistant behavior for optimal team collaboration.

## Content Structure

### What Should Be Included

**Communication Style:**
```markdown
# Communication Preferences
- Tone: Direct and technical, minimal small talk
- Explanations: Concise with code examples, avoid verbose descriptions
- Questions: Ask for clarification rather than assume requirements
- Updates: Provide progress status for multi-step tasks
```

**Decision Making:**
```markdown
# Decision Preferences
- Code choices: Prefer established patterns over innovative solutions
- Library selection: Use existing dependencies, avoid adding new ones
- Architecture: Follow current project structure, don't restructure
- Performance: Optimize for readability first, performance second
```

**Error Handling:**
```markdown
# Error Response Behavior
- Debug approach: Show reasoning process for complex issues
- Error messages: Include relevant code context and line numbers
- Solution options: Provide 2-3 alternative approaches when possible
- Documentation: Always reference relevant docs or comments
```

**Task Management:**
```markdown
# Work Style Preferences
- Planning: Break complex tasks into smaller steps
- Testing: Run tests after each significant change
- Documentation: Update comments and docs with code changes
- Git workflow: Commit frequently with descriptive messages
```

## Implementation Guidelines

### Response Patterns
- **Technical Queries**: Provide code examples and references
- **Planning Questions**: Offer structured approaches with priorities
- **Error Reports**: Include diagnostic steps and verification methods
- **Feature Requests**: Clarify requirements before implementation

### Collaboration Style
- **Code Reviews**: Focus on functionality, performance, maintainability
- **Discussions**: Present options with pros/cons analysis
- **Disagreements**: Reference project standards and team decisions
- **Learning**: Explain reasoning behind suggestions

### Quality Standards
- **Accuracy**: Verify information before providing answers
- **Completeness**: Address all aspects of complex questions
- **Consistency**: Follow established project patterns
- **Efficiency**: Prioritize solutions that save development time

## Benefits for AI Assistant

**Team Alignment**: Claude matches team communication style
**Predictable Behavior**: Consistent responses across interactions
**Reduced Friction**: Fewer misunderstandings and clarifications
**Enhanced Productivity**: Optimized workflow integration

---

**Implementation Note**: This template should be populated with actual team preferences for AI interaction, communication styles, and behavioral expectations. The format follows Anthropic's guidance for comprehensive behavioral documentation that enables AI assistants to integrate seamlessly into team workflows and match organizational culture.