# Script Detection Logic - Missing Script Detection Framework

**Module**: fallback-command/script-detection-logic.md  
**Parent**: H-FALLBACK-COMMAND.md  
**Purpose**: Missing script detection and identification system

## MISSING SCRIPT DETECTION

### Detection Framework
- **Scan command references**: Buscar todas las referencias a `scripts/` en comandos
- **Verify script existence**: Check si script existe y es executable
- **Dependency analysis**: Identificar scripts que dependen de otros scripts
- **External dependency check**: Verificar herramientas externas (gh, git, etc.)

### Detection Triggers
- **Command execution failure**: Cuando comando falla por script missing
- **Proactive scanning**: Periodic check de script availability
- **User request**: Manual invocation para script validation
- **Hook failure**: Cuando Claude hooks fallan por script missing

## INTEGRATION REFERENCES

**Parent Hub**: ← H-FALLBACK-COMMAND.md (fallback command authority)
**Stub Creation**: → stub-creation-strategy.md (creation protocols)
**Architecture**: → fallback-command-architecture.md (command structure)

---

**PURPOSE**: Complete script detection logic ensuring missing scripts are identified and handled gracefully.