#!/usr/bin/env python3
"""
Predictive Command Recommendation System
CE-Simple Intelligence Enhancement

Analyzes user patterns and context to provide intelligent command recommendations
without being intrusive. Integrates with existing CLAUDE.md workflow.
"""

import json
import os
import re
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set
from collections import defaultdict, Counter
from dataclasses import dataclass, asdict
import sqlite3
from contextlib import contextmanager


@dataclass
class CommandUsage:
    """Command usage metadata"""
    command: str
    timestamp: datetime
    context: str
    session_id: str
    success: bool
    execution_time: float
    user_feedback: Optional[str] = None


@dataclass
class PatternAnalysis:
    """Pattern analysis results"""
    frequent_sequences: List[Tuple[str, float]]
    contextual_triggers: Dict[str, List[str]]
    temporal_patterns: Dict[str, Dict[str, int]]
    success_correlations: Dict[str, float]


@dataclass
class Recommendation:
    """Command recommendation with metadata"""
    command: str
    confidence: float
    reasoning: str
    context_match: float
    estimated_value: float
    integration_opportunities: List[str]


class ConversationAnalyzer:
    """Analyzes conversation history for patterns"""
    
    def __init__(self, narratives_path: str):
        self.narratives_path = Path(narratives_path)
        self.logger = logging.getLogger(__name__)
    
    def extract_command_sequences(self) -> List[List[str]]:
        """Extract command sequences from conversation history"""
        sequences = []
        
        # Analyze conversation files
        conv_path = self.narratives_path / "raw" / "conversations"
        if not conv_path.exists():
            self.logger.warning(f"Conversation path not found: {conv_path}")
            return sequences
        
        for conv_file in conv_path.glob("*.md"):
            try:
                with open(conv_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract commands mentioned in conversation
                commands = self._extract_commands_from_text(content)
                if commands:
                    sequences.append(commands)
                    
            except Exception as e:
                self.logger.error(f"Error processing {conv_file}: {e}")
        
        return sequences
    
    def _extract_commands_from_text(self, text: str) -> List[str]:
        """Extract command mentions from conversation text"""
        # Pattern for /command mentions
        command_pattern = r'/([a-z-]+(?:-[a-z]+)*)'
        
        # Pattern for command file references
        file_pattern = r'\.claude/commands/([a-z-]+(?:-[a-z]+)*)\.md'
        
        commands = []
        
        # Extract direct command mentions
        for match in re.finditer(command_pattern, text):
            command = match.group(1)
            if self._is_valid_command(command):
                commands.append(command)
        
        # Extract file references
        for match in re.finditer(file_pattern, text):
            command = match.group(1)
            if self._is_valid_command(command):
                commands.append(command)
        
        return list(dict.fromkeys(commands))  # Remove duplicates while preserving order
    
    def _is_valid_command(self, command: str) -> bool:
        """Validate if string is a legitimate command"""
        # Check against known commands
        valid_commands = {
            'start', 'session-close', 'create-doc', 'align-doc', 'verify-doc',
            'contextflow-agent', 'extract-insights', 'process-layer', 'analyze',
            'implement', 'explore', 'debug', 'test', 'refactor', 'master-plan'
        }
        
        return command in valid_commands or len(command) > 2
    
    def analyze_contextual_triggers(self, text: str) -> Dict[str, float]:
        """Analyze text for contextual triggers that suggest specific commands"""
        triggers = {
            'create-doc': ['create', 'document', 'write', 'new file', 'documentation'],
            'analyze': ['analyze', 'understand', 'explore', 'investigate', 'examine'],
            'implement': ['implement', 'build', 'create', 'develop', 'code'],
            'debug': ['error', 'bug', 'fix', 'problem', 'issue', 'not working'],
            'test': ['test', 'validate', 'verify', 'check', 'confirm'],
            'refactor': ['refactor', 'clean', 'organize', 'optimize', 'improve'],
            'start': ['start', 'begin', 'initialize', 'setup', 'new session'],
            'session-close': ['close', 'finish', 'complete', 'end', 'summary']
        }
        
        scores = {}
        text_lower = text.lower()
        
        for command, keywords in triggers.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            if score > 0:
                scores[command] = score / len(keywords)  # Normalize by keyword count
        
        return scores


class PatternLearningEngine:
    """Learns patterns from historical usage data"""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.logger = logging.getLogger(__name__)
        self._init_database()
    
    def _init_database(self):
        """Initialize SQLite database for pattern storage"""
        with self._get_db_connection() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS command_usage (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    command TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    context TEXT,
                    session_id TEXT,
                    success INTEGER,
                    execution_time REAL,
                    user_feedback TEXT
                )
            ''')
            
            conn.execute('''
                CREATE TABLE IF NOT EXISTS command_sequences (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sequence TEXT NOT NULL,
                    frequency INTEGER DEFAULT 1,
                    success_rate REAL,
                    last_seen TEXT
                )
            ''')
            
            conn.execute('''
                CREATE TABLE IF NOT EXISTS context_patterns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    context_hash TEXT UNIQUE,
                    context_keywords TEXT,
                    recommended_commands TEXT,
                    success_rate REAL,
                    usage_count INTEGER DEFAULT 1
                )
            ''')
    
    @contextmanager
    def _get_db_connection(self):
        """Get database connection with proper cleanup"""
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()
    
    def record_usage(self, usage: CommandUsage):
        """Record command usage for pattern learning"""
        with self._get_db_connection() as conn:
            conn.execute('''
                INSERT INTO command_usage 
                (command, timestamp, context, session_id, success, execution_time, user_feedback)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                usage.command,
                usage.timestamp.isoformat(),
                usage.context,
                usage.session_id,
                1 if usage.success else 0,
                usage.execution_time,
                usage.user_feedback
            ))
    
    def learn_sequences(self, sequences: List[List[str]]):
        """Learn command sequences from historical data"""
        sequence_counts = Counter()
        
        for sequence in sequences:
            if len(sequence) < 2:
                continue
            
            # Generate subsequences of length 2-4
            for length in range(2, min(5, len(sequence) + 1)):
                for i in range(len(sequence) - length + 1):
                    subseq = tuple(sequence[i:i + length])
                    sequence_counts[subseq] += 1
        
        # Store in database
        with self._get_db_connection() as conn:
            for sequence, count in sequence_counts.items():
                sequence_str = '->'.join(sequence)
                conn.execute('''
                    INSERT OR REPLACE INTO command_sequences 
                    (sequence, frequency, last_seen)
                    VALUES (?, ?, ?)
                ''', (sequence_str, count, datetime.now().isoformat()))
    
    def analyze_temporal_patterns(self) -> Dict[str, Dict[str, int]]:
        """Analyze temporal usage patterns"""
        patterns = defaultdict(lambda: defaultdict(int))
        
        with self._get_db_connection() as conn:
            cursor = conn.execute('''
                SELECT command, timestamp FROM command_usage
                WHERE timestamp > ?
            ''', ((datetime.now() - timedelta(days=30)).isoformat(),))
            
            for command, timestamp_str in cursor.fetchall():
                try:
                    dt = datetime.fromisoformat(timestamp_str)
                    hour = dt.hour
                    day_of_week = dt.strftime('%A')
                    
                    patterns[command]['hour_' + str(hour)] += 1
                    patterns[command]['day_' + day_of_week] += 1
                    
                except Exception as e:
                    self.logger.error(f"Error parsing timestamp {timestamp_str}: {e}")
        
        return dict(patterns)
    
    def get_success_correlations(self) -> Dict[str, float]:
        """Calculate success rates for commands"""
        correlations = {}
        
        with self._get_db_connection() as conn:
            cursor = conn.execute('''
                SELECT command, AVG(success) as success_rate, COUNT(*) as total
                FROM command_usage 
                GROUP BY command
                HAVING total >= 3
            ''')
            
            for command, success_rate, total in cursor.fetchall():
                correlations[command] = success_rate
        
        return correlations


