#!/usr/bin/env python3
"""
Generate exercises for Geography Sec 1 chapters
Following Assessment Objectives (AO) framework:
- AO1: Knowledge (5 exercises) - MCQ, short answer
- AO2: Understanding and Explanation (5 exercises) - explanation questions
- AO3: Interpreting and Evaluating Geographical Data (5 exercises) - data interpretation, source-based

Total: 15 exercises per chapter × 4 chapters = 60 exercises
"""

import json

# ============================================================================
# CHAPTER 1: INTRODUCTION TO GEOGRAPHY - 15 EXERCISES
# ============================================================================

ch1_ao1 = [
    {
        "id": "ex1-what-is-geography",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "What does geography study?",
        "prompt_zh": "地理学研究什么？",
        "choices": [
            "Places and relationships between people and environments",
            "Only maps and locations",
            "Only weather patterns",
            "Only rocks and minerals"
        ],
        "choices_zh": [
            "地方以及人与环境之间的关系",
            "仅地图和位置",
            "仅天气模式",
            "仅岩石和矿物"
        ],
        "answer": 0,
        "explanation": "**Problem**: Identify what geography studies.\n\n**Key Concept**: Geography is the study of places and the relationships between people and their environments.\n\n**Steps**: Geography examines where things are, why they are there, and how they change over time, including both physical and human aspects.\n\n**Answer**: Places and relationships between people and environments.\n\n**Common Mistakes**: Thinking geography only studies maps or only physical features.\n\n**Tip**: Remember: geography = \"geo\" (earth) + \"graphy\" (description/study).",
        "explanation_zh": "**问题**：确定地理学研究什么。\n\n**关键概念**：地理学是研究地方以及人与环境之间关系的学科。\n\n**步骤**：地理学研究事物在哪里、为什么在那里以及如何随时间变化，包括自然和人文方面。\n\n**答案**：地方以及人与环境之间的关系。\n\n**常见错误**：认为地理学只研究地图或只研究自然特征。\n\n**提示**：记住：geography = \"geo\"（地球）+ \"graphy\"（描述/研究）。",
        "hint": "Think about what makes geography different from other subjects.",
        "hint_zh": "想想是什么使地理学与其他学科不同。"
    },
    {
        "id": "ex2-space-concept",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "Which geographical concept answers the question 'Where?'",
        "prompt_zh": "哪个地理概念回答\"在哪里？\"的问题？",
        "choices": [
            "Space",
            "Place",
            "Environment",
            "Scale"
        ],
        "choices_zh": [
            "空间",
            "地点",
            "环境",
            "尺度"
        ],
        "answer": 0,
        "explanation": "**Problem**: Identify which concept answers 'Where?'\n\n**Key Concept**: Space refers to the location and distribution of phenomena on Earth's surface.\n\n**Steps**: Space deals with absolute location (coordinates) and relative location (in relation to other places).\n\n**Answer**: Space.\n\n**Common Mistakes**: Confusing space with place (which asks 'What is it like?').\n\n**Tip**: Space = Where something is; Place = What it's like.",
        "explanation_zh": "**问题**：确定哪个概念回答\"在哪里？\"\n\n**关键概念**：空间是指地球表面现象的位置和分布。\n\n**步骤**：空间涉及绝对位置（坐标）和相对位置（与其他地方的关系）。\n\n**答案**：空间。\n\n**常见错误**：将空间与地点混淆（地点回答\"是什么样的？\"）。\n\n**提示**：空间 = 某物在哪里；地点 = 它是什么样的。",
        "hint": "Think about coordinates like 1°N, 103°E for Singapore.",
        "hint_zh": "想想新加坡的坐标，如北纬1°、东经103°。"
    },
    {
        "id": "ex3-gip-stages",
        "type": "short",
        "difficulty": "easy",
        "prompt": "Name the FIRST stage of the Geographical Inquiry Process (GIP).",
        "prompt_zh": "说出地理探究过程（GIP）的第一阶段。",
        "answer": "Sparking Curiosity",
        "answer_zh": "激发好奇心",
        "explanation": "**Problem**: Identify the first stage of GIP.\n\n**Key Concept**: GIP has four stages: Sparking Curiosity → Gathering Data → Exercising Reasoning → Reflective Thinking.\n\n**Steps**: The first stage involves asking geographical questions and identifying issues to investigate.\n\n**Answer**: Sparking Curiosity.\n\n**Common Mistakes**: Confusing with Gathering Data (the second stage).\n\n**Tip**: Remember the sequence: Spark → Gather → Reason → Reflect.",
        "explanation_zh": "**问题**：确定GIP的第一阶段。\n\n**关键概念**：GIP有四个阶段：激发好奇心 → 收集数据 → 进行推理 → 反思性思考。\n\n**步骤**：第一阶段涉及提出地理问题和确定要调查的问题。\n\n**答案**：激发好奇心。\n\n**常见错误**：与收集数据（第二阶段）混淆。\n\n**提示**：记住顺序：激发 → 收集 → 推理 → 反思。",
        "hint": "It starts with asking questions.",
        "hint_zh": "它从提出问题开始。"
    },
    {
        "id": "ex4-singapore-latitude",
        "type": "mcq",
        "difficulty": "medium",
        "prompt": "Singapore's location at 1°N, 103°E illustrates which geographical concept?",
        "prompt_zh": "新加坡位于北纬1°、东经103°说明了哪个地理概念？",
        "choices": [
            "Space",
            "Place",
            "Environment",
            "Scale"
        ],
        "choices_zh": [
            "空间",
            "地点",
            "环境",
            "尺度"
        ],
        "answer": 0,
        "explanation": "**Problem**: Apply geographical concept to Singapore's coordinates.\n\n**Key Concept**: Space refers to location and distribution using coordinates.\n\n**Steps**: Coordinates (1°N, 103°E) show Singapore's absolute position on Earth's surface, which is the concept of space.\n\n**Answer**: Space.\n\n**Common Mistakes**: Choosing 'Place' which refers to characteristics, not location.\n\n**Tip**: Coordinates always relate to the concept of space.",
        "explanation_zh": "**问题**：将地理概念应用于新加坡的坐标。\n\n**关键概念**：空间是指使用坐标的位置和分布。\n\n**步骤**：坐标（北纬1°、东经103°）显示新加坡在地球表面的绝对位置，这是空间的概念。\n\n**答案**：空间。\n\n**常见错误**：选择\"地点\"，它指的是特征，而非位置。\n\n**提示**：坐标总是与空间概念相关。",
        "hint": "Coordinates show where something is located.",
        "hint_zh": "坐标显示某物的位置。"
    },
    {
        "id": "ex5-scale-levels",
        "type": "mcq",
        "difficulty": "medium",
        "prompt": "Studying water scarcity in the entire Southeast Asia region is an example of which scale?",
        "prompt_zh": "研究整个东南亚地区的水资源短缺是哪个尺度的示例？",
        "choices": [
            "Regional scale",
            "Local scale",
            "National scale",
            "Global scale"
        ],
        "choices_zh": [
            "区域尺度",
            "地方尺度",
            "国家尺度",
            "全球尺度"
        ],
        "answer": 0,
        "explanation": "**Problem**: Identify the appropriate scale for studying Southeast Asia.\n\n**Key Concept**: Scale refers to the level of detail or extent of area being studied.\n\n**Steps**: \n- Local scale: neighborhood/community\n- National scale: one country\n- Regional scale: multiple countries in an area\n- Global scale: worldwide\n\nSoutheast Asia includes multiple countries, so it's regional scale.\n\n**Answer**: Regional scale.\n\n**Common Mistakes**: Confusing regional with global scale.\n\n**Tip**: Regional scale = a group of countries in the same geographic area.",
        "explanation_zh": "**问题**：确定研究东南亚的适当尺度。\n\n**关键概念**：尺度是指所研究区域的详细程度或范围。\n\n**步骤**：\n- 地方尺度：社区\n- 国家尺度：一个国家\n- 区域尺度：一个地区的多个国家\n- 全球尺度：全球\n\n东南亚包括多个国家，所以是区域尺度。\n\n**答案**：区域尺度。\n\n**常见错误**：将区域尺度与全球尺度混淆。\n\n**提示**：区域尺度 = 同一地理区域的一组国家。",
        "hint": "Think about how many countries are in Southeast Asia.",
        "hint_zh": "想想东南亚有多少个国家。"
    }
]

