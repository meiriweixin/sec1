import json

# Create the Elements, Compounds & Chemical Formulas chapter
elements_chapter = {
    "id": "elements-compounds",
    "title": "Elements, Compounds & Chemical Formulas",
    "title_zh": "元素、化合物和化学式",
    "tag": "Chemistry",
    "tag_zh": "化学",
    "description": "Learn about elements, compounds, and how to write chemical formulas",
    "description_zh": "学习元素、化合物以及如何书写化学式",
    "objectives": [
        "Define elements and compounds",
        "Understand the periodic table basics",
        "Write chemical formulas correctly",
        "Distinguish between elements, compounds, and mixtures"
    ],
    "objectives_zh": [
        "定义元素和化合物",
        "理解周期表基础知识",
        "正确书写化学式",
        "区分元素、化合物和混合物"
    ],
    "sections": [
        {
            "id": "elements-intro",
            "type": "text",
            "title": "What are Elements?",
            "title_zh": "什么是元素？",
            "content": """**Elements** are pure substances made of only one type of atom. They cannot be broken down into simpler substances by chemical means.

**Key Points:**
- Elements are the building blocks of all matter
- Each element has unique properties
- Elements are represented by chemical symbols (1-2 letters)
- There are 118 known elements (92 occur naturally)

**Common Elements in Daily Life:**
- **Oxygen (O)** - In the air we breathe (21% of atmosphere)
- **Hydrogen (H)** - Most abundant element in the universe
- **Carbon (C)** - Found in all living things
- **Nitrogen (N)** - Makes up 78% of Earth's atmosphere
- **Iron (Fe)** - Used in construction, found in blood (hemoglobin)
- **Gold (Au)** - Jewelry, electronics
- **Silver (Ag)** - Jewelry, coins, antibacterial properties

**Singapore Context:**
Singapore imports many pure elements for its electronics and pharmaceutical industries, making chemistry knowledge essential for the local economy.""",
            "content_zh": """**元素**是仅由一种原子组成的纯净物质。它们不能通过化学方法分解成更简单的物质。

**要点：**
- 元素是所有物质的基本组成部分
- 每种元素都有独特的性质
- 元素用化学符号表示（1-2个字母）
- 已知有118种元素（92种自然存在）

**日常生活中的常见元素：**
- **氧气 (O)** - 我们呼吸的空气中（占大气的21%）
- **氢气 (H)** - 宇宙中最丰富的元素
- **碳 (C)** - 存在于所有生物中
- **氮气 (N)** - 占地球大气的78%
- **铁 (Fe)** - 用于建筑，存在于血液中（血红蛋白）
- **金 (Au)** - 珠宝、电子产品
- **银 (Ag)** - 珠宝、硬币、抗菌性质

**新加坡背景：**
新加坡为其电子和制药行业进口许多纯元素，使化学知识对当地经济至关重要。"""
        },
        {
            "id": "periodic-table",
            "type": "text",
            "title": "The Periodic Table",
            "title_zh": "元素周期表",
            "content": """The **Periodic Table** organizes all known elements by their atomic number and properties.

**Structure:**
- **Rows = Periods** (7 periods)
- **Columns = Groups** (18 groups)
- Elements in the same group have similar chemical properties

**Important Element Groups:**

**1. Group 1 - Alkali Metals**
- Lithium (Li), Sodium (Na), Potassium (K)
- Very reactive, soft metals
- React violently with water

**2. Group 17 - Halogens**
- Fluorine (F), Chlorine (Cl), Bromine (Br), Iodine (I)
- Very reactive non-metals
- Used in disinfection (chlorine in pools)

**3. Group 18 - Noble Gases**
- Helium (He), Neon (Ne), Argon (Ar)
- Unreactive (stable)
- Used in lighting (neon signs)

**Metals vs Non-Metals:**
- **Metals** (left side): Shiny, conduct electricity, malleable
- **Non-metals** (right side): Dull, poor conductors, brittle
- **Metalloids** (diagonal line): Properties of both

**Reading the Periodic Table:**
Each element box contains:
- **Chemical Symbol** (e.g., Na)
- **Atomic Number** (number of protons)
- **Element Name** (Sodium)
- **Atomic Mass** (average mass of atoms)""",
            "content_zh": """**元素周期表**按原子序数和性质组织所有已知元素。

**结构：**
- **行 = 周期**（7个周期）
- **列 = 族**（18个族）
- 同一族的元素具有相似的化学性质

**重要元素族：**

**1. 第1族 - 碱金属**
- 锂 (Li)、钠 (Na)、钾 (K)
- 非常活泼的软金属
- 与水剧烈反应

**2. 第17族 - 卤素**
- 氟 (F)、氯 (Cl)、溴 (Br)、碘 (I)
- 非常活泼的非金属
- 用于消毒（游泳池中的氯）

**3. 第18族 - 稀有气体**
- 氦 (He)、氖 (Ne)、氩 (Ar)
- 不活泼（稳定）
- 用于照明（霓虹灯）

**金属与非金属：**
- **金属**（左侧）：有光泽、导电、可延展
- **非金属**（右侧）：无光泽、不良导体、易碎
- **类金属**（对角线）：两者的性质

**阅读元素周期表：**
每个元素框包含：
- **化学符号**（例如，Na）
- **原子序数**（质子数）
- **元素名称**（钠）
- **原子质量**（原子的平均质量）"""
        },
        {
            "id": "compounds-intro",
            "type": "text",
            "title": "What are Compounds?",
            "title_zh": "什么是化合物？",
            "content": """**Compounds** are pure substances made of two or more different elements chemically bonded together in fixed proportions.

**Key Differences: Elements vs Compounds**

| Feature | Element | Compound |
|---------|---------|----------|
| **Composition** | One type of atom | Two or more types of atoms |
| **Can be broken down?** | No (by chemical means) | Yes (by chemical reactions) |
| **Properties** | Unique to that element | Different from constituent elements |
| **Symbol** | 1-2 letters (e.g., O) | Chemical formula (e.g., H₂O) |

**Common Compounds:**

**1. Water (H₂O)**
- 2 Hydrogen + 1 Oxygen
- Properties completely different from H₂ gas or O₂ gas
- Essential for life

**2. Carbon Dioxide (CO₂)**
- 1 Carbon + 2 Oxygen
- Produced by respiration
- Used by plants in photosynthesis

**3. Table Salt (NaCl)**
- 1 Sodium + 1 Chlorine
- Sodium alone: explosive metal
- Chlorine alone: toxic gas
- Together: safe to eat!

**4. Sugar (C₁₂H₂₂O₁₁)**
- 12 Carbon + 22 Hydrogen + 11 Oxygen
- Complex compound
- Provides energy

**Singapore Example:**
When you buy a packet drink at a kopitiam, you're consuming many compounds: water (H₂O), sugar (C₁₂H₂₂O₁₁), carbon dioxide (CO₂ for fizz), and various flavoring compounds!""",
            "content_zh": """**化合物**是由两种或多种不同元素以固定比例化学结合而成的纯净物质。

**主要区别：元素与化合物**

| 特征 | 元素 | 化合物 |
|------|------|--------|
| **组成** | 一种原子 | 两种或多种原子 |
| **可以分解吗？** | 不能（通过化学方法） | 可以（通过化学反应） |
| **性质** | 该元素特有 | 与组成元素不同 |
| **符号** | 1-2个字母（例如，O） | 化学式（例如，H₂O） |

**常见化合物：**

**1. 水 (H₂O)**
- 2个氢 + 1个氧
- 性质与H₂气体或O₂气体完全不同
- 生命必需

**2. 二氧化碳 (CO₂)**
- 1个碳 + 2个氧
- 由呼吸产生
- 植物光合作用使用

**3. 食盐 (NaCl)**
- 1个钠 + 1个氯
- 单独的钠：爆炸性金属
- 单独的氯：有毒气体
- 在一起：可以安全食用！

**4. 糖 (C₁₂H₂₂O₁₁)**
- 12个碳 + 22个氢 + 11个氧
- 复杂化合物
- 提供能量

**新加坡例子：**
当你在咖啡店买一包饮料时，你正在消费许多化合物：水（H₂O）、糖（C₁₂H₂₂O₁₁）、二氧化碳（CO₂用于起泡）和各种调味化合物！"""
        },
        {
            "id": "chemical-formulas",
            "type": "text",
            "title": "Writing Chemical Formulas",
            "title_zh": "书写化学式",
            "content": """**Chemical formulas** show which elements are in a compound and how many atoms of each element.

**Formula Rules:**

**1. Element Symbols**
- Always capitalize the first letter
- Second letter (if any) is lowercase
- Examples: H (not h), Ca (not CA or ca), Cl (not CL)

**2. Subscript Numbers**
- Written small and low (subscript)
- Show how many atoms of that element
- If no number shown, it means 1 atom
- Examples:
  - H₂O = 2 hydrogen, 1 oxygen
  - CO₂ = 1 carbon, 2 oxygen
  - H₂SO₄ = 2 hydrogen, 1 sulfur, 4 oxygen

**3. Reading Formulas**
Read from left to right, count all atoms:

**Example: Ca(OH)₂** (Calcium hydroxide)
- 1 Calcium (Ca)
- 2 Oxygen (O) - because of the ₂ outside bracket
- 2 Hydrogen (H) - because of the ₂ outside bracket
- Total: 1 Ca + 2 O + 2 H = 5 atoms

**Common Compounds to Know:**

| Formula | Name | What it is |
|---------|------|------------|
| H₂O | Water | Essential for life |
| CO₂ | Carbon dioxide | In fizzy drinks |
| O₂ | Oxygen | Gas we breathe |
| NaCl | Sodium chloride | Table salt |
| CaCO₃ | Calcium carbonate | Chalk, limestone |
| NH₃ | Ammonia | Cleaning products |
| CH₄ | Methane | Natural gas |
| C₆H₁₂O₆ | Glucose | Blood sugar |

**Singapore Context:**
The tap water in Singapore (PUB's NEWater) is purified H₂O with small amounts of minerals like Ca²⁺ and Mg²⁺ ions added for taste and health!""",
            "content_zh": """**化学式**显示化合物中有哪些元素以及每种元素有多少个原子。

**化学式规则：**

**1. 元素符号**
- 第一个字母始终大写
- 第二个字母（如果有）小写
- 例子：H（不是h），Ca（不是CA或ca），Cl（不是CL）

**2. 下标数字**
- 写得小而低（下标）
- 显示该元素有多少个原子
- 如果没有显示数字，表示1个原子
- 例子：
  - H₂O = 2个氢，1个氧
  - CO₂ = 1个碳，2个氧
  - H₂SO₄ = 2个氢，1个硫，4个氧

**3. 阅读化学式**
从左到右阅读，计算所有原子：

**例子：Ca(OH)₂**（氢氧化钙）
- 1个钙 (Ca)
- 2个氧 (O) - 因为括号外的₂
- 2个氢 (H) - 因为括号外的₂
- 总共：1 Ca + 2 O + 2 H = 5个原子

**需要知道的常见化合物：**

| 化学式 | 名称 | 是什么 |
|--------|------|--------|
| H₂O | 水 | 生命必需 |
| CO₂ | 二氧化碳 | 汽水中 |
| O₂ | 氧气 | 我们呼吸的气体 |
| NaCl | 氯化钠 | 食盐 |
| CaCO₃ | 碳酸钙 | 粉笔、石灰石 |
| NH₃ | 氨 | 清洁产品 |
| CH₄ | 甲烷 | 天然气 |
| C₆H₁₂O₆ | 葡萄糖 | 血糖 |

**新加坡背景：**
新加坡的自来水（公用事业局的新生水）是纯化的H₂O，添加了少量矿物质，如Ca²⁺和Mg²⁺离子，以改善口感和健康！"""
        },
        {
            "id": "element-compound-mixture",
            "type": "text",
            "title": "Elements, Compounds, and Mixtures",
            "title_zh": "元素、化合物和混合物",
            "content": """Understanding the differences between elements, compounds, and mixtures is crucial in chemistry.

**Comparison Table:**

| Property | Element | Compound | Mixture |
|----------|---------|----------|---------|
| **Composition** | One type of atom | Two or more atoms chemically bonded | Two or more substances physically mixed |
| **Can be separated?** | No | Yes (by chemical reaction) | Yes (by physical methods) |
| **Fixed ratio?** | N/A | Yes (always same ratio) | No (any proportion) |
| **New properties?** | N/A | Yes (different from elements) | No (keeps original properties) |
| **Examples** | O₂, Fe, Au | H₂O, NaCl, CO₂ | Air, seawater, salad |

**Visual Analogy:**

**Elements** = Pure ingredients
- Like a bowl of only rice grains

**Compounds** = Recipe (must follow exact proportions)
- Like a cake (flour + eggs + sugar chemically changed by baking)
- Can't separate back into flour, eggs, sugar easily

**Mixtures** = Mixed ingredients (any proportion)
- Like fried rice (rice + vegetables + egg mixed together)
- Can pick out vegetables, rice stays rice

**Singapore Food Examples:**

**1. Laksa (混合物 - Mixture)**
- Noodles + soup + prawns + eggs physically mixed
- You can separate components
- Each ingredient keeps its properties

**2. Kaya Toast (化合物 - Compound)**
- Kaya is made from eggs, sugar, coconut milk, and pandan
- Chemical reactions during cooking create new substance
- Can't easily separate back to original ingredients

**3. Table Salt (化合物 - Compound)**
- NaCl is sodium + chlorine chemically bonded
- Properties completely different from pure sodium or chlorine
- Cannot separate by filtering or boiling

**4. Teh Tarik (混合物 - Mixture)**
- Tea + milk + sugar physically mixed
- Components can be separated (e.g., water evaporates, sugar crystals remain)

**Key Test Questions:**
- "Is it chemically bonded?" → Compound
- "Can you physically separate it?" → Mixture
- "Only one type of atom?" → Element""",
            "content_zh": """理解元素、化合物和混合物之间的区别在化学中至关重要。

**比较表：**

| 性质 | 元素 | 化合物 | 混合物 |
|------|------|--------|--------|
| **组成** | 一种原子 | 两种或多种原子化学结合 | 两种或多种物质物理混合 |
| **可以分离吗？** | 不可以 | 可以（通过化学反应） | 可以（通过物理方法） |
| **固定比例？** | 不适用 | 是（总是相同比例） | 不是（任何比例） |
| **新性质？** | 不适用 | 是（与元素不同） | 不是（保持原有性质） |
| **例子** | O₂, Fe, Au | H₂O, NaCl, CO₂ | 空气、海水、沙拉 |

**视觉类比：**

**元素** = 纯成分
- 就像一碗只有米粒

**化合物** = 食谱（必须遵循确切比例）
- 就像蛋糕（面粉+鸡蛋+糖通过烘焙化学改变）
- 不能轻易分离回面粉、鸡蛋、糖

**混合物** = 混合成分（任何比例）
- 就像炒饭（米饭+蔬菜+鸡蛋混合在一起）
- 可以挑出蔬菜，米饭仍然是米饭

**新加坡食物例子：**

**1. 叻沙（混合物）**
- 面条+汤+虾+鸡蛋物理混合
- 你可以分离组成部分
- 每种成分保持其性质

**2. 咖椰吐司（化合物）**
- 咖椰由鸡蛋、糖、椰奶和班兰制成
- 烹饪过程中的化学反应产生新物质
- 不能轻易分离回原始成分

**3. 食盐（化合物）**
- NaCl是钠+氯化学结合
- 性质与纯钠或氯完全不同
- 不能通过过滤或煮沸分离

**4. 拉茶（混合物）**
- 茶+牛奶+糖物理混合
- 组分可以分离（例如，水蒸发，糖晶体保留）

**关键测试问题：**
- "它是化学结合的吗？" → 化合物
- "你能物理分离它吗？" → 混合物
- "只有一种原子吗？" → 元素"""
        }
    ],
    "exercises": [
        {
            "id": "ex1",
            "type": "mcq",
            "question": "Which of the following is an element?",
            "question_zh": "以下哪项是元素？",
            "choices": ["Water (H₂O)", "Oxygen (O₂)", "Carbon dioxide (CO₂)", "Salt (NaCl)"],
            "choices_zh": ["水 (H₂O)", "氧气 (O₂)", "二氧化碳 (CO₂)", "盐 (NaCl)"],
            "answer": 1,
            "explanation": "Oxygen (O₂) is an element because it contains only one type of atom. Water, carbon dioxide, and salt are all compounds made of two or more different elements.",
            "explanation_zh": "氧气（O₂）是元素，因为它只含有一种原子。水、二氧化碳和盐都是由两种或多种不同元素组成的化合物。"
        },
        {
            "id": "ex2",
            "type": "mcq",
            "question": "How many total atoms are in one molecule of H₂SO₄ (sulfuric acid)?",
            "question_zh": "一个H₂SO₄（硫酸）分子中总共有多少个原子？",
            "choices": ["4 atoms", "5 atoms", "6 atoms", "7 atoms"],
            "choices_zh": ["4个原子", "5个原子", "6个原子", "7个原子"],
            "answer": 3,
            "explanation": "H₂SO₄ contains 2 hydrogen atoms + 1 sulfur atom + 4 oxygen atoms = 7 atoms total.",
            "explanation_zh": "H₂SO₄含有2个氢原子 + 1个硫原子 + 4个氧原子 = 总共7个原子。"
        },
        {
            "id": "ex3",
            "type": "mcq",
            "question": "What is the main difference between a compound and a mixture?",
            "question_zh": "化合物和混合物之间的主要区别是什么？",
            "choices": [
                "Compounds can be separated physically, mixtures cannot",
                "Compounds have chemically bonded elements, mixtures do not",
                "Mixtures have fixed ratios, compounds do not",
                "Compounds are always liquids, mixtures can be any state"
            ],
            "choices_zh": [
                "化合物可以物理分离，混合物不能",
                "化合物具有化学结合的元素，混合物没有",
                "混合物具有固定比例，化合物没有",
                "化合物总是液体，混合物可以是任何状态"
            ],
            "answer": 1,
            "explanation": "In compounds, elements are chemically bonded in fixed ratios and have new properties. In mixtures, substances are physically mixed and keep their original properties.",
            "explanation_zh": "在化合物中，元素以固定比例化学结合并具有新性质。在混合物中，物质物理混合并保持其原有性质。"
        },
        {
            "id": "ex4",
            "type": "mcq",
            "question": "Which group in the periodic table contains the most unreactive elements?",
            "question_zh": "元素周期表中哪一族包含最不活泼的元素？",
            "choices": ["Group 1 (Alkali metals)", "Group 17 (Halogens)", "Group 18 (Noble gases)", "Group 2 (Alkaline earth metals)"],
            "choices_zh": ["第1族（碱金属）", "第17族（卤素）", "第18族（稀有气体）", "第2族（碱土金属）"],
            "answer": 2,
            "explanation": "Group 18 noble gases (He, Ne, Ar, Kr, Xe) are the most unreactive because they have stable electron configurations.",
            "explanation_zh": "第18族稀有气体（He、Ne、Ar、Kr、Xe）最不活泼，因为它们具有稳定的电子构型。"
        },
        {
            "id": "ex5",
            "type": "short",
            "question": "Sodium (Na) is a reactive metal and Chlorine (Cl) is a toxic gas. What compound do they form when chemically bonded?",
            "question_zh": "钠（Na）是一种活泼金属，氯（Cl）是一种有毒气体。它们化学结合时形成什么化合物？",
            "answer": "NaCl",
            "validator": "exact",
            "explanation": "Sodium and chlorine chemically bond to form NaCl (sodium chloride), commonly known as table salt. Despite the dangerous properties of the individual elements, the compound is safe to eat.",
            "explanation_zh": "钠和氯化学结合形成NaCl（氯化钠），通常称为食盐。尽管单独元素具有危险性质，但化合物可以安全食用。"
        }
    ]
}

# Save to a temporary JSON file for review
with open('elements-compounds-chapter.json', 'w', encoding='utf-8') as f:
    json.dump(elements_chapter, f, indent=2, ensure_ascii=False)

print('Elements & Compounds chapter created successfully!')
print('Saved to elements-compounds-chapter.json for review')
