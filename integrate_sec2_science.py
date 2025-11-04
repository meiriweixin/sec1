"""
Integrate Secondary 2 Science chapters into content.json
Creates backup before integration
"""

import json
import shutil
from datetime import datetime

def main():
    # Backup original file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"src/data/content-backup-{timestamp}.json"
    shutil.copy("src/data/content.json", backup_file)
    print(f"✅ Backup created: {backup_file}")

    # Load existing content
    with open("src/data/content.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Load new Sec 2 chapters
    with open("chapters/science-sec2-chapters.json", "r", encoding="utf-8") as f:
        sec2_chapters = json.load(f)

    print(f"\n📚 Loaded {len(sec2_chapters)} Secondary 2 Science chapters")

    # Find Science subject
    science_subject = None
    for subject in data["subjects"]:
        if subject["id"] == "science":
            science_subject = subject
            break

    if not science_subject:
        print("❌ Error: Science subject not found!")
        return

    # Count existing chapters by grade
    sec1_count = sum(1 for ch in science_subject["chapters"] if ch.get("gradeLevel") == "sec1")
    sec2_count_before = sum(1 for ch in science_subject["chapters"] if ch.get("gradeLevel") == "sec2")

    print(f"\n📊 Current Science chapters:")
    print(f"  Sec 1: {sec1_count}")
    print(f"  Sec 2: {sec2_count_before}")

    # Add Sec 2 chapters
    science_subject["chapters"].extend(sec2_chapters)

    # Save updated content
    with open("src/data/content.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # Verify
    sec2_count_after = sum(1 for ch in science_subject["chapters"] if ch.get("gradeLevel") == "sec2")
    total_chapters = len(science_subject["chapters"])

    print(f"\n✅ Integration complete!")
    print(f"\n📊 Updated Science chapters:")
    print(f"  Sec 1: {sec1_count}")
    print(f"  Sec 2: {sec2_count_after}")
    print(f"  Total: {total_chapters}")

    # Summary by tag
    chemistry = sum(1 for ch in science_subject["chapters"] if ch.get("gradeLevel") == "sec2" and ch.get("tag") == "Chemistry")
    physics = sum(1 for ch in science_subject["chapters"] if ch.get("gradeLevel") == "sec2" and ch.get("tag") == "Physics")
    biology = sum(1 for ch in science_subject["chapters"] if ch.get("gradeLevel") == "sec2" and ch.get("tag") == "Biology")

    print(f"\n📊 Sec 2 breakdown:")
    print(f"  Chemistry: {chemistry}")
    print(f"  Physics: {physics}")
    print(f"  Biology: {biology}")

    # Count total exercises
    total_exercises = sum(len(ch["exercises"]) for ch in sec2_chapters)
    total_sections = sum(len(ch["sections"]) for ch in sec2_chapters)

    print(f"\n📊 Content stats:")
    print(f"  Total sections: {total_sections}")
    print(f"  Total exercises: {total_exercises}")

if __name__ == "__main__":
    main()
