# Chapter Update Examples & Templates

This document provides concrete examples of how to transform chapters from their current state to the required concept + example pattern.

---

## Template Structure

### Standard Pattern (Minimum 2-3 Pairs)

```json
{
  "id": "chapter-id",
  "title": "Chapter Title",
  "title_zh": "章节标题",
  "sections": [
    {
      "type": "text",
      "title": "Concept 1: Introduction to Topic",
      "title_zh": "概念1：主题简介",
      "content": "Explain the core concept here with clear definitions and explanations."
    },
    {
      "type": "example",
      "title": "Example 1: Applying Concept 1",
      "title_zh": "例子1：应用概念1",
      "content": "Step 1: [First step]\nStep 2: [Second step]\nAnswer: [Final answer]"
    },
    {
      "type": "text",
      "title": "Concept 2: Building on the Basics",
      "title_zh": "概念2：深入基础",
      "content": "Explain the next concept, building on concept 1."
    },
    {
      "type": "example",
      "title": "Example 2: Applying Concept 2",
      "title_zh": "例子2：应用概念2",
      "content": "Step 1: [First step]\nStep 2: [Second step]\nAnswer: [Final answer]"
    }
  ],
  "exercises": [...]
}
```

---

## Example 1: Transforming a MINIMAL Chapter (🔴)

### BEFORE: sentence-construction (1 section only)

```json
{
  "id": "sentence-construction",
  "title": "Sentence Construction",
  "title_zh": "句子结构",
  "sections": [
    {
      "type": "text",
      "content": "SENTENCE FRAGMENT: Incomplete sentence missing subject or verb. Example: 'Running in the park.' (Who is running?) FIX: 'The dog is running in the park.'\n\nRUN-ON SENTENCE: Two or more complete sentences joined incorrectly. Example: 'I love reading books are my favorite.' FIX: 'I love reading. Books are my favorite.' OR 'I love reading because books are my favorite.'\n\nSENTENCE VARIETY: Mix short and long sentences. Use different sentence beginnings. Combine simple sentences into compound (two independent clauses with and/but/or) or complex sentences (independent + dependent clause with because/although/when)."
    }
  ]
}
```

### AFTER: sentence-construction (Expanded with examples)

