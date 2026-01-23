#!/usr/bin/env python3
"""Presentation Validator - Checks cognitive load and design principles"""
import re
import sys
from pathlib import Path
from html.parser import HTMLParser

class PresentationValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides = []
        self.current_slide_text = []
        self.in_slide = False
        self.colors_used = set()
        self.violations = []
        self.warnings = []
        
    def handle_starttag(self, tag, attrs):
        if tag == 'div' and any(k == 'class' and 'slide' in v for k, v in attrs):
            self.in_slide = True
            self.current_slide_text = []
        # Track colors
        for k, v in attrs:
            if k == 'style' and 'color' in v:
                colors = re.findall(r'#[0-9A-Fa-f]{6}', v)
                self.colors_used.update(colors)
                
    def handle_endtag(self, tag):
        if tag == 'div' and self.in_slide:
            self.in_slide = False
            self.slides.append(' '.join(self.current_slide_text))
            
    def handle_data(self, data):
        if self.in_slide:
            self.current_slide_text.append(data.strip())
            
    def validate(self, html_content):
        self.feed(html_content)
        
        # Validation checks
        for i, slide in enumerate(self.slides, 1):
            words = len(slide.split())
            bullets = slide.count('•') + slide.count('-')
            
            # Check word count (≤30 words, except first slide can be 40-50)
            if i == 1 and words > 50:
                self.violations.append(f"Slide {i}: {words} words (exec summary max 50)")
            elif i > 1 and words > 30:
                self.violations.append(f"Slide {i}: {words} words (max 30)")
            elif words > 25:
                self.warnings.append(f"Slide {i}: {words} words (approaching limit)")
                
            # Check bullet points (≤4)
            if bullets > 4:
                self.violations.append(f"Slide {i}: {bullets} bullets (max 4)")
                
        # Check color count (≤4 colors)
        if len(self.colors_used) > 4:
            self.violations.append(f"Uses {len(self.colors_used)} colors (max 4)")
            
        # Check total slides for primacy/recency zones
        total = len(self.slides)
        if total > 0:
            primacy_end = max(1, int(total * 0.2))
            recency_start = int(total * 0.8)
            print(f"\n📊 Structure Analysis:")
            print(f"Total slides: {total}")
            print(f"Primacy zone (critical messages): Slides 1-{primacy_end}")
            print(f"Recency zone (CTAs): Slides {recency_start}-{total}")
            
        return len(self.violations) == 0
        
def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_presentation.py <presentation.html>")
        sys.exit(1)
        
    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
        
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    validator = PresentationValidator()
    is_valid = validator.validate(html)
    
    print("\n🔍 Presentation Validation Results\n")
    print("=" * 50)
    
    if validator.violations:
        print("\n❌ VIOLATIONS (Must Fix):")
        for v in validator.violations:
            print(f"  • {v}")
            
    if validator.warnings:
        print("\n⚠️  WARNINGS (Review Recommended):")
        for w in validator.warnings:
            print(f"  • {w}")
            
    if is_valid and not validator.warnings:
        print("\n✅ All checks passed! Presentation meets cognitive load standards.")
    elif is_valid:
        print("\n✅ No violations, but review warnings above.")
    else:
        print("\n❌ Validation failed. Fix violations above.")
        
    print("\n" + "=" * 50)
    sys.exit(0 if is_valid else 1)

if __name__ == '__main__':
    main()
