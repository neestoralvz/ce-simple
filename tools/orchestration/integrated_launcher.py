#!/usr/bin/env python3
"""
Integrated Launcher for Complete Multi-Conversation System
Combines background monitoring + orchestration system
"""

import json
import subprocess
import time
import threading
from pathlib import Path
from typing import Dict, List, Any

from conversation_orchestrator import get_orchestrator
from conversation_interface import ConversationClient

class IntegratedSystem:
    """Complete multi-conversation system with monitoring integration"""
    
    def __init__(self, base_dir: str = "/Users/nalve/ce-simple"):
        self.base_dir = Path(base_dir)
        self.launchers_dir = self.base_dir / "tools" / "launchers"
        self.orchestration_dir = self.base_dir / "tools" / "orchestration"
        
        # System components
        self.health_monitor_running = False
        self.orchestration_active = False
        self.dashboard_running = False
        
    def start_complete_system(self):
        """Start the complete integrated system"""
        print("🚀 Starting Complete Multi-Conversation System...")
        print("=" * 60)
        
        # 1. Start health monitoring
        print("📊 Starting Health Monitor...")
        if self._start_health_monitor():
            print("✅ Health Monitor: RUNNING")
            self.health_monitor_running = True
        else:
            print("❌ Health Monitor: FAILED")
        
        # 2. Initialize orchestration system
        print("\n🎯 Initializing Orchestration System...")
        try:
            self.orchestrator = get_orchestrator()
            print("✅ Orchestration: INITIALIZED")
            self.orchestration_active = True
        except Exception as e:
            print(f"❌ Orchestration: FAILED - {e}")
        
        # 3. Create sample tasks for demonstration
        print("\n📋 Setting up Demo Tasks...")
        self._create_demo_tasks()
        
        # 4. Show system status
        print("\n📈 System Status:")
        self._show_system_status()
        
        print("\n" + "=" * 60)
        print("🎉 Multi-Conversation System READY!")
        print("\nNext steps:")
        print("  1. Open multiple Claude Code terminals")
        print("  2. In each terminal, run: python3 tools/orchestration/conversation_interface.py setup <type>")
        print("  3. Start dashboard: python3 tools/orchestration/orchestration_dashboard.py monitor")
        print("\nAvailable conversation types: git, testing, implementation, monitoring")
        
    def _start_health_monitor(self) -> bool:
        """Start health monitoring background process"""
        try:
            result = subprocess.run([
                str(self.launchers_dir / "start_health_monitor.sh"), "start"
            ], capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                # Verify it started
                time.sleep(2)
                status_result = subprocess.run([
                    "python3", str(self.launchers_dir / "claude_code_integration.py"), "check-all"
                ], capture_output=True, text=True, timeout=10)
                
                if status_result.returncode == 0:
                    status_data = json.loads(status_result.stdout)
                    return status_data.get("processes", {}).get("health_monitor", {}).get("health_monitor", {}).get("status") == "running"
            
            return False
            
        except Exception as e:
            print(f"Error starting health monitor: {e}")
            return False
    
    def _create_demo_tasks(self):
        """Create demonstration tasks"""
        try:
            # Create a demo client
            demo_client = ConversationClient("system_setup", ["system_administration"])
            
            # Create sample tasks
            tasks_created = []
            
            # Git workflow task
            task1 = demo_client.create_task(
                title="Clean Git Repository",
                description="Push 3 commits ahead and stage 5 untracked files from current git status",
                task_type="git_workflow",
                priority=1,
                estimated_minutes=10
            )
            if task1:
                tasks_created.append(("Git Cleanup", task1))
            
            # Testing task
            task2 = demo_client.create_task(
                title="Validate Multi-Conversation System",
                description="Test /start-concurrent-worktrees command and verify functionality",
                task_type="testing", 
                priority=2,
                estimated_minutes=20
            )
            if task2:
                tasks_created.append(("System Validation", task2))
            
            # Implementation task
            task3 = demo_client.create_task(
                title="Implement Feature Enhancement",
                description="Add new functionality based on parallel conversation testing results",
                task_type="implementation",
                priority=3,
                depends_on=task2,
                estimated_minutes=45
            )
            if task3:
                tasks_created.append(("Feature Implementation", task3))
            
            # Monitoring task
            task4 = demo_client.create_task(
                title="Monitor System Performance",
                description="Track multi-conversation orchestration performance and optimize",
                task_type="monitoring",
                priority=2,
                estimated_minutes=30
            )
            if task4:
                tasks_created.append(("Performance Monitoring", task4))
            
            print(f"✅ Created {len(tasks_created)} demo tasks:")
            for name, task_id in tasks_created:
                print(f"   - {name} (ID: {task_id[:8]})")
                
        except Exception as e:
            print(f"❌ Error creating demo tasks: {e}")
    
    def _show_system_status(self):
        """Show current system status"""
        try:
            # Health monitor status
            health_status = subprocess.run([
                "python3", str(self.launchers_dir / "claude_code_integration.py"), "check-all"
            ], capture_output=True, text=True, timeout=10)
            
            if health_status.returncode == 0:
                health_data = json.loads(health_status.stdout)
                health_monitor = health_data.get("processes", {}).get("health_monitor", {})
                if health_monitor.get("health_monitor", {}).get("status") == "running":
                    print("  📊 Health Monitor: ✅ RUNNING")
                    print(f"     Database: {health_monitor.get('database', {}).get('health_records', 0)} records")
                else:
                    print("  📊 Health Monitor: ❌ NOT RUNNING")
            
            # Orchestration status
            if self.orchestration_active:
                status = self.orchestrator.get_system_status()
                print(f"  🎯 Orchestration: ✅ ACTIVE")
                print(f"     Active Conversations: {status.get('active_conversations', 0)}")
                print(f"     Total Tasks: {status.get('total_tasks', 0)}")
                print(f"     Recent Messages: {status.get('recent_messages', 0)}")
            else:
                print("  🎯 Orchestration: ❌ INACTIVE")
                
        except Exception as e:
            print(f"  ❌ Error getting system status: {e}")
    
    def stop_system(self):
        """Stop all system components"""
        print("🛑 Stopping Multi-Conversation System...")
        
        # Stop health monitor
        if self.health_monitor_running:
            try:
                subprocess.run([
                    str(self.launchers_dir / "stop_all_monitors.sh"), "stop"
                ], timeout=30)
                print("✅ Health Monitor: STOPPED")
            except Exception as e:
                print(f"❌ Error stopping health monitor: {e}")
        
        print("✅ System shutdown complete")
    
    def create_conversation_starter_scripts(self):
        """Create convenient starter scripts for different conversation types"""
        scripts_dir = self.base_dir / "tools" / "conversation_starters"
        scripts_dir.mkdir(exist_ok=True)
        
        conversation_types = {
            "git": {
                "capabilities": ["git_workflow", "repository_management"],
                "description": "Git workflow specialist"
            },
            "testing": {
                "capabilities": ["testing", "validation", "quality_assurance"],
                "description": "Testing and validation specialist"
            },
            "implementation": {
                "capabilities": ["implementation", "coding", "development"],
                "description": "Implementation and development specialist"
            },
            "monitoring": {
                "capabilities": ["monitoring", "health_checks", "system_analysis"],
                "description": "System monitoring specialist"
            }
        }
        
        for conv_type, config in conversation_types.items():
            script_content = f'''#!/usr/bin/env python3
"""
{config['description'].title()} Conversation Starter
Auto-connects to orchestration system with specialized capabilities
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'orchestration'))

from conversation_interface import ConversationClient

def main():
    print("🎯 Starting {config['description']}...")
    
    # Create specialized client
    client = ConversationClient(
        conversation_id="{conv_type}_specialist",
        capabilities={config['capabilities']}
    )
    
    print(f"✅ Connected to orchestration system")
    print(f"🔧 Capabilities: {', '.join(config['capabilities'])}")
    print("")
    
    # Show available tasks
    print("📋 Available tasks:")
    client.get_my_tasks()
    print("")
    
    # Check for messages
    print("📬 Recent messages:")
    messages = client.get_messages()
    if not messages:
        print("   No recent messages")
    print("")
    
    # Show system overview
    print("🌐 System overview:")
    client.get_system_overview()
    print("")
    
    print("💡 Conversation ready! You can now:")
    print(f"   - Claim tasks: client.claim_next_task()")
    print(f"   - Create tasks: client.create_task('Title', 'Description', 'task_type')")
    print(f"   - Send messages: client.broadcast('Your message')")
    print(f"   - Get overview: client.get_system_overview()")
    print("")
    print("🚀 Happy orchestrating!")
    
    return client

if __name__ == "__main__":
    client = main()
    
    # Keep the script running for interaction
    print("Press Ctrl+C to exit...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\\n👋 Conversation ended")
'''
            
            script_path = scripts_dir / f"start_{conv_type}_conversation.py"
            with open(script_path, 'w') as f:
                f.write(script_content)
            script_path.chmod(0o755)
        
        print(f"✅ Created conversation starter scripts in {scripts_dir}")
        return scripts_dir

def claude_start_complete_system():
    """Claude Code helper function to start the complete system"""
    system = IntegratedSystem()
    system.start_complete_system()
    return system

def claude_create_conversation(conv_type: str = "general"):
    """Claude Code helper to create a conversation client"""
    type_mapping = {
        "git": {"id": "git_specialist", "caps": ["git_workflow", "repository_management"]},
        "testing": {"id": "testing_specialist", "caps": ["testing", "validation"]},
        "implementation": {"id": "impl_specialist", "caps": ["implementation", "coding"]},
        "monitoring": {"id": "monitor_specialist", "caps": ["monitoring", "health_checks"]},
        "general": {"id": "general_specialist", "caps": ["general"]}
    }
    
    config = type_mapping.get(conv_type, type_mapping["general"])
    client = ConversationClient(config["id"], config["caps"])
    return client

def claude_quick_setup():
    """Quick setup for Claude Code - start system and create general conversation"""
    print("🚀 Quick Setup: Multi-Conversation System")
    
    # Start system
    system = IntegratedSystem()
    system.start_complete_system()
    
    # Create conversation client
    client = ConversationClient("claude_main", ["general", "orchestration"])
    
    print("\n✅ Quick setup complete!")
    print("🎯 You now have:")
    print("  - Background health monitoring running")
    print("  - Orchestration system active")
    print("  - Main conversation client ready")
    print("\n💡 Try these commands:")
    print("  - client.claim_next_task()")
    print("  - client.get_system_overview()")
    print("  - client.broadcast('Hello from Claude Code!')")
    
    return {"system": system, "client": client}

# CLI Interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "start":
            system = IntegratedSystem()
            system.start_complete_system()
        
        elif command == "stop":
            system = IntegratedSystem()  
            system.stop_system()
        
        elif command == "create-starters":
            system = IntegratedSystem()
            scripts_dir = system.create_conversation_starter_scripts()
            print(f"Starter scripts created in: {scripts_dir}")
        
        elif command == "quick":
            result = claude_quick_setup()
            print("System ready for use!")
        
        else:
            print(f"Unknown command: {command}")
            sys.exit(1)
    
    else:
        print("Usage: python integrated_launcher.py <command>")
        print("")
        print("Commands:")
        print("  start           - Start complete system")
        print("  stop            - Stop all components")
        print("  create-starters - Create conversation starter scripts")
        print("  quick           - Quick setup with defaults")
        print("")
        print("For Claude Code integration:")
        print("  claude_start_complete_system() - Start everything")
        print("  claude_create_conversation('git') - Create specialized conversation")
        print("  claude_quick_setup() - Quick setup with defaults")