# ContextFlow v3 - Core Commands

## Principios Fundamentales Clarificados

**CONVERSACIÓN SOCRÁTICA**: Expansiva, sin restricciones - verdadero descubrimiento
**SLASH COMMANDS**: Ejecutivos, optimizados - acción post-descubrimiento  
**TOKEN ECONOMY**: Solo documentación/artefactos - invisible al usuario

## Arquitectura Refinada

### Flujo Orgánico Natural
```
Descubrimiento → Ejecución → Insights → Nuevo Descubrimiento → Nueva Ejecución...
```

**Sin fases "completas"** - crecimiento continuo con retroalimentación natural

### Sesión Retroalimentación (Recomendación)
```
1. CONFIRMACIÓN: "¿Los resultados coinciden con expectativas?"
2. INSIGHTS: "¿Qué te sorprendió? ¿Qué ves ahora que no veías antes?"  
3. FIJACIÓN: "¿Qué se vuelve 'regla' para situaciones futuras?"
```

## Core Commands Prototype

## Command: /analyze
```markdown
---
contextflow:
  next: ["visualize", "refactor", "document"]
  prev: ["explore"]
  triggers: ["analysis complete", "patterns identified", "issues found"]
---

Analyze codebase: $ARGUMENTS

EXECUTE:
1. Scan target files/directories
2. Identify patterns, issues, opportunities
3. Generate actionable insights

OUTPUT: 
- Issue count: X critical, Y warnings
- Top 3 patterns detected
- Max 3 priority recommendations

SUGGEST: Use /visualize for charts or /refactor for improvements
```

## Command: /refactor
```markdown
---
contextflow:
  next: ["test", "commit", "document"]
  prev: ["analyze"]
  triggers: ["refactoring complete", "code improved"]
---

Refactor code: $ARGUMENTS

EXECUTE:
1. Identify improvement opportunities
2. Apply best practices maintaining functionality
3. Verify changes work correctly

OUTPUT:
- Changes summary (max 50 words)
- Performance impact estimate
- Breaking changes: none/minor/major

SUGGEST: Use /test to validate or /commit to save progress
```

## Command: /test
```markdown
---
contextflow:
  next: ["commit", "deploy", "document"]
  prev: ["refactor", "implement"]
  triggers: ["tests passing", "coverage complete"]
---

Test implementation: $ARGUMENTS

EXECUTE:
1. Run existing tests
2. Add missing test coverage
3. Validate functionality

OUTPUT:
- Test status: X passed, Y failed
- Coverage: Z%
- New tests added: N

SUGGEST: Use /commit if all green or /debug if failures
```

## Command: /implement
```markdown
---
contextflow:
  next: ["test", "review", "integrate"]
  prev: ["design", "plan"]
  triggers: ["implementation complete", "feature ready"]
---

Implement feature: $ARGUMENTS

EXECUTE:
1. Create/modify necessary files
2. Follow established patterns
3. Add basic error handling

OUTPUT:
- Files modified: N
- New functionality: [brief description]
- Dependencies added: [list or none]

SUGGEST: Use /test next or /review for code quality check
```

## Command: /explore
```markdown
---
contextflow:
  next: ["analyze", "design", "understand"]
  triggers: ["exploration complete", "context gathered"]
---

Explore codebase: $ARGUMENTS

EXECUTE:
1. Navigate project structure
2. Understand architecture/patterns
3. Identify relevant components

OUTPUT:
- Project type: [detected stack]
- Key directories: [max 5]
- Main patterns: [max 3]

SUGGEST: Use /analyze for deep dive or /design for new features
```

## Command: /debug
```markdown
---
contextflow:
  next: ["test", "fix", "analyze"]
  prev: ["test"]
  triggers: ["bug identified", "fix applied"]
---

Debug issue: $ARGUMENTS

EXECUTE:
1. Reproduce the problem
2. Trace root cause
3. Suggest/apply fix

OUTPUT:
- Issue type: [category]
- Root cause: [brief explanation]
- Fix applied: [what was changed]

SUGGEST: Use /test to verify fix or /analyze if complex issue
```

## Auto-Sugerencia Engine

### Post-Command Response Template
```markdown
✅ [COMMAND] complete.

NEXT RECOMMENDED:
- /[primary-next] - [specific reason]
- /[alternative] - [different approach]
- /[optional] - [if time permits]

Type /[command] or describe next goal.
```

### Context-Aware Suggestions
```markdown
# Workflow detection examples:

EXPLORATION PHASE DETECTED:
- Project scan complete
- SUGGEST: /analyze for issues or /design for new work

IMPLEMENTATION PHASE DETECTED:  
- Code changes made
- SUGGEST: /test validation or /commit progress

DEBUGGING PHASE DETECTED:
- Tests failing
- SUGGEST: /debug root cause or /analyze patterns

ERROR STATE DETECTED:
- Build/tests broken
- SUGGEST: /debug immediate or /rollback if available
```

## Integration Example

### Usage Flow:
```bash
> /explore user-authentication
✅ Explore complete.
Project type: Node.js/Express + React
Key dirs: /auth, /middleware, /routes, /models, /tests
Patterns: JWT tokens, bcrypt hashing, role-based access

NEXT RECOMMENDED:
- /analyze - Deep dive security review  
- /implement - Add new auth feature
- /test - Validate existing auth flow

> /analyze auth security
✅ Analysis complete.
Issues: 2 critical, 3 warnings
Patterns: Consistent JWT usage, missing rate limiting, weak password policy
Recommendations: Add rate limiting, strengthen passwords, audit logs

NEXT RECOMMENDED:
- /refactor - Apply security improvements
- /implement - Add missing features  
- /document - Security documentation

> /refactor rate-limiting
✅ Refactoring complete.
Changes: Added express-rate-limit middleware, configured per-route limits
Performance: Minimal impact, prevents abuse
Breaking: None - backwards compatible

NEXT RECOMMENDED:
- /test - Validate rate limiting works
- /commit - Save security improvements
- /document - Update API docs
```

## Metadata Implementation

### Command Discovery
- Commands auto-registered from `.claude/commands/*.md`
- Metadata parsed from frontmatter
- Suggestions computed from `next`, `prev`, `triggers`

### Context Tracking
- Session state: current command, recent commands, workflow pattern
- Trigger detection: output analysis for completion phrases
- Suggestion ranking: relevance + recency + user patterns

### Personalization
- Track command sequences user prefers
- Learn which suggestions get accepted
- Adapt recommendations based on usage patterns