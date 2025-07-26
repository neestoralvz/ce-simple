# Git Protocols - Technical Authority

**Updated**: 2025-07-24 | **Authority**: Complete git workflow standards | **Limit**: 80 lines
**Purpose**: Single source of truth for git operations across system

## Commit Protocols (Lines 5-25)
### **Commit Message Standards**
- **Format**: `Type: Description | Context | Co-Authored-By: Claude <noreply@anthropic.com>`
- **Types**: `System|Feature|Fix|Refactor|Docs|Test|Archive`
- **Description**: Concise action-focused summary
- **Context**: Brief explanation when not obvious
- **Length**: Subject ≤50 chars, body ≤72 chars per line

### **Commit Process**
1. **git status** - Review all changes
2. **git diff** - Verify exact modifications  
3. **git add [files]** - Stage relevant changes
4. **git commit -m "$(cat <<'EOF'...)"** - Use HEREDOC for formatting
5. **Validation** - Ensure commit contains all intended changes

### **Pre-commit Requirements**
- Line limit validation (≤80 lines docs)
- PTS compliance check
- Reference integrity verification
- No secrets or keys committed

## Branch Management (Lines 26-45)  
### **Branch Strategy**
- **main**: Production-ready, stable code
- **feature/**: New functionality development
- **fix/**: Bug resolution branches
- **refactor/**: Code improvement without feature changes

### **Branch Operations**
- **Create**: `git checkout -b feature/description`
- **Switch**: `git checkout branch-name`
- **Update**: `git pull origin main` before merging
- **Clean**: `git branch -d feature/completed` after merge

### **Merge Protocol**
- **Pull Request Required**: No direct main commits
- **Review Process**: Code review before merge
- **Conflict Resolution**: Systematic conflict handling
- **Validation**: Full testing before merge approval

## Pull Request Standards (Lines 46-65)
### **PR Creation**
```bash
gh pr create --title "Type: Description" --body "$(cat <<'EOF'
## Summary
- [Bullet point changes]

## Test plan  
- [Testing checklist]

🤖 Generated with [Claude Code](https://claude.ai/code)
EOF
)"
```

### **PR Requirements**
- **Summary**: Clear description of changes
- **Test Plan**: Validation approach
- **Documentation**: Updated docs if needed
- **Line Compliance**: All files meet standards

### **Review Criteria**
- **Functionality**: Changes work as intended
- **Standards**: PTS compliance verified
- **Integration**: No system conflicts
- **Documentation**: Adequate explanation provided

## Workflow Integration (Lines 66-80)
### **Development Cycle**
1. **git checkout -b feature/name** - Create feature branch
2. **Development** - Implement changes following standards
3. **git add . && git commit** - Commit with proper message
4. **git push -u origin feature/name** - Push to remote
5. **gh pr create** - Create pull request
6. **Review & Merge** - Code review and integration

### **Quality Gates**
- **Pre-commit**: Automated validation
- **Pre-push**: Integration testing
- **Pre-merge**: Code review approval
- **Post-merge**: System validation

### **Best Practices**
- **Small Commits**: Atomic, focused changes
- **Clear Messages**: Descriptive commit descriptions
- **Regular Pushes**: Backup work frequently
- **Clean History**: Logical commit progression

---
**Authority**: This file is the single source of truth for git protocols across entire system.