import json

# Load current content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Define all new exercises for each chapter
exercises_by_chapter = {
    'factors-multiples-primes': [
        {
            "id": "fmp-ex13",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "How many prime numbers are there between 20 and 40?",
            "prompt_zh": "20到40之间有多少个质数？",
            "choices": ["3", "4", "5", "6"],
            "choices_zh": ["3", "4", "5", "6"],
            "answer": 1,
            "explanation": "Prime numbers between 20 and 40 are: 23, 29, 31, 37 (4 primes)",
            "explanation_zh": "20到40之间的质数是：23、29、31、37（4个质数）"
        },
        {
            "id": "fmp-ex14",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "What is the LCM of 12, 18, and 24?",
            "prompt_zh": "12、18和24的最小公倍数是多少？",
            "choices": ["72", "144", "216", "432"],
            "choices_zh": ["72", "144", "216", "432"],
            "answer": 0,
            "explanation": "Prime factorization: 12=2²×3, 18=2×3², 24=2³×3. LCM = 2³×3² = 72",
            "explanation_zh": "质因数分解：12=2²×3，18=2×3²，24=2³×3。最小公倍数 = 2³×3² = 72"
        },
        {
            "id": "fmp-ex15",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "What is the HCF of 48, 72, and 96?",
            "prompt_zh": "48、72和96的最大公约数是多少？",
            "choices": ["12", "24", "48", "96"],
            "choices_zh": ["12", "24", "48", "96"],
            "answer": 1,
            "explanation": "Prime factorization: 48=2⁴×3, 72=2³×3², 96=2⁵×3. HCF = 2³×3 = 24",
            "explanation_zh": "质因数分解：48=2⁴×3，72=2³×3²，96=2⁵×3。最大公约数 = 2³×3 = 24"
        }
    ],
    'approximations-estimations': [
        {
            "id": "approx-ex11",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "Round 4.567 to 1 decimal place:",
            "prompt_zh": "将4.567四舍五入到1位小数：",
            "choices": ["4.5", "4.6", "5.0", "4.57"],
            "choices_zh": ["4.5", "4.6", "5.0", "4.57"],
            "answer": 1,
            "explanation": "Look at 2nd decimal place: 6 ≥ 5, so round up. 4.567 ≈ 4.6",
            "explanation_zh": "看第2位小数：6 ≥ 5，所以向上舍入。4.567 ≈ 4.6"
        },
        {
            "id": "approx-ex12",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "Estimate 398 × 21 by rounding to nearest 10:",
            "prompt_zh": "通过四舍五入到最接近的10来估算398 × 21：",
            "choices": ["8000", "8400", "7800", "6000"],
            "choices_zh": ["8000", "8400", "7800", "6000"],
            "answer": 0,
            "explanation": "400 × 20 = 8000",
            "explanation_zh": "400 × 20 = 8000"
        },
        {
            "id": "approx-ex13",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "Express 0.0456 in standard form:",
            "prompt_zh": "将0.0456表示为标准形式：",
            "choices": ["4.56 × 10⁻²", "4.56 × 10⁻³", "45.6 × 10⁻³", "456 × 10⁻⁴"],
            "choices_zh": ["4.56 × 10⁻²", "4.56 × 10⁻³", "45.6 × 10⁻³", "456 × 10⁻⁴"],
            "answer": 0,
            "explanation": "Move decimal point 2 places right: 0.0456 = 4.56 × 10⁻²",
            "explanation_zh": "将小数点向右移动2位：0.0456 = 4.56 × 10⁻²"
        },
        {
            "id": "approx-ex14",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "Calculate (3.2 × 10⁴) × (2.5 × 10⁻²):",
            "prompt_zh": "计算(3.2 × 10⁴) × (2.5 × 10⁻²)：",
            "choices": ["8 × 10²", "8 × 10⁶", "8 × 10³", "80"],
            "choices_zh": ["8 × 10²", "8 × 10⁶", "8 × 10³", "80"],
            "answer": 0,
            "explanation": "(3.2 × 2.5) × (10⁴ × 10⁻²) = 8 × 10² = 800",
            "explanation_zh": "(3.2 × 2.5) × (10⁴ × 10⁻²) = 8 × 10² = 800"
        },
        {
            "id": "approx-ex15",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "Round 2,847 to the nearest hundred:",
            "prompt_zh": "将2,847四舍五入到最接近的百：",
            "choices": ["2,800", "2,900", "3,000", "2,850"],
            "choices_zh": ["2,800", "2,900", "3,000", "2,850"],
            "answer": 0,
            "explanation": "47 < 50, so round down to 2,800",
            "explanation_zh": "47 < 50，所以向下舍入到2,800"
        }
    ],
    'algebraic-expressions': [
        {
            "id": "alg-ex13",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "Expand 3(2x - 5):",
            "prompt_zh": "展开3(2x - 5)：",
            "choices": ["6x - 15", "6x - 5", "6x + 15", "5x - 15"],
            "choices_zh": ["6x - 15", "6x - 5", "6x + 15", "5x - 15"],
            "answer": 0,
            "explanation": "3 × 2x = 6x, 3 × (-5) = -15, so 3(2x - 5) = 6x - 15",
            "explanation_zh": "3 × 2x = 6x，3 × (-5) = -15，所以3(2x - 5) = 6x - 15"
        },
        {
            "id": "alg-ex14",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "Factorize 6x + 9:",
            "prompt_zh": "因式分解6x + 9：",
            "choices": ["3(2x + 3)", "6(x + 9)", "3(2x + 9)", "9(x + 1)"],
            "choices_zh": ["3(2x + 3)", "6(x + 9)", "3(2x + 9)", "9(x + 1)"],
            "answer": 0,
            "explanation": "HCF of 6 and 9 is 3: 6x + 9 = 3(2x + 3)",
            "explanation_zh": "6和9的最大公约数是3：6x + 9 = 3(2x + 3)"
        },
        {
            "id": "alg-ex15",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "Simplify: 5x² - 2x + 3x² + 7x",
            "prompt_zh": "化简：5x² - 2x + 3x² + 7x",
            "choices": ["8x² + 5x", "8x² - 5x", "2x² + 5x", "8x + 5x²"],
            "choices_zh": ["8x² + 5x", "8x² - 5x", "2x² + 5x", "8x + 5x²"],
            "answer": 0,
            "explanation": "Combine like terms: (5x² + 3x²) + (-2x + 7x) = 8x² + 5x",
            "explanation_zh": "合并同类项：(5x² + 3x²) + (-2x + 7x) = 8x² + 5x"
        }
    ]
}

