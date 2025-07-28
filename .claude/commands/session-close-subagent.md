---
contextflow:
  purpose: "Subagent deployment for standard user session closure with comprehensive analysis"
  parent-command: "session-close"
  auxiliary: true
  input-format: "analysis-results"
  execution-mode: "task-tools-deployment"
  research-driven: false
---

# Auxiliary Command `/session-close-subagent`

## Purpose
Execute session closure for standard user context via 4 Task tools deployment for comprehensive analysis.

## Task Tools Deployment Strategy

### Task 1: Research Specialist
```python
Task(
    description="Identify theme, category, and commands mentioned",
    prompt=load_template("research-specialist.md").customize({
        "research_objective": "CONVERSATION ANALYSIS - Extract key elements",
        "domain": "session conversation analysis",
        "topics": [
            "Theme identification (primary/secondary topics, evolution, decision points)",
            "Category classification (document creation, architecture, implementation, planning, analysis, troubleshooting, optimization, user feedback, system evolution, methodology refinement)",
            "Commands detection (explicit mentions, implied commands, modifications discussed, new requirements)"
        ],
        "output_format": "Structured analysis con theme, category, commands inventory",
        "data_inputs": ["conversation_content", "session_context", "timeline"]
    }),
    subagent_type="general-purpose"
)
```

### Task 2: Architecture Validator
```python
Task(
    description="Detect decisions and command changes required",
    prompt=load_template("architecture-validator.md").customize({
        "validation_mission": "DECISION DETECTION - Identify system changes",
        "analysis_scope": [
            "Conversation content and system context",
            "Command ecosystem and existing structure", 
            "User commitments and promises made"
        ],
        "validation_areas": [
            "Explicit decisions (system behavior, architecture changes, methodology updates, command modifications)",
            "Command changes required (create, modify, deprecate, integration updates)",
            "System architecture impact (core changes, rules updates, documentation, integration points)"
        ],
        "output_format": "Decision inventory con specific command change requirements"
    }),
    subagent_type="general-purpose"
)
```

### Task 3: Voice Preservation Specialist
```python
Task(
    description="Extract user voice quotes and command commitments",
    prompt=load_template("voice-preservation.md").customize({
        "preservation_mission": "VOICE EXTRACTION - Preserve user voice exactly",
        "preservation_scope": [
            "Conversation content and user statements",
            "Commitment tracking and promises made",
            "Voice evolution and preference changes"
        ],
        "extraction_requirements": [
            "Exact user quotes (ZERO paraphrasing, complete attribution, context preservation)",
            "Command commitments (explicit promises, implementation timeline, scope agreements)",
            "User voice evolution (preference changes, workflow insights, methodology updates, usage patterns)"
        ],
        "output_format": "Exact user voice quotes con complete attribution + commitment inventory",
        "voice_thresholds": "≥54/60 minimum score with zero contamination tolerance"
    }),
    subagent_type="general-purpose"
)
```

### Task 4: Content Optimizer
```python
Task(
    description="Scan conversation for command modifications and creations",
    prompt=load_template("content-optimizer.md").customize({
        "optimization_objective": "COMMAND CHANGE SCANNING - Identify all command impacts",
        "content_target": "Command ecosystem changes and requirements",
        "optimization_targets": [
            "New command requirements (explicit requests, workflow gaps, missing functionality, integration needs)",
            "Existing command modifications (specific changes, behavior modifications, integration updates, optimization opportunities)",
            "Command creation specifications (detailed requirements, integration points, workflow integration, technical considerations)"
        ],
        "analysis_dimensions": [
            "Full conversation scope with existing commands context",
            "User requests and implementation feasibility",
            "Command ecosystem impact assessment"
        ],
        "output_format": "Complete command change specification con implementation details"
    }),
    subagent_type="general-purpose"
)
```

## Main Agent Consolidation

### Specialist Output Integration
```python
def consolidate_specialist_outputs(task_outputs):
    return {
        'comprehensive_analysis': merge_analysis_results(task_outputs),
        'command_changes_consolidated': consolidate_command_changes(task_outputs),
        'voice_preservation_verified': validate_voice_preservation(task_outputs),
        'implementation_roadmap': generate_implementation_plan(task_outputs)
    }
```

### Command Updates Application
```python
def apply_subagent_command_updates(consolidated_results):
    if consolidated_results.command_changes_consolidated:
        command_updates = execute_command_updates_from_specialist_analysis(
            consolidated_results.command_changes_consolidated
        )
        
        if consolidated_results.core_decisions_changed:
            claude_md_updates = update_claude_md_from_decisions(
                consolidated_results.comprehensive_analysis.decisions_made
            )
        
        return {
            'updates_applied': True,
            'command_updates': command_updates,
            'claude_md_updates': claude_md_updates if 'claude_md_updates' in locals() else None
        }
    
    return {'updates_applied': False}
```

## File Generation Workflow

### Narrative Creation
```python
def generate_subagent_narrative(consolidated_results, timestamp_mx):
    narrative_content = create_comprehensive_narrative(
        conversation_transcript=consolidated_results.comprehensive_analysis.conversation_content,
        specialist_analysis=consolidated_results.comprehensive_analysis,
        command_changes=consolidated_results.command_changes_consolidated,
        voice_quotes=consolidated_results.voice_preservation_verified,
        timestamp=timestamp_mx
    )
    
    return create_narrative_file(
        f"narratives/raw/conversations/{timestamp_mx}_{consolidated_results.theme}.md",
        narrative_content
    )
```

### Smart Handoff Consolidation
```python
def execute_subagent_handoff_consolidation(consolidated_results, timestamp_mx):
    return execute_smart_handoff_consolidation_logic(
        analysis_results=consolidated_results,
        timestamp_mx=timestamp_mx,
        consolidation_mode="subagent_comprehensive"
    )
```

## Output Structure
```json
{
  "execution_mode": "subagent",
  "task_tools_deployed": 4,
  "specialist_results": {
    "research_analysis": "...",
    "architecture_validation": "...",
    "voice_preservation": "...",
    "content_optimization": "..."
  },
  "consolidated_output": {
    "comprehensive_analysis": "...",
    "command_updates_applied": true,
    "files_generated": [...],
    "ready_for_git": true
  }
}
```

## Integration Points
- **INPUT**: Analysis results from session-close-analysis
- **OUTPUT**: Complete session closure results for git workflow
- **NEXT**: session-close-git for universal git commit execution

---
**Function**: Comprehensive subagent-based session closure for standard user context