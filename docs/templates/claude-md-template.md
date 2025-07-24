# CLAUDE.md Template - Four-Section Architecture

**Target Length**: ≤{{MAX_LINES_CLAUDE_MD}} lines total
**Purpose**: Navigation and essential references only
**Principle**: All details referenced, not included
**Architecture**: Four-section structure with practical development integration

## Configuration Variables

| Variable | Description | Default Value |
|----------|-------------|---------------|
| `{{PROJECT_NAME}}` | Project name | ce-simple |
| `{{MAX_LINES_CLAUDE_MD}}` | Maximum lines for CLAUDE.md | 50 |
| `{{MAX_LINES_COMMANDS}}` | Maximum lines per command | 150 |
| `{{MAX_LINES_DOCS}}` | Maximum lines per document | 200 |
| `{{GLOBAL_COMMANDS_COUNT}}` | Number of global commands | 86 |
| `{{COMMAND_CATEGORIES_COUNT}}` | Number of command categories | 15 |
| `{{LOCAL_COMMANDS_COUNT}}` | Number of local essential commands | 3 |
| `{{VALIDATION_COMPONENTS_COUNT}}` | Number of PTS validation components | 12 |
| `{{UPDATE_DATE}}` | Last update date | [CURRENT_DATE] |

## Section Structure & Line Limits

### 1. Header + Tech Stack (8 lines max)
```markdown
# CLAUDE.md - {{PROJECT_NAME}}

**Last Updated**: {{UPDATE_DATE}}

## Tech Stack
- **Platform**: Claude Code slash commands
- **Architecture**: Self-contained commands with Task Tool parallel execution
- **Validation**: PTS (Pragmatic Technical Simplicity) {{VALIDATION_COMPONENTS_COUNT}}-component framework
```

### 2. Project Structure (10 lines max)
```markdown
## Project Structure  
```
{{PROJECT_NAME}}/
├── CLAUDE_RULES.md          # Partnership protocol (READ FIRST)
├── docs/                    # Documentation (@docs/core/README.md)
├── export/commands/         # {{GLOBAL_COMMANDS_COUNT}} global commands ({{COMMAND_CATEGORIES_COUNT}} categories)
├── commands/                # {{LOCAL_COMMANDS_COUNT}} essential local commands
└── development/             # Prototyping workspace
```
```

### 3. Commands (12 lines max)
```markdown
## Commands

### Essential Local Commands
- `/init-project` - Complete project initialization
- `/start` - Project analysis and guidance  
- `/explore-codebase` - Understand project structure

### Master Workflow Commands  
- `/master-execute` - Complete workflow orchestration
- `/git-workflow` - Git integration with commit protocols
- `/validate-recursive` - 5-retry validation system

**Global System**: {{GLOBAL_COMMANDS_COUNT}} commands in export/commands/ → @export/CLAUDE.md
```

### 4. Standards (8 lines max)
```markdown
## Standards

### Command Development
- **Length Limit**: {{MAX_LINES_COMMANDS}} lines maximum per command
- **PTS Compliance**: {{VALIDATION_COMPONENTS_COUNT}}/{{VALIDATION_COMPONENTS_COUNT}} components required (@docs/core/pts-framework.md)
- **Self-Contained**: No external dependencies
- **English Only**: Zero mixed language content
- **Quality Gates**: @docs/core/pts-checklist.md
```

### 5. Testing & Quality (6 lines max)
```markdown
## Testing & Quality

**PTS Validation**: @docs/core/pts-checklist.md
**Standards**: @docs/core/development-principles.md  
**Authority Hierarchy**: CLAUDE_RULES.md → docs/vision/ → docs/core/
```

### 6. Practical Development (6 lines max)
```markdown
## Section 4: Practical Development (Context-Triggered)
**Basic Commands** → READ docs/standards/basic-commands.md:20-50
**Code Style** → READ docs/standards/code-style-preferences.md:15-40
**Development Workflow** → READ docs/standards/development-workflow.md:25-60
**Environment Setup** → READ docs/standards/environment-setup.md:15-35
**Known Issues** → READ docs/standards/known-issues-warnings.md:20-45
**AI Behavior** → READ docs/standards/behavioral-preferences.md:15-40
```

### 7. Tech Stack (2 lines max)
```markdown
## Tech Stack
- **Platform**: Claude Code slash commands | **Architecture**: Self-contained commands with Task Tool parallel execution
- **Authority**: docs/vision/ → CLAUDE_RULES → docs/core/ → CLAUDE | **Prohibitions**: No Spanish | No marketing | No PTS bypass
```

### 8. Footer (2 lines max)
```markdown
---
**Core Principle**: Simple building blocks with single responsibility that orchestrate into complex workflows.
```

## Template Usage

### Content Rules
- **No detailed explanations** - only references to full docs
- **No examples** - link to example files instead  
- **No implementation details** - reference appropriate docs/ sections
- **No redundancy** - single source of truth principle

### Line Budget Distribution (Four-Section Architecture)
- Header: 3 lines
- Section 1 (Essential Context): 4 lines
- Section 2 (Conditional Instructions): 6 lines
- Section 3 (Context Navigation): 6 lines
- Section 4 (Practical Development): 6 lines
- Tech Stack: 2 lines
- Footer: 2 lines
- **Total**: 29 lines ({{MAX_LINES_CLAUDE_MD}} line budget)

### Validation Checklist (Four-Section Architecture)
- [ ] Total lines ≤{{MAX_LINES_CLAUDE_MD}}
- [ ] Four sections properly structured and labeled
- [ ] Section 1: @ imports for essential context
- [ ] Section 2: Conditional instructions with READ syntax
- [ ] Section 3: Directory navigation with markdown links
- [ ] Section 4: Practical development with Anthropic best practices
- [ ] All details referenced, not included
- [ ] Clear navigation to full documentation
- [ ] No redundant information
- [ ] English-only content
- [ ] Single responsibility maintained

## Cognitive Load Principle

**Purpose**: This four-section template ensures CLAUDE.md serves as a lightweight navigation hub with integrated practical development guidance, reducing cognitive load while maintaining full system access through references and Anthropic best practices integration.

## Template Usage Instructions

1. **Replace Variables**: Substitute all `{{VARIABLE_NAME}}` with actual values
2. **Verify Line Counts**: Ensure each section stays within specified limits
3. **Update References**: Confirm all @docs/ links point to existing files
4. **Validate Total**: Final file must be ≤{{MAX_LINES_CLAUDE_MD}} lines