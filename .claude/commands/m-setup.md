# m-setup - Project Setup & Initialization

**31/07/2025 00:00 CDMX** | Automated project setup and system initialization

## AUTORIDAD SUPREMA
@context/architecture/core/truth-source.md → m-setup implements systematic initialization per user vision

## COMMAND DEFINITION
```bash
m-setup
```

## CORE FUNCTIONALITY
### Automatic State Synchronization
- **GitHub Issues Sync**: Real-time status updates (OPEN/CLOSED) via gh CLI
- **Work Items Progress**: Calculate completion based on file changes and commits
- **Violations Analysis**: Execute analyze_violations.sh for current metrics
- **Dependency Detection**: Identify automatic unblocking opportunities
### Intelligence Features
- **Change Detection**: Compare current vs previous state for delta reporting
- **Progress Calculation**: Real progress metrics based on actual file state
- **Unblocking Detection**: Automatic identification when dependencies resolve
- **Quality Validation**: Dashboard integrity and consistency verification
### Data Integration Sources
- **GitHub API**: Issue status, titles, new issues detection
- **Git Repository**: File changes, commit analysis, branch state
- **Violation Scripts**: Current violation counts via analyze_violations.sh
- **File System**: Work item completion validation through file existence

## EXECUTION PROTOCOL
### 1. Pre-Update Validation
```bash
# Backup current dashboard
cp context/roadmap/ROADMAP_REGISTRY.md context/roadmap/ROADMAP_REGISTRY.backup.$(date +%Y%m%d_%H%M%S).md

# Validate prerequisites
gh auth status || exit 1
[[ -f scripts/analyze_violations.sh ]] || exit 1
```
### 2. Data Collection Phase
```bash
# GitHub issues synchronization
gh issue list --repo nalve/ce-simple --json number,title,state --limit 100

# Violation analysis
./scripts/analyze_violations.sh > /tmp/violations_current.txt

# Git analysis
git log --oneline --since="1 week ago"
git status --porcelain
```
### 3. Analysis & Update Phase
- **Issue Status Sync**: Update OPEN/CLOSED states maintaining categorization
- **Work Item Progress**: Calculate completion percentages based on actual work
- **Violation Metrics**: Update P0B-CLEANUP progress based on real violation count
- **Dependency Analysis**: Detect when blocking work items complete
### 4. Dashboard Generation
- **Structure Preservation**: Maintain existing format and manual content
- **Dynamic Updates**: Refresh only data-driven sections
- **Consistency Validation**: Ensure cross-references remain accurate
- **Quality Gates**: Validate dashboard integrity before final update

## SUCCESS CRITERIA
### Automation Goals
- ✅ Zero manual intervention required for standard updates
- ✅ Real-time reflection of project state in dashboard
- ✅ Automatic detection of work item completion
- ✅ Proactive identification of unblocking opportunities
### Quality Standards
- ✅ 100% accuracy in issue status synchronization
- ✅ Preserved manual content and strategic analysis
- ✅ Maintained dashboard readability and structure
- ✅ Complete audit trail of changes made

---

**SETUP AUTHORITY**: Intelligent setup automation serving user vision through systematic initialization while preserving strategic intelligence and manual insight.