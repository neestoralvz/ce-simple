# Multi-Conversation Management Guide

**Purpose**: Step-by-step user guide for managing 6 simultaneous Claude Code conversations  
**Target**: Users executing complex parallel workflows  
**Authority**: User Interface Management - VDD Framework  
**Status**: Active | **Lines**: ≤150

## Setup Phase: Opening 6 Conversations

### Step 1: Browser Preparation
1. **Open Chrome/Safari** with sufficient RAM allocation
2. **Create new browser window** (Cmd+Shift+N on Mac, Ctrl+Shift+N on Windows)
3. **Navigate to** claude.ai/code
4. **Pin the tab** (right-click → Pin Tab)

### Step 2: Tab Organization Strategy
```
Tab Layout (Left to Right):
[1-Master] [2-Search] [3-Analysis] [4-Implementation] [5-Validation] [6-Documentation]
```

**Opening Sequence**:
1. Tab 1: Keep original conversation (Master Coordinator)
2. Tabs 2-6: Cmd+T (Mac) or Ctrl+T (Windows) → Navigate to claude.ai/code
3. **Pin all tabs** for visual organization
4. **Rename tabs** using browser extension or mental mapping

### Step 3: Conversation Initialization
**Master Conversation (Tab 1)**:
```
I need to coordinate 6 parallel conversations for [your project]. 
Please provide the initialization commands for each conversation.
```

**Specialized Conversations (Tabs 2-6)**:
- Wait for Master to provide specific initialization commands
- Copy-paste exact commands provided by Master
- Confirm initialization before proceeding

## Command Sequences for Synchronized Launch

### Phase 1: Project Assessment (Parallel Launch)
**Master Command**:
```
Deploy 5 specialized agents for [project name]:
1. Codebase Search Agent
2. Technical Analysis Agent  
3. Implementation Agent
4. Quality Validation Agent
5. Documentation Agent

Provide initialization commands for each.
```

**Agent-Specific Commands** (Copy to respective tabs):
```
Tab 2 (Search): "I am the Codebase Search Agent for [project]. Ready for search tasks."
Tab 3 (Analysis): "I am the Technical Analysis Agent for [project]. Ready for analysis tasks."
Tab 4 (Implementation): "I am the Implementation Agent for [project]. Ready for coding tasks."
Tab 5 (Validation): "I am the Quality Validation Agent for [project]. Ready for testing tasks."
Tab 6 (Documentation): "I am the Documentation Agent for [project]. Ready for doc tasks."
```

### Phase 2: Task Distribution
**From Master to Agents** (Sequential):
1. Master analyzes requirements
2. Master provides specific tasks to each agent
3. Agents confirm task understanding
4. Agents execute in parallel

## Progress Monitoring Strategies

### Real-Time Status Tracking
**Visual Tab Management**:
- ✅ Green: Task completed
- ⚡ Yellow: Task in progress  
- ⏳ Blue: Waiting for input
- ❌ Red: Error/needs attention

**Browser Tab Naming** (if extension available):
```
[1-✅Master] [2-⚡Search] [3-⏳Analysis] [4-✅Impl] [5-⚡Valid] [6-✅Docs]
```

### Individual Agent Result Viewing
**Each Agent Tab Should Show**:
1. **Task Confirmation**: "I understand I need to [specific task]"
2. **Progress Updates**: Regular status reports during execution
3. **Individual Results**: Complete output before integration
4. **Success Confirmation**: Clear completion signal

**Master Orchestration**:
- Collects results from each agent
- Shows attribution to specific agents
- Provides synthesis while maintaining individual visibility

## Communication Flow Optimization

### Standard Communication Pattern
```
Master → Agent: "Search for X patterns in codebase"
Agent → Master: "Found 15 instances of X in 8 files. Full results: [detailed output]"
Master → User: "Search Agent found 15 instances across 8 files: [summary + attribution]"
```

### Efficient Task Handoffs
1. **Master sends clear, specific tasks** to each agent
2. **Agents confirm understanding** before execution
3. **Agents report progress** at key milestones
4. **Agents provide complete results** before Master synthesis
5. **Master synthesizes with clear attribution** to individual agents

## Troubleshooting Common Issues

### Connection Problems
**Symptom**: Agent conversation becomes unresponsive
**Solution**: 
1. Refresh the specific tab (Cmd+R / Ctrl+R)
2. Re-initialize that agent with same context
3. Continue from last confirmed checkpoint

### Context Loss
**Symptom**: Agent forgets previous instructions
**Solution**:
1. Master provides context recap to affected agent
2. Agent confirms understanding before continuing
3. Resume task execution

### Task Conflicts
**Symptom**: Multiple agents working on same file
**Solution**:
1. Master identifies conflict
2. Reassigns tasks with clear boundaries
3. Agents confirm non-overlapping responsibilities

### Synchronization Issues
**Symptom**: Agents complete at different times
**Solution**:
1. Master tracks completion status
2. Fast agents provide results and wait
3. Master coordinates next phase when all ready

## Time Management & Efficiency Tips

### Optimal Workflow Timing
- **Setup Phase**: 5-10 minutes (one-time per session)
- **Task Distribution**: 2-3 minutes per wave
- **Parallel Execution**: 5-15 minutes (depending on complexity)
- **Results Integration**: 3-5 minutes per wave

### Keyboard Shortcuts for Efficiency
```
Mac:
- Cmd+Tab: Switch between applications
- Cmd+Shift+A: Switch between tabs quickly
- Cmd+1 through Cmd+6: Jump directly to tabs 1-6

Windows:
- Alt+Tab: Switch between applications  
- Ctrl+Tab: Switch between tabs
- Ctrl+1 through Ctrl+6: Jump directly to tabs 1-6
```

### Best Practices
1. **Keep Master conversation active** for coordination
2. **Check agent status every 5 minutes** during execution
3. **Save important results immediately** in each conversation
4. **Use clear, specific language** in all communications
5. **Maintain session notes** for complex workflows

## Results Integration Procedures

### Individual Agent Reporting
**Each agent must provide**:
1. Task completion confirmation
2. Detailed results with specific findings
3. Any issues or blockers encountered
4. Recommendations for next steps

### Master Integration Process
1. **Collect all agent results** individually
2. **Verify completeness** of each agent's work
3. **Identify patterns and connections** across results
4. **Synthesize coherent summary** with clear agent attribution
5. **Present integrated results** to user with source transparency

### Quality Assurance
- Master validates each agent's work quality
- User can review individual agent contributions
- Clear audit trail of who did what
- Rollback capability if agent results need revision

---

**Success Metric**: User can efficiently coordinate 6 parallel conversations with clear visibility into each agent's individual work and seamless results integration.