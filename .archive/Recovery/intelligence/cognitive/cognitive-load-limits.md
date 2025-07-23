# Cognitive Load Limits for Components

## 🧠 FUNDAMENTAL COGNITIVE BOUNDARIES

**CRITICAL PRINCIPLE**: All components must respect cognitive load limits to maintain optimal performance and prevent overload.

### Core Cognitive Limits
- **Maximum targets per orchestrator**: 4 simultaneous
- **Maximum file size**: 200 lines per component
- **Maximum context usage**: 70% before handoff consideration
- **Maximum dependency depth**: 3 levels

## 📊 COGNITIVE LOAD METRICS

### Orchestrator Load Calculation
```
Cognitive Load = (Active Agents + Active Tasks + Context %) / 100
Target: <0.70 (70%)
Warning: >0.80 (80%)
Critical: >0.90 (90% - immediate handoff required)
```

### Component Complexity Scoring
```
Base Score = 10
+ Lines: (line_count / 200) * 20
+ Dependencies: dependency_count * 10
+ External References: external_refs * 15
+ Cognitive Complexity: complexity_factor * 25

Target: <50 points
Warning: 50-75 points
Critical: >75 points (requires refactoring)
```

## 🎯 LOAD OPTIMIZATION STRATEGIES

### For Orchestrators
- **Parallel deployment**: Up to 4 agents simultaneously
- **Sequential when necessary**: Complex interdependent tasks
- **Handoff preparation**: At 90% context usage
- **Sub-orchestrator creation**: For tasks >4 targets

### For Agents
- **Focused specialization**: Single responsibility principle
- **Efficient tool usage**: Minimal context consumption
- **Result consolidation**: Compact reporting format
- **Error handling**: Graceful failure management

### For Behaviors
- **Modular application**: Apply to specific components only
- **Context awareness**: Monitor cognitive load impact
- **Progressive enhancement**: Layer complexity gradually
- **Resource optimization**: Minimal overhead patterns

## 🔧 LOAD MANAGEMENT PROTOCOLS

### Context Usage Monitoring
```
if (context_usage > 70%) {
    → Consider lazy loading for non-critical content
    → Prepare for potential handoff
    → Optimize communication patterns
}

if (context_usage > 90%) {
    → Immediate handoff preparation required
    → Emergency context optimization
    → Critical operation only mode
}
```

### Cognitive Complexity Management
```
if (orchestrator_targets > 4) {
    → Create sub-orchestrator for overflow
    → Maintain 4-target limit per level
    → Implement hierarchical coordination
}

if (component_size > 200_lines) {
    → Refactor into multiple components
    → Implement lazy loading patterns
    → Create modular structure
}
```

## 📋 COMPONENT DESIGN GUIDELINES

### Single Responsibility Principle
- **One primary function** per component
- **Clear, focused purpose** statement
- **Minimal external dependencies** 
- **Efficient resource usage**

### Modular Architecture
- **Self-contained units** where possible
- **Clean interfaces** between components
- **Lazy loading support** for optional content
- **Progressive complexity** layers

### Communication Optimization
- **Compact notification format** for routine operations
- **Detailed reporting** only when necessary
- **Batch operations** to reduce overhead
- **Context-aware messaging** patterns

## ⚡ PERFORMANCE OPTIMIZATION

### Context Efficiency
- **Reuse loaded content** when possible
- **Cache frequently accessed** components
- **Batch related operations** together
- **Optimize loading patterns** for common workflows

### Resource Management
- **Monitor memory usage** continuously
- **Implement garbage collection** for unused components
- **Optimize data structures** for minimal overhead
- **Use efficient algorithms** for complex operations

## 📊 SUCCESS METRICS

### Cognitive Load Health
- **Average context usage**: <60%
- **Peak context usage**: <80%
- **Handoff frequency**: <10% of operations
- **Component efficiency**: >90% successful operations

### Performance Indicators
- **Response time**: <2 seconds for standard operations
- **Resource utilization**: <70% of available capacity
- **Error rate**: <5% of total operations
- **Success rate**: >95% task completion

---

**These cognitive load limits ensure optimal performance and prevent system overload while maintaining the intelligence and efficiency of the component ecosystem.**