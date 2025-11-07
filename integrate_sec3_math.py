import json
import shutil
from datetime import datetime

# Create backup
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_file = f"src/data/content-backup-{timestamp}.json"
shutil.copy("src/data/content.json", backup_file)
print(f"Created backup: {backup_file}")

# Load existing content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    content = json.load(f)

# Load new Sec 3 Math chapters
with open('chapters/sec3-math-chapters.json', 'r', encoding='utf-8') as f:
    sec3_math_chapters = json.load(f)

# Find Math subject and add Sec 3 chapters
for subject in content['subjects']:
    if subject['id'] == 'math':
        # Get existing chapter IDs to avoid duplicates
        existing_ids = {ch['id'] for ch in subject['chapters']}

        # Add new chapters only if they don't exist
        new_chapters_added = 0
        for chapter in sec3_math_chapters:
            if chapter['id'] not in existing_ids:
                subject['chapters'].append(chapter)
                new_chapters_added += 1

        print(f"Added {new_chapters_added} Secondary 3 Mathematics chapters")
        print(f"Total Math chapters now: {len(subject['chapters'])}")
        break

# Save updated content
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(content, f, ensure_ascii=False, indent=2)

print("Integration complete!")

# Verify the integration
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    content = json.load(f)

for subject in content['subjects']:
    if subject['id'] == 'math':
        sec1_chapters = [ch for ch in subject['chapters'] if ch.get('gradeLevel') == 'sec1']
        sec2_chapters = [ch for ch in subject['chapters'] if ch.get('gradeLevel') == 'sec2']
        sec3_chapters = [ch for ch in subject['chapters'] if ch.get('gradeLevel') == 'sec3']

        print(f"\nVerification:")
        print(f"  Sec 1 Math chapters: {len(sec1_chapters)}")
        print(f"  Sec 2 Math chapters: {len(sec2_chapters)}")
        print(f"  Sec 3 Math chapters: {len(sec3_chapters)}")
        print(f"\nSec 3 Math chapters:")
        for ch in sec3_chapters:
            ex_count = len(ch.get('exercises', []))
            print(f"  - {ch['title']}: {ex_count} exercises")
