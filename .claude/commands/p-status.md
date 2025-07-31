# p-status - Project Overview Dashboard

**31/07/2025 00:00 CDMX** | Comprehensive project construction status overview
**LOAD:** /modules:status_dashboard_templates + /modules:project_progress_templates

## Function
Display complete project status, progress across all layers, and overall health.

## Usage
```bash
p-status           # Full project status dashboard
p-status summary   # Condensed overview
p-status health    # Focus on blockers and issues
```

## Dashboard Format → /modules:project_progress_templates

## Health Indicators → /modules:status_dashboard_templates

## Detailed Status Views

### p-status summary
```
📊 [project-type]: Layer [X]/[Total] ([X]% complete)
🎯 Focus: [Current layer description]
⏳ Next Gate: [Days/items until advancement]
🟢 Health: [Status indicator]
```

### p-status health
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

## Core Function
Detailed project metrics and progress analysis with predictive insights

**Analysis Scope**: Layer-specific metrics, velocity tracking, completion estimates, integration status

---
**Authority:** Comprehensive project tracking + health monitoring methodology
**Integration:** → All planning commands, project tracking, health monitoring