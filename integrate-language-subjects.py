#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Integrate English and Chinese language subjects into content.json
"""

import json
import os
from datetime import datetime

# Backup current content.json
def backup_content():
    if os.path.exists('src/data/content.json'):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = f'src/data/content-backup-{timestamp}.json'
        with open('src/data/content.json', 'r', encoding='utf-8') as f:
            content = json.load(f)
        with open(backup_path, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False, indent=2)
        print(f"📦 Backed up content.json to {backup_path}")
        return content
    return None

# Load current content
current_content = backup_content()

if current_content is None:
    print("❌ Error: content.json not found")
    exit(1)

# English Language Subject
english_subject = {
    "id": "english",
    "title": "English Language",
    "title_zh": "英语",
    "description": "Master English grammar, vocabulary, writing, and comprehension skills",
    "description_zh": "掌握英语语法、词汇、写作和阅读理解技能",
    "color": "from-indigo-500 to-purple-500",
    "chapters": []
}

# Chinese Language Subject
chinese_subject = {
    "id": "chinese",
    "title": "Chinese Language (华文)",
    "title_zh": "华文",
    "description": "Master Chinese grammar, vocabulary, idioms, and composition skills",
    "description_zh": "掌握中文语法、词汇、成语和作文技能",
    "color": "from-red-500 to-orange-500",
    "chapters": []
}

# Load English chapters (all 6)
english_chapter_files = [
    'english-grammar-foundations.json',
    'english-vocabulary-building.json',
    'english-sentence-construction.json',
    'english-narrative-writing.json',
    'english-reading-comprehension.json',
    'english-editing-proofreading.json'
]

for filename in english_chapter_files:
    filepath = f'chapters/{filename}'
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            chapter = json.load(f)
            english_subject['chapters'].append(chapter)
            print(f"✅ Loaded {filename}")
    else:
        print(f"⚠️  Warning: {filename} not found")

# Load Chinese chapters (all 6)
chinese_chapter_files = [
    'chinese-grammar-fundamentals.json',
    'chinese-vocabulary-building.json',
    'chinese-idioms-proverbs.json',
    'chinese-composition-writing.json',
    'chinese-reading-comprehension.json',
    'chinese-sentence-correction.json'
]

for filename in chinese_chapter_files:
    filepath = f'chapters/{filename}'
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            chapter = json.load(f)
            chinese_subject['chapters'].append(chapter)
            print(f"✅ Loaded {filename}")
    else:
        print(f"⚠️  Warning: {filename} not found")

# Add language subjects to the beginning of the subjects array
new_subjects = [english_subject, chinese_subject]

# Keep existing subjects (math, science) but skip old english/chinese
for subject in current_content['subjects']:
    if subject['id'] not in ['english', 'chinese']:
        new_subjects.append(subject)

# Update content
current_content['subjects'] = new_subjects

# Save updated content.json
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(current_content, f, ensure_ascii=False, indent=2)

print("\n✨ Successfully integrated language subjects into content.json!")
print(f"\n📊 Summary:")
print(f"   - English chapters: {len(english_subject['chapters'])}")
print(f"   - Chinese chapters: {len(chinese_subject['chapters'])}")
print(f"   - Total subjects: {len(new_subjects)}")
print("\n🎯 Subject order:")
for i, subject in enumerate(new_subjects, 1):
    title = subject.get('title', 'Unknown')
    chapter_count = len(subject.get('chapters', []))
    print(f"   {i}. {title} ({chapter_count} chapters)")
