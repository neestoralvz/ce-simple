#!/usr/bin/env python3
"""
Claude Code Efficiency Dashboard
Real-time monitoring of Claude Code CLI performance and Task tool effectiveness
"""

import json
import time
import datetime
from pathlib import Path
from typing import Dict, List, Any
import sqlite3
import os

class ClaudeCodeEfficiencyDashboard:
    """
    Efficiency tracking specifically for Claude Code CLI operations
    Focus on Task tool performance, command execution metrics, and user workflow optimization
    """
    
    def __init__(self, workspace_path: str = "/Users/nalve/ce-simple"):
        self.workspace = Path(workspace_path)
        self.db_path = self.workspace / "data" / "claude-code-metrics.db"
        self.session_id = f"claude-code-{int(time.time())}"
        self.init_database()
        
    def init_database(self):
        """Initialize SQLite database for Claude Code metrics"""
        self.db_path.parent.mkdir(exist_ok=True)
        
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS task_tool_metrics (
                    id INTEGER PRIMARY KEY,
                    session_id TEXT,
                    timestamp DATETIME,
                    task_type TEXT,
                    execution_time REAL,
                    token_usage INTEGER,
                    success_rate REAL,
                    parallel_efficiency REAL
                )
            """)
            
            conn.execute("""
                CREATE TABLE IF NOT EXISTS command_performance (
                    id INTEGER PRIMARY KEY,
                    session_id TEXT,
                    timestamp DATETIME,
                    command_name TEXT,
                    context_loading_time REAL,
                    decision_tree_accuracy REAL,
                    user_satisfaction REAL
                )
            """)
            
            conn.execute("""
                CREATE TABLE IF NOT EXISTS workflow_efficiency (
                    id INTEGER PRIMARY KEY,
                    session_id TEXT,
                    timestamp DATETIME,
                    workflow_type TEXT,
                    steps_completed INTEGER,
                    total_time REAL,
                    claude_code_specific_metrics TEXT
                )
            """)
    
    def track_task_tool_performance(self, task_type: str, execution_time: float, 
                                  token_usage: int, success_rate: float, 
                                  parallel_efficiency: float):
        """Track Task tool specific performance metrics for Claude Code"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT INTO task_tool_metrics 
                (session_id, timestamp, task_type, execution_time, token_usage, success_rate, parallel_efficiency)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                self.session_id,
                datetime.datetime.now(),
                task_type,
                execution_time,
                token_usage,
                success_rate,
                parallel_efficiency
            ))
    
    def track_command_efficiency(self, command_name: str, context_loading_time: float,
                               decision_tree_accuracy: float, user_satisfaction: float):
        """Track Claude Code command performance"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT INTO command_performance
                (session_id, timestamp, command_name, context_loading_time, decision_tree_accuracy, user_satisfaction)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                self.session_id,
                datetime.datetime.now(),
                command_name,
                context_loading_time,
                decision_tree_accuracy,
                user_satisfaction
            ))
    
    def track_workflow_completion(self, workflow_type: str, steps_completed: int,
                                total_time: float, claude_code_metrics: Dict[str, Any]):
        """Track Claude Code specific workflow patterns"""
        metrics_json = json.dumps(claude_code_metrics)
        
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT INTO workflow_efficiency
                (session_id, timestamp, workflow_type, steps_completed, total_time, claude_code_specific_metrics)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                self.session_id,
                datetime.datetime.now(),
                workflow_type,
                steps_completed,
                total_time,
                metrics_json
            ))
    
    def generate_real_time_dashboard(self) -> Dict[str, Any]:
        """Generate real-time dashboard data for Claude Code operations"""
        dashboard_data = {
            "timestamp": datetime.datetime.now().isoformat(),
            "session_id": self.session_id,
            "task_tool_performance": self._get_task_tool_metrics(),
            "command_efficiency": self._get_command_metrics(),
            "workflow_patterns": self._get_workflow_metrics(),
            "claude_code_insights": self._get_claude_code_insights()
        }
        
        # Save dashboard data
        dashboard_path = self.workspace / "data" / "claude-code-dashboard.json"
        with open(dashboard_path, 'w') as f:
            json.dump(dashboard_data, f, indent=2)
            
        return dashboard_data
    
    def _get_task_tool_metrics(self) -> Dict[str, Any]:
        """Get Task tool performance metrics"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("""
                SELECT task_type, AVG(execution_time), AVG(success_rate), AVG(parallel_efficiency)
                FROM task_tool_metrics 
                WHERE timestamp > datetime('now', '-1 hour')
                GROUP BY task_type
            """)
            
            metrics = {}
            for row in cursor.fetchall():
                task_type, avg_time, avg_success, avg_parallel = row
                metrics[task_type] = {
                    "average_execution_time": avg_time,
                    "success_rate": avg_success,
                    "parallel_efficiency": avg_parallel
                }
                
        return metrics
    
    def _get_command_metrics(self) -> Dict[str, Any]:
        """Get Claude Code command performance metrics"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("""
                SELECT command_name, AVG(context_loading_time), AVG(decision_tree_accuracy), AVG(user_satisfaction)
                FROM command_performance
                WHERE timestamp > datetime('now', '-1 hour')
                GROUP BY command_name
            """)
            
            metrics = {}
            for row in cursor.fetchall():
                cmd, avg_loading, avg_accuracy, avg_satisfaction = row
                metrics[cmd] = {
                    "context_loading_time": avg_loading,
                    "decision_tree_accuracy": avg_accuracy,
                    "user_satisfaction": avg_satisfaction
                }
                
        return metrics
    
    def _get_workflow_metrics(self) -> Dict[str, Any]:
        """Get workflow efficiency patterns"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("""
                SELECT workflow_type, AVG(total_time), AVG(steps_completed)
                FROM workflow_efficiency
                WHERE timestamp > datetime('now', '-1 hour')
                GROUP BY workflow_type
            """)
            
            metrics = {}
            for row in cursor.fetchall():
                workflow, avg_time, avg_steps = row
                metrics[workflow] = {
                    "average_completion_time": avg_time,
                    "average_steps": avg_steps
                }
                
        return metrics
    
    def _get_claude_code_insights(self) -> Dict[str, Any]:
        """Generate Claude Code specific insights"""
        return {
            "session_efficiency": self._calculate_session_efficiency(),
            "task_tool_utilization": self._calculate_task_tool_utilization(),
            "parallel_execution_score": self._calculate_parallel_score(),
            "claude_code_optimization_suggestions": self._generate_optimization_suggestions()
        }
    
    def _calculate_session_efficiency(self) -> float:
        """Calculate overall session efficiency for Claude Code operations"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("""
                SELECT AVG(success_rate) FROM task_tool_metrics 
                WHERE session_id = ?
            """, (self.session_id,))
            
            result = cursor.fetchone()
            return result[0] if result[0] else 0.0
    
    def _calculate_task_tool_utilization(self) -> float:
        """Calculate Task tool utilization efficiency"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("""
                SELECT AVG(parallel_efficiency) FROM task_tool_metrics 
                WHERE session_id = ?
            """, (self.session_id,))
            
            result = cursor.fetchone()
            return result[0] if result[0] else 0.0
    
    def _calculate_parallel_score(self) -> float:
        """Calculate parallel execution effectiveness"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("""
                SELECT COUNT(*) as concurrent_tasks
                FROM task_tool_metrics 
                WHERE session_id = ? AND timestamp > datetime('now', '-5 minutes')
                GROUP BY timestamp
                ORDER BY concurrent_tasks DESC
                LIMIT 1
            """, (self.session_id,))
            
            result = cursor.fetchone()
            concurrent_tasks = result[0] if result else 1
            
            # Score based on concurrent task execution (Claude Code strength)
            return min(concurrent_tasks / 5.0, 1.0)  # Max score at 5+ concurrent tasks
    
    def _generate_optimization_suggestions(self) -> List[str]:
        """Generate Claude Code specific optimization suggestions"""
        suggestions = []
        
        # Analyze recent performance
        session_efficiency = self._calculate_session_efficiency()
        parallel_score = self._calculate_parallel_score()
        
        if session_efficiency < 0.8:
            suggestions.append("Consider using more specific Task tool prompts for better success rates")
        
        if parallel_score < 0.6:
            suggestions.append("Increase parallel Task tool usage for better Claude Code efficiency")
            
        suggestions.append("Monitor token usage patterns for context optimization")
        suggestions.append("Track command decision tree accuracy for workflow improvements")
        
        return suggestions

if __name__ == "__main__":
    # Initialize dashboard
    dashboard = ClaudeCodeEfficiencyDashboard()
    
    # Example usage - track some metrics
    dashboard.track_task_tool_performance("research", 2.5, 1500, 0.95, 0.8)
    dashboard.track_command_efficiency("/start", 1.2, 0.92, 0.88)
    dashboard.track_workflow_completion("document_creation", 3, 45.0, {
        "claude_code_tools_used": ["Task", "Write", "Read"],
        "parallel_tasks": 2,
        "context_switches": 1
    })
    
    # Generate dashboard
    data = dashboard.generate_real_time_dashboard()
    print("Claude Code Efficiency Dashboard Generated")
    print(f"Session ID: {dashboard.session_id}")
    print(f"Dashboard saved to: {dashboard.workspace}/data/claude-code-dashboard.json")