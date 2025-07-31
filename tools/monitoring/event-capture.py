#!/usr/bin/env python3
"""
event-capture.py - Git Event Monitoring and Capture System
Part of Git Workflow Analysis Implementation
Created: 2025-07-31

Captures and logs Git events for workflow analysis and performance monitoring.
Integrates with existing Claude Code Hooks system for comprehensive event tracking.
"""

import json
import time
import sys
import os
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

class GitEventCapture:
    """Git event monitoring and capture system"""
    
    def __init__(self, project_root: str = None):
        """Initialize event capture system"""
        self.project_root = Path(project_root) if project_root else Path.cwd()
        self.events_dir = self.project_root / "tools" / "monitoring" / "events"
        self.events_dir.mkdir(parents=True, exist_ok=True)
        
        self.log_file = self.events_dir / "git-events.log"
        self.json_log = self.events_dir / "git-events.json"
        
        # Performance thresholds (based on ADR-027 <200ms requirement)
        self.performance_thresholds = {
            "hook_execution": 200,  # milliseconds
            "command_execution": 1000,  # milliseconds
            "analysis_time": 5000  # milliseconds
        }
    
    def log_event(self, event_type: str, event_data: Dict[str, Any]) -> None:
        """Log event with timestamp and metadata"""
        timestamp = datetime.now().isoformat()
        
        # Create event record
        event_record = {
            "timestamp": timestamp,
            "type": event_type,
            "data": event_data,
            "project": str(self.project_root),
            "branch": self._get_current_branch(),
            "commit": self._get_current_commit()
        }
        
        # Log to text file
        with open(self.log_file, 'a') as f:
            f.write(f"{timestamp} [{event_type}] {json.dumps(event_data)}\n")
        
        # Log to JSON file
        with open(self.json_log, 'a') as f:
            f.write(json.dumps(event_record) + "\n")
    
    def capture_git_command(self, command: List[str]) -> Dict[str, Any]:
        """Capture Git command execution with performance metrics"""
        start_time = time.time()
        
        try:
            result = subprocess.run(
                command,
                cwd=self.project_root,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            
            event_data = {
                "command": " ".join(command),
                "return_code": result.returncode,
                "execution_time_ms": round(execution_time, 2),
                "stdout": result.stdout[:1000],  # Limit output size
                "stderr": result.stderr[:1000] if result.stderr else None,
                "performance_ok": execution_time < self.performance_thresholds.get("command_execution", 1000)
            }
            
            self.log_event("git_command", event_data)
            return event_data
            
        except subprocess.TimeoutExpired:
            event_data = {
                "command": " ".join(command),
                "error": "timeout",
                "execution_time_ms": 30000,
                "performance_ok": False
            }
            self.log_event("git_command_timeout", event_data)
            return event_data
        
        except Exception as e:
            event_data = {
                "command": " ".join(command),
                "error": str(e),
                "performance_ok": False
            }
            self.log_event("git_command_error", event_data)
            return event_data
    
    def capture_hook_event(self, hook_name: str, hook_data: Dict[str, Any]) -> None:
        """Capture Git hook execution event"""
        event_data = {
            "hook_name": hook_name,
            "execution_time_ms": hook_data.get("execution_time_ms", 0),
            "success": hook_data.get("success", False),
            "performance_ok": hook_data.get("execution_time_ms", 0) < self.performance_thresholds.get("hook_execution", 200),
            "details": hook_data
        }
        
        self.log_event("git_hook", event_data)
    
    def capture_workflow_event(self, workflow_type: str, workflow_data: Dict[str, Any]) -> None:
        """Capture workflow-level events"""
        event_data = {
            "workflow_type": workflow_type,
            "branch": self._get_current_branch(),
            "details": workflow_data
        }
        
        self.log_event("workflow", event_data)
    
    def get_performance_summary(self, hours: int = 24) -> Dict[str, Any]:
        """Get performance summary for the last N hours"""
        cutoff_time = datetime.now().timestamp() - (hours * 3600)
        
        events = []
        if self.json_log.exists():
            with open(self.json_log, 'r') as f:
                for line in f:
                    try:
                        event = json.loads(line.strip())
                        event_time = datetime.fromisoformat(event["timestamp"]).timestamp()
                        if event_time >= cutoff_time:
                            events.append(event)
                    except (json.JSONDecodeError, KeyError, ValueError):
                        continue
        
        # Calculate summary statistics
        git_commands = [e for e in events if e["type"] == "git_command"]
        hook_events = [e for e in events if e["type"] == "git_hook"]
        
        summary = {
            "period_hours": hours,
            "total_events": len(events),
            "git_commands": {
                "count": len(git_commands),
                "avg_execution_ms": self._calculate_avg_time(git_commands, "data.execution_time_ms"),
                "performance_issues": len([e for e in git_commands if not e.get("data", {}).get("performance_ok", True)])
            },
            "git_hooks": {
                "count": len(hook_events),
                "avg_execution_ms": self._calculate_avg_time(hook_events, "data.execution_time_ms"),
                "performance_issues": len([e for e in hook_events if not e.get("data", {}).get("performance_ok", True)])
            }
        }
        
        return summary
    
    def _get_current_branch(self) -> Optional[str]:
        """Get current Git branch"""
        try:
            result = subprocess.run(
                ["git", "branch", "--show-current"],
                cwd=self.project_root,
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.stdout.strip() if result.returncode == 0 else None
        except:
            return None
    
    def _get_current_commit(self) -> Optional[str]:
        """Get current Git commit hash"""
        try:
            result = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=self.project_root,
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.stdout.strip()[:8] if result.returncode == 0 else None
        except:
            return None
    
    def _calculate_avg_time(self, events: List[Dict], time_path: str) -> float:
        """Calculate average execution time from events"""
        times = []
        for event in events:
            try:
                # Navigate nested dictionary path
                value = event
                for key in time_path.split("."):
                    value = value[key]
                if isinstance(value, (int, float)):
                    times.append(value)
            except (KeyError, TypeError):
                continue
        
        return round(sum(times) / len(times), 2) if times else 0.0

def main():
    """Main execution for command-line usage"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Git Event Capture System")
    parser.add_argument("--project-root", help="Project root directory")
    parser.add_argument("--command", nargs="+", help="Git command to capture")
    parser.add_argument("--hook", help="Hook name for hook event")
    parser.add_argument("--hook-data", help="Hook data JSON")
    parser.add_argument("--workflow", help="Workflow type")
    parser.add_argument("--workflow-data", help="Workflow data JSON")
    parser.add_argument("--summary", type=int, help="Get performance summary for N hours")
    
    args = parser.parse_args()
    
    # Initialize capture system
    capture = GitEventCapture(args.project_root)
    
    if args.command:
        result = capture.capture_git_command(args.command)
        print(json.dumps(result, indent=2))
    
    elif args.hook and args.hook_data:
        try:
            hook_data = json.loads(args.hook_data)
            capture.capture_hook_event(args.hook, hook_data)
            print(f"Hook event captured: {args.hook}")
        except json.JSONDecodeError:
            print("Error: Invalid hook data JSON", file=sys.stderr)
            sys.exit(1)
    
    elif args.workflow and args.workflow_data:
        try:
            workflow_data = json.loads(args.workflow_data)
            capture.capture_workflow_event(args.workflow, workflow_data)
            print(f"Workflow event captured: {args.workflow}")
        except json.JSONDecodeError:
            print("Error: Invalid workflow data JSON", file=sys.stderr)
            sys.exit(1)
    
    elif args.summary:
        summary = capture.get_performance_summary(args.summary)
        print(json.dumps(summary, indent=2))
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()