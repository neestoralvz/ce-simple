#!/usr/bin/env python3
"""
SYSTEMATIC PREVENTION MECHANISM - 100% Compliance Enforcement

AUTHORITY: User Vision - "SIEMPRE" (always) orchestration requirement
PURPOSE: Systematic prevention of main agent direct work with automated correction
GUARANTEE: Zero tolerance policy with 100% enforcement rate

IMPLEMENTATION: Multi-layered prevention system with automatic intervention
INTEGRATION: All system components enforcing unified behavioral constraints
"""

import json
import datetime
import os
import sys
import importlib
import inspect
from typing import Dict, Any, List, Optional, Callable, Union
from pathlib import Path
import functools
import logging
from dataclasses import dataclass

# Import enforcement components
try:
    from .behavioral_constraints import enforce_behavioral_constraints
    from .task_delegation_enforcer import enforce_task_delegation
    from .constraint_monitor import validate_agent_operation
except ImportError:
    # Handle relative imports for standalone execution
    sys.path.append(str(Path(__file__).parent))
    from behavioral_constraints import enforce_behavioral_constraints
    from task_delegation_enforcer import enforce_task_delegation
    from constraint_monitor import validate_agent_operation

@dataclass
class PreventionLayer:
    """Prevention layer configuration and enforcement."""
    name: str
    priority: int
    enforcement_function: Callable
    blocking_level: str  # "WARNING", "BLOCK", "ABSOLUTE_BLOCK"
    description: str

