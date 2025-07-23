# CLAUDE.md Import Strategies - Learning Capture

**Research Date**: 2025-07-23  
**Context**: Optimization of CLAUDE.md file efficiency and import capabilities  
**Status**: Critical learning - implementation required

## Key Discovery

**CLAUDE.md supports native @ import syntax** for including complete file contents automatically when Claude Code CLI starts sessions.

## Research Findings

### Native @ Import Syntax (Claude Code CLI)

```markdown
# CLAUDE.md with real imports
@docs/core/project-structure.md
@docs/commands/command-index.md
@docs/standards/command-standards.md
```

**Capabilities**:
- ✅ **Automatic inclusion** - File contents loaded into context at session start
- ✅ **Native support** - Built into Claude Code CLI
- ✅ **Token efficient** - Content included once, not duplicated
- ✅ **Dynamic updates** - Changes in imported files reflected automatically

### Dynamic # Integration

```markdown
# During session, press # to add content automatically
# Claude incorporates instructions into relevant CLAUDE.md
```

**Workflow**:
- Press `#` during conversation
- Claude adds content to appropriate CLAUDE.md file
- Team benefits from shared improvements via git commits

### File Placement Strategy

**Hierarchy** (Claude searches in order):
1. `./CLAUDE.md` - Project-specific (most common)
2. `./CLAUDE.local.md` - Local-only (.gitignored)
3. Parent directories - For monorepos
4. Child directories - On-demand loading
5. `~/.claude/CLAUDE.md` - Global defaults

## Current Implementation Gap

**ce-simple project**: Currently using Markdown references instead of @ imports

### Before (References - 90 lines)
```markdown
[Ver estructura completa →](docs/core/project-structure.md)
[Ver índice completo de comandos →](docs/commands/command-index.md)
```

### After (@ Imports - Projected ~40 lines + full content access)
```markdown
@docs/core/project-structure.md
@docs/commands/command-index.md
```

## Efficiency Analysis

### Token Budget Impact
- **References**: User must manually click/read separate files
- **@ Imports**: Complete content automatically available in Claude's context
- **Result**: Better AI understanding, no manual navigation required

### Maintenance Benefits
- **Single source of truth**: Changes in imported files automatically reflected
- **No duplication**: Content defined once, used everywhere
- **Team coordination**: All team members get consistent context

## Implementation Strategy

### Phase 1: Convert High-Value Imports
```markdown
@docs/core/project-structure.md      # Complete project structure
@docs/commands/command-index.md      # All command listings
@docs/standards/command-standards.md # Development standards
```

### Phase 2: Strategic Content Organization
- Keep essential overview in main CLAUDE.md
- Import detailed specifications from organized files
- Maintain progressive disclosure through import hierarchy

### Phase 3: Team Adoption
- Document @ import best practices
- Update documentation standards
- Train team on dynamic # content addition

## MDX Alternative Research

**MDX Transclusion** (For non-Claude environments):
```mdx
import ProjectStructure from './docs/core/project-structure.md'
<ProjectStructure />
```

**Conclusion**: @ imports are superior for Claude Code CLI usage, MDX better for web documentation.

## Next Steps

1. **Implement @ imports** in ce-simple CLAUDE.md
2. **Document best practices** in standards
3. **Measure efficiency gains** in token usage and context quality
4. **Capture patterns** for future projects

## Success Metrics

- **CLAUDE.md size reduction**: Target <50 lines core content
- **Context completeness**: All essential info available without navigation
- **Team adoption**: Consistent usage across development sessions
- **Maintenance efficiency**: Single-point updates, automatic propagation

---

**Critical Learning**: @ import syntax transforms CLAUDE.md from static reference to dynamic context engine, enabling truly efficient AI-assisted development workflows.