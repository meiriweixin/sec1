import json

# Load existing JC 1 chapters
with open('chapters/jc1_math_chapters.json', 'r', encoding='utf-8') as f:
    jc1_chapters = json.load(f)

# Chapter 8: Exponential & Logarithmic Functions - 15 exercises
chapter_8_exercises = [
    # Easy (1-5)
    {
        "id": "exp-log-jc1-ex1",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "Simplify: 2³ × 2⁴",
        "prompt_zh": "简化：2³ × 2⁴",
        "choices": [
            "2⁷",
            "2¹²",
            "4⁷",
            "2¹"
        ],
        "choices_zh": [
            "2⁷",
            "2¹²",
            "4⁷",
            "2¹"
        ],
        "answer": 0,
        "explanation": "**Problem:** Apply the law of indices for multiplication.\n\n**Key Concept:** When multiplying powers with the same base: aᵐ × aⁿ = aᵐ⁺ⁿ\n\n**Steps:**\n1. Identify: Base is 2, exponents are 3 and 4\n2. Apply rule: 2³ × 2⁴ = 2³⁺⁴ = 2⁷\n\n**Answer:** 2⁷\n\n**Common Mistakes:** Multiplying the exponents (getting 2¹²) instead of adding them.\n\n**Tip:** Add exponents when multiplying, multiply exponents when raising a power to a power.",
        "explanation_zh": "**问题：** 应用乘法的指数定律。\n\n**关键概念：** 当乘以相同底数的幂时：aᵐ × aⁿ = aᵐ⁺ⁿ\n\n**步骤：**\n1. 识别：底数是 2，指数是 3 和 4\n2. 应用规则：2³ × 2⁴ = 2³⁺⁴ = 2⁷\n\n**答案：** 2⁷\n\n**常见错误：** 乘以指数（得到 2¹²）而不是加上它们。\n\n**提示：** 乘法时加指数，幂的幂时乘指数。"
    },
    {
        "id": "exp-log-jc1-ex2",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "Evaluate: log₁₀ 1000",
        "prompt_zh": "求值：log₁₀ 1000",
        "choices": [
            "3",
            "10",
            "1000",
            "100"
        ],
        "choices_zh": [
            "3",
            "10",
            "1000",
            "100"
        ],
        "answer": 0,
        "explanation": "**Problem:** Find the logarithm base 10 of 1000.\n\n**Key Concept:** logₐ b = c means aᶜ = b. Ask: \"10 to what power equals 1000?\"\n\n**Steps:**\n1. Question: 10? = 1000\n2. Since 1000 = 10 × 10 × 10 = 10³\n3. Therefore: log₁₀ 1000 = 3\n\n**Answer:** 3\n\n**Common Mistakes:** Confusing the logarithm value with the number itself.\n\n**Tip:** log₁₀ is asking \"how many zeros\" for powers of 10: log₁₀ 10 = 1, log₁₀ 100 = 2, log₁₀ 1000 = 3.",
        "explanation_zh": "**问题：** 求 1000 的以 10 为底的对数。\n\n**关键概念：** logₐ b = c 意味着 aᶜ = b。问：\"10 的什么次方等于 1000？\"\n\n**步骤：**\n1. 问题：10? = 1000\n2. 因为 1000 = 10 × 10 × 10 = 10³\n3. 因此：log₁₀ 1000 = 3\n\n**答案：** 3\n\n**常见错误：** 混淆对数值和数字本身。\n\n**提示：** log₁₀ 问的是\"有多少个零\"对于 10 的幂：log₁₀ 10 = 1，log₁₀ 100 = 2，log₁₀ 1000 = 3。"
    },
    {
        "id": "exp-log-jc1-ex3",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "Solve: 2ˣ = 8",
        "prompt_zh": "求解：2ˣ = 8",
        "choices": [
            "x = 3",
            "x = 4",
            "x = 2",
            "x = 8"
        ],
        "choices_zh": [
            "x = 3",
            "x = 4",
            "x = 2",
            "x = 8"
        ],
        "answer": 0,
        "explanation": "**Problem:** Solve exponential equation by expressing both sides with same base.\n\n**Key Concept:** If aˣ = aʸ, then x = y.\n\n**Steps:**\n1. Express 8 as a power of 2: 8 = 2³\n2. Equation becomes: 2ˣ = 2³\n3. Since bases are equal: x = 3\n\n**Answer:** x = 3\n\n**Common Mistakes:** Dividing both sides by 2 (doesn't work for exponential equations).\n\n**Tip:** Always try to express both sides with the same base first.",
        "explanation_zh": "**问题：** 通过用相同底数表示两边来求解指数方程。\n\n**关键概念：** 如果 aˣ = aʸ，那么 x = y。\n\n**步骤：**\n1. 将 8 表示为 2 的幂：8 = 2³\n2. 方程变为：2ˣ = 2³\n3. 因为底数相等：x = 3\n\n**答案：** x = 3\n\n**常见错误：** 两边除以 2（对指数方程不起作用）。\n\n**提示：** 总是先尝试用相同底数表示两边。"
    },
    {
        "id": "exp-log-jc1-ex4",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "Simplify: log₅ 5",
        "prompt_zh": "简化：log₅ 5",
        "choices": [
            "1",
            "5",
            "0",
            "25"
        ],
        "choices_zh": [
            "1",
            "5",
            "0",
            "25"
        ],
        "answer": 0,
        "explanation": "**Problem:** Apply the identity logₐ a = 1.\n\n**Key Concept:** Any number to the power of 1 equals itself: a¹ = a, so logₐ a = 1.\n\n**Steps:**\n1. Question: 5? = 5\n2. Answer: 5¹ = 5\n3. Therefore: log₅ 5 = 1\n\n**Answer:** 1\n\n**Common Mistakes:** Thinking log₅ 5 = 5 or log₅ 5 = 0.\n\n**Tip:** Universal rule: logₐ a = 1 for any base a > 0, a ≠ 1.",
        "explanation_zh": "**问题：** 应用恒等式 logₐ a = 1。\n\n**关键概念：** 任何数的 1 次方等于自身：a¹ = a，所以 logₐ a = 1。\n\n**步骤：**\n1. 问题：5? = 5\n2. 答案：5¹ = 5\n3. 因此：log₅ 5 = 1\n\n**答案：** 1\n\n**常见错误：** 认为 log₅ 5 = 5 或 log₅ 5 = 0。\n\n**提示：** 通用规则：对于任何底数 a > 0, a ≠ 1，logₐ a = 1。"
    },
    {
        "id": "exp-log-jc1-ex5",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "Express log 50 in terms of log 2 and log 5.",
        "prompt_zh": "用 log 2 和 log 5 表示 log 50。",
        "choices": [
            "2 log 5 + log 2",
            "log 5 + log 2",
            "log 5 × log 2",
            "log 5 - log 2"
        ],
        "choices_zh": [
            "2 log 5 + log 2",
            "log 5 + log 2",
            "log 5 × log 2",
            "log 5 - log 2"
        ],
        "answer": 0,
        "explanation": "**Problem:** Use logarithm laws to expand log 50.\n\n**Key Concept:** log(ab) = log a + log b and log(aⁿ) = n log a.\n\n**Steps:**\n1. Factor 50: 50 = 2 × 25 = 2 × 5²\n2. Apply product rule: log 50 = log(2 × 5²)\n3. Expand: log 50 = log 2 + log(5²)\n4. Apply power rule: log(5²) = 2 log 5\n5. Therefore: log 50 = log 2 + 2 log 5 = 2 log 5 + log 2\n\n**Answer:** 2 log 5 + log 2\n\n**Common Mistakes:** Writing log(a + b) instead of recognizing log(ab) = log a + log b.\n\n**Tip:** Always factor the number first to identify products and powers.",
        "explanation_zh": "**问题：** 使用对数定律展开 log 50。\n\n**关键概念：** log(ab) = log a + log b 和 log(aⁿ) = n log a。\n\n**步骤：**\n1. 因式分解 50：50 = 2 × 25 = 2 × 5²\n2. 应用乘积规则：log 50 = log(2 × 5²)\n3. 展开：log 50 = log 2 + log(5²)\n4. 应用幂规则：log(5²) = 2 log 5\n5. 因此：log 50 = log 2 + 2 log 5 = 2 log 5 + log 2\n\n**答案：** 2 log 5 + log 2\n\n**常见错误：** 写 log(a + b) 而不是识别 log(ab) = log a + log b。\n\n**提示：** 总是先对数字进行因式分解以识别乘积和幂。"
    },

    # Medium (6-10)
    {
        "id": "exp-log-jc1-ex6",
        "type": "mcq",
        "difficulty": "medium",
        "prompt": "Singapore's population growth can be modeled by P = P₀ × 1.02ᵗ, where t is years. How long does it take for the population to double? (Use log 2 ≈ 0.301)",
        "prompt_zh": "新加坡的人口增长可以用 P = P₀ × 1.02ᵗ 建模，其中 t 是年数。人口翻倍需要多长时间？（使用 log 2 ≈ 0.301）",
        "choices": [
            "35 years",
            "50 years",
            "25 years",
            "70 years"
        ],
        "choices_zh": [
            "35 年",
            "50 年",
            "25 年",
            "70 年"
        ],
        "answer": 0,
        "explanation": "**Problem:** Solve 2P₀ = P₀ × 1.02ᵗ for t.\n\n**Key Concept:** Use logarithms to solve exponential equations.\n\n**Steps:**\n1. Equation: 2P₀ = P₀ × 1.02ᵗ\n2. Divide by P₀: 2 = 1.02ᵗ\n3. Take log₁₀ of both sides: log 2 = log(1.02ᵗ)\n4. Apply power rule: log 2 = t × log 1.02\n5. Solve for t: t = (log 2) / (log 1.02)\n6. Calculate: t ≈ 0.301 / 0.0086 ≈ 35 years\n   (Note: log 1.02 ≈ 0.0086)\n\n**Answer:** 35 years\n\n**Common Mistakes:** Dividing 2 by 1.02 instead of using logarithms.\n\n**Tip:** Singapore population growth: 2% annual growth means doubling time ≈ 70/2 = 35 years (Rule of 70).",
        "explanation_zh": "**问题：** 求解 2P₀ = P₀ × 1.02ᵗ 中的 t。\n\n**关键概念：** 使用对数求解指数方程。\n\n**步骤：**\n1. 方程：2P₀ = P₀ × 1.02ᵗ\n2. 除以 P₀：2 = 1.02ᵗ\n3. 两边取 log₁₀：log 2 = log(1.02ᵗ)\n4. 应用幂规则：log 2 = t × log 1.02\n5. 解 t：t = (log 2) / (log 1.02)\n6. 计算：t ≈ 0.301 / 0.0086 ≈ 35 年\n   （注意：log 1.02 ≈ 0.0086）\n\n**答案：** 35 年\n\n**常见错误：** 除以 2 除以 1.02 而不是使用对数。\n\n**提示：** 新加坡人口增长：2% 的年增长率意味着翻倍时间 ≈ 70/2 = 35 年（70 法则）。"
    },
    {
        "id": "exp-log-jc1-ex7",
        "type": "mcq",
        "difficulty": "medium",
        "prompt": "Simplify: log₃ 27 - log₃ 9",
        "prompt_zh": "简化：log₃ 27 - log₃ 9",
        "choices": [
            "1",
            "3",
            "2",
            "0"
        ],
        "choices_zh": [
            "1",
            "3",
            "2",
            "0"
        ],
        "answer": 0,
        "explanation": "**Problem:** Use quotient rule for logarithms.\n\n**Key Concept:** log a - log b = log(a/b)\n\n**Steps:**\n1. Apply quotient rule: log₃ 27 - log₃ 9 = log₃(27/9)\n2. Simplify: log₃(27/9) = log₃ 3\n3. Apply identity: log₃ 3 = 1\n\n**Answer:** 1\n\n**Common Mistakes:** Calculating log₃ 27 = 3 and log₃ 9 = 2 separately, then doing 3 - 2 = 1 (correct answer, but longer method).\n\n**Tip:** Using the quotient rule is faster than evaluating each logarithm separately.",
        "explanation_zh": "**问题：** 使用对数的商规则。\n\n**关键概念：** log a - log b = log(a/b)\n\n**步骤：**\n1. 应用商规则：log₃ 27 - log₃ 9 = log₃(27/9)\n2. 简化：log₃(27/9) = log₃ 3\n3. 应用恒等式：log₃ 3 = 1\n\n**答案：** 1\n\n**常见错误：** 分别计算 log₃ 27 = 3 和 log₃ 9 = 2，然后做 3 - 2 = 1（答案正确，但方法较长）。\n\n**提示：** 使用商规则比分别求每个对数更快。"
    },
    {
        "id": "exp-log-jc1-ex8",
        "type": "mcq",
        "difficulty": "medium",
        "prompt": "Solve: 3²ˣ⁺¹ = 27",
        "prompt_zh": "求解：3²ˣ⁺¹ = 27",
        "choices": [
            "x = 1",
            "x = 2",
            "x = 3",
            "x = 0"
        ],
        "choices_zh": [
            "x = 1",
            "x = 2",
            "x = 3",
            "x = 0"
        ],
        "answer": 0,
        "explanation": "**Problem:** Express both sides with same base and equate exponents.\n\n**Key Concept:** If aᵐ = aⁿ, then m = n.\n\n**Steps:**\n1. Express 27 as power of 3: 27 = 3³\n2. Equation: 3²ˣ⁺¹ = 3³\n3. Equate exponents: 2x + 1 = 3\n4. Solve: 2x = 2, so x = 1\n\n**Answer:** x = 1\n\n**Common Mistakes:** Forgetting to distribute when simplifying 2x + 1.\n\n**Tip:** Verify: When x = 1, 3²⁽¹⁾⁺¹ = 3³ = 27 ✓",
        "explanation_zh": "**问题：** 用相同底数表示两边并等式指数。\n\n**关键概念：** 如果 aᵐ = aⁿ，那么 m = n。\n\n**步骤：**\n1. 将 27 表示为 3 的幂：27 = 3³\n2. 方程：3²ˣ⁺¹ = 3³\n3. 等式指数：2x + 1 = 3\n4. 解：2x = 2，所以 x = 1\n\n**答案：** x = 1\n\n**常见错误：** 简化 2x + 1 时忘记分配。\n\n**提示：** 验证：当 x = 1 时，3²⁽¹⁾⁺¹ = 3³ = 27 ✓"
    },
    {
        "id": "exp-log-jc1-ex9",
        "type": "short",
        "difficulty": "medium",
        "prompt": "Given log₁₀ 2 = 0.301 and log₁₀ 3 = 0.477, find log₁₀ 12. Give answer to 3 decimal places.",
        "prompt_zh": "已知 log₁₀ 2 = 0.301 和 log₁₀ 3 = 0.477，求 log₁₀ 12。答案保留 3 位小数。",
        "answer": "1.079",
        "validator": "numeric",
        "explanation": "**Problem:** Express 12 in terms of 2 and 3, then use logarithm laws.\n\n**Key Concept:** log(ab) = log a + log b and log(aⁿ) = n log a.\n\n**Steps:**\n1. Factor 12: 12 = 4 × 3 = 2² × 3\n2. Apply product rule: log₁₀ 12 = log₁₀(2² × 3)\n3. Expand: log₁₀ 12 = log₁₀(2²) + log₁₀ 3\n4. Apply power rule: log₁₀(2²) = 2 log₁₀ 2\n5. Substitute values: log₁₀ 12 = 2(0.301) + 0.477\n6. Calculate: log₁₀ 12 = 0.602 + 0.477 = 1.079\n\n**Answer:** 1.079\n\n**Common Mistakes:** Trying to calculate log₁₀ 12 directly without using given values.\n\n**Tip:** Always look for ways to express the number using the given logarithm values.",
        "explanation_zh": "**问题：** 用 2 和 3 表示 12，然后使用对数定律。\n\n**关键概念：** log(ab) = log a + log b 和 log(aⁿ) = n log a。\n\n**步骤：**\n1. 因式分解 12：12 = 4 × 3 = 2² × 3\n2. 应用乘积规则：log₁₀ 12 = log₁₀(2² × 3)\n3. 展开：log₁₀ 12 = log₁₀(2²) + log₁₀ 3\n4. 应用幂规则：log₁₀(2²) = 2 log₁₀ 2\n5. 代入值：log₁₀ 12 = 2(0.301) + 0.477\n6. 计算：log₁₀ 12 = 0.602 + 0.477 = 1.079\n\n**答案：** 1.079\n\n**常见错误：** 试图直接计算 log₁₀ 12 而不使用给定的值。\n\n**提示：** 总是寻找使用给定对数值表示数字的方法。"
    },
    {
        "id": "exp-log-jc1-ex10",
        "type": "mcq",
        "difficulty": "medium",
        "prompt": "The Richter scale for earthquakes is defined by M = log₁₀(I/I₀), where I is intensity. If one earthquake measures 6.0 and another measures 8.0, how many times more intense is the second?",
        "prompt_zh": "地震的里氏震级由 M = log₁₀(I/I₀) 定义，其中 I 是强度。如果一次地震测量为 6.0，另一次测量为 8.0，第二次的强度是多少倍？",
        "choices": [
            "100 times",
            "2 times",
            "1000 times",
            "10 times"
        ],
        "choices_zh": [
            "100 倍",
            "2 倍",
            "1000 倍",
            "10 倍"
        ],
        "answer": 0,
        "explanation": "**Problem:** Compare intensities using logarithmic scale.\n\n**Key Concept:** Each unit increase on Richter scale = 10 times intensity increase.\n\n**Steps:**\n1. For M₁ = 6: 6 = log₁₀(I₁/I₀), so I₁ = I₀ × 10⁶\n2. For M₂ = 8: 8 = log₁₀(I₂/I₀), so I₂ = I₀ × 10⁸\n3. Ratio: I₂/I₁ = (I₀ × 10⁸)/(I₀ × 10⁶) = 10⁸⁻⁶ = 10² = 100\n\n**Answer:** 100 times\n\n**Common Mistakes:** Thinking the difference is just 8 - 6 = 2 times.\n\n**Tip:** Logarithmic scales: a difference of 2 means 10² = 100 times more intense.",
        "explanation_zh": "**问题：** 使用对数尺度比较强度。\n\n**关键概念：** 里氏震级每增加一个单位 = 强度增加 10 倍。\n\n**步骤：**\n1. 对于 M₁ = 6：6 = log₁₀(I₁/I₀)，所以 I₁ = I₀ × 10⁶\n2. 对于 M₂ = 8：8 = log₁₀(I₂/I₀)，所以 I₂ = I₀ × 10⁸\n3. 比率：I₂/I₁ = (I₀ × 10⁸)/(I₀ × 10⁶) = 10⁸⁻⁶ = 10² = 100\n\n**答案：** 100 倍\n\n**常见错误：** 认为差异只是 8 - 6 = 2 倍。\n\n**提示：** 对数尺度：差 2 意味着 10² = 100 倍更强。"
    },

    # Hard (11-15)
    {
        "id": "exp-log-jc1-ex11",
        "type": "mcq",
        "difficulty": "hard",
        "prompt": "Solve: 4ˣ - 6(2ˣ) + 8 = 0",
        "prompt_zh": "求解：4ˣ - 6(2ˣ) + 8 = 0",
        "choices": [
            "x = 1 or x = 2",
            "x = 2 only",
            "x = 3 or x = 4",
            "x = 0 or x = 1"
        ],
        "choices_zh": [
            "x = 1 或 x = 2",
            "仅 x = 2",
            "x = 3 或 x = 4",
            "x = 0 或 x = 1"
        ],
        "answer": 0,
        "explanation": "**Problem:** Solve by substitution (let u = 2ˣ).\n\n**Key Concept:** Recognize that 4ˣ = (2²)ˣ = 2²ˣ = (2ˣ)², so this is quadratic in 2ˣ.\n\n**Steps:**\n1. Rewrite: (2ˣ)² - 6(2ˣ) + 8 = 0\n2. Let u = 2ˣ: u² - 6u + 8 = 0\n3. Factor: (u - 2)(u - 4) = 0\n4. Solutions: u = 2 or u = 4\n5. Case 1: 2ˣ = 2 = 2¹, so x = 1\n6. Case 2: 2ˣ = 4 = 2², so x = 2\n\n**Answer:** x = 1 or x = 2\n\n**Common Mistakes:** Not recognizing 4ˣ as (2ˣ)².\n\n**Tip:** When bases are related (4 = 2²), substitution transforms exponential to quadratic.",
        "explanation_zh": "**问题：** 通过替换求解（令 u = 2ˣ）。\n\n**关键概念：** 识别 4ˣ = (2²)ˣ = 2²ˣ = (2ˣ)²，所以这是关于 2ˣ 的二次方程。\n\n**步骤：**\n1. 重写：(2ˣ)² - 6(2ˣ) + 8 = 0\n2. 令 u = 2ˣ：u² - 6u + 8 = 0\n3. 因式分解：(u - 2)(u - 4) = 0\n4. 解：u = 2 或 u = 4\n5. 情况 1：2ˣ = 2 = 2¹，所以 x = 1\n6. 情况 2：2ˣ = 4 = 2²，所以 x = 2\n\n**答案：** x = 1 或 x = 2\n\n**常见错误：** 没有识别 4ˣ 为 (2ˣ)²。\n\n**提示：** 当底数相关时（4 = 2²），替换将指数方程转换为二次方程。"
    },
    {
        "id": "exp-log-jc1-ex12",
        "type": "short",
        "difficulty": "hard",
        "prompt": "A Singapore startup's revenue R (in thousands of dollars) after t years is modeled by R = 50e^(0.3t). After how many years will revenue reach $200,000? Use ln 4 ≈ 1.386. Give answer to 1 decimal place.",
        "prompt_zh": "一家新加坡初创公司的收入 R（以千美元计）在 t 年后由 R = 50e^(0.3t) 建模。收入达到 $200,000 需要多少年？使用 ln 4 ≈ 1.386。答案保留 1 位小数。",
        "answer": "4.6",
        "validator": "numeric",
        "explanation": "**Problem:** Solve 200 = 50e^(0.3t) for t.\n\n**Key Concept:** Use natural logarithm (ln) to solve exponential equations with base e.\n\n**Steps:**\n1. Equation: 200 = 50e^(0.3t)\n2. Divide by 50: 4 = e^(0.3t)\n3. Take ln of both sides: ln 4 = ln(e^(0.3t))\n4. Apply ln(e^x) = x: ln 4 = 0.3t\n5. Solve: t = (ln 4) / 0.3\n6. Calculate: t = 1.386 / 0.3 = 4.62 years\n7. To 1 d.p.: t ≈ 4.6 years\n\n**Answer:** 4.6\n\n**Common Mistakes:** Using log₁₀ instead of ln when base is e.\n\n**Tip:** Singapore startups: Exponential growth models are common for tech companies in the early years.",
        "explanation_zh": "**问题：** 求解 200 = 50e^(0.3t) 中的 t。\n\n**关键概念：** 使用自然对数（ln）求解以 e 为底的指数方程。\n\n**步骤：**\n1. 方程：200 = 50e^(0.3t)\n2. 除以 50：4 = e^(0.3t)\n3. 两边取 ln：ln 4 = ln(e^(0.3t))\n4. 应用 ln(e^x) = x：ln 4 = 0.3t\n5. 解：t = (ln 4) / 0.3\n6. 计算：t = 1.386 / 0.3 = 4.62 年\n7. 保留 1 位小数：t ≈ 4.6 年\n\n**答案：** 4.6\n\n**常见错误：** 当底数为 e 时使用 log₁₀ 而不是 ln。\n\n**提示：** 新加坡初创公司：指数增长模型在早期对科技公司很常见。"
    },
    {
        "id": "exp-log-jc1-ex13",
        "type": "mcq",
        "difficulty": "hard",
        "prompt": "Simplify: log₂(x² - 9) - log₂(x - 3), where x > 3.",
        "prompt_zh": "简化：log₂(x² - 9) - log₂(x - 3)，其中 x > 3。",
        "choices": [
            "log₂(x + 3)",
            "log₂(x² - 3x - 9)",
            "log₂ 6",
            "log₂(x - 3)"
        ],
        "choices_zh": [
            "log₂(x + 3)",
            "log₂(x² - 3x - 9)",
            "log₂ 6",
            "log₂(x - 3)"
        ],
        "answer": 0,
        "explanation": "**Problem:** Use quotient rule and factor the difference of squares.\n\n**Key Concept:** log a - log b = log(a/b) and x² - 9 = (x - 3)(x + 3).\n\n**Steps:**\n1. Apply quotient rule: log₂(x² - 9) - log₂(x - 3) = log₂[(x² - 9)/(x - 3)]\n2. Factor numerator: x² - 9 = (x - 3)(x + 3)\n3. Simplify: [(x - 3)(x + 3)]/(x - 3) = x + 3 (since x ≠ 3)\n4. Therefore: log₂(x + 3)\n\n**Answer:** log₂(x + 3)\n\n**Common Mistakes:** Not factoring x² - 9 before simplifying.\n\n**Tip:** Always look for algebraic simplification opportunities (factoring, canceling) before applying log rules.",
        "explanation_zh": "**问题：** 使用商规则并因式分解平方差。\n\n**关键概念：** log a - log b = log(a/b) 和 x² - 9 = (x - 3)(x + 3)。\n\n**步骤：**\n1. 应用商规则：log₂(x² - 9) - log₂(x - 3) = log₂[(x² - 9)/(x - 3)]\n2. 因式分解分子：x² - 9 = (x - 3)(x + 3)\n3. 简化：[(x - 3)(x + 3)]/(x - 3) = x + 3（因为 x ≠ 3）\n4. 因此：log₂(x + 3)\n\n**答案：** log₂(x + 3)\n\n**常见错误：** 简化前没有因式分解 x² - 9。\n\n**提示：** 在应用对数规则之前，总是寻找代数简化机会（因式分解、消去）。"
    },
    {
        "id": "exp-log-jc1-ex14",
        "type": "mcq",
        "difficulty": "hard",
        "prompt": "Given that log_a x = 3 and log_a y = 5, express log_a(√x / y³) in terms of given values.",
        "prompt_zh": "已知 log_a x = 3 和 log_a y = 5，用给定值表示 log_a(√x / y³)。",
        "choices": [
            "-13.5",
            "1.5",
            "-14",
            "8"
        ],
        "choices_zh": [
            "-13.5",
            "1.5",
            "-14",
            "8"
        ],
        "answer": 0,
        "explanation": "**Problem:** Apply multiple logarithm laws.\n\n**Key Concept:** Use log(a/b) = log a - log b, log(aⁿ) = n log a, and log(√a) = (1/2)log a.\n\n**Steps:**\n1. Rewrite: log_a(√x / y³) = log_a(x^(1/2) / y³)\n2. Apply quotient rule: log_a(x^(1/2)) - log_a(y³)\n3. Apply power rule: (1/2)log_a x - 3 log_a y\n4. Substitute given values: (1/2)(3) - 3(5)\n5. Calculate: 1.5 - 15 = -13.5\n\n**Answer:** -13.5\n\n**Common Mistakes:** Forgetting to apply power rule to both √x and y³.\n\n**Tip:** Work systematically: quotient rule first, then power rule, then substitute.",
        "explanation_zh": "**问题：** 应用多个对数定律。\n\n**关键概念：** 使用 log(a/b) = log a - log b，log(aⁿ) = n log a，和 log(√a) = (1/2)log a。\n\n**步骤：**\n1. 重写：log_a(√x / y³) = log_a(x^(1/2) / y³)\n2. 应用商规则：log_a(x^(1/2)) - log_a(y³)\n3. 应用幂规则：(1/2)log_a x - 3 log_a y\n4. 代入给定值：(1/2)(3) - 3(5)\n5. 计算：1.5 - 15 = -13.5\n\n**答案：** -13.5\n\n**常见错误：** 忘记对 √x 和 y³ 都应用幂规则。\n\n**提示：** 系统地工作：先商规则，然后幂规则，然后代入。"
    },
    {
        "id": "exp-log-jc1-ex15",
        "type": "short",
        "difficulty": "hard",
        "prompt": "Solve for x: log₃(x + 1) + log₃(x - 1) = 1. Give the positive solution.",
        "prompt_zh": "求解 x：log₃(x + 1) + log₃(x - 1) = 1。给出正解。",
        "answer": "2",
        "validator": "numeric",
        "explanation": "**Problem:** Combine logarithms and convert to exponential form.\n\n**Key Concept:** log a + log b = log(ab) and if log_c d = e, then c^e = d.\n\n**Steps:**\n1. Apply product rule: log₃[(x + 1)(x - 1)] = 1\n2. Expand: log₃(x² - 1) = 1\n3. Convert to exponential: 3¹ = x² - 1\n4. Simplify: 3 = x² - 1\n5. Rearrange: x² = 4\n6. Solve: x = ±2\n7. Check domain: x must be > 1 (for x - 1 > 0)\n8. Therefore: x = 2\n\n**Answer:** 2\n\n**Common Mistakes:** Accepting x = -2 without checking the domain (log₃(-2 - 1) is undefined).\n\n**Tip:** ALWAYS check domain restrictions for logarithms: arguments must be positive.",
        "explanation_zh": "**问题：** 合并对数并转换为指数形式。\n\n**关键概念：** log a + log b = log(ab) 和如果 log_c d = e，那么 c^e = d。\n\n**步骤：**\n1. 应用乘积规则：log₃[(x + 1)(x - 1)] = 1\n2. 展开：log₃(x² - 1) = 1\n3. 转换为指数：3¹ = x² - 1\n4. 简化：3 = x² - 1\n5. 重新排列：x² = 4\n6. 解：x = ±2\n7. 检查定义域：x 必须 > 1（对于 x - 1 > 0）\n8. 因此：x = 2\n\n**答案：** 2\n\n**常见错误：** 不检查定义域就接受 x = -2（log₃(-2 - 1) 未定义）。\n\n**提示：** 总是检查对数的定义域限制：参数必须为正。"
    }
]

# Find Chapter 8 and add exercises
for chapter in jc1_chapters:
    if chapter['id'] == 'exponential-logarithmic-jc1':
        chapter['exercises'] = chapter_8_exercises
        print(f"✓ Added 15 exercises to Chapter 8: {chapter['title']}")

# Save updated chapters
with open('chapters/jc1_math_chapters.json', 'w', encoding='utf-8') as f:
    json.dump(jc1_chapters, f, ensure_ascii=False, indent=2)

print("\n✓ Chapter 8 exercises saved to chapters/jc1_math_chapters.json")
print(f"Total exercises for Chapter 8: {len(chapter_8_exercises)}")
print("Difficulty distribution: 5 easy, 5 medium, 5 hard")
print("\n" + "="*60)
print("ALL JC 1 MATHEMATICS EXERCISES COMPLETE!")
print("="*60)
print("Total: 120 exercises across 8 chapters")
print("Next step: Integrate into main content.json")
