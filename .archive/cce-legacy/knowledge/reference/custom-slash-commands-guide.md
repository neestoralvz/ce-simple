# Custom Slash Commands Guide - Real Executable Functionality

**Meta-Principle**: "Bridge the gap between Context Engineering templates and executable slash commands through Claude Code's native custom command system"

**Purpose**: MANDATORY guide for creating real executable slash commands that map to Context Engineering workflows using Claude Code's `~/.claude/commands/` system.

---

## 🎯 **Overview**

### **CRITICAL Understanding**
- **Context Engineering Templates**: Documentation patterns in `docs/commands/` (NOT executable)
- **Native Claude Slash Commands**: Built-in commands like `/help`, `/status`, `/clear` (executable)
- **Custom Slash Commands**: User-created commands in `~/.claude/commands/` (executable)

### **Solution Architecture**
Create custom slash commands that execute Context Engineering workflows using Task tool orchestration.

---

## 🚀 **Quick Setup**

### **Step 1: Create Custom Command Directory**
```bash
mkdir -p ~/.claude/commands/context-engineering
```

### **Step 2: Create Core Command**
```bash
# Create ~/.claude/commands/context-engineering/ce.md
```

### **Step 3: Test Functionality**
```markdown
# In Claude Code interface
/context-engineering:ce analyze system
```

---

## 📋 **Command Creation Templates**

### **Basic Command Template**
```markdown
---
description: "Context Engineering meta-orchestrator"
allowed-tools: "Task, Read, Write, Bash"
argument-hint: "[objective]"
examples: ["analyze system", "optimize workflow", "review code"]
---

Activate Context Engineering system for: $ARGUMENTS

Execute comprehensive analysis using:
1. Read relevant command templates from docs/commands/
2. Use Task tool for multi-step orchestration  
3. Apply P55/P56 compliance protocols
4. Deliver results with writing standards compliance

@./docs/commands/README.md
@./docs/knowledge/README.md
@./CLAUDE.md

Apply systematic Context Engineering workflow with maximum efficiency.
```

### **Thinking Command Template**
```markdown
---
description: "Progressive thinking sequence activation"
allowed-tools: "Task, Read"
argument-hint: "[complexity_topic]"
examples: ["complex algorithm", "system architecture", "strategic decision"]
---

Activate progressive thinking sequence for: $ARGUMENTS

Execute systematic analysis using:
1. Read thinking framework from docs/commands/behavioral/intelligence/thinking.md
2. Apply complexity assessment (≥0.9 triggers deep analysis)
3. Use Task tool for multi-perspective evaluation
4. Deliver strategic recommendations

@./docs/commands/behavioral/intelligence/thinking.md
@./docs/commands/behavioral/intelligence/progressive-thinking-sequence.md

Implement Context Engineering thinking protocols with cognitive rigor.
```

### **Decision Command Template**
```markdown
---
description: "Smart routing and decision engine"
allowed-tools: "Task, Read, Grep"
argument-hint: "[decision_context]"
examples: ["technical choice", "workflow optimization", "resource allocation"]
---

Activate decision engine for: $ARGUMENTS

Execute decision framework using:
1. Read decision templates from docs/commands/executable/core-routing/decision.md
2. Apply mathematical triggers and routing logic
3. Use Task tool for multi-criteria analysis
4. Deliver clear recommendations with rationale

@./docs/commands/executable/core-routing/decision.md
@./docs/commands/executable/core-routing/adaptive-routing.md

Apply Context Engineering decision protocols with mathematical precision.
```

---

## 🔧 **Advanced Command Features**

### **Namespacing**
```markdown
# File: ~/.claude/commands/ce/core.md → Command: /ce:core
# File: ~/.claude/commands/ce/thinking.md → Command: /ce:thinking  
# File: ~/.claude/commands/ce/decision.md → Command: /ce:decision
```

### **Dynamic Arguments**
```markdown
---
description: "Context Engineering workflow with dynamic parameters"
allowed-tools: "Task, Read, Write, Bash, Grep"
argument-hint: "[workflow] [complexity] [urgency]"
---

Execute Context Engineering workflow: $ARGUMENTS

Parse arguments:
- Workflow: $1 (e.g., analysis, optimization, review)
- Complexity: $2 (e.g., low, medium, high) 
- Urgency: $3 (e.g., normal, urgent, critical)

Apply appropriate templates based on parameters.
```

### **Conditional Logic**
```markdown
Execute workflow based on complexity:
- If complexity >= 0.9: Use progressive thinking sequence
- If urgency = critical: Apply parallel task execution
- If workflow = review: Use quality assurance protocols

@./docs/commands/behavioral/intelligence/complexity.md
@./docs/commands/executable/execution/parallel-tool-execution.md
```

