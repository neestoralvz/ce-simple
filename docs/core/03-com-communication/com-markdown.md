# Markdown Standards

**Updated**: 2025-07-24 | **Authority**: Official Markdown compliance & readability framework  
**Navigation**: [System Hub](../navigation/index.md) | [Communication Rules](communication-rules.md) | [Documentation Standards](documentation-standards.md)

## Core Compliance Framework

**Principle**: Clean, structured, technically precise → following official Markdown specifications

### Header Hierarchy → Visual Structure
- `#` H1 (document title only) | `##` H2 (main sections) | `###` H3 (subsections)
- **Never skip levels**: H1→H2→H3 (never H1→H3) | **Spacing**: Empty line before/after headers
- **Consistency**: Same style throughout document | **Purpose**: Each header serves navigation

### List Standards → Information Architecture
**Bullets**: `-` (hyphen) for unordered | `1.` `2.` for ordered | **Indentation**: 2 spaces per level
**Alignment**: Correct with parent content | **Spacing**: No empty lines between same-level items

```markdown
## Correct ✅
- Main item
  - Sub-item (2 spaces)
  - Another sub-item
- Second main item

## Incorrect ❌
- Main item

  - Sub-item (unnecessary empty line)
* Mixing bullet styles
```

### Code Standards → Technical Precision
**Inline**: `backticks` for commands/variables/paths | **Blocks**: ````language` with specified language
**File paths**: Always in `code format` when mentioning files | **Commands**: Always in backticks

### Emphasis Rules → Content Hierarchy
**Bold**: `**text**` for key concepts/technical terms | **Italic**: `*text*` for subtle emphasis (minimal use)
**Avoid combining**: No `***text***` except critical cases | **Purpose**: Enhance readability, not decoration

### Link Standards → Navigation Excellence
**Format**: `[descriptive text](url)` | Text must be meaningful, not generic
**References**: `[text][ref]` + `[ref]: url` at end for long URLs
**Internal**: Standard markdown links `[Title](docs/path/file.md)` for ce-simple references
**@ Import Restriction**: @ syntax ONLY works in CLAUDE.md files, NOT in regular documentation

### Table Format → Data Presentation
```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data     | Data     | Data     |
```
**Alignment**: Pipes aligned | Headers always with separator | Content concise

### Spacing Protocol → Document Flow
**Paragraphs**: One empty line between | **Sections**: One empty line before/after headers
**Lists**: No empty lines between same-level items | **Code blocks**: One empty line before/after

## Anti-Patterns → Compliance Violations

**Critical Errors**:
- ❌ Headers without spacing: `##Header` → `## Header`
- ❌ Inconsistent lists: Mixing `-` `*` `+` bullets
- ❌ Excessive emphasis: `**every** *word* **emphasized**`
- ❌ Generic links: `[click here](url)` → `[view documentation](url)`
- ❌ Unformatted code: use git status → use `git status`
- ❌ Incorrect nesting: H1→H3 (skipping H2)

## Readability Framework

### Visual Hierarchy → Scanning Optimization
**Headers**: Create clear visual structure | **Bullets**: Enable rapid scanning
**Consistency**: Same format for similar elements | **Predictability**: Consistent patterns throughout

### Content Organization → Information Flow
**Logical progression**: General → specific information flow
**Grouped content**: Related elements clustered | **Clear purpose**: Each section serves evident function
**Reference access**: Links and cross-references well-organized

## Validation Protocol

### Pre-Commit Checklist
- [ ] Headers follow correct hierarchy (H1→H2→H3)
- [ ] Lists use consistent format (`-` for bullets)
- [ ] Code uses appropriate backticks
- [ ] Links have descriptive text
- [ ] Correct spacing between sections
- [ ] No anti-patterns present

### Readability Verification
- [ ] Clear visual structure when scanning
- [ ] Descriptive and useful headers
- [ ] Easy content navigation
- [ ] Functional references and links

## Integration Standards

### ce-simple Specific → System Compliance
**Internal references**: Use `[Title](docs/path/file.md)` syntax for regular docs | **Commands**: `/command-name` in backticks
**Conditional instructions**: `**IF condition** → READ docs/path/file.md` pattern for workflows
**@ Import restriction**: @ syntax reserved for CLAUDE.md files only
**Documentation**: All `.md` files follow these standards exactly

### Tool Integration → Quality Assurance
**Preview validation**: Check with Markdown preview before commit
**Linting**: Use markdownlint when available | **Consistency**: Review related documents
**Compliance**: This document exemplifies all standards it defines

---

## See Also
- **[Communication Rules](communication-rules.md)** - Language & tone requirements
- **[Documentation Standards](documentation-standards.md)** - Content structure & limits
- **[Context Compaction](../standards/context-compaction-techniques.md)** - Formatting optimization
- **[System Navigation](../navigation/index.md)** - Complete system access hub
- **[Git Workflow](git-workflow-protocols.md)** - Version control integration

**Application**: Apply to ALL Markdown files → Validate before commit → Prioritize readability and official Markdown standard adherence