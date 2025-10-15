#!/usr/bin/env python3
"""Simple script to merge expanded Forces & Motion chapter into content.json"""

import json
import shutil
from pathlib import Path

# Paths
content_file = Path("src/data/content.json")
expanded_file = Path("expanded-chapters/05-forces-motion.json")
backup_file = Path(f"src/data/content-backup-{Path(__file__).stem}.json")

print("🔄 Loading files...")

# Load content.json
with open(content_file, 'r', encoding='utf-8') as f:
    content = json.load(f)

# Load expanded chapter
with open(expanded_file, 'r', encoding='utf-8') as f:
    expanded_chapter = json.load(f)

# Find science subject
science = next((s for s in content['subjects'] if s['id'] == 'science'), None)
if not science:
    print("❌ Science subject not found!")
    exit(1)

# Find forces-motion chapter index
chapter_idx = next((i for i, c in enumerate(science['chapters']) if c['id'] == 'forces-motion'), None)
if chapter_idx is None:
    print("❌ Forces & Motion chapter not found!")
    exit(1)

old_chapter = science['chapters'][chapter_idx]
print(f"\n📊 Current chapter stats:")
print(f"   Sections: {len(old_chapter['sections'])}")
print(f"   Exercises: {len(old_chapter['exercises'])}")

print(f"\n📊 Expanded chapter stats:")
print(f"   Sections: {len(expanded_chapter['sections'])}")
print(f"   Exercises: {len(expanded_chapter['exercises'])}")

# Create backup
print(f"\n💾 Creating backup: {backup_file.name}")
shutil.copy2(content_file, backup_file)

# Replace chapter
science['chapters'][chapter_idx] = expanded_chapter

# Save updated content
print("\n✍️ Writing updated content.json...")
with open(content_file, 'w', encoding='utf-8') as f:
    json.dump(content, f, indent=2, ensure_ascii=False)

print("\n✅ SUCCESS! Forces & Motion chapter has been expanded!")
print("\n🎯 Next steps:")
print("   1. Run: npm run dev")
print("   2. Navigate to: Science > Forces & Motion")
print("   3. You should now see 7 sections and 12 exercises!")
print("\n💡 Tip: If you see issues, restore from backup:")
print(f"   copy {backup_file} {content_file}")












