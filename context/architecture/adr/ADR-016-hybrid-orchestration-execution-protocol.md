# ADR-016: Hybrid Orchestration-Execution Protocol - Navigation Hub

**Status**: ✅ ACCEPTED | **Date**: 2025-07-30 | **Category**: Process & Methodology
**Decision**: Implementar protocolo híbrido que diferencia capacidades orquestador vs ejecutor

## AUTORIDAD SUPREMA
@context/architecture/core/truth-source.md → ADR-016 implements hybrid protocol resolving operational blocking per architectural decision authority

## DECISION SUMMARY
**Hybrid Protocol Architecture** resolving fundamental conflict between mandatory orchestration and subagent execution capabilities through intelligent level differentiation.

### **PROTOCOL ARCHITECTURE MODULES**

```markdown
Hybrid Orchestration-Execution Protocol System:
├─ **Orchestration Core** → adr-016-modules/orchestration-core/
│   ├─ Orquestador level technical capabilities
│   ├─ Mandatory orchestration responsibilities
│   ├─ Complex task evaluation protocols
│   └─ Systematic coordination frameworks
├─ **Execution Protocols** → adr-016-modules/execution-protocols/
│   ├─ Subagent level technical capabilities
│   ├─ Direct execution responsibilities
│   ├─ Autonomous delegation frameworks
│   └─ Implementation tool protocols
├─ **Hybrid Coordination** → adr-016-modules/hybrid-coordination/
│   ├─ Orquestación vs Ejecución decision matrix
│   ├─ Intelligent transition protocols
│   ├─ Problem identification and resolution
│   └─ Coordination benefits and rationale
└─ **Validation Frameworks** → adr-016-modules/validation-frameworks/
    ├─ Technical, process, and quality validation
    ├─ Operational and business success metrics
    ├─ Risk mitigation strategies
    └─ Continuous improvement protocols
```

## USAGE PROTOCOL

### **Navigation to Specialized Modules**
- **Orchestration Core**: → adr-016-modules/orchestration-core/ for orquestador capabilities and responsibilities
- **Execution Protocols**: → adr-016-modules/execution-protocols/ for subagent execution frameworks
- **Hybrid Coordination**: → adr-016-modules/hybrid-coordination/ for intelligent decision matrix and transition logic
- **Validation Frameworks**: → adr-016-modules/validation-frameworks/ for success metrics and quality assurance

### **Problem Resolution Framework**
**Conflicto Técnico Fundamental** resolved through specialized modules:
- Subagentes NO pueden usar Task tools → Execution Protocols module
- Orquestación sistemática requerida → Orchestration Core module  
- Decision complexity management → Hybrid Coordination module
- Quality preservation across levels → Validation Frameworks module

## INTEGRATION REFERENCES

### Authority Chain
← **@context/architecture/core/truth-source.md** (architectural decision authority)
→ **adr-016-modules/** (specialized protocol modules)

### Related Decisions
←→ **ADR-011**: Mandatory Operational Protocol Enforcement (base sistemática preservada)
←→ **@context/architecture/patterns.md** (orchestration pattern integration)

---

**ADR-016 DECLARATION**: This navigation hub implements hybrid orchestration-execution protocol through specialized modular architecture, resolving operational blocking while preserving systematic excellence and achieving ≤80 line compliance per architectural decision authority.

**SUCCESS VALIDATION**: Elimina bloqueos sistémicos enabling both systematic excellence and operational efficiency through intelligent level differentiation.