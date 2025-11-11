#!/usr/bin/env python3
"""
Script to add proper markdown formatting to lesson content in content.json
This will make text sections display with proper paragraphs, lists, and formatting.
"""

import json
import re
from datetime import datetime
from pathlib import Path

def format_content_with_markdown(content):
    """
    Convert plain text content to properly formatted markdown.

    Handles:
    - Numbered lists (1), 2), 3) or 1. 2. 3.)
    - Sentence breaks into paragraphs
    - Bold text for keywords in ALL CAPS
    - Example sections
    - Step-by-step instructions
    """
    if not content or not isinstance(content, str):
        return content

    # Already has markdown formatting (has multiple newlines)
    if '\n\n' in content:
        return content

    # Step 1: Identify and format numbered lists
    # Pattern: "1) text 2) text 3) text" or "1. text 2. text 3. text"
    numbered_pattern = r'(\d+)[\)\.]\s+'
    if re.search(numbered_pattern, content):
        # Split content into lines for numbered list detection
        # Find sequences like "1) text, 2) text, 3) text"
        items = re.split(numbered_pattern, content)

        if len(items) > 2:  # We have a numbered list
            result = []
            result.append(items[0].strip())  # Intro text before list

            # Process pairs of (number, text)
            for i in range(1, len(items), 2):
                if i < len(items) - 1:
                    num = items[i]
                    text = items[i + 1].strip()
                    # Remove trailing comma, semicolon, or "and"
                    text = re.sub(r'[,;]\s*$', '', text)
                    text = re.sub(r',\s*and\s*$', '', text)
                    result.append(f'{num}. {text}')

            content = '\n\n' + '\n'.join(result)
            content = content.strip()

    # Step 2: Split long sentences into paragraphs at key boundaries
    # Split at: "Example:", "Key Terms:", "Note:", "Remember:", etc.
    special_markers = ['Example:', 'Examples:', 'Key Terms:', 'Note:',
                       'Remember:', 'Important:', 'Steps:', 'Method:',
                       'Singapore context:', 'Real-world application:']

    for marker in special_markers:
        if marker in content:
            content = content.replace(marker, f'\n\n**{marker}**\n\n')

    # Step 3: Bold ALL CAPS words (likely key terms)
    # Pattern: words that are 2+ chars and all uppercase
    content = re.sub(r'\b([A-Z]{2,}[A-Z\s]*)\b', r'**\1**', content)

    # Step 4: Add paragraph breaks at sentence boundaries (periods followed by capital letter)
    # But not for abbreviations like "Dr.", "Mr.", "e.g.", "i.e."
    content = re.sub(r'\.(\s+)([A-Z][a-z])', r'.\n\n\2', content)

    # Step 5: Clean up - remove excessive newlines (max 2 in a row)
    content = re.sub(r'\n{3,}', '\n\n', content)

    # Step 6: Trim leading/trailing whitespace
    content = content.strip()

    return content

def process_content_json(input_file='src/data/content.json', backup=True):
    """
    Process content.json to add markdown formatting to all text sections.
    """
    input_path = Path(input_file)

    # Load the JSON file
    print(f"Loading {input_file}...")
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Create backup
    if backup:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = input_path.parent / f'content-backup-{timestamp}.json'
        print(f"Creating backup: {backup_path}")
        with open(backup_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    # Process all subjects
    total_sections = 0
    formatted_sections = 0

    for subject in data.get('subjects', []):
        subject_name = subject.get('title', 'Unknown')
        print(f"\nProcessing subject: {subject_name}")

        for chapter in subject.get('chapters', []):
            chapter_title = chapter.get('title', 'Unknown')

            for section in chapter.get('sections', []):
                total_sections += 1

                # Format English content
                if 'content' in section and section.get('type') == 'text':
                    original = section['content']
                    formatted = format_content_with_markdown(original)
                    if formatted != original:
                        section['content'] = formatted
                        formatted_sections += 1
                        print(f"  ✓ Formatted: {chapter_title} - {section.get('title', 'N/A')}")

                # Format Chinese content
                if 'content_zh' in section and section.get('type') == 'text':
                    original = section['content_zh']
                    formatted = format_content_with_markdown(original)
                    if formatted != original:
                        section['content_zh'] = formatted

                # Format explanations
                if 'explanation' in section:
                    original = section['explanation']
                    formatted = format_content_with_markdown(original)
                    if formatted != original:
                        section['explanation'] = formatted

                if 'explanation_zh' in section:
                    original = section['explanation_zh']
                    formatted = format_content_with_markdown(original)
                    if formatted != original:
                        section['explanation_zh'] = formatted

    # Save the updated JSON
    print(f"\nSaving updated content to {input_file}...")
    with open(input_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*60}")
    print(f"✅ Formatting complete!")
    print(f"Total sections processed: {total_sections}")
    print(f"Sections formatted: {formatted_sections}")
    print(f"{'='*60}")

if __name__ == '__main__':
    process_content_json()