ch1_ao2 = [
    {
        "id": "ex6-place-characteristics",
        "type": "short",
        "difficulty": "medium",
        "prompt": "Explain what the geographical concept of 'Place' refers to.",
        "prompt_zh": "解释地理概念\"地点\"指的是什么。",
        "answer": "Place refers to the physical and human characteristics that make a location unique",
        "answer_zh": "地点是指使一个位置独特的自然和人文特征",
        "explanation": "**Problem**: Explain the concept of 'Place'.\n\n**Key Concept**: Place describes what makes a location special and different from other locations.\n\n**Steps**: Place includes both:\n- Physical characteristics (landforms, climate, vegetation)\n- Human characteristics (buildings, culture, activities)\n\nExample: Marina Bay's characteristics include iconic buildings (Marina Bay Sands), waterfront setting, and cultural venues.\n\n**Answer**: Place refers to the physical and human characteristics that make a location unique.\n\n**Common Mistakes**: Confusing place with space (location).\n\n**Tip**: Place answers 'What is it like?' while space answers 'Where is it?'",
        "explanation_zh": "**问题**：解释\"地点\"的概念。\n\n**关键概念**：地点描述了使一个位置特殊并与其他位置不同的东西。\n\n**步骤**：地点包括：\n- 自然特征（地形、气候、植被）\n- 人文特征（建筑、文化、活动）\n\n示例：滨海湾的特征包括标志性建筑（滨海湾金沙）、海滨环境和文化场所。\n\n**答案**：地点是指使一个位置独特的自然和人文特征。\n\n**常见错误**：将地点与空间（位置）混淆。\n\n**提示**：地点回答\"是什么样的？\"而空间回答\"在哪里？\"",
        "hint": "Think about what makes Singapore different from other countries.",
        "hint_zh": "想想是什么使新加坡与其他国家不同。"
    },
    {
        "id": "ex7-environment-interaction",
        "type": "short",
        "difficulty": "medium",
        "prompt": "Give ONE example of how Singapore has modified its environment.",
        "prompt_zh": "举一个新加坡如何改造其环境的例子。",
        "answer": "Land reclamation to expand territory",
        "answer_zh": "填海造地以扩大领土",
        "explanation": "**Problem**: Provide an example of human-environment interaction in Singapore.\n\n**Key Concept**: Environment concept examines how people interact with and modify their surroundings.\n\n**Steps**: Singapore has modified its environment through:\n- Land reclamation (added 25% to land area)\n- Building reservoirs (Marina Barrage)\n- Creating green spaces (Gardens by the Bay)\n- Constructing underground infrastructure (MRT tunnels)\n\n**Answer**: Land reclamation to expand territory (or any valid example above).\n\n**Common Mistakes**: Describing the environment instead of explaining how humans modified it.\n\n**Tip**: Look for how Singapore overcomes natural limitations through technology.",
        "explanation_zh": "**问题**：提供新加坡人与环境互动的示例。\n\n**关键概念**：环境概念研究人们如何与周围环境互动和改造。\n\n**步骤**：新加坡通过以下方式改造了环境：\n- 填海造地（增加了25%的土地面积）\n- 建造水库（滨海堤坝）\n- 创建绿色空间（滨海湾花园）\n- 建造地下基础设施（地铁隧道）\n\n**答案**：填海造地以扩大领土（或上述任何有效示例）。\n\n**常见错误**：描述环境而不是解释人类如何改造它。\n\n**提示**：寻找新加坡如何通过技术克服自然限制。",
        "hint": "Think about how Singapore increased its land area.",
        "hint_zh": "想想新加坡如何增加其土地面积。"
    },
    {
        "id": "ex8-gip-reasoning",
        "type": "short",
        "difficulty": "medium",
        "prompt": "In the GIP stage of 'Exercising Reasoning', what do geographers do with the data they have collected?",
        "prompt_zh": "在GIP的\"进行推理\"阶段，地理学家对他们收集的数据做什么？",
        "answer": "Analyze and interpret data to identify patterns, relationships, and trends",
        "answer_zh": "分析和解释数据以识别模式、关系和趋势",
        "explanation": "**Problem**: Explain what happens in the 'Exercising Reasoning' stage.\n\n**Key Concept**: This stage involves making sense of collected data.\n\n**Steps**: In Exercising Reasoning, geographers:\n1. Analyze data systematically\n2. Interpret what the data shows\n3. Identify patterns and relationships\n4. Draw evidence-based conclusions\n\nExample: After collecting rainfall data, analyze whether rainfall varies by season and explain why.\n\n**Answer**: Analyze and interpret data to identify patterns, relationships, and trends.\n\n**Common Mistakes**: Thinking this stage only involves collecting more data.\n\n**Tip**: Reasoning = thinking about what the data means, not just having the data.",
        "explanation_zh": "**问题**：解释\"进行推理\"阶段发生了什么。\n\n**关键概念**：这个阶段涉及理解收集的数据。\n\n**步骤**：在进行推理中，地理学家：\n1. 系统地分析数据\n2. 解释数据显示的内容\n3. 识别模式和关系\n4. 得出基于证据的结论\n\n示例：收集降雨数据后，分析降雨是否因季节而异并解释原因。\n\n**答案**：分析和解释数据以识别模式、关系和趋势。\n\n**常见错误**：认为这个阶段只涉及收集更多数据。\n\n**提示**：推理 = 思考数据的含义，而不仅仅是拥有数据。",
        "hint": "Think about what you do after you have collected data.",
        "hint_zh": "想想你收集数据后做什么。"
    },
    {
        "id": "ex9-why-study-geography",
        "type": "short",
        "difficulty": "medium",
        "prompt": "Explain ONE reason why studying geography is important for Singapore.",
        "prompt_zh": "解释为什么学习地理学对新加坡很重要的一个原因。",
        "answer": "It helps us understand and solve challenges like water scarcity and limited land",
        "answer_zh": "它帮助我们理解和解决水资源短缺和土地有限等挑战",
        "explanation": "**Problem**: Explain the importance of geography for Singapore.\n\n**Key Concept**: Geography provides tools to understand and address local challenges.\n\n**Steps**: For Singapore, geography is important because it helps us:\n- Manage water resources (we import water and use NEWater)\n- Plan urban development (limited land requires careful planning)\n- Address climate change (rising sea levels threaten low-lying areas)\n- Understand our strategic location for trade\n\n**Answer**: It helps us understand and solve challenges like water scarcity and limited land (or any valid reason above).\n\n**Common Mistakes**: Giving a general reason without linking to Singapore's specific context.\n\n**Tip**: Think about Singapore's unique challenges: small size, limited resources, island nation.",
        "explanation_zh": "**问题**：解释地理学对新加坡的重要性。\n\n**关键概念**：地理学提供了理解和应对本地挑战的工具。\n\n**步骤**：对于新加坡，地理学很重要，因为它帮助我们：\n- 管理水资源（我们进口水并使用新生水）\n- 规划城市发展（有限的土地需要仔细规划）\n- 应对气候变化（海平面上升威胁低洼地区）\n- 理解我们在贸易中的战略位置\n\n**答案**：它帮助我们理解和解决水资源短缺和土地有限等挑战（或上述任何有效原因）。\n\n**常见错误**：给出一般原因而没有联系到新加坡的具体背景。\n\n**提示**：想想新加坡的独特挑战：小面积、有限资源、岛国。",
        "hint": "Think about Singapore's limited natural resources.",
        "hint_zh": "想想新加坡有限的自然资源。"
    },
    {
        "id": "ex10-gi-fieldwork",
        "type": "short",
        "difficulty": "hard",
        "prompt": "What is the difference between Geographical Inquiry Process (GIP) and Geographical Investigation (GI)?",
        "prompt_zh": "地理探究过程（GIP）和地理调查（GI）有什么区别？",
        "answer": "GI involves actual fieldwork while GIP is a broader framework that can use secondary data",
        "answer_zh": "GI涉及实际的实地考察，而GIP是可以使用次要数据的更广泛的框架",
        "explanation": "**Problem**: Distinguish between GIP and GI.\n\n**Key Concept**: Both are inquiry methods but differ in data collection approach.\n\n**Steps**: \n- **GIP**: 4-stage framework (Spark Curiosity, Gather Data, Exercise Reasoning, Reflect) - can use any data sources\n- **GI**: 5-stage process that specifically requires **fieldwork** - collecting primary data through direct observation and measurement\n\nGI is a specialized application of GIP with emphasis on hands-on data collection.\n\n**Answer**: GI involves actual fieldwork while GIP is a broader framework that can use secondary data.\n\n**Common Mistakes**: Thinking they are the same thing.\n\n**Tip**: GI = GIP + fieldwork requirement.",
        "explanation_zh": "**问题**：区分GIP和GI。\n\n**关键概念**：两者都是探究方法，但数据收集方法不同。\n\n**步骤**：\n- **GIP**：4阶段框架（激发好奇心、收集数据、进行推理、反思）- 可以使用任何数据来源\n- **GI**：5阶段过程，特别需要**实地考察** - 通过直接观察和测量收集原始数据\n\nGI是GIP的专门应用，强调动手数据收集。\n\n**答案**：GI涉及实际的实地考察，而GIP是可以使用次要数据的更广泛的框架。\n\n**常见错误**：认为它们是同一件事。\n\n**提示**：GI = GIP + 实地考察要求。",
        "hint": "Think about whether you need to go outside to collect data.",
        "hint_zh": "想想你是否需要外出收集数据。"
    }
]