class RecommendationEngine:
    """Generates intelligent command recommendations"""
    
    def __init__(self, learning_engine: PatternLearningEngine, 
                 conversation_analyzer: ConversationAnalyzer):
        self.learning_engine = learning_engine
        self.conversation_analyzer = conversation_analyzer
        self.logger = logging.getLogger(__name__)
    
    def generate_recommendations(self, current_context: str, 
                               recent_commands: List[str] = None,
                               max_recommendations: int = 5) -> List[Recommendation]:
        """Generate contextual command recommendations"""
        recommendations = []
        
        # Analyze current context for triggers
        contextual_scores = self.conversation_analyzer.analyze_contextual_triggers(current_context)
        
        # Get sequence-based recommendations
        sequence_recs = self._get_sequence_recommendations(recent_commands or [])
        
        # Get temporal pattern recommendations
        temporal_recs = self._get_temporal_recommendations()
        
        # Combine and score recommendations
        all_candidates = {}
        
        # Add contextual recommendations
        for command, score in contextual_scores.items():
            all_candidates[command] = {
                'contextual_score': score,
                'sequence_score': 0,
                'temporal_score': 0,
                'reasoning': f"Contextual match based on current discussion"
            }
        
        # Add sequence recommendations
        for command, score in sequence_recs.items():
            if command not in all_candidates:
                all_candidates[command] = {
                    'contextual_score': 0,
                    'sequence_score': score,
                    'temporal_score': 0,
                    'reasoning': f"Frequent sequence pattern"
                }
            else:
                all_candidates[command]['sequence_score'] = score
                all_candidates[command]['reasoning'] += " + sequence pattern"
        
        # Add temporal recommendations
        for command, score in temporal_recs.items():
            if command not in all_candidates:
                all_candidates[command] = {
                    'contextual_score': 0,
                    'sequence_score': 0,
                    'temporal_score': score,
                    'reasoning': f"Temporal usage pattern"
                }
            else:
                all_candidates[command]['temporal_score'] = score
                all_candidates[command]['reasoning'] += " + temporal pattern"
        
        # Calculate final scores and create recommendations
        success_correlations = self.learning_engine.get_success_correlations()
        
        for command, scores in all_candidates.items():
            confidence = self._calculate_confidence(scores, success_correlations.get(command, 0.5))
            
            if confidence > 0.3:  # Minimum confidence threshold
                recommendation = Recommendation(
                    command=command,
                    confidence=confidence,
                    reasoning=scores['reasoning'],
                    context_match=scores['contextual_score'],
                    estimated_value=self._estimate_value(command, scores),
                    integration_opportunities=self._find_integration_opportunities(command)
                )
                recommendations.append(recommendation)
        
        # Sort by confidence and return top recommendations
        recommendations.sort(key=lambda x: x.confidence, reverse=True)
        return recommendations[:max_recommendations]
    
    def _get_sequence_recommendations(self, recent_commands: List[str]) -> Dict[str, float]:
        """Get recommendations based on command sequences"""
        if not recent_commands:
            return {}
        
        recommendations = {}
        
        with self.learning_engine._get_db_connection() as conn:
            # Look for sequences that start with recent commands
            for i in range(len(recent_commands)):
                prefix = '->'.join(recent_commands[i:])
                cursor = conn.execute('''
                    SELECT sequence, frequency FROM command_sequences
                    WHERE sequence LIKE ? AND frequency > 1
                    ORDER BY frequency DESC
                    LIMIT 10
                ''', (prefix + '%',))
                
                for sequence_str, frequency in cursor.fetchall():
                    sequence = sequence_str.split('->')
                    if len(sequence) > len(recent_commands[i:]):
                        next_command = sequence[len(recent_commands[i:]) + i]
                        score = frequency / 10.0  # Normalize frequency
                        recommendations[next_command] = max(
                            recommendations.get(next_command, 0), score
                        )
        
        return recommendations
    
    def _get_temporal_recommendations(self) -> Dict[str, float]:
        """Get recommendations based on temporal patterns"""
        current_time = datetime.now()
        current_hour = current_time.hour
        current_day = current_time.strftime('%A')
        
        temporal_patterns = self.learning_engine.analyze_temporal_patterns()
        recommendations = {}
        
        for command, patterns in temporal_patterns.items():
            hour_key = f'hour_{current_hour}'
            day_key = f'day_{current_day}'
            
            hour_score = patterns.get(hour_key, 0) / 100.0  # Normalize
            day_score = patterns.get(day_key, 0) / 100.0   # Normalize
            
            total_score = (hour_score + day_score) / 2
            if total_score > 0.1:
                recommendations[command] = total_score
        
        return recommendations
    
    def _calculate_confidence(self, scores: Dict[str, float], success_rate: float) -> float:
        """Calculate overall confidence for a recommendation"""
        # Weighted combination of different scores
        weights = {
            'contextual_score': 0.5,
            'sequence_score': 0.3,
            'temporal_score': 0.2
        }
        
        base_confidence = sum(scores[key] * weights[key] for key in weights)
        
        # Adjust by success rate
        confidence = base_confidence * (0.5 + success_rate * 0.5)
        
        # Cap at 0.95 to maintain humility
        return min(confidence, 0.95)
    
    def _estimate_value(self, command: str, scores: Dict[str, float]) -> float:
        """Estimate the value/utility of executing this command"""
        # Base value estimates for different command types
        base_values = {
            'create-doc': 0.8,    # High value for documentation
            'analyze': 0.7,       # High value for understanding
            'implement': 0.9,     # Very high value for implementation
            'debug': 0.6,         # Medium-high value for problem solving
            'test': 0.7,          # High value for validation
            'start': 0.5,         # Medium value for session management
            'session-close': 0.4  # Lower value but necessary
        }
        
        base_value = base_values.get(command, 0.5)
        
        # Adjust based on contextual relevance
        context_boost = scores['contextual_score'] * 0.3
        
        return min(base_value + context_boost, 1.0)
    
    def _find_integration_opportunities(self, command: str) -> List[str]:
        """Find integration opportunities with other commands"""
        integration_patterns = {
            'create-doc': ['align-doc', 'verify-doc'],
            'analyze': ['implement', 'test'],
            'implement': ['test', 'debug'],
            'debug': ['test', 'refactor'],
            'start': ['extract-insights', 'analyze'],
            'contextflow-agent': ['process-layer', 'session-close']
        }
        
        return integration_patterns.get(command, [])


