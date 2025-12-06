#!/usr/bin/env python3
"""Check JC1, JC2, and A-Level content coverage."""
import json

with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Collect chapters by grade level
jc1_chapters = {}
jc2_chapters = {}
alevel_chapters = {}
olevel_chapters = {}

for subject in data['subjects']:
    subj_id = subject['id']
    subj_title = subject['title']
    
    for chapter in subject['chapters']:
        grade = chapter.get('gradeLevel', '')
        ch_info = (chapter['id'], chapter['title'], len(chapter.get('exercises', [])))
        
        if grade == 'jc1':
            if subj_id not in jc1_chapters:
                jc1_chapters[subj_id] = []
            jc1_chapters[subj_id].append(ch_info)
        elif grade == 'jc2':
            if subj_id not in jc2_chapters:
                jc2_chapters[subj_id] = []
            jc2_chapters[subj_id].append(ch_info)
        elif grade == 'alevel':
            if subj_id not in alevel_chapters:
                alevel_chapters[subj_id] = []
            alevel_chapters[subj_id].append(ch_info)
        elif grade == 'olevel':
            if subj_id not in olevel_chapters:
                olevel_chapters[subj_id] = []
            olevel_chapters[subj_id].append(ch_info)

print("=" * 70)
print("JC1 CONTENT")
print("=" * 70)
if jc1_chapters:
    for subj, chapters in jc1_chapters.items():
        print(f"\n[{subj}] - {len(chapters)} chapters")
        for ch_id, title, ex_count in chapters:
            print(f"  • {title} ({ex_count} exercises)")
else:
    print("No JC1 content found!")

print("\n" + "=" * 70)
print("JC2 CONTENT")
print("=" * 70)
if jc2_chapters:
    for subj, chapters in jc2_chapters.items():
        print(f"\n[{subj}] - {len(chapters)} chapters")
        for ch_id, title, ex_count in chapters:
            print(f"  • {title} ({ex_count} exercises)")
else:
    print("No JC2 content found!")

print("\n" + "=" * 70)
print("A-LEVEL EXAM PREP CONTENT")
print("=" * 70)
if alevel_chapters:
    for subj, chapters in alevel_chapters.items():
        print(f"\n[{subj}] - {len(chapters)} chapters")
        for ch_id, title, ex_count in chapters:
            print(f"  • {title} ({ex_count} exercises)")
else:
    print("No A-Level content found!")

print("\n" + "=" * 70)
print("O-LEVEL EXAM PREP CONTENT")
print("=" * 70)
if olevel_chapters:
    for subj, chapters in olevel_chapters.items():
        print(f"\n[{subj}] - {len(chapters)} chapters")
        for ch_id, title, ex_count in chapters:
            print(f"  • {title} ({ex_count} exercises)")
else:
    print("No O-Level content found!")

# List all subjects
print("\n" + "=" * 70)
print("ALL SUBJECTS IN THE APP")
print("=" * 70)
for subject in data['subjects']:
    print(f"  • {subject['id']}: {subject['title']}")

# Expected JC subjects
print("\n" + "=" * 70)
print("EXPECTED JC/A-LEVEL SUBJECTS (Singapore H2 Syllabus)")
print("=" * 70)
expected = [
    "Mathematics (H2)", "Physics (H2)", "Chemistry (H2)", "Biology (H2)",
    "Economics (H2)", "English Language", "Chinese Language", 
    "General Paper (GP)", "Project Work (PW)"
]
for e in expected:
    print(f"  • {e}")

# Summary
print("\n" + "=" * 70)
print("SUMMARY - MISSING CONTENT")
print("=" * 70)
print("\nJC1 subjects with content:", list(jc1_chapters.keys()) if jc1_chapters else "None")
print("JC2 subjects with content:", list(jc2_chapters.keys()) if jc2_chapters else "None")
print("A-Level subjects with content:", list(alevel_chapters.keys()) if alevel_chapters else "None")

