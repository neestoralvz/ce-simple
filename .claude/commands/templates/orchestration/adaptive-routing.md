# Adaptive Routing Orchestration - Pattern Template

## Pattern Definition (2025 Framework Standard)
**Pattern**: Dynamic Agent Selection with Context-Aware Routing Intelligence
**Approach**: AI-driven routing decisions based on real-time context, performance, and optimization criteria
**Use Case**: Complex, evolving tasks requiring intelligent adaptation and optimal resource utilization

## Orchestration Framework
This template implements adaptive routing patterns inspired by 2025 AI orchestration advances, featuring intelligent decision-making, predictive routing, and self-optimizing workflows.

## Pattern Structure

### Adaptive Routing Engine
```
Routing Intelligence: [AI-Driven Decision Engine]
├── Context Analysis: Real-time task requirement assessment
├── Specialist Matching: Optimal agent selection based on multiple criteria
├── Performance Prediction: Expected outcome modeling for routing options
├── Dynamic Adaptation: Real-time routing adjustment based on feedback
└── Learning Integration: Continuous improvement from routing outcomes
```

### Intelligent Routing Flow
```
Task Input: [Initial Request]
    ↓ (analysis: context, requirements, constraints)
Routing Engine: [Multi-Criteria Decision Analysis]
    ↓ (evaluation: specialist capabilities, availability, performance history)
Dynamic Selection: [Optimal Specialist Choice]
    ↓ (execution: task processing with continuous monitoring)
Adaptive Feedback: [Performance monitoring and routing adjustment]
    ↓ (learning: routing outcome analysis and model updates)
Routing Optimization: [Improved future routing decisions]
```

## Implementation Template

### Intelligent Research Routing (Example)
```
Adaptive Routing: Intelligent Research Investigation
Routing Engine: Context-Aware Research Specialist Selection
Success Criteria: Optimal research quality with maximum efficiency
Learning Model: Continuous routing improvement based on research outcomes

Initial Routing Analysis:
Task: Adaptive Routing Engine
Description: "Analyze research requirements and select optimal specialist routing"
Subagent: general-purpose
Prompt: "Actúa como Adaptive Routing Engine experto siguiendo 2025 AI orchestration best practices. Tu misión: analyze and route research task optimally:

ROUTING ANALYSIS FRAMEWORK:
- **Context Assessment**: Deep analysis of research requirements, domain complexity, time constraints
- **Specialist Evaluation**: Multi-dimensional assessment of available specialists and their capabilities
- **Performance Prediction**: Model expected outcomes for different routing options
- **Resource Optimization**: Balance quality, speed, and resource utilization
- **Risk Assessment**: Evaluate routing risks and mitigation strategies

ROUTING DECISION CRITERIA:
□ **Task Complexity**: Match specialist expertise to task difficulty and domain requirements
□ **Quality Requirements**: Select specialists with highest probability of meeting quality standards
□ **Time Constraints**: Optimize routing for speed without compromising essential quality
□ **Resource Availability**: Consider specialist capacity and workload distribution
□ **Historical Performance**: Weight specialists based on past performance in similar tasks
□ **Learning Opportunity**: Factor in potential for routing decision learning and improvement

ROUTING INTELLIGENCE OUTPUT:
**🎯 ROUTING DECISION ANALYSIS:**

**Task Assessment:**
- **Domain**: [Research domain classification]
- **Complexity Score**: [1-10 with complexity factors]
- **Quality Requirements**: [Quality level needed with specific criteria]
- **Time Constraints**: [Timeline requirements and flexibility]
- **Resource Constraints**: [Available resources and limitations]

**Specialist Evaluation Matrix:**
| Specialist | Domain Match | Availability | Quality Score | Speed | Risk |
|------------|--------------|--------------|---------------|-------|------|
| Research Specialist | [X/10] | [Available/Busy] | [X/10] | [X/10] | [Low/Med/High] |
| Context Analyst | [X/10] | [Available/Busy] | [X/10] | [X/10] | [Low/Med/High] |
| Integration Specialist | [X/10] | [Available/Busy] | [X/10] | [X/10] | [Low/Med/High] |

**Routing Decision:** [Selected Specialist]
**Confidence Level:** [X%] - [Reasoning for confidence level]
**Expected Outcome:** [Quality: X/10, Speed: X/10, Resource Efficiency: X/10]
**Fallback Options:** [Alternative routing if primary selection fails]
**Monitoring Criteria:** [What to monitor for adaptive routing adjustments]

**Dynamic Routing Instructions:**
IF (initial_results_indicate_different_expertise_needed) {
    ANALYZE_ROUTING_ADJUSTMENT(current_progress, new_requirements)
    CONSIDER_SPECIALIST_HANDOFF(optimal_specialist, context_preservation)
}

IF (performance_below_expectations) {
    EVALUATE_SPECIALIST_AUGMENTATION(additional_specialists, collaborative_approach)
    IMPLEMENT_PERFORMANCE_IMPROVEMENT(specific_guidance, resource_adjustment)
}

Continue with selected specialist..."

Selected Specialist Execution with Adaptive Monitoring:
Task: [Selected Specialist Based on Routing Decision]
Description: "Execute research with adaptive routing monitoring"
Subagent: general-purpose
Prompt: "[Selected Specialist Template]
Adaptive Context: Research task with intelligent routing oversight
Performance Monitoring: Track progress against routing predictions
Adaptation Triggers: Signal routing engine if context changes or performance issues arise

Research Focus: [Specific research requirements based on routing analysis]
Quality Target: [Quality requirements from routing decision]
Efficiency Target: [Speed and resource targets from routing optimization]

Adaptive Signaling:
- Signal if task complexity exceeds initial assessment
- Signal if different expertise becomes needed during research
- Signal if quality/time trade-offs need routing engine evaluation
- Signal routing engine for performance feedback and learning data"

Adaptive Routing Adjustment Example:
IF (research_reveals_integration_complexity) {
    ROUTING_ENGINE_REASSESSMENT(
        new_context: "Integration complexity discovered during research",
        current_progress: "[Research specialist findings]",
        adjusted_requirements: "Technical integration expertise now required",
        routing_options: [
            "Continue with Research Specialist + Integration Specialist collaboration",
            "Handoff to Integration Specialist with research context",
            "Parallel processing: Research continues + Integration analysis"
        ]
    )
    
    ADAPTIVE_DECISION: [Selected routing adjustment with reasoning]
    IMPLEMENTATION: [How routing change is executed]
    LEARNING_UPDATE: [What routing engine learns from this adaptation]
}
```