class PredictiveSystem:
    """Main predictive system orchestrator"""
    
    def __init__(self, base_path: str = "/Users/nalve/ce-simple"):
        self.base_path = Path(base_path)
        self.narratives_path = self.base_path / "narratives"
        self.db_path = self.base_path / "tools" / "automation" / "predictive.db"
        
        # Ensure directories exist
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Initialize components
        self.conversation_analyzer = ConversationAnalyzer(str(self.narratives_path))
        self.learning_engine = PatternLearningEngine(str(self.db_path))
        self.recommendation_engine = RecommendationEngine(
            self.learning_engine, self.conversation_analyzer
        )
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.base_path / "tools" / "automation" / "predictive.log"),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def initialize_system(self):
        """Initialize the predictive system with historical data"""
        self.logger.info("Initializing predictive system...")
        
        # Extract and learn from conversation sequences
        sequences = self.conversation_analyzer.extract_command_sequences()
        self.learning_engine.learn_sequences(sequences)
        
        self.logger.info(f"Learned from {len(sequences)} conversation sequences")
    
    def get_recommendations(self, context: str, recent_commands: List[str] = None) -> List[Recommendation]:
        """Get command recommendations for current context"""
        try:
            recommendations = self.recommendation_engine.generate_recommendations(
                context, recent_commands
            )
            
            self.logger.info(f"Generated {len(recommendations)} recommendations")
            return recommendations
            
        except Exception as e:
            self.logger.error(f"Error generating recommendations: {e}")
            return []
    
    def record_command_usage(self, command: str, context: str, success: bool = True,
                           execution_time: float = 0.0, user_feedback: str = None):
        """Record command usage for learning"""
        usage = CommandUsage(
            command=command,
            timestamp=datetime.now(),
            context=context,
            session_id=self._get_current_session_id(),
            success=success,
            execution_time=execution_time,
            user_feedback=user_feedback
        )
        
        self.learning_engine.record_usage(usage)
    
    def _get_current_session_id(self) -> str:
        """Generate or retrieve current session ID"""
        # Simple session ID based on current date/time
        return datetime.now().strftime("%Y-%m-%d_%H-%M")
    
    def export_patterns(self) -> Dict:
        """Export learned patterns for analysis or backup"""
        patterns = {}
        
        with self.learning_engine._get_db_connection() as conn:
            # Export sequences
            cursor = conn.execute('SELECT * FROM command_sequences ORDER BY frequency DESC')
            patterns['sequences'] = [
                {'sequence': row[1], 'frequency': row[2], 'success_rate': row[3]}
                for row in cursor.fetchall()
            ]
            
            # Export usage stats
            cursor = conn.execute('''
                SELECT command, COUNT(*) as usage_count, AVG(success) as success_rate
                FROM command_usage 
                GROUP BY command
                ORDER BY usage_count DESC
            ''')
            patterns['command_stats'] = [
                {'command': row[0], 'usage_count': row[1], 'success_rate': row[2]}
                for row in cursor.fetchall()
            ]
        
        return patterns


