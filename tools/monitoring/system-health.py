#!/usr/bin/env python3
"""
System Health Monitoring Suite
Comprehensive monitoring for system health and user voice preservation metrics
"""

import json
import time
import os
import logging
import statistics
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from collections import defaultdict, deque
import hashlib
import sqlite3

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class SystemHealthMetrics:
    """Core system health indicators"""
    timestamp: float
    cpu_usage: float
    memory_usage: float
    response_time: float
    success_rate: float
    error_count: int
    active_sessions: int
    availability_score: float
    
@dataclass
class UserVoiceMetrics:
    """User voice preservation tracking"""
    timestamp: float
    intent_preservation_score: float
    context_accuracy: float
    voice_authenticity: float
    decision_fidelity: float
    original_request_hash: str
    processed_output_quality: float
    
@dataclass
class CommandMetrics:
    """Command effectiveness tracking"""
    timestamp: float
    command_name: str
    execution_time: float
    success: bool
    error_type: Optional[str]
    resource_usage: Dict[str, float]
    user_satisfaction: Optional[float]
    output_quality: float

@dataclass
class IntegrationMetrics:
    """Cross-system integration quality"""
    timestamp: float
    component_a: str
    component_b: str
    interaction_latency: float
    data_integrity_score: float
    handoff_success: bool
    sync_accuracy: float

class HealthDatabase:
    """SQLite database for metrics storage"""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize database tables"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS system_health (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp REAL,
                    cpu_usage REAL,
                    memory_usage REAL,
                    response_time REAL,
                    success_rate REAL,
                    error_count INTEGER,
                    active_sessions INTEGER,
                    availability_score REAL
                )
            ''')
            
            conn.execute('''
                CREATE TABLE IF NOT EXISTS user_voice (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp REAL,
                    intent_preservation_score REAL,
                    context_accuracy REAL,
                    voice_authenticity REAL,
                    decision_fidelity REAL,
                    original_request_hash TEXT,
                    processed_output_quality REAL
                )
            ''')
            
            conn.execute('''
                CREATE TABLE IF NOT EXISTS command_metrics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp REAL,
                    command_name TEXT,
                    execution_time REAL,
                    success BOOLEAN,
                    error_type TEXT,
                    resource_usage TEXT,
                    user_satisfaction REAL,
                    output_quality REAL
                )
            ''')
            
            conn.execute('''
                CREATE TABLE IF NOT EXISTS integration_metrics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp REAL,
                    component_a TEXT,
                    component_b TEXT,
                    interaction_latency REAL,
                    data_integrity_score REAL,
                    handoff_success BOOLEAN,
                    sync_accuracy REAL
                )
            ''')
            
            conn.execute('''
                CREATE TABLE IF NOT EXISTS alerts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp REAL,
                    alert_type TEXT,
                    severity TEXT,
                    message TEXT,
                    resolved BOOLEAN DEFAULT FALSE,
                    resolution_time REAL
                )
            ''')

    def store_system_health(self, metrics: SystemHealthMetrics):
        """Store system health metrics"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                INSERT INTO system_health 
                (timestamp, cpu_usage, memory_usage, response_time, success_rate, 
                 error_count, active_sessions, availability_score)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                metrics.timestamp, metrics.cpu_usage, metrics.memory_usage,
                metrics.response_time, metrics.success_rate, metrics.error_count,
                metrics.active_sessions, metrics.availability_score
            ))

    def store_user_voice(self, metrics: UserVoiceMetrics):
        """Store user voice metrics"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                INSERT INTO user_voice 
                (timestamp, intent_preservation_score, context_accuracy, voice_authenticity,
                 decision_fidelity, original_request_hash, processed_output_quality)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                metrics.timestamp, metrics.intent_preservation_score, metrics.context_accuracy,
                metrics.voice_authenticity, metrics.decision_fidelity, 
                metrics.original_request_hash, metrics.processed_output_quality
            ))

    def store_command_metrics(self, metrics: CommandMetrics):
        """Store command metrics"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                INSERT INTO command_metrics 
                (timestamp, command_name, execution_time, success, error_type,
                 resource_usage, user_satisfaction, output_quality)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                metrics.timestamp, metrics.command_name, metrics.execution_time,
                metrics.success, metrics.error_type, json.dumps(metrics.resource_usage),
                metrics.user_satisfaction, metrics.output_quality
            ))

    def store_integration_metrics(self, metrics: IntegrationMetrics):
        """Store integration metrics"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                INSERT INTO integration_metrics 
                (timestamp, component_a, component_b, interaction_latency,
                 data_integrity_score, handoff_success, sync_accuracy)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                metrics.timestamp, metrics.component_a, metrics.component_b,
                metrics.interaction_latency, metrics.data_integrity_score,
                metrics.handoff_success, metrics.sync_accuracy
            ))

    def store_alert(self, alert_type: str, severity: str, message: str):
        """Store alert"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                INSERT INTO alerts (timestamp, alert_type, severity, message)
                VALUES (?, ?, ?, ?)
            ''', (time.time(), alert_type, severity, message))

