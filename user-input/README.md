# User Input - Sacred User Space

**Purpose**: This directory contains ALL content directly provided by the user. This is Sacred User Space - AI agents must never modify, interpret, or add content here except for literal transcriptions of user interviews.

## Authority Hierarchy

**user-input/** = **Absolute Authority** - Source of truth for all project decisions
**docs/** = Implementation derived from this source

## Directory Structure

### `/vision/`
Pure conceptual content from user:
- Philosophy and methodology 
- Core concepts and principles
- User's vision for the system
- Organic, conversational user thoughts

### `/technical-requirements/`
Technical specifications mentioned by user:
- Technical decisions made by user
- Architecture preferences expressed by user
- Implementation constraints specified by user
- Technical vision from user perspective

### `/evolution/`
User feedback and context evolution:
- Interview transcriptions (literal)
- User feedback sessions
- Evolution of thinking over time
- Retrospective insights from user

### `/context/`
User feedback sessions via interview command:
- Systematic feedback capture (logros, desafios, errores, obstaculos, aprendizajes)
- Session-based retrospectives
- VDD framework performance assessment
- User satisfaction and improvement suggestions

## Sacred Space Rules

1. **AI Never Modifies**: Agents cannot edit, improve, or interpret content in this space
2. **User Authority**: Only direct user input or literal transcriptions allowed
3. **Organic Content**: Preserves conversational, unstructured user thoughts
4. **Source of Truth**: Maximum authority for all project creation decisions

## Content Flow

```
User Says Something → user-input/ (literal preservation)
                   ↓
AI Interprets/Implements → docs/ (structured derivatives)
```

**Duplication Expected**: Content appears in both spaces - organic source here, structured implementation in docs/

---

**Core Principle**: This space preserves the authentic user voice that drives all Vision Driven Development.