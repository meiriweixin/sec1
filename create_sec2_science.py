"""
Generate Secondary 2 Science chapters following Singapore MOE syllabus.
Based on Sec 1 structure: 15 exercises per chapter, 2-9 sections per chapter.
"""

import json
from datetime import datetime

# Secondary 2 Science chapters based on MOE syllabus
sec2_science_chapters = [
    # CHEMISTRY (5 chapters)
    {
        "id": "chemical-changes-sec2",
        "gradeLevel": "sec2",
        "title": "Chemical Changes",
        "title_zh": "化学变化",
        "description": "Physical vs chemical changes, signs of chemical reactions",
        "description_zh": "物理变化与化学变化、化学反应的迹象",
        "tag": "Chemistry",
        "tag_zh": "化学",
        "objectives": [
            "Distinguish between physical and chemical changes",
            "Identify signs of chemical reactions",
            "Understand conservation of mass",
            "Write word equations for simple reactions"
        ],
        "objectives_zh": [
            "区分物理变化和化学变化",
            "识别化学反应的迹象",
            "理解质量守恒",
            "为简单反应写出文字方程式"
        ]
    },
    {
        "id": "oxidation-reduction-sec2",
        "gradeLevel": "sec2",
        "title": "Oxidation & Reduction",
        "title_zh": "氧化与还原",
        "description": "Combustion, rusting, and redox reactions",
        "description_zh": "燃烧、生锈和氧化还原反应",
        "tag": "Chemistry",
        "tag_zh": "化学",
        "objectives": [
            "Define oxidation and reduction",
            "Explain the process of rusting",
            "Describe combustion reactions",
            "Identify oxidizing and reducing agents"
        ],
        "objectives_zh": [
            "定义氧化和还原",
            "解释生锈过程",
            "描述燃烧反应",
            "识别氧化剂和还原剂"
        ]
    },
    {
        "id": "rate-of-reaction-sec2",
        "gradeLevel": "sec2",
        "title": "Rate of Reaction",
        "title_zh": "反应速率",
        "description": "Factors affecting reaction rates: temperature, concentration, surface area, catalyst",
        "description_zh": "影响反应速率的因素：温度、浓度、表面积、催化剂",
        "tag": "Chemistry",
        "tag_zh": "化学",
        "objectives": [
            "Define rate of reaction",
            "Explain how temperature affects reaction rate",
            "Describe the effect of concentration and surface area",
            "Understand the role of catalysts"
        ],
        "objectives_zh": [
            "定义反应速率",
            "解释温度如何影响反应速率",
            "描述浓度和表面积的影响",
            "理解催化剂的作用"
        ]
    },
    {
        "id": "reactivity-series-sec2",
        "gradeLevel": "sec2",
        "title": "Reactivity Series of Metals",
        "title_zh": "金属活动性顺序",
        "description": "Comparing reactivity of metals, displacement reactions",
        "description_zh": "比较金属的活动性、置换反应",
        "tag": "Chemistry",
        "tag_zh": "化学",
        "objectives": [
            "Arrange metals in order of reactivity",
            "Predict displacement reactions",
            "Relate reactivity to extraction methods",
            "Explain reactions with water, acids, and oxygen"
        ],
        "objectives_zh": [
            "按活动性顺序排列金属",
            "预测置换反应",
            "将活动性与提取方法联系起来",
            "解释与水、酸和氧气的反应"
        ]
    },
    {
        "id": "chemical-bonding-sec2",
        "gradeLevel": "sec2",
        "title": "Chemical Bonding",
        "title_zh": "化学键",
        "description": "Ionic and covalent bonding, properties of compounds",
        "description_zh": "离子键和共价键、化合物的性质",
        "tag": "Chemistry",
        "tag_zh": "化学",
        "objectives": [
            "Describe ionic bonding",
            "Describe covalent bonding",
            "Compare properties of ionic and covalent compounds",
            "Draw simple electron diagrams"
        ],
        "objectives_zh": [
            "描述离子键",
            "描述共价键",
            "比较离子化合物和共价化合物的性质",
            "绘制简单的电子图"
        ]
    },

    # PHYSICS (5 chapters)
    {
        "id": "work-energy-power-sec2",
        "gradeLevel": "sec2",
        "title": "Work, Energy & Power",
        "title_zh": "功、能量和功率",
        "description": "Work done, energy transformations, power calculations",
        "description_zh": "做功、能量转换、功率计算",
        "tag": "Physics",
        "tag_zh": "物理",
        "objectives": [
            "Define work, energy, and power",
            "Calculate work done and power",
            "Apply principle of conservation of energy",
            "Identify energy transformations in Singapore context (MRT, HDB lifts)"
        ],
        "objectives_zh": [
            "定义功、能量和功率",
            "计算功和功率",
            "应用能量守恒原理",
            "识别新加坡环境中的能量转换（地铁、组屋电梯）"
        ]
    },
    {
        "id": "moments-sec2",
        "gradeLevel": "sec2",
        "title": "Moments & Levers",
        "title_zh": "力矩与杠杆",
        "description": "Turning effect of forces, principle of moments",
        "description_zh": "力的转动效应、力矩原理",
        "tag": "Physics",
        "tag_zh": "物理",
        "objectives": [
            "Define moment of a force",
            "Apply principle of moments",
            "Solve problems on levers and balance",
            "Identify everyday applications (see-saw, door handles)"
        ],
        "objectives_zh": [
            "定义力矩",
            "应用力矩原理",
            "解决杠杆和平衡问题",
            "识别日常应用（跷跷板、门把手）"
        ]
    },
    {
        "id": "kinetic-particle-theory-sec2",
        "gradeLevel": "sec2",
        "title": "Kinetic Particle Theory",
        "title_zh": "分子动理论",
        "description": "States of matter, changes of state, gas pressure",
        "description_zh": "物质的状态、状态变化、气体压强",
        "tag": "Physics",
        "tag_zh": "物理",
        "objectives": [
            "Describe kinetic particle model for solids, liquids, gases",
            "Explain changes of state",
            "Relate gas pressure to particle collisions",
            "Apply to Singapore's humidity and weather patterns"
        ],
        "objectives_zh": [
            "描述固体、液体、气体的分子动理论模型",
            "解释状态变化",
            "将气体压强与粒子碰撞联系起来",
            "应用于新加坡的湿度和天气模式"
        ]
    },
    {
        "id": "sound-sec2",
        "gradeLevel": "sec2",
        "title": "Sound",
        "title_zh": "声音",
        "description": "Production and transmission of sound, wave properties",
        "description_zh": "声音的产生和传播、波的性质",
        "tag": "Physics",
        "tag_zh": "物理",
        "objectives": [
            "Explain how sound is produced and transmitted",
            "Describe properties of sound waves",
            "Relate frequency to pitch and amplitude to loudness",
            "Understand noise pollution in urban Singapore"
        ],
        "objectives_zh": [
            "解释声音如何产生和传播",
            "描述声波的性质",
            "将频率与音调、振幅与响度联系起来",
            "理解新加坡城市的噪音污染"
        ]
    },
    {
        "id": "magnetism-sec2",
        "gradeLevel": "sec2",
        "title": "Magnetism",
        "title_zh": "磁学",
        "description": "Magnetic materials, magnetic fields, electromagnets",
        "description_zh": "磁性材料、磁场、电磁铁",
        "tag": "Physics",
        "tag_zh": "物理",
        "objectives": [
            "Identify magnetic and non-magnetic materials",
            "Describe magnetic field patterns",
            "Explain how electromagnets work",
            "Understand applications in MRT systems"
        ],
        "objectives_zh": [
            "识别磁性和非磁性材料",
            "描述磁场模式",
            "解释电磁铁的工作原理",
            "理解在地铁系统中的应用"
        ]
    },

    # BIOLOGY (5 chapters)
    {
        "id": "photosynthesis-sec2",
        "gradeLevel": "sec2",
        "title": "Photosynthesis",
        "title_zh": "光合作用",
        "description": "Process of photosynthesis, factors affecting rate, importance",
        "description_zh": "光合作用过程、影响速率的因素、重要性",
        "tag": "Biology",
        "tag_zh": "生物",
        "objectives": [
            "Describe the process of photosynthesis",
            "Write the word equation for photosynthesis",
            "Identify factors affecting photosynthesis rate",
            "Explain importance for Singapore's green spaces"
        ],
        "objectives_zh": [
            "描述光合作用过程",
            "写出光合作用的文字方程式",
            "识别影响光合作用速率的因素",
            "解释对新加坡绿色空间的重要性"
        ]
    },
    {
        "id": "transport-plants-sec2",
        "gradeLevel": "sec2",
        "title": "Transport in Plants",
        "title_zh": "植物中的运输",
        "description": "Xylem, phloem, transpiration, water uptake",
        "description_zh": "木质部、韧皮部、蒸腾作用、水分吸收",
        "tag": "Biology",
        "tag_zh": "生物",
        "objectives": [
            "Describe structure and function of xylem and phloem",
            "Explain transpiration process",
            "Identify factors affecting transpiration rate",
            "Relate to tropical plants in Singapore's climate"
        ],
        "objectives_zh": [
            "描述木质部和韧皮部的结构和功能",
            "解释蒸腾作用过程",
            "识别影响蒸腾速率的因素",
            "与新加坡气候中的热带植物联系起来"
        ]
    },
    {
        "id": "respiration-sec2",
        "gradeLevel": "sec2",
        "title": "Respiration",
        "title_zh": "呼吸作用",
        "description": "Aerobic and anaerobic respiration, energy release",
        "description_zh": "有氧呼吸和无氧呼吸、能量释放",
        "tag": "Biology",
        "tag_zh": "生物",
        "objectives": [
            "Compare aerobic and anaerobic respiration",
            "Write word equations for both types",
            "Explain energy release in cells",
            "Apply to exercise and Singapore's hot climate"
        ],
        "objectives_zh": [
            "比较有氧呼吸和无氧呼吸",
            "写出两种类型的文字方程式",
            "解释细胞中的能量释放",
            "应用于运动和新加坡的炎热气候"
        ]
    },
    {
        "id": "human-transport-sec2",
        "gradeLevel": "sec2",
        "title": "Human Transport System",
        "title_zh": "人体运输系统",
        "description": "Blood, blood vessels, heart, circulation",
        "description_zh": "血液、血管、心脏、循环",
        "tag": "Biology",
        "tag_zh": "生物",
        "objectives": [
            "Describe components and functions of blood",
            "Compare arteries, veins, and capillaries",
            "Explain the structure and function of the heart",
            "Understand health implications in Singapore's aging population"
        ],
        "objectives_zh": [
            "描述血液的成分和功能",
            "比较动脉、静脉和毛细血管",
            "解释心脏的结构和功能",
            "理解新加坡老龄化人口的健康影响"
        ]
    },
    {
        "id": "coordination-response-sec2",
        "gradeLevel": "sec2",
        "title": "Coordination & Response",
        "title_zh": "协调与反应",
        "description": "Nervous system, hormones, homeostasis",
        "description_zh": "神经系统、激素、稳态",
        "tag": "Biology",
        "tag_zh": "生物",
        "objectives": [
            "Describe the structure of the nervous system",
            "Explain reflex actions",
            "Compare nervous and hormonal coordination",
            "Understand homeostasis and temperature regulation in tropical climate"
        ],
        "objectives_zh": [
            "描述神经系统的结构",
            "解释反射动作",
            "比较神经协调和激素协调",
            "理解热带气候中的稳态和温度调节"
        ]
    }
]

