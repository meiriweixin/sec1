#!/usr/bin/env python3
"""
Integrate Sec 4 Science chapters into main content.json
"""
import json
import shutil
from datetime import datetime

# Create backup
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
backup_path = f'src/data/content-backup-sec4-science-{timestamp}.json'
shutil.copy('src/data/content.json', backup_path)
print(f"✅ Backup created: {backup_path}")

# Load main content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    content = json.load(f)

# Load Sec 4 Science chapters
with open('chapters/sec4_science_chapters.json', 'r', encoding='utf-8') as f:
    sec4_chapters = json.load(f)

# Find Science subject
science_subject = None
for subject in content['subjects']:
    if subject['id'] == 'science':
        science_subject = subject
        break

if not science_subject:
    print("❌ Science subject not found!")
    exit(1)

# Check for duplicates
existing_ids = {ch['id'] for ch in science_subject['chapters']}
new_chapters = [ch for ch in sec4_chapters if ch['id'] not in existing_ids]

if not new_chapters:
    print("⚠️ All Sec 4 Science chapters already exist in content.json")
    exit(0)

# Add new chapters
science_subject['chapters'].extend(new_chapters)

# Save updated content
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(content, f, ensure_ascii=False, indent=2)

print(f"\n✅ Added {len(new_chapters)} Sec 4 Science chapters to content.json!")
print("\nIntegrated chapters:")
for ch in new_chapters:
    sections = len(ch.get('sections', []))
    exercises = len(ch.get('exercises', []))
    print(f"  [{ch['tag']}] {ch['title']} - {sections} sections, {exercises} exercises")

# Count all Science chapters by grade
grade_counts = {}
for ch in science_subject['chapters']:
    grade = ch.get('gradeLevel', 'unknown')
    grade_counts[grade] = grade_counts.get(grade, 0) + 1

print("\n📊 Science chapters by grade level:")
for grade in ['sec1', 'sec2', 'sec3', 'sec4']:
    count = grade_counts.get(grade, 0)
    print(f"  {grade.upper()}: {count} chapters")

print(f"\n📚 Total Science chapters: {len(science_subject['chapters'])}")
print("\n⚠️ Note: Exercises are empty - run exercise generation script next!")














