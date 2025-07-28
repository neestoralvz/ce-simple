# categorize-feedback

## Purpose

Automatically categorize user feedback using Spanish terminology (logros, desafios, errores, obstaculos, aprendizajes) with embedded classification algorithms and action recommendations.

## Principles

- **Automated Classification**: 5-category Spanish terminology system with pattern recognition
- **Embedded Intelligence**: All classification algorithms embedded inline for sub-agent compatibility
- **Action Generation**: Automatic action recommendations based on category assignment
- **Sacred Space Integration**: Preserves user authenticity while enabling systematic analysis

## Execution Process

### Phase 1: Feedback Text Processing
Mark "Feedback Text Processing and Preprocessing" as in_progress using TodoWrite

Process raw feedback text for classification:

```python
# Embedded Text Preprocessing Algorithm
def preprocess_feedback(feedback_text):
    import re
    
    # Normalize case and remove punctuation
    text = feedback_text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    
    # Tokenize and remove stop words
    stop_words = ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by']
    tokens = [word for word in text.split() if word not in stop_words and len(word) > 2]
    
    return tokens, text
```

Extract key features:
- Word frequency analysis
- N-gram pattern identification (1-3 words)
- Sentiment indicators and emotional tone
- Temporal indicators (past/present/future tense)
- Negation detection and context analysis

### Phase 2: Category Classification Analysis
Mark "Multi-Category Classification with Confidence Scoring" as in_progress using TodoWrite

**MANDATORY**: Deploy Task Tool with specialized classification agents for parallel analysis across all five categories:

Apply embedded classification algorithms for all five categories:

```python
# Embedded Classification Algorithm
def classify_feedback(tokens, full_text):
    category_scores = {}
    
    # logros (Achievements) - Pattern Keywords
    logros_patterns = {
        'direct': ['completed', 'successful', 'achieved', 'accomplished', 'delivered', 'finished', 'done'],
        'comparative': ['improved', 'optimized', 'enhanced', 'increased', 'better', 'faster', 'more'],
        'quantitative': ['100%', 'deployed', 'live', 'working', 'functional', 'operational'],
        'emotional': ['satisfied', 'pleased', 'happy', 'excited', 'proud', 'great', 'excellent']
    }
    
    # desafios (Challenges) - Pattern Keywords  
    desafios_patterns = {
        'opportunity': ['opportunity', 'potential', 'could', 'might', 'possible', 'consider'],
        'growth': ['challenge', 'learn', 'develop', 'improve', 'enhance', 'upgrade'],
        'future': ['next', 'future', 'upcoming', 'planned', 'roadmap', 'vision'],
        'conditional': ['if', 'when', 'should', 'would', 'recommend', 'suggest']
    }
    
    # errores (Errors) - Pattern Keywords
    errores_patterns = {
        'direct': ['error', 'bug', 'mistake', 'wrong', 'incorrect', 'failed', 'failure'],
        'negative': ['broken', 'not working', 'doesnt', 'cant', 'unable', 'impossible'],
        'problems': ['issue', 'problem', 'trouble', 'difficulty', 'fault', 'malfunction'],
        'quality': ['regression', 'degradation', 'worse', 'slower', 'unstable', 'crash']
    }
    
    # obstaculos (Obstacles) - Pattern Keywords
    obstaculos_patterns = {
        'blocking': ['blocked', 'stuck', 'cant', 'unable', 'impossible', 'prevented'],
        'limitations': ['limited', 'constraint', 'restriction', 'bottleneck', 'capacity'],
        'dependencies': ['waiting', 'depends', 'requires', 'needs', 'blocked by', 'external'],
        'resources': ['lack', 'missing', 'insufficient', 'shortage', 'unavailable', 'budget']
    }
    
    # aprendizajes (Learnings) - Pattern Keywords
    aprendizajes_patterns = {
        'discovery': ['learned', 'discovered', 'realized', 'found', 'noticed', 'observed'],
        'understanding': ['understand', 'insight', 'pattern', 'principle', 'concept', 'theory'],
        'knowledge': ['know', 'aware', 'recognize', 'identify', 'analyze', 'study'],
        'wisdom': ['best practice', 'lesson', 'experience', 'methodology', 'approach']
    }
    
    # Calculate scores for each category
    all_patterns = {
        'logros': logros_patterns,
        'desafios': desafios_patterns, 
        'errores': errores_patterns,
        'obstaculos': obstaculos_patterns,
        'aprendizajes': aprendizajes_patterns
    }
    
    for category, patterns in all_patterns.items():
        score = 0.0
        for pattern_type, keywords in patterns.items():
            for keyword in keywords:
                if keyword in full_text:
                    score += 1.0 * (1.2 if pattern_type == 'direct' else 1.0)
        
        # Normalize by text length and apply confidence threshold
        confidence = min(score / max(len(tokens), 1), 1.0)
        category_scores[category] = confidence
    
    return category_scores
```

Perform multi-category analysis:
- Primary category assignment (highest confidence >0.6)
- Secondary category identification (additional scores >0.6)
- Confidence assessment and manual review flagging
- Cross-category relationship detection using correlation patterns

### Phase 3: Priority Scoring and Action Generation
Mark "Priority Assessment and Action Recommendation Generation" as in_progress using TodoWrite

