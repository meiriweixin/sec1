#!/usr/bin/env python3
"""
Update exam prep chapters to use 'olevel' and 'alevel' grade levels
instead of 'sec4' and 'jc2'.
"""

import json
from datetime import datetime
import shutil

def main():
    content_path = "src/data/content.json"

    # Create backup
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"src/data/content-backup-grade-update-{timestamp}.json"
    shutil.copy2(content_path, backup_path)
    print(f"📦 Created backup: {backup_path}")

    # Load content
    with open(content_path, 'r', encoding='utf-8') as f:
        content = json.load(f)

    # O-Level exam prep chapter IDs (should be gradeLevel: 'olevel')
    olevel_chapter_ids = [
        "olevel-english-paper1-prep",
        "olevel-english-paper2-prep",
        "olevel-english-oral-listening-prep",
        "olevel-chinese-paper1-prep",
        "olevel-chinese-paper2-prep",
        "olevel-chinese-oral-listening-prep",
        "olevel-math-algebra-prep",
        "olevel-math-geometry-prep",
        "olevel-math-stats-prep",
        "olevel-science-physics-prep",
        "olevel-science-chemistry-prep",
        "olevel-science-biology-prep",
        "olevel-computing-prep",
    ]

    # A-Level exam prep chapter IDs (should be gradeLevel: 'alevel')
    alevel_chapter_ids = [
        "alevel-math-paper1-prep",
        "alevel-math-paper2-prep",
        "alevel-math-exam-strategies",
        "alevel-physics-paper1-prep",
        "alevel-physics-paper2-prep",
        "alevel-physics-paper3-prep",
        "alevel-chemistry-paper1-prep",
        "alevel-chemistry-paper2-prep",
        "alevel-chemistry-paper3-prep",
    ]

    updated_count = {"olevel": 0, "alevel": 0}

    for subject in content["subjects"]:
        for chapter in subject["chapters"]:
            if chapter["id"] in olevel_chapter_ids:
                old_grade = chapter.get("gradeLevel", "none")
                chapter["gradeLevel"] = "olevel"
                print(f"   ✅ {chapter['id']}: {old_grade} → olevel")
                updated_count["olevel"] += 1
            elif chapter["id"] in alevel_chapter_ids:
                old_grade = chapter.get("gradeLevel", "none")
                chapter["gradeLevel"] = "alevel"
                print(f"   ✅ {chapter['id']}: {old_grade} → alevel")
                updated_count["alevel"] += 1

    # Save updated content
    with open(content_path, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Update complete!")
    print(f"   - O-Level chapters updated: {updated_count['olevel']}")
    print(f"   - A-Level chapters updated: {updated_count['alevel']}")

if __name__ == "__main__":
    main()
