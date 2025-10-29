#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

def fix_curly_quotes_in_file(filepath):
    """Fix curly quotes in a JSON file"""
    print(f"Processing {filepath}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Count before
    left_count = content.count('\u201c')
    right_count = content.count('\u201d')
    single_left = content.count('\u2018')
    single_right = content.count('\u2019')

    print(f"  Found {left_count} left and {right_count} right double curly quotes")
    print(f"  Found {single_left} left and {single_right} right single curly quotes")

    # Replace curly quotes with straight quotes (escaped for JSON strings)
    content = content.replace('\u201c', '\\"')
    content = content.replace('\u201d', '\\"')
    content = content.replace('\u2018', "'")
    content = content.replace('\u2019', "'")

    # Write fixed content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    # Validate
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            json.load(f)
        print(f"  ✅ {filepath} is now valid JSON\n")
        return True
    except json.JSONDecodeError as e:
        print(f"  ❌ Still invalid: {e}\n")
        return False

if __name__ == '__main__':
    files = [
        'chapters/science-electrical-systems.json',
        'chapters/science-physical-properties.json'
    ]

    for f in files:
        fix_curly_quotes_in_file(f)
