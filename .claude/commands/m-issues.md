# m-issues - Batch Issue Management

**31/07/2025 00:00 CDMX**

Efficient batch creation of multiple GitHub issues while maintaining conversation flow and ensuring template compliance per Issue #13 requirements.

## Core Functionality:
- **Parallel Processing**: Create multiple issues simultaneously without blocking
- **Template Validation**: Ensure all issues follow standardized structure from Issue #11
- **Natural Integration**: Seamless integration with conversation-first development
- **Error Handling**: Robust error handling with rollback capability

## Usage Patterns:

### 1. Interactive JSON Creation
When multiple issues emerge from conversation:
```
m-issues --interactive
```
- Guides through issue creation with prompts
- Automatically applies template structure
- Validates before creation

### 2. JSON File Input
For pre-defined issue sets:
```
m-issues path/to/issues.json [max_parallel]
```
- Reads structured JSON input
- Creates issues in parallel (default: 3 concurrent)
- Provides detailed progress feedback

### 3. Sample Generation
For learning the input format:
```
m-issues --sample [output_file.json]
```
- Generates sample JSON with proper structure
- Shows all available fields and options
- Ready-to-edit template

## Implementation Process:

### Step 1: Input Validation
1. **Template Structure Check**: Validate all required sections present
2. **Field Validation**: Ensure title, context, requirements, approach, success criteria
3. **JSON Format**: Verify proper JSON structure and syntax
4. **GitHub Auth**: Confirm GitHub CLI authentication

### Step 2: Parallel Execution
1. **Process Management**: Control concurrent issue creation (max 3 by default)
2. **Progress Tracking**: Real-time feedback on creation status
3. **Error Isolation**: Individual issue failures don't block others
4. **Resource Management**: Respect GitHub API rate limits

### Step 3: Results & Recovery
1. **Success Reporting**: List all successfully created issues with URLs
2. **Failure Analysis**: Detailed error reporting for failed issues
3. **Partial Success**: Continue with successful creations even if some fail
4. **Conversation Flow**: Return control to conversation immediately after completion

## JSON Input Format:

```json
{
  "issues": [
    {
      "title": "Issue Title",
      "context": "Background and problem description",
      "requirements": "Specific requirements list",
      "approach": "Implementation strategy",
      "success": "Success criteria and acceptance tests",
      "dependencies": "Dependencies or related work (optional)",
      "additional": "Additional context (optional)",
      "labels": ["label1", "label2"] // optional
    }
  ]
}
```

## Command Integration:
- **After q-explore**: Create issues for discovered work items
- **During w-plan**: Batch create issues for planned phases
- **With m-handoff**: Create multiple handoff-ready issues
- **Post q-research**: Convert research findings to actionable issues