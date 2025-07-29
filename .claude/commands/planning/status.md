# /planning:status - Project Overview Dashboard

**29/07/2025 16:35 CDMX** | Comprehensive project construction status overview

## Function
Display complete project status, progress across all layers, and overall health.

## Usage
```bash
/planning:status           # Full project status dashboard
/planning:status summary   # Condensed overview
/planning:status health    # Focus on blockers and issues
```

## Dashboard Format

### Project Overview
```
📊 Project Status Dashboard: [project-type]

🎯 Overall Progress: [X]% Complete ([Y/Z] layers finished)
📅 Project Age: [Duration since initialization]
🔄 Current Phase: Layer [X] - [Description]
⏱️  Focus Duration: [Time in current layer]

📈 Layer Progress:
Layer 1: [■■■■■] 100% ✅ COMPLETED ([completion date])
Layer 2: [■■■□□]  60% 🔄 ACTIVE    ([start date])
Layer 3: [□□□□□]   0% ⏳ PENDING   (blocked by Layer 2)
Layer 4: [□□□□□]   0% ⏳ PENDING   (blocked by Layer 2)
```

### Health Indicators

#### 🟢 Healthy Project
```
🟢 Project Health: GOOD
  ✅ All dependencies resolved
  ✅ No blocking issues detected  
  ✅ Progress steady within current layer
  ✅ Quality standards maintained
```

#### 🟡 Attention Needed
```
🟡 Project Health: NEEDS ATTENTION
  ⚠️  [X] items overdue in current layer
  ⚠️  Quality drift detected ([specific issues])
  ⚠️  Dependencies may need review
  💡 Suggested actions: [recommendations]
```

#### 🔴 Blocked/Issues
```
🔴 Project Health: BLOCKED
  🚫 Gate criteria failed: [specific failures]
  🚫 Critical dependencies broken: [details]
  🚫 Quality standards violated: [violations]
  🛠️  Required actions: [mandatory fixes]
```

## Detailed Status Views

### /planning:status summary
```
📊 [project-type]: Layer [X]/[Total] ([X]% complete)
🎯 Focus: [Current layer description]
⏳ Next Gate: [Days/items until advancement]
🟢 Health: [Status indicator]
```

### /planning:status health
```
🏥 Project Health Analysis:

🔍 Current Issues:
  • [Issue 1] - [Severity] - [Estimated fix time]
  • [Issue 2] - [Severity] - [Estimated fix time]

⚠️  Potential Risks:
  • [Risk 1] - [Probability] - [Impact if occurs]
  • [Risk 2] - [Probability] - [Impact if occurs]

💡 Recommendations:
  1. [Specific action for highest priority issue]
  2. [Preventive action for highest risk]
  3. [Optimization suggestion]
```

## Progress Tracking

### Layer-Specific Metrics
**Layer 1 (Foundation):**
- Architecture decisions finalized: [X/Y]
- Core principles established: [✅/❌]
- Authority structure: [Status]

**Layer 2 (Development):**
- Features implemented: [X/Y] 
- Code quality compliance: [X/Y files ≤80 lines]
- Testing coverage: [%]

**Layer 3 (Integration):**
- Component integration: [X/Y connections]
- End-to-end validation: [Test results]
- Performance benchmarks: [Metrics]

**Layer 4 (Distribution):**
- Packaging completion: [Status]
- Documentation coverage: [%]
- Distribution readiness: [✅/❌]

### Velocity Tracking
**Daily progress:** Average items completed per day
**Layer velocity:** Time spent in each layer historically
**Productivity trends:** Progress acceleration/deceleration patterns
**Bottleneck identification:** Layers with longest duration

## Predictive Analysis

### Completion Estimates
**Current layer:** Estimated completion based on remaining work
**Next layer:** Predicted start date based on current velocity
**Project completion:** Overall timeline projection with confidence intervals

### Risk Factors
**Dependency risks:** Likelihood of foundation changes affecting later layers
**Scope creep:** Detection of expanding requirements beyond original plan
**Quality debt:** Accumulation of shortcuts that may require future rework

## Integration Insights

### Cross-Command Status
**Planning ecosystem:** Status of all planning commands (init, layers, gate, focus)
**Project coherence:** Alignment between planning state and actual project state
**Command usage patterns:** Frequency and effectiveness of planning command usage

### Context Integration
**File compliance:** Percentage of files meeting ≤80 line requirement
**Reference integrity:** Status of cross-reference system health
**Authority alignment:** Compliance with TRUTH_SOURCE.md hierarchy

## Historical Analysis

### Progress History
**Layer transitions:** Dates and durations of each layer completion
**Gate passages:** Success rate and time required for gate validations
**Focus changes:** Frequency and reasons for layer focus shifts

### Learning Extraction
**Bottleneck patterns:** Recurring issues across similar project phases
**Success factors:** Conditions that accelerated progress
**Optimization opportunities:** Process improvements for future projects

## Export Readiness

### Distribution Preparation Status
**Framework stability:** Core system ready for replication
**Template completeness:** Project type templates comprehensive
**Documentation status:** Usage guides and examples ready
**Testing validation:** Framework proven with real projects

---
**Authority:** Comprehensive project tracking + health monitoring methodology
**Integration:** → All planning commands, project tracking, health monitoring