Apply embedded priority scoring algorithms:

```python
# Embedded Priority Scoring Algorithm
def calculate_priority(category_scores, feedback_metadata):
    base_weights = {
        'errores': 0.90,     # Critical - immediate attention
        'obstaculos': 0.80,  # High - blocking progress  
        'desafios': 0.60,    # Medium - growth opportunities
        'aprendizajes': 0.55, # Medium - strategic value
        'logros': 0.40       # Low - positive reinforcement
    }
    
    primary_category = max(category_scores.items(), key=lambda x: x[1])
    base_priority = base_weights.get(primary_category[0], 0.5)
    
    # Apply dynamic modifiers
    frequency_multiplier = min(feedback_metadata.get('frequency', 1) * 0.2 + 1.0, 2.0)
    impact_multiplier = feedback_metadata.get('impact_scope', 1.0)  # 0.8-2.5 range
    temporal_multiplier = feedback_metadata.get('urgency_factor', 1.0)  # 1.0-3.0 range
    
    final_priority = base_priority * frequency_multiplier * impact_multiplier * temporal_multiplier
    return min(final_priority, 1.0)

# Embedded Action Recommendation Algorithm  
def generate_actions(primary_category, priority_score, feedback_content):
    action_templates = {
        'logros': [
            'Document success patterns for replication',
            'Share achievement impact with stakeholders', 
            'Analyze success factors for systematic improvement',
            'Create knowledge documentation for replicable patterns',
            'Schedule achievement recognition and team communication'
        ],
        'desafios': [
            'Create improvement roadmap with specific milestones',
            'Allocate appropriate resources and team members',
            'Design learning initiatives for skill development',
            'Schedule focused challenge resolution sessions',
            'Establish measurable success metrics and tracking'
        ],
        'errores': [
            'Immediate error resolution and system stabilization',
            'Conduct root cause analysis to prevent recurrence', 
            'Enhance quality assurance and detection processes',
            'Communicate status updates to affected users',
            'Implement prevention measures in development workflow'
        ],
        'obstaculos': [
            'Reallocate resources to remove blocking obstacles',
            'Optimize processes to minimize future obstacles',
            'Address external dependencies causing blockages',
            'Plan system upgrades removing technical limitations', 
            'Develop strategic constraint resolution approaches'
        ],
        'aprendizajes': [
            'Document insights for organizational learning',
            'Develop best practices from learning patterns',
            'Create training programs sharing insights across teams',
            'Refine methodologies incorporating new insights',
            'Schedule knowledge sharing sessions and documentation'
        ]
    }
    
    category_actions = action_templates.get(primary_category, [])
    
    # Select top 3 actions based on priority and context
    if priority_score > 0.8:
        return category_actions[:3]  # High priority - focus on critical actions
    elif priority_score > 0.6:
        return category_actions[:2]  # Medium priority - key actions
    else:
        return category_actions[:1]  # Low priority - single focused action
```

Generate comprehensive feedback analysis:
- Category assignment with confidence scores
- Priority calculation with urgency indicators
- Automated action recommendations with timelines
- Integration points with Sacred User Space preservation

### Phase 4: Results Integration and Output
Mark "Results Generation and Sacred Space Integration" as in_progress using TodoWrite

Create structured feedback analysis output:

```json
{
  "feedback_analysis": {
    "original_feedback": "[Preserved user feedback text]",
    "timestamp": "[ISO timestamp]",
    "classification": {
      "primary_category": "errores",
      "confidence": 0.85,
      "secondary_categories": ["obstaculos"],
      "all_scores": {
        "logros": 0.1,
        "desafios": 0.3, 
        "errores": 0.85,
        "obstaculos": 0.65,
        "aprendizajes": 0.2
      }
    },
    "priority_assessment": {
      "final_priority": 0.92,
      "urgency_level": "Critical",
      "estimated_timeline": "Immediate (0-24 hours)",
      "impact_scope": "System-wide"
    },
    "recommended_actions": [
      "Immediate error resolution and system stabilization",
      "Conduct root cause analysis to prevent recurrence",
      "Enhance quality assurance and detection processes"
    ],
    "sacred_space_preservation": {
      "user_voice_maintained": true,
      "context_preserved": true,
      "authenticity_verified": true
    }
  }
}
```

Complete categorization workflow:
- Save analysis to user-input/context/ with timestamp
- Generate action items in appropriate tracking system
- Update correlation analysis database with category relationships
- Trigger priority-based notification and escalation protocols

Mark all TodoWrite tasks as completed

---

## Implementation Standards

**Embedded Intelligence**: All classification algorithms included inline for sub-agent execution
**Sacred Space Compliance**: Preserves user authenticity while enabling systematic analysis  
**Multi-Category Support**: Handles complex feedback spanning multiple classification categories
**Action Integration**: Automatic generation of category-specific actionable recommendations

**Authority References**:
- [Feedback Categorization Framework](../docs/core/03-com-communication/com-feedback-categorization-framework.md) - Classification system
- [Priority Scoring](../docs/core/05-per-performance/per-feedback-priority-scoring.md) - Priority algorithms
- [Action Recommendations](../docs/core/04-pro-protocols/pro-feedback-action-recommendations.md) - Action generation