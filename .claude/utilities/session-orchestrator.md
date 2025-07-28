# Session Orchestrator Utility

## Purpose
Standardized patterns for session orchestration workflows including handoff generation, file management, and git integration.

## Core Orchestration Functions

### 1. Smart Handoff Consolidation Logic
```python
def execute_smart_handoff_consolidation(analysis_results, timestamp_mx, consolidation_mode="auto"):
    """
    Universal handoff consolidation logic for both direct and subagent modes.
    
    Args:
        analysis_results: Analysis output from session-close-analysis
        timestamp_mx: Mexico timezone timestamp
        consolidation_mode: "orchestrator_direct" | "subagent_comprehensive" | "auto"
    
    Returns:
        handoff_result: Consolidated handoff with archive management
    """
    current_date = get_current_date_mx()
    master_handoff_path = f"handoff/{current_date}_master-consolidated.md"
    
    # Check for existing handoffs to consolidate
    existing_handoffs = scan_existing_handoffs(current_date)
    
    if existing_handoffs and len(existing_handoffs) > 0:
        # Consolidation required
        consolidated_content = generate_consolidated_handoff(
            existing_handoffs, 
            analysis_results,
            consolidation_mode
        )
        
        # Archive existing handoffs
        archive_result = archive_existing_handoffs(existing_handoffs, current_date)
        
        # Create master consolidated
        create_master_handoff(master_handoff_path, consolidated_content)
        
        return {
            'handoff_path': master_handoff_path,
            'consolidation_applied': True,
            'sessions_consolidated': len(existing_handoffs),
            'archive_result': archive_result,
            'handoff_status': 'consolidated'
        }
    else:
        # No consolidation needed - create individual handoff
        individual_handoff_path = f"handoff/{timestamp_mx}_{analysis_results.theme}.md"
        handoff_content = generate_individual_handoff(analysis_results, consolidation_mode)
        
        create_individual_handoff(individual_handoff_path, handoff_content)
        
        return {
            'handoff_path': individual_handoff_path,
            'consolidation_applied': False,
            'sessions_consolidated': 0,
            'archive_result': None,
            'handoff_status': 'individual'
        }
```

### 2. Universal File Generation Patterns
```python
def execute_session_file_generation(analysis_results, timestamp_mx, execution_mode):
    """
    Universal file generation for both execution modes.
    
    Returns:
        file_generation_result: Complete file generation status
    """
    files_generated = []
    
    # 1. Narrative file creation
    narrative_path = f"narratives/raw/conversations/{timestamp_mx}_{analysis_results.theme}.md"
    narrative_content = generate_narrative_content(
        analysis_results.conversation_content,
        analysis_results.analysis,
        analysis_results.command_changes,
        execution_mode
    )
    
    create_narrative_file(narrative_path, narrative_content)
    files_generated.append(narrative_path)
    
    # 2. Smart handoff generation
    handoff_result = execute_smart_handoff_consolidation(
        analysis_results, 
        timestamp_mx, 
        f"{execution_mode}_mode"
    )
    files_generated.append(handoff_result.handoff_path)
    
    return {
        'narrative_created': True,
        'narrative_path': narrative_path,
        'handoff_result': handoff_result,
        'files_generated': files_generated,
        'generation_mode': execution_mode
    }
```

### 3. Command Update Application Patterns
```python
def execute_universal_command_updates(analysis_results, execution_mode):
    """
    Universal command update application for both modes.
    
    Returns:
        update_result: Command update application status
    """
    if not analysis_results.command_changes:
        return {
            'updates_applied': False,
            'changes_count': 0,
            'claude_md_updated': False
        }
    
    applied_changes = []
    
    # Apply command changes
    for change in analysis_results.command_changes:
        if change.type == 'create':
            result = execute_command_creation(change.specs)
            applied_changes.append(result)
        elif change.type == 'modify':
            result = execute_command_modification(change.target, change.updates)
            applied_changes.append(result)
        elif change.type == 'claude_md_update':
            result = update_claude_md_with_decisions(change.decisions)
            applied_changes.append(result)
    
    return {
        'updates_applied': True,
        'changes_count': len(applied_changes),
        'applied_changes': applied_changes,
        'claude_md_updated': any(change.type == 'claude_md_update' for change in analysis_results.command_changes)
    }
```

### 4. Session Analysis Consolidation
```python
def consolidate_session_analysis(analysis_input, execution_mode):
    """
    Universal session analysis consolidation for both modes.
    
    Returns:
        consolidated_analysis: Unified analysis structure
    """
    if execution_mode == "orchestrator_direct":
        # Direct integrated analysis
        return {
            'theme': extract_primary_topic(analysis_input.conversation_content),
            'category': classify_session_type(analysis_input.conversation_content),
            'commands_mentioned': scan_command_mentions(analysis_input.conversation_content),
            'decisions_made': extract_system_changes(analysis_input.conversation_content),
            'voice_quotes': preserve_exact_user_quotes(analysis_input.conversation_content),
            'command_changes': detect_command_modifications(analysis_input.conversation_content),
            'execution_mode': 'direct'
        }
    else:
        # Requires Task tools deployment - placeholder for subagent results consolidation
        return {
            'analysis_method': 'subagent_deployment_required',
            'task_tools_count': 4,
            'execution_mode': 'subagent',
            'consolidation_deferred': True
        }
```

## Integration Patterns

### Mode-Agnostic Workflow
```python
def execute_universal_session_closure(analysis_input):
    """
    Universal session closure workflow supporting both execution modes.
    """
    # Step 1: Detect execution mode
    execution_mode = detect_execution_context(analysis_input.conversation_context)
    
    # Step 2: Mode-specific analysis
    analysis_results = consolidate_session_analysis(analysis_input, execution_mode)
    
    # Step 3: Universal command updates
    update_results = execute_universal_command_updates(analysis_results, execution_mode)
    
    # Step 4: Universal file generation
    file_results = execute_session_file_generation(analysis_results, analysis_input.timestamp_mx, execution_mode)
    
    return {
        'execution_mode': execution_mode,
        'analysis': analysis_results,
        'updates': update_results,
        'files': file_results,
        'ready_for_git': True
    }
```

## Utility Functions

### Date and Timestamp Management
```python
def get_current_date_mx():
    return $(TZ='America/Mexico_City' date +'%Y-%m-%d')

def get_current_timestamp_mx():
    return $(TZ='America/Mexico_City' date +'%Y-%m-%d_%H-%M')
```

### File Management
```python
def scan_existing_handoffs(current_date):
    return glob(f"handoff/{current_date}_*.md") - [f"handoff/{current_date}_master-consolidated.md"]

def archive_existing_handoffs(handoff_files, current_date):
    archive_dir = f"handoff/archive/{current_date}/"
    ensure_directory_exists(archive_dir)
    
    for handoff in handoff_files:
        move_file(handoff, f"{archive_dir}{basename(handoff)}")
    
    return {
        'archived_count': len(handoff_files),
        'archive_directory': archive_dir
    }
```

---
**Function**: Universal session orchestration utilities supporting both execution modes