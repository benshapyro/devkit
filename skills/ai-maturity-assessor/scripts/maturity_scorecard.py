#!/usr/bin/env python3
"""
AI Maturity Scorecard Generator

Calculates weighted maturity scores across four phases based on assessment responses.
Compares against industry benchmarks and generates detailed gap analysis.
"""

import json
import sys
from typing import Dict, List, Tuple
from dataclasses import dataclass
from pathlib import Path


@dataclass
class PhaseWeights:
    """Weight distribution for subsections within each phase"""
    phase1 = {"executive": 0.30, "data": 0.25, "governance": 0.25, "risk": 0.20}
    phase2 = {"literacy": 0.30, "champions": 0.25, "training": 0.25, "culture": 0.20}
    phase3 = {"intake": 0.25, "prioritization": 0.30, "backlog": 0.25, "reusability": 0.20}
    phase4 = {"teams": 0.20, "evaluation": 0.30, "production": 0.30, "improvement": 0.20}


# Question to subsection mapping
QUESTION_SUBSECTIONS = {
    # Phase 1
    "Q1": "executive", "Q2": "data", "Q3": "governance", "Q4": "risk",
    # Phase 2
    "Q5": "literacy", "Q6": "champions", "Q7": "training", "Q8": "culture",
    # Phase 3
    "Q9": "intake", "Q10": "prioritization", "Q11": "backlog", "Q12": "reusability",
    # Phase 4
    "Q13": "teams", "Q14": "evaluation", "Q15": "production", "Q16": "improvement"
}


def calculate_subsection_score(responses: Dict, subsection_questions: List[str]) -> Tuple[float, List[int]]:
    """Calculate average score for a subsection based on question responses"""
    scores = []
    for q_id in subsection_questions:
        if q_id in responses:
            scores.append(responses[q_id]["score"])
    
    return (sum(scores) / len(scores) * 20) if scores else 0.0, scores


def calculate_phase_score(responses: Dict, phase_num: int, weights: Dict) -> Dict:
    """Calculate weighted phase score with subsection breakdown"""
    phase_prefix = f"Q{(phase_num-1)*4 + 1}"
    
    subsection_scores = {}
    subsection_raw_scores = {}
    
    for subsection, weight in weights.items():
        # Find questions for this subsection
        questions = [q_id for q_id, sub in QUESTION_SUBSECTIONS.items() 
                    if sub == subsection and q_id.startswith(f"Q{phase_num*4-3}") or 
                       q_id.startswith(f"Q{phase_num*4-2}") or
                       q_id.startswith(f"Q{phase_num*4-1}") or
                       q_id.startswith(f"Q{phase_num*4}")]
        
        score, raw = calculate_subsection_score(responses, questions)
        subsection_scores[subsection] = score
        subsection_raw_scores[subsection] = raw
    
    # Calculate weighted phase score
    phase_score = sum(score * weights[sub] for sub, score in subsection_scores.items())
    
    return {
        "overall": round(phase_score, 1),
        "subsections": subsection_scores,
        "raw_scores": subsection_raw_scores
    }


def get_maturity_level(score: float) -> str:
    """Convert numeric score to maturity level"""
    if score >= 91: return "Optimizing"
    if score >= 76: return "Managed"
    if score >= 51: return "Defined"
    if score >= 26: return "Developing"
    return "Initial"


def get_benchmark_comparison(score: float, org_size: str, phase: int) -> Dict:
    """Compare score against benchmark ranges for organization size"""
    benchmarks = {
        "small": {
            1: (35, 45), 2: (40, 50), 3: (30, 40), 4: (25, 35)
        },
        "mid": {
            1: (45, 55), 2: (45, 55), 3: (35, 45), 4: (30, 40)
        },
        "large": {
            1: (55, 65), 2: (50, 60), 3: (40, 50), 4: (35, 45)
        },
        "enterprise": {
            1: (60, 70), 2: (55, 65), 3: (45, 55), 4: (40, 50)
        }
    }
    
    size_key = org_size.lower()
    if size_key not in benchmarks:
        size_key = "mid"
    
    low, high = benchmarks[size_key][phase]
    
    if score < low:
        position = "Below peer average"
        percentile = "20th-40th percentile"
    elif score > high:
        position = "Above peer average"
        percentile = "60th-80th percentile"
    else:
        position = "Within peer range"
        percentile = "40th-60th percentile"
    
    return {
        "position": position,
        "percentile": percentile,
        "peer_range": f"{low}-{high}",
        "gap_to_average": round(score - ((low + high) / 2), 1)
    }