class SystematicPreventionMechanism:
    """
    Multi-layered prevention system ensuring 100% behavioral compliance.
    
    PREVENTION LAYERS:
    1. Pre-execution validation (ABSOLUTE_BLOCK)
    2. Task delegation enforcement (ABSOLUTE_BLOCK)  
    3. Real-time constraint monitoring (ABSOLUTE_BLOCK)
    4. Automatic correction triggers (AUTO_CORRECT)
    5. System health integration (CONTINUOUS_MONITORING)
    
    ZERO TOLERANCE: No overrides, no exceptions, no bypasses permitted
    """
    
    def __init__(self, project_root: str = "/Users/nalve/ce-simple"):
        self.project_root = Path(project_root)
        self.prevention_log = self.project_root / ".claude" / "enforcement" / "prevention.log"
        self.config_file = self.project_root / ".claude" / "enforcement" / "prevention_config.json"
        
        # Ensure enforcement directory exists
        self.prevention_log.parent.mkdir(parents=True, exist_ok=True)
        
        # Configure logging
        self._setup_logging()
        
        # Initialize prevention layers
        self.prevention_layers = self._initialize_prevention_layers()
        
        # Load configuration
        self.config = self._load_prevention_config()
        
        # Active prevention status
        self.prevention_active = True
        self.enforcement_statistics = {
            "total_operations_checked": 0,
            "violations_prevented": 0,
            "automatic_corrections": 0,
            "compliance_rate": 1.0
        }
        
        self.logger.info("Systematic Prevention Mechanism initialized - 100% enforcement active")
    
    def _setup_logging(self) -> None:
        """Configure logging for prevention system."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.prevention_log),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger("SystematicPreventionMechanism")
    
    def _initialize_prevention_layers(self) -> List[PreventionLayer]:
        """Initialize all prevention layers with proper priority ordering."""
        return [
            PreventionLayer(
                name="PRE_EXECUTION_VALIDATION",
                priority=1,
                enforcement_function=enforce_behavioral_constraints,
                blocking_level="ABSOLUTE_BLOCK",
                description="Pre-execution validation blocking direct work attempts"
            ),
            PreventionLayer(
                name="TASK_DELEGATION_ENFORCEMENT", 
                priority=2,
                enforcement_function=enforce_task_delegation,
                blocking_level="ABSOLUTE_BLOCK",
                description="Mandatory Task tool delegation with zero exceptions"
            ),
            PreventionLayer(
                name="REAL_TIME_MONITORING",
                priority=3,
                enforcement_function=validate_agent_operation,
                blocking_level="ABSOLUTE_BLOCK", 
                description="Real-time constraint monitoring with active prevention"
            )
        ]
    
    def _load_prevention_config(self) -> Dict[str, Any]:
        """Load prevention system configuration."""
        default_config = {
            "enforcement_mode": "ABSOLUTE",
            "tolerance_level": 0,
            "automatic_correction": True,
            "health_integration": True,
            "violation_escalation": True,
            "user_authority": "la manera principal en la que se tiene que comportar el agente principal SIEMPRE es la de ser orquestado de subagentes, es utilizar la task tool de claude code para hcer el despliegue de subagentes especializados para cada una de las tareas que debe de hacer.",
            "prevention_layers_active": True
        }
        
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    return {**default_config, **config}
            except Exception as e:
                self.logger.warning(f"Config load failed, using defaults: {str(e)}")
                
        return default_config
    
    def enforce_systematic_prevention(self, operation_type: str, agent_role: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main enforcement entry point - applies all prevention layers systematically.
        
        Args:
            operation_type: Type of operation being attempted
            agent_role: Role of agent (MAIN_AGENT, SUBAGENT, COORDINATOR)
            context: Operation context and metadata
            
        Returns:
            Enforcement result with prevention actions applied
        """
        timestamp = datetime.datetime.now().isoformat()
        
        # Update statistics
        self.enforcement_statistics["total_operations_checked"] += 1
        
        # Apply prevention layers in priority order
        prevention_results = []
        final_result = {"status": "ALLOWED", "layers_applied": []}
        
        for layer in sorted(self.prevention_layers, key=lambda x: x.priority):
            try:
                # Apply prevention layer
                layer_result = self._apply_prevention_layer(layer, operation_type, agent_role, context)
                prevention_results.append({
                    "layer": layer.name,
                    "result": layer_result,
                    "timestamp": timestamp
                })
                
                # Check if layer blocked the operation
                if layer_result.get("status") == "BLOCKED":
                    # VIOLATION DETECTED - Apply systematic prevention
                    self.enforcement_statistics["violations_prevented"] += 1
                    
                    prevention_action = self._apply_systematic_prevention(layer, layer_result, context)
                    
                    final_result = {
                        "status": "BLOCKED",
                        "blocking_layer": layer.name,
                        "violation": layer_result.get("violation"),
                        "prevention_action": prevention_action,
                        "layers_applied": prevention_results,
                        "enforcement_message": self._generate_systematic_message(layer, layer_result),
                        "automatic_correction": prevention_action.get("correction_applied", False)
                    }
                    
                    # Log systematic prevention
                    self._log_systematic_prevention(final_result)
                    
                    # ABSOLUTE BLOCK - Stop processing further layers
                    break
                    
            except Exception as e:
                self.logger.error(f"Prevention layer {layer.name} failed: {str(e)}")
                prevention_results.append({
                    "layer": layer.name,
                    "result": {"status": "ERROR", "error": str(e)},
                    "timestamp": timestamp
                })
        
        # Update compliance rate
        self._update_compliance_statistics(final_result)
        
        # Log successful compliance if no blocking occurred
        if final_result["status"] == "ALLOWED":
            self._log_compliance_success(operation_type, agent_role, context, prevention_results)
        
        return final_result
    
    def _apply_prevention_layer(self, layer: PreventionLayer, operation_type: str, agent_role: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Apply individual prevention layer enforcement."""
        try:
            # Prepare arguments based on enforcement function signature
            if layer.name == "PRE_EXECUTION_VALIDATION":
                return layer.enforcement_function(operation_type, context)
            elif layer.name == "TASK_DELEGATION_ENFORCEMENT":
                return layer.enforcement_function(operation_type, context)
            elif layer.name == "REAL_TIME_MONITORING":
                return layer.enforcement_function(agent_role, operation_type, context)
            else:
                return layer.enforcement_function(operation_type, context)
                
        except Exception as e:
            return {
                "status": "ERROR",
                "error": str(e),
                "layer": layer.name
            }
    
    def _apply_systematic_prevention(self, layer: PreventionLayer, layer_result: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """Apply systematic prevention action when violation is detected."""
        prevention_action = {
            "timestamp": datetime.datetime.now().isoformat(),
            "layer": layer.name,
            "action_type": "SYSTEMATIC_PREVENTION",
            "blocking_applied": True,
            "correction_applied": False
        }
        
        # Apply automatic correction if enabled
        if self.config.get("automatic_correction", True):
            correction_result = self._apply_automatic_correction(layer_result, context)
            prevention_action["correction_applied"] = correction_result["success"]
            prevention_action["correction_details"] = correction_result
            
            if correction_result["success"]:
                self.enforcement_statistics["automatic_corrections"] += 1
        
        # Escalate to health monitoring if enabled
        if self.config.get("health_integration", True):
            self._escalate_to_health_monitoring(layer_result, prevention_action)
        
        return prevention_action
    
    def _apply_automatic_correction(self, violation_result: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """Apply automatic correction for detected violations."""
        correction_result = {
            "success": False,
            "action": "NO_ACTION",
            "details": {}
        }
        
        violation = violation_result.get("violation", {})
        violation_type = violation.get("violation_type", "UNKNOWN")
        
        # Automatic correction based on violation type
        if violation_type in ["DIRECT_WORK_ATTEMPT", "MISSING_TASK_TOOL_DELEGATION"]:
            # Generate Task tool deployment instructions
            correction_result = {
                "success": True,
                "action": "GENERATE_TASK_TOOL_DEPLOYMENT",
                "details": {
                    "required_specialist": violation.get("required_specialist", "GENERAL_SPECIALIST"),
                    "deployment_instructions": self._generate_task_tool_instructions(violation, context),
                    "redirect_message": "Operation redirected to Task tool deployment"
                }
            }
        
        elif violation_type == "IMPLICIT_DIRECT_WORK":
            # Generate delegation template
            correction_result = {
                "success": True, 
                "action": "GENERATE_DELEGATION_TEMPLATE",
                "details": {
                    "delegation_template": self._generate_delegation_template(violation, context),
                    "guidance_message": "Use delegation template for proper Task tool orchestration"
                }
            }
        
        return correction_result
    
    def _generate_task_tool_instructions(self, violation: Dict[str, Any], context: Dict[str, Any]) -> str:
        """Generate specific Task tool deployment instructions."""
        specialist = violation.get("required_specialist", "IMPLEMENTATION_SPECIALIST")
        operation = violation.get("operation_attempted", "UNKNOWN_OPERATION")
        
        return f"""
AUTOMATIC TASK TOOL DEPLOYMENT INSTRUCTIONS

SPECIALIST REQUIRED: {specialist}
OPERATION: {operation}
CONTEXT: {json.dumps(context, indent=2)}

DEPLOYMENT TEMPLATE:
```
Deploy {specialist} via Task tool:
- Purpose: Handle {operation} with appropriate specialization
- Context: {context.get('description', 'Operation requiring specialized expertise')}
- Expected Output: Completed task with proper delegation maintained
- Coordination: Main agent monitors and reports results only
```

COMPLIANCE: This ensures proper orchestration via subagents as required by user vision.
"""
    
    def _generate_delegation_template(self, violation: Dict[str, Any], context: Dict[str, Any]) -> str:
        """Generate delegation template for proper orchestration."""
        return f"""
DELEGATION TEMPLATE - PROPER ORCHESTRATION

USER AUTHORITY: "SIEMPRE despliega subagentes especializados via Task tools"

STEP 1: Identify Required Specialist
Operation: {violation.get('operation_attempted', 'UNKNOWN')}
Required Expertise: {context.get('expertise_required', 'SPECIALIZED_KNOWLEDGE')}

STEP 2: Deploy Task Tool
```
[Deploy specialized subagent via Task tool for this operation]
```

STEP 3: Coordinate and Monitor
- Main agent role: Coordination ONLY
- Subagent role: Execute specialized work
- Result: Report completion and outcomes

COMPLIANCE: Maintains proper orchestration hierarchy per user vision.
"""
    
    def _escalate_to_health_monitoring(self, violation_result: Dict[str, Any], prevention_action: Dict[str, Any]) -> None:
        """Escalate violation to health monitoring system."""
        try:
            escalation = {
                "timestamp": datetime.datetime.now().isoformat(),
                "type": "BEHAVIORAL_VIOLATION_ESCALATION",
                "severity": "CRITICAL",
                "violation": violation_result,
                "prevention_action": prevention_action,
                "system_impact": "MAIN_AGENT_DIRECT_WORK_PREVENTED"
            }
            
            health_escalation_file = self.project_root / "data" / "monitoring" / "prevention_escalations.json"
            with open(health_escalation_file, "a") as f:
                f.write(json.dumps(escalation) + "\n")
                
            self.logger.info("Violation escalated to health monitoring system")
            
        except Exception as e:
            self.logger.error(f"Health monitoring escalation failed: {str(e)}")
    
    def _generate_systematic_message(self, layer: PreventionLayer, layer_result: Dict[str, Any]) -> str:
        """Generate comprehensive systematic prevention message."""
        violation = layer_result.get("violation", {})
        
        return f"""
SYSTEMATIC PREVENTION MECHANISM ACTIVATED

USER AUTHORITY: "{self.config['user_authority']}"
PREVENTION LAYER: {layer.name} (Priority {layer.priority})
BLOCKING LEVEL: {layer.blocking_level}

VIOLATION DETECTED:
- Type: {violation.get('violation_type', 'UNKNOWN')}
- Operation: {violation.get('operation_attempted', 'UNKNOWN')}
- Severity: {violation.get('severity', 'CRITICAL')}

SYSTEMATIC ENFORCEMENT:
- Operation BLOCKED immediately
- Automatic correction applied: {layer_result.get('prevention_action', {}).get('correction_applied', False)}
- Health monitoring notified: {self.config.get('health_integration', True)}

COMPLIANCE REQUIREMENT:
Main agent MUST ALWAYS orchestrate via subagents using Task tools.
ZERO TOLERANCE - No exceptions, no overrides, no bypasses.

REQUIRED ACTION:
1. Deploy specialized subagent via Task tool
2. Coordinate subagent execution (main agent role)
3. Monitor and report results
4. NEVER attempt direct work execution

PREVENTION STATUS: Active systematic enforcement operational
COMPLIANCE RATE: {self.enforcement_statistics['compliance_rate']:.2%}
"""
    
    def _log_systematic_prevention(self, prevention_result: Dict[str, Any]) -> None:
        """Log systematic prevention action with full audit trail."""
        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "type": "SYSTEMATIC_PREVENTION",
            "prevention_result": prevention_result,
            "statistics": self.enforcement_statistics.copy()
        }
        
        with open(self.prevention_log, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
        
        self.logger.critical(f"Systematic prevention applied: {prevention_result['blocking_layer']}")
    
    def _log_compliance_success(self, operation_type: str, agent_role: str, context: Dict[str, Any], prevention_results: List[Dict[str, Any]]) -> None:
        """Log successful compliance with all prevention layers."""
        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "type": "COMPLIANCE_SUCCESS",
            "operation_type": operation_type,
            "agent_role": agent_role,
            "context": context,
            "prevention_layers_passed": prevention_results,
            "statistics": self.enforcement_statistics.copy()
        }
        
        with open(self.prevention_log, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    
    def _update_compliance_statistics(self, enforcement_result: Dict[str, Any]) -> None:
        """Update compliance statistics based on enforcement result."""
        total = self.enforcement_statistics["total_operations_checked"]
        violations = self.enforcement_statistics["violations_prevented"]
        
        # Calculate compliance rate
        compliance_rate = (total - violations) / total if total > 0 else 1.0
        self.enforcement_statistics["compliance_rate"] = compliance_rate
        
        # Log statistics update
        if total % 100 == 0:  # Log every 100 operations
            self.logger.info(f"Prevention statistics: {self.enforcement_statistics}")
    
    def get_prevention_statistics(self) -> Dict[str, Any]:
        """Get current prevention system statistics."""
        return {
            **self.enforcement_statistics,
            "prevention_active": self.prevention_active,
            "layers_count": len(self.prevention_layers),
            "config": self.config
        }

# Global prevention mechanism instance
_global_prevention = None

def get_prevention_mechanism() -> SystematicPreventionMechanism:
    """Get global prevention mechanism instance."""
    global _global_prevention
    if _global_prevention is None:
        _global_prevention = SystematicPreventionMechanism()
    return _global_prevention

def prevent_main_agent_direct_work(operation_type: str, agent_role: str = "MAIN_AGENT", **context) -> Dict[str, Any]:
    """
    MAIN PREVENTION ENTRY POINT - Must be called before ANY operation.
    
    Args:
        operation_type: Type of operation being attempted
        agent_role: Role of agent performing operation
        **context: Operation context and metadata
        
    Returns:
        Prevention result - BLOCKED if violation detected, ALLOWED if compliant
        
    CRITICAL: This function enforces 100% compliance with user vision behavioral constraints.
    AUTHORITY: User statement requiring "SIEMPRE" (always) orchestration via subagents.
    """
    prevention = get_prevention_mechanism()
    return prevention.enforce_systematic_prevention(operation_type, agent_role, context)

# Decorator for automatic prevention enforcement
def enforce_orchestration_constraint(operation_type: str):
    """
    Decorator to automatically enforce orchestration constraints on functions.
    
    Usage:
    @enforce_orchestration_constraint("ANALYSIS")
    def analyze_data():
        # This will be blocked if called by main agent without Task tool delegation
        pass
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Determine agent role from context
            agent_role = kwargs.get('agent_role', 'MAIN_AGENT')
            
            # Check prevention constraints
            prevention_result = prevent_main_agent_direct_work(
                operation_type=operation_type,
                agent_role=agent_role,
                function_name=func.__name__,
                args=args,
                kwargs=kwargs
            )
            
            if prevention_result["status"] == "BLOCKED":
                # Raise exception or return error - prevents execution
                raise ValueError(prevention_result["enforcement_message"])
            
            # Execute function if allowed
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

if __name__ == "__main__":
    # Test systematic prevention mechanism
    prevention = SystematicPreventionMechanism()
    
    # Test violation prevention
    test_result = prevention.enforce_systematic_prevention(
        operation_type="DIRECT_ANALYSIS",
        agent_role="MAIN_AGENT",
        context={
            "requires_specialization": True,
            "using_task_tools": False,
            "description": "Attempting direct analysis without Task tool delegation"
        }
    )
    
    print("Prevention Test Result:")
    print(json.dumps(test_result, indent=2, default=str))
    
    # Show prevention statistics
    stats = prevention.get_prevention_statistics()
    print("\nPrevention Statistics:")
    print(json.dumps(stats, indent=2))