```json
{
  "id": "sentence-construction",
  "title": "Sentence Construction",
  "title_zh": "句子结构",
  "sections": [
    {
      "type": "text",
      "title": "Concept 1: Sentence Fragments and How to Fix Them",
      "title_zh": "概念1：句子片段及修正方法",
      "content": "A SENTENCE FRAGMENT is an incomplete sentence that's missing a subject, verb, or complete thought. It cannot stand alone as a proper sentence.\n\nCommon fragment types:\n• Missing subject: 'Running in the park.'\n• Missing verb: 'The big brown dog in the park.'\n• Dependent clause alone: 'Because I was tired.'\n\nTo fix fragments: Add the missing subject or verb, or connect to a complete sentence."
    },
    {
      "type": "example",
      "title": "Example 1: Fixing Sentence Fragments",
      "title_zh": "例子1：修正句子片段",
      "content": "FRAGMENT: 'Running in the park every morning.'\nProblem: Missing subject (who is running?) and helping verb\nFIX: 'I am running in the park every morning.'\n\nFRAGMENT: 'Because the exam was difficult.'\nProblem: Dependent clause without main clause\nFIX: 'I studied hard because the exam was difficult.'\n\nFRAGMENT: 'The student with the blue backpack.'\nProblem: Missing verb (what about the student?)\nFIX: 'The student with the blue backpack arrived late.'"
    },
    {
      "type": "text",
      "title": "Concept 2: Run-On Sentences and Correction Methods",
      "title_zh": "概念2：连写句及修正方法",
      "content": "A RUN-ON SENTENCE incorrectly joins two or more independent clauses without proper punctuation or conjunctions.\n\nTypes of run-ons:\n• Fused sentence: Two sentences with no punctuation between them\n• Comma splice: Two sentences joined with only a comma\n\nCorrection methods:\n1. Separate into two sentences (use period)\n2. Use coordinating conjunction (and, but, or, so) with comma\n3. Use semicolon\n4. Use subordinating conjunction (because, although, when)"
    },
    {
      "type": "example",
      "title": "Example 2: Fixing Run-On Sentences",
      "title_zh": "例子2：修正连写句",
      "content": "RUN-ON: 'I love reading books are my favorite.'\n\nMethod 1 - Separate: 'I love reading. Books are my favorite.'\nMethod 2 - Conjunction: 'I love reading, and books are my favorite.'\nMethod 3 - Semicolon: 'I love reading; books are my favorite.'\nMethod 4 - Subordination: 'I love reading because books are my favorite.'\n\nRUN-ON: 'The weather is hot we should go swimming.'\nCORRECTION: 'The weather is hot, so we should go swimming.'"
    },
    {
      "type": "text",
      "title": "Concept 3: Sentence Variety for Better Writing",
      "title_zh": "概念3：句子多样性提升写作",
      "content": "Good writers use SENTENCE VARIETY to make writing more interesting and engaging.\n\nTechniques:\n1. Mix sentence lengths (short, medium, long)\n2. Vary sentence beginnings (don't always start with subject)\n3. Combine sentence types:\n   • Simple: One independent clause\n   • Compound: Two independent clauses (and, but, or)\n   • Complex: Independent + dependent clause (because, although, when)"
    },
    {
      "type": "example",
      "title": "Example 3: Adding Sentence Variety",
      "title_zh": "例子3：增加句子多样性",
      "content": "BORING (all simple, same structure):\n'I woke up. I brushed my teeth. I ate breakfast. I went to school.'\n\nBETTER (varied lengths and structures):\n'I woke up early. After brushing my teeth and eating a quick breakfast, I rushed to catch the bus to school.'\n\nTechniques used:\n✓ Combined related actions\n✓ Used transitional phrases ('After')\n✓ Mixed short sentence with longer complex sentence\n✓ Varied sentence beginnings"
    }
  ],
  "exercises": [...]
}
```

**Key Changes:**
- Expanded from 1 to 6 sections (3 concept + 3 example pairs)
- Added clear titles for each section
- Separated concepts into logical progression
- Added detailed, step-by-step examples
- Used Singapore Secondary 1 appropriate content

---

## Example 2: Transforming a NO_EXAMPLES Chapter (🔵)

### BEFORE: chinese-grammar-basics (2 texts, no examples)

```json
{
  "id": "chinese-grammar-basics",
  "title": "Grammar Fundamentals",
  "title_zh": "语法基础",
  "sections": [
    {
      "type": "text",
      "content": "Chinese sentence structure follows: 主语(Subject) + 谓语(Predicate) + 宾语(Object). Example: 我(S) 吃(V) 苹果(O) = I eat apple. Time/place often goes BEFORE the verb: 昨天(time) 我 在学校(place) 见到 他 = Yesterday I at school saw him."
    },
    {
      "type": "text",
      "content": "Measure words (量词) are essential in Chinese. Common ones: 个(general), 本(books), 张(flat items), 只(animals), 条(long items). Pattern: Number + Measure Word + Noun. Example: 三本书 (three books), 一只猫 (one cat), 两张纸 (two sheets of paper)."
    }
  ]
}
```

### AFTER: chinese-grammar-basics (2 concepts + 2 examples)

