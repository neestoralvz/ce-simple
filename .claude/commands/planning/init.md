# /planning:init - Project Construction Initialization

**29/07/2025 16:15 CDMX** | Initialize dependency layers for any project type

## Function
Initialize construction layers and dependency management for specified project type.

## Usage
```bash
/planning:init [project-type]
/planning:init web-app
/planning:init cli-tool  
/planning:init api-service
```

## Supported Project Types

### web-app (Full Stack Web Application)
**Layers:** Database → Backend → Frontend → Integration → Distribution
**Dependencies:** Schema stable before APIs, APIs stable before components
**Validation:** Each layer must pass readiness gate before advancement

### cli-tool (Command Line Tool)  
**Layers:** Core Logic → Commands → Configuration → Packaging → Distribution
**Dependencies:** Business logic before interface, interface before config
**Validation:** Core functionality proven before command wrapping

### api-service (Backend API Service)
**Layers:** Schema → Endpoints → Security → Testing → Distribution  
**Dependencies:** Data models before routes, routes before auth
**Validation:** API functionality before security implementation

### mobile-app (Mobile Application)
**Layers:** Design → Backend → App Development → Testing → Store
**Dependencies:** UI/UX decisions before backend, backend before app
**Validation:** Service layer stable before mobile integration

## Execution Protocol

### 1. Project Type Validation
**Input validation:** Verify project type is supported template
**Fallback:** Show available project types if invalid/missing
**Context preservation:** Store project type for subsequent planning commands

### 2. Layer Structure Creation
**Load template:** Apply dependency structure for chosen project type
**Create tracking:** Initialize current layer focus (always Layer 1)
**Generate readiness gates:** Set validation criteria for each layer

### 3. Project State Initialization  
**Status tracking:** Create project progress tracking system
**Focus setting:** Set current layer focus to Layer 1 (Foundation)
**Validation setup:** Prepare readiness gate criteria for advancement

## Integration Points

### Context Planning Update
**File creation:** Update context/planning/current.md with project initialization
**Project tracking:** Record project type and initial state
**Authority chain:** Reference appropriate project template documentation

### Command Ecosystem Integration
**Subsequent commands:** Enable /planning:layers, /planning:gate, /planning:focus
**Status accessibility:** Make project state available to all planning commands
**Validation preparation:** Set foundation for systematic layer advancement

## Output Format

### Successful Initialization
```
✅ Project initialized: [project-type]

📋 Construction Layers Defined:
Layer 1: [Foundation description] 🔄 ACTIVE
Layer 2: [Second layer] ⏳ PENDING  
Layer 3: [Third layer] ⏳ PENDING
Layer 4: [Final layer] ⏳ PENDING

🎯 Current Focus: Layer 1 - [Foundation description]
📋 Next: Work within Layer 1. Use /planning:gate when ready to advance.
```

### Error States
- **Missing project type:** Show available templates + usage example
- **Invalid project type:** Suggest closest match + show supported types  
- **Already initialized:** Show current state + ask if user wants to reinitialize

## Templates Reference

**Template loading:** → context/planning/project_templates/[type].md
**Dependency reference:** → context/planning/dependency_layers.md
**Authority source:** → context/TRUTH_SOURCE.md planning patterns

---
**Authority:** Planning initialization methodology + dependency layers framework
**Integration:** → /planning:layers, /planning:gate, /planning:focus, /planning:status