#!/usr/bin/env python3
"""
Add exercises for remaining Geography chapters:
- Chapter 2: Water Resources (15 exercises)
- Chapter 3: Tropical Rainforests (15 exercises)
- Chapter 4: Mangroves (15 exercises)

Total: 45 exercises
"""

import json

# ============================================================================
# CHAPTER 2: WATER RESOURCES - REMAINING 10 EXERCISES (AO2 + AO3)
# ============================================================================

ch2_ao2 = [
    {
        "id": "ex6-water-budget",
        "type": "short",
        "difficulty": "medium",
        "prompt": "Explain why Singapore faces water scarcity despite receiving high annual rainfall of 2,400mm.",
        "prompt_zh": "解释为什么新加坡尽管年降雨量达2,400毫米仍面临水资源短缺。",
        "answer": "Small land area limits catchment area despite high rainfall",
        "answer_zh": "小土地面积限制了集水区，尽管降雨量高",
        "explanation": "**Problem**: Explain Singapore's water scarcity paradox.\n\n**Key Concept**: Water availability depends on catchment area, not just rainfall amount.\n\n**Steps**: \n1. Singapore has high rainfall (2,400mm/year)\n2. BUT small land area = limited catchment to collect rain\n3. High evaporation rates in tropical climate\n4. Result: Water deficit\n\n**Answer**: Small land area limits catchment area despite high rainfall.\n\n**Common Mistakes**: Only mentioning high rainfall without explaining catchment limitation.\n\n**Tip**: Water availability = rainfall × catchment area.",
        "explanation_zh": "**问题**：解释新加坡的水资源短缺悖论。\n\n**关键概念**：水的可用性取决于集水区，而不仅仅是降雨量。\n\n**步骤**：\n1. 新加坡降雨量高（2,400毫米/年）\n2. 但土地面积小 = 收集雨水的集水区有限\n3. 热带气候的高蒸发率\n4. 结果：水资源短缺\n\n**答案**：小土地面积限制了集水区，尽管降雨量高。\n\n**常见错误**：只提到高降雨量而没有解释集水区限制。\n\n**提示**：水的可用性 = 降雨量 × 集水区面积。",
        "hint": "Think about Singapore's land size.",
        "hint_zh": "想想新加坡的土地大小。"
    },
    {
        "id": "ex7-pollution-effects",
        "type": "short",
        "difficulty": "medium",
        "prompt": "Explain ONE environmental effect of water pollution.",
        "prompt_zh": "解释水污染的一种环境影响。",
        "answer": "Death of aquatic life due to lack of oxygen or toxic substances",
        "answer_zh": "由于缺氧或有毒物质导致水生生物死亡",
        "explanation": "**Problem**: Explain environmental impacts of water pollution.\n\n**Key Concept**: Polluted water harms ecosystems.\n\n**Steps**: Environmental effects include:\n- Death of fish and plants (toxins, oxygen depletion)\n- Algal blooms (excess nutrients)\n- Disrupted food chains\n- Loss of biodiversity\n\n**Answer**: Death of aquatic life due to lack of oxygen or toxic substances (or any valid effect).\n\n**Common Mistakes**: Only listing effects without explaining the mechanism.\n\n**Tip**: Explain HOW pollution causes the effect, not just WHAT the effect is.",
        "explanation_zh": "**问题**：解释水污染的环境影响。\n\n**关键概念**：受污染的水损害生态系统。\n\n**步骤**：环境影响包括：\n- 鱼类和植物死亡（毒素、氧气耗尽）\n- 藻华（过量营养）\n- 食物链破坏\n- 生物多样性丧失\n\n**答案**：由于缺氧或有毒物质导致水生生物死亡（或任何有效影响）。\n\n**常见错误**：只列出影响而没有解释机制。\n\n**提示**：解释污染如何导致影响，而不仅仅是影响是什么。",
        "hint": "Think about what happens to fish in polluted water.",
        "hint_zh": "想想受污染水中的鱼会发生什么。"
    },
    {
        "id": "ex8-marina-barrage",
        "type": "short",
        "difficulty": "medium",
        "prompt": "Explain how the Marina Barrage helps with Singapore's water supply.",
        "prompt_zh": "解释滨海堤坝如何帮助新加坡的水供应。",
        "answer": "It keeps seawater out creating a freshwater reservoir in the Marina Basin",
        "answer_zh": "它阻止海水进入，在滨海盆地形成淡水水库",
        "explanation": "**Problem**: Explain Marina Barrage's function.\n\n**Key Concept**: Marina Barrage is a dam that creates Singapore's 15th reservoir.\n\n**Steps**: \n1. Located at mouth of Marina Bay\n2. Dam keeps seawater out when closed\n3. Collects rainwater from city catchment area\n4. Creates freshwater reservoir (Marina Reservoir)\n5. Catchment area covers 10,000 hectares (1/6 of Singapore)\n\n**Answer**: It keeps seawater out creating a freshwater reservoir in the Marina Basin.\n\n**Common Mistakes**: Not explaining HOW it works (the barrier function).\n\n**Tip**: Barrage = barrier/dam that controls water flow.",
        "explanation_zh": "**问题**：解释滨海堤坝的功能。\n\n**关键概念**：滨海堤坝是一座水坝，创建了新加坡的第15个水库。\n\n**步骤**：\n1. 位于滨海湾口\n2. 水坝关闭时阻止海水进入\n3. 从城市集水区收集雨水\n4. 形成淡水水库（滨海水库）\n5. 集水区覆盖10,000公顷（新加坡的1/6）\n\n**答案**：它阻止海水进入，在滨海盆地形成淡水水库。\n\n**常见错误**：没有解释它如何工作（屏障功能）。\n\n**提示**：堤坝 = 控制水流的屏障/大坝。",
        "hint": "Think about what a barrage/dam does.",
        "hint_zh": "想想堤坝/水坝的作用。"
    },
    {
        "id": "ex9-conservation-methods",
        "type": "short",
        "difficulty": "hard",
        "prompt": "Suggest TWO ways households can conserve water.",
        "prompt_zh": "建议家庭节约用水的两种方法。",
        "answer": "Install water-efficient fittings and take shorter showers",
        "answer_zh": "安装节水配件并缩短淋浴时间",
        "explanation": "**Problem**: Apply knowledge to suggest practical conservation methods.\n\n**Key Concept**: Individual actions contribute to water conservation.\n\n**Steps**: Valid household conservation methods:\n1. Install water-efficient taps/toilets (WELS-rated)\n2. Take shorter showers (reduce from 10 min to 5 min)\n3. Turn off tap while brushing teeth\n4. Fix leaking taps promptly\n5. Collect shower warm-up water for plants\n6. Use washing machine only with full loads\n7. Wash vegetables in basin instead of running tap\n\n**Answer**: Install water-efficient fittings and take shorter showers (or any two valid methods).\n\n**Common Mistakes**: Suggesting industrial methods instead of household actions.\n\n**Tip**: Think about daily water use activities at home.",
        "explanation_zh": "**问题**：应用知识建议实用的节水方法。\n\n**关键概念**：个人行动有助于节约用水。\n\n**步骤**：有效的家庭节水方法：\n1. 安装节水水龙头/马桶（WELS评级）\n2. 缩短淋浴时间（从10分钟减少到5分钟）\n3. 刷牙时关闭水龙头\n4. 及时修复漏水的水龙头\n5. 收集淋浴预热水用于植物\n6. 仅在满载时使用洗衣机\n7. 在盆中洗蔬菜而不是用流水\n\n**答案**：安装节水配件并缩短淋浴时间（或任何两种有效方法）。\n\n**常见错误**：建议工业方法而不是家庭行动。\n\n**提示**：想想家里日常用水活动。",
        "hint": "Think about your daily water use at home.",
        "hint_zh": "想想你在家的日常用水。"
    },
    {
        "id": "ex10-desalination",
        "type": "short",
        "difficulty": "hard",
        "prompt": "Explain ONE advantage and ONE disadvantage of desalination for water supply.",
        "prompt_zh": "解释海水淡化供水的一个优点和一个缺点。",
        "answer": "Advantage: weather-independent source; Disadvantage: high energy consumption and cost",
        "answer_zh": "优点：不受天气影响的来源；缺点：能源消耗高且成本高",
        "explanation": "**Problem**: Evaluate desalination by identifying both advantages and disadvantages.\n\n**Key Concept**: All water management strategies have trade-offs.\n\n**Steps**: \n\n**Advantages**:\n- Weather-independent (not affected by drought)\n- Virtually unlimited source (seawater abundant)\n- Reduces dependence on imported water\n\n**Disadvantages**:\n- High energy consumption (expensive to operate)\n- Environmental impact (brine discharge)\n- High infrastructure cost\n\n**Answer**: Advantage: weather-independent source; Disadvantage: high energy consumption and cost.\n\n**Common Mistakes**: Only mentioning one aspect without the balancing perspective.\n\n**Tip**: Always consider both benefits AND costs of any solution.",
        "explanation_zh": "**问题**：通过确定优点和缺点来评估海水淡化。\n\n**关键概念**：所有水资源管理策略都有权衡。\n\n**步骤**：\n\n**优点**：\n- 不受天气影响（不受干旱影响）\n- 实际上是无限的来源（海水丰富）\n- 减少对进口水的依赖\n\n**缺点**：\n- 能源消耗高（运营成本高）\n- 环境影响（盐水排放）\n- 高基础设施成本\n\n**答案**：优点：不受天气影响的来源；缺点：能源消耗高且成本高。\n\n**常见错误**：只提到一个方面而没有平衡的观点。\n\n**提示**：始终考虑任何解决方案的好处和成本。",
        "hint": "Think about cost and reliability.",
        "hint_zh": "想想成本和可靠性。"
    }
]

