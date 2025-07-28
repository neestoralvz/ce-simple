#!/usr/bin/env python3
"""
Claude Code Health Monitoring System
Comprehensive health tracking for Claude Code CLI operations, session management, and system performance
"""

import json
import time
import datetime
import psutil
import threading
from pathlib import Path
from typing import Dict, List, Any, Optional
import sqlite3
from dataclasses import dataclass, asdict
import logging
from enum import Enum

class HealthStatus(Enum):
    HEALTHY = "healthy"
    WARNING = "warning"
    CRITICAL = "critical"
    UNKNOWN = "unknown"

@dataclass
class HealthMetric:
    """Individual health metric for Claude Code operations"""
    name: str
    value: float
    status: HealthStatus
    threshold_warning: float
    threshold_critical: float
    timestamp: datetime.datetime
    context: Dict[str, Any]

@dataclass
class SystemHealth:
    """Overall system health assessment"""
    overall_status: HealthStatus
    health_score: float
    metrics: List[HealthMetric]
    recommendations: List[str]
    last_updated: datetime.datetime

class ClaudeCodeHealthMonitor:
    """
    Comprehensive health monitoring specifically for Claude Code CLI operations
    Tracks performance, session health, Task tool effectiveness, and system resources
    """
    
    def __init__(self, workspace_path: str = "/Users/nalve/ce-simple"):
        self.workspace = Path(workspace_path)
        self.db_path = self.workspace / "data" / "claude-code-health.db"
        self.monitoring_active = False
        self.monitoring_thread = None
        self.session_id = f"health-monitor-{int(time.time())}"
        
        # Health thresholds specific to Claude Code operations
        self.thresholds = {
            'task_tool_success_rate': {'warning': 0.8, 'critical': 0.6},
            'context_loading_time': {'warning': 3.0, 'critical': 5.0},
            'parallel_execution_efficiency': {'warning': 0.7, 'critical': 0.5},
            'session_continuity_score': {'warning': 0.8, 'critical': 0.6},
            'token_economy_efficiency': {'warning': 0.8, 'critical': 0.6},
            'command_response_time': {'warning': 10.0, 'critical': 20.0},
            'memory_usage_mb': {'warning': 1024, 'critical': 2048},
            'cpu_usage_percent': {'warning': 80, 'critical': 95},
            'disk_usage_percent': {'warning': 85, 'critical': 95}
        }
        
        self.init_database()
        self.setup_logging()
        
    def setup_logging(self):
        """Setup logging for health monitoring"""
        log_path = self.workspace / "data" / "health-monitor.log"
        log_path.parent.mkdir(exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_path),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger(__name__)
    
    def init_database(self):
        """Initialize SQLite database for health metrics"""
        self.db_path.parent.mkdir(exist_ok=True)
        
        with sqlite3.connect(self.db_path) as conn:
            # Health metrics table
            conn.execute("""
                CREATE TABLE IF NOT EXISTS health_metrics (
                    id INTEGER PRIMARY KEY,
                    session_id TEXT,
                    timestamp DATETIME,
                    metric_name TEXT,
                    metric_value REAL,
                    status TEXT,
                    threshold_warning REAL,
                    threshold_critical REAL,
                    context TEXT
                )
            """)
            
            # System health snapshots
            conn.execute("""
                CREATE TABLE IF NOT EXISTS system_health_snapshots (
                    id INTEGER PRIMARY KEY,
                    session_id TEXT,
                    timestamp DATETIME,
                    overall_status TEXT,
                    health_score REAL,
                    metrics_count INTEGER,
                    recommendations TEXT
                )
            """)
            
            # Session tracking
            conn.execute("""
                CREATE TABLE IF NOT EXISTS session_health (
                    id INTEGER PRIMARY KEY,
                    session_id TEXT,
                    start_time DATETIME,
                    end_time DATETIME,
                    total_commands INTEGER,
                    success_rate REAL,
                    average_response_time REAL,
                    health_incidents INTEGER
                )
            """)
    
    def start_monitoring(self, interval_seconds: int = 30):
        """Start continuous health monitoring"""
        if self.monitoring_active:
            self.logger.warning("Health monitoring already active")
            return
        
        self.monitoring_active = True
        self.monitoring_thread = threading.Thread(
            target=self._monitoring_loop,
            args=(interval_seconds,),
            daemon=True
        )
        self.monitoring_thread.start()
        self.logger.info(f"Health monitoring started with {interval_seconds}s interval")
    
    def stop_monitoring(self):
        """Stop continuous health monitoring"""
        if not self.monitoring_active:
            return
        
        self.monitoring_active = False
        if self.monitoring_thread:
            self.monitoring_thread.join(timeout=5)
        
        self.logger.info("Health monitoring stopped")
    
    def _monitoring_loop(self, interval_seconds: int):
        """Main monitoring loop"""
        while self.monitoring_active:
            try:
                health_assessment = self.assess_system_health()
                self._store_health_assessment(health_assessment)
                
                # Check for critical issues
                if health_assessment.overall_status == HealthStatus.CRITICAL:
                    self._handle_critical_health_issue(health_assessment)
                
                time.sleep(interval_seconds)
                
            except Exception as e:
                self.logger.error(f"Error in monitoring loop: {e}")
                time.sleep(interval_seconds)
    
    def assess_system_health(self) -> SystemHealth:
        """Comprehensive system health assessment for Claude Code operations"""
        metrics = []
        
        # Claude Code specific metrics
        metrics.extend(self._assess_task_tool_health())
        metrics.extend(self._assess_context_management_health())
        metrics.extend(self._assess_session_health())
        metrics.extend(self._assess_workflow_health())
        
        # System resource metrics
        metrics.extend(self._assess_system_resources())
        
        # Calculate overall health
        overall_status, health_score = self._calculate_overall_health(metrics)
        recommendations = self._generate_health_recommendations(metrics)
        
        return SystemHealth(
            overall_status=overall_status,
            health_score=health_score,
            metrics=metrics,
            recommendations=recommendations,
            last_updated=datetime.datetime.now()
        )
    
    def _assess_task_tool_health(self) -> List[HealthMetric]:
        """Assess Task tool performance and health"""
        metrics = []
        
        # Get recent Task tool performance data
        task_performance = self._get_recent_task_performance()
        
        # Task tool success rate
        success_rate = task_performance.get('success_rate', 0.9)
        metrics.append(HealthMetric(
            name='task_tool_success_rate',
            value=success_rate,
            status=self._get_status_from_value('task_tool_success_rate', success_rate, reverse=True),
            threshold_warning=self.thresholds['task_tool_success_rate']['warning'],
            threshold_critical=self.thresholds['task_tool_success_rate']['critical'],
            timestamp=datetime.datetime.now(),
            context={'measurement_period': 'last_hour', 'sample_size': task_performance.get('sample_size', 0)}
        ))
        
        # Parallel execution efficiency
        parallel_efficiency = task_performance.get('parallel_efficiency', 0.8)
        metrics.append(HealthMetric(
            name='parallel_execution_efficiency',
            value=parallel_efficiency,
            status=self._get_status_from_value('parallel_execution_efficiency', parallel_efficiency, reverse=True),
            threshold_warning=self.thresholds['parallel_execution_efficiency']['warning'],
            threshold_critical=self.thresholds['parallel_execution_efficiency']['critical'],
            timestamp=datetime.datetime.now(),
            context={'concurrent_tasks_avg': task_performance.get('concurrent_tasks_avg', 2)}
        ))
        
        return metrics
    
    def _assess_context_management_health(self) -> List[HealthMetric]:
        """Assess context loading and management performance"""
        metrics = []
        
        context_performance = self._get_recent_context_performance()
        
        # Context loading time
        loading_time = context_performance.get('average_loading_time', 2.0)
        metrics.append(HealthMetric(
            name='context_loading_time',
            value=loading_time,
            status=self._get_status_from_value('context_loading_time', loading_time),
            threshold_warning=self.thresholds['context_loading_time']['warning'],
            threshold_critical=self.thresholds['context_loading_time']['critical'],
            timestamp=datetime.datetime.now(),
            context={'context_size_avg': context_performance.get('average_context_size', 5000)}
        ))
        
        # Token economy efficiency
        token_efficiency = context_performance.get('token_efficiency', 0.85)
        metrics.append(HealthMetric(
            name='token_economy_efficiency',
            value=token_efficiency,
            status=self._get_status_from_value('token_economy_efficiency', token_efficiency, reverse=True),
            threshold_warning=self.thresholds['token_economy_efficiency']['warning'],
            threshold_critical=self.thresholds['token_economy_efficiency']['critical'],
            timestamp=datetime.datetime.now(),
            context={'token_waste_percentage': (1 - token_efficiency) * 100}
        ))
        
        return metrics
    
    def _assess_session_health(self) -> List[HealthMetric]:
        """Assess Claude Code session continuity and health"""
        metrics = []
        
        session_data = self._get_current_session_health()
        
        # Session continuity score
        continuity_score = session_data.get('continuity_score', 0.9)
        metrics.append(HealthMetric(
            name='session_continuity_score',
            value=continuity_score,
            status=self._get_status_from_value('session_continuity_score', continuity_score, reverse=True),
            threshold_warning=self.thresholds['session_continuity_score']['warning'],
            threshold_critical=self.thresholds['session_continuity_score']['critical'],
            timestamp=datetime.datetime.now(),
            context={'handoff_success_rate': session_data.get('handoff_success_rate', 0.95)}
        ))
        
        # Command response time
        response_time = session_data.get('average_response_time', 5.0)
        metrics.append(HealthMetric(
            name='command_response_time',
            value=response_time,
            status=self._get_status_from_value('command_response_time', response_time),
            threshold_warning=self.thresholds['command_response_time']['warning'],
            threshold_critical=self.thresholds['command_response_time']['critical'],
            timestamp=datetime.datetime.now(),
            context={'commands_processed': session_data.get('commands_processed', 0)}
        ))
        
        return metrics
    
    def _assess_workflow_health(self) -> List[HealthMetric]:
        """Assess workflow execution health"""
        metrics = []
        
        # This would assess workflow-specific health metrics
        # For now, return empty list as it requires workflow tracking integration
        return metrics
    
    def _assess_system_resources(self) -> List[HealthMetric]:
        """Assess system resource health"""
        metrics = []
        
        # Memory usage
        memory = psutil.virtual_memory()
        memory_mb = memory.used / (1024 * 1024)
        metrics.append(HealthMetric(
            name='memory_usage_mb',
            value=memory_mb,
            status=self._get_status_from_value('memory_usage_mb', memory_mb),
            threshold_warning=self.thresholds['memory_usage_mb']['warning'],
            threshold_critical=self.thresholds['memory_usage_mb']['critical'],
            timestamp=datetime.datetime.now(),
            context={'total_memory_mb': memory.total / (1024 * 1024), 'available_mb': memory.available / (1024 * 1024)}
        ))
        
        # CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)
        metrics.append(HealthMetric(
            name='cpu_usage_percent',
            value=cpu_percent,
            status=self._get_status_from_value('cpu_usage_percent', cpu_percent),
            threshold_warning=self.thresholds['cpu_usage_percent']['warning'],
            threshold_critical=self.thresholds['cpu_usage_percent']['critical'],
            timestamp=datetime.datetime.now(),
            context={'cpu_count': psutil.cpu_count()}
        ))
        
        # Disk usage
        disk = psutil.disk_usage(str(self.workspace))
        disk_percent = (disk.used / disk.total) * 100
        metrics.append(HealthMetric(
            name='disk_usage_percent',
            value=disk_percent,
            status=self._get_status_from_value('disk_usage_percent', disk_percent),
            threshold_warning=self.thresholds['disk_usage_percent']['warning'],
            threshold_critical=self.thresholds['disk_usage_percent']['critical'],
            timestamp=datetime.datetime.now(),
            context={'total_gb': disk.total / (1024**3), 'free_gb': disk.free / (1024**3)}
        ))
        
        return metrics
    
    def _get_status_from_value(self, metric_name: str, value: float, reverse: bool = False) -> HealthStatus:
        """Determine health status from metric value"""
        thresholds = self.thresholds.get(metric_name, {'warning': 0.8, 'critical': 0.6})
        
        if reverse:
            # For metrics where higher is better (e.g., success rate)
            if value < thresholds['critical']:
                return HealthStatus.CRITICAL
            elif value < thresholds['warning']:
                return HealthStatus.WARNING
            else:
                return HealthStatus.HEALTHY
        else:
            # For metrics where lower is better (e.g., response time)
            if value > thresholds['critical']:
                return HealthStatus.CRITICAL
            elif value > thresholds['warning']:
                return HealthStatus.WARNING
            else:
                return HealthStatus.HEALTHY
    
    def _calculate_overall_health(self, metrics: List[HealthMetric]) -> tuple[HealthStatus, float]:
        """Calculate overall system health status and score"""
        if not metrics:
            return HealthStatus.UNKNOWN, 0.0
        
        status_weights = {
            HealthStatus.HEALTHY: 1.0,
            HealthStatus.WARNING: 0.6,
            HealthStatus.CRITICAL: 0.2,
            HealthStatus.UNKNOWN: 0.0
        }
        
        # Calculate weighted score
        total_score = sum(status_weights[metric.status] for metric in metrics)
        health_score = total_score / len(metrics)
        
        # Determine overall status
        critical_count = sum(1 for m in metrics if m.status == HealthStatus.CRITICAL)
        warning_count = sum(1 for m in metrics if m.status == HealthStatus.WARNING)
        
        if critical_count > 0:
            overall_status = HealthStatus.CRITICAL
        elif warning_count > len(metrics) * 0.3:  # More than 30% warnings
            overall_status = HealthStatus.WARNING
        else:
            overall_status = HealthStatus.HEALTHY
        
        return overall_status, health_score
    
    def _generate_health_recommendations(self, metrics: List[HealthMetric]) -> List[str]:
        """Generate health improvement recommendations"""
        recommendations = []
        
        for metric in metrics:
            if metric.status == HealthStatus.CRITICAL:
                recommendations.extend(self._get_critical_recommendations(metric))
            elif metric.status == HealthStatus.WARNING:
                recommendations.extend(self._get_warning_recommendations(metric))
        
        # Remove duplicates
        return list(set(recommendations))
    
    def _get_critical_recommendations(self, metric: HealthMetric) -> List[str]:
        """Get recommendations for critical health issues"""
        recommendations = {
            'task_tool_success_rate': [
                "Review Task tool prompt patterns for optimization",
                "Check for system resource constraints affecting Task tools",
                "Analyze failed Task tool executions for common patterns"
            ],
            'context_loading_time': [
                "Implement context compaction strategies",
                "Review import statements for unnecessary context loading",
                "Consider progressive context loading for complex workflows"
            ],
            'parallel_execution_efficiency': [
                "Optimize parallel Task tool deployment strategies",
                "Review task dependencies for parallel execution barriers",
                "Increase concurrent task limits if system resources allow"
            ],
            'memory_usage_mb': [
                "Clear unnecessary context from memory",
                "Restart Claude Code session to free memory",
                "Review memory-intensive operations"
            ],
            'cpu_usage_percent': [
                "Reduce parallel task count temporarily",
                "Check for background processes consuming CPU",
                "Consider spreading workload across multiple sessions"
            ]
        }
        
        return recommendations.get(metric.name, [f"Critical issue detected with {metric.name}"])
    
    def _get_warning_recommendations(self, metric: HealthMetric) -> List[str]:
        """Get recommendations for warning-level health issues"""
        recommendations = {
            'task_tool_success_rate': [
                "Monitor Task tool performance trends",
                "Consider adjusting Task tool timeout settings"
            ],
            'context_loading_time': [
                "Review context loading patterns for optimization opportunities",
                "Consider implementing context caching"
            ],
            'token_economy_efficiency': [
                "Analyze token usage patterns for optimization",
                "Review context compaction effectiveness"
            ]
        }
        
        return recommendations.get(metric.name, [f"Monitor {metric.name} trend"])
    
    def _get_recent_task_performance(self) -> Dict[str, Any]:
        """Get recent Task tool performance data"""
        # This would integrate with the efficiency dashboard
        # For now, return mock data
        return {
            'success_rate': 0.92,
            'parallel_efficiency': 0.85,
            'sample_size': 50,
            'concurrent_tasks_avg': 3.2
        }
    
    def _get_recent_context_performance(self) -> Dict[str, Any]:
        """Get recent context management performance data"""
        # This would integrate with context management systems
        # For now, return mock data
        return {
            'average_loading_time': 1.8,
            'token_efficiency': 0.88,
            'average_context_size': 4500
        }
    
    def _get_current_session_health(self) -> Dict[str, Any]:
        """Get current session health data"""
        # This would integrate with session management
        # For now, return mock data
        return {
            'continuity_score': 0.93,
            'handoff_success_rate': 0.97,
            'average_response_time': 4.2,
            'commands_processed': 25
        }
    
    def _store_health_assessment(self, health: SystemHealth):
        """Store health assessment in database"""
        with sqlite3.connect(self.db_path) as conn:
            # Store individual metrics
            for metric in health.metrics:
                conn.execute("""
                    INSERT INTO health_metrics 
                    (session_id, timestamp, metric_name, metric_value, status, threshold_warning, threshold_critical, context)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    self.session_id,
                    metric.timestamp,
                    metric.name,
                    metric.value,
                    metric.status.value,
                    metric.threshold_warning,
                    metric.threshold_critical,
                    json.dumps(metric.context)
                ))
            
            # Store overall health snapshot
            conn.execute("""
                INSERT INTO system_health_snapshots
                (session_id, timestamp, overall_status, health_score, metrics_count, recommendations)  
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                self.session_id,
                health.last_updated,
                health.overall_status.value,
                health.health_score,
                len(health.metrics),
                json.dumps(health.recommendations)
            ))
    
    def _handle_critical_health_issue(self, health: SystemHealth):
        """Handle critical health issues"""
        self.logger.critical(f"Critical health issue detected. Score: {health.health_score}")
        
        critical_metrics = [m for m in health.metrics if m.status == HealthStatus.CRITICAL]
        for metric in critical_metrics:
            self.logger.critical(f"Critical metric: {metric.name} = {metric.value}")
        
        # Save critical health report
        report_path = self.workspace / "data" / f"critical-health-{int(time.time())}.json"
        with open(report_path, 'w') as f:
            json.dump(asdict(health), f, indent=2, default=str)
    
    def generate_health_report(self) -> Dict[str, Any]:
        """Generate comprehensive health report"""
        health = self.assess_system_health()
        
        report = {
            'timestamp': datetime.datetime.now().isoformat(),
            'session_id': self.session_id,
            'overall_health': {
                'status': health.overall_status.value,
                'score': health.health_score
            },
            'metrics': [asdict(metric) for metric in health.metrics],
            'recommendations': health.recommendations,
            'historical_trends': self._get_health_trends(),
            'claude_code_specifics': {
                'task_tool_health': self._summarize_task_tool_health(health.metrics),
                'context_management_health': self._summarize_context_health(health.metrics),
                'session_health': self._summarize_session_health(health.metrics)
            }
        }
        
        # Save report
        report_path = self.workspace / "data" / "claude-code-health-report.json"
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        return report
    
    def _get_health_trends(self) -> Dict[str, Any]:
        """Get health trends over time"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("""
                SELECT metric_name, AVG(metric_value), COUNT(*)
                FROM health_metrics 
                WHERE timestamp > datetime('now', '-24 hours')
                GROUP BY metric_name
            """)
            
            trends = {}
            for row in cursor.fetchall():
                metric_name, avg_value, count = row
                trends[metric_name] = {
                    'average_24h': avg_value,
                    'sample_count': count
                }
                
        return trends
    
    def _summarize_task_tool_health(self, metrics: List[HealthMetric]) -> Dict[str, Any]:
        """Summarize Task tool specific health"""
        task_metrics = [m for m in metrics if 'task_tool' in m.name or 'parallel' in m.name]
        
        if not task_metrics:
            return {'status': 'no_data'}
        
        healthy_count = sum(1 for m in task_metrics if m.status == HealthStatus.HEALTHY)
        
        return {
            'overall_status': 'healthy' if healthy_count == len(task_metrics) else 'needs_attention',
            'metrics_count': len(task_metrics),
            'healthy_count': healthy_count,
            'key_metrics': {m.name: m.value for m in task_metrics}
        }
    
    def _summarize_context_health(self, metrics: List[HealthMetric]) -> Dict[str, Any]:
        """Summarize context management health"""
        context_metrics = [m for m in metrics if 'context' in m.name or 'token' in m.name]
        
        if not context_metrics:
            return {'status': 'no_data'}
        
        healthy_count = sum(1 for m in context_metrics if m.status == HealthStatus.HEALTHY)
        
        return {
            'overall_status': 'healthy' if healthy_count == len(context_metrics) else 'needs_attention',
            'metrics_count': len(context_metrics),
            'healthy_count': healthy_count,
            'key_metrics': {m.name: m.value for m in context_metrics}
        }
    
    def _summarize_session_health(self, metrics: List[HealthMetric]) -> Dict[str, Any]:
        """Summarize session health"""
        session_metrics = [m for m in metrics if 'session' in m.name or 'command' in m.name]
        
        if not session_metrics:
            return {'status': 'no_data'}
        
        healthy_count = sum(1 for m in session_metrics if m.status == HealthStatus.HEALTHY)
        
        return {
            'overall_status': 'healthy' if healthy_count == len(session_metrics) else 'needs_attention',
            'metrics_count': len(session_metrics),
            'healthy_count': healthy_count,
            'key_metrics': {m.name: m.value for m in session_metrics}
        }

if __name__ == "__main__":
    # Initialize health monitor
    monitor = ClaudeCodeHealthMonitor()
    
    # Generate one-time health report
    print("Generating Claude Code health assessment...")
    report = monitor.generate_health_report()
    
    print(f"Health Status: {report['overall_health']['status']}")
    print(f"Health Score: {report['overall_health']['score']:.2f}")
    print(f"Report saved to: {monitor.workspace}/data/claude-code-health-report.json")
    
    # Optionally start continuous monitoring
    start_continuous = input("Start continuous monitoring? (y/n): ").lower().strip() == 'y'
    if start_continuous:
        monitor.start_monitoring(interval_seconds=60)
        print("Continuous monitoring started. Press Ctrl+C to stop.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            monitor.stop_monitoring()
            print("Monitoring stopped.")