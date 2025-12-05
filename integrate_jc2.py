import json
from datetime import datetime

# Create backup
backup_file = f'src/data/content-backup-jc2-integration-{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    backup_data = json.load(f)
with open(backup_file, 'w', encoding='utf-8') as f:
    json.dump(backup_data, f, ensure_ascii=False, indent=2)
print(f"✓ Backup created: {backup_file}")

# Load JC 2 chapters
with open('chapters/jc2_math_chapters.json', 'r', encoding='utf-8') as f:
    jc2_chapters = json.load(f)

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

# Remove existing JC 2 chapters first (to prevent duplicates)
original_count = len(math_subject['chapters'])
math_subject['chapters'] = [ch for ch in math_subject['chapters'] if ch.get('gradeLevel') != 'jc2']
removed = original_count - len(math_subject['chapters'])
if removed > 0:
    print(f"Removed {removed} existing JC 2 chapters to prevent duplicates")

# Append JC 2 chapters to Math
math_subject['chapters'].extend(jc2_chapters)

# Save updated content
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(content, f, ensure_ascii=False, indent=2)

print(f"\n{'='*60}")
print(f"✓ Successfully integrated JC 2 Mathematics chapters")
print(f"{'='*60}")

# Verify the integration
jc1_count = sum(1 for ch in math_subject['chapters'] if ch.get('gradeLevel') == 'jc1')
jc2_count = sum(1 for ch in math_subject['chapters'] if ch.get('gradeLevel') == 'jc2')
total_chapters = len(math_subject['chapters'])
total_exercises = sum(len(ch.get('exercises', [])) for ch in math_subject['chapters'])

print("\nMathematics Content Summary:")
print(f"  Total chapters: {total_chapters}")
print(f"  JC 1 chapters: {jc1_count}")
print(f"  JC 2 chapters: {jc2_count}")
print(f"  Total exercises: {total_exercises}")

print("\nJC 2 chapters added:")
for i, ch in enumerate(jc2_chapters, 1):
    sections = len(ch.get('sections', []))
    exercises = len(ch.get('exercises', []))
    print(f"  {i}. {ch['title']}: {sections} sections, {exercises} exercises")
