import json

# Load current content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Define exercises for remaining chapters
exercises_by_chapter = {
    'percentage': [
        {
            "id": "pct-ex6",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "Find 25% of 80:",
            "prompt_zh": "求80的25%：",
            "choices": ["20", "25", "15", "30"],
            "choices_zh": ["20", "25", "15", "30"],
            "answer": 0,
            "explanation": "25% of 80 = 0.25 × 80 = 20",
            "explanation_zh": "80的25% = 0.25 × 80 = 20"
        },
        {
            "id": "pct-ex7",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "A shirt costs $40. After a 20% discount, what is the sale price?",
            "prompt_zh": "一件衬衫原价$40。打8折后，售价是多少？",
            "choices": ["$32", "$30", "$35", "$38"],
            "choices_zh": ["$32", "$30", "$35", "$38"],
            "answer": 0,
            "explanation": "Discount = 20% of $40 = $8. Sale price = $40 - $8 = $32",
            "explanation_zh": "折扣 = $40的20% = $8。售价 = $40 - $8 = $32"
        },
        {
            "id": "pct-ex8",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "A phone costs $600 before 9% GST. What is the total price with GST?",
            "prompt_zh": "一部手机加GST前价格是$600。加上9%的GST后总价是多少？",
            "choices": ["$654", "$600", "$640", "$690"],
            "choices_zh": ["$654", "$600", "$640", "$690"],
            "answer": 0,
            "explanation": "GST = 9% of $600 = $54. Total = $600 + $54 = $654",
            "explanation_zh": "GST = $600的9% = $54。总价 = $600 + $54 = $654"
        },
        {
            "id": "pct-ex9",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "Express 3/5 as a percentage:",
            "prompt_zh": "将3/5表示为百分比：",
            "choices": ["60%", "50%", "65%", "75%"],
            "choices_zh": ["60%", "50%", "65%", "75%"],
            "answer": 0,
            "explanation": "3/5 = 0.6 = 60%",
            "explanation_zh": "3/5 = 0.6 = 60%"
        },
        {
            "id": "pct-ex10",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "A population increases from 500 to 650. What is the percentage increase?",
            "prompt_zh": "人口从500增加到650。增长率是多少？",
            "choices": ["30%", "25%", "20%", "35%"],
            "choices_zh": ["30%", "25%", "20%", "35%"],
            "answer": 0,
            "explanation": "Increase = 150. Percentage = (150/500) × 100% = 30%",
            "explanation_zh": "增长 = 150。百分比 = (150/500) × 100% = 30%"
        },
        {
            "id": "pct-ex11",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "What is 10% of 250?",
            "prompt_zh": "250的10%是多少？",
            "choices": ["25", "20", "30", "15"],
            "choices_zh": ["25", "20", "30", "15"],
            "answer": 0,
            "explanation": "10% of 250 = 0.1 × 250 = 25",
            "explanation_zh": "250的10% = 0.1 × 250 = 25"
        },
        {
            "id": "pct-ex12",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "A shopkeeper marks up an item by 40% on its cost of $50. What is the marked price?",
            "prompt_zh": "店主将成本为$50的商品加价40%。标价是多少？",
            "choices": ["$70", "$65", "$75", "$60"],
            "choices_zh": ["$70", "$65", "$75", "$60"],
            "answer": 0,
            "explanation": "Mark up = 40% of $50 = $20. Marked price = $50 + $20 = $70",
            "explanation_zh": "加价 = $50的40% = $20。标价 = $50 + $20 = $70"
        },
        {
            "id": "pct-ex13",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "A car depreciates by 15% each year. If it costs $40,000, what is its value after 1 year?",
            "prompt_zh": "一辆汽车每年贬值15%。如果它的价格是$40,000，1年后的价值是多少？",
            "choices": ["$34,000", "$36,000", "$38,000", "$32,000"],
            "choices_zh": ["$34,000", "$36,000", "$38,000", "$32,000"],
            "answer": 0,
            "explanation": "Depreciation = 15% of $40,000 = $6,000. Value = $40,000 - $6,000 = $34,000",
            "explanation_zh": "贬值 = $40,000的15% = $6,000。价值 = $40,000 - $6,000 = $34,000"
        },
        {
            "id": "pct-ex14",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "Express 0.85 as a percentage:",
            "prompt_zh": "将0.85表示为百分比：",
            "choices": ["85%", "8.5%", "0.85%", "850%"],
            "choices_zh": ["85%", "8.5%", "0.85%", "850%"],
            "answer": 0,
            "explanation": "0.85 = 85/100 = 85%",
            "explanation_zh": "0.85 = 85/100 = 85%"
        },
        {
            "id": "pct-ex15",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "A school has 60% boys. If there are 240 boys, how many students in total?",
            "prompt_zh": "一所学校有60%的男生。如果有240个男生，总共有多少学生？",
            "choices": ["400", "360", "480", "320"],
            "choices_zh": ["400", "360", "480", "320"],
            "answer": 0,
            "explanation": "60% = 240, so 100% = 240 ÷ 0.6 = 400 students",
            "explanation_zh": "60% = 240，所以100% = 240 ÷ 0.6 = 400名学生"
        }
    ],
    'patterns-sequences': [
        {
            "id": "pat-ex2",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "Find the next term: 2, 5, 8, 11, ___",
            "prompt_zh": "找出下一项：2, 5, 8, 11, ___",
            "choices": ["14", "15", "13", "16"],
            "choices_zh": ["14", "15", "13", "16"],
            "answer": 0,
            "explanation": "Pattern: +3 each time. 11 + 3 = 14",
            "explanation_zh": "规律：每次+3。11 + 3 = 14"
        },
        {
            "id": "pat-ex3",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "What is the 10th term of the sequence: 3, 7, 11, 15, ...?",
            "prompt_zh": "序列3, 7, 11, 15, ...的第10项是什么？",
            "choices": ["39", "35", "43", "41"],
            "choices_zh": ["39", "35", "43", "41"],
            "answer": 0,
            "explanation": "Pattern: first term = 3, common difference = 4. T₁₀ = 3 + (10-1)×4 = 39",
            "explanation_zh": "规律：首项 = 3，公差 = 4。T₁₀ = 3 + (10-1)×4 = 39"
        },
        {
            "id": "pat-ex4",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "Find the missing term: 1, 4, 9, 16, ___, 36",
            "prompt_zh": "找出缺失项：1, 4, 9, 16, ___, 36",
            "choices": ["25", "20", "24", "30"],
            "choices_zh": ["25", "20", "24", "30"],
            "answer": 0,
            "explanation": "Pattern: 1², 2², 3², 4², 5², 6² = 1, 4, 9, 16, 25, 36",
            "explanation_zh": "规律：1², 2², 3², 4², 5², 6² = 1, 4, 9, 16, 25, 36"
        },
        {
            "id": "pat-ex5",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "Find the nth term formula for: 5, 8, 11, 14, ...",
            "prompt_zh": "找出序列5, 8, 11, 14, ...的第n项公式",
            "choices": ["3n + 2", "3n + 5", "4n + 1", "2n + 3"],
            "choices_zh": ["3n + 2", "3n + 5", "4n + 1", "2n + 3"],
            "answer": 0,
            "explanation": "First term = 5, common difference = 3. Formula: 3n + 2",
            "explanation_zh": "首项 = 5，公差 = 3。公式：3n + 2"
        },
        {
            "id": "pat-ex6",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "Find the sum of first 5 terms: 2, 4, 6, 8, 10",
            "prompt_zh": "求前5项的和：2, 4, 6, 8, 10",
            "choices": ["30", "25", "35", "20"],
            "choices_zh": ["30", "25", "35", "20"],
            "answer": 0,
            "explanation": "Sum = 2 + 4 + 6 + 8 + 10 = 30",
            "explanation_zh": "和 = 2 + 4 + 6 + 8 + 10 = 30"
        },
        {
            "id": "pat-ex7",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "Find the pattern: 1, 3, 9, 27, ___",
            "prompt_zh": "找出规律：1, 3, 9, 27, ___",
            "choices": ["81", "54", "72", "90"],
            "choices_zh": ["81", "54", "72", "90"],
            "answer": 0,
            "explanation": "Pattern: ×3 each time. 27 × 3 = 81",
            "explanation_zh": "规律：每次×3。27 × 3 = 81"
        },
        {
            "id": "pat-ex8",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "Which term equals 50 in the sequence: 2, 5, 8, 11, ...?",
            "prompt_zh": "序列2, 5, 8, 11, ...中哪一项等于50？",
            "choices": ["17th", "16th", "18th", "15th"],
            "choices_zh": ["第17项", "第16项", "第18项", "第15项"],
            "answer": 0,
            "explanation": "Formula: 3n - 1 = 50, so 3n = 51, n = 17",
            "explanation_zh": "公式：3n - 1 = 50，所以3n = 51，n = 17"
        },
        {
            "id": "pat-ex9",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "Find the 20th term: 1, -2, 3, -4, 5, -6, ...",
            "prompt_zh": "找出第20项：1, -2, 3, -4, 5, -6, ...",
            "choices": ["-20", "20", "-19", "19"],
            "choices_zh": ["-20", "20", "-19", "19"],
            "answer": 0,
            "explanation": "Pattern: alternating signs, absolute value = n. T₂₀ = -20 (even position is negative)",
            "explanation_zh": "规律：交替符号，绝对值 = n。T₂₀ = -20（偶数位置是负数）"
        },
        {
            "id": "pat-ex10",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "Find the next term: 1, 1, 2, 3, 5, 8, ___",
            "prompt_zh": "找出下一项：1, 1, 2, 3, 5, 8, ___",
            "choices": ["13", "12", "11", "15"],
            "choices_zh": ["13", "12", "11", "15"],
            "answer": 0,
            "explanation": "Fibonacci sequence: each term = sum of previous two. 5 + 8 = 13",
            "explanation_zh": "斐波那契数列：每项 = 前两项之和。5 + 8 = 13"
        },
        {
            "id": "pat-ex11",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "Find the pattern: 100, 90, 80, 70, ___",
            "prompt_zh": "找出规律：100, 90, 80, 70, ___",
            "choices": ["60", "65", "50", "55"],
            "choices_zh": ["60", "65", "50", "55"],
            "answer": 0,
            "explanation": "Pattern: -10 each time. 70 - 10 = 60",
            "explanation_zh": "规律：每次-10。70 - 10 = 60"
        },
        {
            "id": "pat-ex12",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "A sequence has T_n = 2n² + 1. Find T₅:",
            "prompt_zh": "一个序列的第n项为T_n = 2n² + 1。求T₅：",
            "choices": ["51", "49", "53", "50"],
            "choices_zh": ["51", "49", "53", "50"],
            "answer": 0,
            "explanation": "T₅ = 2(5)² + 1 = 2(25) + 1 = 51",
            "explanation_zh": "T₅ = 2(5)² + 1 = 2(25) + 1 = 51"
        },
        {
            "id": "pat-ex13",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "Find the common difference: 15, 12, 9, 6, ...",
            "prompt_zh": "找出公差：15, 12, 9, 6, ...",
            "choices": ["-3", "3", "-4", "4"],
            "choices_zh": ["-3", "3", "-4", "4"],
            "answer": 0,
            "explanation": "Common difference = 12 - 15 = -3",
            "explanation_zh": "公差 = 12 - 15 = -3"
        },
        {
            "id": "pat-ex14",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "Which number comes next: 2, 4, 8, 16, ___?",
            "prompt_zh": "下一个数字是什么：2, 4, 8, 16, ___？",
            "choices": ["32", "24", "20", "30"],
            "choices_zh": ["32", "24", "20", "30"],
            "answer": 0,
            "explanation": "Pattern: ×2 each time. 16 × 2 = 32",
            "explanation_zh": "规律：每次×2。16 × 2 = 32"
        },
        {
            "id": "pat-ex15",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "How many terms are there in the sequence: 5, 8, 11, ..., 50?",
            "prompt_zh": "序列5, 8, 11, ..., 50中有多少项？",
            "choices": ["16", "15", "17", "14"],
            "choices_zh": ["16", "15", "17", "14"],
            "answer": 0,
            "explanation": "Formula: 3n + 2 = 50, 3n = 48, n = 16 terms",
            "explanation_zh": "公式：3n + 2 = 50，3n = 48，n = 16项"
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

print("\n✓ Math exercises batch 2 updated successfully!")
