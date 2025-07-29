# Multi-Conversation Coordination - Ultra-Orchestrator Configuration

**29/07/2025** | Consolidated multi-conversation coordination protocols and patterns

## Ultra-Orchestrator Architecture

### Core Coordination Principles
- **Usuario como ultra-orchestrator**: User coordinates N parallel agents
- **Branch isolation**: Each conversation operates in separate git worktree
- **Background intelligence**: Persistent processes coordinate communication
- **Authority preservation**: User maintains vision authority while orchestrating

### N-Conversation Management Pattern
```markdown
**User Role Evolution**: From vision-provider to ultra-orchestrator
**Parallel Capability**: Support N conversations (4+ as needed)
**State isolation**: Prevent cross-conversation conflicts
**Integration responsibility**: User determines final system state
```

## Communication Protocols

### Inter-Conversation Ticket System
```markdown
## Ticket Structure
[timestamp] ticket: [message content]

## Communication Files
- shared_state/tickets.md → Inter-conversation messages
- shared_state/status.md → Current state across conversations
- shared_state/priorities.md → Task coordination
- shared_state/convergence.md → Integration coordination
```

### Shared State Management
```bash
# Update shared status template
{
    echo "# Current State Across Conversations"
    echo ""
    echo "## System State"
    echo "- Last update: $(date)"
    echo "- Active processes: $(pgrep -f "background_monitor|conversation_coordinator|communication_daemon" | wc -l)"
    echo "- Current branch: $(git branch --show-current 2>/dev/null)"
    echo ""
    echo "## Active Conversations"
    echo "- Conversation branches: $(git branch --list | grep -E "(conversation-|task-)" | wc -l)"
    echo "- Pending tickets: $(grep -c "ticket:" shared_state/tickets.md 2>/dev/null || echo 0)"
} > shared_state/status.md
```

## Coordination Patterns

### Multi-Conversation Assessment
```markdown
## Trigger Conditions
- **"paralelo", "múltiple"** → multi-Task tools simultáneas
- **>5 independent tasks** → parallel execution consideration
- **Coordination needed** → usuario ultra-orchestrator mode
- **Background work** → inter-conversation tickets system
```

### Branch-Per-Conversation Setup
```bash
# Setup parallel conversation branches
git worktree add ../conversation-branch-1 conversation-1
git worktree add ../conversation-branch-2 conversation-2
git worktree add ../conversation-branch-3 conversation-3
git worktree add ../conversation-branch-4 conversation-4

# Create shared coordination directory
mkdir -p shared_state
```

### Parallel Execution Workflow
```markdown
## Execution Pattern
1. **Task complexity assessment** → Determine if parallelization needed
2. **Branch preparation** → Setup git worktrees for parallel conversations
3. **Conversation spawning** → Launch N conversations (4+ as required)
4. **User ultra-orchestration** → User coordinates parallel agent execution
5. **Background coordination** → Monitoring + inter-conversation communication
6. **Convergent integration** → Authority-preserved results consolidation
```

## Orchestration Commands

### Multi-Conversation Command Set
```markdown
- **`/workflows:start`** → Universal ultra-orchestrator entry with multi-conversation assessment
- **`/actions:git`** → Git-native worktree management for parallel conversations
- **`/workflows:debug`** → Systematic resolution + background process management
- **`/maintain`** → System maintenance + git worktree coordination
- **`/workflows:close`** → Session capture + multi-conversation convergence
```

### Template Multi-Agent Coordination
```markdown
"Agente [X] completado: [RESULTADO] → Agentes [Y,Z] continúan parallel. Estado general: [X/Y] completados."
```

## Quality Management

### Multi-Conversation Quality Gates
- **Independent validation**: Each conversation validates its output
- **Authority hierarchy**: User-vision authority applies across all conversations
- **Challenge system integration**: Problem/solution detection across branches
- **User feedback priority**: Over AI optimization recommendations across conversations

### Convergent Integration Protocol
```markdown
## Integration Steps
1. **Cross-conversation results collection**
2. **Authority alignment verification** (user-vision/TRUTH_SOURCE.md)
3. **Conflict resolution** → Authority hierarchy resolves integration conflicts
4. **Quality validation** → Challenge system integration for final output
5. **System coherence verification** → Complete system integration validated
```

## Emergency Protocol

### Multi-Conversation Emergency Setup
```markdown
1. Setup git worktrees for parallel execution
2. User becomes ultra-orchestrator of conversations
3. Background processes coordinate communication
4. Authority validation at convergence
```

### Recovery Patterns
```bash
# Emergency cleanup all conversations
cleanup_all_conversations() {
    stop_all_background_processes
    cleanup_conversation_branches
    rm -rf shared_state
    echo "Emergency cleanup completed"
}
```

## Integration Architecture

### Background Intelligence Integration
- **Persistent Process Management**: Background processes manage cross-conversation coordination
- **Continuous monitoring**: Maintain system state awareness across conversations
- **Inter-conversation bridge**: Background processes coordinate conversation communication
- **State synchronization**: Maintain coherence across parallel conversations

### Ultra-Orchestrator Success Indicators
- **Zero interrupciones** durante ejecución multi-tarea
- **Notificaciones transparentes** sin pausar flujo
- **Completitud automática** hasta lista vacía
- **Usuario como ultra-orchestrator** efectivo
- **Productivity máxima** sin friction

---
**Source Consolidation**: Extracted from context/operational/patterns/orchestrator_coordination.md + context/operational/operations/architecture_implementation.md + context/operational/enforcement/triggers_semanticos.md

**Usage**: Apply these coordination patterns when implementing multi-conversation parallel execution for complex tasks requiring distributed agent coordination.