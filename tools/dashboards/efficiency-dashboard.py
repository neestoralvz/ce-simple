#!/usr/bin/env python3
"""
CE-Simple Efficiency Dashboard
Real-time command performance tracking with research-driven 2025 best practices
"""

import json
import time
import os
import sqlite3
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from pathlib import Path
import subprocess
from dataclasses import dataclass, asdict
from collections import defaultdict, deque
import asyncio
import websockets
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
import logging

@dataclass
class CommandMetrics:
    """Command execution metrics following 2025 monitoring best practices"""
    timestamp: str
    command: str
    execution_time: float
    success: bool
    token_usage: int
    user_context: str
    error_message: Optional[str] = None
    resource_usage: Dict[str, float] = None

class MetricsCollector:
    """Research-driven metrics collection with real-time capabilities"""
    
    def __init__(self, db_path: str = "data/metrics/efficiency.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.init_database()
        
        # Real-time storage (following 2025 best practices)
        self.recent_metrics = deque(maxlen=1000)
        self.active_sessions = {}
        self.pattern_cache = {}
        
        # Performance thresholds (research-based defaults)
        self.thresholds = {
            'response_time_warning': 2.0,
            'response_time_critical': 5.0,
            'error_rate_warning': 0.05,
            'error_rate_critical': 0.10,
            'token_efficiency_minimum': 0.7
        }
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
    
    def init_database(self):
        """Initialize SQLite database with optimized schema"""
        conn = sqlite3.connect(self.db_path)
        conn.execute('''
            CREATE TABLE IF NOT EXISTS command_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                command TEXT NOT NULL,
                execution_time REAL NOT NULL,
                success BOOLEAN NOT NULL,
                token_usage INTEGER NOT NULL,
                user_context TEXT,
                error_message TEXT,
                resource_usage TEXT,
                session_id TEXT,
                INDEX(timestamp),
                INDEX(command),
                INDEX(success)
            )
        ''')
        
        conn.execute('''
            CREATE TABLE IF NOT EXISTS performance_trends (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                avg_response_time REAL,
                success_rate REAL,
                total_commands INTEGER,
                unique_users INTEGER,
                INDEX(date)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def record_command(self, metrics: CommandMetrics) -> str:
        """Record command execution with real-time processing"""
        # Store in database
        conn = sqlite3.connect(self.db_path)
        resource_json = json.dumps(metrics.resource_usage) if metrics.resource_usage else None
        
        cursor = conn.execute('''
            INSERT INTO command_metrics 
            (timestamp, command, execution_time, success, token_usage, 
             user_context, error_message, resource_usage, session_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            metrics.timestamp, metrics.command, metrics.execution_time,
            metrics.success, metrics.token_usage, metrics.user_context,
            metrics.error_message, resource_json, 
            self.get_current_session_id()
        ))
        
        record_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        # Add to real-time cache
        self.recent_metrics.append(metrics)
        
        # Trigger alerts if needed
        self._check_performance_alerts(metrics)
        
        return str(record_id)
    
    def get_real_time_metrics(self) -> Dict:
        """Get current performance metrics for dashboard"""
        if not self.recent_metrics:
            return {"status": "no_data"}
        
        recent_window = 300  # 5 minutes
        now = datetime.now()
        recent_data = [
            m for m in self.recent_metrics 
            if (now - datetime.fromisoformat(m.timestamp)).seconds < recent_window
        ]
        
        if not recent_data:
            return {"status": "no_recent_data"}
        
        # Calculate key metrics following research best practices
        total_commands = len(recent_data)
        successful_commands = sum(1 for m in recent_data if m.success)
        avg_response_time = sum(m.execution_time for m in recent_data) / total_commands
        success_rate = successful_commands / total_commands
        
        # Command frequency analysis
        command_frequency = defaultdict(int)
        for m in recent_data:
            command_frequency[m.command] += 1
        
        # Performance health score (0-100)
        health_score = self._calculate_health_score(avg_response_time, success_rate)
        
        return {
            "timestamp": now.isoformat(),
            "total_commands": total_commands,
            "success_rate": round(success_rate, 3),
            "avg_response_time": round(avg_response_time, 3),
            "health_score": health_score,
            "most_used_commands": dict(sorted(command_frequency.items(), 
                                            key=lambda x: x[1], reverse=True)[:5]),
            "alerts": self._get_active_alerts(),
            "trend_direction": self._calculate_trend()
        }
    
    def get_historical_data(self, hours: int = 24) -> Dict:
        """Get historical performance data"""
        conn = sqlite3.connect(self.db_path)
        
        start_time = (datetime.now() - timedelta(hours=hours)).isoformat()
        
        cursor = conn.execute('''
            SELECT 
                strftime('%Y-%m-%d %H:00', timestamp) as hour,
                AVG(execution_time) as avg_time,
                AVG(CASE WHEN success THEN 1.0 ELSE 0.0 END) as success_rate,
                COUNT(*) as command_count
            FROM command_metrics 
            WHERE timestamp > ?
            GROUP BY hour
            ORDER BY hour
        ''', (start_time,))
        
        hourly_data = cursor.fetchall()
        conn.close()
        
        return {
            "timeframe_hours": hours,
            "data_points": [
                {
                    "hour": row[0],
                    "avg_response_time": round(row[1], 3),
                    "success_rate": round(row[2], 3),
                    "command_count": row[3]
                }
                for row in hourly_data
            ]
        }
    
    def _calculate_health_score(self, avg_response_time: float, success_rate: float) -> int:
        """Calculate overall system health score using research-based formula"""
        # Response time score (0-50 points)
        if avg_response_time <= 1.0:
            time_score = 50
        elif avg_response_time <= 2.0:
            time_score = 40
        elif avg_response_time <= 5.0:
            time_score = 25
        else:
            time_score = 0
        
        # Success rate score (0-50 points)
        success_score = int(success_rate * 50)
        
        return min(100, time_score + success_score)
    
    def _check_performance_alerts(self, metrics: CommandMetrics):
        """Check for performance alerts based on thresholds"""
        alerts = []
        
        if metrics.execution_time > self.thresholds['response_time_critical']:
            alerts.append({
                "level": "critical",
                "type": "response_time",
                "message": f"Command {metrics.command} took {metrics.execution_time:.2f}s",
                "timestamp": metrics.timestamp
            })
        elif metrics.execution_time > self.thresholds['response_time_warning']:
            alerts.append({
                "level": "warning",
                "type": "response_time",
                "message": f"Slow response for {metrics.command}: {metrics.execution_time:.2f}s",
                "timestamp": metrics.timestamp
            })
        
        if not metrics.success:
            alerts.append({
                "level": "error",
                "type": "command_failure",
                "message": f"Command failed: {metrics.command}",
                "error": metrics.error_message,
                "timestamp": metrics.timestamp
            })
        
        # Store alerts for dashboard
        if alerts:
            self._store_alerts(alerts)
    
    def _store_alerts(self, alerts: List[Dict]):
        """Store alerts for real-time dashboard display"""
        alert_file = Path("data/metrics/alerts.json")
        alert_file.parent.mkdir(parents=True, exist_ok=True)
        
        existing_alerts = []
        if alert_file.exists():
            with open(alert_file) as f:
                existing_alerts = json.load(f)
        
        # Keep only recent alerts (last hour)
        now = datetime.now()
        cutoff = now - timedelta(hours=1)
        
        recent_alerts = [
            alert for alert in existing_alerts
            if datetime.fromisoformat(alert["timestamp"]) > cutoff
        ]
        
        recent_alerts.extend(alerts)
        
        with open(alert_file, 'w') as f:
            json.dump(recent_alerts, f, indent=2)
    
    def _get_active_alerts(self) -> List[Dict]:
        """Get currently active alerts"""
        alert_file = Path("data/metrics/alerts.json")
        if not alert_file.exists():
            return []
        
        with open(alert_file) as f:
            alerts = json.load(f)
        
        return alerts[-10:]  # Return last 10 alerts
    
    def _calculate_trend(self) -> str:
        """Calculate performance trend direction"""
        if len(self.recent_metrics) < 10:
            return "insufficient_data"
        
        recent_10 = list(self.recent_metrics)[-10:]
        older_10 = list(self.recent_metrics)[-20:-10] if len(self.recent_metrics) >= 20 else []
        
        if not older_10:
            return "baseline"
        
        recent_avg = sum(m.execution_time for m in recent_10) / len(recent_10)
        older_avg = sum(m.execution_time for m in older_10) / len(older_10)
        
        if recent_avg < older_avg * 0.9:
            return "improving"
        elif recent_avg > older_avg * 1.1:
            return "degrading"
        else:
            return "stable"
    
    def get_current_session_id(self) -> str:
        """Get current session identifier"""
        return f"session_{datetime.now().strftime('%Y%m%d_%H%M')}"

class DashboardServer:
    """Real-time dashboard server with WebSocket support"""
    
    def __init__(self, collector: MetricsCollector, port: int = 8080):
        self.collector = collector
        self.port = port
        self.websocket_clients = set()
        
    def start(self):
        """Start dashboard server with real-time updates"""
        # Create dashboard HTML
        self._create_dashboard_html()
        
        # Start WebSocket server for real-time updates
        websocket_thread = threading.Thread(
            target=self._start_websocket_server,
            daemon=True
        )
        websocket_thread.start()
        
        # Start HTTP server for dashboard
        http_thread = threading.Thread(
            target=self._start_http_server,
            daemon=True
        )
        http_thread.start()
        
        print(f"Efficiency Dashboard running at http://localhost:{self.port}")
        print(f"WebSocket updates at ws://localhost:{self.port + 1}")
        
        return http_thread, websocket_thread
    
    def _create_dashboard_html(self):
        """Create responsive dashboard HTML with research-based design"""
        dashboard_dir = Path("tools/dashboards/web")
        dashboard_dir.mkdir(parents=True, exist_ok=True)
        
        html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CE-Simple Efficiency Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f5f5f5;
        }
        .dashboard-header {
            text-align: center;
            margin-bottom: 30px;
        }
        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .metric-card {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .metric-value {
            font-size: 2em;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .metric-label {
            color: #666;
            font-size: 0.9em;
        }
        .health-score {
            text-align: center;
        }
        .health-good { color: #28a745; }
        .health-warning { color: #ffc107; }
        .health-critical { color: #dc3545; }
        .alerts-panel {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .alert {
            padding: 10px;
            margin: 5px 0;
            border-radius: 4px;
        }
        .alert-critical { background: #f8d7da; color: #721c24; }
        .alert-warning { background: #fff3cd; color: #856404; }
        .alert-error { background: #f8d7da; color: #721c24; }
        .chart-container {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-top: 20px;
        }
        .status-indicator {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            display: inline-block;
            margin-right: 5px;
        }
        .status-online { background: #28a745; }
        .status-warning { background: #ffc107; }
        .status-offline { background: #dc3545; }
    </style>
</head>
<body>
    <div class="dashboard-header">
        <h1>CE-Simple Efficiency Dashboard</h1>
        <p>Real-time command performance monitoring</p>
        <span id="connection-status" class="status-indicator status-offline"></span>
        <span id="last-update">Connecting...</span>
    </div>
    
    <div class="metrics-grid">
        <div class="metric-card">
            <div class="metric-value" id="total-commands">-</div>
            <div class="metric-label">Commands (5min)</div>
        </div>
        <div class="metric-card">
            <div class="metric-value" id="success-rate">-</div>
            <div class="metric-label">Success Rate</div>
        </div>
        <div class="metric-card">
            <div class="metric-value" id="avg-response">-</div>
            <div class="metric-label">Avg Response Time</div>
        </div>
        <div class="metric-card health-score">
            <div class="metric-value" id="health-score">-</div>
            <div class="metric-label">System Health</div>
        </div>
    </div>
    
    <div class="chart-container">
        <h3>Response Time Trend</h3>
        <canvas id="response-chart"></canvas>
    </div>
    
    <div class="alerts-panel">
        <h3>Recent Alerts</h3>
        <div id="alerts-container">No alerts</div>
    </div>
    
    <script>
        const ws = new WebSocket('ws://localhost:8081');
        const connectionStatus = document.getElementById('connection-status');
        const lastUpdate = document.getElementById('last-update');
        
        // Chart setup
        const ctx = document.getElementById('response-chart').getContext('2d');
        const responseChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [],
                datasets: [{
                    label: 'Response Time (s)',
                    data: [],
                    borderColor: '#007bff',
                    tension: 0.1
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
        
        ws.onopen = function() {
            connectionStatus.className = 'status-indicator status-online';
            lastUpdate.textContent = 'Connected';
        };
        
        ws.onmessage = function(event) {
            const data = JSON.parse(event.data);
            updateDashboard(data);
        };
        
        ws.onclose = function() {
            connectionStatus.className = 'status-indicator status-offline';
            lastUpdate.textContent = 'Disconnected';
        };
        
        function updateDashboard(data) {
            if (data.status && data.status !== 'ok') {
                return;
            }
            
            // Update metrics
            document.getElementById('total-commands').textContent = data.total_commands;
            document.getElementById('success-rate').textContent = (data.success_rate * 100).toFixed(1) + '%';
            document.getElementById('avg-response').textContent = data.avg_response_time.toFixed(2) + 's';
            
            // Update health score with color
            const healthScore = data.health_score;
            const healthElement = document.getElementById('health-score');
            healthElement.textContent = healthScore;
            healthElement.className = 'metric-value ' + 
                (healthScore >= 80 ? 'health-good' : 
                 healthScore >= 60 ? 'health-warning' : 'health-critical');
            
            // Update connection status
            connectionStatus.className = 'status-indicator ' + 
                (healthScore >= 80 ? 'status-online' : 'status-warning');
            lastUpdate.textContent = 'Updated: ' + new Date().toLocaleTimeString();
            
            // Update alerts
            updateAlerts(data.alerts || []);
            
            // Update chart (simplified for demo)
            if (responseChart.data.labels.length > 20) {
                responseChart.data.labels.shift();
                responseChart.data.datasets[0].data.shift();
            }
            responseChart.data.labels.push(new Date().toLocaleTimeString());
            responseChart.data.datasets[0].data.push(data.avg_response_time);
            responseChart.update();
        }
        
        function updateAlerts(alerts) {
            const container = document.getElementById('alerts-container');
            if (alerts.length === 0) {
                container.innerHTML = 'No recent alerts';
                return;
            }
            
            container.innerHTML = alerts.map(alert => 
                `<div class="alert alert-${alert.level}">
                    <strong>${alert.type}</strong>: ${alert.message}
                    <br><small>${new Date(alert.timestamp).toLocaleString()}</small>
                </div>`
            ).join('');
        }
        
        // Request initial data
        fetch('/api/metrics')
            .then(response => response.json())
            .then(data => updateDashboard(data))
            .catch(console.error);
    </script>
</body>
</html>'''
        
        with open(dashboard_dir / "index.html", 'w') as f:
            f.write(html_content)
    
    def _start_websocket_server(self):
        """Start WebSocket server for real-time updates"""
        async def handle_client(websocket, path):
            self.websocket_clients.add(websocket)
            try:
                await websocket.wait_closed()
            finally:
                self.websocket_clients.remove(websocket)
        
        async def broadcast_updates():
            while True:
                if self.websocket_clients:
                    metrics = self.collector.get_real_time_metrics()
                    message = json.dumps(metrics)
                    
                    # Broadcast to all connected clients
                    disconnected = set()
                    for client in self.websocket_clients:
                        try:
                            await client.send(message)
                        except:
                            disconnected.add(client)
                    
                    # Remove disconnected clients
                    for client in disconnected:
                        self.websocket_clients.discard(client)
                
                await asyncio.sleep(5)  # Update every 5 seconds
        
        async def main():
            server = await websockets.serve(handle_client, "localhost", self.port + 1)
            await asyncio.gather(
                server.wait_closed(),
                broadcast_updates()
            )
        
        asyncio.run(main())
    
    def _start_http_server(self):
        """Start HTTP server for dashboard"""
        os.chdir("tools/dashboards/web")
        server = HTTPServer(("localhost", self.port), SimpleHTTPRequestHandler)
        server.serve_forever()

# Command line interface
if __name__ == "__main__":
    import sys
    
    collector = MetricsCollector()
    
    if len(sys.argv) > 1 and sys.argv[1] == "record":
        # Record a test command
        metrics = CommandMetrics(
            timestamp=datetime.now().isoformat(),
            command=sys.argv[2] if len(sys.argv) > 2 else "test-command",
            execution_time=float(sys.argv[3]) if len(sys.argv) > 3 else 1.5,
            success=True,
            token_usage=150,
            user_context="cli-test",
            resource_usage={"cpu": 0.3, "memory": 0.2}
        )
        record_id = collector.record_command(metrics)
        print(f"Recorded command metrics: {record_id}")
    
    elif len(sys.argv) > 1 and sys.argv[1] == "server":
        # Start dashboard server
        dashboard = DashboardServer(collector)
        http_thread, ws_thread = dashboard.start()
        
        try:
            http_thread.join()
        except KeyboardInterrupt:
            print("\nShutting down dashboard...")
    
    else:
        # Show current metrics
        metrics = collector.get_real_time_metrics()
        print("Current System Metrics:")
        print(json.dumps(metrics, indent=2))