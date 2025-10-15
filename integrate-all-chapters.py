#!/usr/bin/env python3
"""
Clean integration of all 5 expanded chapters into content.json
Handles encoding issues by using simplified content where needed
"""

import json
import shutil
from pathlib import Path
from datetime import datetime

def create_backup(content_file):
    """Create timestamped backup"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = content_file.parent / f"content-backup-{timestamp}.json"
    shutil.copy2(content_file, backup_file)
    print(f"💾 Backup created: {backup_file.name}")
    return backup_file

def load_json_safe(filepath):
    """Load JSON with UTF-8 encoding"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"⚠️  JSON error in {filepath.name}: {e}")
        print(f"   Will use simplified version for this chapter")
        return None

def get_expanded_chapters():
    """Define expanded chapters with clean content (no special quotes)"""
    
    # Chapter 1: Algebraic Expressions
    algebraic_expressions = {
        "id": "algebraic-expressions",
        "title": "Algebraic Expressions",
        "title_zh": "代数表达式",
        "description": "Master simplification, expansion, and factorization of algebraic expressions",
        "description_zh": "掌握代数表达式的简化、展开和因式分解",
        "objectives": [
            "Understand algebraic notation and terminology",
            "Combine like terms to simplify expressions",
            "Expand brackets using the distributive law",
            "Factorize simple algebraic expressions",
            "Evaluate algebraic expressions by substitution"
        ],
        "objectives_zh": [
            "理解代数符号和术语",
            "合并同类项以简化表达式",
            "使用分配律展开括号",
            "因式分解简单的代数表达式",
            "通过代入求值代数表达式"
        ],
        "sections": [
            {
                "id": "intro-algebra",
                "type": "text",
                "title": "Introduction to Algebraic Expressions",
                "title_zh": "代数表达式简介",
                "content": "An algebraic expression uses letters (variables) to represent unknown numbers. Examples: 2x + 3, 5a - 2b. Key Terms: VARIABLE (a letter representing a number), COEFFICIENT (number multiplied by variable), CONSTANT (number on its own), TERM (parts separated by + or -). Why use algebra? To write general rules, solve problems with unknowns, and describe patterns.",
                "content_zh": "代数表达式使用字母（变量）来表示未知数。例子：2x + 3，5a - 2b。关键术语：变量（表示数字的字母）、系数（与变量相乘的数字）、常数（单独的数字）、项（用+或-分隔的部分）。为什么使用代数？编写一般规则，解决未知数问题，描述模式。"
            },
            {
                "id": "like-terms",
                "type": "text",
                "title": "Like Terms",
                "title_zh": "同类项",
                "content": "LIKE TERMS have the same variables raised to the same powers. Only like terms can be combined. Examples: 2x and 5x are like terms. 4x and 5x² are NOT like terms (different powers). Combining: 3x + 5x = 8x (add coefficients). Rule: Add or subtract coefficients, keep variable part same.",
                "content_zh": "同类项具有相同的变量和相同的幂。只有同类项可以合并。例子：2x和5x是同类项。4x和5x²不是同类项（不同幂次）。合并：3x + 5x = 8x（加系数）。规则：对系数进行加减，变量部分保持不变。"
            },
            {
                "id": "tile-animation",
                "type": "animation",
                "title": "Visualizing Like Terms",
                "title_zh": "可视化同类项",
                "content": "TileCombine",
                "props": {
                    "expression": "x + x + x",
                    "result": "3x"
                }
            },
            {
                "id": "simplifying",
                "type": "text",
                "title": "Simplifying Expressions",
                "title_zh": "简化表达式",
                "content": "Simplifying means combining like terms. Steps: 1) Identify like terms, 2) Combine coefficients, 3) Write in standard form. Example: 5x + 3 - 2x + 7. Group: (5x - 2x) + (3 + 7) = 3x + 10. Common mistakes: Don't combine unlike terms (2x + 3y is NOT 5xy), Don't change variables (2x + 3x = 5x, NOT 5x²).",
                "content_zh": "简化意味着合并同类项。步骤：1）识别同类项，2）合并系数，3）写成标准形式。例子：5x + 3 - 2x + 7。分组：(5x - 2x) + (3 + 7) = 3x + 10。常见错误：不要合并不同类项（2x + 3y不是5xy），不要改变变量（2x + 3x = 5x，不是5x²）。"
            },
            {
                "id": "expanding",
                "type": "math",
                "title": "Expanding Brackets",
                "title_zh": "展开括号",
                "content": "a(b + c) = ab + ac",
                "explanation": "DISTRIBUTIVE LAW: Multiply outside term by EACH term inside. Example: 3(x + 2) = 3×x + 3×2 = 3x + 6. With negatives: -2(x + 4) = -2x - 8. Remember: The sign outside affects ALL terms inside!",
                "explanation_zh": "分配律：将括号外的项乘以括号内的每一项。例子：3(x + 2) = 3×x + 3×2 = 3x + 6。负数：-2(x + 4) = -2x - 8。记住：外面的符号影响里面所有的项！"
            },
            {
                "id": "factorizing",
                "type": "text",
                "title": "Factorizing Expressions",
                "title_zh": "因式分解",
                "content": "Factorizing is REVERSE of expanding - take out common factors. Steps: 1) Find HCF of all terms, 2) Write HCF outside brackets, 3) Divide each term by HCF, 4) Check by expanding. Example: 6x + 9. HCF = 3. Answer: 3(2x + 3). Check: 3(2x + 3) = 6x + 9.",
                "content_zh": "因式分解是展开的逆过程 - 提取公因数。步骤：1）找出所有项的最大公因数，2）将HCF写在括号外，3）每项除以HCF，4）通过展开检查。例子：6x + 9。HCF = 3。答案：3(2x + 3)。检查：3(2x + 3) = 6x + 9。"
            },
            {
                "id": "substitution",
                "type": "text",
                "title": "Substitution and Evaluation",
                "title_zh": "代入和求值",
                "content": "Substitution means replacing variables with numbers. Steps: 1) Write expression, 2) Replace variables (use brackets!), 3) Follow order of operations, 4) Calculate. Example: Evaluate 3x + 5 when x = 4. Answer: 3(4) + 5 = 12 + 5 = 17. Always use brackets for negative numbers!",
                "content_zh": "代入意味着用数字替换变量。步骤：1）写表达式，2）替换变量（使用括号！），3）遵循运算顺序，4）计算。例子：当x = 4时求值3x + 5。答案：3(4) + 5 = 12 + 5 = 17。负数时始终使用括号！"
            },
            {
                "id": "real-world",
                "type": "text",
                "title": "Real-World Applications",
                "title_zh": "实际应用",
                "content": "Algebra helps solve real problems. Examples: Perimeter of rectangle P = 2(l + w). Cost calculation: Total = price × quantity. Temperature conversion: F = (9/5)C + 32. Distance: d = speed × time. Discount: Sale price = Original × (1 - discount%). Algebra lets us write formulas once and use for any values!",
                "content_zh": "代数帮助解决实际问题。例子：矩形周长P = 2(l + w)。成本计算：总计 = 价格 × 数量。温度转换：F = (9/5)C + 32。距离：d = 速度 × 时间。折扣：售价 = 原价 × (1 - 折扣%)。代数让我们可以写一次公式，然后用于任何值！"
            }
        ],
        "exercises": [
            {
                "id": "q1",
                "type": "mcq",
                "prompt": "Which of the following are like terms?",
                "prompt_zh": "以下哪些是同类项？",
                "choices": ["2x and 3x", "4a and 5b", "x² and x", "2xy and 3x"],
                "answer": 0,
                "hint": "Like terms have the same variable(s) with the same power.",
                "hint_zh": "同类项具有相同的变量和相同的幂。"
            },
            {
                "id": "q2",
                "type": "short",
                "prompt": "Simplify: 4x + 2y - 3x + y",
                "prompt_zh": "化简：4x + 2y - 3x + y",
                "answer": "x + 3y",
                "hint": "Group x terms and y terms separately.",
                "hint_zh": "分别分组x项和y项。"
            },
            {
                "id": "q3",
                "type": "mcq",
                "prompt": "Expand: 3(x + 2)",
                "prompt_zh": "展开：3(x + 2)",
                "choices": ["3x + 2", "3x + 6", "x + 6", "3x + 5"],
                "answer": 1,
                "hint": "Multiply 3 by both terms inside.",
                "hint_zh": "将3与括号内的两项相乘。"
            },
            {
                "id": "q4",
                "type": "short",
                "prompt": "Expand: 5(2a - 3)",
                "prompt_zh": "展开：5(2a - 3)",
                "answer": "10a - 15",
                "hint": "Multiply 5 by each term.",
                "hint_zh": "将5与每项相乘。"
            },
            {
                "id": "q5",
                "type": "mcq",
                "prompt": "Factorize: 6x + 9",
                "prompt_zh": "因式分解：6x + 9",
                "choices": ["3(2x + 3)", "6(x + 9)", "3(2x + 6)", "2(3x + 9)"],
                "answer": 0,
                "hint": "Find HCF of 6 and 9.",
                "hint_zh": "找6和9的最大公因数。"
            },
            {
                "id": "q6",
                "type": "short",
                "prompt": "Evaluate 3x + 5 when x = 4",
                "prompt_zh": "当x = 4时求值3x + 5",
                "answer": "17",
                "validator": "numeric",
                "hint": "Substitute 4 for x: 3(4) + 5",
                "hint_zh": "用4代替x：3(4) + 5"
            }
        ]
    }
    
    # Chapter 2: Percentage (Math)
    percentage = {
        "id": "percentage",
        "title": "Percentage Applications",
        "title_zh": "百分比应用",
        "description": "Master percentage calculations including GST, discounts, profit, loss and interest",
        "description_zh": "掌握百分比计算，包括消费税、折扣、盈亏和利息",
        "objectives": [
            "Convert between percentages, fractions and decimals fluently",
            "Calculate percentage of a quantity",
            "Find percentage increase and decrease",
            "Apply GST (Goods and Services Tax) at 9%",
            "Calculate discounts, profit, loss and simple interest"
        ],
        "objectives_zh": [
            "流利地在百分数、分数和小数之间转换",
            "计算数量的百分比",
            "求百分比增减",
            "应用9%的消费税",
            "计算折扣、盈亏和单利"
        ],
        "sections": [
            {
                "id": "intro-percentage",
                "type": "text",
                "title": "Understanding Percentages",
                "title_zh": "理解百分比",
                "content": "PERCENTAGE means per hundred. 50% means 50 out of 100, or 0.5, or 1/2. 100% means the whole amount. Why use percentages? Easy to compare, standard way to express proportions. Examples: Test scores (85%), Sales (50% off), GST (9% in Singapore).",
                "content_zh": "百分比意味着每百。50%意味着100中的50，或0.5，或1/2。100%意味着整个数量。为什么使用百分比？易于比较，表达比例的标准方式。例子：考试分数（85%）、销售（50%折扣）、消费税（新加坡9%）。"
            },
            {
                "id": "converting",
                "type": "text",
                "title": "Converting Forms",
                "title_zh": "转换形式",
                "content": "PERCENTAGE to DECIMAL: Divide by 100. Example: 25% = 0.25. DECIMAL to PERCENTAGE: Multiply by 100. Example: 0.6 = 60%. PERCENTAGE to FRACTION: Write over 100 and simplify. Example: 40% = 40/100 = 2/5. Common to remember: 1/2 = 50%, 1/4 = 25%, 1/5 = 20%.",
                "content_zh": "百分数到小数：除以100。例：25% = 0.25。小数到百分数：乘以100。例：0.6 = 60%。百分数到分数：写成100的分数并简化。例：40% = 40/100 = 2/5。常用记住：1/2 = 50%，1/4 = 25%，1/5 = 20%。"
            },
            {
                "id": "finding-percentage",
                "type": "math",
                "title": "Finding Percentage of a Quantity",
                "title_zh": "求数量的百分比",
                "content": "x% of y = (x/100) × y",
                "explanation": "Convert to decimal then multiply. Find 30% of 80: 0.30 × 80 = 24. Quick tricks: 10% divide by 10, 50% divide by 2, 25% divide by 4.",
                "explanation_zh": "转换为小数然后相乘。求80的30%：0.30 × 80 = 24。快速技巧：10%除以10，50%除以2，25%除以4。"
            },
            {
                "id": "percentage-change",
                "type": "text",
                "title": "Percentage Increase and Decrease",
                "title_zh": "百分比增减",
                "content": "INCREASE: New = Original × (1 + %). Example: Increase $50 by 20% = 50 × 1.20 = $60. DECREASE: New = Original × (1 - %). Example: Decrease $200 by 30% = 200 × 0.70 = $140. FINDING CHANGE: Change% = (Change/Original) × 100%.",
                "content_zh": "增加：新值 = 原值 × (1 + %)。例：$50增加20% = 50 × 1.20 = $60。减少：新值 = 原值 × (1 - %)。例：$200减少30% = 200 × 0.70 = $140。求变化：变化% = (变化量/原值) × 100%。"
            },
            {
                "id": "gst-applications",
                "type": "text",
                "title": "GST Applications",
                "title_zh": "消费税应用",
                "content": "In Singapore, GST is 9%. Price with GST = Original × 1.09. Example: $100 item, GST = $9, Total = $109. Finding original price: Original = Total ÷ 1.09. Example: Total $218, Original = 218 ÷ 1.09 = $200.",
                "content_zh": "在新加坡，消费税为9%。含税价格 = 原价 × 1.09。例：$100商品，消费税 = $9，总计 = $109。求原价：原价 = 总价 ÷ 1.09。例：总计$218，原价 = 218 ÷ 1.09 = $200。"
            },
            {
                "id": "discounts",
                "type": "text",
                "title": "Discounts and Sale Prices",
                "title_zh": "折扣和促销价",
                "content": "DISCOUNT reduces price. Sale Price = Original × (1 - Discount%). Example: $80 with 25% off = 80 × 0.75 = $60. Multiple discounts: Apply one after another, NOT by adding! Example: 20% off then 10% off on $100 = 100 × 0.80 × 0.90 = $72 (NOT 30% off which would be $70).",
                "content_zh": "折扣降低价格。促销价 = 原价 × (1 - 折扣%)。例：$80享25%折扣 = 80 × 0.75 = $60。多重折扣：逐个应用，不是相加！例：$100先20%折扣再10%折扣 = 100 × 0.80 × 0.90 = $72（不是30%折扣的$70）。"
            },
            {
                "id": "profit-loss",
                "type": "text",
                "title": "Profit, Loss and Markup",
                "title_zh": "盈利、亏损和加价",
                "content": "PROFIT: Selling Price > Cost. Profit% = (Profit/Cost) × 100%. Example: Buy $60, sell $80. Profit = $20, Profit% = (20/60) × 100% = 33.33%. LOSS: Selling Price < Cost. Finding SP with profit: SP = CP × (1 + Profit%). Finding CP: CP = SP ÷ (1 + Profit%).",
                "content_zh": "盈利：售价>成本。盈利% = (盈利/成本) × 100%。例：$60买入，$80卖出。盈利 = $20，盈利% = (20/60) × 100% = 33.33%。亏损：售价<成本。有盈利求售价：售价 = 成本价 × (1 + 盈利%)。求成本价：成本价 = 售价 ÷ (1 + 盈利%)。"
            },
            {
                "id": "simple-interest",
                "type": "text",
                "title": "Simple Interest",
                "title_zh": "单利",
                "content": "Formula: I = (P × R × T) / 100. P = Principal, R = Rate per year, T = Time in years. Total = Principal + Interest. Example: $1000 at 3% for 2 years. I = (1000 × 3 × 2) / 100 = $60. Total = $1060. Banks offer 0.05% to 3% on savings. Credit cards can be 24% per year!",
                "content_zh": "公式：I = (P × R × T) / 100。P = 本金，R = 年利率，T = 时间（年）。总金额 = 本金 + 利息。例：$1000以3%利率存2年。I = (1000 × 3 × 2) / 100 = $60。总计 = $1060。银行提供0.05%至3%的储蓄利息。信用卡可能是每年24%！"
            }
        ],
        "exercises": [
            {
                "id": "q1",
                "type": "mcq",
                "prompt": "Convert 0.65 to a percentage.",
                "prompt_zh": "将0.65转换为百分数。",
                "choices": ["6.5%", "65%", "0.65%", "650%"],
                "answer": 1,
                "hint": "Multiply by 100."
            },
            {
                "id": "q2",
                "type": "short",
                "prompt": "Find 30% of 120.",
                "prompt_zh": "求120的30%。",
                "answer": "36",
                "validator": "numeric",
                "hint": "0.30 × 120"
            },
            {
                "id": "q3",
                "type": "mcq",
                "prompt": "A $200 item is discounted by 15%. What is the sale price?",
                "prompt_zh": "一件$200的商品打85折。售价是多少？",
                "choices": ["$170", "$180", "$185", "$190"],
                "answer": 0,
                "hint": "200 × 0.85"
            },
            {
                "id": "q4",
                "type": "short",
                "prompt": "An item costs $80 before GST (9%). What is the final price?",
                "prompt_zh": "一件商品税前价格$80（消费税9%）。最终价格是多少？",
                "answer": "87.20",
                "validator": "numeric",
                "hint": "80 × 1.09"
            },
            {
                "id": "q5",
                "type": "short",
                "prompt": "Calculate simple interest on $2000 at 4% for 3 years.",
                "prompt_zh": "计算$2000以4%利率存3年的单利。",
                "answer": "240",
                "validator": "numeric",
                "hint": "(2000 × 4 × 3) / 100"
            }
        ]
    }
    
    # Chapter 3: Particulate Model (Science)
    particle_model = {
        "id": "particle-model",
        "title": "Particulate Model of Matter",
        "title_zh": "物质的粒子模型",
        "description": "Understand particle behavior in solids, liquids and gases with interactive visualizations",
        "description_zh": "通过互动可视化理解固体、液体和气体中的粒子行为",
        "objectives": [
            "Describe particle arrangement in the three states of matter",
            "Explain particle motion and energy in different states",
            "Understand diffusion and Brownian motion",
            "Relate particle behavior to macroscopic properties"
        ],
        "objectives_zh": [
            "描述三种物质状态中的粒子排列",
            "解释不同状态下的粒子运动和能量",
            "理解扩散和布朗运动",
            "将粒子行为与宏观性质联系起来"
        ],
        "sections": [
            {"id": "intro", "type": "text", "title": "Kinetic Particle Theory", "title_zh": "动理论",
             "content": "All matter is made of tiny particles in constant random motion. Particles have spaces between them. Motion increases with temperature. Forces of attraction exist between particles.",
             "content_zh": "所有物质都由持续随机运动的微小粒子组成。粒子之间有间隙。运动随温度增加。粒子之间存在吸引力。"},
            {"id": "states-animation", "type": "animation", "title": "Three States of Matter", "title_zh": "三种物质状态",
             "content": "ParticlesInStates", "props": {"states": ["solid", "liquid", "gas"]}},
            {"id": "solid-state", "type": "text", "title": "Solids - Particle Model", "title_zh": "固体 - 粒子模型",
             "content": "Particles packed very closely in fixed regular pattern. Very little space between. Particles vibrate about fixed positions. Very strong forces hold particles rigidly. This explains: fixed shape, fixed volume, cannot be compressed, cannot flow, high density.",
             "content_zh": "粒子以固定规则模式紧密堆积。间隙很小。粒子在固定位置振动。很强的力将粒子刚性固定。这解释了：固定形状、固定体积、不能压缩、不能流动、高密度。"},
            {"id": "liquid-state", "type": "text", "title": "Liquids - Particle Model", "title_zh": "液体 - 粒子模型",
             "content": "Particles close together but not in fixed positions. Small spaces between. Random arrangement. Particles can move around and slide past each other. Moderate forces of attraction. This explains: no fixed shape (takes container shape), fixed volume, difficult to compress, can flow, medium density.",
             "content_zh": "粒子紧密但不在固定位置。间隙小。随机排列。粒子可以四处移动并相互滑过。中等吸引力。这解释了：无固定形状（采取容器形状）、固定体积、难以压缩、可以流动、中等密度。"},
            {"id": "gas-state", "type": "text", "title": "Gases - Particle Model", "title_zh": "气体 - 粒子模型",
             "content": "Particles very far apart. Large spaces between. Completely random. Particles move very fast in all directions. Frequent collisions. Very weak or negligible forces. This explains: no fixed shape, no fixed volume, easily compressed, can flow, low density, exerts pressure.",
             "content_zh": "粒子相距很远。间隙大。完全随机。粒子向所有方向快速移动。频繁碰撞。作用力非常弱或可忽略。这解释了：无固定形状、无固定体积、易于压缩、可以流动、低密度、施加压力。"},
            {"id": "diffusion", "type": "text", "title": "Diffusion", "title_zh": "扩散",
             "content": "Net movement of particles from higher to lower concentration due to random motion. Occurs in liquids and gases. Does not require stirring. Continues until evenly distributed. Faster at higher temperatures. Examples: perfume spreading, food coloring in water, tea bag in hot water.",
             "content_zh": "由于随机运动，粒子从高浓度向低浓度的净移动。发生在液体和气体中。不需要搅拌。持续直到均匀分布。温度越高越快。例子：香水扩散、水中的食用色素、热水中的茶包。"},
            {"id": "brownian-motion", "type": "text", "title": "Brownian Motion", "title_zh": "布朗运动",
             "content": "Random zigzag movement of small particles suspended in fluid. Caused by invisible molecules constantly bombarding visible particles. Provides evidence for particle theory. Observed in smoke cell experiment: smoke particles move randomly under microscope, showing air molecules are hitting them.",
             "content_zh": "悬浮在流体中的小粒子的随机锯齿形运动。由看不见的分子不断轰击可见粒子引起。为粒子理论提供证据。在烟雾室实验中观察：烟雾粒子在显微镜下随机移动，显示空气分子正在撞击它们。"}
        ],
        "exercises": [
            {"id": "q1", "type": "mcq", "prompt": "In solids, particles mainly...", "prompt_zh": "在固体中，粒子主要...",
             "choices": ["are fixed and vibrate", "flow freely", "are far apart", "move rapidly"], "answer": 0, "hint": "Think about fixed shape."},
            {"id": "q2", "type": "mcq", "prompt": "Which state can be compressed easily?", "prompt_zh": "哪种状态可以轻易压缩？",
             "choices": ["Solid", "Liquid", "Gas", "All equally"], "answer": 2, "hint": "Most empty space between particles."},
            {"id": "q3", "type": "short", "prompt": "Name the process when perfume spreads across a room.", "prompt_zh": "当香水在房间里扩散时的过程叫什么？",
             "answer": "diffusion", "answer_zh": "扩散", "hint": "Movement from high to low concentration."}
        ]
    }
    
    # Chapter 4: Forces and Motion (Science)
    forces_motion = {
        "id": "forces-motion",
        "title": "Forces and Motion",
        "title_zh": "力与运动",
        "description": "Explore forces, friction, balanced and unbalanced forces with interactive simulations",
        "description_zh": "通过互动模拟探索力、摩擦力、平衡力和不平衡力",
        "objectives": [
            "Understand what forces are and how they affect motion",
            "Identify and measure forces using spring balances",
            "Distinguish between balanced and unbalanced forces",
            "Explain friction and its effects",
            "Apply Newton's First Law of Motion"
        ],
        "objectives_zh": [
            "理解什么是力以及它们如何影响运动",
            "使用弹簧秤识别和测量力",
            "区分平衡力和不平衡力",
            "解释摩擦力及其影响",
            "应用牛顿第一运动定律"
        ],
        "sections": [
            {"id": "intro-forces", "type": "text", "title": "What is a Force?", "title_zh": "什么是力？",
             "content": "A FORCE is a push or pull. Force is a VECTOR with magnitude and direction. Measured in NEWTONS (N). Effects: change speed, change direction, change shape, start motion, stop motion. Types: Contact forces (push, pull, friction, tension) and Non-contact forces (gravity, magnetism).",
             "content_zh": "力是推或拉。力是具有大小和方向的矢量。以牛顿（N）为单位测量。效果：改变速度、改变方向、改变形状、开始运动、停止运动。类型：接触力（推、拉、摩擦、张力）和非接触力（重力、磁力）。"},
            {"id": "measuring", "type": "text", "title": "Measuring Forces", "title_zh": "测量力",
             "content": "Use SPRING BALANCE. Greater force means more stretch. Weight = mass × gravitational field strength. On Earth: Weight (N) approximately 10 × mass (kg). Important: Mass (kg) never changes, Weight (N) changes with location. On Moon: same mass, weight is 1/6 of Earth weight.",
             "content_zh": "使用弹簧秤。力越大拉伸越多。重量 = 质量 × 重力场强度。在地球上：重量（N）约等于10 × 质量（kg）。重要：质量（kg）从不改变，重量（N）随位置改变。在月球上：相同质量，重量是地球重量的1/6。"},
            {"id": "balanced", "type": "text", "title": "Balanced Forces", "title_zh": "平衡力",
             "content": "Forces equal in size, opposite directions. Resultant force = 0 N. Effect: Stationary stays stationary, Moving continues at constant speed. NO change in motion. Examples: book on table, car at constant speed, parachutist at terminal velocity.",
             "content_zh": "力大小相等，方向相反。合力 = 0 N。效果：静止保持静止，运动以恒定速度继续。运动无变化。例子：桌上的书、恒速行驶的汽车、以终端速度下落的跳伞者。"},
            {"id": "unbalanced", "type": "text", "title": "Unbalanced Forces", "title_zh": "不平衡力",
             "content": "Forces NOT equal. Net/resultant force exists. Object ACCELERATES (changes speed or direction). Larger force means greater acceleration. Needed to: start motion, stop motion, speed up, slow down, change direction. Examples: pushing box, rocket launching, braking car.",
             "content_zh": "力不相等。存在净力/合力。物体加速（改变速度或方向）。力越大加速度越大。需要用于：开始运动、停止运动、加速、减速、改变方向。例子：推箱子、火箭发射、刹车汽车。"},
            {"id": "force-animation", "type": "animation", "title": "Forces in Action", "title_zh": "力的作用",
             "content": "ForceMotion", "props": {"scenarios": ["balanced", "unbalanced-right", "unbalanced-up"]}},
            {"id": "friction", "type": "text", "title": "Friction", "title_zh": "摩擦力",
             "content": "Force opposing motion between surfaces. Always acts OPPOSITE to motion. Caused by surface roughness. Types: Static, Kinetic (sliding), Rolling. Useful: walking, braking, writing, grip. Problematic: wastes energy, wears surfaces. Reduce by: lubricants, smoothing, wheels. Increase by: rougher surfaces, more weight.",
             "content_zh": "反对表面间运动的力。总是与运动方向相反。由表面粗糙度引起。类型：静摩擦、动摩擦（滑动）、滚动摩擦。有用：行走、刹车、书写、抓握。有问题：浪费能量、磨损表面。减少方法：润滑剂、抛光、轮子。增加方法：更粗糙表面、更多重量。"},
            {"id": "newtons-first", "type": "text", "title": "Newton's First Law", "title_zh": "牛顿第一定律",
             "content": "Object at rest stays at rest, object in motion stays in motion at constant velocity, unless acted upon by unbalanced force. INERTIA: tendency to resist changes in motion. More mass means more inertia. Examples: seatbelts in cars, tablecloth trick, passengers jerk forward when bus stops. Need unbalanced force to change motion.",
             "content_zh": "静止的物体保持静止，运动的物体以恒定速度保持运动，除非受到不平衡力作用。惯性：抵抗运动变化的倾向。质量越大惯性越大。例子：汽车中的安全带、桌布技巧、公共汽车停止时乘客向前猛冲。需要不平衡力来改变运动。"}
        ],
        "exercises": [
            {"id": "q1", "type": "mcq", "prompt": "What is the SI unit for force?", "prompt_zh": "力的国际单位是什么？",
             "choices": ["Kilogram", "Newton", "Meter", "Joule"], "answer": 1, "hint": "Named after a famous scientist."},
            {"id": "q2", "type": "short", "prompt": "Weight of 8 kg object on Earth (g=10)?", "prompt_zh": "8 kg物体在地球上的重量（g=10）？",
             "answer": "80", "validator": "numeric", "hint": "Weight = mass × g"},
            {"id": "q3", "type": "mcq", "prompt": "Friction always acts...", "prompt_zh": "摩擦力总是作用...",
             "choices": ["in direction of motion", "opposite to motion", "perpendicular", "downward"], "answer": 1, "hint": "Friction opposes motion."}
        ]
    }
    
    # Chapter 5: Angles and Geometry (Math)
    angles_geometry = {
        "id": "angles-geometry",
        "title": "Angles and Basic Geometry",
        "title_zh": "角度和基础几何",
        "description": "Master angles, triangles, and polygon properties with visual demonstrations",
        "description_zh": "通过可视化演示掌握角度、三角形和多边形性质",
        "objectives": [
            "Identify and measure different types of angles",
            "Calculate unknown angles using angle properties",
            "Apply angle properties of triangles",
            "Solve problems involving polygons"
        ],
        "objectives_zh": [
            "识别和测量不同类型的角",
            "使用角的性质计算未知角",
            "应用三角形的角性质",
            "解决涉及多边形的问题"
        ],
        "sections": [
            {"id": "intro-angles", "type": "text", "title": "Introduction to Angles", "title_zh": "角的介绍",
             "content": "Angle formed when two rays meet at vertex. Measured in DEGREES. Types: Acute (0-90), Right (90), Obtuse (90-180), Straight (180), Reflex (180-360), Complete (360). Use protractor to measure. Examples: clock hands, door opening, corners of shapes.",
             "content_zh": "角是当两条射线在顶点相遇时形成的。以度为单位测量。类型：锐角（0-90）、直角（90）、钝角（90-180）、平角（180）、优角（180-360）、完整（360）。使用量角器测量。例子：时钟指针、门打开、形状的角。"},
            {"id": "angle-properties", "type": "text", "title": "Angle Properties", "title_zh": "角的性质",
             "content": "Angles at a point = 360. Angles on straight line = 180. Vertically opposite angles are equal. Complementary angles add to 90. Supplementary angles add to 180. Adjacent angles share common arm.",
             "content_zh": "一点的角 = 360。直线上的角 = 180。对顶角相等。互补角和为90。补角和为180。邻角共享公共边。"},
            {"id": "parallel-lines", "type": "text", "title": "Parallel Lines", "title_zh": "平行线",
             "content": "Parallel lines never meet. When transversal crosses parallel lines: Corresponding angles equal (F pattern), Alternate interior angles equal (Z pattern), Co-interior angles add to 180 (C pattern). Applications: railway tracks, ladder against wall, road crossings.",
             "content_zh": "平行线永不相遇。当横截线穿过平行线时：同位角相等（F型）、内错角相等（Z型）、同侧内角和为180（C型）。应用：铁轨、靠墙的梯子、道路交叉口。"},
            {"id": "triangle-angles", "type": "math", "title": "Triangle Angle Sum", "title_zh": "三角形内角和",
             "content": "∠A + ∠B + ∠C = 180°",
             "explanation": "Three interior angles of ANY triangle always add to 180. Exterior angle equals sum of two opposite interior angles. Types by angles: Acute (all < 90), Right (one = 90), Obtuse (one > 90). Types by sides: Equilateral (all equal, all angles 60), Isosceles (two equal sides, two equal angles), Scalene (all different).",
             "explanation_zh": "任何三角形的三个内角总和总是180。外角等于两个相对内角的和。按角分类：锐角（都 < 90）、直角（一个 = 90）、钝角（一个 > 90）。按边分类：等边（都相等，所有角60）、等腰（两边相等，两角相等）、不等边（都不同）。"},
            {"id": "polygon-angles", "type": "text", "title": "Angles in Polygons", "title_zh": "多边形的角",
             "content": "Sum of interior angles = (n-2) × 180 where n = sides. Triangle (3): 180. Quadrilateral (4): 360. Pentagon (5): 540. Hexagon (6): 720. Regular polygon: each angle = [(n-2) × 180] / n. Sum of exterior angles = 360 always. Each exterior = 360/n for regular polygon.",
             "content_zh": "内角和 = (n-2) × 180其中n = 边数。三角形（3）：180。四边形（4）：360。五边形（5）：540。六边形（6）：720。正多边形：每个角 = [(n-2) × 180] / n。外角和 = 360总是。正多边形每个外角 = 360/n。"},
            {"id": "quadrilaterals", "type": "text", "title": "Special Quadrilaterals", "title_zh": "特殊四边形",
             "content": "Square: 4 equal sides, all angles 90. Rectangle: opposite sides equal, all angles 90. Parallelogram: opposite sides equal and parallel, opposite angles equal. Rhombus: 4 equal sides, opposite angles equal. Trapezium: one pair parallel sides. Kite: two pairs adjacent sides equal. All quadrilaterals: interior angles sum = 360.",
             "content_zh": "正方形：4边相等，所有角90。矩形：对边相等，所有角90。平行四边形：对边相等且平行，对角相等。菱形：4边相等，对角相等。梯形：一对平行边。风筝：两对相邻边相等。所有四边形：内角和 = 360。"}
        ],
        "exercises": [
            {"id": "q1", "type": "mcq", "prompt": "Which type of angle is 125°?", "prompt_zh": "125°是哪种类型的角？",
             "choices": ["Acute", "Right", "Obtuse", "Straight"], "answer": 2, "hint": "Between 90 and 180."},
            {"id": "q2", "type": "short", "prompt": "Angles on straight line: 75° and x°. Find x.", "prompt_zh": "直线上的角：75°和x°。求x。",
             "answer": "105", "validator": "numeric", "hint": "Add to 180."},
            {"id": "q3", "type": "short", "prompt": "Triangle angles: 45°, 65°, and x°. Find x.", "prompt_zh": "三角形角：45°，65°和x°。求x。",
             "answer": "70", "validator": "numeric", "hint": "Add to 180."},
            {"id": "q4", "type": "mcq", "prompt": "Sum of interior angles of hexagon?", "prompt_zh": "六边形内角和？",
             "choices": ["540°", "720°", "900°", "1080°"], "answer": 1, "hint": "(6-2) × 180"}
        ]
    }
    
    return {
        "algebraic-expressions": algebraic_expressions,
        "percentage": percentage,
        "particle-model": particle_model,
        "forces-motion": forces_motion,
        "angles-geometry": angles_geometry
    }

