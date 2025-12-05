#!/usr/bin/env python3
"""
Integrate JC1 Chemistry chapters into main content.json
Creates a new Chemistry (H2) subject with JC1 chapters
"""
import json
import shutil
from datetime import datetime

# Create backup
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
backup_file = f'src/data/content-backup-jc1-chemistry-{timestamp}.json'
shutil.copy('src/data/content.json', backup_file)
print(f"✅ Backup created: {backup_file}")

# Load main content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    content = json.load(f)

# Load JC1 Chemistry chapters
with open('chapters/jc1_chemistry_chapters.json', 'r', encoding='utf-8') as f:
    jc1_chemistry = json.load(f)

# Check if Chemistry subject exists
chemistry_subject = None
for subject in content['subjects']:
    if subject['id'] == 'chemistry-jc':
        chemistry_subject = subject
        break

# If Chemistry subject doesn't exist, create it
if not chemistry_subject:
    print("📚 Creating new Chemistry (H2) subject...")
    chemistry_subject = {
        "id": "chemistry-jc",
        "title": "Chemistry (H2)",
        "title_zh": "化学 (H2)",
        "description": "Singapore-Cambridge GCE A-Level H2 Chemistry for JC students",
        "description_zh": "新加坡-剑桥GCE A水准H2化学（适用于初级学院学生）",
        "color": "from-green-500 to-emerald-600",
        "chapters": []
    }
    # Insert after physics-jc subject
    physics_index = next(i for i, s in enumerate(content['subjects']) if s['id'] == 'physics-jc')
    content['subjects'].insert(physics_index + 1, chemistry_subject)
else:
    print("📚 Found existing Chemistry (H2) subject")

# Add JC1 Chemistry chapters
print(f"📝 Adding {len(jc1_chemistry)} JC1 Chemistry chapters...")
chemistry_subject['chapters'] = jc1_chemistry

# Save updated content
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(content, f, ensure_ascii=False, indent=2)

print("\n✅ Integration Complete!")
print(f"📊 Total subjects: {len(content['subjects'])}")
print(f"📖 Chemistry chapters: {len(chemistry_subject['chapters'])}")
print(f"📄 Total sections: {sum(len(ch['sections']) for ch in chemistry_subject['chapters'])}")

print("\n🔍 Chemistry Subject Details:")
print(f"  ID: {chemistry_subject['id']}")
print(f"  Title: {chemistry_subject['title']}")
print(f"  Chapters:")
for i, chapter in enumerate(chemistry_subject['chapters'], 1):
    print(f"    {i}. {chapter['title']} - {chapter['gradeLevel']} ({len(chapter['sections'])} sections)")

print("\n✨ Next steps:")
print("1. Start dev server: npm run dev")
print("2. Login and select JC 1 grade level")
print("3. Navigate to Chemistry (H2) subject")
print("4. Verify all 8 chapters appear")
print("5. Generate exercises for all chapters")