def create_sections_for_chapter(chapter_data):
    """Create 2-9 sections per chapter based on topic"""
    chapter_id = chapter_data["id"]

    sections_map = {
        "chemical-changes-sec2": [
            {
                "id": "physical-vs-chemical",
                "type": "text",
                "title": "Physical vs Chemical Changes",
                "title_zh": "物理变化与化学变化",
                "content": "Physical changes involve changes in state or appearance without forming new substances (e.g., melting ice). Chemical changes form new substances with different properties (e.g., burning wood).",
                "content_zh": "物理变化涉及状态或外观的变化，但不形成新物质（例如，冰融化）。化学变化形成具有不同性质的新物质（例如，木材燃烧）。"
            },
            {
                "id": "signs-reactions",
                "type": "text",
                "title": "Signs of Chemical Reactions",
                "title_zh": "化学反应的迹象",
                "content": "Signs include: color change, gas production (bubbles), precipitate formation, temperature change, and light emission. In Singapore's humid climate, rusting of metal structures is a common chemical change.",
                "content_zh": "迹象包括：颜色变化、产生气体（气泡）、形成沉淀、温度变化和发光。在新加坡的潮湿气候中，金属结构的生锈是常见的化学变化。"
            },
            {
                "id": "conservation-mass",
                "type": "text",
                "title": "Conservation of Mass",
                "title_zh": "质量守恒",
                "content": "In a chemical reaction, the total mass of reactants equals the total mass of products. No atoms are created or destroyed, only rearranged.",
                "content_zh": "在化学反应中，反应物的总质量等于生成物的总质量。没有原子被创造或破坏，只是重新排列。"
            }
        ],
        "oxidation-reduction-sec2": [
            {
                "id": "oxidation-definition",
                "type": "text",
                "title": "What is Oxidation?",
                "title_zh": "什么是氧化？",
                "content": "Oxidation is the gain of oxygen or loss of electrons. Examples: rusting of iron (common in Singapore's coastal areas), burning of fuels.",
                "content_zh": "氧化是获得氧或失去电子。例如：铁的生锈（在新加坡沿海地区很常见）、燃料的燃烧。"
            },
            {
                "id": "reduction-definition",
                "type": "text",
                "title": "What is Reduction?",
                "title_zh": "什么是还原？",
                "content": "Reduction is the loss of oxygen or gain of electrons. Oxidation and reduction always occur together in redox reactions.",
                "content_zh": "还原是失去氧或获得电子。氧化和还原总是在氧化还原反应中同时发生。"
            },
            {
                "id": "combustion",
                "type": "text",
                "title": "Combustion",
                "title_zh": "燃烧",
                "content": "Combustion is rapid oxidation producing heat and light. Complete combustion of hydrocarbons produces CO₂ and H₂O. Incomplete combustion produces CO (toxic) and soot.",
                "content_zh": "燃烧是产生热和光的快速氧化。碳氢化合物的完全燃烧产生CO₂和H₂O。不完全燃烧产生CO（有毒）和烟灰。"
            },
            {
                "id": "rusting",
                "type": "text",
                "title": "Rusting of Iron",
                "title_zh": "铁的生锈",
                "content": "Iron rusts when exposed to oxygen and water, forming hydrated iron(III) oxide. Singapore's high humidity accelerates rusting. Prevention methods: painting, oiling, galvanizing.",
                "content_zh": "铁暴露于氧气和水时会生锈，形成水合氧化铁(III)。新加坡的高湿度加速了生锈。预防方法：涂漆、上油、镀锌。"
            }
        ],
        "rate-of-reaction-sec2": [
            {
                "id": "rate-definition",
                "type": "text",
                "title": "Rate of Reaction",
                "title_zh": "反应速率",
                "content": "Rate of reaction measures how fast reactants are used up or products are formed. It can be measured by volume of gas produced, mass change, or color change.",
                "content_zh": "反应速率测量反应物被消耗或产物形成的速度。可以通过产生的气体体积、质量变化或颜色变化来测量。"
            },
            {
                "id": "temperature-effect",
                "type": "text",
                "title": "Effect of Temperature",
                "title_zh": "温度的影响",
                "content": "Higher temperature increases reaction rate. Particles move faster, collide more frequently with greater energy. In Singapore's hot climate (avg 27-32°C), food spoils faster than in cooler countries.",
                "content_zh": "较高的温度增加反应速率。粒子移动更快，以更大的能量更频繁地碰撞。在新加坡的炎热气候（平均27-32°C）中，食物比在较冷的国家变质更快。"
            },
            {
                "id": "concentration-surface-area",
                "type": "text",
                "title": "Concentration & Surface Area",
                "title_zh": "浓度和表面积",
                "content": "Higher concentration and larger surface area increase reaction rate by providing more particles for collisions. Example: powdered sugar dissolves faster than sugar cubes.",
                "content_zh": "较高的浓度和较大的表面积通过提供更多的粒子进行碰撞来增加反应速率。例如：糖粉比方糖溶解得更快。"
            },
            {
                "id": "catalysts",
                "type": "text",
                "title": "Catalysts",
                "title_zh": "催化剂",
                "content": "Catalysts speed up reactions without being consumed. Enzymes are biological catalysts. Singapore's petrochemical industry uses catalysts extensively.",
                "content_zh": "催化剂在不被消耗的情况下加速反应。酶是生物催化剂。新加坡的石化工业广泛使用催化剂。"
            }
        ],
        "reactivity-series-sec2": [
            {
                "id": "reactivity-order",
                "type": "text",
                "title": "Reactivity Series",
                "title_zh": "金属活动性顺序",
                "content": "Metals in order of decreasing reactivity: Potassium > Sodium > Calcium > Magnesium > Aluminium > Zinc > Iron > Lead > Copper > Silver > Gold > Platinum",
                "content_zh": "金属按活动性递减顺序：钾 > 钠 > 钙 > 镁 > 铝 > 锌 > 铁 > 铅 > 铜 > 银 > 金 > 铂"
            },
            {
                "id": "displacement",
                "type": "text",
                "title": "Displacement Reactions",
                "title_zh": "置换反应",
                "content": "A more reactive metal can displace a less reactive metal from its compound. Example: Zinc + Copper sulfate → Zinc sulfate + Copper",
                "content_zh": "活动性较强的金属可以从其化合物中置换活动性较弱的金属。例如：锌 + 硫酸铜 → 硫酸锌 + 铜"
            },
            {
                "id": "metal-extraction",
                "type": "text",
                "title": "Metal Extraction",
                "title_zh": "金属提取",
                "content": "More reactive metals (above carbon) are extracted by electrolysis. Less reactive metals (below carbon) are extracted by reduction with carbon or found native.",
                "content_zh": "活动性较强的金属（碳以上）通过电解提取。活动性较弱的金属（碳以下）通过碳还原提取或以自然形式存在。"
            }
        ],
        "chemical-bonding-sec2": [
            {
                "id": "ionic-bonding",
                "type": "text",
                "title": "Ionic Bonding",
                "title_zh": "离子键",
                "content": "Ionic bonding involves transfer of electrons from metal to non-metal, forming positive and negative ions held together by electrostatic attraction. Example: NaCl (sodium chloride, table salt used in Singapore hawker food).",
                "content_zh": "离子键涉及电子从金属转移到非金属，形成通过静电吸引力结合在一起的正离子和负离子。例如：NaCl（氯化钠，新加坡小贩食品中使用的食盐）。"
            },
            {
                "id": "covalent-bonding",
                "type": "text",
                "title": "Covalent Bonding",
                "title_zh": "共价键",
                "content": "Covalent bonding involves sharing of electrons between non-metal atoms. Example: H₂O, CO₂, CH₄ (methane, natural gas used in Singapore homes).",
                "content_zh": "共价键涉及非金属原子之间的电子共享。例如：H₂O、CO₂、CH₄（甲烷，新加坡家庭使用的天然气）。"
            },
            {
                "id": "properties-comparison",
                "type": "text",
                "title": "Properties of Ionic vs Covalent",
                "title_zh": "离子化合物与共价化合物的性质",
                "content": "Ionic compounds: high melting points, conduct electricity when molten/dissolved, brittle. Covalent compounds: low melting points, don't conduct electricity, softer.",
                "content_zh": "离子化合物：高熔点、熔融/溶解时导电、脆。共价化合物：低熔点、不导电、较软。"
            }
        ],
        "work-energy-power-sec2": [
            {
                "id": "work-definition",
                "type": "text",
                "title": "Work Done",
                "title_zh": "功",
                "content": "Work done = Force × Distance moved in direction of force. Unit: Joule (J). Example: Lifting shopping bags up HDB stairs.",
                "content_zh": "功 = 力 × 在力的方向上移动的距离。单位：焦耳(J)。例如：将购物袋提上组屋楼梯。"
            },
            {
                "id": "energy-types",
                "type": "text",
                "title": "Forms of Energy",
                "title_zh": "能量的形式",
                "content": "Forms of energy: kinetic, potential (gravitational, elastic), thermal, chemical, electrical, nuclear, light, sound. Energy can transform but total amount is conserved.",
                "content_zh": "能量的形式：动能、势能（重力势能、弹性势能）、热能、化学能、电能、核能、光能、声能。能量可以转换，但总量守恒。"
            },
            {
                "id": "power-definition",
                "type": "text",
                "title": "Power",
                "title_zh": "功率",
                "content": "Power = Work done ÷ Time taken. Unit: Watt (W). 1 W = 1 J/s. Example: Singapore's MRT trains have high power motors for quick acceleration.",
                "content_zh": "功率 = 功 ÷ 时间。单位：瓦特(W)。1 W = 1 J/s。例如：新加坡地铁列车具有用于快速加速的高功率电机。"
            }
        ],
        "moments-sec2": [
            {
                "id": "moment-definition",
                "type": "text",
                "title": "Moment of a Force",
                "title_zh": "力矩",
                "content": "Moment = Force × Perpendicular distance from pivot. Unit: Newton-meter (Nm). The turning effect of a force. Example: Opening a door - easier to push far from hinges.",
                "content_zh": "力矩 = 力 × 从支点的垂直距离。单位：牛顿米(Nm)。力的转动效应。例如：开门 - 在远离铰链处推更容易。"
            },
            {
                "id": "principle-of-moments",
                "type": "text",
                "title": "Principle of Moments",
                "title_zh": "力矩原理",
                "content": "For a balanced object: Sum of clockwise moments = Sum of anticlockwise moments. Applications: see-saws, crowbars, scissors, wrenches.",
                "content_zh": "对于平衡的物体：顺时针力矩之和 = 逆时针力矩之和。应用：跷跷板、撬棍、剪刀、扳手。"
            },
            {
                "id": "center-of-gravity",
                "type": "text",
                "title": "Center of Gravity",
                "title_zh": "重心",
                "content": "The point where the entire weight of an object appears to act. Objects with low center of gravity are more stable (e.g., HDB blocks have wide bases).",
                "content_zh": "物体整个重量似乎作用的点。重心低的物体更稳定（例如，组屋有宽阔的基础）。"
            }
        ],
        "kinetic-particle-theory-sec2": [
            {
                "id": "particle-model",
                "type": "animation",
                "title": "States of Matter",
                "title_zh": "物质的状态",
                "content": "ParticlesInStates",
                "props": {"interactive": True}
            },
            {
                "id": "changes-of-state",
                "type": "text",
                "title": "Changes of State",
                "title_zh": "状态变化",
                "content": "Melting, freezing, evaporation, condensation, sublimation. During state changes, temperature remains constant. Singapore's high humidity (80-90%) means water evaporates slower.",
                "content_zh": "熔化、凝固、蒸发、凝结、升华。在状态变化期间，温度保持恒定。新加坡的高湿度（80-90%）意味着水蒸发较慢。"
            },
            {
                "id": "gas-pressure",
                "type": "text",
                "title": "Gas Pressure",
                "title_zh": "气体压强",
                "content": "Gas pressure is caused by collisions of gas particles with container walls. Pressure increases with: higher temperature, smaller volume, more particles.",
                "content_zh": "气体压强是由气体粒子与容器壁的碰撞引起的。压强随着以下因素增加：较高的温度、较小的体积、更多的粒子。"
            }
        ],
        "sound-sec2": [
            {
                "id": "sound-production",
                "type": "text",
                "title": "Production of Sound",
                "title_zh": "声音的产生",
                "content": "Sound is produced by vibrations. It travels as longitudinal waves requiring a medium (solid, liquid, or gas). Sound cannot travel through vacuum.",
                "content_zh": "声音由振动产生。它以纵波的形式传播，需要介质（固体、液体或气体）。声音不能在真空中传播。"
            },
            {
                "id": "sound-properties",
                "type": "text",
                "title": "Properties of Sound",
                "title_zh": "声音的性质",
                "content": "Frequency (Hz) determines pitch - high frequency = high pitch. Amplitude determines loudness - large amplitude = loud sound. Speed of sound in air ≈ 330 m/s.",
                "content_zh": "频率(Hz)决定音调 - 高频率 = 高音调。振幅决定响度 - 大振幅 = 大声。空气中的声速 ≈ 330 m/s。"
            },
            {
                "id": "noise-pollution",
                "type": "text",
                "title": "Noise Pollution",
                "title_zh": "噪音污染",
                "content": "Excessive noise (>85 dB) can damage hearing. Singapore's NEA monitors noise from construction, traffic, and industrial areas. Soundproofing uses soft materials to absorb sound.",
                "content_zh": "过度噪音（>85 dB）会损害听力。新加坡国家环境局监测来自建筑、交通和工业区的噪音。隔音使用柔软材料吸收声音。"
            }
        ],
        "magnetism-sec2": [
            {
                "id": "magnetic-materials",
                "type": "text",
                "title": "Magnetic Materials",
                "title_zh": "磁性材料",
                "content": "Magnetic materials: iron, steel, nickel, cobalt. Non-magnetic: copper, aluminium, plastic, wood. Steel is a permanent magnet; iron is temporary.",
                "content_zh": "磁性材料：铁、钢、镍、钴。非磁性：铜、铝、塑料、木材。钢是永久磁铁；铁是临时磁铁。"
            },
            {
                "id": "magnetic-fields",
                "type": "text",
                "title": "Magnetic Fields",
                "title_zh": "磁场",
                "content": "Magnetic field lines go from North to South pole outside the magnet. Like poles repel, unlike poles attract. Earth is a giant magnet.",
                "content_zh": "磁场线从磁铁外部的北极到南极。同极相斥，异极相吸。地球是一个巨大的磁铁。"
            },
            {
                "id": "electromagnets",
                "type": "text",
                "title": "Electromagnets",
                "title_zh": "电磁铁",
                "content": "Electromagnet = coil of wire around iron core carrying current. Strength increases with: more turns, stronger current, soft iron core. Used in MRT motors, speakers, doorbells.",
                "content_zh": "电磁铁 = 绕在铁芯周围的载流线圈。强度随着以下因素增加：更多匝数、更强电流、软铁芯。用于地铁电机、扬声器、门铃。"
            }
        ],
        "photosynthesis-sec2": [
            {
                "id": "photosynthesis-process",
                "type": "text",
                "title": "Photosynthesis",
                "title_zh": "光合作用",
                "content": "Process where plants make glucose using light energy. Word equation: Carbon dioxide + Water → (light, chlorophyll) → Glucose + Oxygen. Occurs in chloroplasts.",
                "content_zh": "植物利用光能制造葡萄糖的过程。文字方程式：二氧化碳 + 水 → （光，叶绿素） → 葡萄糖 + 氧气。发生在叶绿体中。"
            },
            {
                "id": "factors-affecting",
                "type": "text",
                "title": "Factors Affecting Photosynthesis",
                "title_zh": "影响光合作用的因素",
                "content": "Light intensity, CO₂ concentration, temperature, and chlorophyll. Singapore's tropical climate (high light, heat) is ideal for plant growth. Limiting factor: the factor in shortest supply.",
                "content_zh": "光强度、CO₂浓度、温度和叶绿素。新加坡的热带气候（高光照、高温）非常适合植物生长。限制因素：供应最少的因素。"
            },
            {
                "id": "importance",
                "type": "text",
                "title": "Importance of Photosynthesis",
                "title_zh": "光合作用的重要性",
                "content": "Produces food for all life, releases oxygen, removes CO₂ from atmosphere. Singapore's Gardens by the Bay and park connector network help maintain air quality.",
                "content_zh": "为所有生命产生食物，释放氧气，从大气中去除CO₂。新加坡的滨海湾花园和公园连道网络有助于维持空气质量。"
            }
        ],
        "transport-plants-sec2": [
            {
                "id": "xylem-phloem",
                "type": "text",
                "title": "Xylem and Phloem",
                "title_zh": "木质部和韧皮部",
                "content": "Xylem transports water and minerals upward from roots. Phloem transports sugars (products of photosynthesis) up and down. Both form vascular bundles.",
                "content_zh": "木质部从根部向上运输水和矿物质。韧皮部向上和向下运输糖（光合作用的产物）。两者形成维管束。"
            },
            {
                "id": "transpiration",
                "type": "text",
                "title": "Transpiration",
                "title_zh": "蒸腾作用",
                "content": "Loss of water vapor through stomata in leaves. Creates transpiration pull drawing water upward. Factors: temperature, humidity, wind, light. High humidity in Singapore slows transpiration.",
                "content_zh": "通过叶片中的气孔失去水蒸气。产生蒸腾拉力将水向上吸引。因素：温度、湿度、风、光。新加坡的高湿度减慢了蒸腾作用。"
            },
            {
                "id": "adaptations",
                "type": "text",
                "title": "Adaptations of Plants",
                "title_zh": "植物的适应",
                "content": "Tropical plants in Singapore have broad leaves for photosynthesis, drip tips for rain runoff, shallow roots for nutrient-poor soil, waxy cuticles to reduce water loss.",
                "content_zh": "新加坡的热带植物有宽大的叶子用于光合作用、滴水尖端用于雨水流失、浅根用于营养贫乏的土壤、蜡质角质层以减少水分流失。"
            }
        ],
        "respiration-sec2": [
            {
                "id": "aerobic-respiration",
                "type": "text",
                "title": "Aerobic Respiration",
                "title_zh": "有氧呼吸",
                "content": "Glucose + Oxygen → Carbon dioxide + Water + Energy (ATP). Occurs in mitochondria. Releases large amount of energy efficiently. Most common type in cells.",
                "content_zh": "葡萄糖 + 氧气 → 二氧化碳 + 水 + 能量(ATP)。发生在线粒体中。有效释放大量能量。细胞中最常见的类型。"
            },
            {
                "id": "anaerobic-respiration",
                "type": "text",
                "title": "Anaerobic Respiration",
                "title_zh": "无氧呼吸",
                "content": "Without oxygen. In animals: Glucose → Lactic acid + Energy. In plants/yeast: Glucose → Ethanol + Carbon dioxide + Energy. Less energy released. Used during intense exercise.",
                "content_zh": "没有氧气。在动物中：葡萄糖 → 乳酸 + 能量。在植物/酵母中：葡萄糖 → 乙醇 + 二氧化碳 + 能量。释放的能量较少。在剧烈运动期间使用。"
            },
            {
                "id": "comparison",
                "type": "text",
                "title": "Comparing Respiration Types",
                "title_zh": "比较呼吸类型",
                "content": "Aerobic: needs O₂, produces CO₂+H₂O, lots of energy, in mitochondria. Anaerobic: no O₂, produces lactic acid/ethanol, little energy, in cytoplasm. Singapore athletes train in heat/humidity affecting respiration.",
                "content_zh": "有氧：需要O₂，产生CO₂+H₂O，大量能量，在线粒体中。无氧：无O₂，产生乳酸/乙醇，少量能量，在细胞质中。新加坡运动员在影响呼吸的高温/高湿度中训练。"
            }
        ],
        "human-transport-sec2": [
            {
                "id": "blood-components",
                "type": "text",
                "title": "Components of Blood",
                "title_zh": "血液的成分",
                "content": "Red blood cells (carry O₂), white blood cells (fight infection), platelets (clotting), plasma (liquid transport). Adults have 4-6 liters of blood.",
                "content_zh": "红细胞（携带O₂）、白细胞（对抗感染）、血小板（凝血）、血浆（液体运输）。成年人有4-6升血液。"
            },
            {
                "id": "blood-vessels",
                "type": "text",
                "title": "Types of Blood Vessels",
                "title_zh": "血管类型",
                "content": "Arteries: thick walls, carry blood away from heart, high pressure. Veins: thin walls, valves, carry blood to heart, low pressure. Capillaries: one cell thick, exchange of materials.",
                "content_zh": "动脉：厚壁，从心脏输送血液，高压。静脉：薄壁，瓣膜，向心脏输送血液，低压。毛细血管：一个细胞厚，物质交换。"
            },
            {
                "id": "heart-circulation",
                "type": "text",
                "title": "Heart and Circulation",
                "title_zh": "心脏和循环",
                "content": "Double circulation: pulmonary (heart-lungs-heart) and systemic (heart-body-heart). Heart has 4 chambers. Valves prevent backflow. Heart disease is a concern in aging Singapore population.",
                "content_zh": "双循环：肺循环（心脏-肺-心脏）和体循环（心脏-身体-心脏）。心脏有4个腔室。瓣膜防止回流。心脏病是新加坡老龄化人口的一个关注点。"
            }
        ],
        "coordination-response-sec2": [
            {
                "id": "nervous-system",
                "type": "text",
                "title": "Nervous System",
                "title_zh": "神经系统",
                "content": "CNS (brain, spinal cord) processes information. PNS (nerves) carries signals. Neurons transmit electrical impulses rapidly for quick responses.",
                "content_zh": "中枢神经系统（大脑、脊髓）处理信息。周围神经系统（神经）传递信号。神经元快速传递电脉冲以进行快速反应。"
            },
            {
                "id": "reflex-actions",
                "type": "text",
                "title": "Reflex Actions",
                "title_zh": "反射动作",
                "content": "Automatic, rapid, protective responses. Reflex arc: receptor → sensory neuron → relay neuron → motor neuron → effector. Example: pulling hand from hot object.",
                "content_zh": "自动、快速、保护性反应。反射弧：感受器 → 感觉神经元 → 中继神经元 → 运动神经元 → 效应器。例如：从热物体上拉手。"
            },
            {
                "id": "hormones-homeostasis",
                "type": "text",
                "title": "Hormones and Homeostasis",
                "title_zh": "激素和稳态",
                "content": "Hormones: chemical messengers in blood, slower but longer-lasting. Homeostasis maintains constant internal environment (temperature, blood sugar). In Singapore's 30°C+ heat, body cools via sweating.",
                "content_zh": "激素：血液中的化学信使，较慢但持续时间较长。稳态维持恒定的内部环境（温度、血糖）。在新加坡30°C+的高温中，身体通过出汗降温。"
            }
        ]
    }

    return sections_map.get(chapter_id, [
        {
            "id": "overview",
            "type": "text",
            "title": chapter_data["title"],
            "title_zh": chapter_data["title_zh"],
            "content": chapter_data["description"],
            "content_zh": chapter_data["description_zh"]
        }
    ])

