#!/bin/bash

# CE-Simple Real-Time Monitoring Hook
# Captures Claude Code tool usage for real-time health monitoring

set -e

# Configuration
EVENT_CAPTURE="/Users/nalve/ce-simple/tools/monitoring/event-capture.py"
HEALTH_API="/Users/nalve/ce-simple/tools/monitoring/system-health.py"
LOG_FILE="/Users/nalve/ce-simple/data/monitoring/claude-events.log"

# Hook parameters
HOOK_EVENT="$1"        # PRE, POST, NOTIFY, STOP
TOOL_NAME="$2"         # Tool being used
TOOL_INPUT="$3"        # Tool input/parameters
TOOL_OUTPUT="$4"       # Tool output (POST only)

# Ensure log directory exists
mkdir -p "$(dirname "$LOG_FILE")"

# Get session information
SESSION_ID="${CLAUDE_SESSION_ID:-$(date +%Y%m%d_%H%M)}"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%S.%fZ")

# Calculate execution time for POST events
if [[ "$HOOK_EVENT" == "POST" ]]; then
    # Try to find matching PRE event timing
    TIMER_FILE="/tmp/claude_timer_${TOOL_NAME//\//_}_$$"
    if [[ -f "$TIMER_FILE" ]]; then
        START_TIME=$(cat "$TIMER_FILE")
        CURRENT_TIME=$(date +%s.%N)
        EXECUTION_TIME=$(echo "$CURRENT_TIME - $START_TIME" | bc -l 2>/dev/null || echo "0.0")
        rm -f "$TIMER_FILE"
    else
        EXECUTION_TIME="0.0"
    fi
else
    # For PRE events, start timer
    if [[ "$HOOK_EVENT" == "PRE" ]]; then
        TIMER_FILE="/tmp/claude_timer_${TOOL_NAME//\//_}_$$"
        date +%s.%N > "$TIMER_FILE"
    fi
    EXECUTION_TIME="0.0"
fi

# Determine success status
SUCCESS="true"
CONTEXT_PRESERVED="true"
USER_VOICE_MAINTAINED="true"

# Analyze tool output for success indicators (POST events only)
if [[ "$HOOK_EVENT" == "POST" && -n "$TOOL_OUTPUT" ]]; then
    # Check for common error patterns
    if echo "$TOOL_OUTPUT" | grep -qi "error\|failed\|exception\|denied"; then
        SUCCESS="false"
    fi
    
    # Check for context preservation indicators
    if echo "$TOOL_OUTPUT" | grep -qi "context.*lost\|state.*invalid"; then
        CONTEXT_PRESERVED="false"
    fi
    
    # Check for user voice preservation
    if echo "$TOOL_INPUT" | grep -qi "user.*voice\|preserve.*intent"; then
        USER_VOICE_MAINTAINED="true"
    fi
fi

# Log event locally
echo "[$(date)] $HOOK_EVENT-$TOOL_NAME: Session $SESSION_ID (${EXECUTION_TIME}s)" >> "$LOG_FILE"

# Create event payload
EVENT_DATA=$(cat <<EOF
{
  "event_type": "claude_${HOOK_EVENT,,}",
  "timestamp": "$TIMESTAMP",
  "tool_name": "$TOOL_NAME",
  "session_id": "$SESSION_ID",
  "execution_time": $EXECUTION_TIME,
  "success": $SUCCESS,
  "context_preserved": $CONTEXT_PRESERVED,
  "user_voice_maintained": $USER_VOICE_MAINTAINED,
  "hook_event": "$HOOK_EVENT",
  "metadata": {
    "tool_input_length": $(echo -n "$TOOL_INPUT" | wc -c),
    "tool_output_length": $(echo -n "$TOOL_OUTPUT" | wc -c),
    "process_id": $$
  }
}
EOF
)

# Send to event capture system (non-blocking)
if [[ -f "$EVENT_CAPTURE" ]]; then
    echo "$EVENT_DATA" | python3 "$EVENT_CAPTURE" capture-claude-event > /dev/null 2>&1 &
fi

# Update health daemon (non-blocking)
if [[ -f "$HEALTH_API" && "$HOOK_EVENT" == "POST" ]]; then
    python3 "$HEALTH_API" record-tool "$TOOL_NAME" "$EXECUTION_TIME" "$SUCCESS" > /dev/null 2>&1 &
fi

# Real-time dashboard notification (non-blocking)
curl -s -X POST "http://localhost:5000/api/claude-event" \
    -H "Content-Type: application/json" \
    -d "$EVENT_DATA" > /dev/null 2>&1 &

exit 0