ch1_ao3 = [
    {
        "id": "ex11-map-scale",
        "type": "mcq",
        "difficulty": "medium",
        "prompt": "A map shows that 1 cm represents 5 km in reality. What type of scale does this represent?",
        "prompt_zh": "一张地图显示1厘米代表现实中的5公里。这代表什么类型的尺度？",
        "choices": [
            "Statement scale",
            "Local scale",
            "Regional scale",
            "Graphical scale"
        ],
        "choices_zh": [
            "文字比例尺",
            "地方尺度",
            "区域尺度",
            "图形比例尺"
        ],
        "answer": 0,
        "explanation": "**Problem**: Identify the type of map scale being used.\n\n**Key Concept**: Maps use different types of scales to show relationship between map distance and actual distance.\n\n**Steps**: \n- **Statement scale**: Words/numbers (e.g., '1 cm = 5 km')\n- **Ratio scale**: Numbers only (e.g., 1:500,000)\n- **Graphical scale**: Visual bar showing distance\n\nThe question describes a statement scale.\n\n**Answer**: Statement scale.\n\n**Common Mistakes**: Confusing map scale with geographical scale (local/regional/global).\n\n**Tip**: If it uses words to explain the scale, it's a statement scale.",
        "explanation_zh": "**问题**：确定正在使用的地图比例尺类型。\n\n**关键概念**：地图使用不同类型的比例尺来显示地图距离和实际距离之间的关系。\n\n**步骤**：\n- **文字比例尺**：文字/数字（例如，\"1厘米 = 5公里\"）\n- **比率比例尺**：仅数字（例如，1:500,000）\n- **图形比例尺**：显示距离的视觉条\n\n问题描述的是文字比例尺。\n\n**答案**：文字比例尺。\n\n**常见错误**：将地图比例尺与地理尺度（地方/区域/全球）混淆。\n\n**提示**：如果它使用文字来解释比例尺，那就是文字比例尺。",
        "hint": "Look at how the scale is expressed - in words or just numbers?",
        "hint_zh": "看比例尺如何表达 - 用文字还是只用数字？"
    },
    {
        "id": "ex12-photo-interpretation",
        "type": "mcq",
        "difficulty": "medium",
        "prompt": "Study the photograph of Marina Bay Sands. Which geographical concept does analyzing this photograph help you understand?",
        "prompt_zh": "研究滨海湾金沙的照片。分析这张照片有助于你理解哪个地理概念？",
        "choices": [
            "Place - what Marina Bay is like",
            "Space - where Marina Bay is located",
            "Scale - the size of Marina Bay",
            "Environment - the climate of Marina Bay"
        ],
        "choices_zh": [
            "地点 - 滨海湾是什么样的",
            "空间 - 滨海湾在哪里",
            "尺度 - 滨海湾的大小",
            "环境 - 滨海湾的气候"
        ],
        "answer": 0,
        "explanation": "**Problem**: Apply geographical concepts to photograph interpretation.\n\n**Key Concept**: Different data sources (photos, maps, statistics) help understand different geographical concepts.\n\n**Steps**: \n- Photographs show **characteristics** and features of a place\n- They answer 'What is it like?' rather than 'Where is it?'\n- Marina Bay Sands photo shows iconic architecture, waterfront, modern development = characteristics of the place\n\n**Answer**: Place - what Marina Bay is like.\n\n**Common Mistakes**: Choosing space because the photo shows a location.\n\n**Tip**: Photos are best for understanding 'Place' (characteristics), while maps are best for 'Space' (location).",
        "explanation_zh": "**问题**：将地理概念应用于照片解释。\n\n**关键概念**：不同的数据来源（照片、地图、统计数据）有助于理解不同的地理概念。\n\n**步骤**：\n- 照片显示地点的**特征**和特点\n- 它们回答\"是什么样的？\"而不是\"在哪里？\"\n- 滨海湾金沙照片显示标志性建筑、海滨、现代发展 = 地点的特征\n\n**答案**：地点 - 滨海湾是什么样的。\n\n**常见错误**：选择空间，因为照片显示了一个位置。\n\n**提示**：照片最适合理解\"地点\"（特征），而地图最适合\"空间\"（位置）。",
        "hint": "Think about what information photographs provide best.",
        "hint_zh": "想想照片最能提供什么信息。"
    },
    {
        "id": "ex13-singapore-coordinates",
        "type": "short",
        "difficulty": "medium",
        "prompt": "Singapore is located at approximately 1°N, 103°E. Based on these coordinates, is Singapore in the Northern or Southern Hemisphere?",
        "prompt_zh": "新加坡大约位于北纬1°、东经103°。根据这些坐标，新加坡在北半球还是南半球？",
        "answer": "Northern Hemisphere",
        "answer_zh": "北半球",
        "explanation": "**Problem**: Interpret coordinates to determine hemisphere location.\n\n**Key Concept**: Coordinates use latitude (N/S) and longitude (E/W) to pinpoint locations.\n\n**Steps**: \n1. Latitude of 1°N means 1 degree North of the equator\n2. 'N' (North) indicates Northern Hemisphere\n3. 'S' would indicate Southern Hemisphere\n4. Singapore is just north of the equator\n\n**Answer**: Northern Hemisphere.\n\n**Common Mistakes**: Confusing latitude with longitude, or N/S with E/W.\n\n**Tip**: N = Northern Hemisphere, S = Southern Hemisphere. Singapore's N shows it's in Northern Hemisphere.",
        "explanation_zh": "**问题**：解释坐标以确定半球位置。\n\n**关键概念**：坐标使用纬度（N/S）和经度（E/W）来精确定位。\n\n**步骤**：\n1. 北纬1°意味着在赤道以北1度\n2. \"N\"（北）表示北半球\n3. \"S\"表示南半球\n4. 新加坡在赤道以北\n\n**答案**：北半球。\n\n**常见错误**：将纬度与经度混淆，或将N/S与E/W混淆。\n\n**提示**：N = 北半球，S = 南半球。新加坡的N显示它在北半球。",
        "hint": "Look at the N in the latitude coordinate.",
        "hint_zh": "看纬度坐标中的N。"
    },
    {
        "id": "ex14-data-collection",
        "type": "mcq",
        "difficulty": "hard",
        "prompt": "Students are investigating traffic patterns near their school. Which method represents PRIMARY data collection?",
        "prompt_zh": "学生正在调查学校附近的交通模式。哪种方法代表原始数据收集？",
        "choices": [
            "Counting vehicles at different times of day",
            "Reading transport statistics from LTA website",
            "Looking at traffic maps online",
            "Watching videos of the area on YouTube"
        ],
        "choices_zh": [
            "在一天的不同时间计数车辆",
            "从陆路交通管理局网站阅读交通统计数据",
            "在线查看交通地图",
            "在YouTube上观看该地区的视频"
        ],
        "answer": 0,
        "explanation": "**Problem**: Distinguish between primary and secondary data collection.\n\n**Key Concept**: \n- **Primary data**: Collected firsthand by the investigator (observations, surveys, measurements)\n- **Secondary data**: Obtained from existing sources (books, websites, databases)\n\n**Steps**: Analyze each option:\n1. Counting vehicles = direct observation = PRIMARY\n2. LTA statistics = existing data = SECONDARY\n3. Online maps = existing data = SECONDARY\n4. YouTube videos = existing data = SECONDARY\n\n**Answer**: Counting vehicles at different times of day.\n\n**Common Mistakes**: Thinking all methods that use technology are secondary data.\n\n**Tip**: If YOU are the one collecting/measuring/observing, it's primary data.",
        "explanation_zh": "**问题**：区分原始数据和次要数据收集。\n\n**关键概念**：\n- **原始数据**：由调查者直接收集（观察、调查、测量）\n- **次要数据**：从现有来源获得（书籍、网站、数据库）\n\n**步骤**：分析每个选项：\n1. 计数车辆 = 直接观察 = 原始\n2. 陆路交通管理局统计 = 现有数据 = 次要\n3. 在线地图 = 现有数据 = 次要\n4. YouTube视频 = 现有数据 = 次要\n\n**答案**：在一天的不同时间计数车辆。\n\n**常见错误**：认为所有使用技术的方法都是次要数据。\n\n**提示**：如果你是收集/测量/观察的人，那就是原始数据。",
        "hint": "Which method involves students doing their own observations?",
        "hint_zh": "哪种方法涉及学生自己的观察？"
    },
    {
        "id": "ex15-gi-application",
        "type": "short",
        "difficulty": "hard",
        "prompt": "A class plans to investigate plastic pollution at East Coast Park beach. Suggest ONE method they could use to collect PRIMARY data.",
        "prompt_zh": "一个班级计划调查东海岸公园海滩的塑料污染。建议他们可以使用一种方法来收集原始数据。",
        "answer": "Count the number of plastic items found along a measured section of beach",
        "answer_zh": "计算在测量的海滩段发现的塑料物品数量",
        "explanation": "**Problem**: Apply understanding of primary data collection to a real investigation.\n\n**Key Concept**: Geographical Investigation (GI) requires collecting primary data through fieldwork.\n\n**Steps**: Valid methods for investigating beach plastic pollution include:\n- Counting plastic items along transects\n- Categorizing types of plastic waste\n- Measuring area covered by plastic\n- Surveying beachgoers about littering behavior\n- Taking photographs for visual analysis\n\n**Answer**: Count the number of plastic items found along a measured section of beach (or any valid method above).\n\n**Common Mistakes**: Suggesting secondary data methods like reading LTA reports.\n\n**Tip**: PRIMARY data = go to the location and collect data yourself through observation/measurement.",
        "explanation_zh": "**问题**：将对原始数据收集的理解应用于真实调查。\n\n**关键概念**：地理调查（GI）需要通过实地考察收集原始数据。\n\n**步骤**：调查海滩塑料污染的有效方法包括：\n- 沿样带计数塑料物品\n- 分类塑料废物类型\n- 测量塑料覆盖的面积\n- 调查海滩游客的丢弃行为\n- 拍照进行视觉分析\n\n**答案**：计算在测量的海滩段发现的塑料物品数量（或上述任何有效方法）。\n\n**常见错误**：建议次要数据方法，如阅读陆路交通管理局报告。\n\n**提示**：原始数据 = 去位置并通过观察/测量自己收集数据。",
        "hint": "Think about what students can observe or measure at the beach.",
        "hint_zh": "想想学生可以在海滩观察或测量什么。"
    }
]

