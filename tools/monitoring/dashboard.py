#!/usr/bin/env python3
"""
Real-time Health Dashboard
Web-based dashboard for system health and user voice preservation monitoring
"""

import json
import time
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any
from flask import Flask, render_template, jsonify, request
import plotly.graph_objs as go
import plotly.utils
from system_health import MetricsCollector

app = Flask(__name__)

class HealthDashboard:
    """Real-time dashboard for system health monitoring"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.collector = MetricsCollector(base_path)
        self.db_path = self.base_path / "monitoring.db"
    
    def get_dashboard_data(self, hours: int = 24) -> Dict[str, Any]:
        """Get all data needed for dashboard"""
        end_time = time.time()
        start_time = end_time - (hours * 3600)
        
        return {
            'real_time_status': self.collector.get_real_time_status(),
            'system_health_chart': self._get_system_health_chart(start_time, end_time),
            'voice_preservation_chart': self._get_voice_preservation_chart(start_time, end_time),
            'command_performance_chart': self._get_command_performance_chart(start_time, end_time),
            'integration_quality_chart': self._get_integration_quality_chart(start_time, end_time),
            'alerts_table': self._get_recent_alerts(),
            'performance_metrics': self._get_performance_metrics(start_time, end_time),
            'recommendations': self._get_recommendations()
        }
    
    def _get_system_health_chart(self, start_time: float, end_time: float) -> Dict[str, Any]:
        """Generate system health chart data"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('''
                SELECT timestamp, cpu_usage, memory_usage, response_time, 
                       success_rate, availability_score
                FROM system_health 
                WHERE timestamp BETWEEN ? AND ?
                ORDER BY timestamp
            ''', (start_time, end_time))
            
            data = cursor.fetchall()
        
        if not data:
            return {'data': [], 'layout': {}}
        
        timestamps = [datetime.fromtimestamp(row[0]) for row in data]
        cpu_usage = [row[1] for row in data]
        memory_usage = [row[2] for row in data]
        response_time = [row[3] for row in data]
        success_rate = [row[4] for row in data]
        availability = [row[5] for row in data]
        
        traces = [
            go.Scatter(x=timestamps, y=cpu_usage, name='CPU Usage (%)', 
                      line=dict(color='#ff6b6b'), yaxis='y'),
            go.Scatter(x=timestamps, y=memory_usage, name='Memory Usage (%)', 
                      line=dict(color='#4ecdc4'), yaxis='y'),
            go.Scatter(x=timestamps, y=response_time, name='Response Time (s)', 
                      line=dict(color='#45b7d1'), yaxis='y2'),
            go.Scatter(x=timestamps, y=success_rate, name='Success Rate (%)', 
                      line=dict(color='#96ceb4'), yaxis='y'),
            go.Scatter(x=timestamps, y=availability, name='Availability (%)', 
                      line=dict(color='#feca57', width=3), yaxis='y')
        ]
        
        layout = go.Layout(
            title='System Health Metrics',
            xaxis=dict(title='Time'),
            yaxis=dict(title='Percentage / Usage', side='left'),
            yaxis2=dict(title='Response Time (s)', side='right', overlaying='y'),
            hovermode='x unified',
            legend=dict(x=0, y=1)
        )
        
        return {
            'data': traces,
            'layout': layout
        }
    
    def _get_voice_preservation_chart(self, start_time: float, end_time: float) -> Dict[str, Any]:
        """Generate voice preservation chart data"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('''
                SELECT timestamp, intent_preservation_score, context_accuracy,
                       voice_authenticity, decision_fidelity, processed_output_quality
                FROM user_voice 
                WHERE timestamp BETWEEN ? AND ?
                ORDER BY timestamp
            ''', (start_time, end_time))
            
            data = cursor.fetchall()
        
        if not data:
            return {'data': [], 'layout': {}}
        
        timestamps = [datetime.fromtimestamp(row[0]) for row in data]
        intent_preservation = [row[1] for row in data]
        context_accuracy = [row[2] for row in data]
        voice_authenticity = [row[3] for row in data]
        decision_fidelity = [row[4] for row in data]
        output_quality = [row[5] for row in data]
        
        traces = [
            go.Scatter(x=timestamps, y=intent_preservation, name='Intent Preservation', 
                      line=dict(color='#ff6b6b', width=3)),
            go.Scatter(x=timestamps, y=context_accuracy, name='Context Accuracy', 
                      line=dict(color='#4ecdc4')),
            go.Scatter(x=timestamps, y=voice_authenticity, name='Voice Authenticity', 
                      line=dict(color='#45b7d1')),
            go.Scatter(x=timestamps, y=decision_fidelity, name='Decision Fidelity', 
                      line=dict(color='#96ceb4')),
            go.Scatter(x=timestamps, y=output_quality, name='Output Quality', 
                      line=dict(color='#feca57'))
        ]
        
        layout = go.Layout(
            title='User Voice Preservation Metrics',
            xaxis=dict(title='Time'),
            yaxis=dict(title='Score (%)', range=[0, 100]),
            hovermode='x unified',
            legend=dict(x=0, y=1)
        )
        
        return {
            'data': traces,
            'layout': layout
        }
    
    def _get_command_performance_chart(self, start_time: float, end_time: float) -> Dict[str, Any]:
        """Generate command performance chart data"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('''
                SELECT command_name, AVG(execution_time) as avg_time,
                       COUNT(*) as count,
                       SUM(CASE WHEN success THEN 1 ELSE 0 END) * 100.0 / COUNT(*) as success_rate
                FROM command_metrics 
                WHERE timestamp BETWEEN ? AND ?
                GROUP BY command_name
                HAVING count >= 3
                ORDER BY avg_time DESC
            ''', (start_time, end_time))
            
            data = cursor.fetchall()
        
        if not data:
            return {'data': [], 'layout': {}}
        
        commands = [row[0] for row in data]
        avg_times = [row[1] for row in data]
        success_rates = [row[3] for row in data]
        
        traces = [
            go.Bar(x=commands, y=avg_times, name='Avg Execution Time (s)', 
                   marker=dict(color='#45b7d1'), yaxis='y'),
            go.Scatter(x=commands, y=success_rates, name='Success Rate (%)', 
                      line=dict(color='#ff6b6b', width=3), 
                      mode='lines+markers', yaxis='y2')
        ]
        
        layout = go.Layout(
            title='Command Performance Analysis',
            xaxis=dict(title='Commands', tickangle=45),
            yaxis=dict(title='Execution Time (s)', side='left'),
            yaxis2=dict(title='Success Rate (%)', side='right', overlaying='y', range=[0, 100]),
            hovermode='x',
            legend=dict(x=0, y=1)
        )
        
        return {
            'data': traces,
            'layout': layout
        }
    
    def _get_integration_quality_chart(self, start_time: float, end_time: float) -> Dict[str, Any]:
        """Generate integration quality chart data"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('''
                SELECT timestamp, interaction_latency, data_integrity_score, sync_accuracy
                FROM integration_metrics 
                WHERE timestamp BETWEEN ? AND ?
                ORDER BY timestamp
            ''', (start_time, end_time))
            
            data = cursor.fetchall()
        
        if not data:
            return {'data': [], 'layout': {}}
        
        timestamps = [datetime.fromtimestamp(row[0]) for row in data]
        latency = [row[1] for row in data]
        integrity = [row[2] for row in data]
        sync_accuracy = [row[3] for row in data]
        
        traces = [
            go.Scatter(x=timestamps, y=latency, name='Interaction Latency (s)', 
                      line=dict(color='#ff6b6b'), yaxis='y2'),
            go.Scatter(x=timestamps, y=integrity, name='Data Integrity (%)', 
                      line=dict(color='#4ecdc4'), yaxis='y'),
            go.Scatter(x=timestamps, y=sync_accuracy, name='Sync Accuracy (%)', 
                      line=dict(color='#45b7d1'), yaxis='y')
        ]
        
        layout = go.Layout(
            title='Integration Quality Metrics',
            xaxis=dict(title='Time'),
            yaxis=dict(title='Score (%)', side='left'),
            yaxis2=dict(title='Latency (s)', side='right', overlaying='y'),
            hovermode='x unified',
            legend=dict(x=0, y=1)
        )
        
        return {
            'data': traces,
            'layout': layout
        }
    
    def _get_recent_alerts(self, limit: int = 20) -> List[Dict[str, Any]]:
        """Get recent alerts for alerts table"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('''
                SELECT timestamp, alert_type, severity, message, resolved
                FROM alerts 
                ORDER BY timestamp DESC
                LIMIT ?
            ''', (limit,))
            
            data = cursor.fetchall()
        
        alerts = []
        for row in data:
            alerts.append({
                'timestamp': datetime.fromtimestamp(row[0]).strftime('%Y-%m-%d %H:%M:%S'),
                'type': row[1],
                'severity': row[2],
                'message': row[3],
                'resolved': bool(row[4])
            })
        
        return alerts
    
    def _get_performance_metrics(self, start_time: float, end_time: float) -> Dict[str, Any]:
        """Get performance summary metrics"""
        with sqlite3.connect(self.db_path) as conn:
            # System metrics
            system_cursor = conn.execute('''
                SELECT AVG(cpu_usage), AVG(memory_usage), AVG(response_time),
                       AVG(success_rate), AVG(availability_score)
                FROM system_health 
                WHERE timestamp BETWEEN ? AND ?
            ''', (start_time, end_time))
            system_data = system_cursor.fetchone()
            
            # Voice metrics
            voice_cursor = conn.execute('''
                SELECT AVG(intent_preservation_score), AVG(context_accuracy),
                       AVG(voice_authenticity), AVG(decision_fidelity)
                FROM user_voice 
                WHERE timestamp BETWEEN ? AND ?
            ''', (start_time, end_time))
            voice_data = voice_cursor.fetchone()
            
            # Command metrics
            command_cursor = conn.execute('''
                SELECT COUNT(*), AVG(execution_time),
                       SUM(CASE WHEN success THEN 1 ELSE 0 END) * 100.0 / COUNT(*)
                FROM command_metrics 
                WHERE timestamp BETWEEN ? AND ?
            ''', (start_time, end_time))
            command_data = command_cursor.fetchone()
        
        return {
            'system': {
                'avg_cpu': round(system_data[0] or 0, 1),
                'avg_memory': round(system_data[1] or 0, 1),
                'avg_response_time': round(system_data[2] or 0, 3),
                'avg_success_rate': round(system_data[3] or 0, 1),
                'avg_availability': round(system_data[4] or 0, 1)
            },
            'voice': {
                'avg_intent_preservation': round(voice_data[0] or 0, 1),
                'avg_context_accuracy': round(voice_data[1] or 0, 1),
                'avg_voice_authenticity': round(voice_data[2] or 0, 1),
                'avg_decision_fidelity': round(voice_data[3] or 0, 1)
            },
            'commands': {
                'total_commands': int(command_data[0] or 0),
                'avg_execution_time': round(command_data[1] or 0, 3),
                'success_rate': round(command_data[2] or 0, 1)
            }
        }
    
    def _get_recommendations(self) -> List[Dict[str, str]]:
        """Get current system recommendations"""
        recommendations = self.collector._generate_recommendations()
        
        return [
            {
                'type': 'optimization',
                'priority': 'medium',
                'message': rec
            }
            for rec in recommendations
        ]

# Flask routes for web dashboard
dashboard_instance = None

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('dashboard.html')

@app.route('/api/dashboard-data')
def api_dashboard_data():
    """API endpoint for dashboard data"""
    global dashboard_instance
    if not dashboard_instance:
        return jsonify({'error': 'Dashboard not initialized'})
    
    hours = request.args.get('hours', 24, type=int)
    data = dashboard_instance.get_dashboard_data(hours)
    
    # Convert plotly figures to JSON for frontend
    for chart_key in ['system_health_chart', 'voice_preservation_chart', 
                      'command_performance_chart', 'integration_quality_chart']:
        if chart_key in data and data[chart_key]['data']:
            data[chart_key] = json.loads(plotly.utils.PlotlyJSONEncoder().encode({
                'data': data[chart_key]['data'],
                'layout': data[chart_key]['layout']
            }))
    
    return jsonify(data)

@app.route('/api/real-time-status')
def api_real_time_status():
    """API endpoint for real-time status"""
    global dashboard_instance
    if not dashboard_instance:
        return jsonify({'error': 'Dashboard not initialized'})
    
    status = dashboard_instance.collector.get_real_time_status()
    return jsonify(status)

@app.route('/api/alerts')
def api_alerts():
    """API endpoint for alerts"""
    global dashboard_instance
    if not dashboard_instance:
        return jsonify({'error': 'Dashboard not initialized'})
    
    alerts = dashboard_instance._get_recent_alerts()
    return jsonify(alerts)

@app.route('/api/git-event', methods=['POST'])
def api_git_event():
    """API endpoint for receiving real-time git events"""
    try:
        event_data = request.get_json()
        if not event_data:
            return jsonify({'error': 'No event data provided'}), 400
        
        # Log the event (could also trigger real-time updates)
        print(f"Real-time git event: {event_data.get('event_type')} on {event_data.get('git_data', {}).get('branch')}")
        
        return jsonify({'status': 'received', 'event_id': str(time.time())})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/claude-event', methods=['POST'])
def api_claude_event():
    """API endpoint for receiving real-time Claude events"""
    try:
        event_data = request.get_json()
        if not event_data:
            return jsonify({'error': 'No event data provided'}), 400
        
        # Log the event (could also trigger real-time updates)
        print(f"Real-time Claude event: {event_data.get('tool_name')} - {event_data.get('hook_event')}")
        
        return jsonify({'status': 'received', 'event_id': str(time.time())})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/real-time-event', methods=['POST'])
def api_real_time_event():
    """Generic API endpoint for real-time events"""
    try:
        event_data = request.get_json()
        if not event_data:
            return jsonify({'error': 'No event data provided'}), 400
        
        # Log the event
        print(f"Real-time event: {event_data.get('event_type', 'unknown')}")
        
        return jsonify({'status': 'received', 'timestamp': time.time()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# HTML template for dashboard
DASHBOARD_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>System Health Dashboard</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
            color: #2c3e50;
        }
        .status-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .status-card {
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            text-align: center;
        }
        .status-value {
            font-size: 2em;
            font-weight: bold;
            margin: 10px 0;
        }
        .status-label {
            color: #666;
            font-size: 0.9em;
        }
        .chart-container {
            background: white;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .chart {
            height: 400px;
        }
        .alerts-container {
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .alert-item {
            padding: 10px;
            margin: 5px 0;
            border-left: 4px solid #ddd;
            background: #f9f9f9;
        }
        .alert-critical {
            border-left-color: #e74c3c;
        }
        .alert-warning {
            border-left-color: #f39c12;
        }
        .alert-info {
            border-left-color: #3498db;
        }
        .controls {
            text-align: center;
            margin-bottom: 20px;
        }
        .controls select {
            padding: 8px 12px;
            border-radius: 4px;
            border: 1px solid #ddd;
            margin: 0 10px;
        }
        .refresh-indicator {
            position: fixed;
            top: 20px;
            right: 20px;
            background: #2ecc71;
            color: white;
            padding: 10px 15px;
            border-radius: 4px;
            display: none;
        }
        .trend-up { color: #27ae60; }
        .trend-down { color: #e74c3c; }
        .trend-stable { color: #f39c12; }
    </style>
</head>
<body>
    <div class="refresh-indicator" id="refreshIndicator">
        Refreshing data...
    </div>
    
    <div class="header">
        <h1>System Health & User Voice Preservation Dashboard</h1>
        <p>Real-time monitoring of system performance and voice authenticity</p>
    </div>
    
    <div class="controls">
        <label>Time Range:</label>
        <select id="timeRange">
            <option value="1">Last 1 Hour</option>
            <option value="6">Last 6 Hours</option>
            <option value="24" selected>Last 24 Hours</option>
            <option value="168">Last 7 Days</option>
        </select>
        <button onclick="refreshData()">Refresh Now</button>
    </div>
    
    <div id="statusGrid" class="status-grid">
        <!-- Status cards will be populated by JavaScript -->
    </div>
    
    <div class="chart-container">
        <div id="systemHealthChart" class="chart"></div>
    </div>
    
    <div class="chart-container">
        <div id="voicePreservationChart" class="chart"></div>
    </div>
    
    <div class="chart-container">
        <div id="commandPerformanceChart" class="chart"></div>
    </div>
    
    <div class="chart-container">
        <div id="integrationQualityChart" class="chart"></div>
    </div>
    
    <div class="alerts-container">
        <h3>Recent Alerts</h3>
        <div id="alertsList">
            <!-- Alerts will be populated by JavaScript -->
        </div>
    </div>

    <script>
        let refreshInterval;
        
        function showRefreshIndicator() {
            $('#refreshIndicator').show().delay(1000).fadeOut();
        }
        
        function updateStatusCards(status) {
            const statusGrid = $('#statusGrid');
            statusGrid.empty();
            
            const cards = [
                {
                    label: 'Overall Health',
                    value: status.overall_health ? status.overall_health.toFixed(1) + '%' : 'N/A',
                    trend: status.trends ? status.trends.system : 'stable'
                },
                {
                    label: 'Voice Preservation',
                    value: status.voice_metrics ? status.voice_metrics.intent_preservation_score.toFixed(1) + '%' : 'N/A',
                    trend: status.trends ? status.trends.voice : 'stable'
                },
                {
                    label: 'System Availability',
                    value: status.system_metrics ? status.system_metrics.availability_score.toFixed(1) + '%' : 'N/A',
                    trend: status.trends ? status.trends.system : 'stable'
                },
                {
                    label: 'Active Alerts',
                    value: status.active_alerts ? status.active_alerts.length : '0',
                    trend: 'stable'
                }
            ];
            
            cards.forEach(card => {
                const trendClass = `trend-${card.trend}`;
                statusGrid.append(`
                    <div class="status-card">
                        <div class="status-value ${trendClass}">${card.value}</div>
                        <div class="status-label">${card.label}</div>
                    </div>
                `);
            });
        }
        
        function updateAlerts(alerts) {
            const alertsList = $('#alertsList');
            alertsList.empty();
            
            if (alerts.length === 0) {
                alertsList.append('<p>No recent alerts</p>');
                return;
            }
            
            alerts.slice(0, 10).forEach(alert => {
                const alertClass = `alert-${alert.severity}`;
                const resolvedText = alert.resolved ? ' (Resolved)' : '';
                alertsList.append(`
                    <div class="alert-item ${alertClass}">
                        <strong>${alert.type}</strong> - ${alert.severity}${resolvedText}<br>
                        <small>${alert.timestamp}</small><br>
                        ${alert.message}
                    </div>
                `);
            });
        }
        
        function refreshData() {
            showRefreshIndicator();
            const hours = $('#timeRange').val();
            
            // Fetch dashboard data
            $.get(`/api/dashboard-data?hours=${hours}`)
                .done(function(data) {
                    // Update status cards
                    updateStatusCards(data.real_time_status);
                    
                    // Update charts
                    if (data.system_health_chart.data) {
                        Plotly.newPlot('systemHealthChart', 
                            data.system_health_chart.data, 
                            data.system_health_chart.layout);
                    }
                    
                    if (data.voice_preservation_chart.data) {
                        Plotly.newPlot('voicePreservationChart', 
                            data.voice_preservation_chart.data, 
                            data.voice_preservation_chart.layout);
                    }
                    
                    if (data.command_performance_chart.data) {
                        Plotly.newPlot('commandPerformanceChart', 
                            data.command_performance_chart.data, 
                            data.command_performance_chart.layout);
                    }
                    
                    if (data.integration_quality_chart.data) {
                        Plotly.newPlot('integrationQualityChart', 
                            data.integration_quality_chart.data, 
                            data.integration_quality_chart.layout);
                    }
                    
                    // Update alerts
                    updateAlerts(data.alerts_table);
                })
                .fail(function() {
                    console.error('Failed to fetch dashboard data');
                });
        }
        
        // Initialize dashboard
        $(document).ready(function() {
            refreshData();
            
            // Set up auto-refresh every 30 seconds
            refreshInterval = setInterval(function() {
                // Only refresh status, not full charts
                $.get('/api/real-time-status')
                    .done(function(status) {
                        updateStatusCards(status);
                    });
            }, 30000);
            
            // Handle time range changes
            $('#timeRange').change(function() {
                refreshData();
            });
        });
        
        // Clean up on page unload
        $(window).on('beforeunload', function() {
            if (refreshInterval) {
                clearInterval(refreshInterval);
            }
        });
    </script>
</body>
</html>
'''

def run_dashboard(base_path: str = '/Users/nalve/ce-simple/tools/monitoring', 
                 host: str = '127.0.0.1', port: int = 5000):
    """Run the dashboard web server"""
    global dashboard_instance
    
    # Initialize dashboard
    dashboard_instance = HealthDashboard(base_path)
    
    # Create templates directory and file
    templates_dir = Path(base_path) / 'templates'
    templates_dir.mkdir(exist_ok=True)
    
    template_path = templates_dir / 'dashboard.html'
    with open(template_path, 'w') as f:
        f.write(DASHBOARD_TEMPLATE)
    
    # Configure Flask template directory
    app.template_folder = str(templates_dir)
    
    print(f"Starting dashboard server at http://{host}:{port}")
    print("Press Ctrl+C to stop")
    
    app.run(host=host, port=port, debug=False)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Health Dashboard Server')
    parser.add_argument('--base-path', default='/Users/nalve/ce-simple/tools/monitoring',
                       help='Base path for monitoring data')
    parser.add_argument('--host', default='127.0.0.1', help='Host to bind to')
    parser.add_argument('--port', type=int, default=5000, help='Port to bind to')
    
    args = parser.parse_args()
    
    run_dashboard(args.base_path, args.host, args.port)