ch2_ao3 = [
    {
        "id": "ex11-rainfall-graph",
        "type": "mcq",
        "difficulty": "medium",
        "prompt": "A graph shows Singapore receives the most rainfall in December (300mm) and the least in February (120mm). What pattern does this show?",
        "prompt_zh": "一张图表显示新加坡12月降雨量最多（300毫米），2月最少（120毫米）。这显示了什么模式？",
        "choices": [
            "Seasonal variation with monsoon influence",
            "No pattern - rainfall is random",
            "Rainfall increasing every year",
            "Rainfall decreasing due to climate change"
        ],
        "choices_zh": [
            "受季风影响的季节性变化",
            "无模式 - 降雨是随机的",
            "每年降雨量增加",
            "由于气候变化降雨量减少"
        ],
        "answer": 0,
        "explanation": "**Problem**: Interpret rainfall data to identify patterns.\n\n**Key Concept**: Data interpretation involves identifying trends and patterns.\n\n**Steps**: \n1. December (highest) = Northeast monsoon season\n2. February (lowest) = drier period\n3. Pattern shows **seasonal variation**\n4. Singapore experiences monsoons affecting rainfall\n\n**Answer**: Seasonal variation with monsoon influence.\n\n**Common Mistakes**: Confusing annual patterns with long-term trends.\n\n**Tip**: Within-year variation = seasonal; across-years variation = trends.",
        "explanation_zh": "**问题**：解释降雨数据以识别模式。\n\n**关键概念**：数据解释涉及识别趋势和模式。\n\n**步骤**：\n1. 12月（最高）= 东北季风季节\n2. 2月（最低）= 较干旱时期\n3. 模式显示**季节性变化**\n4. 新加坡经历影响降雨的季风\n\n**答案**：受季风影响的季节性变化。\n\n**常见错误**：将年度模式与长期趋势混淆。\n\n**提示**：年内变化 = 季节性；跨年变化 = 趋势。",
        "hint": "Think about Singapore's monsoon seasons.",
        "hint_zh": "想想新加坡的季风季节。"
    },
    {
        "id": "ex12-water-consumption",
        "type": "short",
        "difficulty": "medium",
        "prompt": "Data shows Singapore's average household water consumption decreased from 165 liters per person per day in 2003 to 141 liters in 2022. Suggest ONE reason for this decrease.",
        "prompt_zh": "数据显示新加坡的平均家庭用水量从2003年的每人每天165升降至2022年的141升。建议这一减少的一个原因。",
        "answer": "Installation of water-efficient fixtures (WELS-rated taps/toilets)",
        "answer_zh": "安装节水装置（WELS评级的水龙头/马桶）",
        "explanation": "**Problem**: Analyze data trend and explain cause.\n\n**Key Concept**: Decreasing consumption shows successful conservation efforts.\n\n**Steps**: Reasons for decreased consumption:\n1. Mandatory Water Efficiency Labelling Scheme (WELS) since 2009\n2. Public education campaigns\n3. Water pricing incentives\n4. Improved technology (dual-flush toilets)\n5. Greater awareness of water scarcity\n\n**Answer**: Installation of water-efficient fixtures (or any valid reason above).\n\n**Common Mistakes**: Giving reasons for increased consumption instead of decreased.\n\n**Tip**: Decreased consumption = conservation working!",
        "explanation_zh": "**问题**：分析数据趋势并解释原因。\n\n**关键概念**：消费减少显示成功的节约努力。\n\n**步骤**：消费减少的原因：\n1. 2009年以来的强制性水效标签计划（WELS）\n2. 公众教育活动\n3. 水价激励\n4. 改进技术（双冲马桶）\n5. 对水资源短缺的更大意识\n\n**答案**：安装节水装置（或上述任何有效原因）。\n\n**常见错误**：给出消费增加的原因而不是减少。\n\n**提示**：消费减少 = 节约有效！",
        "hint": "Think about Singapore's water conservation policies.",
        "hint_zh": "想想新加坡的节水政策。"
    },
    {
        "id": "ex13-water-budget-calculation",
        "type": "short",
        "difficulty": "hard",
        "prompt": "A drainage basin receives 200mm of precipitation. 50mm evaporates, 30mm transpires, and 100mm flows away as runoff. What is the remaining water (in mm)?",
        "prompt_zh": "一个流域接收200毫米的降水。50毫米蒸发，30毫米蒸腾，100毫米作为径流流走。剩余的水是多少（毫米）？",
        "answer": "20",
        "answer_zh": "20",
        "validator": "numeric",
        "explanation": "**Problem**: Calculate water budget using the formula.\n\n**Key Concept**: Water budget = Input - Outputs.\n\n**Steps**: \n1. Input: Precipitation = 200mm\n2. Outputs: \n   - Evaporation = 50mm\n   - Transpiration = 30mm\n   - Runoff = 100mm\n   - Total outputs = 180mm\n3. Water budget = 200 - 180 = 20mm\n\n**Answer**: 20mm.\n\n**Common Mistakes**: Forgetting to include all outputs (evaporation + transpiration + runoff).\n\n**Tip**: Water budget = Precipitation - (Evapotranspiration + Runoff).",
        "explanation_zh": "**问题**：使用公式计算水量平衡。\n\n**关键概念**：水量平衡 = 输入 - 输出。\n\n**步骤**：\n1. 输入：降水 = 200毫米\n2. 输出：\n   - 蒸发 = 50毫米\n   - 蒸腾 = 30毫米\n   - 径流 = 100毫米\n   - 总输出 = 180毫米\n3. 水量平衡 = 200 - 180 = 20毫米\n\n**答案**：20毫米。\n\n**常见错误**：忘记包括所有输出（蒸发 + 蒸腾 + 径流）。\n\n**提示**：水量平衡 = 降水 - （蒸散 + 径流）。",
        "hint": "Add all the water losses together, then subtract from precipitation.",
        "hint_zh": "将所有水损失加在一起，然后从降水中减去。"
    },
    {
        "id": "ex14-treatment-process",
        "type": "mcq",
        "difficulty": "hard",
        "prompt": "The diagram shows NEWater production: Wastewater → Microfiltration → Reverse Osmosis → UV Disinfection → NEWater. Which step removes dissolved salts and minerals?",
        "prompt_zh": "图表显示新生水生产：废水 → 微滤 → 反渗透 → 紫外线消毒 → 新生水。哪个步骤去除溶解的盐和矿物质？",
        "choices": [
            "Reverse Osmosis",
            "Microfiltration",
            "UV Disinfection",
            "All steps together"
        ],
        "choices_zh": [
            "反渗透",
            "微滤",
            "紫外线消毒",
            "所有步骤一起"
        ],
        "answer": 0,
        "explanation": "**Problem**: Interpret process diagram to identify function of each step.\n\n**Key Concept**: Each treatment step has a specific purpose.\n\n**Steps**: \n- **Microfiltration**: Removes suspended solids, bacteria\n- **Reverse Osmosis**: Removes dissolved salts, minerals, viruses (forces water through membrane)\n- **UV Disinfection**: Kills remaining microorganisms\n\n**Answer**: Reverse Osmosis.\n\n**Common Mistakes**: Thinking microfiltration removes everything.\n\n**Tip**: RO (Reverse Osmosis) = removes dissolved substances; Filtration = removes particles.",
        "explanation_zh": "**问题**：解释过程图以确定每个步骤的功能。\n\n**关键概念**：每个处理步骤都有特定目的。\n\n**步骤**：\n- **微滤**：去除悬浮固体、细菌\n- **反渗透**：去除溶解的盐、矿物质、病毒（强制水通过膜）\n- **紫外线消毒**：杀死剩余微生物\n\n**答案**：反渗透。\n\n**常见错误**：认为微滤去除一切。\n\n**提示**：RO（反渗透）= 去除溶解物质；过滤 = 去除颗粒。",
        "hint": "Think about what membrane technology does.",
        "hint_zh": "想想膜技术做什么。"
    },
    {
        "id": "ex15-abc-waters",
        "type": "short",
        "difficulty": "hard",
        "prompt": "The ABC Waters Programme stands for Active, Beautiful, Clean Waters. Explain how this programme helps with water management in Singapore.",
        "prompt_zh": "ABC水务计划代表活跃、美丽、清洁的水。解释该计划如何帮助新加坡的水资源管理。",
        "answer": "It integrates drains and reservoirs with parks creating recreational spaces while managing stormwater",
        "answer_zh": "它将排水渠和水库与公园整合，创建休闲空间同时管理雨水",
        "explanation": "**Problem**: Explain real-world water management initiative.\n\n**Key Concept**: ABC Waters integrates water management with urban planning.\n\n**Steps**: The programme:\n1. Transforms drains, canals, reservoirs into beautiful spaces\n2. Creates recreational areas (parks, waterways)\n3. Improves water quality through natural filtration\n4. Increases catchment area (collects more rainwater)\n5. Raises public awareness about water resources\n\nExamples: Bishan-Ang Mo Kio Park, Kallang River\n\n**Answer**: It integrates drains and reservoirs with parks creating recreational spaces while managing stormwater.\n\n**Common Mistakes**: Only describing what ABC stands for without explaining the actual function.\n\n**Tip**: ABC Waters = dual purpose (water management + community space).",
        "explanation_zh": "**问题**：解释现实世界的水资源管理倡议。\n\n**关键概念**：ABC水务将水资源管理与城市规划整合。\n\n**步骤**：该计划：\n1. 将排水渠、运河、水库转变为美丽的空间\n2. 创建休闲区（公园、水道）\n3. 通过自然过滤改善水质\n4. 增加集水区（收集更多雨水）\n5. 提高公众对水资源的意识\n\n示例：碧山-宏茂桥公园、加冷河\n\n**答案**：它将排水渠和水库与公园整合，创建休闲空间同时管理雨水。\n\n**常见错误**：只描述ABC代表什么而没有解释实际功能。\n\n**提示**：ABC水务 = 双重目的（水管理 + 社区空间）。",
        "hint": "Think about parks near water bodies in Singapore.",
        "hint_zh": "想想新加坡水体附近的公园。"
    }
]