def create_exercises_for_chapter(chapter_data):
    """Create 15 exercises per chapter with varied difficulty"""
    chapter_id = chapter_data["id"]
    base_id = chapter_id.replace("-sec2", "")

    # Generate 15 varied exercises
    exercises = []

    # Pattern: 5 easy, 5 medium, 5 hard
    # Types: mcq, short, multi, drag-order, match

    for i in range(1, 16):
        if i <= 5:
            difficulty = "easy"
        elif i <= 10:
            difficulty = "medium"
        else:
            difficulty = "hard"

        # Vary question types
        if i % 5 == 1:
            q_type = "mcq"
        elif i % 5 == 2:
            q_type = "short"
        elif i % 5 == 3:
            q_type = "multi"
        elif i % 5 == 4:
            q_type = "mcq"
        else:
            q_type = "short"

        exercise = {
            "id": f"{base_id}-q{i}",
            "type": q_type,
            "difficulty": difficulty,
            "prompt": f"[{chapter_data['title']} - Question {i}]",
            "prompt_zh": f"[{chapter_data['title_zh']} - 问题 {i}]",
        }

        if q_type == "mcq":
            exercise["choices"] = ["Option A", "Option B", "Option C", "Option D"]
            exercise["answer"] = i % 4
            exercise["hint"] = "Think about the key concepts."
            exercise["hint_zh"] = "想想关键概念。"
        elif q_type == "short":
            exercise["answer"] = "sample answer"
            exercise["validator"] = "exact"
            exercise["hint"] = "Review the section notes."
            exercise["hint_zh"] = "查看章节注释。"
        elif q_type == "multi":
            exercise["choices"] = ["Option A", "Option B", "Option C", "Option D"]
            exercise["answers"] = [0, 1]
            exercise["hint"] = "More than one answer is correct."
            exercise["hint_zh"] = "多个答案是正确的。"

        exercises.append(exercise)

    return exercises

