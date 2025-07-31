# Implementation Strategy - Dual-Phase Organization Framework

**31/07/2025 12:30 CDMX** | L2-MODULAR extraction from H-SCRIPTS-CLASSIFICATION.md

## AUTORIDAD SUPREMA
@context/roadmap/H-SCRIPTS-CLASSIFICATION.md → scripts-classification/implementation-strategy.md implements dual-phase strategy per classification authority

## DUAL-PHASE IMPLEMENTATION STRATEGY

### **Phase A: Directory Organization & Cleanup**
**Comprehensive scripts ecosystem reorganization with cleanup:**

1. **Functional Categorization**: Organize 29+ scripts into 9 functional directories
2. **Dependency Mapping**: Document script execution order and interdependencies  
3. **Directory Cleanup**: Consolidate 12+ analysis_results directories into single current state
4. **Documentation System**: Create category READMEs plus master navigation guide
5. **Migration Validation**: Test all script functionality after reorganization

### **Phase B: Hook Integration Strategy** 
**Automated lifecycle integration for optimal workflow:**

1. **Lifecycle Classification**: Categorize scripts by execution timing
   - **Pre-conversation hooks**: Scripts executing before conversation initiation
   - **Post-conversation hooks**: Scripts executing after conversation completion  
   - **Post-edit hooks**: Scripts executing after file modifications
   - **On-demand utilities**: Scripts invoked by explicit commands
   - **Batch operations**: Scripts for mass processing workflows

## SCRIPT LIFECYCLE CLASSIFICATION

### **CLAUDE HOOKS CANDIDATES**:
- `conversation-workspace.sh` → **pre-conversation hook**
  - Función: Setup git worktree-based conversation isolation
  - Timing: Antes de iniciar cualquier conversación
  - Integration: `.claude/hooks/pre-conversation.sh`

- `context-extract.sh` → **post-conversation hook**
  - Función: Extract conversation insights para system evolution
  - Timing: Al finalizar conversación exitosa
  - Integration: `.claude/hooks/post-conversation.sh`

- `validate-context-coherence.sh` → **post-edit hook**
  - Función: Validate CLAUDE.md conditional links coherence
  - Timing: Después de editar archivos de contexto
  - Integration: `.claude/hooks/post-edit.sh`

- `quality-gate.sh` → **post-conversation hook**
  - Función: Quality assurance validation
  - Timing: Al finalizar conversación antes de cleanup
  - Integration: `.claude/hooks/post-conversation.sh` (combined with context-extract)

### **UTILITY SCRIPTS (Command-triggered)**:
- `analyze_violations.sh` → **utility script**
  - Función: File size violation analysis para PHASE_0_EMERGENCY
  - Trigger: Comando específico o periodic analysis
  - Integration: Remains in `scripts/` - invoked by commands

- `parallel-tool-manager.sh` → **utility script**
  - Función: Coordination system para parallel tool execution
  - Trigger: Durante orquestación de subagentes
  - Integration: Remains in `scripts/` - used by /core orchestration

## INTEGRATION ARCHITECTURE

### **Hook Integration Architecture**
**Claude Hooks Integration**:
- Combine related scripts in single hooks to reduce overhead
- Create composite hooks (e.g., post-conversation runs both context-extract + quality-gate)
- Ensure hooks fail gracefully when dependencies missing
- Provide fallback manual alternatives

### **Fallback Strategy Design**
- **Hook failures**: Commands should continue with manual alternatives
- **Missing scripts**: Auto-creation of stub scripts with proper interfaces
- **Dependency failures**: Graceful degradation without blocking workflow
- **Manual overrides**: User can disable hooks when needed

---

**IMPLEMENTATION STRATEGY AUTHORITY**: Dual-phase organization framework preserving complete functionality through systematic directory organization and lifecycle integration per L2-MODULAR extraction methodology.