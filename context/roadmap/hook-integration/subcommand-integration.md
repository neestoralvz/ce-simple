# Subcommand Integration - Hook-Command Coordination

**Module**: hook-integration/subcommand-integration.md  
**Parent**: H-HOOK-INTEGRATION.md  
**Purpose**: Hook and subcommand coordination protocols

## HOOK-SUBCOMMAND COORDINATION

### Coordination Protocol

- **pre-conversation hook** coordinates with `/core-workspace`
- **post-conversation hook** coordinates with `/core-finalize`  
- **post-edit hook** coordinates with `/core-validate`

### Integration Framework

**Hooks run automatically**: Background automation layer
**Subcommands handle explicit operations**: User-initiated actions
**Fallback coordination**: Subcommands provide manual alternatives cuando hooks fail
**State sharing**: Hooks y subcommands share status via log files

### Coordination Implementation

- **Automatic Background Layer**: Hooks provide invisible automation
- **Manual Operation Layer**: Subcommands handle explicit user actions
- **Fallback Coordination**: Seamless fallback when automation fails
- **State Synchronization**: Shared status via standardized log files

## INTEGRATION REFERENCES

**Parent Hub**: ← H-HOOK-INTEGRATION.md (hook system integration authority)
**Implementation Strategy**: → implementation-strategy.md (hook design patterns)
**Fallback Framework**: → fallback-framework.md (degradation protocols)

---

**PURPOSE**: Hook and subcommand coordination protocols with state sharing and fallback mechanisms.