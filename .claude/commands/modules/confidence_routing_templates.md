# Confidence Routing Templates Module

## High Confidence Template (80-100%)
```
🎯 Intent Detected: [Project Type] Initialization

Auto-executing: /planning:init [project-type]

Detected from: "[user input]"
Confidence: [X]%
```

## Medium Confidence Template (50-79%)
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

## Low Confidence Template (< 50%)
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

## Successful Detection Template
```
🎯 Intent Detected: [Project Type]

Auto-executing: /planning:init [project-type]

📋 Project initialized with layers:
Layer 1: [Layer 1 Name] 🔄 ACTIVE
Layer 2: [Layer 2 Name] ⏳ PENDING  
Layer 3: [Layer 3 Name] ⏳ PENDING
Layer 4: [Layer 4 Name] ⏳ PENDING

🎯 Current Focus: Layer 1 - [Description]
📋 Next: [Next action description]
```

## Help Intent Response Template
```
🆘 Current Project Status:

📊 Project: [project-name] ([project-description])
🎯 Current Focus: Layer [X] - [layer-name]
📈 Progress: [status description]

💡 Suggested next actions:
1. [Primary action]: [command]
2. [Secondary action]: [command]
3. [Tertiary action]: [command]

Need specific help? Describe what you're trying to do.
```

**Usage**: Confidence-based response templates for semantic intent routing