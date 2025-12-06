import json
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('A-LEVEL EXAM PREP:')
for subject in data['subjects']:
    chapters = [ch for ch in subject['chapters'] if ch.get('gradeLevel') == 'alevel']
    if chapters:
        print(f"  [{subject['id']}]: {len(chapters)} chapters")
        for ch in chapters:
            print(f"    - {ch['title']}")

