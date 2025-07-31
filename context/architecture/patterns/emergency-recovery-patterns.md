# Emergency Recovery Patterns - System Resilience Architecture

**31/07/2025** | Emergency recovery patterns for inaccessible resources and system resilience

## AUTORIDAD SUPREMA
↑ @context/architecture/patterns.md → emergency-recovery-patterns.md implements emergency recovery patterns per system resilience authority

## PRINCIPIO FUNDAMENTAL
**"Systematic recovery preserves data and system integrity during access failures"** - Proactive recovery patterns for inaccessible resources with complete data preservation and system restoration.

## INACCESSIBLE RESOURCE RECOVERY PATTERN

### **Pattern Context**
**Problem**: Critical resources become inaccessible due to security constraints, permissions, or tool limitations
**Solution**: Systematic recovery through alternative access methods and data preservation protocols
**Evidence**: Recovery of uncommitted changes from inaccessible external git worktrees

### **Recovery Protocol Framework**
1. **Detection Phase**: Identify inaccessible resources with content verification
2. **Assessment Phase**: Evaluate recovery feasibility and data criticality
3. **Extraction Phase**: Use alternative access methods for data recovery
4. **Preservation Phase**: Apply recovered data to accessible locations
5. **Cleanup Phase**: Systematic cleanup of inaccessible resources
6. **Prevention Phase**: Implement measures to prevent future occurrences

## GIT WORKTREE RECOVERY PATTERN

### **Emergency Recovery Implementation**
```bash
# Detection
git worktree list | grep inaccessible-path
git -C inaccessible-path status --porcelain

# Assessment  
changes_count=$(git -C inaccessible-path status --porcelain | wc -l)
if [[ $changes_count -gt 0 ]]; then
    # Critical recovery needed
fi

# Extraction
git -C inaccessible-path diff HEAD > changes.patch
git -C inaccessible-path ls-files --others --exclude-standard

# Preservation
git apply changes.patch  # or manual file creation
git add recovered-files

# Cleanup
git worktree remove inaccessible-path --force
```

### **Recovery Decision Matrix**
```
Resource State    | Recovery Method        | Data Risk | Action Priority
------------------|------------------------|-----------|----------------
Uncommitted       | Alternative access     | HIGH      | IMMEDIATE
Committed         | Reference extraction   | LOW       | SCHEDULED
Mixed state       | Selective recovery     | MEDIUM    | URGENT
Clean state       | Direct cleanup         | NONE      | ROUTINE
```

## ORPHANED RESOURCE CLEANUP PATTERN

### **Systematic Cleanup Protocol**
1. **Inventory Phase**: List all potentially orphaned resources
2. **Validation Phase**: Verify orphaned status through system queries
3. **Safety Phase**: Create recovery checkpoints before cleanup
4. **Cleanup Phase**: Remove confirmed orphaned resources
5. **Verification Phase**: Confirm successful cleanup without data loss

### **Implementation Framework**
- **Detection**: `git worktree prune` + directory existence validation
- **Cleanup**: Force removal with `--force` flags when safe
- **Prevention**: Automated cleanup scripts for regular maintenance

## FALLBACK ARCHITECTURE PATTERN

### **Multi-Level Fallback Strategy**
1. **Primary**: Use preferred access method (e.g., external worktree)
2. **Secondary**: Fallback to alternative method (e.g., internal worktree)
3. **Tertiary**: Manual recovery procedures when automation fails
4. **Emergency**: System reconstruction from available backups

### **Resilience Integration**
- **Proactive Monitoring**: Detect potential access issues before they become critical
- **Automated Recovery**: Scripts handle common recovery scenarios
- **Manual Procedures**: Documented steps for complex recovery situations
- **System Learning**: Update prevention measures based on recovery experiences

## INTEGRATION REFERENCES

### ← @context/architecture/claude_code/worktree-accessibility-patterns.md
**Connection**: Emergency recovery complements accessibility patterns for complete resilience
**Protocol**: Recovery patterns provide systematic approach when accessibility patterns fail

### ←→ scripts/infrastructure/conversation-workspace.sh
**Connection**: Recovery patterns implemented through enhanced workspace management
**Protocol**: Script provides both prevention and recovery capabilities for worktree issues

---

**EMERGENCY RECOVERY DECLARATION**: This pattern documentation captures systematic approaches to emergency recovery, providing resilience architecture for inaccessible resources while maintaining data integrity and system functionality.

**PATTERN VALIDATION**: Pattern validated through successful recovery of uncommitted changes from inaccessible external worktrees during system troubleshooting session.