def main():
    """Generate complete Sec 2 Science chapters"""
    print("🧪 Generating Secondary 2 Science Chapters...")
    print(f"Total chapters to create: {len(sec2_science_chapters)}")

    complete_chapters = []

    for i, chapter_data in enumerate(sec2_science_chapters, 1):
        print(f"\n[{i}/{len(sec2_science_chapters)}] Creating: {chapter_data['title']}")

        # Create sections
        sections = create_sections_for_chapter(chapter_data)
        print(f"  ✓ Sections: {len(sections)}")

        # Create exercises
        exercises = create_exercises_for_chapter(chapter_data)
        print(f"  ✓ Exercises: {len(exercises)}")

        # Combine
        complete_chapter = {
            **chapter_data,
            "sections": sections,
            "exercises": exercises
        }

        complete_chapters.append(complete_chapter)

    # Save to file
    output_file = "chapters/science-sec2-chapters.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(complete_chapters, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Successfully created {len(complete_chapters)} Sec 2 Science chapters")
    print(f"📁 Saved to: {output_file}")

    # Summary
    total_sections = sum(len(ch['sections']) for ch in complete_chapters)
    total_exercises = sum(len(ch['exercises']) for ch in complete_chapters)

    print(f"\n📊 Summary:")
    print(f"  Chemistry chapters: {sum(1 for ch in complete_chapters if ch['tag'] == 'Chemistry')}")
    print(f"  Physics chapters: {sum(1 for ch in complete_chapters if ch['tag'] == 'Physics')}")
    print(f"  Biology chapters: {sum(1 for ch in complete_chapters if ch['tag'] == 'Biology')}")
    print(f"  Total sections: {total_sections}")
    print(f"  Total exercises: {total_exercises}")

if __name__ == "__main__":
    main()
