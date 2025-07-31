#!/usr/bin/env python3
"""
metrics-analyzer.py - Performance Metrics Analysis and Visualization
Part of Git Workflow Analysis Implementation
Created: 2025-07-31

Analyzes Git workflow performance metrics and generates visualizations
for monitoring system efficiency and identifying optimization opportunities.
"""

import json
import os
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any
import subprocess

class MetricsAnalyzer:
    """Performance metrics analysis and visualization system"""
    
    def __init__(self, project_root: str = None):
        """Initialize metrics analyzer"""
        self.project_root = Path(project_root) if project_root else Path.cwd()
        self.metrics_dir = self.project_root / "tools" / "monitoring" / "metrics"
        self.metrics_dir.mkdir(parents=True, exist_ok=True)
        
        self.events_dir = self.project_root / "tools" / "monitoring" / "events"
        self.health_dir = self.project_root / "tools" / "monitoring" / "health"
        
        # Performance thresholds for analysis
        self.thresholds = {
            "hook_execution_ms": 200,
            "git_operation_ms": 1000,
            "health_check_ms": 5000,
            "conversation_start_ms": 10000
        }
    
    def analyze_performance_trends(self, hours: int = 24) -> Dict[str, Any]:
        """Analyze performance trends over time"""
        cutoff_time = datetime.now() - timedelta(hours=hours)
        
        # Load event data
        events = self._load_events_since(cutoff_time)
        
        # Analyze different performance categories
        analysis = {
            "period_hours": hours,
            "analysis_time": datetime.now().isoformat(),
            "git_operations": self._analyze_git_operations(events),
            "hook_performance": self._analyze_hook_performance(events),
            "conversation_metrics": self._analyze_conversation_metrics(events),
            "system_health_trends": self._analyze_health_trends(cutoff_time),
            "performance_summary": {}
        }
        
        # Generate performance summary
        analysis["performance_summary"] = self._generate_performance_summary(analysis)
        
        # Save analysis results
        self._save_analysis(analysis)
        
        return analysis
    
    def generate_performance_report(self, format: str = "text") -> str:
        """Generate performance report in specified format"""
        analysis = self.analyze_performance_trends(24)
        
        if format == "json":
            return json.dumps(analysis, indent=2)
        elif format == "csv":
            return self._format_as_csv(analysis)
        else:
            return self._format_as_text(analysis)
    
    def get_performance_alerts(self) -> List[Dict[str, Any]]:
        """Get performance alerts based on thresholds"""
        analysis = self.analyze_performance_trends(1)  # Last hour
        alerts = []
        
        # Check Git operations performance
        git_ops = analysis.get("git_operations", {})
        if git_ops.get("avg_execution_ms", 0) > self.thresholds["git_operation_ms"]:
            alerts.append({
                "type": "performance",
                "severity": "warning",
                "component": "git_operations",
                "message": f"Git operations averaging {git_ops.get('avg_execution_ms', 0):.1f}ms (threshold: {self.thresholds['git_operation_ms']}ms)",
                "timestamp": datetime.now().isoformat()
            })
        
        # Check hook performance
        hook_perf = analysis.get("hook_performance", {})
        if hook_perf.get("avg_execution_ms", 0) > self.thresholds["hook_execution_ms"]:
            alerts.append({
                "type": "performance",
                "severity": "critical",
                "component": "git_hooks",
                "message": f"Git hooks averaging {hook_perf.get('avg_execution_ms', 0):.1f}ms (threshold: {self.thresholds['hook_execution_ms']}ms)",
                "timestamp": datetime.now().isoformat()
            })
        
        # Check conversation startup time
        conv_metrics = analysis.get("conversation_metrics", {})
        if conv_metrics.get("avg_start_time_ms", 0) > self.thresholds["conversation_start_ms"]:
            alerts.append({
                "type": "performance",
                "severity": "warning",
                "component": "conversation_startup",
                "message": f"Conversation startup averaging {conv_metrics.get('avg_start_time_ms', 0):.1f}ms (threshold: {self.thresholds['conversation_start_ms']}ms)",
                "timestamp": datetime.now().isoformat()
            })
        
        return alerts
    
    def _load_events_since(self, cutoff_time: datetime) -> List[Dict[str, Any]]:
        """Load events from event log since cutoff time"""
        events = []
        events_file = self.events_dir / "git-events.json"
        
        if not events_file.exists():
            return events
        
        try:
            with open(events_file, 'r') as f:
                for line in f:
                    try:
                        event = json.loads(line.strip())
                        event_time = datetime.fromisoformat(event["timestamp"])
                        if event_time >= cutoff_time:
                            events.append(event)
                    except (json.JSONDecodeError, KeyError, ValueError):
                        continue
        except:
            pass
        
        return events
    
    def _analyze_git_operations(self, events: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze Git operation performance"""
        git_events = [e for e in events if e.get("type") == "git_command"]
        
        if not git_events:
            return {"count": 0, "avg_execution_ms": 0, "performance_issues": 0}
        
        execution_times = []
        performance_issues = 0
        
        for event in git_events:
            exec_time = event.get("data", {}).get("execution_time_ms", 0)
            if exec_time > 0:
                execution_times.append(exec_time)
                if exec_time > self.thresholds["git_operation_ms"]:
                    performance_issues += 1
        
        return {
            "count": len(git_events),
            "avg_execution_ms": sum(execution_times) / len(execution_times) if execution_times else 0,
            "max_execution_ms": max(execution_times) if execution_times else 0,
            "min_execution_ms": min(execution_times) if execution_times else 0,
            "performance_issues": performance_issues,
            "success_rate": len([e for e in git_events if e.get("data", {}).get("return_code") == 0]) / len(git_events) * 100
        }
    
    def _analyze_hook_performance(self, events: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze Git hook performance"""
        hook_events = [e for e in events if e.get("type") == "git_hook"]
        
        if not hook_events:
            return {"count": 0, "avg_execution_ms": 0, "performance_issues": 0}
        
        execution_times = []
        performance_issues = 0
        
        for event in hook_events:
            exec_time = event.get("data", {}).get("execution_time_ms", 0)
            if exec_time > 0:
                execution_times.append(exec_time)
                if exec_time > self.thresholds["hook_execution_ms"]:
                    performance_issues += 1
        
        return {
            "count": len(hook_events),
            "avg_execution_ms": sum(execution_times) / len(execution_times) if execution_times else 0,
            "max_execution_ms": max(execution_times) if execution_times else 0,
            "performance_issues": performance_issues,
            "success_rate": len([e for e in hook_events if e.get("data", {}).get("success", False)]) / len(hook_events) * 100 if hook_events else 0
        }
    
    def _analyze_conversation_metrics(self, events: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze conversation workflow metrics"""
        conv_events = [e for e in events if e.get("type") == "workflow" and "conversation" in e.get("data", {}).get("workflow_type", "")]
        
        conversations = {}
        for event in conv_events:
            workflow_type = event.get("data", {}).get("workflow_type", "")
            branch = event.get("data", {}).get("details", {}).get("branch", "unknown")
            
            if branch not in conversations:
                conversations[branch] = {"start": None, "complete": None, "events": []}
            
            conversations[branch]["events"].append(event)
            
            if "start" in workflow_type:
                conversations[branch]["start"] = event["timestamp"]
            elif "complete" in workflow_type:
                conversations[branch]["complete"] = event["timestamp"]
        
        # Calculate conversation durations
        durations = []
        for branch, data in conversations.items():
            if data["start"] and data["complete"]:
                start_time = datetime.fromisoformat(data["start"])
                complete_time = datetime.fromisoformat(data["complete"])
                duration_minutes = (complete_time - start_time).total_seconds() / 60
                durations.append(duration_minutes)
        
        return {
            "active_conversations": len([c for c in conversations.values() if c["start"] and not c["complete"]]),
            "completed_conversations": len([c for c in conversations.values() if c["start"] and c["complete"]]),
            "avg_duration_minutes": sum(durations) / len(durations) if durations else 0,
            "total_events": len(conv_events)
        }
    
    def _analyze_health_trends(self, cutoff_time: datetime) -> Dict[str, Any]:
        """Analyze system health trends"""
        health_files = []
        if self.health_dir.exists():
            for file_path in self.health_dir.glob("system-health.log"):
                health_files.append(file_path)
        
        # Basic health trend analysis
        return {
            "health_checks": len(health_files),
            "trend": "stable"  # Simple placeholder
        }
    
    def _generate_performance_summary(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Generate overall performance summary"""
        git_ops = analysis.get("git_operations", {})
        hook_perf = analysis.get("hook_performance", {})
        conv_metrics = analysis.get("conversation_metrics", {})
        
        # Calculate overall performance score (0-100)
        score = 100
        
        # Penalize for performance issues
        if git_ops.get("performance_issues", 0) > 0:
            score -= min(20, git_ops["performance_issues"] * 5)
        
        if hook_perf.get("performance_issues", 0) > 0:
            score -= min(30, hook_perf["performance_issues"] * 10)
        
        # Penalize for low success rates
        if git_ops.get("success_rate", 100) < 95:
            score -= (95 - git_ops["success_rate"]) * 2
        
        return {
            "overall_score": max(0, score),
            "status": "excellent" if score >= 90 else "good" if score >= 70 else "warning" if score >= 50 else "critical",
            "recommendations": self._generate_recommendations(analysis)
        }
    
    def _generate_recommendations(self, analysis: Dict[str, Any]) -> List[str]:
        """Generate performance improvement recommendations"""
        recommendations = []
        
        git_ops = analysis.get("git_operations", {})
        hook_perf = analysis.get("hook_performance", {})
        
        if git_ops.get("avg_execution_ms", 0) > 500:
            recommendations.append("Consider git gc to optimize repository performance")
        
        if hook_perf.get("performance_issues", 0) > 0:
            recommendations.append("Review Git hooks for performance optimization")
        
        if git_ops.get("success_rate", 100) < 95:
            recommendations.append("Investigate Git operation failures")
        
        if not recommendations:
            recommendations.append("System performance is optimal")
        
        return recommendations
    
    def _save_analysis(self, analysis: Dict[str, Any]) -> None:
        """Save analysis results to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.metrics_dir / f"performance_analysis_{timestamp}.json"
        
        try:
            with open(filename, 'w') as f:
                json.dump(analysis, f, indent=2)
        except:
            pass
    
    def _format_as_text(self, analysis: Dict[str, Any]) -> str:
        """Format analysis as readable text report"""
        lines = []
        lines.append("📊 Git Workflow Performance Analysis")
        lines.append("=" * 50)
        lines.append(f"Analysis Period: {analysis['period_hours']} hours")
        lines.append(f"Generated: {analysis['analysis_time']}")
        lines.append("")
        
        # Git Operations
        git_ops = analysis.get("git_operations", {})
        lines.append("🔧 Git Operations Performance:")
        lines.append(f"  Total Operations: {git_ops.get('count', 0)}")
        lines.append(f"  Average Time: {git_ops.get('avg_execution_ms', 0):.1f}ms")
        lines.append(f"  Success Rate: {git_ops.get('success_rate', 0):.1f}%")
        lines.append(f"  Performance Issues: {git_ops.get('performance_issues', 0)}")
        lines.append("")
        
        # Hook Performance
        hook_perf = analysis.get("hook_performance", {})
        lines.append("🪝 Git Hooks Performance:")
        lines.append(f"  Total Executions: {hook_perf.get('count', 0)}")
        lines.append(f"  Average Time: {hook_perf.get('avg_execution_ms', 0):.1f}ms")
        lines.append(f"  Success Rate: {hook_perf.get('success_rate', 0):.1f}%")
        lines.append(f"  Performance Issues: {hook_perf.get('performance_issues', 0)}")
        lines.append("")
        
        # Conversation Metrics
        conv_metrics = analysis.get("conversation_metrics", {})
        lines.append("💬 Conversation Workflow:")
        lines.append(f"  Active Conversations: {conv_metrics.get('active_conversations', 0)}")
        lines.append(f"  Completed Conversations: {conv_metrics.get('completed_conversations', 0)}")
        lines.append(f"  Average Duration: {conv_metrics.get('avg_duration_minutes', 0):.1f} minutes")
        lines.append("")
        
        # Performance Summary
        summary = analysis.get("performance_summary", {})
        lines.append("📈 Performance Summary:")
        lines.append(f"  Overall Score: {summary.get('overall_score', 0)}/100")
        lines.append(f"  Status: {summary.get('status', 'unknown').upper()}")
        lines.append("")
        
        # Recommendations
        recommendations = summary.get("recommendations", [])
        if recommendations:
            lines.append("💡 Recommendations:")
            for rec in recommendations:
                lines.append(f"  • {rec}")
        
        return "\n".join(lines)
    
    def _format_as_csv(self, analysis: Dict[str, Any]) -> str:
        """Format analysis as CSV data"""
        lines = []
        lines.append("metric,value,unit")
        
        git_ops = analysis.get("git_operations", {})
        lines.append(f"git_operations_count,{git_ops.get('count', 0)},count")
        lines.append(f"git_operations_avg_time,{git_ops.get('avg_execution_ms', 0):.1f},milliseconds")
        lines.append(f"git_operations_success_rate,{git_ops.get('success_rate', 0):.1f},percent")
        
        hook_perf = analysis.get("hook_performance", {})
        lines.append(f"git_hooks_count,{hook_perf.get('count', 0)},count")
        lines.append(f"git_hooks_avg_time,{hook_perf.get('avg_execution_ms', 0):.1f},milliseconds")
        lines.append(f"git_hooks_success_rate,{hook_perf.get('success_rate', 0):.1f},percent")
        
        conv_metrics = analysis.get("conversation_metrics", {})
        lines.append(f"conversations_active,{conv_metrics.get('active_conversations', 0)},count")
        lines.append(f"conversations_completed,{conv_metrics.get('completed_conversations', 0)},count")
        lines.append(f"conversations_avg_duration,{conv_metrics.get('avg_duration_minutes', 0):.1f},minutes")
        
        summary = analysis.get("performance_summary", {})
        lines.append(f"overall_score,{summary.get('overall_score', 0)},score")
        
        return "\n".join(lines)

def main():
    """Main execution for command-line usage"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Performance Metrics Analyzer")
    parser.add_argument("--project-root", help="Project root directory")
    parser.add_argument("--analyze", type=int, default=24, help="Analyze performance for N hours")
    parser.add_argument("--report", choices=["text", "json", "csv"], default="text", help="Report format")
    parser.add_argument("--alerts", action="store_true", help="Show performance alerts")
    parser.add_argument("--continuous", type=int, help="Continuous monitoring (seconds interval)")
    
    args = parser.parse_args()
    
    analyzer = MetricsAnalyzer(args.project_root)
    
    if args.continuous:
        print(f"🔄 Starting continuous metrics monitoring (interval: {args.continuous}s)")
        try:
            while True:
                alerts = analyzer.get_performance_alerts()
                if alerts:
                    print(f"{datetime.now().strftime('%H:%M:%S')} - Alerts: {len(alerts)}")
                    for alert in alerts:
                        print(f"  ⚠️ {alert['severity'].upper()}: {alert['message']}")
                else:
                    print(f"{datetime.now().strftime('%H:%M:%S')} - No performance alerts")
                time.sleep(args.continuous)
        except KeyboardInterrupt:
            print("\nMonitoring stopped")
    
    elif args.alerts:
        alerts = analyzer.get_performance_alerts()
        if alerts:
            print("⚠️ Performance Alerts:")
            for alert in alerts:
                print(f"  {alert['severity'].upper()}: {alert['message']}")
        else:
            print("✅ No performance alerts")
    
    else:
        report = analyzer.generate_performance_report(args.report)
        print(report)

if __name__ == "__main__":
    main()