# Backup & Safety Scripts

**Category**: System Protection & Recovery
**Scripts**: 3 scripts providing comprehensive safety architecture

## Scripts Overview

### **backup_secure.sh**
**Purpose**: Triple backup system with git checkpoints
**Usage**: `./backup_secure.sh`
**Features**: Original → backup → working copy with integrity validation

### **rollback_safe.sh**
**Purpose**: Safe system recovery from backups
**Usage**: `./rollback_safe.sh [OPTIONS] BACKUP_DIR`
**Features**: Full/selective rollback with post-rollback validation

### **rollback-manager.sh**
**Purpose**: Advanced rollback coordination and management
**Usage**: `./rollback-manager.sh [OPERATION]`
**Features**: Backup management, rollback orchestration, emergency recovery

## Safety Protocols

### **Before Every Operation**
1. ✅ Run `backup_secure.sh` for triple backup protection
2. ✅ Verify git working directory clean state
3. ✅ Create recovery checkpoints

### **Emergency Recovery**
1. 🚨 **System Corruption**: `./rollback_safe.sh -fgv backup_dir`
2. 🚨 **Partial Failure**: `./rollback_safe.sh -s backup_dir file1.md`
3. 🚨 **Validation Failure**: Immediate rollback with validation

## Integration Points

- **PHASE_0_EMERGENCY**: Critical safety layer for mass extraction operations
- **L2-Modular System**: Backup protection for systematic extractions
- **All Workflows**: Universal safety requirement before any modifications

## Dependencies

- **Input**: Source files, git repository state
- **Output**: Protected backup systems enabling safe experimentation