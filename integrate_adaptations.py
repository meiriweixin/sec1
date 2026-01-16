#!/usr/bin/env python3
"""
Integration script for Secondary 1 Adaptations Biology chapter
Adds the Adaptations chapter to the Science subject in content.json
"""

import json
import os
from datetime import datetime

def create_backup(filename):
    """Create a timestamped backup of content.json"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"src/data/content-backup-adaptations-{timestamp}.json"
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = json.load(f)
    
    with open(backup_filename, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Backup created: {backup_filename}")
    return backup_filename

def load_adaptations_chapter():
    """Load the Adaptations chapter from JSON file"""
    chapter_file = "chapters/sec1_adaptations_chapter.json"
    
    if not os.path.exists(chapter_file):
        raise FileNotFoundError(f"Chapter file not found: {chapter_file}")
    
    with open(chapter_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    return data['chapter']

def integrate_chapter():
    """Integrate the Adaptations chapter into content.json"""
    content_file = "src/data/content.json"
    
    # Create backup first
    print("Creating backup of content.json...")
    backup_file = create_backup(content_file)
    
    # Load main content file
    print("Loading content.json...")
    with open(content_file, 'r', encoding='utf-8') as f:
        content = json.load(f)
    
    # Load adaptations chapter
    print("Loading Adaptations chapter...")
    adaptations_chapter = load_adaptations_chapter()
    
    # Find the Science subject
    science_subject = None
    for subject in content['subjects']:
        if subject['id'] == 'science':
            science_subject = subject
            break
    
    if not science_subject:
        raise ValueError("Science subject not found in content.json")
    
    # Check if chapter already exists
    existing_chapter = None
    for i, chapter in enumerate(science_subject['chapters']):
        if chapter['id'] == 'adaptations':
            existing_chapter = i
            break
    
    if existing_chapter is not None:
        print(f"⚠️  Adaptations chapter already exists at index {existing_chapter}")
        print("Replacing existing chapter...")
        science_subject['chapters'][existing_chapter] = adaptations_chapter
    else:
        print("Adding new Adaptations chapter...")
        # Find the position after all Sec 1 Biology chapters
        # We want to add it after the last Sec 1 Biology chapter
        insert_position = 0
        for i, chapter in enumerate(science_subject['chapters']):
            if chapter.get('gradeLevel') == 'sec1' and chapter.get('tag') == 'Biology':
                insert_position = i + 1
        
        science_subject['chapters'].insert(insert_position, adaptations_chapter)
    
    # Save updated content
    print("Saving updated content.json...")
    with open(content_file, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    
    # Verify the integration
    print("\n✅ Integration complete!")
    print(f"✅ Chapter ID: {adaptations_chapter['id']}")
    print(f"✅ Chapter Title: {adaptations_chapter['title']} / {adaptations_chapter['title_zh']}")
    print(f"✅ Grade Level: {adaptations_chapter['gradeLevel']}")
    print(f"✅ Tag: {adaptations_chapter['tag']} / {adaptations_chapter['tag_zh']}")
    print(f"✅ Sections: {len(adaptations_chapter['sections'])}")
    print(f"✅ Exercises: {len(adaptations_chapter['exercises'])}")
    
    # Count Sec 1 Biology chapters
    sec1_bio_chapters = [
        ch for ch in science_subject['chapters']
        if ch.get('gradeLevel') == 'sec1' and ch.get('tag') == 'Biology'
    ]
    
    print(f"\n📊 Total Sec 1 Biology chapters in Science subject: {len(sec1_bio_chapters)}")
    print("\nSec 1 Biology chapters:")
    for i, ch in enumerate(sec1_bio_chapters, 1):
        print(f"  {i}. {ch['title']} ({ch['id']})")
    
    return True

if __name__ == "__main__":
    try:
        print("=" * 60)
        print("Secondary 1 Adaptations Chapter Integration")
        print("=" * 60)
        print()
        
        integrate_chapter()
        
        print("\n" + "=" * 60)
        print("✅ SUCCESS: Adaptations chapter integrated successfully!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ ERROR: Integration failed!")
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        exit(1)
