#!/usr/bin/env python3
"""
BEHAVIORAL ENFORCEMENT SYSTEM - Main Agent Orchestration Constraints

AUTHORITY: user_vision/ > CLAUDE.md > Commands
PURPOSE: Enforce ABSOLUTE prohibition of direct work by main agent
REQUIREMENT: "la manera principal en la que se tiene que comportar el agente principal 
             SIEMPRE es la de ser orquestado de subagentes, es utilizar la task tool 
             de claude code para hcer el despliegue de subagentes especializados para 
             cada una de las tareas que debe de hacer."

IMPLEMENTATION: Pre-execution validation with active blocking mechanism
"""

import json
import datetime
import os
import sys
from typing import Dict, Any, List, Optional
from pathlib import Path

class BehavioralConstraintEnforcer:
    """
    Enforces main agent behavioral constraints with zero tolerance policy.
    
    ABSOLUTE PROHIBITION: Main agent doing any direct work
    MANDATORY BEHAVIOR: ALWAYS delegate via Task tools to specialized subagents
    ENFORCEMENT LEVEL: 100% compliance required - no exceptions
    """
    
    def __init__(self, project_root: str = "/Users/nalve/ce-simple"):
        self.project_root = Path(project_root)
        self.violations_log = self.project_root / ".claude" / "enforcement" / "violations.log"
        self.enforcement_log = self.project_root / ".claude" / "enforcement" / "enforcement.log"
        self.health_monitor = self.project_root / "data" / "monitoring" / "health.db"
        
        # Ensure enforcement directory exists
        self.violations_log.parent.mkdir(parents=True, exist_ok=True)
        
        # Load user vision authority
        self.user_vision_authority = self._load_user_vision()
        
    def _load_user_vision(self) -> Dict[str, Any]:
        """Load authentic user vision from conversation sources."""
        vision_path = self.project_root / "user_vision"
        
        # Core behavioral constraint from user conversation
        core_constraint = {
            "source": "2025-07-28_22-00_transformacion-arquitectural-multi-subagent.md",
            "quote": "la manera principal en la que se tiene que comportar el agente principal SIEMPRE es la de ser orquestado de subagentes, es utilizar la task tool de claude code para hcer el despliegue de subagentes especializados para cada una de las tareas que debe de hacer.",
            "authority_level": "ULTIMATE",
            "enforcement": "ABSOLUTE_PROHIBITION_DIRECT_WORK"
        }
        
        return {
            "behavioral_constraint": core_constraint,
            "violation_tolerance": 0,
            "enforcement_mode": "ACTIVE_BLOCKING"
        }
    
    def validate_pre_execution(self, operation_type: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        PRE-EXECUTION VALIDATION - Blocks main agent direct work attempts.
        
        Args:
            operation_type: Type of operation being attempted
            context: Execution context and metadata
            
        Returns:
            Validation result with blocking instructions if violation detected
        """
        timestamp = datetime.datetime.now().isoformat()
        
        # Check if main agent is attempting direct work
        if self._is_direct_work_attempt(operation_type, context):
            violation = {
                "timestamp": timestamp,
                "operation_type": operation_type,
                "context": context,
                "violation_type": "DIRECT_WORK_ATTEMPT",
                "severity": "CRITICAL",
                "action_required": "IMMEDIATE_TASK_TOOL_DELEGATION",
                "user_authority": self.user_vision_authority["behavioral_constraint"]["quote"]
            }
            
            self._log_violation(violation)
            return {
                "status": "BLOCKED",
                "violation": violation,
                "redirect_to": "TASK_TOOL_DEPLOYMENT",
                "enforcement_message": self._generate_enforcement_message(violation)
            }
        
        # Operation allowed - log compliance
        self._log_compliance(operation_type, context, timestamp)
        return {
            "status": "ALLOWED",
            "timestamp": timestamp,
            "compliance_verified": True
        }
    
    def _is_direct_work_attempt(self, operation_type: str, context: Dict[str, Any]) -> bool:
        """
        Determine if operation constitutes direct work by main agent.
        
        FORBIDDEN OPERATIONS:
        - Direct analysis or research
        - Direct implementation or coding  
        - Direct problem solving or troubleshooting
        - Direct content creation or documentation
        - Direct technical work or data processing
        """
        forbidden_operations = [
            "DIRECT_ANALYSIS",
            "DIRECT_RESEARCH", 
            "DIRECT_IMPLEMENTATION",
            "DIRECT_CODING",
            "DIRECT_PROBLEM_SOLVING",
            "DIRECT_TROUBLESHOOTING",
            "DIRECT_CONTENT_CREATION",
            "DIRECT_DOCUMENTATION",
            "DIRECT_TECHNICAL_WORK",
            "DIRECT_DATA_PROCESSING"
        ]
        
        # Check operation type
        if operation_type in forbidden_operations:
            return True
            
        # Check context for direct work indicators
        if context.get("agent_role") == "MAIN_AGENT" and context.get("work_type") != "COORDINATION":
            return True
            
        # Check if Task tools are being bypassed for work that requires subagent specialization
        if context.get("requires_specialization", False) and not context.get("using_task_tools", False):
            return True
            
        return False
    
    def _log_violation(self, violation: Dict[str, Any]) -> None:
        """Log behavioral constraint violation with full audit trail."""
        with open(self.violations_log, "a") as f:
            f.write(json.dumps(violation) + "\n")
            
        # Alert health monitoring system
        self._alert_health_monitor(violation)
    
    def _log_compliance(self, operation_type: str, context: Dict[str, Any], timestamp: str) -> None:
        """Log successful compliance with behavioral constraints."""
        compliance_record = {
            "timestamp": timestamp,
            "operation_type": operation_type,
            "context": context,
            "status": "COMPLIANT",
            "enforcement_result": "ALLOWED"
        }
        
        with open(self.enforcement_log, "a") as f:
            f.write(json.dumps(compliance_record) + "\n")
    
    def _alert_health_monitor(self, violation: Dict[str, Any]) -> None:
        """Alert health monitoring system of behavioral constraint violation."""
        try:
            alert = {
                "timestamp": violation["timestamp"],
                "type": "BEHAVIORAL_CONSTRAINT_VIOLATION",
                "severity": "CRITICAL",
                "violation": violation,
                "system_impact": "MAIN_AGENT_DIRECT_WORK_BLOCKED"
            }
            
            # Write to health monitoring system
            health_alert_path = self.project_root / "data" / "monitoring" / "behavioral_alerts.json"
            with open(health_alert_path, "a") as f:
                f.write(json.dumps(alert) + "\n")
                
        except Exception as e:
            # Ensure violation logging doesn't fail silently
            with open(self.violations_log, "a") as f:
                f.write(f"HEALTH_MONITOR_ALERT_FAILED: {str(e)}\n")
    
    def _generate_enforcement_message(self, violation: Dict[str, Any]) -> str:
        """Generate enforcement message with user authority citation."""
        return f"""
BEHAVIORAL CONSTRAINT VIOLATION DETECTED

AUTHORITY SOURCE: User Vision (ULTIMATE)
USER STATEMENT: "{self.user_vision_authority['behavioral_constraint']['quote']}"

VIOLATION: Main agent attempting direct work
OPERATION: {violation['operation_type']}
TIMESTAMP: {violation['timestamp']}

ENFORCEMENT ACTION: Operation BLOCKED
REQUIRED CORRECTION: Deploy specialized subagent via Task tools

COMPLIANCE PROTOCOL:
1. Identify required specialization for this task
2. Deploy Task tool with appropriate subagent configuration  
3. Coordinate and monitor subagent execution
4. Report results without performing direct work

ZERO TOLERANCE POLICY: This behavior must happen "SIEMPRE" (always) as user specified.
"""

def enforce_behavioral_constraints(operation_type: str, context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Main enforcement entry point - validates all operations against behavioral constraints.
    
    CRITICAL: This function MUST be called before any main agent operation attempt.
    PURPOSE: Ensure 100% compliance with user vision behavioral requirements.
    """
    enforcer = BehavioralConstraintEnforcer()
    return enforcer.validate_pre_execution(operation_type, context)

# Integration hooks for Claude Code
def validate_main_agent_operation(operation_type: str, **kwargs) -> bool:
    """Hook for validating main agent operations before execution."""
    context = kwargs
    result = enforce_behavioral_constraints(operation_type, context)
    
    if result["status"] == "BLOCKED":
        print(result["enforcement_message"])
        return False
        
    return True

if __name__ == "__main__":
    # Test enforcement system
    test_context = {
        "agent_role": "MAIN_AGENT",
        "work_type": "ANALYSIS",
        "requires_specialization": True,
        "using_task_tools": False
    }
    
    result = enforce_behavioral_constraints("DIRECT_ANALYSIS", test_context)
    print(json.dumps(result, indent=2))