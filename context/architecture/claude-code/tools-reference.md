# Claude Code Tools Reference - Agent Utilization Guide

**31/07/2025 CDMX** | Complete tool inventory and optimization patterns for agent utilization

## AUTORIDAD SUPREMA
@context/architecture/claude-code.md → tools-reference.md implements comprehensive tool documentation per research authority

## PRINCIPIO FUNDAMENTAL
**"Complete tool mastery enables maximum conversation-first development efficiency"** - Every Claude Code tool optimized for systematic agent utilization while preserving user authority supremacy.

## COMPLETE TOOL INVENTORY (14 Tools)

### 📁 FILE OPERATIONS CATEGORY (5 Tools)

#### **Read Tool** - Multi-Format File Access
- **Function**: Read text files, images, PDFs, Jupyter notebooks with line-specific access
- **Best Practices**: Always use before Edit operations, supports offset/limit for large files
- **Optimization**: Batch multiple file reads in parallel for efficiency
- **Authority**: OBLIGATORIO before any Edit/Write operation per CLAUDE.md

#### **Edit Tool** - Precise Single-File Modification  
- **Function**: Exact string replacement with unique matching requirements
- **Best Practices**: Read file first, ensure old_string uniqueness, preserve indentation
- **Optimization**: Use replace_all for systematic variable renaming
- **Authority**: Must preserve user authority through accurate content preservation

#### **MultiEdit Tool** - Atomic Multi-Operation Editing
- **Function**: Multiple edits in single transaction with rollback capability
- **Best Practices**: Sequential edit application, conflict prevention through careful planning
- **Optimization**: Preferred for multiple changes to same file over sequential Edit calls
- **Authority**: Atomic operations ensure authority preservation through consistency

#### **Write Tool** - File Creation/Overwriting
- **Function**: Complete file creation with overwrite capability
- **Best Practices**: Read existing file first if modifying, avoid proactive documentation creation
- **Optimization**: Use only when new files absolutely necessary
- **Authority**: Must serve user vision, never create unsolicited documentation

#### **LS Tool** - Directory Navigation
- **Function**: Directory listing with absolute paths, filtering support
- **Best Practices**: Use absolute paths, leverage ignore patterns for focused results
- **Optimization**: Verify parent directories before file operations
- **Authority**: Validation step ensuring accurate file location

### 🔍 SEARCH & NAVIGATION CATEGORY (3 Tools)

#### **Bash Tool** - Secure Shell Execution
- **Function**: Command execution with git integration, timeout management, persistent session
- **Best Practices**: Quote paths with spaces, avoid find/grep (use Grep/Glob instead), use ; or && for multiple commands
- **Optimization**: Batch operations in single call, maintain working directory through absolute paths
- **Authority**: Critical for git operations and system automation per infrastructure standards

#### **Glob Tool** - High-Performance Pattern Matching
- **Function**: Fast file pattern matching for any codebase size, modification time sorting
- **Best Practices**: Use for name-based searches, batch multiple patterns, leverage ** for recursive search
- **Optimization**: Preferred over Bash find commands for performance
- **Authority**: Essential for codebase exploration and pattern recognition

#### **Grep Tool** - Advanced Content Search
- **Function**: Ripgrep-powered content search with regex, file filtering, multiline support
- **Best Practices**: Use content output mode with context (-A/-B/-C), filter by type/glob patterns
- **Optimization**: Batch multiple searches, use multiline for cross-line patterns
- **Authority**: Primary tool for semantic pattern detection and content analysis

### 🌐 RESEARCH & WEB INTEGRATION CATEGORY (2 Tools)

#### **WebSearch Tool** - Real-Time Research  
- **Function**: Current information beyond knowledge cutoff, domain filtering support
- **Best Practices**: Account for current date in queries, use domain filtering strategically
- **Optimization**: Combine with WebFetch for comprehensive research pipeline
- **Authority**: Enables research-first methodology per methodology.md authority

#### **WebFetch Tool** - AI-Processed Content Retrieval
- **Function**: URL content fetching with AI processing, 15-minute cache, markdown conversion
- **Best Practices**: Use descriptive prompts for content extraction, handle redirects appropriately
- **Optimization**: Leverage caching for repeated access, combine with WebSearch for research
- **Authority**: Critical for evidence-based decision making and external validation

