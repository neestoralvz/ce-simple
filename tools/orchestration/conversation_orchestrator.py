#!/usr/bin/env python3
"""
Multi-Conversation Orchestration System
Intelligent task delegation and inter-conversation communication
"""

import json
import sqlite3
import uuid
import threading
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path
from dataclasses import dataclass, asdict
from enum import Enum

class TaskStatus(Enum):
    PENDING = "pending"
    CLAIMED = "claimed"
    IN_PROGRESS = "in_progress"  
    COMPLETED = "completed"
    FAILED = "failed"
    BLOCKED = "blocked"

class TaskType(Enum):
    GIT_WORKFLOW = "git_workflow"
    TESTING = "testing"
    IMPLEMENTATION = "implementation"
    MONITORING = "monitoring"
    RESEARCH = "research"
    DOCUMENTATION = "documentation"
    VALIDATION = "validation"

class MessageType(Enum):
    STATUS_UPDATE = "status_update"
    TASK_REQUEST = "task_request"
    HELP_REQUEST = "help_request"
    COMPLETION_NOTICE = "completion_notice"
    BROADCAST = "broadcast"
    DELEGATION = "delegation"

@dataclass
class ConversationTask:
    """Individual task in the orchestration system"""
    task_id: str
    conversation_id: str
    priority: int  # 1=highest, 5=lowest
    status: TaskStatus
    task_type: TaskType
    title: str
    description: str
    assigned_to: Optional[str] = None
    claimed_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    depends_on: Optional[str] = None  # task_id of dependency
    metadata: Optional[Dict[str, Any]] = None
    estimated_minutes: Optional[int] = None
    
    def to_dict(self) -> Dict:
        data = asdict(self)
        # Convert enums to strings
        data['status'] = self.status.value
        data['task_type'] = self.task_type.value
        # Convert timestamps to ISO strings
        for field in ['claimed_at', 'created_at', 'updated_at']:
            if data[field]:
                data[field] = data[field].isoformat()
        return data

@dataclass
class ConversationMessage:
    """Inter-conversation message"""
    message_id: str
    from_conversation: str
    to_conversation: str  # or 'broadcast'
    message_type: MessageType
    content: Dict[str, Any]
    read_by: List[str]
    created_at: datetime
    
    def to_dict(self) -> Dict:
        data = asdict(self)
        data['message_type'] = self.message_type.value
        data['created_at'] = self.created_at.isoformat()
        return data

