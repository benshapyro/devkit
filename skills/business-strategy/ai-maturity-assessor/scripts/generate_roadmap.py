#!/usr/bin/env python3
"""
AI Transformation Roadmap Generator

Creates detailed 12-18 month transformation roadmaps based on maturity scores.
Sequences initiatives, estimates investments, and projects ROI timeline.
"""

import json
import sys
from datetime import datetime, timedelta
from typing import Dict, List
from dataclasses import dataclass


@dataclass
class Initiative:
    """Represents a transformation initiative"""
    name: str
    phase: str
    duration_weeks: int
    investment_low: int
    investment_high: int
    dependencies: List[str]
    quick_win: bool
    roi_timeline_months: int
    expected_impact: str


def generate_initiatives(scores: Dict, context: Dict) -> List[Initiative]:
    """Generate prioritized initiatives based on maturity gaps"""
    
    initiatives = []
    phase_scores = scores["phase_scores"]
    org_size = context.get("size", "mid")
    
    # Phase 1: Foundation initiatives
    if phase_scores["Phase 1: Foundations"]["overall"] < 50:
        if phase_scores["Phase 1: Foundations"]["subsections"].get("executive", 0) < 50:
            initiatives.append(Initiative(
                name="Establish Executive Sponsorship & Steering Committee",
                phase="Phase 1",
                duration_weeks=6,
                investment_low=25000,
                investment_high=50000,
                dependencies=[],
                quick_win=True,
                roi_timeline_months=0,  # Enabler
                expected_impact="Enable decision-making and resource allocation"
            ))
        
        if phase_scores["Phase 1: Foundations"]["subsections"].get("governance", 0) < 50:
            initiatives.append(Initiative(
                name="Design & Launch AI Center of Excellence",
                phase="Phase 1",
                duration_weeks=8,
                investment_low=40000,
                investment_high=80000,
                dependencies=["Establish Executive Sponsorship & Steering Committee"],
                quick_win=False,
                roi_timeline_months=0,  # Enabler
                expected_impact="Systematic coordination and governance"
            ))
        
        if phase_scores["Phase 1: Foundations"]["subsections"].get("data", 0) < 50:
            initiatives.append(Initiative(
                name="Data Inventory & AI-Ready Data Framework",
                phase="Phase 1",
                duration_weeks=10,
                investment_low=50000,
                investment_high=120000,
                dependencies=[],
                quick_win=False,
                roi_timeline_months=0,  # Enabler
                expected_impact="Enable data access for AI development"
            ))
        
        if phase_scores["Phase 1: Foundations"]["subsections"].get("risk", 0) < 50:
            initiatives.append(Initiative(
                name="Responsible AI Framework & Risk Assessment Process",
                phase="Phase 1",
                duration_weeks=6,
                investment_low=30000,
                investment_high=60000,
                dependencies=["Design & Launch AI Center of Excellence"],
                quick_win=False,
                roi_timeline_months=0,  # Enabler
                expected_impact="Risk mitigation and regulatory compliance"
            ))
    
    # Phase 2: Fluency initiatives
    if phase_scores["Phase 2: AI Fluency"]["overall"] < 50:
        if phase_scores["Phase 2: AI Fluency"]["subsections"].get("literacy", 0) < 50:
            initiatives.append(Initiative(
                name="Enterprise-Wide AI Literacy Program (Wave 1: Priority Teams)",
                phase="Phase 2",
                duration_weeks=12,
                investment_low=80000,
                investment_high=150000,
                dependencies=["Establish Executive Sponsorship & Steering Committee"],
                quick_win=True,
                roi_timeline_months=3,
                expected_impact="15-25% productivity improvement in trained teams"
            ))
        
        if phase_scores["Phase 2: AI Fluency"]["subsections"].get("champions", 0) < 50:
            initiatives.append(Initiative(
                name="Champion Network & Knowledge Sharing Infrastructure",
                phase="Phase 2",
                duration_weeks=8,
                investment_low=30000,
                investment_high=60000,
                dependencies=["Enterprise-Wide AI Literacy Program (Wave 1: Priority Teams)"],
                quick_win=True,
                roi_timeline_months=2,
                expected_impact="Accelerated learning and use case discovery"
            ))
        
        if phase_scores["Phase 2: AI Fluency"]["subsections"].get("culture", 0) < 50:
            initiatives.append(Initiative(
                name="Innovation Time Policy & Experimentation Framework",
                phase="Phase 2",
                duration_weeks=4,
                investment_low=15000,
                investment_high=30000,
                dependencies=["Champion Network & Knowledge Sharing Infrastructure"],
                quick_win=True,
                roi_timeline_months=2,
                expected_impact="100+ use case submissions from distributed innovation"
            ))
    
    # Phase 3: Prioritization initiatives
    if phase_scores["Phase 3: Scope & Prioritize"]["overall"] < 50:
        if phase_scores["Phase 3: Scope & Prioritize"]["subsections"].get("intake", 0) < 50:
            initiatives.append(Initiative(
                name="Use Case Intake & Evaluation Process Design",
                phase="Phase 3",
                duration_weeks=6,
                investment_low=40000,
                investment_high=70000,
                dependencies=["Design & Launch AI Center of Excellence"],
                quick_win=True,
                roi_timeline_months=1,
                expected_impact="Systematic capture and evaluation of opportunities"
            ))
        
        if phase_scores["Phase 3: Scope & Prioritize"]["subsections"].get("prioritization", 0) < 50:
            initiatives.append(Initiative(
                name="Discovery Sessions & Initial Backlog Development",
                phase="Phase 3",
                duration_weeks=8,
                investment_low=60000,
                investment_high=100000,
                dependencies=["Use Case Intake & Evaluation Process Design", "Champion Network & Knowledge Sharing Infrastructure"],
                quick_win=False,
                roi_timeline_months=2,
                expected_impact="Prioritized portfolio of 30-50 validated use cases"
            ))
        
        if phase_scores["Phase 3: Scope & Prioritize"]["subsections"].get("reusability", 0) < 50:
            initiatives.append(Initiative(
                name="Component Library & Reusability Framework",
                phase="Phase 3",
                duration_weeks=6,
                investment_low=40000,
                investment_high=80000,
                dependencies=["Discovery Sessions & Initial Backlog Development"],
                quick_win=False,
                roi_timeline_months=4,
                expected_impact="30-50% faster delivery through reuse"
            ))
    
    # Phase 4: Production initiatives
    if phase_scores["Phase 4: Build & Scale"]["overall"] < 50:
        if phase_scores["Phase 4: Build & Scale"]["subsections"].get("teams", 0) < 50:
            initiatives.append(Initiative(
                name="Form Cross-Functional AI Development Teams (2-3 teams)",
                phase="Phase 4",
                duration_weeks=4,
                investment_low=50000,
                investment_high=100000,
                dependencies=["Discovery Sessions & Initial Backlog Development"],
                quick_win=False,
                roi_timeline_months=1,
                expected_impact="Dedicated capacity for systematic delivery"
            ))
        
        if phase_scores["Phase 4: Build & Scale"]["subsections"].get("evaluation", 0) < 50:
            initiatives.append(Initiative(
                name="Evaluation Framework & Gated Deployment Process",
                phase="Phase 4",
                duration_weeks=6,
                investment_low=40000,
                investment_high=70000,
                dependencies=["Responsible AI Framework & Risk Assessment Process"],
                quick_win=False,
                roi_timeline_months=2,
                expected_impact="Reduced failure rate and production quality"
            ))
        
        if phase_scores["Phase 4: Build & Scale"]["subsections"].get("production", 0) < 50:
            initiatives.append(Initiative(
                name="First Wave Production Deployments (3-5 use cases)",
                phase="Phase 4",
                duration_weeks=16,
                investment_low=120000,
                investment_high=250000,
                dependencies=["Form Cross-Functional AI Development Teams (2-3 teams)", "Evaluation Framework & Gated Deployment Process", "Data Inventory & AI-Ready Data Framework"],
                quick_win=False,
                roi_timeline_months=6,
                expected_impact="Measurable business value and reference cases"
            ))
        
        if phase_scores["Phase 4: Build & Scale"]["subsections"].get("improvement", 0) < 50:
            initiatives.append(Initiative(
                name="Continuous Improvement & Learning Capture System",
                phase="Phase 4",
                duration_weeks=4,
                investment_low=20000,
                investment_high=40000,
                dependencies=["First Wave Production Deployments (3-5 use cases)"],
                quick_win=True,
                roi_timeline_months=2,
                expected_impact="Accelerated learning and systematic capability building"
            ))
    
    return initiatives


