# p-init - Project Construction Initialization

**31/07/2025 00:00 CDMX** | Initialize dependency layers for any project type

## Function
Initialize construction layers and dependency management for specified project type.

## Usage
```bash
p-init [project-type]
p-init web-app
p-init cli-tool  
p-init api-service
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
**File creation:** Update context/architecture/core/methodology.md with project initialization
**Project tracking:** Record project type and initial state
**Authority chain:** Reference appropriate project template documentation

### Command Ecosystem Integration
**Subsequent commands:** Enable p-layers, p-gate, p-focus
**Status accessibility:** Make project state available to all planning commands
**Validation preparation:** Set foundation for systematic layer advancement

## Output Format

### Successful Initialization
## Core Function
Initialize project with dependency-based construction layers and set current focus to Layer 1

**Features**: Project type detection + layer template loading + state persistence + integration with planning commands

---
**Authority:** Planning initialization methodology + dependency layers framework
**Integration:** → p-layers, p-gate, p-focus, p-status