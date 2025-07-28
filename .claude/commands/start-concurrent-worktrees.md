---
contextflow:
  purpose: "Multi-conversation parallel orchestration via git worktrees + document coordination"
  methodology: "Ultra-parallel with shared state coordination document"
  auto-research: true
  websearch-integration: true
  mcp-context7-enabled: true
  research-driven: conditional
---

# Comando `/start-concurrent-worktrees` - Ultra-Parallel Multi-Conversation System

## OBLIGATORIO: RESEARCH FIRST PROTOCOL
**SYSTEMATIC INTEGRATION**: Siempre usar WebSearch + MCP Context7 con fecha actual para investigación actualizada antes de ejecución.

### Pre-Execution Research (AUTOMATIC):
```bash
# Get current date for recent research
current_date=$(date)

# WebSearch with current date
WebSearch: "git worktree best practices ${current_date}"
WebSearch: "multi-agent coordination patterns ${current_date}" 
WebSearch: "document-based synchronization ${current_date}"

# MCP Context7 analysis
MCP Context7: "Analyze coordination patterns for parallel development"
```

## Core Imperative
**Usuario como Ultra-Orchestrator** de N conversaciones paralelas concurrentes, cada una con:
- Agente principal independiente capaz de orquestar subagentes
- Git worktree dedicado para aislamiento completo
- Documento de coordinación compartido para sincronización asíncrona

## Arquitectura de Coordinación

### Git Worktree Structure:
```
Main Repo: /Users/nalve/ce-simple (master)
├── worktrees/
│   ├── priority-1-validation/     # Conversación 1
│   ├── priority-2-git-cleanup/    # Conversación 2  
│   ├── priority-3-implementation/ # Conversación 3
│   └── priority-N-custom/         # Conversación N
└── coordination-state.md          # Documento compartido
```

### Document-Based Coordination Bus:
```markdown
# Multi-Conversation Coordination State
**Last Updated**: [timestamp] by [conversation-id]

## Active Conversations Status:
- [1] Validation: [status] | Last: [timestamp] | Next: [actions]
- [2] Git Integration: [status] | Last: [timestamp] | Next: [actions]
- [3] Implementation: [status] | Last: [timestamp] | Next: [actions]

## Shared Decision Context:
### User Voice (IMMUTABLE):
> "[exact user quotes]" - Source: [conversation-thread]

### Cross-Conversation Dependencies:
- Conv1 → Conv3: [dependency description]
- Conv2 → Conv1: [dependency description]

### Resolved Conflicts:
- Issue: [description] | Resolution: [solution] | Applied by: [conv-id]
```

## Task Tools Deployment Protocol

### 1. Worktree Creation Specialist:
```
Task: Worktree Management Specialist
Description: "Create git worktrees with coordination setup"
Subagent: general-purpose
Prompt: "
RESEARCH-DRIVEN EXECUTION:
1. WebSearch current git worktree best practices with date: ${current_date}
2. Create worktree structure based on latest patterns found
3. Initialize coordination-state.md with multi-agent synchronization template
4. Set up cross-conversation communication protocol
5. Validate worktree isolation and shared state access
"
```

### 2. Conversation Starter Generator:
```
Task: Multi-Conversation Template Specialist  
Description: "Generate N conversation starter prompts"
Subagent: general-purpose
Prompt: "
For each priority identified, create conversation starter that includes:
1. WebSearch integration for current best practices
2. MCP Context7 consultation for pattern analysis  
3. Auto-loading of coordination-state.md for context
4. Specialized focus area with clear boundaries
5. Synchronization protocol with shared document updates

Base each starter on research findings from current date: ${current_date}
"
```

### 3. Coordination Protocol Validator:
```
Task: Ultra-Parallel Synchronization Specialist
Description: "Validate cross-conversation coordination mechanisms" 
Subagent: general-purpose
Prompt: "
VALIDATION MISSION:
1. Research latest multi-agent coordination patterns (${current_date})
2. Verify document-based synchronization functionality
3. Test conflict resolution mechanisms
4. Validate shared state management without corruption
5. Confirm isolation between worktrees while enabling communication
"
```

## Conversation Starter Templates

### Priority-Based Conversation Initialization:
```
### Conversation [N]: [PRIORITY_NAME]
**Worktree**: worktrees/[priority-folder]/
**Focus**: [specific area]
**Research Protocol**: WebSearch + MCP Context7 integration mandatory

STARTUP SEQUENCE:
1. cd worktrees/[priority-folder]/
2. Load coordination-state.md for shared context
3. WebSearch: "[priority area] best practices $(date)"
4. MCP Context7: "Analyze [priority area] coordination patterns"
5. Execute specialized work within defined boundaries
6. Update coordination-state.md with progress + decisions
7. Sync critical changes back to main repo when appropriate
```

## Cross-Conversation Communication Protocol

### Asynchronous Updates:
- Each conversation commits updates to coordination-state.md
- Conversations poll shared document for dependency changes  
- Conflict resolution via research-driven best practices
- Critical decisions require cross-conversation validation

### Dependency Management:
- Explicit dependency declarations in coordination document
- Blocking/non-blocking dependency handling
- Automatic notification system via document state changes

## User Interface Recommendations

### Multi-Terminal Setup:
```bash
# Terminal 1: Master coordination
cd /Users/nalve/ce-simple
git worktree list
tail -f coordination-state.md

# Terminal 2-N: Individual conversations  
cd worktrees/priority-X/
# Start Claude Code conversation with priority-specific context
```

### Conversation Management Commands:
- `/status-all`: View all conversation states
- `/sync-state`: Force synchronization of coordination document
- `/resolve-conflicts`: Research-driven conflict resolution
- `/consolidate-results`: Merge work from all conversations

## Success Criteria + Evolution Protocol:
- [ ] N worktrees created with proper isolation
- [ ] Coordination document functioning as communication bus
- [ ] Each conversation has independent agent orchestration capability
- [ ] WebSearch + MCP Context7 integration systematic in all conversations
- [ ] Cross-conversation dependencies managed without conflicts
- [ ] User voice preserved across all parallel conversations
- [ ] Research-first protocol integrated systematically
- [ ] System learns and evolves coordination patterns automatically

## Systematic Integration Notes:
**LEARNED PATTERN**: Always research with current date for updated practices
**LEARNED PATTERN**: WebSearch + MCP Context7 must be systematic, not optional  
**LEARNED PATTERN**: Document-based coordination scales better than direct communication
**LEARNED PATTERN**: Usuario as Ultra-Orchestrator > Multi-Agent > Single Agent hierarchy

---
**Evolution Target**: Self-improving ultra-parallel system that systematically integrates all user feedback into coordination patterns.