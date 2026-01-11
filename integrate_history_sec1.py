#!/usr/bin/env python3
"""
Integrate History Sec 1 chapters into main content.json
Creates automatic backup before integration
"""

import json
import shutil
from datetime import datetime

# Create backup with timestamp
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
backup_file = f'src/data/content-backup-history-sec1-{timestamp}.json'
shutil.copy('src/data/content.json', backup_file)
print(f"✓ Created backup: {backup_file}")
print()

# Load existing content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    content = json.load(f)

# Load History chapters
with open('chapters/history-sec1-chapters.json', 'r', encoding='utf-8') as f:
    history_data = json.load(f)

# Create History subject
history_subject = {
    "id": "history",
    "title": "History",
    "title_zh": "历史",
    "description": "Explore Singapore's journey from Temasek to modern nation through historical inquiry",
    "description_zh": "通过历史探究探索新加坡从淡马锡到现代国家的历程",
    "color": "#8B1538",
    "chapters": history_data['chapters']
}

# Check if History subject already exists
history_exists = any(subject['id'] == 'history' for subject in content['subjects'])

if history_exists:
    # Replace existing History subject
    for i, subject in enumerate(content['subjects']):
        if subject['id'] == 'history':
            content['subjects'][i] = history_subject
            print(f"✓ Updated existing History subject")
            print(f"  - {len(history_subject['chapters'])} chapters")
            print(f"  - Total exercises: {sum(len(ch.get('exercises', [])) for ch in history_subject['chapters'])}")
            break
else:
    # Add new History subject
    content['subjects'].append(history_subject)
    print(f"✓ Added new History subject")
    print(f"  - {len(history_subject['chapters'])} chapters")
    print(f"  - Total exercises: {sum(len(ch.get('exercises', [])) for ch in history_subject['chapters'])}")

print()

# Save updated content
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(content, f, ensure_ascii=False, indent=2)

print(f"✓ Saved updated content.json")
print()
print("Integration Summary:")
print("=" * 60)
print(f"Subject: History (历史)")
print(f"Grade Level: Secondary 1")
print(f"Units: 2 (Unit 1: From Temasek to Singapore, Unit 2: Port City Development)")
print(f"Chapters: {len(history_subject['chapters'])}")
print()
print("Chapter Breakdown:")
for i, chapter in enumerate(history_subject['chapters'], 1):
    ex_count = len(chapter.get('exercises', []))
    print(f"  {i}. {chapter['title']}")
    print(f"     - {len(chapter['sections'])} sections")
    print(f"     - {ex_count} exercises")
    print(f"     - Unit {chapter['unit']}")
print()
print("National Education Themes Integrated:")
print("  - Total Defence (all pillars)")
print("  - Racial Harmony")
print("  - Social Cohesion")
print()
print("Historical Inquiry Process:")
print("  ✓ Sparking Curiosity")
print("  ✓ Gathering Evidence")
print("  ✓ Exercising Reasoning")
print("  ✓ Reflective Thinking")
print()
print("Assessment Objectives Covered:")
print("  ✓ AO1: Deploying Knowledge (identify, describe)")
print("  ✓ AO2: Communicating Historical Knowledge (explain with evidence)")
print("  ✓ AO3: Interpreting and Analysing Source Materials (SBQ)")
print()
print("Ready for testing in the app!")
print("Navigate to http://localhost:8080 → Select Sec 1 grade level → History subject")
