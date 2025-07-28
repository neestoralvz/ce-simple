#!/usr/bin/env python3
"""
TASK DELEGATION ENFORCEMENT SYSTEM

AUTHORITY: User Vision - "SIEMPRE despliega subagentes especializados via Task tools"
PURPOSE: Ensure 100% compliance with mandatory Task tool delegation
REQUIREMENT: All work MUST be delegated to specialized subagents via Task tools

VIOLATION LOGGING: Complete audit trail of compliance and violations
INTEGRATION: Health monitoring system alerts for behavioral violations
"""

import json
import datetime
import os
import subprocess
from typing import Dict, Any, List, Optional, Tuple
from pathlib import Path
import sqlite3

class TaskDelegationEnforcer:
    """
    Enforces mandatory Task tool delegation with zero exceptions policy.
    
    CORE PRINCIPLE: Main agent NEVER executes work directly
    ENFORCEMENT: Active blocking with automatic redirection to Task tools
    COMPLIANCE: 100% delegation requirement - no overrides permitted
    """
    
    def __init__(self, project_root: str = "/Users/nalve/ce-simple"):
        self.project_root = Path(project_root)
        self.delegation_log = self.project_root / ".claude" / "enforcement" / "delegation.log"
        self.compliance_db = self.project_root / ".claude" / "enforcement" / "compliance.db"
        
        # Ensure enforcement directory exists
        self.delegation_log.parent.mkdir(parents=True, exist_ok=True)
        
        # Initialize compliance database
        self._init_compliance_db()
        
        # Specialized subagent configurations
        self.subagent_specialists = self._load_specialist_configs()
    
    def _init_compliance_db(self) -> None:
        """Initialize SQLite database for compliance tracking."""
        conn = sqlite3.connect(self.compliance_db)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS delegation_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                operation_type TEXT NOT NULL,
                required_specialist TEXT NOT NULL,
                task_tool_used BOOLEAN NOT NULL,
                compliance_status TEXT NOT NULL,
                violation_details TEXT,
                enforcement_action TEXT,
                user_authority TEXT
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS specialist_deployments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                specialist_type TEXT NOT NULL,
                task_description TEXT NOT NULL,
                deployment_method TEXT NOT NULL,
                success_status BOOLEAN NOT NULL,
                execution_context TEXT
            )
        """)
        
        conn.commit()
        conn.close()
    
    def _load_specialist_configs(self) -> Dict[str, Dict[str, Any]]:
        """Load specialized subagent configurations for different task types."""
        return {
            "RESEARCH_SPECIALIST": {
                "purpose": "Investigation + benchmarking + best practices",
                "task_tool_config": "research_deployment",
                "expertise": ["web_search", "pattern_analysis", "best_practices", "benchmarking"],
                "forbidden_for_main": True
            },
            "ARCHITECTURE_VALIDATOR": {
                "purpose": "System consistency + integration verification",
                "task_tool_config": "architecture_validation",
                "expertise": ["system_design", "integration_patterns", "consistency_checks"],
                "forbidden_for_main": True
            },
            "CONTENT_OPTIMIZER": {
                "purpose": "Token economy + structure optimization",
                "task_tool_config": "content_optimization",
                "expertise": ["token_efficiency", "structure_design", "optimization"],
                "forbidden_for_main": True
            },
            "VOICE_PRESERVATION": {
                "purpose": "User intent exactitude + authenticity validation",
                "task_tool_config": "voice_validation",
                "expertise": ["user_intent", "authenticity_check", "voice_preservation"],
                "forbidden_for_main": True
            },
            "QUALITY_ASSURANCE": {
                "purpose": "Final validation + standards compliance",
                "task_tool_config": "quality_validation",
                "expertise": ["standards_compliance", "quality_gates", "final_validation"],
                "forbidden_for_main": True
            },
            "IMPLEMENTATION_SPECIALIST": {
                "purpose": "Code implementation + technical execution",
                "task_tool_config": "implementation_deployment",
                "expertise": ["coding", "technical_implementation", "execution"],
                "forbidden_for_main": True
            }
        }
    
    def enforce_delegation(self, operation_type: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Enforce mandatory Task tool delegation for all work operations.
        
        Args:
            operation_type: Type of operation being attempted
            context: Execution context including work details
            
        Returns:
            Enforcement result with delegation instructions or blocking
        """
        timestamp = datetime.datetime.now().isoformat()
        
        # Determine required specialist
        required_specialist = self._identify_required_specialist(operation_type, context)
        
        # Check if Task tools are being used
        using_task_tools = context.get("using_task_tools", False)
        
        if not using_task_tools and required_specialist:
            # VIOLATION: Direct work attempt without Task tool delegation
            violation = {
                "timestamp": timestamp,
                "operation_type": operation_type,
                "required_specialist": required_specialist,
                "violation_type": "MISSING_TASK_TOOL_DELEGATION",
                "context": context,
                "severity": "CRITICAL",
                "user_authority": "SIEMPRE despliega subagentes especializados via Task tools"
            }
            
            self._log_violation(violation)
            self._record_compliance_event(violation, "VIOLATION")
            
            return {
                "status": "BLOCKED",
                "violation": violation,
                "required_action": "DEPLOY_TASK_TOOL",
                "specialist_config": self.subagent_specialists[required_specialist],
                "enforcement_message": self._generate_delegation_message(violation)
            }
        
        elif using_task_tools and required_specialist:
            # COMPLIANCE: Proper Task tool delegation
            compliance = {
                "timestamp": timestamp,
                "operation_type": operation_type,
                "required_specialist": required_specialist,
                "context": context,
                "status": "COMPLIANT"
            }
            
            self._log_compliance(compliance)
            self._record_compliance_event(compliance, "COMPLIANT")
            
            return {
                "status": "ALLOWED",
                "compliance": compliance,
                "specialist_deployed": required_specialist
            }
        
        else:
            # Coordination-only operations allowed for main agent
            return {
                "status": "ALLOWED",
                "note": "Coordination operation - no delegation required"
            }
    
    def _identify_required_specialist(self, operation_type: str, context: Dict[str, Any]) -> Optional[str]:
        """
        Identify which specialized subagent is required for the operation.
        
        MAPPING: Operation types to required specialist subagents
        PRINCIPLE: All work requiring expertise must be delegated
        """
        operation_specialist_map = {
            # Research operations
            "RESEARCH": "RESEARCH_SPECIALIST",
            "INVESTIGATION": "RESEARCH_SPECIALIST", 
            "BENCHMARKING": "RESEARCH_SPECIALIST",
            "BEST_PRACTICES": "RESEARCH_SPECIALIST",
            "WEB_SEARCH": "RESEARCH_SPECIALIST",
            
            # Architecture operations  
            "ARCHITECTURE_ANALYSIS": "ARCHITECTURE_VALIDATOR",
            "SYSTEM_DESIGN": "ARCHITECTURE_VALIDATOR",
            "INTEGRATION_CHECK": "ARCHITECTURE_VALIDATOR",
            "CONSISTENCY_VALIDATION": "ARCHITECTURE_VALIDATOR",
            
            # Content operations
            "CONTENT_CREATION": "CONTENT_OPTIMIZER",
            "DOCUMENT_CREATION": "CONTENT_OPTIMIZER",
            "STRUCTURE_OPTIMIZATION": "CONTENT_OPTIMIZER",
            "TOKEN_OPTIMIZATION": "CONTENT_OPTIMIZER",
            
            # Voice preservation operations
            "USER_INTENT_VALIDATION": "VOICE_PRESERVATION",
            "AUTHENTICITY_CHECK": "VOICE_PRESERVATION",
            "VOICE_ANALYSIS": "VOICE_PRESERVATION",
            
            # Quality operations
            "QUALITY_VALIDATION": "QUALITY_ASSURANCE",
            "STANDARDS_CHECK": "QUALITY_ASSURANCE",
            "FINAL_VALIDATION": "QUALITY_ASSURANCE",
            
            # Implementation operations
            "CODE_IMPLEMENTATION": "IMPLEMENTATION_SPECIALIST",
            "TECHNICAL_EXECUTION": "IMPLEMENTATION_SPECIALIST",
            "CODING": "IMPLEMENTATION_SPECIALIST",
            "FILE_CREATION": "IMPLEMENTATION_SPECIALIST",
            "FILE_EDITING": "IMPLEMENTATION_SPECIALIST"
        }
        
        # Check direct operation type mapping
        specialist = operation_specialist_map.get(operation_type)
        if specialist:
            return specialist
            
        # Check context for specialization requirements
        if context.get("requires_expertise"):
            expertise_type = context.get("expertise_type")
            for specialist_key, config in self.subagent_specialists.items():
                if expertise_type in config["expertise"]:
                    return specialist_key
        
        # Check if operation involves file manipulation (requires implementation specialist)
        if any(key in context for key in ["file_path", "editing", "creation", "modification"]):
            return "IMPLEMENTATION_SPECIALIST"
            
        return None
    
    def _log_violation(self, violation: Dict[str, Any]) -> None:
        """Log Task tool delegation violation with complete audit trail."""
        with open(self.delegation_log, "a") as f:
            log_entry = {
                "type": "VIOLATION",
                "data": violation
            }
            f.write(json.dumps(log_entry) + "\n")
    
    def _log_compliance(self, compliance: Dict[str, Any]) -> None:
        """Log successful Task tool delegation compliance."""
        with open(self.delegation_log, "a") as f:
            log_entry = {
                "type": "COMPLIANCE", 
                "data": compliance
            }
            f.write(json.dumps(log_entry) + "\n")
    
    def _record_compliance_event(self, event_data: Dict[str, Any], status: str) -> None:
        """Record compliance event in database for analytics."""
        conn = sqlite3.connect(self.compliance_db)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO delegation_events (
                timestamp, operation_type, required_specialist, task_tool_used,
                compliance_status, violation_details, enforcement_action, user_authority
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            event_data["timestamp"],
            event_data["operation_type"],
            event_data.get("required_specialist", ""),
            event_data.get("using_task_tools", False),
            status,
            json.dumps(event_data.get("context", {})),
            event_data.get("enforcement_action", ""),
            event_data.get("user_authority", "")
        ))
        
        conn.commit()
        conn.close()
    
    def _generate_delegation_message(self, violation: Dict[str, Any]) -> str:
        """Generate enforcement message with specific delegation instructions."""
        specialist = violation["required_specialist"]
        config = self.subagent_specialists[specialist]
        
        return f"""
TASK DELEGATION VIOLATION DETECTED

USER AUTHORITY: "{violation['user_authority']}"
OPERATION: {violation['operation_type']}
REQUIRED SPECIALIST: {specialist}

VIOLATION: Main agent attempting direct work that requires specialization
ENFORCEMENT: Operation BLOCKED - Task tool deployment required

DELEGATION INSTRUCTIONS:
1. Deploy Task tool with specialist: {specialist}
2. Specialist purpose: {config['purpose']}
3. Specialist expertise: {', '.join(config['expertise'])}
4. Task tool configuration: {config['task_tool_config']}

COMPLIANCE PROTOCOL:
- Main agent role: Coordination and monitoring ONLY
- Specialized work: MUST be delegated via Task tools
- Zero exceptions: This requirement is ABSOLUTE

NEXT ACTION: Deploy Task tool with {specialist} configuration
"""

