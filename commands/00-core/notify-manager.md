# /notify-manager - Central Notification System

## Purpose

Provide centralized notification management for transparent delegation, task handoffs, and system state changes to ensure complete visibility across agents, sessions, and workflow transitions in the ce-simple orchestration system.

## Principles and Guidelines

- **Transparent Operations**: All delegations, handoffs, and state changes generate clear notifications with context
- **Centralized Tracking**: Maintain single source of truth for system notifications and status updates  
- **Intelligent Routing**: Route notifications to appropriate agents, sessions, or documentation systems automatically
- **Audit Trail**: Create permanent record of all system interactions for debugging and optimization

## Execution Process

### Phase 1: Notification Infrastructure
Use TodoWrite to establish notification tracking system. Create notification categories (delegation, handoff, status, error, completion) and define routing rules for each type. Establish notification storage and retrieval patterns.

### Phase 2: Integration Points
Integrate notification triggers into existing commands and workflows. Add notification calls to key system operations including task delegation, agent handoffs, context updates, and completion events. Test notification flow across command boundaries.

### Phase 3: Transparency Protocols
Implement user-facing notification display and system status reporting. Create notification consolidation and summary functions. Establish real-time status updates for long-running operations and parallel task execution.

### Phase 4: Management Interface
Create notification management commands for viewing, filtering, and clearing notifications. Implement notification analytics and pattern detection. Establish notification-based debugging and system health monitoring capabilities.

---

**Single Responsibility**: Manage centralized notifications for transparent delegation and system state tracking.