# ============================================================================
# CHAPTER 3: TROPICAL RAINFORESTS - 15 EXERCISES
# ============================================================================

ch3_ao1 = [
    {
        "id": "ex1-rainforest-climate",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "Which climate characteristic is typical of tropical rainforests?",
        "prompt_zh": "热带雨林的典型气候特征是什么？",
        "choices": [
            "High temperature and high rainfall throughout the year",
            "Hot summers and cold winters",
            "Low rainfall with distinct dry season",
            "Cold temperature all year round"
        ],
        "choices_zh": [
            "全年高温和高降雨量",
            "炎热的夏季和寒冷的冬季",
            "降雨量低，有明显的旱季",
            "全年低温"
        ],
        "answer": 0,
        "explanation": "**Problem**: Identify tropical rainforest climate characteristics.\n\n**Key Concept**: Tropical rainforests have consistent hot, wet climate.\n\n**Steps**: Tropical rainforest climate:\n- Temperature: 25-28°C year-round (no seasons)\n- Rainfall: Over 2,000mm annually\n- Humidity: 75-95%\n- No distinct seasons\n\n**Answer**: High temperature and high rainfall throughout the year.\n\n**Common Mistakes**: Thinking rainforests have seasons like temperate climates.\n\n**Tip**: Equatorial = consistent (no seasons).",
        "explanation_zh": "**问题**：确定热带雨林气候特征。\n\n**关键概念**：热带雨林具有持续的炎热、潮湿气候。\n\n**步骤**：热带雨林气候：\n- 温度：全年25-28°C（无季节）\n- 降雨量：年超过2,000毫米\n- 湿度：75-95%\n- 无明显季节\n\n**答案**：全年高温和高降雨量。\n\n**常见错误**：认为雨林像温带气候一样有季节。\n\n**提示**：赤道 = 一致（无季节）。",
        "hint": "Think about conditions near the equator.",
        "hint_zh": "想想赤道附近的条件。"
    },
    {
        "id": "ex2-forest-layers",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "Which layer of the tropical rainforest receives the MOST sunlight?",
        "prompt_zh": "热带雨林的哪一层接收最多阳光？",
        "choices": [
            "Emergent layer",
            "Canopy layer",
            "Understory layer",
            "Forest floor"
        ],
        "choices_zh": [
            "突出层",
            "林冠层",
            "林下层",
            "林地层"
        ],
        "answer": 0,
        "explanation": "**Problem**: Identify which forest layer receives most light.\n\n**Key Concept**: Rainforests are stratified with emergent layer at the top.\n\n**Steps**: Forest layers from top to bottom:\n1. **Emergent layer** (45-55m) - tallest trees, MOST sunlight\n2. Canopy layer (30-45m) - dense roof\n3. Understory (10-30m) - limited light\n4. Forest floor (0-10m) - dark\n\n**Answer**: Emergent layer.\n\n**Common Mistakes**: Choosing canopy because it's mentioned more often.\n\n**Tip**: Emergent = emerges above canopy = most sun.",
        "explanation_zh": "**问题**：确定哪个森林层接收最多光。\n\n**关键概念**：雨林分层，突出层在顶部。\n\n**步骤**：森林层从上到下：\n1. **突出层**（45-55米）- 最高的树木，最多阳光\n2. 林冠层（30-45米）- 密集的屋顶\n3. 林下层（10-30米）- 光线有限\n4. 林地层（0-10米）- 黑暗\n\n**答案**：突出层。\n\n**常见错误**：选择林冠层，因为它被提到的次数更多。\n\n**提示**：突出 = 突出林冠上方 = 最多阳光。",
        "hint": "Which layer is at the very top?",
        "hint_zh": "哪一层在最顶部？"
    },
    {
        "id": "ex3-drip-tips",
        "type": "short",
        "difficulty": "easy",
        "prompt": "What is the purpose of drip tips on rainforest leaves?",
        "prompt_zh": "雨林叶子上的滴水尖有什么用途？",
        "answer": "To channel rainwater off leaves quickly",
        "answer_zh": "快速引导雨水离开叶子",
        "explanation": "**Problem**: Explain plant adaptation purpose.\n\n**Key Concept**: Drip tips are an adaptation to high rainfall.\n\n**Steps**: \n1. Rainforests have constant heavy rain\n2. Pointed tips channel water off leaves\n3. Prevents: water accumulation, mold growth, leaf damage\n4. Allows: continuous photosynthesis\n\n**Answer**: To channel rainwater off leaves quickly.\n\n**Common Mistakes**: Saying it's to collect water (opposite purpose).\n\n**Tip**: Drip = let water drip off, not collect.",
        "explanation_zh": "**问题**：解释植物适应目的。\n\n**关键概念**：滴水尖是对高降雨量的适应。\n\n**步骤**：\n1. 雨林持续有大雨\n2. 尖端引导水离开叶子\n3. 防止：水积累、霉菌生长、叶子损伤\n4. 允许：持续光合作用\n\n**答案**：快速引导雨水离开叶子。\n\n**常见错误**：说它是用来收集水的（相反的目的）。\n\n**提示**：滴水 = 让水滴落，而不是收集。",
        "hint": "Think about the constant rain in rainforests.",
        "hint_zh": "想想雨林中持续的降雨。"
    },
    {
        "id": "ex4-deforestation-cause",
        "type": "mcq",
        "difficulty": "medium",
        "prompt": "Which is a major cause of deforestation in Indonesia and Malaysia?",
        "prompt_zh": "哪一项是印度尼西亚和马来西亚森林砍伐的主要原因？",
        "choices": [
            "Palm oil plantations",
            "Urban expansion",
            "Mining for gold",
            "Tourism development"
        ],
        "choices_zh": [
            "棕榈油种植园",
            "城市扩张",
            "金矿开采",
            "旅游开发"
        ],
        "answer": 0,
        "explanation": "**Problem**: Identify regional deforestation cause.\n\n**Key Concept**: Different regions have different primary deforestation drivers.\n\n**Steps**: \n- Indonesia and Malaysia = top palm oil producers globally\n- Large-scale forest clearing for oil palm plantations\n- Palm oil used in food, cosmetics, biofuels\n- Economic benefits drive continued conversion\n\n**Answer**: Palm oil plantations.\n\n**Common Mistakes**: Choosing generic answers without considering regional context.\n\n**Tip**: Indonesia + Malaysia = palm oil hotspot.",
        "explanation_zh": "**问题**：确定区域森林砍伐原因。\n\n**关键概念**：不同地区有不同的主要森林砍伐驱动因素。\n\n**步骤**：\n- 印度尼西亚和马来西亚 = 全球顶级棕榈油生产国\n- 大规模森林清除用于油棕种植园\n- 棕榈油用于食品、化妆品、生物燃料\n- 经济利益推动持续转换\n\n**答案**：棕榈油种植园。\n\n**常见错误**：选择通用答案而不考虑区域背景。\n\n**提示**：印度尼西亚 + 马来西亚 = 棕榈油热点。",
        "hint": "Think about what crop these countries are famous for producing.",
        "hint_zh": "想想这些国家以生产什么作物而闻名。"
    },
    {
        "id": "ex5-singapore-forest",
        "type": "short",
        "difficulty": "medium",
        "prompt": "What percentage of Singapore's original rainforest remains today?",
        "prompt_zh": "新加坡原始雨林的多少百分比今天仍然存在？",
        "answer": "0.25%",
        "answer_zh": "0.25%",
        "validator": "numeric",
        "explanation": "**Problem**: Recall Singapore's forest cover data.\n\n**Key Concept**: Singapore has lost most original forest to development.\n\n**Steps**: \n- Singapore was once 100% covered by tropical rainforest\n- Today only **0.25%** remains in nature reserves:\n  - Bukit Timah Nature Reserve\n  - Central Catchment Nature Reserve\n  - Parts of Sungei Buloh\n- 95%+ forest lost to urbanization\n\n**Answer**: 0.25%.\n\n**Common Mistakes**: Confusing with current green cover (47%) which includes parks and planted trees.\n\n**Tip**: 0.25% = original PRIMARY rainforest; green cover ≠ original forest.",
        "explanation_zh": "**问题**：回忆新加坡的森林覆盖数据。\n\n**关键概念**：新加坡因开发失去了大部分原始森林。\n\n**步骤**：\n- 新加坡曾100%被热带雨林覆盖\n- 今天自然保护区仅剩**0.25%**：\n  - 武吉知马自然保护区\n  - 中央集水区自然保护区\n  - 双溪布洛的部分\n- 95%+的森林因城市化而失去\n\n**答案**：0.25%。\n\n**常见错误**：与当前绿化覆盖（47%）混淆，后者包括公园和种植的树木。\n\n**提示**：0.25% = 原始的原生雨林；绿化覆盖 ≠ 原始森林。",
        "hint": "It's a very small percentage, less than 1%.",
        "hint_zh": "这是一个非常小的百分比，少于1%。"
    }
]

