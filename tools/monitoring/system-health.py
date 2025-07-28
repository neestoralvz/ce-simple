#!/usr/bin/env python3  
"""
CE-Simple System Health & User Voice Preservation Monitoring Suite
Claude Code CLI Specific Implementation - 2025 Best Practices
"""

import json
import os
import sqlite3
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from pathlib import Path
from dataclasses import dataclass, asdict
import subprocess
import hashlib
import logging
import time
from collections import defaultdict, deque
import threading
import asyncio

@dataclass
class HealthMetrics:
    """System health metrics following Claude Code best practices"""
    timestamp: str
    system_performance: Dict[str, float]
    user_voice_preservation: Dict[str, float] 
    command_effectiveness: Dict[str, float]
    integration_quality: Dict[str, float]
    claude_code_metrics: Dict[str, float]

@dataclass
class VoicePreservationMetric:
    """User voice preservation tracking specific to Claude Code"""
    session_id: str
    user_decision: str
    preservation_score: float
    authenticity_markers: List[str]
    context_fidelity: float
    decision_traceability: bool
    timestamp: str

class ClaudeCodeHealthMonitor:
    """Comprehensive monitoring for Claude Code CLI operations"""
    
    def __init__(self, data_path: str = "data/monitoring/health.db"):
        self.data_path = Path(data_path)
        self.data_path.parent.mkdir(parents=True, exist_ok=True)
        
        self.init_database()
        
        # Claude Code specific configurations
        self.config = {
            "voice_preservation_threshold": 0.95,
            "system_health_threshold": 0.80,
            "task_tool_success_threshold": 0.90,
            "context_fidelity_minimum": 0.85,
            "integration_quality_target": 0.92,
            "monitoring_interval": 30  # seconds
        }
        
        # Real-time monitoring storage
        self.recent_metrics = deque(maxlen=500)
        self.voice_preservation_cache = deque(maxlen=200)
        self.active_sessions = {}
        self.alert_history = deque(maxlen=100)
        
        # Claude Code tool tracking
        self.tool_usage_stats = defaultdict(lambda: {
            'total_calls': 0,
            'successful_calls': 0, 
            'avg_execution_time': 0.0,
            'context_preservation_rate': 0.0
        })
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Load existing data into caches
        self._load_existing_data()
        
        # Start background monitoring
        self.start_monitoring_thread()
    
    def init_database(self):
        """Initialize SQLite database with Claude Code specific schema"""
        conn = sqlite3.connect(self.data_path)
        
        # System health metrics table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS health_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                system_performance TEXT NOT NULL,
                user_voice_preservation TEXT NOT NULL,
                command_effectiveness TEXT NOT NULL,
                integration_quality TEXT NOT NULL,
                claude_code_metrics TEXT NOT NULL,
                overall_score REAL NOT NULL,
                session_id TEXT
            )
        ''')
        
        # Create indexes
        conn.execute('CREATE INDEX IF NOT EXISTS idx_timestamp ON health_metrics(timestamp)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_score ON health_metrics(overall_score)')
        
        # User voice preservation tracking
        conn.execute('''
            CREATE TABLE IF NOT EXISTS voice_preservation (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                user_decision TEXT NOT NULL,
                preservation_score REAL NOT NULL,
                authenticity_markers TEXT NOT NULL,
                context_fidelity REAL NOT NULL,
                decision_traceability BOOLEAN NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
        
        # Create indexes for voice_preservation
        conn.execute('CREATE INDEX IF NOT EXISTS idx_voice_session ON voice_preservation(session_id)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_voice_score ON voice_preservation(preservation_score)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_voice_timestamp ON voice_preservation(timestamp)')
        
        # Claude Code tool performance
        conn.execute('''
            CREATE TABLE IF NOT EXISTS tool_performance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tool_name TEXT NOT NULL,
                execution_time REAL NOT NULL,
                success BOOLEAN NOT NULL,
                context_preserved BOOLEAN NOT NULL,
                user_voice_maintained BOOLEAN NOT NULL,
                subagent_coordination BOOLEAN,
                timestamp TEXT NOT NULL,
                session_id TEXT
            )
        ''')
        
        # Create indexes for tool_performance
        conn.execute('CREATE INDEX IF NOT EXISTS idx_tool_name ON tool_performance(tool_name)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_tool_timestamp ON tool_performance(timestamp)')
        
        # System alerts and anomalies
        conn.execute('''
            CREATE TABLE IF NOT EXISTS system_alerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                alert_type TEXT NOT NULL,
                severity TEXT NOT NULL,
                message TEXT NOT NULL,
                metrics TEXT,
                resolved BOOLEAN DEFAULT FALSE,
                timestamp TEXT NOT NULL
            )
        ''')
        
        # Create indexes for system_alerts
        conn.execute('CREATE INDEX IF NOT EXISTS idx_alert_type ON system_alerts(alert_type)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_alert_severity ON system_alerts(severity)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_alert_timestamp ON system_alerts(timestamp)')
        
        conn.commit()
        conn.close()
    
    def _load_existing_data(self):
        """Load existing voice preservation data into cache on startup"""
        try:
            conn = sqlite3.connect(self.data_path)
            
            # Load recent voice preservation records (last 24 hours)
            cutoff = (datetime.now() - timedelta(hours=24)).isoformat()
            cursor = conn.execute('''
                SELECT session_id, user_decision, preservation_score, 
                       authenticity_markers, context_fidelity, decision_traceability, timestamp
                FROM voice_preservation 
                WHERE timestamp > ?
                ORDER BY timestamp DESC
                LIMIT 200
            ''', (cutoff,))
            
            voice_records = cursor.fetchall()
            conn.close()
            
            # Populate voice preservation cache
            for record in voice_records:
                voice_metric = VoicePreservationMetric(
                    session_id=record[0],
                    user_decision=record[1], 
                    preservation_score=record[2],
                    authenticity_markers=json.loads(record[3]),
                    context_fidelity=record[4],
                    decision_traceability=bool(record[5]),
                    timestamp=record[6]
                )
                self.voice_preservation_cache.append(voice_metric)
            
            if voice_records:
                self.logger.info(f"Loaded {len(voice_records)} existing voice preservation records into cache")
            else:
                self.logger.warning("No existing voice preservation records found - this may indicate data collection issues")
                
        except Exception as e:
            self.logger.error(f"Error loading existing data: {e}")
    
    def record_tool_execution(self, tool_name: str, execution_time: float, 
                            success: bool, context_preserved: bool = True,
                            user_voice_maintained: bool = True,
                            subagent_coordination: bool = False) -> str:
        """Record Claude Code tool execution metrics"""
        conn = sqlite3.connect(self.data_path)
        
        session_id = self.get_current_session_id()
        
        cursor = conn.execute('''
            INSERT INTO tool_performance 
            (tool_name, execution_time, success, context_preserved, 
             user_voice_maintained, subagent_coordination, timestamp, session_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            tool_name, execution_time, success, context_preserved,
            user_voice_maintained, subagent_coordination,
            datetime.now().isoformat(), session_id
        ))
        
        record_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        # Update real-time stats
        self._update_tool_stats(tool_name, execution_time, success, context_preserved)
        
        # Check for performance alerts
        self._check_tool_performance_alerts(tool_name, execution_time, success)
        
        return str(record_id)
    
    def record_voice_preservation(self, session_id: str, user_decision: str,
                                preservation_score: float, authenticity_markers: List[str],
                                context_fidelity: float, decision_traceability: bool) -> str:
        """Record user voice preservation metrics"""
        voice_metric = VoicePreservationMetric(
            session_id=session_id,
            user_decision=user_decision,
            preservation_score=preservation_score,
            authenticity_markers=authenticity_markers,
            context_fidelity=context_fidelity,
            decision_traceability=decision_traceability,
            timestamp=datetime.now().isoformat()
        )
        
        conn = sqlite3.connect(self.data_path)
        
        cursor = conn.execute('''
            INSERT INTO voice_preservation 
            (session_id, user_decision, preservation_score, authenticity_markers,
             context_fidelity, decision_traceability, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            voice_metric.session_id, voice_metric.user_decision,
            voice_metric.preservation_score, json.dumps(voice_metric.authenticity_markers),
            voice_metric.context_fidelity, voice_metric.decision_traceability,
            voice_metric.timestamp
        ))
        
        record_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        # Add to real-time cache
        self.voice_preservation_cache.append(voice_metric)
        
        # Check voice preservation alerts
        self._check_voice_preservation_alerts(voice_metric)
        
        return str(record_id)
    
    def get_system_health_snapshot(self) -> Dict:
        """Get comprehensive system health snapshot"""
        now = datetime.now()
        
        # System performance metrics
        system_perf = self._calculate_system_performance()
        
        # User voice preservation metrics  
        voice_preservation = self._calculate_voice_preservation_metrics()
        
        # Command effectiveness metrics
        command_effectiveness = self._calculate_command_effectiveness()
        
        # Integration quality metrics
        integration_quality = self._calculate_integration_quality()
        
        # Claude Code specific metrics
        claude_code_metrics = self._calculate_claude_code_metrics()
        
        # Overall health score
        overall_score = self._calculate_overall_health_score(
            system_perf, voice_preservation, command_effectiveness,
            integration_quality, claude_code_metrics
        )
        
        health_snapshot = {
            "timestamp": now.isoformat(),
            "overall_health_score": round(overall_score, 3),
            "system_performance": system_perf,
            "user_voice_preservation": voice_preservation,
            "command_effectiveness": command_effectiveness, 
            "integration_quality": integration_quality,
            "claude_code_metrics": claude_code_metrics,
            "active_alerts": self._get_active_alerts(),
            "recommendations": self._generate_health_recommendations(overall_score)
        }
        
        # Store in database
        self._store_health_metrics(health_snapshot)
        
        return health_snapshot
    
    def _calculate_system_performance(self) -> Dict[str, float]:
        """Calculate system performance metrics"""
        # Get recent tool executions (last hour)
        cutoff = (datetime.now() - timedelta(hours=1)).isoformat()
        
        conn = sqlite3.connect(self.data_path)
        cursor = conn.execute('''
            SELECT AVG(execution_time) as avg_time,
                   AVG(CASE WHEN success THEN 1.0 ELSE 0.0 END) as success_rate,
                   COUNT(*) as total_executions
            FROM tool_performance 
            WHERE timestamp > ?
        ''', (cutoff,))
        
        result = cursor.fetchone()
        conn.close()
        
        if result and result[2] > 0:
            avg_response_time = result[0] or 0.0
            success_rate = result[1] or 0.0
            total_executions = result[2]
            
            # Performance score calculation
            response_score = max(0, 1.0 - (avg_response_time / 10.0))  # 10s max
            performance_score = (response_score * 0.4) + (success_rate * 0.6)
            
            return {
                "avg_response_time": round(avg_response_time, 3),
                "success_rate": round(success_rate, 3),
                "total_executions": total_executions,
                "performance_score": round(performance_score, 3),
                "response_efficiency": round(response_score, 3)
            }
        
        return {
            "avg_response_time": 0.0,
            "success_rate": 0.0, 
            "total_executions": 0,
            "performance_score": 0.0,
            "response_efficiency": 0.0
        }
    
    def _calculate_voice_preservation_metrics(self) -> Dict[str, float]:
        """Calculate user voice preservation metrics"""
        if not self.voice_preservation_cache:
            return {
                "preservation_score": 0.0,
                "authenticity_rate": 0.0,
                "context_fidelity": 0.0,
                "decision_traceability": 0.0,
                "total_decisions": 0
            }
        
        recent_metrics = list(self.voice_preservation_cache)[-50:]  # Last 50 decisions
        
        avg_preservation = sum(m.preservation_score for m in recent_metrics) / len(recent_metrics)
        avg_fidelity = sum(m.context_fidelity for m in recent_metrics) / len(recent_metrics)
        traceability_rate = sum(1 for m in recent_metrics if m.decision_traceability) / len(recent_metrics)
        
        # Authenticity rate based on preservation score threshold
        authenticity_rate = sum(1 for m in recent_metrics 
                              if m.preservation_score >= self.config["voice_preservation_threshold"]) / len(recent_metrics)
        
        return {
            "preservation_score": round(avg_preservation, 3),
            "authenticity_rate": round(authenticity_rate, 3),
            "context_fidelity": round(avg_fidelity, 3),
            "decision_traceability": round(traceability_rate, 3),
            "total_decisions": len(recent_metrics)
        }
    
    def _calculate_command_effectiveness(self) -> Dict[str, float]:
        """Calculate command effectiveness metrics"""
        # Analyze tool usage patterns
        effectiveness_scores = {}
        
        for tool_name, stats in self.tool_usage_stats.items():
            if stats['total_calls'] > 0:
                success_rate = stats['successful_calls'] / stats['total_calls']
                
                # Time efficiency score (lower is better, normalized)
                time_efficiency = max(0, 1.0 - (stats['avg_execution_time'] / 30.0))  # 30s baseline
                
                # Context preservation rate
                context_rate = stats['context_preservation_rate']
                
                # Combined effectiveness score
                effectiveness = (success_rate * 0.4) + (time_efficiency * 0.3) + (context_rate * 0.3)
                effectiveness_scores[tool_name] = round(effectiveness, 3)
        
        if effectiveness_scores:
            avg_effectiveness = sum(effectiveness_scores.values()) / len(effectiveness_scores)
            most_effective = max(effectiveness_scores.items(), key=lambda x: x[1])
            least_effective = min(effectiveness_scores.items(), key=lambda x: x[1])
            
            return {
                "average_effectiveness": round(avg_effectiveness, 3),
                "tool_scores": effectiveness_scores,
                "most_effective_tool": most_effective[0],
                "most_effective_score": most_effective[1],
                "least_effective_tool": least_effective[0],
                "least_effective_score": least_effective[1],
                "total_tools_monitored": len(effectiveness_scores)
            }
        
        return {
            "average_effectiveness": 0.0,
            "tool_scores": {},
            "total_tools_monitored": 0
        }
    
    def _calculate_integration_quality(self) -> Dict[str, float]:
        """Calculate CE-Simple ↔ ContextFlow integration quality"""
        # Check recent integrations
        cutoff = (datetime.now() - timedelta(hours=24)).isoformat()
        
        conn = sqlite3.connect(self.data_path)
        cursor = conn.execute('''
            SELECT AVG(CASE WHEN context_preserved THEN 1.0 ELSE 0.0 END) as context_rate,
                   AVG(CASE WHEN user_voice_maintained THEN 1.0 ELSE 0.0 END) as voice_rate,
                   AVG(CASE WHEN subagent_coordination THEN 1.0 ELSE 0.0 END) as coordination_rate,
                   COUNT(*) as total_integrations
            FROM tool_performance 
            WHERE timestamp > ? AND tool_name LIKE '%contextflow%'
        ''', (cutoff,))
        
        result = cursor.fetchone()
        conn.close()
        
        if result and result[3] > 0:
            context_preservation = result[0] or 0.0
            voice_maintenance = result[1] or 0.0  
            coordination_success = result[2] or 0.0
            total_integrations = result[3]
            
            # Integration quality score
            quality_score = (context_preservation * 0.4) + (voice_maintenance * 0.4) + (coordination_success * 0.2)
            
            return {
                "context_preservation_rate": round(context_preservation, 3),
                "voice_maintenance_rate": round(voice_maintenance, 3),
                "coordination_success_rate": round(coordination_success, 3),
                "integration_quality_score": round(quality_score, 3),
                "total_integrations": total_integrations
            }
        
        return {
            "context_preservation_rate": 0.0,
            "voice_maintenance_rate": 0.0,
            "coordination_success_rate": 0.0,
            "integration_quality_score": 0.0,
            "total_integrations": 0
        }
    
    def _calculate_claude_code_metrics(self) -> Dict[str, float]:
        """Calculate Claude Code CLI specific metrics"""
        # Count Task tool deployments and subagent coordination
        cutoff = (datetime.now() - timedelta(hours=6)).isoformat()
        
        conn = sqlite3.connect(self.data_path)
        
        # Task tool usage
        cursor = conn.execute('''
            SELECT COUNT(*) as task_deployments,
                   AVG(CASE WHEN success THEN 1.0 ELSE 0.0 END) as task_success_rate
            FROM tool_performance 
            WHERE timestamp > ? AND tool_name = 'Task'
        ''', (cutoff,))
        
        task_result = cursor.fetchone()
        
        # Subagent coordination
        cursor = conn.execute('''
            SELECT COUNT(*) as coordination_events,
                   AVG(CASE WHEN subagent_coordination THEN 1.0 ELSE 0.0 END) as coordination_rate
            FROM tool_performance 
            WHERE timestamp > ? AND subagent_coordination IS NOT NULL
        ''', (cutoff,))
        
        coordination_result = cursor.fetchone()
        
        # Parallel execution detection (multiple tools within short timespan)
        cursor = conn.execute('''
            SELECT COUNT(DISTINCT session_id) as parallel_sessions
            FROM (
                SELECT session_id, 
                       COUNT(*) as concurrent_tools,
                       MAX(datetime(timestamp)) - MIN(datetime(timestamp)) as duration_seconds
                FROM tool_performance 
                WHERE timestamp > ?
                GROUP BY session_id
                HAVING concurrent_tools > 1 AND duration_seconds < 60
            )
        ''', (cutoff,))
        
        parallel_result = cursor.fetchone()
        
        conn.close()
        
        # Calculate Claude Code efficiency metrics
        task_deployments = task_result[0] if task_result else 0
        task_success_rate = task_result[1] if task_result and task_result[1] else 0.0
        coordination_events = coordination_result[0] if coordination_result else 0
        coordination_rate = coordination_result[1] if coordination_result and coordination_result[1] else 0.0
        parallel_sessions = parallel_result[0] if parallel_result else 0
        
        # Claude Code optimization score
        optimization_score = (task_success_rate * 0.4) + (coordination_rate * 0.3) + (min(1.0, parallel_sessions / 10) * 0.3)
        
        return {
            "task_tool_deployments": task_deployments,
            "task_success_rate": round(task_success_rate, 3),
            "subagent_coordination_events": coordination_events,
            "coordination_success_rate": round(coordination_rate, 3),
            "parallel_execution_sessions": parallel_sessions,
            "claude_code_optimization_score": round(optimization_score, 3)
        }
    
    def _calculate_overall_health_score(self, system_perf: Dict, voice_preservation: Dict,
                                      command_effectiveness: Dict, integration_quality: Dict,
                                      claude_code_metrics: Dict) -> float:
        """Calculate weighted overall health score"""
        # Weighted scoring based on importance
        weights = {
            "user_voice_preservation": 0.35,  # Highest priority
            "system_performance": 0.25,
            "command_effectiveness": 0.20,
            "integration_quality": 0.15,
            "claude_code_optimization": 0.05
        }
        
        scores = {
            "user_voice_preservation": voice_preservation.get("preservation_score", 0.0),
            "system_performance": system_perf.get("performance_score", 0.0),
            "command_effectiveness": command_effectiveness.get("average_effectiveness", 0.0),
            "integration_quality": integration_quality.get("integration_quality_score", 0.0),
            "claude_code_optimization": claude_code_metrics.get("claude_code_optimization_score", 0.0)
        }
        
        overall_score = sum(scores[metric] * weights[metric] for metric in weights.keys())
        return min(1.0, max(0.0, overall_score))  # Clamp between 0 and 1
    
    def _check_tool_performance_alerts(self, tool_name: str, execution_time: float, success: bool):
        """Check for performance-related alerts"""
        alerts = []
        
        # Long execution time alert
        if execution_time > 30.0:  # 30 seconds
            alerts.append({
                "type": "performance",
                "severity": "warning" if execution_time < 60.0 else "critical",
                "message": f"Tool {tool_name} took {execution_time:.1f}s to execute",
                "tool": tool_name,
                "execution_time": execution_time
            })
        
        # Tool failure alert
        if not success:
            alerts.append({
                "type": "tool_failure",
                "severity": "error",
                "message": f"Tool {tool_name} execution failed",
                "tool": tool_name
            })
        
        # Store alerts
        if alerts:
            self._store_alerts(alerts)
    
    def _check_voice_preservation_alerts(self, voice_metric: VoicePreservationMetric):
        """Check for user voice preservation alerts"""
        alerts = []
        
        # Low preservation score
        if voice_metric.preservation_score < self.config["voice_preservation_threshold"]:
            severity = "critical" if voice_metric.preservation_score < 0.8 else "warning"
            alerts.append({
                "type": "voice_preservation",
                "severity": severity,
                "message": f"User voice preservation score low: {voice_metric.preservation_score:.2f}",
                "session_id": voice_metric.session_id,
                "preservation_score": voice_metric.preservation_score
            })
        
        # Low context fidelity
        if voice_metric.context_fidelity < self.config["context_fidelity_minimum"]:
            alerts.append({
                "type": "context_fidelity",
                "severity": "warning",
                "message": f"Context fidelity below threshold: {voice_metric.context_fidelity:.2f}",
                "session_id": voice_metric.session_id,
                "context_fidelity": voice_metric.context_fidelity
            })
        
        # Decision traceability failure
        if not voice_metric.decision_traceability:
            alerts.append({
                "type": "decision_traceability",
                "severity": "warning",
                "message": "User decision traceability lost",
                "session_id": voice_metric.session_id,
                "user_decision": voice_metric.user_decision[:100]  # Truncate for storage
            })
        
        if alerts:
            self._store_alerts(alerts)
    
    def _store_alerts(self, alerts: List[Dict]):
        """Store system alerts"""
        conn = sqlite3.connect(self.data_path)
        
        for alert in alerts:
            conn.execute('''
                INSERT INTO system_alerts 
                (alert_type, severity, message, metrics, timestamp)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                alert["type"], alert["severity"], alert["message"],
                json.dumps({k: v for k, v in alert.items() if k not in ["type", "severity", "message"]}),
                datetime.now().isoformat()
            ))
        
        conn.commit()
        conn.close()
        
        # Add to alert history
        self.alert_history.extend(alerts)
    
    def _get_active_alerts(self) -> List[Dict]:
        """Get currently active alerts"""
        cutoff = (datetime.now() - timedelta(hours=1)).isoformat()
        
        conn = sqlite3.connect(self.data_path)
        cursor = conn.execute('''
            SELECT alert_type, severity, message, metrics, timestamp
            FROM system_alerts 
            WHERE timestamp > ? AND resolved = FALSE
            ORDER BY timestamp DESC
            LIMIT 20
        ''', (cutoff,))
        
        alerts = []
        for row in cursor.fetchall():
            alert = {
                "type": row[0],
                "severity": row[1],
                "message": row[2],
                "timestamp": row[4]
            }
            
            # Add metrics if available
            try:
                if row[3]:
                    alert.update(json.loads(row[3]))
            except json.JSONDecodeError:
                pass
            
            alerts.append(alert)
        
        conn.close()
        return alerts
    
    def _generate_health_recommendations(self, overall_score: float) -> List[str]:
        """Generate health improvement recommendations"""
        recommendations = []
        
        if overall_score < 0.7:
            recommendations.append("System health critical - immediate attention required")
        elif overall_score < 0.8:
            recommendations.append("System performance degraded - optimization needed")
        
        # Check specific metrics for targeted recommendations
        recent_alerts = list(self.alert_history)[-10:]
        
        voice_alerts = [a for a in recent_alerts if a["type"] in ["voice_preservation", "context_fidelity"]]
        if voice_alerts:
            recommendations.append("User voice preservation issues detected - review context handling")
        
        performance_alerts = [a for a in recent_alerts if a["type"] == "performance"]
        if performance_alerts:
            recommendations.append("Performance degradation detected - consider parallel execution optimization")
        
        tool_failures = [a for a in recent_alerts if a["type"] == "tool_failure"]
        if tool_failures:
            recommendations.append("Tool execution failures detected - review error handling")
        
        return recommendations
    
    def _store_health_metrics(self, health_data: Dict):
        """Store health metrics in database"""
        conn = sqlite3.connect(self.data_path)
        
        conn.execute('''
            INSERT INTO health_metrics 
            (timestamp, system_performance, user_voice_preservation, 
             command_effectiveness, integration_quality, claude_code_metrics,
             overall_score, session_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            health_data["timestamp"],
            json.dumps(health_data["system_performance"]),
            json.dumps(health_data["user_voice_preservation"]),
            json.dumps(health_data["command_effectiveness"]),
            json.dumps(health_data["integration_quality"]),
            json.dumps(health_data["claude_code_metrics"]),
            health_data["overall_health_score"],
            self.get_current_session_id()
        ))
        
        conn.commit()
        conn.close()
    
    def _update_tool_stats(self, tool_name: str, execution_time: float, success: bool, context_preserved: bool):
        """Update real-time tool statistics"""
        stats = self.tool_usage_stats[tool_name]
        
        # Update counters
        stats['total_calls'] += 1
        if success:
            stats['successful_calls'] += 1
        
        # Update moving average for execution time
        current_avg = stats['avg_execution_time']
        total_calls = stats['total_calls']
        stats['avg_execution_time'] = ((current_avg * (total_calls - 1)) + execution_time) / total_calls
        
        # Update context preservation rate
        preservation_count = stats.get('context_preserved_count', 0)
        if context_preserved:
            preservation_count += 1
        stats['context_preserved_count'] = preservation_count
        stats['context_preservation_rate'] = preservation_count / total_calls
    
    def get_current_session_id(self) -> str:
        """Get current session identifier"""
        return f"session_{datetime.now().strftime('%Y%m%d_%H%M')}"
    
    def start_monitoring_thread(self):
        """Start background monitoring thread"""
        def monitoring_loop():
            while True:
                try:
                    # Generate health snapshot
                    health_snapshot = self.get_system_health_snapshot()
                    
                    # Add to recent metrics
                    self.recent_metrics.append(health_snapshot)
                    
                    # Log health status
                    self.logger.info(f"System Health: {health_snapshot['overall_health_score']:.2f}")
                    
                    # Sleep until next monitoring cycle
                    time.sleep(self.config["monitoring_interval"])
                    
                except Exception as e:
                    self.logger.error(f"Monitoring error: {e}")
                    time.sleep(60)  # Wait longer on error
        
        monitor_thread = threading.Thread(target=monitoring_loop, daemon=True)
        monitor_thread.start()
        self.logger.info("System health monitoring started")

# API Interface
class HealthMonitoringAPI:
    """API interface for system health monitoring"""
    
    def __init__(self):
        self.monitor = ClaudeCodeHealthMonitor()
    
    def get_health_status(self) -> Dict:
        """Get current system health status"""
        return self.monitor.get_system_health_snapshot()
    
    def record_tool_usage(self, tool_name: str, execution_time: float, 
                         success: bool, context_preserved: bool = True,
                         user_voice_maintained: bool = True) -> str:
        """Record tool usage for monitoring"""
        return self.monitor.record_tool_execution(
            tool_name, execution_time, success, context_preserved, user_voice_maintained
        )
    
    def record_user_decision(self, user_decision: str, preservation_score: float,
                           authenticity_markers: List[str], context_fidelity: float) -> str:
        """Record user voice preservation metrics"""
        session_id = self.monitor.get_current_session_id()
        decision_traceability = preservation_score >= 0.9  # High preservation = good traceability
        
        return self.monitor.record_voice_preservation(
            session_id, user_decision, preservation_score, authenticity_markers,
            context_fidelity, decision_traceability
        )
    
    def get_alerts(self) -> List[Dict]:
        """Get active system alerts"""
        return self.monitor._get_active_alerts()

# Daemon Mode Implementation
def daemon_mode():
    """Run health monitor in daemon mode for external process management"""
    import signal
    import atexit
    
    # Configuration for daemon mode
    status_file = Path("data/monitoring/health_daemon_status.json")
    status_file.parent.mkdir(parents=True, exist_ok=True)
    
    api = HealthMonitoringAPI()
    
    # Signal handlers for graceful shutdown
    def signal_handler(signum, frame):
        print(f"\nReceived signal {signum}, shutting down gracefully...")
        
        # Update status file
        status_data = {
            "status": "shutting_down",
            "timestamp": datetime.now().isoformat(),
            "signal": signum
        }
        with open(status_file, 'w') as f:
            json.dump(status_data, f, indent=2)
        
        sys.exit(0)
    
    def cleanup_on_exit():
        """Cleanup function called on exit"""
        status_data = {
            "status": "stopped",
            "timestamp": datetime.now().isoformat(),
            "reason": "normal_exit"
        }
        try:
            with open(status_file, 'w') as f:
                json.dump(status_data, f, indent=2)
        except:
            pass  # Don't fail on cleanup
    
    # Register signal handlers
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    atexit.register(cleanup_on_exit)
    
    # Write initial status
    start_time = datetime.now()
    status_data = {
        "status": "running",
        "pid": os.getpid(),
        "started_at": start_time.isoformat(),
        "mode": "daemon"
    }
    with open(status_file, 'w') as f:
        json.dump(status_data, f, indent=2)
    
    print(f"CE-Simple Health Monitor Daemon started (PID: {os.getpid()})")
    print(f"Status file: {status_file}")
    print("Press Ctrl+C to stop")
    
    # Main daemon loop
    cycle_count = 0
    while True:
        try:
            # Get health snapshot
            health = api.get_health_status()
            
            # Update status file with current health
            status_data = {
                "status": "running",
                "pid": os.getpid(),
                "started_at": start_time.isoformat(),
                "last_update": datetime.now().isoformat(),
                "cycle_count": cycle_count,
                "mode": "daemon",
                "health_score": health["overall_health_score"],
                "voice_preservation": health["user_voice_preservation"]["preservation_score"],
                "active_alerts": len(health["active_alerts"])
            }
            with open(status_file, 'w') as f:
                json.dump(status_data, f, indent=2)
            
            # Log every 10 cycles (5 minutes with 30s intervals)
            if cycle_count % 10 == 0:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Health: {health['overall_health_score']:.2f}, "
                      f"Voice: {health['user_voice_preservation']['preservation_score']:.2f}, "
                      f"Alerts: {len(health['active_alerts'])}")
            
            cycle_count += 1
            time.sleep(30)  # 30 second intervals
            
        except KeyboardInterrupt:
            print("\nDaemon interrupted by user")
            break
        except Exception as e:
            print(f"Error in daemon loop: {e}")
            
            # Update status with error
            status_data = {
                "status": "error",
                "pid": os.getpid(),
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
            try:
                with open(status_file, 'w') as f:
                    json.dump(status_data, f, indent=2)
            except:
                pass
            
            time.sleep(60)  # Wait longer on error

# CLI Interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "daemon":
            daemon_mode()
            sys.exit(0)
        
        api = HealthMonitoringAPI()
        
        if command == "status":
            health = api.get_health_status()
            print(json.dumps(health, indent=2))
        
        elif command == "record-tool":
            tool_name = sys.argv[2] if len(sys.argv) > 2 else "unknown"
            exec_time = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
            success = sys.argv[4].lower() == 'true' if len(sys.argv) > 4 else True
            
            record_id = api.record_tool_usage(tool_name, exec_time, success)
            print(f"Recorded tool usage: {record_id}")
        
        elif command == "record-voice":
            decision = sys.argv[2] if len(sys.argv) > 2 else "test decision"
            score = float(sys.argv[3]) if len(sys.argv) > 3 else 0.95
            fidelity = float(sys.argv[4]) if len(sys.argv) > 4 else 0.90
            
            record_id = api.record_user_decision(decision, score, ["authentic"], fidelity)
            print(f"Recorded user voice: {record_id}")
        
        elif command == "alerts":
            alerts = api.get_alerts()
            print(json.dumps(alerts, indent=2))
        
        elif command == "daemon-status":
            # Check daemon status from file
            status_file = Path("data/monitoring/health_daemon_status.json")
            if status_file.exists():
                with open(status_file, 'r') as f:
                    status = json.load(f)
                print(json.dumps(status, indent=2))
            else:
                print(json.dumps({"status": "not_running"}, indent=2))
        
        else:
            print("Usage: python system-health.py [daemon|status|record-tool|record-voice|alerts|daemon-status] [args...]")
            print("")
            print("Commands:")
            print("  daemon       - Run in daemon mode (for external launcher)")
            print("  status       - Show current health status")
            print("  daemon-status- Show daemon status from file")
            print("  record-tool  - Record tool usage")
            print("  record-voice - Record voice preservation")
            print("  alerts       - Show active alerts")
    
    else:
        print("CE-Simple System Health Monitor - Claude Code CLI Specific")
        print("Real-time monitoring of system health and user voice preservation")
        print("")
        print("Run with 'daemon' for background monitoring via external launcher")
        
        # Show current status
        api = HealthMonitoringAPI()
        health = api.get_health_status()
        print(f"\nCurrent Health Score: {health['overall_health_score']:.2f}")
        print(f"User Voice Preservation: {health['user_voice_preservation']['preservation_score']:.2f}")
        print(f"System Performance: {health['system_performance']['performance_score']:.2f}")
        
        if health['active_alerts']:
            print(f"\nActive Alerts: {len(health['active_alerts'])}")
            for alert in health['active_alerts'][:3]:
                print(f"  - {alert['severity'].upper()}: {alert['message']}")