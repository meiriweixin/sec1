import json

# Load content.json
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find chapters
english = next((s for s in data['subjects'] if s['id'] == 'english'), None)
chinese = next((s for s in data['subjects'] if s['id'] == 'chinese'), None)

# English Writing - add to existing exercises
if english:
    write_ch = next((c for c in english['chapters'] if c['id'] == 'narrative-writing'), None)
    if write_ch:
        current_count = len(write_ch.get('exercises', []))
        print(f"English Narrative Writing currently has {current_count} exercises")
        print("Adding 15 more writing exercises...")

# Save (placeholder - will add exercises separately)
print("Setup complete - ready to add exercises")
