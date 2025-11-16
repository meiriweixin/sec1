#!/usr/bin/env python3
"""
Integrate Sec 4 Math chapters into content.json
"""

import json
import os
from datetime import datetime

# Paths
chapters_dir = "chapters"
content_file = "src/data/content.json"

# Create backup
backup_file = f"src/data/content-backup-{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

# Sec 4 Math chapter files
sec4_math_files = [
    'sec4-math-quadratic-functions-graphs.json',
    'sec4-math-simultaneous-equations-advanced.json',
    'sec4-math-coordinate-geometry-advanced.json',
    'sec4-math-trigonometry-advanced.json',
    'sec4-math-probability-advanced.json',
    'sec4-math-applications-of-mathematics.json'
]

# Read content.json
print("Reading content.json...")
with open(content_file, 'r', encoding='utf-8') as f:
    content = json.load(f)

# Create backup
print(f"Creating backup: {backup_file}")
with open(backup_file, 'w', encoding='utf-8') as f:
    json.dump(content, f, ensure_ascii=False, indent=2)

# Find math subject
math_subject = None
for subject in content['subjects']:
    if subject['id'] == 'math':
        math_subject = subject
        break

if not math_subject:
    print("❌ Math subject not found in content.json")
    exit(1)

# Read and add Sec 4 Math chapters
print("\nIntegrating Sec 4 Math chapters...")
added_chapters = []

for filename in sec4_math_files:
    filepath = os.path.join(chapters_dir, filename)

    if not os.path.exists(filepath):
        print(f"⚠️  File not found: {filename}")
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        chapter = json.load(f)

    # Check if chapter already exists
    existing = False
    for i, existing_chapter in enumerate(math_subject['chapters']):
        if existing_chapter['id'] == chapter['id']:
            # Replace existing chapter
            math_subject['chapters'][i] = chapter
            existing = True
            print(f"✓ Updated: {chapter['title']} ({len(chapter.get('exercises', []))} exercises)")
            break

    if not existing:
        # Add new chapter
        math_subject['chapters'].append(chapter)
        print(f"✓ Added: {chapter['title']} ({len(chapter.get('exercises', []))} exercises)")

    added_chapters.append(chapter['title'])

# Write updated content.json
print("\nWriting updated content.json...")
with open(content_file, 'w', encoding='utf-8') as f:
    json.dump(content, f, ensure_ascii=False, indent=2)

# Summary
print("\n" + "="*60)
print("✅ Integration complete!")
print("="*60)
print(f"\nAdded/Updated {len(added_chapters)} Sec 4 Math chapters:")
for title in added_chapters:
    print(f"  - {title}")

# Count total math chapters and exercises
total_chapters = len(math_subject['chapters'])
total_exercises = sum(len(ch.get('exercises', [])) for ch in math_subject['chapters'])
sec4_chapters = sum(1 for ch in math_subject['chapters'] if ch.get('gradeLevel') == 'sec4')

print(f"\nMathematics subject totals:")
print(f"  Total chapters: {total_chapters}")
print(f"  Sec 4 chapters: {sec4_chapters}")
print(f"  Total exercises: {total_exercises}")
print(f"\nBackup saved: {backup_file}")
