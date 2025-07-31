# Worktree Accessibility Patterns - Claude Code Security Integration

**31/07/2025** | Claude Code security constraint patterns and dual-worktree architecture

## AUTORIDAD SUPREMA
↑ @context/architecture/claude_code/README.md → worktree-accessibility-patterns.md implements Claude Code worktree access patterns per security discovery

## PRINCIPIO FUNDAMENTAL
**"Dual-worktree architecture preserves both isolation and accessibility"** - External worktrees for isolation, internal worktrees for Claude Code accessibility, with systematic fallback protocols.

## CLAUDE CODE SECURITY CONSTRAINTS DISCOVERY

### **Security Limitation Pattern**
**Constraint**: Claude Code can only access files within current working directory tree
**Impact**: External git worktrees (created outside project directory) become inaccessible
**Discovery Context**: emergency-critical-files worktree at `/Users/nalve/ce-simple-emergency-critical` was inaccessible despite being valid git worktree

### **Access Pattern Matrix**
```
Worktree Location          | Claude Code Access | Isolation Level | Use Case
---------------------------|--------------------|-----------------|-----------
External (../project-name) | ❌ BLOCKED        | HIGH           | Full isolation
Internal (./worktrees/)    | ✅ FULL ACCESS   | MEDIUM         | Tool accessibility
Conversation (./.conv-*)   | ✅ FULL ACCESS   | LOW            | Session isolation
```

## DUAL-WORKTREE ARCHITECTURE PATTERN

### **Architecture Components**
1. **External Worktrees**: `../project-external-worktree` for complete isolation
2. **Internal Worktrees**: `./worktrees/internal-worktree` for Claude Code accessibility
3. **Conversation Workspaces**: `./.conversation-workspaces/conv-*` for session isolation

### **Decision Logic**
```bash
IF task_requires_claude_code_access:
    USE internal_worktree (./worktrees/)
ELIF complete_isolation_needed:
    USE external_worktree (../project-name)
ELSE:
    USE conversation_workspace (./.conversation-workspaces/)
```

### **Implementation Pattern**
- **Primary Strategy**: External worktrees for maximum isolation
- **Fallback Strategy**: Internal worktrees when Claude Code access required
- **Recovery Strategy**: Manual change extraction when external becomes inaccessible

## RECOVERY PATTERNS

### **Uncommitted Change Recovery**
1. **Detection**: `git -C external-worktree status --porcelain`
2. **Extraction**: `git -C external-worktree diff` to capture changes
3. **Application**: Apply changes to accessible worktree or main branch
4. **Cleanup**: `git worktree remove external-worktree --force`

### **Orphaned Worktree Cleanup**
- **Detection**: `git worktree list` vs directory existence
- **Cleanup**: `git worktree prune` + manual directory removal
- **Prevention**: Always use cleanup scripts for worktree management

## INTEGRATION REFERENCES

### ← context/architecture/claude_code/branch-per-conversation-patterns.md
**Connection**: Worktree accessibility complements branch-per-conversation methodology
**Protocol**: Accessibility patterns enable effective branch isolation strategies

### ←→ scripts/infrastructure/conversation-workspace.sh
**Connection**: Implementation of dual-worktree patterns through enhanced script functionality
**Protocol**: Script provides both external and internal worktree creation capabilities

---

**ACCESSIBILITY PATTERNS DECLARATION**: This pattern documentation captures Claude Code security constraints discovery and dual-worktree architecture solution, providing systematic approach to worktree accessibility while preserving isolation capabilities.

**DISCOVERY CONTEXT**: Pattern emerged from session addressing inaccessible external worktrees containing uncommitted changes, leading to systematic solution architecture.