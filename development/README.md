# Development Workspace

**Purpose**: Development environment for command prototyping, testing, and staging before deployment to export/

## Directory Structure

### prototypes/
Command prototypes and experimental implementations. Used for rapid iteration and concept validation.

### testing/
Testing environment for command validation and quality assurance. STP compliance testing and integration validation.

### staging/
Pre-deployment validation area. Final quality checks before commands move to export/ for global deployment.

## Development Workflow

1. **Prototype** → Create initial command concepts in prototypes/
2. **Test** → Validate functionality and STP compliance in testing/
3. **Stage** → Final validation and deployment preparation in staging/
4. **Deploy** → Move validated commands to export/

## Standards

- **STP Compliance**: All commands must pass 12-component validation
- **Autocontainment**: Commands reference only other commands via slash syntax
- **Single Responsibility**: Each command does exactly one thing well
- **150 Line Limit**: Maximum command length for LLM optimization

## Quality Gates

- **Prototype**: Concept validation and basic functionality
- **Testing**: Full STP compliance and integration testing
- **Staging**: Deployment readiness and final quality verification
- **Export**: Production-ready global commands