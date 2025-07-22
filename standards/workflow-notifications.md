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

### Phase Tracking System
**MANDATORY**: Each workflow phase MUST announce start and completion

#### Discovery Phase
```
🎯 START: Discovery workflow initiated [HH:MM:SS]
📊 DISCOVERY: Generating contextual questions → User input required
📊 DISCOVERY: User responses analyzed → Context sufficiency: [%]
✓ DISCOVERY: Context validation complete → Proceeding to exploration
```

#### Exploration Phase
```
🔧 EXPLORATION: Deploying [N] agents → [parallel/sequential] mode
🔧 EXPLORATION: Agent-01 (/explore-codebase) → Active
🔧 EXPLORATION: Agent-02 (/explore-web) → Active
🔧 EXPLORATION: Agent-01 completed → Results integrated
✓ EXPLORATION: All agents completed → Analysis ready
```

#### Analysis Phase
```
⚡ ANALYSIS: Think-layers activated → Depth level 1/4
⚡ ANALYSIS: Pattern recognition phase → [N] patterns identified
⚡ ANALYSIS: Integration phase → Consolidating findings
✓ ANALYSIS: Plan generation complete → Ready for execution
```

### Agent Communication Protocol

#### Deployment Notification
```
🔄 DEPLOY: [Main-Agent] → [Task-Agent] 
   Objective: [specific task]
   Context: [relevant information]
   Expected: [deliverable format]
```

#### Execution Notification
```
⚡ EXECUTE: [Task-Agent] processing [objective]
   Progress: [current phase]
   Status: [on-track/delayed/blocked]
   ETA: [estimated completion]
```

#### Return Notification
```
✓ RETURN: [Task-Agent] → [Main-Agent]
   Result: [summary of findings]
   Deliverable: [file/context generated]
   Next: [suggested follow-up action]
```

### User Communication Standards

#### Progress Updates
**FREQUENCY**: Every significant state change
**FORMAT**: Clear, concise, actionable information
**CONTENT**: Current status, next steps, user actions required

#### Attention Alerts
```
⚠️ ALERT: User input required
   Context: [what information is needed]
   Options: [available choices]
   Impact: [consequence of decision]
```

#### Completion Summaries
```
✓ COMPLETION: [Workflow] finished successfully
   Duration: [total time]
   Outputs: [files/context generated]
   Next: [recommended follow-up commands]
```

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

#### Complexity Detection
```
⚡ AUTO-TRIGGER: High complexity detected
   Request: [user input analysis]
   Complexity: [score/10]
   Action: Activating /start workflow
```

#### Context Insufficiency
```
⚠️ CONTEXT-ALERT: Insufficient information detected
   Missing: [specific context areas]
   Action: Initiating discovery questions
   Required: [estimated information needed]
```

### Workflow Transitions
```
🔄 TRANSITION: [Current-Command] → [Next-Command]
   Reason: [transition trigger]
   Handoff: [context passed]
   Continuation: [workflow maintains state]
```

## 📊 SUCCESS METRICS

### Completion Tracking
**REQUIRED**: Every workflow MUST report success metrics

#### Standard Metrics
- **Duration**: Total time elapsed
- **Efficiency**: Tasks completed vs planned
- **Quality**: Output validation scores
- **Coverage**: Exploration completeness percentage

#### Report Format
```
✓ SUCCESS-METRICS: [Workflow] completed
   Duration: [MM:SS]
   Efficiency: [completed/planned tasks]
   Quality: [validation score %]
   Coverage: [exploration completeness %]
   User Satisfaction: [feedback required]
```

## 🚫 ERROR HANDLING

### Failure Notifications
```
⚠️ ERROR: [Component] failure detected
   Issue: [specific problem]
   Impact: [affected workflows]
   Recovery: [automatic/manual action]
   ETA: [expected resolution time]
```

### Recovery Protocols
```
🔄 RECOVERY: Attempting error resolution
   Method: [recovery strategy]
   Progress: [current status]
   Fallback: [alternative approach if needed]
```

---

**CRITICAL**: ALL commands MUST implement this notification system for transparent orchestration and user awareness. No silent operations permitted.