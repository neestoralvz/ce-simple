#!/usr/bin/env python3
"""
Real-time Orchestration Dashboard
Live monitoring of multi-conversation coordination system
"""

import json
import time
import threading
from datetime import datetime
from typing import Dict, List, Any
from pathlib import Path

from conversation_orchestrator import get_orchestrator, TaskStatus, TaskType

class OrchestrationDashboard:
    """Real-time dashboard for conversation orchestration system"""
    
    def __init__(self, refresh_interval: int = 5):
        self.orchestrator = get_orchestrator()
        self.refresh_interval = refresh_interval
        self.running = False
        
    def start_monitoring(self):
        """Start real-time dashboard monitoring"""
        self.running = True
        
        print("🚀 Starting Orchestration Dashboard...")
        print("Press Ctrl+C to stop\n")
        
        try:
            while self.running:
                self.display_dashboard()
                time.sleep(self.refresh_interval)
        except KeyboardInterrupt:
            print("\n\n👋 Dashboard stopped by user")
            self.running = False
    
    def display_dashboard(self):
        """Display current system status"""
        # Clear screen
        print("\033[2J\033[H", end="")
        
        # Header
        print("=" * 80)
        print(f"🎯 MULTI-CONVERSATION ORCHESTRATION DASHBOARD")
        print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Refresh: {self.refresh_interval}s")
        print("=" * 80)
        
        # Get system status
        status = self.orchestrator.get_system_status()
        
        # System Overview
        print(f"\n📊 SYSTEM OVERVIEW")
        print(f"├─ Active Conversations: {status.get('active_conversations', 0)}")
        print(f"├─ Total Tasks: {status.get('total_tasks', 0)}")
        print(f"├─ Recent Messages: {status.get('recent_messages', 0)}")
        print(f"└─ System Health: {status.get('system_health', 'unknown').upper()}")
        
        # Task Status Breakdown
        task_counts = status.get('task_counts', {})
        if task_counts:
            print(f"\n📋 TASK STATUS BREAKDOWN")
            total_tasks = sum(task_counts.values())
            
            for status_name, count in task_counts.items():
                percentage = (count / total_tasks * 100) if total_tasks > 0 else 0
                bar = self._create_progress_bar(percentage, 20)
                emoji = self._get_status_emoji(status_name)
                print(f"├─ {emoji} {status_name.title():<12}: {count:>3} {bar} {percentage:5.1f}%")
        
        # Active Conversations
        conversations = status.get('conversations', [])
        if conversations:
            print(f"\n👥 ACTIVE CONVERSATIONS ({len(conversations)})")
            for i, conv in enumerate(conversations):
                prefix = "├─" if i < len(conversations) - 1 else "└─"
                conv_id = conv['conversation_id']
                capabilities = ', '.join(conv['capabilities'])
                last_seen = conv['last_seen']
                
                # Parse timestamp and show relative time
                try:
                    last_dt = datetime.fromisoformat(last_seen.replace('Z', '+00:00'))
                    time_diff = datetime.now() - last_dt.replace(tzinfo=None)
                    if time_diff.total_seconds() < 60:
                        time_str = f"{int(time_diff.total_seconds())}s ago"
                    else:
                        time_str = f"{int(time_diff.total_seconds() / 60)}m ago"
                except:
                    time_str = "unknown"
                
                print(f"{prefix} 🤖 {conv_id:<20} | 🎯 {capabilities:<20} | ⏰ {time_str}")
        
        # Recent Tasks (last 10)
        recent_tasks = self.orchestrator.get_active_tasks()[:10]
        if recent_tasks:
            print(f"\n📌 RECENT ACTIVE TASKS (showing {len(recent_tasks)})")
            for i, task in enumerate(recent_tasks):
                prefix = "├─" if i < len(recent_tasks) - 1 else "└─"
                
                # Task info
                task_id = task.task_id[:8]
                title = task.title[:30] + "..." if len(task.title) > 30 else task.title
                status_emoji = self._get_status_emoji(task.status.value)
                type_emoji = self._get_type_emoji(task.task_type.value)
                priority_indicator = "🔥" * (6 - task.priority) if task.priority <= 5 else ""
                
                # Assigned info
                assigned = task.assigned_to or "unassigned"
                if assigned != "unassigned":
                    assigned = assigned[:15] + "..." if len(assigned) > 15 else assigned
                
                print(f"{prefix} {status_emoji} {type_emoji} {task_id} | {priority_indicator:<5} {title:<35} | 👤 {assigned}")
        else:
            print(f"\n📌 RECENT ACTIVE TASKS")
            print("└─ No active tasks")
        
        # System Statistics
        self._display_statistics()
        
        # Control Instructions
        print(f"\n{'─' * 80}")
        print(f"💡 Press Ctrl+C to stop | Refresh every {self.refresh_interval}s")
        print(f"🔧 System monitoring: Health Monitor (PID: check status)")
    
    def _display_statistics(self):
        """Display system performance statistics"""
        try:
            # Get all tasks for statistics
            conn = self.orchestrator._get_db()
            
            # Task completion rate (last 24 hours)
            cursor = conn.execute('''
                SELECT 
                    COUNT(*) as total,
                    SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) as completed
                FROM conversation_tasks 
                WHERE created_at > datetime('now', '-24 hours')
            ''')
            row = cursor.fetchone()
            total_24h = row[0] if row else 0
            completed_24h = row[1] if row else 0
            completion_rate = (completed_24h / total_24h * 100) if total_24h > 0 else 0
            
            # Average task time
            cursor = conn.execute('''
                SELECT AVG(
                    (julianday(updated_at) - julianday(claimed_at)) * 24 * 60
                ) as avg_minutes
                FROM conversation_tasks 
                WHERE status = 'completed' 
                AND claimed_at IS NOT NULL 
                AND updated_at > datetime('now', '-24 hours')
            ''')
            row = cursor.fetchone()
            avg_time = row[0] if row and row[0] else 0
            
            # Message activity
            cursor = conn.execute('''
                SELECT COUNT(*) 
                FROM conversation_messages 
                WHERE created_at > datetime('now', '-1 hour')
            ''')
            messages_1h = cursor.fetchone()[0]
            
            print(f"\n📈 PERFORMANCE STATISTICS (24h)")
            print(f"├─ 📊 Completion Rate: {completion_rate:.1f}% ({completed_24h}/{total_24h})")
            print(f"├─ ⏱️  Avg Task Time: {avg_time:.1f} minutes")
            print(f"├─ 💬 Messages/Hour: {messages_1h}")
            print(f"└─ 🎯 System Load: {'High' if total_24h > 20 else 'Normal' if total_24h > 5 else 'Light'}")
            
        except Exception as e:
            print(f"\n📈 PERFORMANCE STATISTICS")
            print(f"└─ ❌ Error loading statistics: {e}")
    
    def _create_progress_bar(self, percentage: float, width: int = 20) -> str:
        """Create ASCII progress bar"""
        filled = int(percentage / 100 * width)
        bar = "█" * filled + "░" * (width - filled)
        return f"[{bar}]"
    
    def _get_status_emoji(self, status: str) -> str:
        """Get emoji for task status"""
        status_emojis = {
            "pending": "⏳",
            "claimed": "🎯", 
            "in_progress": "⚡",
            "completed": "✅",
            "failed": "❌",
            "blocked": "🚫"
        }
        return status_emojis.get(status, "❓")
    
    def _get_type_emoji(self, task_type: str) -> str:
        """Get emoji for task type"""
        type_emojis = {
            "git_workflow": "🔄",
            "testing": "🧪",
            "implementation": "💻",
            "monitoring": "📊",
            "research": "🔍",
            "documentation": "📝",
            "validation": "✅"
        }
        return type_emojis.get(task_type, "📋")
    
    def generate_report(self) -> Dict[str, Any]:
        """Generate detailed system report"""
        status = self.orchestrator.get_system_status()
        
        # Enhanced statistics
        conn = self.orchestrator._get_db()
        
        # Task distribution by type
        cursor = conn.execute('''
            SELECT task_type, COUNT(*) as count
            FROM conversation_tasks
            WHERE status NOT IN ('completed', 'failed')
            GROUP BY task_type
        ''')
        task_types = dict(cursor.fetchall())
        
        # Conversation workload
        cursor = conn.execute('''
            SELECT assigned_to, COUNT(*) as active_tasks
            FROM conversation_tasks
            WHERE status IN ('claimed', 'in_progress')
            AND assigned_to IS NOT NULL
            GROUP BY assigned_to
        ''')
        workloads = dict(cursor.fetchall())
        
        # Recent activity
        cursor = conn.execute('''
            SELECT DATE(created_at) as date, COUNT(*) as tasks_created
            FROM conversation_tasks
            WHERE created_at > datetime('now', '-7 days')
            GROUP BY DATE(created_at)
            ORDER BY date DESC
        ''')
        daily_activity = dict(cursor.fetchall())
        
        report = {
            **status,
            "task_distribution": task_types,
            "conversation_workloads": workloads,
            "daily_activity": daily_activity,
            "report_generated": datetime.now().isoformat()
        }
        
        return report
    
    def export_report(self, filepath: str = None):
        """Export system report to JSON file"""
        if filepath is None:
            filepath = f"data/orchestration/reports/system_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        report_path = Path(filepath)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        
        report = self.generate_report()
        
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"📊 Report exported to: {report_path}")
        return str(report_path)

# Command-line interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "monitor":
            dashboard = OrchestrationDashboard()
            dashboard.start_monitoring()
        
        elif command == "status":
            dashboard = OrchestrationDashboard()
            dashboard.display_dashboard()
        
        elif command == "report":
            dashboard = OrchestrationDashboard()
            report = dashboard.generate_report()
            print(json.dumps(report, indent=2))
        
        elif command == "export":
            dashboard = OrchestrationDashboard()
            filepath = sys.argv[2] if len(sys.argv) > 2 else None
            dashboard.export_report(filepath)
        
        else:
            print(f"Unknown command: {command}")
            sys.exit(1)
    
    else:
        print("Usage: python orchestration_dashboard.py <command>")
        print("")
        print("Commands:")
        print("  monitor  - Start real-time dashboard")
        print("  status   - Show current status once")
        print("  report   - Generate JSON report")
        print("  export   - Export report to file")
        print("")
        print("Examples:")
        print("  python orchestration_dashboard.py monitor")
        print("  python orchestration_dashboard.py export my_report.json")