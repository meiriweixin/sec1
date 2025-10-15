#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix smart quotes in content.json"""

with open('src/data/content.json', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace smart quotes with regular quotes
content = content.replace('"', '"')
content = content.replace('"', '"')
content = content.replace(''', "'")
content = content.replace(''', "'")

# Write back
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed smart quotes in content.json")
