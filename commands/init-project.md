# init-project

## Purpose

Initialize ce-simple project with git repository, directory structure, and core documentation.

## Principles

- **Single Responsibility**: Project initialization only
- **Directness**: Three sequential phases without indirection
- **Technical Precision**: Specific git, directory, and file operations
- **Error Recovery**: Clear fallbacks with actionable guidance

## Execution Process

### Phase 1: Git Repository Setup
Initialize git repository with standard configuration:

Pre-execution validation:
```bash
REQUIREMENT_CHECK: Git available | STATUS: check | ACTION: set_git_capability_level
```

Use Bash to setup git:
```bash
git init
git config --local user.name "Developer"  
git config --local user.email "dev@project.local"
```

If git initialization fails:
```
ERROR: Git repository initialization failed
CAUSE: Git not available or permission denied
IMPACT: Version control functionality unavailable
RECOVERY: Install git: 'brew install git' or 'sudo apt install git'
CONTINUE: Project structure proceeds without version control
```

### Phase 2: Directory Structure Creation
Create essential project directories:

Pre-execution validation:
```bash
REQUIREMENT_CHECK: Write permissions on pwd | STATUS: check | ACTION: abort_if_no_write
```

Use Bash to create structure:
```bash
mkdir -p commands docs/core docs/vision archive
```

Required directories:
- `commands/` - Slash command definitions
- `docs/core/` - System architecture
- `docs/vision/` - Project philosophy  
- `archive/` - Preserved components

If directory creation fails:
```
ERROR: Directory creation failed for '<specific_directory>'
CAUSE: Permission denied or filesystem full
IMPACT: Project structure incomplete
RECOVERY: Run 'sudo mkdir -p <directories>' or choose different location
CONTINUE: Proceeding with successfully created directories: <list>
```

### Phase 3: Core Documentation Generation
Generate essential project files:

Use Write to create:
1. `CLAUDE.md` - System overview and command catalog
2. `README.md` - Project introduction and quick start
3. `docs/core/README.md` - Architecture documentation index

Required content:
- Project purpose and structure
- Available commands and usage
- Development principles reference
- Quick start workflow

If documentation creation fails:
```
ERROR: Documentation file creation failed: '<filename>'
CAUSE: Write permission denied or disk full
IMPACT: Core documentation missing
RECOVERY: Manual file creation - template content provided below
CONTINUE: Proceeding with successfully created files: <list>
```

Final validation:
- Verify git repository (if available)
- Confirm directory structure  
- Validate core documentation
- Create initial commit (if git available)

---

## Implementation Standards

**Single Responsibility**: Project initialization only - creates git repo, directories, and core docs
**Tool Usage**: Direct Bash and Write calls without orchestration overhead
**Error Handling**: Specific error messages with manual resolution steps
**Validation**: Confirm each phase completion before proceeding

**Authority References**:
@./docs/core/development-principles.md
@./docs/vision/overview.md