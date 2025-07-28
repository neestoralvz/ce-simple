"""
BEHAVIORAL ENFORCEMENT SYSTEM - Integration Module

AUTHORITY: User Vision (ULTIMATE)
PURPOSE: Comprehensive enforcement of main agent orchestration constraints
REQUIREMENT: "la manera principal en la que se tiene que comportar el agente principal 
             SIEMPRE es la de ser orquestado de subagentes"

INTEGRATION: Complete enforcement ecosystem with health monitoring integration
"""

from .prevention_system import (
    prevent_main_agent_direct_work,
    enforce_orchestration_constraint,
    get_prevention_mechanism
)

from .behavioral_constraints import (
    enforce_behavioral_constraints,
    validate_main_agent_operation
)

from .task_delegation_enforcer import (
    enforce_task_delegation,
    get_compliance_statistics
)

from .constraint_monitor import (
    validate_agent_operation,
    get_constraint_monitor
)

from .health_integration import (
    record_compliance_event,
    record_violation_event,
    update_health_metrics,
    get_compliance_status
)

# Main enforcement entry points
__all__ = [
    # Primary enforcement functions
    'prevent_main_agent_direct_work',
    'enforce_orchestration_constraint',
    'validate_agent_operation',
    
    # Compliance tracking
    'record_compliance_event',
    'record_violation_event',
    'get_compliance_status',
    
    # System components
    'get_prevention_mechanism',
    'get_constraint_monitor',
    'update_health_metrics'
]

# System-wide enforcement function
def enforce_user_vision_constraints(operation_type: str, agent_role: str = "MAIN_AGENT", **context):
    """
    ULTIMATE ENFORCEMENT FUNCTION - Ensures 100% compliance with user vision.
    
    This function implements the user's absolute requirement:
    "SIEMPRE despliega subagentes especializados via Task tools"
    
    Args:
        operation_type: Type of operation being attempted
        agent_role: Role of agent (MAIN_AGENT, SUBAGENT)
        **context: Operation context and metadata
        
    Returns:
        Enforcement result - BLOCKED if violation detected, ALLOWED if compliant
        
    AUTHORITY: User Vision (ULTIMATE) - Zero tolerance policy
    """
    return prevent_main_agent_direct_work(operation_type, agent_role, **context)

# User vision compliance verification
def verify_orchestration_compliance():
    """
    Verify current system compliance with user vision requirements.
    
    Returns comprehensive compliance status including:
    - Orchestration compliance rate
    - Task delegation success rate  
    - Violation prevention effectiveness
    - Overall behavioral health score
    """
    return get_compliance_status()

# System health integration
def integrate_with_health_monitoring():
    """
    Integrate behavioral enforcement with system health monitoring.
    
    Updates health metrics with behavioral compliance data and
    ensures continuous monitoring of orchestration requirements.
    """
    return update_health_metrics()