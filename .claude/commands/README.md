# VDD Commands - Core System

**Purpose**: Self-contained commands using Task Tool for parallel execution

## Command Philosophy (from user-input/)

**User Vision**: "Commands are crystallized intelligence that orchestrate parallel sub-agents via Task Tool to execute complex workflows through sophisticated coordination."

**Technical Reality**: 
- Task Tool enables up to 10 parallel sub-agents per command
- Commands must be self-contained (sub-agents can't access external files)
- All logic, patterns, templates embedded inline
- Real parallelization: 8-16 for searches, 5-10 for files, 4-8 for analysis

## Core Commands (Real Implementation)

### `/explore-codebase`
**Purpose**: Intelligent codebase exploration with parallel analysis
**Parallelization**: 8 concurrent search streams
**Real functionality**: Uses Task Tool to parallelize file exploration

### `/init-project`  
**Purpose**: Project initialization with Git WorkTrees setup
**Parallelization**: 5 concurrent setup operations
**Real functionality**: Creates real project structure

### `/start`
**Purpose**: Project analysis and guidance
**Parallelization**: 4 parallel analysis streams
**Real functionality**: Analyzes current state and provides guidance

## Implementation Standards

**All commands follow**:
1. Task Tool parallel execution (not simulated)
2. Self-contained logic (no external dependencies)
3. Real Git-based metrics
4. PTS Framework validation
5. Clear progress indication

---

**Truth**: These commands use real Task Tool parallelization, not architectural simulation.