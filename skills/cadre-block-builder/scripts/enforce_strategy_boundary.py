#!/usr/bin/env python3
"""
Strategy Boundary Enforcement
Prevents mixing strategy and implementation in the same block
"""

# Strategy clusters = consulting without building
STRATEGY_CLUSTERS = {'discovery', 'process_design', 'training'}

# Implementation clusters = building/integrating/deploying
IMPLEMENTATION_CLUSTERS = {
    'integration', 
    'development', 
    'automation', 
    'ai_llm', 
    'testing', 
    'deployment', 
    'optimization'
}


class StrategyBoundaryViolation(Exception):
    """Raised when strategy and implementation clusters are mixed"""
    pass


def validate_boundary(block_clusters):
    """
    Validates that strategy and implementation clusters aren't mixed
    
    Args:
        block_clusters: list or set of cluster names
    
    Raises:
        StrategyBoundaryViolation if mixing detected
    
    Returns:
        dict with block_type and validation details
    """
    cluster_set = set(block_clusters)
    
    has_strategy = bool(cluster_set & STRATEGY_CLUSTERS)
    has_implementation = bool(cluster_set & IMPLEMENTATION_CLUSTERS)
    
    if has_strategy and has_implementation:
        strategy_found = cluster_set & STRATEGY_CLUSTERS
        implementation_found = cluster_set & IMPLEMENTATION_CLUSTERS
        
        raise StrategyBoundaryViolation(
            f"BOUNDARY VIOLATION: Cannot mix strategy and implementation in same block.\n\n"
            f"Strategy clusters detected: {', '.join(strategy_found)}\n"
            f"Implementation clusters detected: {', '.join(implementation_found)}\n\n"
            f"SOLUTION: Split into separate engagements:\n"
            f"  • Strategy Block: {', '.join(strategy_found)}\n"
            f"  • Implementation Block: {', '.join(implementation_found)}\n\n"
            f"WHY: Implementation requires separate discovery after strategy approval.\n"
            f"This protects both project quality and separate engagement revenue."
        )
    
    if has_strategy:
        block_type = 'strategy_only'
        message = "✓ Strategy-only engagement (consulting, no implementation)"
    elif has_implementation:
        block_type = 'implementation'
        message = "✓ Implementation engagement (building/integrating)"
    else:
        block_type = 'unknown'
        message = "⚠ No recognized clusters identified"
    
    return {
        'valid': True,
        'block_type': block_type,
        'message': message,
        'clusters': list(cluster_set)
    }


if __name__ == '__main__':
    # Test cases
    print("Test 1: Strategy only (VALID)")
    try:
        result = validate_boundary(['discovery', 'process_design'])
        print(f"  {result['message']}\n")
    except StrategyBoundaryViolation as e:
        print(f"  ERROR: {e}\n")
    
    print("Test 2: Implementation only (VALID)")
    try:
        result = validate_boundary(['integration', 'testing', 'deployment'])
        print(f"  {result['message']}\n")
    except StrategyBoundaryViolation as e:
        print(f"  ERROR: {e}\n")
    
    print("Test 3: Mixed strategy + implementation (INVALID)")
    try:
        result = validate_boundary(['discovery', 'process_design', 'integration', 'development'])
        print(f"  {result['message']}\n")
    except StrategyBoundaryViolation as e:
        print(f"  CAUGHT: {e}\n")