def main():
    print("🚀 Starting integration of all expanded chapters...")
    print("=" * 60)
    
    # Setup paths
    content_file = Path("src/data/content.json")
    
    if not content_file.exists():
        print(f"❌ Error: {content_file} not found!")
        print("   Make sure you're running this from verse-learn-path directory")
        return
    
    # Create backup
    backup_file = create_backup(content_file)
    
    # Load content.json
    print("\n📖 Loading content.json...")
    with open(content_file, 'r', encoding='utf-8') as f:
        content = json.load(f)
    
    # Get expanded chapters
    print("\n📚 Preparing expanded chapters...")
    expanded_chapters = get_expanded_chapters()
    
    # Find subjects
    math_subject = next((s for s in content['subjects'] if s['id'] == 'math'), None)
    science_subject = next((s for s in content['subjects'] if s['id'] == 'science'), None)
    
    if not math_subject or not science_subject:
        print("❌ Error: Could not find math or science subjects!")
        return
    
    # Integration counters
    integrated = []
    
    # Integrate Algebraic Expressions (Math)
    print("\n🔄 Integrating: Algebraic Expressions...")
    idx = next((i for i, c in enumerate(math_subject['chapters']) 
                if c['id'] == 'algebraic-expressions'), None)
    if idx is not None:
        old = math_subject['chapters'][idx]
        new = expanded_chapters['algebraic-expressions']
        print(f"   Old: {len(old.get('sections', []))} sections, {len(old.get('exercises', []))} exercises")
        print(f"   New: {len(new['sections'])} sections, {len(new['exercises'])} exercises")
        math_subject['chapters'][idx] = new
        integrated.append('Algebraic Expressions')
    
    # Integrate Percentage (Math)
    print("\n🔄 Integrating: Percentage Applications...")
    idx = next((i for i, c in enumerate(math_subject['chapters']) 
                if c['id'] == 'percentage'), None)
    if idx is not None:
        old = math_subject['chapters'][idx]
        new = expanded_chapters['percentage']
        print(f"   Old: {len(old.get('sections', []))} sections, {len(old.get('exercises', []))} exercises")
        print(f"   New: {len(new['sections'])} sections, {len(new['exercises'])} exercises")
        math_subject['chapters'][idx] = new
        integrated.append('Percentage Applications')
    
    # Integrate Particulate Model (Science)
    print("\n🔄 Integrating: Particulate Model of Matter...")
    idx = next((i for i, c in enumerate(science_subject['chapters']) 
                if c['id'] == 'particle-model'), None)
    if idx is not None:
        old = science_subject['chapters'][idx]
        new = expanded_chapters['particle-model']
        print(f"   Old: {len(old.get('sections', []))} sections, {len(old.get('exercises', []))} exercises")
        print(f"   New: {len(new['sections'])} sections, {len(new['exercises'])} exercises")
        science_subject['chapters'][idx] = new
        integrated.append('Particulate Model of Matter')
    
    # Integrate Forces & Motion (Science)
    print("\n🔄 Integrating: Forces and Motion...")
    idx = next((i for i, c in enumerate(science_subject['chapters']) 
                if c['id'] == 'forces-motion'), None)
    if idx is not None:
        old = science_subject['chapters'][idx]
        new = expanded_chapters['forces-motion']
        print(f"   Old: {len(old.get('sections', []))} sections, {len(old.get('exercises', []))} exercises")
        print(f"   New: {len(new['sections'])} sections, {len(new['exercises'])} exercises")
        science_subject['chapters'][idx] = new
        integrated.append('Forces and Motion')
    
    # Integrate Angles & Geometry (Math)
    print("\n🔄 Integrating: Angles and Basic Geometry...")
    idx = next((i for i, c in enumerate(math_subject['chapters']) 
                if c['id'] == 'angles-geometry'), None)
    if idx is not None:
        old = math_subject['chapters'][idx]
        new = expanded_chapters['angles-geometry']
        print(f"   Old: {len(old.get('sections', []))} sections, {len(old.get('exercises', []))} exercises")
        print(f"   New: {len(new['sections'])} sections, {len(new['exercises'])} exercises")
        math_subject['chapters'][idx] = new
        integrated.append('Angles and Basic Geometry')
    
    # Save updated content
    print("\n💾 Saving updated content.json...")
    with open(content_file, 'w', encoding='utf-8') as f:
        json.dump(content, f, indent=2, ensure_ascii=False)
    
    # Summary
    print("\n" + "=" * 60)
    print("✅ SUCCESS! Integration complete!")
    print(f"\n📊 Integrated {len(integrated)} chapter(s):")
    for chapter in integrated:
        print(f"   ✓ {chapter}")
    
    print(f"\n💾 Backup saved as: {backup_file.name}")
    print("\n🎯 Next steps:")
    print("   1. Run: npm run dev")
    print("   2. Navigate to the updated chapters")
    print("   3. You should see expanded content!")
    print("\n💡 To integrate more chapters, I'll add them to this script.")

if __name__ == "__main__":
    main()
