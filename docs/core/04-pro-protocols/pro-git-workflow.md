# Git Workflow Protocols

**Updated: 2025-07-24** | **Authority**: Git workflow standards implementing Partnership Protocol

## Commit Excellence Standards

### Claude Code Commit Protocol
**Mandatory signature for all commits**:
```bash
🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
```
- **Implementation**: Heredoc format `git commit -m "$(cat <<'EOF'\n<message>\n\n<signature>\nEOF\n)"`
- **Integration**: Pre-commit hooks + CI/CD compatible | **No exceptions**: Every commit requires signature

### Commit Structure & Atomicity
**Standard format**: `<type>: <description>` followed by mandatory signature
- **Types**: feat (new feature) | fix (bug fix) | docs (documentation) | refactor (code restructuring) | test (testing) | style (formatting) | chore (maintenance)
- **Scope principles**: Single purpose commits | Complete functional changes | Independent rollback units | Self-contained modifications
- **Message guidelines**: Focus on why > what | ≤72 characters first line | Clear action and expected outcome

### Commit Quality Standards
**Before every commit**:
1. Run `git status` to review all changes
2. Run `git diff` to validate modifications  
3. Review `git log --oneline -5` for message consistency
4. Verify all changes serve single purpose
5. Ensure commit is functionally complete

## Branch Management Excellence

### Git Worktree Strategy (Mandatory)
**Parallel development**: `git worktree add -b <branch> <path>` → Independent directories → Seamless context switching
- **Benefits**: Complete isolation | Shared .git | Resource efficiency | Parallel workflows
- **Use cases**: Feature development | Bug fixes | Experimental changes | Documentation updates

### Branch Conventions & Integration
**Naming standards**:
- `feature/<description>` - New functionality development
- `fix/<issue-description>` - Bug fixes and corrections  
- `docs/<section>` - Documentation updates and improvements
- `chore/<task>` - Maintenance and administrative tasks

**Integration hierarchy**: Fast-forward preferred > Merge commits > Rebase for cleanup
**Conflict resolution**: Immediate resolution → Context preservation → Pattern documentation → Thorough testing

## Advanced Git Operations

### Pre-Commit Quality Gates
**Automated validation checklist**:
- PTS compliance verification (all 12 components)
- Length limits enforcement (≤150 lines commands, ≤200 lines docs)
- Cross-reference integrity checks
- Quality metrics validation
- English-only content verification

**State management**: `git status` → `git diff --staged` → `git log --oneline -10` → Branch hygiene verification

### Repository Operations & Maintenance
**Daily workflow standards**:
- Regular commits (maximum 30-minute intervals during active work)
- Push to remote repository at end of each session
- Tag significant milestones and releases appropriately  
- Archive completed branches to maintain repository hygiene
- Monthly cleanup of merged branches and obsolete references

**Monitoring and integration**:
- Editor git integration enabled for real-time status
- Automated hooks for quality enforcement and validation
- CI/CD pipeline triggers on push events
- Health metrics tracking (commit frequency, branch health, merge success rates)

## Error Handling & Recovery

### Common Scenarios & Solutions
**Commit mistakes**: `git commit --amend` (fix last) | `git reset --soft HEAD~1` (undo, keep changes) | `git reset --hard HEAD~1` (undo completely)
**Branch issues**: `git checkout -b recovery` | `git cherry-pick <commit>` | `git rebase -i HEAD~n` (cleanup)

**Merge conflict resolution workflow**:
1. Identify conflicting files with `git status`
2. Open files and resolve `<<<<<<<` `=======` `>>>>>>>` markers
3. Test functionality thoroughly after resolution
4. Stage resolved files with `git add`
5. Complete merge with `git commit`
6. Document resolution patterns for team reference

## Cross-Module Integration

### Git + Development Standards Integration
**PTS compliance**: Every commit validated (12 components) → Structure integrity → Documentation sync → Change validation
**Tool coordination**: Multiple worktrees | Version control agents | State coordination | Change aggregation protocols

### Git + Project Governance Integration  
**Authority hierarchy**: Structure validation → Protocol compliance → Cross-reference maintenance → System alignment
**Quality enforcement**: Standards validation → Governance rules → Integration testing → Mandatory documentation updates

---

**Application**: All git operations must follow these protocols to maintain system quality and consistency. Reference this document for all version control decisions and workflow implementations.