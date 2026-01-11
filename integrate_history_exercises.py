#!/usr/bin/env python3
"""
Integrate generated History exercises into content.json
"""

import json
import shutil
from datetime import datetime

# Create backup first
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_file = f"src/data/content-backup-history-{timestamp}.json"
shutil.copy("src/data/content.json", backup_file)
print(f"📦 Created backup: {backup_file}")

# Load content.json
with open("src/data/content.json", "r", encoding="utf-8") as f:
    content = json.load(f)

# Load generated exercises
with open("chapters/history_exercises.json", "r", encoding="utf-8") as f:
    history_exercises = json.load(f)

# Find the history subject
history_subject = None
for subject in content["subjects"]:
    if subject["id"] == "history":
        history_subject = subject
        break

if not history_subject:
    print("❌ Error: Could not find history subject in content.json")
    exit(1)

# Integrate exercises into each chapter
chapters_updated = 0
for chapter in history_subject["chapters"]:
    chapter_id = chapter["id"]
    if chapter_id in history_exercises:
        # Check if exercises already exist
        if chapter.get("exercises") and len(chapter["exercises"]) > 0:
            print(f"⚠️  Chapter '{chapter_id}' already has {len(chapter['exercises'])} exercises - skipping")
            continue
        
        # Add exercises
        chapter["exercises"] = history_exercises[chapter_id]
        chapters_updated += 1
        print(f"✅ Added {len(history_exercises[chapter_id])} exercises to '{chapter_id}'")

# Save updated content.json
with open("src/data/content.json", "w", encoding="utf-8") as f:
    json.dump(content, f, ensure_ascii=False, indent=2)

print(f"\n🎉 Integration complete!")
print(f"📊 Updated {chapters_updated} chapters")
print(f"💾 Saved to: src/data/content.json")
print(f"\n✨ History exercises are now ready for testing!")
