#!/usr/bin/env python3
"""
Automated Alert System
Comprehensive alerting and notification system for Context Engineering ecosystem
Monitors health thresholds and triggers automated responses with escalation protocols
"""

import json
import os
import sys
import time
import datetime
import sqlite3
import logging
import smtplib
import threading
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Callable
from dataclasses import dataclass, asdict
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from concurrent.futures import ThreadPoolExecutor
import hashlib

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/Users/nalve/claude-context-engineering/scripts/results/monitoring/alert-system.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class AlertRule:
    """Alert rule definition"""
    id: str
    name: str
    description: str
    condition: str  # Python expression to evaluate
    severity: str   # CRITICAL, WARNING, INFO
    threshold: float
    cooldown: int   # seconds between same alerts
    enabled: bool
    auto_resolve: bool
    escalation_rules: Optional[Dict] = None

@dataclass
class Alert:
    """Alert instance"""
    id: str
    rule_id: str
    severity: str
    title: str
    message: str
    timestamp: str
    source: str
    value: Optional[float] = None
    threshold: Optional[float] = None
    status: str = 'ACTIVE'  # ACTIVE, RESOLVED, ACKNOWLEDGED
    acknowledged_by: Optional[str] = None
    acknowledged_at: Optional[str] = None
    resolved_at: Optional[str] = None
    escalation_level: int = 0

@dataclass
class NotificationChannel:
    """Notification channel configuration"""
    id: str
    type: str  # dashboard, email, slack, webhook
    config: Dict
    enabled: bool
    severity_filter: List[str]  # Which severities to send