def identify_gaps(phase_data: Dict, phase_name: str) -> List[Dict]:
    """Identify specific capability gaps based on subsection scores"""
    gaps = []
    
    for subsection, score in phase_data["subsections"].items():
        if score < 50:  # Below "Defined" level
            severity = "Critical" if score < 26 else "Significant" if score < 40 else "Moderate"
            gaps.append({
                "phase": phase_name,
                "subsection": subsection,
                "score": score,
                "severity": severity,
                "recommendation": get_gap_recommendation(phase_name, subsection, score)
            })
    
    return sorted(gaps, key=lambda x: x["score"])


def get_gap_recommendation(phase: str, subsection: str, score: float) -> str:
    """Generate specific recommendation for a gap"""
    recommendations = {
        ("Phase 1", "executive"): "Secure dedicated executive sponsor with budget authority and establish monthly steering committee",
        ("Phase 1", "data"): "Conduct data inventory, implement classification framework, and define AI-ready data access policies",
        ("Phase 1", "governance"): "Establish AI Center of Excellence with clear decision rights and tiered approval process",
        ("Phase 1", "risk"): "Adopt responsible AI principles and implement systematic risk assessment for all use cases",
        
        ("Phase 2", "literacy"): "Launch role-specific AI training program starting with Product and Engineering teams",
        ("Phase 2", "champions"): "Identify 10-15 champions across departments and establish quarterly showcase rituals",
        ("Phase 2", "training"): "Develop structured curriculum with hands-on practice and clear skill progression paths",
        ("Phase 2", "culture"): "Create innovation time policy and celebrate early wins through leadership communication",
        
        ("Phase 3", "intake"): "Design simple use case submission process with templates and 5-day review SLA",
        ("Phase 3", "prioritization"): "Implement multi-dimensional scoring rubric (impact/effort/risk/reuse) with cross-functional review",
        ("Phase 3", "backlog"): "Establish visible backlog with quarterly prioritization reviews and resource allocation planning",
        ("Phase 3", "reusability"): "Create component library and implement reuse-first policy with discovery tools",
        
        ("Phase 4", "teams"): "Form 2-3 cross-functional teams with dedicated business SMEs and executive sponsors",
        ("Phase 4", "evaluation"): "Implement gated evaluation checkpoints (MVP/Pilot/Production) with predefined success criteria",
        ("Phase 4", "production"): "Build CI/CD pipeline for AI deployments with automated monitoring and rollback capability",
        ("Phase 4", "improvement"): "Establish retrospective cadence and systematic capture of learnings in knowledge base"
    }
    
    return recommendations.get((phase, subsection), f"Strengthen {subsection} capabilities through focused investment")


def generate_scorecard(responses: Dict, org_context: Dict) -> Dict:
    """Generate complete maturity scorecard with scores, benchmarks, and gaps"""
    
    weights = PhaseWeights()
    
    # Calculate scores for each phase
    phase_scores = {
        "Phase 1: Foundations": calculate_phase_score(responses, 1, weights.phase1),
        "Phase 2: AI Fluency": calculate_phase_score(responses, 2, weights.phase2),
        "Phase 3: Scope & Prioritize": calculate_phase_score(responses, 3, weights.phase3),
        "Phase 4: Build & Scale": calculate_phase_score(responses, 4, weights.phase4)
    }
    
    # Calculate overall score
    overall_score = sum(data["overall"] for data in phase_scores.values()) / 4
    
    # Get organization context
    org_size = org_context.get("size", "mid")
    industry = org_context.get("industry", "general")
    
    # Add maturity levels and benchmarks
    for i, (phase_name, phase_data) in enumerate(phase_scores.items(), 1):
        phase_data["maturity_level"] = get_maturity_level(phase_data["overall"])
        phase_data["benchmark"] = get_benchmark_comparison(phase_data["overall"], org_size, i)
    
    # Identify gaps across all phases
    all_gaps = []
    for phase_name, phase_data in phase_scores.items():
        all_gaps.extend(identify_gaps(phase_data, phase_name))
    
    # Generate summary insights
    insights = generate_insights(phase_scores, overall_score, all_gaps)
    
    return {
        "overall_score": round(overall_score, 1),
        "overall_maturity_level": get_maturity_level(overall_score),
        "organization": org_context,
        "phase_scores": phase_scores,
        "capability_gaps": all_gaps,
        "insights": insights,
        "timestamp": org_context.get("timestamp", "")
    }


