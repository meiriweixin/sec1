#!/usr/bin/env python3
"""
Comprehensive fix for all lesson content formatting issues.
Fixes broken markdown, adds proper structure, and ensures readability.
"""

import json
import re
from datetime import datetime

def fix_broken_markdown(content):
    """Fix common markdown formatting errors"""
    # Fix broken bold: **text **word → **text** word
    content = re.sub(r'\*\*([^*]+)\s+\*\*', r'**\1**', content)

    # Fix single asterisks that should be double
    content = re.sub(r'(?<!\*)\*(?!\*)([^*]+)(?<!\*)\*(?!\*)', r'**\1**', content)

    # Ensure space after periods for better readability
    content = re.sub(r'\.([A-Z])', r'. \1', content)

    return content

def enhance_si_units_content(content):
    """Specifically enhance SI Base Units section"""
    enhanced = """**SI (International System of Units)** is the standard measurement system used worldwide in science.

**The seven SI base units:**

1. **Meter (m)** - Length/distance
2. **Kilogram (kg)** - Mass
3. **Second (s)** - Time
4. **Ampere (A)** - Electric current
5. **Kelvin (K)** - Temperature
6. **Mole (mol)** - Amount of substance
7. **Candela (cd)** - Luminous intensity

**Why SI units?**

🔹 Universal standard for scientific communication
🔹 Easy conversion between units (based on powers of 10)
🔹 Precise and consistent measurements

**Common SI units in Singapore:**

🔹 **Length**: Meters (m) - MRT track lengths, building heights
🔹 **Mass**: Kilograms (kg) - Body weight, food portions at hawker centers
🔹 **Time**: Seconds (s) - Race timing at Singapore Sports Hub
🔹 **Temperature**: Celsius (°C) - Weather reports (27-28°C average)

**Examples:**
- Height of Singapore Flyer: 165 m
- Mass of a durian: ~2 kg
- Daily temperature: 27°C (300 K)"""

    return enhanced

def enhance_laboratory_safety(content):
    """Enhance laboratory safety content"""
    if len(content) > 300:  # Already detailed
        return content

    enhanced = """**Laboratory Safety Rules:**

Safety in the science lab protects you and others from harm.

**Essential safety rules:**

1. **Eye protection**: Always wear safety goggles when handling chemicals
2. **Clothing**: Tie back long hair, remove loose jewelry, wear closed shoes
3. **No food or drink**: Never eat or drink in the laboratory
4. **Follow instructions**: Read procedures carefully before starting experiments
5. **Handle chemicals carefully**: Never taste or smell chemicals directly
6. **Clean workspace**: Keep area tidy, wipe up spills immediately
7. **Wash hands**: Always wash hands after experiments
8. **Report accidents**: Tell teacher immediately about any spills, breakage, or injuries

**Emergency equipment in Singapore school labs:**

🔹 Fire extinguishers and fire blankets
🔹 Emergency shower and eyewash stations
🔹 First aid kits
🔹 Fume cupboards for dangerous fumes
🔹 Safety signs and evacuation routes

**Important reminders:**

⚠️ Never work alone in the lab
⚠️ Know the location of emergency exits
⚠️ Listen carefully to teacher instructions"""

    return enhanced

def enhance_generic_content(section_id, title, content):
    """Enhance generic lesson content with better formatting"""
    # Skip if already well-formatted
    if content.count('\n\n') >= 3 and '**' in content and len(content) > 300:
        return content

    # Fix broken markdown
    content = fix_broken_markdown(content)

    # If content is one long paragraph, try to structure it
    if '\n\n' not in content and len(content) > 200:
        # Add paragraph break after first sentence
        content = re.sub(r'\.(\s+[A-Z])', r'.\n\n\1', content, count=1)

    return content

def main():
    content_file = "src/data/content.json"
    backup_file = f"src/data/content-backup-formatting-fix-{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    print("="*70)
    print("COMPREHENSIVE LESSON FORMATTING FIX")
    print("="*70)

    # Read content
    print("\nReading content.json...")
    with open(content_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Backup
    print(f"Creating backup: {backup_file}")
    with open(backup_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    fixed_count = 0
    enhanced_count = 0

    for subject in data['subjects']:
        if subject['id'] == 'ai-playground':
            continue

        for chapter in subject['chapters']:
            for section in chapter.get('sections', []):
                section_id = section.get('id', '')
                title = section.get('title', '')
                content = section.get('content', '')
                original_content = content

                # Fix broken markdown
                if '** **' in content or '* *' in content:
                    content = fix_broken_markdown(content)
                    fixed_count += 1
                    print(f"🔧 Fixed markdown: {chapter['title']} - {title}")

                # Specific enhancements for known problematic sections
                if 'si' in section_id.lower() or 'base unit' in title.lower():
                    content = enhance_si_units_content(content)
                    enhanced_count += 1
                    print(f"✨ Enhanced: {chapter['title']} - {title}")

                elif 'safety' in section_id.lower() or 'safety' in title.lower():
                    content = enhance_laboratory_safety(content)
                    enhanced_count += 1
                    print(f"✨ Enhanced: {chapter['title']} - {title}")

                else:
                    # Generic enhancement
                    enhanced = enhance_generic_content(section_id, title, content)
                    if enhanced != content:
                        content = enhanced
                        enhanced_count += 1
                        print(f"📝 Improved: {chapter['title']} - {title}")

                # Update if changed
                if content != original_content:
                    section['content'] = content
                    # Also update Chinese if exists
                    if section.get('content_zh') and '** **' in section.get('content_zh', ''):
                        section['content_zh'] = fix_broken_markdown(section['content_zh'])

    # Save
    print(f"\nSaving fixed content...")
    with open(content_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("\n" + "="*70)
    print("✅ FORMATTING FIX COMPLETE")
    print("="*70)
    print(f"Broken markdown fixed: {fixed_count}")
    print(f"Content enhanced: {enhanced_count}")
    print(f"Total improvements: {fixed_count + enhanced_count}")
    print(f"\nBackup saved: {backup_file}")


if __name__ == '__main__':
    main()
