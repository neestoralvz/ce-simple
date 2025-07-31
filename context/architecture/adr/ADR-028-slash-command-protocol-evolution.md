# ADR-028: Slash Command Protocol Evolution

**Date**: 2025-07-31  
**Status**: ACCEPTED  
**Authority**: User UX preference + Claude Code native functionality integration

## Context

Initial implementation referenced file path `@.claude/commands/core.md` directly in CLAUDE.md protocol. During implementation refinement, user suggested evolution to slash command `/core` for better UX and native Claude Code integration.

**Problem Statement**: 
- File path references less elegant than native slash commands
- Claude Code slash commands provide better user experience
- Direct file references bypass Claude Code native functionality
- Opportunity to leverage built-in command infrastructure

## Decision

**EVOLVE TO SLASH COMMAND PROTOCOL OBLIGATORIO** with `/core` as native command invocation replacing file path references.

### Evolution Framework:
1. **Native Integration**: Leverage Claude Code slash command infrastructure
2. **UX Enhancement**: More elegant and natural command invocation  
3. **Functional Optimization**: Direct command execution vs file reference
4. **Syntax Simplification**: `/core` vs `@.claude/commands/core.md`

### Implementation Pattern:
- **critical_instruction**: "ejecutar /core como protocolo OBLIGATORIO"
- **universal_protocol**: "CLAUDE.md → /core → acción solicitada"
- **PROTOCOLO CORE**: "/core OBLIGATORIO → orchestration authority"
- **PRINCIPIO ESENCIAL**: "EJECUTA /core OBLIGATORIO como PRIMER paso"

### Migration Protocol:
- Replace ALL file path references with slash command
- Maintain identical enforcement language and requirements
- Preserve complete functionality while improving syntax
- Update all protocol documentation consistently

## Consequences

### Positive:
- **Enhanced UX**: More natural and elegant command invocation
- **Native Integration**: Leverages Claude Code built-in functionality
- **Simplified Syntax**: Cleaner protocol documentation
- **Better Performance**: Direct command execution pathway

### Negative:
- **Migration Required**: All existing implementations need updating
- **Dependency**: Relies on Claude Code slash command infrastructure

### Risk Mitigation:
- **Backward Compatibility**: File still exists for reference/debugging
- **Clear Migration Path**: Detailed instructions for evolution provided

## Implementation Evidence

**Successful Evolution Validated**: Complete protocol migration executed with:
- ✅ Header critical_instruction updated to `/core`
- ✅ PROTOCOLO CORE references updated consistently  
- ✅ PROTOCOLO UNIVERSAL DE INICIO aligned with slash command
- ✅ PRINCIPIO ESENCIAL MANDATORIO updated throughout
- ✅ All enforcement language preserved during migration

## Compliance Monitoring

**Evolution Protocol**: Slash command invocation OBLIGATORIO maintains all systematic thinking preservation
**Quality Gates**: Command functionality DEBE preserved during syntax evolution
**Standards Integration**: Native Claude Code integration FUNDAMENTAL for user experience optimization

## References

- **Authority Source**: User UX preference + native Claude Code functionality
- **Implementation**: CLAUDE.md complete evolution to `/core` slash command
- **Technical Standards**: Claude Code slash command architecture integration
- **Enforcement**: llm-enforcement-principle.md compliance maintained

---
**EVOLUTION**: Slash command protocol represents UX-driven architectural improvement while preserving complete systematic functionality and enforcement standards.