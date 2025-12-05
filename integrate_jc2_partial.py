#!/usr/bin/env python3
"""
Integrate JC 2 Mathematics Chapters 1-3 into content.json
Adds 45 exercises across 3 chapters to the main app
"""

import json
import shutil
from datetime import datetime

def integrate_jc2_chapters():
    """Integrate first 3 JC 2 chapters into main content"""

    # Create backup
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = f'src/data/content-backup-jc2-partial-{timestamp}.json'
    shutil.copy('src/data/content.json', backup_path)
    print(f"✓ Created backup: {backup_path}")

    # Load JC 2 chapters
    with open('chapters/jc2_math_chapters.json', 'r', encoding='utf-8') as f:
        jc2_chapters = json.load(f)

    # Load main content
    with open('src/data/content.json', 'r', encoding='utf-8') as f:
        content = json.load(f)

    # Find Mathematics subject
    math_subject = None
    for subject in content['subjects']:
        if subject['id'] == 'math':
            math_subject = subject
            break

    if not math_subject:
        print("✗ Error: Mathematics subject not found in content.json")
        return

    # Get only chapters 1-3 (indices 0-2)
    chapters_to_add = jc2_chapters[:3]

    # Check which chapters already exist
    existing_chapter_ids = {ch['id'] for ch in math_subject['chapters']}
    new_chapters = []
    updated_chapters = []

    for chapter in chapters_to_add:
        chapter_id = chapter['id']
        if chapter_id in existing_chapter_ids:
            # Update existing chapter
            for i, existing_ch in enumerate(math_subject['chapters']):
                if existing_ch['id'] == chapter_id:
                    math_subject['chapters'][i] = chapter
                    updated_chapters.append(chapter['title'])
                    break
        else:
            # Add new chapter
            math_subject['chapters'].append(chapter)
            new_chapters.append(chapter['title'])

    # Save updated content
    with open('src/data/content.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)

    # Report results
    print("\n✓ JC 2 Mathematics integration complete!")
    print(f"\n📊 Summary:")
    print(f"  Chapters added: {len(new_chapters)}")
    print(f"  Chapters updated: {len(updated_chapters)}")

    if new_chapters:
        print(f"\n  New chapters:")
        for title in new_chapters:
            print(f"    - {title}")

    if updated_chapters:
        print(f"\n  Updated chapters:")
        for title in updated_chapters:
            print(f"    - {title}")

    # Count total exercises
    total_exercises = sum(len(ch.get('exercises', [])) for ch in chapters_to_add)
    print(f"\n  Total exercises added: {total_exercises}")

    # Verify in content.json
    jc2_math_chapters = [ch for ch in math_subject['chapters'] if ch.get('gradeLevel') == 'jc2']
    print(f"\n  JC 2 Mathematics chapters in app: {len(jc2_math_chapters)}")

    print("\n✓ Integration successful!")
    print("  Run 'npm run dev' to test in the app")

if __name__ == '__main__':
    integrate_jc2_chapters()
