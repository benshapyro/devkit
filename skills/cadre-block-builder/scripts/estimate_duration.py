#!/usr/bin/env python3
"""
Duration Estimation Script
Calculates duration ranges based on activity cluster complexity
"""

# Duration ranges in weeks (min, max) for each complexity level
CLUSTER_DURATIONS = {
    'discovery': {
        'simple': (1, 2),
        'medium': (2, 4),
        'complex': (4, 8)
    },
    'process_design': {
        'simple': (1, 2),
        'medium': (2, 3),
        'complex': (3, 6)
    },
    'integration': {
        'simple': (2, 4),
        'medium': (4, 8),
        'complex': (8, 16)
    },
    'development': {
        'simple': (4, 6),
        'medium': (8, 12),
        'complex': (12, 24)
    },
    'automation': {
        'simple': (1, 3),
        'medium': (3, 6),
        'complex': (6, 12)
    },
    'ai_llm': {
        'simple': (3, 6),
        'medium': (6, 10),
        'complex': (10, 20)
    },
    'testing': {
        'simple': (1, 2),
        'medium': (2, 4),
        'complex': (4, 8)
    },
    'deployment': {
        'simple': (1, 2),
        'medium': (2, 4),
        'complex': (4, 8)
    },
    'training': {
        'simple': (1, 2),
        'medium': (2, 3),
        'complex': (3, 6)
    },
    'optimization': {
        'simple': (2, 4),
        'medium': (4, 8),
        'complex': (8, 12)
    }
}


def estimate_duration(clusters_with_complexity):
    """
    Calculate total duration from activity clusters with complexity ratings
    
    Args:
        clusters_with_complexity: dict like {'discovery': 'medium', 'integration': 'complex'}
    
    Returns:
        dict with total weeks range and breakdown
    """
    total_min = 0
    total_max = 0
    breakdown = {}
    
    for cluster, complexity in clusters_with_complexity.items():
        if cluster not in CLUSTER_DURATIONS:
            raise ValueError(f"Unknown cluster: {cluster}")
        if complexity not in CLUSTER_DURATIONS[cluster]:
            raise ValueError(f"Unknown complexity '{complexity}' for cluster '{cluster}'")
        
        min_weeks, max_weeks = CLUSTER_DURATIONS[cluster][complexity]
        total_min += min_weeks
        total_max += max_weeks
        breakdown[cluster] = f"{min_weeks}-{max_weeks} weeks"
    
    # Determine confidence level based on range spread
    range_spread = total_max - total_min
    if range_spread <= 4:
        confidence = 'high'
    elif range_spread <= 12:
        confidence = 'medium'
    else:
        confidence = 'low'
    
    return {
        'total_weeks': f"{total_min}-{total_max}",
        'total_months': f"{total_min/4:.1f}-{total_max/4:.1f}",
        'breakdown': breakdown,
        'confidence': confidence
    }


if __name__ == '__main__':
    # Example usage
    example_clusters = {
        'discovery': 'medium',
        'integration': 'complex',
        'testing': 'simple'
    }
    
    result = estimate_duration(example_clusters)
    print("Duration Estimate:")
    print(f"  Total: {result['total_weeks']} weeks ({result['total_months']} months)")
    print(f"  Confidence: {result['confidence']}")
    print("\n  Breakdown:")
    for cluster, duration in result['breakdown'].items():
        print(f"    {cluster}: {duration}")
