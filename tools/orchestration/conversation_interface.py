#!/usr/bin/env python3
"""
Inter-Conversation Interface
Easy-to-use API for conversations to interact with the orchestration system
"""

import json
import os
import socket
from typing import Dict, List, Optional, Any
from datetime import datetime
from pathlib import Path

from conversation_orchestrator import (
    get_orchestrator, 
    ConversationTask, 
    TaskType, 
    TaskStatus, 
    MessageType
)

class ConversationClient:
    """Simple client interface for conversations to use orchestration system"""
    
    def __init__(self, conversation_id: str = None, capabilities: List[str] = None):
        self.conversation_id = conversation_id or self._generate_conversation_id()
        self.capabilities = capabilities or ["general"]
        self.orchestrator = get_orchestrator()
        
        # Register this conversation
        self.orchestrator.register_conversation(self.conversation_id, self.capabilities)
        
        print(f"🎯 Conversation {self.conversation_id} registered with capabilities: {self.capabilities}")
    
    def _generate_conversation_id(self) -> str:
        """Generate unique conversation ID based on environment"""
        hostname = socket.gethostname()
        pid = os.getpid()
        timestamp = datetime.now().strftime("%H%M%S")
        return f"conv_{hostname}_{pid}_{timestamp}"
    
    # === TASK MANAGEMENT ===
    
    def create_task(self, title: str, description: str, task_type: str,
                   priority: int = 3, depends_on: str = None, 
                   estimated_minutes: int = None) -> str:
        """
        Create a new task
        
        Args:
            title: Short task description
            description: Detailed task description  
            task_type: Type of task (git_workflow, testing, implementation, etc.)
            priority: 1=highest, 5=lowest
            depends_on: ID of task this depends on
            estimated_minutes: Estimated completion time
            
        Returns:
            task_id if successful, None if failed
        """
        try:
            task_type_enum = TaskType(task_type)
            task_id = self.orchestrator.create_task(
                conversation_id=self.conversation_id,
                title=title,
                description=description,
                task_type=task_type_enum,
                priority=priority,
                depends_on=depends_on,
                estimated_minutes=estimated_minutes
            )
            
            if task_id:
                print(f"✅ Created task: {title} (ID: {task_id[:8]})")
            else:
                print(f"❌ Failed to create task: {title}")
                
            return task_id
            
        except ValueError as e:
            print(f"❌ Invalid task type '{task_type}'. Valid types: {[t.value for t in TaskType]}")
            return None
        except Exception as e:
            print(f"❌ Error creating task: {e}")
            return None
    
    def claim_next_task(self, task_types: List[str] = None) -> Optional[ConversationTask]:
        """
        Claim the next available task
        
        Args:
            task_types: List of task types to consider (optional)
            
        Returns:
            ConversationTask if claimed, None if no tasks available
        """
        try:
            type_enums = None
            if task_types:
                type_enums = [TaskType(t) for t in task_types]
                
            task = self.orchestrator.claim_task(self.conversation_id, type_enums)
            
            if task:
                print(f"🎯 Claimed task: {task.title} (ID: {task.task_id[:8]})")
                print(f"   Type: {task.task_type.value}, Priority: {task.priority}")
                print(f"   Description: {task.description}")
                
                # Auto-update to in_progress
                self.update_task_status(task.task_id, "in_progress", "Started working on task")
            else:
                print("📭 No available tasks to claim")
                
            return task
            
        except ValueError as e:
            print(f"❌ Invalid task type in {task_types}")
            return None
        except Exception as e:
            print(f"❌ Error claiming task: {e}")
            return None
    
    def update_task_status(self, task_id: str, status: str, message: str = None) -> bool:
        """
        Update task status
        
        Args:
            task_id: Task ID to update
            status: New status (pending, claimed, in_progress, completed, failed, blocked)
            message: Optional status message
            
        Returns:
            True if successful
        """
        try:
            status_enum = TaskStatus(status)
            success = self.orchestrator.update_task_status(
                task_id=task_id,
                status=status_enum,
                conversation_id=self.conversation_id,
                message=message
            )
            
            if success:
                print(f"✅ Updated task {task_id[:8]} status to: {status}")
                if message:
                    print(f"   Message: {message}")
            else:
                print(f"❌ Failed to update task {task_id[:8]} status")
                
            return success
            
        except ValueError as e:
            print(f"❌ Invalid status '{status}'. Valid statuses: {[s.value for s in TaskStatus]}")
            return False
        except Exception as e:
            print(f"❌ Error updating task status: {e}")
            return False
    
    def complete_task(self, task_id: str, message: str = "Task completed successfully") -> bool:
        """Mark task as completed"""
        return self.update_task_status(task_id, "completed", message)
    
    def fail_task(self, task_id: str, message: str = "Task failed") -> bool:
        """Mark task as failed"""
        return self.update_task_status(task_id, "failed", message)
    
    def delegate_task(self, to_conversation: str, title: str, description: str,
                     task_type: str, priority: int = 3) -> str:
        """
        Delegate a task to another conversation
        
        Args:
            to_conversation: Target conversation ID
            title: Task title
            description: Task description
            task_type: Type of task
            priority: Task priority
            
        Returns:
            task_id if successful
        """
        try:
            task_type_enum = TaskType(task_type)
            task_id = self.orchestrator.delegate_task(
                from_conversation=self.conversation_id,
                to_conversation=to_conversation,
                title=title,
                description=description,
                task_type=task_type_enum,
                priority=priority
            )
            
            if task_id:
                print(f"📤 Delegated task to {to_conversation}: {title} (ID: {task_id[:8]})")
            else:
                print(f"❌ Failed to delegate task to {to_conversation}")
                
            return task_id
            
        except ValueError as e:
            print(f"❌ Invalid task type '{task_type}'")
            return None
        except Exception as e:
            print(f"❌ Error delegating task: {e}")
            return None
    
    # === COMMUNICATION ===
    
    def send_message(self, to_conversation: str, message_type: str, content: Dict[str, Any]) -> str:
        """
        Send a message to another conversation
        
        Args:
            to_conversation: Target conversation ID or 'broadcast'
            message_type: Type of message (status_update, help_request, etc.)
            content: Message content
            
        Returns:
            message_id if successful
        """
        try:
            message_type_enum = MessageType(message_type)
            message_id = self.orchestrator.send_message(
                from_conversation=self.conversation_id,
                to_conversation=to_conversation,
                message_type=message_type_enum,
                content=content
            )
            
            if message_id:
                target = to_conversation if to_conversation != "broadcast" else "ALL"
                print(f"📨 Sent {message_type} to {target} (ID: {message_id[:8]})")
            else:
                print(f"❌ Failed to send message")
                
            return message_id
            
        except ValueError as e:
            print(f"❌ Invalid message type '{message_type}'. Valid types: {[t.value for t in MessageType]}")
            return None
        except Exception as e:
            print(f"❌ Error sending message: {e}")
            return None
    
    def broadcast(self, message: str, data: Dict[str, Any] = None) -> str:
        """Send broadcast message to all conversations"""
        content = {"message": message}
        if data:
            content.update(data)
            
        return self.send_message("broadcast", "broadcast", content)
    
    def request_help(self, issue: str, details: Dict[str, Any] = None) -> str:
        """Request help from other conversations"""
        content = {"issue": issue, "from": self.conversation_id}
        if details:
            content.update(details)
            
        return self.send_message("broadcast", "help_request", content)
    
    def get_messages(self, unread_only: bool = True) -> List[Dict[str, Any]]:
        """
        Get messages for this conversation
        
        Args:
            unread_only: Only return unread messages
            
        Returns:
            List of message dictionaries
        """
        try:
            messages = self.orchestrator.get_messages(self.conversation_id, unread_only)
            
            message_dicts = []
            for msg in messages:
                message_dict = msg.to_dict()
                message_dicts.append(message_dict)
                
                # Mark as read
                self.orchestrator.mark_message_read(msg.message_id, self.conversation_id)
            
            if message_dicts:
                print(f"📬 Retrieved {len(message_dicts)} {'unread ' if unread_only else ''}messages")
            
            return message_dicts
            
        except Exception as e:
            print(f"❌ Error getting messages: {e}")
            return []
    
    # === STATUS AND MONITORING ===
    
    def get_my_tasks(self) -> List[Dict[str, Any]]:
        """Get tasks assigned to this conversation"""
        try:
            tasks = self.orchestrator.get_active_tasks(self.conversation_id)
            task_dicts = [task.to_dict() for task in tasks]
            
            if task_dicts:
                print(f"📋 Found {len(task_dicts)} active tasks")
                for task in task_dicts[:3]:  # Show first 3
                    print(f"   - {task['title']} ({task['status']})")
            else:
                print("📋 No active tasks assigned")
                
            return task_dicts
            
        except Exception as e:
            print(f"❌ Error getting tasks: {e}")
            return []
    
    def get_system_overview(self) -> Dict[str, Any]:
        """Get overview of entire orchestration system"""
        try:
            status = self.orchestrator.get_system_status()
            
            print(f"🌐 System Overview:")
            print(f"   Active Conversations: {status.get('active_conversations', 0)}")
            print(f"   Total Tasks: {status.get('total_tasks', 0)}")
            print(f"   Recent Messages: {status.get('recent_messages', 0)}")
            
            task_counts = status.get('task_counts', {})
            if task_counts:
                print(f"   Task Status:")
                for status_name, count in task_counts.items():
                    print(f"     {status_name}: {count}")
            
            return status
            
        except Exception as e:
            print(f"❌ Error getting system overview: {e}")
            return {}
    
    def list_conversations(self) -> List[Dict[str, Any]]:
        """List all active conversations"""
        try:
            status = self.orchestrator.get_system_status()
            conversations = status.get('conversations', [])
            
            print(f"👥 Active Conversations ({len(conversations)}):")
            for conv in conversations:
                print(f"   - {conv['conversation_id']} ({', '.join(conv['capabilities'])})")
                print(f"     Last seen: {conv['last_seen']}")
            
            return conversations
            
        except Exception as e:
            print(f"❌ Error listing conversations: {e}")
            return []

