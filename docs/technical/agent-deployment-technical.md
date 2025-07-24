# Agent Deployment - Technical Authority

**Updated**: 2025-07-24 | **Authority**: Task Tool coordination & parallel execution | **Limit**: 80 lines
**Purpose**: Single source of truth for agent deployment patterns

## Core Principles (Lines 5-20)
**Primary Orchestrator**: Main system coordinates all Task Tool deployments  
**Parallel Priority**: Execute all tools in parallel/simultaneous mode within single messages
**Specialization**: Clear specialization area + specific objective + sufficient context
**Efficiency**: Maximize execution through batched tool calls
**Coordination**: Multiple agents for complex operations

### Agent Deployment Protocol
1. **Provide Context**: Complete background for success
2. **Define Objective**: Specific, measurable goal
3. **Specify Sources**: Relevant files and documentation
4. **Set Boundaries**: Clear scope and constraints
5. **Coordinate Execution**: Manage parallel operations

## Parallel Execution Patterns (Lines 21-40)
### **Single Message Batching**
```
Correct: Multiple tool calls in one message
<tool1>...</tool1><tool2>...</tool2><tool3>...</tool3>

Incorrect: Sequential messages
Message 1: <tool1>...</tool1>
Message 2: <tool2>...</tool2>
```

### **Coordination Strategies**
- **Concurrent Analysis**: Multiple agents analyzing different aspects
- **Parallel Research**: Simultaneous information gathering
- **Coordinated Implementation**: Synchronized execution phases
- **Batch Processing**: Group related operations

### **Communication Patterns**
- **Task Specification**: Clear, detailed task descriptions
- **Context Sharing**: Relevant background information
- **Result Integration**: Combine parallel outputs effectively

## Specialization Framework (Lines 41-60)
### **Agent Types**
- **Research Agents**: Information gathering and analysis
- **Implementation Agents**: Code and content creation
- **Validation Agents**: Quality assurance and testing
- **Coordination Agents**: Complex operation management

### **Specialization Requirements**
- **Expertise Area**: Clear domain focus (search, file ops, analysis)
- **Objective Definition**: Specific, measurable outcomes
- **Context Provision**: Sufficient background for autonomous operation
- **Resource Access**: Required files, tools, and permissions
- **Success Criteria**: Clear completion indicators

### **Integration Points**
- **Result Compilation**: Systematic output integration
- **Error Handling**: Coordinated failure management
- **Quality Assurance**: Validation across agent outputs
- **Feedback Loops**: Learning from agent performance

## Best Practices (Lines 61-80)
### **Deployment Optimization**
- **Never Sequential**: Always parallel when possible
- **Context Economy**: Minimal necessary context per agent
- **Clear Boundaries**: Well-defined agent responsibilities
- **Result Validation**: Systematic output verification

### **Common Patterns**
- **Search + Analysis**: Information gathering with processing
- **Create + Validate**: Content creation with quality checking
- **Research + Implementation**: Discovery followed by execution
- **Coordinate + Monitor**: Complex operation management

### **Performance Guidelines**
- **Batch Operations**: Group related tasks
- **Minimize Context**: Essential information only
- **Clear Objectives**: Specific, measurable goals
- **Validate Results**: Systematic quality checking

---
**Authority**: This file is the single source of truth for agent deployment across entire system.