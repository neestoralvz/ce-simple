# Basic Commands Standard

**Updated**: 2025-07-24 | **Authority**: Anthropic CLAUDE.md best practices | **Limit**: 100 lines

## Purpose

This file should document the essential commands that Claude needs to know to work effectively with this project. Based on official Anthropic best practices, this section serves as the primary command reference for AI assistant interactions.

## Content Structure

### What Should Be Included

**Essential Build Commands:**
```markdown
# Build & Development
- npm run dev: Start development server
- npm run build: Build for production
- npm run preview: Preview production build
```

**Testing Commands:**
```markdown
# Testing
- npm run test: Run test suite
- npm run test:watch: Run tests in watch mode
- npm run test:coverage: Generate coverage reports
```

**Code Quality Commands:**
```markdown
# Quality Assurance
- npm run lint: Run linter
- npm run lint:fix: Auto-fix linting issues
- npm run typecheck: Verify TypeScript types
- npm run format: Format code with prettier
```

**Utility Commands:**
```markdown
# Utilities
- npm run clean: Clean build artifacts
- npm run deploy: Deploy to production
- npm run analyze: Analyze bundle size
```

## Implementation Guidelines

### Command Documentation Format
- **Brief Description**: One-line explanation of what each command does
- **Common Usage**: When and why to use each command
- **Prerequisites**: Any setup required before running
- **Expected Output**: What success/failure looks like

### Priority Levels
1. **Critical**: Commands needed for basic development (dev, build, test)
2. **Important**: Quality assurance commands (lint, typecheck)
3. **Utility**: Helper commands for specific tasks

### Project Integration
- Commands should reflect actual package.json scripts
- Include project-specific bash commands if any
- Document any environment-specific variations
- Reference any custom tooling or scripts

## Benefits for AI Assistant

**Context Awareness**: Claude understands available operations
**Workflow Efficiency**: Can suggest appropriate commands for tasks
**Error Prevention**: Knows correct syntax and usage patterns
**Team Consistency**: Everyone uses same command references

---

**Implementation Note**: This file template should be populated with actual project commands from package.json and any custom scripts. The format follows Anthropic's recommendation for concise, specific command documentation that reduces cognitive load while providing complete operational context.