# ============================================================================
# CHAPTER 2: WATER RESOURCES - 15 EXERCISES
# ============================================================================

ch2_ao1 = [
    {
        "id": "ex1-hydrological-cycle",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "Which process in the hydrological cycle involves water changing from liquid to gas?",
        "prompt_zh": "水文循环中的哪个过程涉及水从液态变为气态？",
        "choices": [
            "Evaporation",
            "Condensation",
            "Precipitation",
            "Infiltration"
        ],
        "choices_zh": [
            "蒸发",
            "凝结",
            "降水",
            "渗透"
        ],
        "answer": 0,
        "explanation": "**Problem**: Identify the process of water changing state from liquid to gas.\n\n**Key Concept**: The hydrological cycle involves water changing between different states.\n\n**Steps**: \n- Evaporation: liquid → gas (heat from sun)\n- Condensation: gas → liquid (cooling)\n- Precipitation: water falling (rain, snow)\n- Infiltration: water soaking into ground\n\n**Answer**: Evaporation.\n\n**Common Mistakes**: Confusing evaporation with transpiration (plants releasing water vapor).\n\n**Tip**: Evaporation = water evaporating into the air.",
        "explanation_zh": "**问题**：确定水从液态变为气态的过程。\n\n**关键概念**：水文循环涉及水在不同状态之间的变化。\n\n**步骤**：\n- 蒸发：液态 → 气态（太阳热量）\n- 凝结：气态 → 液态（冷却）\n- 降水：水落下（雨、雪）\n- 渗透：水渗入地下\n\n**答案**：蒸发。\n\n**常见错误**：将蒸发与蒸腾（植物释放水蒸气）混淆。\n\n**提示**：蒸发 = 水蒸发到空气中。",
        "hint": "Think about what happens to water on a hot sunny day.",
        "hint_zh": "想想在炎热的晴天水会发生什么。"
    },
    {
        "id": "ex2-four-national-taps",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "Which of the following is NOT one of Singapore's Four National Taps?",
        "prompt_zh": "以下哪一项不是新加坡四大国家水喉之一？",
        "choices": [
            "Rainwater harvesting from homes",
            "Local catchment water",
            "Imported water",
            "NEWater"
        ],
        "choices_zh": [
            "家庭雨水收集",
            "本地集水区水",
            "进口水",
            "新生水"
        ],
        "answer": 0,
        "explanation": "**Problem**: Identify Singapore's Four National Taps water sources.\n\n**Key Concept**: Singapore diversifies water supply through four main sources.\n\n**Steps**: The Four National Taps are:\n1. Local catchment water (reservoirs)\n2. Imported water (from Johor, Malaysia)\n3. NEWater (treated wastewater)\n4. Desalinated water (from seawater)\n\nRainwater harvesting from homes is encouraged but not one of the Four National Taps.\n\n**Answer**: Rainwater harvesting from homes.\n\n**Common Mistakes**: Thinking all water sources are part of the Four Taps.\n\n**Tip**: Remember the official four: Catchment, Import, NEWater, Desalination.",
        "explanation_zh": "**问题**：确定新加坡的四大国家水喉水源。\n\n**关键概念**：新加坡通过四个主要来源使水供应多样化。\n\n**步骤**：四大国家水喉是：\n1. 本地集水区水（水库）\n2. 进口水（来自马来西亚柔佛）\n3. 新生水（处理过的废水）\n4. 淡化水（来自海水）\n\n家庭雨水收集是受鼓励的，但不是四大国家水喉之一。\n\n**答案**：家庭雨水收集。\n\n**常见错误**：认为所有水源都是四大水喉的一部分。\n\n**提示**：记住官方四个：集水区、进口、新生水、淡化。",
        "hint": "Think about PUB's official water supply strategy.",
        "hint_zh": "想想公用事业局的官方供水策略。"
    },
    {
        "id": "ex3-water-uses",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "Manufacturing semiconductors in factories is an example of which type of water use?",
        "prompt_zh": "在工厂制造半导体是哪种水使用类型的示例？",
        "choices": [
            "Industrial use",
            "Domestic use",
            "Agricultural use",
            "Commercial use"
        ],
        "choices_zh": [
            "工业用途",
            "家庭用途",
            "农业用途",
            "商业用途"
        ],
        "answer": 0,
        "explanation": "**Problem**: Classify water use type for semiconductor manufacturing.\n\n**Key Concept**: Water uses are categorized into domestic, industrial, agricultural, and commercial.\n\n**Steps**: \n- Domestic: household activities\n- Industrial: manufacturing, factories\n- Agricultural: farming, irrigation\n- Commercial: businesses, offices, hotels\n\nSemiconductor manufacturing is industrial production.\n\n**Answer**: Industrial use.\n\n**Common Mistakes**: Choosing commercial use (which is for retail/service businesses).\n\n**Tip**: Manufacturing = industrial; Retail/services = commercial.",
        "explanation_zh": "**问题**：为半导体制造分类水使用类型。\n\n**关键概念**：水的使用分为家庭、工业、农业和商业。\n\n**步骤**：\n- 家庭：家庭活动\n- 工业：制造、工厂\n- 农业：农业、灌溉\n- 商业：企业、办公室、酒店\n\n半导体制造是工业生产。\n\n**答案**：工业用途。\n\n**常见错误**：选择商业用途（用于零售/服务企业）。\n\n**提示**：制造 = 工业；零售/服务 = 商业。",
        "hint": "Think about what category factories fall under.",
        "hint_zh": "想想工厂属于什么类别。"
    },
    {
        "id": "ex4-water-pollution-source",
        "type": "mcq",
        "difficulty": "medium",
        "prompt": "Fertilizers from farms washing into rivers is an example of which cause of water pollution?",
        "prompt_zh": "农场的肥料流入河流是水污染的哪种原因的示例？",
        "choices": [
            "Agricultural runoff",
            "Industrial waste",
            "Sewage",
            "Oil spills"
        ],
        "choices_zh": [
            "农业径流",
            "工业废物",
            "污水",
            "石油泄漏"
        ],
        "answer": 0,
        "explanation": "**Problem**: Identify the pollution source type.\n\n**Key Concept**: Water pollution has different sources based on origin.\n\n**Steps**: \n- Agricultural runoff: fertilizers, pesticides from farms\n- Industrial waste: chemicals from factories\n- Sewage: human waste\n- Oil spills: petroleum from ships\n\nFertilizers from farms = agricultural runoff.\n\n**Answer**: Agricultural runoff.\n\n**Common Mistakes**: Thinking all chemical pollution is industrial.\n\n**Tip**: If it comes from farming activities, it's agricultural runoff.",
        "explanation_zh": "**问题**：确定污染源类型。\n\n**关键概念**：水污染有基于来源的不同来源。\n\n**步骤**：\n- 农业径流：来自农场的肥料、农药\n- 工业废物：来自工厂的化学品\n- 污水：人类废物\n- 石油泄漏：来自船只的石油\n\n来自农场的肥料 = 农业径流。\n\n**答案**：农业径流。\n\n**常见错误**：认为所有化学污染都是工业污染。\n\n**提示**：如果它来自农业活动，那就是农业径流。",
        "hint": "The pollution is coming from farms, not factories.",
        "hint_zh": "污染来自农场，而非工厂。"
    },
    {
        "id": "ex5-newater",
        "type": "short",
        "difficulty": "medium",
        "prompt": "What is NEWater made from?",
        "prompt_zh": "新生水是由什么制成的？",
        "answer": "Treated wastewater",
        "answer_zh": "处理过的废水",
        "explanation": "**Problem**: Identify the source of NEWater.\n\n**Key Concept**: NEWater is Singapore's solution to water scarcity using advanced technology.\n\n**Steps**: \n1. NEWater is recycled water\n2. Source: wastewater (used water from homes and businesses)\n3. Process: Advanced membrane technology and UV treatment\n4. Result: Ultra-clean, high-grade reclaimed water\n\nNEWater meets up to 40% of Singapore's current water needs.\n\n**Answer**: Treated wastewater (or recycled water).\n\n**Common Mistakes**: Saying seawater (that's desalinated water, not NEWater).\n\n**Tip**: NEWater = NEW water from WASTE water.",
        "explanation_zh": "**问题**：确定新生水的来源。\n\n**关键概念**：新生水是新加坡使用先进技术解决水资源短缺的解决方案。\n\n**步骤**：\n1. 新生水是回收水\n2. 来源：废水（来自家庭和企业的用过的水）\n3. 过程：先进膜技术和紫外线处理\n4. 结果：超清洁、高品质的回收水\n\n新生水满足新加坡当前水需求的40%。\n\n**答案**：处理过的废水（或回收水）。\n\n**常见错误**：说海水（那是淡化水，不是新生水）。\n\n**提示**：新生水 = 来自废水的新水。",
        "hint": "Think about the word 'recycled'.",
        "hint_zh": "想想\"回收\"这个词。"
    }
]

# Due to length constraints, I'll create a separate continuation with remaining exercises
# This file would be too long, so let me create the complete exercises in the integration step

def main():
    """Load existing chapters and add exercises"""
    # Load the chapter file
    with open('chapters/geography-sec1-chapters.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Add exercises to Chapter 1
    ch1_exercises = ch1_ao1 + ch1_ao2 + ch1_ao3
    data['chapters'][0]['exercises'] = ch1_exercises

    print(f"✓ Added {len(ch1_exercises)} exercises to Chapter 1: Introduction to Geography")

    # Save updated file
    with open('chapters/geography-sec1-chapters.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Successfully updated geography-sec1-chapters.json")
    print(f"  Total exercises added: {len(ch1_exercises)}")
    print(f"  Next: Create exercises for remaining chapters (Water, Rainforests, Mangroves)")

if __name__ == "__main__":
    main()
