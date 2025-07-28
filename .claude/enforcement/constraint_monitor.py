#!/usr/bin/env python3
"""
BEHAVIORAL CONSTRAINT MONITORING SYSTEM

AUTHORITY: User Vision - Real-time enforcement of orchestration constraints
PURPOSE: Active monitoring and prevention of main agent behavioral violations
INTEGRATION: Health monitoring system + violation logging + automatic correction

PRINCIPLE: "la manera principal en la que se tiene que comportar el agente principal 
           SIEMPRE es la de ser orquestado de subagentes" - ZERO EXCEPTIONS
"""

import json
import datetime
import time
import threading
import sqlite3
import os
import sys
from typing import Dict, Any, List, Optional, Callable
from pathlib import Path
import logging
from dataclasses import dataclass
from enum import Enum

class ViolationSeverity(Enum):
    """Violation severity levels for enforcement escalation."""
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"
    ABSOLUTE = "ABSOLUTE"

@dataclass
class ConstraintViolation:
    """Structured representation of behavioral constraint violation."""
    timestamp: str
    violation_type: str
    severity: ViolationSeverity
    operation_attempted: str
    context: Dict[str, Any]
    user_authority: str
    enforcement_action: str
    prevention_applied: bool

class BehavioralConstraintMonitor:
    """
    Real-time monitoring system for behavioral constraint enforcement.
    
    MONITORING SCOPE:
    - Pre-execution validation of all operations
    - Real-time detection of direct work attempts
    - Automatic prevention and redirection
    - Continuous compliance verification
    - Health system integration
    """
    
    def __init__(self, project_root: str = "/Users/nalve/ce-simple"):
        self.project_root = Path(project_root)
        self.monitor_db = self.project_root / ".claude" / "enforcement" / "monitor.db"
        self.active_monitoring = True
        self.violation_callbacks: List[Callable] = []
        
        # Ensure monitoring directory exists
        self.monitor_db.parent.mkdir(parents=True, exist_ok=True)
        
        # Initialize monitoring database
        self._init_monitor_db()
        
        # Configure logging
        self._setup_logging()
        
        # Load user vision constraints
        self.user_constraints = self._load_user_constraints()
        
        # Start monitoring thread
        self.monitor_thread = None
        self.start_monitoring()
    
    def _init_monitor_db(self) -> None:
        """Initialize SQLite database for real-time monitoring."""
        conn = sqlite3.connect(self.monitor_db)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS constraint_violations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                violation_type TEXT NOT NULL,
                severity TEXT NOT NULL,
                operation_attempted TEXT NOT NULL,
                context_data TEXT NOT NULL,
                user_authority TEXT NOT NULL,
                enforcement_action TEXT NOT NULL,
                prevention_applied BOOLEAN NOT NULL,
                resolved BOOLEAN DEFAULT FALSE
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS monitoring_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                event_type TEXT NOT NULL,
                agent_role TEXT NOT NULL,
                operation_type TEXT NOT NULL,
                compliance_status TEXT NOT NULL,
                details TEXT
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS enforcement_actions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                violation_id INTEGER,
                action_type TEXT NOT NULL,
                action_details TEXT NOT NULL,
                success BOOLEAN NOT NULL,
                FOREIGN KEY (violation_id) REFERENCES constraint_violations (id)
            )
        """)
        
        conn.commit()
        conn.close()
    
    def _setup_logging(self) -> None:
        """Configure logging for constraint monitoring."""
        log_path = self.project_root / ".claude" / "enforcement" / "monitor.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_path),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger("BehavioralConstraintMonitor")
    
    def _load_user_constraints(self) -> Dict[str, Any]:
        """Load user vision behavioral constraints from authentic sources."""
        return {
            "orchestration_requirement": {
                "quote": "la manera principal en la que se tiene que comportar el agente principal SIEMPRE es la de ser orquestado de subagentes, es utilizar la task tool de claude code para hcer el despliegue de subagentes especializados para cada una de las tareas que debe de hacer.",
                "authority": "ULTIMATE",
                "enforcement": "ABSOLUTE",
                "exceptions": 0
            },
            "forbidden_behaviors": [
                "DIRECT_ANALYSIS",
                "DIRECT_RESEARCH", 
                "DIRECT_IMPLEMENTATION",
                "DIRECT_CODING",
                "DIRECT_PROBLEM_SOLVING",
                "DIRECT_CONTENT_CREATION",
                "DIRECT_TECHNICAL_WORK"
            ],
            "required_behaviors": [
                "TASK_TOOL_DEPLOYMENT",
                "SUBAGENT_COORDINATION", 
                "DELEGATION_ORCHESTRATION",
                "MONITORING_ONLY"
            ]
        }
    
    def start_monitoring(self) -> None:
        """Start real-time behavioral constraint monitoring."""
        if self.monitor_thread and self.monitor_thread.is_alive():
            return
            
        self.active_monitoring = True
        self.monitor_thread = threading.Thread(target=self._monitoring_loop, daemon=True)
        self.monitor_thread.start()
        
        self.logger.info("Behavioral constraint monitoring started")
    
    def stop_monitoring(self) -> None:
        """Stop real-time monitoring."""
        self.active_monitoring = False
        if self.monitor_thread:
            self.monitor_thread.join()
            
        self.logger.info("Behavioral constraint monitoring stopped")
    
    def _monitoring_loop(self) -> None:
        """Main monitoring loop for real-time constraint enforcement."""
        while self.active_monitoring:
            try:
                # Check for ongoing violations
                self._check_active_violations()
                
                # Verify system compliance
                self._verify_system_compliance()
                
                # Update health monitoring integration
                self._update_health_integration()
                
                # Sleep before next check
                time.sleep(1)  # 1-second monitoring interval
                
            except Exception as e:
                self.logger.error(f"Monitoring loop error: {str(e)}")
                time.sleep(5)  # Longer sleep on error
    
    def validate_operation(self, agent_role: str, operation_type: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Real-time validation of agent operations against behavioral constraints.
        
        Args:
            agent_role: Role of agent attempting operation (MAIN_AGENT, SUBAGENT)
            operation_type: Type of operation being attempted
            context: Operation context and metadata
            
        Returns:
            Validation result with enforcement actions if needed
        """
        timestamp = datetime.datetime.now().isoformat()
        
        # Record monitoring event
        self._record_monitoring_event(timestamp, agent_role, operation_type, context)
        
        # Check for violations
        violation = self._detect_violation(agent_role, operation_type, context)
        
        if violation:
            # VIOLATION DETECTED - Apply enforcement
            violation_record = ConstraintViolation(
                timestamp=timestamp,
                violation_type=violation["type"],
                severity=ViolationSeverity(violation["severity"]),
                operation_attempted=operation_type,
                context=context,
                user_authority=self.user_constraints["orchestration_requirement"]["quote"],
                enforcement_action=violation["enforcement_action"],
                prevention_applied=True
            )
            
            # Log violation
            self._record_violation(violation_record)
            
            # Apply enforcement action
            enforcement_result = self._apply_enforcement_action(violation_record)
            
            # Notify violation callbacks
            self._notify_violation_callbacks(violation_record)
            
            return {
                "status": "BLOCKED",
                "violation": violation_record,
                "enforcement": enforcement_result,
                "message": self._generate_violation_message(violation_record)
            }
        
        else:
            # COMPLIANT OPERATION
            return {
                "status": "ALLOWED",
                "timestamp": timestamp,
                "compliance_verified": True
            }
    
    def _detect_violation(self, agent_role: str, operation_type: str, context: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Detect behavioral constraint violations in real-time."""
        
        # Check if main agent is attempting forbidden direct work
        if agent_role == "MAIN_AGENT":
            forbidden_operations = self.user_constraints["forbidden_behaviors"]
            
            if operation_type in forbidden_operations:
                return {
                    "type": "DIRECT_WORK_ATTEMPT",
                    "severity": "CRITICAL",
                    "enforcement_action": "BLOCK_AND_REDIRECT_TO_TASK_TOOLS"
                }
            
            # Check if operation requires specialization but no Task tool is being used
            if context.get("requires_specialization", False) and not context.get("using_task_tools", False):
                return {
                    "type": "MISSING_TASK_TOOL_DELEGATION",
                    "severity": "CRITICAL", 
                    "enforcement_action": "BLOCK_AND_REQUIRE_TASK_TOOL_DEPLOYMENT"
                }
            
            # Check for implicit direct work patterns
            direct_work_indicators = ["file_editing", "content_creation", "analysis", "research", "implementation"]
            if any(indicator in str(context).lower() for indicator in direct_work_indicators):
                if not context.get("delegated_via_task_tool", False):
                    return {
                        "type": "IMPLICIT_DIRECT_WORK",
                        "severity": "HIGH",
                        "enforcement_action": "BLOCK_AND_REQUIRE_DELEGATION"
                    }
        
        return None
    
    def _record_violation(self, violation: ConstraintViolation) -> None:
        """Record violation in monitoring database."""
        conn = sqlite3.connect(self.monitor_db)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO constraint_violations (
                timestamp, violation_type, severity, operation_attempted,
                context_data, user_authority, enforcement_action, prevention_applied
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            violation.timestamp,
            violation.violation_type,
            violation.severity.value,
            violation.operation_attempted,
            json.dumps(violation.context),
            violation.user_authority,
            violation.enforcement_action,
            violation.prevention_applied
        ))
        
        conn.commit()
        conn.close()
        
        self.logger.critical(f"Behavioral constraint violation: {violation.violation_type}")
    
    def _record_monitoring_event(self, timestamp: str, agent_role: str, operation_type: str, context: Dict[str, Any]) -> None:
        """Record monitoring event for audit trail."""
        conn = sqlite3.connect(self.monitor_db)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO monitoring_events (
                timestamp, event_type, agent_role, operation_type,
                compliance_status, details
            ) VALUES (?, ?, ?, ?, ?, ?)
        """, (
            timestamp,
            "OPERATION_VALIDATION",
            agent_role,
            operation_type,
            "PENDING_VALIDATION",
            json.dumps(context)
        ))
        
        conn.commit()
        conn.close()
    
    def _apply_enforcement_action(self, violation: ConstraintViolation) -> Dict[str, Any]:
        """Apply enforcement action for detected violation."""
        action_result = {
            "action_applied": violation.enforcement_action,
            "timestamp": datetime.datetime.now().isoformat(),
            "success": True
        }
        
        # Log enforcement action
        conn = sqlite3.connect(self.monitor_db)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO enforcement_actions (
                timestamp, action_type, action_details, success
            ) VALUES (?, ?, ?, ?)
        """, (
            action_result["timestamp"],
            violation.enforcement_action,
            json.dumps(violation.context),
            action_result["success"]
        ))
        
        conn.commit()
        conn.close()
        
        return action_result
    
    def _generate_violation_message(self, violation: ConstraintViolation) -> str:
        """Generate detailed violation message with enforcement instructions."""
        return f"""
