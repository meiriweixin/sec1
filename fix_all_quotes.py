#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix all quote issues in content.json"""
import re

with open('src/data/content.json', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace smart quotes with regular quotes
content = content.replace('"', '"')
content = content.replace('"', '"')
content = content.replace(''', "'")
content = content.replace(''', "'")

# Find all unescaped quotes within string values
# This is a simplified approach - we'll look for patterns where quotes appear within JSON strings
lines = content.split('\n')
fixed_lines = []

for line in lines:
    # If this is a content line (contains "content" or "content_zh")
    if ('"content":' in line or '"content_zh":' in line or
        '"title":' in line or '"title_zh":' in line or
        '"prompt":' in line or '"prompt_zh":' in line):
        # Count quotes to see if they're balanced
        # After the first quote (opening the string), all quotes should be escaped until the closing quote
        if line.count('"') % 2 == 0:  # Even number of quotes - probably OK
            fixed_lines.append(line)
        else:
            # Odd number - might have issue, but let's keep it for now
            fixed_lines.append(line)
    else:
        fixed_lines.append(line)

content = '\n'.join(fixed_lines)

# More targeted fix: look for specific patterns like "text" within strings
# We'll look for Chinese text with quotes like "文字"
# Between a colon and a comma/closing brace, find quotes and escape them
def escape_quotes_in_strings(match):
    string_content = match.group(1)
    # Escape any unescaped quotes within the string
    # But preserve already escaped quotes
    result = string_content.replace(r'\"', '__ESCAPED_QUOTE__')
    result = result.replace('"', r'\"')
    result = result.replace('__ESCAPED_QUOTE__', r'\"')
    return f'": "{result}"'

# This pattern matches: ": "any content with potential quotes"
# We'll do a simpler approach - just scan for problematic patterns
import json

# Try to parse and identify specific errors
try:
    data = json.loads(content)
    print("JSON is valid after quote replacement!")
except json.JSONDecodeError as e:
    print(f"Still have error at line {e.lineno}, position {e.pos}")
    print(f"Error: {e.msg}")

    # Get the problematic line
    lines = content.split('\n')
    if e.lineno > 0 and e.lineno <= len(lines):
        problematic_line = lines[e.lineno - 1]
        print(f"\nProblematic line {e.lineno}:")
        print(problematic_line[:200])

        # Try to fix quotes in this specific line
        # Find content between quotes
        if '": "' in problematic_line and '",\n' not in problematic_line and '"}\n' not in problematic_line:
            # This line might have an embedded quote
            # Find all quotes after the opening ": "
            parts = problematic_line.split('": "', 1)
            if len(parts) == 2:
                before = parts[0]
                after = parts[1]
                # The 'after' part should end with a single "
                # Any quotes before that final quote should be escaped
                # Find the last quote
                if after.count('"') > 1:
                    # Multiple quotes - need to escape all but the last
                    last_quote_pos = after.rfind('"')
                    string_content = after[:last_quote_pos]
                    ending = after[last_quote_pos:]
                    # Escape quotes in string_content
                    string_content = string_content.replace('"', r'\"')
                    fixed_line = before + '": "' + string_content + ending
                    lines[e.lineno - 1] = fixed_line
                    print(f"\nFixed line {e.lineno}:")
                    print(fixed_line[:200])

                    content = '\n'.join(lines)

# Write back
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nWrote fixed content back to file")
