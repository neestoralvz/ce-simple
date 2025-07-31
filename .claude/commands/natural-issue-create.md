# /natural-issue-create - Natural Issue Creation Protocol

**31/07/2025 CDMX** | Natural language issue creation with context-aware classification and automatic workflow integration

## AUTORIDAD SUPREMA
@context/architecture/orchestration.md → natural-issue-create.md implements natural conversation patterns per L4-Pure Orchestration methodology

## PRINCIPIO FUNDAMENTAL
**"Natural language issue creation preserving conversation flow while capturing complete context"** - Enable intuitive issue creation through natural conversation patterns without disrupting dialogue flow or losing contextual information.

## NATURAL CONVERSATION PATTERNS

### **Conversational Issue Triggers**
Natural language patterns that automatically trigger issue creation:

```
NATURAL TRIGGERS:
├── "This would be good to track as an issue"
├── "We should create an issue for this"
├── "Let's file this for later"
├── "This needs its own issue"
├── "Can you create an issue for [task]?"
├── "Add this to the backlog"
└── "Track this separately"
```

### **Context-Aware Detection**
Automatic detection during conversation flow:
- **Scope Expansion**: Tasks discovered during execution requiring separate attention
- **Future Work**: Enhancements or improvements mentioned during implementation
- **Related Tasks**: Dependencies or follow-up work identified during discussion
- **Documentation Needs**: Documentation or process improvements discovered

## NATURAL LANGUAGE PROCESSING

### **Intent Recognition Framework**
```
CONVERSATION ANALYSIS:
├── EXPLICIT REQUEST: Direct user request for issue creation
├── IMPLIED NEED: Task complexity suggests separate tracking
├── SCOPE DISCOVERY: Work discovered outside current objectives
└── WORKFLOW OPTIMIZATION: Process improvements identified
```

### **Context Extraction Protocol**
**Automatic Context Capture**:
1. **Conversation Context**: Current discussion topic and background
2. **Technical Context**: Files, components, or systems being discussed
3. **User Intent**: Explicit or implied user goals and objectives
4. **Priority Indicators**: Urgency or importance signals from conversation

### **Smart Classification System**
```
NATURAL CLASSIFICATION:
├── URGENCY INDICATORS: "urgent", "critical", "asap", "blocking" → HIGH priority
├── TIMELINE REFERENCES: "later", "future", "someday" → LOW priority
├── COMPLEXITY SIGNALS: "simple", "quick", "easy" → MICRO-TASK
└── SCOPE INDICATORS: "comprehensive", "overhaul", "redesign" → COMPLEX-TASK
```

## CONVERSATION-FIRST WORKFLOW

### **Seamless Integration Protocol**
1. **Continue Conversation**: Issue creation doesn't interrupt natural dialogue flow
2. **Context Preservation**: Complete conversation context captured in issue
3. **Reference Linking**: Automatic bidirectional linking between conversation and issue
4. **Follow-up Enablement**: Issues provide sufficient context for future execution

### **Natural Language Template Generation**
Instead of rigid templates, use conversational structure:

```markdown
# [Natural Title from Conversation]

**Found during**: [Conversation topic/context]
**Mentioned by**: [User/System] while discussing [context]

## What we discovered
[Natural description preserving conversation tone]

## Why this matters
[Context and rationale from conversation]

## What needs to happen
- [ ] [Action items in natural language]
- [ ] [Additional steps identified]

## Context from conversation
- **Discussion**: [Link to conversation]
- **Related work**: [Current objectives]
- **Timeline context**: [When this was discovered]

---
**Created naturally during conversation** | **Context preserved**
```

## WORKFLOW INTEGRATION

### **TodoWrite Integration**
- **Automatic Addition**: Issues automatically added to TodoWrite for tracking
- **Status Synchronization**: Issue status updates reflect in TodoWrite
- **Priority Alignment**: TodoWrite priorities align with issue classifications
- **Context Linking**: Complete traceability between TodoWrite and issues

### **Conversation Continuity**
- **No Interruption**: Issue creation happens in background
- **Status Updates**: Brief confirmations without disrupting flow
- **Context Preservation**: Full conversation context captured
- **Reference Availability**: Issues immediately available for reference

### **Natural Confirmation Patterns**
```
CONFIRMATION STYLES:
├── "✓ Tracked: [Brief description] as Issue #X"
├── "📝 Added to backlog: [Title] (Issue #X)"
├── "🎯 Created issue for [task] - continuing with [current work]"
└── "Issue #X created for [context] - available for future work"
```

## COMMAND EXECUTION MODES

### **Interactive Mode**
```bash
User: "We should create an issue for improving the documentation"
System: ✓ Created Issue #42: "Improve documentation" - continuing with current task
```

### **Explicit Mode**
```bash
/natural-issue-create "Add validation to user input" --priority medium
```

### **Batch Mode**
```bash
User: "Let's track these three things: validation, error handling, and performance optimization"
System: ✓ Created 3 issues: #43 (validation), #44 (error handling), #45 (performance) - all linked to current conversation
```

## SMART DEFAULTS SYSTEM

### **Context-Aware Defaults**
- **Priority**: Inferred from conversation urgency and user tone
- **Timeline**: Based on user language patterns ("later" = low priority, "soon" = medium)
- **Classification**: Automatic categorization based on complexity indicators
- **Labels**: Auto-generated from conversation context and technical domain

### **Learning Adaptation**
- **User Patterns**: Learn from user's issue creation patterns and preferences
- **Context Recognition**: Improve context detection based on successful issue resolutions
- **Priority Alignment**: Adapt priority classification to match user's actual prioritization
- **Workflow Integration**: Optimize integration based on user workflow patterns

## QUALITY ASSURANCE

### **Context Completeness Validation**
- **Conversation Link**: Every issue links back to creating conversation
- **Technical Context**: Relevant files, components, systems referenced
- **User Intent**: Clear understanding of user's objectives captured
- **Action Clarity**: Next steps are clearly defined and actionable

### **Natural Language Quality**
- **Conversational Tone**: Issues read naturally, not robotically
- **Context Preservation**: Original conversation context and tone maintained
- **Clarity**: Technical and non-technical stakeholders can understand
- **Completeness**: Sufficient information for future implementation

## SUCCESS METRICS

### **User Experience Metrics**
- **Conversation Flow**: Zero interruption to natural dialogue
- **Context Accuracy**: 95%+ accuracy in capturing user intent
- **Follow-up Success**: Issues provide sufficient context for future work
- **User Satisfaction**: Natural, intuitive issue creation experience

### **Technical Metrics**
- **Classification Accuracy**: 90%+ correct automatic classification
- **Context Completeness**: 100% conversation context preservation
- **Integration Success**: Seamless TodoWrite and workflow integration
- **Reference Integrity**: Complete traceability and linking

## COMMAND SYNTAX

### **Natural Invocation**
No rigid syntax required - natural conversation patterns trigger automatically:
- "Can you track this as an issue?"
- "Let's create an issue for the validation work"
- "This should be its own issue"

### **Explicit Invocation**
```bash
/natural-issue-create [description] [--priority low|medium|high] [--type micro|complex|enhancement]
```

### **Batch Invocation**
```bash
/natural-issue-create batch [conversation_context]
```

---

**NATURAL ISSUE CREATION DECLARATION**: This protocol enables intuitive, conversation-first issue creation that preserves natural dialogue flow while capturing complete context and enabling systematic workflow integration.

**EVOLUTION PATHWAY**: Natural conversation → intent recognition → context capture → issue creation → workflow integration