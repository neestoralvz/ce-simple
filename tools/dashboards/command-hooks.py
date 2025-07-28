#!/usr/bin/env python3
"""
Command Execution Hooks for CE-Simple Efficiency Dashboard Integration
Provides non-intrusive monitoring of command execution performance
"""

import time
import json
import requests
import threading
from datetime import datetime
from functools import wraps
from typing import Dict, Any, Optional, List
import logging
import os
import uuid

# Configuration
DASHBOARD_API_URL = "http://localhost:8080/api/command"
HOOK_ENABLED = os.getenv("CE_DASHBOARD_ENABLED", "true").lower() == "true"
LOG_LEVEL = os.getenv("CE_LOG_LEVEL", "INFO")

# Set up logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('ce-hooks')

class CommandMetricsCollector:
    """Collects and manages command execution metrics"""
    
    def __init__(self):
        self.session_id = str(uuid.uuid4())
        self.command_stack = []
        self.context_cache = {}
        self.lock = threading.Lock()
        
    def start_command(self, command_name: str, context_data: Dict[str, Any] = None) -> str:
        """Start tracking a command execution"""
        execution_id = str(uuid.uuid4())
        
        with self.lock:
            execution_record = {
                "execution_id": execution_id,
                "command": command_name,
                "start_time": time.time(),
                "session_id": self.session_id,
                "context_loaded": len(context_data) if context_data else 0,
                "parent_command": self.command_stack[-1] if self.command_stack else None,
                "subagents_deployed": [],
                "user_corrections": 0,
                "token_usage": 0
            }
            
            self.command_stack.append(execution_record)
            
        logger.debug(f"Started tracking command: {command_name} [{execution_id}]")
        return execution_id
    
    def add_subagent(self, execution_id: str, subagent_type: str):
        """Record subagent deployment"""
        with self.lock:
            for record in self.command_stack:
                if record["execution_id"] == execution_id:
                    record["subagents_deployed"].append(subagent_type)
                    break
    
    def add_user_correction(self, execution_id: str):
        """Record user correction/clarification"""
        with self.lock:
            for record in self.command_stack:
                if record["execution_id"] == execution_id:
                    record["user_corrections"] += 1
                    break
    
    def add_token_usage(self, execution_id: str, tokens: int):
        """Record token usage"""
        with self.lock:
            for record in self.command_stack:
                if record["execution_id"] == execution_id:
                    record["token_usage"] += tokens
                    break
    
    def end_command(self, execution_id: str, success: bool = True, error: str = None) -> Dict[str, Any]:
        """End tracking and return metrics"""
        end_time = time.time()
        
        with self.lock:
            # Find and remove the command record
            execution_record = None
            for i, record in enumerate(self.command_stack):
                if record["execution_id"] == execution_id:
                    execution_record = self.command_stack.pop(i)
                    break
            
            if not execution_record:
                logger.warning(f"Command execution not found: {execution_id}")
                return {}
            
            # Calculate metrics
            execution_time_ms = (end_time - execution_record["start_time"]) * 1000
            
            metrics = {
                "execution_id": execution_id,
                "command": execution_record["command"],
                "execution_time_ms": round(execution_time_ms, 2),
                "success": success,
                "error": error,
                "session_id": execution_record["session_id"],
                "context_loaded": execution_record["context_loaded"],
                "subagents_deployed": execution_record["subagents_deployed"],
                "user_corrections": execution_record["user_corrections"],
                "token_usage": execution_record["token_usage"],
                "timestamp": datetime.now().isoformat(),
                "parent_command": execution_record["parent_command"]["command"] if execution_record["parent_command"] else None
            }
            
            # Send to dashboard asynchronously
            self._send_metrics_async(metrics)
            
            return metrics
    
    def _send_metrics_async(self, metrics: Dict[str, Any]):
        """Send metrics to dashboard API asynchronously"""
        if not HOOK_ENABLED:
            return
        
        def send_metrics():
            try:
                response = requests.post(
                    DASHBOARD_API_URL,
                    json=metrics,
                    timeout=2  # Short timeout to avoid blocking command execution
                )
                if response.status_code == 200:
                    logger.debug(f"Metrics sent successfully for command: {metrics['command']}")
                else:
                    logger.warning(f"Failed to send metrics: {response.status_code}")
            except requests.exceptions.RequestException as e:
                logger.debug(f"Dashboard API unavailable: {e}")
        
        # Send in background thread
        thread = threading.Thread(target=send_metrics, daemon=True)
        thread.start()

# Global metrics collector instance
metrics_collector = CommandMetricsCollector()

