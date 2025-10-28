import json
from datetime import datetime

# Read content.json
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Backup first
backup_filename = f'src/data/content-backup-{datetime.now().strftime("%Y%m%d-%H%M%S")}.json'
with open(backup_filename, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f'Created backup: {backup_filename}')

# Add gradeLevel to all chapters (default to sec1 for existing content)
chapters_updated = 0
for subject in data['subjects']:
    # Skip AI Playground - it doesn't have chapters
    if subject['id'] == 'ai-playground':
        continue

    for chapter in subject.get('chapters', []):
        # Add gradeLevel if it doesn't exist
        if 'gradeLevel' not in chapter:
            chapter['gradeLevel'] = 'sec1'
            chapters_updated += 1

print(f'Updated {chapters_updated} chapters with gradeLevel: sec1')

# Save updated content
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Successfully updated content.json')
print('\nNext steps:')
print('- All existing chapters now have gradeLevel: "sec1"')
print('- When adding Sec 2-4 and JC 1-2 content, set gradeLevel accordingly')
print('- Available values: "sec1", "sec2", "sec3", "sec4", "jc1", "jc2"')
