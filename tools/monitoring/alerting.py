#!/usr/bin/env python3
"""
Advanced Alerting System
Intelligent alerting with anomaly detection, threshold monitoring, and notification management
"""

import json
import time
import logging
import smtplib
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass, asdict
from email.mime.text import MimeText
from email.mime.multipart import MimeMultipart
import statistics
from collections import defaultdict, deque

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class AlertRule:
    """Alert rule configuration"""
    rule_id: str
    name: str
    metric_type: str  # 'system', 'voice', 'command', 'integration'
    metric_field: str
    condition: str  # 'above', 'below', 'equals', 'anomaly'
    threshold: float
    severity: str  # 'critical', 'warning', 'info'
    cooldown_minutes: int
    enabled: bool
    notification_channels: List[str]
    description: str

@dataclass
class Alert:
    """Alert instance"""
    alert_id: str
    rule_id: str
    timestamp: float
    severity: str
    title: str
    message: str
    metric_value: float
    threshold: float
    resolved: bool
    resolution_timestamp: Optional[float]
    notification_sent: bool

@dataclass
class AnomalyDetectionConfig:
    """Configuration for anomaly detection"""
    window_size: int  # Number of data points for analysis
    sensitivity: float  # Multiplier for standard deviation threshold
    min_data_points: int  # Minimum points needed for detection
    trend_threshold: float  # Threshold for trend-based anomalies

class AnomalyDetector:
    """Statistical anomaly detection for metrics"""
    
    def __init__(self, config: AnomalyDetectionConfig):
        self.config = config
        self.metric_windows = defaultdict(lambda: deque(maxlen=config.window_size))
        self.baseline_stats = defaultdict(dict)
    
    def add_data_point(self, metric_key: str, value: float, timestamp: float):
        """Add a data point for anomaly analysis"""
        self.metric_windows[metric_key].append((timestamp, value))
        self._update_baseline_stats(metric_key)
    
    def detect_anomaly(self, metric_key: str, current_value: float) -> Optional[Dict[str, Any]]:
        """Detect if current value is anomalous"""
        window = self.metric_windows[metric_key]
        
        if len(window) < self.config.min_data_points:
            return None
        
        stats = self.baseline_stats[metric_key]
        if not stats:
            return None
        
        mean = stats['mean']
        std_dev = stats['std_dev']
        
        # Z-score based anomaly detection
        if std_dev > 0:
            z_score = abs(current_value - mean) / std_dev
            threshold = self.config.sensitivity
            
            if z_score > threshold:
                return {
                    'type': 'statistical',
                    'z_score': z_score,
                    'threshold': threshold,
                    'baseline_mean': mean,
                    'baseline_std': std_dev,
                    'deviation': current_value - mean
                }
        
        # Trend-based anomaly detection
        if len(window) >= 5:
            recent_values = [v[1] for v in list(window)[-5:]]
            trend = self._calculate_trend(recent_values)
            
            if abs(trend) > self.config.trend_threshold:
                return {
                    'type': 'trend',
                    'trend_slope': trend,
                    'threshold': self.config.trend_threshold,
                    'recent_values': recent_values
                }
        
        return None
    
    def _update_baseline_stats(self, metric_key: str):
        """Update baseline statistics for a metric"""
        window = self.metric_windows[metric_key]
        values = [v[1] for v in window]
        
        if len(values) >= self.config.min_data_points:
            self.baseline_stats[metric_key] = {
                'mean': statistics.mean(values),
                'std_dev': statistics.stdev(values) if len(values) > 1 else 0,
                'median': statistics.median(values),
                'min': min(values),
                'max': max(values)
            }
    
    def _calculate_trend(self, values: List[float]) -> float:
        """Calculate trend slope from values"""
        if len(values) < 2:
            return 0
        
        # Simple linear regression slope
        n = len(values)
        x_sum = sum(range(n))
        y_sum = sum(values)
        xy_sum = sum(i * values[i] for i in range(n))
        x2_sum = sum(i * i for i in range(n))
        
        if n * x2_sum - x_sum * x_sum == 0:
            return 0
        
        slope = (n * xy_sum - x_sum * y_sum) / (n * x2_sum - x_sum * x_sum)
        return slope

