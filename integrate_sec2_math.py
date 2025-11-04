"""
Integrate Secondary 2 Math chapters into content.json
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

    # Load new Sec 2 Math chapters
    with open("chapters/math-sec2-chapters.json", "r", encoding="utf-8") as f:
        sec2_chapters = json.load(f)

    print(f"\n📚 Loaded {len(sec2_chapters)} Secondary 2 Math chapters")

    # Find Math subject
    math_subject = None
    for subject in data["subjects"]:
        if subject["id"] == "math":
            math_subject = subject
            break

    if not math_subject:
        print("❌ Error: Math subject not found!")
        return

    # Count existing chapters by grade
    sec1_count = sum(1 for ch in math_subject["chapters"] if ch.get("gradeLevel") == "sec1")
    sec2_count_before = sum(1 for ch in math_subject["chapters"] if ch.get("gradeLevel") == "sec2")

    print(f"\n📊 Current Math chapters:")
    print(f"  Sec 1: {sec1_count}")
    print(f"  Sec 2: {sec2_count_before}")

    # Remove any existing sec2 chapters, then add fresh ones
    math_subject["chapters"] = [ch for ch in math_subject["chapters"] if ch.get("gradeLevel") != "sec2"]
    math_subject["chapters"].extend(sec2_chapters)

    # Save updated content
    with open("src/data/content.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # Verify
    sec2_count_after = sum(1 for ch in math_subject["chapters"] if ch.get("gradeLevel") == "sec2")
    total_chapters = len(math_subject["chapters"])

    print(f"\n✅ Integration complete!")
    print(f"\n📊 Updated Math chapters:")
    print(f"  Sec 1: {sec1_count}")
    print(f"  Sec 2: {sec2_count_after}")
    print(f"  Total: {total_chapters}")

    # Summary by tag
    algebra = sum(1 for ch in math_subject["chapters"] if ch.get("gradeLevel") == "sec2" and ch.get("tag") == "Algebra")
    geometry = sum(1 for ch in math_subject["chapters"] if ch.get("gradeLevel") == "sec2" and ch.get("tag") == "Geometry")
    statistics = sum(1 for ch in math_subject["chapters"] if ch.get("gradeLevel") == "sec2" and ch.get("tag") == "Statistics")

    print(f"\n📊 Sec 2 breakdown:")
    print(f"  Algebra: {algebra}")
    print(f"  Geometry: {geometry}")
    print(f"  Statistics: {statistics}")

    # Count total exercises
    total_exercises = sum(len(ch["exercises"]) for ch in sec2_chapters)
    total_sections = sum(len(ch["sections"]) for ch in sec2_chapters)

    print(f"\n📊 Content stats:")
    print(f"  Total sections: {total_sections}")
    print(f"  Total exercises: {total_exercises}")

if __name__ == "__main__":
    main()
