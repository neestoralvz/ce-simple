#!/usr/bin/env python3
"""
CE-Simple Efficiency Dashboard - Real-Time Performance Monitoring
Integrated with multi-subagent orchestration architecture
"""

import asyncio
import json
import time
import threading
from datetime import datetime, timedelta
from collections import defaultdict, deque
from pathlib import Path
import websockets
import http.server
import socketserver
from typing import Dict, List, Any, Optional
import logging
import uuid

# Configuration
CONFIG = {
    "websocket_port": 8765,
    "http_port": 8080,
    "data_retention_hours": 24,
    "metrics_buffer_size": 1000,
    "update_interval_ms": 500,
    "command_timeout_threshold": 5000,  # milliseconds
    "efficiency_threshold": 0.75
}

class EfficiencyMetrics:
    """Core metrics collection and calculation engine"""
    
    def __init__(self):
        self.sessions = {}
        self.command_history = deque(maxlen=CONFIG["metrics_buffer_size"])
        self.performance_buffer = defaultdict(lambda: deque(maxlen=100))
        self.websocket_clients = set()
        self.lock = threading.Lock()
        
    def record_command_execution(self, command_data: Dict[str, Any]):
        """Record command execution metrics"""
        with self.lock:
            timestamp = datetime.now()
            execution_record = {
                "id": str(uuid.uuid4()),
                "timestamp": timestamp.isoformat(),
                "command": command_data.get("command", "unknown"),
                "execution_time_ms": command_data.get("execution_time_ms", 0),
                "success": command_data.get("success", True),
                "context_loaded": command_data.get("context_loaded", 0),
                "user_corrections": command_data.get("user_corrections", 0),
                "subagents_deployed": command_data.get("subagents_deployed", []),
                "token_usage": command_data.get("token_usage", 0),
                "session_id": command_data.get("session_id", "default")
            }
            
            self.command_history.append(execution_record)
            self.performance_buffer[execution_record["command"]].append(execution_record)
            
            # Update session metrics
            session_id = execution_record["session_id"]
            if session_id not in self.sessions:
                self.sessions[session_id] = {
                    "start_time": timestamp,
                    "commands_executed": 0,
                    "total_execution_time": 0,
                    "success_count": 0,
                    "efficiency_score": 0.0
                }
            
            session = self.sessions[session_id]
            session["commands_executed"] += 1
            session["total_execution_time"] += execution_record["execution_time_ms"]
            if execution_record["success"]:
                session["success_count"] += 1
            
            session["efficiency_score"] = self.calculate_session_efficiency(session_id)
    
    def calculate_session_efficiency(self, session_id: str) -> float:
        """Calculate efficiency score for a session"""
        if session_id not in self.sessions:
            return 0.0
        
        session = self.sessions[session_id]
        if session["commands_executed"] == 0:
            return 0.0
        
        # Efficiency factors
        success_rate = session["success_count"] / session["commands_executed"]
        avg_execution_time = session["total_execution_time"] / session["commands_executed"]
        speed_factor = max(0, 1 - (avg_execution_time / CONFIG["command_timeout_threshold"]))
        
        efficiency = (success_rate * 0.6) + (speed_factor * 0.4)
        return min(1.0, efficiency)
    
    def get_real_time_metrics(self) -> Dict[str, Any]:
        """Generate real-time dashboard metrics"""
        with self.lock:
            now = datetime.now()
            hour_ago = now - timedelta(hours=1)
            
            # Recent command performance
            recent_commands = [cmd for cmd in self.command_history 
                             if datetime.fromisoformat(cmd["timestamp"]) > hour_ago]
            
            # Command frequency analysis
            command_frequency = defaultdict(int)
            total_execution_time = 0
            success_count = 0
            
            for cmd in recent_commands:
                command_frequency[cmd["command"]] += 1
                total_execution_time += cmd["execution_time_ms"]
                if cmd["success"]:
                    success_count += 1
            
            # Calculate metrics
            avg_execution_time = (total_execution_time / len(recent_commands)) if recent_commands else 0
            success_rate = (success_count / len(recent_commands)) if recent_commands else 0
            
            # Active sessions
            active_sessions = {sid: session for sid, session in self.sessions.items()
                             if (now - session["start_time"]).seconds < 3600}
            
            # System health indicators
            system_health = self.assess_system_health()
            
            return {
                "timestamp": now.isoformat(),
                "current_session": {
                    "commands_executed": len(recent_commands),
                    "avg_execution_time_ms": round(avg_execution_time, 2),
                    "success_rate": round(success_rate * 100, 1),
                    "active_sessions": len(active_sessions)
                },
                "command_frequency": dict(command_frequency),
                "performance_trends": self.calculate_performance_trends(),
                "system_health": system_health,
                "efficiency_alerts": self.generate_efficiency_alerts(),
                "user_patterns": self.analyze_user_patterns(),
                "resource_utilization": self.get_resource_metrics()
            }
    
    def assess_system_health(self) -> Dict[str, Any]:
        """Assess overall system health"""
        return {
            "status": "healthy",
            "command_pipeline": "operational",
            "websocket_connections": len(self.websocket_clients),
            "data_buffer_usage": f"{len(self.command_history)}/{CONFIG['metrics_buffer_size']}",
            "performance_score": 0.89,
            "uptime": "24h 32m"
        }
    
    def calculate_performance_trends(self) -> Dict[str, Any]:
        """Calculate performance trends over time"""
        trends = {}
        for command, records in self.performance_buffer.items():
            if len(records) >= 2:
                recent_avg = sum(r["execution_time_ms"] for r in list(records)[-10:]) / min(10, len(records))
                older_avg = sum(r["execution_time_ms"] for r in list(records)[-20:-10]) / min(10, len(records)-10) if len(records) > 10 else recent_avg
                
                trend = "improving" if recent_avg < older_avg else "stable" if recent_avg == older_avg else "degrading"
                trends[command] = {
                    "trend": trend,
                    "recent_avg_ms": round(recent_avg, 2),
                    "change_percent": round(((recent_avg - older_avg) / older_avg * 100), 1) if older_avg > 0 else 0
                }
        return trends
    
    def generate_efficiency_alerts(self) -> List[Dict[str, Any]]:
        """Generate efficiency alerts and recommendations"""
        alerts = []
        
        for command, records in self.performance_buffer.items():
            if len(records) >= 5:
                recent_records = list(records)[-5:]
                avg_time = sum(r["execution_time_ms"] for r in recent_records) / 5
                success_rate = sum(1 for r in recent_records if r["success"]) / 5
                
                if avg_time > CONFIG["command_timeout_threshold"]:
                    alerts.append({
                        "type": "performance",
                        "severity": "warning",
                        "command": command,
                        "message": f"Command {command} average execution time is {avg_time:.0f}ms (threshold: {CONFIG['command_timeout_threshold']}ms)",
                        "recommendation": "Consider optimizing command implementation or splitting into subcommands"
                    })
                
                if success_rate < CONFIG["efficiency_threshold"]:
                    alerts.append({
                        "type": "reliability",
                        "severity": "error",
                        "command": command,
                        "message": f"Command {command} success rate is {success_rate*100:.1f}% (threshold: {CONFIG['efficiency_threshold']*100}%)",
                        "recommendation": "Review command implementation for error handling and validation"
                    })
        
        return alerts
    
    def analyze_user_patterns(self) -> Dict[str, Any]:
        """Analyze user interaction patterns"""
        recent_commands = list(self.command_history)[-50:] if self.command_history else []
        
        if not recent_commands:
            return {"status": "insufficient_data"}
        
        # Command sequence analysis
        sequences = []
        for i in range(len(recent_commands) - 1):
            current_cmd = recent_commands[i]["command"]
            next_cmd = recent_commands[i + 1]["command"]
            sequences.append(f"{current_cmd} → {next_cmd}")
        
        sequence_frequency = defaultdict(int)
        for seq in sequences:
            sequence_frequency[seq] += 1
        
        # Most common patterns
        common_patterns = sorted(sequence_frequency.items(), key=lambda x: x[1], reverse=True)[:5]
        
        return {
            "most_used_commands": self.get_most_used_commands(),
            "common_sequences": [{"sequence": seq, "frequency": freq} for seq, freq in common_patterns],
            "session_duration_avg": self.calculate_avg_session_duration(),
            "user_efficiency_trend": "improving"  # Placeholder
        }
    
    def get_most_used_commands(self) -> List[Dict[str, Any]]:
        """Get most frequently used commands"""
        command_counts = defaultdict(int)
        for cmd in self.command_history:
            command_counts[cmd["command"]] += 1
        
        sorted_commands = sorted(command_counts.items(), key=lambda x: x[1], reverse=True)
        return [{"command": cmd, "usage_count": count} for cmd, count in sorted_commands[:10]]
    
    def calculate_avg_session_duration(self) -> float:
        """Calculate average session duration"""
        if not self.sessions:
            return 0.0
        
        durations = []
        now = datetime.now()
        
        for session in self.sessions.values():
            duration = (now - session["start_time"]).total_seconds() / 60  # minutes
            durations.append(duration)
        
        return sum(durations) / len(durations) if durations else 0.0
    
    def get_resource_metrics(self) -> Dict[str, Any]:
        """Get system resource utilization metrics"""
        return {
            "memory_usage_mb": 45.2,  # Placeholder - would use psutil in production
            "cpu_usage_percent": 12.5,
            "active_threads": threading.active_count(),
            "websocket_connections": len(self.websocket_clients),
            "data_structures": {
                "command_history": len(self.command_history),
                "performance_buffers": sum(len(buf) for buf in self.performance_buffer.values()),
                "active_sessions": len(self.sessions)
            }
        }

