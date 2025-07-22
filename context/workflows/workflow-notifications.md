# Workflow Notification Examples - Implementation Templates

## 🔧 Command-Specific Notification Patterns

### Discovery Workflow Notifications
```
🎯 START: Discovery workflow initiated [HH:MM:SS]
📊 DISCOVERY: Generating contextual questions → User input required
📊 DISCOVERY: User responses analyzed → Context sufficiency: [%]
✓ DISCOVERY: Context validation complete → Proceeding to exploration
```

### Exploration Phase Notifications
```
🔧 EXPLORATION: Deploying [N] agents → [parallel/sequential] mode
🔧 EXPLORATION: Agent-01 (/explore-codebase) → Active
🔧 EXPLORATION: Agent-02 (/explore-web) → Active
🔧 EXPLORATION: Agent-01 completed → Results integrated
✓ EXPLORATION: All agents completed → Analysis ready
```

### Analysis Phase Notifications
```
⚡ ANALYSIS: Think-layers activated → Depth level 1/4
⚡ ANALYSIS: Pattern recognition phase → [N] patterns identified
⚡ ANALYSIS: Integration phase → Consolidating findings
✓ ANALYSIS: Plan generation complete → Ready for execution
```

## 🤖 Agent Communication Examples

### Deployment Notification
```
🔄 DEPLOY: [Main-Agent] → [Task-Agent] 
   Objective: [specific task]
   Context: [relevant information]
   Expected: [deliverable format]
```

### Execution Notification
```
⚡ EXECUTE: [Task-Agent] processing [objective]
   Progress: [current phase]
   Status: [on-track/delayed/blocked]
   ETA: [estimated completion]
```

### Return Notification
```
✓ RETURN: [Task-Agent] → [Main-Agent]
   Result: [summary of findings]
   Deliverable: [file/context generated]
   Next: [suggested follow-up action]
```

## ⚠️ Alert and Error Examples

### Attention Alerts
```
⚠️ ALERT: User input required
   Context: [what information is needed]
   Options: [available choices]
   Impact: [consequence of decision]
```

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

## 🔄 System State Examples

### Complexity Detection
```
⚡ AUTO-TRIGGER: High complexity detected
   Request: [user input analysis]
   Complexity: [score/10]
   Action: Activating /start workflow
```

### Context Insufficiency
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

## 📊 Success Metrics Examples

### Completion Summaries
```
✓ COMPLETION: [Workflow] finished successfully
   Duration: [total time]
   Outputs: [files/context generated]
   Next: [recommended follow-up commands]
```

### Standard Metrics Report
```
✓ SUCCESS-METRICS: [Workflow] completed
   Duration: [MM:SS]
   Efficiency: [completed/planned tasks]
   Quality: [validation score %]
   Coverage: [exploration completeness %]
   User Satisfaction: [feedback required]
```

## 🧠 Agent Capacity Examples

### Capacity Indicators
```
🔧 AGENT-01: Capacity 70% → Operating normally
⚠️ AGENT-02: Capacity 90% → Approaching limits
🔄 AGENT-03: Capacity 95% → Load balancing triggered
```

### Load Balancing Notifications
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

## 🧠 Learning Capture Notifications

### Learning Value Assessment
```
🎯 ASSESSMENT: Learning value evaluation initiated
   Complexity: [novelty + reusability + importance + complexity]/10
   Score: [X]/10 points
   Threshold: ≥4 → Interview activation
```

### Results Learning Notifications  
```
📊 DECISION: User interview activated → [question-count] dynamic questions
🔍 INTEGRITY: System validation initiated → [X] commands from executed workflow
⚠️  GAPS: [N] system gaps discovered → [priority breakdown]
✅ COMPLETION: Learning + validation captured → [pattern-count] patterns enhanced
🚫 SKIP: Auto-documentation → Low learning value detected
```

### Pattern Documentation Updates
```
📚 CAPTURE: Decision documented → [pattern-category] updated  
🔗 INTEGRATION: Context enhanced → [context-file] enriched
🧠 LEARNING: Pattern detection active → [discovery-type] identified
```

### System Evolution Tracking
```
🎯 EVOLUTION: Command network enhancement triggered
   Patterns: [N] validated patterns integrated
   Improvements: [specific enhancements]
   Impact: [system coherence score]
```

---

**CONTEXT**: Implementation examples extracted from workflow-notifications.md for progressive disclosure. Contains detailed notification templates and formatting patterns for all workflow scenarios including learning capture and system evolution.