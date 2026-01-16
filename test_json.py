import json

with open('chapters/sec1_adaptations_chapter.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    
print("✅ JSON loaded successfully!")
print(f"Chapter: {data['chapter']['title']}")
print(f"Sections: {len(data['chapter']['sections'])}")
print(f"Exercises: {len(data['chapter']['exercises'])}")
