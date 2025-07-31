# Hook Integration Classification - Complete Script Lifecycle Mapping

**31/07/2025 14:00 CDMX** | PC-PARALLEL Phase B: Complete lifecycle classification for Claude Code hooks integration

## AUTORIDAD SUPREMA
@context/architecture/core/truth-source.md → PC-PARALLEL Phase B → Hook Integration Classification per H-SCRIPTS-CLASSIFICATION authority

## LIFECYCLE CLASSIFICATION FRAMEWORK

### **🚀 PRE-CONVERSATION HOOKS** (1 script)
**Execution Timing**: Before conversation initiation
**Purpose**: Setup and preparation for conversation workspace

#### `conversation-workspace.sh` → `.claude/hooks/pre-conversation.sh`
- **Function**: Git worktree-based conversation isolation setup
- **Trigger**: Claude Code conversation start
- **Dependencies**: Git repository, worktree support
- **Fallback**: Manual workspace creation if hook fails

### **🏁 POST-CONVERSATION HOOKS** (2 scripts - Composite)
**Execution Timing**: After successful conversation completion
**Purpose**: Knowledge extraction and quality assurance

#### Composite Hook: `.claude/hooks/post-conversation.sh`
**Primary**: `context-extract.sh`
- **Function**: Extract conversation insights for system evolution
- **Output**: Knowledge integration to operational/context systems
- **Dependencies**: Successful conversation completion

**Secondary**: `quality-gate.sh`
- **Function**: Quality assurance validation post-conversation
- **Output**: System health verification and compliance checking
- **Dependencies**: Context extraction completion

### **📝 POST-EDIT HOOKS** (1 script)
**Execution Timing**: After file modifications in context/
**Purpose**: Maintain system coherence and validate changes

#### `validate-context-coherence.sh` → `.claude/hooks/post-edit.sh`
- **Function**: Validate CLAUDE.md conditional links coherence
- **Trigger**: Context file modifications
- **Dependencies**: Context architecture files
- **Fallback**: Manual coherence validation via command

### **⚡ ON-DEMAND UTILITY SCRIPTS** (25+ scripts)
**Execution Timing**: Command-triggered or batch operations
**Purpose**: Specialized functionality invoked by commands
**Integration**: Remain in scripts/ - accessed via command system

#### **Analysis Utilities** (4 scripts)
- `analyze_violations.sh` - File size violation analysis
- `analyze_real_violations.sh` - Real-time violation detection  
- `enhanced_analyze_violations.sh` - Advanced analysis with patterns
- `domain-classifier.sh` - Content domain classification

#### **Validation Utilities** (6 scripts)
- `validate_integrity.sh` - System health validation
- `authority-validator.sh` - Authority chain validation
- `validate-script-communication.sh` - Script communication validation
- `validation_suite.sh` - Complete validation suite
- **Note**: `validate-context-coherence.sh` → POST-EDIT HOOK
- **Note**: `quality-gate.sh` → POST-CONVERSATION HOOK

#### **Backup & Safety Utilities** (3 scripts)
- `backup_secure.sh` - Triple backup system
- `rollback_safe.sh` - Emergency recovery system
- `rollback-manager.sh` - Advanced rollback management

#### **Batch Processing Utilities** (3 scripts)
- `batch-l2-modular.sh` - Mass L2-modular extraction
- `batch-issue-create.sh` - Parallel GitHub issue creation
- `batch_reference_updater.sh` - Mass reference updates

#### **Extraction Utilities** (2 scripts)
- `extract_assisted.sh` - Semiautomated extraction with checkpoints
- `l2_modular_extractor.sh` - L2-modular content extraction
- **Note**: `context-extract.sh` → POST-CONVERSATION HOOK

#### **Infrastructure Utilities** (3 scripts)
- `parallel-tool-manager.sh` - Parallel tool execution coordination
- `progress-tracker.sh` - Progress monitoring and tracking
- `handoff-init.sh` - Intelligent handoff/issue creation
- **Note**: `conversation-workspace.sh` → PRE-CONVERSATION HOOK

#### **Maintenance Utilities** (3 scripts)
- `cleanup_backup_cascades.sh` - Backup cleanup automation
- `fix-raw-conversations.sh` - Conversation path fixes
- `fix-script-communication.sh` - Script communication fixes

#### **Integration Utilities** (3 scripts)
- `cross-reference-updater.sh` - Cross-reference management
- `roadmap-update.sh` - Dashboard synchronization
- `test-roadmap-update.sh` - Integration testing

#### **Issue Management Utilities** (2 scripts)
- `issue-detector.sh` - Automatic GitHub issue detection
- `create_distribution.sh` - Distribution package creation

#### **Specialized Modules** (2 scripts)
- `conversation-analyzer.sh` - Conversation intelligence analysis
- `dashboard-integrator.sh` - Dashboard automation integration

## HOOK ARCHITECTURE DESIGN

### **Composite Hook Strategy**
**post-conversation.sh** combines:
1. `context-extract.sh` (primary) → Knowledge extraction
2. `quality-gate.sh` (secondary) → Quality validation
3. **Execution Order**: Extract → Validate → Report

### **Graceful Degradation Protocol**
- **Hook Failures**: Continue with warning, enable manual alternatives
- **Missing Dependencies**: Skip hook execution, log requirement
- **Partial Success**: Complete successful components, report failures

### **Fallback Mechanisms**
- **Pre-conversation failure**: Manual workspace setup guidance
- **Post-conversation failure**: Manual extraction commands provided
- **Post-edit failure**: Manual coherence validation instructions

## SUCCESS CRITERIA

### **Hook Integration Success**
- ✅ **4 Scripts** identified for automated hooks (pre/post-conversation/post-edit)
- ✅ **29+ Scripts** classified as on-demand utilities  
- ✅ **Composite hooks** designed for efficiency (post-conversation)
- ✅ **Fallback systems** specified for all automation points

### **Classification Completeness**
- ✅ **100% Script Coverage**: All 32+ scripts categorized by lifecycle
- ✅ **Clear Integration Path**: Hooks vs utilities clearly defined
- ✅ **Dependency Mapping**: All requirements and fallbacks documented

---

**HOOK INTEGRATION CLASSIFICATION DECLARATION**: Complete lifecycle mapping of 32+ scripts with 4 automated hooks (composite post-conversation) and 29+ on-demand utilities, preserving functionality while enabling Claude Code lifecycle automation per PC-PARALLEL Phase B architecture.

**EVOLUTION PATHWAY**: Classification → Hook Architecture → Implementation → Gradual Migration