### Multi-Phase Adaptive Orchestration (Example)
```
Adaptive Orchestration: Complex System Analysis with Dynamic Routing
Routing Engine: Multi-Phase Intelligent Coordination
Success Criteria: Optimal specialist utilization across changing requirements
Learning Integration: Cross-phase routing optimization

Phase 1: Initial Analysis with Adaptive Specialist Selection
Routing Decision: Analyze requirements and select initial specialist configuration

Context Analysis:
- System complexity assessment
- Multiple analysis dimensions identified
- Resource and time constraint evaluation
- Quality requirement specification

Dynamic Specialist Configuration:
Based on initial analysis, routing engine selects:
├── Primary: [Specialist A] for [Primary analysis dimension]
├── Secondary: [Specialist B] for [Secondary analysis dimension] 
├── Monitoring: [Specialist C] on standby for [Potential complexity area]
└── Integration: [Specialist D] for [Result consolidation] - Phase 2

Phase 1 Execution with Adaptive Monitoring:
[Selected specialists execute with routing engine monitoring progress]

Adaptive Trigger Example:
IF (Phase_1_reveals_security_concerns_not_initially_identified) {
    ROUTING_ENGINE_ADAPTATION(
        trigger: "Security concerns discovered - not in initial analysis",
        current_state: "[Phase 1 progress and findings]",
        new_requirements: "Security expertise now critical for comprehensive analysis",
        adaptation_options: [
            "Add Security Auditor to current phase",
            "Schedule Security Auditor for Phase 2 with priority",
            "Restructure remaining phases to include security focus"
        ]
    )
    
    ADAPTIVE_ROUTING_DECISION: [Selected adaptation strategy]
    PHASE_RESTRUCTURING: [How phases are modified]
    SPECIALIST_COORDINATION: [How new specialist is integrated]
}

Phase 2: Adaptive Integration Based on Phase 1 Learning
Routing Engine Reassessment:
- Incorporate all Phase 1 findings into routing decisions
- Adjust specialist selection based on discovered complexity
- Optimize Phase 2 configuration for maximum effectiveness

Dynamic Phase 2 Configuration:
Based on Phase 1 adaptive learning:
├── Integration Focus: [Adjusted based on Phase 1 complexity discovery]
├── Quality Assurance: [Enhanced based on Phase 1 quality requirements]
├── Specialist Selection: [Optimized based on Phase 1 performance data]
└── Final Delivery: [Configured for optimal outcome delivery]

Cross-Phase Learning Integration:
Routing engine updates decision models based on:
- Phase 1 routing decision effectiveness
- Specialist performance against predictions
- Adaptation success rates and outcomes
- Quality vs efficiency trade-off optimization
```

