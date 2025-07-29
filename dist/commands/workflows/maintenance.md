# /workflows:maintenance - Sistema Maintenance Dispatcher

**29/07/2025 12:00 CDMX**

## AUTORIDAD SUPREMA
@context/TRUTH_SOURCE.md → @context/operational/enforcement/anti_monolithic_prevention.md

## CORE FUNCTION
Maintenance sistemático via drift detection + batch recreation coordination

## SEMANTIC TRIGGERS

### System Drift Detection
**Triggers**: Files >80 lines, conceptual duplication, template violations
**Auto-activation**: @context/operational/enforcement/anti_monolithic_prevention.md
**Execute**: Health scan + @context/operational/enforcement/quality_gates.md
**Validate**: /actions:recreate delegation + alignment verification

### Batch Recreation Pattern
**Triggers**: Multiple files requiring alignment, authority conflicts detected  
**Auto-activation**: @context/operational/behaviors/orchestration_protocol.md
**Execute**: Parallel /actions:recreate coordination + Think x4 sequencing
**Validate**: @context/operational/enforcement/behavioral_enforcement.md

### Proactive Maintenance Pattern
**Triggers**: Session start, post-changes, periodic health checks
**Auto-activation**: @context/operational/operations/methodology_protocol.md  
**Execute**: Automated health scanning + priority ranking
**Validate**: @context/operational/enforcement/quality_gates.md

## MAINTENANCE PROTOCOL
1. **Health scan** → drift detection ≥30%
2. **Batch coordination** → /actions:recreate delegation
3. **Integration verification** → system coherence validation
4. **Report generation** → maintenance visibility

## DETECTION RULES
- Files >80 lines → recreation candidates
- Conceptual duplication >2 files → consolidation analysis  
- Template violations → compliance enforcement
- Authority conflicts → immediate recreation priority

## REFERENCIAS CONDICIONALES
**Anti-monolithic enforcement**: @context/operational/enforcement/anti_monolithic_prevention.md
**Quality gates**: @context/operational/enforcement/quality_gates.md
**Orchestration protocol**: @context/operational/behaviors/orchestration_protocol.md
**Recreation integration**: @context/operational/operations/methodology_protocol.md
**Behavioral enforcement**: @context/operational/enforcement/behavioral_enforcement.md

---
**Authority Chain**: TRUTH_SOURCE → enforcement → recreation coordination
**Token Optimization**: Reference-only + automated delegation
**Compliance**: ≤80 lines + reference-only protocol + batch coordination
