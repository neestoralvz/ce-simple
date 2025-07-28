# Enhanced Interview Command Specification

**Purpose**: Self-contained command specification with embedded intelligence for Task Tool compatibility  
**Authority**: Standards layer - command implementation requirements  
**Think×4**: Comprehensive specification with embedded logic architecture  
**Lines**: ≤200

## Command Architecture Specification

### Self-Containment Requirements
```
Embedded Logic Framework:
1. Complete Algorithm Embedding:
   - All categorization algorithms embedded inline
   - Dynamic questioning protocols integrated within command
   - Context preservation mechanisms built into command logic
   - Template selection and adaptation logic embedded

2. No External Dependencies:
   - All question banks and categorization rules embedded
   - Template structures included within command specification
   - Response analysis algorithms integrated inline
   - Context analysis logic built into command execution

3. Task Tool Compatibility:
   - Sub-agents cannot access external files or commands
   - All logic and templates passed explicitly to sub-agents
   - Complete interview intelligence embedded in deployment prompts
   - Self-validating execution with embedded quality checks
```

### Embedded Intelligence Architecture
```
Inline Algorithm Integration:
1. Spanish Categorization Engine:
   logros_patterns = ["completed", "successful", "improved", "achieved", "optimized", "effective"]
   desafios_patterns = ["opportunity", "challenge", "potential", "enhancement", "could improve", "would benefit"]  
   errores_patterns = ["error", "failed", "mistake", "broken", "bug", "incorrect", "regression"]
   obstaculos_patterns = ["blocked", "limited", "constraint", "dependency", "impediment", "bottleneck"]
   aprendizajes_patterns = ["learned", "insight", "discovered", "understanding", "pattern", "principle"]

2. Dynamic Question Generation:
   question_effectiveness_threshold = 0.6
   response_depth_minimum = 50_characters
   category_coverage_target = 80_percent
   engagement_optimization_trigger = 3_short_responses

3. Context Preservation Logic:
   session_context_layers = ["system_state", "user_activity", "historical", "environmental"]
   context_quality_threshold = 0.9
   temporal_bridging_gap_max = 14_days
   context_metadata_required = ["timestamp", "session_type", "context_score", "coverage_metrics"]
```

## Command Implementation Specification

### Enhanced Interview Command Structure
```markdown
# /user-interview-advanced - Enhanced Feedback Collection

**Purpose**: Sophisticated feedback collection with embedded intelligence
**Self-Containment**: All logic, templates, and algorithms embedded inline
**Task Tool Deployment**: 4 parallel sub-agents with embedded specialization

## Embedded Intelligence Framework

### Spanish Categorization Algorithm (Embedded)
```
categorize_response(response_text):
    scores = {}
    
    # logros (Achievements) scoring
    logros_indicators = ["completed", "successful", "improved", "achieved", "optimized", "effective", "accomplished", "exceeded", "delivered", "satisfied"]
    scores["logros"] = calculate_pattern_score(response_text, logros_indicators)
    
    # desafios (Challenges) scoring  
    desafios_indicators = ["opportunity", "challenge", "potential", "enhancement", "could improve", "would benefit", "growth", "development", "advancement", "optimization"]
    scores["desafios"] = calculate_pattern_score(response_text, desafios_indicators)
    
    # errores (Errors) scoring
    errores_indicators = ["error", "failed", "mistake", "broken", "bug", "incorrect", "regression", "malfunction", "crash", "failure"]
    scores["errores"] = calculate_pattern_score(response_text, errores_indicators)
    
    # obstaculos (Obstacles) scoring
    obstaculos_indicators = ["blocked", "limited", "constraint", "dependency", "impediment", "bottleneck", "barrier", "restriction", "limitation", "hindrance"]
    scores["obstaculos"] = calculate_pattern_score(response_text, obstaculos_indicators)
    
    # aprendizajes (Learnings) scoring
    aprendizajes_indicators = ["learned", "insight", "discovered", "understanding", "pattern", "principle", "realization", "knowledge", "wisdom", "experience"]
    scores["aprendizajes"] = calculate_pattern_score(response_text, aprendizajes_indicators)
    
    return assign_categories(scores, threshold=0.6)