## Adaptive Routing Intelligence

### Context-Aware Decision Making
```
Multi-Dimensional Context Analysis:
def analyze_routing_context(task, environment, constraints):
    # Task Characteristics
    task_complexity = assess_complexity(task.requirements, task.domain)
    task_urgency = evaluate_urgency(task.timeline, task.priority)
    task_quality_needs = analyze_quality_requirements(task.standards, task.output_needs)
    
    # Environmental Factors
    specialist_availability = assess_specialist_capacity(available_specialists)
    resource_constraints = evaluate_resource_limitations(compute, time, expertise)
    system_load = analyze_current_system_utilization(active_tasks, performance_metrics)
    
    # Historical Performance
    routing_history = analyze_similar_task_routing(task_similarity, specialist_performance)
    success_patterns = identify_successful_routing_patterns(historical_outcomes)
    failure_patterns = identify_routing_failure_modes(historical_issues)
    
    return routing_context_profile(task_chars, env_factors, historical_data)
```

### Predictive Routing Models
```
Outcome Prediction Framework:
def predict_routing_outcomes(routing_options, context_profile):
    for option in routing_options:
        # Quality Prediction
        quality_score = predict_quality_outcome(
            specialist_expertise=option.specialist.expertise_match,
            task_complexity=context_profile.complexity,
            historical_performance=option.specialist.history
        )
        
        # Speed Prediction  
        completion_time = predict_completion_time(
            specialist_speed=option.specialist.processing_speed,
            task_scope=context_profile.scope,
            current_workload=option.specialist.current_load
        )
        
        # Resource Efficiency
        resource_usage = predict_resource_consumption(
            specialist_efficiency=option.specialist.efficiency_rating,
            task_requirements=context_profile.resource_needs,
            optimization_potential=option.specialist.optimization_ability
        )
        
        # Risk Assessment
        failure_risk = assess_routing_risk(
            specialist_reliability=option.specialist.reliability_score,
            task_difficulty=context_profile.difficulty,
            environmental_factors=context_profile.environment
        )
        
        option.predicted_outcome = RoutingOutcome(quality_score, completion_time, resource_usage, failure_risk)
    
    return rank_routing_options(routing_options, optimization_criteria)
```

### Dynamic Adaptation Engine
```
Real-Time Routing Adjustment:
def monitor_and_adapt_routing(active_routing, performance_data):
    # Performance Monitoring
    current_performance = assess_current_performance(active_routing, performance_data)
    deviation_from_prediction = calculate_prediction_accuracy(
        predicted_outcome=active_routing.predicted_outcome,
        actual_performance=current_performance
    )
    
    # Adaptation Triggers
    if deviation_from_prediction > adaptation_threshold:
        adaptation_options = generate_adaptation_strategies(
            current_state=active_routing.current_state,
            performance_gap=deviation_from_prediction,
            available_alternatives=assess_alternative_routing()
        )
        
        optimal_adaptation = select_optimal_adaptation(
            adaptation_options,
            cost_benefit_analysis=True,
            context_preservation=True
        )
        
        if optimal_adaptation.benefit > adaptation_cost:
            execute_routing_adaptation(optimal_adaptation)
            update_routing_models(adaptation_outcome)
```

## 2025 Adaptive Routing Practices

