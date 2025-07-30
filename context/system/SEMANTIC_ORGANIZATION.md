# SEMANTIC_ORGANIZATION.md - File Organization Authority

**29/07/2025 16:45 CDMX** | Single source of truth para semantic file organization

## AUTORIDAD SUPREMA
Este archivo define la organización semántica de TODOS los archivos del sistema

## STORAGE PATHS CONFIGURATION

### Core Storage Variables
```yaml
# Primary storage locations
CONVERSATION_STORAGE: "context/archive/conversations_processed"  # Processed conversation archives only
CONTEXT_OPERATIONAL: "context/operational"     # Living system patterns & behaviors  
CONTEXT_ARCHIVE: "context/archive"            # Historical preservation & processed content
CONTEXT_SYSTEM: "context/system"              # System configuration & templates
PLANNING_ACTIVE: "context/planning"           # Current work & active planning

# Specialized directories  
SYSTEM_TEMPLATES: "context/system/templates"  # Reusable command & content templates
USER_VISION: "context/archive/user-vision-layers" # User vision distillation layers
```

## CONDITIONAL ROUTING RULES

### Session & Conversation Management
```yaml
# Session operations → Conversation storage
IF: conversation_close OR session_end
→ STORE_IN: ${CONVERSATION_STORAGE}/[timestamp]_[session-description].md

# Session analysis & compacting results  
IF: actions:compact OR session_analysis
→ STORE_IN: ${CONVERSATION_STORAGE}/[timestamp]_[analysis-type].md
```

### Knowledge & Pattern Management
```yaml
# Pattern discovery → Operational context
IF: pattern_discovery OR methodology_update OR behavior_definition
→ UPDATE: ${CONTEXT_OPERATIONAL}/patterns/[pattern-name].md
→ OR: ${CONTEXT_OPERATIONAL}/behaviors/[behavior-name].md

# Knowledge integration → Operational operations
IF: knowledge_integration OR protocol_definition  
→ UPDATE: ${CONTEXT_OPERATIONAL}/operations/[operation-name].md
```

### System Configuration
```yaml  
# Template creation → System templates
IF: template_creation OR command_template OR role_template
→ STORE_IN: ${SYSTEM_TEMPLATES}/[template-type]/[template-name].md

# System configuration → System directory
IF: system_configuration OR organization_rules OR anti_patterns
→ STORE_IN: ${CONTEXT_SYSTEM}/[config-name].md
```

### Planning & Coordination
```yaml
# Active planning → Planning directory
IF: planning_update OR current_status OR active_coordination
→ UPDATE: ${PLANNING_ACTIVE}/[planning-file].md

# Historical planning → Archive
IF: planning_completion OR milestone_achieved
→ MOVE: ${PLANNING_ACTIVE}/[file] → ${CONTEXT_ARCHIVE}/[timestamp]_[file]
```

### Content Processing & Archive
```yaml
# Content processing → Archive with processing status
IF: content_processed OR distillation_complete OR insights_extracted  
→ MOVE: ${CONVERSATION_STORAGE}/[file] → ${CONTEXT_ARCHIVE}/conversations_processed/[file]

# User vision distillation → Vision layers
IF: vision_distillation OR user_voice_crystallization
→ STORE_IN: ${USER_VISION}/layer[N]/[vision-aspect].md
```

## SEMANTIC ORGANIZATION PRINCIPLES

### Content-Based Classification
- **Conversations**: Raw session content, immediate outputs, dialogue preservation
- **Operational**: Living system knowledge, patterns in active use, current behaviors  
- **Archive**: Processed content, historical reference, completed cycles
- **System**: Configuration, templates, organizational rules, static structure
- **Planning**: Active coordination, current work, forward-looking content

### Lifecycle Management
```yaml
# Content evolution pathway
Raw Session → Conversation Storage → Processing → Operational Integration → Archive Preservation

# Living vs Historical distinction  
Living: content/operational/ (actively referenced, current system state)
Historical: context/archive/ (reference, processed, completed cycles)
```

### Access Patterns
- **Frequent Access**: conversations/, context/operational/, context/planning/
- **Reference Access**: context/system/, context/archive/
- **Template Access**: context/system/templates/

## FILE NAMING CONVENTIONS

### Timestamp Format
```yaml
# Session files: YYYYMMDD_HHMM_[description].md
20250729_1645_semantic-organization-implementation.md

# Non-session files: [semantic-name].md  
orchestrator_methodology.md
authority_framework.md
```

### Semantic Naming
- **Descriptive over cryptic**: `authority_framework.md` > `auth.md`
- **Function over implementation**: `orchestration_protocol.md` > `multi_agent_coordinator.md`
- **Consistent separators**: Use `_` for multi-word files, `-` for session descriptions

## INTEGRATION WITH CLAUDE CODE

### Expected Behavior
```yaml
# Claude Code should read these variables and route files accordingly
IF: Claude Code creates conversation file
→ CHECK: ${CONVERSATION_STORAGE} variable
→ CREATE: file in conversations/ directory

# All system operations should respect semantic paths
IF: Any file operation by system commands
→ CONSULT: this authority file for correct path
→ ROUTE: according to conditional rules
```

### Fallback Handling
```yaml
# If variables not readable
→ FALLBACK: to current directory structure
→ LOG: configuration read failure for debugging
→ PRESERVE: functionality while attempting path resolution
```

## VALIDATION RULES

### Path Consistency  
- All storage paths MUST exist as directories
- No hardcoded paths in command files - reference variables only
- Variables MUST be readable by Claude Code system

### Content Integrity
- File moves preserve content exactly  
- Timestamp integrity maintained during transitions
- Cross-references updated during path changes

---

**AUTHORITY CHAIN**: This file → CLAUDE.md → All system file operations
**INTEGRATION**: Referenced by CLAUDE.md sistema configuración
**EVOLUTION**: Update this file to change system-wide file organization behavior