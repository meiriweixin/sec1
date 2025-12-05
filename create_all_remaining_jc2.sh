#!/bin/bash
# Batch create all remaining JC 2 chapters (4-8)

echo "Creating JC 2 Chapters 4-8 exercises..."
echo "This will generate 75 exercises (15 per chapter)"
echo ""

# Chapter 4
python create_jc2_chapter4_complete.py

# Chapter 5  
python create_jc2_chapter5_complete.py

# Chapter 6
python create_jc2_chapter6_complete.py

# Chapter 7
python create_jc2_chapter7_complete.py

# Chapter 8
python create_jc2_chapter8_complete.py

echo ""
echo "✓ All JC 2 exercises complete!"

# Check final status
python -c "
import json
with open('chapters/jc2_math_chapters.json', 'r', encoding='utf-8') as f:
    chapters = json.load(f)
total = sum(len(ch.get('exercises', [])) for ch in chapters)
print(f'Total: {total}/120 exercises ({total/120*100:.0f}%)')
"
