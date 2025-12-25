import json
from datetime import datetime

# Create backup
backup_path = f"src/data/content-backup-complete-lang-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open(backup_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"✓ Backup created: {backup_path}")

# Load new exercises
with open('english_reading_new.json', 'r', encoding='utf-8') as f:
    eng_reading = json.load(f)

with open('chinese_reading_new.json', 'r', encoding='utf-8') as f:
    chi_reading = json.load(f)

with open('chinese_writing_new.json', 'r', encoding='utf-8') as f:
    chi_writing = json.load(f)

print("\nLoaded exercise files:")
print(f"  English Reading: {len(eng_reading)} exercises")
print(f"  Chinese Reading: {len(chi_reading)} exercises")
print(f"  Chinese Writing: {len(chi_writing)} exercises")

# Find subjects
english = next((s for s in data['subjects'] if s['id'] == 'english'), None)
chinese = next((s for s in data['subjects'] if s['id'] == 'chinese'), None)

if not english or not chinese:
    print("ERROR: Could not find English or Chinese subject")
    exit(1)

# Find chapters
eng_read_ch = next((c for c in english['chapters']
                    if c['id'] == 'reading-comprehension' and c.get('gradeLevel') == 'sec1'), None)
chi_read_ch = next((c for c in chinese['chapters']
                    if c['id'] == 'chinese-reading-comprehension' and c.get('gradeLevel') == 'sec1'), None)
chi_writ_ch = next((c for c in chinese['chapters']
                    if c['id'] == 'chinese-composition-writing' and c.get('gradeLevel') == 'sec1'), None)

if not eng_read_ch:
    print("ERROR: Could not find English Reading Comprehension chapter")
    exit(1)
if not chi_read_ch:
    print("ERROR: Could not find Chinese Reading Comprehension chapter")
    exit(1)
if not chi_writ_ch:
    print("ERROR: Could not find Chinese Composition Writing chapter")
    exit(1)

print("\n" + "="*60)
print("INTEGRATING EXERCISES")
print("="*60)

# Check if already integrated
eng_read_current = len(eng_read_ch.get('exercises', []))
chi_read_current = len(chi_read_ch.get('exercises', []))
chi_writ_current = len(chi_writ_ch.get('exercises', []))

print(f"\nCurrent counts:")
print(f"  English Reading: {eng_read_current} exercises")
print(f"  Chinese Reading: {chi_read_current} exercises")
print(f"  Chinese Writing: {chi_writ_current} exercises")

# Integrate English Reading (if not already done)
if eng_read_current < 30:
    print(f"\n✓ Adding {len(eng_reading)} exercises to English Reading...")
    eng_read_ch['exercises'].extend(eng_reading)
else:
    print("\n✓ English Reading already has 30 exercises, skipping")

# Integrate Chinese Reading
if chi_read_current < 30:
    print(f"✓ Adding {len(chi_reading)} exercises to Chinese Reading...")
    chi_read_ch['exercises'].extend(chi_reading)
else:
    print("✓ Chinese Reading already has 30 exercises, skipping")

# Integrate Chinese Writing
if chi_writ_current < 30:
    print(f"✓ Adding {len(chi_writing)} exercises to Chinese Writing...")
    chi_writ_ch['exercises'].extend(chi_writing)
else:
    print("✓ Chinese Writing already has 30 exercises, skipping")

# Save
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\n" + "="*60)
print("INTEGRATION COMPLETE")
print("="*60)

# Final counts
print(f"\nFinal counts:")
print(f"  English Reading: {len(eng_read_ch['exercises'])} exercises")
print(f"  Chinese Reading: {len(chi_read_ch['exercises'])} exercises")
print(f"  Chinese Writing: {len(chi_writ_ch['exercises'])} exercises")

print(f"\nBackup saved to: {backup_path}")
print("✓ All language exercises integrated successfully!")