# API Functions for Integration
def get_smart_suggestions(context: str, recent_commands: List[str] = None) -> List[Dict]:
    """
    Main API function for getting command suggestions
    Returns list of suggestion dictionaries for easy integration
    """
    system = PredictiveSystem()
    recommendations = system.get_recommendations(context, recent_commands)
    
    return [
        {
            'command': rec.command,
            'confidence': rec.confidence,
            'reasoning': rec.reasoning,
            'estimated_value': rec.estimated_value,
            'integration_opportunities': rec.integration_opportunities
        }
        for rec in recommendations
    ]


def record_usage(command: str, context: str, success: bool = True, 
                execution_time: float = 0.0, feedback: str = None):
    """
    API function for recording command usage
    Should be called after command execution
    """
    system = PredictiveSystem()
    system.record_command_usage(command, context, success, execution_time, feedback)


def initialize_learning():
    """
    Initialize the learning system with historical data
    Should be called once during system setup
    """
    system = PredictiveSystem()
    system.initialize_system()


if __name__ == "__main__":
    # Example usage and testing
    system = PredictiveSystem()
    system.initialize_system()
    
    # Test recommendations
    test_context = "I need to create documentation for the new feature and then validate it"
    recommendations = system.get_recommendations(test_context)
    
    print("Predictive Recommendations:")
    for rec in recommendations:
        print(f"  /{rec.command} (confidence: {rec.confidence:.2f}) - {rec.reasoning}")
        if rec.integration_opportunities:
            print(f"    → Suggested follow-ups: {', '.join(rec.integration_opportunities)}")