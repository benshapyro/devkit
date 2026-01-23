#!/usr/bin/env python3
"""
Block Structure Validator
Ensures blocks have all required sections and proper formatting
"""

REQUIRED_SECTIONS = [
    'Block Overview',
    'Month',
    'One-Liner',
    'Outcome',
    'Activities',
    'Deliverables',
    'Success Indicators',
    'Client Time Required',
    'Decision Gate'
]

INTERNAL_ONLY_SECTIONS = [
    'Activity Clusters',
    'Confidence Score',
    'Risk Checkpoint',
    'Assumptions'
]


def validate_block_structure(block_text, version='internal'):
    """
    Validates that a block contains all required sections
    
    Args:
        block_text: String content of the block
        version: 'internal' or 'client'
    
    Returns:
        dict with validation results
    """
    errors = []
    warnings = []
    
    # Check for required sections
    missing_sections = []
    for section in REQUIRED_SECTIONS:
        if section not in block_text:
            missing_sections.append(section)
    
    if missing_sections:
        errors.append(f"Missing required sections: {', '.join(missing_sections)}")
    
    # Version-specific checks
    if version == 'internal':
        # Internal version should have internal-only sections
        for section in INTERNAL_ONLY_SECTIONS:
            if section not in block_text:
                warnings.append(f"Internal version missing optional section: {section}")
    
    elif version == 'client':
        # Client version should NOT have internal-only sections
        for section in INTERNAL_ONLY_SECTIONS:
            if section in block_text:
                errors.append(f"Client version should not contain: {section}")
        
        # Client version should be more concise
        if 'Internal Notes' in block_text or 'Technical Details' in block_text:
            errors.append("Client version contains internal-only content")
    
    # Check for decision gates
    if 'Decision Gate' not in block_text and 'Decision Point' not in block_text:
        errors.append("No decision gate found - blocks should have phase checkpoints")
    
    # Check for outcome focus
    if 'Outcome' in block_text:
        # Ensure outcomes are present for each month
        month_count = block_text.count('Month ')
        outcome_count = block_text.count('Outcome:')
        if month_count > outcome_count:
            warnings.append(f"Found {month_count} months but only {outcome_count} outcomes")
    
    # Determine overall validity
    is_valid = len(errors) == 0
    
    return {
        'valid': is_valid,
        'errors': errors,
        'warnings': warnings,
        'version': version
    }


def print_validation_results(results):
    """Pretty print validation results"""
    print(f"\n{'='*50}")
    print(f"Block Validation Results ({results['version']} version)")
    print(f"{'='*50}\n")
    
    if results['valid']:
        print("✅ VALID: Block structure is correct\n")
    else:
        print("❌ INVALID: Block has structural issues\n")
    
    if results['errors']:
        print("ERRORS (must fix):")
        for error in results['errors']:
            print(f"  ❌ {error}")
        print()
    
    if results['warnings']:
        print("WARNINGS (should review):")
        for warning in results['warnings']:
            print(f"  ⚠️  {warning}")
        print()
    
    if results['valid'] and not results['warnings']:
        print("All checks passed! 🎉\n")


if __name__ == '__main__':
    # Test with minimal valid block
    test_block_internal = """
# Test Block - Internal Version

## Block Overview
Building a Salesforce-HubSpot integration

## Activity Clusters
- Discovery (simple)
- Integration (medium)

## Confidence Score
Score: 75%

## Risk Checkpoint
1. API documentation unknown

## Assumptions
- Data is clean

## Month 1
**One-Liner**: Discovery Sprint
**Outcome**: Requirements validated
**Activities**: 
- Stakeholder interviews
- API audit
**Deliverables**: Requirements doc
**Success Indicators**: Signed off requirements
**Client Time Required**: VP Sales - 2 hrs/week
**Decision Gate**: Review requirements, proceed to build phase
"""
    
    print("Testing internal version...")
    results = validate_block_structure(test_block_internal, 'internal')
    print_validation_results(results)
    
    test_block_client = """
# Test Block - Client Version

## Overview
Building a Salesforce-HubSpot integration

## Month 1
**What You'll Get**: Validated requirements
**Key Activities**: 
- Stakeholder interviews
- API audit
**Deliverables**: Requirements doc
**Success Indicators**: Signed off requirements
**What We Need From You**: VP Sales - 2 hrs/week
**Decision Point**: Review requirements, proceed to build phase
"""
    
    print("\nTesting client version...")
    results = validate_block_structure(test_block_client, 'client')
    print_validation_results(results)
