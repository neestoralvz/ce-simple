# CE-Simple Efficiency Dashboard

Real-time performance monitoring system for CE-Simple command ecosystem with multi-subagent orchestration support.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Start dashboard
python3 efficiency-dashboard.py

# Access dashboard
open http://localhost:8080
```

## Architecture

**Multi-Subagent Integration**: Tracks orchestration effectiveness and subagent deployment patterns
**Token Economy Compliance**: Optimizes resource usage and monitors context loading efficiency  
**Real-Time Updates**: WebSocket-based live dashboard with <500ms update intervals
**Non-Intrusive Monitoring**: <5ms execution overhead with graceful degradation

## Components

- `efficiency-dashboard.py` - Main dashboard server with WebSocket support
- `dashboard.html` - Interactive real-time dashboard interface
- `command-hooks.py` - Integration hooks for existing commands
- `integration-guide.md` - Complete integration documentation

## Key Features

- **Performance Metrics**: Command execution times, success rates, resource usage
- **User Pattern Analysis**: Workflow sequences, session duration, efficiency trends
- **System Health Monitoring**: Pipeline status, integration health, performance alerts
- **Subagent Tracking**: Multi-subagent orchestration effectiveness monitoring

## Integration

```python
from tools.dashboards.command_hooks import track_command_performance

@track_command_performance("start")
def start_command():
    # Existing command implementation
    return result
```

## Dashboard Endpoints

- `http://localhost:8080` - Main dashboard interface
- `ws://localhost:8765` - WebSocket real-time updates
- `http://localhost:8080/api/metrics` - JSON metrics API
- `http://localhost:8080/api/command` - Command execution API

See `integration-guide.md` for complete implementation details.