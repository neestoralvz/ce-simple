# Plan Notification Standards - Visual Communication Authority

**31/07/2025 14:30 CDMX** | Standard notification formats for ExitPlanMode cuadros de plan

## AUTORIDAD SUPREMA
@context/architecture/ux-placement.md → plan-notification-standards.md implements plan notification consistency per UX authority

## PRINCIPIO FUNDAMENTAL
**"Badge format with double line breaks creates optimal visual hierarchy for plan notifications"** - Consistent, scannable, and prioritized visual communication within ExitPlanMode boxes.

## STANDARD BADGE FORMAT

### Template Structure
```markdown
`[EMOJI] [NIVEL]` [Descripción concisa]

`[EMOJI] [NIVEL]` [Descripción concisa]

`[EMOJI] [NIVEL]` [Descripción concisa]
```

### Format Requirements
- **Double line breaks** between each badge for optimal spacing
- **Backticks** around emoji + level for visual emphasis
- **Concise descriptions** - maximum 8-10 words after badge
- **Emoji-first hierarchy** - visual priority through color coding
- **3-8 items maximum** - scalable without crowding

## STANDARD EMOJI CODES

### Priority Levels (Color-based Hierarchy)
- `🔴 CRÍTICO` - **Blocks system/pipeline** - immediate action required
- `🟡 ACTIVO` - **In progress** - requires attention/monitoring  
- `🟢 LISTO` - **Available/completed** - ready for action
- `⚠️ ATENCIÓN` - **Requires review** - attention needed but not blocking

### Status Indicators (Function-based)
- `✅ COMPLETADO` - **Task/phase finished** - success confirmation
- `📈 CERCA` - **Significant progress** - nearing completion milestone
- `⚡ OPORTUNIDAD` - **Optional action available** - can be done in parallel
- `🎯 OBJETIVO` - **Primary goal/target** - main focus of plan

### Workflow States
- `📋 PLAN` - **Planning phase** - strategy being developed
- `🔄 PROCESO` - **Active execution** - currently being worked
- `⏸️ BLOQUEADO` - **Dependency blocked** - waiting for prerequisite
- `🚀 SIGUIENTE` - **Next action** - immediate next step

## USAGE GUIDELINES

### When to Use Badge Notifications in Plans
- **Status updates** on multiple work items
- **Priority communication** for action items
- **Progress indicators** for ongoing work
- **Dependency highlighting** for blocked items
- **Opportunity identification** for parallel work

### When NOT to Use Badge Format
- **Single item updates** - use regular markdown emphasis
- **Detailed explanations** - use structured sections instead
- **Code or technical details** - use code blocks or tables
- **Long descriptions** - break into bullet points or sections

## EXAMPLES IN CONTEXT

### Example 1: Roadmap Status Update
```markdown
`🔴 CRÍTICO` P0B-CLEANUP al 45% bloqueando pipeline

`🟡 ACTIVO` PC-PARALLEL progresando al 53%

`✅ LISTO` 8 issues independientes disponibles

`📈 CERCA` H6 con 27% reducción adicional
```

### Example 2: Action Items Priority
```markdown
`🎯 OBJETIVO` Completar validación de compliance

`⚡ OPORTUNIDAD` Trabajar issues paralelos mientras esperamos

`⚠️ ATENCIÓN` Dependencies P0B → P1 requieren review

`🚀 SIGUIENTE` Preparar P1-UX-FIX una vez P0B complete
```

### Example 3: Progress Monitoring
```markdown
`✅ COMPLETADO` GitHub Issues workflow mejorado

`📋 PLAN` Conversation completion assessment diseñado

`🔄 PROCESO` Integration testing en curso

`📈 CERCA` Protocol validation al 85%
```

## INTEGRATION WITH SYSTEM

### Relationship to Post-Execution Notifications
**Plan Notifications**: Propose what will be done (future-focused)
**Post-Execution Notifications**: Report what was accomplished (result-focused)

**Plan Format**: `🔴 CRÍTICO` P0B-CLEANUP bloqueando pipeline
**Post-Execution Format**: ✅ P0B-CLEANUP completado - 157 violations resolved

### Consistency Standards
- **Same emoji codes** across plan and execution contexts
- **Similar priority hierarchy** maintained throughout system
- **Visual coherence** between planning and results communication
- **Scalable formatting** works in both contexts

## QUALITY STANDARDS

### Visual Hierarchy Requirements
- **Priority emojis first** (🔴 > 🟡 > 🟢)
- **Status emojis second** (✅, 📈, ⚡, ⚠️)
- **Workflow emojis last** (📋, 🔄, ⏸️, 🚀)
- **Consistent ordering** within each category

### Content Quality Gates
- **Concise descriptions** - avoid redundancy
- **Action-oriented language** - focus on what's happening/needed
- **Specific details** - avoid vague status updates
- **User-relevant information** - focus on impact and next steps

---

**PLAN NOTIFICATION STANDARDS DECLARATION**: This standard ensures consistent, scannable, and prioritized visual communication within ExitPlanMode boxes through badge format with double line breaks and systematic emoji coding.

**EVOLUTION PATHWAY**: User feedback → format refinement → emoji code expansion → visual hierarchy optimization