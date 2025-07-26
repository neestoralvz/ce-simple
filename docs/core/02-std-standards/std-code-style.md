# Code Style Preferences Standard

**Updated**: 2025-07-24 | **Authority**: Anthropic CLAUDE.md best practices | **Limit**: 100 lines

## Purpose

This file should document the specific code formatting, naming conventions, and structural preferences for this project. Based on official Anthropic recommendations, this ensures Claude writes code that matches team standards and project conventions.

## Content Structure

### What Should Be Included

**Import/Export Standards:**
```markdown
# Import Preferences
- Use ES modules syntax (import/export), not CommonJS (require)
- Destructure imports when possible: import { foo, bar } from 'module'
- Prefer named exports over default exports
- Group imports: built-in → external → internal
```

**Formatting Standards:**
```markdown
# Code Formatting
- Indentation: 2 spaces (no tabs)
- Line length: 100 characters maximum
- Semicolons: Always required
- Quotes: Single quotes for strings, double for JSX attributes
- Trailing commas: Always in multiline structures
```

**Naming Conventions:**
```markdown
# Naming Standards
- Variables: camelCase
- Functions: camelCase with descriptive verbs
- Components: PascalCase
- Files: kebab-case for regular files, PascalCase for components
- Constants: SCREAMING_SNAKE_CASE
```

**Code Organization:**
```markdown
# File Structure
- One component per file
- Export at bottom of file
- Group related functions together
- Separate business logic from presentation
```

## Implementation Guidelines

### Language-Specific Preferences
- **JavaScript/TypeScript**: Specific syntax preferences
- **CSS/Styling**: Naming conventions, organization patterns
- **HTML**: Attribute ordering, semantic structure
- **Configuration**: File formatting standards

### Tool Integration
- **Prettier**: Automated formatting rules
- **ESLint**: Linting rules and exceptions  
- **TypeScript**: Type annotation preferences
- **Editor Config**: IDE-specific settings

### Code Quality Principles
- **Readability**: Code should be self-documenting
- **Consistency**: Follow established patterns
- **Simplicity**: Prefer explicit over clever code
- **Performance**: Consider efficiency in critical paths

## Benefits for AI Assistant

**Consistent Output**: Claude generates code matching team style
**Reduced Reviews**: Less time spent on style corrections
**Team Harmony**: Everyone follows same conventions
**Quality Maintenance**: Automated adherence to standards

---

**Implementation Note**: This template should be populated with actual project-specific style preferences, ESLint/Prettier configurations, and team-agreed conventions. The format follows Anthropic's guidance for specific, actionable style documentation that eliminates ambiguity in AI-generated code.