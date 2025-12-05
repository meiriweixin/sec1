# JC 2 Mathematics Exercise Generation Guide

## Status: 2/120 exercises complete (1.7%)

This guide provides complete instructions for generating the remaining 118 JC 2 Mathematics exercises.

## Exercise Requirements

**Format:** Follow JC 1 pattern (proven successful)
- 15 exercises per chapter (5 easy, 5 medium, 5 hard)
- Pedagogical 6-step explanation format
- Bilingual (English + Chinese)
- Singapore-specific context
- Smart answer validation
- Multiple question types (MCQ, short answer)

## Chapter Structure

### Chapter 1: Integration Techniques (13/15 remaining)
**Topics:** Substitution, integration by parts, partial fractions
**Status:** 2 exercises created (both easy)
**Needed:** 3 more easy, 5 medium, 5 hard

**Singapore contexts to use:**
- MRT construction rates
- HDB population density modeling
- CPF investment returns
- NEWater production rates

**Exercise ideas:**
- Easy: Basic substitution (∫ 2x(x²+1)³ dx), standard integrals
- Medium: Integration by parts (∫ x ln x dx, ∫ x² e^x dx)
- Hard: Partial fractions with linear factors, combined techniques

### Chapter 2: Definite Integrals & Applications (0/15)
**Topics:** Fundamental theorem, area between curves, volumes of revolution
**Status:** 0 exercises
**Needed:** 5 easy, 5 medium, 5 hard

**Singapore contexts:**
- Changi Airport passenger traffic growth
- Land reclamation area calculations
- Marina Bay Sands architectural volumes
- Singapore Flyer rotation applications

**Exercise ideas:**
- Easy: Evaluate ∫₀² (2x + 3) dx, simple area under curve
- Medium: Area between y = x² and y = 2x, volume of revolution
- Hard: Multiple curves, washer method, shell method applications

### Chapter 3: Differential Equations (0/15)
**Topics:** Separable equations, growth/decay, Newton's cooling
**Status:** 0 exercises
**Needed:** 5 easy, 5 medium, 5 hard

**Singapore contexts:**
- COVID-19 infection modeling (logistic growth)
- Singapore solar panel adoption rates
- NEWater cooling processes
- Population growth projections

**Exercise ideas:**
- Easy: Solve dy/dx = 2y with y(0) = 3
- Medium: Exponential growth/decay with half-life
- Hard: Logistic growth, Newton's cooling with real data

### Chapter 4: Maclaurin Series (0/15)
**Topics:** Series expansions, approximations, operations with series
**Status:** 0 exercises
**Needed:** 5 easy, 5 medium, 5 hard

**Singapore contexts:**
- GPS accuracy calculations
- Bridge engineering (small deflections)
- Aerospace trajectory calculations
- Financial compound interest approximations

**Exercise ideas:**
- Easy: Find first 3 terms of e^x series, expand sin x
- Medium: Series operations, e^(2x), cos x · e^x
- Hard: Approximations with error bounds, √(1+x) applications

### Chapter 5: Permutations & Combinations (0/15)
**Topics:** Arrangements, selections, restrictions
**Status:** 0 exercises
**Needed:** 5 easy, 5 medium, 5 hard

**Singapore contexts:**
- MRT station routing
- National Service platoon selection
- HDB flat preference ranking
- Hawker center seating arrangements
- Car plate number combinations
- National Day VIP seating

**Exercise ideas:**
- Easy: ⁵P₃, ⁸C₃, factorial calculations
- Medium: Circular arrangements, repetitions (SINGAPORE)
- Hard: Restrictions (ethnic representation, seating constraints)

### Chapter 6: Probability & Distributions (0/15)
**Topics:** Probability rules, conditional probability, binomial distribution
**Status:** 0 exercises
**Needed:** 5 easy, 5 medium, 5 hard