---

## 🎯 **Command Mapping Strategy**

### **Priority Commands for Implementation**

**Tier 1: Essential**
- `/ce:core` → Meta-orchestrator activation
- `/ce:thinking` → Progressive thinking sequence
- `/ce:decision` → Decision engine and routing
- `/ce:validate` → Quality assurance and verification

**Tier 2: Workflow**
- `/ce:execute` → Execution orchestration
- `/ce:parallel` → Multi-task coordination
- `/ce:optimize` → System optimization
- `/ce:sync` → Documentation synchronization

**Tier 3: Specialized**
- `/ce:containerize` → Docker automation
- `/ce:math-verify` → Mathematical validation
- `/ce:git-workflow` → Git worktree management
- `/ce:monitor` → System monitoring

---

## 📊 **Implementation Phases**

### **Phase 1: Core Framework** (2-4 hours)
```bash
# Create basic structure
mkdir -p ~/.claude/commands/ce

# Implement core commands
touch ~/.claude/commands/ce/core.md
touch ~/.claude/commands/ce/thinking.md  
touch ~/.claude/commands/ce/decision.md
```

### **Phase 2: Workflow Integration** (4-6 hours)
- Implement Task tool orchestration patterns
- Add argument parsing and conditional logic
- Test command execution and debugging

### **Phase 3: Advanced Features** (6-8 hours)  
- Add dynamic parameter handling
- Implement cross-command communication
- Create specialized workflow commands

---

## 🔍 **Testing and Validation**

### **Basic Testing**
```markdown
# Test command discovery
/help

# Test basic execution  
/ce:core test workflow

# Test with arguments
/ce:thinking complex algorithm analysis

# Test error handling
/ce:invalid command
```

### **Advanced Testing**
```markdown
# Test conditional logic
/ce:decision urgent technical choice

# Test file references
/ce:core @specific-file.md

# Test tool integration
/ce:validate current system state
```

---

## 🚨 **Common Issues and Solutions**

### **Command Not Found**
```bash
# Check file location
ls -la ~/.claude/commands/ce/

# Verify syntax  
cat ~/.claude/commands/ce/core.md

# Test command availability
/help | grep ce
```

### **Execution Errors**
```markdown
# Check tool permissions
allowed-tools: "Task, Read, Write"

# Verify file references
@./docs/commands/README.md

# Debug argument parsing
echo "Arguments: $ARGUMENTS"
```

### **Performance Issues**
```markdown
# Optimize file references
@./docs/commands/specific-file.md  # Good
@./docs/commands/  # Too broad

# Limit tool usage
allowed-tools: "Task, Read"  # Minimal set
```

---

## 🎭 **Integration with Context Engineering**

### **Workflow Pattern**
1. **Custom slash command** triggers execution
2. **Task tool** orchestrates workflow  
3. **Read tool** accesses Context Engineering templates
4. **Write tool** delivers results with compliance

### **Example Integration**
```markdown
# User executes:
/ce:thinking system architecture

# Command triggers:
- Read thinking template
- Use Task tool for analysis
- Apply Context Engineering protocols  
- Deliver structured output
```

---

## 📈 **Performance Benefits**

### **User Experience**
- **≤1 step access** to Context Engineering workflows
- **Native Claude interface** integration
- **Argument support** for customization
- **Error handling** and validation

### **System Efficiency**  
- **Direct execution** without manual orchestration
- **Template reuse** with custom parameters
- **Consistent workflow** patterns
- **Quality assurance** integration

---

## 🔗 **Cross-Reference Network**

### **Related Documentation**
- **[Claude Code Native Commands](./claude-code-native-commands.md)** → Complete native command reference
- **[Command System](../commands/README.md)** → Context Engineering templates
- **[Writing Standards](../writing-standards.md)** → Output compliance requirements

### **Integration Points**
- **Task Tool**: Primary execution engine
- **Read Tool**: Template access mechanism  
- **P55/P56 Protocols**: Quality assurance framework
- **Git Worktrees**: Parallel execution support

---

**Custom Commands**: Transform Context Engineering templates into executable slash commands using Claude Code's native custom command system for seamless workflow integration.

**Performance**: Custom slash commands provide ≤1 step access to Context Engineering workflows with native Claude Code interface integration and full argument support.

**Navigation**: [Knowledge Hub](../README.md) | [Native Commands](./claude-code-native-commands.md) | [Context Engineering Commands](../commands/README.md)