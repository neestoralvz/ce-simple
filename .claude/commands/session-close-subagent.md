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
    prompt="""Actúa como Research Specialist. CONVERSATION ANALYSIS MISSION: Extract key elements.

CONVERSATION INPUT:
- Complete conversation: {analysis_input.conversation_content}
- Session context: {analysis_input.session_context}
- Timeline: {analysis_input.timeline}

ANALYSIS OBJECTIVES:
1. Theme Identification:
   - Primary topic/focus of conversation
   - Secondary themes discussed
   - Evolution of topics throughout session
   - Key decision points reached

2. Category Classification:
   - Document creation, architecture discussion, implementation
   - Planning, analysis, troubleshooting, optimization
   - User feedback, system evolution, methodology refinement

3. Commands Detection:
   - Commands explicitly mentioned or requested
   - Implied commands from user requests
   - Command modifications discussed
   - New command requirements identified

OUTPUT: Structured analysis con theme, category, commands inventory.""",
    subagent_type="general-purpose"
)
```

### Task 2: Architecture Validator
```python
Task(
    description="Detect decisions and command changes required",
    prompt="""Actúa como Architecture Validator. DECISION DETECTION MISSION: Identify system changes.

DECISION ANALYSIS SCOPE:
- Conversation content: {analysis_input.conversation_content}
- System context: Current architecture state
- Command ecosystem: Existing commands structure
- User commitments: Promises made during session

DECISION DETECTION:
1. Explicit Decisions Made:
   - User decisions about system behavior
   - Architecture changes approved
   - Methodology updates decided
   - Command modifications agreed upon

2. Command Changes Required:
   - New commands to be created
   - Existing commands to be modified
   - Commands to be deprecated/removed
   - Command integration updates needed

3. System Architecture Impact:
   - Core system changes required
   - Rules system updates needed
   - Documentation updates required
   - Integration points affected

OUTPUT: Decision inventory con specific command change requirements.""",
    subagent_type="general-purpose"
)
```

### Task 3: Voice Preservation Specialist
```python
Task(
    description="Extract user voice quotes and command commitments",
    prompt="""Actúa como Voice Preservation Specialist. VOICE EXTRACTION MISSION: Preserve user voice exactly.

VOICE PRESERVATION SCOPE:
- Conversation content: {analysis_input.conversation_content}
- User statements: All user messages in conversation
- Commitment tracking: Promises and decisions made
- Voice evolution: Changes in user preferences

VOICE EXTRACTION REQUIREMENTS:
1. Exact User Quotes:
   - All significant user statements (ZERO paraphrasing)
   - Complete source attribution with message timestamps
   - Context preservation for each quote
   - Intent clarification where needed

2. Command Commitments:
   - Explicit commitments made about commands
   - Implementation promises given
   - Timeline commitments stated
   - Scope agreements reached

3. User Voice Evolution:
   - Changes in preferences during session
   - New insights about user workflow
   - Methodology preference updates
   - System usage pattern changes

OUTPUT: Exact user voice quotes con complete attribution + commitment inventory.""",
    subagent_type="general-purpose"
)
```

### Task 4: Content Optimizer
```python
Task(
    description="Scan conversation for command modifications and creations",
    prompt="""Actúa como Content Optimizer. COMMAND CHANGE SCANNING MISSION: Identify all command impacts.

COMMAND SCANNING SCOPE:
- Full conversation: {analysis_input.conversation_content}
- Existing commands: Current command ecosystem state
- User requests: All command-related requests made
- Implementation context: Technical feasibility assessment

COMMAND CHANGE DETECTION:
1. New Command Requirements:
   - Commands explicitly requested
   - Workflow gaps requiring new commands
   - User needs indicating missing functionality
   - Integration commands needed

2. Existing Command Modifications:
   - Specific changes requested to existing commands
   - Behavior modifications discussed
   - Integration updates needed
   - Optimization opportunities identified

3. Command Creation Specifications:
   - Detailed requirements for new commands
   - Integration points with existing system
   - User workflow integration needs
   - Technical implementation considerations

OUTPUT: Complete command change specification con implementation details.""",
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