#!/usr/bin/env python3
"""
Estimate monthly ClickUp automation usage based on workflow definitions.

Usage:
    python estimate_usage.py

Interactively prompts for automation details and calculates projected monthly usage.
"""

import json
from dataclasses import dataclass
from typing import Optional


@dataclass
class AutomationEstimate:
    """Single automation usage estimate."""
    name: str
    actions_per_trigger: int
    triggers_per_day: float = 0
    triggers_per_week: float = 0
    triggers_per_month: float = 0
    
    @property
    def monthly_triggers(self) -> float:
        """Calculate total monthly triggers from any frequency input."""
        daily = self.triggers_per_day * 30
        weekly = self.triggers_per_week * 4.33
        monthly = self.triggers_per_month
        return daily + weekly + monthly
    
    @property
    def monthly_actions(self) -> float:
        """Calculate total monthly actions."""
        return self.monthly_triggers * self.actions_per_trigger


def get_float_input(prompt: str, default: float = 0) -> float:
    """Get float input with default value."""
    response = input(f"{prompt} [{default}]: ").strip()
    if not response:
        return default
    try:
        return float(response)
    except ValueError:
        print(f"  Invalid number, using default: {default}")
        return default


def get_int_input(prompt: str, default: int = 1) -> int:
    """Get integer input with default value."""
    response = input(f"{prompt} [{default}]: ").strip()
    if not response:
        return default
    try:
        return int(response)
    except ValueError:
        print(f"  Invalid number, using default: {default}")
        return default


def collect_automation() -> Optional[AutomationEstimate]:
    """Interactively collect automation details."""
    print("\n--- New Automation ---")
    name = input("Automation name (or 'done' to finish): ").strip()
    
    if name.lower() == 'done' or not name:
        return None
    
    print("\nHow many actions does this automation perform per trigger?")
    print("  (Count each: status change, notification, task creation, etc.)")
    actions = get_int_input("Actions per trigger", 1)
    
    print("\nHow often does the trigger occur?")
    print("  (Enter frequency for ONE of the following, leave others as 0)")
    
    daily = get_float_input("  Times per DAY", 0)
    weekly = get_float_input("  Times per WEEK", 0)
    monthly = get_float_input("  Times per MONTH", 0)
    
    return AutomationEstimate(
        name=name,
        actions_per_trigger=actions,
        triggers_per_day=daily,
        triggers_per_week=weekly,
        triggers_per_month=monthly
    )


def print_summary(automations: list[AutomationEstimate], plan_limit: int):
    """Print usage summary and recommendations."""
    total_actions = sum(a.monthly_actions for a in automations)
    usage_percent = (total_actions / plan_limit) * 100
    
    print("\n" + "="*60)
    print("MONTHLY AUTOMATION USAGE ESTIMATE")
    print("="*60)
    
    # Detail by automation
    print(f"\n{'Automation':<35} {'Triggers':<12} {'Actions':<12}")
    print("-"*60)
    
    for a in sorted(automations, key=lambda x: x.monthly_actions, reverse=True):
        print(f"{a.name[:34]:<35} {a.monthly_triggers:>10.0f}   {a.monthly_actions:>10.0f}")
    
    print("-"*60)
    print(f"{'TOTAL':<35} {'':<12} {total_actions:>10.0f}")
    
    # Summary
    print(f"\n📊 SUMMARY")
    print(f"   Estimated monthly actions: {total_actions:,.0f}")
    print(f"   Plan limit: {plan_limit:,}")
    print(f"   Usage: {usage_percent:.1f}%")
    print(f"   Remaining headroom: {plan_limit - total_actions:,.0f} actions")
    
    # Recommendations
    print(f"\n💡 RECOMMENDATIONS")
    
    if usage_percent > 90:
        print("   ⚠️  CRITICAL: Projected usage exceeds 90% of limit!")
        print("   • Review top automations for consolidation opportunities")
        print("   • Move complex logic to webhooks + external automation")
        print("   • Consider upgrading to Business Plus (25k) or Enterprise (250k)")
    elif usage_percent > 70:
        print("   ⚡ CAUTION: Usage approaching limit")
        print("   • Add conditions to filter unnecessary triggers")
        print("   • Consolidate similar automations")
        print("   • Monitor actual usage in first month")
    elif usage_percent > 40:
        print("   ✅ HEALTHY: Good headroom for growth")
        print("   • Continue monitoring monthly")
        print("   • Document automations for maintenance")
    else:
        print("   ✅ EXCELLENT: Plenty of capacity")
        print("   • Room to add more automations")
        print("   • Consider automating additional workflows")
    
    # Top consumers
    if len(automations) >= 3:
        print(f"\n🔍 TOP 3 CONSUMERS")
        for a in sorted(automations, key=lambda x: x.monthly_actions, reverse=True)[:3]:
            pct = (a.monthly_actions / total_actions) * 100 if total_actions > 0 else 0
            print(f"   • {a.name}: {a.monthly_actions:,.0f} actions ({pct:.0f}% of total)")


def main():
    print("="*60)
    print("CLICKUP AUTOMATION USAGE ESTIMATOR")
    print("="*60)
    
    print("\nWhich ClickUp plan are you on?")
    print("  1. Business (10,000 actions/month)")
    print("  2. Business Plus (25,000 actions/month)")
    print("  3. Enterprise (250,000 actions/month)")
    
    plan_choice = input("\nSelect plan [1]: ").strip() or "1"
    
    plan_limits = {
        "1": 10000,
        "2": 25000,
        "3": 250000
    }
    plan_limit = plan_limits.get(plan_choice, 10000)
    
    print(f"\n📋 Plan limit: {plan_limit:,} actions/month")
    print("\nEnter your automations one by one.")
    print("Type 'done' when finished.\n")
    
    automations = []
    
    while True:
        automation = collect_automation()
        if automation is None:
            break
        automations.append(automation)
        print(f"  ✓ Added: {automation.name} ({automation.monthly_actions:.0f} actions/month)")
    
    if not automations:
        print("\nNo automations entered. Exiting.")
        return
    
    print_summary(automations, plan_limit)
    
    # Offer to save
    save = input("\n💾 Save estimate to JSON? [y/N]: ").strip().lower()
    if save == 'y':
        output = {
            "plan_limit": plan_limit,
            "automations": [
                {
                    "name": a.name,
                    "actions_per_trigger": a.actions_per_trigger,
                    "triggers_per_day": a.triggers_per_day,
                    "triggers_per_week": a.triggers_per_week,
                    "triggers_per_month": a.triggers_per_month,
                    "monthly_actions": a.monthly_actions
                }
                for a in automations
            ],
            "total_monthly_actions": sum(a.monthly_actions for a in automations)
        }
        
        filename = "automation_estimate.json"
        with open(filename, "w") as f:
            json.dump(output, f, indent=2)
        print(f"  Saved to {filename}")


if __name__ == "__main__":
    main()
