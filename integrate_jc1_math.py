#!/usr/bin/env python3
"""
Integrate JC 1 Mathematics chapters into main content.json
"""

import json
import shutil
from datetime import datetime

# Create backup
content_file = 'src/data/content.json'
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
backup_file = f'src/data/content-backup-jc1-integration-{timestamp}.json'
shutil.copy(content_file, backup_file)
print(f"✅ Created backup: {backup_file}")
print()

# Load main content
with open(content_file, 'r', encoding='utf-8') as f:
    main_content = json.load(f)

# Load JC 1 chapters
with open('chapters/jc1_math_chapters.json', 'r', encoding='utf-8') as f:
    jc1_chapters = json.load(f)

# Find Mathematics subject
math_subject = None
for subject in main_content['subjects']:
    if subject['id'] == 'math':
        math_subject = subject
        break

if not math_subject:
    print("❌ Error: Mathematics subject not found!")
    exit(1)

# Count existing chapters by grade level
existing_counts = {}
for chapter in math_subject['chapters']:
    grade = chapter.get('gradeLevel', 'unknown')
    existing_counts[grade] = existing_counts.get(grade, 0) + 1

print("Current Mathematics chapters by grade level:")
for grade in ['sec1', 'sec2', 'sec3', 'sec4', 'jc1', 'jc2']:
    count = existing_counts.get(grade, 0)
    print(f"  {grade.upper()}: {count} chapters")
print()

# Add JC 1 chapters
print(f"Adding {len(jc1_chapters)} JC 1 chapters...")
for chapter in jc1_chapters:
    # Count exercises
    ex_count = len(chapter.get('exercises', []))
    print(f"  • {chapter['title']}: {len(chapter.get('sections', []))} sections, {ex_count} exercises")

# Append to mathematics chapters
math_subject['chapters'].extend(jc1_chapters)

# Save updated content
with open(content_file, 'w', encoding='utf-8') as f:
    json.dump(main_content, f, ensure_ascii=False, indent=2)

print()
print("✅ Successfully integrated JC 1 Mathematics chapters!")
print()

# Count final totals
final_counts = {}
total_exercises = 0
for chapter in math_subject['chapters']:
    grade = chapter.get('gradeLevel', 'unknown')
    final_counts[grade] = final_counts.get(grade, 0) + 1
    total_exercises += len(chapter.get('exercises', []))

print("Updated Mathematics chapters by grade level:")
for grade in ['sec1', 'sec2', 'sec3', 'sec4', 'jc1', 'jc2']:
    count = final_counts.get(grade, 0)
    print(f"  {grade.upper()}: {count} chapters")

print()
print(f"Total Mathematics chapters: {len(math_subject['chapters'])}")
print(f"Total Mathematics exercises: {total_exercises}")
print()
print("🎉 JC 1 content is now available in the app!")
print("   Students can select 'JC 1' grade level to see the new chapters.")
