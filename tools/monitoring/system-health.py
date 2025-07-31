#!/usr/bin/env python3
"""
system-health.py - System Health Monitoring and Diagnostics
Part of Git Workflow Analysis Implementation  
Created: 2025-07-31

Monitors system health, Git hooks status, and workflow performance.
Provides health dashboard and diagnostic capabilities for the Git workflow system.
"""

import json
import os
import sys
import subprocess
import time
import psutil
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple

class SystemHealthMonitor:
    """System health monitoring and diagnostics"""
    
    def __init__(self, project_root: str = None):
        """Initialize health monitoring system"""
        self.project_root = Path(project_root) if project_root else Path.cwd()
        self.health_dir = self.project_root / "tools" / "monitoring" / "health"
        self.health_dir.mkdir(parents=True, exist_ok=True)
        
        self.health_log = self.health_dir / "system-health.log"
        self.status_file = self.health_dir / "current-status.json"
        
        # Health check thresholds
        self.thresholds = {
            "disk_usage_percent": 90,
            "memory_usage_percent": 85,
            "hook_execution_time_ms": 200,
            "git_operation_time_ms": 1000,
            "file_count_warning": 10000
        }
    
    def check_system_resources(self) -> Dict[str, Any]:
        """Check system resource utilization"""
        try:
            # CPU usage
            cpu_percent = psutil.cpu_percent(interval=1)
            
            # Memory usage
            memory = psutil.virtual_memory()
            memory_percent = memory.percent
            
            # Disk usage for project root
            disk = psutil.disk_usage(str(self.project_root))
            disk_percent = (disk.used / disk.total) * 100
            
            return {
                "cpu_percent": round(cpu_percent, 1),
                "memory_percent": round(memory_percent, 1),
                "disk_percent": round(disk_percent, 1),
                "disk_free_gb": round(disk.free / (1024**3), 2),
                "memory_available_gb": round(memory.available / (1024**3), 2),
                "status": "healthy" if all([
                    cpu_percent < 90,
                    memory_percent < self.thresholds["memory_usage_percent"],
                    disk_percent < self.thresholds["disk_usage_percent"]
                ]) else "warning"
            }
        except Exception as e:
            return {
                "error": str(e),
                "status": "error"
            }
    
    def check_git_hooks_status(self) -> Dict[str, Any]:
        """Check Git hooks installation and health"""
        hooks_dir = self.project_root / ".git" / "hooks"
        
        if not hooks_dir.exists():
            return {
                "status": "error",
                "message": "Git hooks directory not found",
                "hooks": {}
            }
        
        # Expected hooks based on handoff analysis
        expected_hooks = [
            "pre-commit",
            "post-commit", 
            "pre-push",
            "post-merge",
            "commit-msg"
        ]
        
        hooks_status = {}
        working_hooks = 0
        
        for hook_name in expected_hooks:
            hook_file = hooks_dir / hook_name
            
            if hook_file.exists():
                # Check if executable
                is_executable = os.access(hook_file, os.X_OK)
                
                # Test hook execution (dry run)
                execution_ok = self._test_hook_execution(hook_file)
                
                hooks_status[hook_name] = {
                    "exists": True,
                    "executable": is_executable,
                    "working": execution_ok,
                    "size_bytes": hook_file.stat().st_size
                }
                
                if is_executable and execution_ok:
                    working_hooks += 1
            else:
                hooks_status[hook_name] = {
                    "exists": False,
                    "executable": False,
                    "working": False
                }
        
        return {
            "status": "healthy" if working_hooks == len(expected_hooks) else "warning",
            "working_hooks": working_hooks,
            "total_expected": len(expected_hooks),
            "hooks": hooks_status
        }
    
    def check_git_performance(self) -> Dict[str, Any]:
        """Check Git operation performance"""
        performance_tests = [
            (["git", "status"], "status"),
            (["git", "log", "--oneline", "-10"], "log"),
            (["git", "branch", "--show-current"], "branch")
        ]
        
        results = {}
        all_healthy = True
        
        for command, test_name in performance_tests:
            start_time = time.time()
            
            try:
                result = subprocess.run(
                    command,
                    cwd=self.project_root,
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                execution_time = (time.time() - start_time) * 1000
                
                results[test_name] = {
                    "execution_time_ms": round(execution_time, 2),
                    "success": result.returncode == 0,
                    "performance_ok": execution_time < self.thresholds["git_operation_time_ms"]
                }
                
                if not results[test_name]["performance_ok"]:
                    all_healthy = False
                    
            except subprocess.TimeoutExpired:
                results[test_name] = {
                    "execution_time_ms": 10000,
                    "success": False,
                    "performance_ok": False,
                    "error": "timeout"
                }
                all_healthy = False
            except Exception as e:
                results[test_name] = {
                    "success": False,
                    "performance_ok": False,
                    "error": str(e)
                }
                all_healthy = False
        
        return {
            "status": "healthy" if all_healthy else "warning",
            "tests": results
        }
    
    def check_project_health(self) -> Dict[str, Any]:
        """Check project-specific health metrics"""
        try:
            # File count check
            total_files = sum(1 for _ in self.project_root.rglob("*") if _.is_file())
            
            # Check for large files (>1MB)
            large_files = []
            for file_path in self.project_root.rglob("*"):
                if file_path.is_file():
                    try:
                        size_mb = file_path.stat().st_size / (1024 * 1024)
                        if size_mb > 1:
                            large_files.append({
                                "path": str(file_path.relative_to(self.project_root)),
                                "size_mb": round(size_mb, 2)
                            })
                    except:
                        continue
            
            # Check context directory health (based on 80-line violations)
            context_dir = self.project_root / "context"
            context_health = self._check_context_directory_health(context_dir)
            
            return {
                "status": "healthy" if total_files < self.thresholds["file_count_warning"] else "warning",
                "total_files": total_files,
                "large_files_count": len(large_files),
                "large_files": large_files[:10],  # Limit output
                "context_directory": context_health
            }
            
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }
    
    def generate_health_report(self) -> Dict[str, Any]:
        """Generate comprehensive health report"""
        timestamp = datetime.now().isoformat()
        
        report = {
            "timestamp": timestamp,
            "project_root": str(self.project_root),
            "system_resources": self.check_system_resources(),
            "git_hooks": self.check_git_hooks_status(),
            "git_performance": self.check_git_performance(),
            "project_health": self.check_project_health()
        }
        
        # Calculate overall health status
        statuses = [
            report["system_resources"].get("status", "error"),
            report["git_hooks"].get("status", "error"),
            report["git_performance"].get("status", "error"),
            report["project_health"].get("status", "error")
        ]
        
        if "error" in statuses:
            overall_status = "error"
        elif "warning" in statuses:
            overall_status = "warning"
        else:
            overall_status = "healthy"
        
        report["overall_status"] = overall_status
        
        # Save current status
        with open(self.status_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        # Log to health log
        with open(self.health_log, 'a') as f:
            f.write(f"{timestamp} [HEALTH_CHECK] {overall_status}\n")
        
        return report
    
    def get_health_dashboard_data(self) -> Dict[str, Any]:
        """Get health data formatted for dashboard display"""
        report = self.generate_health_report()
        
        # Create dashboard-friendly summary
        dashboard = {
            "overall_status": report["overall_status"],
            "last_check": report["timestamp"],
            "summary": {
                "system": {
                    "status": report["system_resources"]["status"],
                    "cpu": f"{report['system_resources'].get('cpu_percent', 0)}%",
                    "memory": f"{report['system_resources'].get('memory_percent', 0)}%",
                    "disk": f"{report['system_resources'].get('disk_percent', 0)}%"
                },
                "git_hooks": {
                    "status": report["git_hooks"]["status"],
                    "working": f"{report['git_hooks'].get('working_hooks', 0)}/{report['git_hooks'].get('total_expected', 0)}"
                },
                "performance": {
                    "status": report["git_performance"]["status"],
                    "avg_time": self._calculate_avg_performance_time(report["git_performance"])
                },
                "project": {
                    "status": report["project_health"]["status"],
                    "files": report["project_health"].get("total_files", 0)
                }
            }
        }
        
        return dashboard
    
    def _test_hook_execution(self, hook_file: Path) -> bool:
        """Test if a Git hook can execute without errors"""
        try:
            # Simple test - check if file is readable and has proper shebang
            with open(hook_file, 'r') as f:
                first_line = f.readline().strip()
                return first_line.startswith('#!')
        except:
            return False
    
    def _check_context_directory_health(self, context_dir: Path) -> Dict[str, Any]:
        """Check context directory for 80-line violations and structure health"""
        if not context_dir.exists():
            return {"status": "error", "message": "Context directory not found"}
        
        violations = []
        total_files = 0
        
        for file_path in context_dir.rglob("*.md"):
            if file_path.is_file():
                total_files += 1
                try:
                    with open(file_path, 'r') as f:
                        line_count = sum(1 for _ in f)
                        if line_count > 80:
                            violations.append({
                                "file": str(file_path.relative_to(self.project_root)),
                                "lines": line_count
                            })
                except:
                    continue
        
        return {
            "status": "healthy" if len(violations) == 0 else "warning",
            "total_files": total_files,
            "violations": len(violations),
            "violation_details": violations[:5]  # Limit output
        }
    
    def _calculate_avg_performance_time(self, performance_data: Dict[str, Any]) -> str:
        """Calculate average performance time from test results"""
        tests = performance_data.get("tests", {})
        times = []
        
        for test_data in tests.values():
            if "execution_time_ms" in test_data:
                times.append(test_data["execution_time_ms"])
        
        if times:
            avg_time = sum(times) / len(times)
            return f"{avg_time:.1f}ms"
        return "N/A"

def main():
    """Main execution for command-line usage"""
    import argparse
    
    parser = argparse.ArgumentParser(description="System Health Monitor")
    parser.add_argument("--project-root", help="Project root directory")
    parser.add_argument("--report", action="store_true", help="Generate health report")
    parser.add_argument("--dashboard", action="store_true", help="Get dashboard data")
    parser.add_argument("--continuous", type=int, help="Run continuous monitoring (seconds interval)")
    
    args = parser.parse_args()
    
    monitor = SystemHealthMonitor(args.project_root)
    
    if args.continuous:
        print(f"Starting continuous monitoring (interval: {args.continuous}s)")
        try:
            while True:
                report = monitor.generate_health_report()
                print(f"{datetime.now().strftime('%H:%M:%S')} - Status: {report['overall_status']}")
                time.sleep(args.continuous)
        except KeyboardInterrupt:
            print("\nMonitoring stopped")
    
    elif args.dashboard:
        dashboard = monitor.get_health_dashboard_data()
        print(json.dumps(dashboard, indent=2))
    
    else:
        # Default: generate report
        report = monitor.generate_health_report()
        print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()