```

### Dynamic Questioning Engine (Embedded)
```
generate_followup_question(category, response_text, context):
    
    if category == "logros":
        if response_depth(response_text) < 0.5:
            return "Can you describe what specifically made this successful?"
        elif expertise_level(context) == "high":
            return "What patterns do you see in this success that might apply elsewhere?"
        else:
            return "How did this achievement impact your broader workflow?"
    
    elif category == "desafios":
        if context["recent_challenges"] > 2:
            return "How does this challenge relate to others you've mentioned?"
        elif response_engagement(response_text) < 0.6:
            return "What would be the first small step toward addressing this?"
        else:
            return "What resources or support would help tackle this challenge?"
    
    elif category == "errores":
        urgency_score = calculate_error_urgency(response_text)
        if urgency_score > 0.8:
            return "How is this error currently blocking your work?"
        else:
            return "What information would have helped prevent this error?"
    
    elif category == "obstaculos":
        if context["obstacle_patterns"] > 1:
            return "Do you see connections between this and other obstacles you've faced?"
        else:
            return "What would need to change to remove this obstacle entirely?"
    
    elif category == "aprendizajes":
        application_potential = assess_learning_scope(response_text)
        if application_potential == "high":
            return "How might this insight transform your approach in other areas?"
        else:
            return "What surprised you most about this discovery?"
    
    return generate_neutral_followup(response_text, context)
```

### Context Preservation Framework (Embedded)
```
preserve_session_context(session_data):
    
    context_layers = {
        "system_state": {
            "vdd_version": detect_vdd_version(),
            "recent_changes": analyze_git_activity(days=7),
            "performance_metrics": get_system_health(),
            "active_projects": identify_active_projects()
        },
        "user_activity": {
            "command_patterns": analyze_command_usage(days=14),
            "workflow_efficiency": calculate_efficiency_metrics(),
            "interaction_style": assess_communication_patterns(),
            "focus_areas": identify_development_focus()
        },
        "historical": {
            "previous_sessions": load_feedback_history(),
            "recurring_themes": identify_theme_patterns(),
            "action_item_status": track_action_resolutions(),
            "satisfaction_trends": analyze_satisfaction_evolution()
        },
        "environmental": {
            "project_phase": detect_project_phase(),
            "external_factors": assess_environmental_context(),
            "resource_constraints": evaluate_resource_availability(),
            "collaboration_patterns": analyze_team_dynamics()
        }
    }
    
    return validate_context_completeness(context_layers)
```

## Sub-Agent Deployment Specification

### Agent 1: Context Analysis and Question Generation
**Embedded Task**: Pre-session context assembly and base question generation
**Self-Contained Logic**:
- Embedded git analysis algorithms for recent activity assessment
- Inline previous session integration logic with continuity question generation
- Built-in user preference pattern recognition with question style adaptation
- Embedded context quality validation and session planning optimization

### Agent 2: Dynamic Interview Execution
**Embedded Task**: Real-time interview conduct with adaptive questioning
**Self-Contained Logic**:
- Complete Spanish categorization engine embedded inline
- Full dynamic questioning algorithm with real-time adaptation
- Embedded response analysis and engagement optimization logic
- Inline session flow management with category coverage optimization

### Agent 3: Real-Time Context Tracking
**Embedded Task**: Session context monitoring and preservation
**Self-Contained Logic**:
- Complete context preservation framework embedded
- Inline session quality metrics and effectiveness tracking
- Embedded pattern recognition and real-time insight generation
- Built-in context validation and completeness verification

### Agent 4: Feedback Synthesis and Documentation
**Embedded Task**: Sacred space documentation and system integration
**Self-Contained Logic**:
- Complete feedback template selection and generation embedded
- Inline categorization confidence scoring and validation
- Embedded action item generation and priority scoring algorithms
- Built-in sacred space compliance and quality assurance validation

## Execution Quality Standards

### Self-Containment Validation
```
validate_command_self_containment():
    checks = {
        "no_external_file_references": verify_no_external_deps(),
        "complete_algorithm_embedding": validate_embedded_logic(),
        "template_inclusion": verify_embedded_templates(),
        "task_tool_compatibility": validate_sub_agent_deployment()
    }
    return all(checks.values())
```

### Performance Standards
```
execution_requirements = {
    "context_analysis_time": "< 3 minutes",
    "interview_session_time": "15-45 minutes adaptive",
    "real_time_processing": "< 5 seconds per response",
    "documentation_generation": "< 2 minutes",
    "total_session_time": "< 60 minutes maximum"
}

quality_standards = {
    "category_classification_accuracy": "> 95%",
    "context_preservation_completeness": "> 99%",
    "user_satisfaction_score": "> 8.5/10",
    "action_item_relevance": "> 90%",
    "sacred_space_compliance": "100%"
}
```

---

**Self-Contained Excellence**: Complete embedded intelligence architecture ensuring Task Tool compatibility with sophisticated interview capabilities and Sacred Space preservation.