# === CONVENIENCE FUNCTIONS FOR CLAUDE CODE ===

def claude_start_orchestration(conversation_id: str = None, capabilities: List[str] = None) -> ConversationClient:
    """
    Start orchestration for a Claude Code conversation
    
    Usage in Claude Code:
    client = claude_start_orchestration("terminal_1", ["git_workflow", "testing"])
    """
    return ConversationClient(conversation_id, capabilities)

def claude_create_task(client: ConversationClient, title: str, description: str, 
                      task_type: str = "implementation", priority: int = 3) -> str:
    """
    Create a task via Claude Code
    
    Usage:
    task_id = claude_create_task(client, "Fix git workflow", "Push commits and stage files", "git_workflow", 1)
    """
    return client.create_task(title, description, task_type, priority)

def claude_claim_task(client: ConversationClient, task_types: List[str] = None) -> Dict[str, Any]:
    """
    Claim next task via Claude Code
    
    Usage:
    task = claude_claim_task(client, ["git_workflow", "testing"])
    """
    task = client.claim_next_task(task_types)
    return task.to_dict() if task else None

def claude_complete_task(client: ConversationClient, task_id: str, message: str = "Completed") -> bool:
    """
    Complete a task via Claude Code
    
    Usage:
    claude_complete_task(client, task_id, "Git workflow completed successfully")
    """
    return client.complete_task(task_id, message)