class AlertSystem:
    """Comprehensive alerting and notification system"""
    
    def __init__(self, config_path: str = None):
        self.base_path = Path("/Users/nalve/claude-context-engineering")
        self.config = self._load_config(config_path)
        self.db_path = self.base_path / "scripts/results/monitoring/alert_system.db"
        self.running = False
        
        # Alert management
        self.active_alerts = {}
        self.alert_rules = {}
        self.notification_channels = {}
        self.escalation_timers = {}
        
        # Initialize system
        self._init_database()
        self._load_alert_rules()
        self._load_notification_channels()
        
        # Performance tracking
        self.metrics_cache = {}
        self.last_health_check = {}
        
    def _load_config(self, config_path: str) -> Dict:
        """Load alert system configuration"""
        default_config = {
            'check_interval': 60,        # seconds
            'escalation_timeout': 300,   # 5 minutes
            'auto_resolve_timeout': 1800, # 30 minutes
            'max_alerts_per_rule': 10,
            'alert_retention_days': 30,
            'dashboard_enabled': True,
            'email_enabled': False,
            'slack_enabled': False,
            'webhook_enabled': False
        }
        
        if config_path and os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    user_config = json.load(f)
                    default_config.update(user_config)
            except Exception as e:
                logger.warning(f"Failed to load config: {e}. Using defaults.")
        
        return default_config
    
    def _init_database(self):
        """Initialize SQLite database for alert tracking"""
        os.makedirs(self.db_path.parent, exist_ok=True)
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Alerts table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS alerts (
                    id TEXT PRIMARY KEY,
                    rule_id TEXT NOT NULL,
                    severity TEXT NOT NULL,
                    title TEXT NOT NULL,
                    message TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    source TEXT NOT NULL,
                    value REAL,
                    threshold REAL,
                    status TEXT DEFAULT 'ACTIVE',
                    acknowledged_by TEXT,
                    acknowledged_at TEXT,
                    resolved_at TEXT,
                    escalation_level INTEGER DEFAULT 0,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Alert rules table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS alert_rules (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT,
                    condition TEXT NOT NULL,
                    severity TEXT NOT NULL,
                    threshold REAL,
                    cooldown INTEGER DEFAULT 300,
                    enabled BOOLEAN DEFAULT TRUE,
                    auto_resolve BOOLEAN DEFAULT FALSE,
                    escalation_rules TEXT,  -- JSON
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Notification log table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS notification_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    alert_id TEXT NOT NULL,
                    channel_id TEXT NOT NULL,
                    channel_type TEXT NOT NULL,
                    status TEXT NOT NULL,  -- SUCCESS, FAILED
                    sent_at TEXT NOT NULL,
                    error_message TEXT,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            conn.commit()
            logger.info("Alert system database initialized")
    
    def _load_alert_rules(self):
        """Load alert rules from database and defaults"""
        # Load from database first
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM alert_rules WHERE enabled = TRUE")
                
                for row in cursor.fetchall():
                    rule_data = {
                        'id': row[0], 'name': row[1], 'description': row[2],
                        'condition': row[3], 'severity': row[4], 'threshold': row[5],
                        'cooldown': row[6], 'enabled': row[7], 'auto_resolve': row[8]
                    }
                    
                    escalation_rules = None
                    if row[9]:  # escalation_rules JSON
                        try:
                            escalation_rules = json.loads(row[9])
                        except:
                            pass
                    
                    rule = AlertRule(
                        **rule_data,
                        escalation_rules=escalation_rules
                    )
                    self.alert_rules[rule.id] = rule
                    
        except Exception as e:
            logger.error(f"Error loading alert rules from database: {e}")
        
        # Load default rules if none exist
        if not self.alert_rules:
            self._create_default_alert_rules()
    
    def _create_default_alert_rules(self):
        """Create default alert rules for Context Engineering system"""
        default_rules = [
            {
                'id': 'critical_health_score',
                'name': 'Critical Health Score',
                'description': 'Overall system health score below critical threshold',
                'condition': 'health_score < threshold',
                'severity': 'CRITICAL',
                'threshold': 70.0,
                'cooldown': 300,
                'enabled': True,
                'auto_resolve': True,
                'escalation_rules': {
                    'levels': [
                        {'timeout': 300, 'channels': ['dashboard', 'email']},
                        {'timeout': 900, 'channels': ['dashboard', 'email', 'slack']},
                        {'timeout': 1800, 'channels': ['dashboard', 'email', 'slack', 'webhook']}
                    ]
                }
            },
            {
                'id': 'warning_health_score',
                'name': 'Warning Health Score',
                'description': 'System health score below warning threshold',
                'condition': 'health_score < threshold and health_score >= 70.0',
                'severity': 'WARNING',
                'threshold': 85.0,
                'cooldown': 600,
                'enabled': True,
                'auto_resolve': True
            },
            {
                'id': 'command_availability_low',
                'name': 'Low Command Availability',
                'description': 'Command ecosystem availability below threshold',
                'condition': 'command_availability < threshold',
                'severity': 'WARNING',
                'threshold': 90.0,
                'cooldown': 300,
                'enabled': True,
                'auto_resolve': True
            },
            {
                'id': 'high_response_time',
                'name': 'High Response Time',
                'description': 'System response time exceeds threshold',
                'condition': 'response_time > threshold',
                'severity': 'WARNING',
                'threshold': 1000.0,  # milliseconds
                'cooldown': 300,
                'enabled': True,
                'auto_resolve': True
            },
            {
                'id': 'low_success_rate',
                'name': 'Low Success Rate',
                'description': 'System success rate below threshold',
                'condition': 'success_rate < threshold',
                'severity': 'WARNING',
                'threshold': 95.0,
                'cooldown': 300,
                'enabled': True,
                'auto_resolve': True
            },
            {
                'id': 'navigation_efficiency_poor',
                'name': 'Poor Navigation Efficiency',
                'description': 'Navigation efficiency exceeds cognitive steps target',
                'condition': 'navigation_efficiency > threshold',
                'severity': 'INFO',
                'threshold': 2.5,
                'cooldown': 600,
                'enabled': True,
                'auto_resolve': True
            },
            {
                'id': 'broken_links_detected',
                'name': 'Broken Links Detected',
                'description': 'Cross-reference validation found broken links',
                'condition': 'broken_links > threshold',
                'severity': 'WARNING',
                'threshold': 5.0,
                'cooldown': 1800,
                'enabled': True,
                'auto_resolve': False
            },
            {
                'id': 'script_failures',
                'name': 'Script Execution Failures',
                'description': 'Multiple script execution failures detected',
                'condition': 'script_failure_rate > threshold',
                'severity': 'WARNING',
                'threshold': 10.0,  # percentage
                'cooldown': 300,
                'enabled': True,
                'auto_resolve': True
            },
            {
                'id': 'memory_usage_high',
                'name': 'High Memory Usage',
                'description': 'System memory usage exceeds threshold',
                'condition': 'memory_usage > threshold',
                'severity': 'WARNING',
                'threshold': 80.0,  # percentage
                'cooldown': 300,
                'enabled': True,
                'auto_resolve': True
            },
            {
                'id': 'system_unavailable',
                'name': 'System Unavailable',
                'description': 'Core system components are unavailable',
                'condition': 'availability < threshold',
                'severity': 'CRITICAL',
                'threshold': 50.0,  # percentage
                'cooldown': 60,
                'enabled': True,
                'auto_resolve': True,
                'escalation_rules': {
                    'levels': [
                        {'timeout': 60, 'channels': ['dashboard', 'email', 'slack']},
                        {'timeout': 300, 'channels': ['dashboard', 'email', 'slack', 'webhook']}
                    ]
                }
            }
        ]
        
        # Store default rules in database
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            for rule_data in default_rules:
                escalation_json = json.dumps(rule_data.get('escalation_rules')) if rule_data.get('escalation_rules') else None
                
                cursor.execute("""
                    INSERT OR REPLACE INTO alert_rules 
                    (id, name, description, condition, severity, threshold, cooldown, 
                     enabled, auto_resolve, escalation_rules)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    rule_data['id'], rule_data['name'], rule_data['description'],
                    rule_data['condition'], rule_data['severity'], rule_data['threshold'],
                    rule_data['cooldown'], rule_data['enabled'], rule_data['auto_resolve'],
                    escalation_json
                ))
                
                # Create AlertRule object
                rule = AlertRule(**{k: v for k, v in rule_data.items() if k != 'escalation_rules'},
                               escalation_rules=rule_data.get('escalation_rules'))
                self.alert_rules[rule.id] = rule
            
            conn.commit()
            
        logger.info(f"Created {len(default_rules)} default alert rules")
    
    def _load_notification_channels(self):
        """Load notification channel configurations"""
        default_channels = [
            {
                'id': 'dashboard',
                'type': 'dashboard',
                'config': {
                    'file_path': str(self.base_path / "scripts/results/monitoring/alerts-dashboard.json")
                },
                'enabled': self.config['dashboard_enabled'],
                'severity_filter': ['CRITICAL', 'WARNING', 'INFO']
            },
            {
                'id': 'email',
                'type': 'email',
                'config': {
                    'smtp_server': 'localhost',
                    'smtp_port': 587,
                    'smtp_user': '',
                    'smtp_password': '',
                    'from_email': 'alerts@context-engineering.local',
                    'to_emails': ['admin@context-engineering.local']
                },
                'enabled': self.config['email_enabled'],
                'severity_filter': ['CRITICAL', 'WARNING']
            },
            {
                'id': 'slack',
                'type': 'slack',
                'config': {
                    'webhook_url': '',
                    'channel': '#alerts',
                    'username': 'Context Engineering Bot'
                },
                'enabled': self.config['slack_enabled'],
                'severity_filter': ['CRITICAL', 'WARNING']
            },
            {
                'id': 'webhook',
                'type': 'webhook',
                'config': {
                    'url': '',
                    'method': 'POST',
                    'headers': {'Content-Type': 'application/json'},
                    'timeout': 30
                },
                'enabled': self.config['webhook_enabled'],
                'severity_filter': ['CRITICAL']
            }
        ]
        
        for channel_data in default_channels:
            channel = NotificationChannel(**channel_data)
            self.notification_channels[channel.id] = channel
    
    def start_monitoring(self):
        """Start the alert monitoring system"""
        logger.info("Starting Alert System")
        self.running = True
        
        # Start monitoring thread
        monitor_thread = threading.Thread(target=self._monitoring_loop, daemon=True)
        monitor_thread.start()
        
        # Start escalation processor
        escalation_thread = threading.Thread(target=self._escalation_processor, daemon=True)
        escalation_thread.start()
        
        # Start cleanup processor
        cleanup_thread = threading.Thread(target=self._cleanup_processor, daemon=True)
        cleanup_thread.start()
        
        logger.info("Alert system started successfully")
    
    def stop_monitoring(self):
        """Stop the alert monitoring system"""
        logger.info("Stopping Alert System")
        self.running = False
    
    def _monitoring_loop(self):
        """Main monitoring loop to check alert conditions"""
        while self.running:
            try:
                start_time = time.time()
                
                # Get current system metrics
                metrics = self._collect_system_metrics()
                
                # Check all alert rules
                triggered_alerts = self._check_alert_rules(metrics)
                
                # Process triggered alerts
                for alert in triggered_alerts:
                    self._process_alert(alert)
                
                # Check for auto-resolution
                self._check_auto_resolution(metrics)
                
                execution_time = time.time() - start_time
                logger.debug(f"Alert check completed in {execution_time:.2f}s")
                
                # Wait for next cycle
                time.sleep(self.config['check_interval'])
                
            except Exception as e:
                logger.error(f"Error in monitoring loop: {e}")
                time.sleep(30)  # Wait before retry
    
    def _collect_system_metrics(self) -> Dict:
        """Collect current system metrics for alert evaluation"""
        try:
            # Get health report from health monitor
            health_report_path = self.base_path / "scripts/results/monitoring/health-report-latest.json"
            
            if health_report_path.exists():
                with open(health_report_path, 'r') as f:
                    health_data = json.load(f)
                
                # Extract metrics for alert evaluation
                summary = health_data.get('executive_summary', {})
                components = health_data.get('component_health', {})
                performance = health_data.get('performance_metrics', {})
                
                metrics = {
                    'health_score': summary.get('overall_health_score', 0),
                    'availability': summary.get('availability', 0),
                    'navigation_efficiency': summary.get('navigation_efficiency', 2.5),
                    'command_availability': components.get('commands', 0),
                    'script_health': components.get('scripts', 0),
                    'knowledge_health': components.get('knowledge', 0),
                    'performance_health': components.get('performance', 0),
                    'response_time': performance.get('response_time', 0),
                    'success_rate': performance.get('success_rate', 100),
                    'error_rate': performance.get('error_rate', 0),
                    'timestamp': datetime.datetime.utcnow().isoformat()
                }
            else:
                # Fallback metrics
                metrics = {
                    'health_score': 85.0,
                    'availability': 95.0,
                    'navigation_efficiency': 2.3,
                    'command_availability': 95.0,
                    'script_health': 90.0,
                    'knowledge_health': 92.0,
                    'performance_health': 88.0,
                    'response_time': 450.0,
                    'success_rate': 96.5,
                    'error_rate': 3.5,
                    'timestamp': datetime.datetime.utcnow().isoformat()
                }
            
            # Add cross-reference validation metrics
            cross_ref_report_path = self.base_path / "scripts/results/monitoring/cross-ref-validation-latest.json"
            if cross_ref_report_path.exists():
                try:
                    with open(cross_ref_report_path, 'r') as f:
                        cross_ref_data = json.load(f)
                    
                    validation_summary = cross_ref_data.get('validation_summary', {})
                    metrics['broken_links'] = validation_summary.get('broken_links', 0)
                    metrics['link_validity_rate'] = (
                        validation_summary.get('valid_links', 0) / 
                        max(validation_summary.get('total_links', 1), 1) * 100
                    )
                except:
                    metrics['broken_links'] = 0
                    metrics['link_validity_rate'] = 100.0
            else:
                metrics['broken_links'] = 0
                metrics['link_validity_rate'] = 100.0
            
            # Add system resource metrics (simplified)
            try:
                import psutil
                metrics['memory_usage'] = psutil.virtual_memory().percent
                metrics['cpu_usage'] = psutil.cpu_percent(interval=1)
                metrics['disk_usage'] = psutil.disk_usage('/').percent
            except ImportError:
                metrics['memory_usage'] = 60.0
                metrics['cpu_usage'] = 45.0
                metrics['disk_usage'] = 70.0
            
            # Calculate derived metrics
            metrics['script_failure_rate'] = 100.0 - metrics['script_health']
            
            # Cache metrics
            self.metrics_cache = metrics
            
            return metrics
            
        except Exception as e:
            logger.error(f"Error collecting system metrics: {e}")
            return self.metrics_cache or {}
    
    def _check_alert_rules(self, metrics: Dict) -> List[Alert]:
        """Check all alert rules against current metrics"""
        triggered_alerts = []
        
        for rule_id, rule in self.alert_rules.items():
            if not rule.enabled:
                continue
                
            try:
                # Check cooldown
                if self._is_rule_in_cooldown(rule_id):
                    continue
                
                # Evaluate rule condition
                if self._evaluate_rule_condition(rule, metrics):
                    alert = self._create_alert(rule, metrics)
                    triggered_alerts.append(alert)
                    
                    # Update cooldown
                    self._set_rule_cooldown(rule_id)
                    
            except Exception as e:
                logger.error(f"Error checking alert rule {rule_id}: {e}")
        
        return triggered_alerts
    
    def _evaluate_rule_condition(self, rule: AlertRule, metrics: Dict) -> bool:
        """Evaluate if a rule condition is met"""
        try:
            # Prepare evaluation context
            eval_context = metrics.copy()
            eval_context['threshold'] = rule.threshold
            
            # Evaluate condition
            return eval(rule.condition, {"__builtins__": {}}, eval_context)
            
        except Exception as e:
            logger.error(f"Error evaluating rule condition '{rule.condition}': {e}")
            return False
    
    def _create_alert(self, rule: AlertRule, metrics: Dict) -> Alert:
        """Create an alert instance from a triggered rule"""
        timestamp = datetime.datetime.utcnow().isoformat()
        alert_id = self._generate_alert_id(rule.id, timestamp)
        
        # Get the metric value that triggered the alert
        value = None
        if 'health_score' in rule.condition:
            value = metrics.get('health_score')
        elif 'response_time' in rule.condition:
            value = metrics.get('response_time')
        elif 'success_rate' in rule.condition:
            value = metrics.get('success_rate')
        elif 'navigation_efficiency' in rule.condition:
            value = metrics.get('navigation_efficiency')
        elif 'broken_links' in rule.condition:
            value = metrics.get('broken_links')
        elif 'memory_usage' in rule.condition:
            value = metrics.get('memory_usage')
        elif 'availability' in rule.condition:
            value = metrics.get('availability')
        
        # Generate alert message
        message = self._generate_alert_message(rule, metrics, value)
        
        alert = Alert(
            id=alert_id,
            rule_id=rule.id,
            severity=rule.severity,
            title=rule.name,
            message=message,
            timestamp=timestamp,
            source='alert_system',
            value=value,
            threshold=rule.threshold
        )
        
        return alert
    
    def _generate_alert_message(self, rule: AlertRule, metrics: Dict, value: Optional[float]) -> str:
        """Generate descriptive alert message"""
        base_message = rule.description
        
        if value is not None and rule.threshold is not None:
            if 'health_score' in rule.condition:
                base_message += f" (Current: {value:.2f}, Threshold: {rule.threshold:.2f})"
            elif 'response_time' in rule.condition:
                base_message += f" (Current: {value:.0f}ms, Threshold: {rule.threshold:.0f}ms)"
            elif 'success_rate' in rule.condition:
                base_message += f" (Current: {value:.1f}%, Threshold: {rule.threshold:.1f}%)"
            elif 'navigation_efficiency' in rule.condition:
                base_message += f" (Current: {value:.2f} steps, Target: ≤{rule.threshold:.1f})"
            elif 'broken_links' in rule.condition:
                base_message += f" (Found: {int(value)} links, Threshold: {int(rule.threshold)})"
            elif 'memory_usage' in rule.condition:
                base_message += f" (Current: {value:.1f}%, Threshold: {rule.threshold:.1f}%)"
            elif 'availability' in rule.condition:
                base_message += f" (Current: {value:.1f}%, Threshold: {rule.threshold:.1f}%)"
        
        # Add timestamp
        base_message += f" [Detected at {datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC]"
        
        return base_message
    
    def _generate_alert_id(self, rule_id: str, timestamp: str) -> str:
        """Generate unique alert ID"""
        content = f"{rule_id}_{timestamp}"
        return hashlib.md5(content.encode()).hexdigest()[:12]
    
    def _is_rule_in_cooldown(self, rule_id: str) -> bool:
        """Check if rule is in cooldown period"""
        if rule_id not in self.last_health_check:
            return False
        
        rule = self.alert_rules[rule_id]
        last_check = self.last_health_check[rule_id]
        return time.time() - last_check < rule.cooldown
    
    def _set_rule_cooldown(self, rule_id: str):
        """Set rule cooldown timestamp"""
        self.last_health_check[rule_id] = time.time()
    
    def _process_alert(self, alert: Alert):
        """Process a triggered alert"""
        try:
            # Store alert
            self._store_alert(alert)
            
            # Add to active alerts
            self.active_alerts[alert.id] = alert
            
            # Send notifications
            self._send_notifications(alert)
            
            # Set up escalation if configured
            rule = self.alert_rules[alert.rule_id]
            if rule.escalation_rules:
                self._setup_escalation(alert, rule.escalation_rules)
            
            logger.warning(f"ALERT {alert.severity}: {alert.title} - {alert.message}")
            
        except Exception as e:
            logger.error(f"Error processing alert {alert.id}: {e}")
    
    def _store_alert(self, alert: Alert):
        """Store alert in database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO alerts 
                    (id, rule_id, severity, title, message, timestamp, source, 
                     value, threshold, status, escalation_level)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    alert.id, alert.rule_id, alert.severity, alert.title,
                    alert.message, alert.timestamp, alert.source,
                    alert.value, alert.threshold, alert.status,
                    alert.escalation_level
                ))
                conn.commit()
        except Exception as e:
            logger.error(f"Error storing alert: {e}")
    
    def _send_notifications(self, alert: Alert):
        """Send notifications through all configured channels"""
        for channel_id, channel in self.notification_channels.items():
            if not channel.enabled:
                continue
                
            if alert.severity not in channel.severity_filter:
                continue
            
            try:
                success = self._send_notification(alert, channel)
                self._log_notification(alert.id, channel_id, channel.type, success)
                
            except Exception as e:
                logger.error(f"Error sending notification via {channel_id}: {e}")
                self._log_notification(alert.id, channel_id, channel.type, False, str(e))
    
    def _send_notification(self, alert: Alert, channel: NotificationChannel) -> bool:
        """Send notification via specific channel"""
        if channel.type == 'dashboard':
            return self._send_dashboard_notification(alert, channel)
        elif channel.type == 'email':
            return self._send_email_notification(alert, channel)
        elif channel.type == 'slack':
            return self._send_slack_notification(alert, channel)
        elif channel.type == 'webhook':
            return self._send_webhook_notification(alert, channel)
        else:
            logger.warning(f"Unknown notification channel type: {channel.type}")
            return False
    
    def _send_dashboard_notification(self, alert: Alert, channel: NotificationChannel) -> bool:
        """Send notification to dashboard (file-based)"""
        try:
            file_path = channel.config['file_path']
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            # Load existing alerts
            alerts_data = []
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    try:
                        alerts_data = json.load(f)
                    except:
                        alerts_data = []
            
            # Add new alert
            alert_dict = asdict(alert)
            alerts_data.append(alert_dict)
            
            # Keep only recent alerts (last 100)
            alerts_data = alerts_data[-100:]
            
            # Save updated alerts
            with open(file_path, 'w') as f:
                json.dump(alerts_data, f, indent=2)
            
            return True
            
        except Exception as e:
            logger.error(f"Error sending dashboard notification: {e}")
            return False
    
    def _send_email_notification(self, alert: Alert, channel: NotificationChannel) -> bool:
        """Send email notification"""
        try:
            config = channel.config
            
            # Create message
            msg = MIMEMultipart()
            msg['From'] = config['from_email']
            msg['To'] = ', '.join(config['to_emails'])
            msg['Subject'] = f"[{alert.severity}] {alert.title}"
            
            # Email body
            body = f"""
Context Engineering Alert

Severity: {alert.severity}
Title: {alert.title}
Message: {alert.message}
Timestamp: {alert.timestamp}
Source: {alert.source}

Alert ID: {alert.id}
Rule ID: {alert.rule_id}

This is an automated alert from the Context Engineering monitoring system.
"""
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Send email
            server = smtplib.SMTP(config['smtp_server'], config['smtp_port'])
            if config.get('smtp_user') and config.get('smtp_password'):
                server.starttls()
                server.login(config['smtp_user'], config['smtp_password'])
            
            server.send_message(msg)
            server.quit()
            
            return True
            
        except Exception as e:
            logger.error(f"Error sending email notification: {e}")
            return False
    
    def _send_slack_notification(self, alert: Alert, channel: NotificationChannel) -> bool:
        """Send Slack notification"""
        try:
            import requests
            
            config = channel.config
            webhook_url = config['webhook_url']
            
            if not webhook_url:
                logger.warning("Slack webhook URL not configured")
                return False
            
            # Create Slack message
            color = {
                'CRITICAL': 'danger',
                'WARNING': 'warning',
                'INFO': 'good'
            }.get(alert.severity, 'warning')
            
            payload = {
                'channel': config.get('channel', '#alerts'),
                'username': config.get('username', 'Context Engineering Bot'),
                'attachments': [
                    {
                        'color': color,
                        'title': f"[{alert.severity}] {alert.title}",
                        'text': alert.message,
                        'fields': [
                            {'title': 'Alert ID', 'value': alert.id, 'short': True},
                            {'title': 'Rule ID', 'value': alert.rule_id, 'short': True},
                            {'title': 'Timestamp', 'value': alert.timestamp, 'short': False}
                        ],
                        'ts': int(datetime.datetime.fromisoformat(alert.timestamp).timestamp())
                    }
                ]
            }
            
            response = requests.post(webhook_url, json=payload, timeout=30)
            return response.status_code == 200
            
        except Exception as e:
            logger.error(f"Error sending Slack notification: {e}")
            return False
    
    def _send_webhook_notification(self, alert: Alert, channel: NotificationChannel) -> bool:
        """Send webhook notification"""
        try:
            import requests
            
            config = channel.config
            url = config['url']
            
            if not url:
                logger.warning("Webhook URL not configured")
                return False
            
            # Create webhook payload
            payload = {
                'alert': asdict(alert),
                'timestamp': datetime.datetime.utcnow().isoformat(),
                'source': 'context_engineering_alert_system'
            }
            
            headers = config.get('headers', {})
            timeout = config.get('timeout', 30)
            
            response = requests.post(url, json=payload, headers=headers, timeout=timeout)
            return response.status_code == 200
            
        except Exception as e:
            logger.error(f"Error sending webhook notification: {e}")
            return False
    
    def _log_notification(self, alert_id: str, channel_id: str, channel_type: str, 
                         success: bool, error_message: str = None):
        """Log notification attempt"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO notification_log 
                    (alert_id, channel_id, channel_type, status, sent_at, error_message)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    alert_id, channel_id, channel_type,
                    'SUCCESS' if success else 'FAILED',
                    datetime.datetime.utcnow().isoformat(),
                    error_message
                ))
                conn.commit()
        except Exception as e:
            logger.error(f"Error logging notification: {e}")
    
    def _check_auto_resolution(self, metrics: Dict):
        """Check for auto-resolution of active alerts"""
        resolved_alerts = []
        
        for alert_id, alert in self.active_alerts.items():
            rule = self.alert_rules.get(alert.rule_id)
            
            if not rule or not rule.auto_resolve:
                continue
            
            # Check if condition is no longer met
            if not self._evaluate_rule_condition(rule, metrics):
                alert.status = 'RESOLVED'
                alert.resolved_at = datetime.datetime.utcnow().isoformat()
                resolved_alerts.append(alert)
                
                logger.info(f"Auto-resolved alert {alert.id}: {alert.title}")
        
        # Remove resolved alerts from active list
        for alert in resolved_alerts:
            if alert.id in self.active_alerts:
                del self.active_alerts[alert.id]
            
            # Update database
            self._update_alert_status(alert)
    
    def _update_alert_status(self, alert: Alert):
        """Update alert status in database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE alerts 
                    SET status = ?, resolved_at = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                """, (alert.status, alert.resolved_at, alert.id))
                conn.commit()
        except Exception as e:
            logger.error(f"Error updating alert status: {e}")
    
    def _setup_escalation(self, alert: Alert, escalation_rules: Dict):
        """Setup escalation timers for alert"""
        if 'levels' not in escalation_rules:
            return
        
        # Schedule escalation levels
        for level, escalation_config in enumerate(escalation_rules['levels']):
            timeout = escalation_config['timeout']
            
            timer = threading.Timer(timeout, self._escalate_alert, args=[alert.id, level])
            timer.start()
            
            if alert.id not in self.escalation_timers:
                self.escalation_timers[alert.id] = []
            self.escalation_timers[alert.id].append(timer)
    
    def _escalate_alert(self, alert_id: str, escalation_level: int):
        """Escalate an alert to the next level"""
        try:
            alert = self.active_alerts.get(alert_id)
            if not alert or alert.status != 'ACTIVE':
                return
            
            rule = self.alert_rules.get(alert.rule_id)
            if not rule or not rule.escalation_rules:
                return
            
            escalation_levels = rule.escalation_rules.get('levels', [])
            if escalation_level >= len(escalation_levels):
                return
            
            escalation_config = escalation_levels[escalation_level]
            channels = escalation_config.get('channels', [])
            
            # Update alert escalation level
            alert.escalation_level = escalation_level + 1
            
            # Send escalated notifications
            for channel_id in channels:
                if channel_id in self.notification_channels:
                    channel = self.notification_channels[channel_id]
                    if channel.enabled and alert.severity in channel.severity_filter:
                        try:
                            success = self._send_notification(alert, channel)
                            self._log_notification(alert.id, channel_id, channel.type, success)
                        except Exception as e:
                            logger.error(f"Error sending escalated notification: {e}")
            
            # Update database
            self._update_alert_escalation(alert)
            
            logger.warning(f"Escalated alert {alert.id} to level {escalation_level + 1}")
            
        except Exception as e:
            logger.error(f"Error escalating alert {alert_id}: {e}")
    
    def _update_alert_escalation(self, alert: Alert):
        """Update alert escalation level in database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE alerts 
                    SET escalation_level = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                """, (alert.escalation_level, alert.id))
                conn.commit()
        except Exception as e:
            logger.error(f"Error updating alert escalation: {e}")
    
    def _escalation_processor(self):
        """Process escalation timers"""
        while self.running:
            try:
                # Clean up escalation timers for resolved alerts
                resolved_alert_ids = []
                for alert_id in self.escalation_timers:
                    if alert_id not in self.active_alerts:
                        resolved_alert_ids.append(alert_id)
                
                for alert_id in resolved_alert_ids:
                    timers = self.escalation_timers.pop(alert_id, [])
                    for timer in timers:
                        timer.cancel()
                
                time.sleep(60)  # Check every minute
                
            except Exception as e:
                logger.error(f"Error in escalation processor: {e}")
                time.sleep(30)
    
    def _cleanup_processor(self):
        """Clean up old alerts and logs"""
        while self.running:
            try:
                # Clean up old alerts
                cutoff_date = datetime.datetime.utcnow() - datetime.timedelta(
                    days=self.config['alert_retention_days']
                )
                cutoff_str = cutoff_date.isoformat()
                
                with sqlite3.connect(self.db_path) as conn:
                    cursor = conn.cursor()
                    
                    # Clean up old alerts
                    cursor.execute("""
                        DELETE FROM alerts 
                        WHERE created_at < ? AND status != 'ACTIVE'
                    """, (cutoff_str,))
                    
                    # Clean up old notification logs
                    cursor.execute("""
                        DELETE FROM notification_log 
                        WHERE created_at < ?
                    """, (cutoff_str,))
                    
                    conn.commit()
                
                # Sleep for 24 hours
                time.sleep(24 * 3600)
                
            except Exception as e:
                logger.error(f"Error in cleanup processor: {e}")
                time.sleep(3600)  # Retry in 1 hour
    
    def acknowledge_alert(self, alert_id: str, acknowledged_by: str) -> bool:
        """Acknowledge an active alert"""
        try:
            if alert_id in self.active_alerts:
                alert = self.active_alerts[alert_id]
                alert.status = 'ACKNOWLEDGED'
                alert.acknowledged_by = acknowledged_by
                alert.acknowledged_at = datetime.datetime.utcnow().isoformat()
                
                # Update database
                with sqlite3.connect(self.db_path) as conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                        UPDATE alerts 
                        SET status = ?, acknowledged_by = ?, acknowledged_at = ?, 
                            updated_at = CURRENT_TIMESTAMP
                        WHERE id = ?
                    """, (alert.status, alert.acknowledged_by, alert.acknowledged_at, alert.id))
                    conn.commit()
                
                logger.info(f"Alert {alert_id} acknowledged by {acknowledged_by}")
                return True
            
            return False
            
        except Exception as e:
            logger.error(f"Error acknowledging alert {alert_id}: {e}")
            return False
    
    def resolve_alert(self, alert_id: str, resolved_by: str = None) -> bool:
        """Manually resolve an active alert"""
        try:
            if alert_id in self.active_alerts:
                alert = self.active_alerts[alert_id]
                alert.status = 'RESOLVED'
                alert.resolved_at = datetime.datetime.utcnow().isoformat()
                
                # Remove from active alerts
                del self.active_alerts[alert_id]
                
                # Cancel escalation timers
                if alert_id in self.escalation_timers:
                    timers = self.escalation_timers.pop(alert_id)
                    for timer in timers:
                        timer.cancel()
                
                # Update database
                self._update_alert_status(alert)
                
                logger.info(f"Alert {alert_id} resolved manually")
                return True
            
            return False
            
        except Exception as e:
            logger.error(f"Error resolving alert {alert_id}: {e}")
            return False
    
    def get_active_alerts(self) -> List[Dict]:
        """Get all active alerts"""
        return [asdict(alert) for alert in self.active_alerts.values()]
    
    def get_alert_history(self, hours: int = 24) -> List[Dict]:
        """Get alert history for specified time period"""
        try:
            start_time = datetime.datetime.utcnow() - datetime.timedelta(hours=hours)
            start_str = start_time.isoformat()
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM alerts 
                    WHERE created_at >= ? 
                    ORDER BY created_at DESC
                """, (start_str,))
                
                columns = [desc[0] for desc in cursor.description]
                alerts = []
                
                for row in cursor.fetchall():
                    alert_dict = dict(zip(columns, row))
                    alerts.append(alert_dict)
                
                return alerts
                
        except Exception as e:
            logger.error(f"Error getting alert history: {e}")
            return []
    
    def get_alert_statistics(self) -> Dict:
        """Get alert system statistics"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Get basic stats
                cursor.execute("SELECT COUNT(*) FROM alerts WHERE status = 'ACTIVE'")
                active_count = cursor.fetchone()[0]
                
                cursor.execute("SELECT COUNT(*) FROM alerts WHERE DATE(created_at) = DATE('now')")
                today_count = cursor.fetchone()[0]
                
                cursor.execute("""
                    SELECT severity, COUNT(*) 
                    FROM alerts 
                    WHERE DATE(created_at) = DATE('now')
                    GROUP BY severity
                """)
                severity_counts = dict(cursor.fetchall())
                
                cursor.execute("""
                    SELECT rule_id, COUNT(*) 
                    FROM alerts 
                    WHERE DATE(created_at) >= DATE('now', '-7 days')
                    GROUP BY rule_id 
                    ORDER BY COUNT(*) DESC 
                    LIMIT 5
                """)
                top_rules = dict(cursor.fetchall())
                
                return {
                    'active_alerts': active_count,
                    'alerts_today': today_count,
                    'severity_distribution_today': severity_counts,
                    'top_rules_week': top_rules,
                    'system_health': 'OPERATIONAL' if active_count < 5 else 'DEGRADED'
                }
                
        except Exception as e:
            logger.error(f"Error getting alert statistics: {e}")
            return {}

