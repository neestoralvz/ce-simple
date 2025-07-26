# VDD Metrics Dashboard

**Category**: Math & Analytics | **Complexity**: Moderate | **Token Economy**: Track & Optimize

## Purpose
Automated monitoring and optimization tool for Vision Driven Development (VDD) projects focusing on token economy efficiency and information value tracking.

## Usage
```bash
# Run from project root containing vdd-metrics-dashboard.py
./vdd-dashboard.sh [COMMAND]

# Basic analysis
./vdd-dashboard.sh

# Continuous monitoring  
./vdd-dashboard.sh watch

# Quick overview
./vdd-dashboard.sh quick

# JSON export
./vdd-dashboard.sh json > metrics.json

# Single file analysis
./vdd-dashboard.sh file path/to/file.md
```

## 12 Core VDD Metrics Tracked

1. **Token Density**: Valuable information / total tokens (0-1 score)
2. **Cross-Reference Count**: References to each file
3. **Content Age**: Days since last significant update  
4. **File Length**: Current vs recommended line limits
5. **Duplication Score**: Similarity with other files (0-100%)
6. **User Input Ratio**: % content user-input/ vs docs/
7. **Navigation Health**: % files with proper README navigation
8. **Modularization Index**: Average files per concept
9. **Implementation Gap**: Ideas in user-input/ without docs/ derivatives
10. **Session Efficiency**: Ideas captured per time session
11. **Context Reuse**: Frequency of referencing existing content
12. **Challenge Success**: Ideas refined after challenges

## Key Features

### VDD Framework Integration
- **Sacred User Space**: Respects user-input/ as absolute authority
- **Implementation Tracking**: Monitors docs/ derivatives from user vision
- **Token Optimization**: Identifies content duplication and bloat
- **Context Economy**: Tracks reference patterns and reuse efficiency

### Automated Analysis
- **Background calculations** (no user interaction needed)
- **Per-file metrics** display
- **Simple, practical interface** (avoids overengineering)
- **Token economy focus** - optimizes for context maintenance

## Installation

1. **Download Dashboard**: Copy vdd-metrics-dashboard.py to project root
2. **Configure**: Edit vdd-config.json for project-specific settings
3. **Make Executable**: `chmod +x vdd-dashboard.sh`
4. **Test**: Run `./vdd-dashboard.sh quick`

## Output Understanding

### Priority Alerts
- **High duplication** (>50% similarity with other files)
- **Oversized files** (>1.5x recommended length)
- **Stale content** (>30 days without updates)
- **Implementation gaps** (user-input/ without docs/ derivatives)
- **Low token density** (<0.3 information value)

### Health Indicators
- **Token density >0.5**: Good information value
- **Duplication <20%**: Acceptable content overlap
- **Navigation health >0.8**: Good README coverage
- **User-input ratio**: Balanced sacred space vs implementations

## Context Integration

Works with any project following VDD methodology:
- **user-input/**: Sacred user space (absolute authority)
- **docs/**: AI implementations derived from user input
- **export/**: Global command systems

**Technical**: Python 3.x, analyzes .md files, ~2 second performance for 200+ files

---

**Application**: Run regularly to maintain VDD token economy, optimize information density, and track the sacred user-input/ vs docs/ balance for context efficiency.