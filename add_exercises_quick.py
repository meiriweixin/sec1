import json
from datetime import datetime

# Load content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Load English Reading exercises (already created)
with open('english_reading_new.json', 'r', encoding='utf-8') as f:
    eng_reading_new = json.load(f)

print("Adding exercises to English and Chinese subjects...")
print("="*60)

# Find subjects
english = next((s for s in data['subjects'] if s['id'] == 'english'), None)
chinese = next((s for s in data['subjects'] if s['id'] == 'chinese'), None)

# ENGLISH WRITING - 15 exercises with full content
# (English reading already done - has 30 exercises)

english_writing_exercises = []
# Import from separate JSON file to avoid quote issues
import json as json_lib

# Since we have quote issues, let's add them programmatically
# We already have english_reading_new integrated

print("\nChinese and remaining English exercises will be added next...")
print("Current status:")

if english:
    for ch in english['chapters']:
        if ch.get('gradeLevel') == 'sec1' and ('read' in ch['id'] or 'writ' in ch['id']):
            print(f"  English - {ch['title']}: {len(ch.get('exercises', []))} exercises")

if chinese:
    for ch in chinese['chapters']:
        if ch.get('gradeLevel') == 'sec1' and ('read' in ch['id'] or 'writ' in ch['id'] or 'compos' in ch['id']):
            print(f"  Chinese - {ch['title']}: {len(ch.get('exercises', []))} exercises")

print("\nReady for next batch...")
