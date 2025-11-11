#!/usr/bin/env python3
"""
Script to add proper markdown formatting to lesson content in content.json
Version 2 - Simplified and more robust
"""

import json
import re
from datetime import datetime
from pathlib import Path

def format_content_with_markdown(content):
    """
    Convert plain text content to properly formatted markdown.
    """
    if not content or not isinstance(content, str):
        return content

    # Already has markdown formatting (has multiple newlines)
    if '\n\n' in content:
        return content

    # Step 1: Handle numbered lists like "1) text 2) text 3) text" or "1. text, 2. text, 3. text"
    # Look for pattern: digit followed by ) or . then text
    numbered_list_pattern = r'(\d+)[\)\.]\s+([^0-9]+?)(?=\d+[\)\.]|\. Example:|\. Key Terms:|\. Note:|$)'

    matches = list(re.finditer(numbered_list_pattern, content))

    if len(matches) >= 2:  # At least 2 numbered items = it's a list
        # Extract the intro text (before first number)
        first_match = matches[0]
        intro = content[:first_match.start()].strip()

        # Build the formatted list
        list_items = []
        for match in matches:
            num = match.group(1)
            text = match.group(2).strip()
            # Clean up trailing punctuation
            text = re.sub(r'[,;]\s*$', '', text)
            text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
            list_items.append(f'{num}. {text}')

        # Get any text after the last list item
        last_match = matches[-1]
        outro = content[last_match.end():].strip()

        # Combine everything
        parts = []
        if intro:
            parts.append(intro)
        parts.append('\n'.join(list_items))
        if outro:
            parts.append(outro)

        content = '\n\n'.join(parts)

    # Step 2: Format special sections (Example, Key Terms, etc.)
    special_markers = [
        'Example:', 'Examples:', 'Key Terms:', 'Note:', 'Remember:',
        'Important:', 'Steps:', 'Method:', 'Singapore context:',
        'Real-world application:'
    ]

    for marker in special_markers:
        if marker in content:
            content = re.sub(f'\\s*{re.escape(marker)}\\s*', f'\n\n**{marker}**\n\n', content)

    # Step 3: Bold ALL CAPS terms (likely keywords)
    # Match words that are 2+ chars and all uppercase
    content = re.sub(r'\b([A-Z]{2,}[A-Z\s]*?)\b(?=\s|,|\.|\))', r'**\1**', content)

    # Step 4: Add paragraph breaks at sentence boundaries
    # Split at periods followed by capital letter (but not abbreviations)
    content = re.sub(r'\.(\s+)([A-Z][a-z])', r'.\n\n\2', content)

    # Step 5: Clean up excessive newlines (max 2 in a row)
    content = re.sub(r'\n{3,}', '\n\n', content)

    # Step 6: Trim whitespace
    content = content.strip()

    return content

def process_content_json(input_file='src/data/content.json', backup=True):
    """
    Process content.json to add markdown formatting to all text sections.
    """
    input_path = Path(input_file)

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
                        print(f"  ✓ {chapter_title} - {section.get('title', 'N/A')}")

                # Format Chinese content
                if 'content_zh' in section and section.get('type') == 'text':
                    original = section['content_zh']
                    formatted = format_content_with_markdown(original)
                    if formatted != original:
                        section['content_zh'] = formatted

                # Format explanations
                for field in ['explanation', 'explanation_zh']:
                    if field in section:
                        original = section[field]
                        formatted = format_content_with_markdown(original)
                        if formatted != original:
                            section[field] = formatted

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
