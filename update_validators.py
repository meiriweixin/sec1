#!/usr/bin/env python3
"""
Update Exercise Validators in content.json
Removes 'exact' validator to use new smart default validation
"""

import json
import shutil
from datetime import datetime

def main():
    content_file = 'src/data/content.json'

    # Create backup
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = f'src/data/content-backup-{timestamp}.json'
    shutil.copy(content_file, backup_file)
    print(f"Created backup: {backup_file}")

    # Load content
    with open(content_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Track changes
    changed_count = 0
    total_short_exercises = 0
    validator_counts = {}

    # Process all subjects and chapters
    for subject in data['subjects']:
        subject_name = subject.get('title', 'Unknown')
        for chapter in subject.get('chapters', []):
            chapter_name = chapter.get('title', 'Unknown')

            for exercise in chapter.get('exercises', []):
                if exercise.get('type') == 'short':
                    total_short_exercises += 1
                    current_validator = exercise.get('validator', 'default')

                    # Count validator usage
                    validator_counts[current_validator] = validator_counts.get(current_validator, 0) + 1

                    # Remove 'exact' validator to use smart default
                    if exercise.get('validator') == 'exact':
                        exercise.pop('validator')
                        changed_count += 1
                        print(f"Updated: {subject_name} > {chapter_name} > {exercise.get('id', 'unknown')}")

    # Save updated content
    with open(content_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Print summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Total short-answer exercises: {total_short_exercises}")
    print(f"\nValidator distribution BEFORE update:")
    for validator, count in sorted(validator_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {validator:15} : {count:3} exercises")
    print(f"\nChanged {changed_count} exercises from 'exact' to smart default")
    print(f"\nKeeping specialized validators:")
    print(f"  - numeric   : {validator_counts.get('numeric', 0)} exercises (numeric answers)")
    print(f"  - fraction  : {validator_counts.get('fraction', 0)} exercises (fraction formats)")
    print(f"  - equation  : {validator_counts.get('equation', 0)} exercises (equation validation)")
    print(f"\nBackup saved to: {backup_file}")
    print(f"Updated file:    {content_file}")
    print("="*60)

if __name__ == '__main__':
    main()
