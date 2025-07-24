# Environment Setup Standard

**Updated**: 2025-07-24 | **Authority**: Anthropic CLAUDE.md best practices | **Limit**: 100 lines

## Purpose

This file should document the development environment requirements, installation procedures, and configuration steps needed to work on this project. Based on official Anthropic recommendations, this ensures Claude understands the technical context and dependencies.

## Content Structure

### What Should Be Included

**System Requirements:**
```markdown
# Prerequisites
- Node.js: 18.x or higher
- npm: 9.x or higher (or yarn/pnpm equivalent)
- Git: Latest stable version
- Operating System: macOS/Linux/Windows WSL2
```

**Development Tools:**
```markdown
# Required Tools
- Code Editor: VS Code with recommended extensions
- Browser: Chrome/Firefox for testing
- Terminal: bash/zsh with preferred configuration
- Package Manager: npm (primary), yarn (alternative)
```

**Environment Variables:**
```markdown
# Configuration
- DATABASE_URL: Database connection string
- API_KEY: External service authentication
- NODE_ENV: development/staging/production
- PORT: Application port (default: 3000)
```

**Installation Steps:**
```markdown
# Setup Process
1. Clone repository: git clone [repo-url]
2. Install dependencies: npm install
3. Copy environment: cp .env.example .env.local
4. Start development: npm run dev
```

## Implementation Guidelines

### Version Management
- **Node Version**: Specify exact versions or use .nvmrc
- **Package Versions**: Lock file requirements and updates
- **Tool Compatibility**: IDE extensions and configuration
- **OS-specific**: Platform-specific setup instructions

### Configuration Files
- **Environment**: .env file templates and examples
- **Editor**: VS Code settings and extensions
- **Git**: .gitignore and repository settings
- **Build Tools**: Webpack, Vite, or build system configuration

### Troubleshooting Setup
- **Common Issues**: Permission errors, version conflicts
- **Platform Differences**: macOS vs Windows vs Linux specifics
- **Dependency Problems**: Node modules, native dependencies
- **Performance**: Memory limits, build optimization

## Benefits for AI Assistant

**Context Awareness**: Claude understands technical constraints
**Error Resolution**: Can suggest environment-related fixes
**Setup Assistance**: Guides users through installation issues
**Compatibility**: Knows version requirements and limitations

---

**Implementation Note**: This template should be populated with actual project requirements, specific version numbers, and step-by-step setup instructions. The format follows Anthropic's guidance for comprehensive environment documentation that enables AI assistants to provide accurate technical support and troubleshooting.