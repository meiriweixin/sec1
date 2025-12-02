#!/usr/bin/env python3
"""
Comprehensive Exercise Content Analysis
"""

import json
from collections import defaultdict

with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('=' * 80)
print('COMPREHENSIVE EXERCISE ANALYSIS')
print('=' * 80)
print()

# Overall stats
total_exercises = 0
total_chapters = 0
exercise_types_global = defaultdict(int)
difficulty_global = defaultdict(int)

# Per subject analysis
for subject in data['subjects']:
    if subject['id'] == 'ai-playground':
        continue

    subject_name = subject['title']
    chapters = subject.get('chapters', [])

    print(f'📚 {subject_name}')
    print('-' * 80)

    subject_exercises = 0
    subject_types = defaultdict(int)
    subject_diff = defaultdict(int)
    chapters_with_ex = 0

    for chapter in chapters:
        total_chapters += 1
        exercises = chapter.get('exercises', [])

        if exercises:
            chapters_with_ex += 1
            subject_exercises += len(exercises)
            total_exercises += len(exercises)

            for ex in exercises:
                ex_type = ex.get('type', 'unknown')
                subject_types[ex_type] += 1
                exercise_types_global[ex_type] += 1

                diff = ex.get('difficulty', 'unspecified')
                # Handle case where difficulty might be a list (data issue)
                if isinstance(diff, list):
                    diff = 'unspecified'
                subject_diff[diff] += 1
                difficulty_global[diff] += 1

    # Print subject summary
    print(f'Chapters: {len(chapters)} total, {chapters_with_ex} with exercises')
    print(f'Total exercises: {subject_exercises}')
    print(f'Average per chapter: {subject_exercises / len(chapters):.1f}')

    print(f'\\nExercise types:')
    for ex_type in sorted(subject_types.keys()):
        count = subject_types[ex_type]
        pct = (count / subject_exercises * 100) if subject_exercises > 0 else 0
        print(f'  {ex_type:15} : {count:4} ({pct:5.1f}%)')

    print(f'\\nDifficulty distribution:')
    for diff in ['easy', 'medium', 'hard', 'unspecified']:
        count = subject_diff.get(diff, 0)
        pct = (count / subject_exercises * 100) if subject_exercises > 0 else 0
        print(f'  {diff:15} : {count:4} ({pct:5.1f}%)')

    print()

# Global summary
print('=' * 80)
print('OVERALL SUMMARY')
print('=' * 80)
print(f'Total chapters: {total_chapters}')
print(f'Total exercises: {total_exercises}')
print(f'Average exercises per chapter: {total_exercises / total_chapters:.1f}')
print()

print('Exercise type distribution:')
for ex_type in sorted(exercise_types_global.keys(), key=lambda x: exercise_types_global[x], reverse=True):
    count = exercise_types_global[ex_type]
    pct = (count / total_exercises * 100) if total_exercises > 0 else 0
    print(f'  {ex_type:15} : {count:4} ({pct:5.1f}%)')

print()
print('Difficulty distribution:')
for diff in ['easy', 'medium', 'hard', 'unspecified']:
    count = difficulty_global.get(diff, 0)
    pct = (count / total_exercises * 100) if total_exercises > 0 else 0
    print(f'  {diff:15} : {count:4} ({pct:5.1f}%)')

print('=' * 80)