def claude_get_overview(client: ConversationClient) -> Dict[str, Any]:
    """
    Get system overview via Claude Code
    
    Usage:
    overview = claude_get_overview(client)
    """
    return client.get_system_overview()

def claude_broadcast(client: ConversationClient, message: str) -> str:
    """
    Broadcast message via Claude Code
    
    Usage:
    claude_broadcast(client, "Starting git workflow cleanup")
    """
    return client.broadcast(message)

# Quick setup for different conversation types
def setup_git_conversation() -> ConversationClient:
    """Setup conversation specialized in git workflows"""
    return ConversationClient(
        conversation_id="git_specialist",
        capabilities=["git_workflow", "repository_management"]
    )

def setup_testing_conversation() -> ConversationClient:
    """Setup conversation specialized in testing"""
    return ConversationClient(
        conversation_id="testing_specialist", 
        capabilities=["testing", "validation", "quality_assurance"]
    )

def setup_implementation_conversation() -> ConversationClient:
    """Setup conversation specialized in implementation"""
    return ConversationClient(
        conversation_id="implementation_specialist",
        capabilities=["implementation", "coding", "development"]
    )

def setup_monitoring_conversation() -> ConversationClient:
    """Setup conversation specialized in monitoring"""
    return ConversationClient(
        conversation_id="monitoring_specialist",
        capabilities=["monitoring", "health_checks", "system_analysis"]
    )

