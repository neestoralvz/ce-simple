#!/usr/bin/env python3
"""
HEALTH MONITORING INTEGRATION - Continuous Behavioral Compliance Validation

AUTHORITY: User Vision + System Health Monitoring Integration
PURPOSE: Integrate behavioral enforcement with existing health monitoring system
FUNCTION: Continuous validation, alerting, and compliance tracking

INTEGRATION POINTS:
- /data/monitoring/health.db - Main health database
- /data/monitoring/health_daemon_status.json - Health daemon status
- /data/monitoring/health_monitor.log - Health monitoring logs

BEHAVIORAL METRICS:
- Orchestration compliance rate
- Task tool delegation success rate
- Main agent direct work prevention rate
- Violation frequency and patterns
"""

import json
import datetime
import sqlite3
import os
import sys
import time
import threading
from typing import Dict, Any, List, Optional, Tuple
from pathlib import Path
import logging

class HealthMonitoringIntegration:
    """
    Integrates behavioral enforcement with existing health monitoring system.
    
    INTEGRATION FEATURES:
    - Real-time behavioral compliance metrics
    - Automatic health score adjustments based on violations
    - Alert generation for behavioral constraint violations
    - Historical compliance tracking and analysis
    - Integration with existing health daemon
    """
    
    def __init__(self, project_root: str = "/Users/nalve/ce-simple"):
        self.project_root = Path(project_root)
        self.health_db = self.project_root / "data" / "monitoring" / "health.db"
        self.health_status = self.project_root / "data" / "monitoring" / "health_daemon_status.json"
        self.integration_log = self.project_root / ".claude" / "enforcement" / "health_integration.log"
        
        # Ensure directories exist
        self.integration_log.parent.mkdir(parents=True, exist_ok=True)
        self.health_db.parent.mkdir(parents=True, exist_ok=True)
        
        # Configure logging
        self._setup_logging()
        
        # Initialize health database integration
        self._init_health_integration()
        
        # Behavioral compliance metrics
        self.compliance_metrics = {
            "orchestration_compliance_rate": 1.0,
            "task_delegation_success_rate": 1.0,
            "violation_prevention_rate": 1.0,
            "behavioral_health_score": 1.0,
            "last_violation_timestamp": None,
            "total_operations_monitored": 0,
            "violations_prevented": 0
        }
        
        self.logger.info("Health monitoring integration initialized")
    
    def _setup_logging(self) -> None:
        """Configure logging for health integration."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.integration_log),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger("HealthMonitoringIntegration")
    
    def _init_health_integration(self) -> None:
        """Initialize health database integration tables."""
        try:
            conn = sqlite3.connect(self.health_db)
            cursor = conn.cursor()
            
            # Create behavioral compliance table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS behavioral_compliance (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    compliance_type TEXT NOT NULL,
                    compliance_rate REAL NOT NULL,
                    violation_count INTEGER DEFAULT 0,
                    success_count INTEGER DEFAULT 0,
                    health_impact REAL NOT NULL,
                    details TEXT
                )
            """)
            
            # Create behavioral violations table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS behavioral_violations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    violation_type TEXT NOT NULL,
                    severity TEXT NOT NULL,
                    agent_role TEXT NOT NULL,
                    operation_attempted TEXT NOT NULL,
                    prevention_applied BOOLEAN NOT NULL,
                    health_impact REAL NOT NULL,
                    user_authority TEXT NOT NULL,
                    context_data TEXT
                )
            """)
            
            # Create behavioral health metrics table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS behavioral_health_metrics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    metric_name TEXT NOT NULL,
                    metric_value REAL NOT NULL,
                    trend TEXT NOT NULL,
                    impact_on_system_health REAL NOT NULL,
                    recommendations TEXT
                )
            """)
            
            conn.commit()
            conn.close()
            
            self.logger.info("Health database integration tables initialized")
            
        except Exception as e:
            self.logger.error(f"Health database initialization failed: {str(e)}")
    
    def record_behavioral_compliance(self, compliance_data: Dict[str, Any]) -> None:
        """Record behavioral compliance event in health monitoring system."""
        try:
            timestamp = datetime.datetime.now().isoformat()
            
            conn = sqlite3.connect(self.health_db)
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT INTO behavioral_compliance (
                    timestamp, compliance_type, compliance_rate, 
                    violation_count, success_count, health_impact, details
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                timestamp,
                compliance_data.get("compliance_type", "ORCHESTRATION_COMPLIANCE"),
                compliance_data.get("compliance_rate", 1.0),
                compliance_data.get("violation_count", 0),
                compliance_data.get("success_count", 1),
                self._calculate_health_impact(compliance_data),
                json.dumps(compliance_data.get("details", {}))
            ))
            
            conn.commit()
            conn.close()
            
            # Update compliance metrics
            self._update_compliance_metrics(compliance_data)
            
            self.logger.info(f"Behavioral compliance recorded: {compliance_data.get('compliance_type')}")
            
        except Exception as e:
            self.logger.error(f"Failed to record behavioral compliance: {str(e)}")
    
    def record_behavioral_violation(self, violation_data: Dict[str, Any]) -> None:
        """Record behavioral violation in health monitoring system."""
        try:
            timestamp = datetime.datetime.now().isoformat()
            
            conn = sqlite3.connect(self.health_db)
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT INTO behavioral_violations (
                    timestamp, violation_type, severity, agent_role,
                    operation_attempted, prevention_applied, health_impact,
                    user_authority, context_data
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                timestamp,
                violation_data.get("violation_type", "UNKNOWN"),
                violation_data.get("severity", "CRITICAL"),
                violation_data.get("agent_role", "MAIN_AGENT"),
                violation_data.get("operation_attempted", "UNKNOWN"),
                violation_data.get("prevention_applied", True),
                self._calculate_violation_health_impact(violation_data),
                violation_data.get("user_authority", ""),
                json.dumps(violation_data.get("context", {}))
            ))
            
            conn.commit()
            conn.close()
            
            # Update violation metrics
            self._update_violation_metrics(violation_data)
            
            # Generate health alert
            self._generate_health_alert(violation_data)
            
            self.logger.critical(f"Behavioral violation recorded: {violation_data.get('violation_type')}")
            
        except Exception as e:
            self.logger.error(f"Failed to record behavioral violation: {str(e)}")
    
    def update_behavioral_health_metrics(self) -> Dict[str, Any]:
        """Update and calculate current behavioral health metrics."""
        try:
            timestamp = datetime.datetime.now().isoformat()
            
            # Calculate current metrics
            metrics = self._calculate_current_metrics()
            
            # Record in health database
            conn = sqlite3.connect(self.health_db)
            cursor = conn.cursor()
            
            for metric_name, metric_data in metrics.items():
                cursor.execute("""
                    INSERT INTO behavioral_health_metrics (
                        timestamp, metric_name, metric_value, trend,
                        impact_on_system_health, recommendations
                    ) VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    timestamp,
                    metric_name,
                    metric_data["value"],
                    metric_data["trend"],
                    metric_data["system_impact"],
                    json.dumps(metric_data["recommendations"])
                ))
            
            conn.commit()
            conn.close()
            
            # Update overall behavioral health score
            behavioral_health_score = self._calculate_behavioral_health_score(metrics)
            self.compliance_metrics["behavioral_health_score"] = behavioral_health_score
            
            # Update health daemon status if needed
            self._update_health_daemon_status(behavioral_health_score)
            
            return {
                "timestamp": timestamp,
                "metrics": metrics,
                "behavioral_health_score": behavioral_health_score,
                "overall_compliance": self.compliance_metrics
            }
            
        except Exception as e:
            self.logger.error(f"Failed to update behavioral health metrics: {str(e)}")
            return {"error": str(e)}
    
    def _calculate_health_impact(self, compliance_data: Dict[str, Any]) -> float:
        """Calculate health impact of compliance event."""
        compliance_rate = compliance_data.get("compliance_rate", 1.0)
        violation_count = compliance_data.get("violation_count", 0)
        
        # Positive impact for high compliance, negative for violations
        base_impact = compliance_rate * 0.1
        violation_penalty = violation_count * -0.05
        
        return max(-1.0, min(1.0, base_impact + violation_penalty))
    
    def _calculate_violation_health_impact(self, violation_data: Dict[str, Any]) -> float:
        """Calculate health impact of behavioral violation."""
        severity = violation_data.get("severity", "MEDIUM")
        prevention_applied = violation_data.get("prevention_applied", True)
        
        # Severity impact mapping
        severity_impact = {
            "LOW": -0.1,
            "MEDIUM": -0.2,
            "HIGH": -0.4,
            "CRITICAL": -0.7,
            "ABSOLUTE": -1.0
        }
        
        base_impact = severity_impact.get(severity, -0.5)
        
        # Reduction if prevention was applied
        if prevention_applied:
            base_impact *= 0.5  # 50% reduction for prevented violations
        
        return base_impact
    
    def _update_compliance_metrics(self, compliance_data: Dict[str, Any]) -> None:
        """Update internal compliance metrics."""
        self.compliance_metrics["total_operations_monitored"] += 1
        
        # Update compliance rates based on compliance data
        compliance_type = compliance_data.get("compliance_type", "ORCHESTRATION_COMPLIANCE")
        compliance_rate = compliance_data.get("compliance_rate", 1.0)
        
        if compliance_type == "ORCHESTRATION_COMPLIANCE":
            self.compliance_metrics["orchestration_compliance_rate"] = compliance_rate
        elif compliance_type == "TASK_DELEGATION":
            self.compliance_metrics["task_delegation_success_rate"] = compliance_rate
    
    def _update_violation_metrics(self, violation_data: Dict[str, Any]) -> None:
        """Update internal violation metrics."""
        self.compliance_metrics["violations_prevented"] += 1
        self.compliance_metrics["last_violation_timestamp"] = datetime.datetime.now().isoformat()
        
        # Recalculate violation prevention rate
        total_ops = self.compliance_metrics["total_operations_monitored"]
        if total_ops > 0:
            prevention_rate = self.compliance_metrics["violations_prevented"] / total_ops
            self.compliance_metrics["violation_prevention_rate"] = min(1.0, prevention_rate)
    
    def _calculate_current_metrics(self) -> Dict[str, Dict[str, Any]]:
        """Calculate current behavioral health metrics."""
        return {
            "orchestration_compliance": {
                "value": self.compliance_metrics["orchestration_compliance_rate"],
                "trend": self._calculate_trend("orchestration_compliance_rate"),
                "system_impact": 0.3,  # High impact on system health
                "recommendations": self._get_compliance_recommendations("orchestration")
            },
            "task_delegation_success": {
                "value": self.compliance_metrics["task_delegation_success_rate"],
                "trend": self._calculate_trend("task_delegation_success_rate"),
                "system_impact": 0.2,
                "recommendations": self._get_compliance_recommendations("delegation")
            },
            "violation_prevention": {
                "value": self.compliance_metrics["violation_prevention_rate"],
                "trend": self._calculate_trend("violation_prevention_rate"),
                "system_impact": 0.4,  # Very high impact
                "recommendations": self._get_compliance_recommendations("prevention")
            }
        }
    
    def _calculate_trend(self, metric_name: str) -> str:
        """Calculate trend for a specific metric (simplified)."""
        # This would normally compare recent values to determine trend
        current_value = self.compliance_metrics.get(metric_name, 1.0)
        
        if current_value >= 0.95:
            return "EXCELLENT"
        elif current_value >= 0.8:
            return "GOOD"
        elif current_value >= 0.6:
            return "DECLINING"
        else:
            return "CRITICAL"
    
    def _get_compliance_recommendations(self, compliance_area: str) -> List[str]:
        """Get recommendations for improving compliance in specific areas."""
        recommendations = {
            "orchestration": [
                "Ensure all main agent operations use Task tool delegation",
                "Review orchestration patterns for consistency",
                "Implement automatic Task tool deployment validation"
            ],
            "delegation": [
                "Verify specialized subagent configurations",
                "Optimize Task tool deployment efficiency",
                "Monitor delegation success patterns"
            ],
            "prevention": [
                "Strengthen pre-execution validation",
                "Enhance violation detection algorithms",
                "Improve automatic correction mechanisms"
            ]
        }
        
        return recommendations.get(compliance_area, ["Review behavioral compliance protocols"])
    
    def _calculate_behavioral_health_score(self, metrics: Dict[str, Dict[str, Any]]) -> float:
        """Calculate overall behavioral health score."""
        total_score = 0.0
        total_weight = 0.0
        
        for metric_name, metric_data in metrics.items():
            value = metric_data["value"]
            weight = metric_data["system_impact"]
            
            total_score += value * weight
            total_weight += weight
        
        return total_score / total_weight if total_weight > 0 else 1.0
    
    def _update_health_daemon_status(self, behavioral_health_score: float) -> None:
        """Update health daemon status with behavioral compliance information."""
        try:
            if self.health_status.exists():
                with open(self.health_status, 'r') as f:
                    status = json.load(f)
                
                # Add behavioral compliance to status
                status["behavioral_compliance"] = {
                    "health_score": behavioral_health_score,
                    "orchestration_compliance": self.compliance_metrics["orchestration_compliance_rate"],
                    "last_update": datetime.datetime.now().isoformat(),
                    "violations_prevented": self.compliance_metrics["violations_prevented"]
                }
                
                # Update overall health score to include behavioral component
                if "health_score" in status:
                    original_health = status["health_score"]
                    # Weighted combination: 70% original health, 30% behavioral health
                    combined_health = (original_health * 0.7) + (behavioral_health_score * 0.3)
                    status["health_score"] = combined_health
                
                with open(self.health_status, 'w') as f:
                    json.dump(status, f, indent=2)
                
                self.logger.info(f"Health daemon status updated with behavioral score: {behavioral_health_score:.3f}")
                
        except Exception as e:
            self.logger.error(f"Failed to update health daemon status: {str(e)}")
    
    def _generate_health_alert(self, violation_data: Dict[str, Any]) -> None:
        """Generate health monitoring alert for behavioral violations."""
        try:
            alert = {
                "timestamp": datetime.datetime.now().isoformat(),
                "type": "BEHAVIORAL_VIOLATION_ALERT",
                "severity": violation_data.get("severity", "CRITICAL"),
                "violation_type": violation_data.get("violation_type", "UNKNOWN"),
                "agent_role": violation_data.get("agent_role", "MAIN_AGENT"),
                "operation_attempted": violation_data.get("operation_attempted", "UNKNOWN"),
                "prevention_applied": violation_data.get("prevention_applied", True),
                "user_authority": violation_data.get("user_authority", ""),
                "health_impact": self._calculate_violation_health_impact(violation_data),
                "recommended_action": "Review orchestration compliance protocols"
            }
            
            # Write alert to health monitoring alerts file
            alerts_file = self.project_root / "data" / "monitoring" / "behavioral_alerts.json"
            with open(alerts_file, "a") as f:
                f.write(json.dumps(alert) + "\n")
            
            self.logger.warning(f"Health alert generated for violation: {violation_data.get('violation_type')}")
            
        except Exception as e:
            self.logger.error(f"Failed to generate health alert: {str(e)}")
    
    def get_compliance_dashboard(self) -> Dict[str, Any]:
        """Get comprehensive compliance dashboard data."""
        try:
            # Update current metrics
            current_metrics = self.update_behavioral_health_metrics()
            
            # Get historical compliance data
            conn = sqlite3.connect(self.health_db)
            cursor = conn.cursor()
            
            # Recent violations
            cursor.execute("""
                SELECT violation_type, COUNT(*) as count
                FROM behavioral_violations
                WHERE timestamp > datetime('now', '-24 hours')
                GROUP BY violation_type
            """)
            recent_violations = dict(cursor.fetchall())
            
            # Compliance trends
            cursor.execute("""
                SELECT compliance_type, AVG(compliance_rate) as avg_rate
                FROM behavioral_compliance
                WHERE timestamp > datetime('now', '-7 days')
                GROUP BY compliance_type
            """)
            compliance_trends = dict(cursor.fetchall())
            
            conn.close()
            
            return {
                "current_metrics": current_metrics,
                "compliance_summary": self.compliance_metrics,
                "recent_violations": recent_violations,
                "compliance_trends": compliance_trends,
                "dashboard_timestamp": datetime.datetime.now().isoformat()
            }
            
        except Exception as e:
            self.logger.error(f"Failed to generate compliance dashboard: {str(e)}")
            return {"error": str(e)}

# Global health integration instance
_global_health_integration = None

def get_health_integration() -> HealthMonitoringIntegration:
    """Get global health monitoring integration instance."""
    global _global_health_integration
    if _global_health_integration is None:
        _global_health_integration = HealthMonitoringIntegration()
    return _global_health_integration

def record_compliance_event(compliance_data: Dict[str, Any]) -> None:
    """Record behavioral compliance event in health monitoring."""
    integration = get_health_integration()
    integration.record_behavioral_compliance(compliance_data)

def record_violation_event(violation_data: Dict[str, Any]) -> None:
    """Record behavioral violation event in health monitoring."""
    integration = get_health_integration()
    integration.record_behavioral_violation(violation_data)

def update_health_metrics() -> Dict[str, Any]:
    """Update behavioral health metrics in monitoring system."""
    integration = get_health_integration()
    return integration.update_behavioral_health_metrics()

def get_compliance_status() -> Dict[str, Any]:
    """Get current behavioral compliance status."""
    integration = get_health_integration()
    return integration.get_compliance_dashboard()

if __name__ == "__main__":
    # Test health monitoring integration
    integration = HealthMonitoringIntegration()
    
    # Test recording compliance
    compliance_data = {
        "compliance_type": "ORCHESTRATION_COMPLIANCE",
        "compliance_rate": 0.95,
        "success_count": 19,
        "violation_count": 1,
        "details": {"test": "integration_test"}
    }
    integration.record_behavioral_compliance(compliance_data)
    
    # Test recording violation
    violation_data = {
        "violation_type": "DIRECT_WORK_ATTEMPT",
        "severity": "CRITICAL",
        "agent_role": "MAIN_AGENT",
        "operation_attempted": "DIRECT_ANALYSIS",
        "prevention_applied": True,
        "user_authority": "SIEMPRE despliega subagentes especializados via Task tools",
        "context": {"test": "violation_test"}
    }
    integration.record_behavioral_violation(violation_data)
    
    # Get compliance dashboard
    dashboard = integration.get_compliance_dashboard()
    print("Compliance Dashboard:")
    print(json.dumps(dashboard, indent=2, default=str))