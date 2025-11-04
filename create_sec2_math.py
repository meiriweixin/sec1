"""
Generate Secondary 2 Mathematics chapters following Singapore MOE syllabus.
Based on Sec 1 structure: 15 exercises per chapter, multiple sections.
"""

import json

# Secondary 2 Math chapters based on MOE syllabus
sec2_math_chapters = [
    # ALGEBRA & EQUATIONS (6 chapters)
    {
        "id": "linear-equations-two-variables-sec2",
        "gradeLevel": "sec2",
        "title": "Linear Equations in Two Variables",
        "title_zh": "二元一次方程",
        "description": "Solving simultaneous linear equations using substitution and elimination methods",
        "description_zh": "使用代入法和消元法求解二元一次方程组",
        "tag": "Algebra",
        "tag_zh": "代数",
        "objectives": [
            "Solve simultaneous equations by substitution",
            "Solve simultaneous equations by elimination",
            "Apply to real-world problems",
            "Interpret solutions graphically"
        ],
        "objectives_zh": [
            "用代入法求解二元一次方程组",
            "用消元法求解二元一次方程组",
            "应用于实际问题",
            "图形解释解"
        ],
        "sections": [
            {
                "id": "substitution-method",
                "type": "text",
                "title": "Substitution Method",
                "title_zh": "代入法",
                "content": "To solve simultaneous equations by substitution: 1) Make one variable the subject in one equation, 2) Substitute into the other equation, 3) Solve for the remaining variable, 4) Find the other variable. Example: Singapore hawker stalls - if 2 plates of chicken rice and 3 drinks cost $12, and 1 plate costs $2 more than a drink, find the prices.",
                "content_zh": "用代入法求解二元一次方程组：1）在一个方程中将一个变量表示为另一个的函数，2）代入另一个方程，3）求解剩余变量，4）求另一个变量。例如：新加坡小贩摊位 - 如果2盘鸡饭和3杯饮料共12元，1盘比1杯贵2元，求价格。"
            },
            {
                "id": "elimination-method",
                "type": "text",
                "title": "Elimination Method",
                "title_zh": "消元法",
                "content": "To solve by elimination: 1) Make coefficients of one variable equal by multiplying, 2) Add or subtract equations to eliminate that variable, 3) Solve for remaining variable, 4) Substitute back to find the other. Useful for Singapore transportation problems (MRT + bus trips).",
                "content_zh": "用消元法求解：1）通过乘法使一个变量的系数相等，2）加减方程消去该变量，3）求解剩余变量，4）代回求另一个。适用于新加坡交通问题（地铁+巴士行程）。"
            },
            {
                "id": "applications",
                "type": "text",
                "title": "Real-World Applications",
                "title_zh": "实际应用",
                "content": "Simultaneous equations solve problems involving: pricing (GST-inclusive vs exclusive), mixtures (coffee stalls mixing beans), motion (MRT and walking speeds), and budgeting (HDB conservancy charges).",
                "content_zh": "二元一次方程组解决涉及以下问题：定价（含消费税与不含）、混合（咖啡摊混合咖啡豆）、运动（地铁和步行速度）和预算（组屋管理费）。"
            }
        ],
        "exercises": []  # Will be filled by separate script
    },

    {
        "id": "algebraic-manipulation-sec2",
        "gradeLevel": "sec2",
        "title": "Algebraic Manipulation & Formulae",
        "title_zh": "代数运算与公式",
        "description": "Expansion, factorization, and changing the subject of formulae",
        "description_zh": "展开、因式分解和改变公式主项",
        "tag": "Algebra",
        "tag_zh": "代数",
        "objectives": [
            "Expand algebraic products including (a+b)(c+d)",
            "Factorize algebraic expressions",
            "Change the subject of a formula",
            "Apply to practical Singapore contexts"
        ],
        "objectives_zh": [
            "展开代数乘积，包括(a+b)(c+d)",
            "因式分解代数表达式",
            "改变公式的主项",
            "应用于新加坡实际情境"
        ],
        "sections": [
            {
                "id": "expansion",
                "type": "text",
                "title": "Algebraic Expansion",
                "title_zh": "代数展开",
                "content": "Expand (a+b)(c+d) = ac + ad + bc + bd. Use FOIL method (First, Outer, Inner, Last). Example: Calculate total cost when buying multiple items with Singapore GST (9%).",
                "content_zh": "展开(a+b)(c+d) = ac + ad + bc + bd。使用FOIL法（首、外、内、尾）。例如：计算购买多件物品加新加坡消费税（9%）的总成本。"
            },
            {
                "id": "factorization",
                "type": "text",
                "title": "Factorization",
                "title_zh": "因式分解",
                "content": "Factorize by: 1) Common factors, 2) Grouping, 3) Difference of two squares (a²-b²=(a+b)(a-b)). Used in Singapore construction calculations for HDB floor areas.",
                "content_zh": "因式分解：1）提公因式，2）分组，3）平方差公式(a²-b²=(a+b)(a-b))。用于新加坡组屋楼面面积的建筑计算。"
            },
            {
                "id": "changing-subject",
                "type": "text",
                "title": "Changing the Subject",
                "title_zh": "改变公式主项",
                "content": "To make x the subject: 1) Move terms not containing x to one side, 2) Isolate x by inverse operations. Example: Convert temperature formulas C = (F-32)×5/9 (Singapore uses Celsius, understand Fahrenheit).",
                "content_zh": "将x作为主项：1）将不含x的项移到一边，2）用逆运算分离x。例如：转换温度公式C = (F-32)×5/9（新加坡使用摄氏度，理解华氏度）。"
            }
        ],
        "exercises": []
    },

    {
        "id": "quadratic-expressions-sec2",
        "gradeLevel": "sec2",
        "title": "Quadratic Expressions & Equations",
        "title_zh": "二次表达式与方程",
        "description": "Factorizing and solving quadratic equations",
        "description_zh": "因式分解和求解二次方程",
        "tag": "Algebra",
        "tag_zh": "代数",
        "objectives": [
            "Factorize quadratic expressions ax²+bx+c",
            "Solve quadratic equations by factorization",
            "Solve simple quadratic equations using formula",
            "Apply to area and motion problems"
        ],
        "objectives_zh": [
            "因式分解二次表达式ax²+bx+c",
            "用因式分解求解二次方程",
            "用公式求解简单二次方程",
            "应用于面积和运动问题"
        ],
        "sections": [
            {
                "id": "factorizing-quadratics",
                "type": "text",
                "title": "Factorizing Quadratics",
                "title_zh": "因式分解二次式",
                "content": "To factorize x²+bx+c, find two numbers that multiply to c and add to b. For ax²+bx+c, use cross-method or grouping. Example: Calculate rectangular HDB room dimensions when area is known.",
                "content_zh": "因式分解x²+bx+c，找两个数相乘等于c，相加等于b。对于ax²+bx+c，使用十字相乘法或分组。例如：已知面积计算组屋房间矩形尺寸。"
            },
            {
                "id": "solving-by-factorization",
                "type": "text",
                "title": "Solving by Factorization",
                "title_zh": "用因式分解求解",
                "content": "Steps: 1) Rearrange to ax²+bx+c=0, 2) Factorize to (x+p)(x+q)=0, 3) Set each factor to zero: x+p=0 or x+q=0. Used in Singapore projectile motion (throwing objects).",
                "content_zh": "步骤：1）重排为ax²+bx+c=0，2）因式分解为(x+p)(x+q)=0，3）令每个因子为零：x+p=0或x+q=0。用于新加坡抛物运动（投掷物体）。"
            },
            {
                "id": "quadratic-formula",
                "type": "text",
                "title": "Quadratic Formula",
                "title_zh": "二次公式",
                "content": "For ax²+bx+c=0: x = (-b ± √(b²-4ac)) / 2a. Use when factorization is difficult. Singapore applications: calculating optimal prices with profit margins.",
                "content_zh": "对于ax²+bx+c=0：x = (-b ± √(b²-4ac)) / 2a。当因式分解困难时使用。新加坡应用：计算利润率的最优价格。"
            }
        ],
        "exercises": []
    },

    {
        "id": "functions-graphs-sec2",
        "gradeLevel": "sec2",
        "title": "Functions and Graphs",
        "title_zh": "函数与图形",
        "description": "Understanding functions, domain, range, and graphing",
        "description_zh": "理解函数、定义域、值域和绘图",
        "tag": "Algebra",
        "tag_zh": "代数",
        "objectives": [
            "Understand function notation f(x)",
            "Find domain and range",
            "Draw and interpret graphs",
            "Solve problems using graphs"
        ],
        "objectives_zh": [
            "理解函数符号f(x)",
            "求定义域和值域",
            "绘制和解释图形",
            "用图形解决问题"
        ],
        "sections": [
            {
                "id": "function-notation",
                "type": "text",
                "title": "Function Notation",
                "title_zh": "函数符号",
                "content": "f(x) means 'function of x'. If f(x)=2x+3, then f(5)=2(5)+3=13. Example: Singapore taxi fare function f(d)=base+rate×distance, where d is distance in km.",
                "content_zh": "f(x)表示'x的函数'。如果f(x)=2x+3，则f(5)=2(5)+3=13。例如：新加坡出租车费用函数f(d)=起步价+单价×距离，其中d是公里距离。"
            },
            {
                "id": "domain-range",
                "type": "text",
                "title": "Domain and Range",
                "title_zh": "定义域和值域",
                "content": "Domain: all possible input (x) values. Range: all possible output (y) values. For Singapore context: f(t)=temperature during day, domain is 0≤t≤24 hours, range is 24≤f(t)≤33°C.",
                "content_zh": "定义域：所有可能的输入(x)值。值域：所有可能的输出(y)值。新加坡情境：f(t)=一天中的温度，定义域是0≤t≤24小时，值域是24≤f(t)≤33°C。"
            },
            {
                "id": "graphing",
                "type": "text",
                "title": "Drawing Graphs",
                "title_zh": "绘制图形",
                "content": "Plot points by substituting x values into function. Join points smoothly for linear/quadratic functions. Example: Graph Singapore MRT crowd levels by time of day.",
                "content_zh": "通过将x值代入函数绘制点。对于线性/二次函数平滑连接点。例如：绘制新加坡地铁客流量随时间变化的图形。"
            }
        ],
        "exercises": []
    },

    {
        "id": "inequalities-sec2",
        "gradeLevel": "sec2",
        "title": "Linear Inequalities",
        "title_zh": "线性不等式",
        "description": "Solving and graphing linear inequalities",
        "description_zh": "求解和绘制线性不等式",
        "tag": "Algebra",
        "tag_zh": "代数",
        "objectives": [
            "Solve linear inequalities",
            "Represent solutions on number line",
            "Solve simultaneous linear inequalities",
            "Apply to real-world constraints"
        ],
        "objectives_zh": [
            "求解线性不等式",
            "在数轴上表示解",
            "求解二元线性不等式组",
            "应用于实际约束条件"
        ],
        "sections": [
            {
                "id": "solving-inequalities",
                "type": "text",
                "title": "Solving Inequalities",
                "title_zh": "求解不等式",
                "content": "Solve like equations, but reverse inequality sign when multiplying/dividing by negative number. Example: Singapore student budget - if you have $50 and items cost $7 each, how many can you buy? 7x ≤ 50, x ≤ 7.14, so maximum 7 items.",
                "content_zh": "像方程一样求解，但乘除负数时反转不等号。例如：新加坡学生预算 - 如果你有50元，物品每件7元，能买多少？7x ≤ 50，x ≤ 7.14，所以最多7件。"
            },
            {
                "id": "number-line",
                "type": "text",
                "title": "Number Line Representation",
                "title_zh": "数轴表示",
                "content": "Use open circle (○) for < or >, closed circle (●) for ≤ or ≥. Shade region of solutions. For x > 3, open circle at 3, shade right.",
                "content_zh": "对于<或>使用空心圆（○），对于≤或≥使用实心圆（●）。阴影表示解的区域。对于x > 3，在3处空心圆，向右阴影。"
            },
            {
                "id": "applications",
                "type": "text",
                "title": "Real-World Applications",
                "title_zh": "实际应用",
                "content": "Inequalities model constraints: Singapore HDB income ceiling ($14,000/month for BTO), age restrictions (≥21 for marriage), speed limits (≤50 km/h in residential), temperature ranges (aircon 23-25°C).",
                "content_zh": "不等式模拟约束：新加坡组屋收入上限（预购组屋月收入≤$14,000）、年龄限制（结婚≥21岁）、速度限制（住宅区≤50 km/h）、温度范围（空调23-25°C）。"
            }
        ],
        "exercises": []
    },

    {
        "id": "indices-sec2",
        "gradeLevel": "sec2",
        "title": "Indices (Index Notation)",
        "title_zh": "指数",
        "description": "Laws of indices and calculations with powers",
        "description_zh": "指数定律和幂的计算",
        "tag": "Algebra",
        "tag_zh": "代数",
        "objectives": [
            "Apply laws of indices: aᵐ × aⁿ = aᵐ⁺ⁿ",
            "Understand negative and zero indices",
            "Simplify expressions with indices",
            "Apply to scientific notation"
        ],
        "objectives_zh": [
            "应用指数定律：aᵐ × aⁿ = aᵐ⁺ⁿ",
            "理解负指数和零指数",
            "化简指数表达式",
            "应用于科学记数法"
        ],
        "sections": [
            {
                "id": "laws-of-indices",
                "type": "text",
                "title": "Laws of Indices",
                "title_zh": "指数定律",
                "content": "Key laws: aᵐ × aⁿ = aᵐ⁺ⁿ, aᵐ ÷ aⁿ = aᵐ⁻ⁿ, (aᵐ)ⁿ = aᵐⁿ, a⁰ = 1, a⁻ⁿ = 1/aⁿ. Singapore application: exponential growth of population (5.7 million in 2023).",
                "content_zh": "关键定律：aᵐ × aⁿ = aᵐ⁺ⁿ，aᵐ ÷ aⁿ = aᵐ⁻ⁿ，(aᵐ)ⁿ = aᵐⁿ，a⁰ = 1，a⁻ⁿ = 1/aⁿ。新加坡应用：人口指数增长（2023年570万）。"
            },
            {
                "id": "negative-zero-indices",
                "type": "text",
                "title": "Negative and Zero Indices",
                "title_zh": "负指数和零指数",
                "content": "Any number to power 0 equals 1: 5⁰=1. Negative power is reciprocal: 2⁻³ = 1/2³ = 1/8. Used in Singapore science: measuring small quantities in labs.",
                "content_zh": "任何数的0次方等于1：5⁰=1。负指数是倒数：2⁻³ = 1/2³ = 1/8。用于新加坡科学：实验室测量微小量。"
            },
            {
                "id": "scientific-notation",
                "type": "text",
                "title": "Scientific Notation",
                "title_zh": "科学记数法",
                "content": "Write large/small numbers as a × 10ⁿ where 1≤a<10. Singapore examples: Area = 733.1 km² = 7.331 × 10² km², Population density = 8,000/km² = 8 × 10³/km².",
                "content_zh": "将大/小数字写成a × 10ⁿ，其中1≤a<10。新加坡例子：面积 = 733.1 km² = 7.331 × 10² km²，人口密度 = 8,000/km² = 8 × 10³/km²。"
            }
        ],
        "exercises": []
    },

    # GEOMETRY (5 chapters)
    {
        "id": "congruence-similarity-sec2",
        "gradeLevel": "sec2",
        "title": "Congruence and Similarity",
        "title_zh": "全等与相似",
        "description": "Congruent and similar triangles, scale drawings",
        "description_zh": "全等三角形和相似三角形，比例绘图",
        "tag": "Geometry",
        "tag_zh": "几何",
        "objectives": [
            "Identify congruent triangles (SSS, SAS, ASA, RHS)",
            "Identify similar triangles (AAA, SAS)",
            "Use properties to solve problems",
            "Apply to scale drawings and maps"
        ],
        "objectives_zh": [
            "识别全等三角形（SSS、SAS、ASA、RHS）",
            "识别相似三角形（AAA、SAS）",
            "使用性质解决问题",
            "应用于比例绘图和地图"
        ],
        "sections": [
            {
                "id": "congruent-triangles",
                "type": "text",
                "title": "Congruent Triangles",
                "title_zh": "全等三角形",
                "content": "Triangles are congruent if same shape and size. Tests: SSS (3 sides equal), SAS (2 sides and included angle), ASA (2 angles and included side), RHS (right angle, hypotenuse, side). Singapore construction: ensuring HDB building frames are identical.",
                "content_zh": "三角形形状和大小相同则全等。判定：SSS（三边相等）、SAS（两边及夹角）、ASA（两角及夹边）、RHS（直角、斜边、边）。新加坡建筑：确保组屋建筑框架相同。"
            },
            {
                "id": "similar-triangles",
                "type": "text",
                "title": "Similar Triangles",
                "title_zh": "相似三角形",
                "content": "Triangles are similar if same shape but different size. Tests: AAA (3 angles equal), SAS (2 sides proportional with equal included angle). Corresponding sides are proportional. Example: Scale models of Singapore landmarks.",
                "content_zh": "三角形形状相同但大小不同则相似。判定：AAA（三角相等）、SAS（两边成比例且夹角相等）。对应边成比例。例如：新加坡地标的比例模型。"
            },
            {
                "id": "scale-drawings",
                "type": "text",
                "title": "Scale Drawings",
                "title_zh": "比例绘图",
                "content": "Scale 1:n means drawing is 1/n of actual size. Scale 1:50000 on Singapore map means 1 cm = 0.5 km. Used in HDB floor plans, MRT network maps.",
                "content_zh": "比例1:n表示图形是实际大小的1/n。新加坡地图上1:50000表示1厘米 = 0.5公里。用于组屋平面图、地铁网络图。"
            }
        ],
        "exercises": []
    },

    {
        "id": "pythagoras-theorem-sec2",
        "gradeLevel": "sec2",
        "title": "Pythagoras' Theorem",
        "title_zh": "勾股定理",
        "description": "Application of Pythagoras' theorem in 2D and 3D",
        "description_zh": "勾股定理在二维和三维中的应用",
        "tag": "Geometry",
        "tag_zh": "几何",
        "objectives": [
            "Apply Pythagoras' theorem: a²+b²=c²",
            "Find unknown sides in right-angled triangles",
            "Solve problems in 3D shapes",
            "Apply to real-world Singapore contexts"
        ],
        "objectives_zh": [
            "应用勾股定理：a²+b²=c²",
            "求直角三角形中的未知边",
            "解决三维形状中的问题",
            "应用于新加坡实际情境"
        ],
        "sections": [
            {
                "id": "pythagoras-2d",
                "type": "text",
                "title": "Pythagoras in 2D",
                "title_zh": "二维勾股定理",
                "content": "For right-angled triangle: a²+b²=c² where c is hypotenuse. Find missing side: rearrange formula. Example: Calculate diagonal distance across rectangular HDB void deck, or shortest path across Singapore Botanic Gardens rectangular lawn.",
                "content_zh": "对于直角三角形：a²+b²=c²，其中c是斜边。求缺边：重排公式。例如：计算组屋空地矩形对角线距离，或穿过新加坡植物园矩形草坪的最短路径。"
            },
            {
                "id": "pythagoras-3d",
                "type": "text",
                "title": "Pythagoras in 3D",
                "title_zh": "三维勾股定理",
                "content": "For cuboid with length l, width w, height h: diagonal d² = l²+w²+h². Apply twice: first find base diagonal, then use with height. Example: HDB room corner to opposite corner distance, or lift cable length.",
                "content_zh": "对于长方体，长l、宽w、高h：对角线d² = l²+w²+h²。应用两次：先求底面对角线，再与高度使用。例如：组屋房间角到对角的距离，或电梯电缆长度。"
            },
            {
                "id": "applications",
                "type": "text",
                "title": "Real-World Applications",
                "title_zh": "实际应用",
                "content": "Pythagoras used in: Singapore construction (checking if corners are 90°), navigation (shortest distance between MRT stations), surveying (measuring building heights), sports (calculating field dimensions).",
                "content_zh": "勾股定理用于：新加坡建筑（检查角是否为90°）、导航（地铁站之间的最短距离）、测量（测量建筑物高度）、体育（计算场地尺寸）。"
            }
        ],
        "exercises": []
    },

    {
        "id": "circle-properties-sec2",
        "gradeLevel": "sec2",
        "title": "Properties of Circles",
        "title_zh": "圆的性质",
        "description": "Circle theorems, arc, chord, and tangent properties",
        "description_zh": "圆定理、弧、弦和切线性质",
        "tag": "Geometry",
        "tag_zh": "几何",
        "objectives": [
            "Understand circle terminology",
            "Apply angle properties in circles",
            "Use chord and tangent properties",
            "Solve problems involving circles"
        ],
        "objectives_zh": [
            "理解圆的术语",
            "应用圆中的角性质",
            "使用弦和切线性质",
            "解决涉及圆的问题"
        ],
        "sections": [
            {
                "id": "circle-parts",
                "type": "text",
                "title": "Parts of a Circle",
                "title_zh": "圆的各部分",
                "content": "Radius: center to circumference. Diameter: 2 × radius, passes through center. Chord: line joining two points on circle. Arc: part of circumference. Tangent: line touching circle at one point. Example: Singapore's roundabouts (circular roads).",
                "content_zh": "半径：圆心到圆周。直径：2 × 半径，通过圆心。弦：连接圆上两点的线。弧：圆周的一部分。切线：在一点接触圆的线。例如：新加坡的环岛（圆形道路）。"
            },
            {
                "id": "angle-properties",
                "type": "text",
                "title": "Angle Properties",
                "title_zh": "角的性质",
                "content": "Key theorems: Angle in semicircle = 90°. Angles in same segment are equal. Angle at center = 2 × angle at circumference. Used in Singapore: designing circular gardens, roundabouts, observation wheel (Singapore Flyer).",
                "content_zh": "关键定理：半圆上的角 = 90°。同弧所对的圆周角相等。圆心角 = 2 × 圆周角。用于新加坡：设计圆形花园、环岛、观景轮（新加坡摩天观景轮）。"
            },
            {
                "id": "tangent-properties",
                "type": "text",
                "title": "Tangent Properties",
                "title_zh": "切线性质",
                "content": "Tangent perpendicular to radius at point of contact. Two tangents from external point are equal length. Example: Singapore cable car routes touch circular supports, wheel spokes perpendicular to rim.",
                "content_zh": "切线在切点处垂直于半径。从外部点引的两条切线长度相等。例如：新加坡缆车路线接触圆形支架，车轮辐条垂直于边缘。"
            }
        ],
        "exercises": []
    },

    {
        "id": "mensuration-2d-sec2",
        "gradeLevel": "sec2",
        "title": "Mensuration: Area & Perimeter",
        "title_zh": "测量：面积和周长",
        "description": "Advanced area and perimeter of composite shapes",
        "description_zh": "复合图形的高级面积和周长",
        "tag": "Geometry",
        "tag_zh": "几何",
        "objectives": [
            "Calculate area of trapezium, parallelogram",
            "Find area and circumference of circles",
            "Solve problems with composite shapes",
            "Apply to HDB floor plans and parks"
        ],
        "objectives_zh": [
            "计算梯形、平行四边形的面积",
            "求圆的面积和周长",
            "解决复合图形问题",
            "应用于组屋平面图和公园"
        ],
        "sections": [
            {
                "id": "quadrilaterals",
                "type": "text",
                "title": "Area of Quadrilaterals",
                "title_zh": "四边形的面积",
                "content": "Trapezium: A = ½(a+b)h where a, b are parallel sides, h is height. Parallelogram: A = base × height. Example: Singapore HDB multi-storey carpark ramps (trapezoidal), playground designs.",
                "content_zh": "梯形：A = ½(a+b)h，其中a、b是平行边，h是高。平行四边形：A = 底 × 高。例如：新加坡组屋多层停车场坡道（梯形）、游乐场设计。"
            },
            {
                "id": "circles",
                "type": "text",
                "title": "Circles: Area & Circumference",
                "title_zh": "圆：面积和周长",
                "content": "Circumference: C = 2πr or πd. Area: A = πr². For sectors: arc length = θ/360 × 2πr, sector area = θ/360 × πr². Singapore application: roundabout areas, circular gardens (Gardens by the Bay), fountain designs.",
                "content_zh": "周长：C = 2πr或πd。面积：A = πr²。对于扇形：弧长 = θ/360 × 2πr，扇形面积 = θ/360 × πr²。新加坡应用：环岛面积、圆形花园（滨海湾花园）、喷泉设计。"
            },
            {
                "id": "composite-shapes",
                "type": "text",
                "title": "Composite Shapes",
                "title_zh": "复合图形",
                "content": "Break complex shapes into simpler parts (rectangles, triangles, circles). Add/subtract areas. Example: HDB flat floor plans (L-shaped rooms), Singapore parks with mixed shapes.",
                "content_zh": "将复杂形状分解为简单部分（矩形、三角形、圆形）。加减面积。例如：组屋平面图（L形房间）、新加坡混合形状的公园。"
            }
        ],
        "exercises": []
    },

    {
        "id": "mensuration-3d-sec2",
        "gradeLevel": "sec2",
        "title": "Mensuration: Volume & Surface Area",
        "title_zh": "测量：体积和表面积",
        "description": "Volume and surface area of prisms, cylinders, pyramids, cones, spheres",
        "description_zh": "棱柱、圆柱、棱锥、圆锥、球的体积和表面积",
        "tag": "Geometry",
        "tag_zh": "几何",
        "objectives": [
            "Calculate volume and surface area of prisms",
            "Find volume and surface area of cylinders",
            "Calculate for pyramids, cones, and spheres",
            "Apply to Singapore water tanks, buildings"
        ],
        "objectives_zh": [
            "计算棱柱的体积和表面积",
            "求圆柱的体积和表面积",
            "计算棱锥、圆锥和球",
            "应用于新加坡水箱、建筑物"
        ],
        "sections": [
            {
                "id": "prisms-cylinders",
                "type": "text",
                "title": "Prisms and Cylinders",
                "title_zh": "棱柱和圆柱",
                "content": "Prism: V = base area × height. Cylinder: V = πr²h, Surface area = 2πr² + 2πrh. Singapore examples: HDB water tanks (cylindrical), rectangular storage rooms, MRT tunnels.",
                "content_zh": "棱柱：V = 底面积 × 高。圆柱：V = πr²h，表面积 = 2πr² + 2πrh。新加坡例子：组屋水箱（圆柱形）、矩形储藏室、地铁隧道。"
            },
            {
                "id": "pyramids-cones",
                "type": "text",
                "title": "Pyramids and Cones",
                "title_zh": "棱锥和圆锥",
                "content": "Pyramid: V = ⅓ × base area × height. Cone: V = ⅓πr²h, Surface area = πr² + πrl (l=slant height). Example: Singapore roof designs, traffic cones, decorative structures.",
                "content_zh": "棱锥：V = ⅓ × 底面积 × 高。圆锥：V = ⅓πr²h，表面积 = πr² + πrl（l=斜高）。例如：新加坡屋顶设计、交通锥、装饰结构。"
            },
            {
                "id": "spheres",
                "type": "text",
                "title": "Spheres",
                "title_zh": "球",
                "content": "Volume: V = ⁴⁄₃πr³. Surface area: A = 4πr². Singapore applications: dome structures (Science Centre), spherical water tanks, globe at Esplanade, sports balls.",
                "content_zh": "体积：V = ⁴⁄₃πr³。表面积：A = 4πr²。新加坡应用：圆顶结构（科学中心）、球形水箱、滨海艺术中心地球仪、运动球。"
            }
        ],
        "exercises": []
    },

    # STATISTICS & PROBABILITY (3 chapters)
    {
        "id": "data-analysis-sec2",
        "gradeLevel": "sec2",
        "title": "Data Analysis & Statistics",
        "title_zh": "数据分析与统计",
        "description": "Mean, median, mode, range, and interpreting data",
        "description_zh": "均值、中位数、众数、极差和数据解释",
        "tag": "Statistics",
        "tag_zh": "统计",
        "objectives": [
            "Calculate mean, median, mode, range",
            "Interpret and compare data sets",
            "Draw and interpret statistical charts",
            "Apply to Singapore data (population, weather)"
        ],
        "objectives_zh": [
            "计算均值、中位数、众数、极差",
            "解释和比较数据集",
            "绘制和解释统计图表",
            "应用于新加坡数据（人口、天气）"
        ],
        "sections": [
            {
                "id": "measures-central-tendency",
                "type": "text",
                "title": "Measures of Central Tendency",
                "title_zh": "集中趋势的度量",
                "content": "Mean: sum ÷ count. Median: middle value when ordered. Mode: most frequent value. Example: Average temperature in Singapore (mean 28°C), median HDB resale price, most common family size (mode).",
                "content_zh": "均值：总和 ÷ 数量。中位数：排序后的中间值。众数：最频繁的值。例如：新加坡平均温度（均值28°C）、组屋转售价格中位数、最常见家庭规模（众数）。"
            },
            {
                "id": "range-spread",
                "type": "text",
                "title": "Range and Spread",
                "title_zh": "极差和分布",
                "content": "Range: highest - lowest value. Measures spread of data. Large range = more variation. Example: Singapore daily temperature range (24-33°C = 9°C range), exam scores range.",
                "content_zh": "极差：最高值 - 最低值。测量数据分布。大极差 = 更多变化。例如：新加坡日温差（24-33°C = 9°C极差）、考试分数极差。"
            },
            {
                "id": "charts-graphs",
                "type": "text",
                "title": "Statistical Charts",
                "title_zh": "统计图表",
                "content": "Bar charts: compare categories. Pie charts: show proportions. Line graphs: show trends over time. Example: Singapore population growth chart, ethnic composition pie chart, MRT ridership trends.",
                "content_zh": "条形图：比较类别。饼图：显示比例。折线图：显示随时间的趋势。例如：新加坡人口增长图表、种族组成饼图、地铁乘客量趋势。"
            }
        ],
        "exercises": []
    },

    {
        "id": "probability-sec2",
        "gradeLevel": "sec2",
        "title": "Probability",
        "title_zh": "概率",
        "description": "Basic probability, combined events, and probability trees",
        "description_zh": "基本概率、复合事件和概率树",
        "tag": "Statistics",
        "tag_zh": "统计",
        "objectives": [
            "Calculate probability of single events",
            "Find probability of combined events",
            "Use probability trees",
            "Apply to real-world situations"
        ],
        "objectives_zh": [
            "计算单一事件的概率",
            "求复合事件的概率",
            "使用概率树",
            "应用于实际情况"
        ],
        "sections": [
            {
                "id": "basic-probability",
                "type": "text",
                "title": "Basic Probability",
                "title_zh": "基本概率",
                "content": "Probability = favorable outcomes ÷ total outcomes. Value between 0 (impossible) and 1 (certain). Example: Probability of rain in Singapore (high in Nov-Jan), probability of bus arriving within 5 min.",
                "content_zh": "概率 = 有利结果 ÷ 总结果。值在0（不可能）和1（确定）之间。例如：新加坡下雨的概率（11-1月高）、5分钟内公交车到达的概率。"
            },
            {
                "id": "combined-events",
                "type": "text",
                "title": "Combined Events",
                "title_zh": "复合事件",
                "content": "AND: multiply probabilities (P(A and B) = P(A) × P(B) if independent). OR: add probabilities (P(A or B) = P(A) + P(B) if mutually exclusive). Example: Probability of catching both MRT and bus on time.",
                "content_zh": "与：乘概率（如果独立，P(A且B) = P(A) × P(B)）。或：加概率（如果互斥，P(A或B) = P(A) + P(B)）。例如：地铁和公交车都准点的概率。"
            },
            {
                "id": "probability-trees",
                "type": "text",
                "title": "Probability Trees",
                "title_zh": "概率树",
                "content": "Tree diagrams show all possible outcomes with probabilities on branches. Multiply along branches for final probability. Example: Singapore weather forecasts (sunny/rainy over multiple days).",
                "content_zh": "树形图显示所有可能结果，分支上标概率。沿分支相乘得最终概率。例如：新加坡天气预报（多日晴天/雨天）。"
            }
        ],
        "exercises": []
    },

    {
        "id": "sets-venn-diagrams-sec2",
        "gradeLevel": "sec2",
        "title": "Sets and Venn Diagrams",
        "title_zh": "集合与维恩图",
        "description": "Set notation, operations, and Venn diagrams",
        "description_zh": "集合符号、运算和维恩图",
        "tag": "Statistics",
        "tag_zh": "统计",
        "objectives": [
            "Use set notation and vocabulary",
            "Perform set operations (union, intersection)",
            "Draw and interpret Venn diagrams",
            "Solve problems using sets"
        ],
        "objectives_zh": [
            "使用集合符号和词汇",
            "执行集合运算（并集、交集）",
            "绘制和解释维恩图",
            "使用集合解决问题"
        ],
        "sections": [
            {
                "id": "set-notation",
                "type": "text",
                "title": "Set Notation",
                "title_zh": "集合符号",
                "content": "Set: collection of objects. Element: ∈ (belongs to). Subset: ⊆. Empty set: ∅. Example: Set of Singapore MRT lines = {Red, Green, Purple, Yellow, Blue, Brown, Grey}, set of primes < 10 = {2,3,5,7}.",
                "content_zh": "集合：对象的集合。元素：∈（属于）。子集：⊆。空集：∅。例如：新加坡地铁线路集合 = {红、绿、紫、黄、蓝、棕、灰}，小于10的质数集合 = {2,3,5,7}。"
            },
            {
                "id": "set-operations",
                "type": "text",
                "title": "Set Operations",
                "title_zh": "集合运算",
                "content": "Union A∪B: all elements in A or B. Intersection A∩B: elements in both A and B. Complement A': elements not in A. Example: Students taking Math ∪ Science, students in both Chess ∩ Robotics clubs.",
                "content_zh": "并集A∪B：A或B中的所有元素。交集A∩B：同时在A和B中的元素。补集A'：不在A中的元素。例如：选数学∪科学的学生，同时参加国际象棋∩机器人俱乐部的学生。"
            },
            {
                "id": "venn-diagrams",
                "type": "text",
                "title": "Venn Diagrams",
                "title_zh": "维恩图",
                "content": "Visual representation of sets using overlapping circles. Overlap shows intersection. Use to solve problems with 2-3 sets. Example: Singapore students studying Mandarin, Malay, Tamil; students playing football, basketball.",
                "content_zh": "使用重叠圆圈直观表示集合。重叠显示交集。用于解决2-3个集合的问题。例如：学习华语、马来语、泰米尔语的新加坡学生；踢足球、打篮球的学生。"
            }
        ],
        "exercises": []
    }
]

print(f"📚 Creating {len(sec2_math_chapters)} Secondary 2 Mathematics chapters...")
print(f"   Algebra: {sum(1 for ch in sec2_math_chapters if ch['tag'] == 'Algebra')}")
print(f"   Geometry: {sum(1 for ch in sec2_math_chapters if ch['tag'] == 'Geometry')}")
print(f"   Statistics: {sum(1 for ch in sec2_math_chapters if ch['tag'] == 'Statistics')}")

# Save chapters
output_file = "chapters/math-sec2-chapters.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(sec2_math_chapters, f, indent=2, ensure_ascii=False)

print(f"\n✅ Created {len(sec2_math_chapters)} chapters")
print(f"📁 Saved to: {output_file}")
print(f"\n⚠️ Note: Exercises need to be added separately")