```json
{
  "id": "chinese-grammar-basics",
  "title": "Grammar Fundamentals",
  "title_zh": "语法基础",
  "sections": [
    {
      "type": "text",
      "title": "Concept 1: Basic Chinese Sentence Structure",
      "title_zh": "概念1：基本汉语句子结构",
      "content": "Chinese sentence structure follows a clear pattern:\n\n主语(Subject) + 谓语(Predicate/Verb) + 宾语(Object)\n\nKey differences from English:\n• Time words (昨天, 今天, 明天) come BEFORE the verb\n• Place words (在学校, 在家) also come BEFORE the verb\n• Pattern: Subject + Time + Place + Verb + Object\n\nExample structure: 我(S) + 昨天(T) + 在学校(P) + 见到(V) + 他(O)\n= Yesterday I at school saw him\n= I saw him at school yesterday"
    },
    {
      "type": "example",
      "title": "Example 1: Building Correct Chinese Sentences",
      "title_zh": "例子1：构建正确的汉语句子",
      "content": "Let's build sentences with proper word order:\n\nExample 1 - Simple sentence:\n我 吃 苹果\n(I) (eat) (apple)\n= I eat an apple\n\nExample 2 - Adding time:\n❌ WRONG: 我 吃 苹果 昨天 (time at end)\n✅ CORRECT: 我 昨天 吃 苹果 (time before verb)\n= I ate an apple yesterday\n\nExample 3 - Adding time AND place:\n我 + 昨天 + 在学校 + 见到 + 他\n(I) (yesterday) (at school) (saw) (him)\n= I saw him at school yesterday\n\nExample 4 - Common Singapore context:\n我 今天 在巴刹 买 菜\n(I) (today) (at market) (buy) (vegetables)\n= I bought vegetables at the market today"
    },
    {
      "type": "text",
      "title": "Concept 2: Measure Words (量词)",
      "title_zh": "概念2：量词",
      "content": "Chinese requires MEASURE WORDS between numbers and nouns. You cannot say '三书' (three books) - you must use the correct measure word.\n\nPattern: Number + Measure Word + Noun\n\nCommon measure words:\n• 个 (gè) - General/default, people\n• 本 (běn) - Books, notebooks\n• 张 (zhāng) - Flat objects (paper, photos, tables)\n• 只 (zhī) - Animals, some objects\n• 条 (tiáo) - Long objects (fish, pants, rivers)\n• 件 (jiàn) - Clothes, matters\n• 杯 (bēi) - Cups/glasses of liquid\n• 碗 (wǎn) - Bowls of food"
    },
    {
      "type": "example",
      "title": "Example 2: Using Measure Words Correctly",
      "title_zh": "例子2：正确使用量词",
      "content": "Practice using the right measure word:\n\nBooks/Notebooks (本):\n一本书 (yī běn shū) = one book\n三本笔记本 (sān běn bǐjìběn) = three notebooks\n\nFlat items (张):\n两张纸 (liǎng zhāng zhǐ) = two sheets of paper\n一张桌子 (yī zhāng zhuōzi) = one table\n四张照片 (sì zhāng zhàopiàn) = four photos\n\nAnimals (只):\n一只猫 (yī zhī māo) = one cat\n五只鸡 (wǔ zhī jī) = five chickens\n\nSingapore examples:\n两杯咖啡 (liǎng bēi kāfēi) = two cups of coffee (kopi)\n三件校服 (sān jiàn xiàofú) = three school uniforms\n一碗叻沙 (yī wǎn lèshā) = one bowl of laksa\n\nCommon mistake:\n❌ 三书 (missing measure word)\n✅ 三本书 (correct with 本)"
    }
  ],
  "exercises": [...]
}
```

**Key Changes:**
- Kept 2 main concepts (good structure)
- Added clear titles with English + Chinese
- Added 2 example sections with step-by-step demonstrations
- Used Singapore context (巴刹/market, 咖啡/kopi, 叻沙/laksa)
- Showed common mistakes and corrections
- Progressive difficulty in examples

---

## Example 3: Transforming a PARTIAL Chapter (🟡)

### BEFORE: integers-rational (5 unpaired texts)

```json
{
  "sections": [
    {
      "type": "text",
      "content": "Integers include positive numbers..."
    },
    {
      "type": "text",
      "content": "We use integers in everyday life..."
    },
    {
      "type": "animation",
      "content": "NumberLineReveal"
    },
    {
      "type": "text",
      "content": "Concept: When adding integers with the same sign..."
    },
    {
      "type": "text",
      "content": "Concept: When adding integers with different signs..."
    },
    {
      "type": "text",
      "content": "Concept: To subtract integers..."
    },
    {
      "type": "text",
      "content": "Concept: When multiplying or dividing with same sign..."
    },
    {
      "type": "text",
      "content": "Concept: When multiplying or dividing with different signs..."
    },
    {
      "type": "animation",
      "content": "NumberLineReveal"
    }
  ]
}
```

