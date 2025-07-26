# Dashboards - VDD Metrics and Monitoring

**Purpose**: Real-time monitoring and metrics analysis for VDD framework  
**Authority**: Monitoring layer - project health tracking  
**Status**: Active | **Lines**: ≤80

## Dashboard Tools

### vdd-dashboard.sh
Interactive wrapper script providing easy access to VDD metrics with colored output and multiple modes.

**Usage**:
```bash
./vdd-dashboard.sh              # Basic metrics report
./vdd-dashboard.sh watch        # Continuous monitoring
./vdd-dashboard.sh json         # JSON output format
./vdd-dashboard.sh quick        # Quick summary only
./vdd-dashboard.sh file <path>  # Analyze specific file
```

### vdd-metrics-dashboard.py
Core Python metrics analysis engine performing comprehensive project analysis.

**Features**:
- Token economy tracking and optimization suggestions
- Content duplication detection across files
- File age and maintenance status monitoring
- Implementation gap analysis between vision and reality

## Key Metrics

### Token Economy
- **Token Density**: Content efficiency per line
- **Duplication Rate**: Redundant content percentage
- **File Length Ratio**: Size optimization opportunities

### Project Health
- **Implementation Gap**: Vision vs reality alignment
- **Navigation Health**: Cross-reference integrity
- **Content Age**: Maintenance urgency indicators

### Optimization Opportunities
- High-impact files for refactoring
- Content consolidation candidates
- Structure improvement suggestions

## Configuration

Dashboard behavior controlled by `../config/vdd-config.json`:
- Metric thresholds and alert levels
- Monitoring intervals and file limits
- Output formatting preferences

## Dependencies

**Required**: python3, bash  
**Recommended**: colorama (Python package for colored output)

## Output Formats

**Text Mode**: Human-readable with color coding and progress indicators  
**JSON Mode**: Machine-readable for integration with other tools  
**Watch Mode**: Continuous monitoring with real-time updates

---

**Monitoring Philosophy**: Transparent project health visibility with actionable insights