# === COMMAND LINE INTERFACE ===

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python conversation_interface.py <command> [args...]")
        print("")
        print("Commands:")
        print("  setup <type>     - Setup conversation (git|testing|implementation|monitoring)")
        print("  create-task      - Interactive task creation")
        print("  claim-task       - Claim next available task")
        print("  overview         - Show system overview")
        print("  messages         - Show recent messages")
        print("  test             - Run test scenario")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "setup":
        conv_type = sys.argv[2] if len(sys.argv) > 2 else "general"
        
        if conv_type == "git":
            client = setup_git_conversation()
        elif conv_type == "testing":
            client = setup_testing_conversation()
        elif conv_type == "implementation":
            client = setup_implementation_conversation()
        elif conv_type == "monitoring":
            client = setup_monitoring_conversation()
        else:
            client = ConversationClient()
        
        print(f"Conversation setup complete: {client.conversation_id}")
    
    elif command == "create-task":
        client = ConversationClient()
        
        title = input("Task title: ")
        description = input("Task description: ")
        task_type = input("Task type (implementation): ") or "implementation"
        priority = int(input("Priority (1-5, default 3): ") or "3")
        
        task_id = client.create_task(title, description, task_type, priority)
        print(f"Created task: {task_id}")
    
    elif command == "claim-task":
        client = ConversationClient()
        task = client.claim_next_task()
        if task:
            print(f"Claimed: {task.title}")
        else:
            print("No tasks available")
    
    elif command == "overview":
        client = ConversationClient()
        client.get_system_overview()
    
    elif command == "messages":
        client = ConversationClient()
        messages = client.get_messages()
        for msg in messages:
            print(f"From {msg['from_conversation']}: {msg['content']}")
    
    elif command == "test":
        print("🧪 Running orchestration test scenario...")
        
        # Create test client
        client = ConversationClient("test_client", ["testing"])
        
        # Create some test tasks
        task1 = client.create_task("Test Git Workflow", "Test push and stage operations", "git_workflow", 1)
        task2 = client.create_task("Run System Tests", "Execute validation tests", "testing", 2)
        
        # Claim and work on task
        claimed = client.claim_next_task()
        if claimed:
            client.complete_task(claimed.task_id, "Test completed successfully")
        
        # Send test broadcast
        client.broadcast("Test orchestration system operational")
        
        # Get overview
        client.get_system_overview()
        
        print("✅ Test scenario completed")
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)