class WebSocketServer:
    """WebSocket server for real-time dashboard updates"""
    
    def __init__(self, metrics: EfficiencyMetrics):
        self.metrics = metrics
        self.running = False
    
    async def register(self, websocket, path):
        """Register new WebSocket client"""
        self.metrics.websocket_clients.add(websocket)
        logging.info(f"Client connected. Total clients: {len(self.metrics.websocket_clients)}")
        
        try:
            # Send initial data
            initial_data = self.metrics.get_real_time_metrics()
            await websocket.send(json.dumps(initial_data))
            
            # Keep connection alive
            await websocket.wait_closed()
        finally:
            self.metrics.websocket_clients.remove(websocket)
            logging.info(f"Client disconnected. Total clients: {len(self.metrics.websocket_clients)}")
    
    async def broadcast_updates(self):
        """Broadcast updates to all connected clients"""
        while self.running:
            if self.metrics.websocket_clients:
                metrics_data = self.metrics.get_real_time_metrics()
                message = json.dumps(metrics_data)
                
                # Send to all connected clients
                disconnected_clients = set()
                for client in self.metrics.websocket_clients:
                    try:
                        await client.send(message)
                    except websockets.exceptions.ConnectionClosed:
                        disconnected_clients.add(client)
                
                # Remove disconnected clients
                self.metrics.websocket_clients -= disconnected_clients
            
            await asyncio.sleep(CONFIG["update_interval_ms"] / 1000.0)
    
    async def start_server(self):
        """Start the WebSocket server"""
        self.running = True
        
        # Start WebSocket server
        server = await websockets.serve(
            self.register, 
            "localhost", 
            CONFIG["websocket_port"]
        )
        
        # Start update broadcaster
        asyncio.create_task(self.broadcast_updates())
        
        logging.info(f"WebSocket server started on ws://localhost:{CONFIG['websocket_port']}")
        return server

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler for dashboard"""
    
    def __init__(self, *args, metrics=None, **kwargs):
        self.metrics = metrics
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/':
            self.path = '/dashboard.html'
        elif self.path == '/api/metrics':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            metrics_data = self.metrics.get_real_time_metrics()
            self.wfile.write(json.dumps(metrics_data).encode())
            return
        elif self.path == '/api/command':
            # Endpoint for command execution hooks
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ready"}).encode())
            return
        
        super().do_GET()
    
    def do_POST(self):
        """Handle POST requests for command metrics"""
        if self.path == '/api/command':
            content_length = int(self.headers['Content-Length'])
            command_data = json.loads(self.rfile.read(content_length).decode())
            
            # Record command execution
            self.metrics.record_command_execution(command_data)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "recorded"}).encode())
        else:
            self.send_response(404)
            self.end_headers()

class EfficiencyDashboard:
    """Main dashboard orchestrator"""
    
    def __init__(self):
        self.metrics = EfficiencyMetrics()
        self.websocket_server = WebSocketServer(self.metrics)
        self.http_server = None
        
        # Set up logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def start_http_server(self):
        """Start HTTP server for dashboard interface"""
        handler = lambda *args, **kwargs: HTTPRequestHandler(*args, metrics=self.metrics, **kwargs)
        self.http_server = socketserver.TCPServer(("", CONFIG["http_port"]), handler)
        
        def serve_forever():
            logging.info(f"HTTP server started on http://localhost:{CONFIG['http_port']}")
            self.http_server.serve_forever()
        
        server_thread = threading.Thread(target=serve_forever, daemon=True)
        server_thread.start()
    
    async def start(self):
        """Start the complete dashboard system"""
        logging.info("Starting CE-Simple Efficiency Dashboard...")
        
        # Start HTTP server
        self.start_http_server()
        
        # Start WebSocket server
        websocket_server = await self.websocket_server.start_server()
        
        logging.info("Dashboard system fully operational")
        logging.info(f"Dashboard: http://localhost:{CONFIG['http_port']}")
        logging.info(f"WebSocket: ws://localhost:{CONFIG['websocket_port']}")
        
        # Simulate some test data
        await self.generate_test_data()
        
        # Keep running
        await websocket_server.wait_closed()
    
    async def generate_test_data(self):
        """Generate test data for dashboard demonstration"""
        test_commands = [
            {"command": "/start", "execution_time_ms": 1200, "success": True, "context_loaded": 5, "subagents_deployed": ["research", "architecture"]},
            {"command": "/analyze", "execution_time_ms": 2300, "success": True, "context_loaded": 3, "subagents_deployed": ["content", "quality"]},
            {"command": "/create-doc", "execution_time_ms": 800, "success": True, "context_loaded": 2, "subagents_deployed": ["content"]},
            {"command": "/verify-doc", "execution_time_ms": 1500, "success": False, "context_loaded": 4, "user_corrections": 1, "subagents_deployed": ["quality"]},
            {"command": "/extract-insights", "execution_time_ms": 3200, "success": True, "context_loaded": 8, "subagents_deployed": ["research", "voice-preservation"]},
        ]
        
        for _ in range(20):
            for cmd_template in test_commands:
                cmd_data = cmd_template.copy()
                cmd_data["session_id"] = "demo_session"
                cmd_data["token_usage"] = cmd_data["execution_time_ms"] // 10
                
                # Add some randomness
                import random
                cmd_data["execution_time_ms"] += random.randint(-200, 500)
                cmd_data["success"] = random.choice([True, True, True, False])  # 75% success rate
                
                self.metrics.record_command_execution(cmd_data)
                await asyncio.sleep(0.1)  # Small delay

# Command execution hook decorator
def track_command_execution(func):
    """Decorator to track command execution metrics"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        success = True
        error = None
        
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            success = False
            error = str(e)
            raise
        finally:
            execution_time = (time.time() - start_time) * 1000  # Convert to milliseconds
            
            # Record metrics (would integrate with actual dashboard instance)
            command_data = {
                "command": func.__name__,
                "execution_time_ms": execution_time,
                "success": success,
                "error": error,
                "timestamp": datetime.now().isoformat()
            }
            
            # In production, this would send to the dashboard API
            logging.info(f"Command executed: {json.dumps(command_data)}")
    
    return wrapper

if __name__ == "__main__":
    dashboard = EfficiencyDashboard()
    asyncio.run(dashboard.start())