def track_command_performance(command_name: str = None, track_subagents: bool = True):
    """
    Decorator to track command execution performance
    
    Usage:
        @track_command_performance()
        def my_command():
            # Command implementation
            pass
        
        @track_command_performance("custom-name", track_subagents=False)
        def another_command():
            # Command implementation
            pass
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal command_name
            if command_name is None:
                command_name = func.__name__
            
            # Start tracking
            execution_id = metrics_collector.start_command(
                command_name,
                context_data=kwargs.get('context', {})
            )
            
            success = True
            error = None
            result = None
            
            try:
                # Execute the command
                result = func(*args, **kwargs)
                
                # If result contains subagent information, track it
                if track_subagents and isinstance(result, dict):
                    subagents = result.get('subagents_used', [])
                    for subagent in subagents:
                        metrics_collector.add_subagent(execution_id, subagent)
                
                return result
                
            except Exception as e:
                success = False
                error = str(e)
                logger.error(f"Command {command_name} failed: {error}")
                raise
                
            finally:
                # End tracking
                metrics = metrics_collector.end_command(execution_id, success, error)
                logger.info(f"Command executed: {command_name} - {metrics.get('execution_time_ms', 0):.0f}ms - {'SUCCESS' if success else 'FAILED'}")
        
        return wrapper
    return decorator

def track_subagent_deployment(subagent_type: str):
    """Record subagent deployment for current command"""
    if metrics_collector.command_stack:
        current_execution = metrics_collector.command_stack[-1]["execution_id"]
        metrics_collector.add_subagent(current_execution, subagent_type)

def track_user_correction():
    """Record user correction for current command"""
    if metrics_collector.command_stack:
        current_execution = metrics_collector.command_stack[-1]["execution_id"]
        metrics_collector.add_user_correction(current_execution)

def track_token_usage(tokens: int):
    """Record token usage for current command"""
    if metrics_collector.command_stack:
        current_execution = metrics_collector.command_stack[-1]["execution_id"]
        metrics_collector.add_token_usage(current_execution, tokens)

class CommandContext:
    """Context manager for command execution tracking"""
    
    def __init__(self, command_name: str, context_data: Dict[str, Any] = None):
        self.command_name = command_name
        self.context_data = context_data or {}
        self.execution_id = None
    
    def __enter__(self):
        self.execution_id = metrics_collector.start_command(
            self.command_name,
            self.context_data
        )
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        success = exc_type is None
        error = str(exc_val) if exc_val else None
        metrics_collector.end_command(self.execution_id, success, error)
    
    def add_subagent(self, subagent_type: str):
        """Add subagent to current execution"""
        if self.execution_id:
            metrics_collector.add_subagent(self.execution_id, subagent_type)
    
    def add_correction(self):
        """Add user correction to current execution"""
        if self.execution_id:
            metrics_collector.add_user_correction(self.execution_id)
    
    def add_tokens(self, tokens: int):
        """Add token usage to current execution"""
        if self.execution_id:
            metrics_collector.add_token_usage(self.execution_id, tokens)

# Integration helpers for existing commands
def integrate_with_existing_commands():
    """
    Integration patterns for existing CE-Simple commands
    This would be imported and used in command files
    """
    
    # Example integration for /start command
    @track_command_performance("start")
    def enhanced_start_command():
        """Enhanced start command with metrics tracking"""
        with CommandContext("start") as ctx:
            # Git status check
            ctx.add_subagent("git-analyzer")
            
            # Load handoff context
            ctx.add_subagent("context-loader")
            
            # Extract insights
            ctx.add_subagent("insight-extractor")
            
            # Simulate command execution
            time.sleep(1.2)  # Simulated work
            
            return {
                "status": "success",
                "subagents_used": ["git-analyzer", "context-loader", "insight-extractor"],
                "insights_extracted": 5,
                "handoff_loaded": True
            }
    
    # Example integration for /create-doc command
    @track_command_performance("create-doc")
    def enhanced_create_doc_command(doc_type: str, description: str):
        """Enhanced create-doc command with metrics tracking"""
        track_subagent_deployment("content-specialist")
        
        # Simulate some processing time
        time.sleep(0.8)
        
        if "error" in description.lower():
            # Simulate user correction needed
            track_user_correction()
            raise ValueError("Document description needs clarification")
        
        track_token_usage(450)  # Estimated token usage
        
        return {
            "status": "success",
            "document_created": f"{doc_type}_document.md",
            "tokens_used": 450
        }
    
    return {
        "start": enhanced_start_command,
        "create_doc": enhanced_create_doc_command
    }

# Command execution monitoring for existing system
class CECommandMonitor:
    """Monitor for CE-Simple command ecosystem"""
    
    def __init__(self):
        self.active_sessions = {}
        self.command_registry = {}
    
    def register_command(self, command_name: str, command_func):
        """Register a command for monitoring"""
        wrapped_command = track_command_performance(command_name)(command_func)
        self.command_registry[command_name] = wrapped_command
        return wrapped_command
    
    def execute_command(self, command_name: str, *args, **kwargs):
        """Execute a registered command with monitoring"""
        if command_name not in self.command_registry:
            raise ValueError(f"Command not registered: {command_name}")
        
        return self.command_registry[command_name](*args, **kwargs)
    
    def get_session_metrics(self, session_id: str = None) -> Dict[str, Any]:
        """Get metrics for a specific session"""
        target_session = session_id or metrics_collector.session_id
        
        # This would be implemented to aggregate session-specific metrics
        return {
            "session_id": target_session,
            "status": "active",
            "commands_executed": len(metrics_collector.command_stack),
            "current_command": metrics_collector.command_stack[-1]["command"] if metrics_collector.command_stack else None
        }

# Export main components
__all__ = [
    'track_command_performance',
    'track_subagent_deployment', 
    'track_user_correction',
    'track_token_usage',
    'CommandContext',
    'CECommandMonitor',
    'metrics_collector'
]

if __name__ == "__main__":
    # Demo usage
    print("CE-Simple Command Hooks Demo")
    
    # Test the decorator
    @track_command_performance("demo-command")
    def demo_command():
        track_subagent_deployment("research-specialist")
        track_subagent_deployment("content-optimizer")
        time.sleep(0.5)  # Simulate work
        track_token_usage(250)
        return {"status": "success", "result": "demo completed"}
    
    # Test context manager
    def demo_context_command():
        with CommandContext("demo-context") as ctx:
            ctx.add_subagent("architecture-validator")
            time.sleep(0.3)
            ctx.add_tokens(180)
            return {"status": "context demo completed"}
    
    # Run demos
    print("Running decorator demo...")
    result1 = demo_command()
    print(f"Result: {result1}")
    
    print("Running context manager demo...")
    result2 = demo_context_command()
    print(f"Result: {result2}")
    
    print("Demo completed. Check dashboard for metrics.")