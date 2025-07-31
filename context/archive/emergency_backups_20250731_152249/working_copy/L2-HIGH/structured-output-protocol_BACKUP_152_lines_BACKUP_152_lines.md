# Structured Output Protocol - Data-Driven Communication Authority

**31/07/2025 CDMX** | Enhanced communication protocol for structured script outputs

## AUTORIDAD SUPREMA
@context/architecture/standards/script-communication-protocol.md → structured-output-protocol.md implements enhanced structured communication per refined analysis

## PRINCIPIO FUNDAMENTAL
**"Scripts generate structured data, Claude Code provides contextual interpretation"** - Balance between technical data processing and natural user communication through structured formats.

## REFINED COMMUNICATION CATEGORIES

### **Category 1: Pure Technical Scripts** (Silent Processing)
Scripts that perform technical operations without user-facing results:
- File processing utilities
- Data transformation scripts  
- System maintenance scripts
- **Protocol**: No user output, only technical data/logs

### **Category 2: Analysis & Validation Scripts** (Structured Output)
Scripts that generate results requiring user interpretation:
- Validation and compliance checking
- Analysis and reporting scripts
- Status and summary generators  
- **Protocol**: Structured output (JSON/CSV) + Claude interpretation

### **Category 3: Interactive Scripts** (Special Handling)
Scripts requiring user input or confirmation:
- Configuration setup scripts
- Emergency diagnostic tools
- User preference collectors
- **Protocol**: Maintain interactivity with clear separation

## STRUCTURED OUTPUT FORMATS

### **JSON Output Pattern** (Preferred)
```bash
# Generate structured JSON for Claude Code interpretation
cat << EOF
{
    "timestamp": "$(date -Iseconds)",
    "operation": "validation",
    "status": "completed",
    "metrics": {
        "files_processed": $processed,
        "violations_found": $violations,
        "success_rate": $((success * 100 / total))
    },
    "details": [
        {"file": "path1", "status": "compliant", "lines": 75},
        {"file": "path2", "status": "violation", "lines": 125}
    ]
}
EOF
```

### **CSV Output Pattern** (Alternative)
```bash
# Generate CSV for tabular data
echo "file,status,lines,domain,priority"
echo "$file_path,$status,$line_count,$domain,$priority"
```

### **Status Code Pattern** (Simple)
```bash
# Simple status with error code
echo "$processed|$success|$failed|$(date)"
exit 0  # 0=success, 1=warnings, 2=errors
```

## CLAUDE CODE INTERPRETATION FRAMEWORK

### **Data Processing & Communication**
Claude Code receives structured output and provides:
- **Contextual explanation**: "He ejecutado la validación de 47 archivos..."
- **Business context**: "Encontré 12 violaciones que requieren atención..."
- **Action recommendations**: "Sugiero procesar primero los 5 archivos críticos..."
- **Progress updates**: "El sistema está 85% compliant con los estándares..."

### **Error Handling & User Guidance**
- **Technical errors**: Script exit codes indicate issues
- **User communication**: Claude explains technical problems in natural language
- **Recovery suggestions**: Claude provides actionable next steps
- **Context preservation**: All communication maintains conversation flow

## IMPLEMENTATION STRATEGY

### **Phase 1: Identify Script Categories**
- **Audit existing scripts** to determine proper category
- **Pure technical**: Convert to silent processing
- **Analysis/validation**: Implement structured output
- **Interactive**: Maintain special handling

### **Phase 2: Implement Structured Outputs**
- **JSON templates** for complex validation scripts
- **CSV formats** for tabular analysis results
- **Status codes** for simple operation results
- **Error handling** with proper exit codes

### **Phase 3: Claude Code Integration**
- **Output parsing**: Claude reads and interprets structured data
- **Natural communication**: Claude translates technical results to user language
- **Context maintenance**: All communication preserves conversation flow
- **Action guidance**: Claude provides user-appropriate recommendations

## VALIDATION CHECKLIST

### **Script Compliance**
- ✅ Category properly identified (technical/analysis/interactive)
- ✅ Appropriate output format implemented (JSON/CSV/status)
- ✅ No direct user communication in analysis scripts
- ✅ Proper error codes and handling

### **Communication Quality**
- ✅ Claude Code interprets all structured outputs
- ✅ Natural language explanation of technical results
- ✅ Business context provided for all findings
- ✅ User authority and conversation flow preserved

## EXAMPLE TRANSFORMATIONS

### **Before (Direct Communication):**
```bash
echo "🔍 Analyzing 47 files..."
echo "Found 12 violations requiring attention"
echo "Critical: 3 files, High: 5 files, Medium: 4 files"
echo "Recommendation: Process critical files first"
```

### **After (Structured Output):**
```bash
cat << EOF
{
    "files_analyzed": 47,
    "violations": {
        "total": 12,
        "critical": 3,
        "high": 5,
        "medium": 4
    },
    "recommendation": "process_critical_first"
}
EOF
```

**Claude Code then communicates:**
"He analizado 47 archivos y encontré 12 violaciones que requieren atención. Hay 3 archivos críticos, 5 de alta prioridad, y 4 de prioridad media. Recomiendo procesar primero los archivos críticos para resolver los problemas más importantes."

---

**STRUCTURED OUTPUT DECLARATION**: This enhanced protocol balances technical data processing with natural user communication through structured formats, enabling both precise data handling and conversation-first development principles.

**EVOLUTION PATHWAY**: Script categorization → structured output implementation → Claude Code interpretation → natural user communication