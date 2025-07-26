# VDD Metrics Dashboard - Token Economy Tracking

**Purpose**: Automated monitoring and optimization tool for Vision Driven Development (VDD) projects focusing on token economy efficiency and information value tracking.

## Features

The dashboard tracks **12 specific VDD metrics** designed to optimize token usage and maintain the sacred user-input/ vs docs/ relationship:

### Core Token Economy Metrics

1. **Token Density** (0-1): Valuable information / total tokens
2. **Cross-Reference Count**: How often each file is referenced  
3. **Content Age**: Days since last significant update
4. **File Length**: Current vs recommended line limits
5. **Duplication Score** (0-100%): Similarity with other files
6. **User Input Ratio**: % content from user-input/ vs docs/
7. **Navigation Health**: % files with proper README navigation
8. **Modularization Index**: Average files per concept
9. **Implementation Gap**: Ideas in user-input/ without docs/ derivatives  
10. **Session Efficiency**: Ideas captured per time session
11. **Context Reuse**: Frequency of referencing existing content
12. **Challenge Success**: Ideas refined after challenges

### VDD Framework Integration

- **Sacred User Space**: Respects user-input/ as absolute authority
- **Implementation Tracking**: Monitors docs/ derivatives from user vision
- **Token Optimization**: Identifies content duplication and bloat
- **Context Economy**: Tracks reference patterns and reuse efficiency

## Quick Start

### Run Basic Analysis
```bash
# Simple dashboard report
./vdd-dashboard.sh

# Quick overview (summary only)  
./vdd-dashboard.sh quick

# JSON output for automation
./vdd-dashboard.sh json > metrics.json
```

### Continuous Monitoring  
```bash
# Watch mode (updates every minute)
./vdd-dashboard.sh watch
```

### File-Specific Analysis
```bash
# Analyze single file
./vdd-dashboard.sh file docs/core/project-structure-current.md
```

## Understanding the Output

### Aggregate Metrics Summary
- **token_density**: Overall information value (target: >0.5)
- **user_input_vs_docs_ratio**: Balance between sacred space and implementations  
- **duplication_score**: System-wide content overlap (target: <20%)
- **navigation_health**: README coverage (target: >0.8)

### Top Optimization Opportunities
Automatically identifies:
- High duplication files (>50% similarity)
- Oversized files (>1.5x recommended length)
- Stale content (>30 days old)
- Implementation gaps (user-input/ without docs/ derivatives)
- Low information density (<0.3 token density)

### Priority File Analysis
Files ranked by optimization need:
- **Priority Score**: Combined urgency metric
- **Category**: user-input, docs, or export
- **Key Metrics**: Quick view of all 12 measurements

## Configuration

Edit `vdd-config.json` to customize:

```json
{
  "metric_thresholds": {
    "token_density_minimum": 0.3,
    "duplication_warning": 50.0,
    "file_length_warning": 1.5,
    "content_age_warning": 30
  },
  "file_type_limits": {
    "user-input": 200,
    "docs": 100, 
    "export": 150
  }
}
```

## Current Project Analysis

**Latest scan results for ce-simple:**
- **Files analyzed**: 226
- **Categories**: 4 user-input, 138 docs, 84 export  
- **Token density**: 0.524 (good information value)
- **User-input ratio**: 0.029 (appropriate AI implementation balance)
- **Main issues**: Some duplicate content in docs/core/, oversized files

## Automated Background Tracking

The dashboard runs without user interaction and provides:
- **No manual intervention** required for calculations
- **Per-file metrics** for detailed analysis
- **Simple interface** avoiding overengineering  
- **Token economy focus** for context maintenance
- **Background automation** for continuous monitoring

## Integration with VDD Workflow

### For User-Input Management
- Tracks implementation gaps (user vision without docs/ derivatives)
- Monitors sacred space violations
- Validates user input ratio balance

### For Docs Optimization  
- Identifies duplicate content across files
- Tracks file length vs recommended limits
- Monitors reference patterns and navigation health

### For Token Economy
- Calculates information density per file and aggregate
- Tracks context reuse patterns
- Identifies optimization opportunities

## Technical Details

**Requirements**: Python 3.x (no additional dependencies)
**Performance**: Analyzes 200+ files in ~2 seconds
**Output Formats**: Human-readable text, JSON for automation
**File Types**: Focuses on .md files across VDD structure

**Architecture**:
- `VDDMetricsEngine`: Core calculation engine
- `VDDDashboard`: Reporting and interface layer  
- Configuration-driven thresholds and limits
- Extensible metric system for future enhancements

---

**Core Principle**: This dashboard maintains the VDD token economy by tracking information value density while preserving the sacred user-input/ space and monitoring AI implementation quality in docs/.