**Problems:**
- Text sections 3, 4, 5, 6, 7 have no following examples
- Animations at positions 2 and 8 aren't paired with specific concepts

### AFTER: integers-rational (Properly paired)

```json
{
  "sections": [
    {
      "type": "text",
      "title": "Introduction to Integers",
      "title_zh": "整数简介",
      "content": "Integers include positive numbers..."
    },
    {
      "type": "text",
      "title": "Real-World Integer Examples",
      "title_zh": "整数的实际应用",
      "content": "We use integers in everyday life..."
    },
    {
      "type": "animation",
      "title": "Visualizing the Number Line",
      "title_zh": "数轴可视化",
      "content": "NumberLineReveal",
      "props": {
        "showNegatives": true,
        "range": [-10, 10]
      }
    },
    {
      "type": "text",
      "title": "Concept 1: Adding Integers (Same Sign)",
      "title_zh": "概念1：相同符号整数相加",
      "content": "When adding integers with the same sign, add the numbers and keep the sign.\n\nRule: (+) + (+) = (+)  or  (-) + (-) = (-)"
    },
    {
      "type": "example",
      "title": "Example 1: Adding Same Sign Integers",
      "title_zh": "例子1：相同符号整数相加",
      "content": "Example A: (+5) + (+3)\nStep 1: Both positive, add numbers: 5 + 3 = 8\nStep 2: Keep positive sign\nAnswer: +8\n\nExample B: (-7) + (-2)\nStep 1: Both negative, add numbers: 7 + 2 = 9\nStep 2: Keep negative sign\nAnswer: -9\n\nSingapore context: Temperature drops 3°C in morning, then drops 2°C more = -3 + (-2) = -5°C total drop"
    },
    {
      "type": "text",
      "title": "Concept 2: Adding Integers (Different Signs)",
      "title_zh": "概念2：不同符号整数相加",
      "content": "When adding integers with different signs, subtract the smaller from the larger and take the sign of the larger number.\n\nRule: (+) + (-) or (-) + (+) = sign of larger number"
    },
    {
      "type": "example",
      "title": "Example 2: Adding Different Sign Integers",
      "title_zh": "例子2：不同符号整数相加",
      "content": "Example A: (+8) + (-3)\nStep 1: Different signs, subtract: 8 - 3 = 5\nStep 2: Larger number was positive, so answer is positive\nAnswer: +5\n\nExample B: (-10) + (+4)\nStep 1: Different signs, subtract: 10 - 4 = 6\nStep 2: Larger number was negative, so answer is negative\nAnswer: -6\n\nBank account example: Start with $8 credit, spend $3 = +8 + (-3) = +5 (still $5 credit)"
    },
    {
      "type": "text",
      "title": "Concept 3: Subtracting Integers",
      "title_zh": "概念3：整数减法",
      "content": "To subtract integers, change subtraction to ADDITION and flip the sign of the second number.\n\nRule: a - b = a + (-b)\n\nThen follow addition rules."
    },
    {
      "type": "example",
      "title": "Example 3: Subtracting Integers",
      "title_zh": "例子3：整数减法",
      "content": "Example A: (+7) - (+3)\nStep 1: Change to addition: (+7) + (-3)\nStep 2: Apply addition rules: 7 - 3 = 4\nAnswer: +4\n\nExample B: (-5) - (+2)\nStep 1: Change to addition: (-5) + (-2)\nStep 2: Same sign, add: 5 + 2 = 7, keep negative\nAnswer: -7\n\nExample C: (-4) - (-6)\nStep 1: Change to addition: (-4) + (+6)\nStep 2: Different signs: 6 - 4 = 2, positive wins\nAnswer: +2\n\nElevator example: Start at floor -2, go down 3 floors = -2 - 3 = -2 + (-3) = -5"
    },
    {
      "type": "text",
      "title": "Concept 4: Multiplying/Dividing (Same Sign)",
      "title_zh": "概念4：相同符号整数乘除",
      "content": "When multiplying or dividing integers with the SAME sign, the answer is POSITIVE.\n\nRules:\n(+) × (+) = (+)    or    (+) ÷ (+) = (+)\n(-) × (-) = (+)    or    (-) ÷ (-) = (+)"
    },
    {
      "type": "example",
      "title": "Example 4: Multiplying/Dividing Same Signs",
      "title_zh": "例子4：相同符号整数乘除",
      "content": "Multiplication:\nExample A: (+4) × (+3) = +12 (positive × positive = positive)\nExample B: (-5) × (-2) = +10 (negative × negative = positive)\n\nDivision:\nExample C: (+12) ÷ (+3) = +4\nExample D: (-20) ÷ (-4) = +5\n\nMemory trick: Same signs = Positive result"
    },
    {
      "type": "text",
      "title": "Concept 5: Multiplying/Dividing (Different Signs)",
      "title_zh": "概念5：不同符号整数乘除",
      "content": "When multiplying or dividing integers with DIFFERENT signs, the answer is NEGATIVE.\n\nRules:\n(+) × (-) = (-)    or    (+) ÷ (-) = (-)\n(-) × (+) = (-)    or    (-) ÷ (+) = (-)"
    },
    {
      "type": "example",
      "title": "Example 5: Multiplying/Dividing Different Signs",
      "title_zh": "例子5：不同符号整数乘除",
      "content": "Multiplication:\nExample A: (+6) × (-2) = -12\nExample B: (-4) × (+5) = -20\n\nDivision:\nExample C: (+15) ÷ (-3) = -5\nExample D: (-18) ÷ (+6) = -3\n\nDebt example: Borrow $5 from 3 friends = 3 × (-5) = -15 (owe $15 total)\n\nMemory trick: Different signs = Negative result"
    }
  ]
}
```

