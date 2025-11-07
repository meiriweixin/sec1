#!/usr/bin/env python3
"""
Integrate Sec 3 Science chapters into content.json.
Creates backup before modifying.
"""

import json
import os
from datetime import datetime

def create_backup():
    """Create a backup of content.json with timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"src/data/content-backup-{timestamp}.json"

    with open('src/data/content.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(backup_filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Backup created: {backup_filename}")
    return backup_filename

def load_sec3_science_chapters():
    """Load all Sec 3 Science chapter files."""
    chapters = []
    chapters_dir = 'chapters'

    # Get all sec3-science files
    filenames = sorted([f for f in os.listdir(chapters_dir) if f.startswith('sec3-science-')])

    for filename in filenames:
        filepath = os.path.join(chapters_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            chapter = json.load(f)
            chapters.append(chapter)
            print(f"Loaded: {chapter['title']} ({chapter['tag']})")

    return chapters

def integrate_chapters():
    """Integrate Sec 3 Science chapters into content.json."""

    # Create backup first
    create_backup()

    # Load existing content
    with open('src/data/content.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Find Science subject
    science_subject = None
    for subject in data['subjects']:
        if subject['id'] == 'science':
            science_subject = subject
            break

    if not science_subject:
        print("❌ Error: Science subject not found!")
        return

    # Load new Sec 3 Science chapters
    print("\n📚 Loading Sec 3 Science chapters...")
    new_chapters = load_sec3_science_chapters()

    # Check for duplicates
    existing_ids = {ch['id'] for ch in science_subject['chapters']}
    new_chapter_ids = {ch['id'] for ch in new_chapters}
    duplicates = existing_ids & new_chapter_ids

    if duplicates:
        print(f"\n⚠️  Warning: Found duplicate chapter IDs: {duplicates}")
        print("Removing existing chapters with these IDs...")
        science_subject['chapters'] = [
            ch for ch in science_subject['chapters']
            if ch['id'] not in duplicates
        ]

    # Add new chapters
    science_subject['chapters'].extend(new_chapters)

    print(f"\n✅ Added {len(new_chapters)} Sec 3 Science chapters")

    # Count chapters by grade level
    chapters_by_grade = {}
    for chapter in science_subject['chapters']:
        grade = chapter.get('gradeLevel', 'unknown')
        chapters_by_grade[grade] = chapters_by_grade.get(grade, 0) + 1

    print("\n📊 Science chapters by grade level:")
    for grade in sorted(chapters_by_grade.keys()):
        print(f"  {grade}: {chapters_by_grade[grade]} chapters")

    # Save updated content
    with open('src/data/content.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Successfully integrated Sec 3 Science into content.json")
    print(f"Total Science chapters: {len(science_subject['chapters'])}")

if __name__ == "__main__":
    print("=" * 60)
    print("SEC 3 SCIENCE INTEGRATION")
    print("=" * 60)
    integrate_chapters()
    print("\n" + "=" * 60)
    print("Integration complete! Test with: npm run dev")
    print("=" * 60)
