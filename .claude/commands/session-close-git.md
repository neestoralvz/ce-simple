---
contextflow:
  purpose: "Universal git commit workflow for session closure with comprehensive traceability"
  parent-command: "session-close"
  auxiliary: true
  input-format: "execution-results"
  execution-mode: "git-workflow"
  research-driven: false
---

# Auxiliary Command `/session-close-git`

## Purpose
Execute enhanced git commit workflow with comprehensive session change documentation and traceability.

## Git Workflow Execution

### Phase 1: Git Status Assessment
```bash
def assess_git_status():
    # Check current git status for modified files
    git status
    
    # Identify session-related changes
    modified_files = identify_session_modified_files()
    new_files = identify_session_created_files()
    
    return {
        'modified_commands': filter_command_changes(modified_files),
        'new_narratives': filter_narrative_files(new_files),
        'handoff_changes': filter_handoff_changes(modified_files, new_files),
        'claude_md_updated': check_claude_md_changes(modified_files)
    }
```

### Phase 2: Smart File Addition
```bash
def execute_smart_git_add(session_changes):
    # Add command-related changes
    for command in session_changes.modified_commands:
        git add .claude/commands/{command}
    
    # Add CLAUDE.md if modified
    if session_changes.claude_md_updated:
        git add CLAUDE.md
    
    # Smart handoff git handling
    current_date = $(TZ='America/Mexico_City' date +'%Y-%m-%d')
    master_handoff = f"handoff/{current_date}_master-consolidated.md"
    
    if file_exists(master_handoff):
        git add {master_handoff}
        # Add archive directory if created
        if directory_exists(f"handoff/archive/{current_date}/"):
            git add handoff/archive/{current_date}/
    else:
        # Add individual handoff files
        for handoff in session_changes.handoff_changes:
            git add {handoff}
    
    # Add new conversation narrative
    for narrative in session_changes.new_narratives:
        git add narratives/raw/conversations/{narrative}
```

### Phase 3: Enhanced Commit Message Generation
```python
def generate_enhanced_commit_message(execution_results):
    timestamp_mx = $(TZ='America/Mexico_City' date +'%Y-%m-%d %H:%M')
    session_theme = execution_results.analysis.theme
    
    # Handoff management status
    current_date = $(TZ='America/Mexico_City' date +'%Y-%m-%d')
    master_handoff_exists = file_exists(f"handoff/{current_date}_master-consolidated.md")
    handoff_status = "Updated" if master_handoff_exists else "Created"
    
    # Count archived sessions if applicable
    archived_sessions = count_archived_sessions(current_date) if master_handoff_exists else 0
    
    commit_message = f"""Session {timestamp_mx}: {session_theme}

Handoff Management:
- Master consolidated: {handoff_status}
- Sessions archived: {archived_sessions} individual handoffs consolidated
- Archive status: Clean handoff directory maintained

Command updates applied:"""
    
    # Add command changes
    for change in execution_results.updates.command_changes:
        commit_message += f"\n- {change.command}: {change.description}"
    
    commit_message += "\n\nUser decisions implemented:"
    
    # Add user decisions
    for decision in execution_results.analysis.decisions_made:
        commit_message += f"\n- {decision}"
    
    commit_message += "\n\n🤖 Generated with Claude Code\nCo-Authored-By: Claude <noreply@anthropic.com>"
    
    return commit_message
```

### Phase 4: Git Commit Execution
```bash
def execute_enhanced_git_commit(execution_results):
    commit_message = generate_enhanced_commit_message(execution_results)
    
    # Use HEREDOC for proper formatting
    git commit -m "$(cat <<'EOF'
{commit_message}
EOF
)"
    
    return {
        'commit_successful': True,
        'commit_hash': get_latest_commit_hash(),
        'files_committed': count_committed_files(),
        'commit_message': commit_message
    }
```

## Git Workflow Benefits

### Comprehensive Traceability
- **Session Changes**: All command modifications documented
- **User Decisions**: Direct user voice preservation in commit history
- **Handoff Management**: Smart consolidation tracking
- **Archive Management**: Clean directory maintenance documented

### Enhanced Commit Messages
```bash
# Example Enhanced Commit Message
Session 2025-07-28 15:45: Command Factorization Implementation

Handoff Management:
- Master consolidated: Updated
- Sessions archived: 3 individual handoffs consolidated
- Archive status: Clean handoff directory maintained

Command updates applied:
- session-close.md: Modular factorization applied
- session-close-analysis.md: Created auxiliary command
- session-close-direct.md: Created orchestrator mode
- session-close-subagent.md: Created subagent mode
- session-close-git.md: Created git workflow module

User decisions implemented:
- "comandos son muy largos y eso no debería de ser así"
- "es necesario factorizar mucho"
- Modular factorization following user vision authority

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>
```

## Implementation Flow
```python
def execute_session_close_git(execution_results):
    # Step 1: Assess current git state
    git_status = assess_git_status()
    
    # Step 2: Smart file addition based on session changes
    execute_smart_git_add(git_status)
    
    # Step 3: Generate comprehensive commit message
    commit_message = generate_enhanced_commit_message(execution_results)
    
    # Step 4: Execute git commit with enhanced documentation
    commit_result = execute_enhanced_git_commit(execution_results)
    
    return {
        'git_workflow_completed': True,
        'commit_result': commit_result,
        'traceability_maintained': True,
        'session_closure_finalized': True
    }
```

## Output Structure
```json
{
  "git_workflow_completed": true,
  "commit_details": {
    "commit_hash": "...",
    "files_committed": 5,
    "commit_message_lines": 15,
    "traceability_score": "comprehensive"
  },
  "handoff_management": {
    "consolidation_applied": true,
    "archive_management": "completed",
    "directory_cleanup": true
  },
  "session_closure": {
    "status": "finalized",
    "changes_documented": true,
    "user_voice_preserved": true
  }
}
```

## Integration Points
- **INPUT**: Execution results from session-close-direct/subagent
- **OUTPUT**: Finalized session closure with git commit completion
- **NEXT**: Session closure complete - ready for new session context

---
**Function**: Universal git workflow ensuring comprehensive session change traceability