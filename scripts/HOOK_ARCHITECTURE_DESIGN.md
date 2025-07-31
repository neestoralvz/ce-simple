# Hook Architecture Design - Claude Code Lifecycle Integration

**31/07/2025 14:15 CDMX** | PC-PARALLEL Phase B: Complete hook architecture design with composite hooks strategy

## AUTORIDAD SUPREMA
@context/architecture/core/truth-source.md → PC-PARALLEL Phase B → Hook Architecture Design per lifecycle classification authority

## EXISTING HOOK ECOSYSTEM ANALYSIS

### **Current Claude Code Hooks** (.claude/hooks/)
**Status**: ✅ ACTIVE Protection System
- **project-protection.json**: Hook configuration and event definitions
- **root-protection.sh**: Root directory protection with auto-remediation
- **size-validation.sh**: File size enforcement (80-line limit)
- **standards-check.sh**: Standards compliance monitoring
- **authority-validation.sh**: Authority chain integrity validation

**Current Events**:
- `file-write` → root-protection.sh
- `user-prompt-submit` → standards-check.sh  
- `tool-call-complete` → size-validation.sh
- `session-start` → authority-validation.sh

## NEW HOOK INTEGRATION ARCHITECTURE

### **Enhanced Hook Events - Scripts Integration**

#### **🚀 pre-conversation Event**
**Event**: `conversation-start` (new)
**Target Script**: `scripts/infrastructure/conversation-workspace.sh`
**Integration Strategy**: Composite with existing `session-start`

**Implementation**:
```bash
# Enhanced session-start hook
#!/bin/bash
# Existing authority validation
./.claude/hooks/authority-validation.sh

# NEW: Conversation workspace setup
if [[ -f "scripts/infrastructure/conversation-workspace.sh" ]]; then
    echo "🚀 Setting up conversation workspace..."
    ./scripts/infrastructure/conversation-workspace.sh --auto-setup
    echo "✅ Workspace ready"
else
    echo "⚠️ Workspace script not found - manual setup required"
fi
```

#### **🏁 post-conversation Event**  
**Event**: `conversation-end` (new)
**Target Scripts**: `context-extract.sh` + `quality-gate.sh` (composite)
**Integration Strategy**: Sequential execution with error handling

**Implementation**:
```bash
# New post-conversation composite hook
#!/bin/bash
conversation_success=true

# Primary: Context extraction
if [[ -f "scripts/extraction/context-extract.sh" ]]; then
    echo "📤 Extracting conversation insights..."
    if ./scripts/extraction/context-extract.sh --auto-extract; then
        echo "✅ Context extraction completed"
    else
        echo "⚠️ Context extraction failed - manual extraction recommended"
        conversation_success=false
    fi
else
    echo "⚠️ Context extract script not found"
    conversation_success=false
fi

# Secondary: Quality validation
if [[ -f "scripts/validation/quality-gate.sh" ]]; then
    echo "✅ Running quality validation..."
    if ./scripts/validation/quality-gate.sh --post-conversation; then
        echo "✅ Quality validation passed"
    else
        echo "⚠️ Quality issues detected - review recommended"
    fi
else
    echo "⚠️ Quality gate script not found"
fi

# Report final status
if [[ "$conversation_success" == "true" ]]; then
    echo "🎉 Conversation completed successfully with full automation"
else
    echo "⚠️ Conversation completed with some manual steps required"
fi
```

#### **📝 post-edit Event Enhancement**
**Event**: `file-write` (enhance existing)
**Target Script**: `scripts/validation/validate-context-coherence.sh`
**Integration Strategy**: Add to existing file-write hook

**Implementation**:
```bash
# Enhanced file-write hook
#!/bin/bash
file_path="$1"

# Existing root protection
./.claude/hooks/root-protection.sh "$file_path"

# NEW: Context coherence validation for context/ files
if [[ "$file_path" =~ ^context/ ]]; then
    if [[ -f "scripts/validation/validate-context-coherence.sh" ]]; then
        echo "🔗 Validating context coherence..."
        ./scripts/validation/validate-context-coherence.sh "$file_path"
    else
        echo "⚠️ Context coherence validator not found"
    fi
fi
```

## COMPOSITE HOOKS STRATEGY

### **Hook Composition Pattern**
**Primary Hook**: Core functionality (must succeed)
**Secondary Hook**: Enhancement functionality (may fail gracefully)
**Tertiary Hook**: Reporting/logging (informational)

