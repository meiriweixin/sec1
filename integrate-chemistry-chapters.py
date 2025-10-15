import json
from datetime import datetime

# Load content.json
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Load new chapters
with open('elements-compounds-chapter.json', 'r', encoding='utf-8') as f:
    elements_chapter = json.load(f)

with open('acids-bases-chapter.json', 'r', encoding='utf-8') as f:
    acids_chapter = json.load(f)

# Tag existing Science chapters according to their content
chapter_tags = {
    'scientific-methods': ('General', '综合'),
    'particle-model': ('Chemistry', '化学'),  # Already tagged
    'mixtures-separation': ('Chemistry', '化学'),  # Already tagged
    'cells': ('Biology', '生物'),
    'light': ('Physics', '物理'),
    'heat-temperature': ('Physics', '物理'),
    'forces-motion': ('Physics', '物理'),
    'digestive-system': ('Biology', '生物'),
    'respiratory-system': ('Biology', '生物'),
    'circulatory-system': ('Biology', '生物'),
    'reproduction': ('Biology', '生物')
}

# Find Science subject and update
for subject in data['subjects']:
    if subject['id'] == 'science':
        # Tag existing chapters
        for chapter in subject['chapters']:
            chapter_id = chapter['id']
            if chapter_id in chapter_tags:
                chapter['tag'] = chapter_tags[chapter_id][0]
                chapter['tag_zh'] = chapter_tags[chapter_id][1]
                print(f"Tagged {chapter_id} as {chapter_tags[chapter_id][0]}")

        # Insert new Chemistry chapters after mixtures-separation
        mixtures_index = next(i for i, ch in enumerate(subject['chapters']) if ch['id'] == 'mixtures-separation')

        # Insert Elements chapter
        subject['chapters'].insert(mixtures_index + 1, elements_chapter)
        print(f"\nInserted 'elements-compounds' chapter after 'mixtures-separation'")

        # Insert Acids & Bases chapter
        subject['chapters'].insert(mixtures_index + 2, acids_chapter)
        print(f"Inserted 'acids-bases' chapter after 'elements-compounds'")

        # Print final chapter list
        print(f"\n=== Final Science Chapters ({len(subject['chapters'])} total) ===")
        for i, ch in enumerate(subject['chapters'], 1):
            tag = ch.get('tag', 'No tag')
            print(f"{i}. {ch['id']} - {ch['title']} (Tag: {tag})")

        break

# Save updated content
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\n✅ All Chemistry chapters integrated successfully!")
print("✅ All Science chapters tagged!")