BEHAVIORAL CONSTRAINT VIOLATION - REAL-TIME DETECTION

USER AUTHORITY: "{violation.user_authority}"
VIOLATION TYPE: {violation.violation_type}
SEVERITY: {violation.severity.value}
OPERATION ATTEMPTED: {violation.operation_attempted}
TIMESTAMP: {violation.timestamp}

ENFORCEMENT ACTION: {violation.enforcement_action}
PREVENTION APPLIED: {violation.prevention_applied}

COMPLIANCE REQUIREMENT:
Main agent MUST ALWAYS orchestrate via subagents using Task tools.
NO EXCEPTIONS - This is an ABSOLUTE requirement.

CORRECTIVE ACTION REQUIRED:
1. Deploy specialized subagent via Task tool
2. Coordinate subagent execution
3. Monitor and report results
4. NEVER attempt direct work execution

MONITORING STATUS: Active enforcement in effect
"""
    
    def _check_active_violations(self) -> None:
        """Check for ongoing or unresolved violations."""
        conn = sqlite3.connect(self.monitor_db)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT COUNT(*) FROM constraint_violations 
            WHERE resolved = FALSE AND severity IN ('CRITICAL', 'ABSOLUTE')
        """)
        
        active_critical_violations = cursor.fetchone()[0]
        
        if active_critical_violations > 0:
            self.logger.warning(f"Active critical violations: {active_critical_violations}")
            
        conn.close()
    
    def _verify_system_compliance(self) -> None:
        """Verify overall system compliance with behavioral constraints."""
        # Check compliance metrics
        conn = sqlite3.connect(self.monitor_db)
        cursor = conn.cursor()
        
        # Get recent compliance rate
        cursor.execute("""
            SELECT compliance_status, COUNT(*) as count
            FROM monitoring_events
            WHERE timestamp > datetime('now', '-1 hour')
            GROUP BY compliance_status
        """)
        
        recent_events = dict(cursor.fetchall())
        total_recent = sum(recent_events.values())
        
        if total_recent > 0:
            violation_rate = recent_events.get("VIOLATION", 0) / total_recent
            if violation_rate > 0.1:  # More than 10% violations
                self.logger.warning(f"High violation rate detected: {violation_rate:.2%}")
        
        conn.close()
    
    def _update_health_integration(self) -> None:
        """Update health monitoring system with constraint compliance status."""
        try:
            health_status = {
                "behavioral_compliance": self._get_compliance_metrics(),
                "active_monitoring": self.active_monitoring,
                "last_update": datetime.datetime.now().isoformat()
            }
            
            health_file = self.project_root / "data" / "monitoring" / "behavioral_health.json"
            with open(health_file, "w") as f:
                json.dump(health_status, f, indent=2)
                
        except Exception as e:
            self.logger.error(f"Health integration update failed: {str(e)}")
    
    def _get_compliance_metrics(self) -> Dict[str, Any]:
        """Get current compliance metrics."""
        conn = sqlite3.connect(self.monitor_db)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT 
                COUNT(*) as total_events,
                SUM(CASE WHEN compliance_status = 'COMPLIANT' THEN 1 ELSE 0 END) as compliant_events,
                SUM(CASE WHEN compliance_status = 'VIOLATION' THEN 1 ELSE 0 END) as violations
            FROM monitoring_events
            WHERE timestamp > datetime('now', '-24 hours')
        """)
        
        metrics = cursor.fetchone()
        total, compliant, violations = metrics or (0, 0, 0)
        
        compliance_rate = compliant / total if total > 0 else 1.0
        
        conn.close()
        
        return {
            "total_events_24h": total,
            "compliant_events": compliant,
            "violations": violations,
            "compliance_rate": compliance_rate,
            "status": "HEALTHY" if compliance_rate >= 0.95 else "WARNING" if compliance_rate >= 0.8 else "CRITICAL"
        }
    
    def add_violation_callback(self, callback: Callable[[ConstraintViolation], None]) -> None:
        """Add callback to be notified of violations."""
        self.violation_callbacks.append(callback)
    
    def _notify_violation_callbacks(self, violation: ConstraintViolation) -> None:
        """Notify all registered violation callbacks."""
        for callback in self.violation_callbacks:
            try:
                callback(violation)
            except Exception as e:
                self.logger.error(f"Violation callback error: {str(e)}")

# Global monitor instance
_global_monitor = None

def get_constraint_monitor() -> BehavioralConstraintMonitor:
    """Get global constraint monitor instance."""
    global _global_monitor
    if _global_monitor is None:
        _global_monitor = BehavioralConstraintMonitor()
    return _global_monitor

def validate_agent_operation(agent_role: str, operation_type: str, **context) -> Dict[str, Any]:
    """
    Main entry point for real-time operation validation.
    
    CRITICAL: Must be called before ANY agent operation
    PURPOSE: Ensure behavioral constraint compliance in real-time
    """
    monitor = get_constraint_monitor()
    return monitor.validate_operation(agent_role, operation_type, context)

if __name__ == "__main__":
    # Test constraint monitoring
    monitor = BehavioralConstraintMonitor()
    
    # Test violation detection
    test_result = monitor.validate_operation(
        "MAIN_AGENT",
        "DIRECT_ANALYSIS",
        {"requires_specialization": True, "using_task_tools": False}
    )
    
    print(json.dumps(test_result, indent=2, default=str))
    
    # Show compliance metrics
    metrics = monitor._get_compliance_metrics()
    print("\nCompliance Metrics:")
    print(json.dumps(metrics, indent=2))