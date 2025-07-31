# Semantic Planning - Intent-Driven Command Dispatch

**29/07/2025 16:10 CDMX** | Semantic command recognition and intelligent routing

## Core Innovation

**Problem:** Users must know exact commands vs natural intent expression
**Solution:** Semantic dispatcher que understands intent + auto-routes to appropriate planning

## Semantic Command Strategy

### /intent - Universal Dispatcher
**Function:** Natural language → project type detection → automatic planning initialization
**Examples:**
```bash
/intent "quiero hacer una API con auth"     → web-backend project
/intent "necesito una landing page"         → frontend project  
/intent "CLI tool para devs"               → cli-tool project
/intent "mobile app con database"          → mobile-fullstack project
```

### Semantic Recognition Patterns
**Project Type Detection:**
- "API", "backend", "server" → api-service template
- "website", "landing", "frontend" → web-frontend template
- "CLI", "command line", "tool" → cli-tool template
- "mobile", "app", "iOS", "Android" → mobile-app template
- "fullstack", "web app", "complete" → web-app template

**Intent Classification:**
- "quiero", "necesito", "crear" → project initialization intent
- "estoy en", "continuando", "siguiendo" → resume/status intent
- "terminé", "completé", "siguiente" → layer advancement intent
- "ayuda", "qué hacer", "stuck" → guidance/help intent

## Auto-Execution Flow

### 1. Intent Analysis
**Input:** Natural language user expression
**Process:** Semantic pattern matching + context analysis
**Output:** Project type + intent classification + confidence score

### 2. Automatic Planning Setup
**High confidence (>80%):** Auto-execute planning initialization
**Medium confidence (50-80%):** Suggest with confirmation
**Low confidence (<50%):** Ask clarifying questions

### 3. Intelligent Routing
**Initialization intent:** → `/planning:init {detected-type}`
**Resume intent:** → `/planning:focus` + `/planning:status`
**Advancement intent:** → `/planning:gate` validation
**Guidance intent:** → Show appropriate playbook/help

## Integration with Current System

### CLAUDE.md Semantic Triggers Enhancement
**Current triggers:** Pattern recognition based on explicit keywords
**Enhanced:** Natural language intent recognition + automatic command routing
**Addition:** 
```
### Intent/Planning Pattern
**Semantic triggers**: Natural language project expressions + intent to plan/organize + Domain any technical project + Output intelligent routing
**Auto-activation**: "quiero hacer", "necesito crear" → /intent activation automatic
**Execute**: Task tool → /intent analysis + appropriate planning command
**Validate**: Task tool → project setup correctness + user confirmation
```

### Command Ecosystem Integration
**Standalone operation:** /intent works independently
**Chain integration:** /intent → /planning:init → subsequent planning commands
**Context preservation:** Intent analysis informs all subsequent planning decisions

## Fallback Strategy

### When Semantic Detection Fails
**Graceful degradation:** Show available project templates for manual selection
**Learning opportunity:** Ask user to specify intent more clearly for pattern learning
**Manual override:** Always allow direct command execution as fallback

### Confidence Thresholds
**Auto-execute:** 80%+ confidence in project type detection
**Confirm first:** 50-80% confidence with suggested action
**Ask questions:** <50% confidence with clarification prompts

## Future Extension Capability

### Learning from Usage
**Pattern recognition improvement:** Track successful intent → command mappings
**Vocabulary expansion:** Learn project-specific terminology from user
**Context awareness:** Consider conversation history for better intent understanding

### Template Expansion
**New project types:** Easy addition of semantic patterns for new templates
**Domain-specific:** Industry-specific project type recognition
**Custom patterns:** User-defined intent → command mappings

---
## Enlaces → Información Complementaria
**Si necesitas dependency layers:** → context/operational/patterns/dependency_layers.md:15-45
**Si requieres command implementation:** → .claude/commands/planning/intent.md
**Si buscas semantic triggers:** → @context/architecture/core/truth-source.md:22-35

---
**Authority Source:** User semantic command need + conversation analysis insight
**Trazabilidad:** Conversation 29/07/2025 16:00 → Semantic dispatcher methodology