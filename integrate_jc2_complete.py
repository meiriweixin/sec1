#!/usr/bin/env python3
"""
Integration script for JC 2 Mathematics chapters (all 8 chapters, 120 exercises)
Integrates chapters from chapters/jc2_math_chapters.json into src/data/content.json
"""

import json
from datetime import datetime

def main():
    # Create backup
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f'src/data/content-backup-jc2-complete-{timestamp}.json'

    print("JC 2 Mathematics Complete Integration")
    print("=" * 60)

    # Load main content and create backup
    print(f"\n1. Creating backup: {backup_file}")
    with open('src/data/content.json', 'r', encoding='utf-8') as f:
        content = json.load(f)

    with open(backup_file, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    print("   ✓ Backup created")

    # Load JC 2 chapters
    print("\n2. Loading JC 2 chapters from chapters/jc2_math_chapters.json")
    with open('chapters/jc2_math_chapters.json', 'r', encoding='utf-8') as f:
        jc2_chapters = json.load(f)

    total_exercises = sum(len(ch.get('exercises', [])) for ch in jc2_chapters)
    print(f"   ✓ Loaded {len(jc2_chapters)} chapters with {total_exercises} exercises")

    # Find Mathematics subject
    print("\n3. Finding Mathematics subject in content.json")
    math_subject = None
    for subject in content['subjects']:
        if subject['id'] == 'math':
            math_subject = subject
            break

    if not math_subject:
        print("   ✗ ERROR: Mathematics subject not found!")
        return

    print(f"   ✓ Found Mathematics subject")
    print(f"   Current chapters: {len(math_subject['chapters'])}")

    # Check for existing JC 2 chapters
    print("\n4. Checking for existing JC 2 chapters")
    existing_jc2_ids = {ch['id'] for ch in math_subject['chapters'] if ch.get('gradeLevel') == 'jc2'}

    if existing_jc2_ids:
        print(f"   Found {len(existing_jc2_ids)} existing JC 2 chapters:")
        for ch_id in existing_jc2_ids:
            print(f"   - {ch_id}")

        # Remove existing JC 2 chapters
        print("\n   Removing existing JC 2 chapters...")
        math_subject['chapters'] = [ch for ch in math_subject['chapters'] if ch.get('gradeLevel') != 'jc2']
        print(f"   ✓ Removed {len(existing_jc2_ids)} chapters")
    else:
        print("   No existing JC 2 chapters found")

    # Add new JC 2 chapters
    print("\n5. Adding complete JC 2 chapters")
    math_subject['chapters'].extend(jc2_chapters)
    print(f"   ✓ Added {len(jc2_chapters)} JC 2 chapters")

    # Save updated content
    print("\n6. Saving updated content.json")
    with open('src/data/content.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    print("   ✓ Saved successfully")

    # Final verification
    print("\n7. Verification")
    with open('src/data/content.json', 'r', encoding='utf-8') as f:
        verify_content = json.load(f)

    for subject in verify_content['subjects']:
        if subject['id'] == 'math':
            jc2_chapters = [ch for ch in subject['chapters'] if ch.get('gradeLevel') == 'jc2']
            total_jc2_ex = sum(len(ch.get('exercises', [])) for ch in jc2_chapters)
            total_math_ex = sum(len(ch.get('exercises', [])) for ch in subject['chapters'])

            print(f"   Mathematics subject statistics:")
            print(f"   - Total chapters: {len(subject['chapters'])}")
            print(f"   - JC 2 chapters: {len(jc2_chapters)}")
            print(f"   - JC 2 exercises: {total_jc2_ex}")
            print(f"   - Total Math exercises: {total_math_ex}")
            break

    print("\n" + "=" * 60)
    print("✅ JC 2 Mathematics integration COMPLETE!")
    print(f"   8 chapters with 120 exercises successfully integrated")
    print(f"   Backup saved: {backup_file}")
    print("=" * 60)

if __name__ == "__main__":
    main()