def sequence_initiatives(initiatives: List[Initiative]) -> List[Dict]:
    """Sequence initiatives based on dependencies and quick wins"""
    
    sequenced = []
    completed = set()
    current_week = 0
    
    # First, schedule quick wins without dependencies
    quick_wins = [i for i in initiatives if i.quick_win and not i.dependencies]
    for init in quick_wins:
        sequenced.append({
            "initiative": init,
            "start_week": current_week,
            "end_week": current_week + init.duration_weeks,
            "parallel_group": 1
        })
        completed.add(init.name)
        current_week = max(current_week, 4)  # Space out quick wins
    
    # Then schedule remaining initiatives in dependency order
    remaining = [i for i in initiatives if i.name not in completed]
    max_iterations = len(remaining) * 2  # Prevent infinite loops
    iteration = 0
    
    while remaining and iteration < max_iterations:
        iteration += 1
        scheduled_this_round = []
        
        for init in remaining:
            # Check if all dependencies are complete
            if all(dep in completed for dep in init.dependencies):
                # Find the latest end time of dependencies
                dep_end_time = 0
                for dep_name in init.dependencies:
                    for s in sequenced:
                        if s["initiative"].name == dep_name:
                            dep_end_time = max(dep_end_time, s["end_week"])
                
                start_time = max(current_week, dep_end_time)
                sequenced.append({
                    "initiative": init,
                    "start_week": start_time,
                    "end_week": start_time + init.duration_weeks,
                    "parallel_group": len([s for s in sequenced if s["start_week"] == start_time]) + 1
                })
                completed.add(init.name)
                scheduled_this_round.append(init)
        
        # Remove scheduled initiatives from remaining
        remaining = [i for i in remaining if i not in scheduled_this_round]
        
        # Advance time if we scheduled something
        if scheduled_this_round:
            current_week = max(s["end_week"] for s in sequenced if s["initiative"] in scheduled_this_round)
    
    return sorted(sequenced, key=lambda x: (x["start_week"], x["parallel_group"]))


