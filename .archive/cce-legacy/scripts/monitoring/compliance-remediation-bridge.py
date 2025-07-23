#!/usr/bin/env python3
"""
Compliance Remediation Bridge - Context Engineering
MANDATORY: Automated bridge between P55/P56 detection and remediation systems
Implements Phase 3: Detection→Remediation→Alerting Integration

CRITICAL REQUIREMENTS:
- Real-time compliance monitoring integration
- Automated remediation trigger on violations
- Escalation for failed remediation attempts
- Success/failure alerting with metrics
- Zero-downtime operation

REMEDIATION TRIGGERS:
1. Script Execution Gap (≥95% threshold violation)
2. Mandatory Script Compliance (≥95% threshold violation)
3. Transparency Compliance (≥90% threshold violation)
4. Tool Call Execution (≥80% threshold violation)
5. Real Work Ratio (≥70% threshold violation)

INTEGRATION POINTS:
- Enhanced P55/P56 Monitor → This Bridge → Automated Remediation Framework
- This Bridge → Real-time Alert System → Dashboard/Notifications
- Failed Remediation → Escalation Protocol → Manual Intervention Queue
"""

import os
import json
import time
import subprocess
import threading
import sqlite3
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
import schedule
import signal
import atexit
from collections import defaultdict, deque
import hashlib

# Import existing systems
import sys
sys.path.append(str(Path(__file__).parent))

try:
    from automated_remediation_framework import AutomatedRemediationFramework, auto_remediate_violations
    from real_time_governance_alerts import RealTimeAlertSystem, send_governance_alert
except ImportError:
    print("⚠️  Warning: Automated systems not available, running in monitoring-only mode")
    AutomatedRemediationFramework = None
    RealTimeAlertSystem = None

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent.parent
BRIDGE_CONFIG = PROJECT_ROOT / 'scripts/governance/bridge-config.json'
BRIDGE_DB = PROJECT_ROOT / 'scripts/results/governance/compliance-bridge.db'
BRIDGE_LOG = PROJECT_ROOT / 'scripts/results/governance/compliance-bridge.log'
MONITORING_RESULTS = PROJECT_ROOT / 'scripts/results/compliance/enhanced'
REMEDIATION_QUEUE = PROJECT_ROOT / 'scripts/results/governance/remediation-queue'
ESCALATION_QUEUE = PROJECT_ROOT / 'scripts/results/governance/escalation-queue'

# Monitoring configuration
MONITORING_INTERVAL = 300  # 5 minutes
REMEDIATION_TIMEOUT = 600  # 10 minutes
MAX_REMEDIATION_ATTEMPTS = 3
ESCALATION_THRESHOLD = 2  # Failed remediation attempts before escalation
COMPLIANCE_HISTORY_DAYS = 7

# Compliance thresholds (from enhanced monitor)
COMPLIANCE_THRESHOLDS = {
    'tool_call_execution_minimum': 0.80,
    'real_work_minimum': 0.70,
    'script_execution_minimum': 0.95,
    'mandatory_script_minimum': 0.95,
    'command_integration_minimum': 0.80,
    'transparency_minimum': 0.90
}

# Violation severity mapping
VIOLATION_SEVERITY_MAP = {
    'script_execution_compliant': 'critical',      # Script execution is core to P55
    'mandatory_script_compliant': 'critical',     # Mandatory scripts are core to system
    'transparency_compliant': 'high',             # P56 transparency important for auditing
    'command_integration_compliant': 'warning',   # Integration affects efficiency
    'tool_call_compliant': 'emergency',           # Tool calls are fundamental
    'real_work_compliant': 'emergency'            # Real work ratio is fundamental
}

