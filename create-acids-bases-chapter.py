import json

# Create the Acids & Bases chapter
acids_bases_chapter = {
    "id": "acids-bases",
    "title": "Acids & Bases",
    "title_zh": "酸和碱",
    "tag": "Chemistry",
    "tag_zh": "化学",
    "description": "Understand the properties of acids and bases and how to identify them",
    "description_zh": "理解酸和碱的性质以及如何识别它们",
    "objectives": [
        "Define acids and bases",
        "Understand the pH scale",
        "Identify common acids and bases",
        "Learn about neutralization reactions",
        "Recognize indicators and their color changes"
    ],
    "objectives_zh": [
        "定义酸和碱",
        "理解pH值",
        "识别常见的酸和碱",
        "学习中和反应",
        "识别指示剂及其颜色变化"
    ],
    "sections": [
        {
            "id": "acids-intro",
            "type": "text",
            "title": "What are Acids?",
            "title_zh": "什么是酸？",
            "content": """**Acids** are substances that produce hydrogen ions (H⁺) when dissolved in water.

**Properties of Acids:**
- Taste sour (but NEVER taste chemicals in a lab!)
- Turn blue litmus paper red
- pH less than 7
- React with metals to produce hydrogen gas
- Conduct electricity when dissolved in water (electrolytes)
- Corrosive (can damage skin and materials)

**Common Acids in Daily Life:**

**1. Hydrochloric Acid (HCl)**
- Produced in your stomach (stomach acid)
- Helps digest food
- Concentration in stomach: pH 1-2

**2. Citric Acid (C₆H₈O₇)**
- Found in citrus fruits (oranges, lemons, limes)
- Gives sour taste
- Used as food preservative

**3. Acetic Acid (CH₃COOH)**
- Main component of vinegar
- Used in cooking and cleaning
- pH around 2.5

**4. Sulfuric Acid (H₂SO₄)**
- Used in car batteries
- Industrial chemical
- Very corrosive - handle with extreme care

**5. Carbonic Acid (H₂CO₃)**
- In fizzy drinks (carbonated beverages)
- Formed when CO₂ dissolves in water
- Gives drinks their "fizz"

**Singapore Context:**
Many local foods contain acids:
- **Lime juice** in laksa (citric acid)
- **Tamarind** in assam laksa (tartaric acid)
- **Vinegar** in achar (acetic acid)
- **Vitamin C drinks** (ascorbic acid)

The tangy taste you enjoy in these foods comes from acids!""",
            "content_zh": """**酸**是溶于水时产生氢离子（H⁺）的物质。

**酸的性质：**
- 味道酸（但绝不要在实验室里品尝化学物质！）
- 使蓝色石蕊试纸变红
- pH值小于7
- 与金属反应产生氢气
- 溶于水时导电（电解质）
- 腐蚀性（可以损坏皮肤和材料）

**日常生活中的常见酸：**

**1. 盐酸 (HCl)**
- 在你的胃中产生（胃酸）
- 帮助消化食物
- 胃中浓度：pH 1-2

**2. 柠檬酸 (C₆H₈O₇)**
- 存在于柑橘类水果（橙子、柠檬、酸橙）
- 提供酸味
- 用作食品防腐剂

**3. 乙酸 (CH₃COOH)**
- 醋的主要成分
- 用于烹饪和清洁
- pH约2.5

**4. 硫酸 (H₂SO₄)**
- 用于汽车电池
- 工业化学品
- 非常腐蚀性 - 需要极其小心处理

**5. 碳酸 (H₂CO₃)**
- 存在于汽水中（碳酸饮料）
- 当CO₂溶于水时形成
- 使饮料"起泡"

**新加坡背景：**
许多本地食物含有酸：
- 叻沙中的**青柠汁**（柠檬酸）
- 亚参叻沙中的**罗望子**（酒石酸）
- 亚查中的**醋**（乙酸）
- **维生素C饮料**（抗坏血酸）

你在这些食物中享受的酸味来自酸！"""
        },
        {
            "id": "bases-intro",
            "type": "text",
            "title": "What are Bases?",
            "title_zh": "什么是碱？",
            "content": """**Bases** are substances that produce hydroxide ions (OH⁻) when dissolved in water. Alkalis are bases that dissolve in water.

**Properties of Bases:**
- Taste bitter (but NEVER taste chemicals!)
- Feel slippery/soapy to touch
- Turn red litmus paper blue
- pH greater than 7
- Conduct electricity when dissolved in water
- Corrosive in high concentrations

**Common Bases in Daily Life:**

**1. Sodium Hydroxide (NaOH)**
- Also called caustic soda or lye
- Used in soap making
- Used in drain cleaners
- Very corrosive - pH 14

**2. Calcium Hydroxide (Ca(OH)₂)**
- Also called slaked lime
- Used in construction (cement, mortar)
- Used to neutralize acidic soil

**3. Ammonia (NH₃)**
- Found in cleaning products
- Strong smell
- Used in window cleaners
- pH around 11

**4. Sodium Bicarbonate (NaHCO₃)**
- Also called baking soda
- Used in baking (makes cakes rise)
- Mild antacid (treats heartburn)
- Used for cleaning

**5. Magnesium Hydroxide (Mg(OH)₂)**
- Main ingredient in "Milk of Magnesia"
- Used as antacid medicine
- Neutralizes excess stomach acid

**Singapore Context:**
You encounter bases daily:
- **Soap and shampoo** (sodium hydroxide base)
- **Toothpaste** (contains mild bases to neutralize mouth acids)
- **Baking kuehs** (baking soda makes them fluffy)
- **Antacid tablets** at pharmacies (neutralize stomach acid)
- **Cleaning products** for toilets and kitchens

**Important Safety Note:**
Strong acids and strong bases are both dangerous! Always handle with care, wear gloves, and never mix chemicals unless you know it's safe.""",
            "content_zh": """**碱**是溶于水时产生氢氧根离子（OH⁻）的物质。碱是溶于水的碱。

**碱的性质：**
- 味道苦（但绝不要品尝化学物质！）
- 触摸时感觉滑腻/肥皂状
- 使红色石蕊试纸变蓝
- pH值大于7
- 溶于水时导电
- 高浓度时具有腐蚀性

**日常生活中的常见碱：**

**1. 氢氧化钠 (NaOH)**
- 也称为苛性钠或碱液
- 用于制皂
- 用于排水管清洁剂
- 非常腐蚀性 - pH 14

**2. 氢氧化钙 (Ca(OH)₂)**
- 也称为熟石灰
- 用于建筑（水泥、砂浆）
- 用于中和酸性土壤

**3. 氨 (NH₃)**
- 存在于清洁产品中
- 强烈气味
- 用于玻璃清洁剂
- pH约11

**4. 碳酸氢钠 (NaHCO₃)**
- 也称为小苏打
- 用于烘焙（使蛋糕膨胀）
- 温和的抗酸剂（治疗胃灼热）
- 用于清洁

**5. 氢氧化镁 (Mg(OH)₂)**
- "镁乳"的主要成分
- 用作抗酸药
- 中和过量胃酸

**新加坡背景：**
你每天都会遇到碱：
- **肥皂和洗发水**（氢氧化钠碱）
- **牙膏**（含有温和的碱以中和口腔酸）
- **烘焙糕点**（小苏打使它们蓬松）
- **药店的抗酸片**（中和胃酸）
- **厕所和厨房的清洁产品**

**重要安全提示：**
强酸和强碱都很危险！始终小心处理，戴手套，绝不要混合化学品，除非你知道这是安全的。"""
        },
        {
            "id": "ph-scale",
            "type": "text",
            "title": "The pH Scale",
            "title_zh": "pH值",
            "content": """The **pH scale** measures how acidic or basic a solution is. It ranges from 0 to 14.

**Understanding pH:**

**pH < 7: ACIDIC**
- 0-2: Strong acids (battery acid, stomach acid)
- 3-6: Weak acids (vinegar, orange juice, rain)

**pH = 7: NEUTRAL**
- Pure water
- Neither acidic nor basic

**pH > 7: BASIC (ALKALINE)**
- 8-10: Weak bases (baking soda, seawater)
- 11-14: Strong bases (ammonia, drain cleaner)

**pH Scale Visual:**
```
0 ← ACIDIC | NEUTRAL | BASIC → 14
    (H⁺ ions)    7    (OH⁻ ions)
```

**Common Substances and their pH:**

| Substance | pH | Type |
|-----------|-----|------|
| Battery acid | 0-1 | Strong acid |
| Stomach acid | 1-2 | Strong acid |
| Lemon juice | 2 | Acid |
| Vinegar | 2.5 | Acid |
| Orange juice | 3-4 | Weak acid |
| Tomato juice | 4 | Weak acid |
| Black coffee | 5 | Weak acid |
| Milk | 6.5 | Weak acid |
| **Pure water** | **7** | **Neutral** |
| Blood | 7.4 | Slightly basic |
| Seawater | 8 | Slightly basic |
| Baking soda | 9 | Base |
| Milk of Magnesia | 10 | Base |
| Ammonia | 11-12 | Strong base |
| Bleach | 12-13 | Strong base |
| Drain cleaner | 14 | Strong base |

**Key Points:**
- Each pH unit represents a 10× change in acidity
- pH 2 is 10 times more acidic than pH 3
- pH 2 is 100 times more acidic than pH 4
- Lower pH = more H⁺ ions = more acidic
- Higher pH = more OH⁻ ions = more basic

**Singapore Examples:**
- **Kopi (coffee)**: pH ~5 (slightly acidic)
- **Teh (tea)**: pH ~6 (slightly acidic)
- **Tap water**: pH ~7 (neutral, safe to drink)
- **Swimming pool water**: pH 7.2-7.8 (slightly basic, chlorine added)""",
            "content_zh": """**pH值**测量溶液的酸性或碱性。范围从0到14。

**理解pH值：**

**pH < 7：酸性**
- 0-2：强酸（电池酸、胃酸）
- 3-6：弱酸（醋、橙汁、雨水）

**pH = 7：中性**
- 纯水
- 既不酸也不碱

**pH > 7：碱性（碱性）**
- 8-10：弱碱（小苏打、海水）
- 11-14：强碱（氨、排水管清洁剂）

**pH值可视化：**
```
0 ← 酸性 | 中性 | 碱性 → 14
    (H⁺离子)   7   (OH⁻离子)
```

**常见物质及其pH值：**

| 物质 | pH | 类型 |
|------|-----|------|
| 电池酸 | 0-1 | 强酸 |
| 胃酸 | 1-2 | 强酸 |
| 柠檬汁 | 2 | 酸 |
| 醋 | 2.5 | 酸 |
| 橙汁 | 3-4 | 弱酸 |
| 番茄汁 | 4 | 弱酸 |
| 黑咖啡 | 5 | 弱酸 |
| 牛奶 | 6.5 | 弱酸 |
| **纯水** | **7** | **中性** |
| 血液 | 7.4 | 微碱 |
| 海水 | 8 | 微碱 |
| 小苏打 | 9 | 碱 |
| 镁乳 | 10 | 碱 |
| 氨 | 11-12 | 强碱 |
| 漂白剂 | 12-13 | 强碱 |
| 排水管清洁剂 | 14 | 强碱 |

**要点：**
- 每个pH单位代表酸度的10倍变化
- pH 2比pH 3酸10倍
- pH 2比pH 4酸100倍
- 较低的pH值 = 更多H⁺离子 = 更酸
- 较高的pH值 = 更多OH⁻离子 = 更碱

**新加坡例子：**
- **咖啡**：pH ~5（微酸）
- **茶**：pH ~6（微酸）
- **自来水**：pH ~7（中性，安全饮用）
- **游泳池水**：pH 7.2-7.8（微碱，添加了氯）"""
        },
        {
            "id": "indicators",
            "type": "text",
            "title": "Indicators and Testing",
            "title_zh": "指示剂和测试",
            "content": """**Indicators** are substances that change color depending on whether they're in an acid or a base.

**Common Indicators:**

**1. Litmus Paper**
- Most commonly used indicator
- **Blue litmus paper**: Turns RED in acid, stays blue in base
- **Red litmus paper**: Turns BLUE in base, stays red in acid
- Cannot tell exact pH, only if acid or base

**2. Universal Indicator**
- Changes through a range of colors
- Shows approximate pH value
- Color chart:
  - **Red/Orange**: pH 0-4 (Strong/weak acid)
  - **Yellow**: pH 5-6 (Weak acid)
  - **Green**: pH 7 (Neutral)
  - **Blue**: pH 8-10 (Weak base)
  - **Purple**: pH 11-14 (Strong base)

**3. Phenolphthalein**
- **Colorless** in acid and neutral (pH < 8)
- **Pink** in base (pH > 8)
- Used in titrations

**4. Methyl Orange**
- **Red** in acid (pH < 3)
- **Yellow** in base and neutral (pH > 4)
- **Orange** at transition point

**Natural Indicators:**
Many plant materials can act as indicators!

**Red Cabbage Juice:**
- Red/Pink in acid
- Purple in neutral
- Green/Yellow in base
- Can make this at home!

**Turmeric:**
- Yellow in acid and neutral
- Red/Brown in base
- Common in curry

**How to Test pH:**

**Method 1: Litmus Paper**
1. Dip litmus paper in solution
2. Observe color change
3. Determine if acid or base

**Method 2: Universal Indicator**
1. Add a few drops to solution
2. Observe color
3. Compare to color chart
4. Read approximate pH

**Method 3: pH Meter (Digital)**
1. Calibrate meter
2. Dip probe in solution
3. Read exact pH on screen
4. Most accurate method

**Singapore Context:**
You can test household items:
- **Lemon juice** (should turn litmus red - acidic)
- **Baking soda solution** (should turn litmus blue - basic)
- **Vinegar** (acidic - red litmus)
- **Soap water** (basic - blue litmus)
- **Tap water** (neutral - no change)

**Fun Experiment at Home:**
Boil red cabbage, collect the purple juice, and test it with vinegar (turns red), water (stays purple), and baking soda solution (turns green)!""",
            "content_zh": """**指示剂**是根据它们在酸或碱中而改变颜色的物质。

**常见指示剂：**

**1. 石蕊试纸**
- 最常用的指示剂
- **蓝色石蕊试纸**：在酸中变红，在碱中保持蓝色
- **红色石蕊试纸**：在碱中变蓝，在酸中保持红色
- 不能告诉确切的pH值，只能判断是酸还是碱

**2. 通用指示剂**
- 通过一系列颜色变化
- 显示大约的pH值
- 颜色表：
  - **红色/橙色**：pH 0-4（强/弱酸）
  - **黄色**：pH 5-6（弱酸）
  - **绿色**：pH 7（中性）
  - **蓝色**：pH 8-10（弱碱）
  - **紫色**：pH 11-14（强碱）

**3. 酚酞**
- 在酸和中性中**无色**（pH < 8）
- 在碱中**粉红色**（pH > 8）
- 用于滴定

**4. 甲基橙**
- 在酸中**红色**（pH < 3）
- 在碱和中性中**黄色**（pH > 4）
- 在过渡点**橙色**

**天然指示剂：**
许多植物材料可以充当指示剂！

**紫甘蓝汁：**
- 在酸中红色/粉红色
- 在中性中紫色
- 在碱中绿色/黄色
- 可以在家制作！

**姜黄：**
- 在酸和中性中黄色
- 在碱中红色/棕色
- 常见于咖喱中

**如何测试pH值：**

**方法1：石蕊试纸**
1. 将石蕊试纸浸入溶液中
2. 观察颜色变化
3. 确定是酸还是碱

**方法2：通用指示剂**
1. 向溶液中添加几滴
2. 观察颜色
3. 与颜色表比较
4. 读取大约的pH值

**方法3：pH计（数字）**
1. 校准仪表
2. 将探头浸入溶液中
3. 在屏幕上读取确切的pH值
4. 最准确的方法

**新加坡背景：**
你可以测试家庭用品：
- **柠檬汁**（应使石蕊试纸变红 - 酸性）
- **小苏打溶液**（应使石蕊试纸变蓝 - 碱性）
- **醋**（酸性 - 红色石蕊）
- **肥皂水**（碱性 - 蓝色石蕊）
- **自来水**（中性 - 无变化）

**在家的有趣实验：**
煮紫甘蓝，收集紫色汁液，用醋（变红）、水（保持紫色）和小苏打溶液（变绿）测试它！"""
        },
        {
            "id": "neutralization",
            "type": "text",
            "title": "Neutralization Reactions",
            "title_zh": "中和反应",
            "content": """**Neutralization** is a chemical reaction between an acid and a base that produces salt and water.

**General Formula:**
```
Acid + Base → Salt + Water
```

**Example Reactions:**

**1. Hydrochloric Acid + Sodium Hydroxide**
```
HCl + NaOH → NaCl + H₂O
(Acid + Base → Salt + Water)
```
- Products: Sodium chloride (table salt) + water
- The solution becomes neutral (pH 7)

**2. Sulfuric Acid + Magnesium Hydroxide**
```
H₂SO₄ + Mg(OH)₂ → MgSO₄ + 2H₂O
```
- Products: Magnesium sulfate (Epsom salt) + water
- Used in antacid medicine!

**3. Nitric Acid + Potassium Hydroxide**
```
HNO₃ + KOH → KNO₃ + H₂O
```
- Products: Potassium nitrate (fertilizer) + water

**What Happens During Neutralization:**
- H⁺ ions from acid + OH⁻ ions from base → H₂O (water)
- The remaining ions form a salt
- Heat is released (exothermic reaction)
- pH moves toward 7 (neutral)

**Real-Life Applications:**

**1. Treating Stomach Acidity (Heartburn)**
- Problem: Excess stomach acid (HCl) causes pain
- Solution: Take antacid tablet (contains base like Mg(OH)₂)
- Reaction: HCl + Mg(OH)₂ → MgCl₂ + H₂O
- Result: Acid neutralized, pain relief

**2. Treating Insect Stings**

**Bee Sting** (acidic venom):
- Apply baking soda paste (base)
- Base neutralizes the acid
- Reduces pain and swelling

**Wasp Sting** (basic venom):
- Apply vinegar (acid)
- Acid neutralizes the base
- Reduces pain and swelling

**3. Agriculture - Soil Treatment**

**Acidic Soil** (bad for some plants):
- Add lime (calcium hydroxide - base)
- Neutralizes excess acid
- Improves plant growth

**Basic Soil** (bad for other plants):
- Add sulfur (forms acid when wet)
- Neutralizes excess base
- Better growing conditions

**4. Industrial Waste Treatment**
- Factory waste may be very acidic or basic
- Add opposite substance to neutralize
- Make waste safe before releasing to environment

**5. Toothpaste**
- Bacteria in mouth produce acids
- Acids damage tooth enamel
- Toothpaste contains mild bases
- Neutralizes acids, protects teeth

**Singapore Context:**

**1. PUB Water Treatment**
- Adjusts pH of water supply
- Uses bases to neutralize acidic water
- Ensures safe drinking water (pH ~7)

**2. Swimming Pools**
- Need to maintain pH 7.2-7.8
- Add acid if too basic
- Add base if too acidic
- Keeps water safe and comfortable

**3. Cooking**
- If curry is too sour (acidic), add a pinch of baking soda (base)
- Neutralizes excess acid
- Balances flavor

**Signs of Neutralization:**
- Temperature increases (gets warmer)
- Bubbling may occur
- Color change if indicator present
- pH moves toward 7""",
            "content_zh": """**中和**是酸和碱之间的化学反应，产生盐和水。

**通式：**
```
酸 + 碱 → 盐 + 水
```

**反应例子：**

**1. 盐酸 + 氢氧化钠**
```
HCl + NaOH → NaCl + H₂O
(酸 + 碱 → 盐 + 水)
```
- 产物：氯化钠（食盐）+ 水
- 溶液变为中性（pH 7）

**2. 硫酸 + 氢氧化镁**
```
H₂SO₄ + Mg(OH)₂ → MgSO₄ + 2H₂O
```
- 产物：硫酸镁（泻盐）+ 水
- 用于抗酸药！

**3. 硝酸 + 氢氧化钾**
```
HNO₃ + KOH → KNO₃ + H₂O
```
- 产物：硝酸钾（肥料）+ 水

**中和过程中发生的事情：**
- 酸的H⁺离子 + 碱的OH⁻离子 → H₂O（水）
- 剩余离子形成盐
- 释放热量（放热反应）
- pH值向7（中性）移动

**实际应用：**

**1. 治疗胃酸（胃灼热）**
- 问题：过量胃酸（HCl）引起疼痛
- 解决方案：服用抗酸片（含有碱，如Mg(OH)₂）
- 反应：HCl + Mg(OH)₂ → MgCl₂ + H₂O
- 结果：酸被中和，疼痛缓解

**2. 治疗昆虫叮咬**

**蜜蜂叮咬**（酸性毒液）：
- 涂抹小苏打膏（碱）
- 碱中和酸
- 减少疼痛和肿胀

**黄蜂叮咬**（碱性毒液）：
- 涂抹醋（酸）
- 酸中和碱
- 减少疼痛和肿胀

**3. 农业 - 土壤处理**

**酸性土壤**（对某些植物不利）：
- 添加石灰（氢氧化钙 - 碱）
- 中和过量酸
- 改善植物生长

**碱性土壤**（对其他植物不利）：
- 添加硫（湿时形成酸）
- 中和过量碱
- 更好的生长条件

**4. 工业废物处理**
- 工厂废物可能非常酸性或碱性
- 添加相反物质进行中和
- 在释放到环境前使废物安全

**5. 牙膏**
- 口腔中的细菌产生酸
- 酸损害牙釉质
- 牙膏含有温和的碱
- 中和酸，保护牙齿

**新加坡背景：**

**1. 公用事业局水处理**
- 调整供水的pH值
- 使用碱中和酸性水
- 确保安全饮用水（pH ~7）

**2. 游泳池**
- 需要维持pH 7.2-7.8
- 如果太碱性则添加酸
- 如果太酸性则添加碱
- 保持水安全舒适

**3. 烹饪**
- 如果咖喱太酸（酸性），加一撮小苏打（碱）
- 中和过量酸
- 平衡味道

**中和的迹象：**
- 温度升高（变暖）
- 可能出现冒泡
- 如果存在指示剂，颜色会改变
- pH值向7移动"""
        }
    ],
    "exercises": [
        {
            "id": "ex1",
            "type": "mcq",
            "question": "Which of the following is a property of acids?",
            "question_zh": "以下哪项是酸的性质？",
            "choices": [
                "Turn red litmus paper blue",
                "Feel slippery to touch",
                "Have pH greater than 7",
                "Turn blue litmus paper red"
            ],
            "choices_zh": [
                "使红色石蕊试纸变蓝",
                "触摸时感觉滑腻",
                "pH值大于7",
                "使蓝色石蕊试纸变红"
            ],
            "answer": 3,
            "explanation": "Acids turn blue litmus paper red. The other options are properties of bases.",
            "explanation_zh": "酸使蓝色石蕊试纸变红。其他选项是碱的性质。"
        },
        {
            "id": "ex2",
            "type": "mcq",
            "question": "What is the pH of a neutral solution?",
            "question_zh": "中性溶液的pH值是多少？",
            "choices": ["0", "7", "14", "1"],
            "choices_zh": ["0", "7", "14", "1"],
            "answer": 1,
            "explanation": "A neutral solution has a pH of 7. Pure water is an example of a neutral substance.",
            "explanation_zh": "中性溶液的pH值为7。纯水是中性物质的一个例子。"
        },
        {
            "id": "ex3",
            "type": "mcq",
            "question": "What are the products of a neutralization reaction between an acid and a base?",
            "question_zh": "酸和碱之间的中和反应的产物是什么？",
            "choices": [
                "Salt and hydrogen gas",
                "Salt and water",
                "Water and carbon dioxide",
                "Only salt"
            ],
            "choices_zh": [
                "盐和氢气",
                "盐和水",
                "水和二氧化碳",
                "只有盐"
            ],
            "answer": 1,
            "explanation": "Neutralization reactions between acids and bases produce salt and water. The general equation is: Acid + Base → Salt + Water",
            "explanation_zh": "酸和碱之间的中和反应产生盐和水。通式为：酸 + 碱 → 盐 + 水"
        },
        {
            "id": "ex4",
            "type": "mcq",
            "question": "A solution has a pH of 3. How would you describe this solution?",
            "question_zh": "一个溶液的pH值为3。你会如何描述这个溶液？",
            "choices": [
                "Strongly basic",
                "Weakly basic",
                "Neutral",
                "Acidic"
            ],
            "choices_zh": [
                "强碱性",
                "弱碱性",
                "中性",
                "酸性"
            ],
            "answer": 3,
            "explanation": "Any solution with pH less than 7 is acidic. pH 3 is acidic (common examples: vinegar, lemon juice).",
            "explanation_zh": "任何pH值小于7的溶液都是酸性的。pH 3是酸性的（常见例子：醋、柠檬汁）。"
        },
        {
            "id": "ex5",
            "type": "mcq",
            "question": "Why do we use antacid medicine to treat heartburn?",
            "question_zh": "为什么我们使用抗酸药治疗胃灼热？",
            "choices": [
                "Antacids increase stomach acid",
                "Antacids are acidic and add more acid",
                "Antacids are basic and neutralize excess stomach acid",
                "Antacids have no effect on stomach acid"
            ],
            "choices_zh": [
                "抗酸药增加胃酸",
                "抗酸药是酸性的，增加更多酸",
                "抗酸药是碱性的，中和过量胃酸",
                "抗酸药对胃酸没有影响"
            ],
            "answer": 2,
            "explanation": "Antacids contain bases (like magnesium hydroxide) that neutralize excess stomach acid through a neutralization reaction, relieving heartburn symptoms.",
            "explanation_zh": "抗酸药含有碱（如氢氧化镁），通过中和反应中和过量胃酸，缓解胃灼热症状。"
        },
        {
            "id": "ex6",
            "type": "short",
            "question": "Complete this neutralization equation: HCl + NaOH → ___ + H₂O",
            "question_zh": "完成这个中和方程：HCl + NaOH → ___ + H₂O",
            "answer": "NaCl",
            "validator": "exact",
            "explanation": "When hydrochloric acid (HCl) reacts with sodium hydroxide (NaOH), they form sodium chloride (NaCl - table salt) and water (H₂O).",
            "explanation_zh": "当盐酸（HCl）与氢氧化钠（NaOH）反应时，它们形成氯化钠（NaCl - 食盐）和水（H₂O）。"
        }
    ]
}

# Save to a temporary JSON file for review
with open('acids-bases-chapter.json', 'w', encoding='utf-8') as f:
    json.dump(acids_bases_chapter, f, indent=2, ensure_ascii=False)

print('Acids & Bases chapter created successfully!')
print('Saved to acids-bases-chapter.json for review')
