# Validation Checklist - Autocontainment Criteria Framework

**31/07/2025** | L2-MODULAR extraction from H-AUTOCONTAINMENT-VALIDATION.md

## AUTORIDAD SUPREMA
@context/roadmap/H-AUTOCONTAINMENT-VALIDATION.md → autocontainment-validation/validation-checklist.md implements validation criteria per autocontainment authority

## AUTOCONTAINMENT VALIDATION CHECKLIST

### **Validation Criteria per Command**

#### **✅ Zero External References**
- No `@context/` references en content
- No `scripts/` references en execution paths
- No external file dependencies
- No absolute path references outside `.claude/commands/`

#### **✅ Embedded Context Complete**
- All necessary context embedded within command
- Core principles y templates included internally
- Decision logic self-contained
- Authority chain embedded sin external links

#### **✅ Graceful Degradation**
- Manual alternatives embedded para automation failures
- Fallback procedures included within command
- Error handling que no depende de external resources
- Recovery instructions autocontenidas

#### **✅ Functional Independence**
- Command executes completely standalone
- No dependencies on external scripts
- No required setup outside command execution
- Complete functionality without external files

## VALIDATION FRAMEWORK

### **Commands Scope**
- **Comandos a validar**: /core dispatcher + 6 subcomandos + /script-fallback
- **Restricción crítica**: NO references a `@context/`, `scripts/`, o external files
- **Objetivo**: Complete compliance con autocontainment requirement
- **Standard**: Comandos deben funcionar completamente standalone

### **Compliance Requirements**
- **Zero External Dependencies**: Complete functional independence from external resources
- **Embedded Completeness**: All necessary context and logic contained within commands
- **Fallback Integration**: Manual alternatives and error handling embedded
- **Standalone Execution**: Full functionality without external file dependencies

---

**VALIDATION CHECKLIST AUTHORITY**: Complete autocontainment validation criteria framework preserving systematic compliance assessment through specialized validation requirements per L2-MODULAR extraction methodology.