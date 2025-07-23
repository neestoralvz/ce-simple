# Automation Directory

**Purpose**: Executable scripts and automated systems for project operations.

## Directory Structure

### Core (`/core/`)
**Python Intelligence Scripts** - Advanced automation and orchestration
- Pattern recognition systems
- Intelligent orchestration engines  
- Performance optimization systems
- Governance and monitoring systems

### Scripts (`/scripts/`)
**Shell Operational Scripts** - System operations and maintenance
- Git workflow automation
- File system operations
- Deployment and configuration scripts
- System maintenance utilities

### Testing (`/testing/`)
**Validation Scripts** - Quality assurance and testing
- Automated test suites
- Compliance validation scripts
- Performance testing tools
- Integration test frameworks

### Config (`/config/`)
**Configuration Files** - System and application configuration
- Environment configurations
- Service configurations
- Tool configurations
- Integration settings

## File Organization Rules

**Python Files** (.py):
- Core intelligence: `/core/`
- Operational scripts: `/scripts/` 
- Test automation: `/testing/`

**Shell Scripts** (.sh):
- System operations: `/scripts/`
- Test execution: `/testing/`

**Configuration** (.json, .yaml, .toml):
- All configurations: `/config/`

**JavaScript** (.js):
- Web interfaces: `/scripts/web/`
- Build tools: `/scripts/build/`

## Navigation Patterns

**Predictable Locations**:
- Intelligence systems: `automation/core/{domain}-{system}.py`
- Operational tools: `automation/scripts/{purpose}-{action}.sh`
- Test suites: `automation/testing/{component}-test.py`
- Configurations: `automation/config/{service}-config.{format}`

**Quick Access**:
- Core systems: `find automation/core -name "*orchestrat*"`
- Scripts by purpose: `find automation/scripts -name "*git*"`
- Test suites: `find automation/testing -name "*test*"`

## Integration Points

- **Commands**: Automation called from executable commands
- **Documentation**: Implementation guides in `docs/implementation/`
- **Templates**: Automation templates in `templates/automation/`
- **Standards**: Development standards in `docs/standards/`