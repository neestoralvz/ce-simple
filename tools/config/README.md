# Configuration - VDD Framework Settings

**Purpose**: Configuration files for VDD tools and framework behavior  
**Authority**: Configuration layer - tool behavior control  
**Status**: Active | **Lines**: ≤80

## Configuration Files

### vdd-config.json
Main VDD framework configuration controlling metrics, thresholds, and tool behavior.

## Configuration Sections

### Project Settings
```json
{
  "project_settings": {
    "name": "vdd",
    "vdd_version": "1.0",
    "token_economy_focus": true,
    "sacred_user_space": "user-input/",
    "ai_implementation_space": "docs/",
    "global_commands": "export/commands/"
  }
}
```

### Metric Thresholds
Controls when warnings and alerts are triggered:
- `token_density_minimum`: Minimum content density (0.3)
- `duplication_warning`: Duplication percentage threshold (50.0%)
- `file_length_warning`: File length multiplier (1.5x)
- `implementation_gap_critical`: Critical gap threshold (0.5)

### File Type Limits
Maximum recommended lines per file type:
- `user-input`: 200 lines (sacred user space)
- `docs`: 100 lines (AI implementation)
- `export`: 150 lines (command library)
- `other`: 100 lines (general files)

### Monitoring Settings
Dashboard and continuous monitoring behavior:
- `watch_interval_seconds`: Monitoring frequency (60s)
- `priority_file_count`: Files to highlight (20)
- `alert_thresholds`: Critical warning levels

## Usage

### Direct Configuration
```bash
# Edit configuration
nano tools/config/vdd-config.json

# Validate configuration
python3 -m json.tool tools/config/vdd-config.json
```

### Environment Integration
Configuration is automatically loaded by VDD dashboard tools and validation scripts.

---

**Configuration Philosophy**: Transparent, adjustable settings that adapt to project needs