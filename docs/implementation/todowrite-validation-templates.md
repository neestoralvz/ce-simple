# TodoWrite Validation & Decision Checklist Templates

## 🎯 Purpose
Standardized templates for TodoWrite behavioral reinforcement providing consistent validation, evaluation, and decision-making across all commands.

## 📋 CORE VALIDATION TEMPLATES

### Template 1: Structural Validation Checklist
```json
[
  {"content": "🏗️ STRUCTURE: Verify docs/, context/, .claude/ directories exist", "status": "pending", "priority": "high", "id": "struct-dirs"},
  {"content": "🔗 REFERENCES: Validate cross-reference integrity in command files", "status": "pending", "priority": "high", "id": "struct-refs"},
  {"content": "📏 SIZE: Ensure files comply with size limits (≤200 lines)", "status": "pending", "priority": "medium", "id": "struct-size"},
  {"content": "⚡ AUTO-CORRECT: Fix any structural violations detected", "status": "pending", "priority": "high", "id": "struct-fix"}
]
```

### Template 2: Context Assessment Checklist
```json
[
  {"content": "🎯 OBJECTIVE: Clarify user request and expected outcomes", "status": "pending", "priority": "high", "id": "context-objective"},
  {"content": "📊 COMPLEXITY: Assess task complexity for optimal workflow", "status": "pending", "priority": "high", "id": "context-complexity"},
  {"content": "🔍 SUFFICIENCY: Determine if context is complete for execution", "status": "pending", "priority": "medium", "id": "context-sufficient"},
  {"content": "❓ CLARIFICATION: Generate questions if context incomplete", "status": "pending", "priority": "medium", "id": "context-clarify"}
]
```

### Template 3: Quality Assurance Checklist
```json
[
  {"content": "✅ STANDARDS: Apply anti-bias and evidence-based protocols", "status": "pending", "priority": "high", "id": "qa-standards"},
  {"content": "🎚️ THRESHOLD: Meet minimum quality requirements (85% health)", "status": "pending", "priority": "high", "id": "qa-threshold"},
  {"content": "🔄 VALIDATION: Cross-validate findings across sources/methods", "status": "pending", "priority": "medium", "id": "qa-validate"},
  {"content": "📈 OPTIMIZATION: Apply performance and efficiency improvements", "status": "pending", "priority": "medium", "id": "qa-optimize"}
]
```

### Template 4: Progress Tracking Checklist
```json
[
  {"content": "📢 NOTIFICATIONS: Generate transparent progress updates", "status": "pending", "priority": "medium", "id": "progress-notify"},
  {"content": "🔄 UPDATES: Maintain real-time todo status changes", "status": "pending", "priority": "medium", "id": "progress-updates"},
  {"content": "📊 METRICS: Track performance and completion indicators", "status": "pending", "priority": "low", "id": "progress-metrics"},
  {"content": "🎯 COMPLETION: Verify all objectives successfully achieved", "status": "pending", "priority": "medium", "id": "progress-complete"}
]
```

## 🔧 COMMAND-SPECIFIC DECISION TEMPLATES

### `/start` Decision Matrix Template
```json
[
  {"content": "🤔 DECISION: Determine parallel vs sequential agent deployment", "status": "pending", "priority": "high", "id": "start-parallel"},
  {"content": "🎯 STRATEGY: Select optimal exploration strategy (local/web/mixed)", "status": "pending", "priority": "high", "id": "start-strategy"},
  {"content": "⚡ ACTIVATION: Trigger appropriate command workflows", "status": "pending", "priority": "medium", "id": "start-activate"},
  {"content": "🧠 REASONING: Document decision rationale transparently", "status": "pending", "priority": "medium", "id": "start-reasoning"}
]
```

### `/explore-codebase` Optimization Template
```json
[
  {"content": "📏 ASSESSMENT: Analyze codebase size for parallelization (12-52 ops)", "status": "pending", "priority": "high", "id": "explore-assess"},
  {"content": "⚡ DEPLOYMENT: Execute optimal operation count based on size", "status": "pending", "priority": "high", "id": "explore-deploy"},
  {"content": "🔍 DISCOVERY: Apply anti-bias pattern recognition protocols", "status": "pending", "priority": "high", "id": "explore-discover"},
  {"content": "📝 DOCUMENTATION: Generate context files from findings", "status": "pending", "priority": "medium", "id": "explore-document"}
]
```

### `/explore-web` Research Template  
```json
[
  {"content": "🌐 SCOPE: Determine research depth and topic complexity", "status": "pending", "priority": "high", "id": "web-scope"},
  {"content": "⚡ PARALLEL: Deploy optimal search count (4-16 operations)", "status": "pending", "priority": "high", "id": "web-parallel"},
  {"content": "🔍 VALIDATION: Cross-reference findings across sources", "status": "pending", "priority": "medium", "id": "web-validate"},
  {"content": "🎯 SYNTHESIS: Consolidate research into actionable intelligence", "status": "pending", "priority": "medium", "id": "web-synthesize"}
]
```

