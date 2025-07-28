#!/usr/bin/env python3
"""
Claude Code Integration for Background Process Management
Solves the Claude Code background process limitation
"""

import json
import subprocess
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime

class BackgroundProcessManager:
    """Manages background processes for Claude Code integration"""
    
    def __init__(self, base_dir: Path):
        self.base_dir = Path(base_dir)
        self.launchers_dir = self.base_dir / "tools" / "launchers"
        self.monitor_dir = self.base_dir / "data" / "monitoring"
        
        # Ensure directories exist
        self.monitor_dir.mkdir(parents=True, exist_ok=True)
        
        # Process definitions
        self.processes = {
            "health_monitor": {
                "launcher": self.launchers_dir / "start_health_monitor.sh",
                "pid_file": self.monitor_dir / "health_monitor.pid",
                "status_file": self.monitor_dir / "health_status.json",
                "log_file": self.monitor_dir / "health_monitor.log",
                "description": "System health and voice preservation monitoring"
            }
        }
    
    def check_process_status(self, process_name: str) -> Dict:
        """Check status of a specific background process"""
        if process_name not in self.processes:
            return {"error": f"Unknown process: {process_name}"}
        
        process = self.processes[process_name]
        
        try:
            # Use the check_process_status.sh script
            result = subprocess.run([
                str(self.launchers_dir / "check_process_status.sh"), "json"
            ], capture_output=True, text=True, timeout=10)
            
            if result.returncode == 0:
                return json.loads(result.stdout)
            else:
                return {
                    "error": "Failed to check process status",
                    "stderr": result.stderr
                }
        
        except subprocess.TimeoutExpired:
            return {"error": "Timeout checking process status"}
        except json.JSONDecodeError:
            return {"error": "Invalid JSON response from status checker"}
        except Exception as e:
            return {"error": f"Exception checking process: {str(e)}"}
    
    def start_process(self, process_name: str) -> Dict:
        """Start a background process"""
        if process_name not in self.processes:
            return {"error": f"Unknown process: {process_name}"}
        
        process = self.processes[process_name]
        
        try:
            # Check if already running
            status = self.check_process_status(process_name)
            if status.get("health_monitor", {}).get("status") == "running":
                return {
                    "status": "already_running",
                    "pid": status["health_monitor"]["pid"],
                    "message": f"{process_name} is already running"
                }
            
            # Start the process
            result = subprocess.run([
                str(process["launcher"]), "start"
            ], capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                # Wait a moment and check if it started successfully
                time.sleep(2)
                status = self.check_process_status(process_name)
                
                if status.get("health_monitor", {}).get("status") == "running":
                    return {
                        "status": "started",
                        "pid": status["health_monitor"]["pid"],
                        "message": f"{process_name} started successfully",
                        "stdout": result.stdout
                    }
                else:
                    return {
                        "status": "failed",
                        "message": f"{process_name} failed to start properly",
                        "stdout": result.stdout,
                        "stderr": result.stderr
                    }
            else:
                return {
                    "status": "failed",
                    "message": f"Failed to start {process_name}",
                    "stdout": result.stdout,
                    "stderr": result.stderr
                }
        
        except subprocess.TimeoutExpired:
            return {"error": f"Timeout starting {process_name}"}
        except Exception as e:
            return {"error": f"Exception starting process: {str(e)}"}
    
    def stop_process(self, process_name: str) -> Dict:
        """Stop a background process"""
        if process_name not in self.processes:
            return {"error": f"Unknown process: {process_name}"}
        
        process = self.processes[process_name]
        
        try:
            result = subprocess.run([
                str(process["launcher"]), "stop"
            ], capture_output=True, text=True, timeout=30)
            
            return {
                "status": "stopped" if result.returncode == 0 else "failed",
                "message": f"{process_name} stop command executed",
                "stdout": result.stdout,
                "stderr": result.stderr
            }
        
        except subprocess.TimeoutExpired:
            return {"error": f"Timeout stopping {process_name}"}
        except Exception as e:
            return {"error": f"Exception stopping process: {str(e)}"}
    
    def restart_process(self, process_name: str) -> Dict:
        """Restart a background process"""
        if process_name not in self.processes:
            return {"error": f"Unknown process: {process_name}"}
        
        process = self.processes[process_name]
        
        try:
            result = subprocess.run([
                str(process["launcher"]), "restart"
            ], capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                # Verify it restarted
                time.sleep(3)
                status = self.check_process_status(process_name)
                
                return {
                    "status": "restarted",
                    "message": f"{process_name} restarted successfully",
                    "current_status": status,
                    "stdout": result.stdout
                }
            else:
                return {
                    "status": "failed",
                    "message": f"Failed to restart {process_name}",
                    "stdout": result.stdout,
                    "stderr": result.stderr
                }
        
        except subprocess.TimeoutExpired:
            return {"error": f"Timeout restarting {process_name}"}
        except Exception as e:
            return {"error": f"Exception restarting process: {str(e)}"}
    
    def get_all_processes_status(self) -> Dict:
        """Get status of all managed processes"""
        status = {
            "timestamp": datetime.now().isoformat(),
            "processes": {}
        }
        
        for process_name in self.processes:
            status["processes"][process_name] = self.check_process_status(process_name)
        
        return status
    
    def stop_all_processes(self) -> Dict:
        """Stop all background processes"""
        try:
            result = subprocess.run([
                str(self.launchers_dir / "stop_all_monitors.sh"), "stop"
            ], capture_output=True, text=True, timeout=60)
            
            return {
                "status": "completed",
                "message": "All processes stop command executed",
                "stdout": result.stdout,
                "stderr": result.stderr,
                "return_code": result.returncode
            }
        
        except subprocess.TimeoutExpired:
            return {"error": "Timeout stopping all processes"}
        except Exception as e:
            return {"error": f"Exception stopping all processes: {str(e)}"}
    
    def get_process_logs(self, process_name: str, lines: int = 20) -> Dict:
        """Get recent log entries for a process"""
        if process_name not in self.processes:
            return {"error": f"Unknown process: {process_name}"}
        
        process = self.processes[process_name]
        log_file = process["log_file"]
        
        if not log_file.exists():
            return {
                "status": "no_logs",
                "message": f"Log file not found: {log_file}"
            }
        
        try:
            result = subprocess.run([
                "tail", "-n", str(lines), str(log_file)
            ], capture_output=True, text=True, timeout=10)
            
            return {
                "status": "success",
                "log_file": str(log_file),
                "lines": lines,
                "content": result.stdout.split('\n') if result.stdout else []
            }
        
        except subprocess.TimeoutExpired:
            return {"error": "Timeout reading log file"}
        except Exception as e:
            return {"error": f"Exception reading logs: {str(e)}"}

# Claude Code Helper Functions
def claude_check_monitors() -> str:
    """Claude Code helper: Check all monitoring processes status"""
    manager = BackgroundProcessManager("/Users/nalve/ce-simple")
    status = manager.get_all_processes_status()
    return json.dumps(status, indent=2)

def claude_start_health_monitor() -> str:
    """Claude Code helper: Start health monitoring"""
    manager = BackgroundProcessManager("/Users/nalve/ce-simple")
    result = manager.start_process("health_monitor")
    return json.dumps(result, indent=2)

def claude_stop_health_monitor() -> str:
    """Claude Code helper: Stop health monitoring"""
    manager = BackgroundProcessManager("/Users/nalve/ce-simple")
    result = manager.stop_process("health_monitor")
    return json.dumps(result, indent=2)

def claude_restart_health_monitor() -> str:
    """Claude Code helper: Restart health monitoring"""
    manager = BackgroundProcessManager("/Users/nalve/ce-simple")
    result = manager.restart_process("health_monitor")
    return json.dumps(result, indent=2)

def claude_get_health_logs(lines: int = 10) -> str:
    """Claude Code helper: Get recent health monitor logs"""
    manager = BackgroundProcessManager("/Users/nalve/ce-simple")
    result = manager.get_process_logs("health_monitor", lines)
    return json.dumps(result, indent=2)

def claude_system_overview() -> str:
    """Claude Code helper: Complete system overview"""
    try:
        result = subprocess.run([
            "/Users/nalve/ce-simple/tools/launchers/check_process_status.sh", "overview"
        ], capture_output=True, text=True, timeout=15)
        
        return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
    
    except Exception as e:
        return f"Error getting system overview: {str(e)}"

# Documentation for Claude Code integration
JSON_DOC = {
    "claude_commands": [
        {
            "function": "claude_check_monitors",
            "description": "Check status of all background monitoring processes",
            "usage": "claude_check_monitors()"
        },
        {
            "function": "claude_start_health_monitor", 
            "description": "Start the health monitoring daemon",
            "usage": "claude_start_health_monitor()"
        },
        {
            "function": "claude_stop_health_monitor",
            "description": "Stop the health monitoring daemon", 
            "usage": "claude_stop_health_monitor()"
        },
        {
            "function": "claude_restart_health_monitor",
            "description": "Restart the health monitoring daemon",
            "usage": "claude_restart_health_monitor()"
        },
        {
            "function": "claude_get_health_logs",
            "description": "Get recent health monitor log entries",
            "usage": "claude_get_health_logs(lines=20)"
        },
        {
            "function": "claude_system_overview",
            "description": "Get complete system status overview",
            "usage": "claude_system_overview()"
        }
    ]
}

# CLI Interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python claude_code_integration.py <command> [args]")
        print("")
        print("Commands:")
        print("  check-all        - Check status of all processes")
        print("  start <process>  - Start a background process")
        print("  stop <process>   - Stop a background process")
        print("  restart <process>- Restart a background process")
        print("  stop-all         - Stop all background processes")
        print("  logs <process>   - Get recent log entries")
        print("  overview         - Complete system overview")
        print("")
        print("Available processes: health_monitor")
        print("")
        print("Claude Code Integration Functions:")
        for cmd in JSON_DOC["claude_commands"]:
            print(f"  {cmd['function']} - {cmd['description']}")
        sys.exit(1)
    
    manager = BackgroundProcessManager("/Users/nalve/ce-simple")
    command = sys.argv[1]
    
    if command == "check-all":
        result = manager.get_all_processes_status()
        print(json.dumps(result, indent=2))
    
    elif command == "start" and len(sys.argv) > 2:
        process_name = sys.argv[2]
        result = manager.start_process(process_name)
        print(json.dumps(result, indent=2))
    
    elif command == "stop" and len(sys.argv) > 2:
        process_name = sys.argv[2]
        result = manager.stop_process(process_name)
        print(json.dumps(result, indent=2))
    
    elif command == "restart" and len(sys.argv) > 2:
        process_name = sys.argv[2]
        result = manager.restart_process(process_name)
        print(json.dumps(result, indent=2))
    
    elif command == "stop-all":
        result = manager.stop_all_processes()
        print(json.dumps(result, indent=2))
    
    elif command == "logs" and len(sys.argv) > 2:
        process_name = sys.argv[2]
        lines = int(sys.argv[3]) if len(sys.argv) > 3 else 20
        result = manager.get_process_logs(process_name, lines)
        print(json.dumps(result, indent=2))
    
    elif command == "overview":
        print(claude_system_overview())
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)