# Logging configuration
os.makedirs(BRIDGE_LOG.parent, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(BRIDGE_LOG),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class ComplianceViolation:
    """Compliance violation data structure"""
    id: str
    timestamp: datetime
    violation_type: str
    severity: str
    current_value: float
    threshold_value: float
    compliance_factor: str
    gap_size: float
    source_report: str
    remediation_attempts: int = 0
    remediation_status: str = 'pending'  # pending, in_progress, completed, failed, escalated
    last_remediation_attempt: Optional[datetime] = None
    escalated_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None

@dataclass
class RemediationRequest:
    """Remediation request data structure"""
    id: str
    timestamp: datetime
    violations: List[ComplianceViolation]
    priority: str  # low, medium, high, critical, emergency
    estimated_time: float
    auto_approved: bool
    assigned_remediator: str  # 'automated', 'manual', 'escalated'
    status: str = 'queued'  # queued, processing, completed, failed, cancelled

@dataclass
class EscalationItem:
    """Escalation item for manual intervention"""
    id: str
    timestamp: datetime
    violation: ComplianceViolation
    remediation_attempts: List[Dict[str, Any]]
    reason: str
    severity: str
    manual_intervention_required: str
    status: str = 'pending'  # pending, assigned, in_progress, resolved

class ComplianceRemediationBridge:
    """Bridge between compliance detection and automated remediation"""
    
    def __init__(self):
        self.running = False
        self.monitoring_thread = None
        self.remediation_thread = None
        
        # System components
        self.remediation_framework = None
        self.alert_system = None
        
        # Operational data
        self.compliance_history = deque(maxlen=1000)
        self.active_violations = {}
        self.remediation_queue = deque()
        self.escalation_queue = deque()
        
        # Statistics
        self.stats = {
            'monitoring_cycles': 0,
            'violations_detected': 0,
            'remediations_attempted': 0,
            'remediations_successful': 0,
            'remediations_failed': 0,
            'escalations_created': 0,
            'avg_detection_time': 0.0,
            'avg_remediation_time': 0.0
        }
        
        self.init_directories()
        self.init_database()
        self.load_configuration()
        self.init_external_systems()
        
        # Register cleanup
        atexit.register(self.cleanup)
        signal.signal(signal.SIGTERM, self._signal_handler)
        signal.signal(signal.SIGINT, self._signal_handler)
    
    def init_directories(self):
        """Initialize bridge directories"""
        for directory in [BRIDGE_DB.parent, REMEDIATION_QUEUE, ESCALATION_QUEUE]:
            os.makedirs(directory, exist_ok=True)
    
    def init_database(self):
        """Initialize compliance bridge database"""
        try:
            with sqlite3.connect(BRIDGE_DB) as conn:
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS compliance_violations (
                        id TEXT PRIMARY KEY,
                        timestamp TEXT NOT NULL,
                        violation_type TEXT NOT NULL,
                        severity TEXT NOT NULL,
                        current_value REAL NOT NULL,
                        threshold_value REAL NOT NULL,
                        compliance_factor TEXT NOT NULL,
                        gap_size REAL NOT NULL,
                        source_report TEXT NOT NULL,
                        remediation_attempts INTEGER DEFAULT 0,
                        remediation_status TEXT DEFAULT 'pending',
                        last_remediation_attempt TEXT,
                        escalated_at TEXT,
                        resolved_at TEXT
                    )
                ''')
                
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS remediation_requests (
                        id TEXT PRIMARY KEY,
                        timestamp TEXT NOT NULL,
                        violations TEXT NOT NULL,
                        priority TEXT NOT NULL,
                        estimated_time REAL NOT NULL,
                        auto_approved BOOLEAN NOT NULL,
                        assigned_remediator TEXT NOT NULL,
                        status TEXT DEFAULT 'queued'
                    )
                ''')
                
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS escalation_items (
                        id TEXT PRIMARY KEY,
                        timestamp TEXT NOT NULL,
                        violation_id TEXT NOT NULL,
                        remediation_attempts TEXT NOT NULL,
                        reason TEXT NOT NULL,
                        severity TEXT NOT NULL,
                        manual_intervention_required TEXT NOT NULL,
                        status TEXT DEFAULT 'pending',
                        FOREIGN KEY (violation_id) REFERENCES compliance_violations (id)
                    )
                ''')
                
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS bridge_metrics (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp TEXT NOT NULL,
                        monitoring_cycles INTEGER NOT NULL,
                        violations_detected INTEGER NOT NULL,
                        remediations_attempted INTEGER NOT NULL,
                        remediations_successful INTEGER NOT NULL,
                        remediations_failed INTEGER NOT NULL,
                        escalations_created INTEGER NOT NULL,
                        avg_detection_time REAL NOT NULL,
                        avg_remediation_time REAL NOT NULL
                    )
                ''')
                
                conn.commit()
                logger.info("Compliance bridge database initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize bridge database: {e}")
            raise
    
    def load_configuration(self):
        """Load bridge configuration"""
        try:
            if BRIDGE_CONFIG.exists():
                with open(BRIDGE_CONFIG, 'r') as f:
                    config = json.load(f)
                    
                # Update configuration with loaded values
                global MONITORING_INTERVAL, REMEDIATION_TIMEOUT, MAX_REMEDIATION_ATTEMPTS
                MONITORING_INTERVAL = config.get('monitoring_interval', MONITORING_INTERVAL)
                REMEDIATION_TIMEOUT = config.get('remediation_timeout', REMEDIATION_TIMEOUT)
                MAX_REMEDIATION_ATTEMPTS = config.get('max_remediation_attempts', MAX_REMEDIATION_ATTEMPTS)
                
                logger.info("Bridge configuration loaded successfully")
            else:
                self._create_default_configuration()
        except Exception as e:
            logger.error(f"Failed to load bridge configuration: {e}")
            self._create_default_configuration()
    
    def _create_default_configuration(self):
        """Create default bridge configuration"""
        default_config = {
            "monitoring_interval": MONITORING_INTERVAL,
            "remediation_timeout": REMEDIATION_TIMEOUT,
            "max_remediation_attempts": MAX_REMEDIATION_ATTEMPTS,
            "escalation_threshold": ESCALATION_THRESHOLD,
            "compliance_thresholds": COMPLIANCE_THRESHOLDS,
            "violation_severity_map": VIOLATION_SEVERITY_MAP,
            "auto_remediation": {
                "enabled": True,
                "max_concurrent": 3,
                "timeout_per_action": 300,
                "confidence_threshold": 0.80
            },
            "alerting": {
                "enabled": True,
                "immediate_alert_severities": ["critical", "emergency"],
                "daily_summary": True,
                "escalation_alerts": True
            },
            "monitoring": {
                "compliance_history_retention_days": COMPLIANCE_HISTORY_DAYS,
                "monitoring_source": str(MONITORING_RESULTS),
                "report_pattern": "enhanced-p55-p56-report-*.json"
            }
        }
        
        with open(BRIDGE_CONFIG, 'w') as f:
            json.dump(default_config, f, indent=2)
        
        logger.info("Default bridge configuration created")
    
    def init_external_systems(self):
        """Initialize external system connections"""
        try:
            # Initialize remediation framework
            if AutomatedRemediationFramework:
                self.remediation_framework = AutomatedRemediationFramework()
                logger.info("Automated remediation framework initialized")
            else:
                logger.warning("Automated remediation framework not available")
            
            # Initialize alert system
            if RealTimeAlertSystem:
                self.alert_system = RealTimeAlertSystem()
                logger.info("Real-time alert system initialized")
            else:
                logger.warning("Real-time alert system not available")
                
        except Exception as e:
            logger.error(f"Failed to initialize external systems: {e}")
    
    def start_monitoring(self):
        """Start compliance monitoring and remediation bridge"""
        if self.running:
            logger.warning("Bridge already running")
            return
        
        self.running = True
        logger.info("Starting compliance remediation bridge")
        
        # Start monitoring thread
        self.monitoring_thread = threading.Thread(target=self._monitoring_loop, daemon=True)
        self.monitoring_thread.start()
        
        # Start remediation processing thread
        self.remediation_thread = threading.Thread(target=self._remediation_loop, daemon=True)
        self.remediation_thread.start()
        
        # Schedule periodic tasks
        schedule.every(MONITORING_INTERVAL).seconds.do(self._check_compliance)
        schedule.every(1).hours.do(self._process_escalations)
        schedule.every(24).hours.do(self._generate_daily_summary)
        schedule.every(7).days.do(self._cleanup_old_data)
        
        logger.info("Compliance remediation bridge started successfully")
    
    def stop_monitoring(self):
        """Stop compliance monitoring and remediation bridge"""
        self.running = False
        logger.info("Stopping compliance remediation bridge")
    
    def _monitoring_loop(self):
        """Main monitoring loop"""
        while self.running:
            try:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
            except Exception as e:
                logger.error(f"Error in monitoring loop: {e}")
                time.sleep(60)
    
    def _remediation_loop(self):
        """Process remediation queue"""
        while self.running:
            try:
                if self.remediation_queue:
                    request = self.remediation_queue.popleft()
                    self._process_remediation_request(request)
                else:
                    time.sleep(30)  # Check every 30 seconds
            except Exception as e:
                logger.error(f"Error in remediation loop: {e}")
                time.sleep(30)
    
    def _check_compliance(self):
        """Check compliance status and trigger remediation if needed"""
        try:
            start_time = time.time()
            logger.info("Checking compliance status...")
            
            # Find most recent compliance report
            latest_report = self._get_latest_compliance_report()
            if not latest_report:
                logger.warning("No compliance reports found")
                return
            
            # Parse compliance data
            violations = self._analyze_compliance_report(latest_report)
            
            if violations:
                logger.warning(f"Found {len(violations)} compliance violations")
                
                # Send immediate alerts for critical violations
                self._send_violation_alerts(violations)
                
                # Create remediation requests
                self._create_remediation_requests(violations)
                
                # Update statistics
                self.stats['violations_detected'] += len(violations)
            else:
                logger.info("All compliance checks passed")
            
            self.stats['monitoring_cycles'] += 1
            self.stats['avg_detection_time'] = time.time() - start_time
            
            # Store metrics
            self._store_bridge_metrics()
            
        except Exception as e:
            logger.error(f"Failed to check compliance: {e}")
    
    def _get_latest_compliance_report(self) -> Optional[Path]:
        """Get the most recent compliance report"""
        try:
            report_files = list(MONITORING_RESULTS.glob("enhanced-p55-p56-report-*.json"))
            if not report_files:
                return None
            
            # Sort by modification time and get the latest
            latest_report = max(report_files, key=lambda f: f.stat().st_mtime)
            
            # Check if report is recent (within last hour)
            file_age = time.time() - latest_report.stat().st_mtime
            if file_age > 3600:  # 1 hour
                logger.warning(f"Latest compliance report is {file_age/60:.1f} minutes old")
            
            return latest_report
            
        except Exception as e:
            logger.error(f"Failed to get latest compliance report: {e}")
            return None
    
    def _analyze_compliance_report(self, report_file: Path) -> List[ComplianceViolation]:
        """Analyze compliance report and identify violations"""
        try:
            with open(report_file, 'r') as f:
                report_data = json.load(f)
            
            report = report_data.get('enhanced_p55_p56_compliance_report', {})
            compliance_results = report.get('compliance_results', {})
            calculated_metrics = report.get('calculated_metrics', {})
            
            violations = []
            
            # Check each compliance factor
            compliance_checks = [
                ('tool_call_compliant', 'tool_call_execution', 'core_p55_p56', 'tool_call_execution_ratio'),
                ('real_work_compliant', 'real_work', 'core_p55_p56', 'real_work_ratio'),
                ('script_execution_compliant', 'script_execution', 'enhanced_script_metrics', 'script_execution_ratio'),
                ('mandatory_script_compliant', 'mandatory_script', 'enhanced_script_metrics', 'mandatory_script_compliance'),
                ('command_integration_compliant', 'command_integration', 'enhanced_script_metrics', 'command_integration_ratio'),
                ('transparency_compliant', 'transparency', 'transparency_metrics', 'transparency_ratio')
            ]
            
            for compliant_key, violation_type, metrics_section, ratio_key in compliance_checks:
                is_compliant = compliance_results.get(compliant_key, True)
                if not is_compliant:
                    current_value = calculated_metrics.get(metrics_section, {}).get(ratio_key, 0.0)
                    threshold_value = COMPLIANCE_THRESHOLDS.get(f"{violation_type}_minimum", 0.0)
                    gap_size = threshold_value - current_value
                    
                    violation = ComplianceViolation(
                        id=f"violation_{int(time.time() * 1000)}_{hash(violation_type) % 10000}",
                        timestamp=datetime.now(),
                        violation_type=violation_type,
                        severity=VIOLATION_SEVERITY_MAP.get(compliant_key, 'warning'),
                        current_value=current_value,
                        threshold_value=threshold_value,
                        compliance_factor=compliant_key,
                        gap_size=gap_size,
                        source_report=str(report_file.name)
                    )
                    
                    violations.append(violation)
                    
                    # Store violation in database
                    self._store_violation(violation)
                    
                    logger.warning(f"Compliance violation: {violation_type} at {current_value:.3f} "
                                 f"(threshold: {threshold_value:.3f}, gap: {gap_size:.3f})")
            
            return violations
            
        except Exception as e:
            logger.error(f"Failed to analyze compliance report: {e}")
            return []
    
    def _send_violation_alerts(self, violations: List[ComplianceViolation]):
        """Send alerts for compliance violations"""
        try:
            if not self.alert_system or not send_governance_alert:
                logger.warning("Alert system not available")
                return
            
            for violation in violations:
                # Send immediate alert for critical/emergency violations
                if violation.severity in ['critical', 'emergency']:
                    alert_title = f"COMPLIANCE VIOLATION: {violation.violation_type.replace('_', ' ').title()}"
                    alert_message = (
                        f"Compliance factor '{violation.compliance_factor}' failed validation.\n"
                        f"Current: {violation.current_value:.3f} | Required: {violation.threshold_value:.3f}\n"
                        f"Gap: {violation.gap_size:.3f} | Severity: {violation.severity.upper()}\n"
                        f"Source: {violation.source_report}"
                    )
                    
                    violation_data = {
                        'violation_id': violation.id,
                        'violation_type': violation.violation_type,
                        'current_value': violation.current_value,
                        'threshold_value': violation.threshold_value,
                        'gap_size': violation.gap_size,
                        'compliance_factor': violation.compliance_factor
                    }
                    
                    send_governance_alert(
                        alert_type='compliance_violation',
                        severity=violation.severity,
                        title=alert_title,
                        message=alert_message,
                        source='compliance_remediation_bridge',
                        file_path=violation.source_report,
                        violation_data=violation_data
                    )
                    
                    logger.info(f"Alert sent for {violation.severity} violation: {violation.violation_type}")
                
        except Exception as e:
            logger.error(f"Failed to send violation alerts: {e}")
    
    def _create_remediation_requests(self, violations: List[ComplianceViolation]):
        """Create remediation requests for violations"""
        try:
            # Group violations by priority for batch processing
            priority_groups = defaultdict(list)
            
            for violation in violations:
                priority = self._determine_remediation_priority(violation)
                priority_groups[priority].append(violation)
            
            # Create remediation requests for each priority group
            for priority, group_violations in priority_groups.items():
                request_id = f"remediation_{int(time.time() * 1000)}_{hash(str(group_violations)) % 10000}"
                
                estimated_time = self._estimate_remediation_time(group_violations)
                auto_approved = self._should_auto_approve(group_violations, priority)
                
                request = RemediationRequest(
                    id=request_id,
                    timestamp=datetime.now(),
                    violations=group_violations,
                    priority=priority,
                    estimated_time=estimated_time,
                    auto_approved=auto_approved,
                    assigned_remediator='automated' if auto_approved else 'manual'
                )
                
                # Add to remediation queue
                self.remediation_queue.append(request)
                
                # Store request in database
                self._store_remediation_request(request)
                
                logger.info(f"Created remediation request {request_id}: {priority} priority, "
                          f"{len(group_violations)} violations, auto_approved: {auto_approved}")
        
        except Exception as e:
            logger.error(f"Failed to create remediation requests: {e}")
    
    def _determine_remediation_priority(self, violation: ComplianceViolation) -> str:
        """Determine remediation priority based on violation severity and type"""
        if violation.severity == 'emergency':
            return 'emergency'
        elif violation.severity == 'critical':
            return 'critical'
        elif violation.severity == 'high':
            return 'high'
        elif violation.gap_size > 0.5:  # Large gap
            return 'medium'
        else:
            return 'low'
    
    def _estimate_remediation_time(self, violations: List[ComplianceViolation]) -> float:
        """Estimate time required for remediation"""
        base_time_map = {
            'script_execution': 300,      # 5 minutes - script infrastructure
            'mandatory_script': 180,      # 3 minutes - enable mandatory scripts
            'transparency': 120,          # 2 minutes - add transparency features
            'command_integration': 240,   # 4 minutes - bridge commands and scripts
            'tool_call_execution': 600,   # 10 minutes - fundamental system fix
            'real_work': 480              # 8 minutes - workflow optimization
        }
        
        total_time = 0
        for violation in violations:
            base_time = base_time_map.get(violation.violation_type, 300)
            # Adjust for gap size
            gap_multiplier = 1 + (violation.gap_size * 2)  # Larger gaps take longer
            total_time += base_time * gap_multiplier
        
        return total_time
    
    def _should_auto_approve(self, violations: List[ComplianceViolation], priority: str) -> bool:
        """Determine if remediation should be auto-approved"""
        # Auto-approve if all violations are automatable types
        automatable_types = {'transparency', 'command_integration'}
        
        # Auto-approve low/medium priority violations of automatable types
        if priority in ['low', 'medium']:
            return all(v.violation_type in automatable_types for v in violations)
        
        # Auto-approve high priority transparency issues
        if priority == 'high':
            return all(v.violation_type == 'transparency' for v in violations)
        
        # Critical and emergency violations require manual approval by default
        return False
    
    def _process_remediation_request(self, request: RemediationRequest):
        """Process a remediation request"""
        try:
            logger.info(f"Processing remediation request {request.id}")
            start_time = time.time()
            
            if not request.auto_approved:
                logger.info(f"Request {request.id} requires manual approval, queuing...")
                self._queue_for_manual_approval(request)
                return
            
            if not self.remediation_framework:
                logger.error("Remediation framework not available")
                self._escalate_request(request, "Remediation framework unavailable")
                return
            
            # Convert violations to remediation format
            remediation_violations = []
            for violation in request.violations:
                remediation_violations.append({
                    'violation_type': self._map_violation_to_remediation_type(violation.violation_type),
                    'file_path': self._determine_remediation_target(violation),
                    'current_value': violation.current_value,
                    'threshold_value': violation.threshold_value,
                    'description': f"{violation.violation_type} compliance gap"
                })
            
            # Execute automated remediation
            result = auto_remediate_violations(remediation_violations, auto_execute=True)
            
            processing_time = time.time() - start_time
            
            if result.get('status') == 'success':
                logger.info(f"Remediation request {request.id} completed successfully in {processing_time:.1f}s")
                
                # Mark violations as resolved
                for violation in request.violations:
                    violation.resolved_at = datetime.now()
                    violation.remediation_status = 'completed'
                    self._update_violation_status(violation)
                
                # Send success alert
                self._send_remediation_success_alert(request, result, processing_time)
                
                self.stats['remediations_successful'] += 1
                
            else:
                logger.error(f"Remediation request {request.id} failed: {result.get('error')}")
                
                # Increment attempt count and check for escalation
                for violation in request.violations:
                    violation.remediation_attempts += 1
                    violation.last_remediation_attempt = datetime.now()
                    
                    if violation.remediation_attempts >= MAX_REMEDIATION_ATTEMPTS:
                        self._escalate_violation(violation, f"Failed after {MAX_REMEDIATION_ATTEMPTS} attempts")
                    else:
                        violation.remediation_status = 'failed'
                        # Re-queue for retry later
                        self.remediation_queue.append(request)
                    
                    self._update_violation_status(violation)
                
                # Send failure alert
                self._send_remediation_failure_alert(request, result)
                
                self.stats['remediations_failed'] += 1
            
            self.stats['remediations_attempted'] += 1
            self.stats['avg_remediation_time'] = processing_time
            
        except Exception as e:
            logger.error(f"Failed to process remediation request {request.id}: {e}")
            self._escalate_request(request, f"Processing error: {str(e)}")
    
    def _map_violation_to_remediation_type(self, violation_type: str) -> str:
        """Map compliance violation type to remediation type"""
        mapping = {
            'script_execution': 'compliance',
            'mandatory_script': 'compliance', 
            'transparency': 'compliance',
            'command_integration': 'performance',
            'tool_call_execution': 'performance',
            'real_work': 'performance'
        }
        return mapping.get(violation_type, 'compliance')
    
    def _determine_remediation_target(self, violation: ComplianceViolation) -> str:
        """Determine the target file/system for remediation"""
        if violation.violation_type in ['script_execution', 'mandatory_script']:
            return 'system_wide'  # System-wide script execution improvements
        elif violation.violation_type == 'transparency':
            return 'scripts/compliance/enhanced-p55-p56-monitor.sh'  # Transparency improvements
        elif violation.violation_type == 'command_integration':
            return 'docs/commands'  # Command-script integration improvements
        else:
            return 'system_wide'  # General system improvements
    
    def _escalate_violation(self, violation: ComplianceViolation, reason: str):
        """Escalate violation for manual intervention"""
        try:
            escalation_id = f"escalation_{int(time.time() * 1000)}_{hash(violation.id) % 10000}"
            
            escalation = EscalationItem(
                id=escalation_id,
                timestamp=datetime.now(),
                violation=violation,
                remediation_attempts=[],  # TODO: Collect from database
                reason=reason,
                severity=violation.severity,
                manual_intervention_required=self._generate_intervention_guide(violation)
            )
            
            self.escalation_queue.append(escalation)
            self._store_escalation(escalation)
            
            # Mark violation as escalated
            violation.escalated_at = datetime.now()
            violation.remediation_status = 'escalated'
            self._update_violation_status(violation)
            
            # Send escalation alert
            self._send_escalation_alert(escalation)
            
            self.stats['escalations_created'] += 1
            
            logger.warning(f"Violation {violation.id} escalated: {reason}")
            
        except Exception as e:
            logger.error(f"Failed to escalate violation {violation.id}: {e}")
    
    def _generate_intervention_guide(self, violation: ComplianceViolation) -> str:
        """Generate manual intervention guide for escalated violation"""
        guides = {
            'script_execution': """
MANUAL INTERVENTION REQUIRED: Script Execution Infrastructure

1. Verify script execution permissions:
   chmod +x scripts/compliance/*.sh
   chmod +x scripts/monitoring/*.py

2. Check script integration in commands:
   grep -r "scripts/" docs/commands/

3. Add script execution calls to relevant commands:
   Add explicit script execution in P55/P56 commands

4. Test script execution:
   bash scripts/compliance/enhanced-p55-p56-monitor.sh --real-time
""",
            'mandatory_script': """
MANUAL INTERVENTION REQUIRED: Mandatory Script Compliance

1. Identify mandatory script requirements:
   grep -r "MANDATORY.*script" docs/commands/

2. Create execution bridges:
   Add script calls to command implementations

3. Update command documentation:
   Document required script executions

4. Validate compliance:
   Run compliance monitor to verify improvements
""",
            'transparency': """
MANUAL INTERVENTION REQUIRED: P56 Transparency Compliance

1. Add visual announcements to commands:
   Use ╔ ║ ╚ box formatting
   Add EXECUTING/ACTIVE TOOL CALL messages

2. Update monitoring scripts:
   Add transparency logging to script outputs

3. Enhance command transparency:
   Document tool call executions clearly

4. Test transparency detection:
   Run enhanced P55/P56 monitor to verify improvements
"""
        }
        
        return guides.get(violation.violation_type, 
                         f"Manual intervention required for {violation.violation_type} compliance gap")
    
    def _send_remediation_success_alert(self, request: RemediationRequest, result: Dict, processing_time: float):
        """Send alert for successful remediation"""
        if not send_governance_alert:
            return
        
        try:
            send_governance_alert(
                alert_type='remediation_success',
                severity='info',
                title=f"Remediation Successful: {request.priority.title()} Priority",
                message=f"Successfully remediated {len(request.violations)} compliance violations in {processing_time:.1f}s",
                source='compliance_remediation_bridge',
                violation_data={
                    'request_id': request.id,
                    'violations_count': len(request.violations),
                    'processing_time': processing_time,
                    'success_rate': result.get('success_rate', 1.0)
                }
            )
        except Exception as e:
            logger.error(f"Failed to send remediation success alert: {e}")
    
    def _send_remediation_failure_alert(self, request: RemediationRequest, result: Dict):
        """Send alert for failed remediation"""
        if not send_governance_alert:
            return
        
        try:
            send_governance_alert(
                alert_type='remediation_failure',
                severity='high',
                title=f"Remediation Failed: {request.priority.title()} Priority",
                message=f"Failed to remediate {len(request.violations)} compliance violations: {result.get('error', 'Unknown error')}",
                source='compliance_remediation_bridge',
                violation_data={
                    'request_id': request.id,
                    'violations_count': len(request.violations),
                    'error': result.get('error'),
                    'status': result.get('status')
                }
            )
        except Exception as e:
            logger.error(f"Failed to send remediation failure alert: {e}")
    
    def _send_escalation_alert(self, escalation: EscalationItem):
        """Send alert for escalated violation"""
        if not send_governance_alert:
            return
        
        try:
            send_governance_alert(
                alert_type='compliance_escalation',
                severity='critical',
                title=f"Manual Intervention Required: {escalation.violation.violation_type}",
                message=f"Violation escalated after failed remediation attempts: {escalation.reason}",
                source='compliance_remediation_bridge',
                violation_data={
                    'escalation_id': escalation.id,
                    'violation_id': escalation.violation.id,
                    'violation_type': escalation.violation.violation_type,
                    'gap_size': escalation.violation.gap_size,
                    'manual_intervention_guide': escalation.manual_intervention_required
                }
            )
        except Exception as e:
            logger.error(f"Failed to send escalation alert: {e}")
    
    def _store_violation(self, violation: ComplianceViolation):
        """Store violation in database"""
        try:
            with sqlite3.connect(BRIDGE_DB) as conn:
                conn.execute('''
                    INSERT OR REPLACE INTO compliance_violations (
                        id, timestamp, violation_type, severity, current_value,
                        threshold_value, compliance_factor, gap_size, source_report,
                        remediation_attempts, remediation_status, last_remediation_attempt,
                        escalated_at, resolved_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    violation.id,
                    violation.timestamp.isoformat(),
                    violation.violation_type,
                    violation.severity,
                    violation.current_value,
                    violation.threshold_value,
                    violation.compliance_factor,
                    violation.gap_size,
                    violation.source_report,
                    violation.remediation_attempts,
                    violation.remediation_status,
                    violation.last_remediation_attempt.isoformat() if violation.last_remediation_attempt else None,
                    violation.escalated_at.isoformat() if violation.escalated_at else None,
                    violation.resolved_at.isoformat() if violation.resolved_at else None
                ))
                conn.commit()
        except Exception as e:
            logger.error(f"Failed to store violation: {e}")
    
    def _update_violation_status(self, violation: ComplianceViolation):
        """Update violation status in database"""
        try:
            with sqlite3.connect(BRIDGE_DB) as conn:
                conn.execute('''
                    UPDATE compliance_violations 
                    SET remediation_attempts = ?, remediation_status = ?,
                        last_remediation_attempt = ?, escalated_at = ?, resolved_at = ?
                    WHERE id = ?
                ''', (
                    violation.remediation_attempts,
                    violation.remediation_status,
                    violation.last_remediation_attempt.isoformat() if violation.last_remediation_attempt else None,
                    violation.escalated_at.isoformat() if violation.escalated_at else None,
                    violation.resolved_at.isoformat() if violation.resolved_at else None,
                    violation.id
                ))
                conn.commit()
        except Exception as e:
            logger.error(f"Failed to update violation status: {e}")
    
    def _store_remediation_request(self, request: RemediationRequest):
        """Store remediation request in database"""
        try:
            with sqlite3.connect(BRIDGE_DB) as conn:
                conn.execute('''
                    INSERT INTO remediation_requests (
                        id, timestamp, violations, priority, estimated_time,
                        auto_approved, assigned_remediator, status
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    request.id,
                    request.timestamp.isoformat(),
                    json.dumps([asdict(v) for v in request.violations]),
                    request.priority,
                    request.estimated_time,
                    request.auto_approved,
                    request.assigned_remediator,
                    request.status
                ))
                conn.commit()
        except Exception as e:
            logger.error(f"Failed to store remediation request: {e}")
    
    def _store_escalation(self, escalation: EscalationItem):
        """Store escalation in database"""
        try:
            with sqlite3.connect(BRIDGE_DB) as conn:
                conn.execute('''
                    INSERT INTO escalation_items (
                        id, timestamp, violation_id, remediation_attempts,
                        reason, severity, manual_intervention_required, status
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    escalation.id,
                    escalation.timestamp.isoformat(),
                    escalation.violation.id,
                    json.dumps(escalation.remediation_attempts),
                    escalation.reason,
                    escalation.severity,
                    escalation.manual_intervention_required,
                    escalation.status
                ))
                conn.commit()
        except Exception as e:
            logger.error(f"Failed to store escalation: {e}")
    
    def _store_bridge_metrics(self):
        """Store bridge metrics in database"""
        try:
            with sqlite3.connect(BRIDGE_DB) as conn:
                conn.execute('''
                    INSERT INTO bridge_metrics (
                        timestamp, monitoring_cycles, violations_detected,
                        remediations_attempted, remediations_successful,
                        remediations_failed, escalations_created,
                        avg_detection_time, avg_remediation_time
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    datetime.now().isoformat(),
                    self.stats['monitoring_cycles'],
                    self.stats['violations_detected'],
                    self.stats['remediations_attempted'],
                    self.stats['remediations_successful'],
                    self.stats['remediations_failed'],
                    self.stats['escalations_created'],
                    self.stats['avg_detection_time'],
                    self.stats['avg_remediation_time']
                ))
                conn.commit()
        except Exception as e:
            logger.error(f"Failed to store bridge metrics: {e}")
    
    def _queue_for_manual_approval(self, request: RemediationRequest):
        """Queue request for manual approval"""
        # This would integrate with a ticket system or manual queue
        logger.info(f"Request {request.id} queued for manual approval")
        # TODO: Implement manual approval workflow
    
    def _escalate_request(self, request: RemediationRequest, reason: str):
        """Escalate entire request for manual intervention"""
        for violation in request.violations:
            self._escalate_violation(violation, reason)
    
    def _process_escalations(self):
        """Process escalation queue (periodic task)"""
        logger.info("Processing escalation queue...")
        # TODO: Implement escalation processing workflow
    
    def _generate_daily_summary(self):
        """Generate daily compliance summary"""
        logger.info("Generating daily compliance summary...")
        # TODO: Implement daily summary generation
    
    def _cleanup_old_data(self):
        """Cleanup old data (weekly task)"""
        logger.info("Cleaning up old compliance data...")
        # TODO: Implement data cleanup
    
    def cleanup(self):
        """Cleanup resources"""
        self.stop_monitoring()
    
    def _signal_handler(self, signum, frame):
        """Handle shutdown signals"""
        logger.info(f"Received signal {signum}, shutting down gracefully")
        self.cleanup()
        exit(0)

def main():
    """Main bridge execution"""
    try:
        bridge = ComplianceRemediationBridge()
        bridge.start_monitoring()
        
        print("\n" + "="*80)
        print("COMPLIANCE REMEDIATION BRIDGE ACTIVE")
        print("="*80)
        print("⚡ Real-time compliance monitoring")
        print("🔧 Automated remediation on violations") 
        print("🚨 Escalation for failed attempts")
        print("📊 Dashboard integration")
        print("="*80)
        print("\nPress Ctrl+C to stop...")
        
        # Keep running
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        logger.info("Bridge stopped by user")
    except Exception as e:
        logger.error(f"Bridge failed: {e}")
        raise

if __name__ == "__main__":
    main()