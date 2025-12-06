#!/usr/bin/env python3
import json

with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Checking for placeholder exercises...")
placeholder_chapters = []

for subject in data['subjects']:
    for chapter in subject['chapters']:
        exercises = chapter.get('exercises', [])
        if exercises:
            first_ex = exercises[0]
            choices = first_ex.get('choices', [])
            prompt = first_ex.get('prompt', '')
            
            # Check for placeholders
            if 'Option A' in str(choices) or 'Option B' in str(choices):
                placeholder_chapters.append((subject['id'], chapter['id'], chapter['title']))
            elif 'concept question' in prompt.lower():
                placeholder_chapters.append((subject['id'], chapter['id'], chapter['title']))

if placeholder_chapters:
    print(f"\nChapters with placeholder exercises ({len(placeholder_chapters)}):")
    for subj, ch_id, title in placeholder_chapters:
        print(f"  [{subj}] {ch_id}: {title}")
else:
    print("\nNo placeholder exercises found!")