### AI-Enhanced Decision Intelligence
```
Machine Learning Integration:
- Neural network models for specialist-task matching optimization
- Reinforcement learning for routing decision improvement over time
- Natural language processing for task requirement understanding
- Computer vision for performance pattern recognition

Predictive Analytics:
- Real-time performance prediction based on current context
- Resource utilization forecasting for optimal routing decisions
- Quality outcome prediction with confidence intervals
- Risk assessment with probabilistic failure mode analysis
```

### Autonomous System Evolution
```
Self-Improving Routing:
- Automated routing model updates based on outcome feedback
- Continuous optimization of decision criteria and weights
- Emergent routing patterns discovery through outcome analysis
- Autonomous specialist capability assessment and tracking

Distributed Learning:
- Cross-system routing intelligence sharing
- Federated learning for routing optimization across environments
- Collaborative intelligence for complex routing scenarios
- Network effect optimization through distributed routing data
```

### Real-Time Optimization
```
Dynamic Resource Allocation:
- Real-time specialist workload balancing for optimal utilization
- Adaptive priority management based on changing requirements
- Dynamic quality threshold adjustment based on context evolution
- Real-time performance optimization through routing adaptation
```

## Error Handling and Recovery

### Intelligent Error Recovery
```
Adaptive Error Management:
IF (routing_prediction_accuracy < threshold) {
    ANALYZE_PREDICTION_FAILURE(actual_vs_predicted, context_factors)
    UPDATE_PREDICTION_MODELS(failure_analysis, improved_factors)
    IMPLEMENT_CORRECTIVE_ROUTING(alternative_specialists, recovery_strategy)
}

IF (specialist_performance_degradation_detected) {
    EVALUATE_PERFORMANCE_FACTORS(workload, complexity, resource_constraints)
    IMPLEMENT_PERFORMANCE_SUPPORT(additional_resources, task_simplification)
    IF (performance_remains_inadequate) {
        EXECUTE_SPECIALIST_SUBSTITUTION(optimal_replacement, context_transfer)
    }
}
```

### System-Level Resilience
```
Routing System Fault Tolerance:
IF (routing_engine_failure_detected) {
    FALLBACK_TO_STATIC_ROUTING(predefined_patterns, conservative_decisions)
    IMPLEMENT_MANUAL_ROUTING_OVERRIDE(human_decision_support)
    RESTORE_ADAPTIVE_ROUTING(gradual_restoration, safety_validation)
}

IF (cascade_failure_risk_detected) {
    IMPLEMENT_CIRCUIT_BREAKER(routing_pause, stability_assessment)
    ISOLATE_FAILING_COMPONENTS(specialist_isolation, task_redistribution)
    GRADUAL_SYSTEM_RESTORATION(monitored_recovery, performance_validation)
}
```

## Integration with CE-Simple Ecosystem

### Voice Preservation in Adaptive Routing
- User voice context incorporated into routing decision criteria
- Voice authenticity maintained through all routing adaptations
- Voice preservation quality weighted in routing optimization
- User intent alignment validated throughout adaptive routing process

### Token Economy Optimization
- Token usage predictions integrated into routing decisions
- Dynamic token budget allocation based on routing efficiency
- Context compression optimization at routing decision points
- Quality vs token efficiency balanced in adaptive routing models

## Usage Examples

### Simple Adaptive Routing
```
Task Analysis → Context Assessment → Specialist Matching → Performance Prediction
→ Routing Decision → Execution Monitoring → Adaptive Adjustment → Outcome Learning
```

### Complex Multi-Criteria Adaptation
```
Multi-Phase Analysis → Dynamic Context Evolution → Real-Time Specialist Reallocation
→ Performance Optimization → Quality Threshold Adjustment → Integrated Delivery
```

## Quality Criteria for Adaptive Routing Output
- [ ] Intelligent routing decisions based on comprehensive context analysis
- [ ] Accurate performance prediction with measurable confidence levels
- [ ] Real-time adaptation capabilities with performance monitoring
- [ ] Continuous learning integration with routing model improvement
- [ ] Optimal resource utilization with quality outcome achievement
- [ ] Comprehensive error handling with intelligent recovery strategies