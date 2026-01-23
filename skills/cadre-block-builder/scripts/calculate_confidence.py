#!/usr/bin/env python3
"""
Confidence Score Calculator
Scores block confidence (internal use only) based on risk factors and experience
"""

def calculate_confidence(
    risk_count=0,
    assumption_count=0,
    has_similar_past_work=False,
    team_familiar_with_tech=False,
    client_relationship='new',
    dependencies_confirmed=False
):
    """
    Calculate confidence score for a block
    
    Args:
        risk_count: Number of identified risks
        assumption_count: Number of unvalidated assumptions
        has_similar_past_work: Have we done similar projects before?
        team_familiar_with_tech: Is team experienced with the tech stack?
        client_relationship: 'new', 'existing', or 'long_term'
        dependencies_confirmed: Are external dependencies secured?
    
    Returns:
        dict with score, level, and explanation
    """
    # Start with baseline
    base_score = 85
    factors = []
    
    # Deductions for unknowns
    if risk_count > 0:
        deduction = risk_count * 5
        base_score -= deduction
        factors.append(f"- {deduction}% for {risk_count} identified risk(s)")
    
    if assumption_count > 0:
        deduction = assumption_count * 3
        base_score -= deduction
        factors.append(f"- {deduction}% for {assumption_count} unvalidated assumption(s)")
    
    if not dependencies_confirmed:
        base_score -= 5
        factors.append(f"- 5% for unconfirmed external dependencies")
    
    # Bonuses for experience
    if has_similar_past_work:
        base_score += 10
        factors.append(f"+ 10% for similar past project experience")
    
    if team_familiar_with_tech:
        base_score += 5
        factors.append(f"+ 5% for team familiarity with technology")
    
    # Client relationship bonus
    relationship_bonus = {
        'new': 0,
        'existing': 5,
        'long_term': 10
    }
    bonus = relationship_bonus.get(client_relationship, 0)
    if bonus > 0:
        base_score += bonus
        factors.append(f"+ {bonus}% for {client_relationship} client relationship")
    
    # Clamp score between 0-100
    final_score = max(0, min(100, base_score))
    
    # Determine confidence level
    if final_score >= 80:
        level = 'high'
        interpretation = 'Strong confidence in estimates'
    elif final_score >= 60:
        level = 'medium-high'
        interpretation = 'Good confidence with some uncertainties'
    elif final_score >= 40:
        level = 'medium'
        interpretation = 'Moderate confidence, several unknowns'
    elif final_score >= 20:
        level = 'low-medium'
        interpretation = 'Limited confidence, significant risks'
    else:
        level = 'low'
        interpretation = 'Very uncertain, requires more discovery'
    
    return {
        'score': final_score,
        'level': level,
        'interpretation': interpretation,
        'factors': factors,
        'recommendation': get_recommendation(final_score)
    }


def get_recommendation(score):
    """Provide recommendation based on confidence score"""
    if score >= 80:
        return "Proceed with current plan"
    elif score >= 60:
        return "Proceed but monitor flagged risks closely"
    elif score >= 40:
        return "Consider additional discovery sprint to reduce uncertainty"
    else:
        return "Recommend discovery phase before committing to timeline"


if __name__ == '__main__':
    # Example: Strong confidence scenario
    print("Example 1: Strong Confidence")
    result = calculate_confidence(
        risk_count=1,
        assumption_count=2,
        has_similar_past_work=True,
        team_familiar_with_tech=True,
        client_relationship='existing',
        dependencies_confirmed=True
    )
    print(f"  Score: {result['score']}% ({result['level']})")
    print(f"  {result['interpretation']}")
    print(f"  Factors:")
    for factor in result['factors']:
        print(f"    {factor}")
    print(f"  Recommendation: {result['recommendation']}\n")
    
    # Example: Low confidence scenario
    print("Example 2: Low Confidence")
    result = calculate_confidence(
        risk_count=5,
        assumption_count=4,
        has_similar_past_work=False,
        team_familiar_with_tech=False,
        client_relationship='new',
        dependencies_confirmed=False
    )
    print(f"  Score: {result['score']}% ({result['level']})")
    print(f"  {result['interpretation']}")
    print(f"  Factors:")
    for factor in result['factors']:
        print(f"    {factor}")
    print(f"  Recommendation: {result['recommendation']}")