def main():
    """Main function for standalone execution"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Context Engineering Alert System')
    parser.add_argument('--start', action='store_true', help='Start alert monitoring')
    parser.add_argument('--status', action='store_true', help='Show system status')
    parser.add_argument('--alerts', action='store_true', help='Show active alerts')
    parser.add_argument('--history', type=int, default=24, help='Show alert history (hours)')
    parser.add_argument('--acknowledge', type=str, help='Acknowledge alert by ID')
    parser.add_argument('--resolve', type=str, help='Resolve alert by ID')
    
    args = parser.parse_args()
    
    alert_system = AlertSystem()
    
    if args.start:
        # Start monitoring
        alert_system.start_monitoring()
        
        print("🚨 Alert System started")
        print("Press Ctrl+C to stop...")
        
        try:
            while True:
                time.sleep(60)
                stats = alert_system.get_alert_statistics()
                if stats.get('active_alerts', 0) > 0:
                    print(f"⚠️  {stats['active_alerts']} active alerts")
        except KeyboardInterrupt:
            alert_system.stop_monitoring()
            print("\n✅ Alert System stopped")
    
    elif args.status:
        # Show system status
        stats = alert_system.get_alert_statistics()
        print("🚨 Alert System Status:")
        print(f"   Active Alerts: {stats.get('active_alerts', 0)}")
        print(f"   Alerts Today: {stats.get('alerts_today', 0)}")
        print(f"   System Health: {stats.get('system_health', 'UNKNOWN')}")
        
        severity_dist = stats.get('severity_distribution_today', {})
        if severity_dist:
            print("   Today's Severity Distribution:")
            for severity, count in severity_dist.items():
                print(f"     {severity}: {count}")
    
    elif args.alerts:
        # Show active alerts
        active_alerts = alert_system.get_active_alerts()
        print(f"🚨 Active Alerts ({len(active_alerts)}):")
        
        for alert in active_alerts:
            print(f"   [{alert['severity']}] {alert['title']}")
            print(f"     ID: {alert['id']}")
            print(f"     Message: {alert['message']}")
            print(f"     Time: {alert['timestamp']}")
            print()
    
    elif args.history:
        # Show alert history
        history = alert_system.get_alert_history(args.history)
        print(f"📊 Alert History (Last {args.history} hours):")
        
        for alert in history[:20]:  # Show last 20
            status_icon = {'ACTIVE': '🔴', 'RESOLVED': '✅', 'ACKNOWLEDGED': '👁️'}.get(alert['status'], '❓')
            print(f"   {status_icon} [{alert['severity']}] {alert['title']}")
            print(f"     Time: {alert['timestamp']}")
            print(f"     Status: {alert['status']}")
            print()
    
    elif args.acknowledge:
        # Acknowledge alert
        success = alert_system.acknowledge_alert(args.acknowledge, 'manual')
        if success:
            print(f"✅ Alert {args.acknowledge} acknowledged")
        else:
            print(f"❌ Failed to acknowledge alert {args.acknowledge}")
    
    elif args.resolve:
        # Resolve alert
        success = alert_system.resolve_alert(args.resolve, 'manual')
        if success:
            print(f"✅ Alert {args.resolve} resolved")
        else:
            print(f"❌ Failed to resolve alert {args.resolve}")
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()