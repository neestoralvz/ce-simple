# Writing Standards - Clear Communication

**Purpose**: Standardized writing guidelines for natural language instructions and documentation

## Core Principles

**≤15 Words Rule**: Keep instructions concise and actionable
- Maximum 15 words per instruction or bullet point
- Focus on single, clear action per statement
- Eliminate unnecessary words and redundancy

**Natural Language**: Write for Claude Code execution clarity
- Use direct, imperative language
- Avoid technical jargon when simpler terms work
- Structure for immediate comprehension and action

**Optimal Granularity**: Balance detail with usability
- Provide enough detail for accurate execution
- Avoid overwhelming with excessive specificity
- Group related actions logically

## Instruction Writing

### Structure Guidelines
**Format**: Action + Target + Context (when needed)

**Examples**:
- ✅ "Create new component in src/components directory"
- ✅ "Analyze performance bottlenecks using profiling tools"
- ❌ "You should create a new component file in the src/components directory if one doesn't already exist"

### Word Economy
**Essential Elements Only**:
- Action verb (required)
- Target object (required)  
- Location/context (when necessary)
- Method/tool (when specific approach needed)

**Eliminate**:
- Filler words: "please", "just", "simply", "go ahead and"
- Redundant phrases: "make sure to", "be sure that"
- Uncertain language: "maybe", "perhaps", "you might want to"

## Documentation Standards

### Section Structure
**Hierarchy**: Use consistent heading levels
- H1: Document title
- H2: Major sections (Overview, Implementation, Reference)
- H3: Subsections within major areas
- H4: Specific details and examples

### Content Flow
**Progressive Disclosure**:
1. Purpose statement (what and why)
2. Quick start (immediate action)
3. Implementation details (how to)
4. Reference information (supporting details)

### Clarity Techniques
**Active Voice**: Use active rather than passive construction
- ✅ "Execute the command to analyze performance" 
- ❌ "Performance can be analyzed by executing the command"

**Parallel Structure**: Maintain consistent phrasing in lists
- ✅ "Create, test, deploy" or "Creating, testing, deploying"
- ❌ "Create, testing, deployment"

## Command Writing

### Task Instructions
**Direct Commands**: Write as if instructing Claude Code directly
- "Read file contents from specified path"
- "Execute grep search across codebase"
- "Generate summary with key findings"

### Error Prevention
**Specific Paths**: Always use absolute file paths
- ✅ "/Users/project/src/components/Button.tsx"
- ❌ "src/components/Button.tsx"

**Clear Parameters**: Specify required vs. optional parameters
- ✅ "Search pattern (required), file type (optional)"
- ❌ "Search for pattern in files"

## Validation Examples

### Effective Instructions
```
✅ Read configuration file from project root
✅ Search for TODO comments in TypeScript files  
✅ Create backup before modifying original files
✅ Execute tests and report failures with line numbers
```

### Ineffective Instructions
```
❌ Please go ahead and read the configuration file from the project root directory
❌ You should search through all the TypeScript files to find any TODO comments
❌ Make sure to create a backup copy before you start modifying the original files
❌ Run the test suite and provide a detailed report of any failures including line numbers
```

### Documentation Examples
```
✅ **Quick Start**: Copy template and customize for specific needs
✅ **Implementation**: Follow 4-phase execution pattern
✅ **Validation**: Check requirements using provided checklist

❌ **Getting Started**: To begin using this system, you should copy the template file and then customize it according to your specific requirements and use case
```

## Validation Checklist

- [ ] Instructions ≤15 words each
- [ ] Natural language for Claude Code clarity
- [ ] Active voice used consistently
- [ ] Specific, actionable statements
- [ ] Absolute file paths provided
- [ ] Consistent parallel structure in lists
- [ ] Progressive disclosure in documentation
- [ ] Essential information only, no filler words