class ConversationOrchestrator:
    """Main orchestration system for multi-conversation coordination"""
    
    def __init__(self, db_path: str = "data/orchestration/conversations.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Thread-safe database connections
        self._local = threading.local()
        
        # Initialize database
        self._init_database()
        
        # Conversation registry
        self.active_conversations = {}  # conversation_id -> last_seen
        self.conversation_capabilities = {}  # conversation_id -> [capabilities]
        
        # Auto-cleanup thread
        self._start_cleanup_thread()
    
    def _get_db(self) -> sqlite3.Connection:
        """Get thread-local database connection"""
        if not hasattr(self._local, 'db'):
            self._local.db = sqlite3.connect(
                self.db_path,
                timeout=30.0,
                check_same_thread=False
            )
            self._local.db.execute("PRAGMA journal_mode=WAL")
            self._local.db.execute("PRAGMA synchronous=NORMAL")
        return self._local.db
    
    def _init_database(self):
        """Initialize SQLite database with orchestration schema"""
        conn = self._get_db()
        
        # Conversation tasks table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS conversation_tasks (
                task_id TEXT PRIMARY KEY,
                conversation_id TEXT NOT NULL,
                priority INTEGER NOT NULL DEFAULT 3,
                status TEXT NOT NULL DEFAULT 'pending',
                task_type TEXT NOT NULL,
                title TEXT NOT NULL,
                description TEXT,
                assigned_to TEXT,
                claimed_at TIMESTAMP,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                depends_on TEXT,
                metadata TEXT, -- JSON
                estimated_minutes INTEGER
            )
        ''')
        
        # Inter-conversation messages table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS conversation_messages (
                message_id TEXT PRIMARY KEY,
                from_conversation TEXT NOT NULL,
                to_conversation TEXT NOT NULL,
                message_type TEXT NOT NULL,
                content TEXT NOT NULL, -- JSON
                read_by TEXT NOT NULL DEFAULT '[]', -- JSON array
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Conversation registry table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS conversation_registry (
                conversation_id TEXT PRIMARY KEY,
                status TEXT NOT NULL DEFAULT 'active',
                capabilities TEXT NOT NULL DEFAULT '[]', -- JSON array
                last_seen TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                metadata TEXT DEFAULT '{}' -- JSON
            )
        ''')
        
        # Create indexes for performance
        conn.execute('CREATE INDEX IF NOT EXISTS idx_tasks_status ON conversation_tasks(status)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_tasks_priority ON conversation_tasks(priority)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_tasks_type ON conversation_tasks(task_type)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_tasks_assigned ON conversation_tasks(assigned_to)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_messages_to ON conversation_messages(to_conversation)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_messages_type ON conversation_messages(message_type)')
        
        conn.commit()
    
    def register_conversation(self, conversation_id: str, capabilities: List[str] = None) -> bool:
        """Register a conversation as active in the orchestration system"""
        if capabilities is None:
            capabilities = ["general"]
        
        conn = self._get_db()
        try:
            conn.execute('''
                INSERT OR REPLACE INTO conversation_registry 
                (conversation_id, capabilities, last_seen)
                VALUES (?, ?, CURRENT_TIMESTAMP)
            ''', (conversation_id, json.dumps(capabilities)))
            
            conn.commit()
            
            self.active_conversations[conversation_id] = datetime.now()
            self.conversation_capabilities[conversation_id] = capabilities
            
            return True
        except Exception as e:
            print(f"Error registering conversation {conversation_id}: {e}")
            return False
    
    def create_task(self, 
                   conversation_id: str,
                   title: str,
                   description: str,
                   task_type: TaskType,
                   priority: int = 3,
                   depends_on: str = None,
                   estimated_minutes: int = None,
                   metadata: Dict[str, Any] = None) -> str:
        """Create a new task in the orchestration system"""
        
        task_id = str(uuid.uuid4())
        
        conn = self._get_db()
        try:
            conn.execute('''
                INSERT INTO conversation_tasks 
                (task_id, conversation_id, priority, status, task_type, title, 
                 description, depends_on, metadata, estimated_minutes)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                task_id, conversation_id, priority, TaskStatus.PENDING.value,
                task_type.value, title, description, depends_on,
                json.dumps(metadata or {}), estimated_minutes
            ))
            
            conn.commit()
            
            # Broadcast task creation
            self._broadcast_message(
                from_conversation=conversation_id,
                message_type=MessageType.BROADCAST,
                content={
                    "event": "task_created",
                    "task_id": task_id,
                    "title": title,
                    "task_type": task_type.value,
                    "priority": priority
                }
            )
            
            return task_id
            
        except Exception as e:
            print(f"Error creating task: {e}")
            return None
    
    def claim_task(self, conversation_id: str, task_types: List[TaskType] = None) -> Optional[ConversationTask]:
        """Claim the next available task for a conversation"""
        
        # Update last seen
        self.active_conversations[conversation_id] = datetime.now()
        
        conn = self._get_db()
        
        # Build WHERE clause for task types
        type_filter = ""
        params = [TaskStatus.PENDING.value]
        
        if task_types:
            type_placeholders = ",".join("?" * len(task_types))
            type_filter = f"AND task_type IN ({type_placeholders})"
            params.extend([t.value for t in task_types])
        
        try:
            # Find highest priority available task with no unmet dependencies
            cursor = conn.execute(f'''
                SELECT task_id, conversation_id, priority, status, task_type, title, 
                       description, assigned_to, claimed_at, created_at, updated_at, 
                       depends_on, metadata, estimated_minutes
                FROM conversation_tasks 
                WHERE status = ? 
                  {type_filter}
                  AND (depends_on IS NULL OR depends_on IN (
                      SELECT task_id FROM conversation_tasks WHERE status = 'completed'
                  ))
                ORDER BY priority ASC, created_at ASC
                LIMIT 1
            ''', params)
            
            row = cursor.fetchone()
            if not row:
                return None
            
            task_id = row[0]
            
            # Atomically claim the task
            result = conn.execute('''
                UPDATE conversation_tasks 
                SET status = ?, assigned_to = ?, claimed_at = CURRENT_TIMESTAMP,
                    updated_at = CURRENT_TIMESTAMP
                WHERE task_id = ? AND status = ?
            ''', (TaskStatus.CLAIMED.value, conversation_id, task_id, TaskStatus.PENDING.value))
            
            if result.rowcount == 0:
                # Someone else claimed it
                return None
            
            conn.commit()
            
            # Create task object
            task = ConversationTask(
                task_id=row[0],
                conversation_id=row[1],
                priority=row[2],
                status=TaskStatus(row[3]),
                task_type=TaskType(row[4]),
                title=row[5],
                description=row[6],
                assigned_to=row[7],
                claimed_at=datetime.fromisoformat(row[8]) if row[8] else None,
                created_at=datetime.fromisoformat(row[9]) if row[9] else None,
                updated_at=datetime.fromisoformat(row[10]) if row[10] else None,
                depends_on=row[11],
                metadata=json.loads(row[12]) if row[12] else {},
                estimated_minutes=row[13]
            )
            
            # Notify other conversations
            self._broadcast_message(
                from_conversation=conversation_id,
                message_type=MessageType.STATUS_UPDATE,
                content={
                    "event": "task_claimed",
                    "task_id": task_id,
                    "title": task.title,
                    "claimed_by": conversation_id
                }
            )
            
            return task
            
        except Exception as e:
            print(f"Error claiming task: {e}")
            return None
    
    def update_task_status(self, task_id: str, status: TaskStatus, 
                          conversation_id: str, message: str = None) -> bool:
        """Update task status and notify other conversations"""
        
        conn = self._get_db()
        try:
            result = conn.execute('''
                UPDATE conversation_tasks 
                SET status = ?, updated_at = CURRENT_TIMESTAMP
                WHERE task_id = ? AND assigned_to = ?
            ''', (status.value, task_id, conversation_id))
            
            if result.rowcount == 0:
                return False
            
            conn.commit()
            
            # Get task details for notification
            cursor = conn.execute(
                'SELECT title, task_type FROM conversation_tasks WHERE task_id = ?',
                (task_id,)
            )
            row = cursor.fetchone()
            
            if row:
                # Broadcast status update
                self._broadcast_message(
                    from_conversation=conversation_id,
                    message_type=MessageType.STATUS_UPDATE,
                    content={
                        "event": "task_status_updated",
                        "task_id": task_id,
                        "title": row[0],
                        "task_type": row[1],
                        "new_status": status.value,
                        "message": message,
                        "updated_by": conversation_id
                    }
                )
            
            return True
            
        except Exception as e:
            print(f"Error updating task status: {e}")
            return False
    
    def delegate_task(self, from_conversation: str, to_conversation: str,
                     title: str, description: str, task_type: TaskType,
                     priority: int = 3) -> str:
        """Delegate a task to a specific conversation"""
        
        task_id = self.create_task(
            conversation_id=from_conversation,
            title=title,
            description=description,
            task_type=task_type,
            priority=priority,
            metadata={"delegated_to": to_conversation}
        )
        
        if task_id:
            # Send delegation message
            self.send_message(
                from_conversation=from_conversation,
                to_conversation=to_conversation,
                message_type=MessageType.DELEGATION,
                content={
                    "task_id": task_id,
                    "title": title,
                    "description": description,
                    "task_type": task_type.value,
                    "priority": priority,
                    "message": f"Task delegated from {from_conversation}"
                }
            )
        
        return task_id
    
    def send_message(self, from_conversation: str, to_conversation: str,
                    message_type: MessageType, content: Dict[str, Any]) -> str:
        """Send a message between conversations"""
        
        message_id = str(uuid.uuid4())
        
        conn = self._get_db()
        try:
            conn.execute('''
                INSERT INTO conversation_messages
                (message_id, from_conversation, to_conversation, message_type, content)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                message_id, from_conversation, to_conversation,
                message_type.value, json.dumps(content)
            ))
            
            conn.commit()
            return message_id
            
        except Exception as e:
            print(f"Error sending message: {e}")
            return None
    
    def get_messages(self, conversation_id: str, unread_only: bool = True) -> List[ConversationMessage]:
        """Get messages for a conversation"""
        
        conn = self._get_db()
        
        where_clause = "WHERE (to_conversation = ? OR to_conversation = 'broadcast')"
        params = [conversation_id]
        
        if unread_only:
            where_clause += " AND NOT JSON_EXTRACT(read_by, '$') LIKE ?"
            params.append(f'%"{conversation_id}"%')
        
        try:
            cursor = conn.execute(f'''
                SELECT message_id, from_conversation, to_conversation, message_type,
                       content, read_by, created_at
                FROM conversation_messages
                {where_clause}
                ORDER BY created_at DESC
                LIMIT 50
            ''', params)
            
            messages = []
            for row in cursor.fetchall():
                message = ConversationMessage(
                    message_id=row[0],
                    from_conversation=row[1],
                    to_conversation=row[2],
                    message_type=MessageType(row[3]),
                    content=json.loads(row[4]),
                    read_by=json.loads(row[5]),
                    created_at=datetime.fromisoformat(row[6])
                )
                messages.append(message)
            
            return messages
            
        except Exception as e:
            print(f"Error getting messages: {e}")
            return []
    
    def mark_message_read(self, message_id: str, conversation_id: str) -> bool:
        """Mark a message as read by a conversation"""
        
        conn = self._get_db()
        try:
            # Get current read_by list
            cursor = conn.execute(
                'SELECT read_by FROM conversation_messages WHERE message_id = ?',
                (message_id,)
            )
            row = cursor.fetchone()
            if not row:
                return False
            
            read_by = json.loads(row[0])
            if conversation_id not in read_by:
                read_by.append(conversation_id)
                
                conn.execute('''
                    UPDATE conversation_messages 
                    SET read_by = ? 
                    WHERE message_id = ?
                ''', (json.dumps(read_by), message_id))
                
                conn.commit()
            
            return True
            
        except Exception as e:
            print(f"Error marking message read: {e}")
            return False
    
    def get_active_tasks(self, conversation_id: str = None) -> List[ConversationTask]:
        """Get all active tasks, optionally filtered by conversation"""
        
        conn = self._get_db()
        
        where_clause = "WHERE status NOT IN ('completed', 'failed')"
        params = []
        
        if conversation_id:
            where_clause += " AND (assigned_to = ? OR conversation_id = ?)"
            params.extend([conversation_id, conversation_id])
        
        try:
            cursor = conn.execute(f'''
                SELECT task_id, conversation_id, priority, status, task_type, title,
                       description, assigned_to, claimed_at, created_at, updated_at,
                       depends_on, metadata, estimated_minutes
                FROM conversation_tasks
                {where_clause}
                ORDER BY priority ASC, created_at ASC
            ''', params)
            
            tasks = []
            for row in cursor.fetchall():
                task = ConversationTask(
                    task_id=row[0],
                    conversation_id=row[1],
                    priority=row[2],
                    status=TaskStatus(row[3]),
                    task_type=TaskType(row[4]),
                    title=row[5],
                    description=row[6],
                    assigned_to=row[7],
                    claimed_at=datetime.fromisoformat(row[8]) if row[8] else None,
                    created_at=datetime.fromisoformat(row[9]) if row[9] else None,
                    updated_at=datetime.fromisoformat(row[10]) if row[10] else None,
                    depends_on=row[11],
                    metadata=json.loads(row[12]) if row[12] else {},
                    estimated_minutes=row[13]
                )
                tasks.append(task)
            
            return tasks
            
        except Exception as e:
            print(f"Error getting active tasks: {e}")
            return []
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get overall system status for dashboard"""
        
        conn = self._get_db()
        
        try:
            # Task statistics
            cursor = conn.execute('''
                SELECT status, COUNT(*) as count
                FROM conversation_tasks
                GROUP BY status
            ''')
            task_counts = dict(cursor.fetchall())
            
            # Active conversations
            cursor = conn.execute('''
                SELECT conversation_id, capabilities, last_seen
                FROM conversation_registry
                WHERE status = 'active'
                AND last_seen > datetime('now', '-5 minutes')
            ''')
            active_conversations = []
            for row in cursor.fetchall():
                active_conversations.append({
                    "conversation_id": row[0],
                    "capabilities": json.loads(row[1]),
                    "last_seen": row[2]
                })
            
            # Recent messages
            cursor = conn.execute('''
                SELECT COUNT(*) as count
                FROM conversation_messages
                WHERE created_at > datetime('now', '-1 hour')
            ''')
            recent_messages = cursor.fetchone()[0]
            
            return {
                "timestamp": datetime.now().isoformat(),
                "active_conversations": len(active_conversations),
                "conversations": active_conversations,
                "task_counts": task_counts,
                "recent_messages": recent_messages,
                "total_tasks": sum(task_counts.values()),
                "system_health": "operational"
            }
            
        except Exception as e:
            print(f"Error getting system status: {e}")
            return {"error": str(e)}
    
    def _broadcast_message(self, from_conversation: str, message_type: MessageType,
                          content: Dict[str, Any]):
        """Send a broadcast message to all conversations"""
        self.send_message(
            from_conversation=from_conversation,
            to_conversation="broadcast",
            message_type=message_type,
            content=content
        )
    
    def _start_cleanup_thread(self):
        """Start background thread for cleaning up old data"""
        def cleanup_loop():
            while True:
                try:
                    conn = self._get_db()
                    
                    # Clean up old messages (older than 7 days)
                    conn.execute('''
                        DELETE FROM conversation_messages
                        WHERE created_at < datetime('now', '-7 days')
                    ''')
                    
                    # Clean up completed tasks (older than 3 days)
                    conn.execute('''
                        DELETE FROM conversation_tasks
                        WHERE status = 'completed' 
                        AND updated_at < datetime('now', '-3 days')
                    ''')
                    
                    # Mark inactive conversations
                    conn.execute('''
                        UPDATE conversation_registry
                        SET status = 'inactive'
                        WHERE last_seen < datetime('now', '-10 minutes')
                    ''')
                    
                    conn.commit()
                    
                except Exception as e:
                    print(f"Cleanup error: {e}")
                
                time.sleep(300)  # 5 minutes
        
        cleanup_thread = threading.Thread(target=cleanup_loop, daemon=True)
        cleanup_thread.start()

# Global orchestrator instance
_orchestrator = None

def get_orchestrator() -> ConversationOrchestrator:
    """Get the global orchestrator instance"""
    global _orchestrator
    if _orchestrator is None:
        _orchestrator = ConversationOrchestrator()
    return _orchestrator