class NotificationManager:
    """Manage alert notifications across multiple channels"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.notification_history = deque(maxlen=1000)
        self.rate_limits = defaultdict(list)
    
    def send_notification(self, alert: Alert, channels: List[str]) -> bool:
        """Send notification through specified channels"""
        success = True
        
        for channel in channels:
            try:
                if self._check_rate_limit(channel, alert.severity):
                    channel_success = self._send_to_channel(channel, alert)
                    success = success and channel_success
                else:
                    logger.warning(f"Rate limit exceeded for channel {channel}")
                    success = False
            except Exception as e:
                logger.error(f"Failed to send notification to {channel}: {e}")
                success = False
        
        self.notification_history.append({
            'timestamp': time.time(),
            'alert_id': alert.alert_id,
            'channels': channels,
            'success': success
        })
        
        return success
    
    def _check_rate_limit(self, channel: str, severity: str) -> bool:
        """Check if notification is within rate limits"""
        now = time.time()
        channel_history = self.rate_limits[channel]
        
        # Clean old entries
        self.rate_limits[channel] = [t for t in channel_history 
                                   if now - t < 3600]  # 1 hour window
        
        # Rate limits by severity
        limits = {
            'critical': 10,  # 10 per hour
            'warning': 5,    # 5 per hour
            'info': 2        # 2 per hour
        }
        
        current_count = len(self.rate_limits[channel])
        limit = limits.get(severity, 1)
        
        if current_count < limit:
            self.rate_limits[channel].append(now)
            return True
        
        return False
    
    def _send_to_channel(self, channel: str, alert: Alert) -> bool:
        """Send alert to specific notification channel"""
        if channel == 'email':
            return self._send_email(alert)
        elif channel == 'webhook':
            return self._send_webhook(alert)
        elif channel == 'log':
            return self._send_log(alert)
        elif channel == 'file':
            return self._send_file(alert)
        else:
            logger.warning(f"Unknown notification channel: {channel}")
            return False
    
    def _send_email(self, alert: Alert) -> bool:
        """Send email notification"""
        try:
            email_config = self.config.get('email', {})
            if not email_config:
                logger.warning("Email configuration not found")
                return False
            
            msg = MimeMultipart()
            msg['From'] = email_config['from']
            msg['To'] = email_config['to']
            msg['Subject'] = f"[{alert.severity.upper()}] {alert.title}"
            
            body = f"""
Alert Details:
- Alert ID: {alert.alert_id}
- Severity: {alert.severity}
- Timestamp: {datetime.fromtimestamp(alert.timestamp)}
- Message: {alert.message}
- Metric Value: {alert.metric_value}
- Threshold: {alert.threshold}

