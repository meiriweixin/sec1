import json

# Load current content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Define exercises for geometry chapters
exercises_by_chapter = {
    'inequalities': [
        {
            "id": "ineq-ex4",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "Solve: x + 5 > 10",
            "prompt_zh": "解：x + 5 > 10",
            "choices": ["x > 5", "x < 5", "x > 15", "x < 15"],
            "choices_zh": ["x > 5", "x < 5", "x > 15", "x < 15"],
            "answer": 0,
            "explanation": "Subtract 5 from both sides: x > 10 - 5, x > 5",
            "explanation_zh": "两边都减5：x > 10 - 5，x > 5"
        },
        {
            "id": "ineq-ex5",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "Solve: 3x < 12",
            "prompt_zh": "解：3x < 12",
            "choices": ["x < 4", "x > 4", "x < 36", "x > 36"],
            "choices_zh": ["x < 4", "x > 4", "x < 36", "x > 36"],
            "answer": 0,
            "explanation": "Divide both sides by 3: x < 12/3, x < 4",
            "explanation_zh": "两边都除以3：x < 12/3，x < 4"
        },
        {
            "id": "ineq-ex6",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "Solve: -2x ≥ 8",
            "prompt_zh": "解：-2x ≥ 8",
            "choices": ["x ≤ -4", "x ≥ -4", "x ≤ 4", "x ≥ 4"],
            "choices_zh": ["x ≤ -4", "x ≥ -4", "x ≤ 4", "x ≥ 4"],
            "answer": 0,
            "explanation": "Divide by -2 (flip inequality): x ≤ -4",
            "explanation_zh": "除以-2（翻转不等号）：x ≤ -4"
        },
        {
            "id": "ineq-ex7",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "Which value satisfies x > 3?",
            "prompt_zh": "哪个值满足x > 3？",
            "choices": ["4", "3", "2", "1"],
            "choices_zh": ["4", "3", "2", "1"],
            "answer": 0,
            "explanation": "Only 4 is greater than 3",
            "explanation_zh": "只有4大于3"
        },
        {
            "id": "ineq-ex8",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "Solve: 2x + 3 ≤ 11",
            "prompt_zh": "解：2x + 3 ≤ 11",
            "choices": ["x ≤ 4", "x ≥ 4", "x ≤ 7", "x ≥ 7"],
            "choices_zh": ["x ≤ 4", "x ≥ 4", "x ≤ 7", "x ≥ 7"],
            "answer": 0,
            "explanation": "Subtract 3: 2x ≤ 8. Divide by 2: x ≤ 4",
            "explanation_zh": "减3：2x ≤ 8。除以2：x ≤ 4"
        },
        {
            "id": "ineq-ex9",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "Solve: 5 - x > 2",
            "prompt_zh": "解：5 - x > 2",
            "choices": ["x < 3", "x > 3", "x < 7", "x > 7"],
            "choices_zh": ["x < 3", "x > 3", "x < 7", "x > 7"],
            "answer": 0,
            "explanation": "Subtract 5: -x > -3. Multiply by -1 (flip): x < 3",
            "explanation_zh": "减5：-x > -3。乘以-1（翻转）：x < 3"
        },
        {
            "id": "ineq-ex10",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "Which inequality represents: 'x is at most 7'?",
            "prompt_zh": "哪个不等式表示：\"x最多为7\"？",
            "choices": ["x ≤ 7", "x < 7", "x ≥ 7", "x > 7"],
            "choices_zh": ["x ≤ 7", "x < 7", "x ≥ 7", "x > 7"],
            "answer": 0,
            "explanation": "'At most' means 'less than or equal to': x ≤ 7",
            "explanation_zh": "\"最多\"意思是\"小于或等于\"：x ≤ 7"
        },
        {
            "id": "ineq-ex11",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "Solve: x - 4 < 6",
            "prompt_zh": "解：x - 4 < 6",
            "choices": ["x < 10", "x > 10", "x < 2", "x > 2"],
            "choices_zh": ["x < 10", "x > 10", "x < 2", "x > 2"],
            "answer": 0,
            "explanation": "Add 4 to both sides: x < 10",
            "explanation_zh": "两边都加4：x < 10"
        },
        {
            "id": "ineq-ex12",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "Solve: 3(x - 2) > 9",
            "prompt_zh": "解：3(x - 2) > 9",
            "choices": ["x > 5", "x < 5", "x > 3", "x < 3"],
            "choices_zh": ["x > 5", "x < 5", "x > 3", "x < 3"],
            "answer": 0,
            "explanation": "Divide by 3: x - 2 > 3. Add 2: x > 5",
            "explanation_zh": "除以3：x - 2 > 3。加2：x > 5"
        },
        {
            "id": "ineq-ex13",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "Which value does NOT satisfy x ≥ -2?",
            "prompt_zh": "哪个值不满足x ≥ -2？",
            "choices": ["-3", "-2", "0", "5"],
            "choices_zh": ["-3", "-2", "0", "5"],
            "answer": 0,
            "explanation": "-3 < -2, so it doesn't satisfy x ≥ -2",
            "explanation_zh": "-3 < -2，所以它不满足x ≥ -2"
        },
        {
            "id": "ineq-ex14",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "Solve: x/2 > 3",
            "prompt_zh": "解：x/2 > 3",
            "choices": ["x > 6", "x < 6", "x > 1.5", "x < 1.5"],
            "choices_zh": ["x > 6", "x < 6", "x > 1.5", "x < 1.5"],
            "answer": 0,
            "explanation": "Multiply both sides by 2: x > 6",
            "explanation_zh": "两边都乘以2：x > 6"
        },
        {
            "id": "ineq-ex15",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "A student needs at least 80 marks to pass. Write an inequality for marks m:",
            "prompt_zh": "一个学生需要至少80分才能及格。为分数m写一个不等式：",
            "choices": ["m ≥ 80", "m > 80", "m ≤ 80", "m < 80"],
            "choices_zh": ["m ≥ 80", "m > 80", "m ≤ 80", "m < 80"],
            "answer": 0,
            "explanation": "'At least 80' means 'greater than or equal to 80': m ≥ 80",
            "explanation_zh": "\"至少80\"意思是\"大于或等于80\"：m ≥ 80"
        }
    ],
    'angles-geometry': [
        {
            "id": "geo-ex2",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "What is the sum of angles in a triangle?",
            "prompt_zh": "三角形的内角和是多少？",
            "choices": ["180°", "360°", "90°", "270°"],
            "choices_zh": ["180°", "360°", "90°", "270°"],
            "answer": 0,
            "explanation": "The sum of all angles in any triangle is always 180°",
            "explanation_zh": "任何三角形的内角和总是180°"
        },
        {
            "id": "geo-ex3",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "Two angles are complementary. One angle is 35°. Find the other:",
            "prompt_zh": "两个角互为余角。一个角是35°。求另一个：",
            "choices": ["55°", "145°", "90°", "180°"],
            "choices_zh": ["55°", "145°", "90°", "180°"],
            "answer": 0,
            "explanation": "Complementary angles add to 90°. Other angle = 90° - 35° = 55°",
            "explanation_zh": "余角之和为90°。另一个角 = 90° - 35° = 55°"
        },
        {
            "id": "geo-ex4",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "Two angles are supplementary. One angle is 120°. Find the other:",
            "prompt_zh": "两个角互为补角。一个角是120°。求另一个：",
            "choices": ["60°", "90°", "240°", "180°"],
            "choices_zh": ["60°", "90°", "240°", "180°"],
            "answer": 0,
            "explanation": "Supplementary angles add to 180°. Other angle = 180° - 120° = 60°",
            "explanation_zh": "补角之和为180°。另一个角 = 180° - 120° = 60°"
        },
        {
            "id": "geo-ex5",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "What type of angle is 45°?",
            "prompt_zh": "45°是什么类型的角？",
            "choices": ["Acute", "Right", "Obtuse", "Straight"],
            "choices_zh": ["锐角", "直角", "钝角", "平角"],
            "answer": 0,
            "explanation": "Acute angles are between 0° and 90°",
            "explanation_zh": "锐角在0°到90°之间"
        },
        {
            "id": "geo-ex6",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "Find angle x if angles on a straight line are x and 2x:",
            "prompt_zh": "如果直线上的角是x和2x，求角x：",
            "choices": ["60°", "90°", "120°", "180°"],
            "choices_zh": ["60°", "90°", "120°", "180°"],
            "answer": 0,
            "explanation": "Angles on a straight line: x + 2x = 180°, 3x = 180°, x = 60°",
            "explanation_zh": "直线上的角：x + 2x = 180°，3x = 180°，x = 60°"
        },
        {
            "id": "geo-ex7",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "Vertically opposite angles are:",
            "prompt_zh": "对顶角是：",
            "choices": ["Equal", "Supplementary", "Complementary", "Different"],
            "choices_zh": ["相等", "互补", "互余", "不同"],
            "answer": 0,
            "explanation": "Vertically opposite angles are always equal",
            "explanation_zh": "对顶角总是相等"
        },
        {
            "id": "geo-ex8",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "What is a right angle?",
            "prompt_zh": "什么是直角？",
            "choices": ["90°", "180°", "45°", "270°"],
            "choices_zh": ["90°", "180°", "45°", "270°"],
            "answer": 0,
            "explanation": "A right angle measures exactly 90°",
            "explanation_zh": "直角正好是90°"
        },
        {
            "id": "geo-ex9",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "In triangle ABC, angle A = 50°, angle B = 60°. Find angle C:",
            "prompt_zh": "在三角形ABC中，角A = 50°，角B = 60°。求角C：",
            "choices": ["70°", "110°", "120°", "130°"],
            "choices_zh": ["70°", "110°", "120°", "130°"],
            "answer": 0,
            "explanation": "Sum = 180°. Angle C = 180° - 50° - 60° = 70°",
            "explanation_zh": "和 = 180°。角C = 180° - 50° - 60° = 70°"
        },
        {
            "id": "geo-ex10",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "Parallel lines cut by a transversal form alternate angles that are:",
            "prompt_zh": "平行线被截线所截形成的内错角是：",
            "choices": ["Equal", "Supplementary", "Complementary", "Different"],
            "choices_zh": ["相等", "互补", "互余", "不同"],
            "answer": 0,
            "explanation": "Alternate angles formed by parallel lines are equal",
            "explanation_zh": "平行线形成的内错角相等"
        },
        {
            "id": "geo-ex11",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "What type of angle is 150°?",
            "prompt_zh": "150°是什么类型的角？",
            "choices": ["Obtuse", "Acute", "Right", "Reflex"],
            "choices_zh": ["钝角", "锐角", "直角", "优角"],
            "answer": 0,
            "explanation": "Obtuse angles are between 90° and 180°",
            "explanation_zh": "钝角在90°到180°之间"
        },
        {
            "id": "geo-ex12",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "Angles around a point sum to:",
            "prompt_zh": "一点周围的角的和是：",
            "choices": ["360°", "180°", "270°", "90°"],
            "choices_zh": ["360°", "180°", "270°", "90°"],
            "answer": 0,
            "explanation": "Angles around a point always sum to 360°",
            "explanation_zh": "一点周围的角的和总是360°"
        },
        {
            "id": "geo-ex13",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "Corresponding angles formed by parallel lines are:",
            "prompt_zh": "平行线形成的同位角是：",
            "choices": ["Equal", "Supplementary", "Complementary", "Different"],
            "choices_zh": ["相等", "互补", "互余", "不同"],
            "answer": 0,
            "explanation": "Corresponding angles with parallel lines are equal",
            "explanation_zh": "平行线的同位角相等"
        },
        {
            "id": "geo-ex14",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "An angle greater than 180° but less than 360° is called:",
            "prompt_zh": "大于180°但小于360°的角称为：",
            "choices": ["Reflex angle", "Obtuse angle", "Acute angle", "Right angle"],
            "choices_zh": ["优角", "钝角", "锐角", "直角"],
            "answer": 0,
            "explanation": "Reflex angles are between 180° and 360°",
            "explanation_zh": "优角在180°到360°之间"
        },
        {
            "id": "geo-ex15",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "Interior angles on the same side of a transversal with parallel lines are:",
            "prompt_zh": "平行线被截线所截，同侧内角是：",
            "choices": ["Supplementary", "Equal", "Complementary", "Vertically opposite"],
            "choices_zh": ["互补", "相等", "互余", "对顶"],
            "answer": 0,
            "explanation": "Co-interior angles with parallel lines sum to 180° (supplementary)",
            "explanation_zh": "平行线的同侧内角和为180°（互补）"
        }
    ]
}

# Apply exercises to chapters
for subject in data['subjects']:
    if subject['id'] == 'math':
        for chapter in subject['chapters']:
            if chapter['id'] in exercises_by_chapter:
                new_exercises = exercises_by_chapter[chapter['id']]
                chapter['exercises'].extend(new_exercises)
                print(f"Added {len(new_exercises)} exercises to {chapter['title']}")
                print(f"Total exercises now: {len(chapter['exercises'])}")

# Save updated content
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\n✓ Math exercises batch 3 updated successfully!")
