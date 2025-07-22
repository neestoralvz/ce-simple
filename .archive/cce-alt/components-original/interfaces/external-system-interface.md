# External System Interface

## 🎯 PURPOSE

**Interface Protocol**: Define cómo los componentes dentro de components/ interactúan con sistemas externos manteniendo autocontención.

### Core Principle
Components **NEVER** access external files directly - all external operations must go through this interface.

## 📋 AVAILABLE EXTERNAL OPERATIONS

### File Operations (Outside components/)
```
Interface.FileRead(external_path) → content
Interface.FileWrite(external_path, content) → status
Interface.FileList(external_directory) → file_list
Interface.FileExists(external_path) → boolean
```

### System Operations
```
Interface.BashExecute(command) → output
Interface.SystemControl(operation) → result
Interface.ProcessManagement(action) → status
```

### Web Operations
```
Interface.WebFetch(url, prompt) → content
Interface.WebSearch(query) → results
Interface.WebIntelligence(research_task) → analysis
```

### Tool Access (Claude Code Tools)
```
Interface.ToolAccess(tool_name, parameters) → result
Interface.BatchTools(tool_list) → results
Interface.ToolValidation(tool_result) → verified_result
```

## 🔧 USAGE PROTOCOL

### For Agents
```markdown
# ❌ PROHIBITED - Direct external access
Task("system/protocols/external-file.md")

# ✅ CORRECT - Via interface
Interface.FileRead("system/protocols/external-file.md")
```

### For Orchestrators
```markdown
# ❌ PROHIBITED - Direct external deployment
Task("system/agents/external-agent")

# ✅ CORRECT - Via interface coordination
Interface.ExternalCoordination(agent_type, mission, target)
```

### For Behaviors
```markdown
# ❌ PROHIBITED - Direct external file modification
Edit("../system/file.md", old, new)

# ✅ CORRECT - Via interface
Interface.FileWrite("system/file.md", new_content)
```

## 🎭 INTERFACE IMPLEMENTATION

### Request Format
```
Interface.[OPERATION](parameters) {
    → Validate request within components/ context
    → Log external operation for audit
    → Execute operation via appropriate Claude Code tool
    → Return result in standardized format
    → Update internal tracking metrics
}
```

### Response Format
```
{
    "operation": "[operation_name]",
    "status": "[success/error]",
    "data": "[operation_result]",
    "metadata": {
        "timestamp": "[execution_time]",
        "component": "[requesting_component]",
        "context_usage": "[percentage]"
    }
}
```

## 📊 EXTERNAL OPERATION TRACKING

### Audit Log Format
```
📊 [EXTERNAL] Interface.[OPERATION] | component:[name] | target:[external_path] | status:[result]
```

### Performance Metrics
- **External operations count**: Total external calls
- **Success rate**: Percentage of successful external operations  
- **Context impact**: Context usage per external operation
- **Response time**: Average external operation duration

## ⚠️ SECURITY & VALIDATION

### Access Control
- **Whitelist approach**: Only approved external paths allowed
- **Component validation**: Verify requesting component authority
- **Operation validation**: Ensure operation necessity and safety
- **Result sanitization**: Clean external data before internal use

### Error Handling
- **Graceful failures**: No component crashes on external errors
- **Fallback mechanisms**: Alternative approaches when external fails
- **Error reporting**: Standardized error communication
- **Recovery protocols**: Automatic retry and recovery procedures

## 🚀 IMPLEMENTATION GUIDELINES

### Phase 1: Interface Creation
1. Implement core interface functions
2. Create validation mechanisms
3. Establish audit logging
4. Test basic external operations

### Phase 2: Component Integration
1. Update components to use interface
2. Remove direct external references
3. Implement error handling
4. Test component isolation

### Phase 3: Performance Optimization
1. Cache frequent external operations
2. Batch related external calls
3. Optimize context usage
4. Monitor performance metrics

---

**This interface ensures complete self-containment while maintaining full access to external systems through a controlled, auditable, and optimized pathway.**