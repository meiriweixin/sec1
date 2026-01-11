#!/usr/bin/env python3
"""Check History chapters for sections"""

import json

with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find History subject
history = [s for s in data['subjects'] if s['id'] == 'history'][0]

print("History Chapters Status:\n")
for ch in history['chapters']:
    sections = ch.get('sections', [])
    exercises = ch.get('exercises', [])
    
    print(f"📚 {ch['title']}")
    print(f"   ID: {ch['id']}")
    print(f"   Sections: {len(sections)}")
    print(f"   Exercises: {len(exercises)}")
    
    # Check if sections have content_zh
    if sections:
        sections_with_zh = sum(1 for s in sections if 'content_zh' in s)
        print(f"   Sections with Chinese content: {sections_with_zh}/{len(sections)}")
    
    print()
