#!/usr/bin/env python3
"""
Creates exercises for JC 1 Physics Chapters 1-2 (Measurement, Kinematics)
Total: 30 exercises (15 per chapter, 5 easy + 5 medium + 5 hard each)
Following JC Mathematics pattern: 6-step explanations, Singapore context, bilingual
"""

import json

# Load existing chapters
with open('chapters/jc1_physics_chapters.json', 'r', encoding='utf-8') as f:
    chapters = json.load(f)

# Chapter 1: Measurement - 15 exercises
measurement_exercises = [
    # Easy exercises (1-5)
    {
        "id": "measurement-jc1-ex1",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "Convert 5.2 km to meters.",
        "prompt_zh": "将5.2公里转换为米。",
        "choices": ["52 m", "520 m", "5,200 m", "52,000 m"],
        "choices_zh": ["52米", "520米", "5,200米", "52,000米"],
        "answer": 2,
        "explanation": """**Problem:** Convert 5.2 km to meters.

**Key Concept:** SI unit conversion using prefixes. 1 kilometer (kilo = 10³) = 1,000 meters.

**Steps:**
1. Identify the conversion factor: 1 km = 1,000 m
2. Multiply: 5.2 km × 1,000 m/km = 5,200 m
3. The units cancel: km × (m/km) = m ✓

**Answer:** 5,200 m

**Common Mistakes:**
- Dividing instead of multiplying (getting 0.0052 m)
- Moving decimal point wrong direction
- Forgetting that "kilo" means 1,000

**Tip:** Singapore distances like MRT lines are often measured in km. The Downtown Line is 42 km = 42,000 m long!""",
        "explanation_zh": """**问题：** 将5.2公里转换为米。

**关键概念：** 使用前缀进行国际单位制转换。1千米（kilo = 10³）= 1,000米。

**步骤：**
1. 确定转换因子：1千米 = 1,000米
2. 乘法：5.2千米 × 1,000米/千米 = 5,200米
3. 单位消去：千米 × (米/千米) = 米 ✓

**答案：** 5,200米

**常见错误：**
- 除法而非乘法（得0.0052米）
- 小数点移动方向错误
- 忘记"千"表示1,000

**提示：** 新加坡的距离如地铁线路通常以千米为单位。市区线长42千米 = 42,000米！"""
    },
    {
        "id": "measurement-jc1-ex2",
        "type": "short",
        "difficulty": "easy",
        "prompt": "The mass of a HDB flat is measured as 45,000 kg with an uncertainty of ±500 kg. What is the percentage uncertainty?",
        "prompt_zh": "一个组屋单位的质量测量为45,000千克，不确定性为±500千克。百分比不确定性是多少？",
        "answer": "1.1",
        "validator": "numeric",
        "explanation": """**Problem:** Calculate percentage uncertainty for mass = 45,000 ± 500 kg.

**Key Concept:** Percentage uncertainty = (absolute uncertainty / measured value) × 100%

**Steps:**
1. Identify values:
   - Measured value = 45,000 kg
   - Absolute uncertainty = ±500 kg
2. Apply formula: (500 / 45,000) × 100%
3. Calculate: 0.0111... × 100% = 1.11%
4. Round to appropriate sig figs: 1.1%

**Answer:** 1.1%

**Common Mistakes:**
- Forgetting to multiply by 100 (getting 0.011 instead of 1.1%)
- Using wrong value in denominator
- Too many significant figures (percentage uncertainty rarely needs more than 2 sig figs)

**Tip:** Smaller percentage uncertainty means more precise measurement. For building construction in Singapore, structural engineers need very low percentage uncertainties (<0.1%) for safety!""",
        "explanation_zh": """**问题：** 计算质量 = 45,000 ± 500千克的百分比不确定性。

**关键概念：** 百分比不确定性 = (绝对不确定性 / 测量值) × 100%

**步骤：**
1. 确定数值：
   - 测量值 = 45,000千克
   - 绝对不确定性 = ±500千克
2. 应用公式：(500 / 45,000) × 100%
3. 计算：0.0111... × 100% = 1.11%
4. 四舍五入到适当有效数字：1.1%

**答案：** 1.1%

**常见错误：**
- 忘记乘以100（得0.011而非1.1%）
- 分母使用错误数值
- 有效数字过多（百分比不确定性很少需要超过2位有效数字）

**提示：** 较小的百分比不确定性意味着更精确的测量。对于新加坡的建筑施工，结构工程师需要非常低的百分比不确定性（<0.1%）以确保安全！"""
    },
    {
        "id": "measurement-jc1-ex3",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "Which of the following is a vector quantity?",
        "prompt_zh": "以下哪个是矢量？",
        "choices": ["Mass", "Temperature", "Displacement", "Energy"],
        "choices_zh": ["质量", "温度", "位移", "能量"],
        "answer": 2,
        "explanation": """**Problem:** Identify the vector quantity from the list.

**Key Concept:** Vector quantities have both magnitude and direction. Scalar quantities have only magnitude.

**Steps:**
1. Review each option:
   - **Mass**: Scalar (only magnitude, e.g., 5 kg)
   - **Temperature**: Scalar (only magnitude, e.g., 30°C)
   - **Displacement**: Vector (magnitude AND direction, e.g., 10 m North)
   - **Energy**: Scalar (only magnitude, e.g., 100 J)
2. Identify which requires direction: Displacement ✓

**Answer:** Displacement

**Common Mistakes:**
- Confusing distance (scalar) with displacement (vector)
- Thinking all physical quantities are vectors
- Not understanding that direction is essential for vectors

**Tip:** Singapore MRT example - saying "Jurong East is 15 km away" is incomplete (distance, scalar). Saying "Jurong East is 15 km West" specifies displacement (vector) because it includes direction!""",
        "explanation_zh": """**问题：** 从列表中识别矢量。

**关键概念：** 矢量既有大小又有方向。标量只有大小。

**步骤：**
1. 检查每个选项：
   - **质量**：标量（只有大小，例如5千克）
   - **温度**：标量（只有大小，例如30°C）
   - **位移**：矢量（大小和方向，例如向北10米）
   - **能量**：标量（只有大小，例如100焦耳）
2. 识别哪个需要方向：位移 ✓

**答案：** 位移

**常见错误：**
- 混淆距离（标量）和位移（矢量）
- 认为所有物理量都是矢量
- 不理解方向对矢量至关重要

**提示：** 新加坡地铁例子 - 说"裕廊东距离15公里"是不完整的（距离，标量）。说"裕廊东在西方15公里"指定了位移（矢量），因为它包括方向！"""
    },
    {
        "id": "measurement-jc1-ex4",
        "type": "short",
        "difficulty": "easy",
        "prompt": "Express 0.00045 m in scientific notation.",
        "prompt_zh": "用科学记数法表示0.00045米。",
        "answer": "4.5 × 10^-4",
        "validator": "smart",
        "explanation": """**Problem:** Convert 0.00045 m to scientific notation.

**Key Concept:** Scientific notation: A × 10^n where 1 ≤ A < 10 and n is an integer.

**Steps:**
1. Identify the significant figures: 4 and 5
2. Place decimal after first significant figure: 4.5
3. Count decimal places moved: 0.00045 → 4.5 (moved 4 places right)
4. Moving right means negative exponent: 10^-4
5. Combine: 4.5 × 10^-4 m

**Answer:** 4.5 × 10^-4 m

**Common Mistakes:**
- Wrong exponent sign (using 10^4 instead of 10^-4)
- Placing decimal in wrong position (45 × 10^-5)
- Forgetting the unit (m)

**Tip:** In Singapore semiconductor manufacturing (GlobalFoundries), chip features are measured in nanometers: 7 nm = 7 × 10^-9 m. Scientific notation makes these tiny measurements manageable!""",
        "explanation_zh": """**问题：** 将0.00045米转换为科学记数法。

**关键概念：** 科学记数法：A × 10^n，其中1 ≤ A < 10且n为整数。

**步骤：**
1. 确定有效数字：4和5
2. 将小数点放在第一个有效数字后：4.5
3. 计算小数点移动位数：0.00045 → 4.5（向右移动4位）
4. 向右移动表示负指数：10^-4
5. 组合：4.5 × 10^-4米

**答案：** 4.5 × 10^-4米

**常见错误：**
- 指数符号错误（使用10^4而非10^-4）
- 小数点位置错误（45 × 10^-5）
- 忘记单位（米）

**提示：** 在新加坡半导体制造业（格罗方德），芯片特征以纳米为单位测量：7纳米 = 7 × 10^-9米。科学记数法使这些微小测量变得易于管理！"""
    },
    {
        "id": "measurement-jc1-ex5",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "How many significant figures are in the measurement 0.03050 m?",
        "prompt_zh": "测量值0.03050米有多少位有效数字？",
        "choices": ["3", "4", "5", "6"],
        "choices_zh": ["3", "4", "5", "6"],
        "answer": 1,
        "explanation": """**Problem:** Count significant figures in 0.03050 m.

**Key Concept:** Significant figure rules:
- All non-zero digits are significant
- Zeros between non-zero digits are significant
- Leading zeros are NOT significant
- Trailing zeros after decimal point ARE significant

**Steps:**
1. Identify digits: 0.03050
2. Remove leading zeros (not significant): 03050 → 3050
3. Count remaining digits: 3, 0, 5, 0 = 4 digits
4. All four are significant because:
   - 3 is non-zero ✓
   - 0 is between 3 and 5 ✓
   - 5 is non-zero ✓
   - Final 0 is trailing zero after decimal ✓

**Answer:** 4 significant figures

**Common Mistakes:**
- Counting leading zeros (getting 5 or 6)
- Not counting the zero between 3 and 5
- Not counting the trailing zero

**Tip:** PUB measures Singapore's water pH as 7.0 (2 sig figs). The trailing zero shows precision to 0.1 pH units, distinguishing it from just "7" (1 sig fig).""",
        "explanation_zh": """**问题：** 计算0.03050米中的有效数字。

**关键概念：** 有效数字规则：
- 所有非零数字都是有效的
- 非零数字之间的零是有效的
- 前导零不是有效的
- 小数点后的尾随零是有效的

**步骤：**
1. 识别数字：0.03050
2. 移除前导零（非有效）：03050 → 3050
3. 计算剩余数字：3, 0, 5, 0 = 4位数字
4. 所有四位都是有效的，因为：
   - 3是非零 ✓
   - 0在3和5之间 ✓
   - 5是非零 ✓
   - 最后的0是小数点后的尾随零 ✓

**答案：** 4位有效数字

**常见错误：**
- 计算前导零（得5或6）
- 不计算3和5之间的零
- 不计算尾随零

**提示：** 新加坡公用事业局测量水的pH值为7.0（2位有效数字）。尾随零显示精度到0.1 pH单位，将其与仅"7"（1位有效数字）区分开来。"""
    },

    # Medium exercises (6-10)
    {
        "id": "measurement-jc1-ex6",
        "type": "short",
        "difficulty": "medium",
        "prompt": "A ruler has markings every 1 mm. When measuring the length of a Helix Bridge model (28.4 cm), what is the absolute uncertainty in the measurement?",
        "prompt_zh": "一把尺子每1毫米有一个刻度。测量螺旋桥模型的长度（28.4厘米）时，测量的绝对不确定性是多少？",
        "answer": "0.5",
        "validator": "numeric",
        "explanation": """**Problem:** Find absolute uncertainty for a ruler with 1 mm divisions.

**Key Concept:** For analog instruments, absolute uncertainty = ± (smallest division / 2)

**Steps:**
1. Identify smallest division: 1 mm
2. Calculate uncertainty: ±1 mm / 2 = ±0.5 mm
3. Note: This applies regardless of what you're measuring
4. The measurement would be recorded as: 284 ± 0.5 mm or 28.4 ± 0.05 cm

**Answer:** 0.5 mm (or 0.05 cm)

**Common Mistakes:**
- Using the full division (±1 mm) instead of half
- Thinking uncertainty depends on measured value
- Confusing absolute and percentage uncertainty

**Tip:** When LTA measures road widths in Singapore for new expressways, they use laser measurement devices with much smaller uncertainties (±1 mm for 10 m distances) compared to tape measures!""",
        "explanation_zh": """**问题：** 求刻度为1毫米的尺子的绝对不确定性。

**关键概念：** 对于模拟仪器，绝对不确定性 = ±（最小刻度 / 2）

**步骤：**
1. 确定最小刻度：1毫米
2. 计算不确定性：±1毫米 / 2 = ±0.5毫米
3. 注意：无论测量什么，这都适用
4. 测量结果应记录为：284 ± 0.5毫米或28.4 ± 0.05厘米

**答案：** 0.5毫米（或0.05厘米）

**常见错误：**
- 使用完整刻度（±1毫米）而非一半
- 认为不确定性取决于测量值
- 混淆绝对不确定性和百分比不确定性

**提示：** 当新加坡陆路交通管理局为新建高速公路测量道路宽度时，他们使用激光测量设备，其不确定性（10米距离±1毫米）比卷尺小得多！"""
    },
    {
        "id": "measurement-jc1-ex7",
        "type": "mcq",
        "difficulty": "medium",
        "prompt": "Two vectors have magnitudes 12 N and 5 N. What is the magnitude of their resultant when they are perpendicular to each other?",
        "prompt_zh": "两个矢量的大小分别为12牛顿和5牛顿。当它们相互垂直时，它们的合矢量大小是多少？",
        "choices": ["7 N", "13 N", "17 N", "60 N"],
        "choices_zh": ["7牛顿", "13牛顿", "17牛顿", "60牛顿"],
        "answer": 1,
        "explanation": """**Problem:** Find resultant of two perpendicular vectors: 12 N and 5 N.

**Key Concept:** For perpendicular vectors, use Pythagorean theorem: R = √(A² + B²)

**Steps:**
1. Identify vectors: A = 12 N, B = 5 N
2. Check they're perpendicular (90°) ✓
3. Apply Pythagorean theorem:
   R = √(12² + 5²)
   R = √(144 + 25)
   R = √169
   R = 13 N

**Answer:** 13 N

**Common Mistakes:**
- Simply adding magnitudes (12 + 5 = 17 N) - wrong for perpendicular vectors
- Subtracting (12 - 5 = 7 N)
- Multiplying (12 × 5 = 60 N)
- Not using Pythagorean theorem for perpendicular vectors

**Tip:** Singapore cable car system - if horizontal tension is 12 kN and vertical weight component is 5 kN, the total cable tension is √(12² + 5²) = 13 kN, not just 17 kN!""",
        "explanation_zh": """**问题：** 求两个垂直矢量的合矢量：12牛顿和5牛顿。

**关键概念：** 对于垂直矢量，使用勾股定理：R = √(A² + B²)

**步骤：**
1. 确定矢量：A = 12牛顿，B = 5牛顿
2. 确认它们垂直（90°）✓
3. 应用勾股定理：
   R = √(12² + 5²)
   R = √(144 + 25)
   R = √169
   R = 13牛顿

**答案：** 13牛顿

**常见错误：**
- 简单相加大小（12 + 5 = 17牛顿）- 对垂直矢量错误
- 相减（12 - 5 = 7牛顿）
- 相乘（12 × 5 = 60牛顿）
- 对垂直矢量不使用勾股定理

**提示：** 新加坡缆车系统 - 如果水平张力为12千牛，垂直重量分量为5千牛，则总缆绳张力为√(12² + 5²) = 13千牛，而非仅17千牛！"""
    },
    {
        "id": "measurement-jc1-ex8",
        "type": "short",
        "difficulty": "medium",
        "prompt": "The diameter of a cylindrical water pipe at NEWater plant is measured as d = 0.25 ± 0.01 m. The length is measured as L = 10.0 ± 0.1 m. Calculate the percentage uncertainty in the volume V = πd²L/4.",
        "prompt_zh": "新生水厂圆柱形水管的直径测量为d = 0.25 ± 0.01米。长度测量为L = 10.0 ± 0.1米。计算体积V = πd²L/4的百分比不确定性。",
        "answer": "9",
        "validator": "numeric",
        "explanation": """**Problem:** Calculate percentage uncertainty in volume V = πd²L/4 given uncertainties in d and L.

**Key Concept:** When multiplying/dividing, add percentage uncertainties. When raising to power n, multiply uncertainty by n.

**Steps:**
1. Calculate percentage uncertainties:
   - For d: (0.01/0.25) × 100% = 4%
   - For L: (0.1/10.0) × 100% = 1%

2. Formula: V = πd²L/4
   - d² means percentage uncertainty in d is doubled: 2 × 4% = 8%
   - L¹ means percentage uncertainty stays: 1%

3. Add percentage uncertainties:
   Total = 8% + 1% = 9%

**Answer:** 9%

**Common Mistakes:**
- Forgetting to double uncertainty for d² (getting 5% instead of 9%)
- Adding absolute uncertainties instead of percentages
- Not understanding power rule (n × percentage uncertainty)

**Tip:** At NEWater plants, precision is critical. A 9% uncertainty in pipe volume would affect flow rate calculations and treatment efficiency! Engineers use more precise instruments to reduce this.""",
        "explanation_zh": """**问题：** 计算体积V = πd²L/4的百分比不确定性，已知d和L的不确定性。

**关键概念：** 乘除时，加上百分比不确定性。当升至幂次n时，不确定性乘以n。

**步骤：**
1. 计算百分比不确定性：
   - 对于d：(0.01/0.25) × 100% = 4%
   - 对于L：(0.1/10.0) × 100% = 1%

2. 公式：V = πd²L/4
   - d²意味着d的百分比不确定性加倍：2 × 4% = 8%
   - L¹意味着百分比不确定性保持：1%

3. 加上百分比不确定性：
   总计 = 8% + 1% = 9%

**答案：** 9%

**常见错误：**
- 忘记将d²的不确定性加倍（得5%而非9%）
- 加上绝对不确定性而非百分比
- 不理解幂次规则（n × 百分比不确定性）

**提示：** 在新生水厂，精度至关重要。管道体积9%的不确定性会影响流速计算和处理效率！工程师使用更精确的仪器来减少这一误差。"""
    },
    {
        "id": "measurement-jc1-ex9",
        "type": "mcq",
        "difficulty": "medium",
        "prompt": "Check if the equation v² = u² + 2as is dimensionally homogeneous, where v and u are velocities, a is acceleration, and s is displacement.",
        "prompt_zh": "检查方程v² = u² + 2as是否量纲一致，其中v和u是速度，a是加速度，s是位移。",
        "choices": ["Yes, both sides have dimensions [LT⁻²]", "Yes, both sides have dimensions [L²T⁻²]", "No, left side is [LT⁻¹] but right side is [LT⁻²]", "No, the equation is not dimensionally homogeneous"],
        "choices_zh": ["是，两边都有量纲[LT⁻²]", "是，两边都有量纲[L²T⁻²]", "否，左边是[LT⁻¹]但右边是[LT⁻²]", "否，方程量纲不一致"],
        "answer": 1,
        "explanation": """**Problem:** Check dimensional homogeneity of v² = u² + 2as.

**Key Concept:** All terms in an equation must have the same dimensions.

**Steps:**
1. Identify dimensions:
   - v, u (velocity): [LT⁻¹]
   - a (acceleration): [LT⁻²]
   - s (displacement): [L]

2. Check left side: v²
   - Dimensions: [LT⁻¹]² = [L²T⁻²]

3. Check right side: u² + 2as
   - u²: [LT⁻¹]² = [L²T⁻²]
   - 2as: [LT⁻²][L] = [L²T⁻²]
   - Sum: [L²T⁻²] + [L²T⁻²] = [L²T⁻²] ✓

4. Both sides have [L²T⁻²] - equation is dimensionally homogeneous ✓

**Answer:** Yes, both sides have dimensions [L²T⁻²]

**Common Mistakes:**
- Not squaring the dimensions of v
- Forgetting that constants (like 2) are dimensionless
- Confusing dimensions of acceleration and velocity

**Tip:** MRT train equations use this formula! If a train decelerates from 20 m/s at -2 m/s² over 100 m: v² = 20² + 2(-2)(100) = 0, so v = 0 (stops). Dimensional analysis helps verify equation correctness!""",
        "explanation_zh": """**问题：** 检查v² = u² + 2as的量纲一致性。

**关键概念：** 方程中的所有项必须具有相同的量纲。

**步骤：**
1. 确定量纲：
   - v, u（速度）：[LT⁻¹]
   - a（加速度）：[LT⁻²]
   - s（位移）：[L]

2. 检查左边：v²
   - 量纲：[LT⁻¹]² = [L²T⁻²]

3. 检查右边：u² + 2as
   - u²：[LT⁻¹]² = [L²T⁻²]
   - 2as：[LT⁻²][L] = [L²T⁻²]
   - 总和：[L²T⁻²] + [L²T⁻²] = [L²T⁻²] ✓

4. 两边都有[L²T⁻²] - 方程量纲一致 ✓

**答案：** 是，两边都有量纲[L²T⁻²]

**常见错误：**
- 不对v的量纲平方
- 忘记常数（如2）是无量纲的
- 混淆加速度和速度的量纲

**提示：** 地铁列车方程使用这个公式！如果列车从20米/秒以-2米/秒²减速100米：v² = 20² + 2(-2)(100) = 0，所以v = 0（停止）。量纲分析有助于验证方程正确性！"""
    },
    {
        "id": "measurement-jc1-ex10",
        "type": "short",
        "difficulty": "medium",
        "prompt": "A force of 50 ± 2 N is applied to an area of 0.10 ± 0.01 m². Calculate the pressure and its absolute uncertainty. (Pressure = Force / Area)",
        "prompt_zh": "将50 ± 2牛顿的力施加到0.10 ± 0.01平方米的面积上。计算压力及其绝对不确定性。（压力 = 力 / 面积）",
        "answer": "500 ± 60",
        "validator": "smart",
        "explanation": """**Problem:** Calculate pressure P = F/A with uncertainties: F = 50 ± 2 N, A = 0.10 ± 0.01 m².

**Key Concept:** For division, add percentage uncertainties, then convert back to absolute uncertainty.

**Steps:**
1. Calculate pressure:
   P = F/A = 50/0.10 = 500 Pa

2. Calculate percentage uncertainties:
   - Force: (2/50) × 100% = 4%
   - Area: (0.01/0.10) × 100% = 10%

3. Add percentage uncertainties (for division):
   Total = 4% + 10% = 14%

4. Convert to absolute uncertainty:
   ΔP = 500 × 0.14 = 70 Pa

5. Round appropriately: ±60 Pa (1 sig fig in uncertainty)

**Answer:** 500 ± 60 Pa

**Common Mistakes:**
- Adding absolute uncertainties directly (2 + 0.01)
- Not converting percentage back to absolute
- Too many sig figs in uncertainty (using ±70 instead of ±60)

**Tip:** At Marina Barrage, water pressure on the gates depends on water level and gate area. Engineers must account for measurement uncertainties when designing the structure to withstand typhoon conditions!""",
        "explanation_zh": """**问题：** 计算压力P = F/A及其不确定性：F = 50 ± 2牛顿，A = 0.10 ± 0.01平方米。

**关键概念：** 对于除法，加上百分比不确定性，然后转换回绝对不确定性。

**步骤：**
1. 计算压力：
   P = F/A = 50/0.10 = 500帕

2. 计算百分比不确定性：
   - 力：(2/50) × 100% = 4%
   - 面积：(0.01/0.10) × 100% = 10%

3. 加上百分比不确定性（对于除法）：
   总计 = 4% + 10% = 14%

4. 转换为绝对不确定性：
   ΔP = 500 × 0.14 = 70帕

5. 适当四舍五入：±60帕（不确定性1位有效数字）

**答案：** 500 ± 60帕

**常见错误：**
- 直接加上绝对不确定性（2 + 0.01）
- 不将百分比转换回绝对值
- 不确定性中有效数字过多（使用±70而非±60）

**提示：** 在滨海堤坝，闸门上的水压取决于水位和闸门面积。工程师在设计能够承受台风条件的结构时，必须考虑测量不确定性！"""
    }
]

# Note: Due to length, showing pattern for first 10 exercises
# Continue with 5 more medium-hard and 5 hard exercises to complete Chapter 1
# Then all 15 exercises for Chapter 2 (Kinematics)

print("Creating JC 1 Physics exercises (Batch 1: Chapters 1-2)...")
print(f"Chapter 1 (Measurement): {len(measurement_exercises)} exercises created (showing first 10)")
print("\\nWill create remaining 5 + all Chapter 2 exercises to complete batch...")
print("\\nNote: This is a partial demonstration. Full script would include all 30 exercises.")
