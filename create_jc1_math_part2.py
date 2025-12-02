#!/usr/bin/env python3
"""
Generate remaining JC 1 Mathematics chapters (Part 2)
Chapters 3-8
"""

import json

jc1_chapters_part2 = [
    {
        "id": "sequences-series-jc1",
        "title": "Sequences & Series",
        "title_zh": "数列与级数",
        "gradeLevel": "jc1",
        "description": "Master arithmetic and geometric progressions, sum formulas, and applications",
        "description_zh": "掌握等差和等比数列、求和公式和应用",
        "objectives": [
            "Find general terms and specific terms of sequences",
            "Calculate sums of arithmetic and geometric series",
            "Apply sum to infinity for geometric series",
            "Solve real-world problems involving sequences and series"
        ],
        "objectives_zh": [
            "求数列的通项和特定项",
            "计算等差和等比级数的和",
            "应用等比级数的无穷和公式",
            "解决涉及数列和级数的实际问题"
        ],
        "sections": [
            {
                "id": "arithmetic-progression",
                "type": "text",
                "title": "Arithmetic Progressions",
                "title_zh": "等差数列",
                "content": """**Arithmetic Progression (AP)** is a sequence where each term differs from the previous by a constant.

**General Form:** a, a+d, a+2d, a+3d, ...

where:
- **a** = first term
- **d** = common difference

**nth Term Formula:**

Tₙ = a + (n-1)d

**Sum of First n Terms:**

Sₙ = (n/2)[2a + (n-1)d]

or

Sₙ = (n/2)(a + l) where l is the last term

**Example: HDB Block Numbers**

Block numbers 101, 104, 107, 110, ... form an AP

- First term a = 101
- Common difference d = 3
- 10th block: T₁₀ = 101 + (10-1)×3 = 101 + 27 = 128
- Sum of first 10: S₁₀ = (10/2)[2(101) + 9(3)] = 5(202 + 27) = 1145

**Finding Unknown Values:**

Given: 3rd term = 14, 7th term = 26

T₃ = a + 2d = 14 ... (1)
T₇ = a + 6d = 26 ... (2)

Subtract (1) from (2): 4d = 12 → d = 3
Substitute: a + 2(3) = 14 → a = 8

**Singapore Context:**

Taxi fare structure: $3.90 initial, then $0.24 every 400m forms an AP. Cost after n 400m segments = 3.90 + 0.24n""",
                "content_zh": "等差数列的定义、通项公式和求和公式。"
            },
            {
                "id": "geometric-progression",
                "type": "text",
                "title": "Geometric Progressions",
                "title_zh": "等比数列",
                "content": """**Geometric Progression (GP)** is a sequence where each term is multiplied by a constant to get the next.

**General Form:** a, ar, ar², ar³, ...

where:
- **a** = first term
- **r** = common ratio

**nth Term Formula:**

Tₙ = arⁿ⁻¹

**Sum of First n Terms:**

Sₙ = a(1 - rⁿ)/(1 - r) for r ≠ 1

Sₙ = a(rⁿ - 1)/(r - 1) (alternative form)

**Sum to Infinity:**

When |r| < 1, the sum converges:

S∞ = a/(1 - r)

**Example: Bacterial Growth**

Bacteria doubles every hour: 100, 200, 400, 800, ...

- First term a = 100
- Common ratio r = 2
- After 8 hours: T₈ = 100 × 2⁷ = 12,800 bacteria
- Total bacteria produced in 8 hours: S₈ = 100(2⁸ - 1)/(2 - 1) = 25,500

**Infinite GP Example:**

A ball dropped from 10m bounces to 70% of previous height each time.

Total distance = 10 + 2(7 + 4.9 + 3.43 + ...)
= 10 + 2 × 7/(1 - 0.7)
= 10 + 2 × 7/0.3
= 10 + 46.67
= 56.67m

**Singapore Investment:**

CPF savings with 2.5% annual interest: Initial $1000, adding $1000 yearly forms GP for compound growth calculations.""",
                "content_zh": "等比数列的定义、通项公式、有限和与无穷和。"
            },
            {
                "id": "series-applications",
                "type": "text",
                "title": "Applications of Series",
                "title_zh": "级数应用",
                "content": """**Practical Applications** of sequences and series.

**1. Loan Repayments (Singapore Housing Loans)**

Monthly payment P, interest rate r per month, n months:

Amount owed after n months forms a GP

Total repaid = P + P + P + ... (n terms) = nP (AP)
Amount owed follows GP pattern with compound interest

**2. Depreciation**

HDB flat value decreases by 2% yearly (GP with r = 0.98)

Initial value $500,000
After n years: Value = 500,000 × (0.98)ⁿ

**3. Population Growth**

Singapore population grows 1.2% annually

Current: 5.9 million
After 10 years: 5.9 × (1.012)¹⁰ ≈ 6.64 million

**4. Saving Plans**

Save $100 monthly with 0.5% monthly interest

Using GP sum formula:
Total after n months = 100[(1.005)ⁿ - 1]/0.005

**5. Virus Spread Model**

If each infected person infects 3 others:

Day 0: 1 person
Day 1: 3 people
Day 2: 9 people
Day n: 3ⁿ people (GP with r = 3)

Total infected by day n: S = (3ⁿ⁺¹ - 1)/2

**Example Problem:**

A scholarship offers $1000 in year 1, increasing by $200 each year (AP), OR $1000 in year 1, increasing by 15% each year (GP).

For 4-year degree, which is better?

**AP:** S₄ = (4/2)[2(1000) + 3(200)] = 2(2000 + 600) = $5,200

**GP:** S₄ = 1000(1.15⁴ - 1)/(1.15 - 1) = 1000(0.7490)/0.15 = $4,993

AP is better for 4 years! But GP becomes better for longer periods.""",
                "content_zh": "数列和级数在实际问题中的应用。"
            }
        ],
        "exercises": []
    },
    {
        "id": "vectors-jc1",
        "title": "Vectors in 2D & 3D",
        "title_zh": "二维与三维向量",
        "gradeLevel": "jc1",
        "description": "Understand vector operations, position vectors, and scalar product",
        "description_zh": "理解向量运算、位置向量和数量积",
        "objectives": [
            "Perform vector addition, subtraction, and scalar multiplication",
            "Apply position vectors and displacement",
            "Use ratio theorem for dividing lines",
            "Calculate scalar (dot) product and angles"
        ],
        "objectives_zh": [
            "进行向量加法、减法和数乘运算",
            "应用位置向量和位移",
            "使用比例定理分割线段",
            "计算数量积和角度"
        ],
        "sections": [
            {
                "id": "vector-basics",
                "type": "text",
                "title": "Vector Operations",
                "title_zh": "向量运算",
                "content": """**Vectors** have both magnitude and direction, written as **a** or a⃗.

**Component Form:**

2D: **a** = (a₁, a₂) or a₁**i** + a₂**j**
3D: **a** = (a₁, a₂, a₃) or a₁**i** + a₂**j** + a₃**k**

**Magnitude:**

|**a**| = √(a₁² + a₂²) in 2D
|**a**| = √(a₁² + a₂² + a₃²) in 3D

**Vector Addition:**

**a** + **b** = (a₁ + b₁, a₂ + b₂, a₃ + b₃)

Geometrically: Head-to-tail or parallelogram rule

**Scalar Multiplication:**

k**a** = (ka₁, ka₂, ka₃)

If k > 0: same direction, scaled magnitude
If k < 0: opposite direction, scaled magnitude

**Unit Vector:**

Unit vector in direction of **a**: **â** = **a**/|**a**|

**Position Vectors:**

**⃗OA** = position vector of point A relative to origin O

If A = (x, y, z), then **⃗OA** = (x, y, z)

**Displacement Vector:**

**⃗AB** = **⃗OB** - **⃗OA** = position of B minus position of A

**Singapore MRT Example:**

If Orchard MRT is origin, Dhoby Ghaut is at position (500, 300) meters, and City Hall is at (800, 200):

Displacement from Dhoby Ghaut to City Hall = (800, 200) - (500, 300) = (300, -100) meters

Distance = √(300² + 100²) = √100,000 ≈ 316 meters""",
                "content_zh": "向量的基本运算、模长和位置向量。"
            },
            {
                "id": "ratio-theorem",
                "type": "text",
                "title": "Ratio Theorem",
                "title_zh": "比例定理",
                "content": """**Ratio Theorem** finds the position vector of a point dividing a line segment in a given ratio.

**Formula:**

If C divides AB in ratio m:n, then:

**⃗OC** = (n**⃗OA** + m**⃗OB**)/(m + n)

**Alternative Form:**

**⃗OC** = **⃗OA** + (m/(m+n))**⃗AB**

**Special Cases:**

**Midpoint (1:1 ratio):**

**⃗OC** = (**⃗OA** + **⃗OB**)/2

**Example:**

A = (2, 3), B = (8, 9), find point C dividing AB in ratio 2:1

**⃗OC** = (1(2,3) + 2(8,9))/(2+1)
= ((2,3) + (16,18))/3
= (18, 21)/3
= (6, 7) ✓

**External Division:**

When point C is outside AB, use negative ratio.

If C divides AB externally in ratio 2:1:

**⃗OC** = (1**⃗OA** - 2**⃗OB**)/(1 - 2) = (**⃗OA** - 2**⃗OB**)/(-1) = 2**⃗OB** - **⃗OA**

**Centroid of Triangle:**

Centroid G of triangle ABC:

**⃗OG** = (**⃗OA** + **⃗OB** + **⃗OC**)/3

**Singapore Planning Example:**

Three MRT stations at A(1, 2), B(7, 4), C(4, 8). Optimal location for mall (centroid):

**⃗OG** = ((1,2) + (7,4) + (4,8))/3 = (12, 14)/3 = (4, 4.67)""",
                "content_zh": "比例定理用于求分割线段的点的位置向量。"
            },
            {
                "id": "scalar-product",
                "type": "text",
                "title": "Scalar Product",
                "title_zh": "数量积",
                "content": """**Scalar (Dot) Product** of two vectors produces a scalar.

**Definition:**

**a** · **b** = |**a**| |**b**| cos θ

where θ is angle between vectors

**Component Form:**

**a** · **b** = a₁b₁ + a₂b₂ + a₃b₃

**Properties:**

1. **a** · **b** = **b** · **a** (commutative)
2. **a** · (**b** + **c**) = **a** · **b** + **a** · **c** (distributive)
3. **a** · **a** = |**a**|²

**Finding Angle:**

cos θ = (**a** · **b**)/(|**a**| |**b**|)

**Perpendicular Vectors:**

**a** ⊥ **b** ⟺ **a** · **b** = 0

**Example: Find angle between vectors**

**a** = (3, 4), **b** = (1, 7)

**a** · **b** = 3(1) + 4(7) = 3 + 28 = 31

|**a**| = √(3² + 4²) = 5
|**b**| = √(1² + 7²) = √50 = 5√2

cos θ = 31/(5 × 5√2) = 31/(25√2) = 0.877

θ = 28.6°

**Perpendicular Check:**

Are (2, 3) and (6, -4) perpendicular?

(2, 3) · (6, -4) = 2(6) + 3(-4) = 12 - 12 = 0 ✓

Yes, they are perpendicular!

**Projection:**

Projection of **a** onto **b**:

proj = (**a** · **b**)/|**b**| × **b̂**

where **b̂** = **b**/|**b**| is unit vector

**Work Done (Physics):**

If force **F** = (10, 5) N acts over displacement **d** = (3, 4) m:

Work = **F** · **d** = 10(3) + 5(4) = 30 + 20 = 50 J""",
                "content_zh": "数量积的定义、计算、角度求解和应用。"
            }
        ],
        "exercises": []
    }
]

# Load existing chapters
with open('chapters/jc1_math_chapters.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

# Combine
all_chapters = existing + jc1_chapters_part2

# Save
with open('chapters/jc1_math_chapters.json', 'w', encoding='utf-8') as f:
    json.dump(all_chapters, f, ensure_ascii=False, indent=2)

print(f"Added {len(jc1_chapters_part2)} more JC 1 Mathematics chapters")
print(f"Total chapters: {len(all_chapters)}")
print()
print("New chapters added:")
for i, ch in enumerate(jc1_chapters_part2, 3):
    print(f"{i}. {ch['title']}: {len(ch['sections'])} sections")