**Singapore contexts:**
- COVID-19 testing (Bayes' theorem)
- ERP gantry taxi proportions
- Singapore weather (rainy days)
- 4D lottery expected value
- Grab driver earnings

**Exercise ideas:**
- Easy: P(A∪B), P(A|B), basic binomial
- Medium: Bayes' theorem, binomial with at least/at most
- Hard: Expectation and variance calculations, combined events

### Chapter 7: Sampling & Hypothesis Testing (0/15)
**Topics:** Central Limit Theorem, confidence intervals, hypothesis tests
**Status:** 0 exercises
**Needed:** 5 easy, 5 medium, 5 hard

**Singapore contexts:**
- HDB resale prices
- IT professional salaries (MOM data)
- Commute time surveys (LTA)
- Voter polls
- NEWater pH testing
- Vaccine effectiveness

**Exercise ideas:**
- Easy: Sample mean probability with CLT
- Medium: 95% confidence interval construction
- Hard: Hypothesis testing (two-tailed, one-tailed, p-values)

### Chapter 8: Complex Numbers (0/15)
**Topics:** Operations, Argand diagram, polar form, De Moivre's theorem
**Status:** 0 exercises
**Needed:** 5 easy, 5 medium, 5 hard

**Singapore contexts:**
- Electrical engineering (AC circuits, impedance)
- GPS navigation (ship displacement)
- Telecommunications (5G signal processing)
- Bridge/structural engineering
- ArtScience Museum architecture (rotational symmetry)

**Exercise ideas:**
- Easy: Add/subtract/multiply complex numbers, find modulus
- Medium: Convert to polar form, multiply/divide in polar
- Hard: De Moivre's theorem (powers), nth roots, geometric applications

## Implementation Steps

### Step 1: Create Exercise Files
For each chapter, create `create_jc2_exercises_chapterN.py`:

```python
import json

with open('chapters/jc2_math_chapters.json', 'r', encoding='utf-8') as f:
    jc2_chapters = json.load(f)

chapter_N_exercises = [
    # 15 exercises following template
]

# Find and update chapter
for ch in jc2_chapters:
    if ch['id'] == 'chapter-id-jc2':
        ch['exercises'] = chapter_N_exercises
        print(f"✓ Added {len(chapter_N_exercises)} exercises")
        break

# Save
with open('chapters/jc2_math_chapters.json', 'w', encoding='utf-8') as f:
    json.dump(jc2_chapters, f, ensure_ascii=False, indent=2)
```

### Step 2: Exercise Template

```python
{
    "id": "chapter-abbrev-jc2-exN",
    "type": "mcq",  # or "short"
    "difficulty": "easy",  # or "medium", "hard"
    "prompt": "English question text",
    "prompt_zh": "中文问题文本",
    "choices": ["A", "B", "C", "D"],  # MCQ only
    "choices_zh": ["A", "B", "C", "D"],  # MCQ only
    "answer": 0,  # or string for short answer
    "validator": "smart",  # for short answer, optional
    "explanation": "**Problem:** ...\n\n**Key Concept:** ...\n\n**Steps:**\n1. ...\n\n**Answer:** ...\n\n**Common Mistakes:** ...\n\n**Tip:** ...",
    "explanation_zh": "**问题：** ...\n\n**关键概念：** ...\n\n**步骤：**\n1. ...\n\n**答案：** ...\n\n**常见错误：** ...\n\n**提示：** ..."
}
```

### Step 3: Batch Creation Order

1. **Batch 1:** Chapters 1-2 (Integration) - 30 exercises
2. **Batch 2:** Chapters 3-4 (DE & Maclaurin) - 30 exercises
3. **Batch 3:** Chapters 5-6 (Counting & Probability) - 30 exercises
4. **Batch 4:** Chapters 7-8 (Stats & Complex) - 30 exercises

### Step 4: Integration

After all exercises created:

```python
# integrate_jc2.py
import json
from datetime import datetime

# Backup
backup_file = f'src/data/content-backup-jc2-{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    backup = json.load(f)
with open(backup_file, 'w', encoding='utf-8') as f:
    json.dump(backup, f, ensure_ascii=False, indent=2)

# Load JC 2 chapters and main content
with open('chapters/jc2_math_chapters.json', 'r', encoding='utf-8') as f:
    jc2_chapters = json.load(f)
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    content = json.load(f)

# Find Math subject and append JC 2 chapters
for subject in content['subjects']:
    if subject['id'] == 'math':
        subject['chapters'].extend(jc2_chapters)
        break

# Save
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(content, f, ensure_ascii=False, indent=2)

print("✓ JC 2 chapters integrated into content.json")
```

## Quality Checklist

Before marking complete, verify:
- [ ] All 120 exercises created (15 per chapter)
- [ ] Difficulty distribution: 5-5-5 per chapter
- [ ] All explanations use 6-step format
- [ ] Bilingual content (English + Chinese)
- [ ] Singapore context in examples
- [ ] Answer validation tested
- [ ] Integrated into main content.json
- [ ] Total exercise count updated in CLAUDE.md

## Expected Final Totals

After JC 2 completion:
- **Total chapters:** 151 (143 current + 8 JC 2)
- **Total exercises:** 2,235 (2,115 current + 120 JC 2)
- **Mathematics exercises:** 900 (780 current + 120 JC 2)
- **JC Mathematics exercises:** 240 (120 JC 1 + 120 JC 2)

## Chapter IDs Reference

```
integration-techniques-jc2
definite-integrals-applications-jc2
differential-equations-jc2
maclaurin-series-jc2
permutations-combinations-jc2
probability-distributions-jc2
sampling-hypothesis-testing-jc2
complex-numbers-jc2
```

## Notes

- Refer to `create_jc1_exercises_batch*.py` for working examples
- Use existing JC 1 exercises as quality benchmark
- Maintain consistency with platform's exercise validation system
- Test small batches before creating full sets
- Singapore context is mandatory for engagement
