#!/usr/bin/env python3
"""Cognitive Load Analyzer - Analyzes information density and attention management"""
import sys
from pathlib import Path
from html.parser import HTMLParser

class CognitiveLoadAnalyzer(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides = []
        self.current_slide = {'text': [], 'images': 0, 'lists': 0}
        self.in_slide = False
        
    def handle_starttag(self, tag, attrs):
        if tag == 'div' and any(k == 'class' and 'slide' in v for k, v in attrs):
            if self.in_slide:
                self.slides.append(self.current_slide)
            self.in_slide = True
            self.current_slide = {'text': [], 'images': 0, 'lists': 0}
        elif self.in_slide:
            if tag == 'img':
                self.current_slide['images'] += 1
            elif tag in ['ul', 'ol']:
                self.current_slide['lists'] += 1
                
    def handle_data(self, data):
        if self.in_slide:
            self.current_slide['text'].append(data.strip())
            
    def analyze(self, html):
        self.feed(html)
        if self.in_slide:
            self.slides.append(self.current_slide)
            
        print("\n🧠 Cognitive Load Analysis\n" + "="*50)
        
        issues = []
        for i, slide in enumerate(self.slides, 1):
            text = ' '.join(slide['text'])
            words = len(text.split())
            chunks = slide['lists'] + slide['images']
            
            load = 'LOW'
            if words > 40 or chunks > 4:
                load = 'HIGH'
                issues.append(f"Slide {i}: {load} load ({words}w, {chunks} chunks)")
            elif words > 25 or chunks > 3:
                load = 'MEDIUM'
                
            if i <= 3 or i >= len(self.slides) - 2:
                zone = 'PRIMACY' if i <= 3 else 'RECENCY'
                print(f"Slide {i} [{zone}]: {load} load - {words}w, {chunks} chunks")
            elif load != 'LOW':
                print(f"Slide {i}: {load} load - {words}w, {chunks} chunks")
                
        if len(self.slides) > 10:
            print(f"\n⏱️  Cognitive Break Recommendations:")
            print(f"  • Break after slide {min(4, len(self.slides))} (~10 min mark)")
            print(f"  • Break after slide {min(8, len(self.slides))} (~20 min mark)")
            
        if issues:
            print(f"\n⚠️  {len(issues)} slides need cognitive load reduction:")
            for issue in issues[:5]:
                print(f"  • {issue}")
        else:
            print(f"\n✅ Cognitive load well-managed across all slides")
            
        print("="*50 + "\n")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python check_cognitive_load.py <presentation.html>")
        sys.exit(1)
    with open(sys.argv[1], 'r') as f:
        CognitiveLoadAnalyzer().analyze(f.read())
