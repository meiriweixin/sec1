#!/usr/bin/env python3
"""
Generate JC 1 Mathematics chapters with lessons and exercises
Aligned with Singapore MOE H2 Mathematics syllabus
"""

import json
from datetime import datetime

# JC 1 Mathematics chapters
jc1_chapters = [
    {
        "id": "functions-graphical-transformations-jc1",
        "title": "Functions & Graphical Transformations",
        "title_zh": "函数与图形变换",
        "gradeLevel": "jc1",
        "description": "Master function transformations including translations, reflections, and stretches",
        "description_zh": "掌握函数变换，包括平移、反射和伸缩",
        "objectives": [
            "Understand and apply graphical transformations (translations, reflections, stretches)",
            "Sketch transformed graphs of common functions",
            "Determine the equation of a transformed graph",
            "Solve problems involving composite transformations"
        ],
        "objectives_zh": [
            "理解并应用图形变换（平移、反射、伸缩）",
            "绘制常见函数的变换图形",
            "确定变换图形的方程",
            "解决涉及复合变换的问题"
        ],
        "sections": [
            {
                "id": "transformations-basics",
                "type": "text",
                "title": "Types of Transformations",
                "title_zh": "变换类型",
                "content": """**Graphical transformations** modify the position, shape, or orientation of a graph.

**Four Main Types:**

**1. Translation**
- y = f(x) + a → shifts graph **UP** by a units
- y = f(x) - a → shifts graph **DOWN** by a units
- y = f(x + a) → shifts graph **LEFT** by a units
- y = f(x - a) → shifts graph **RIGHT** by a units

**2. Reflection**
- y = -f(x) → reflects in **x-axis** (flip vertically)
- y = f(-x) → reflects in **y-axis** (flip horizontally)

**3. Stretch**
- y = af(x) where a > 1 → **vertical stretch** by factor a
- y = af(x) where 0 < a < 1 → **vertical compression**
- y = f(ax) where a > 1 → **horizontal compression** by factor 1/a
- y = f(ax) where 0 < a < 1 → **horizontal stretch**

**4. Composite Transformations**
- Apply transformations in sequence
- Order matters! Apply transformations closest to x first

**Singapore Example:**

The MRT fare pricing function f(d) = 0.8 + 0.05d (where d is distance in km) is transformed to y = 2f(d) - 0.3 during peak hours, representing doubled base fare with a discount.""",
                "content_zh": "图形变换修改图形的位置、形状或方向。"
            },
            {
                "id": "transformation-examples",
                "type": "text",
                "title": "Working with Transformations",
                "title_zh": "变换实例",
                "content": """**How to sketch transformed graphs:**

**Step-by-step process:**

1. **Identify the base function** (e.g., x², √x, |x|, sin x)
2. **List all transformations** from the equation
3. **Determine the order** of transformations
4. **Apply each transformation** systematically
5. **Mark key points** and asymptotes

**Example: Sketch y = 2(x + 1)² - 3**

Base function: y = x² (parabola)

Transformations:
- (x + 1): shift LEFT 1 unit
- ×2: vertical stretch factor 2
- -3: shift DOWN 3 units

Order: Left 1 → Stretch ×2 → Down 3

Key point (0,0) becomes:
- After left 1: (-1, 0)
- After stretch: (-1, 0)
- After down 3: (-1, -3) ✓

**Common Mistake:**

Students often confuse y = f(x + 1) with shifting RIGHT. Remember: adding inside moves LEFT!

**HDB Example:**

If h(t) represents HDB flat prices over time, then y = 1.2h(t - 5) + 50000 means prices increased 20% and shifted 5 years forward, plus $50,000 inflation adjustment.""",
                "content_zh": "如何绘制变换图形的步骤。"
            },
            {
                "id": "inverse-functions",
                "type": "text",
                "title": "Inverse Functions",
                "title_zh": "反函数",
                "content": """**Inverse functions** reverse the effect of the original function.

**Definition:**

If y = f(x), then x = f⁻¹(y)

The inverse function f⁻¹ satisfies: f⁻¹(f(x)) = x and f(f⁻¹(x)) = x

**Finding Inverse Functions:**

**Steps:**

1. Replace f(x) with y
2. Swap x and y
3. Make y the subject
4. Replace y with f⁻¹(x)

**Example:** Find inverse of f(x) = 2x + 3

1. y = 2x + 3
2. x = 2y + 3 (swap)
3. x - 3 = 2y → y = (x - 3)/2
4. f⁻¹(x) = (x - 3)/2

**Graphical Property:**

The graphs of y = f(x) and y = f⁻¹(x) are **reflections** in the line y = x.

**One-to-One Requirement:**

A function must be **one-to-one** (passes horizontal line test) to have an inverse.

**Restricting Domain:**

For many-to-one functions (like x²), restrict the domain to make them one-to-one.

Example: f(x) = x² for x ≥ 0 has inverse f⁻¹(x) = √x

**Singapore Context:**

Temperature conversion: C = (5/9)(F - 32) has inverse F = (9/5)C + 32, allowing conversion both ways.""",
                "content_zh": "反函数的定义、求法和图形性质。"
            }
        ],
        "exercises": []  # Will be added separately
    },
    {
        "id": "rational-modulus-functions-jc1",
        "title": "Rational & Modulus Functions",
        "title_zh": "有理函数与绝对值函数",
        "gradeLevel": "jc1",
        "description": "Understand and sketch rational functions with asymptotes and modulus functions",
        "description_zh": "理解和绘制有理函数（含渐近线）和绝对值函数",
        "objectives": [
            "Identify vertical and horizontal asymptotes of rational functions",
            "Sketch graphs of rational functions",
            "Solve equations involving modulus functions",
            "Apply modulus functions to real-world problems"
        ],
        "objectives_zh": [
            "识别有理函数的垂直和水平渐近线",
            "绘制有理函数图形",
            "解绝对值函数方程",
            "应用绝对值函数于实际问题"
        ],
        "sections": [
            {
                "id": "rational-functions",
                "type": "text",
                "title": "Rational Functions",
                "title_zh": "有理函数",
                "content": """**Rational functions** have the form: f(x) = P(x)/Q(x) where P and Q are polynomials.

**Key Features:**

**1. Vertical Asymptotes**

Occur where denominator = 0 (and numerator ≠ 0)

To find: Set Q(x) = 0 and solve for x

Example: f(x) = 1/(x - 2) has vertical asymptote at x = 2

**2. Horizontal Asymptotes**

Depend on degrees of numerator and denominator:

- If degree(P) < degree(Q): y = 0
- If degree(P) = degree(Q): y = (leading coefficient of P)/(leading coefficient of Q)
- If degree(P) > degree(Q): No horizontal asymptote (may have oblique)

**3. Oblique Asymptotes**

When degree(P) = degree(Q) + 1, divide polynomials to find oblique asymptote

**Sketching Steps:**

1. Find **x-intercepts** (numerator = 0)
2. Find **y-intercept** (set x = 0)
3. Find **vertical asymptotes** (denominator = 0)
4. Find **horizontal/oblique asymptotes**
5. Test behavior near asymptotes
6. Sketch curve

**Example: f(x) = (2x + 3)/(x - 1)**

- x-intercept: 2x + 3 = 0 → x = -3/2
- y-intercept: f(0) = 3/(-1) = -3
- Vertical asymptote: x = 1
- Horizontal asymptote: y = 2 (same degree, ratio of coefficients)

**Singapore Context:**

Cost per student for school excursion: C(n) = (1000 + 20n)/n where n is number of students. As n increases, cost approaches $20 per student (horizontal asymptote).""",
                "content_zh": "有理函数的定义、渐近线和绘图方法。"
            },
            {
                "id": "modulus-functions",
                "type": "text",
                "title": "Modulus Functions",
                "title_zh": "绝对值函数",
                "content": """**Modulus (Absolute Value)** represents distance from zero.

**Definition:**

|x| = { x if x ≥ 0, -x if x < 0 }

**Properties:**

1. |x| ≥ 0 for all x
2. |xy| = |x| × |y|
3. |x/y| = |x| / |y| (y ≠ 0)
4. |x + y| ≤ |x| + |y| (triangle inequality)

**Graphing Modulus Functions:**

**Basic graph y = |x|:** V-shaped, vertex at origin

**Transformations:**
- y = |f(x)|: Reflect negative parts above x-axis
- y = f(|x|): Reflect positive half across y-axis

**Solving Modulus Equations:**

**Method 1: Case analysis**

Split into cases based on sign of expression inside modulus

Example: |2x - 3| = 5

Case 1: 2x - 3 ≥ 0 → 2x - 3 = 5 → x = 4 ✓
Case 2: 2x - 3 < 0 → -(2x - 3) = 5 → x = -1 ✓

Solutions: x = -1 or x = 4

**Method 2: Squaring**

|f(x)| = a → f(x)² = a² (valid when a ≥ 0)

**Modulus Inequalities:**

|x| < a means -a < x < a
|x| > a means x < -a or x > a

**Example: |x - 2| < 3**

-3 < x - 2 < 3
-1 < x < 5

**Singapore Context:**

Quality control: |weight - 500g| ≤ 5g ensures products are within 5g of target weight (between 495g and 505g).""",
                "content_zh": "绝对值函数的定义、图形和方程解法。"
            },
            {
                "id": "combined-functions",
                "type": "text",
                "title": "Combining Functions",
                "title_zh": "组合函数",
                "content": """**Composite Functions** combine two or more functions.

**Notation:** (f ∘ g)(x) = f(g(x))

Read as "f of g of x" or "f composed with g"

**Finding Composite Functions:**

**Example:** f(x) = x² and g(x) = 2x + 1

(f ∘ g)(x) = f(g(x)) = f(2x + 1) = (2x + 1)² = 4x² + 4x + 1

(g ∘ f)(x) = g(f(x)) = g(x²) = 2x² + 1

**Note:** f ∘ g ≠ g ∘ f (order matters!)

**Domain Considerations:**

For f(g(x)) to be defined:
1. g(x) must be defined
2. g(x) must be in domain of f

**Example:** f(x) = √x and g(x) = x - 4

Domain of f ∘ g: Need x - 4 ≥ 0 → x ≥ 4

**Self-Composition:**

f ∘ f means f(f(x))

Example: f(x) = 1/x → (f ∘ f)(x) = f(1/x) = 1/(1/x) = x

**Applications:**

**Singapore MRT Example:**

Let d(t) = distance traveled as function of time
Let c(d) = cost as function of distance

Then (c ∘ d)(t) gives cost as function of time

**Temperature Conversion:**

Let f = Celsius to Fahrenheit: f(C) = (9/5)C + 32
Let g = Fahrenheit to Kelvin: g(F) = (5/9)(F - 32) + 273.15

Then g ∘ f converts Celsius directly to Kelvin.""",
                "content_zh": "复合函数的定义、计算和应用。"
            }
        ],
        "exercises": []
    }
]

# Save to file
output_file = 'chapters/jc1_math_chapters.json'

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(jc1_chapters, f, ensure_ascii=False, indent=2)

print(f"Created {len(jc1_chapters)} JC 1 Mathematics chapters")
print(f"Saved to: {output_file}")
print()
print("Chapters created:")
for i, ch in enumerate(jc1_chapters, 1):
    print(f"{i}. {ch['title']}: {len(ch['sections'])} sections")
