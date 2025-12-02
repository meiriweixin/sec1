#!/usr/bin/env python3
"""
Fix common formatting issues in all lesson content
"""

import json
import shutil
import re
from datetime import datetime

def fix_content_formatting(content):
    """Fix common formatting issues in content"""
    if not content:
        return content

    original = content

    # Fix: Step numbers separated from content (e.g., "1.\n\nFind" → "1. Find")
    content = re.sub(r'(\d+)\.\n\n([A-Z])', r'\1. \2', content)

    # Fix: Broken bold followed by text (e.g., "**HCF **of" → "**HCF** of")
    content = re.sub(r'\*\*([A-Za-z]+) \*\*', r'**\1**', content)

    # Fix: Extra space after Example:** (e.g., "**Example:**\n\n " → "**Example:**\n\n")
    content = re.sub(r'(\*\*Example:\*\*)\n\n ', r'\1\n\n', content)

    # Fix: Period with newline but missing double newline for paragraphs
    # Only if the next line starts with capital and previous line is complete sentence
    lines = content.split('\n')
    fixed_lines = []
    for i, line in enumerate(lines):
        fixed_lines.append(line)
        # If current line ends with period and next line starts with capital
        # and there's only single newline (not already double)
        if (i < len(lines) - 1 and
            line.strip().endswith('.') and
            lines[i + 1].strip() and
            lines[i + 1][0].isupper() and
            not line.strip().endswith('e.g.') and
            not line.strip().endswith('i.e.') and
            not line.strip().endswith('Dr.') and
            '**' not in lines[i + 1][:10]):  # Not a heading
            # Check if next line is not already separated
            if i + 1 < len(lines) - 1 and lines[i + 1].strip():
                # Add extra newline for paragraph break
                fixed_lines.append('')

    content = '\n'.join(fixed_lines)

    # Remove triple or more newlines (reduce to double)
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content

def main():
    content_file = 'src/data/content.json'

    # Create backup
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = f'src/data/content-backup-autofix-{timestamp}.json'
    shutil.copy(content_file, backup_file)
    print(f"Created backup: {backup_file}")
    print()

    # Load content
    with open(content_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    total_sections = 0
    fixed_sections = 0

    print("="*80)
    print("FIXING ALL LESSON CONTENT FORMATTING ISSUES")
    print("="*80)
    print()

    # Fix all subjects and chapters
    for subject in data['subjects']:
        subject_name = subject.get('title', 'Unknown')

        for chapter in subject.get('chapters', []):
            chapter_name = chapter.get('title', 'Unknown')

            for section in chapter.get('sections', []):
                total_sections += 1
                section_title = section.get('title', 'Unknown')
                section_id = section.get('id', 'unknown')

                fixed = False

                # Fix English content
                if 'content' in section:
                    original = section['content']
                    fixed_content = fix_content_formatting(original)
                    if fixed_content != original:
                        section['content'] = fixed_content
                        print(f"✓ Fixed: {subject_name} > {chapter_name} > {section_title} (EN)")
                        fixed = True

                # Fix Chinese content
                if 'content_zh' in section:
                    original = section['content_zh']
                    fixed_content = fix_content_formatting(original)
                    if fixed_content != original:
                        section['content_zh'] = fixed_content
                        print(f"✓ Fixed: {subject_name} > {chapter_name} > {section_title} (ZH)")
                        fixed = True

                if fixed:
                    fixed_sections += 1

    # Save updated content
    with open(content_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print()
    print("="*80)
    print(f"Total sections checked: {total_sections}")
    print(f"Sections fixed: {fixed_sections}")
    print(f"Backup saved to: {backup_file}")
    print(f"Updated file:    {content_file}")
    print("="*80)
    print()
    print("✅ Formatting fixes complete!")
    print("   Run check_all_formatting.py again to verify remaining issues.")

if __name__ == '__main__':
    main()
