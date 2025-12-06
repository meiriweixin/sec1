#!/usr/bin/env python3
"""Integrate Sec 3 and Sec 4 English and Chinese chapters into content.json."""
import json
import os
from datetime import datetime

def backup_content():
    """Create a backup of content.json."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = f'src/data/content-backup-languages-{timestamp}.json'
    with open('src/data/content.json', 'r', encoding='utf-8') as f:
        content = json.load(f)
    with open(backup_path, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    print(f"Created backup: {backup_path}")
    return content

def load_chapters(filepath):
    """Load chapters from a JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def find_subject(content, subject_id):
    """Find a subject by ID."""
    for subject in content['subjects']:
        if subject['id'] == subject_id:
            return subject
    return None

def main():
    print("=" * 60)
    print("Integrating Sec 3 and Sec 4 English and Chinese chapters")
    print("=" * 60)
    
    # First, run the creation scripts
    print("\n1. Running chapter creation scripts...")
    os.system('python create_sec3_english.py')
    os.system('python create_sec3_english_part2.py')
    os.system('python create_sec3_chinese.py')
    os.system('python create_sec4_languages.py')
    
    # Create backup and load content
    print("\n2. Creating backup and loading content.json...")
    content = backup_content()
    
    # Load all chapter files
    print("\n3. Loading chapter files...")
    sec3_eng_1 = load_chapters('chapters/sec3_english_chapters.json')
    sec3_eng_2 = load_chapters('chapters/sec3_english_chapters_part2.json')
    sec3_chinese = load_chapters('chapters/sec3_chinese_chapters.json')
    sec4_english = load_chapters('chapters/sec4_english_chapters.json')
    sec4_chinese = load_chapters('chapters/sec4_chinese_chapters.json')
    
    # Combine Sec 3 English chapters
    sec3_english = sec3_eng_1 + sec3_eng_2
    
    print(f"   - Sec 3 English: {len(sec3_english)} chapters")
    print(f"   - Sec 3 Chinese: {len(sec3_chinese)} chapters")
    print(f"   - Sec 4 English: {len(sec4_english)} chapters")
    print(f"   - Sec 4 Chinese: {len(sec4_chinese)} chapters")
    
    # Find subjects
    english_subject = find_subject(content, 'english')
    chinese_subject = find_subject(content, 'chinese')
    
    if not english_subject:
        print("ERROR: English subject not found!")
        return
    if not chinese_subject:
        print("ERROR: Chinese subject not found!")
        return
    
    # Get existing chapter IDs to avoid duplicates
    existing_eng_ids = {ch['id'] for ch in english_subject['chapters']}
    existing_chi_ids = {ch['id'] for ch in chinese_subject['chapters']}
    
    # Add new chapters
    print("\n4. Adding new chapters...")
    
    # Add Sec 3 English
    added_eng_3 = 0
    for ch in sec3_english:
        if ch['id'] not in existing_eng_ids:
            english_subject['chapters'].append(ch)
            added_eng_3 += 1
    print(f"   - Added {added_eng_3} Sec 3 English chapters")
    
    # Add Sec 4 English
    added_eng_4 = 0
    for ch in sec4_english:
        if ch['id'] not in existing_eng_ids:
            english_subject['chapters'].append(ch)
            added_eng_4 += 1
    print(f"   - Added {added_eng_4} Sec 4 English chapters")
    
    # Add Sec 3 Chinese
    added_chi_3 = 0
    for ch in sec3_chinese:
        if ch['id'] not in existing_chi_ids:
            chinese_subject['chapters'].append(ch)
            added_chi_3 += 1
    print(f"   - Added {added_chi_3} Sec 3 Chinese chapters")
    
    # Add Sec 4 Chinese
    added_chi_4 = 0
    for ch in sec4_chinese:
        if ch['id'] not in existing_chi_ids:
            chinese_subject['chapters'].append(ch)
            added_chi_4 += 1
    print(f"   - Added {added_chi_4} Sec 4 Chinese chapters")
    
    # Save updated content
    print("\n5. Saving updated content.json...")
    with open('src/data/content.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    
    # Summary
    print("\n" + "=" * 60)
    print("INTEGRATION COMPLETE!")
    print("=" * 60)
    print(f"\nTotal chapters added:")
    print(f"  - English: {added_eng_3 + added_eng_4} chapters ({added_eng_3} Sec 3 + {added_eng_4} Sec 4)")
    print(f"  - Chinese: {added_chi_3 + added_chi_4} chapters ({added_chi_3} Sec 3 + {added_chi_4} Sec 4)")
    print(f"\nTotal English chapters now: {len(english_subject['chapters'])}")
    print(f"Total Chinese chapters now: {len(chinese_subject['chapters'])}")
    
    # Calculate exercises
    total_exercises = sum(len(ch.get('exercises', [])) for ch in sec3_english + sec4_english + sec3_chinese + sec4_chinese)
    print(f"\nTotal new exercises: {total_exercises}")
    
    print("\nPlease run 'npm run dev' to test the changes!")

if __name__ == "__main__":
    main()