This is an automated alert from the System Health Monitoring Suite.
            """
            
            msg.attach(MimeText(body, 'plain'))
            
            with smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port']) as server:
                if email_config.get('use_tls'):
                    server.starttls()
                if email_config.get('username'):
                    server.login(email_config['username'], email_config['password'])
                server.send_message(msg)
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to send email: {e}")
            return False
    
    def _send_webhook(self, alert: Alert) -> bool:
        """Send webhook notification"""
        try:
            import requests
            
            webhook_config = self.config.get('webhook', {})
            if not webhook_config:
                return False
            
            payload = {
                'alert_id': alert.alert_id,
                'severity': alert.severity,
                'title': alert.title,
                'message': alert.message,
                'metric_value': alert.metric_value,
                'threshold': alert.threshold,
                'timestamp': alert.timestamp
            }
            
            response = requests.post(
                webhook_config['url'],
                json=payload,
                headers=webhook_config.get('headers', {}),
                timeout=10
            )
            
            return response.status_code == 200
            
        except Exception as e:
            logger.error(f"Failed to send webhook: {e}")
            return False
    
    def _send_log(self, alert: Alert) -> bool:
        """Send log notification"""
        try:
            log_level = getattr(logging, alert.severity.upper(), logging.INFO)
            logger.log(log_level, f"ALERT: {alert.title} - {alert.message}")
            return True
        except Exception as e:
            logger.error(f"Failed to send log notification: {e}")
            return False
    
    def _send_file(self, alert: Alert) -> bool:
        """Send file notification"""
        try:
            file_config = self.config.get('file', {})
            file_path = file_config.get('path', '/tmp/alerts.json')
            
            alert_data = {
                'timestamp': datetime.fromtimestamp(alert.timestamp).isoformat(),
                'alert_id': alert.alert_id,
                'severity': alert.severity,
                'title': alert.title,
                'message': alert.message,
                'metric_value': alert.metric_value,
                'threshold': alert.threshold
            }
            
            # Append to alerts file
            with open(file_path, 'a') as f:
                f.write(json.dumps(alert_data) + '\n')
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to send file notification: {e}")
            return False

class AlertingEngine:
    """Main alerting engine with rule management and alert processing"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.db_path = self.base_path / "monitoring.db"
        self.config_path = self.base_path / "alerting_config.json"
        
        # Initialize components
        self.anomaly_detector = AnomalyDetector(AnomalyDetectionConfig(
            window_size=50,
            sensitivity=2.5,
            min_data_points=10,
            trend_threshold=0.1
        ))
        
        self.notification_manager = NotificationManager(self._load_notification_config())
        
        # Alert rules and state
        self.alert_rules = {}
        self.active_alerts = {}
        self.alert_cooldowns = defaultdict(float)
        
        # Load configuration
        self._load_alert_rules()
        self._init_database()
    
    def _load_notification_config(self) -> Dict[str, Any]:
        """Load notification configuration"""
        default_config = {
            'email': {
                'enabled': False,
                'smtp_server': 'localhost',
                'smtp_port': 587,
                'use_tls': True,
                'from': 'alerts@system.local',
                'to': 'admin@system.local'
            },
            'webhook': {
                'enabled': False,
                'url': 'http://localhost:8080/alerts'
            },
            'log': {
                'enabled': True
            },
            'file': {
                'enabled': True,
                'path': str(self.base_path / 'alerts.jsonl')
            }
        }
        
        try:
            config_file = self.base_path / 'notification_config.json'
            if config_file.exists():
                with open(config_file) as f:
                    loaded_config = json.load(f)
                    default_config.update(loaded_config)
        except Exception as e:
            logger.warning(f"Failed to load notification config: {e}")
        
        return default_config
    
    def _load_alert_rules(self):
        """Load alert rules from configuration"""
        default_rules = [
            AlertRule(
                rule_id='system_cpu_high',
                name='High CPU Usage',
                metric_type='system',
                metric_field='cpu_usage',
                condition='above',
                threshold=80.0,
                severity='warning',
                cooldown_minutes=15,
                enabled=True,
                notification_channels=['log', 'file'],
                description='CPU usage exceeds 80%'
            ),
            AlertRule(
                rule_id='system_memory_high',
                name='High Memory Usage',
                metric_type='system',
                metric_field='memory_usage',
                condition='above',
                threshold=85.0,
                severity='warning',
                cooldown_minutes=15,
                enabled=True,
                notification_channels=['log', 'file'],
                description='Memory usage exceeds 85%'
            ),
            AlertRule(
                rule_id='system_availability_low',
                name='Low System Availability',
                metric_type='system',
                metric_field='availability_score',
                condition='below',
                threshold=95.0,
                severity='critical',
                cooldown_minutes=5,
                enabled=True,
                notification_channels=['log', 'file', 'email'],
                description='System availability below 95%'
            ),
            AlertRule(
                rule_id='voice_intent_low',
                name='Low Intent Preservation',
                metric_type='voice',
                metric_field='intent_preservation_score',
                condition='below',
                threshold=85.0,
                severity='critical',
                cooldown_minutes=10,
                enabled=True,
                notification_channels=['log', 'file', 'email'],
                description='Intent preservation score below 85%'
            ),
            AlertRule(
                rule_id='voice_authenticity_low',
                name='Low Voice Authenticity',
                metric_type='voice',
                metric_field='voice_authenticity',
                condition='below',
                threshold=80.0,
                severity='warning',
                cooldown_minutes=20,
                enabled=True,
                notification_channels=['log', 'file'],
                description='Voice authenticity score below 80%'
            ),
            AlertRule(
                rule_id='command_response_slow',
                name='Slow Command Response',
                metric_type='system',
                metric_field='response_time',
                condition='above',
                threshold=5.0,
                severity='warning',
                cooldown_minutes=10,
                enabled=True,
                notification_channels=['log', 'file'],
                description='Average response time exceeds 5 seconds'
            ),
            AlertRule(
                rule_id='integration_failure',
                name='Integration Failure',
                metric_type='integration',
                metric_field='handoff_success',
                condition='equals',
                threshold=0.0,  # False
                severity='critical',
                cooldown_minutes=5,
                enabled=True,
                notification_channels=['log', 'file', 'email'],
                description='Integration handoff failure detected'
            )
        ]
        
        # Load from file if exists, otherwise use defaults
        try:
            if self.config_path.exists():
                with open(self.config_path) as f:
                    config_data = json.load(f)
                    for rule_data in config_data.get('rules', []):
                        rule = AlertRule(**rule_data)
                        self.alert_rules[rule.rule_id] = rule
            else:
                # Save default rules
                for rule in default_rules:
                    self.alert_rules[rule.rule_id] = rule
                self._save_alert_rules()
        except Exception as e:
            logger.error(f"Failed to load alert rules: {e}")
            # Use defaults on error
            for rule in default_rules:
                self.alert_rules[rule.rule_id] = rule
    
    def _save_alert_rules(self):
        """Save alert rules to configuration file"""
        try:
            config_data = {
                'rules': [asdict(rule) for rule in self.alert_rules.values()]
            }
            with open(self.config_path, 'w') as f:
                json.dump(config_data, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save alert rules: {e}")
    
    def _init_database(self):
        """Initialize database tables for alerts"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS alert_instances (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        alert_id TEXT,
                        rule_id TEXT,
                        timestamp REAL,
                        severity TEXT,
                        title TEXT,
                        message TEXT,
                        metric_value REAL,
                        threshold REAL,
                        resolved BOOLEAN DEFAULT FALSE,
                        resolution_timestamp REAL,
                        notification_sent BOOLEAN DEFAULT FALSE
                    )
                ''')
                
                conn.execute('''
                    CREATE INDEX IF NOT EXISTS idx_alert_timestamp 
                    ON alert_instances(timestamp)
                ''')
                
                conn.execute('''
                    CREATE INDEX IF NOT EXISTS idx_alert_resolved 
                    ON alert_instances(resolved)
                ''')
        except Exception as e:
            logger.error(f"Failed to initialize alert database: {e}")
    
    def evaluate_metrics(self, metric_type: str, metrics: Dict[str, Any]):
        """Evaluate metrics against alert rules"""
        current_time = time.time()
        
        for rule in self.alert_rules.values():
            if not rule.enabled or rule.metric_type != metric_type:
                continue
            
            if rule.metric_field not in metrics:
                continue
            
            # Check cooldown
            cooldown_key = f"{rule.rule_id}_{metric_type}"
            if current_time < self.alert_cooldowns[cooldown_key]:
                continue
            
            metric_value = metrics[rule.metric_field]
            
            # Evaluate condition
            alert_triggered = self._evaluate_condition(
                rule.condition, metric_value, rule.threshold
            )
            
            # Check for anomalies if condition is 'anomaly'
            if rule.condition == 'anomaly':
                metric_key = f"{metric_type}_{rule.metric_field}"
                self.anomaly_detector.add_data_point(metric_key, metric_value, current_time)
                anomaly = self.anomaly_detector.detect_anomaly(metric_key, metric_value)
                alert_triggered = anomaly is not None
                
                if alert_triggered and anomaly:
                    # Include anomaly details in alert
                    metrics['anomaly_details'] = anomaly
            
            if alert_triggered:
                self._trigger_alert(rule, metric_value, metrics)
                # Set cooldown
                self.alert_cooldowns[cooldown_key] = current_time + (rule.cooldown_minutes * 60)
    
    def _evaluate_condition(self, condition: str, value: float, threshold: float) -> bool:
        """Evaluate alert condition"""
        if condition == 'above':
            return value > threshold
        elif condition == 'below':
            return value < threshold
        elif condition == 'equals':
            return abs(value - threshold) < 0.001  # Float comparison
        else:
            return False
    
    def _trigger_alert(self, rule: AlertRule, metric_value: float, context: Dict[str, Any]):
        """Trigger an alert"""
        alert_id = f"{rule.rule_id}_{int(time.time())}"
        
        # Create alert message
        message = f"{rule.description}. Current value: {metric_value}, Threshold: {rule.threshold}"
        
        # Add anomaly details if available
        if 'anomaly_details' in context:
            anomaly = context['anomaly_details']
            message += f". Anomaly detected: {anomaly['type']}"
        
        alert = Alert(
            alert_id=alert_id,
            rule_id=rule.rule_id,
            timestamp=time.time(),
            severity=rule.severity,
            title=rule.name,
            message=message,
            metric_value=metric_value,
            threshold=rule.threshold,
            resolved=False,
            resolution_timestamp=None,
            notification_sent=False
        )
        
        # Store alert
        self._store_alert(alert)
        self.active_alerts[alert_id] = alert
        
        # Send notifications
        notification_success = self.notification_manager.send_notification(
            alert, rule.notification_channels
        )
        
        if notification_success:
            alert.notification_sent = True
            self._update_alert_notification_status(alert_id, True)
        
        logger.info(f"Alert triggered: {alert.title} - {alert.message}")
    
    def _store_alert(self, alert: Alert):
        """Store alert in database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute('''
                    INSERT INTO alert_instances 
                    (alert_id, rule_id, timestamp, severity, title, message,
                     metric_value, threshold, resolved, notification_sent)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    alert.alert_id, alert.rule_id, alert.timestamp, alert.severity,
                    alert.title, alert.message, alert.metric_value, alert.threshold,
                    alert.resolved, alert.notification_sent
                ))
        except Exception as e:
            logger.error(f"Failed to store alert: {e}")
    
    def _update_alert_notification_status(self, alert_id: str, sent: bool):
        """Update alert notification status"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute('''
                    UPDATE alert_instances 
                    SET notification_sent = ?
                    WHERE alert_id = ?
                ''', (sent, alert_id))
        except Exception as e:
            logger.error(f"Failed to update alert notification status: {e}")
    
    def resolve_alert(self, alert_id: str, resolution_note: str = "") -> bool:
        """Manually resolve an alert"""
        try:
            current_time = time.time()
            
            with sqlite3.connect(self.db_path) as conn:
                conn.execute('''
                    UPDATE alert_instances 
                    SET resolved = TRUE, resolution_timestamp = ?
                    WHERE alert_id = ?
                ''', (current_time, alert_id))
            
            if alert_id in self.active_alerts:
                self.active_alerts[alert_id].resolved = True
                self.active_alerts[alert_id].resolution_timestamp = current_time
                del self.active_alerts[alert_id]
            
            logger.info(f"Alert resolved: {alert_id} - {resolution_note}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to resolve alert {alert_id}: {e}")
            return False
    
    def get_active_alerts(self) -> List[Alert]:
        """Get all active (unresolved) alerts"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute('''
                    SELECT alert_id, rule_id, timestamp, severity, title, message,
                           metric_value, threshold, resolved, resolution_timestamp,
                           notification_sent
                    FROM alert_instances 
                    WHERE resolved = FALSE
                    ORDER BY timestamp DESC
                ''')
                
                alerts = []
                for row in cursor.fetchall():
                    alert = Alert(
                        alert_id=row[0],
                        rule_id=row[1],
                        timestamp=row[2],
                        severity=row[3],
                        title=row[4],
                        message=row[5],
                        metric_value=row[6],
                        threshold=row[7],
                        resolved=bool(row[8]),
                        resolution_timestamp=row[9],
                        notification_sent=bool(row[10])
                    )
                    alerts.append(alert)
                
                return alerts
                
        except Exception as e:
            logger.error(f"Failed to get active alerts: {e}")
            return []
    
    def get_alert_history(self, hours: int = 24) -> List[Alert]:
        """Get alert history for specified time period"""
        try:
            start_time = time.time() - (hours * 3600)
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute('''
                    SELECT alert_id, rule_id, timestamp, severity, title, message,
                           metric_value, threshold, resolved, resolution_timestamp,
                           notification_sent
                    FROM alert_instances 
                    WHERE timestamp >= ?
                    ORDER BY timestamp DESC
                ''', (start_time,))
                
                alerts = []
                for row in cursor.fetchall():
                    alert = Alert(
                        alert_id=row[0],
                        rule_id=row[1],
                        timestamp=row[2],
                        severity=row[3],
                        title=row[4],
                        message=row[5],
                        metric_value=row[6],
                        threshold=row[7],
                        resolved=bool(row[8]),
                        resolution_timestamp=row[9],
                        notification_sent=bool(row[10])
                    )
                    alerts.append(alert)
                
                return alerts
                
        except Exception as e:
            logger.error(f"Failed to get alert history: {e}")
            return []
    
    def get_alert_statistics(self, hours: int = 24) -> Dict[str, Any]:
        """Get alert statistics for specified period"""
        try:
            start_time = time.time() - (hours * 3600)
            
            with sqlite3.connect(self.db_path) as conn:
                # Count by severity
                severity_cursor = conn.execute('''
                    SELECT severity, COUNT(*) 
                    FROM alert_instances 
                    WHERE timestamp >= ?
                    GROUP BY severity
                ''', (start_time,))
                
                severity_counts = dict(severity_cursor.fetchall())
                
                # Count resolved vs unresolved
                resolution_cursor = conn.execute('''
                    SELECT resolved, COUNT(*) 
                    FROM alert_instances 
                    WHERE timestamp >= ?
                    GROUP BY resolved
                ''', (start_time,))
                
                resolution_counts = dict(resolution_cursor.fetchall())
                
                # Top alert types
                rule_cursor = conn.execute('''
                    SELECT rule_id, COUNT(*) 
                    FROM alert_instances 
                    WHERE timestamp >= ?
                    GROUP BY rule_id
                    ORDER BY COUNT(*) DESC
                    LIMIT 10
                ''', (start_time,))
                
                top_rules = dict(rule_cursor.fetchall())
                
                return {
                    'period_hours': hours,
                    'total_alerts': sum(severity_counts.values()),
                    'by_severity': severity_counts,
                    'resolved': resolution_counts.get(1, 0),
                    'unresolved': resolution_counts.get(0, 0),
                    'top_alert_types': top_rules
                }
                
        except Exception as e:
            logger.error(f"Failed to get alert statistics: {e}")
            return {}
    
    def add_alert_rule(self, rule: AlertRule) -> bool:
        """Add or update an alert rule"""
        try:
            self.alert_rules[rule.rule_id] = rule
            self._save_alert_rules()
            logger.info(f"Alert rule added/updated: {rule.rule_id}")
            return True
        except Exception as e:
            logger.error(f"Failed to add alert rule: {e}")
            return False
    
    def remove_alert_rule(self, rule_id: str) -> bool:
        """Remove an alert rule"""
        try:
            if rule_id in self.alert_rules:
                del self.alert_rules[rule_id]
                self._save_alert_rules()
                logger.info(f"Alert rule removed: {rule_id}")
                return True
            return False
        except Exception as e:
            logger.error(f"Failed to remove alert rule: {e}")
            return False
    
    def test_notification_channels(self) -> Dict[str, bool]:
        """Test all notification channels"""
        test_alert = Alert(
            alert_id='test_alert',
            rule_id='test_rule',
            timestamp=time.time(),
            severity='info',
            title='Test Alert',
            message='This is a test alert to verify notification channels',
            metric_value=0.0,
            threshold=0.0,
            resolved=False,
            resolution_timestamp=None,
            notification_sent=False
        )
        
        results = {}
        channels = ['log', 'file', 'email', 'webhook']
        
        for channel in channels:
            try:
                success = self.notification_manager._send_to_channel(channel, test_alert)
                results[channel] = success
            except Exception as e:
                logger.error(f"Failed to test {channel}: {e}")
                results[channel] = False
        
        return results

# CLI interface
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Alerting System')
    parser.add_argument('--base-path', default='/Users/nalve/ce-simple/tools/monitoring',
                       help='Base path for monitoring data')
    parser.add_argument('--test-notifications', action='store_true',
                       help='Test notification channels')
    parser.add_argument('--list-alerts', action='store_true',
                       help='List active alerts')
    parser.add_argument('--alert-history', type=int, default=24,
                       help='Show alert history for N hours')
    parser.add_argument('--resolve-alert', type=str,
                       help='Resolve alert by ID')
    parser.add_argument('--stats', type=int, default=24,
                       help='Show alert statistics for N hours')
    
    args = parser.parse_args()
    
    # Initialize alerting engine
    engine = AlertingEngine(args.base_path)
    
    if args.test_notifications:
        print("Testing notification channels...")
        results = engine.test_notification_channels()
        for channel, success in results.items():
            status = "✓" if success else "✗"
            print(f"{status} {channel}")
    
    elif args.list_alerts:
        alerts = engine.get_active_alerts()
        if alerts:
            print(f"Active alerts ({len(alerts)}):")
            for alert in alerts:
                print(f"- {alert.alert_id}: {alert.title} ({alert.severity})")
        else:
            print("No active alerts")
    
    elif args.resolve_alert:
        success = engine.resolve_alert(args.resolve_alert, "Manually resolved via CLI")
        if success:
            print(f"Alert {args.resolve_alert} resolved")
        else:
            print(f"Failed to resolve alert {args.resolve_alert}")
    
    elif args.stats:
        stats = engine.get_alert_statistics(args.stats)
        print(json.dumps(stats, indent=2))
    
    else:
        history = engine.get_alert_history(args.alert_history)
        print(f"Alert history for last {args.alert_history} hours ({len(history)} alerts):")
        for alert in history[:10]:  # Show last 10
            status = "Resolved" if alert.resolved else "Active"
            print(f"- {alert.timestamp}: {alert.title} ({alert.severity}) - {status}")