def calculate_investments(sequenced: List[Dict]) -> Dict:
    """Calculate investment schedule and totals"""
    
    total_low = sum(item["initiative"].investment_low for item in sequenced)
    total_high = sum(item["initiative"].investment_high for item in sequenced)
    
    # Group by quarter
    quarterly = {}
    for item in sequenced:
        start_quarter = item["start_week"] // 12 + 1
        end_quarter = item["end_week"] // 12 + 1
        
        for q in range(start_quarter, end_quarter + 1):
            if q not in quarterly:
                quarterly[q] = {"low": 0, "high": 0, "initiatives": []}
            
            # Distribute investment across quarters proportionally
            quarters_span = end_quarter - start_quarter + 1
            quarterly[q]["low"] += item["initiative"].investment_low // quarters_span
            quarterly[q]["high"] += item["initiative"].investment_high // quarters_span
            quarterly[q]["initiatives"].append(item["initiative"].name)
    
    return {
        "total_low": total_low,
        "total_high": total_high,
        "quarterly_breakdown": quarterly
    }


def project_roi_timeline(sequenced: List[Dict], context: Dict) -> List[Dict]:
    """Project ROI timeline based on initiative impacts"""
    
    roi_milestones = []
    start_date = datetime.now()
    
    for item in sequenced:
        init = item["initiative"]
        if init.roi_timeline_months > 0:  # Skip enablers
            roi_date = start_date + timedelta(weeks=item["end_week"]) + timedelta(days=init.roi_timeline_months * 30)
            roi_milestones.append({
                "initiative": init.name,
                "expected_value_date": roi_date.strftime("%Y-%m-%d"),
                "months_from_start": (item["end_week"] // 4) + init.roi_timeline_months,
                "impact": init.expected_impact,
                "cumulative": len([m for m in roi_milestones if m["months_from_start"] <= ((item["end_week"] // 4) + init.roi_timeline_months)]) + 1
            })
    
    return sorted(roi_milestones, key=lambda x: x["months_from_start"])


def generate_milestones(sequenced: List[Dict]) -> List[Dict]:
    """Generate key milestones and decision gates"""
    
    milestones = []
    start_date = datetime.now()
    
    # Foundation milestone
    phase1_end = max(item["end_week"] for item in sequenced if item["initiative"].phase == "Phase 1")
    if phase1_end > 0:
        milestones.append({
            "name": "Foundation Complete",
            "date": (start_date + timedelta(weeks=phase1_end)).strftime("%Y-%m-%d"),
            "week": phase1_end,
            "type": "gate",
            "criteria": "Executive alignment secured, governance established, data access policies defined"
        })
    
    # Fluency milestone
    phase2_items = [item for item in sequenced if item["initiative"].phase == "Phase 2"]
    if phase2_items:
        phase2_end = max(item["end_week"] for item in phase2_items)
        milestones.append({
            "name": "Organization AI-Ready",
            "date": (start_date + timedelta(weeks=phase2_end)).strftime("%Y-%m-%d"),
            "week": phase2_end,
            "type": "gate",
            "criteria": "50%+ workforce trained, champion network active, 100+ use cases identified"
        })
    
    # First production
    production_items = [item for item in sequenced if "Production Deployment" in item["initiative"].name]
    if production_items:
        first_prod = production_items[0]["end_week"]
        milestones.append({
            "name": "First Production Deployments",
            "date": (start_date + timedelta(weeks=first_prod)).strftime("%Y-%m-%d"),
            "week": first_prod,
            "type": "milestone",
            "criteria": "3-5 use cases in production, measurable business value, reference cases established"
        })
    
    # Transformation complete
    final_week = max(item["end_week"] for item in sequenced)
    milestones.append({
        "name": "Transformation Phase Complete",
        "date": (start_date + timedelta(weeks=final_week)).strftime("%Y-%m-%d"),
        "week": final_week,
        "type": "gate",
        "criteria": "Systematic delivery capability, continuous improvement cycle, measured business impact"
    })
    
    return sorted(milestones, key=lambda x: x["week"])


def generate_roadmap(scores: Dict, context: Dict) -> Dict:
    """Generate complete transformation roadmap"""
    
    # Generate and sequence initiatives
    initiatives = generate_initiatives(scores, context)
    sequenced = sequence_initiatives(initiatives)
    
    # Calculate investments
    investments = calculate_investments(sequenced)
    
    # Project ROI
    roi_timeline = project_roi_timeline(sequenced, context)
    
    # Generate milestones
    milestones = generate_milestones(sequenced)
    
    # Calculate duration
    total_weeks = max(item["end_week"] for item in sequenced)
    total_months = (total_weeks + 3) // 4  # Round up to nearest month
    
    return {
        "duration_months": total_months,
        "duration_weeks": total_weeks,
        "start_date": datetime.now().strftime("%Y-%m-%d"),
        "target_completion": (datetime.now() + timedelta(weeks=total_weeks)).strftime("%Y-%m-%d"),
        "initiatives": [
            {
                "name": item["initiative"].name,
                "phase": item["initiative"].phase,
                "start_week": item["start_week"],
                "end_week": item["end_week"],
                "duration_weeks": item["initiative"].duration_weeks,
                "investment_range": f"${item['initiative'].investment_low:,}-${item['initiative'].investment_high:,}",
                "dependencies": item["initiative"].dependencies,
                "quick_win": item["initiative"].quick_win,
                "expected_impact": item["initiative"].expected_impact
            }
            for item in sequenced
        ],
        "investment_summary": {
            "total_range": f"${investments['total_low']:,}-${investments['total_high']:,}",
            "quarterly_breakdown": {
                f"Q{q}": {
                    "range": f"${data['low']:,}-${data['high']:,}",
                    "initiatives": data["initiatives"]
                }
                for q, data in investments["quarterly_breakdown"].items()
            }
        },
        "roi_timeline": roi_timeline,
        "milestones": milestones,
        "organization": context
    }


def main():
    """Main execution function"""
    if len(sys.argv) < 3:
        print("Usage: python generate_roadmap.py --scores <maturity_scores.json> --context <context.json>")
        sys.exit(1)
    
    # Parse command line arguments
    scores_file = None
    context_file = None
    
    for i, arg in enumerate(sys.argv):
        if arg == "--scores" and i + 1 < len(sys.argv):
            scores_file = sys.argv[i + 1]
        elif arg == "--context" and i + 1 < len(sys.argv):
            context_file = sys.argv[i + 1]
    
    if not scores_file or not context_file:
        print("Error: Both --scores and --context are required")
        sys.exit(1)
    
    # Load input files
    try:
        with open(scores_file, 'r') as f:
            scores = json.load(f)
        with open(context_file, 'r') as f:
            context = json.load(f)
    except FileNotFoundError as e:
        print(f"Error: Could not find file - {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON - {e}")
        sys.exit(1)
    
    # Generate roadmap
    roadmap = generate_roadmap(scores, context)
    
    # Output results
    output_file = "transformation_roadmap.json"
    with open(output_file, 'w') as f:
        json.dump(roadmap, f, indent=2)
    
    print(f"✅ Roadmap generated successfully: {output_file}")
    print(f"\nTransformation Duration: {roadmap['duration_months']} months ({roadmap['duration_weeks']} weeks)")
    print(f"Total Investment: {roadmap['investment_summary']['total_range']}")
    print(f"Number of Initiatives: {len(roadmap['initiatives'])}")
    print(f"Quick Wins: {sum(1 for i in roadmap['initiatives'] if i['quick_win'])}")
    print(f"\nKey Milestones: {len(roadmap['milestones'])}")


if __name__ == "__main__":
    main()
