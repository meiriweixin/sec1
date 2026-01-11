#!/usr/bin/env python3
"""
Integrate Geography Sec 1 into main content.json
- Creates automatic backup
- Adds Geography as a new subject
- Appends all 4 Geography chapters with exercises
"""

import json
from datetime import datetime
import shutil

def create_backup(source_file):
    """Create timestamped backup"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = f'src/data/content-backup-geography-sec1-{timestamp}.json'
    shutil.copy2(source_file, backup_file)
    print(f"✓ Backup created: {backup_file}")
    return backup_file

def main():
    print("=" * 70)
    print("GEOGRAPHY SEC 1 INTEGRATION")
    print("=" * 70)

    # Paths
    main_content_path = 'src/data/content.json'
    geography_chapters_path = 'chapters/geography-sec1-chapters.json'

    # Step 1: Create backup
    print("\n[1/5] Creating backup...")
    backup_file = create_backup(main_content_path)

    # Step 2: Load existing content
    print("\n[2/5] Loading existing content.json...")
    with open(main_content_path, 'r', encoding='utf-8') as f:
        main_data = json.load(f)

    print(f"  Current subjects: {len(main_data['subjects'])}")
    existing_subject_ids = [s['id'] for s in main_data['subjects']]
    print(f"  Existing IDs: {', '.join(existing_subject_ids)}")

    # Step 3: Load Geography chapters
    print("\n[3/5] Loading Geography chapters...")
    with open(geography_chapters_path, 'r', encoding='utf-8') as f:
        geography_data = json.load(f)

    chapters = geography_data['chapters']
    print(f"  Loaded {len(chapters)} Geography chapters")
    for ch in chapters:
        print(f"    - {ch['title']} ({len(ch['exercises'])} exercises)")

    # Step 4: Create Geography subject
    print("\n[4/5] Creating Geography subject...")

    # Check if geography already exists
    existing_geo = next((s for s in main_data['subjects'] if s['id'] == 'geography'), None)

    if existing_geo:
        print("  ⚠ Geography subject already exists - will append chapters")
        geography_subject = existing_geo
        initial_chapter_count = len(geography_subject.get('chapters', []))
    else:
        print("  Creating new Geography subject...")
        geography_subject = {
            "id": "geography",
            "title": "Geography",
            "title_zh": "地理",
            "description": "Understanding the world around us: physical features, human activities, and environmental interactions",
            "description_zh": "理解我们周围的世界：自然特征、人类活动和环境互动",
            "color": "from-green-600 to-emerald-600",
            "chapters": []
        }
        main_data['subjects'].append(geography_subject)
        initial_chapter_count = 0

    # Step 5: Add chapters to Geography subject
    print("\n[5/5] Adding chapters to Geography subject...")

    if initial_chapter_count == 0:
        geography_subject['chapters'] = chapters
        print(f"  ✓ Added all {len(chapters)} chapters")
    else:
        # REPLACE all chapters with the source file (to maintain correct order)
        geography_subject['chapters'] = chapters
        print(f"  ✓ Replaced all chapters with corrected structure")
        print(f"  ✓ Total Geography chapters: {len(geography_subject['chapters'])}")

    # Save updated content
    print("\n[6/5] Saving updated content.json...")
    with open(main_content_path, 'w', encoding='utf-8') as f:
        json.dump(main_data, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 70)
    print("✓ SUCCESS! Geography Sec 1 integrated into content.json")
    print("=" * 70)

    # Final summary
    print("\nFinal Summary:")
    print(f"  Total subjects: {len(main_data['subjects'])}")

    geography_final = next(s for s in main_data['subjects'] if s['id'] == 'geography')
    total_exercises = sum(len(ch.get('exercises', [])) for ch in geography_final['chapters'])

    print(f"\n  Geography:")
    print(f"    Chapters: {len(geography_final['chapters'])}")
    print(f"    Total Exercises: {total_exercises}")

    for ch in geography_final['chapters']:
        print(f"      - {ch['title']}: {len(ch.get('exercises', []))} exercises")

    print(f"\nBackup saved at: {backup_file}")
    print("\nNext step: Test Geography content in the app (npm run dev)")

if __name__ == "__main__":
    main()
