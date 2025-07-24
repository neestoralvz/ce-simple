# CLAUDE.md - ce-simple

**Last Updated: 2025-07-24**

## Tech Stack
- **Platform**: Claude Code slash commands
- **Language**: English-only documentation and commands
- **Architecture**: Self-contained commands with Task Tool parallel execution
- **Validation**: PTS (Pragmatic Technical Simplicity) 12-component framework

## Project Structure  
```
ce-simple/
├── CLAUDE_RULES.md          # Partnership protocol (READ FIRST)
├── docs/
│   ├── core/                # PTS framework and development principles  
│   ├── vision/              # System philosophy and technical direction
│   ├── rules/               # Modular rule system (7 rule modules)
│   ├── patterns/            # Dynamic pattern storage with internal timestamps
│   └── governance/          # Modular architecture and quality frameworks
├── export/commands/         # 86 production-ready commands (15 categories)
├── commands/                # 3 essential local commands (init-project, start, explore-codebase)
└── development/             # Prototyping and testing workspace
```

## Commands

### Essential Local Commands
- `/init-project` - Complete project initialization with git and structure
- `/start` - Project analysis and guidance with dynamic questioning  
- `/explore-codebase` - Understand project structure and codebase

### Master Workflow Commands  
- `/master-execute` - Complete workflow orchestration with git integration
- `/git-workflow` - Comprehensive git integration with commit protocols
- `/validate-recursive` - 5-retry validation system with learning capture

### Global Export System
- **86 commands** in export/commands/ organized in 15 categories (00-14)
- **Self-contained**: Commands reference only other commands via slash syntax
- **Deploy**: Copy export/commands/ to global Claude Code directory
- **Reference**: @export/CLAUDE.md for complete command documentation

## Code Style

### Command Development Standards
- **Length Limit**: 150 lines maximum per command
- **Autocontained**: All logic, patterns, templates embedded inline
- **Single Responsibility**: Each command does exactly one thing well
- **PTS Compliance**: Must pass all 12 PTS components before deployment
- **Rule Integration**: Reference modular rule system (@docs/rules/)
- **Pattern Capture**: Utilize dynamic pattern storage (@docs/patterns/)
- **Git Workflow**: Integrated commit protocols with vision-driven development

### Documentation Standards
- **English Only**: Zero tolerance for mixed language content
- **Technical Focus**: No marketing language or unnecessary embellishments  
- **Token Efficiency**: CLAUDE.md content prepended to every prompt
- **Context References**: Link to detailed docs rather than inline expansion

## Testing Requirements

### PTS Validation Framework
```bash
# Pre-development validation (2 minutes)
- [ ] Clear purpose in 30 seconds?
- [ ] Single responsibility only?
- [ ] Simplest solution that works?
- [ ] Works without configuration?

# Complete validation (10 minutes) 
- [ ] All 12 PTS components pass?
- [ ] No blocking criteria present?
- [ ] Metrics meet quantitative thresholds?
```

### Quality Gates
- **PTS Compliance**: 12/12 components must pass (blocking requirement)
- **Length Compliance**: ≤150 lines for commands, ≤200 lines for docs
- **English Standard**: Zero Spanish content in system files
- **Self-Containment**: Commands work without external dependencies

## Documentation Standards

### Authority Hierarchy
1. **CLAUDE_RULES.md** - Partnership protocol (foundation authority)
2. **docs/rules/** - Modular rule system (10 specialized rule modules)
3. **docs/core/development-principles.md** - PTS framework and technical standards
4. **docs/vision/overview.md** - System philosophy and direction
5. **CLAUDE.md** - System overview and navigation (this file)

### Reference System
- **Detailed Architecture**: @docs/core/README.md
- **Modular Rules**: @docs/rules/ (10 specialized rule modules)
- **Pattern Storage**: @docs/patterns/ (dynamic patterns with timestamps)
- **Governance Framework**: @docs/governance/ (modular architecture)
- **PTS Framework**: @docs/core/pts-framework.md  
- **Validation Checklist**: @docs/core/pts-checklist.md
- **Command Patterns**: @export/CLAUDE.md

## Do Not

### Development Constraints
- **No Spanish content** in any system file (English-only standard)
- **No marketing language** in technical documentation  
- **No over-orchestration** - avoid excessive TodoWrite usage
- **No configuration dependencies** - commands must work immediately
- **No command length >150 lines** - enforce strict brevity

### Architecture Violations  
- **No external dependencies** in autocontained commands
- **No cross-command file references** - use slash command calls only
- **No vision document authority override** - docs/vision/ is absolute
- **No PTS compliance bypass** - 12/12 components mandatory
- **No rule module bypass** - modular rule system must be consulted
- **No pattern storage circumvention** - dynamic patterns provide context continuity

### Quality Standards
- **No deployment without validation** - PTS compliance required
- **No mixed authority claims** - clear hierarchy maintained
- **No redundant documentation** - single source of truth principle
- **No theoretical frameworks** - practical value required

## Success Criteria

### Command Quality
- **Autocontainment**: 100% self-contained operation
- **PTS Compliance**: 12/12 components pass validation  
- **Practical Value**: Solves real problems effectively
- **English Standard**: Zero mixed-language violations

### System Performance
- **Execution Speed**: Optimized for parallel Task Tool operation
- **Context Economy**: Efficient token usage in all documentation
- **User Experience**: ≤30 seconds to understand command purpose
- **Integration Success**: Seamless operation across different projects
- **Modular Navigation**: Efficient access through rule/pattern/governance modules
- **Vision Alignment**: All changes traceable to vision-driven development

### Partnership Effectiveness
- **Vision Alignment**: 100% decisions traceable to stated vision
- **Quality Enforcement**: 100% PTS compliance maintained
- **Research Value**: Proactive identification of relevant solutions
- **Structure Integrity**: Zero files out of place, clean organization

---

**Core Principle**: Simple building blocks with single responsibility that orchestrate into complex workflows through intelligent parallel execution.