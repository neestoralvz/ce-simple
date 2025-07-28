# Behavioral Enforcement System

## Authority & Purpose

This enforcement system implements the user's ULTIMATE behavioral requirement:

> **User Statement**: "la manera principal en la que se tiene que comportar el agente principal SIEMPRE es la de ser orquestado de subagentes, es utilizar la task tool de claude code para hcer el despliegue de subagentes especializados para cada una de las tareas que debe de hacer."

**Translation**: "The main way the main agent should ALWAYS behave is to be orchestrated by subagents, using Claude Code's task tool to deploy specialized subagents for each of the tasks it must do."

## System Components

### 1. Behavioral Constraints (`behavioral_constraints.py`)
- **Purpose**: Pre-execution validation blocking main agent direct work
- **Authority**: User vision (ULTIMATE)
- **Function**: Detects and blocks forbidden operations
- **Enforcement**: ABSOLUTE PROHIBITION with zero tolerance

### 2. Task Delegation Enforcer (`task_delegation_enforcer.py`) 
- **Purpose**: Mandatory Task tool delegation with complete audit trail
- **Authority**: "SIEMPRE despliega subagentes especializados via Task tools"
- **Function**: Ensures 100% delegation compliance
- **Enforcement**: Automatic blocking with redirection instructions

### 3. Constraint Monitor (`constraint_monitor.py`)
- **Purpose**: Real-time behavioral constraint monitoring
- **Authority**: Continuous enforcement of orchestration requirements
- **Function**: Active violation detection and prevention
- **Enforcement**: Live monitoring with instant blocking

### 4. Prevention System (`prevention_system.py`)
- **Purpose**: Systematic prevention with 100% compliance guarantee
- **Authority**: Multi-layered enforcement architecture
- **Function**: Comprehensive prevention with automatic correction
- **Enforcement**: Zero exceptions policy with systematic intervention

### 5. Health Integration (`health_integration.py`)
- **Purpose**: Integration with existing health monitoring system
- **Authority**: System-wide compliance tracking and reporting
- **Function**: Health metrics, alerts, and compliance dashboards
- **Enforcement**: Continuous validation with health impact calculation

## Usage Patterns

### Main Enforcement Entry Point
```python
from .prevention_system import prevent_main_agent_direct_work

# CRITICAL: Must be called before ANY main agent operation
result = prevent_main_agent_direct_work(
    operation_type="ANALYSIS",
    agent_role="MAIN_AGENT",
    requires_specialization=True,
    using_task_tools=False
)

if result["status"] == "BLOCKED":
    # Operation blocked - must use Task tool delegation
    print(result["enforcement_message"])
```

### Decorator for Automatic Enforcement
```python
from .prevention_system import enforce_orchestration_constraint

@enforce_orchestration_constraint("RESEARCH")
def research_function():
    # This will be blocked if called by main agent without Task tool
    pass
```

### Health Monitoring Integration
```python
from .health_integration import record_compliance_event, get_compliance_status

# Record successful delegation
record_compliance_event({
    "compliance_type": "ORCHESTRATION_COMPLIANCE",
    "compliance_rate": 1.0,
    "success_count": 1
})

# Get compliance dashboard
dashboard = get_compliance_status()
```

## Enforcement Levels

### ABSOLUTE_BLOCK
- **Operations**: All direct work by main agent
- **Authority**: User vision (ULTIMATE)
- **Override**: None permitted
- **Action**: Immediate blocking with Task tool redirection

### CRITICAL_PREVENTION
- **Operations**: Missing Task tool delegation
- **Authority**: "SIEMPRE" requirement
- **Override**: None permitted  
- **Action**: Automatic correction with delegation instructions

### CONTINUOUS_MONITORING
- **Operations**: All agent operations
- **Authority**: System health integration
- **Override**: None permitted
- **Action**: Real-time compliance tracking

## Compliance Requirements

### For Main Agent
**FORBIDDEN**:
- Direct analysis or research
- Direct implementation or coding
- Direct problem solving
- Direct content creation
- Direct technical work

**REQUIRED**:
- Task tool deployment for ALL work
- Coordination and monitoring ONLY
- Delegation to specialized subagents
- Compliance with orchestration hierarchy

### For System Components
**INTEGRATION**:
- All operations must call enforcement functions
- Pre-execution validation is mandatory
- Compliance events must be recorded
- Health monitoring integration required

## Violation Handling

### Detection
- Pre-execution validation catches attempts before execution
- Real-time monitoring detects ongoing violations
- Automatic pattern recognition identifies implicit violations

### Prevention
- Immediate blocking of non-compliant operations
- Automatic redirection to proper Task tool delegation
- Systematic correction with specialized guidance

### Logging
- Complete audit trail of all enforcement actions
- Violation details with user authority citations
- Compliance statistics and health impact calculations

## Health Monitoring Integration

### Metrics Tracked
- Orchestration compliance rate
- Task delegation success rate
- Violation prevention effectiveness
- Overall behavioral health score

### Alerts Generated
- Critical violations trigger immediate alerts
- Compliance degradation warnings
- System health impact notifications

### Dashboard Features
- Real-time compliance status
- Historical trend analysis
- Violation pattern identification
- Recommendation generation

## Authority Hierarchy

1. **User Vision** (ULTIMATE) - Pure user voice from conversations
2. **CLAUDE.md** (HIGH) - System implementation requirements
3. **Enforcement System** (OPERATIONAL) - Active constraint implementation
4. **Health Monitoring** (CONTINUOUS) - Ongoing compliance validation

## Success Criteria

### Implementation Success
- [x] Pre-execution validation system operational
- [x] Task delegation enforcement active
- [x] Real-time constraint monitoring deployed
- [x] Systematic prevention mechanism functional
- [x] Health monitoring integration complete

### Compliance Success  
- **Target**: 100% enforcement rate
- **Tolerance**: Zero exceptions permitted
- **Monitoring**: Continuous validation active
- **Reporting**: Complete audit trail maintained

### User Requirement Fulfillment
- **Behavioral Constraint**: "SIEMPRE" orchestration requirement enforced
- **Authority Preservation**: User vision maintained as ultimate truth
- **System Evolution**: Enforcement integrated with existing architecture
- **Operational Impact**: Main agent behavior systematically corrected

---

**Generated**: Behavioral Enforcement Implementation  
**Status**: OPERATIONAL - 100% Compliance Enforcement Active  
**Authority**: User Vision (ULTIMATE) - "SIEMPRE despliega subagentes especializados"  
**Purpose**: Systematic prevention of main agent direct work violations