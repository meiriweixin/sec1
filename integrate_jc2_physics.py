#!/usr/bin/env python3
"""
Integration script for JC2 Physics into main content.json
Adds JC2 Physics as a new subject with 8 chapters
"""
import json
from datetime import datetime
import shutil

# Create backup
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
backup_file = f'src/data/content-backup-jc2-physics-{timestamp}.json'
shutil.copy('src/data/content.json', backup_file)
print(f"✓ Created backup: {backup_file}")

# Load JC2 Physics chapters
with open('chapters/jc2_physics_chapters.json', 'r', encoding='utf-8') as f:
    jc2_physics_chapters = json.load(f)

print(f"✓ Loaded {len(jc2_physics_chapters)} JC2 Physics chapters")

# Count exercises
total_exercises = sum(len(ch.get('exercises', [])) for ch in jc2_physics_chapters)
print(f"✓ Total exercises: {total_exercises}")

# Load main content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    content = json.load(f)

# Check if physics-jc subject already exists
physics_exists = any(s['id'] == 'physics-jc' for s in content['subjects'])

if physics_exists:
    # Update existing
    for subject in content['subjects']:
        if subject['id'] == 'physics-jc':
            # Find JC2 chapters and update them
            jc2_ids = [ch['id'] for ch in jc2_physics_chapters]
            # Remove old JC2 chapters
            subject['chapters'] = [ch for ch in subject['chapters'] if ch['id'] not in jc2_ids]
            # Add new JC2 chapters
            subject['chapters'].extend(jc2_physics_chapters)
            print(f"✓ Updated physics-jc subject with {len(jc2_physics_chapters)} JC2 chapters")
else:
    # Create new physics-jc subject
    physics_subject = {
        "id": "physics-jc",
        "title": "Physics (H2)",
        "title_zh": "物理 (H2)",
        "description": "H2 Physics for Singapore A-Level (JC 1-2)",
        "description_zh": "新加坡A水准H2物理（初院1-2年级）",
        "color": "from-blue-500 to-cyan-500",
        "chapters": jc2_physics_chapters
    }
    content['subjects'].append(physics_subject)
    print(f"✓ Created new physics-jc subject with {len(jc2_physics_chapters)} chapters")

# Save updated content
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(content, f, ensure_ascii=False, indent=2)

print(f"\n✅ Integration complete!")
print(f"   Backup saved: {backup_file}")
print(f"   JC2 Physics chapters added: {len(jc2_physics_chapters)}")
print(f"   JC2 Physics exercises: {total_exercises}")
print(f"\nNext steps:")
print(f"1. Run 'npm run dev' to test")
print(f"2. Select JC2 grade level")
print(f"3. Navigate to Physics subject")
print(f"4. Verify all 8 chapters appear correctly")
