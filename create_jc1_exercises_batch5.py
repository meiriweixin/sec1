import json

# Load existing JC 1 chapters
with open('chapters/jc1_math_chapters.json', 'r', encoding='utf-8') as f:
    jc1_chapters = json.load(f)

# Chapter 7: Trigonometric Identities & Equations - 15 exercises
chapter_7_exercises = [
    # Easy (1-5)
    {
        "id": "trig-id-jc1-ex1",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "Simplify sin²θ + cos²θ.",
        "prompt_zh": "简化 sin²θ + cos²θ。",
        "choices": [
            "1",
            "0",
            "2",
            "sin θ cos θ"
        ],
        "choices_zh": [
            "1",
            "0",
            "2",
            "sin θ cos θ"
        ],
        "answer": 0,
        "explanation": "**Problem:** Apply the Pythagorean identity.\n\n**Key Concept:** The fundamental identity sin²θ + cos²θ = 1 holds for all angles θ.\n\n**Steps:**\n1. This is the Pythagorean identity, one of the most important trig identities\n2. It's derived from the unit circle: x² + y² = 1 where x = cos θ and y = sin θ\n3. Therefore: sin²θ + cos²θ = 1\n\n**Answer:** 1\n\n**Common Mistakes:** Trying to simplify further when the answer is already in simplest form.\n\n**Tip:** This identity is fundamental - memorize it! It's used in countless trigonometric proofs.",
        "explanation_zh": "**问题：** 应用勾股恒等式。\n\n**关键概念：** 基本恒等式 sin²θ + cos²θ = 1 对所有角 θ 成立。\n\n**步骤：**\n1. 这是勾股恒等式，最重要的三角恒等式之一\n2. 它源自单位圆：x² + y² = 1，其中 x = cos θ 和 y = sin θ\n3. 因此：sin²θ + cos²θ = 1\n\n**答案：** 1\n\n**常见错误：** 当答案已经是最简形式时还试图进一步简化。\n\n**提示：** 这个恒等式是基础 - 记住它！它用于无数三角证明。"
    },
    {
        "id": "trig-id-jc1-ex2",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "Express tan θ in terms of sin θ and cos θ.",
        "prompt_zh": "用 sin θ 和 cos θ 表示 tan θ。",
        "choices": [
            "sin θ / cos θ",
            "cos θ / sin θ",
            "sin θ × cos θ",
            "1 / (sin θ cos θ)"
        ],
        "choices_zh": [
            "sin θ / cos θ",
            "cos θ / sin θ",
            "sin θ × cos θ",
            "1 / (sin θ cos θ)"
        ],
        "answer": 0,
        "explanation": "**Problem:** Write tan θ using sine and cosine.\n\n**Key Concept:** The tangent function is defined as the ratio of sine to cosine.\n\n**Steps:**\n1. By definition: tan θ = sin θ / cos θ\n2. This comes from the right triangle: opposite/adjacent = (opposite/hypotenuse) ÷ (adjacent/hypotenuse)\n\n**Answer:** sin θ / cos θ\n\n**Common Mistakes:** Inverting the fraction (writing cos θ / sin θ, which is cot θ).\n\n**Tip:** Remember: SOH-CAH-TOA → Tan = Opposite/Adjacent = Sin/Cos.",
        "explanation_zh": "**问题：** 使用正弦和余弦写 tan θ。\n\n**关键概念：** 正切函数定义为正弦与余弦的比率。\n\n**步骤：**\n1. 根据定义：tan θ = sin θ / cos θ\n2. 这来自直角三角形：对边/邻边 = (对边/斜边) ÷ (邻边/斜边)\n\n**答案：** sin θ / cos θ\n\n**常见错误：** 颠倒分数（写 cos θ / sin θ，这是 cot θ）。\n\n**提示：** 记住：正切 = 对边/邻边 = 正弦/余弦。"
    },
    {
        "id": "trig-id-jc1-ex3",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "Simplify 1 - cos²θ.",
        "prompt_zh": "简化 1 - cos²θ。",
        "choices": [
            "sin²θ",
            "cos²θ",
            "tan²θ",
            "1"
        ],
        "choices_zh": [
            "sin²θ",
            "cos²θ",
            "tan²θ",
            "1"
        ],
        "answer": 0,
        "explanation": "**Problem:** Use the Pythagorean identity to simplify.\n\n**Key Concept:** Rearrange sin²θ + cos²θ = 1 to get sin²θ = 1 - cos²θ.\n\n**Steps:**\n1. Start with: sin²θ + cos²θ = 1\n2. Subtract cos²θ from both sides: sin²θ = 1 - cos²θ\n3. Therefore: 1 - cos²θ = sin²θ\n\n**Answer:** sin²θ\n\n**Common Mistakes:** Not recognizing this as a rearrangement of the Pythagorean identity.\n\n**Tip:** Similarly, 1 - sin²θ = cos²θ. These forms are very useful for simplification.",
        "explanation_zh": "**问题：** 使用勾股恒等式简化。\n\n**关键概念：** 重新排列 sin²θ + cos²θ = 1 得到 sin²θ = 1 - cos²θ。\n\n**步骤：**\n1. 从 sin²θ + cos²θ = 1 开始\n2. 两边减去 cos²θ：sin²θ = 1 - cos²θ\n3. 因此：1 - cos²θ = sin²θ\n\n**答案：** sin²θ\n\n**常见错误：** 没有认识到这是勾股恒等式的重新排列。\n\n**提示：** 类似地，1 - sin²θ = cos²θ。这些形式对简化非常有用。"
    },
    {
        "id": "trig-id-jc1-ex4",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "What is the exact value of sin 30°?",
        "prompt_zh": "sin 30° 的精确值是多少？",
        "choices": [
            "1/2",
            "√3/2",
            "1/√2",
            "√2/2"
        ],
        "choices_zh": [
            "1/2",
            "√3/2",
            "1/√2",
            "√2/2"
        ],
        "answer": 0,
        "explanation": "**Problem:** Recall the exact value of sin 30°.\n\n**Key Concept:** Special angles (30°, 45°, 60°) have exact trigonometric values.\n\n**Steps:**\n1. From the 30-60-90 triangle with sides 1, √3, 2:\n2. sin 30° = opposite/hypotenuse = 1/2\n\n**Answer:** 1/2\n\n**Common Mistakes:** Confusing sin 30° = 1/2 with sin 60° = √3/2.\n\n**Tip:** Memorize: sin 30° = 1/2, sin 45° = √2/2, sin 60° = √3/2.",
        "explanation_zh": "**问题：** 回忆 sin 30° 的精确值。\n\n**关键概念：** 特殊角（30°、45°、60°）有精确的三角函数值。\n\n**步骤：**\n1. 从边长为 1、√3、2 的 30-60-90 三角形：\n2. sin 30° = 对边/斜边 = 1/2\n\n**答案：** 1/2\n\n**常见错误：** 混淆 sin 30° = 1/2 和 sin 60° = √3/2。\n\n**提示：** 记住：sin 30° = 1/2，sin 45° = √2/2，sin 60° = √3/2。"
    },
    {
        "id": "trig-id-jc1-ex5",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "Solve sin θ = 0.5 for 0° ≤ θ ≤ 180°.",
        "prompt_zh": "求解 sin θ = 0.5，其中 0° ≤ θ ≤ 180°。",
        "choices": [
            "θ = 30° or 150°",
            "θ = 60° or 120°",
            "θ = 45° or 135°",
            "θ = 30° only"
        ],
        "choices_zh": [
            "θ = 30° 或 150°",
            "θ = 60° 或 120°",
            "θ = 45° 或 135°",
            "仅 θ = 30°"
        ],
        "answer": 0,
        "explanation": "**Problem:** Find all angles in [0°, 180°] where sin θ = 0.5.\n\n**Key Concept:** Sine is positive in first and second quadrants, and sin θ = sin(180° - θ).\n\n**Steps:**\n1. Basic angle: sin 30° = 0.5, so one solution is θ = 30°\n2. In second quadrant: θ = 180° - 30° = 150°\n3. Both angles are in the range [0°, 180°]\n\n**Answer:** θ = 30° or 150°\n\n**Common Mistakes:** Only finding one solution (missing the second quadrant angle).\n\n**Tip:** For 0° ≤ θ ≤ 180°, if sin θ = k, solutions are θ and 180° - θ (if both in range).",
        "explanation_zh": "**问题：** 求 [0°, 180°] 中所有满足 sin θ = 0.5 的角。\n\n**关键概念：** 正弦在第一和第二象限为正，且 sin θ = sin(180° - θ)。\n\n**步骤：**\n1. 基本角：sin 30° = 0.5，所以一个解是 θ = 30°\n2. 在第二象限：θ = 180° - 30° = 150°\n3. 两个角都在范围 [0°, 180°] 内\n\n**答案：** θ = 30° 或 150°\n\n**常见错误：** 只找到一个解（遗漏第二象限的角）。\n\n**提示：** 对于 0° ≤ θ ≤ 180°，如果 sin θ = k，解是 θ 和 180° - θ（如果都在范围内）。"
    },

    # Medium (6-10)
    {
        "id": "trig-id-jc1-ex6",
        "type": "mcq",
        "difficulty": "medium",
        "prompt": "Prove the identity: (sin θ + cos θ)² = 1 + 2sin θ cos θ. Which step is correct?",
        "prompt_zh": "证明恒等式：(sin θ + cos θ)² = 1 + 2sin θ cos θ。哪一步是正确的？",
        "choices": [
            "Expand: sin²θ + 2sin θ cos θ + cos²θ = (sin²θ + cos²θ) + 2sin θ cos θ = 1 + 2sin θ cos θ",
            "Cancel: sin θ + cos θ = 1 + 2sin θ cos θ",
            "Square both: sin²θ + cos²θ = 1 + 4sin²θ cos²θ",
            "Divide: sin θ + cos θ = 1/2 + sin θ cos θ"
        ],
        "choices_zh": [
            "展开：sin²θ + 2sin θ cos θ + cos²θ = (sin²θ + cos²θ) + 2sin θ cos θ = 1 + 2sin θ cos θ",
            "消去：sin θ + cos θ = 1 + 2sin θ cos θ",
            "两边平方：sin²θ + cos²θ = 1 + 4sin²θ cos²θ",
            "除以：sin θ + cos θ = 1/2 + sin θ cos θ"
        ],
        "answer": 0,
        "explanation": "**Problem:** Verify the identity by expanding the left side.\n\n**Key Concept:** Use (a + b)² = a² + 2ab + b² and the Pythagorean identity.\n\n**Steps:**\n1. Expand LHS: (sin θ + cos θ)² = sin²θ + 2sin θ cos θ + cos²θ\n2. Group: = (sin²θ + cos²θ) + 2sin θ cos θ\n3. Apply identity: = 1 + 2sin θ cos θ\n4. This equals RHS ✓\n\n**Answer:** Expand: sin²θ + 2sin θ cos θ + cos²θ = (sin²θ + cos²θ) + 2sin θ cos θ = 1 + 2sin θ cos θ\n\n**Common Mistakes:** Not grouping sin²θ + cos²θ to recognize the Pythagorean identity.\n\n**Tip:** When proving identities, work from one side to the other - don't perform operations on both sides simultaneously.",
        "explanation_zh": "**问题：** 通过展开左边验证恒等式。\n\n**关键概念：** 使用 (a + b)² = a² + 2ab + b² 和勾股恒等式。\n\n**步骤：**\n1. 展开左边：(sin θ + cos θ)² = sin²θ + 2sin θ cos θ + cos²θ\n2. 分组：= (sin²θ + cos²θ) + 2sin θ cos θ\n3. 应用恒等式：= 1 + 2sin θ cos θ\n4. 这等于右边 ✓\n\n**答案：** 展开：sin²θ + 2sin θ cos θ + cos²θ = (sin²θ + cos²θ) + 2sin θ cos θ = 1 + 2sin θ cos θ\n\n**常见错误：** 没有分组 sin²θ + cos²θ 来识别勾股恒等式。\n\n**提示：** 证明恒等式时，从一边做到另一边 - 不要同时对两边进行运算。"
    },
    {
        "id": "trig-id-jc1-ex7",
        "type": "mcq",
        "difficulty": "medium",
        "prompt": "At Marina Bay Sands, the angle of elevation to the top of the hotel from a point 200m away is θ, where tan θ = 0.866. If tan²θ + 1 = sec²θ, find sec θ (to 3 significant figures).",
        "prompt_zh": "在滨海湾金沙酒店，从 200 米外的一点到酒店顶部的仰角为 θ，其中 tan θ = 0.866。如果 tan²θ + 1 = sec²θ，求 sec θ（保留 3 位有效数字）。",
        "choices": [
            "1.30",
            "0.866",
            "1.15",
            "1.73"
        ],
        "choices_zh": [
            "1.30",
            "0.866",
            "1.15",
            "1.73"
        ],
        "answer": 0,
        "explanation": "**Problem:** Use the identity tan²θ + 1 = sec²θ to find sec θ.\n\n**Key Concept:** The identity tan²θ + 1 = sec²θ is derived from dividing sin²θ + cos²θ = 1 by cos²θ.\n\n**Steps:**\n1. Given: tan θ = 0.866\n2. Use identity: sec²θ = tan²θ + 1\n3. Calculate: sec²θ = (0.866)² + 1 = 0.750 + 1 = 1.750\n4. Take square root: sec θ = √1.750 ≈ 1.32\n5. To 3 s.f.: sec θ ≈ 1.30\n\n**Answer:** 1.30\n\n**Common Mistakes:** Forgetting to take the square root after finding sec²θ.\n\n**Tip:** Singapore landmarks: Marina Bay Sands is 200m tall - trigonometry helps calculate viewing angles from different distances.",
        "explanation_zh": "**问题：** 使用恒等式 tan²θ + 1 = sec²θ 求 sec θ。\n\n**关键概念：** 恒等式 tan²θ + 1 = sec²θ 源自将 sin²θ + cos²θ = 1 除以 cos²θ。\n\n**步骤：**\n1. 已知：tan θ = 0.866\n2. 使用恒等式：sec²θ = tan²θ + 1\n3. 计算：sec²θ = (0.866)² + 1 = 0.750 + 1 = 1.750\n4. 开平方：sec θ = √1.750 ≈ 1.32\n5. 保留 3 位有效数字：sec θ ≈ 1.30\n\n**答案：** 1.30\n\n**常见错误：** 求出 sec²θ 后忘记开平方。\n\n**提示：** 新加坡地标：滨海湾金沙酒店高 200 米 - 三角函数帮助计算不同距离的观看角度。"
    },
    {
        "id": "trig-id-jc1-ex8",
        "type": "mcq",
        "difficulty": "medium",
        "prompt": "Simplify: (1 + tan²θ) cos²θ.",
        "prompt_zh": "简化：(1 + tan²θ) cos²θ。",
        "choices": [
            "1",
            "sin²θ",
            "cos²θ",
            "tan²θ"
        ],
        "choices_zh": [
            "1",
            "sin²θ",
            "cos²θ",
            "tan²θ"
        ],
        "answer": 0,
        "explanation": "**Problem:** Simplify using trigonometric identities.\n\n**Key Concept:** Use tan²θ + 1 = sec²θ and sec θ = 1/cos θ.\n\n**Steps:**\n1. Recognize: 1 + tan²θ = sec²θ\n2. Substitute: (1 + tan²θ) cos²θ = sec²θ × cos²θ\n3. Since sec θ = 1/cos θ, we have sec²θ = 1/cos²θ\n4. Therefore: (1/cos²θ) × cos²θ = 1\n\n**Answer:** 1\n\n**Common Mistakes:** Not recognizing the identity 1 + tan²θ = sec²θ.\n\n**Tip:** Memorize the three Pythagorean identities: sin²θ + cos²θ = 1, tan²θ + 1 = sec²θ, 1 + cot²θ = csc²θ.",
        "explanation_zh": "**问题：** 使用三角恒等式简化。\n\n**关键概念：** 使用 tan²θ + 1 = sec²θ 和 sec θ = 1/cos θ。\n\n**步骤：**\n1. 识别：1 + tan²θ = sec²θ\n2. 代入：(1 + tan²θ) cos²θ = sec²θ × cos²θ\n3. 因为 sec θ = 1/cos θ，所以 sec²θ = 1/cos²θ\n4. 因此：(1/cos²θ) × cos²θ = 1\n\n**答案：** 1\n\n**常见错误：** 没有识别恒等式 1 + tan²θ = sec²θ。\n\n**提示：** 记住三个勾股恒等式：sin²θ + cos²θ = 1，tan²θ + 1 = sec²θ，1 + cot²θ = csc²θ。"
    },
    {
        "id": "trig-id-jc1-ex9",
        "type": "mcq",
        "difficulty": "medium",
        "prompt": "Solve 2sin²θ - sin θ - 1 = 0 for 0° ≤ θ ≤ 360°.",
        "prompt_zh": "求解 2sin²θ - sin θ - 1 = 0，其中 0° ≤ θ ≤ 360°。",
        "choices": [
            "θ = 90°, 210°, 330°",
            "θ = 30°, 150°",
            "θ = 45°, 135°, 225°, 315°",
            "θ = 60°, 120°, 240°, 300°"
        ],
        "choices_zh": [
            "θ = 90°, 210°, 330°",
            "θ = 30°, 150°",
            "θ = 45°, 135°, 225°, 315°",
            "θ = 60°, 120°, 240°, 300°"
        ],
        "answer": 0,
        "explanation": "**Problem:** Solve quadratic equation in sin θ.\n\n**Key Concept:** Treat as quadratic in sin θ, factor, then solve each case.\n\n**Steps:**\n1. Let u = sin θ: 2u² - u - 1 = 0\n2. Factor: (2u + 1)(u - 1) = 0\n3. Solutions: u = -1/2 or u = 1\n4. Case 1: sin θ = 1 → θ = 90°\n5. Case 2: sin θ = -1/2\n   - Basic angle: sin 30° = 1/2\n   - Sine is negative in quadrants 3 and 4\n   - θ = 180° + 30° = 210° or θ = 360° - 30° = 330°\n6. All solutions: θ = 90°, 210°, 330°\n\n**Answer:** θ = 90°, 210°, 330°\n\n**Common Mistakes:** Missing solutions in different quadrants or not checking all cases.\n\n**Tip:** Always check which quadrants give the correct sign for the trig function.",
        "explanation_zh": "**问题：** 求解关于 sin θ 的二次方程。\n\n**关键概念：** 视为关于 sin θ 的二次方程，因式分解，然后求解每种情况。\n\n**步骤：**\n1. 令 u = sin θ：2u² - u - 1 = 0\n2. 因式分解：(2u + 1)(u - 1) = 0\n3. 解：u = -1/2 或 u = 1\n4. 情况 1：sin θ = 1 → θ = 90°\n5. 情况 2：sin θ = -1/2\n   - 基本角：sin 30° = 1/2\n   - 正弦在第 3 和第 4 象限为负\n   - θ = 180° + 30° = 210° 或 θ = 360° - 30° = 330°\n6. 所有解：θ = 90°, 210°, 330°\n\n**答案：** θ = 90°, 210°, 330°\n\n**常见错误：** 遗漏不同象限的解或没有检查所有情况。\n\n**提示：** 总是检查哪些象限给出三角函数的正确符号。"
    },
    {
        "id": "trig-id-jc1-ex10",
        "type": "short",
        "difficulty": "medium",
        "prompt": "Given that cos θ = 3/5 and θ is acute, find the exact value of tan θ.",
        "prompt_zh": "已知 cos θ = 3/5 且 θ 为锐角，求 tan θ 的精确值。",
        "answer": "4/3",
        "validator": "smart",
        "explanation": "**Problem:** Find tan θ given cos θ and using Pythagorean identity.\n\n**Key Concept:** Use sin²θ + cos²θ = 1 to find sin θ, then tan θ = sin θ / cos θ.\n\n**Steps:**\n1. Given: cos θ = 3/5 and θ is acute (so sin θ > 0)\n2. Use identity: sin²θ + cos²θ = 1\n3. Substitute: sin²θ + (3/5)² = 1\n4. Simplify: sin²θ + 9/25 = 1\n5. Solve: sin²θ = 1 - 9/25 = 16/25\n6. Since θ is acute: sin θ = 4/5 (positive)\n7. Therefore: tan θ = sin θ / cos θ = (4/5) / (3/5) = 4/3\n\n**Answer:** 4/3\n\n**Common Mistakes:** Forgetting to check the quadrant (acute means both sin and cos are positive).\n\n**Tip:** This is a 3-4-5 right triangle! Recognize common Pythagorean triples to save time.",
        "explanation_zh": "**问题：** 已知 cos θ 并使用勾股恒等式求 tan θ。\n\n**关键概念：** 使用 sin²θ + cos²θ = 1 求 sin θ，然后 tan θ = sin θ / cos θ。\n\n**步骤：**\n1. 已知：cos θ = 3/5 且 θ 为锐角（所以 sin θ > 0）\n2. 使用恒等式：sin²θ + cos²θ = 1\n3. 代入：sin²θ + (3/5)² = 1\n4. 简化：sin²θ + 9/25 = 1\n5. 解：sin²θ = 1 - 9/25 = 16/25\n6. 因为 θ 为锐角：sin θ = 4/5（正）\n7. 因此：tan θ = sin θ / cos θ = (4/5) / (3/5) = 4/3\n\n**答案：** 4/3\n\n**常见错误：** 忘记检查象限（锐角意味着 sin 和 cos 都为正）。\n\n**提示：** 这是一个 3-4-5 直角三角形！识别常见的勾股三元组可以节省时间。"
    },

    # Hard (11-15)
    {
        "id": "trig-id-jc1-ex11",
        "type": "mcq",
        "difficulty": "hard",
        "prompt": "Prove that (sin θ)/(1 - cos θ) = (1 + cos θ)/(sin θ) is an identity. Which is the correct first step?",
        "prompt_zh": "证明 (sin θ)/(1 - cos θ) = (1 + cos θ)/(sin θ) 是一个恒等式。哪一个是正确的第一步？",
        "choices": [
            "Cross-multiply: sin²θ = (1 - cos θ)(1 + cos θ) = 1 - cos²θ",
            "Add fractions: sin θ + 1 + cos θ = 1 - cos θ + sin θ",
            "Cancel: 1 = 1",
            "Square both sides: sin²θ/(1 - cos θ)² = (1 + cos θ)²/sin²θ"
        ],
        "choices_zh": [
            "交叉相乘：sin²θ = (1 - cos θ)(1 + cos θ) = 1 - cos²θ",
            "加分数：sin θ + 1 + cos θ = 1 - cos θ + sin θ",
            "消去：1 = 1",
            "两边平方：sin²θ/(1 - cos θ)² = (1 + cos θ)²/sin²θ"
        ],
        "answer": 0,
        "explanation": "**Problem:** Verify the identity by cross-multiplying.\n\n**Key Concept:** Cross-multiply and use difference of squares: (1 - cos θ)(1 + cos θ) = 1 - cos²θ = sin²θ.\n\n**Steps:**\n1. Cross-multiply: sin θ × sin θ = (1 - cos θ)(1 + cos θ)\n2. LHS: sin²θ\n3. RHS: (1 - cos θ)(1 + cos θ) = 1 - cos²θ (difference of squares)\n4. Use identity: 1 - cos²θ = sin²θ\n5. Therefore: sin²θ = sin²θ ✓\n\n**Answer:** Cross-multiply: sin²θ = (1 - cos θ)(1 + cos θ) = 1 - cos²θ\n\n**Common Mistakes:** Not recognizing the difference of squares pattern (a - b)(a + b) = a² - b².\n\n**Tip:** When proving identities with fractions, cross-multiplying is often a good strategy.",
        "explanation_zh": "**问题：** 通过交叉相乘验证恒等式。\n\n**关键概念：** 交叉相乘并使用平方差公式：(1 - cos θ)(1 + cos θ) = 1 - cos²θ = sin²θ。\n\n**步骤：**\n1. 交叉相乘：sin θ × sin θ = (1 - cos θ)(1 + cos θ)\n2. 左边：sin²θ\n3. 右边：(1 - cos θ)(1 + cos θ) = 1 - cos²θ（平方差）\n4. 使用恒等式：1 - cos²θ = sin²θ\n5. 因此：sin²θ = sin²θ ✓\n\n**答案：** 交叉相乘：sin²θ = (1 - cos θ)(1 + cos θ) = 1 - cos²θ\n\n**常见错误：** 没有识别平方差模式 (a - b)(a + b) = a² - b²。\n\n**提示：** 证明含分数的恒等式时，交叉相乘通常是一个好策略。"
    },
    {
        "id": "trig-id-jc1-ex12",
        "type": "mcq",
        "difficulty": "hard",
        "prompt": "The Singapore Flyer (observation wheel) rotates such that the height h meters above ground of a passenger is given by h = 80 + 75sin(θ), where θ is the angle from the starting position. Find all values of θ in [0°, 360°] where the passenger is at height 117.5m.",
        "prompt_zh": "新加坡摩天轮旋转时，乘客距地面的高度 h 米由 h = 80 + 75sin(θ) 给出，其中 θ 是从起始位置的角度。求 [0°, 360°] 中所有使乘客高度为 117.5 米的 θ 值。",
        "choices": [
            "θ = 30°, 150°",
            "θ = 60°, 120°",
            "θ = 45°, 135°",
            "θ = 90° only"
        ],
        "choices_zh": [
            "θ = 30°, 150°",
            "θ = 60°, 120°",
            "θ = 45°, 135°",
            "仅 θ = 90°"
        ],
        "answer": 0,
        "explanation": "**Problem:** Solve 117.5 = 80 + 75sin(θ) for θ in [0°, 360°].\n\n**Key Concept:** Isolate sin(θ), then find all angles in the specified range.\n\n**Steps:**\n1. Equation: 117.5 = 80 + 75sin(θ)\n2. Subtract 80: 37.5 = 75sin(θ)\n3. Divide by 75: sin(θ) = 37.5/75 = 0.5\n4. Basic angle: sin 30° = 0.5\n5. Sine is positive in quadrants 1 and 2\n6. First quadrant: θ = 30°\n7. Second quadrant: θ = 180° - 30° = 150°\n\n**Answer:** θ = 30°, 150°\n\n**Common Mistakes:** Only finding one solution instead of checking all quadrants.\n\n**Tip:** Singapore Flyer: 165m tall wheel (diameter 150m, center at 80m) - passengers reach 117.5m twice per rotation at symmetric positions.",
        "explanation_zh": "**问题：** 求解 117.5 = 80 + 75sin(θ)，其中 θ 在 [0°, 360°]。\n\n**关键概念：** 分离 sin(θ)，然后求指定范围内的所有角。\n\n**步骤：**\n1. 方程：117.5 = 80 + 75sin(θ)\n2. 减去 80：37.5 = 75sin(θ)\n3. 除以 75：sin(θ) = 37.5/75 = 0.5\n4. 基本角：sin 30° = 0.5\n5. 正弦在第 1 和第 2 象限为正\n6. 第一象限：θ = 30°\n7. 第二象限：θ = 180° - 30° = 150°\n\n**答案：** θ = 30°, 150°\n\n**常见错误：** 只找到一个解而不是检查所有象限。\n\n**提示：** 新加坡摩天轮：165 米高的轮子（直径 150 米，中心在 80 米） - 乘客在对称位置每旋转一次两次达到 117.5 米。"
    },
    {
        "id": "trig-id-jc1-ex13",
        "type": "short",
        "difficulty": "hard",
        "prompt": "Solve the equation 2cos²θ + 3sin θ = 0 for 0° ≤ θ ≤ 360°. Give the smallest positive solution in degrees.",
        "prompt_zh": "求解方程 2cos²θ + 3sin θ = 0，其中 0° ≤ θ ≤ 360°。给出最小的正解（以度为单位）。",
        "answer": "210",
        "validator": "numeric",
        "explanation": "**Problem:** Solve equation by converting to single trig function.\n\n**Key Concept:** Use cos²θ = 1 - sin²θ to convert to quadratic in sin θ.\n\n**Steps:**\n1. Replace cos²θ: 2(1 - sin²θ) + 3sin θ = 0\n2. Expand: 2 - 2sin²θ + 3sin θ = 0\n3. Rearrange: -2sin²θ + 3sin θ + 2 = 0\n4. Multiply by -1: 2sin²θ - 3sin θ - 2 = 0\n5. Let u = sin θ: 2u² - 3u - 2 = 0\n6. Factor: (2u + 1)(u - 2) = 0\n7. Solutions: u = -1/2 or u = 2\n8. Since -1 ≤ sin θ ≤ 1, only u = -1/2 is valid\n9. sin θ = -1/2\n10. Basic angle: 30° (since sin 30° = 1/2)\n11. Sine is negative in quadrants 3 and 4:\n    - Q3: θ = 180° + 30° = 210°\n    - Q4: θ = 360° - 30° = 330°\n12. Smallest solution: 210°\n\n**Answer:** 210\n\n**Common Mistakes:** Accepting sin θ = 2 as valid (impossible since |sin θ| ≤ 1).\n\n**Tip:** Always check if solutions are within the range of the trig function before finding angles.",
        "explanation_zh": "**问题：** 通过转换为单一三角函数求解方程。\n\n**关键概念：** 使用 cos²θ = 1 - sin²θ 转换为关于 sin θ 的二次方程。\n\n**步骤：**\n1. 替换 cos²θ：2(1 - sin²θ) + 3sin θ = 0\n2. 展开：2 - 2sin²θ + 3sin θ = 0\n3. 重新排列：-2sin²θ + 3sin θ + 2 = 0\n4. 乘以 -1：2sin²θ - 3sin θ - 2 = 0\n5. 令 u = sin θ：2u² - 3u - 2 = 0\n6. 因式分解：(2u + 1)(u - 2) = 0\n7. 解：u = -1/2 或 u = 2\n8. 因为 -1 ≤ sin θ ≤ 1，只有 u = -1/2 有效\n9. sin θ = -1/2\n10. 基本角：30°（因为 sin 30° = 1/2）\n11. 正弦在第 3 和第 4 象限为负：\n    - 第 3 象限：θ = 180° + 30° = 210°\n    - 第 4 象限：θ = 360° - 30° = 330°\n12. 最小解：210°\n\n**答案：** 210\n\n**常见错误：** 接受 sin θ = 2 为有效（不可能，因为 |sin θ| ≤ 1）。\n\n**提示：** 在求角度之前，总是检查解是否在三角函数的范围内。"
    },
    {
        "id": "trig-id-jc1-ex14",
        "type": "mcq",
        "difficulty": "hard",
        "prompt": "Simplify: (1 - sin θ)(1 + sin θ) / cos²θ.",
        "prompt_zh": "简化：(1 - sin θ)(1 + sin θ) / cos²θ。",
        "choices": [
            "1",
            "sin²θ",
            "tan²θ",
            "sec²θ"
        ],
        "choices_zh": [
            "1",
            "sin²θ",
            "tan²θ",
            "sec²θ"
        ],
        "answer": 0,
        "explanation": "**Problem:** Simplify using difference of squares and Pythagorean identity.\n\n**Key Concept:** (a - b)(a + b) = a² - b² and cos²θ = 1 - sin²θ.\n\n**Steps:**\n1. Numerator: (1 - sin θ)(1 + sin θ) = 1 - sin²θ (difference of squares)\n2. Use identity: 1 - sin²θ = cos²θ\n3. Expression becomes: cos²θ / cos²θ = 1\n\n**Answer:** 1\n\n**Common Mistakes:** Not recognizing the difference of squares pattern in the numerator.\n\n**Tip:** When you see (a - b)(a + b), immediately think a² - b².",
        "explanation_zh": "**问题：** 使用平方差和勾股恒等式简化。\n\n**关键概念：** (a - b)(a + b) = a² - b² 和 cos²θ = 1 - sin²θ。\n\n**步骤：**\n1. 分子：(1 - sin θ)(1 + sin θ) = 1 - sin²θ（平方差）\n2. 使用恒等式：1 - sin²θ = cos²θ\n3. 表达式变为：cos²θ / cos²θ = 1\n\n**答案：** 1\n\n**常见错误：** 没有识别分子中的平方差模式。\n\n**提示：** 当看到 (a - b)(a + b) 时，立即想到 a² - b²。"
    },
    {
        "id": "trig-id-jc1-ex15",
        "type": "mcq",
        "difficulty": "hard",
        "prompt": "Given tan θ = 2 and 180° < θ < 270°, find the exact value of sin θ + cos θ.",
        "prompt_zh": "已知 tan θ = 2 且 180° < θ < 270°，求 sin θ + cos θ 的精确值。",
        "choices": [
            "-3/√5",
            "3/√5",
            "-1/√5",
            "1/√5"
        ],
        "choices_zh": [
            "-3/√5",
            "3/√5",
            "-1/√5",
            "1/√5"
        ],
        "answer": 0,
        "explanation": "**Problem:** Find sin θ and cos θ from tan θ, considering the quadrant.\n\n**Key Concept:** Use tan θ = sin θ / cos θ and sin²θ + cos²θ = 1, checking signs for quadrant 3.\n\n**Steps:**\n1. Given: tan θ = 2 and θ in quadrant 3 (180° < θ < 270°)\n2. In Q3: both sin θ < 0 and cos θ < 0\n3. From tan θ = sin θ / cos θ = 2, we get sin θ = 2cos θ\n4. Substitute into sin²θ + cos²θ = 1:\n   (2cos θ)² + cos²θ = 1\n5. Simplify: 4cos²θ + cos²θ = 1\n6. Therefore: 5cos²θ = 1, so cos²θ = 1/5\n7. Since θ in Q3: cos θ = -1/√5 (negative)\n8. Then: sin θ = 2cos θ = 2(-1/√5) = -2/√5\n9. Sum: sin θ + cos θ = -2/√5 + (-1/√5) = -3/√5\n\n**Answer:** -3/√5\n\n**Common Mistakes:** Forgetting that both sine and cosine are negative in the third quadrant.\n\n**Tip:** Always check the quadrant to determine the correct signs before calculating exact values.",
        "explanation_zh": "**问题：** 从 tan θ 求 sin θ 和 cos θ，考虑象限。\n\n**关键概念：** 使用 tan θ = sin θ / cos θ 和 sin²θ + cos²θ = 1，检查第 3 象限的符号。\n\n**步骤：**\n1. 已知：tan θ = 2 且 θ 在第 3 象限（180° < θ < 270°）\n2. 在第 3 象限：sin θ < 0 和 cos θ < 0\n3. 从 tan θ = sin θ / cos θ = 2，我们得到 sin θ = 2cos θ\n4. 代入 sin²θ + cos²θ = 1：\n   (2cos θ)² + cos²θ = 1\n5. 简化：4cos²θ + cos²θ = 1\n6. 因此：5cos²θ = 1，所以 cos²θ = 1/5\n7. 因为 θ 在第 3 象限：cos θ = -1/√5（负）\n8. 那么：sin θ = 2cos θ = 2(-1/√5) = -2/√5\n9. 和：sin θ + cos θ = -2/√5 + (-1/√5) = -3/√5\n\n**答案：** -3/√5\n\n**常见错误：** 忘记正弦和余弦在第三象限都是负的。\n\n**提示：** 在计算精确值之前，总是检查象限以确定正确的符号。"
    }
]

# Find Chapter 7 and add exercises
for chapter in jc1_chapters:
    if chapter['id'] == 'trigonometric-identities-jc1':
        chapter['exercises'] = chapter_7_exercises
        print(f"✓ Added 15 exercises to Chapter 7: {chapter['title']}")

# Save updated chapters
with open('chapters/jc1_math_chapters.json', 'w', encoding='utf-8') as f:
    json.dump(jc1_chapters, f, ensure_ascii=False, indent=2)

print("\n✓ Chapter 7 exercises saved to chapters/jc1_math_chapters.json")
print(f"Total exercises for Chapter 7: {len(chapter_7_exercises)}")
print("Difficulty distribution: 5 easy, 5 medium, 5 hard")
