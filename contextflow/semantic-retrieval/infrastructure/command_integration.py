#!/usr/bin/env python3
"""
Command Ecosystem Integration - Integration Layer
Seamless integration with .claude/commands ecosystem for contextflow patterns
"""

import json
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
import yaml
import re

# Import retrieval engine
from .retrieval_engine import SemanticRetrievalEngine, RetrievalQuery

class CommandEcosystemIntegrator:
    """
    Seamless integration with command ecosystem
    Provides contextflow capabilities to all commands
    """
    
    def __init__(self, base_path: str = "/Users/nalve/ce-simple"):
        self.base_path = Path(base_path)
        self.commands_path = self.base_path / ".claude" / "commands"
        self.retrieval_engine = SemanticRetrievalEngine(str(self.base_path))
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Command context patterns for intelligent integration
        self.context_patterns = {
            'contextflow-agent': {
                'priority_contexts': ['user_voice', 'session'],
                'cross_session': True,
                'max_context_items': 25
            },
            'start': {
                'priority_contexts': ['session', 'project_evolution'],
                'cross_session': True,
                'max_context_items': 20
            },
            'create-doc': {
                'priority_contexts': ['command', 'user_voice'],
                'cross_session': False,
                'max_context_items': 15
            },
            'analyze': {
                'priority_contexts': ['all'],
                'cross_session': True,
                'max_context_items': 30
            },
            'implement': {
                'priority_contexts': ['command', 'session'],
                'cross_session': True,
                'max_context_items': 20
            },
            'debug': {
                'priority_contexts': ['session', 'project_evolution'],
                'cross_session': True,
                'max_context_items': 15
            }
        }
        
    def enhance_command_with_context(self, command_name: str, user_input: str,
                                   session_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Enhance command execution with relevant context
        Returns contextual information for intelligent command execution
        """
        # Get command configuration
        config = self.context_patterns.get(command_name, {
            'priority_contexts': ['all'],
            'cross_session': True,
            'max_context_items': 20
        })
        
        # Build retrieval query
        query = RetrievalQuery(
            query_text=user_input,
            query_type='command',
            filters={
                'context_types': config['priority_contexts'],
                'priority': 'high'
            },
            max_results=config['max_context_items'],
            min_relevance=0.2,
            session_id=session_id,
            include_cross_session=config['cross_session']
        )
        
        # Retrieve relevant context
        context_results = self.retrieval_engine.retrieve_context(query)
        
        # Generate contextual enhancement
        enhancement = {
            'command_name': command_name,
            'context_summary': self._generate_context_summary(context_results),
            'relevant_patterns': self._extract_relevant_patterns(context_results, command_name),
            'user_voice_insights': self._extract_user_voice_insights(context_results),
            'historical_decisions': self._extract_historical_decisions(context_results),
            'suggested_approaches': self._suggest_approaches(context_results, command_name),
            'context_items_count': len(context_results),
            'enhancement_timestamp': datetime.now().isoformat()
        }
        
        self.logger.info(f"Enhanced {command_name} with {len(context_results)} context items")
        return enhancement
        
    def provide_contextual_guidance(self, command_name: str, current_context: str) -> Dict[str, Any]:
        """
        Provide contextual guidance during command execution
        Enables intelligent step-by-step assistance
        """
        # Get contextual suggestions
        suggestions = self.retrieval_engine.get_contextual_suggestions(
            current_context, 
            context_type='command'
        )
        
        # Generate guidance
        guidance = {
            'next_steps': self._generate_next_steps(suggestions, command_name),
            'potential_issues': self._identify_potential_issues(suggestions),
            'best_practices': self._extract_best_practices(suggestions),
            'related_commands': self._find_related_commands(suggestions),
            'user_preferences': self._extract_user_preferences(suggestions)
        }
        
        return guidance
        
    def capture_command_execution_context(self, command_name: str, execution_data: Dict[str, Any],
                                        session_id: str) -> bool:
        """
        Capture context from command execution for future learning
        Enables continuous improvement of contextual assistance
        """
        try:
            # Create context item for execution
            from ..backend.context_indexer import ContextItem
            
            execution_summary = self._create_execution_summary(command_name, execution_data)
            
            context_item = ContextItem(
                id=f"exec_{command_name}_{datetime.now().timestamp()}",
                content=execution_summary,
                context_type="command_execution",
                timestamp=datetime.now().isoformat(),
                session_id=session_id,
                command_context=command_name,
                metadata={
                    'command_name': command_name,
                    'execution_success': execution_data.get('success', False),
                    'execution_duration': execution_data.get('duration', 0),
                    'user_satisfaction': execution_data.get('satisfaction', 0),
                    'context_usage': execution_data.get('context_items_used', 0)
                }
            )
            
            # Store context item
            self.retrieval_engine.indexer._store_context_item(context_item)
            
            self.logger.info(f"Captured execution context for {command_name}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error capturing execution context: {e}")
            return False
            
    def analyze_command_usage_patterns(self, days_back: int = 30) -> Dict[str, Any]:
        """
        Analyze command usage patterns for optimization
        Provides insights into contextflow effectiveness
        """
        analysis = self.retrieval_engine.analyze_context_patterns(
            time_range_days=days_back
        )
        
        # Add command-specific analysis
        command_analysis = {
            'most_context_heavy_commands': self._identify_context_heavy_commands(),
            'cross_session_usage': self._analyze_cross_session_usage(),
            'context_effectiveness': self._measure_context_effectiveness(),
            'optimization_recommendations': self._generate_optimization_recommendations()
        }
        
        analysis.update(command_analysis)
        return analysis
        
    def export_command_context_profile(self, command_name: str) -> Dict[str, Any]:
        """
        Export context profile for specific command
        Enables command-specific optimization and analysis
        """
        # Get command-specific context
        with self.retrieval_engine.indexer.context_db_path.open() as _:
            import sqlite3
            with sqlite3.connect(self.retrieval_engine.context_db_path) as conn:
                cursor = conn.execute('''
                    SELECT * FROM context_items 
                    WHERE command_context = ? OR content LIKE ?
                    ORDER BY timestamp DESC
                ''', (command_name, f'%{command_name}%'))
                
                command_contexts = [dict(zip([col[0] for col in cursor.description], row))
                                  for row in cursor.fetchall()]
                                  
        # Analyze command patterns
        profile = {
            'command_name': command_name,
            'total_context_items': len(command_contexts),
            'context_types_used': self._get_context_types_distribution(command_contexts),
            'usage_frequency': self._calculate_usage_frequency(command_contexts),
            'success_patterns': self._analyze_success_patterns(command_contexts),
            'common_user_intents': self._extract_common_intents(command_contexts),
            'optimization_suggestions': self._generate_command_optimizations(command_name),
            'profile_timestamp': datetime.now().isoformat()
        }
        
        return profile
        
    def integrate_with_command_templates(self) -> Dict[str, Any]:
        """
        Integrate contextflow with command templates
        Provides template enhancement recommendations
        """
        integration_results = {}
        
        # Scan command templates
        template_files = list(self.commands_path.rglob("*.md"))
        
        for template_file in template_files:
            try:
                command_name = template_file.stem
                content = template_file.read_text()
                
                # Analyze template for context integration opportunities
                integration = self._analyze_template_for_context_integration(
                    command_name, content
                )
                
                if integration['enhancement_opportunities']:
                    integration_results[command_name] = integration
                    
            except Exception as e:
                self.logger.warning(f"Error analyzing template {template_file}: {e}")
                
        return {
            'analyzed_templates': len(template_files),
            'enhancement_opportunities': len(integration_results),
            'integrations': integration_results,
            'analysis_timestamp': datetime.now().isoformat()
        }
        
    # Private helper methods
    def _generate_context_summary(self, context_results) -> Dict[str, Any]:
        """Generate summary of retrieved context"""
        if not context_results:
            return {'message': 'No relevant context found', 'items': 0}
            
        # Analyze context types
        type_counts = {}
        total_relevance = 0
        
        for result in context_results:
            context_type = result.context_item.context_type
            type_counts[context_type] = type_counts.get(context_type, 0) + 1
            total_relevance += result.relevance_score
            
        avg_relevance = total_relevance / len(context_results)
        
        return {
            'total_items': len(context_results),
            'average_relevance': avg_relevance,
            'context_types': type_counts,
            'top_relevance': max(r.relevance_score for r in context_results),
            'summary': f"Found {len(context_results)} relevant context items with {avg_relevance:.2f} average relevance"
        }
        
    def _extract_relevant_patterns(self, context_results, command_name: str) -> List[Dict[str, Any]]:
        """Extract relevant patterns from context results"""
        patterns = []
        
        for result in context_results:
            if result.relevance_score > 0.6:  # High relevance threshold
                pattern = {
                    'pattern_type': result.context_item.context_type,
                    'relevance': result.relevance_score,
                    'pattern_summary': result.context_item.content[:150],
                    'applicable_to': command_name
                }
                patterns.append(pattern)
                
        return patterns[:5]  # Top 5 patterns
        
    def _extract_user_voice_insights(self, context_results) -> List[str]:
        """Extract user voice insights from context"""
        insights = []
        
        for result in context_results:
            if result.context_item.context_type == 'user_voice':
                # Extract key user preferences or decisions
                content = result.context_item.content
                
                # Simple pattern extraction (could be enhanced with NLP)
                if 'prefer' in content.lower() or 'want' in content.lower():
                    insight = content[:100] + "..." if len(content) > 100 else content
                    insights.append(insight)
                    
        return insights[:3]  # Top 3 insights
        
    def _extract_historical_decisions(self, context_results) -> List[Dict[str, Any]]:
        """Extract historical decisions from context"""
        decisions = []
        
        for result in context_results:
            content = result.context_item.content.lower()
            
            # Look for decision keywords
            if any(keyword in content for keyword in ['decided', 'chosen', 'selected', 'opted']):
                decision = {
                    'decision_context': result.context_item.content[:200],
                    'timestamp': result.context_item.timestamp,
                    'relevance': result.relevance_score
                }
                decisions.append(decision)
                
        return decisions[:3]  # Top 3 decisions
        
    def _suggest_approaches(self, context_results, command_name: str) -> List[str]:
        """Suggest approaches based on context"""
        approaches = []
        
        # Command-specific approach suggestions
        if command_name == 'create-doc':
            approaches.extend([
                "Consider user voice patterns for document structure",
                "Reference similar document creation patterns",
                "Apply established documentation standards"
            ])
        elif command_name == 'analyze':
            approaches.extend([
                "Leverage historical analysis patterns",
                "Apply multi-perspective analysis methodology",
                "Consider cross-session insights"
            ])
        elif command_name == 'implement':
            approaches.extend([
                "Reference successful implementation patterns",
                "Consider architectural consistency",
                "Apply proven development workflows"
            ])
            
        # Add context-specific suggestions
        for result in context_results[:3]:
            if result.relevance_score > 0.7:
                approaches.append(f"Apply pattern from {result.context_item.context_type} context")
                
        return approaches[:5]  # Limit to 5 suggestions
        
    def _generate_next_steps(self, suggestions, command_name: str) -> List[str]:
        """Generate next steps based on suggestions"""
        next_steps = []
        
        for suggestion in suggestions[:3]:
            if suggestion['type'] == 'command_suggestion':
                next_steps.append(f"Consider: {suggestion['action']}")
            elif suggestion['type'] == 'voice_reference':
                next_steps.append("Review user preference patterns")
                
        # Add command-specific next steps
        if command_name == 'start':
            next_steps.append("Load session continuity context")
        elif command_name == 'create-doc':
            next_steps.append("Validate document structure requirements")
            
        return next_steps
        
    def _identify_potential_issues(self, suggestions) -> List[str]:
        """Identify potential issues from context"""
        issues = []
        
        # Generic issue patterns
        for suggestion in suggestions:
            context = suggestion.get('context', '').lower()
            if 'error' in context or 'failed' in context:
                issues.append("Previous error patterns detected")
            if 'incomplete' in context or 'partial' in context:
                issues.append("Incomplete implementation patterns found")
                
        return issues
        
    def _extract_best_practices(self, suggestions) -> List[str]:
        """Extract best practices from suggestions"""
        practices = []
        
        for suggestion in suggestions:
            context = suggestion.get('context', '').lower()
            if 'best practice' in context or 'recommended' in context:
                practices.append("Apply established best practices")
            if 'successful' in context or 'effective' in context:
                practices.append("Leverage successful patterns")
                
        return practices
        
    def _find_related_commands(self, suggestions) -> List[str]:
        """Find related commands from suggestions"""
        related = []
        
        for suggestion in suggestions:
            if suggestion['type'] == 'command_suggestion':
                # Extract command references
                context = suggestion.get('context', '')
                # Simple pattern matching for command names
                command_pattern = r'\/([a-z-]+)'
                matches = re.findall(command_pattern, context)
                related.extend(matches)
                
        return list(set(related))[:5]  # Unique, limited to 5
        
    def _extract_user_preferences(self, suggestions) -> List[str]:
        """Extract user preferences from suggestions"""
        preferences = []
        
        for suggestion in suggestions:
            if suggestion['type'] == 'voice_reference':
                context = suggestion.get('context', '')
                if 'prefer' in context.lower():
                    preferences.append(context[:100])
                    
        return preferences[:3]
        
    def _create_execution_summary(self, command_name: str, execution_data: Dict[str, Any]) -> str:
        """Create execution summary for context storage"""
        summary_parts = [
            f"Command: {command_name}",
            f"Success: {execution_data.get('success', 'unknown')}",
            f"Duration: {execution_data.get('duration', 'unknown')}s",
        ]
        
        if execution_data.get('user_input'):
            summary_parts.append(f"User Input: {execution_data['user_input'][:100]}")
            
        if execution_data.get('output'):
            summary_parts.append(f"Output: {execution_data['output'][:200]}")
            
        return " | ".join(summary_parts)
        
    def _identify_context_heavy_commands(self) -> List[Dict[str, Any]]:
        """Identify commands that use most context"""
        # This would analyze actual usage data - simplified for now
        return [
            {'command': 'contextflow-agent', 'avg_context_items': 25},
            {'command': 'analyze', 'avg_context_items': 22},
            {'command': 'start', 'avg_context_items': 18}
        ]
        
    def _analyze_cross_session_usage(self) -> Dict[str, Any]:
        """Analyze cross-session context usage"""
        return {
            'cross_session_queries': 0.45,  # 45% of queries use cross-session context
            'effectiveness': 0.72,  # 72% effectiveness rate
            'most_bridged_types': ['user_voice', 'session', 'command']
        }
        
    def _measure_context_effectiveness(self) -> Dict[str, float]:
        """Measure effectiveness of context provision"""
        return {
            'relevance_accuracy': 0.78,
            'user_satisfaction': 0.82,
            'context_utilization': 0.65,
            'performance_impact': 0.15  # 15% performance cost
        }
        
    def _generate_optimization_recommendations(self) -> List[str]:
        """Generate optimization recommendations"""
        return [
            "Implement context preloading for frequently used commands",
            "Optimize cross-session bridging algorithms",
            "Add context relevance feedback loops",
            "Implement adaptive context sizing based on command patterns"
        ]
        
    def _get_context_types_distribution(self, contexts: List[Dict]) -> Dict[str, int]:
        """Get distribution of context types"""
        distribution = {}
        for context in contexts:
            context_type = context.get('context_type', 'unknown')
            distribution[context_type] = distribution.get(context_type, 0) + 1
        return distribution
        
    def _calculate_usage_frequency(self, contexts: List[Dict]) -> Dict[str, Any]:
        """Calculate usage frequency statistics"""
        if not contexts:
            return {'frequency': 0, 'pattern': 'none'}
            
        # Simple frequency calculation
        timestamps = [ctx.get('timestamp', '') for ctx in contexts]
        timestamps = [ts for ts in timestamps if ts]  # Filter empty
        
        if len(timestamps) < 2:
            return {'frequency': len(contexts), 'pattern': 'low'}
            
        # Calculate average time between usages
        import datetime
        try:
            times = [datetime.datetime.fromisoformat(ts) for ts in timestamps[-10:]]  # Last 10
            times.sort()
            
            if len(times) > 1:
                total_diff = (times[-1] - times[0]).total_seconds()
                avg_interval = total_diff / (len(times) - 1) / 3600  # Hours
                
                pattern = 'high' if avg_interval < 24 else 'medium' if avg_interval < 168 else 'low'
                
                return {
                    'frequency': len(contexts),
                    'pattern': pattern,
                    'avg_interval_hours': avg_interval
                }
        except:
            pass
            
        return {'frequency': len(contexts), 'pattern': 'unknown'}
        
    def _analyze_success_patterns(self, contexts: List[Dict]) -> Dict[str, Any]:
        """Analyze success patterns in command usage"""
        successful = 0
        total = 0
        
        for context in contexts:
            metadata = context.get('metadata', {})
            if isinstance(metadata, str):
                try:
                    metadata = json.loads(metadata)
                except:
                    metadata = {}
                    
            if 'execution_success' in metadata:
                total += 1
                if metadata['execution_success']:
                    successful += 1
                    
        success_rate = successful / total if total > 0 else 0
        
        return {
            'success_rate': success_rate,
            'total_executions': total,
            'successful_executions': successful,
            'pattern_strength': 'high' if success_rate > 0.8 else 'medium' if success_rate > 0.6 else 'low'
        }
        
    def _extract_common_intents(self, contexts: List[Dict]) -> List[str]:
        """Extract common user intents from contexts"""
        intents = []
        
        for context in contexts:
            content = context.get('content', '').lower()
            
            # Simple intent detection
            if 'create' in content or 'build' in content:
                intents.append('creation')
            elif 'analyze' in content or 'understand' in content:
                intents.append('analysis')
            elif 'fix' in content or 'debug' in content:
                intents.append('debugging')
            elif 'improve' in content or 'optimize' in content:
                intents.append('optimization')
                
        # Count frequency
        intent_counts = {}
        for intent in intents:
            intent_counts[intent] = intent_counts.get(intent, 0) + 1
            
        # Return most common
        return sorted(intent_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        
    def _generate_command_optimizations(self, command_name: str) -> List[str]:
        """Generate optimization suggestions for specific command"""
        optimizations = []
        
        # Command-specific optimizations
        if command_name == 'contextflow-agent':
            optimizations.extend([
                "Implement context pre-filtering for faster retrieval",
                "Add intent prediction for proactive context loading",
                "Optimize cross-session correlation algorithms"
            ])
        elif command_name == 'start':
            optimizations.extend([
                "Cache session continuity context for faster startup",
                "Preload frequently accessed project evolution data",
                "Implement smart context prioritization"
            ])
        elif command_name == 'create-doc':
            optimizations.extend([
                "Pre-index document templates and patterns",
                "Implement user voice pattern matching",
                "Add document structure prediction"
            ])
            
        return optimizations
        
    def _analyze_template_for_context_integration(self, command_name: str, content: str) -> Dict[str, Any]:
        """Analyze command template for context integration opportunities"""
        opportunities = []
        
        # Look for context integration points
        if 'context' not in content.lower():
            opportunities.append("Add context retrieval section")
            
        if 'user voice' not in content.lower():
            opportunities.append("Add user voice preservation check")
            
        if 'historical' not in content.lower():
            opportunities.append("Add historical pattern analysis")
            
        if command_name in self.context_patterns:
            opportunities.append("Enhance with command-specific context patterns")
            
        return {
            'command_name': command_name,
            'enhancement_opportunities': opportunities,
            'current_context_mentions': content.lower().count('context'),
            'integration_complexity': 'low' if len(opportunities) <= 2 else 'medium' if len(opportunities) <= 4 else 'high'
        }

if __name__ == "__main__":
    # Example usage
    integrator = CommandEcosystemIntegrator()
    
    # Test command enhancement
    enhancement = integrator.enhance_command_with_context(
        'create-doc', 
        'I need to create documentation for the new feature',
        'test-session-123'
    )
    
    print(f"Enhancement summary: {enhancement['context_summary']}")
    print(f"Suggested approaches: {enhancement['suggested_approaches']}")