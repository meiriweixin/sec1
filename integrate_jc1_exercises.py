import json
from datetime import datetime

# Create backup
backup_file = f'src/data/content-backup-jc1-exercises-{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    backup_data = json.load(f)
with open(backup_file, 'w', encoding='utf-8') as f:
    json.dump(backup_data, f, ensure_ascii=False, indent=2)
print(f"✓ Backup created: {backup_file}")

# Load updated JC 1 chapters (with all exercises)
with open('chapters/jc1_math_chapters.json', 'r', encoding='utf-8') as f:
    updated_jc1_chapters = json.load(f)

# Load main content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    content = json.load(f)

# Find Mathematics subject
math_subject = None
for subject in content['subjects']:
    if subject['id'] == 'math':
        math_subject = subject
        break

if not math_subject:
    print("❌ Mathematics subject not found!")
    exit(1)

# Create a map of chapter IDs to updated chapters
updated_chapters_map = {ch['id']: ch for ch in updated_jc1_chapters}

# Update existing JC 1 chapters with new exercises
updated_count = 0
for i, chapter in enumerate(math_subject['chapters']):
    if chapter['id'] in updated_chapters_map:
        # Replace exercises while keeping other chapter data intact
        updated_chapter = updated_chapters_map[chapter['id']]
        math_subject['chapters'][i]['exercises'] = updated_chapter['exercises']
        exercise_count = len(updated_chapter['exercises'])
        print(f"✓ Updated {chapter['title']}: {exercise_count} exercises")
        updated_count += 1

# Save updated content
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(content, f, ensure_ascii=False, indent=2)

print(f"\n{'='*60}")
print(f"✓ Successfully updated {updated_count} JC 1 Mathematics chapters")
print(f"{'='*60}")

# Verify the integration
total_jc1_exercises = 0
print("\nJC 1 Mathematics chapters in content.json:")
for chapter in math_subject['chapters']:
    if chapter.get('gradeLevel') == 'jc1':
        ex_count = len(chapter.get('exercises', []))
        total_jc1_exercises += ex_count
        print(f"  - {chapter['title']}: {ex_count} exercises")

print(f"\nTotal JC 1 exercises: {total_jc1_exercises}/120")

# Count all math exercises
total_math_exercises = sum(len(ch.get('exercises', [])) for ch in math_subject['chapters'])
print(f"Total Mathematics exercises: {total_math_exercises}")
