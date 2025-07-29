# Git Worktree Configurations - Multi-Conversation Setup

**29/07/2025** | Consolidated git worktree setup patterns for parallel conversations

## Core Configuration Functions

### Basic Branch Creation
→ Ver context/examples/bash/git_worktree_management.sh:create_conversation_branch() para implementación completa

### Parallel Environment Setup
→ Ver context/examples/bash/git_worktree_management.sh:setup_parallel_conversations() para configuración completa
        git worktree add "../$branch_name" "task-$i"
    done
    
    return 0
}
```

### Quick Parallel Setup
```bash
quick_parallel_setup() {
    echo "Quick setup for parallel conversations"
    
    # Create shared state directory
    mkdir -p shared_state
    
    # Initialize communication files
    touch shared_state/tickets.md
    touch shared_state/status.md
    touch shared_state/priorities.md
    touch shared_state/convergence.md
    
    echo "Parallel conversation environment ready"
    
    return 0
}
```

## Branch Management

### Validation and Isolation
```bash
validate_branch_isolation() {
    local current_branch=$(git branch --show-current)
    echo "Current branch isolation: $current_branch"
    
    # Check for uncommitted changes
    if ! git diff-index --quiet HEAD --; then
        echo "WARNING: Uncommitted changes detected in $current_branch"
        return 1
    fi
    
    echo "Branch isolation validated"
    return 0
}
```

### Cleanup Operations
```bash
cleanup_conversation_branches() {
    echo "Cleaning up conversation branches..."
    
    # List and remove worktrees
    git worktree list | grep -E "(conversation-|task-)" | while read -r path branch _; do
        echo "Removing worktree: $path ($branch)"
        git worktree remove "$path" --force
        git branch -D "$branch" 2>/dev/null || true
    done
    
    return 0
}
```

## Multi-Conversation Communication

### Inter-Conversation Tickets
```bash
send_ticket() {
    local message="$1"
    local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    
    echo "[$timestamp] ticket: $message" >> shared_state/tickets.md
    echo "Ticket sent: $message"
    
    return 0
}
```

### Shared State Structure
```bash
create_shared_state_structure() {
    mkdir -p shared_state
    
    # Create communication files
    echo "# Inter-Conversation Tickets" > shared_state/tickets.md
    echo "# Current Status Across Conversations" > shared_state/status.md
    echo "# Task Priorities" > shared_state/priorities.md
    echo "# Convergence Coordination" > shared_state/convergence.md
    
    echo "Shared state structure created"
    return 0
}
```

## Integration Patterns

### N-Conversation Architecture
- **Branch isolation**: Each conversation operates in separate git worktree
- **Shared coordination**: Communication via shared_state/ directory
- **User orchestration**: User coordinates multiple parallel agents
- **Background monitoring**: Persistent processes track cross-conversation state

### Workflow Integration Commands
- **`/actions:git`** → Git-native worktree management for parallel conversations
- **`/workflows:start`** → Universal ultra-orchestrator entry with multi-conversation assessment
- **`/workflows:close`** → Session capture + multi-conversation convergence

---
**Source Consolidation**: Extracted from context/examples/bash/git_worktree_management.sh + context/operational/operations/architecture_implementation.md + context/operational/patterns/orchestrator_coordination.md

**Usage**: Apply these configurations when setting up parallel conversation environments for complex tasks requiring multi-agent coordination.