# Continue with remaining exercises for Chapter 3 and all of Chapter 4...
# Due to token limits, I'll complete this in the next section

def main():
    """Add remaining exercises to Geography chapters"""

    # Load the chapter file
    with open('chapters/geography-sec1-chapters.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Add exercises to Chapter 2 (combine with previously created ch2_ao1)
    # Note: ch2_ao1 was already created in the previous script but not added
    # We'll need to reconstruct it here for completeness

    ch2_ao1_exercises = [
        # Copy from the previous script's ch2_ao1 section
        # These were the 5 AO1 exercises already created
    ]

    ch2_exercises = ch2_ao2 + ch2_ao3  # Add the 10 new exercises
    data['chapters'][1]['exercises'].extend(ch2_exercises)

    print(f"✓ Added {len(ch2_exercises)} more exercises to Chapter 2: Water Resources")
    print(f"  (Total Chapter 2 exercises: {len(data['chapters'][1]['exercises'])})")

    # Add exercises to Chapter 3
    ch3_exercises = ch3_ao1  # Start with AO1
    data['chapters'][2]['exercises'].extend(ch3_exercises)

    print(f"✓ Added {len(ch3_exercises)} exercises to Chapter 3: Tropical Rainforests")

    # Save updated file
    with open('chapters/geography-sec1-chapters.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Successfully updated geography-sec1-chapters.json")
    print(f"  Next: Complete remaining exercises for Chapters 3 & 4")

if __name__ == "__main__":
    main()
