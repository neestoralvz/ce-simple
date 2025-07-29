# Next Action Logic - Reference Index

**Pure Reference-Only** | Navegación workflow automation patterns

## Next Action Component References

### Core Framework & Logic Categories
→ **context/operational/patterns/next_action_framework.md:5-12** (core principles workflow continuity)
→ **context/operational/patterns/next_action_framework.md:16-25** (automatic progression criteria + examples)
→ **context/operational/patterns/next_action_framework.md:29-38** (recommended progression patterns)
→ **context/operational/patterns/next_action_framework.md:42-51** (context-aware routing logic)

### Command Category Implementation
→ **context/operational/patterns/next_action_command_patterns.md:5-17** (roles commands next action)
→ **context/operational/patterns/next_action_command_patterns.md:21-35** (actions commands patterns)
→ **context/operational/patterns/next_action_command_patterns.md:39-50** (workflows commands logic)

### Methodology Integration Patterns  
→ **context/operational/patterns/next_action_methodology_integration.md:5-17** (analysis methodologies)
→ **context/operational/patterns/next_action_methodology_integration.md:21-32** (execution methodologies)
→ **context/operational/patterns/next_action_methodology_integration.md:36-47** (validation methodologies)
→ **context/operational/patterns/next_action_methodology_integration.md:51-64** (methodology chain logic)

### Context Awareness & Workflow Continuity
→ **context/operational/patterns/next_action_context_awareness.md:5-19** (context detection logic)
→ **context/operational/patterns/next_action_context_awareness.md:23-33** (error context handling)
→ **context/operational/patterns/next_action_context_awareness.md:37-48** (workflow continuity validation)
→ **context/operational/patterns/next_action_context_awareness.md:52-73** (logic evolution + pattern recognition)

## Quick Access Logic Patterns

### Progression Decision Matrix
- **Automatic**: Unambiguous conditions, single logical step, system state changes
- **Recommended**: Multiple options exist, user choice valuable, context adaptation beneficial
- **Context-Aware**: Environment-dependent routing (orchestrator vs direct execution)

### Command Category Quick Reference
- **Roles consultation**: Return insights → user/orchestrator decision
- **Roles execution**: Delegate → complete → /workflows:close 
- **Actions creation**: /actions:git (automatic after changes)
- **Actions processing**: /methodology:validation_protocol (automatic)
- **Workflows session**: User choice (start) or cleanup (close)
- **Workflows investigation**: /actions:build (recommended for findings)

### Context Detection Triggers
- **Task tool invocation**: Orchestrator delegation → return structured results
- **Direct user execution**: User command → suggest next productivity step
- **Session position**: Beginning/middle/ending → appropriate workflow routing
- **Error conditions**: Recoverable/system/authority → specialized resolution

### Methodology Integration Logic
- **Analysis complete**: Return to invoking command with insights
- **Execution enhanced**: Continue with methodology applied
- **Validation results**: Route based on pass/fail/conflict status
- **Methodology chains**: Sequential application for complex workflows

## Validation Criteria Framework
- **No dead ends**: Every command has appropriate next action
- **No infinite loops**: Chains eventually reach completion
- **Context consistency**: Actions respect execution environment
- **User agency preserved**: Automatic only when unambiguous

---
**Complete Logic**: Load all 4 reference modules para comprehensive automation understanding
**Command Templates**: → context/system/templates/commands/template_index.md
**Orchestrator Integration**: → context/operational/patterns/orchestrator_methodology.md