# Continue with more chapters...
exercises_by_chapter.update({
    'ratio-rate-proportion': [
        {
            "id": "rrp-ex2",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "Simplify the ratio 12:18",
            "prompt_zh": "化简比率12:18",
            "choices": ["2:3", "3:2", "4:6", "6:9"],
            "choices_zh": ["2:3", "3:2", "4:6", "6:9"],
            "answer": 0,
            "explanation": "Divide both by HCF(6): 12÷6 : 18÷6 = 2:3",
            "explanation_zh": "都除以最大公约数(6)：12÷6 : 18÷6 = 2:3"
        },
        {
            "id": "rrp-ex3",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "The ratio of boys to girls is 3:5. If there are 24 boys, how many girls are there?",
            "prompt_zh": "男生和女生的比率是3:5。如果有24个男生，有多少个女生？",
            "choices": ["40", "32", "15", "45"],
            "choices_zh": ["40", "32", "15", "45"],
            "answer": 0,
            "explanation": "3 parts = 24, so 1 part = 8. Girls = 5 parts = 5 × 8 = 40",
            "explanation_zh": "3份 = 24，所以1份 = 8。女生 = 5份 = 5 × 8 = 40"
        },
        {
            "id": "rrp-ex4",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "A car travels 180 km in 2 hours. What is its average speed?",
            "prompt_zh": "一辆汽车在2小时内行驶180公里。它的平均速度是多少？",
            "choices": ["90 km/h", "180 km/h", "45 km/h", "360 km/h"],
            "choices_zh": ["90公里/小时", "180公里/小时", "45公里/小时", "360公里/小时"],
            "answer": 0,
            "explanation": "Speed = Distance ÷ Time = 180 ÷ 2 = 90 km/h",
            "explanation_zh": "速度 = 距离 ÷ 时间 = 180 ÷ 2 = 90公里/小时"
        },
        {
            "id": "rrp-ex5",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "3 pens cost $4.50. How much do 7 pens cost?",
            "prompt_zh": "3支笔花费$4.50。7支笔花费多少？",
            "choices": ["$10.50", "$12.00", "$9.00", "$13.50"],
            "choices_zh": ["$10.50", "$12.00", "$9.00", "$13.50"],
            "answer": 0,
            "explanation": "1 pen = $4.50 ÷ 3 = $1.50. 7 pens = 7 × $1.50 = $10.50",
            "explanation_zh": "1支笔 = $4.50 ÷ 3 = $1.50。7支笔 = 7 × $1.50 = $10.50"
        },
        {
            "id": "rrp-ex6",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "Divide $120 in the ratio 2:3:5",
            "prompt_zh": "按2:3:5的比率分配$120",
            "choices": ["$24, $36, $60", "$20, $30, $50", "$30, $45, $45", "$40, $40, $40"],
            "choices_zh": ["$24, $36, $60", "$20, $30, $50", "$30, $45, $45", "$40, $40, $40"],
            "answer": 0,
            "explanation": "Total parts = 2+3+5 = 10. 1 part = $12. Shares: $24, $36, $60",
            "explanation_zh": "总份数 = 2+3+5 = 10。1份 = $12。份额：$24、$36、$60"
        },
        {
            "id": "rrp-ex7",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "An MRT train travels from Orchard to Marina Bay (6 km) in 10 minutes. What is the speed in km/h?",
            "prompt_zh": "地铁从乌节路到滨海湾（6公里）需要10分钟。速度是多少公里/小时？",
            "choices": ["36 km/h", "60 km/h", "6 km/h", "30 km/h"],
            "choices_zh": ["36公里/小时", "60公里/小时", "6公里/小时", "30公里/小时"],
            "answer": 0,
            "explanation": "10 min = 1/6 hour. Speed = 6 ÷ (1/6) = 36 km/h",
            "explanation_zh": "10分钟 = 1/6小时。速度 = 6 ÷ (1/6) = 36公里/小时"
        },
        {
            "id": "rrp-ex8",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "If 5:x = 2:6, find x:",
            "prompt_zh": "如果5:x = 2:6，求x：",
            "choices": ["15", "10", "12", "20"],
            "choices_zh": ["15", "10", "12", "20"],
            "answer": 0,
            "explanation": "Cross multiply: 5 × 6 = 2 × x, 30 = 2x, x = 15",
            "explanation_zh": "交叉相乘：5 × 6 = 2 × x，30 = 2x，x = 15"
        },
        {
            "id": "rrp-ex9",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "A recipe for 4 people needs 300g of flour. How much for 10 people?",
            "prompt_zh": "4人份的食谱需要300克面粉。10人份需要多少？",
            "choices": ["750g", "600g", "800g", "900g"],
            "choices_zh": ["750克", "600克", "800克", "900克"],
            "answer": 0,
            "explanation": "1 person needs 300÷4 = 75g. 10 people need 75×10 = 750g",
            "explanation_zh": "1人需要300÷4 = 75克。10人需要75×10 = 750克"
        },
        {
            "id": "rrp-ex10",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "The ratio of length to width of a rectangle is 5:3. If the length is 20 cm, find the width:",
            "prompt_zh": "矩形的长宽比是5:3。如果长是20厘米，求宽：",
            "choices": ["12 cm", "15 cm", "10 cm", "18 cm"],
            "choices_zh": ["12厘米", "15厘米", "10厘米", "18厘米"],
            "answer": 0,
            "explanation": "5 parts = 20, 1 part = 4. Width = 3 parts = 12 cm",
            "explanation_zh": "5份 = 20，1份 = 4。宽 = 3份 = 12厘米"
        },
        {
            "id": "rrp-ex11",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "A tap fills a tank in 6 hours. What fraction of the tank is filled in 1 hour?",
            "prompt_zh": "一个水龙头在6小时内装满水箱。1小时内装满水箱的几分之几？",
            "choices": ["1/6", "1/5", "1/7", "6"],
            "choices_zh": ["1/6", "1/5", "1/7", "6"],
            "answer": 0,
            "explanation": "Rate = 1 tank ÷ 6 hours = 1/6 tank per hour",
            "explanation_zh": "速率 = 1个水箱 ÷ 6小时 = 每小时1/6个水箱"
        },
        {
            "id": "rrp-ex12",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "Express the ratio 2.5:3.5 in simplest form:",
            "prompt_zh": "将比率2.5:3.5表示为最简形式：",
            "choices": ["5:7", "25:35", "1:2", "2:3"],
            "choices_zh": ["5:7", "25:35", "1:2", "2:3"],
            "answer": 0,
            "explanation": "Multiply by 2: 5:7 (or divide by 0.5)",
            "explanation_zh": "乘以2：5:7（或除以0.5）"
        },
        {
            "id": "rrp-ex13",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "3 oranges cost $1.20. What is the unit price?",
            "prompt_zh": "3个橙子花费$1.20。单价是多少？",
            "choices": ["$0.40", "$0.30", "$0.50", "$0.60"],
            "choices_zh": ["$0.40", "$0.30", "$0.50", "$0.60"],
            "answer": 0,
            "explanation": "Unit price = $1.20 ÷ 3 = $0.40 per orange",
            "explanation_zh": "单价 = $1.20 ÷ 3 = 每个橙子$0.40"
        },
        {
            "id": "rrp-ex14",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "Two numbers are in the ratio 4:9. If their sum is 65, find the larger number:",
            "prompt_zh": "两个数的比率是4:9。如果它们的和是65，求较大的数：",
            "choices": ["45", "36", "20", "40"],
            "choices_zh": ["45", "36", "20", "40"],
            "answer": 0,
            "explanation": "Total parts = 13. 1 part = 65÷13 = 5. Larger = 9×5 = 45",
            "explanation_zh": "总份数 = 13。1份 = 65÷13 = 5。较大的数 = 9×5 = 45"
        },
        {
            "id": "rrp-ex15",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "A cyclist travels 45 km in 3 hours. At the same speed, how far in 5 hours?",
            "prompt_zh": "一个骑自行车的人在3小时内行驶45公里。以同样的速度，5小时内能行驶多远？",
            "choices": ["75 km", "60 km", "90 km", "50 km"],
            "choices_zh": ["75公里", "60公里", "90公里", "50公里"],
            "answer": 0,
            "explanation": "Speed = 45÷3 = 15 km/h. Distance = 15×5 = 75 km",
            "explanation_zh": "速度 = 45÷3 = 15公里/小时。距离 = 15×5 = 75公里"
        }
    ]
})

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

print("\n✓ Math exercises batch 1 updated successfully!")
