# Workflow Notifications - Real-Time Progress System

## 🎯 Purpose
Provide transparent, real-time progress tracking for orchestrated agent workflows with standardized communication protocols.

## 📊 NOTIFICATION FRAMEWORK

### Universal Progress Format
```
[SYMBOL] [COMMAND]: [ACTION] → [STATUS] [TIMESTAMP]
```

### Standard Symbols
- 🎯 **START**: Workflow initiation
- 📊 **DISCOVERY**: Information gathering phase
- 🔧 **EXPLORATION**: Agent deployment and execution
- ⚡ **ANALYSIS**: Thinking and processing phases
- ✓ **COMPLETION**: Task finished successfully
- ⚠️ **ALERT**: Attention required
- 🔄 **TRANSITION**: Phase change or handoff

## 🔧 IMPLEMENTATION PROTOCOL

### Standard Notification Format
```
🎯 [PHASE]: [Action] initiated [timestamp/context]
📊 [METRIC]: [Description] → [Status/Progress]
🧠 DECISION: [Brief reasoning] → [Strategy selected]
🔧 [ACTION]: [Description] → [Status/Result]
⚡ [PROGRESS]: [Current state] → [Next action]
✅ [COMPLETION]: [Summary] → [Outcome/Result]
```

### Decision Transparency Framework

#### Decision Context Templates
```
🧠 DECISION: [Strategy] selected → [Primary reason]
🧠 DECISION: [Analysis depth] needed → [Complexity justification]  
🧠 DECISION: [Agent deployment] optimal → [Resource allocation reasoning]
🧠 DECISION: [Execution path] required → [Dependency analysis]
```

#### Progress Rationale Standards
- Include brief reasoning for major workflow decisions
- Provide context for strategy selection (parallel vs sequential)
- Explain analysis depth choices and agent deployment rationale
- Maintain transparency without verbose explanations

### Phase Tracking System
**MANDATORY**: Each workflow phase MUST announce start and completion
**FORMAT**: Standard notification format with phase-specific context
**PHASES**: Discovery, Exploration, Analysis with structured progress indicators

### Agent Communication Protocol

#### Agent Communication Cycle
**DEPLOY**: Main agent → Task agent with objective and context
**EXECUTE**: Task agent processing with progress and status updates
**RETURN**: Task agent → Main agent with results and next steps

### User Communication Standards

#### Progress Updates
**FREQUENCY**: Every significant state change
**FORMAT**: Clear, concise, actionable information
**CONTENT**: Current status, next steps, user actions required

#### Cognitive Load Management

##### Notification Efficiency
- **One-line summaries** over paragraph explanations
- **Strategic timing** to avoid notification fatigue
- **Essential updates** prioritized over comprehensive reporting
- **Decision context** included only when strategy changes

##### User Experience Optimization
- Predictable notification patterns for familiar workflows
- Clear phase transitions with completion indicators
- Transparent decision-making without overwhelming detail
- Progress tracking that enables user confidence in execution

#### Communication Standards
**ALERTS**: User input requests with context, options, and impact
**COMPLETIONS**: Success summaries with duration, outputs, and next steps

## 📋 COGNITIVE LOAD INDICATORS

### Agent Capacity Monitoring
**CRITICAL**: Track and display agent cognitive load

#### Capacity Indicators
```
🔧 AGENT-01: Capacity 70% → Operating normally
⚠️ AGENT-02: Capacity 90% → Approaching limits
🔄 AGENT-03: Capacity 95% → Load balancing triggered
```

#### Load Balancing Notifications
```
🔄 LOAD-BALANCE: Agent-02 task redistributed
   Original: [heavy task]
   Split: [task-A] → Agent-04, [task-B] → Agent-05
   Result: Improved efficiency [%]
```

### Context Switching Alerts
```
🔄 CONTEXT-SWITCH: Agent-01 changing focus
   From: [previous task]
   To: [new task]
   Handoff: [context preservation method]
```

## ⚡ AUTO-ACTIVATION SYSTEM

### Trigger Notifications
**AUTOMATIC**: System detects conditions requiring workflow activation

#### Auto-Activation Triggers
**COMPLEXITY**: High complexity detection with automatic workflow activation
**CONTEXT**: Insufficient information detection with discovery question initiation
**TRANSITIONS**: Command handoffs with reason, context preservation, and state continuity

## 📊 SUCCESS METRICS

### Completion Tracking
**REQUIRED**: Every workflow MUST report success metrics

#### Standard Metrics Framework
**METRICS**: Duration, efficiency, quality, coverage with structured reporting
**REPORTING**: Success metrics with completion tracking and user satisfaction

## 🚫 ERROR HANDLING

### Error Handling Framework
**FAILURES**: Component failure detection with issue, impact, recovery, and ETA
**RECOVERY**: Resolution attempts with method, progress, and fallback strategies

## 🔗 Implementation Examples

### Notification Templates
- **Location**: `../../context/workflows/workflow-notifications.md`
- **Contains**: Detailed notification templates and formatting patterns
- **Usage**: Implementation reference for all notification scenarios

---

**CRITICAL**: ALL commands MUST implement this notification system for transparent orchestration and user awareness. No silent operations permitted.