**Key Changes:**
- Separated concepts into 5 clear text sections with titles
- Added 5 example sections (one for each concept)
- Kept animations but added titles for clarity
- Every concept now has a paired example
- Examples include Singapore context (temperature, bank, elevator)
- Progressive difficulty

---

## Quick Checklist for Any Chapter Update

### Before Submitting:
- [ ] Minimum 2-3 concept+example pairs (4-6 sections total)
- [ ] Every text section followed by example/animation/math section
- [ ] All sections have `title` and `title_zh` fields
- [ ] Examples show step-by-step solutions
- [ ] Singapore-relevant context used where appropriate
- [ ] Content appropriate for Secondary 1 level
- [ ] Both English and Chinese translations accurate
- [ ] Progressive difficulty in examples
- [ ] Clear explanations in concepts
- [ ] No orphaned text sections without examples

---

## Common Patterns by Subject

### Mathematics Chapters
- Concept (text) → Example (example or math)
- Use Singapore context: HDB floors, MRT stations, hawker center prices
- Show multiple worked examples with steps
- Include common mistakes section

### Science Chapters
- Concept (text) → Example/Demonstration (example or animation)
- Use Singapore examples: tropical weather, local plants/animals
- Include safety notes where relevant
- Real-world applications

### Language Chapters (English/Chinese)
- Rule/Technique (text) → Practice Example (example)
- Show before/after corrections
- Include common errors
- Use Singapore context: local places, multicultural references

---

## Section Type Guidelines

### `type: "text"` (Concept sections)
- Clear explanation of concept
- Definitions and rules
- When to use the concept
- Why it's important

### `type: "example"` (Example sections)
- Step-by-step worked solutions
- Multiple examples (at least 2-3)
- Show reasoning at each step
- Include final answer
- Relate to real Singapore context

### `type: "animation"` (Visual demonstrations)
- Name the animation component
- Add props if needed
- Pair with concept OR example section
- Use for complex spatial/visual concepts

### `type: "math"` (Mathematical formulas)
- Show formula clearly
- Explain each variable
- Include when to use it
- Pair with worked examples

---

**End of Examples Document**

For detailed analysis of all chapters, see:
- CHAPTER_UPDATE_PRIORITIES.md (full detailed report)
- CHAPTER_UPDATE_QUICK_REFERENCE.md (quick lookup table)