def generate_insights(phase_scores: Dict, overall_score: float, gaps: List[Dict]) -> Dict:
    """Generate strategic insights from the assessment"""
    
    scores = [data["overall"] for data in phase_scores.values()]
    variance = max(scores) - min(scores)
    
    # Identify patterns
    pattern = "balanced"
    if variance > 25:
        pattern = "uneven"
        if scores[0] > scores[2] and scores[1] > scores[2]:
            pattern = "stuck_in_pilots"  # High P1/P2, low P3/P4
        elif scores[3] > scores[1]:
            pattern = "engineering_only"  # High P4, low P2
    
    # Calculate readiness for next stage
    if overall_score < 40:
        next_stage = "Foundation Building (12-18 months)"
        focus = "Executive alignment, governance, and data infrastructure"
    elif overall_score < 55:
        next_stage = "Systematic Scaling (9-15 months)"
        focus = "Fluency expansion, prioritization frameworks, first production deployments"
    elif overall_score < 70:
        next_stage = "Enterprise Deployment (6-12 months)"
        focus = "Production scaling, continuous improvement, business value capture"
    else:
        next_stage = "Optimization (Ongoing)"
        focus = "Innovation acceleration, competitive differentiation, sustained excellence"
    
    return {
        "maturity_pattern": pattern,
        "score_variance": round(variance, 1),
        "critical_gaps_count": len([g for g in gaps if g["severity"] == "Critical"]),
        "next_stage": next_stage,
        "recommended_focus": focus,
        "estimated_investment": estimate_investment(overall_score, pattern),
        "risk_level": "High" if len([g for g in gaps if g["severity"] == "Critical"]) > 5 else "Moderate" if gaps else "Low"
    }


def estimate_investment(score: float, pattern: str) -> str:
    """Estimate investment range needed for transformation"""
    if score < 35:
        return "$500K-$1M over 18 months (comprehensive foundation building)"
    elif score < 50:
        return "$300K-$700K over 12 months (systematic capability development)"
    elif score < 65:
        return "$200K-$500K over 9 months (targeted scaling initiatives)"
    else:
        return "$100K-$300K over 6 months (optimization and innovation)"


def main():
    """Main execution function"""
    if len(sys.argv) < 3:
        print("Usage: python maturity_scorecard.py --responses <responses.json> --org-context <context.json>")
        sys.exit(1)
    
    # Parse command line arguments
    responses_file = None
    context_file = None
    
    for i, arg in enumerate(sys.argv):
        if arg == "--responses" and i + 1 < len(sys.argv):
            responses_file = sys.argv[i + 1]
        elif arg == "--org-context" and i + 1 < len(sys.argv):
            context_file = sys.argv[i + 1]
    
    if not responses_file or not context_file:
        print("Error: Both --responses and --org-context are required")
        sys.exit(1)
    
    # Load input files
    try:
        with open(responses_file, 'r') as f:
            responses = json.load(f)
        with open(context_file, 'r') as f:
            org_context = json.load(f)
    except FileNotFoundError as e:
        print(f"Error: Could not find file - {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON - {e}")
        sys.exit(1)
    
    # Generate scorecard
    scorecard = generate_scorecard(responses, org_context)
    
    # Output results
    output_file = "maturity_scores.json"
    with open(output_file, 'w') as f:
        json.dump(scorecard, f, indent=2)
    
    print(f"✅ Scorecard generated successfully: {output_file}")
    print(f"\nOverall Score: {scorecard['overall_score']}/100")
    print(f"Maturity Level: {scorecard['overall_maturity_level']}")
    print(f"\nPhase Scores:")
    for phase, data in scorecard['phase_scores'].items():
        print(f"  {phase}: {data['overall']}/100 ({data['maturity_level']})")
    print(f"\nCritical Gaps: {scorecard['insights']['critical_gaps_count']}")
    print(f"Next Stage: {scorecard['insights']['next_stage']}")


if __name__ == "__main__":
    main()
