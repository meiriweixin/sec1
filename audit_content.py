#!/usr/bin/env python3
"""Comprehensive audit of all content by grade level and subject."""
import json

with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Define expected structure
GRADE_LEVELS = ['sec1', 'sec2', 'sec3', 'sec4', 'jc1', 'jc2', 'olevel', 'alevel']

EXPECTED_SUBJECTS = {
    'sec1': ['english', 'chinese', 'math', 'science', 'computing'],
    'sec2': ['english', 'chinese', 'math', 'science', 'computing'],
    'sec3': ['english', 'chinese', 'math', 'science', 'computing'],
    'sec4': ['english', 'chinese', 'math', 'science'],
    'jc1': ['math', 'physics-jc', 'chemistry-jc', 'biology-jc', 'gp', 'economics-jc'],
    'jc2': ['math', 'physics-jc', 'chemistry-jc', 'biology-jc', 'gp', 'economics-jc'],
    'olevel': ['english', 'chinese', 'math', 'science', 'computing'],
    'alevel': ['math', 'physics-jc', 'chemistry-jc', 'biology-jc', 'gp', 'economics-jc'],
}

# Collect data by grade and subject
content_map = {grade: {} for grade in GRADE_LEVELS}

for subject in data['subjects']:
    subj_id = subject['id']
    subj_title = subject['title']
    
    for chapter in subject['chapters']:
        grade = chapter.get('gradeLevel', 'unknown')
        if grade not in content_map:
            content_map[grade] = {}
        
        if subj_id not in content_map[grade]:
            content_map[grade][subj_id] = {
                'title': subj_title,
                'chapters': [],
                'total_exercises': 0,
                'chapters_without_exercises': 0,
                'chapters_without_sections': 0
            }
        
        ex_count = len(chapter.get('exercises', []))
        sec_count = len(chapter.get('sections', []))
        
        content_map[grade][subj_id]['chapters'].append({
            'id': chapter['id'],
            'title': chapter['title'],
            'exercises': ex_count,
            'sections': sec_count
        })
        content_map[grade][subj_id]['total_exercises'] += ex_count
        
        if ex_count == 0:
            content_map[grade][subj_id]['chapters_without_exercises'] += 1
        if sec_count == 0:
            content_map[grade][subj_id]['chapters_without_sections'] += 1

# Print report
print("=" * 80)
print("COMPREHENSIVE CONTENT AUDIT")
print("=" * 80)

total_chapters = 0
total_exercises = 0
issues = []

for grade in GRADE_LEVELS:
    print(f"\n{'=' * 80}")
    print(f"GRADE LEVEL: {grade.upper()}")
    print(f"{'=' * 80}")
    
    expected = EXPECTED_SUBJECTS.get(grade, [])
    actual = content_map.get(grade, {})
    
    # Check for missing subjects
    missing_subjects = [s for s in expected if s not in actual]
    if missing_subjects:
        print(f"\n⚠️  MISSING SUBJECTS: {', '.join(missing_subjects)}")
        for ms in missing_subjects:
            issues.append(f"{grade.upper()}: Missing subject '{ms}'")
    
    if not actual:
        print("\n  No content found for this grade level!")
        issues.append(f"{grade.upper()}: No content at all")
        continue
    
    for subj_id, subj_data in actual.items():
        ch_count = len(subj_data['chapters'])
        ex_count = subj_data['total_exercises']
        no_ex = subj_data['chapters_without_exercises']
        no_sec = subj_data['chapters_without_sections']
        
        total_chapters += ch_count
        total_exercises += ex_count
        
        # Determine status
        status = "✅"
        notes = []
        
        if no_ex > 0:
            status = "⚠️"
            notes.append(f"{no_ex} ch without exercises")
            issues.append(f"{grade.upper()} {subj_id}: {no_ex} chapters without exercises")
        
        if no_sec > 0:
            status = "⚠️"
            notes.append(f"{no_sec} ch without sections")
            issues.append(f"{grade.upper()} {subj_id}: {no_sec} chapters without lessons")
        
        if ch_count < 3:
            notes.append("few chapters")
        
        note_str = f" ({', '.join(notes)})" if notes else ""
        
        print(f"\n  {status} [{subj_id}] {subj_data['title']}")
        print(f"     Chapters: {ch_count} | Exercises: {ex_count}{note_str}")
        
        # List chapters if there are issues
        if no_ex > 0 or no_sec > 0:
            for ch in subj_data['chapters']:
                if ch['exercises'] == 0 or ch['sections'] == 0:
                    ex_status = "❌ no ex" if ch['exercises'] == 0 else f"{ch['exercises']} ex"
                    sec_status = "❌ no sec" if ch['sections'] == 0 else f"{ch['sections']} sec"
                    print(f"        - {ch['title']}: {sec_status}, {ex_status}")

# Summary
print(f"\n{'=' * 80}")
print("SUMMARY")
print("=" * 80)
print(f"\nTotal Chapters: {total_chapters}")
print(f"Total Exercises: {total_exercises}")

if issues:
    print(f"\n⚠️  ISSUES FOUND ({len(issues)}):")
    for issue in issues:
        print(f"   - {issue}")
else:
    print("\n✅ All content is complete!")

# Subject coverage matrix
print(f"\n{'=' * 80}")
print("SUBJECT COVERAGE MATRIX")
print("=" * 80)
print(f"\n{'Subject':<20}", end="")
for grade in GRADE_LEVELS:
    print(f"{grade:>8}", end="")
print()
print("-" * 84)

all_subjects = set()
for grade_data in content_map.values():
    all_subjects.update(grade_data.keys())

for subj in sorted(all_subjects):
    # Get subject title
    title = subj
    for s in data['subjects']:
        if s['id'] == subj:
            title = s['title'][:18]
            break
    
    print(f"{title:<20}", end="")
    for grade in GRADE_LEVELS:
        if subj in content_map.get(grade, {}):
            ch_count = len(content_map[grade][subj]['chapters'])
            print(f"{ch_count:>8}", end="")
        else:
            print(f"{'--':>8}", end="")
    print()

