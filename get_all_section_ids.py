#!/usr/bin/env python3
"""Get all section IDs for History chapters"""

import json

with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find History subject
history = [s for s in data['subjects'] if s['id'] == 'history'][0]

print("History Chapter Section IDs:\n")
for ch in history['chapters']:
    print(f"Chapter: {ch['id']}")
    print(f"Title: {ch['title']}")
    for s in ch.get('sections', []):
        print(f"  - {s['id']}: {s['title']}")
    print()
