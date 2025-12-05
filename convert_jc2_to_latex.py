import json

# Load JC 2 chapters
with open('chapters/jc2_math_chapters.json', 'r', encoding='utf-8') as f:
    chapters = json.load(f)

# Manual fixes for Integration by Parts section (Chapter 1, Section 2)
for ch in chapters:
    if ch['id'] == 'integration-techniques-jc2':
        for section in ch['sections']:
            if section['id'] == 'integration-by-parts':
                # Replace content with proper LaTeX
                section['content'] = """**Integration by parts** is the reverse of the product rule for differentiation. It's used when integrating products of functions.

**Formula:**
$$\\int u \\, dv = uv - \\int v \\, du$$

Alternatively: $\\int u(x)v'(x) \\, dx = u(x)v(x) - \\int u'(x)v(x) \\, dx$

**ILATE rule** for choosing $u$ (in priority order):
- **I**nverse trig functions ($\\arcsin x$, $\\arctan x$)
- **L**ogarithmic functions ($\\ln x$, $\\log x$)
- **A**lgebraic functions ($x^2$, $3x + 1$)
- **T**rigonometric functions ($\\sin x$, $\\cos x$)
- **E**xponential functions ($e^x$, $2^x$)

**Example: Singapore population modeling**

Suppose Singapore's aging population density in a certain district is modeled by $\\int x e^{-x} \\, dx$ (where $x$ represents age groups).

Using ILATE: $u = x$ (algebraic), $dv = e^{-x} \\, dx$

Then: $du = dx$, $v = -e^{-x}$

Applying formula:

$$\\int x e^{-x} \\, dx = x(-e^{-x}) - \\int (-e^{-x}) \\, dx$$

$$= -x e^{-x} + \\int e^{-x} \\, dx$$

$$= -x e^{-x} - e^{-x} + C$$

$$= -e^{-x}(x + 1) + C$$

This helps government agencies plan healthcare and senior services."""

                section['content_zh'] = """**分部积分**是微分乘积法则的逆运算。用于积分函数乘积。

**公式：**
$$\\int u \\, dv = uv - \\int v \\, du$$

或者：$\\int u(x)v'(x) \\, dx = u(x)v(x) - \\int u'(x)v(x) \\, dx$

**ILATE 规则**选择 $u$（按优先级）：
- **I** 反三角函数（$\\arcsin x$、$\\arctan x$）
- **L** 对数函数（$\\ln x$、$\\log x$）
- **A** 代数函数（$x^2$、$3x + 1$）
- **T** 三角函数（$\\sin x$、$\\cos x$）
- **E** 指数函数（$e^x$、$2^x$）

**例子：新加坡人口建模**

假设新加坡某区的老龄人口密度由 $\\int x e^{-x} \\, dx$ 建模（$x$ 代表年龄组）。

使用 ILATE：$u = x$（代数），$dv = e^{-x} \\, dx$

则：$du = dx$，$v = -e^{-x}$

应用公式：

$$\\int x e^{-x} \\, dx = x(-e^{-x}) - \\int (-e^{-x}) \\, dx$$

$$= -x e^{-x} + \\int e^{-x} \\, dx$$

$$= -x e^{-x} - e^{-x} + C$$

$$= -e^{-x}(x + 1) + C$$

这有助于政府机构规划医疗保健和老年服务。"""

# Save updated chapters
with open('chapters/jc2_math_chapters.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, ensure_ascii=False, indent=2)

print("✓ Fixed Integration by Parts section with proper LaTeX notation")
print("\nKey changes:")
print("  - Formulas now use $...$ for inline and $$...$$ for display math")
print("  - e^(-x) → $e^{-x}$")
print("  - Integral symbols properly formatted with \\int")
print("  - Function names use \\sin, \\cos, \\ln, etc.")