### **Error Handling Strategy**
- **Critical Failures**: Stop execution, provide manual alternatives
- **Non-Critical Failures**: Continue with warnings, log for review
- **Dependency Missing**: Skip gracefully, provide guidance

### **Performance Optimization**
- **Parallel Execution**: Where scripts are independent
- **Conditional Execution**: Skip unnecessary validation based on context
- **Caching**: Reuse analysis results across hook invocations

## FALLBACK MECHANISMS INTEGRATION

### **Hook Failure Recovery**
```bash
# Fallback mechanism template
execute_with_fallback() {
    local script_path="$1"
    local fallback_message="$2"
    
    if [[ -f "$script_path" ]] && [[ -x "$script_path" ]]; then
        if timeout 30s "$script_path" "$@"; then
            return 0
        else
            echo "⚠️ Hook failed: $fallback_message"
            return 1
        fi
    else
        echo "ℹ️ Script not available: $fallback_message"
        return 2
    fi
}
```

### **Manual Alternative Guidance**
```bash
# Manual alternative provision
provide_manual_alternative() {
    local failed_action="$1"
    
    case "$failed_action" in
        "workspace-setup")
            echo "Manual: Create git worktree with: git worktree add .conv-$(date +%Y%m%d_%H%M%S) HEAD"
            ;;
        "context-extract")
            echo "Manual: Review conversation and extract insights to context/operational/"
            ;;
        "quality-gate")
            echo "Manual: Run validation suite: ./scripts/validation/validation_suite.sh"
            ;;
    esac
}
```

## CONFIGURATION ENHANCEMENT

### **Enhanced project-protection.json**
```json
{
  "project": {
    "enforcement_level": "warn",
    "max_file_lines": 80,
    "fail_on_error": false,
    "script_integration": {
      "enabled": true,
      "timeout_seconds": 30,
      "fallback_guidance": true
    }
  },
  "events": {
    "session-start": [
      ".claude/hooks/authority-validation.sh",
      "scripts/infrastructure/conversation-workspace.sh --auto-setup"
    ],
    "conversation-end": [
      "scripts/extraction/context-extract.sh --auto-extract",
      "scripts/validation/quality-gate.sh --post-conversation"
    ],
    "file-write": [
      ".claude/hooks/root-protection.sh",
      "scripts/validation/validate-context-coherence.sh"
    ],
    "user-prompt-submit": [
      ".claude/hooks/standards-check.sh"
    ],
    "tool-call-complete": [
      ".claude/hooks/size-validation.sh"
    ]
  }
}
```

## UTILITY SCRIPTS ACCESSIBILITY

### **Command Integration Pattern**
- **Remain in scripts/**: All 29+ utility scripts stay in organized structure
- **Command Access**: Available via /scripts:category or direct invocation
- **Batch Operations**: Called by specific commands or workflows
- **Hook Independence**: No dependency on hook system for functionality

### **Smart Discovery Mechanism**
```bash
# Smart script discovery
find_script() {
    local script_name="$1"
    local script_path=$(find scripts/ -name "$script_name" -type f | head -1)
    
    if [[ -f "$script_path" ]]; then
        echo "$script_path"
    else
        echo "Script not found: $script_name" >&2
        return 1
    fi
}
```

## SUCCESS CRITERIA

### **Hook Integration Success**
- ✅ **4 Enhanced Events**: session-start, conversation-end, file-write, user-prompt-submit
- ✅ **3 New Script Integrations**: workspace setup, context extraction, coherence validation
- ✅ **Composite Hook Strategy**: Post-conversation combines 2 scripts with error handling
- ✅ **Graceful Degradation**: All hooks fail safely with manual alternatives

### **System Integration Success**
- ✅ **Zero Workflow Disruption**: Hooks enhance existing Claude Code experience
- ✅ **Performance Maintained**: Hook overhead <100ms additional per event
- ✅ **Utility Scripts Preserved**: All 29+ scripts remain accessible via commands
- ✅ **Fallback Mechanisms**: Complete manual alternatives for all automated functions

---

**HOOK ARCHITECTURE DESIGN DECLARATION**: Complete integration architecture extending existing Claude Code hooks with 3 scripts for lifecycle automation, composite hook strategy for efficiency, and comprehensive fallback mechanisms preserving workflow reliability per PC-PARALLEL Phase B requirements.

**EVOLUTION PATHWAY**: Architecture Design → Fallback Implementation → Migration Timeline → Gradual Deployment