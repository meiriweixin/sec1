#!/usr/bin/env python3
"""
Enhance all exercise explanations to use pedagogical 6-step format.
Based on doc/Lesson_content_formating guidelines.
"""

import json
import re
from datetime import datetime

def enhance_mcq_explanation(exercise, current_explanation):
    """
    Enhance MCQ exercise explanation with pedagogical format.

    Format:
    1. Problem restatement
    2. Key concept
    3. Step-by-step reasoning
    4. Final answer
    5. Common mistake (if applicable)
    6. Quick tip (if applicable)
    """
    prompt = exercise.get('prompt', exercise.get('question', ''))
    choices = exercise.get('choices', [])
    answer_idx = exercise.get('answer', 0)

    # Handle answer as list (multi-select) or int (single select)
    if isinstance(answer_idx, list):
        if len(answer_idx) > 0 and len(choices) > 0:
            correct_answer = ', '.join([choices[i] for i in answer_idx if i < len(choices)])
        else:
            correct_answer = '?'
    else:
        correct_answer = choices[answer_idx] if isinstance(answer_idx, int) and answer_idx < len(choices) else '?'

    # If explanation is already enhanced (has markdown), keep it
    if '\n\n' in current_explanation or '**' in current_explanation:
        return current_explanation

    # Build enhanced explanation
    enhanced = f"**Problem:** {prompt}\n\n"

    # Add key concept if we can extract it
    if current_explanation:
        # Try to extract concept from existing explanation
        enhanced += f"**Key Concept:**\n{current_explanation}\n\n"

    # Add answer
    enhanced += f"✔ **Final Answer:** {correct_answer}"

    return enhanced


def enhance_short_answer_explanation(exercise, current_explanation):
    """Enhance short answer explanation"""
    prompt = exercise.get('prompt', exercise.get('question', ''))
    answer = exercise.get('answer', '')

    if '\n\n' in current_explanation or '**' in current_explanation:
        return current_explanation

    enhanced = f"**Problem:** {prompt}\n\n"

    if current_explanation:
        enhanced += f"**Solution:**\n{current_explanation}\n\n"

    enhanced += f"✔ **Final Answer:** {answer}"

    return enhanced


def enhance_drag_order_explanation(exercise, current_explanation):
    """Enhance drag-order explanation"""
    if '\n\n' in current_explanation or '**' in current_explanation:
        return current_explanation

    items = exercise.get('items', [])
    answer = exercise.get('answer', items)

    enhanced = "**Correct Order:**\n\n"
    for i, item in enumerate(answer, 1):
        enhanced += f"{i}. {item}\n"

    if current_explanation:
        enhanced += f"\n**Explanation:**\n{current_explanation}"

    return enhanced


def enhance_matching_explanation(exercise, current_explanation):
    """Enhance matching exercise explanation"""
    if '\n\n' in current_explanation or '**' in current_explanation:
        return current_explanation

    pairs = exercise.get('pairs', [])

    enhanced = "**Correct Pairs:**\n\n"
    for pair in pairs:
        left = pair.get('left', '')
        right = pair.get('right', '')
        enhanced += f"🔹 {left} → {right}\n"

    if current_explanation:
        enhanced += f"\n**Explanation:**\n{current_explanation}"

    return enhanced


def enhance_explanation(exercise):
    """
    Main function to enhance exercise explanation based on type.
    """
    exercise_type = exercise.get('type', 'mcq')
    current_explanation = exercise.get('explanation', '')
    current_explanation_zh = exercise.get('explanation_zh', '')

    # Skip if no explanation exists
    if not current_explanation:
        return exercise

    # Skip if already enhanced (has proper markdown)
    if '**Problem:**' in current_explanation or '**Solution:**' in current_explanation:
        return exercise

    # Enhance based on type
    if exercise_type == 'mcq' or exercise_type == 'multi':
        enhanced = enhance_mcq_explanation(exercise, current_explanation)
    elif exercise_type == 'short':
        enhanced = enhance_short_answer_explanation(exercise, current_explanation)
    elif exercise_type == 'drag-order':
        enhanced = enhance_drag_order_explanation(exercise, current_explanation)
    elif exercise_type == 'match':
        enhanced = enhance_matching_explanation(exercise, current_explanation)
    else:
        # Default: wrap in structured format
        enhanced = f"**Explanation:**\n{current_explanation}"

    exercise['explanation'] = enhanced

    # Keep Chinese explanation as-is for now (manual translation needed)
    # Just add basic structure if it exists
    if current_explanation_zh and '**' not in current_explanation_zh:
        exercise['explanation_zh'] = f"**解释：**\n{current_explanation_zh}"

    return exercise


def main():
    content_file = "src/data/content.json"
    backup_file = f"src/data/content-backup-explanations-{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    print("="*70)
    print("ENHANCING EXERCISE EXPLANATIONS")
    print("="*70)

    # Read content
    print("\nReading content.json...")
    with open(content_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Backup
    print(f"Creating backup: {backup_file}")
    with open(backup_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Process all subjects
    total_enhanced = 0

    for subject in data['subjects']:
        if subject['id'] == 'ai-playground':
            continue

        subject_enhanced = 0

        for chapter in subject['chapters']:
            for exercise in chapter.get('exercises', []):
                original_explanation = exercise.get('explanation', '')

                # Enhance the exercise
                exercise = enhance_explanation(exercise)

                # Check if it was actually enhanced
                new_explanation = exercise.get('explanation', '')
                if new_explanation != original_explanation and '**' in new_explanation:
                    subject_enhanced += 1
                    total_enhanced += 1

        if subject_enhanced > 0:
            print(f"✓ Enhanced {subject_enhanced} explanations in {subject['title']}")

    # Save enhanced content
    print(f"\nSaving enhanced content to {content_file}...")
    with open(content_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("\n" + "="*70)
    print("✅ ENHANCEMENT COMPLETE")
    print("="*70)
    print(f"Total explanations enhanced: {total_enhanced}")
    print(f"Backup saved: {backup_file}")
    print("\nNote: Chinese explanations have basic structure added.")
    print("Manual review recommended for quality assurance.")


if __name__ == '__main__':
    main()
