#!/usr/bin/env python3

"""
Performance Metrics Collection System
Purpose: Automated collection of Task Tool and parallel execution metrics  
Authority: implements user-input/technical-requirements/technical-architecture-user.md Performance Architecture
Status: Core automation system for quantitative validation
"""

import json
import time
import os
import sys
import subprocess
import psutil
import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
import logging

# ============================================================================
# CONFIGURATION
# ============================================================================

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
METRICS_DIR = PROJECT_ROOT / "data" / "performance-metrics"
LOG_FILE = METRICS_DIR / "performance.log"

# Ensure metrics directory exists
METRICS_DIR.mkdir(parents=True, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class TaskToolMetrics:
    """Metrics for individual Task Tool agent execution"""
    agent_id: str
    start_time: float
    end_time: float
    duration: float
    memory_usage_mb: float
    cpu_percent: float
    tools_used: List[str]
    files_accessed: List[str]
    success: bool
    error_message: Optional[str] = None

@dataclass
class ParallelExecutionMetrics:
    """Metrics for parallel execution session"""
    session_id: str
    start_time: float
    end_time: float
    total_duration: float
    agent_count: int
    parallel_efficiency: float
    speedup_factor: float
    sequential_estimate: float
    success_rate: float
    agents: List[TaskToolMetrics]

@dataclass
class SystemPerformanceMetrics:
    """Overall system performance metrics"""
    timestamp: str
    cpu_usage: float
    memory_usage_mb: float
    disk_usage_mb: float
    load_average: List[float]
    git_operations_count: int
    file_operations_count: int

# ============================================================================
# TASK TOOL MONITORING
# ============================================================================

class TaskToolMonitor:
    """Monitor Task Tool agent performance and metrics"""
    
    def __init__(self):
        self.active_sessions: Dict[str, Dict] = {}
        self.completed_sessions: List[ParallelExecutionMetrics] = []
        self.state_file = METRICS_DIR / "active_sessions.json"
        self._load_state()
    
    def _save_state(self) -> None:
        """Save active sessions state to file"""
        # Convert dataclass objects to dicts for JSON serialization
        serializable_sessions = {}
        for session_id, session_data in self.active_sessions.items():
            serializable_session = session_data.copy()
            if 'system_snapshot' in serializable_session:
                serializable_session['system_snapshot'] = asdict(serializable_session['system_snapshot'])
            serializable_sessions[session_id] = serializable_session
        
        state = {
            'active_sessions': serializable_sessions,
            'last_updated': datetime.datetime.now().isoformat()
        }
        with open(self.state_file, 'w') as f:
            json.dump(state, f, indent=2)
    
    def _load_state(self) -> None:
        """Load active sessions state from file"""
        if self.state_file.exists():
            try:
                with open(self.state_file, 'r') as f:
                    state = json.load(f)
                self.active_sessions = state.get('active_sessions', {})
                logger.info(f"Loaded {len(self.active_sessions)} active sessions from state file")
            except Exception as e:
                logger.warning(f"Could not load state file: {e}")
                self.active_sessions = {}
    
    def start_session(self, session_id: str, estimated_agents: int) -> None:
        """Start monitoring a new parallel execution session"""
        logger.info(f"Starting performance monitoring for session: {session_id}")
        
        self.active_sessions[session_id] = {
            'start_time': time.time(),
            'estimated_agents': estimated_agents,
            'agents': {},
            'system_snapshot': self._get_system_snapshot()
        }
        self._save_state()
    
    def start_agent(self, session_id: str, agent_id: str, tools_context: List[str] = None) -> None:
        """Start monitoring individual agent"""
        if session_id not in self.active_sessions:
            logger.warning(f"Session {session_id} not found, creating new session")
            self.start_session(session_id, 1)
        
        session = self.active_sessions[session_id]
        session['agents'][agent_id] = {
            'start_time': time.time(),
            'tools_context': tools_context or [],
            'tools_used': [],
            'files_accessed': [],
            'memory_start': self._get_memory_usage()
        }
        
        logger.info(f"Agent {agent_id} started in session {session_id}")
    
    def log_tool_usage(self, session_id: str, agent_id: str, tool_name: str, 
                       files_accessed: List[str] = None) -> None:
        """Log tool usage for an agent"""
        try:
            session = self.active_sessions[session_id]
            agent = session['agents'][agent_id]
            
            agent['tools_used'].append({
                'tool': tool_name,
                'timestamp': time.time(),
                'files': files_accessed or []
            })
            
            if files_accessed:
                agent['files_accessed'].extend(files_accessed)
            
        except KeyError:
            logger.warning(f"Could not log tool usage: session {session_id} or agent {agent_id} not found")
    
    def end_agent(self, session_id: str, agent_id: str, success: bool = True, 
                  error_message: str = None) -> TaskToolMetrics:
        """End monitoring for individual agent and return metrics"""
        try:
            session = self.active_sessions[session_id]
            agent_data = session['agents'][agent_id]
            
            end_time = time.time()
            duration = end_time - agent_data['start_time']
            memory_end = self._get_memory_usage()
            memory_usage = memory_end - agent_data['memory_start']
            
            # Extract tools used
            tools_used = [entry['tool'] for entry in agent_data['tools_used']]
            
            # Create metrics object
            metrics = TaskToolMetrics(
                agent_id=agent_id,
                start_time=agent_data['start_time'],
                end_time=end_time,
                duration=duration,
                memory_usage_mb=memory_usage,
                cpu_percent=psutil.cpu_percent(),
                tools_used=tools_used,
                files_accessed=list(set(agent_data['files_accessed'])),
                success=success,
                error_message=error_message
            )
            
            logger.info(f"Agent {agent_id} completed in {duration:.2f}s")
            return metrics
            
        except KeyError:
            logger.error(f"Could not end agent: session {session_id} or agent {agent_id} not found")
            return None
    
    def end_session(self, session_id: str) -> ParallelExecutionMetrics:
        """End monitoring session and calculate parallel execution metrics"""
        try:
            session = self.active_sessions[session_id]
            end_time = time.time()
            total_duration = end_time - session['start_time']
            
            # Calculate agent metrics
            agent_metrics = []
            for agent_id in session['agents']:
                metrics = self.end_agent(session_id, agent_id)
                if metrics:
                    agent_metrics.append(metrics)
            
            # Calculate parallel efficiency
            if agent_metrics:
                total_agent_time = sum(agent.duration for agent in agent_metrics)
                parallel_efficiency = (total_agent_time / total_duration / len(agent_metrics)) * 100
                speedup_factor = total_agent_time / total_duration
                success_rate = sum(1 for agent in agent_metrics if agent.success) / len(agent_metrics) * 100
            else:
                total_agent_time = total_duration
                parallel_efficiency = 0
                speedup_factor = 1
                success_rate = 0
            
            # Create session metrics
            session_metrics = ParallelExecutionMetrics(
                session_id=session_id,
                start_time=session['start_time'],
                end_time=end_time,
                total_duration=total_duration,
                agent_count=len(agent_metrics),
                parallel_efficiency=parallel_efficiency,
                speedup_factor=speedup_factor,
                sequential_estimate=total_agent_time,
                success_rate=success_rate,
                agents=agent_metrics
            )
            
            self.completed_sessions.append(session_metrics)
            del self.active_sessions[session_id]
            self._save_state()
            
            logger.info(f"Session {session_id} completed: {speedup_factor:.2f}x speedup, {parallel_efficiency:.1f}% efficiency")
            return session_metrics
            
        except KeyError:
            logger.error(f"Could not end session: {session_id} not found")
            return None
    
    def _get_system_snapshot(self) -> SystemPerformanceMetrics:
        """Get current system performance snapshot"""
        return SystemPerformanceMetrics(
            timestamp=datetime.datetime.now().isoformat(),
            cpu_usage=psutil.cpu_percent(),
            memory_usage_mb=psutil.virtual_memory().used / 1024 / 1024,
            disk_usage_mb=psutil.disk_usage('/').used / 1024 / 1024,
            load_average=list(os.getloadavg()) if hasattr(os, 'getloadavg') else [0, 0, 0],
            git_operations_count=0,  # Will be calculated separately
            file_operations_count=0  # Will be calculated separately
        )
    
    def _get_memory_usage(self) -> float:
        """Get current memory usage in MB"""
        return psutil.virtual_memory().used / 1024 / 1024

# ============================================================================
# METRICS COLLECTION AND STORAGE
# ============================================================================

class MetricsCollector:
    """Collect and store performance metrics"""
    
    def __init__(self):
        self.monitor = TaskToolMonitor()
    
    def save_session_metrics(self, session_metrics: ParallelExecutionMetrics) -> None:
        """Save session metrics to file"""
        output_file = METRICS_DIR / f"session_{session_metrics.session_id}_{int(session_metrics.start_time)}.json"
        
        metrics_dict = asdict(session_metrics)
        
        with open(output_file, 'w') as f:
            json.dump(metrics_dict, f, indent=2)
        
        logger.info(f"Session metrics saved to {output_file}")
    
    def save_aggregated_metrics(self) -> None:
        """Save aggregated performance metrics"""
        if not self.monitor.completed_sessions:
            logger.warning("No completed sessions to aggregate")
            return
        
        # Calculate aggregated metrics
        sessions = self.monitor.completed_sessions
        total_sessions = len(sessions)
        
        avg_speedup = sum(s.speedup_factor for s in sessions) / total_sessions
        avg_efficiency = sum(s.parallel_efficiency for s in sessions) / total_sessions
        avg_success_rate = sum(s.success_rate for s in sessions) / total_sessions
        avg_duration = sum(s.total_duration for s in sessions) / total_sessions
        
        # Calculate tool usage statistics
        all_tools = []
        for session in sessions:
            for agent in session.agents:
                all_tools.extend(agent.tools_used)
        
        tool_counts = {}
        for tool in all_tools:
            tool_counts[tool] = tool_counts.get(tool, 0) + 1
        
        aggregated = {
            'metadata': {
                'generated_at': datetime.datetime.now().isoformat(),
                'total_sessions': total_sessions,
                'analysis_period': '30_days'
            },
            'performance_summary': {
                'average_speedup_factor': round(avg_speedup, 2),
                'average_parallel_efficiency': round(avg_efficiency, 1),
                'average_success_rate': round(avg_success_rate, 1),
                'average_session_duration': round(avg_duration, 2),
                'total_agent_executions': sum(s.agent_count for s in sessions)
            },
            'tool_usage_statistics': tool_counts,
            'validation_claims': {
                'speedup_claim_2_5x': avg_speedup >= 2.5,
                'efficiency_threshold_80pct': avg_efficiency >= 80,
                'success_rate_threshold_95pct': avg_success_rate >= 95
            }
        }
        
        output_file = METRICS_DIR / "aggregated_performance.json"
        with open(output_file, 'w') as f:
            json.dump(aggregated, f, indent=2)
        
        logger.info(f"Aggregated metrics saved to {output_file}")
        logger.info(f"Performance validation: {avg_speedup:.2f}x speedup, {avg_efficiency:.1f}% efficiency")
    
    def generate_realtime_dashboard_data(self) -> Dict[str, Any]:
        """Generate real-time dashboard data"""
        current_sessions = len(self.monitor.active_sessions)
        completed_sessions = len(self.monitor.completed_sessions)
        
        if self.monitor.completed_sessions:
            recent_session = self.monitor.completed_sessions[-1]
            last_speedup = recent_session.speedup_factor
            last_efficiency = recent_session.parallel_efficiency
        else:
            last_speedup = 0
            last_efficiency = 0
        
        dashboard_data = {
            'timestamp': datetime.datetime.now().isoformat(),
            'status': {
                'active_sessions': current_sessions,
                'completed_sessions': completed_sessions,
                'system_health': 'healthy' if psutil.cpu_percent() < 80 else 'degraded'
            },
            'recent_performance': {
                'last_speedup_factor': round(last_speedup, 2),
                'last_efficiency': round(last_efficiency, 1),
                'cpu_usage': round(psutil.cpu_percent(), 1),
                'memory_usage_mb': round(psutil.virtual_memory().used / 1024 / 1024, 1)
            }
        }
        
        # Save dashboard data
        dashboard_file = METRICS_DIR / "realtime_dashboard.json"
        with open(dashboard_file, 'w') as f:
            json.dump(dashboard_data, f, indent=2)
        
        return dashboard_data

# ============================================================================
# CLI INTERFACE
# ============================================================================

def main():
    """Main CLI interface for performance collection"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Performance Metrics Collection System')
    parser.add_argument('command', choices=['start-session', 'end-session', 'aggregate', 'dashboard'])
    parser.add_argument('--session-id', help='Session ID for start/end operations')
    parser.add_argument('--agents', type=int, default=1, help='Estimated number of agents')
    
    args = parser.parse_args()
    
    collector = MetricsCollector()
    
    if args.command == 'start-session':
        if not args.session_id:
            logger.error("--session-id required for start-session")
            sys.exit(1)
        collector.monitor.start_session(args.session_id, args.agents)
        
    elif args.command == 'end-session':
        if not args.session_id:
            logger.error("--session-id required for end-session")
            sys.exit(1)
        metrics = collector.monitor.end_session(args.session_id)
        if metrics:
            collector.save_session_metrics(metrics)
            
    elif args.command == 'aggregate':
        collector.save_aggregated_metrics()
        
    elif args.command == 'dashboard':
        dashboard_data = collector.generate_realtime_dashboard_data()
        print(json.dumps(dashboard_data, indent=2))

if __name__ == '__main__':
    main()