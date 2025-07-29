# /intent - Semantic Command Dispatcher

**29/07/2025 16:40 CDMX** | Natural language to intelligent command routing

## Function
Parse natural language intent and automatically route to appropriate planning commands.

## Usage
```bash
/intent "quiero hacer una API con auth"
/intent "necesito una landing page responsive"  
/intent "CLI tool para gestionar archivos"
/intent "mobile app con backend"
/intent "estoy perdido, ¿qué hago?"
```

## Semantic Recognition Patterns

### Project Type Detection
**API/Backend Keywords:** "API", "backend", "server", "endpoints", "microservice"
→ **Routes to:** `/planning:init api-service`

**Frontend Keywords:** "landing", "website", "frontend", "UI", "interfaz", "página"
→ **Routes to:** `/planning:init web-frontend`

**Full-Stack Keywords:** "web app", "aplicación web", "fullstack", "completa"
→ **Routes to:** `/planning:init web-app`

**CLI Keywords:** "CLI", "command line", "terminal", "script", "herramienta"
→ **Routes to:** `/planning:init cli-tool`

**Mobile Keywords:** "mobile", "app móvil", "iOS", "Android", "celular"
→ **Routes to:** `/planning:init mobile-app`

### Intent Classification

#### Initialization Intent
**Keywords:** "quiero hacer", "necesito crear", "empezar", "iniciar", "nuevo proyecto"
**Action:** Project type detection → `/planning:init [detected-type]`
**Confidence threshold:** 80% for auto-execution

#### Status/Help Intent  
**Keywords:** "perdido", "¿qué hago?", "estado", "progreso", "help", "ayuda"
**Action:** Route to `/planning:status` or help system
**Fallback:** Show available commands and current project state

#### Continuation Intent
**Keywords:** "continuar", "seguir", "retomar", "donde quedé", "siguiente paso"
**Action:** Route to `/planning:focus` + `/planning:status`
**Context:** Load current project state and suggest next actions

#### Advancement Intent
**Keywords:** "terminé", "completé", "siguiente fase", "avanzar", "listo"
**Action:** Route to `/planning:gate` for layer validation
**Validation:** Check current layer completion before advancement

## Confidence-Based Routing

### High Confidence (80-100%)
```
🎯 Intent Detected: [Project Type] Initialization

Auto-executing: /planning:init [project-type]

Detected from: "[user input]"
Confidence: [X]%
```

### Medium Confidence (50-79%)
```
🤔 Possible Intent: [Project Type] Initialization

Suggested action: /planning:init [project-type]
Confidence: [X]%

Alternatives:
1. /planning:init [alternative-1]
2. /planning:init [alternative-2]
3. Custom specification

Proceed with suggestion? [Y/n]
```

### Low Confidence (< 50%)
```
❓ Intent Unclear - Need Clarification

I detected keywords: "[detected keywords]"
But couldn't determine specific project type.

Available project types:
• web-app - Full-stack web application
• api-service - Backend API service  
• web-frontend - Frontend application
• cli-tool - Command line tool
• mobile-app - Mobile application

Please specify: /planning:init [type]
Or describe your project in more detail.
```

## Advanced Pattern Recognition

### Context-Aware Detection
**Previous conversation:** Learn from session history for better intent understanding
**Project state:** If project already initialized, route to appropriate continuation commands
**User vocabulary:** Adapt to user's specific terminology over time

### Technology Stack Hints
**Backend tech:** "Node.js", "Python", "Django", "Express" → api-service
**Frontend tech:** "React", "Vue", "Angular", "HTML/CSS" → web-frontend  
**Mobile tech:** "React Native", "Flutter", "Swift", "Kotlin" → mobile-app
**CLI tech:** "Bash", "Python script", "Node CLI" → cli-tool

### Domain-Specific Recognition
**E-commerce:** "tienda", "shop", "ecommerce" → web-app with specific templates
**Analytics:** "dashboard", "métricas", "análisis" → web-app with data focus
**Automation:** "automatizar", "script", "batch" → cli-tool
**Content:** "blog", "CMS", "contenido" → web-frontend or web-app

## Fallback Strategies

### Unknown Project Types
**Learning opportunity:** Ask user to describe project for pattern learning
**Manual routing:** Show available project types for selection
**Custom template:** Offer to create custom layer structure

### Ambiguous Intent
**Clarifying questions:** Ask specific questions to narrow intent
**Multiple suggestions:** Offer top 2-3 possibilities with explanations
**Context gathering:** Request more details about project goals

### No Project Match
**Guidance mode:** Explain planning system and available project types
**Exploration mode:** Help user discover what type of project they want
**Custom assistance:** Offer to help define custom layer structure

## Integration Points

### Planning System Integration
**Seamless routing:** Direct integration with all /planning: commands
**State preservation:** Maintain context across command transitions
**Progress tracking:** Route to appropriate status/progress commands

### Learning System
**Pattern refinement:** Improve recognition based on successful routing
**Vocabulary expansion:** Learn user-specific terminology
**Context building:** Build understanding of user's project preferences

## Output Examples

### Successful Web-App Detection
```
🎯 Intent Detected: Full-Stack Web Application

Auto-executing: /planning:init web-app

📋 Project initialized with layers:
Layer 1: Database Foundation 🔄 ACTIVE
Layer 2: Backend Development ⏳ PENDING  
Layer 3: Frontend Development ⏳ PENDING
Layer 4: Integration & Deploy ⏳ PENDING

🎯 Current Focus: Layer 1 - Database Foundation
📋 Next: Design your data schema and establish database connections.
```

### Help Intent Response
```
🆘 Current Project Status:

📊 Project: ce-simple (Context Engineering Framework)
🎯 Current Focus: Layer 2 - System Crystallization  
📈 Progress: 35/38 files need ≤80 line refactoring

💡 Suggested next actions:
1. Continue modular refactoring: /workflows:start  
2. Check advancement readiness: /planning:gate
3. View detailed status: /planning:status
4. See all layers: /planning:layers

Need specific help? Describe what you're trying to do.
```

---
**Authority:** Semantic recognition methodology + intelligent command routing
**Integration:** → All planning commands, project initialization, natural language processing