### 📋 TASK MANAGEMENT CATEGORY (2 Tools)

#### **TodoWrite Tool** - Task Planning & Progress Tracking
- **Function**: Task list creation with status tracking, session persistence, priority management
- **Best Practices**: Use proactively for complex tasks (3+ steps), mark completed immediately, limit to ONE in_progress task
- **Optimization**: Essential for conversation continuity and multi-session coordination
- **Authority**: OBLIGATORIO for systematic task tracking per methodology authority

#### **Task Tool** - Specialized Agent Orchestration
- **Function**: Deploy specialized subagents with context loading and autonomous execution
- **Best Practices**: Use detailed prompts with ROL + CONTEXTO + INSTRUCCIONES + TAREA structure
- **Optimization**: Deploy multiple agents concurrently for parallel processing
- **Authority**: Core orchestration tool per orchestration.md authority

### 🎯 SPECIALIZED TOOLS CATEGORY (3 Tools)

#### **NotebookRead/NotebookEdit Tools** - Jupyter Integration
- **Function**: Notebook viewing and modification with cell-specific access
- **Best Practices**: Use cell_id for specific targeting, leverage cell_type for appropriate content
- **Optimization**: Prefer over generic Read/Edit for .ipynb files
- **Authority**: Specialized tools ensure notebook integrity

#### **ExitPlanMode Tool** - Planning Workflow Management
- **Function**: User consultation for implementation approval after planning
- **Best Practices**: Use only after complete planning for implementation tasks, not research
- **Optimization**: Ensures user alignment before execution
- **Authority**: User consultation preserves vision supremacy

## OPTIMIZATION PATTERNS FOR AGENT UTILIZATION

### **Parallel Execution Excellence**
```
Optimal Pattern: Single message with multiple tool calls
- WebSearch + WebFetch + TodoWrite (research phase)
- Read + Read + Read (file analysis phase)  
- Edit + Edit + Bash (implementation phase)
- Grep + Glob + LS (discovery phase)
```

### **Research-to-Implementation Pipeline**
```
Phase 1: WebSearch + WebFetch (comprehensive research)
Phase 2: TodoWrite + Task (systematic planning) 
Phase 3: Read → Edit/MultiEdit → Bash (implementation)
Phase 4: Grep + LS (validation and testing)
```

### **Session Continuity Optimization**
```
Session Start: TodoWrite (task planning)
Progress Updates: TodoWrite (status tracking)
Context Restoration: Read (session files)
Session End: TodoWrite (completion marking)
```

## INTEGRATION WITH SYSTEM METHODOLOGY

### **Research-First Protocol Alignment**
- **WebSearch + WebFetch**: Enable systematic research per methodology.md
- **Think x4 Integration**: TodoWrite facilitates systematic analysis tracking
- **Evidence-Based Decisions**: Research tools provide empirical foundation

### **Authority Preservation Standards**
- **Read-Before-Edit**: OBLIGATORIO file operation validation
- **User Vision Supremacy**: All tool usage serves user authority
- **Context Preservation**: Tools maintain conversation-first development

### **Continuous Execution Integration**
- **No Friction Pauses**: Tool combinations eliminate workflow interruptions
- **Systematic Progression**: TodoWrite ensures complete task execution
- **Quality Gates**: Built-in validation through tool sequence optimization

## AGENT UTILIZATION RECOMMENDATIONS

### **For Research Tasks**
1. Start with WebSearch + WebFetch parallel research
2. Use TodoWrite for systematic analysis planning
3. Deploy Task tool for specialized research areas
4. Validate findings through Grep pattern analysis

### **For Implementation Tasks**
1. Always Read files before Edit/Write operations
2. Use MultiEdit for multiple changes to same file
3. Leverage Bash for git operations and automation
4. Track progress through TodoWrite continuous updates

### **For Discovery Tasks**
1. Combine Glob + Grep for comprehensive codebase exploration
2. Use LS for directory structure validation
3. Apply parallel search patterns for efficiency
4. Document findings through systematic tool usage

---

**TOOLS REFERENCE DECLARATION**: This comprehensive guide enables maximum Claude Code tool utilization while preserving user authority supremacy and conversation-first development through systematic optimization patterns.

**EVOLUTION PATHWAY**: Tool mastery → workflow optimization → conversation enhancement