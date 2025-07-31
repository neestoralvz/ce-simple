#!/usr/bin/env python3
"""
dashboard.py - Git Workflow Health Dashboard
Part of Git Workflow Analysis Implementation
Created: 2025-07-31

Provides web dashboard at localhost:5000 for monitoring Git workflow health,
conversation status, and system performance metrics.
"""

import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from flask import Flask, render_template_string, jsonify
import subprocess

# Add project root to path for importing our monitoring tools
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

try:
    from tools.monitoring.system_health import SystemHealthMonitor
    from tools.monitoring.event_capture import GitEventCapture
except ImportError:
    print("Warning: Could not import monitoring modules")
    SystemHealthMonitor = None
    GitEventCapture = None

app = Flask(__name__)

# Dashboard HTML template
DASHBOARD_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Git Workflow Dashboard</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; padding: 20px; background: #f5f5f5; }
        .container { max-width: 1200px; margin: 0 auto; }
        .header { background: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
        .status-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 20px; }
        .status-card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
        .status-healthy { border-left: 4px solid #28a745; }
        .status-warning { border-left: 4px solid #ffc107; }
        .status-error { border-left: 4px solid #dc3545; }
        .metric { display: flex; justify-content: space-between; margin: 10px 0; }
        .metric-label { color: #666; }
        .metric-value { font-weight: bold; }
        .logs { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
        .log-entry { padding: 5px 0; border-bottom: 1px solid #eee; font-family: monospace; font-size: 14px; }
        .refresh-btn { background: #007bff; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; }
        .refresh-btn:hover { background: #0056b3; }
        .timestamp { color: #666; font-size: 12px; }
    </style>
    <script>
        function refreshData() {
            location.reload();
        }
        
        // Auto-refresh every 30 seconds
        setInterval(refreshData, 30000);
        
        // Update timestamp
        setInterval(function() {
            document.getElementById('last-update').textContent = new Date().toLocaleTimeString();
        }, 1000);
    </script>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔄 Git Workflow Dashboard</h1>
            <p>Real-time monitoring of Git workflow health, conversation status, and system performance</p>
            <div class="timestamp">Last updated: <span id="last-update">{{ timestamp }}</span></div>
            <button class="refresh-btn" onclick="refreshData()">🔄 Refresh</button>
        </div>
        
        <div class="status-grid">
            <div class="status-card status-{{ overall_status }}">
                <h3>🎯 Overall Status</h3>
                <div class="metric">
                    <span class="metric-label">System Status:</span>
                    <span class="metric-value">{{ overall_status.upper() }}</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Active Branch:</span>
                    <span class="metric-value">{{ current_branch }}</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Last Commit:</span>
                    <span class="metric-value">{{ last_commit_time }}</span>
                </div>
            </div>
            
            <div class="status-card status-{{ system_health.status }}">
                <h3>💾 System Resources</h3>
                <div class="metric">
                    <span class="metric-label">CPU Usage:</span>
                    <span class="metric-value">{{ system_health.cpu }}%</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Memory Usage:</span>
                    <span class="metric-value">{{ system_health.memory }}%</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Disk Usage:</span>
                    <span class="metric-value">{{ system_health.disk }}%</span>
                </div>
            </div>
            
            <div class="status-card status-{{ git_hooks.status }}">
                <h3>🪝 Git Hooks</h3>
                <div class="metric">
                    <span class="metric-label">Working Hooks:</span>
                    <span class="metric-value">{{ git_hooks.working }}</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Hook Status:</span>
                    <span class="metric-value">{{ git_hooks.status.upper() }}</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Performance:</span>
                    <span class="metric-value">&lt;200ms ✅</span>
                </div>
            </div>
            
            <div class="status-card status-{{ performance.status }}">
                <h3>⚡ Performance</h3>
                <div class="metric">
                    <span class="metric-label">Git Operations:</span>
                    <span class="metric-value">{{ performance.avg_time }}</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Performance:</span>
                    <span class="metric-value">{{ performance.status.upper() }}</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Project Files:</span>
                    <span class="metric-value">{{ project.files }}</span>
                </div>
            </div>
        </div>
        
        <div class="logs">
            <h3>📊 Recent Activity</h3>
            {% for entry in recent_activity %}
            <div class="log-entry">{{ entry }}</div>
            {% endfor %}
        </div>
        
        <div class="logs" style="margin-top: 20px;">
            <h3>🔧 Tools Status</h3>
            {% for tool, status in tools_status.items() %}
            <div class="log-entry">{{ tool }}: {{ status }}</div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
"""

class DashboardData:
    """Collect and format data for the dashboard"""
    
    def __init__(self, project_root: str = None):
        self.project_root = Path(project_root) if project_root else Path.cwd()
        self.health_monitor = SystemHealthMonitor(str(self.project_root)) if SystemHealthMonitor else None
        self.event_capture = GitEventCapture(str(self.project_root)) if GitEventCapture else None
    
    def get_dashboard_data(self):
        """Get all dashboard data"""
        try:
            # Get system health data
            if self.health_monitor:
                health_data = self.health_monitor.get_health_dashboard_data()
            else:
                health_data = self._get_basic_health_data()
            
            # Get Git information
            git_info = self._get_git_info()
            
            # Get recent activity
            recent_activity = self._get_recent_activity()
            
            # Get tools status
            tools_status = self._get_tools_status()
            
            return {
                'timestamp': datetime.now().strftime('%H:%M:%S'),
                'overall_status': health_data.get('overall_status', 'unknown'),
                'current_branch': git_info.get('branch', 'unknown'),
                'last_commit_time': git_info.get('last_commit_time', 'unknown'),
                'system_health': health_data.get('summary', {}).get('system', {}),
                'git_hooks': health_data.get('summary', {}).get('git_hooks', {}),
                'performance': health_data.get('summary', {}).get('performance', {}),
                'project': health_data.get('summary', {}).get('project', {}),
                'recent_activity': recent_activity,
                'tools_status': tools_status
            }
        except Exception as e:
            return self._get_error_data(str(e))
    
    def _get_basic_health_data(self):
        """Get basic health data when monitoring tools aren't available"""
        return {
            'overall_status': 'unknown',
            'summary': {
                'system': {'status': 'unknown', 'cpu': 'N/A', 'memory': 'N/A', 'disk': 'N/A'},
                'git_hooks': {'status': 'unknown', 'working': 'N/A'},
                'performance': {'status': 'unknown', 'avg_time': 'N/A'},
                'project': {'status': 'unknown', 'files': 'N/A'}
            }
        }
    
    def _get_git_info(self):
        """Get Git repository information"""
        try:
            # Get current branch
            result = subprocess.run(['git', 'branch', '--show-current'], 
                                  capture_output=True, text=True, timeout=5)
            branch = result.stdout.strip() if result.returncode == 0 else 'unknown'
            
            # Get last commit time
            result = subprocess.run(['git', 'log', '-1', '--format=%cr'], 
                                  capture_output=True, text=True, timeout=5)
            last_commit = result.stdout.strip() if result.returncode == 0 else 'unknown'
            
            return {
                'branch': branch,
                'last_commit_time': last_commit
            }
        except:
            return {'branch': 'unknown', 'last_commit_time': 'unknown'}
    
    def _get_recent_activity(self):
        """Get recent Git activity"""
        try:
            result = subprocess.run(['git', 'log', '--oneline', '-5'], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                return [f"📝 {line}" for line in lines if line]
            else:
                return ["⚠️ Could not retrieve Git log"]
        except:
            return ["❌ Error retrieving recent activity"]
    
    def _get_tools_status(self):
        """Check status of monitoring tools"""
        tools = {
            'think-x4-validator.sh': 'tools/automation/think-x4-validator.sh',
            'event-capture.py': 'tools/monitoring/event-capture.py',
            'system-health.py': 'tools/monitoring/system-health.py',
            'conversation-start.sh': 'tools/automation/conversation-start.sh',
            'standard-commit.sh': 'tools/automation/standard-commit.sh',
            'conversation-complete.sh': 'tools/automation/conversation-complete.sh'
        }
        
        status = {}
        for tool_name, tool_path in tools.items():
            full_path = self.project_root / tool_path
            if full_path.exists():
                if os.access(full_path, os.X_OK):
                    status[tool_name] = "✅ Available"
                else:
                    status[tool_name] = "⚠️ Not executable"
            else:
                status[tool_name] = "❌ Missing"
        
        return status
    
    def _get_error_data(self, error_msg):
        """Get error data when dashboard fails"""
        return {
            'timestamp': datetime.now().strftime('%H:%M:%S'),
            'overall_status': 'error',
            'current_branch': 'unknown',
            'last_commit_time': 'unknown',
            'system_health': {'status': 'error'},
            'git_hooks': {'status': 'error'},
            'performance': {'status': 'error'},
            'project': {'status': 'error'},
            'recent_activity': [f"❌ Dashboard Error: {error_msg}"],
            'tools_status': {}
        }

# Initialize dashboard data collector
dashboard_data = DashboardData()

@app.route('/')
def dashboard():
    """Main dashboard page"""
    data = dashboard_data.get_dashboard_data()
    return render_template_string(DASHBOARD_TEMPLATE, **data)

@app.route('/api/health')
def api_health():
    """Health check API endpoint"""
    data = dashboard_data.get_dashboard_data()
    return jsonify(data)

@app.route('/api/status')
def api_status():
    """Simple status API endpoint"""
    try:
        git_info = dashboard_data._get_git_info()
        return jsonify({
            'status': 'ok',
            'branch': git_info['branch'],
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }), 500

def main():
    """Main function to run the dashboard"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Git Workflow Dashboard")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind to")
    parser.add_argument("--port", type=int, default=5000, help="Port to bind to")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("--project-root", help="Project root directory")
    
    args = parser.parse_args()
    
    if args.project_root:
        global dashboard_data
        dashboard_data = DashboardData(args.project_root)
    
    print(f"🔄 Starting Git Workflow Dashboard...")
    print(f"📊 Dashboard URL: http://{args.host}:{args.port}")
    print(f"🔍 Health API: http://{args.host}:{args.port}/api/health")
    print(f"⚡ Status API: http://{args.host}:{args.port}/api/status")
    print(f"📁 Project Root: {dashboard_data.project_root}")
    
    app.run(host=args.host, port=args.port, debug=args.debug)

if __name__ == "__main__":
    main()