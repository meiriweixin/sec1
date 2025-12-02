#!/usr/bin/env python3
"""
Generate final JC 1 Mathematics chapters (Part 3)
Chapters 5-8: Differentiation focus
"""

import json

jc1_chapters_part3 = [
    {
        "id": "differentiation-techniques-jc1",
        "title": "Differentiation Techniques",
        "title_zh": "微分技巧",
        "gradeLevel": "jc1",
        "description": "Master product rule, quotient rule, chain rule, and differentiation of special functions",
        "description_zh": "掌握乘积法则、商法则、链式法则和特殊函数求导",
        "objectives": [
            "Apply product rule, quotient rule, and chain rule",
            "Differentiate trigonometric, exponential, and logarithmic functions",
            "Perform parametric differentiation",
            "Use implicit differentiation"
        ],
        "objectives_zh": [
            "应用乘积法则、商法则和链式法则",
            "对三角函数、指数函数和对数函数求导",
            "进行参数求导",
            "使用隐函数求导"
        ],
        "sections": [
            {
                "id": "product-quotient-rules",
                "type": "text",
                "title": "Product & Quotient Rules",
                "title_zh": "乘积法则与商法则",
                "content": """**Product Rule** for differentiating products of functions.

**Product Rule:**

If y = u(x) · v(x), then:

dy/dx = u(dv/dx) + v(du/dx)

Or: (uv)' = u'v + uv'

**Example:** y = x² · sin x

u = x², u' = 2x
v = sin x, v' = cos x

dy/dx = 2x · sin x + x² · cos x = x(2 sin x + x cos x)

**Quotient Rule** for differentiating fractions.

**Quotient Rule:**

If y = u(x)/v(x), then:

dy/dx = [v(du/dx) - u(dv/dx)]/v²

Or: (u/v)' = (u'v - uv')/v²

**Memory Aid:** "Low d-High minus High d-Low, over Low-Low"

**Example:** y = (3x + 1)/(2x - 5)

u = 3x + 1, u' = 3
v = 2x - 5, v' = 2

dy/dx = [(2x - 5)(3) - (3x + 1)(2)]/(2x - 5)²
= [6x - 15 - 6x - 2]/(2x - 5)²
= -17/(2x - 5)²

**When to Use Each:**

- **Product Rule:** When multiplying two functions
- **Quotient Rule:** When dividing functions
- **Simplify first** if possible (e.g., x³/x = x² → easier!)

**Singapore Economics Example:**

Revenue R = price × quantity = p · q
If p = 50 - 0.2q (demand curve):

R = q(50 - 0.2q) = 50q - 0.2q²

dR/dq = 50 - 0.4q (marginal revenue)

Using product rule on R = p · q where p depends on q gives same result!""",
                "content_zh": "乘积法则和商法则的公式、应用和实例。"
            },
            {
                "id": "chain-rule",
                "type": "text",
                "title": "Chain Rule",
                "title_zh": "链式法则",
                "content": """**Chain Rule** for differentiating composite functions.

**Chain Rule:**

If y = f(g(x)), then:

dy/dx = (dy/du) × (du/dx)

where u = g(x)

Or: (f ∘ g)'(x) = f'(g(x)) · g'(x)

**Example: y = (3x + 5)⁷**

Let u = 3x + 5, then y = u⁷

du/dx = 3
dy/du = 7u⁶

dy/dx = 7u⁶ × 3 = 21(3x + 5)⁶

**Multiple Chains:**

For y = f(g(h(x))):

dy/dx = (dy/du) × (du/dv) × (dv/dx)

**Example: y = sin(e³ˣ)**

v = 3x → dv/dx = 3
u = eᵛ = e³ˣ → du/dv = e³ˣ
y = sin u → dy/du = cos u = cos(e³ˣ)

dy/dx = cos(e³ˣ) · e³ˣ · 3 = 3e³ˣ cos(e³ˣ)

**Combining Rules:**

Often need product/quotient + chain rule!

**Example: y = x² √(1 - x²)**

Use product rule: u = x², v = √(1 - x²)

u' = 2x

v = (1 - x²)^(1/2)
v' = (1/2)(1 - x²)^(-1/2) × (-2x) = -x/√(1 - x²) (chain rule!)

dy/dx = 2x √(1 - x²) + x²(-x/√(1 - x²))
= [2x(1 - x²) - x³]/√(1 - x²)
= (2x - 3x³)/√(1 - x²)

**Singapore Temperature Model:**

If T(h) = temperature at height h meters
And h(t) = height of weather balloon at time t

Then dT/dt = (dT/dh) × (dh/dt) gives rate of temperature change as balloon rises.""",
                "content_zh": "链式法则的公式、复合应用和实例。"
            },
            {
                "id": "special-functions",
                "type": "text",
                "title": "Differentiating Special Functions",
                "title_zh": "特殊函数求导",
                "content": """**Standard Derivatives** of common functions.

**Trigonometric Functions:**

d/dx(sin x) = cos x
d/dx(cos x) = -sin x
d/dx(tan x) = sec² x

**Exponential & Logarithmic:**

d/dx(eˣ) = eˣ
d/dx(aˣ) = aˣ ln a
d/dx(ln x) = 1/x
d/dx(log_a x) = 1/(x ln a)

**Combined with Chain Rule:**

d/dx(sin(f(x))) = cos(f(x)) · f'(x)
d/dx(e^f(x)) = e^f(x) · f'(x)
d/dx(ln(f(x))) = f'(x)/f(x)

**Example: y = e^(2x) sin(3x)**

Product + Chain rule:

u = e^(2x), u' = 2e^(2x)
v = sin(3x), v' = 3cos(3x)

dy/dx = 2e^(2x) sin(3x) + 3e^(2x) cos(3x)
= e^(2x)[2 sin(3x) + 3 cos(3x)]

**Example: y = ln(x² + 1)**

Chain rule:

dy/dx = 1/(x² + 1) × 2x = 2x/(x² + 1)

**Logarithmic Differentiation:**

For complicated products/quotients, take ln first!

**Example: y = x^x (x > 0)**

ln y = ln(x^x) = x ln x

Differentiate both sides:

(1/y)(dy/dx) = ln x + x(1/x) = ln x + 1

dy/dx = y(ln x + 1) = x^x(ln x + 1)

**Singapore Population Growth:**

P(t) = 5.9e^(0.012t) million (t in years)

dP/dt = 5.9 × 0.012 × e^(0.012t) = 0.0708e^(0.012t) million per year

Current rate (t=0): 0.0708 million = 70,800 people per year""",
                "content_zh": "三角函数、指数函数、对数函数的导数及其应用。"
            }
        ],
        "exercises": []
    },
    {
        "id": "applications-differentiation-jc1",
        "title": "Applications of Differentiation",
        "title_zh": "微分应用",
        "gradeLevel": "jc1",
        "description": "Apply differentiation to tangents, normals, optimization, and curve sketching",
        "description_zh": "应用微分于切线、法线、优化和曲线绘制",
        "objectives": [
            "Find equations of tangents and normals",
            "Solve connected rates of change problems",
            "Optimize real-world problems (maxima/minima)",
            "Sketch curves using derivatives"
        ],
        "objectives_zh": [
            "求切线和法线方程",
            "解决关联变化率问题",
            "优化实际问题（最大/最小值）",
            "使用导数绘制曲线"
        ],
        "sections": [
            {
                "id": "tangents-normals",
                "type": "text",
                "title": "Tangents & Normals",
                "title_zh": "切线与法线",
                "content": """**Tangent Line** touches curve at exactly one point (locally).

**Finding Tangent Equation:**

**Steps:**

1. Find derivative dy/dx
2. Substitute x-coordinate to find gradient at point
3. Use point-slope form: y - y₁ = m(x - x₁)

**Example: Find tangent to y = x³ - 3x² + 2 at x = 1**

1. dy/dx = 3x² - 6x
2. At x = 1: m = 3(1)² - 6(1) = -3
3. Point: y = (1)³ - 3(1)² + 2 = 0, so (1, 0)
4. Tangent: y - 0 = -3(x - 1) → y = -3x + 3

**Normal Line** is perpendicular to tangent.

**Normal Gradient:**

If tangent gradient = m, normal gradient = -1/m

**Example:** From above, tangent gradient = -3

Normal gradient = -1/(-3) = 1/3

Normal: y - 0 = (1/3)(x - 1) → y = (x - 1)/3 or 3y = x - 1

**Horizontal & Vertical Tangents:**

**Horizontal tangent:** dy/dx = 0
**Vertical tangent:** dx/dy = 0 (or dy/dx undefined)

**Singapore Road Example:**

A curved road follows y = x² - 4x + 5.

At point (2, 1):
- Tangent gradient: dy/dx = 2x - 4 = 0 at x = 2
- Road is **horizontal** at this point (flat section)
- Good for pedestrian crossing!

**Finding Points with Given Tangent:**

Find points on y = x³ where tangent has gradient 12.

dy/dx = 3x² = 12
x² = 4
x = ±2

Points: (2, 8) and (-2, -8)""",
                "content_zh": "切线和法线的定义、求法和应用。"
            },
            {
                "id": "optimization",
                "type": "text",
                "title": "Optimization Problems",
                "title_zh": "优化问题",
                "content": """**Optimization** finds maximum or minimum values.

**Steps for Max/Min Problems:**

1. **Define variables** and constraints
2. **Write function** to optimize
3. **Differentiate** to find dy/dx
4. **Set dy/dx = 0** for turning points
5. **Test** using second derivative or endpoints

**Second Derivative Test:**

- If d²y/dx² > 0: **minimum** point (concave up)
- If d²y/dx² < 0: **maximum** point (concave down)
- If d²y/dx² = 0: **inconclusive** (test around point)

**Example 1: Maximum Area**

Farmer has 100m of fencing for rectangular pen. Find maximum area.

Let width = x, length = y
Perimeter: 2x + 2y = 100 → y = 50 - x

Area: A = xy = x(50 - x) = 50x - x²

dA/dx = 50 - 2x = 0
x = 25m

d²A/dx² = -2 < 0 → maximum ✓

Maximum area = 25 × 25 = 625 m²

**Example 2: Minimum Cost**

HDB flat floor has area 60 m². Tiles for floor cost $50/m², wall tiles $30/m². Minimize total cost for room with square floor.

Let side = x meters, height = h meters
Floor area: x² = 60 → x = √60

Wall area: 4xh = 4√60 · h

Total cost: C = 50(60) + 30(4√60 · h) = 3000 + 120√60 · h

But we need another constraint! (Problem incomplete without height constraint)

**Example 3: Closest Point**

Find point on line y = 2x + 1 closest to origin.

Distance² from origin: D² = x² + y² = x² + (2x + 1)²
= x² + 4x² + 4x + 1 = 5x² + 4x + 1

d(D²)/dx = 10x + 4 = 0
x = -0.4

y = 2(-0.4) + 1 = 0.2

Closest point: (-0.4, 0.2)

**Singapore Business:**

Hawker stall sells 500 - 10p meals daily at price $p.

Cost per meal: $2

Revenue: R = p(500 - 10p) = 500p - 10p²
Cost: C = 2(500 - 10p) = 1000 - 20p
Profit: P = R - C = 500p - 10p² - 1000 + 20p = -10p² + 520p - 1000

dP/dp = -20p + 520 = 0
p = $26

Maximum profit at $26 per meal!

Check: d²P/dp² = -20 < 0 → maximum ✓""",
                "content_zh": "优化问题的求解步骤和实例。"
            },
            {
                "id": "curve-sketching",
                "type": "text",
                "title": "Curve Sketching with Calculus",
                "title_zh": "利用微积分绘制曲线",
                "content": """**Using derivatives** to analyze and sketch curves.

**Key Features to Find:**

1. **Intercepts**
   - x-intercept: set y = 0
   - y-intercept: set x = 0

2. **Turning Points** (Stationary Points)
   - Find where dy/dx = 0
   - Classify using second derivative

3. **Nature of Turning Points:**
   - **Maximum:** dy/dx = 0 and d²y/dx² < 0
   - **Minimum:** dy/dx = 0 and d²y/dx² > 0
   - **Point of Inflection:** dy/dx = 0 and d²y/dx² = 0

4. **Points of Inflection**
   - Find where d²y/dx² = 0
   - Where concavity changes

5. **Asymptotes** (for rational functions)
   - Vertical: denominator = 0
   - Horizontal: limit as x → ±∞

**Example: Sketch y = x³ - 3x² - 9x + 5**

**Step 1: Intercepts**
- y-intercept: y = 5
- x-intercepts: solve x³ - 3x² - 9x + 5 = 0 (use calculator/numerical)

**Step 2: First Derivative**

dy/dx = 3x² - 6x - 9 = 3(x² - 2x - 3) = 3(x - 3)(x + 1)

Turning points at x = -1 and x = 3

**Step 3: Second Derivative**

d²y/dx² = 6x - 6 = 6(x - 1)

At x = -1: d²y/dx² = -12 < 0 → **maximum**
At x = 3: d²y/dx² = 12 > 0 → **minimum**

**Step 4: Coordinates**

Maximum: (-1, 10)
Minimum: (3, -22)

**Step 5: Point of Inflection**

d²y/dx² = 0 when x = 1
y = 1 - 3 - 9 + 5 = -6

Point of inflection: (1, -6)

**Step 6: Behavior**

As x → ∞: y → ∞ (leading term x³)
As x → -∞: y → -∞

**Sketch Features:**
- Cubic curve
- Maximum at (-1, 10)
- Minimum at (3, -22)
- Inflection at (1, -6)
- Passes through (0, 5)

**Singapore Traffic Flow:**

Traffic density d(x) = -0.1x³ + 1.5x² - 4x + 10 (cars per 100m)

Find optimal density:
- dd/dx = -0.3x² + 3x - 4
- Set = 0: x ≈ 1.7 km or x ≈ 7.6 km
- Use second derivative to determine if max or min
- Helps plan traffic light timing!""",
                "content_zh": "使用导数分析和绘制曲线的方法。"
            }
        ],
        "exercises": []
    },
    {
        "id": "trigonometric-identities-jc1",
        "title": "Trigonometric Identities & Equations",
        "title_zh": "三角恒等式与方程",
        "gradeLevel": "jc1",
        "description": "Master addition formulae, double angle formulae, R-formula, and solving trigonometric equations",
        "description_zh": "掌握和角公式、倍角公式、R公式和三角方程求解",
        "objectives": [
            "Apply addition and double angle formulae",
            "Use R-formula to solve trigonometric equations",
            "Solve equations involving multiple angles",
            "Apply trigonometry to real-world problems"
        ],
        "objectives_zh": [
            "应用和角公式和倍角公式",
            "使用R公式求解三角方程",
            "解多角三角方程",
            "应用三角函数于实际问题"
        ],
        "sections": [
            {
                "id": "addition-formulae",
                "type": "text",
                "title": "Addition Formulae",
                "title_zh": "和角公式",
                "content": """**Addition Formulae** for sin, cos, and tan.

**Sine Addition:**

sin(A + B) = sin A cos B + cos A sin B
sin(A - B) = sin A cos B - cos A sin B

**Cosine Addition:**

cos(A + B) = cos A cos B - sin A sin B
cos(A - B) = cos A cos B + sin A sin B

**Tangent Addition:**

tan(A + B) = (tan A + tan B)/(1 - tan A tan B)
tan(A - B) = (tan A - tan B)/(1 + tan A tan B)

**Applications:**

**Example 1:** Find exact value of sin 75°

sin 75° = sin(45° + 30°)
= sin 45° cos 30° + cos 45° sin 30°
= (√2/2)(√3/2) + (√2/2)(1/2)
= (√6 + √2)/4

**Example 2:** Simplify sin(x + 30°) + sin(x - 30°)

= [sin x cos 30° + cos x sin 30°] + [sin x cos 30° - cos x sin 30°]
= 2 sin x cos 30°
= 2 sin x × (√3/2)
= √3 sin x

**Double Angle Formulae:**

sin 2A = 2 sin A cos A

cos 2A = cos² A - sin² A
= 2 cos² A - 1
= 1 - 2 sin² A

tan 2A = (2 tan A)/(1 - tan² A)

**Example:** If sin x = 3/5 and x is acute, find sin 2x

cos x = 4/5 (from Pythagoras)

sin 2x = 2 sin x cos x = 2(3/5)(4/5) = 24/25

**Singapore Ferris Wheel:**

Height of Singapore Flyer capsule:

h(t) = 80 + 75 sin(15t) + 75 cos(15t)

Using addition: sin θ + cos θ = √2 sin(θ + 45°)

h(t) = 80 + 75√2 sin(15t + 45°) meters""",
                "content_zh": "和角公式和倍角公式及其应用。"
            },
            {
                "id": "r-formula",
                "type": "text",
                "title": "R-Formula Method",
                "title_zh": "R公式法",
                "content": """**R-Formula** converts a sin θ + b cos θ into single sine or cosine.

**R-Formula (Sine Form):**

a sin θ + b cos θ = R sin(θ + α)

where:
- R = √(a² + b²)
- tan α = b/a (α in appropriate quadrant)

**R-Formula (Cosine Form):**

a sin θ + b cos θ = R cos(θ - β)

where:
- R = √(a² + b²)
- tan β = a/b

**When to Use:**

- Finding maximum/minimum values
- Solving equations
- Simplifying expressions

**Example 1: Find maximum of f(x) = 3 sin x + 4 cos x**

R = √(3² + 4²) = √25 = 5

tan α = 4/3 → α ≈ 53.1°

f(x) = 5 sin(x + 53.1°)

Maximum value = 5 (when sin(x + 53.1°) = 1)
Occurs when x + 53.1° = 90° → x = 36.9°

**Example 2: Solve 5 sin θ - 12 cos θ = 6.5 for 0° ≤ θ ≤ 360°**

R = √(5² + 12²) = √169 = 13

tan α = -12/5 → α ≈ -67.4° or 112.6° (in 2nd quadrant)

13 sin(θ - 67.4°) = 6.5
sin(θ - 67.4°) = 0.5

θ - 67.4° = 30° or 150°

θ = 97.4° or 217.4°

**Singapore Temperature:**

Daily temperature T(h) = 27 + 3 sin(15h) + 4 cos(15h)

where h is hours after midnight

Using R-formula: R = √(3² + 4²) = 5

T(h) = 27 + 5 sin(15h + α)

Maximum temp = 27 + 5 = 32°C
Minimum temp = 27 - 5 = 22°C

Time of max: when sin(15h + α) = 1""",
                "content_zh": "R公式法的应用和实例。"
            },
            {
                "id": "trig-equations",
                "type": "text",
                "title": "Solving Trigonometric Equations",
                "title_zh": "三角方程求解",
                "content": """**Strategies** for solving trigonometric equations.

**Basic Equations:**

**Type 1: sin x = a**
- Find principal value
- Add period multiples or use symmetry

**Type 2: cos x = a**
- Find principal value
- Use symmetry about y-axis

**Type 3: tan x = a**
- Find principal value
- Add π multiples

**Example 1: Solve sin x = 0.5 for 0 ≤ x ≤ 2π**

Principal value: x = π/6

Other solution in [0, 2π]: x = π - π/6 = 5π/6

Solutions: x = π/6, 5π/6

**Quadratic Type:**

**Example 2: Solve 2 cos² x - cos x - 1 = 0 for 0° ≤ x ≤ 360°**

Let u = cos x:

2u² - u - 1 = 0
(2u + 1)(u - 1) = 0

u = -1/2 or u = 1

cos x = -1/2: x = 120°, 240°
cos x = 1: x = 0°, 360°

Solutions: x = 0°, 120°, 240°, 360°

**Using Identities:**

**Example 3: Solve sin 2x = cos x for 0 ≤ x ≤ π**

2 sin x cos x = cos x
2 sin x cos x - cos x = 0
cos x(2 sin x - 1) = 0

cos x = 0: x = π/2
sin x = 1/2: x = π/6, 5π/6

Solutions: x = π/6, π/2, 5π/6

**General Solutions:**

For sin x = a:
x = α + 2nπ or x = π - α + 2nπ (n ∈ ℤ)

For cos x = a:
x = ±α + 2nπ (n ∈ ℤ)

For tan x = a:
x = α + nπ (n ∈ ℤ)

**Singapore Tides:**

Tide height h = 2 + 1.5 sin(30t) meters (t in hours)

When is height 3m?

2 + 1.5 sin(30t) = 3
sin(30t) = 2/3

30t = 41.8° or 138.2°
t = 1.39h or 4.61h

High tide occurs at 1:23 AM and 4:37 AM""",
                "content_zh": "三角方程的求解策略和实例。"
            }
        ],
        "exercises": []
    },
    {
        "id": "exponential-logarithmic-jc1",
        "title": "Exponential & Logarithmic Functions",
        "title_zh": "指数与对数函数",
        "gradeLevel": "jc1",
        "description": "Master exponential growth/decay, logarithmic laws, and solving exponential equations",
        "description_zh": "掌握指数增长/衰减、对数法则和指数方程求解",
        "objectives": [
            "Apply laws of indices and logarithms",
            "Solve exponential and logarithmic equations",
            "Model growth and decay problems",
            "Apply to real-world scenarios (compound interest, population, decay)"
        ],
        "objectives_zh": [
            "应用指数和对数法则",
            "解指数和对数方程",
            "建立增长和衰减模型",
            "应用于实际场景（复利、人口、衰减）"
        ],
        "sections": [
            {
                "id": "exponential-functions",
                "type": "text",
                "title": "Exponential Functions",
                "title_zh": "指数函数",
                "content": """**Exponential Functions** have form y = aˣ where a > 0, a ≠ 1.

**Properties of y = eˣ:**

- Domain: all real numbers
- Range: y > 0
- y-intercept: (0, 1)
- Asymptote: y = 0 (x-axis)
- Always increasing
- Never touches x-axis

**Laws of Indices:**

1. aᵐ × aⁿ = aᵐ⁺ⁿ
2. aᵐ ÷ aⁿ = aᵐ⁻ⁿ
3. (aᵐ)ⁿ = aᵐⁿ
4. a⁰ = 1
5. a⁻ⁿ = 1/aⁿ
6. a^(m/n) = ⁿ√(aᵐ)

**Exponential Growth:**

P(t) = P₀ · aᵗ

where:
- P₀ = initial amount
- a = growth factor (a > 1)
- t = time

**Example: Singapore Population**

Population P = 5.9 × (1.012)ᵗ million

Growth rate = 1.2% per year

After 10 years: P = 5.9 × (1.012)¹⁰ ≈ 6.64 million

**Compound Interest:**

A = P(1 + r/n)ⁿᵗ

where:
- P = principal
- r = annual interest rate
- n = compounds per year
- t = time in years

**Continuous Compounding:**

A = Peʳᵗ

**Example: CPF Savings**

$10,000 at 2.5% annual interest for 20 years:

A = 10000(1.025)²⁰ = $16,386

**Exponential Decay:**

N(t) = N₀ · e⁻ᵏᵗ

Used for radioactive decay, cooling, depreciation

**Example: HDB Depreciation**

Flat value V = 500000 × (0.98)ᵗ (2% yearly depreciation)

After 30 years: V = 500000 × (0.98)³⁰ ≈ $272,634

**Half-Life:**

Time for quantity to reduce to half:

N(t) = N₀ × (1/2)^(t/T) where T = half-life""",
                "content_zh": "指数函数的性质、增长和衰减模型。"
            },
            {
                "id": "logarithmic-functions",
                "type": "text",
                "title": "Logarithmic Functions",
                "title_zh": "对数函数",
                "content": """**Logarithms** are inverses of exponential functions.

**Definition:**

If aˣ = b, then log_a(b) = x

**Natural Logarithm:**

ln x = log_e(x) where e ≈ 2.71828

**Properties of y = ln x:**

- Domain: x > 0
- Range: all real numbers
- x-intercept: (1, 0)
- Asymptote: x = 0 (y-axis)
- Always increasing
- Passes through (e, 1)

**Laws of Logarithms:**

1. log(xy) = log x + log y
2. log(x/y) = log x - log y
3. log(xⁿ) = n log x
4. log_a(a) = 1
5. log_a(1) = 0
6. a^(log_a(x)) = x
7. log_a(b) = log_c(b)/log_c(a) (change of base)

**Solving Exponential Equations:**

**Example 1:** Solve 2ˣ = 10

Take log both sides:

x log 2 = log 10
x = log 10 / log 2 = 1/0.301 ≈ 3.32

**Example 2:** Solve e^(2x-1) = 5

Take ln both sides:

2x - 1 = ln 5
2x = ln 5 + 1
x = (ln 5 + 1)/2 ≈ 1.305

**Solving Logarithmic Equations:**

**Example 3:** Solve log₂(x) + log₂(x - 3) = 2

log₂[x(x - 3)] = 2
x(x - 3) = 2² = 4
x² - 3x - 4 = 0
(x - 4)(x + 1) = 0

x = 4 (reject x = -1 as log negative is undefined)

**Growth Rate Calculations:**

If population doubles in 20 years:

P(20) = 2P₀
P₀ · e^(20r) = 2P₀
e^(20r) = 2
20r = ln 2
r = ln 2 / 20 ≈ 0.0347 = 3.47% per year

**pH Scale (Chemistry):**

pH = -log₁₀[H⁺]

Singapore tap water pH ≈ 7: [H⁺] = 10⁻⁷ mol/L

**Richter Scale (Earthquakes):**

M = log₁₀(I/I₀)

Magnitude 5 vs 7 = 10² = 100 times more intense!""",
                "content_zh": "对数函数的定义、性质和方程求解。"
            },
            {
                "id": "applications-exp-log",
                "type": "text",
                "title": "Applications of Exponential & Log Functions",
                "title_zh": "指数与对数函数应用",
                "content": """**Real-World Models** using exponential and logarithmic functions.

**1. Population Growth**

Singapore population model:

P(t) = P₀e^(rt)

where r = 0.012 (1.2% growth)

**Question:** When will population reach 7 million?

7 = 5.9e^(0.012t)
7/5.9 = e^(0.012t)
ln(7/5.9) = 0.012t
t = ln(7/5.9)/0.012 ≈ 14.3 years

**2. Compound Interest with Inflation**

**Real value** accounting for inflation:

Real = Nominal / (1 + i)ᵗ

where i = inflation rate

$10,000 at 2.5% interest, 2% inflation, 10 years:

Nominal: 10000(1.025)¹⁰ = $12,801
Real: 12801/(1.02)¹⁰ = $10,517

**3. Learning Curves**

Proficiency P = 100(1 - e^(-kt))

After training time t, proficiency approaches 100%

**Example:** P = 100(1 - e^(-0.1t))

After 10 hours: P = 100(1 - e^(-1)) ≈ 63.2%
After 20 hours: P = 100(1 - e^(-2)) ≈ 86.5%

**4. Drug Concentration**

C(t) = C₀e^(-kt) (exponential decay)

**Example:** Initial dose 100mg, half-life 6 hours

Find k: 50 = 100e^(-6k)
0.5 = e^(-6k)
ln(0.5) = -6k
k = ln(0.5)/(-6) = 0.1155

After 4 hours: C = 100e^(-0.1155×4) ≈ 63mg

**5. Newton's Law of Cooling**

T(t) = Tₐ + (T₀ - Tₐ)e^(-kt)

where:
- T₀ = initial temperature
- Tₐ = ambient temperature

**Example:** Coffee at 90°C in 25°C room

After 5 min at 70°C:

70 = 25 + (90 - 25)e^(-5k)
45 = 65e^(-5k)
e^(-5k) = 45/65
k = -ln(45/65)/5 ≈ 0.074

When is it drinkable (60°C)?

60 = 25 + 65e^(-0.074t)
35 = 65e^(-0.074t)
e^(-0.074t) = 35/65
t = -ln(35/65)/0.074 ≈ 8.0 minutes

**6. Carbon Dating**

C-14 half-life = 5730 years

Amount remaining: N = N₀(1/2)^(t/5730)

Artifact has 60% of original C-14. Age?

0.6 = (1/2)^(t/5730)
log(0.6) = (t/5730)log(0.5)
t = 5730 × log(0.6)/log(0.5) ≈ 4220 years old""",
                "content_zh": "指数和对数函数在实际问题中的应用。"
            }
        ],
        "exercises": []
    }
]

# Load existing chapters
with open('chapters/jc1_math_chapters.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

# Combine
all_chapters = existing + jc1_chapters_part3

# Save
with open('chapters/jc1_math_chapters.json', 'w', encoding='utf-8') as f:
    json.dump(all_chapters, f, ensure_ascii=False, indent=2)

print(f"Added {len(jc1_chapters_part3)} final JC 1 Mathematics chapters")
print(f"Total JC 1 chapters: {len(all_chapters)}")
print()
print("Final chapters added:")
for i, ch in enumerate(jc1_chapters_part3, 5):
    print(f"{i}. {ch['title']}: {len(ch['sections'])} sections")
print()
print("✅ All 8 JC 1 Mathematics chapters created!")
