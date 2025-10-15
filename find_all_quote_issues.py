#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Find all unescaped quotes in JSON strings"""
import json
import re

with open('src/data/content.json', 'r', encoding='utf-8') as f:
    content = f.read()

# Try to parse and find errors iteratively
errors_found = []
max_iterations = 20

for iteration in range(max_iterations):
    try:
        data = json.loads(content)
        print(f"SUCCESS! JSON is valid after {iteration} fixes")
        break
    except json.JSONDecodeError as e:
        print(f"\nIteration {iteration + 1}: Error at line {e.lineno}, position {e.pos}")
        print(f"Error: {e.msg}")

        # Get the problematic area
        lines = content.split('\n')
        if e.lineno > 0 and e.lineno <= len(lines):
            line_idx = e.lineno - 1
            problematic_line = lines[line_idx]

            print(f"Line {e.lineno} (first 150 chars): {problematic_line[:150]}")

            # Check if this line has unescaped quotes
            # Pattern: look for content between ": " and " at end
            if '": "' in problematic_line:
                # Split at the opening of the JSON string value
                parts = problematic_line.split('": "', 1)
                if len(parts) == 2:
                    key_part = parts[0]
                    value_part = parts[1]

                    # Find the last quote (should be the closing quote)
                    # Everything before it is the string content
                    last_quote = value_part.rfind('"')

                    if last_quote > 0:
                        string_content = value_part[:last_quote]
                        after_string = value_part[last_quote:]

                        # Count unescaped quotes in string_content
                        # Look for " that are not preceded by \
                        unescaped = []
                        i = 0
                        while i < len(string_content):
                            if string_content[i] == '"':
                                # Check if it's escaped
                                if i == 0 or string_content[i-1] != '\\':
                                    unescaped.append(i)
                                    print(f"  Found unescaped quote at position {i} in string")
                            i += 1

                        if unescaped:
                            # Fix by escaping these quotes
                            # Work backwards to not mess up indices
                            chars = list(string_content)
                            for pos in reversed(unescaped):
                                chars.insert(pos, '\\')
                            string_content = ''.join(chars)

                            # Reconstruct the line
                            fixed_line = key_part + '": "' + string_content + after_string
                            lines[line_idx] = fixed_line
                            content = '\n'.join(lines)

                            print(f"  Fixed line {e.lineno}")
                            errors_found.append(e.lineno)
                        else:
                            print(f"  ERROR: Could not find unescaped quotes on this line!")
                            print(f"  Full line: {problematic_line}")
                            break
                    else:
                        print(f"  ERROR: Could not parse line structure")
                        break
                else:
                    print(f"  ERROR: Line doesn't match expected pattern")
                    break
            else:
                print(f"  ERROR: Line doesn't contain JSON string pattern")
                break
        else:
            print("ERROR: Line number out of range")
            break
else:
    print(f"\nReached maximum iterations ({max_iterations})")
    print("Could not fully fix the JSON")

# Write the fixed content
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nFixed {len(errors_found)} errors at lines: {errors_found}")
print("Wrote changes to file")