def enforce_task_delegation(operation_type: str, context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Main enforcement entry point for Task tool delegation requirements.
    
    CRITICAL: Must be called before any work operation by main agent
    PURPOSE: Ensure 100% compliance with specialized subagent delegation
    """
    enforcer = TaskDelegationEnforcer()
    return enforcer.enforce_delegation(operation_type, context)

def get_compliance_statistics() -> Dict[str, Any]:
    """Get compliance statistics for monitoring and reporting."""
    enforcer = TaskDelegationEnforcer()
    
    conn = sqlite3.connect(enforcer.compliance_db)
    cursor = conn.cursor()
    
    # Get overall compliance rate
    cursor.execute("""
        SELECT compliance_status, COUNT(*) as count
        FROM delegation_events
        GROUP BY compliance_status
    """)
    
    stats = dict(cursor.fetchall())
    total = sum(stats.values())
    compliance_rate = stats.get("COMPLIANT", 0) / total if total > 0 else 0
    
    conn.close()
    
    return {
        "total_events": total,
        "compliance_rate": compliance_rate,
        "violations": stats.get("VIOLATION", 0),
        "compliant_events": stats.get("COMPLIANT", 0)
    }

if __name__ == "__main__":
    # Test delegation enforcement
    test_context = {
        "work_type": "RESEARCH",
        "requires_expertise": True, 
        "using_task_tools": False
    }
    
    result = enforce_task_delegation("RESEARCH", test_context)
    print(json.dumps(result, indent=2))
    
    # Show compliance statistics
    stats = get_compliance_statistics()
    print("\nCompliance Statistics:")
    print(json.dumps(stats, indent=2))