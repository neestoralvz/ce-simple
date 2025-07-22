# Analyze-Parallel - Parallelization Opportunity Detection & Optimization

## 🎯 Purpose
Detect parallelization opportunities and optimize performance through intelligent workload analysis and resource allocation.

## 🚀 Usage
Execute: `/analyze-parallel [detect|optimize|benchmark] [parameters]`

## 🔧 Implementation

### Autocontained Notification System
```bash
#!/bin/bash
readonly B='\e[34m' G='\e[32m' R='\e[31m' Y='\e[33m' C='\e[36m' M='\e[35m' GB='\e[32;1m' N='\e[0m'
info()     { echo -e "${B}🔵 INFO${N}: $1"; }
success()  { echo -e "${G}🟢 SUCCESS${N}: $1"; }  
error()    { echo -e "${R}🔴 ERROR${N}: $1"; }
warn()     { echo -e "${Y}🟡 WARNING${N}: $1"; }
process()  { echo -e "${C}⚡ PROCESS${N}: $1"; }
data()     { echo -e "${M}📊 DATA${N}: $1"; }
complete() { echo -e "${GB}✅ COMPLETE${N}: $1"; }
```

### Parallelization Detection Protocol
**Real-Time Analysis Framework**:
```javascript
// 1. WORKLOAD ANALYSIS (real execution)
Grep("parallel|concurrent|async|Promise\\.all", {glob: "**/*.{js,ts,py,sh}", output_mode: "count"}) // Count parallel patterns
Grep("for\\s*\\(|while\\s*\\(|map\\s*\\(|forEach", {glob: "**/*.{js,ts,py}", output_mode: "files_with_matches"}) // Find iteration patterns
Bash("find . -type f -name '*.{js,ts,py,sh}' -exec wc -l {} + | sort -nr | head -20") // Identify large files

// 2. PERFORMANCE BOTTLENECK DETECTION (real execution)
Grep("\\b(await|sleep|delay|timeout|throttle)\\b", {glob: "**/*.{js,ts,py}", output_mode: "content", "-n": true}) // Find blocking operations
Grep("sync|blocking|sequential", {glob: "**/*.{js,ts,py,md}", output_mode: "files_with_matches"}) // Find sequential patterns

// 3. OPTIMIZATION OPPORTUNITY SCORING (real execution)
Task("Performance analysis", "analyze codebase for parallelization opportunities and generate optimization recommendations")
```

### Optimization Strategy Framework
**Intelligent Resource Allocation**:
- **Pattern Detection**: Identify sequential operations that can be parallelized
- **Dependency Analysis**: Map operation dependencies and execution chains
- **Resource Assessment**: Evaluate available processing capacity
- **Optimization Scoring**: Rank improvements by impact/effort ratio

### Performance Benchmarking Protocol
**Measurement Integration**:
```javascript
// Performance tracking integration with /track-performance
Bash("if [[ -f tools/performance-tracker.json ]]; then echo 'Performance baseline available'; fi") // Check baseline
Task("Benchmark execution", "measure current performance metrics and establish optimization targets")
```

## ⚡ Triggers

### Input Triggers
**Context**: Performance optimization, parallelization analysis, bottleneck detection
**Keywords**: parallel, concurrent, optimization, performance, bottleneck, async

### Output Triggers
**When**: Optimization opportunities detected → Generate implementation recommendations
**Chain**: analyze-parallel → track-performance → monitor-dev (for validation)

## 🔗 Module Integration

### Command Dependencies
**Performance Suite**:
- `/track-performance` → Baseline metrics and benchmarking
- `/monitor-dev` → Real-time optimization validation
- `/git-worktree` → Isolated optimization testing environment

### Success Indicators
**Optimization Success**: >20% performance improvement in identified bottlenecks
**Detection Success**: 90%+ coverage of parallelizable operations identified
**Implementation Success**: Recommendations successfully applied with measurable gains

## ⚡ EXECUTION LAYER

### Mandatory Tool Executions
```javascript
// 1. CODEBASE SCANNING (real execution)
Glob("**/*.{js,ts,py,sh,go,rs}", {path: "."}) // Find all code files
Grep("(for|while|map|forEach|Promise|async|await)", {glob: "**/*.{js,ts}", output_mode: "count"}) // Count async patterns

// 2. BOTTLENECK DETECTION (real execution)
Grep("\\b(sleep|delay|timeout|block|sync|sequential)\\b", {glob: "**/*", output_mode: "files_with_matches"}) // Find blocking patterns
Task("Bottleneck analysis", "systematic analysis of performance bottlenecks and optimization opportunities")

// 3. OPTIMIZATION SCORING (real execution)  
Bash("echo 'Parallelization analysis: $(date)' >> tools/performance-tracker.json") // Log analysis session
```

---

**CRITICAL**: This command provides intelligent parallelization analysis with real tool execution and measurable optimization recommendations.