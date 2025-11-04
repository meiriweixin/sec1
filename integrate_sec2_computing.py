"""
Integrate Secondary 2 Computing chapters into content.json
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

    # Load new Sec 2 Computing chapters
    with open("chapters/computing-sec2-chapters.json", "r", encoding="utf-8") as f:
        sec2_chapters = json.load(f)

    print(f"\n📚 Loaded {len(sec2_chapters)} Secondary 2 Computing chapters")

    # Find Computing subject
    computing_subject = None
    for subject in data["subjects"]:
        if subject["id"] == "computing":
            computing_subject = subject
            break

    if not computing_subject:
        print("❌ Error: Computing subject not found!")
        return

    # Count existing chapters by grade
    sec3_count = sum(1 for ch in computing_subject["chapters"] if ch.get("gradeLevel") == "sec3")
    sec2_count_before = sum(1 for ch in computing_subject["chapters"] if ch.get("gradeLevel") == "sec2")

    print(f"\n📊 Current Computing chapters:")
    print(f"  Sec 2: {sec2_count_before}")
    print(f"  Sec 3: {sec3_count}")

    # Remove any existing sec2 chapters, then add fresh ones
    computing_subject["chapters"] = [ch for ch in computing_subject["chapters"] if ch.get("gradeLevel") != "sec2"]
    computing_subject["chapters"] = sec2_chapters + computing_subject["chapters"]  # Sec2 first, then Sec3

    # Save updated content
    with open("src/data/content.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # Verify
    sec2_count_after = sum(1 for ch in computing_subject["chapters"] if ch.get("gradeLevel") == "sec2")
    total_chapters = len(computing_subject["chapters"])

    print(f"\n✅ Integration complete!")
    print(f"\n📊 Updated Computing chapters:")
    print(f"  Sec 2: {sec2_count_after}")
    print(f"  Sec 3: {sec3_count}")
    print(f"  Total: {total_chapters}")

    # Summary by tag
    ct = sum(1 for ch in computing_subject["chapters"] if ch.get("gradeLevel") == "sec2" and ch.get("tag") == "Computational Thinking")
    prog = sum(1 for ch in computing_subject["chapters"] if ch.get("gradeLevel") == "sec2" and ch.get("tag") == "Programming")
    web = sum(1 for ch in computing_subject["chapters"] if ch.get("gradeLevel") == "sec2" and ch.get("tag") == "Web Technologies")

    print(f"\n📊 Sec 2 breakdown:")
    print(f"  Computational Thinking: {ct}")
    print(f"  Programming: {prog}")
    print(f"  Web Technologies: {web}")

    # Count total exercises
    total_exercises = sum(len(ch["exercises"]) for ch in sec2_chapters)
    total_sections = sum(len(ch["sections"]) for ch in sec2_chapters)

    print(f"\n📊 Content stats:")
    print(f"  Total sections: {total_sections}")
    print(f"  Total exercises: {total_exercises}")

if __name__ == "__main__":
    main()
