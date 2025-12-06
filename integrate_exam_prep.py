#!/usr/bin/env python3
"""
Integrate O-Level and A-Level exam preparation chapters into content.json.
"""

import json
from datetime import datetime
import shutil

def main():
    # Paths
    content_path = "src/data/content.json"
    olevel_path = "chapters/olevel_exam_prep_chapters.json"
    alevel_path = "chapters/alevel_exam_prep_chapters.json"

    # Create backup
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"src/data/content-backup-exam-prep-{timestamp}.json"
    shutil.copy2(content_path, backup_path)
    print(f"📦 Created backup: {backup_path}")

    # Load content
    with open(content_path, 'r', encoding='utf-8') as f:
        content = json.load(f)

    # Load O-Level chapters
    with open(olevel_path, 'r', encoding='utf-8') as f:
        olevel_chapters = json.load(f)

    # Load A-Level chapters
    with open(alevel_path, 'r', encoding='utf-8') as f:
        alevel_chapters = json.load(f)

    # Subject ID mapping
    subject_mapping = {
        "english": "english",
        "chinese": "chinese",
        "math": "math",
        "science": "science",
        "computing": "computing",
        "physics-jc": "physics-jc",
        "chemistry-jc": "chemistry-jc"
    }

    # Count chapters added
    chapters_added = {
        "olevel": 0,
        "alevel": 0
    }

    # Add O-Level chapters (Sec 4)
    print("\n📚 Adding O-Level exam prep chapters...")
    for subject_key, chapters in olevel_chapters.items():
        subject_id = subject_mapping.get(subject_key)
        if not subject_id:
            print(f"   ⚠️ Unknown subject: {subject_key}")
            continue

        # Find subject in content
        subject = next((s for s in content["subjects"] if s["id"] == subject_id), None)
        if not subject:
            print(f"   ⚠️ Subject not found in content: {subject_id}")
            continue

        # Check for existing chapters and add new ones
        existing_ids = [ch["id"] for ch in subject["chapters"]]
        for chapter in chapters:
            if chapter["id"] not in existing_ids:
                subject["chapters"].append(chapter)
                chapters_added["olevel"] += 1
                print(f"   ✅ Added: {chapter['title']} to {subject_id}")
            else:
                print(f"   ⏭️ Already exists: {chapter['id']}")

    # Add A-Level chapters (JC 2)
    print("\n📚 Adding A-Level exam prep chapters...")
    for subject_key, chapters in alevel_chapters.items():
        subject_id = subject_mapping.get(subject_key)
        if not subject_id:
            print(f"   ⚠️ Unknown subject: {subject_key}")
            continue

        # Find subject in content
        subject = next((s for s in content["subjects"] if s["id"] == subject_id), None)
        if not subject:
            print(f"   ⚠️ Subject not found in content: {subject_id}")
            continue

        # Check for existing chapters and add new ones
        existing_ids = [ch["id"] for ch in subject["chapters"]]
        for chapter in chapters:
            if chapter["id"] not in existing_ids:
                subject["chapters"].append(chapter)
                chapters_added["alevel"] += 1
                print(f"   ✅ Added: {chapter['title']} to {subject_id}")
            else:
                print(f"   ⏭️ Already exists: {chapter['id']}")

    # Save updated content
    with open(content_path, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Integration complete!")
    print(f"   - O-Level chapters added: {chapters_added['olevel']}")
    print(f"   - A-Level chapters added: {chapters_added['alevel']}")
    print(f"   - Total chapters added: {chapters_added['olevel'] + chapters_added['alevel']}")

    # Print summary by subject
    print("\n📊 Content Summary:")
    for subject in content["subjects"]:
        if subject["id"] in ["english", "chinese", "math", "science", "computing", "physics-jc", "chemistry-jc"]:
            total_chapters = len(subject["chapters"])
            sec4_chapters = len([ch for ch in subject["chapters"] if ch.get("gradeLevel") == "sec4"])
            jc2_chapters = len([ch for ch in subject["chapters"] if ch.get("gradeLevel") == "jc2"])
            print(f"   {subject['id']}: {total_chapters} total chapters (Sec 4: {sec4_chapters}, JC 2: {jc2_chapters})")

if __name__ == "__main__":
    main()
