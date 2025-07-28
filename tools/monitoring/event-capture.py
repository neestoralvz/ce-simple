#!/usr/bin/env python3
"""
CE-Simple Real-Time Event Capture System
Captures git events and Claude Code tool usage for real-time monitoring
"""

import json
import sys
import sqlite3
import threading
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any, Optional
import subprocess
import argparse
import logging

class EventCaptureSystem:
    """Real-time event capture and streaming for CE-Simple monitoring"""
    
    def __init__(self, base_path: str = "/Users/nalve/ce-simple"):
        self.base_path = Path(base_path)
        self.monitoring_db = self.base_path / "data/monitoring/health.db"
        self.events_log = self.base_path / "data/monitoring/git-events.log"
        
        # Ensure directories exist
        self.monitoring_db.parent.mkdir(parents=True, exist_ok=True)
        self.events_log.parent.mkdir(parents=True, exist_ok=True)
        
        # Initialize database for real-time events
        self.init_events_database()
        
        # Set up logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
    def init_events_database(self):
        """Initialize events database for real-time capture"""
        conn = sqlite3.connect(self.monitoring_db)
        
        # Git events table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS git_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                event_type TEXT NOT NULL,
                branch TEXT,
                commit_hash TEXT,
                author TEXT,
                files_changed INTEGER DEFAULT 0,
                insertions INTEGER DEFAULT 0,
                deletions INTEGER DEFAULT 0,
                remote TEXT,
                operation_time REAL DEFAULT 0.0,
                metadata TEXT,
                processed BOOLEAN DEFAULT FALSE
            )
        ''')
        
        # Claude Code events table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS claude_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                event_type TEXT NOT NULL,
                tool_name TEXT,
                session_id TEXT,
                execution_time REAL DEFAULT 0.0,
                success BOOLEAN DEFAULT TRUE,
                context_preserved BOOLEAN DEFAULT TRUE,
                user_voice_maintained BOOLEAN DEFAULT TRUE,
                metadata TEXT,
                processed BOOLEAN DEFAULT FALSE
            )
        ''')
        
        # Real-time performance metrics
        conn.execute('''
            CREATE TABLE IF NOT EXISTS performance_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                metric_type TEXT NOT NULL,
                metric_name TEXT NOT NULL,
                metric_value REAL NOT NULL,
                tags TEXT,
                source TEXT DEFAULT 'system'
            )
        ''')
        
        # Create indexes for performance
        conn.execute('CREATE INDEX IF NOT EXISTS idx_git_timestamp ON git_events(timestamp)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_git_type ON git_events(event_type)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_claude_timestamp ON claude_events(timestamp)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_claude_tool ON claude_events(tool_name)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_perf_timestamp ON performance_events(timestamp)')
        
        conn.commit()
        conn.close()
    
    def capture_git_event(self, event_data: Dict[str, Any]) -> str:
        """Capture git event and stream to monitoring systems"""
        try:
            conn = sqlite3.connect(self.monitoring_db)
            
            git_data = event_data.get('git_data', {})
            perf_data = event_data.get('performance_metrics', {})
            
            cursor = conn.execute('''
                INSERT INTO git_events 
                (timestamp, event_type, branch, commit_hash, author, 
                 files_changed, insertions, deletions, remote, operation_time, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                event_data.get('timestamp', datetime.now().isoformat()),
                event_data.get('event_type', 'unknown'),
                git_data.get('branch'),
                git_data.get('commit_hash'),
                git_data.get('author'),
                git_data.get('files_changed', 0),
                git_data.get('insertions', 0),
                git_data.get('deletions', 0),
                git_data.get('remote'),
                perf_data.get('execution_time', 0.0),
                json.dumps(event_data)
            ))
            
            event_id = cursor.lastrowid
            conn.commit()
            conn.close()
            
            # Stream to real-time systems
            self._stream_event_to_systems(event_data)
            
            # Update performance metrics
            self._update_git_performance_metrics(event_data)
            
            self.logger.info(f"Captured git event: {event_data.get('event_type')} -> ID {event_id}")
            return str(event_id)
            
        except Exception as e:
            self.logger.error(f"Error capturing git event: {e}")
            return "error"
    
    def capture_claude_event(self, event_data: Dict[str, Any]) -> str:
        """Capture Claude Code tool usage event"""
        try:
            conn = sqlite3.connect(self.monitoring_db)
            
            cursor = conn.execute('''
                INSERT INTO claude_events 
                (timestamp, event_type, tool_name, session_id, execution_time,
                 success, context_preserved, user_voice_maintained, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                event_data.get('timestamp', datetime.now().isoformat()),
                event_data.get('event_type', 'tool_usage'),
                event_data.get('tool_name'),
                event_data.get('session_id'),
                event_data.get('execution_time', 0.0),
                event_data.get('success', True),
                event_data.get('context_preserved', True),
                event_data.get('user_voice_maintained', True),
                json.dumps(event_data)
            ))
            
            event_id = cursor.lastrowid
            conn.commit()
            conn.close()
            
            # Stream to real-time systems
            self._stream_event_to_systems(event_data)
            
            # Update performance metrics
            self._update_claude_performance_metrics(event_data)
            
            self.logger.info(f"Captured Claude event: {event_data.get('tool_name')} -> ID {event_id}")
            return str(event_id)
            
        except Exception as e:
            self.logger.error(f"Error capturing Claude event: {e}")
            return "error"
    
    def _stream_event_to_systems(self, event_data: Dict[str, Any]):
        """Stream event to various monitoring systems"""
        # Update health daemon status
        self._update_health_daemon_metrics(event_data)
        
        # Send to dashboard if running
        self._send_to_dashboard(event_data)
        
        # Log to structured file
        self._log_structured_event(event_data)
    
    def _update_health_daemon_metrics(self, event_data: Dict[str, Any]):
        """Update health daemon with real-time metrics"""
        try:
            # Calculate dynamic performance score based on git activity
            if event_data.get('event_type', '').startswith('git_'):
                git_score = self._calculate_git_activity_score()
                
                # Update performance metrics table
                conn = sqlite3.connect(self.monitoring_db)
                conn.execute('''
                    INSERT INTO performance_events 
                    (timestamp, metric_type, metric_name, metric_value, source)
                    VALUES (?, ?, ?, ?, ?)
                ''', (
                    datetime.now().isoformat(),
                    'git_activity',
                    'activity_score',
                    git_score,
                    'git_hooks'
                ))
                conn.commit()
                conn.close()
                
        except Exception as e:
            self.logger.error(f"Error updating health daemon metrics: {e}")
    
    def _calculate_git_activity_score(self) -> float:
        """Calculate git activity score based on recent events"""
        try:
            conn = sqlite3.connect(self.monitoring_db)
            
            # Count recent git events (last 15 minutes)
            cutoff = (datetime.now() - timedelta(minutes=15)).isoformat()
            cursor = conn.execute('''
                SELECT COUNT(*), AVG(files_changed), AVG(operation_time)
                FROM git_events 
                WHERE timestamp > ?
            ''', (cutoff,))
            
            result = cursor.fetchone()
            conn.close()
            
            if result and result[0] > 0:
                event_count = result[0]
                avg_files = result[1] or 0
                avg_time = result[2] or 0
                
                # Score formula: activity frequency + file impact - time penalty
                activity_score = min(1.0, (event_count / 10.0))  # 10 events = max activity
                file_score = min(1.0, (avg_files / 20.0))        # 20+ files = high impact
                time_penalty = max(0, min(0.5, avg_time / 10.0)) # >10s = penalty
                
                total_score = (activity_score * 0.5) + (file_score * 0.3) + (0.2 - time_penalty)
                return max(0.0, min(1.0, total_score))
            
            return 0.0
            
        except Exception as e:
            self.logger.error(f"Error calculating git activity score: {e}")
            return 0.0
    
    def _update_git_performance_metrics(self, event_data: Dict[str, Any]):
        """Update git-specific performance metrics"""
        try:
            conn = sqlite3.connect(self.monitoring_db)
            timestamp = datetime.now().isoformat()
            
            # Extract metrics from git event
            git_data = event_data.get('git_data', {})
            event_type = event_data.get('event_type', '')
            
            metrics = [
                ('git_files_changed', git_data.get('files_changed', 0)),
                ('git_insertions', git_data.get('insertions', 0)),
                ('git_deletions', git_data.get('deletions', 0)),
            ]
            
            # Add event-specific metrics
            if event_type == 'git_push':
                metrics.append(('git_commits_pushed', git_data.get('commits_to_push', 0)))
            elif event_type == 'git_checkout':
                metrics.append(('git_commits_pulled', git_data.get('commits_pulled', 0)))
            
            # Insert metrics
            for metric_name, metric_value in metrics:
                if metric_value is not None:
                    conn.execute('''
                        INSERT INTO performance_events 
                        (timestamp, metric_type, metric_name, metric_value, tags, source)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (
                        timestamp, 'git_metrics', metric_name, float(metric_value),
                        json.dumps({'event_type': event_type, 'branch': git_data.get('branch')}),
                        'git_hooks'
                    ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            self.logger.error(f"Error updating git performance metrics: {e}")
    
    def _update_claude_performance_metrics(self, event_data: Dict[str, Any]):
        """Update Claude Code performance metrics"""
        try:
            conn = sqlite3.connect(self.monitoring_db)
            timestamp = datetime.now().isoformat()
            
            metrics = [
                ('claude_execution_time', event_data.get('execution_time', 0.0)),
                ('claude_success_rate', 1.0 if event_data.get('success', True) else 0.0),
                ('claude_context_preservation', 1.0 if event_data.get('context_preserved', True) else 0.0),
                ('claude_voice_maintenance', 1.0 if event_data.get('user_voice_maintained', True) else 0.0),
            ]
            
            for metric_name, metric_value in metrics:
                conn.execute('''
                    INSERT INTO performance_events 
                    (timestamp, metric_type, metric_name, metric_value, tags, source)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    timestamp, 'claude_metrics', metric_name, metric_value,
                    json.dumps({'tool_name': event_data.get('tool_name'), 'session_id': event_data.get('session_id')}),
                    'claude_hooks'
                ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            self.logger.error(f"Error updating Claude performance metrics: {e}")
    
    def _send_to_dashboard(self, event_data: Dict[str, Any]):
        """Send event to real-time dashboard"""
        try:
            import requests
            requests.post(
                "http://localhost:5000/api/real-time-event",
                json=event_data,
                timeout=1
            )
        except:
            # Dashboard not running or unreachable - continue silently
            pass
    
    def _log_structured_event(self, event_data: Dict[str, Any]):
        """Log event to structured log file"""
        try:
            with open(self.events_log, 'a') as f:
                log_entry = {
                    'captured_at': datetime.now().isoformat(),
                    'event': event_data
                }
                f.write(json.dumps(log_entry) + '\n')
        except Exception as e:
            self.logger.error(f"Error writing to events log: {e}")

    def get_recent_events(self, limit: int = 50, event_type: Optional[str] = None) -> list:
        """Get recent events for monitoring dashboard"""
        try:
            conn = sqlite3.connect(self.monitoring_db)
            
            # Build query based on event type
            if event_type == 'git':
                query = '''
                    SELECT timestamp, event_type, branch, commit_hash, author, 
                           files_changed, metadata
                    FROM git_events 
                    ORDER BY timestamp DESC 
                    LIMIT ?
                '''
                cursor = conn.execute(query, (limit,))
                columns = ['timestamp', 'event_type', 'branch', 'commit_hash', 
                          'author', 'files_changed', 'metadata']
            elif event_type == 'claude':
                query = '''
                    SELECT timestamp, event_type, tool_name, session_id, 
                           execution_time, success, metadata
                    FROM claude_events 
                    ORDER BY timestamp DESC 
                    LIMIT ?
                '''
                cursor = conn.execute(query, (limit,))
                columns = ['timestamp', 'event_type', 'tool_name', 'session_id',
                          'execution_time', 'success', 'metadata']
            else:
                # Combined view
                query = '''
                    SELECT 'git' as source, timestamp, event_type, branch, 
                           commit_hash, files_changed, NULL as tool_name, metadata
                    FROM git_events
                    UNION ALL
                    SELECT 'claude' as source, timestamp, event_type, NULL, 
                           NULL, NULL, tool_name, metadata
                    FROM claude_events
                    ORDER BY timestamp DESC 
                    LIMIT ?
                '''
                cursor = conn.execute(query, (limit,))
                columns = ['source', 'timestamp', 'event_type', 'branch',
                          'commit_hash', 'files_changed', 'tool_name', 'metadata']
            
            events = []
            for row in cursor.fetchall():
                event = dict(zip(columns, row))
                # Parse metadata if present
                if event.get('metadata'):
                    try:
                        event['metadata'] = json.loads(event['metadata'])
                    except:
                        pass
                events.append(event)
            
            conn.close()
            return events
            
        except Exception as e:
            self.logger.error(f"Error getting recent events: {e}")
            return []

    def get_performance_summary(self, hours: int = 24) -> Dict[str, Any]:
        """Get performance summary for specified time range"""
        try:
            conn = sqlite3.connect(self.monitoring_db)
            cutoff = (datetime.now() - timedelta(hours=hours)).isoformat()
            
            # Git activity summary
            git_cursor = conn.execute('''
                SELECT 
                    COUNT(*) as total_events,
                    COUNT(DISTINCT event_type) as event_types,
                    AVG(files_changed) as avg_files_changed,
                    SUM(files_changed) as total_files_changed,
                    COUNT(DISTINCT author) as active_authors,
                    COUNT(DISTINCT branch) as active_branches
                FROM git_events 
                WHERE timestamp > ?
            ''', (cutoff,))
            git_stats = git_cursor.fetchone()
            
            # Claude activity summary  
            claude_cursor = conn.execute('''
                SELECT 
                    COUNT(*) as total_events,
                    COUNT(DISTINCT tool_name) as tools_used,
                    AVG(execution_time) as avg_execution_time,
                    AVG(CASE WHEN success THEN 1.0 ELSE 0.0 END) as success_rate,
                    AVG(CASE WHEN context_preserved THEN 1.0 ELSE 0.0 END) as context_rate
                FROM claude_events 
                WHERE timestamp > ?
            ''', (cutoff,))
            claude_stats = claude_cursor.fetchone()
            
            # Performance metrics summary
            perf_cursor = conn.execute('''
                SELECT metric_type, metric_name, AVG(metric_value) as avg_value,
                       MIN(metric_value) as min_value, MAX(metric_value) as max_value
                FROM performance_events 
                WHERE timestamp > ?
                GROUP BY metric_type, metric_name
            ''', (cutoff,))
            
            performance_metrics = {}
            for row in perf_cursor.fetchall():
                metric_type, metric_name, avg_val, min_val, max_val = row
                if metric_type not in performance_metrics:
                    performance_metrics[metric_type] = {}
                performance_metrics[metric_type][metric_name] = {
                    'average': round(avg_val, 3) if avg_val else 0,
                    'min': round(min_val, 3) if min_val else 0,
                    'max': round(max_val, 3) if max_val else 0
                }
            
            conn.close()
            
            return {
                'time_range_hours': hours,
                'generated_at': datetime.now().isoformat(),
                'git_activity': {
                    'total_events': git_stats[0] if git_stats else 0,
                    'event_types': git_stats[1] if git_stats else 0,
                    'avg_files_changed': round(git_stats[2], 1) if git_stats and git_stats[2] else 0,
                    'total_files_changed': git_stats[3] if git_stats else 0,
                    'active_authors': git_stats[4] if git_stats else 0,
                    'active_branches': git_stats[5] if git_stats else 0
                },
                'claude_activity': {
                    'total_events': claude_stats[0] if claude_stats else 0,
                    'tools_used': claude_stats[1] if claude_stats else 0,
                    'avg_execution_time': round(claude_stats[2], 3) if claude_stats and claude_stats[2] else 0,
                    'success_rate': round(claude_stats[3] * 100, 1) if claude_stats and claude_stats[3] else 0,
                    'context_preservation_rate': round(claude_stats[4] * 100, 1) if claude_stats and claude_stats[4] else 0
                },
                'performance_metrics': performance_metrics
            }
            
        except Exception as e:
            self.logger.error(f"Error getting performance summary: {e}")
            return {'error': str(e)}

def main():
    """CLI interface for event capture system"""
    parser = argparse.ArgumentParser(description='CE-Simple Event Capture System')
    parser.add_argument('action', choices=['capture-git-event', 'capture-claude-event', 'recent-events', 'performance-summary'])
    parser.add_argument('--limit', type=int, default=50, help='Limit for recent events')
    parser.add_argument('--hours', type=int, default=24, help='Hours for performance summary')
    parser.add_argument('--type', choices=['git', 'claude'], help='Event type filter')
    
    args = parser.parse_args()
    
    capture_system = EventCaptureSystem()
    
    if args.action == 'capture-git-event':
        # Read JSON from stdin
        try:
            event_data = json.loads(sys.stdin.read())
            result = capture_system.capture_git_event(event_data)
            print(f"Event captured: {result}")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}", file=sys.stderr)
            sys.exit(1)
    
    elif args.action == 'capture-claude-event':
        # Read JSON from stdin
        try:
            event_data = json.loads(sys.stdin.read())
            result = capture_system.capture_claude_event(event_data)
            print(f"Event captured: {result}")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}", file=sys.stderr)
            sys.exit(1)
    
    elif args.action == 'recent-events':
        events = capture_system.get_recent_events(args.limit, args.type)
        print(json.dumps(events, indent=2))
    
    elif args.action == 'performance-summary':
        summary = capture_system.get_performance_summary(args.hours)
        print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()