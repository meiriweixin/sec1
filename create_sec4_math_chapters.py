#!/usr/bin/env python3
"""
Generate Secondary 4 Mathematics chapters aligned with Singapore MOE O-Level syllabus.
Covers advanced topics typically taught in Sec 4 to prepare for O-Level exams.
"""

import json
from datetime import datetime

# Sec 4 Math Chapters based on Singapore O-Level Syllabus
sec4_math_chapters = [
    {
        "id": "quadratic-functions-graphs",
        "title": "Quadratic Functions and Graphs",
        "title_zh": "二次函数与图像",
        "gradeLevel": "sec4",
        "description": "Study quadratic functions, complete the square, and graph parabolas",
        "description_zh": "学习二次函数、配方法和绘制抛物线",
        "objectives": [
            "Express quadratic functions in different forms",
            "Complete the square for quadratic expressions",
            "Sketch graphs of quadratic functions and identify key features",
            "Solve problems involving maximum and minimum values"
        ],
        "objectives_zh": [
            "以不同形式表达二次函数",
            "对二次表达式进行配方",
            "绘制二次函数图像并识别关键特征",
            "解决涉及最大值和最小值的问题"
        ],
        "sections": [
            {
                "id": "quadratic-standard-form",
                "type": "text",
                "title": "Quadratic Functions in Standard Form",
                "title_zh": "标准形式的二次函数",
                "content": "A quadratic function has the form f(x) = ax² + bx + c, where a ≠ 0.\n\n**Key features:**\n\n1. The coefficient 'a' determines the shape and direction\n2. If a > 0, the parabola opens upward (minimum point)\n3. If a < 0, the parabola opens downward (maximum point)\n4. The y-intercept is at (0, c)\n\n**Example: Singapore context**\n\nA water fountain's height h meters above ground is modeled by h = -2t² + 8t + 3, where t is time in seconds.\n\nFind the initial height and maximum height of the water.",
                "content_zh": "二次函数的形式为 f(x) = ax² + bx + c，其中 a ≠ 0。\n\n**关键特征：**\n\n1. 系数'a'决定形状和方向\n2. 如果 a > 0，抛物线向上开口（最小值点）\n3. 如果 a < 0，抛物线向下开口（最大值点）\n4. y截距在(0, c)\n\n**例子：新加坡情境**\n\n喷泉的水高h米由h = -2t² + 8t + 3建模，其中t是时间（秒）。\n\n求初始高度和最大高度。"
            },
            {
                "id": "completing-square",
                "type": "text",
                "title": "Completing the Square",
                "title_zh": "配方法",
                "content": "Completing the square transforms ax² + bx + c into a(x + p)² + q form.\n\n**Steps:**\n\n1. Factor out 'a' from x² and x terms\n2. Take half of the x coefficient, square it\n3. Add and subtract this value inside brackets\n4. Simplify to vertex form\n\n**Why it's useful:**\n\n- Identifies the vertex (turning point) directly\n- Makes sketching graphs easier\n- Helps solve quadratic equations\n- Finds maximum or minimum values\n\n**Singapore exam tip:** Always check your final answer by expanding back to standard form.",
                "content_zh": "配方法将 ax² + bx + c 转换为 a(x + p)² + q 形式。\n\n**步骤：**\n\n1. 从 x² 和 x 项中提取'a'\n2. 取 x 系数的一半，平方\n3. 在括号内加减这个值\n4. 简化为顶点形式\n\n**为什么有用：**\n\n- 直接识别顶点（转折点）\n- 使绘图更容易\n- 帮助解二次方程\n- 找到最大值或最小值\n\n**新加坡考试提示：** 总是通过展开回标准形式来检查答案。"
            },
            {
                "id": "graphing-parabolas",
                "type": "text",
                "title": "Sketching Quadratic Graphs",
                "title_zh": "绘制二次图像",
                "content": "To sketch y = ax² + bx + c accurately:\n\n**Step 1:** Find the y-intercept (set x = 0)\n\n**Step 2:** Find x-intercepts by solving ax² + bx + c = 0 (if they exist)\n\n**Step 3:** Find the vertex using x = -b/(2a), then substitute to find y\n\n**Step 4:** Determine if parabola opens up (a > 0) or down (a < 0)\n\n**Step 5:** Plot key points and sketch a smooth curve\n\n**Key features to label:**\n- Vertex (turning point)\n- Axis of symmetry: x = -b/(2a)\n- Intercepts\n- Direction of opening\n\n**Singapore context:** Graph sketching questions often appear in Paper 2 Section B.",
                "content_zh": "准确绘制 y = ax² + bx + c：\n\n**步骤 1：** 找 y 截距（设 x = 0）\n\n**步骤 2：** 通过解 ax² + bx + c = 0 找 x 截距（如果存在）\n\n**步骤 3：** 使用 x = -b/(2a) 找顶点，然后代入求 y\n\n**步骤 4：** 确定抛物线向上开口（a > 0）还是向下（a < 0）\n\n**步骤 5：** 绘制关键点并画平滑曲线\n\n**要标记的关键特征：**\n- 顶点（转折点）\n- 对称轴：x = -b/(2a)\n- 截距\n- 开口方向\n\n**新加坡情境：** 图像绘制题目经常出现在试卷2 B部分。"
            }
        ],
        "exercises": []
    },
    {
        "id": "simultaneous-equations-advanced",
        "title": "Simultaneous Equations (Linear & Quadratic)",
        "title_zh": "联立方程（线性与二次）",
        "gradeLevel": "sec4",
        "description": "Solve systems involving one linear and one quadratic equation",
        "description_zh": "解包含一个线性和一个二次方程的方程组",
        "objectives": [
            "Solve simultaneous equations with one linear and one quadratic",
            "Interpret solutions graphically",
            "Apply to real-world problems",
            "Understand cases with 0, 1, or 2 solutions"
        ],
        "objectives_zh": [
            "解一个线性和一个二次的联立方程",
            "用图形解释解",
            "应用于实际问题",
            "理解0、1或2个解的情况"
        ],
        "sections": [
            {
                "id": "substitution-method-advanced",
                "type": "text",
                "title": "Substitution Method",
                "title_zh": "代入法",
                "content": "To solve a linear equation with a quadratic equation simultaneously:\n\n**Method:**\n\n1. Rearrange the linear equation to make one variable the subject\n2. Substitute this expression into the quadratic equation\n3. Solve the resulting quadratic equation\n4. Substitute back to find the other variable\n5. Check both solutions\n\n**Example: Singapore MRT fare zones**\n\nThe fare f (in cents) and distance d (in km) relationship is:\n- Linear: f = 50d + 80\n- Quadratic: f = 2d² + 30d + 100\n\nFind where both models predict the same fare.\n\n**Note:** You may get 0, 1, or 2 pairs of solutions depending on whether the line intersects the parabola.",
                "content_zh": "同时解一个线性方程和一个二次方程：\n\n**方法：**\n\n1. 重新排列线性方程使一个变量成为主语\n2. 将此表达式代入二次方程\n3. 解所得二次方程\n4. 代回求另一个变量\n5. 检查两个解\n\n**例子：新加坡地铁票价区**\n\n票价 f（分）和距离 d（公里）的关系是：\n- 线性：f = 50d + 80\n- 二次：f = 2d² + 30d + 100\n\n找出两个模型预测相同票价的点。\n\n**注意：** 根据直线是否与抛物线相交，你可能得到0、1或2对解。"
            },
            {
                "id": "graphical-interpretation",
                "type": "text",
                "title": "Graphical Interpretation",
                "title_zh": "图形解释",
                "content": "The solutions to simultaneous equations represent intersection points of graphs.\n\n**For y = mx + c and y = ax² + bx + c:**\n\n**Case 1: Two solutions**\n- Line intersects parabola at two points\n- Two distinct (x, y) pairs\n\n**Case 2: One solution**\n- Line is tangent to parabola\n- One (x, y) pair\n- Discriminant b² - 4ac = 0\n\n**Case 3: No solution**\n- Line does not intersect parabola\n- No real solutions\n- Discriminant b² - 4ac < 0\n\n**Singapore exam focus:** Questions often ask you to interpret the number of solutions graphically.",
                "content_zh": "联立方程的解代表图像的交点。\n\n**对于 y = mx + c 和 y = ax² + bx + c：**\n\n**情况1：两个解**\n- 直线与抛物线在两点相交\n- 两个不同的(x, y)对\n\n**情况2：一个解**\n- 直线与抛物线相切\n- 一个(x, y)对\n- 判别式 b² - 4ac = 0\n\n**情况3：无解**\n- 直线不与抛物线相交\n- 无实数解\n- 判别式 b² - 4ac < 0\n\n**新加坡考试重点：** 题目经常要求你用图形解释解的数量。"
            }
        ],
        "exercises": []
    },
    {
        "id": "coordinate-geometry-advanced",
        "title": "Advanced Coordinate Geometry",
        "title_zh": "高级坐标几何",
        "gradeLevel": "sec4",
        "description": "Study parallel and perpendicular lines, and equation of circles",
        "description_zh": "学习平行线、垂直线和圆的方程",
        "objectives": [
            "Find equations of parallel and perpendicular lines",
            "Solve problems involving distance and midpoint",
            "Work with the equation of a circle",
            "Apply coordinate geometry to geometric proofs"
        ],
        "objectives_zh": [
            "求平行线和垂直线的方程",
            "解决涉及距离和中点的问题",
            "处理圆的方程",
            "应用坐标几何进行几何证明"
        ],
        "sections": [
            {
                "id": "parallel-perpendicular-lines",
                "type": "text",
                "title": "Parallel and Perpendicular Lines",
                "title_zh": "平行线和垂直线",
                "content": "**Parallel Lines:**\n\nTwo lines are parallel if they have the same gradient.\n- If y = m₁x + c₁ is parallel to y = m₂x + c₂, then m₁ = m₂\n\n**Perpendicular Lines:**\n\nTwo lines are perpendicular if the product of their gradients is -1.\n- If y = m₁x + c₁ is perpendicular to y = m₂x + c₂, then m₁ × m₂ = -1\n- Or m₂ = -1/m₁\n\n**Finding equation of a line:**\n\n1. Find the gradient m\n2. Use y - y₁ = m(x - x₁) with a known point (x₁, y₁)\n3. Rearrange to y = mx + c form\n\n**Singapore context:** Used in urban planning, road design, and architecture.",
                "content_zh": "**平行线：**\n\n两条线平行如果它们有相同的梯度。\n- 如果 y = m₁x + c₁ 平行于 y = m₂x + c₂，则 m₁ = m₂\n\n**垂直线：**\n\n两条线垂直如果它们的梯度乘积为-1。\n- 如果 y = m₁x + c₁ 垂直于 y = m₂x + c₂，则 m₁ × m₂ = -1\n- 或 m₂ = -1/m₁\n\n**求直线方程：**\n\n1. 找梯度 m\n2. 使用 y - y₁ = m(x - x₁) 和已知点 (x₁, y₁)\n3. 重新排列为 y = mx + c 形式\n\n**新加坡情境：** 用于城市规划、道路设计和建筑。"
            },
            {
                "id": "equation-of-circle",
                "type": "text",
                "title": "Equation of a Circle",
                "title_zh": "圆的方程",
                "content": "**Standard form:** (x - a)² + (y - b)² = r²\n\nWhere:\n- Centre is at point (a, b)\n- Radius is r\n\n**Expanded form:** x² + y² + 2gx + 2fy + c = 0\n\nWhere:\n- Centre is at (-g, -f)\n- Radius r = √(g² + f² - c)\n\n**Key skills:**\n\n1. Find centre and radius from equation\n2. Write equation given centre and radius\n3. Determine if a point lies on, inside, or outside circle\n4. Find intersection points with lines\n\n**Singapore application:** Marina Bay Sands design, Gardens by the Bay dome structures.",
                "content_zh": "**标准形式：** (x - a)² + (y - b)² = r²\n\n其中：\n- 中心在点 (a, b)\n- 半径为 r\n\n**展开形式：** x² + y² + 2gx + 2fy + c = 0\n\n其中：\n- 中心在 (-g, -f)\n- 半径 r = √(g² + f² - c)\n\n**关键技能：**\n\n1. 从方程求中心和半径\n2. 给定中心和半径写方程\n3. 确定点在圆上、内部还是外部\n4. 求与直线的交点\n\n**新加坡应用：** 滨海湾金沙设计、滨海湾花园穹顶结构。"
            }
        ],
        "exercises": []
    },
    {
        "id": "trigonometry-advanced",
        "title": "Advanced Trigonometry",
        "title_zh": "高级三角学",
        "gradeLevel": "sec4",
        "description": "Study sine and cosine rules, area of triangles, and 3D problems",
        "description_zh": "学习正弦和余弦定理、三角形面积和3D问题",
        "objectives": [
            "Apply sine rule to find unknown sides and angles",
            "Apply cosine rule to solve triangles",
            "Calculate area of triangles using ½ab sin C",
            "Solve 3D trigonometry problems"
        ],
        "objectives_zh": [
            "应用正弦定理求未知边和角",
            "应用余弦定理解三角形",
            "使用½ab sin C计算三角形面积",
            "解3D三角问题"
        ],
        "sections": [
            {
                "id": "sine-rule",
                "type": "text",
                "title": "Sine Rule",
                "title_zh": "正弦定理",
                "content": "**Sine Rule:** For any triangle ABC with sides a, b, c opposite to angles A, B, C:\n\na/sin A = b/sin B = c/sin C\n\nOr equivalently:\n\nsin A/a = sin B/b = sin C/c\n\n**When to use:**\n- Given two angles and one side (AAS or ASA)\n- Given two sides and an angle opposite one of them (SSA)\n\n**Steps:**\n\n1. Label the triangle with a, b, c opposite A, B, C\n2. Write the sine rule formula\n3. Substitute known values\n4. Solve for unknown\n\n**Singapore context:** Used in surveying, navigation (Singapore Strait), and construction planning.\n\n**Warning:** SSA case may have two possible solutions (ambiguous case).",
                "content_zh": "**正弦定理：** 对于任何三角形ABC，边a, b, c对应角A, B, C：\n\na/sin A = b/sin B = c/sin C\n\n或等价地：\n\nsin A/a = sin B/b = sin C/c\n\n**何时使用：**\n- 给定两角一边（AAS或ASA）\n- 给定两边和其中一边的对角（SSA）\n\n**步骤：**\n\n1. 用a, b, c标记三角形对应A, B, C\n2. 写正弦定理公式\n3. 代入已知值\n4. 解未知数\n\n**新加坡情境：** 用于测量、导航（新加坡海峡）和建筑规划。\n\n**警告：** SSA情况可能有两个解（模棱两可的情况）。"
            },
            {
                "id": "cosine-rule",
                "type": "text",
                "title": "Cosine Rule",
                "title_zh": "余弦定理",
                "content": "**Cosine Rule:** For any triangle ABC:\n\n**To find a side:**\na² = b² + c² - 2bc cos A\n\n**To find an angle:**\ncos A = (b² + c² - a²)/(2bc)\n\n**When to use:**\n- Given three sides (SSS)\n- Given two sides and the included angle (SAS)\n\n**Steps:**\n\n1. Identify what you need to find (side or angle)\n2. Choose appropriate form of cosine rule\n3. Substitute known values carefully\n4. Solve the equation\n\n**Singapore application:** Engineering projects, Changi Airport terminal design, bridge construction.\n\n**Note:** Cosine rule generalizes Pythagoras' theorem (when angle = 90°, cos 90° = 0).",
                "content_zh": "**余弦定理：** 对于任何三角形ABC：\n\n**求边：**\na² = b² + c² - 2bc cos A\n\n**求角：**\ncos A = (b² + c² - a²)/(2bc)\n\n**何时使用：**\n- 给定三边（SSS）\n- 给定两边和夹角（SAS）\n\n**步骤：**\n\n1. 确定要求什么（边或角）\n2. 选择适当的余弦定理形式\n3. 仔细代入已知值\n4. 解方程\n\n**新加坡应用：** 工程项目、樟宜机场航站楼设计、桥梁建设。\n\n**注意：** 余弦定理是毕达哥拉斯定理的推广（当角度=90°时，cos 90°=0）。"
            },
            {
                "id": "area-triangle",
                "type": "text",
                "title": "Area of Triangle Formula",
                "title_zh": "三角形面积公式",
                "content": "**Area formula:** For triangle with sides a and b and included angle C:\n\nArea = ½ab sin C\n\n**When to use:**\n- Given two sides and included angle (SAS)\n- More efficient than base × height when angle is known\n\n**Steps:**\n\n1. Identify the two sides and included angle\n2. Apply Area = ½ab sin C\n3. Calculate using calculator\n4. Include appropriate units (cm², m², etc.)\n\n**Alternative forms:**\n- Area = ½bc sin A\n- Area = ½ac sin B\n\n**Singapore context:** Land area calculations for HDB estates, park planning, urban development.\n\n**Exam tip:** Always check your angle is in degrees mode on calculator.",
                "content_zh": "**面积公式：** 对于有边a和b及夹角C的三角形：\n\n面积 = ½ab sin C\n\n**何时使用：**\n- 给定两边和夹角（SAS）\n- 当已知角度时比底×高更有效\n\n**步骤：**\n\n1. 确定两边和夹角\n2. 应用面积 = ½ab sin C\n3. 用计算器计算\n4. 包括适当的单位（cm²、m²等）\n\n**其他形式：**\n- 面积 = ½bc sin A\n- 面积 = ½ac sin B\n\n**新加坡情境：** HDB社区的土地面积计算、公园规划、城市发展。\n\n**考试提示：** 总是检查计算器是否在度数模式。"
            }
        ],
        "exercises": []
    },
    {
        "id": "probability-advanced",
        "title": "Advanced Probability",
        "title_zh": "高级概率",
        "gradeLevel": "sec4",
        "description": "Study tree diagrams, conditional probability, and probability distributions",
        "description_zh": "学习树形图、条件概率和概率分布",
        "objectives": [
            "Construct and use tree diagrams for multi-stage events",
            "Calculate conditional probabilities",
            "Apply addition and multiplication rules",
            "Solve real-world probability problems"
        ],
        "objectives_zh": [
            "构造和使用多阶段事件的树形图",
            "计算条件概率",
            "应用加法和乘法规则",
            "解决实际概率问题"
        ],
        "sections": [
            {
                "id": "tree-diagrams",
                "type": "text",
                "title": "Probability Tree Diagrams",
                "title_zh": "概率树形图",
                "content": "**Tree diagrams** show all possible outcomes of multi-stage events.\n\n**How to construct:**\n\n1. Draw branches for first event with probabilities\n2. From each branch, draw branches for second event\n3. Continue for all stages\n4. Label all branches with probabilities\n5. Multiply along branches for combined probability\n6. Add probabilities for different paths to same outcome\n\n**Key rules:**\n\n- Probabilities on each set of branches sum to 1\n- **Multiplication rule:** P(A and B) = P(A) × P(B|A)\n- **Addition rule:** P(A or B) = P(A) + P(B) - P(A and B)\n\n**Singapore context:** Weather forecasting, MRT service reliability, medical diagnosis accuracy.",
                "content_zh": "**树形图**显示多阶段事件的所有可能结果。\n\n**如何构造：**\n\n1. 为第一个事件画分支及概率\n2. 从每个分支，为第二个事件画分支\n3. 继续所有阶段\n4. 用概率标记所有分支\n5. 沿分支相乘得组合概率\n6. 将不同路径到相同结果的概率相加\n\n**关键规则：**\n\n- 每组分支的概率和为1\n- **乘法规则：** P(A和B) = P(A) × P(B|A)\n- **加法规则：** P(A或B) = P(A) + P(B) - P(A和B)\n\n**新加坡情境：** 天气预报、地铁服务可靠性、医疗诊断准确性。"
            },
            {
                "id": "conditional-probability",
                "type": "text",
                "title": "Conditional Probability",
                "title_zh": "条件概率",
                "content": "**Conditional probability** P(A|B) is the probability of A occurring given that B has occurred.\n\n**Formula:**\n\nP(A|B) = P(A and B) / P(B)\n\n**Key concepts:**\n\n1. **Independent events:** P(A|B) = P(A)\n   - Event B doesn't affect probability of A\n   - P(A and B) = P(A) × P(B)\n\n2. **Dependent events:** P(A|B) ≠ P(A)\n   - Event B affects probability of A\n   - P(A and B) = P(A) × P(B|A)\n\n**Types of sampling:**\n\n- **With replacement:** Independent events\n- **Without replacement:** Dependent events\n\n**Singapore exam focus:** Questions often involve balls from bags, card games, or quality control scenarios.",
                "content_zh": "**条件概率** P(A|B)是在B发生的条件下A发生的概率。\n\n**公式：**\n\nP(A|B) = P(A和B) / P(B)\n\n**关键概念：**\n\n1. **独立事件：** P(A|B) = P(A)\n   - 事件B不影响A的概率\n   - P(A和B) = P(A) × P(B)\n\n2. **相关事件：** P(A|B) ≠ P(A)\n   - 事件B影响A的概率\n   - P(A和B) = P(A) × P(B|A)\n\n**抽样类型：**\n\n- **有放回：** 独立事件\n- **无放回：** 相关事件\n\n**新加坡考试重点：** 题目经常涉及从袋中取球、纸牌游戏或质量控制场景。"
            }
        ],
        "exercises": []
    },
    {
        "id": "applications-of-mathematics",
        "title": "Applications of Mathematics",
        "title_zh": "数学应用",
        "gradeLevel": "sec4",
        "description": "Apply mathematics to solve real-world problems in various contexts",
        "description_zh": "应用数学解决各种情境中的实际问题",
        "objectives": [
            "Model real-world situations mathematically",
            "Apply multiple mathematical concepts to complex problems",
            "Interpret mathematical results in context",
            "Communicate mathematical reasoning clearly"
        ],
        "objectives_zh": [
            "用数学建模实际情况",
            "将多个数学概念应用于复杂问题",
            "在情境中解释数学结果",
            "清晰表达数学推理"
        ],
        "sections": [
            {
                "id": "optimization-problems",
                "type": "text",
                "title": "Optimization Problems",
                "title_zh": "优化问题",
                "content": "**Optimization** involves finding maximum or minimum values.\n\n**Common applications:**\n\n1. **Maximum area/volume:** Given fixed perimeter or surface area\n2. **Minimum cost:** Finding most economical solution\n3. **Maximum profit:** Business and economics\n4. **Shortest distance:** Navigation and logistics\n\n**Method using quadratics:**\n\n1. Express quantity to optimize as quadratic function\n2. Complete the square to find vertex\n3. Identify if vertex gives maximum or minimum\n4. Interpret answer in context\n\n**Singapore context:**\n\n- HDB flat design: Maximize living space with budget constraints\n- Singapore Port: Optimize container loading\n- Public transport: Minimize travel time\n- NEWater plant: Maximize water treatment efficiency",
                "content_zh": "**优化**涉及找最大值或最小值。\n\n**常见应用：**\n\n1. **最大面积/体积：** 给定固定周长或表面积\n2. **最小成本：** 找最经济的解决方案\n3. **最大利润：** 商业和经济学\n4. **最短距离：** 导航和物流\n\n**使用二次函数的方法：**\n\n1. 将要优化的量表示为二次函数\n2. 配方求顶点\n3. 确定顶点给出最大值还是最小值\n4. 在情境中解释答案\n\n**新加坡情境：**\n\n- HDB公寓设计：在预算约束下最大化生活空间\n- 新加坡港口：优化集装箱装载\n- 公共交通：最小化旅行时间\n- 新生水厂：最大化水处理效率"
            },
            {
                "id": "rate-of-change",
                "type": "text",
                "title": "Rate of Change Applications",
                "title_zh": "变化率应用",
                "content": "**Rate of change** describes how one quantity changes relative to another.\n\n**Gradient interpretation:**\n\n- On distance-time graphs: gradient = speed\n- On speed-time graphs: gradient = acceleration\n- On cost-quantity graphs: gradient = unit cost\n\n**Real-world applications:**\n\n**1. Population growth**\n- Singapore population model: P = P₀(1 + r)ⁿ\n- r = growth rate, n = number of years\n\n**2. Depreciation**\n- Car value: V = V₀(1 - d)ⁿ\n- d = depreciation rate\n\n**3. Temperature change**\n- Climate data analysis\n- Cooling/heating rates\n\n**4. Financial mathematics**\n- Simple interest: I = Prt\n- Compound interest: A = P(1 + r)ⁿ\n\n**Singapore context:** GST calculations, CPF interest, HDB resale price trends.",
                "content_zh": "**变化率**描述一个量相对于另一个量的变化。\n\n**梯度解释：**\n\n- 在距离-时间图上：梯度=速度\n- 在速度-时间图上：梯度=加速度\n- 在成本-数量图上：梯度=单位成本\n\n**实际应用：**\n\n**1. 人口增长**\n- 新加坡人口模型：P = P₀(1 + r)ⁿ\n- r = 增长率，n = 年数\n\n**2. 折旧**\n- 汽车价值：V = V₀(1 - d)ⁿ\n- d = 折旧率\n\n**3. 温度变化**\n- 气候数据分析\n- 冷却/加热速率\n\n**4. 金融数学**\n- 单利：I = Prt\n- 复利：A = P(1 + r)ⁿ\n\n**新加坡情境：** 消费税计算、公积金利息、组屋转售价格趋势。"
            }
        ],
        "exercises": []
    }
]

def save_chapters():
    """Save all Sec 4 Math chapters to individual JSON files."""
    import os

    # Create chapters directory if it doesn't exist
    os.makedirs('chapters', exist_ok=True)

    for chapter in sec4_math_chapters:
        filename = f"chapters/sec4-math-{chapter['id']}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(chapter, f, ensure_ascii=False, indent=2)
        print(f"✓ Created: {filename}")

    print(f"\n{'='*60}")
    print(f"✅ Successfully created {len(sec4_math_chapters)} Sec 4 Math chapters")
    print(f"{'='*60}")
    print("\nChapters created:")
    for i, chapter in enumerate(sec4_math_chapters, 1):
        print(f"{i}. {chapter['title']}")

if __name__ == '__main__':
    save_chapters()
