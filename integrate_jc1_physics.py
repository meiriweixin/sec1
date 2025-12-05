#!/usr/bin/env python3
"""
Integration script for JC 1 Physics (lessons only, exercises to be added later)
Adds Physics as a new subject in content.json
"""

import json
from datetime import datetime

def main():
    # Create backup
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f'src/data/content-backup-physics-integration-{timestamp}.json'

    print("JC 1 Physics Integration (Lessons Only)")
    print("=" * 60)

    # Load main content and create backup
    print(f"\n1. Creating backup: {backup_file}")
    with open('src/data/content.json', 'r', encoding='utf-8') as f:
        content = json.load(f)

    with open(backup_file, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    print("   ✓ Backup created")

    # Load JC 1 Physics chapters
    print("\n2. Loading JC 1 Physics chapters")
    with open('chapters/jc1_physics_chapters.json', 'r', encoding='utf-8') as f:
        physics_chapters = json.load(f)

    total_sections = sum(len(ch.get('sections', [])) for ch in physics_chapters)
    total_exercises = sum(len(ch.get('exercises', [])) for ch in physics_chapters)
    print(f"   ✓ Loaded {len(physics_chapters)} chapters")
    print(f"   ✓ Total sections: {total_sections}")
    print(f"   ✓ Total exercises: {total_exercises}")

    # Create new Physics subject
    print("\n3. Creating Physics (H2) subject")
    physics_subject = {
        "id": "physics-jc",
        "title": "Physics (H2)",
        "title_zh": "物理 (H2)",
        "description": "H2 Physics for Singapore A-Level - comprehensive lessons covering measurement, mechanics, electricity, and waves",
        "description_zh": "新加坡A水准H2物理 - 涵盖测量、力学、电学和波的综合课程",
        "color": "from-blue-500 to-cyan-500",
        "chapters": physics_chapters
    }

    # Check if Physics subject already exists
    physics_exists = any(subj['id'] == 'physics-jc' for subj in content['subjects'])

    if physics_exists:
        print("   ⚠ Physics subject already exists - updating chapters")
        for i, subject in enumerate(content['subjects']):
            if subject['id'] == 'physics-jc':
                content['subjects'][i] = physics_subject
                break
    else:
        print("   ✓ Adding new Physics subject")
        content['subjects'].append(physics_subject)

    # Save updated content
    print("\n4. Saving updated content.json")
    with open('src/data/content.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    print("   ✓ Saved successfully")

    # Final verification
    print("\n5. Verification")
    with open('src/data/content.json', 'r', encoding='utf-8') as f:
        verify_content = json.load(f)

    total_subjects = len(verify_content['subjects'])
    total_chapters = sum(len(subj['chapters']) for subj in verify_content['subjects'])
    total_all_exercises = sum(
        len(ex)
        for subj in verify_content['subjects']
        for ch in subj['chapters']
        for ex in [ch.get('exercises', [])]
    )

    print(f"   Platform statistics:")
    print(f"   - Total subjects: {total_subjects}")
    print(f"   - Total chapters: {total_chapters}")
    print(f"   - Total exercises: {total_all_exercises}")

    # Find and display Physics subject
    for subject in verify_content['subjects']:
        if subject['id'] == 'physics-jc':
            physics_ch_count = len(subject['chapters'])
            physics_sec_count = sum(len(ch.get('sections', [])) for ch in subject['chapters'])
            physics_ex_count = sum(len(ch.get('exercises', [])) for ch in subject['chapters'])

            print(f"\n   Physics (H2) subject:")
            print(f"   - Chapters: {physics_ch_count}")
            print(f"   - Sections: {physics_sec_count}")
            print(f"   - Exercises: {physics_ex_count} (to be added later)")

            print(f"\n   Physics chapters:")
            for i, ch in enumerate(subject['chapters'], 1):
                sec_count = len(ch.get('sections', []))
                print(f"   {i}. {ch['title']} - {sec_count} sections")
            break

    print("\n" + "=" * 60)
    print("✅ JC 1 Physics integration COMPLETE!")
    print(f"   Students can now study {total_sections} lesson sections")
    print(f"   Exercises to be added in future batches")
    print(f"   Backup saved: {backup_file}")
    print("=" * 60)

if __name__ == "__main__":
    main()