class MetricsCollector:
    """Central metrics collection and analysis"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.db_path = self.base_path / "monitoring.db"
        self.db = HealthDatabase(str(self.db_path))
        
        # In-memory caches for real-time analysis
        self.recent_system_metrics = deque(maxlen=100)
        self.recent_voice_metrics = deque(maxlen=100)
        self.recent_command_metrics = deque(maxlen=200)
        self.recent_integration_metrics = deque(maxlen=50)
        
        # Alert thresholds
        self.alert_thresholds = {
            'cpu_usage': 80.0,
            'memory_usage': 85.0,
            'response_time': 5.0,
            'success_rate': 95.0,
            'availability_score': 98.0,
            'intent_preservation_score': 90.0,
            'voice_authenticity': 85.0,
            'context_accuracy': 92.0
        }
        
        # Performance tracking
        self.performance_windows = {
            '1h': deque(maxlen=60),    # 1 hour (1min intervals)
            '24h': deque(maxlen=288),  # 24 hours (5min intervals)
            '7d': deque(maxlen=168)    # 7 days (1hour intervals)
        }

    def collect_system_health(self) -> SystemHealthMetrics:
        """Collect current system health metrics"""
        try:
            # Simulate system metrics collection
            # In production, these would come from actual system monitoring
            
            # CPU and memory would come from psutil or system calls
            cpu_usage = self._get_cpu_usage()
            memory_usage = self._get_memory_usage()
            
            # Response time from recent command executions
            response_time = self._calculate_avg_response_time()
            
            # Success rate from recent operations
            success_rate = self._calculate_success_rate()
            
            # Error count from recent period
            error_count = self._count_recent_errors()
            
            # Active sessions from session tracking
            active_sessions = self._count_active_sessions()
            
            # Overall availability score
            availability_score = self._calculate_availability_score(
                cpu_usage, memory_usage, response_time, success_rate
            )
            
            metrics = SystemHealthMetrics(
                timestamp=time.time(),
                cpu_usage=cpu_usage,
                memory_usage=memory_usage,
                response_time=response_time,
                success_rate=success_rate,
                error_count=error_count,
                active_sessions=active_sessions,
                availability_score=availability_score
            )
            
            self.recent_system_metrics.append(metrics)
            self.db.store_system_health(metrics)
            
            # Check for alerts
            self._check_system_alerts(metrics)
            
            return metrics
            
        except Exception as e:
            logger.error(f"Error collecting system health metrics: {e}")
            raise

    def collect_user_voice_metrics(self, original_request: str, processed_output: str, 
                                 context_data: Dict[str, Any]) -> UserVoiceMetrics:
        """Collect user voice preservation metrics"""
        try:
            # Generate hash of original request for tracking
            request_hash = hashlib.sha256(original_request.encode()).hexdigest()[:16]
            
            # Analyze intent preservation
            intent_score = self._analyze_intent_preservation(original_request, processed_output)
            
            # Check context accuracy
            context_accuracy = self._analyze_context_accuracy(context_data, processed_output)
            
            # Measure voice authenticity
            voice_authenticity = self._analyze_voice_authenticity(original_request, processed_output)
            
            # Check decision fidelity
            decision_fidelity = self._analyze_decision_fidelity(original_request, processed_output)
            
            # Overall output quality
            output_quality = self._assess_output_quality(processed_output)
            
            metrics = UserVoiceMetrics(
                timestamp=time.time(),
                intent_preservation_score=intent_score,
                context_accuracy=context_accuracy,
                voice_authenticity=voice_authenticity,
                decision_fidelity=decision_fidelity,
                original_request_hash=request_hash,
                processed_output_quality=output_quality
            )
            
            self.recent_voice_metrics.append(metrics)
            self.db.store_user_voice(metrics)
            
            # Check for voice preservation alerts
            self._check_voice_alerts(metrics)
            
            return metrics
            
        except Exception as e:
            logger.error(f"Error collecting user voice metrics: {e}")
            raise

    def collect_command_metrics(self, command_name: str, execution_time: float,
                              success: bool, error_type: Optional[str] = None,
                              resource_usage: Optional[Dict[str, float]] = None,
                              user_satisfaction: Optional[float] = None) -> CommandMetrics:
        """Collect command execution metrics"""
        try:
            if resource_usage is None:
                resource_usage = {}
            
            # Assess output quality based on success and execution characteristics
            output_quality = self._assess_command_output_quality(
                success, execution_time, error_type
            )
            
            metrics = CommandMetrics(
                timestamp=time.time(),
                command_name=command_name,
                execution_time=execution_time,
                success=success,
                error_type=error_type,
                resource_usage=resource_usage,
                user_satisfaction=user_satisfaction,
                output_quality=output_quality
            )
            
            self.recent_command_metrics.append(metrics)
            self.db.store_command_metrics(metrics)
            
            # Check for command performance alerts
            self._check_command_alerts(metrics)
            
            return metrics
            
        except Exception as e:
            logger.error(f"Error collecting command metrics: {e}")
            raise

    def collect_integration_metrics(self, component_a: str, component_b: str,
                                  interaction_latency: float, data_integrity_score: float,
                                  handoff_success: bool, sync_accuracy: float) -> IntegrationMetrics:
        """Collect integration quality metrics"""
        try:
            metrics = IntegrationMetrics(
                timestamp=time.time(),
                component_a=component_a,
                component_b=component_b,
                interaction_latency=interaction_latency,
                data_integrity_score=data_integrity_score,
                handoff_success=handoff_success,
                sync_accuracy=sync_accuracy
            )
            
            self.recent_integration_metrics.append(metrics)
            self.db.store_integration_metrics(metrics)
            
            # Check for integration alerts
            self._check_integration_alerts(metrics)
            
            return metrics
            
        except Exception as e:
            logger.error(f"Error collecting integration metrics: {e}")
            raise

    def generate_health_report(self, period_hours: int = 24) -> Dict[str, Any]:
        """Generate comprehensive health report"""
        try:
            end_time = time.time()
            start_time = end_time - (period_hours * 3600)
            
            # Get recent metrics
            system_metrics = [m for m in self.recent_system_metrics if m.timestamp >= start_time]
            voice_metrics = [m for m in self.recent_voice_metrics if m.timestamp >= start_time]
            command_metrics = [m for m in self.recent_command_metrics if m.timestamp >= start_time]
            integration_metrics = [m for m in self.recent_integration_metrics if m.timestamp >= start_time]
            
            report = {
                'report_timestamp': datetime.now().isoformat(),
                'period_hours': period_hours,
                'system_health': self._analyze_system_health(system_metrics),
                'user_voice_preservation': self._analyze_voice_preservation(voice_metrics),
                'command_effectiveness': self._analyze_command_effectiveness(command_metrics),
                'integration_quality': self._analyze_integration_quality(integration_metrics),
                'trend_analysis': self._perform_trend_analysis(),
                'alerts_summary': self._get_alerts_summary(),
                'recommendations': self._generate_recommendations()
            }
            
            # Save report
            report_path = self.base_path / f"health_report_{int(end_time)}.json"
            with open(report_path, 'w') as f:
                json.dump(report, f, indent=2)
            
            return report
            
        except Exception as e:
            logger.error(f"Error generating health report: {e}")
            raise

    def get_real_time_status(self) -> Dict[str, Any]:
        """Get current real-time system status"""
        try:
            current_time = time.time()
            
            # Get most recent metrics
            latest_system = self.recent_system_metrics[-1] if self.recent_system_metrics else None
            latest_voice = self.recent_voice_metrics[-1] if self.recent_voice_metrics else None
            
            # Calculate current trends
            system_trend = self._calculate_system_trend()
            voice_trend = self._calculate_voice_trend()
            
            # Get active alerts
            active_alerts = self._get_active_alerts()
            
            status = {
                'timestamp': current_time,
                'status_time': datetime.now().isoformat(),
                'overall_health': self._calculate_overall_health(),
                'system_metrics': asdict(latest_system) if latest_system else None,
                'voice_metrics': asdict(latest_voice) if latest_voice else None,
                'trends': {
                    'system': system_trend,
                    'voice': voice_trend
                },
                'active_alerts': active_alerts,
                'performance_summary': self._get_performance_summary()
            }
            
            return status
            
        except Exception as e:
            logger.error(f"Error getting real-time status: {e}")
            raise

    # Private helper methods
    
    def _get_cpu_usage(self) -> float:
        """Get current CPU usage (simulated)"""
        # In production, use psutil.cpu_percent()
        import random
        return random.uniform(10, 70)
    
    def _get_memory_usage(self) -> float:
        """Get current memory usage (simulated)"""
        # In production, use psutil.virtual_memory().percent
        import random
        return random.uniform(20, 80)
    
    def _calculate_avg_response_time(self) -> float:
        """Calculate average response time from recent commands"""
        if not self.recent_command_metrics:
            return 0.0
        
        recent_times = [m.execution_time for m in list(self.recent_command_metrics)[-10:]]
        return statistics.mean(recent_times) if recent_times else 0.0
    
    def _calculate_success_rate(self) -> float:
        """Calculate success rate from recent operations"""
        if not self.recent_command_metrics:
            return 100.0
        
        recent_commands = list(self.recent_command_metrics)[-20:]
        successes = sum(1 for m in recent_commands if m.success)
        return (successes / len(recent_commands)) * 100 if recent_commands else 100.0
    
    def _count_recent_errors(self) -> int:
        """Count errors in recent period"""
        cutoff_time = time.time() - 3600  # Last hour
        return sum(1 for m in self.recent_command_metrics 
                  if m.timestamp >= cutoff_time and not m.success)
    
    def _count_active_sessions(self) -> int:
        """Count active sessions (simulated)"""
        # In production, this would track actual active sessions
        import random
        return random.randint(1, 5)
    
    def _calculate_availability_score(self, cpu: float, memory: float, 
                                    response_time: float, success_rate: float) -> float:
        """Calculate overall availability score"""
        # Weighted availability calculation
        cpu_score = max(0, 100 - cpu)
        memory_score = max(0, 100 - memory)
        response_score = max(0, 100 - (response_time * 10))
        
        # Weighted average
        availability = (cpu_score * 0.2 + memory_score * 0.2 + 
                       response_score * 0.3 + success_rate * 0.3)
        
        return min(100, max(0, availability))
    
    def _analyze_intent_preservation(self, original: str, processed: str) -> float:
        """Analyze how well original intent was preserved"""
        # Simplified intent analysis - in production, use NLP techniques
        original_words = set(original.lower().split())
        processed_words = set(processed.lower().split())
        
        if not original_words:
            return 100.0
        
        overlap = len(original_words.intersection(processed_words))
        preservation_score = (overlap / len(original_words)) * 100
        
        # Bonus for maintaining key concepts
        key_indicators = ['create', 'implement', 'analyze', 'monitor', 'track']
        key_preserved = sum(1 for word in key_indicators 
                           if word in original.lower() and word in processed.lower())
        
        if key_preserved > 0:
            preservation_score += key_preserved * 5
        
        return min(100, preservation_score)
    
    def _analyze_context_accuracy(self, context_data: Dict, processed: str) -> float:
        """Analyze context accuracy in processing"""
        # Simplified context analysis
        if not context_data:
            return 90.0  # Default if no context provided
        
        # Check if key context elements are reflected in output
        context_score = 85.0  # Base score
        
        # Look for context preservation indicators
        if 'user_preferences' in context_data:
            context_score += 5
        
        if 'system_state' in context_data:
            context_score += 5
        
        if len(processed) > 100:  # Substantial response suggests context usage
            context_score += 5
        
        return min(100, context_score)
    
    def _analyze_voice_authenticity(self, original: str, processed: str) -> float:
        """Analyze authenticity of user voice preservation"""
        # Simplified authenticity analysis
        authenticity_score = 80.0  # Base score
        
        # Check for direct user quote preservation
        if '"' in original and '"' in processed:
            authenticity_score += 10
        
        # Check for instruction following vs modification
        if 'exactly' in original.lower() or 'precisely' in original.lower():
            authenticity_score += 10
        
        return min(100, authenticity_score)
    
    def _analyze_decision_fidelity(self, original: str, processed: str) -> float:
        """Analyze fidelity to user decisions"""
        # Simplified decision fidelity analysis
        fidelity_score = 85.0  # Base score
        
        # Look for decision-making language
        decision_words = ['choose', 'decide', 'select', 'prefer', 'want', 'need']
        decisions_preserved = sum(1 for word in decision_words 
                                if word in original.lower())
        
        fidelity_score += decisions_preserved * 3
        
        return min(100, fidelity_score)
    
    def _assess_output_quality(self, output: str) -> float:
        """Assess overall output quality"""
        quality_score = 70.0  # Base score
        
        # Length appropriateness
        if 50 <= len(output) <= 2000:
            quality_score += 10
        
        # Structure indicators
        if '\n' in output:  # Has structure
            quality_score += 5
        
        if any(marker in output for marker in ['1.', '2.', '-', '*']):  # Has lists
            quality_score += 5
        
        # Completeness indicators
        if len(output) > 200:  # Substantial response
            quality_score += 10
        
        return min(100, quality_score)
    
    def _assess_command_output_quality(self, success: bool, execution_time: float, 
                                     error_type: Optional[str]) -> float:
        """Assess command output quality"""
        if not success:
            return 30.0 if error_type else 20.0
        
        quality_score = 90.0  # Base for successful commands
        
        # Performance bonus/penalty
        if execution_time < 1.0:
            quality_score += 10
        elif execution_time > 5.0:
            quality_score -= 15
        
        return min(100, max(0, quality_score))
    
    def _check_system_alerts(self, metrics: SystemHealthMetrics):
        """Check system metrics against alert thresholds"""
        alerts = []
        
        if metrics.cpu_usage > self.alert_thresholds['cpu_usage']:
            alerts.append(('cpu_high', 'warning', f'CPU usage: {metrics.cpu_usage:.1f}%'))
        
        if metrics.memory_usage > self.alert_thresholds['memory_usage']:
            alerts.append(('memory_high', 'warning', f'Memory usage: {metrics.memory_usage:.1f}%'))
        
        if metrics.response_time > self.alert_thresholds['response_time']:
            alerts.append(('response_slow', 'warning', f'Response time: {metrics.response_time:.2f}s'))
        
        if metrics.success_rate < self.alert_thresholds['success_rate']:
            alerts.append(('success_low', 'critical', f'Success rate: {metrics.success_rate:.1f}%'))
        
        if metrics.availability_score < self.alert_thresholds['availability_score']:
            alerts.append(('availability_low', 'critical', f'Availability: {metrics.availability_score:.1f}%'))
        
        for alert_type, severity, message in alerts:
            self.db.store_alert(alert_type, severity, message)
    
    def _check_voice_alerts(self, metrics: UserVoiceMetrics):
        """Check voice preservation metrics against thresholds"""
        alerts = []
        
        if metrics.intent_preservation_score < self.alert_thresholds['intent_preservation_score']:
            alerts.append(('intent_preservation_low', 'critical', 
                          f'Intent preservation: {metrics.intent_preservation_score:.1f}%'))
        
        if metrics.voice_authenticity < self.alert_thresholds['voice_authenticity']:
            alerts.append(('voice_authenticity_low', 'warning',
                          f'Voice authenticity: {metrics.voice_authenticity:.1f}%'))
        
        if metrics.context_accuracy < self.alert_thresholds['context_accuracy']:
            alerts.append(('context_accuracy_low', 'warning',
                          f'Context accuracy: {metrics.context_accuracy:.1f}%'))
        
        for alert_type, severity, message in alerts:
            self.db.store_alert(alert_type, severity, message)
    
    def _check_command_alerts(self, metrics: CommandMetrics):
        """Check command metrics for alerts"""
        if not metrics.success:
            self.db.store_alert('command_failure', 'warning', 
                              f'Command {metrics.command_name} failed: {metrics.error_type}')
        
        if metrics.execution_time > 10.0:
            self.db.store_alert('command_slow', 'warning',
                              f'Command {metrics.command_name} took {metrics.execution_time:.2f}s')
    
    def _check_integration_alerts(self, metrics: IntegrationMetrics):
        """Check integration metrics for alerts"""
        if not metrics.handoff_success:
            self.db.store_alert('integration_failure', 'critical',
                              f'Integration failure: {metrics.component_a} -> {metrics.component_b}')
        
        if metrics.interaction_latency > 2.0:
            self.db.store_alert('integration_slow', 'warning',
                              f'Slow integration: {metrics.component_a} -> {metrics.component_b}')
    
    def _analyze_system_health(self, metrics: List[SystemHealthMetrics]) -> Dict[str, Any]:
        """Analyze system health metrics"""
        if not metrics:
            return {'status': 'no_data'}
        
        cpu_values = [m.cpu_usage for m in metrics]
        memory_values = [m.memory_usage for m in metrics]
        response_times = [m.response_time for m in metrics]
        success_rates = [m.success_rate for m in metrics]
        
        return {
            'avg_cpu_usage': statistics.mean(cpu_values),
            'max_cpu_usage': max(cpu_values),
            'avg_memory_usage': statistics.mean(memory_values),
            'max_memory_usage': max(memory_values),
            'avg_response_time': statistics.mean(response_times),
            'max_response_time': max(response_times),
            'avg_success_rate': statistics.mean(success_rates),
            'min_success_rate': min(success_rates),
            'total_errors': sum(m.error_count for m in metrics),
            'availability_trend': self._calculate_trend([m.availability_score for m in metrics])
        }
    
    def _analyze_voice_preservation(self, metrics: List[UserVoiceMetrics]) -> Dict[str, Any]:
        """Analyze voice preservation metrics"""
        if not metrics:
            return {'status': 'no_data'}
        
        intent_scores = [m.intent_preservation_score for m in metrics]
        context_scores = [m.context_accuracy for m in metrics]
        authenticity_scores = [m.voice_authenticity for m in metrics]
        fidelity_scores = [m.decision_fidelity for m in metrics]
        
        return {
            'avg_intent_preservation': statistics.mean(intent_scores),
            'min_intent_preservation': min(intent_scores),
            'avg_context_accuracy': statistics.mean(context_scores),
            'min_context_accuracy': min(context_scores),
            'avg_voice_authenticity': statistics.mean(authenticity_scores),
            'min_voice_authenticity': min(authenticity_scores),
            'avg_decision_fidelity': statistics.mean(fidelity_scores),
            'min_decision_fidelity': min(fidelity_scores),
            'voice_preservation_trend': self._calculate_trend(intent_scores)
        }
    
    def _analyze_command_effectiveness(self, metrics: List[CommandMetrics]) -> Dict[str, Any]:
        """Analyze command effectiveness"""
        if not metrics:
            return {'status': 'no_data'}
        
        execution_times = [m.execution_time for m in metrics]
        success_count = sum(1 for m in metrics if m.success)
        
        # Command-specific analysis
        command_stats = defaultdict(list)
        for m in metrics:
            command_stats[m.command_name].append(m)
        
        command_analysis = {}
        for cmd, cmd_metrics in command_stats.items():
            cmd_success_rate = sum(1 for m in cmd_metrics if m.success) / len(cmd_metrics) * 100
            cmd_avg_time = statistics.mean([m.execution_time for m in cmd_metrics])
            command_analysis[cmd] = {
                'success_rate': cmd_success_rate,
                'avg_execution_time': cmd_avg_time,
                'execution_count': len(cmd_metrics)
            }
        
        return {
            'overall_success_rate': (success_count / len(metrics)) * 100,
            'avg_execution_time': statistics.mean(execution_times),
            'max_execution_time': max(execution_times),
            'total_commands': len(metrics),
            'command_breakdown': command_analysis,
            'performance_trend': self._calculate_trend(execution_times)
        }
    
    def _analyze_integration_quality(self, metrics: List[IntegrationMetrics]) -> Dict[str, Any]:
        """Analyze integration quality"""
        if not metrics:
            return {'status': 'no_data'}
        
        latencies = [m.interaction_latency for m in metrics]
        integrity_scores = [m.data_integrity_score for m in metrics]
        handoff_success_count = sum(1 for m in metrics if m.handoff_success)
        
        return {
            'avg_interaction_latency': statistics.mean(latencies),
            'max_interaction_latency': max(latencies),
            'avg_data_integrity': statistics.mean(integrity_scores),
            'min_data_integrity': min(integrity_scores),
            'handoff_success_rate': (handoff_success_count / len(metrics)) * 100,
            'total_integrations': len(metrics),
            'integration_trend': self._calculate_trend(integrity_scores)
        }
    
    def _perform_trend_analysis(self) -> Dict[str, Any]:
        """Perform trend analysis across all metrics"""
        trends = {}
        
        # System health trends
        if len(self.recent_system_metrics) >= 5:
            recent_availability = [m.availability_score for m in list(self.recent_system_metrics)[-10:]]
            trends['system_health'] = self._calculate_trend(recent_availability)
        
        # Voice preservation trends
        if len(self.recent_voice_metrics) >= 5:
            recent_intent = [m.intent_preservation_score for m in list(self.recent_voice_metrics)[-10:]]
            trends['voice_preservation'] = self._calculate_trend(recent_intent)
        
        # Command performance trends
        if len(self.recent_command_metrics) >= 5:
            recent_times = [m.execution_time for m in list(self.recent_command_metrics)[-20:]]
            trends['command_performance'] = self._calculate_trend(recent_times, reverse=True)
        
        return trends
    
    def _calculate_trend(self, values: List[float], reverse: bool = False) -> str:
        """Calculate trend direction from values"""
        if len(values) < 3:
            return 'insufficient_data'
        
        # Simple trend calculation
        first_half = statistics.mean(values[:len(values)//2])
        second_half = statistics.mean(values[len(values)//2:])
        
        diff = second_half - first_half
        threshold = statistics.stdev(values) * 0.5 if len(values) > 1 else 0.1
        
        if reverse:
            diff = -diff
        
        if diff > threshold:
            return 'improving'
        elif diff < -threshold:
            return 'declining'
        else:
            return 'stable'
    
    def _get_alerts_summary(self) -> Dict[str, Any]:
        """Get summary of recent alerts"""
        # This would query the alerts table
        return {
            'active_alerts': 0,
            'resolved_today': 0,
            'critical_count': 0,
            'warning_count': 0
        }
    
    def _generate_recommendations(self) -> List[str]:
        """Generate optimization recommendations"""
        recommendations = []
        
        # Analyze recent metrics for recommendations
        if self.recent_system_metrics:
            latest_system = self.recent_system_metrics[-1]
            
            if latest_system.cpu_usage > 70:
                recommendations.append("Consider optimizing CPU-intensive operations")
            
            if latest_system.memory_usage > 75:
                recommendations.append("Monitor memory usage and implement cleanup routines")
            
            if latest_system.response_time > 3.0:
                recommendations.append("Investigate performance bottlenecks in command execution")
        
        if self.recent_voice_metrics:
            latest_voice = self.recent_voice_metrics[-1]
            
            if latest_voice.intent_preservation_score < 85:
                recommendations.append("Review user intent preservation algorithms")
            
            if latest_voice.context_accuracy < 90:
                recommendations.append("Enhance context awareness in processing")
        
        if not recommendations:
            recommendations.append("System performing within normal parameters")
        
        return recommendations
    
    def _calculate_system_trend(self) -> str:
        """Calculate current system trend"""
        if len(self.recent_system_metrics) < 5:
            return 'insufficient_data'
        
        recent_scores = [m.availability_score for m in list(self.recent_system_metrics)[-5:]]
        return self._calculate_trend(recent_scores)
    
    def _calculate_voice_trend(self) -> str:
        """Calculate current voice preservation trend"""
        if len(self.recent_voice_metrics) < 5:
            return 'insufficient_data'
        
        recent_scores = [m.intent_preservation_score for m in list(self.recent_voice_metrics)[-5:]]
        return self._calculate_trend(recent_scores)
    
    def _get_active_alerts(self) -> List[Dict[str, Any]]:
        """Get currently active alerts"""
        # This would query the database for unresolved alerts
        return []
    
    def _calculate_overall_health(self) -> float:
        """Calculate overall system health score"""
        if not self.recent_system_metrics or not self.recent_voice_metrics:
            return 0.0
        
        latest_system = self.recent_system_metrics[-1]
        latest_voice = self.recent_voice_metrics[-1]
        
        # Weighted health calculation
        system_weight = 0.4
        voice_weight = 0.6  # User voice preservation is higher priority
        
        system_health = latest_system.availability_score
        voice_health = (latest_voice.intent_preservation_score + 
                       latest_voice.voice_authenticity + 
                       latest_voice.context_accuracy) / 3
        
        overall_health = (system_health * system_weight + voice_health * voice_weight)
        return min(100, max(0, overall_health))
    
    def _get_performance_summary(self) -> Dict[str, Any]:
        """Get performance summary"""
        return {
            'recent_commands': len(self.recent_command_metrics),
            'recent_integrations': len(self.recent_integration_metrics),
            'avg_response_time': self._calculate_avg_response_time(),
            'success_rate': self._calculate_success_rate()
        }

# Main execution and CLI interface
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='System Health Monitoring Suite')
    parser.add_argument('--base-path', default='/Users/nalve/ce-simple/tools/monitoring',
                       help='Base path for monitoring data')
    parser.add_argument('--collect', action='store_true', help='Collect current metrics')
    parser.add_argument('--report', type=int, default=24, help='Generate report for N hours')
    parser.add_argument('--status', action='store_true', help='Show real-time status')
    parser.add_argument('--daemon', action='store_true', help='Run as daemon')
    
    args = parser.parse_args()
    
    # Initialize collector
    collector = MetricsCollector(args.base_path)
    
    if args.collect:
        # Collect current metrics
        system_metrics = collector.collect_system_health()
        print(f"System health collected: {system_metrics.availability_score:.1f}% availability")
        
    elif args.status:
        # Show real-time status
        status = collector.get_real_time_status()
        print(json.dumps(status, indent=2))
        
    elif args.daemon:
        # Run as daemon (simplified)
        print("Starting monitoring daemon...")
        while True:
            try:
                collector.collect_system_health()
                time.sleep(60)  # Collect every minute
            except KeyboardInterrupt:
                print("Monitoring daemon stopped")
                break
                
    else:
        # Generate report
        report = collector.generate_health_report(args.report)
        print(json.dumps(report, indent=2))