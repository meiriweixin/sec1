import json
from datetime import datetime

# Create backup
backup_file = f"src/data/content-backup-humanities-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
with open("src/data/content.json", "r", encoding="utf-8") as f:
    content = json.load(f)
with open(backup_file, "w", encoding="utf-8") as f:
    json.dump(content, f, ensure_ascii=False, indent=2)
print(f"✅ Backup created: {backup_file}")

# Load Humanities chapters
with open("chapters/sec1_humanities_chapters.json", "r", encoding="utf-8") as f:
    humanities_data = json.load(f)

humanities_subject = humanities_data["subjects"][0]

# Check if humanities already exists
existing_humanities = next((s for s in content["subjects"] if s["id"] == "humanities"), None)

if existing_humanities:
    print("⚠️  Humanities subject already exists. Replacing with new version...")
    content["subjects"] = [s for s in content["subjects"] if s["id"] != "humanities"]

# Add Humanities subject
content["subjects"].append(humanities_subject)

# Save updated content.json
with open("src/data/content.json", "w", encoding="utf-8") as f:
    json.dump(content, f, ensure_ascii=False, indent=2)

print(f"\n✅ Humanities integrated into content.json!")
print(f"📚 Subject: {humanities_subject['title']}")
print(f"📖 Total chapters: {len(humanities_subject['chapters'])}")
print(f"✏️  Total exercises: {sum(len(ch['exercises']) for ch in humanities_subject['chapters'])}")
print("\nChapter breakdown:")
for ch in humanities_subject["chapters"]:
    print(f"  - {ch['title']} ({ch['tag']}): {len(ch['sections'])} sections, {len(ch['exercises'])} exercises")
