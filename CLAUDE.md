# CLAUDE.md - Multi-Subagent Intelligence Dispatcher

```import
@/.claude/commands/master-plan.md
@/.claude/commands/contextflow-agent.md
@/.claude/commands/context/methodology-core.md
@/.claude/commands/context/system-architecture.md
```

## IMPERATIVO OPERACIONAL

**VOZ DEL USUARIO = FUENTE DE VERDAD ABSOLUTA** - Preservación exacta de decisiones originales.

**ORQUESTACIÓN OBLIGATORIA** - Agente principal NUNCA ejecuta trabajo directo. SIEMPRE despliega subagentes especializados via Task tools.

**COMMUNICATION RULES** - NUNCA bash para comunicar. Solo main agent comunica al usuario. Subagents NUNCA direct communication.

**ANTI-BIAS ENFORCEMENT** - Redacción agnóstica, neutra. NO adjetivos descriptivos. NO sesgos lingüísticos que influencien LLM behavior.

**PARALLEL TASK TOOLS** - SIEMPRE priorizar Task tools concurrentes en mismo mensaje sobre secuenciales.

**THINK X4 METODOLOGÍA** - Think → Think Hard → Think Harder → Super Think para decisiones complejas.

## ÁRBOL DE DECISIÓN PRINCIPAL

### DECISIÓN INMEDIATA: TIPO DE SOLICITUD

**A. ¿Inicio de sesión?** → EJECUTAR: `/start` con handoff auto-loading
**B. ¿Procesamiento narrativo?** → EJECUTAR: `/extract-insights` → `/process-layer`  
**C. ¿Creación documento?** → OBLIGATORIO: `/create-doc` → `/align-doc` → `/verify-doc` (NO excepciones)
**D. ¿Consulta/exploración?** → EJECUTAR: Subagent orchestration apropiada

## WORKFLOW OBLIGATORIO DOCUMENTOS

**ENFORCEMENT TOTAL - NO EXCEPCIONES PERMITIDAS**

1. **`/create-doc`** - Content Specialist deployment (NUNCA crear documentos directamente)
2. **`/align-doc`** - Architecture Validator deployment (OBLIGATORIO architecture validation)
3. **`/verify-doc`** - Quality Assurance deployment (OBLIGATORIO quality gates)

**Auto-chaining**: Workflow secuencial automático con confirmación usuario.
**Violation**: Crear documentos fuera de este workflow está PROHIBIDO.

## ARQUITECTURA MODULAR

### Estructura Self-Contained
```
/.claude/commands/ (ECOSYSTEM COMPLETO)
    ↓ Commands interoperables únicamente
    ↓ Templates + utilities internos
    ↓ Decision trees optimizados
/narratives/ (DESTILACIÓN ORGÁNICA)
/handoff/ (CONTINUIDAD SESIONES)
```

## SESSION CONTINUITY

### **`/start`** - Git + Project Maintenance + Insights Extraction
- **Git status check** + pull latest changes
- **Auto-load handoff** + full context loading
- **Project maintenance**: Gaps, TODOs, commitments + git analysis
- **Auto-extract insights** de conversations + correlate with commits
- **System evolution** recommendations based on patterns
- **Intelligent options** prioritized by maintenance + insights

### **`/session-close`** - Capture + Command Updates + Git Commit
- **Capture conversation** íntegramente preservando voz
- **Detect command changes** mencionados durante sesión
- **Auto-apply updates** a comandos modified/created
- **Git commit** con trazabilidad completa de changes
- **Generate handoff** con applied changes documented

### **Architecture Logic**
```
Session Close: Capture + Apply (fresh memory de cambios)
Session Start: Maintain + Extract (full context para analysis)
```

---

**SISTEMA EVOLUCIONA ORGÁNICAMENTE** preservando user voice como fuente de verdad mientras optimiza automáticamente architecture + efficiency via multi-subagent intelligence.

**Context detallado**: Ver imports automáticos arriba para methodology, architecture, y token economy.