import json
import re

def convert_math_to_latex(text):
    """Convert plain math notation to LaTeX"""
    if not text:
        return text

    # Replace common math patterns with LaTeX
    replacements = [
        # Exponentials
        (r'e\^x', r'$e^x$'),
        (r'e\^\((-?[\w\s+\-*/]+)\)', lambda m: f'$e^{{{m.group(1)}}}$'),
        (r'2\^x', r'$2^x$'),

        # Fractions
        (r'∫', r'$\\int$'),
        (r'∑', r'$\\sum$'),
        (r'π', r'$\\pi$'),
        (r'θ', r'$\\theta$'),
        (r'α', r'$\\alpha$'),
        (r'β', r'$\\beta$'),
        (r'∞', r'$\\infty$'),

        # Subscripts/superscripts (but not in LaTeX already)
        (r'(?<!\$)x\^2(?!\$)', r'$x^2$'),
        (r'(?<!\$)x\^3(?!\$)', r'$x^3$'),
        (r'(?<!\$)x\^n(?!\$)', r'$x^n$'),

        # Derivatives
        (r'dy/dx', r'$\\frac{dy}{dx}$'),
        (r'dv/dx', r'$\\frac{dv}{dx}$'),
        (r'du/dx', r'$\\frac{du}{dx}$'),

        # Inequality symbols
        (r'≥', r'$\\geq$'),
        (r'≤', r'$\\leq$'),
        (r'≠', r'$\\neq$'),

        # Special functions
        (r'ln\s+x', r'$\\ln x$'),
        (r'ln\(([^)]+)\)', lambda m: f'$\\ln({m.group(1)})$'),
        (r'sin\s+x', r'$\\sin x$'),
        (r'cos\s+x', r'$\\cos x$'),
        (r'tan\s+x', r'$\\tan x$'),
    ]

    result = text
    for pattern, replacement in replacements:
        if callable(replacement):
            result = re.sub(pattern, replacement, result)
        else:
            result = re.sub(pattern, replacement, result)

    return result

# Load JC 2 chapters
with open('chapters/jc2_math_chapters.json', 'r', encoding='utf-8') as f:
    chapters = json.load(f)

# Convert all content to LaTeX
for chapter in chapters:
    for section in chapter.get('sections', []):
        # Convert content
        if 'content' in section:
            section['content'] = convert_math_to_latex(section['content'])
        if 'content_zh' in section:
            section['content_zh'] = convert_math_to_latex(section['content_zh'])

        # Convert explanation
        if 'explanation' in section:
            section['explanation'] = convert_math_to_latex(section['explanation'])
        if 'explanation_zh' in section:
            section['explanation_zh'] = convert_math_to_latex(section['explanation_zh'])

# Save updated chapters
with open('chapters/jc2_math_chapters.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, ensure_ascii=False, indent=2)

print("✓ Converted all JC 2 math content to LaTeX notation")
print("\nUpdated sections:")
for ch in chapters:
    print(f"  {ch['title']}: {len(ch['sections'])} sections")
