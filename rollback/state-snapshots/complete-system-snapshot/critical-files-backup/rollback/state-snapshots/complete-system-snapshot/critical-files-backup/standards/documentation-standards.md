# Documentation Standards

## Purpose
Write clear instructions for Claude Code execution using minimal words and maximum clarity.

**Language**: All documentation must be in English.

## Simplicity Principle
**Simple & Direct, But Sufficient**

- Clear on first read
- Essential only
- Complete information
- Immediately actionable

Example:
```
COMPLEX: "Execute comprehensive analysis of codebase structure including architectural patterns"
SIMPLE: "Analyze codebase structure and identify patterns"
```

## Word Economy
Use fewer words for better results:

- Every word must contribute
- Remove unnecessary phrases
- Focus on action verbs
- Eliminate fluff
- Each concept appears once (no redundancy)

## Length Limits
- Commands: ≤150 lines
- Documentation: ≤200 lines  
- Patterns: ≤100 lines

## Progressive Disclosure
Extract to separate files when content is:
- Rarely needed during daily execution
- Complex details requiring deep study
- Reference material or templates

Keep in main file when content is:
- Used frequently (daily/weekly)
- Essential for basic understanding

Reference format: "See [filename].md for [specific details]"

## Natural Language Instructions

Write direct commands:
```
GOOD: "Search TypeScript files for function definitions"
BAD: "Glob('**/*.ts', {pattern: 'function'})"

GOOD: "Create component with error handling"
BAD: "const component = createComponent({errorBoundary: true})"
```

Use action verbs and specific nouns. Remove "should", "might", "perhaps".

## File Naming
- Core files: `topic.md`
- Detailed content: `topic-details.md`
- Examples: `topic-examples.md`
- Advanced: `topic-advanced.md`

Use lowercase, hyphens for spaces, descriptive but concise names.

## Document Structure

Use the standard template. See ../templates/documentation-template.md for complete structure and variations.

## Anti-Patterns

Never include:
- Programming code
- Theoretical explanations
- Redundant phrases
- Meta-commentary

Avoid:
- Verbose instructions (>15 words)
- Vague descriptions
- Multiple readings needed
- Overwhelming complexity

## Quality Check

Ask yourself:
- Can I execute this immediately?
- Does every word help?
- Would removing any word make it unclear?
- Is this the simplest way to say it?

## When to Improve
- Users confused during execution
- Instructions need re-reading
- Content feels complex
- Words without clear purpose

---

**All documentation follows simple & direct principles using natural language efficiency for Claude Code execution success.**