### `/think-layers` Analysis Template
```json
[
  {"content": "🧠 DEPTH: Determine required analysis depth (L1-L4)", "status": "pending", "priority": "high", "id": "think-depth"},
  {"content": "🔄 ESCALATION: Assess need for deeper analysis layers", "status": "pending", "priority": "high", "id": "think-escalate"},
  {"content": "🎯 CONSOLIDATION: Convert analysis to implementable plan", "status": "pending", "priority": "medium", "id": "think-consolidate"},
  {"content": "📚 LEARNING: Trigger capture-learnings if complexity ≥4", "status": "pending", "priority": "low", "id": "think-learning"}
]
```

### `/capture-learnings` Intelligence Template
```json
[
  {"content": "📊 SCORING: Calculate learning value using assessment framework", "status": "pending", "priority": "high", "id": "learn-score"},
  {"content": "🎤 INTERVIEW: Conduct intelligent questions if threshold ≥4", "status": "pending", "priority": "medium", "id": "learn-interview"},
  {"content": "📝 PATTERNS: Document discovered patterns and insights", "status": "pending", "priority": "medium", "id": "learn-patterns"},
  {"content": "🔧 INTEGRITY: Validate system coherence and gap resolution", "status": "pending", "priority": "low", "id": "learn-integrity"}
]
```

## 🎯 DYNAMIC ADAPTATION TEMPLATES

### Complexity-Based Template Selection
```markdown
### Auto-Template Selection Logic

**Simple Tasks (Complexity 1-3)**:
- Basic validation + progress tracking
- 3-4 todos maximum for cognitive efficiency

**Moderate Tasks (Complexity 4-6)**:
- Full validation + context assessment + quality assurance
- 5-7 todos with priority optimization

**Complex Tasks (Complexity 7-10)**:
- All templates + dynamic adaptation
- 8-12 todos with intelligent load management
```

### Discovery-Based Todo Addition
```json
{
  "structural_violation": {"content": "🚨 URGENT: Fix structural violation - {specific_issue}", "status": "pending", "priority": "high"},
  "performance_opportunity": {"content": "⚡ OPTIMIZE: Implement performance enhancement - {optimization}", "status": "pending", "priority": "medium"},
  "learning_pattern": {"content": "📚 CAPTURE: Document learning pattern - {insight}", "status": "pending", "priority": "low"},
  "quality_issue": {"content": "🔧 CORRECT: Apply quality correction - {issue}", "status": "pending", "priority": "high"}
}
```

## 🔄 PROGRESSIVE TODO MANAGEMENT PROTOCOLS

### Status Transition Rules
```markdown
### Todo Lifecycle Management

1. **Generation**: Auto-create todos at command initialization
2. **Activation**: Mark as "in_progress" when starting action
3. **Completion**: Mark as "completed" immediately after action
4. **Addition**: Add new todos based on discoveries
5. **Cleanup**: Remove obsolete todos to maintain clarity
```

### User Transparency Patterns
```markdown
### Progress Communication Templates

**Starting Action**: 
"🔄 {todo_id}: {action_description} → Moving to in_progress"

**Completing Action**:
"✅ {todo_id}: {action_description} → Completed successfully"

**Adding Discovery**:
"🆕 {todo_id}: {new_requirement} → Added based on {discovery_context}"

**Quality Gate**:
"⚠️ {todo_id}: {issue_detected} → Applying correction protocol"
```

## 📊 TEMPLATE EFFECTIVENESS METRICS

### Success Indicators
- **100% Validation Coverage**: No missed structural or quality checks
- **Predictable Workflows**: Users understand execution progress
- **Consistent Quality**: Automated application of standards
- **Optimal Cognitive Load**: 3-7 todos per command average

### Performance Tracking
- **Template Usage**: Frequency of each template across commands
- **Completion Rates**: Percentage of todos completed successfully  
- **User Satisfaction**: Feedback on workflow transparency
- **Quality Improvements**: Reduction in manual corrections needed

## 🚀 IMPLEMENTATION INTEGRATION

### Command Enhancement Protocol
```markdown
1. **Select Base Templates**: Choose appropriate templates for command type
2. **Customize for Context**: Adapt templates to specific command requirements
3. **Integrate Generation**: Add TodoWrite calls at command initialization
4. **Test Validation**: Verify templates work correctly in practice
5. **Refine Based on Usage**: Optimize templates based on real-world performance
```

### Quality Assurance Checklist
- [ ] **Template Completeness**: All critical validations covered
- [ ] **Priority Optimization**: High-priority items properly flagged
- [ ] **Cognitive Load**: Appropriate todo density for command complexity
- [ ] **User Experience**: Clear and actionable todo descriptions
- [ ] **Integration**: Seamless workflow with existing command structure

---

**AUTOMATION EXCELLENCE**: These templates transform TodoWrite from task tracking to intelligent behavioral guidance, ensuring consistent execution quality across all commands while maintaining optimal user transparency and system reliability.