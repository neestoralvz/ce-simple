# Tools Directory - Development Utilities

**Purpose**: Development tools and utilities for VDD framework  
**Authority**: Tools layer - supporting development workflow  
**Status**: Active | **Lines**: ≤80

## Directory Structure

### 📁 [config/](config/)
Configuration files for VDD tools and dashboards
- `vdd-config.json` - Main VDD framework configuration

### 📁 [dashboards/](dashboards/)  
Monitoring and metrics dashboard tools
- `vdd-dashboard.sh` - Interactive dashboard wrapper script
- `vdd-metrics-dashboard.py` - Python metrics analysis engine

### 📁 [scripts/](scripts/)
Automation and setup scripts  
- `setup-hooks.sh` - Git hooks configuration
- `validate-coherence.sh` - System coherence validation
- `validate-implementation-mandatory.sh` - Implementation validation

### 📁 [templates/](templates/)
Standard templates for VDD components
- Command templates, documentation templates, framework templates
- See [templates/README.md](templates/README.md) for complete listing

## Quick Start

### VDD Metrics Dashboard
```bash
# Basic metrics report
./tools/dashboards/vdd-dashboard.sh

# Continuous monitoring
./tools/dashboards/vdd-dashboard.sh watch

# Quick overview
./tools/dashboards/vdd-dashboard.sh quick
```

### Git Hooks Setup
```bash
# Configure validation hooks
./tools/scripts/setup-hooks.sh
```

### Configuration
Edit `tools/config/vdd-config.json` to customize:
- Metric thresholds and monitoring preferences
- File type limits and alert settings
- Output formatting options

## Dependencies

**Required**: python3, bash, git  
**Optional**: jq (for JSON processing)

## Usage Guidelines

1. **Configuration First**: Review `config/vdd-config.json` before using tools
2. **Dashboard Monitoring**: Use dashboard for regular project health checks  
3. **Template Usage**: Follow template standards for consistent development
4. **Script Automation**: Integrate scripts into development workflow

---

**Tool Philosophy**: Simple, focused utilities that enhance VDD development workflow