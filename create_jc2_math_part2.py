import json

# Load Part 1 chapters
with open('chapters/jc2_math_chapters_part1.json', 'r', encoding='utf-8') as f:
    jc2_chapters = json.load(f)

# Add Part 2 chapters (Statistics and Complex Numbers)
part2_chapters = [
    {
        "id": "permutations-combinations-jc2",
        "title": "Permutations & Combinations",
        "title_zh": "排列与组合",
        "gradeLevel": "jc2",
        "description": "Count arrangements and selections using permutations and combinations",
        "description_zh": "使用排列和组合计数排列和选择",
        "objectives": [
            "Apply permutation formula for arrangements",
            "Use combination formula for selections",
            "Solve problems involving restrictions and repetitions"
        ],
        "objectives_zh": [
            "应用排列公式进行排列",
            "使用组合公式进行选择",
            "解决涉及限制和重复的问题"
        ],
        "sections": [
            {
                "id": "permutations-basics",
                "type": "text",
                "title": "Permutations",
                "title_zh": "排列",
                "content": "**Permutations** count the number of ways to arrange objects where **order matters**.\n\n**Factorial notation:**\nn! = n × (n-1) × (n-2) × ... × 2 × 1\n\nNote: 0! = 1 (by convention)\n\n**Permutation formulas:**\n\n1. **Arranging n different objects:** n!\n\n2. **Arranging r objects from n:** ⁿPᵣ = n!/(n-r)!\n\n3. **Circular permutations:** (n-1)!\n   (Fix one object to avoid overcounting rotations)\n\n4. **Permutations with repetition:**\n   n!/(n₁! × n₂! × ... × nₖ!)\n   where n₁, n₂, ..., nₖ are frequencies of repeated objects\n\n**Example: Singapore MRT line planning**\n\nThe Circle Line has 30 stations. A tourist wants to visit 5 specific stations in a particular order. How many different routes are possible?\n\nThis is ³⁰P₅ = 30!/(30-5)! = 30!/25!\n= 30 × 29 × 28 × 27 × 26\n= 17,100,720 routes\n\n**Circular arrangement example:**\n\nAt a hawker center, 8 people sit around a circular table. How many seating arrangements?\n\n(8-1)! = 7! = 5,040 arrangements\n\n(We fix one person's position to account for rotational symmetry)\n\n**With repetition:**\n\nThe word SINGAPORE has 9 letters with repetitions (2 S's, 2 A's, others unique).\n\nArrangements = 9!/(2! × 2!) = 362,880/4 = 90,720"
            },
            {
                "id": "combinations-basics",
                "type": "text",
                "title": "Combinations",
                "title_zh": "组合",
                "content": "**Combinations** count the number of ways to select objects where **order does not matter**.\n\n**Combination formula:**\nⁿCᵣ = n!/[r!(n-r)!]\n\nAlso written as: (n choose r) or C(n,r)\n\n**Properties:**\n1. ⁿCᵣ = ⁿCₙ₋ᵣ (symmetry)\n2. ⁿC₀ = ⁿCₙ = 1\n3. ⁿC₁ = n\n4. ⁿCᵣ + ⁿCᵣ₋₁ = ⁿ⁺¹Cᵣ (Pascal's identity)\n\n**Permutations vs Combinations:**\n- **Permutation:** Order matters (arranging, ranking)\n- **Combination:** Order doesn't matter (selecting, choosing)\n\n**Example: Singapore National Service selection**\n\nFrom a platoon of 20 recruits, 3 must be selected for a special assignment. How many ways can this be done?\n\nSince order doesn't matter (all 3 have equal roles):\n²⁰C₃ = 20!/(3! × 17!)\n= (20 × 19 × 18)/(3 × 2 × 1)\n= 6,840/6\n= 1,140 ways\n\n**Example: HDB flat selection**\n\nA family applying for a Build-To-Order (BTO) flat in Punggol can choose from 12 different unit types. They need to rank their top 5 preferences.\n\n- **If order matters** (1st choice vs 5th choice): ¹²P₅ = 95,040\n- **If order doesn't matter** (just selecting 5): ¹²C₅ = 792\n\nHDB uses the ranking system, so ¹²P₅ is correct.\n\n**Committee selection:**\n\nA school needs to form a 4-person committee from 15 teachers. How many committees possible?\n\n¹⁵C₄ = 15!/(4! × 11!) = 1,365 committees"
            },
            {
                "id": "restrictions-problems",
                "type": "text",
                "title": "Problems with Restrictions",
                "title_zh": "有限制条件的问题",
                "content": "**Restriction problems** require careful case analysis or complementary counting.\n\n**Common strategies:**\n\n1. **Fix the restricted elements first**\n2. **Use complementary counting:** Total - Unwanted\n3. **Break into cases**\n4. **Treat restricted elements as a single unit**\n\n**Example 1: Singapore ethnic representation**\n\nA 5-member committee must include at least 2 Malay members from a group of 4 Malay and 8 non-Malay candidates.\n\n**Method 1: Case analysis**\n- Case 1: Exactly 2 Malay: ⁴C₂ × ⁸C₃ = 6 × 56 = 336\n- Case 2: Exactly 3 Malay: ⁴C₃ × ⁸C₂ = 4 × 28 = 112\n- Case 3: Exactly 4 Malay: ⁴C₄ × ⁸C₁ = 1 × 8 = 8\n\nTotal: 336 + 112 + 8 = 456 ways\n\n**Method 2: Complementary counting**\nTotal committees: ¹²C₅ = 792\n\nUnwanted (0 or 1 Malay):\n- 0 Malay: ⁴C₀ × ⁸C₅ = 1 × 56 = 56\n- 1 Malay: ⁴C₁ × ⁸C₄ = 4 × 70 = 280\n\nUnwanted total: 56 + 280 = 336\n\nAnswer: 792 - 336 = 456 ways ✓\n\n**Example 2: Seating restrictions**\n\nAt Singapore's National Day Parade, 6 VIPs must be seated in a row. The President and Prime Minister must NOT sit together.\n\n**Total arrangements:** 6! = 720\n\n**Unwanted (President and PM together):**\nTreat them as one unit: 2! × 5! = 2 × 120 = 240\n\n**Answer:** 720 - 240 = 480 arrangements\n\n**Example 3: Car plate numbers**\n\nSingapore car plates have format: SXX####X\n(S=letter, X=letter or digit, #=digit)\n\nHow many plates possible if first letter cannot be I, O, or Q (to avoid confusion)?\n\nFirst letter: 26 - 3 = 23 choices\nNext 2 characters: 36 choices each (26 letters + 10 digits)\nFour digits: 10 choices each\nLast character: 36 choices\n\nTotal: 23 × 36 × 36 × 10⁴ × 36\n= 23 × 36³ × 10⁴\n= 1,072,224,000 possible plates"
            }
        ],
        "exercises": []
    },
    {
        "id": "probability-distributions-jc2",
        "title": "Probability & Distributions",
        "title_zh": "概率与分布",
        "gradeLevel": "jc2",
        "description": "Apply probability rules and work with discrete probability distributions including binomial",
        "description_zh": "应用概率规则并处理包括二项分布在内的离散概率分布",
        "objectives": [
            "Calculate probabilities using addition and multiplication rules",
            "Apply conditional probability and Bayes' theorem",
            "Work with binomial distribution for repeated trials"
        ],
        "objectives_zh": [
            "使用加法和乘法规则计算概率",
            "应用条件概率和贝叶斯定理",
            "处理重复试验的二项分布"
        ],
        "sections": [
            {
                "id": "probability-rules",
                "type": "text",
                "title": "Fundamental Probability Rules",
                "title_zh": "基本概率规则",
                "content": "**Probability** measures the likelihood of an event occurring, ranging from 0 (impossible) to 1 (certain).\n\n**Basic rules:**\n\n1. **Addition Rule** (for mutually exclusive events):\n   P(A ∪ B) = P(A) + P(B)\n\n2. **General Addition Rule:**\n   P(A ∪ B) = P(A) + P(B) - P(A ∩ B)\n\n3. **Multiplication Rule** (for independent events):\n   P(A ∩ B) = P(A) × P(B)\n\n4. **Complement Rule:**\n   P(A') = 1 - P(A)\n\n**Conditional Probability:**\nP(A|B) = P(A ∩ B) / P(B)\n\nReads as: \"Probability of A given B\"\n\n**Example: Singapore COVID-19 testing (2020)**\n\nDuring the pandemic, Singapore implemented widespread testing:\n- 2% of population actually infected (prevalence)\n- Test sensitivity: 95% (correctly identifies infected)\n- Test specificity: 98% (correctly identifies healthy)\n\nIf someone tests positive, what's the probability they're actually infected?\n\nLet I = infected, T+ = tests positive\n\nGiven:\n- P(I) = 0.02, so P(I') = 0.98\n- P(T+|I) = 0.95 (sensitivity)\n- P(T+|I') = 0.02 (false positive rate = 1 - specificity)\n\nUsing law of total probability:\nP(T+) = P(T+|I)P(I) + P(T+|I')P(I')\n= 0.95(0.02) + 0.02(0.98)\n= 0.019 + 0.0196\n= 0.0386\n\nUsing Bayes' theorem:\nP(I|T+) = P(T+|I)P(I) / P(T+)\n= (0.95 × 0.02) / 0.0386\n= 0.019 / 0.0386\n≈ 0.492 or 49.2%\n\nThis counterintuitive result (only ~50% chance despite positive test!) occurred because of low prevalence, highlighting why Singapore used multiple confirmatory tests."
            },
            {
                "id": "binomial-distribution",
                "type": "text",
                "title": "Binomial Distribution",
                "title_zh": "二项分布",
                "content": "**Binomial distribution** models the number of successes in n independent trials, each with probability p of success.\n\n**Requirements:**\n1. Fixed number of trials (n)\n2. Each trial has two outcomes (success/failure)\n3. Probability of success (p) is constant\n4. Trials are independent\n\n**Notation:** X ~ B(n, p)\n\n**Probability mass function:**\nP(X = r) = ⁿCᵣ × p^r × (1-p)^(n-r)\n\n**Mean:** E(X) = np\n**Variance:** Var(X) = np(1-p)\n**Standard deviation:** σ = √[np(1-p)]\n\n**Example: Singapore ERP gantry system**\n\nElectronic Road Pricing (ERP) gantries charge vehicles during peak hours. Suppose 30% of vehicles passing through Orchard Road gantry are taxis.\n\nIn a sample of 10 vehicles, find:\n\na) **Probability exactly 3 are taxis:**\n\nX ~ B(10, 0.3)\n\nP(X = 3) = ¹⁰C₃ × (0.3)³ × (0.7)⁷\n= 120 × 0.027 × 0.0824\n= 0.2668 or 26.68%\n\nb) **Probability at least 2 are taxis:**\n\nP(X ≥ 2) = 1 - P(X < 2)\n= 1 - [P(X=0) + P(X=1)]\n\nP(X=0) = (0.7)¹⁰ = 0.0282\nP(X=1) = 10 × 0.3 × (0.7)⁹ = 0.1211\n\nP(X ≥ 2) = 1 - (0.0282 + 0.1211) = 0.8507 or 85.07%\n\nc) **Expected number of taxis:**\n\nE(X) = np = 10 × 0.3 = 3 taxis\n\n**Example: Singapore rainy days**\n\nHistorically, Singapore experiences rain on 40% of days. In a week (7 days), find the probability of exactly 3 rainy days:\n\nX ~ B(7, 0.4)\n\nP(X = 3) = ⁷C₃ × (0.4)³ × (0.6)⁴\n= 35 × 0.064 × 0.1296\n= 0.2903 or 29.03%\n\nThe National Environment Agency (NEA) uses binomial models for short-term weather forecasting and water resource planning."
            },
            {
                "id": "expectation-variance",
                "type": "text",
                "title": "Expectation and Variance",
                "title_zh": "期望与方差",
                "content": "**Expectation** (mean) represents the long-run average value. **Variance** measures spread around the mean.\n\n**Discrete random variable:**\n\nExpectation: E(X) = μ = Σ xᵢP(X = xᵢ)\n\nVariance: Var(X) = σ² = E(X²) - [E(X)]²\n\nwhere E(X²) = Σ xᵢ²P(X = xᵢ)\n\nStandard deviation: σ = √Var(X)\n\n**Properties:**\n1. E(aX + b) = aE(X) + b\n2. Var(aX + b) = a²Var(X)\n3. If X and Y independent: E(X + Y) = E(X) + E(Y)\n4. If X and Y independent: Var(X + Y) = Var(X) + Var(Y)\n\n**Example: Singapore 4D lottery**\n\nIn Singapore's 4D lottery, you pay $1 to bet on a 4-digit number (0000-9999).\n\nPrize structure:\n- 1st prize: $2,000 (probability: 1/10,000)\n- 2nd prize: $1,000 (probability: 1/10,000)\n- 3rd prize: $500 (probability: 1/10,000)\n- Starter: $250 (probability: 10/10,000)\n- Consolation: $60 (probability: 10/10,000)\n- No prize: $0 (probability: 9,977/10,000)\n\n**Expected winnings:**\n\nE(X) = 2000(1/10,000) + 1000(1/10,000) + 500(1/10,000) + 250(10/10,000) + 60(10/10,000) + 0(9,977/10,000)\n\n= 0.20 + 0.10 + 0.05 + 0.25 + 0.06 + 0\n= $0.66\n\n**Expected profit** = E(X) - cost = $0.66 - $1 = -$0.34\n\nOn average, you lose $0.34 per $1 bet. This demonstrates why lotteries are profitable for operators!\n\n**Example: Singapore Grab rides**\n\nA Grab driver's daily earnings X has probability distribution:\n\n| Earnings ($) | 100 | 150 | 200 | 250 |\n|-------------|-----|-----|-----|-----|\n| P(X = x)    | 0.2 | 0.3 | 0.4 | 0.1 |\n\n**Calculate expectation:**\n\nE(X) = 100(0.2) + 150(0.3) + 200(0.4) + 250(0.1)\n= 20 + 45 + 80 + 25\n= $170 per day\n\n**Calculate variance:**\n\nE(X²) = 100²(0.2) + 150²(0.3) + 200²(0.4) + 250²(0.1)\n= 2,000 + 6,750 + 16,000 + 6,250\n= 31,000\n\nVar(X) = 31,000 - 170² = 31,000 - 28,900 = 2,100\n\nσ = √2,100 ≈ $45.83\n\nThis means typical daily earnings vary by about ±$46 from the mean of $170, helping drivers plan their finances and Grab optimize pricing."
            }
        ],
        "exercises": []
    },
    {
        "id": "sampling-hypothesis-testing-jc2",
        "title": "Sampling & Hypothesis Testing",
        "title_zh": "抽样与假设检验",
        "gradeLevel": "jc2",
        "description": "Understand sampling distributions and perform hypothesis tests for population parameters",
        "description_zh": "理解抽样分布并对总体参数进行假设检验",
        "objectives": [
            "Apply the Central Limit Theorem to sampling distributions",
            "Construct confidence intervals for population mean",
            "Perform hypothesis tests for population mean and proportion"
        ],
        "objectives_zh": [
            "应用中心极限定理于抽样分布",
            "构建总体均值的置信区间",
            "对总体均值和比例进行假设检验"
        ],
        "sections": [
            {
                "id": "sampling-distributions",
                "type": "text",
                "title": "Sampling Distributions & Central Limit Theorem",
                "title_zh": "抽样分布与中心极限定理",
                "content": "**Sampling distribution** describes how sample statistics vary across different samples from the same population.\n\n**Central Limit Theorem (CLT):**\nFor large sample size n (typically n ≥ 30), the sampling distribution of sample mean X̄ is approximately normal:\n\nX̄ ~ N(μ, σ²/n)\n\nwhere μ = population mean, σ = population standard deviation\n\n**Standard error:** SE = σ/√n\n\n**Z-score for sample mean:**\nZ = (X̄ - μ) / (σ/√n)\n\n**Key insights:**\n1. Larger samples → smaller standard error → more precise estimates\n2. CLT applies regardless of population distribution (if n large enough)\n3. Sample size matters more than population size\n\n**Example: Singapore HDB resale prices**\n\nHDB 4-room flats in Tampines have mean resale price μ = $450,000 with standard deviation σ = $60,000.\n\nIf we sample 36 recent transactions, find probability that sample mean exceeds $465,000.\n\nn = 36 (≥30, so CLT applies)\n\nX̄ ~ N(450,000, 60,000²/36)\nX̄ ~ N(450,000, 100,000,000)\n\nStandard error: SE = 60,000/√36 = $10,000\n\nP(X̄ > 465,000) = P(Z > (465,000 - 450,000)/10,000)\n= P(Z > 1.5)\n= 1 - Φ(1.5)\n= 1 - 0.9332\n= 0.0668 or 6.68%\n\nThis helps HDB and property analysts detect unusual market trends that might require policy intervention.\n\n**Example: Singapore's workforce**\n\nMonthly salaries of IT professionals in Singapore: μ = $6,500, σ = $1,200.\n\nIn a sample of 64 IT professionals, what's the probability the sample mean salary is between $6,300 and $6,700?\n\nSE = 1,200/√64 = $150\n\nZ₁ = (6,300 - 6,500)/150 = -1.33\nZ₂ = (6,700 - 6,500)/150 = 1.33\n\nP(6,300 < X̄ < 6,700) = P(-1.33 < Z < 1.33)\n= Φ(1.33) - Φ(-1.33)\n= 0.9082 - 0.0918\n= 0.8164 or 81.64%\n\nThe Ministry of Manpower (MOM) uses such calculations for labor market surveys and salary benchmarking."
            },
            {
                "id": "confidence-intervals",
                "type": "text",
                "title": "Confidence Intervals",
                "title_zh": "置信区间",
                "content": "**Confidence interval** provides a range of plausible values for a population parameter.\n\n**For population mean μ (known σ):**\n\nX̄ ± z* × (σ/√n)\n\nwhere z* is the critical value:\n- 90% confidence: z* = 1.645\n- 95% confidence: z* = 1.96\n- 99% confidence: z* = 2.576\n\n**Interpretation:**\nWe are [C%] confident that the true population mean μ lies within the interval.\n\n**Margin of error:** E = z* × (σ/√n)\n\n**Sample size needed** for margin of error E:\nn = (z*σ/E)²\n\n**Example: Singapore commute times**\n\nA survey of 100 Singaporean workers found mean commute time X̄ = 45 minutes. Historical data shows σ = 12 minutes.\n\nConstruct a 95% confidence interval for μ:\n\nn = 100, X̄ = 45, σ = 12, z* = 1.96\n\nSE = 12/√100 = 1.2\n\nMargin of error: E = 1.96 × 1.2 = 2.352\n\nCI: 45 ± 2.352 = (42.648, 47.352) minutes\n\n**Interpretation:** We are 95% confident that the true mean commute time for all Singaporean workers is between 42.6 and 47.4 minutes.\n\nThe Land Transport Authority (LTA) uses such estimates to:\n- Plan MRT expansions\n- Set bus frequency targets\n- Design park-and-ride facilities\n\n**Example: Singapore voter survey**\n\nBefore an election, a poll of 1,000 voters finds 540 support a particular policy.\n\n**For population proportion p:**\n\nSample proportion: p̂ = 540/1,000 = 0.54\n\nStandard error: SE = √[p̂(1-p̂)/n] = √[0.54(0.46)/1,000] = 0.0158\n\n95% CI: p̂ ± 1.96(SE)\n= 0.54 ± 1.96(0.0158)\n= 0.54 ± 0.031\n= (0.509, 0.571) or (50.9%, 57.1%)\n\n**Interpretation:** We are 95% confident that between 50.9% and 57.1% of all voters support the policy.\n\n**How large a sample for margin of error ±2%?**\n\nE = 0.02, z* = 1.96, assume p̂ ≈ 0.5 (most conservative)\n\nn = (1.96)² × 0.5 × 0.5 / (0.02)²\n= 3.8416 × 0.25 / 0.0004\n= 2,401 voters\n\nThis explains why major political polls in Singapore typically survey 2,000-2,500 people to achieve acceptable precision."
            },
            {
                "id": "hypothesis-testing",
                "type": "text",
                "title": "Hypothesis Testing",
                "title_zh": "假设检验",
                "content": "**Hypothesis testing** determines whether sample data provides sufficient evidence to reject a claim about a population parameter.\n\n**Steps:**\n1. State hypotheses: H₀ (null) and H₁ (alternative)\n2. Choose significance level α (usually 0.05 or 0.01)\n3. Calculate test statistic\n4. Find p-value or compare to critical value\n5. Make decision and state conclusion\n\n**For population mean μ (known σ):**\n\nTest statistic: Z = (X̄ - μ₀) / (σ/√n)\n\n**Types of tests:**\n- **Two-tailed:** H₁: μ ≠ μ₀ (test both directions)\n- **Left-tailed:** H₁: μ < μ₀ (test if less than)\n- **Right-tailed:** H₁: μ > μ₀ (test if greater than)\n\n**Decision rules:**\n- If p-value < α: Reject H₀\n- If p-value ≥ α: Do not reject H₀\n\n**Type I error:** Rejecting H₀ when it's true (probability = α)\n**Type II error:** Failing to reject H₀ when it's false\n\n**Example: Singapore water quality**\n\nPUB claims that NEWater has mean pH of 7.0. A lab tests 40 samples and finds X̄ = 7.15 with known σ = 0.4.\n\nTest at α = 0.05 if the mean pH differs from 7.0.\n\n**Step 1: Hypotheses**\nH₀: μ = 7.0 (PUB's claim is correct)\nH₁: μ ≠ 7.0 (two-tailed test)\n\n**Step 2:** α = 0.05, so critical values: ±1.96\n\n**Step 3: Test statistic**\nZ = (7.15 - 7.0) / (0.4/√40)\n= 0.15 / 0.0632\n= 2.37\n\n**Step 4: P-value**\np = 2 × P(Z > 2.37) = 2 × (1 - 0.9911) = 2 × 0.0089 = 0.0178\n\n**Step 5: Decision**\nSince p = 0.0178 < 0.05, reject H₀.\n\n**Conclusion:** There is sufficient evidence at 5% significance level to conclude that the mean pH differs from 7.0. PUB should investigate.\n\n**Example: Singapore Covid-19 vaccine effectiveness**\n\nBefore vaccination program, 8% of tested individuals were positive. After 3 months of vaccination, in a sample of 500 tests, 30 were positive.\n\nTest if the proportion has decreased (α = 0.01).\n\n**Step 1:**\nH₀: p = 0.08 (no decrease)\nH₁: p < 0.08 (left-tailed: proportion decreased)\n\n**Step 2:** α = 0.01, critical value: -2.33\n\n**Step 3:**\nSample proportion: p̂ = 30/500 = 0.06\n\nTest statistic:\nZ = (0.06 - 0.08) / √[0.08(0.92)/500]\n= -0.02 / 0.0121\n= -1.65\n\n**Step 4:**\np-value = P(Z < -1.65) = 0.0495\n\n**Step 5:**\nSince p = 0.0495 > 0.01, do not reject H₀.\n\n**Conclusion:** At 1% significance level, there is insufficient evidence to conclude that the infection rate has decreased. More data needed or use less stringent α = 0.05 level."
            }
        ],
        "exercises": []
    },
    {
        "id": "complex-numbers-jc2",
        "title": "Complex Numbers",
        "title_zh": "复数",
        "gradeLevel": "jc2",
        "description": "Perform operations with complex numbers and apply them to solve polynomial equations",
        "description_zh": "对复数进行运算并应用于求解多项式方程",
        "objectives": [
            "Perform arithmetic operations with complex numbers",
            "Convert between Cartesian and polar forms",
            "Apply De Moivre's theorem for powers and roots"
        ],
        "objectives_zh": [
            "对复数进行算术运算",
            "在直角坐标形式和极坐标形式之间转换",
            "应用棣莫弗定理求幂和根"
        ],
        "sections": [
            {
                "id": "complex-basics",
                "type": "text",
                "title": "Complex Number Basics",
                "title_zh": "复数基础",
                "content": "**Complex numbers** extend the real number system to include solutions to equations like x² + 1 = 0.\n\n**Imaginary unit:** i = √(-1), so i² = -1\n\n**Standard form:** z = a + bi\n- a is the **real part**: Re(z)\n- b is the **imaginary part**: Im(z)\n\n**Special cases:**\n- Real number: b = 0 (z = a)\n- Pure imaginary: a = 0 (z = bi)\n- Zero: a = b = 0\n\n**Complex conjugate:** If z = a + bi, then z̄ = a - bi\n\n**Properties of conjugates:**\n1. z + z̄ = 2a (real)\n2. z - z̄ = 2bi (pure imaginary)\n3. z × z̄ = a² + b² (real, always ≥ 0)\n4. (z̄)̄ = z\n\n**Operations:**\n\n**Addition:** (a + bi) + (c + di) = (a + c) + (b + d)i\n\n**Subtraction:** (a + bi) - (c + di) = (a - c) + (b - d)i\n\n**Multiplication:**\n(a + bi)(c + di) = ac + adi + bci + bdi²\n= ac + (ad + bc)i + bd(-1)\n= (ac - bd) + (ad + bc)i\n\n**Division:** Multiply numerator and denominator by conjugate of denominator\n\n(a + bi)/(c + di) = (a + bi)(c - di) / [(c + di)(c - di)]\n= [(ac + bd) + (bc - ad)i] / (c² + d²)\n\n**Example: Singapore electrical engineering**\n\nIn AC circuits, impedance Z combines resistance R and reactance X:\n\nZ = R + Xi\n\nFor a Singapore power grid component with Z₁ = 50 + 30i ohms and Z₂ = 40 - 20i ohms:\n\n**Total impedance (series):**\nZ_total = Z₁ + Z₂ = (50 + 40) + (30 - 20)i = 90 + 10i ohms\n\n**Parallel combination** (1/Z_total = 1/Z₁ + 1/Z₂):\n\nFirst find 1/Z₁:\n1/(50 + 30i) = (50 - 30i) / [(50 + 30i)(50 - 30i)]\n= (50 - 30i) / (2500 + 900)\n= (50 - 30i) / 3400\n\nSP Power Grid engineers use complex number calculations for designing efficient power distribution networks across Singapore."
            },
            {
                "id": "argand-polar",
                "type": "text",
                "title": "Argand Diagram & Polar Form",
                "title_zh": "阿根图与极坐标形式",
                "content": "**Argand diagram** represents complex numbers geometrically, with real axis (horizontal) and imaginary axis (vertical).\n\nPoint z = a + bi is plotted at coordinates (a, b).\n\n**Modulus** (distance from origin):\n|z| = √(a² + b²)\n\n**Argument** (angle from positive real axis):\narg(z) = θ = arctan(b/a)\n\nNote: Adjust θ based on quadrant!\n\n**Polar form:** z = r(cos θ + i sin θ)\n\nwhere r = |z| and θ = arg(z)\n\n**Exponential form:** z = re^(iθ)\n\n**Euler's formula:** e^(iθ) = cos θ + i sin θ\n\n**Properties:**\n1. |z₁z₂| = |z₁| × |z₂|\n2. arg(z₁z₂) = arg(z₁) + arg(z₂)\n3. |z₁/z₂| = |z₁| / |z₂|\n4. arg(z₁/z₂) = arg(z₁) - arg(z₂)\n\n**Example: Singapore GPS navigation**\n\nA ship's displacement from Marina Bay can be represented as a complex number.\n\nIf z = 3 + 4i km (3 km east, 4 km north):\n\n**Modulus (distance):**\n|z| = √(3² + 4²) = √(9 + 16) = 5 km\n\n**Argument (bearing from east):**\narg(z) = arctan(4/3) ≈ 53.13° or 0.927 radians\n\n**Polar form:**\nz = 5(cos 53.13° + i sin 53.13°)\n= 5e^(0.927i)\n\n**Example: Singapore telecommunications**\n\nSignal processing for 5G networks uses complex phasors.\n\nConvert z = -1 - √3 i to polar form:\n\n|z| = √(1 + 3) = 2\n\nSince z is in third quadrant:\narg(z) = π + arctan(√3/1) = π + π/3 = 4π/3\n\nPolar form: z = 2[cos(4π/3) + i sin(4π/3)]\n= 2e^(i4π/3)\n\nSingapore Telecommunications (SingTel) and other telecom companies use complex number analysis for optimizing signal strength and reducing interference in dense urban environments like Orchard Road and Marina Bay."
            },
            {
                "id": "de-moivre-theorem",
                "type": "text",
                "title": "De Moivre's Theorem",
                "title_zh": "棣莫弗定理",
                "content": "**De Moivre's Theorem** provides an efficient way to raise complex numbers to integer powers.\n\n**Theorem:**\nIf z = r(cos θ + i sin θ), then:\n\nz^n = r^n(cos nθ + i sin nθ)\n\nOr in exponential form: (re^(iθ))^n = r^n e^(inθ)\n\n**Applications:**\n1. Computing powers of complex numbers\n2. Finding nth roots of complex numbers\n3. Deriving trigonometric identities\n\n**nth roots of complex number:**\n\nIf w = r(cos θ + i sin θ), then the n distinct nth roots are:\n\nz_k = r^(1/n) [cos((θ + 2πk)/n) + i sin((θ + 2πk)/n)]\n\nfor k = 0, 1, 2, ..., n-1\n\n**Example: Singapore structural engineering**\n\nFind (1 + i)⁸:\n\nFirst convert to polar:\n|1 + i| = √2\narg(1 + i) = π/4\n\nSo: 1 + i = √2(cos π/4 + i sin π/4)\n\nApply De Moivre:\n(1 + i)⁸ = (√2)⁸[cos(8π/4) + i sin(8π/4)]\n= 16[cos 2π + i sin 2π]\n= 16[1 + 0i]\n= 16\n\n**Example: Finding cube roots of unity**\n\nSolve z³ = 1:\n\n1 = 1(cos 0 + i sin 0)\n\nThe three cube roots are:\n\nk=0: z₀ = 1^(1/3)[cos(0/3) + i sin(0/3)] = 1\n\nk=1: z₁ = 1^(1/3)[cos(2π/3) + i sin(2π/3)]\n= cos 120° + i sin 120°\n= -1/2 + (√3/2)i\n\nk=2: z₂ = 1^(1/3)[cos(4π/3) + i sin(4π/3)]\n= cos 240° + i sin 240°\n= -1/2 - (√3/2)i\n\n**Verification:** These three roots form an equilateral triangle on the Argand diagram, equally spaced at 120° intervals.\n\n**Singapore application: Architectural design**\n\nThe iconic **ArtScience Museum** lotus design uses rotational symmetry principles related to roots of unity. The 10 \"petals\" are positioned at equal angular intervals:\n\nθ_k = 2πk/10 for k = 0, 1, ..., 9\n\nEach petal position can be represented as:\nz_k = e^(i2πk/10)\n\nThis ensures perfect rotational symmetry, crucial for structural balance and aesthetic appeal. Architects at Moshe Safdie's firm used complex number calculations to optimize the building's unique geometry."
            }
        ],
        "exercises": []
    }
]

# Combine Part 1 and Part 2
jc2_chapters.extend(part2_chapters)

# Save combined chapters
with open('chapters/jc2_math_chapters.json', 'w', encoding='utf-8') as f:
    json.dump(jc2_chapters, f, ensure_ascii=False, indent=2)

print("✓ Created all JC 2 Mathematics chapters")
print(f"  - Total chapters: {len(jc2_chapters)}")
print(f"  - Total sections: {sum(len(ch['sections']) for ch in jc2_chapters)}")
print("\nChapters created:")
for i, ch in enumerate(jc2_chapters, 1):
    print(f"  {i}. {ch['title']} ({len(ch['sections'])} sections)")
print("\n" + "="*60)
print("JC 2 CHAPTERS COMPLETE!")
print("="*60)
print("Next step: Create exercises (120 total, 15 per chapter)")
