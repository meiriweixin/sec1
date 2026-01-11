#!/usr/bin/env python3
"""
Add the missing chapter: "How Can We Sustainably Manage Natural Resources?"
This should come BEFORE the specific resource chapters (Water, Rainforests, Mangroves)
Following the official MOE 2021 Lower Secondary Geography Syllabus structure
"""

import json

def create_sustainability_chapter():
    """Create the thematic question chapter on sustainable resource management"""

    chapter = {
        "id": "sustainable-resource-management-sec1",
        "title": "How Can We Sustainably Manage Natural Resources?",
        "title_zh": "我们如何可持续地管理自然资源？",
        "gradeLevel": "sec1",
        "description": "Understanding natural resources, sustainability principles, and management frameworks",
        "description_zh": "理解自然资源、可持续性原则和管理框架",
        "objectives": [
            "Define natural resources and classify them as renewable or non-renewable",
            "Explain the concept of sustainable development",
            "Understand the relationship between resource use and environmental impact",
            "Analyze factors affecting resource availability and demand",
            "Evaluate strategies for sustainable resource management"
        ],
        "objectives_zh": [
            "定义自然资源并将其分类为可再生或不可再生",
            "解释可持续发展的概念",
            "理解资源使用与环境影响之间的关系",
            "分析影响资源可用性和需求的因素",
            "评估可持续资源管理策略"
        ],
        "sections": [
            {
                "id": "what-are-natural-resources",
                "type": "text",
                "title": "What Are Natural Resources?",
                "title_zh": "什么是自然资源？",
                "content": "**Natural resources** are materials or substances found in nature that humans use to meet their needs and wants.\n\n**Types of Natural Resources:**\n\n**1. Renewable Resources**\n- Can be replenished naturally over time\n- Examples: Water (through hydrological cycle), forests (regrow), solar energy, wind energy\n- **Key point**: Renewable does NOT mean unlimited\n- Can be depleted if used faster than replenishment rate\n\n**2. Non-Renewable Resources**\n- Cannot be replaced once used (or take millions of years to form)\n- Examples: Fossil fuels (coal, oil, natural gas), minerals (iron, copper), precious metals (gold, silver)\n- **Limited supply**: Will eventually run out\n\n**Singapore Examples:**\n- **Renewable**: Rainwater (collected in reservoirs), solar energy (solar panels on HDB roofs)\n- **Non-renewable**: We import fossil fuels for energy, limited natural resources on our island\n- **Challenge**: Small land area + no natural resources = must manage carefully and import sustainably",
                "content_zh": "**自然资源**是在自然界中发现的材料或物质，人类用来满足他们的需求和欲望。\n\n**自然资源的类型：**\n\n**1. 可再生资源**\n- 可以随着时间自然补充\n- 示例：水（通过水文循环）、森林（再生）、太阳能、风能\n- **关键点**：可再生不意味着无限\n- 如果使用速度快于补充速度，可能会耗尽\n\n**2. 不可再生资源**\n- 一旦使用就无法替代（或需要数百万年才能形成）\n- 示例：化石燃料（煤、石油、天然气）、矿物（铁、铜）、贵金属（金、银）\n- **有限供应**：最终会耗尽\n\n**新加坡示例：**\n- **可再生**：雨水（在水库中收集）、太阳能（组屋屋顶的太阳能板）\n- **不可再生**：我们进口化石燃料用于能源，岛上自然资源有限\n- **挑战**：小土地面积 + 无自然资源 = 必须小心管理和可持续进口"
            },
            {
                "id": "what-is-sustainability",
                "type": "text",
                "title": "What Is Sustainable Development?",
                "title_zh": "什么是可持续发展？",
                "content": "**Sustainable development** means meeting the needs of the present without compromising the ability of future generations to meet their own needs.\n\n**The Three Pillars of Sustainability:**\n\n**1. Environmental Sustainability**\n- Protect ecosystems and biodiversity\n- Minimize pollution and waste\n- Conserve natural resources\n- Example: Protecting Singapore's nature reserves (Bukit Timah, Sungei Buloh)\n\n**2. Economic Sustainability**\n- Ensure economic growth and prosperity\n- Create jobs and livelihoods\n- Efficient resource use\n- Example: Singapore's green economy initiatives, eco-tourism\n\n**3. Social Sustainability**\n- Meet human needs (food, water, shelter, health)\n- Ensure equity and fairness\n- Quality of life for all\n- Example: Universal access to clean water in Singapore\n\n**Balance is Key**: All three pillars must work together. Economic growth cannot destroy the environment. Environmental protection cannot ignore people's needs.\n\n**Singapore's Sustainable Development Approach:**\n- **Vision**: City in a Garden, sustainable and livable\n- **Green Plan 2030**: Targets for sustainability\n- **Examples**:\n  - NEWater: Economic (reduce water imports) + Environmental (recycle wastewater) + Social (water security)\n  - Gardens by the Bay: Environmental (biodiversity) + Economic (tourism) + Social (recreation)\n  - Solar panels on HDB: Environmental (clean energy) + Economic (reduce costs) + Social (affordable electricity)",
                "content_zh": "**可持续发展**意味着满足当前需求而不损害后代满足自身需求的能力。\n\n**可持续性的三大支柱：**\n\n**1. 环境可持续性**\n- 保护生态系统和生物多样性\n- 最小化污染和废物\n- 保护自然资源\n- 示例：保护新加坡的自然保护区（武吉知马、双溪布洛）\n\n**2. 经济可持续性**\n- 确保经济增长和繁荣\n- 创造就业和生计\n- 高效利用资源\n- 示例：新加坡的绿色经济倡议、生态旅游\n\n**3. 社会可持续性**\n- 满足人类需求（食物、水、住所、健康）\n- 确保公平和公正\n- 所有人的生活质量\n- 示例：新加坡普遍获得清洁水\n\n**平衡是关键**：所有三个支柱必须共同作用。经济增长不能破坏环境。环境保护不能忽视人们的需求。\n\n**新加坡的可持续发展方法：**\n- **愿景**：花园城市，可持续和宜居\n- **绿色计划2030**：可持续性目标\n- **示例**：\n  - 新生水：经济（减少水进口）+ 环境（回收废水）+ 社会（水安全）\n  - 滨海湾花园：环境（生物多样性）+ 经济（旅游）+ 社会（休闲）\n  - 组屋太阳能板：环境（清洁能源）+ 经济（降低成本）+ 社会（负担得起的电力）"
            },
            {
                "id": "resource-management-principles",
                "type": "text",
                "title": "Principles of Sustainable Resource Management",
                "title_zh": "可持续资源管理原则",
                "content": "**Key Principles for Managing Resources Sustainably:**\n\n**1. Conservation**\n- Use resources efficiently and avoid waste\n- Reduce, Reuse, Recycle (3Rs)\n- Singapore example: Water conservation (10-liter challenge), waste reduction campaigns\n\n**2. Preservation**\n- Protect ecosystems and biodiversity\n- Set aside protected areas\n- Singapore example: Nature reserves (Bukit Timah, Central Catchment) - no development allowed\n\n**3. Substitution**\n- Replace non-renewable with renewable resources\n- Use alternative materials or technologies\n- Singapore example: Solar energy replacing fossil fuels, NEWater reducing imported water dependence\n\n**4. Restoration**\n- Repair damaged ecosystems\n- Reforestation and habitat rehabilitation\n- Singapore example: Mangrove restoration at Pulau Semakau, reforestation programs\n\n**5. Education and Awareness**\n- Teach people about sustainability\n- Change behaviors and attitudes\n- Singapore example: NEWater Visitor Centre, school environmental programs\n\n**6. Regulation and Policy**\n- Laws to protect resources and environment\n- Incentives for sustainable practices\n- Singapore example: Environmental Protection and Management Act, carbon tax, WELS (Water Efficiency Labelling Scheme)\n\n**7. Innovation and Technology**\n- Develop new solutions for resource challenges\n- Improve efficiency through technology\n- Singapore example: Smart water meters, vertical farming, desalination technology\n\n**Applying These Principles:**\n\nThese principles will be applied to specific resources in the following topics:\n- **Water resources**: Conservation (water-saving devices), Substitution (NEWater, desalination), Technology (membrane technology)\n- **Forests**: Preservation (protected reserves), Restoration (reforestation), Regulation (logging bans)\n- **Mangroves**: Preservation (Sungei Buloh), Restoration (replanting), Education (guided walks)",
                "content_zh": "**可持续管理资源的关键原则：**\n\n**1. 保护**\n- 高效使用资源并避免浪费\n- 减少、再利用、回收（3R）\n- 新加坡示例：节水（10升挑战）、减少废物活动\n\n**2. 保存**\n- 保护生态系统和生物多样性\n- 划出保护区\n- 新加坡示例：自然保护区（武吉知马、中央集水区）- 不允许开发\n\n**3. 替代**\n- 用可再生资源替代不可再生资源\n- 使用替代材料或技术\n- 新加坡示例：太阳能替代化石燃料、新生水减少进口水依赖\n\n**4. 恢复**\n- 修复受损生态系统\n- 重新造林和栖息地恢复\n- 新加坡示例：实马高岛红树林恢复、重新造林计划\n\n**5. 教育和意识**\n- 教育人们关于可持续性\n- 改变行为和态度\n- 新加坡示例：新生水访客中心、学校环境项目\n\n**6. 法规和政策**\n- 保护资源和环境的法律\n- 可持续实践的激励措施\n- 新加坡示例：环境保护和管理法、碳税、WELS（水效标签计划）\n\n**7. 创新和技术**\n- 为资源挑战开发新解决方案\n- 通过技术提高效率\n- 新加坡示例：智能水表、垂直农业、海水淡化技术\n\n**应用这些原则：**\n\n这些原则将应用于以下主题中的特定资源：\n- **水资源**：保护（节水设备）、替代（新生水、淡化）、技术（膜技术）\n- **森林**：保存（保护区）、恢复（重新造林）、法规（伐木禁令）\n- **红树林**：保存（双溪布洛）、恢复（重新种植）、教育（导览）"
            },
            {
                "id": "factors-affecting-resources",
                "type": "text",
                "title": "Factors Affecting Resource Use and Availability",
                "title_zh": "影响资源使用和可用性的因素",
                "content": "**Why do some places have more/less resources? Why is demand increasing?**\n\n**Factors Affecting Resource AVAILABILITY:**\n\n**1. Physical Geography**\n- Climate: Rainfall affects water availability\n- Location: Proximity to equator affects solar energy potential\n- Landforms: Flat land easier to develop than mountains\n- Soil: Fertile soil supports agriculture\n- Singapore: Small island, no rivers from other countries, limited natural resources\n\n**2. Technology**\n- Technology can access previously unavailable resources\n- Example: Desalination makes seawater usable, deep-sea drilling for oil\n- Singapore: Advanced technology enables NEWater production, land reclamation\n\n**3. Economics**\n- Cost of extraction and transportation\n- Example: Oil extraction expensive in deep water or Arctic\n- Singapore: Must import resources - economically viable due to trade infrastructure\n\n**Factors Affecting Resource DEMAND:**\n\n**1. Population Growth**\n- More people = more resources needed\n- Global population: 8 billion (2023), projected 10 billion (2050)\n- Singapore: 5.6 million people, increasing demand for water, energy, land\n\n**2. Economic Development**\n- Wealthier countries/people consume more resources\n- Industrialization increases energy and water demand\n- Example: Singapore's industries (semiconductors, refineries) use large amounts of water and energy\n\n**3. Lifestyle and Consumption**\n- Modern lifestyles increase resource use (cars, air conditioning, electronics)\n- Higher standards of living = more consumption\n- Singapore: High per capita consumption due to developed economy\n\n**4. Urbanization**\n- Cities concentrate people and activities\n- Urban areas have high resource demands\n- Singapore: 100% urban, intensive resource use in small area\n\n**Resource Challenges:**\n- **Increasing demand** + **Limited/decreasing supply** = **Resource stress**\n- Examples: Water scarcity in dry regions, deforestation for agriculture, fossil fuel depletion\n- **Solution**: Sustainable management to balance supply and demand",
                "content_zh": "**为什么有些地方拥有更多/更少的资源？为什么需求在增加？**\n\n**影响资源可用性的因素：**\n\n**1. 自然地理**\n- 气候：降雨影响水的可用性\n- 位置：靠近赤道影响太阳能潜力\n- 地形：平地比山地更容易开发\n- 土壤：肥沃土壤支持农业\n- 新加坡：小岛、无来自其他国家的河流、自然资源有限\n\n**2. 技术**\n- 技术可以获取以前无法获得的资源\n- 示例：海水淡化使海水可用、深海石油钻探\n- 新加坡：先进技术使新生水生产、填海造地成为可能\n\n**3. 经济**\n- 提取和运输成本\n- 示例：深水或北极的石油提取昂贵\n- 新加坡：必须进口资源 - 由于贸易基础设施而经济上可行\n\n**影响资源需求的因素：**\n\n**1. 人口增长**\n- 更多人 = 需要更多资源\n- 全球人口：80亿（2023），预计100亿（2050）\n- 新加坡：560万人，对水、能源、土地的需求增加\n\n**2. 经济发展**\n- 更富裕的国家/人民消耗更多资源\n- 工业化增加能源和水需求\n- 示例：新加坡的工业（半导体、炼油厂）使用大量水和能源\n\n**3. 生活方式和消费**\n- 现代生活方式增加资源使用（汽车、空调、电子产品）\n- 更高的生活水平 = 更多消费\n- 新加坡：由于发达经济而人均消费高\n\n**4. 城市化**\n- 城市集中人口和活动\n- 城市地区有高资源需求\n- 新加坡：100%城市、小面积内密集资源使用\n\n**资源挑战：**\n- **需求增加** + **供应有限/减少** = **资源压力**\n- 示例：干旱地区水资源短缺、农业森林砍伐、化石燃料耗尽\n- **解决方案**：可持续管理以平衡供需"
            }
        ],
        "exercises": []  # Will add exercises
    }

    return chapter

def create_sustainability_exercises():
    """Create 15 exercises for sustainability chapter (AO1 + AO2 + AO3)"""

    exercises = [
        # AO1: Knowledge (5)
        {"id":"ex1-renewable","type":"mcq","difficulty":"easy","prompt":"Which is a renewable resource?","prompt_zh":"哪一项是可再生资源？","choices":["Solar energy","Coal","Oil","Gold"],"choices_zh":["太阳能","煤","石油","金"],"answer":0,"explanation":"Renewable resources can be replenished: solar, wind, water, forests. Non-renewable: fossil fuels (coal, oil, gas), minerals, metals.","explanation_zh":"可再生资源可以补充：太阳能、风能、水、森林。不可再生：化石燃料（煤、石油、天然气）、矿物、金属。","hint":"Can it be replenished?","hint_zh":"它能被补充吗？"},

        {"id":"ex2-sustainability-pillars","type":"mcq","difficulty":"easy","prompt":"How many pillars of sustainability are there?","prompt_zh":"可持续性有多少个支柱？","choices":["Three","Two","Four","Five"],"choices_zh":["三个","两个","四个","五个"],"answer":0,"explanation":"Three pillars: 1)Environmental 2)Economic 3)Social. All must work together for true sustainability.","explanation_zh":"三个支柱：1)环境 2)经济 3)社会。所有支柱必须共同作用以实现真正的可持续性。","hint":"Remember: environment, economy, society.","hint_zh":"记住：环境、经济、社会。"},

        {"id":"ex3-3rs","type":"short","difficulty":"easy","prompt":"What do the 3Rs of sustainability stand for?","prompt_zh":"可持续性的3R代表什么？","answer":"Reduce, Reuse, Recycle","answer_zh":"减少、再利用、回收","explanation":"3Rs hierarchy: 1)Reduce (use less) - best option 2)Reuse (use again) 3)Recycle (process into new materials). Reduce is most effective.","explanation_zh":"3R层次：1)减少（使用更少）- 最佳选择 2)再利用（再次使用）3)回收（加工成新材料）。减少最有效。","hint":"R words for conservation.","hint_zh":"保护的R词。"},

        {"id":"ex4-sustainable-development","type":"short","difficulty":"medium","prompt":"Define sustainable development.","prompt_zh":"定义可持续发展。","answer":"Meeting present needs without compromising future generations' ability to meet their needs","answer_zh":"满足当前需求而不损害后代满足需求的能力","explanation":"Sustainable development balances present and future. Use resources responsibly today so they're available tomorrow. Example: Manage forests so they regrow for future use.","explanation_zh":"可持续发展平衡现在和未来。今天负责任地使用资源，以便明天可用。示例：管理森林使其重新生长以供未来使用。","hint":"Present vs future needs.","hint_zh":"现在vs未来需求。"},

        {"id":"ex5-population-demand","type":"mcq","difficulty":"medium","prompt":"Why does population growth increase resource demand?","prompt_zh":"为什么人口增长增加资源需求？","choices":["More people need more resources for food, water, energy, shelter","Population has no effect on resources","Technology solves all resource problems","Resources increase with population"],"choices_zh":["更多人需要更多资源用于食物、水、能源、住所","人口对资源没有影响","技术解决所有资源问题","资源随人口增加"],"answer":0,"explanation":"More people=more consumption. Each person needs food, water, energy, housing, etc. Global population: 8 billion→10 billion (2050) = 25% more demand.","explanation_zh":"更多人=更多消费。每个人需要食物、水、能源、住房等。全球人口：80亿→100亿（2050）= 需求增加25%。","hint":"More people consume...","hint_zh":"更多人消耗..."},

        # AO2: Understanding/Explanation (5)
        {"id":"ex6-renewable-limit","type":"short","difficulty":"medium","prompt":"Explain why renewable resources can still be depleted despite being renewable.","prompt_zh":"解释为什么可再生资源尽管可再生但仍可能被耗尽。","answer":"If used faster than natural replenishment rate","answer_zh":"如果使用速度快于自然补充速度","explanation":"Renewable≠unlimited. Example: Forests renew but if cut faster than regrowth→deforestation. Fish populations renew but overfishing→depletion. Rate matters!","explanation_zh":"可再生≠无限。示例：森林更新但如果砍伐快于重新生长→森林砍伐。鱼类种群更新但过度捕捞→耗尽。速度很重要！","hint":"Speed of use vs speed of renewal.","hint_zh":"使用速度vs更新速度。"},

        {"id":"ex7-three-pillars","type":"short","difficulty":"medium","prompt":"Explain why all three pillars of sustainability must work together.","prompt_zh":"解释为什么可持续性的三个支柱必须共同作用。","answer":"Balance needed - economic growth cannot destroy environment or ignore social needs","answer_zh":"需要平衡 - 经济增长不能破坏环境或忽视社会需求","explanation":"Cannot sacrifice one for another: Pure economic focus→environmental damage. Pure environmental focus→people suffer economically. Need balanced approach. Singapore NEWater example: economic (save money)+environmental (recycle)+social (water security).","explanation_zh":"不能为另一个牺牲一个：纯经济关注→环境破坏。纯环境关注→人们经济受苦。需要平衡方法。新加坡新生水示例：经济（省钱）+环境（回收）+社会（水安全）。","hint":"Trade-offs and balance.","hint_zh":"权衡和平衡。"},

        {"id":"ex8-substitution","type":"short","difficulty":"medium","prompt":"How does substitution help sustainable resource management?","prompt_zh":"替代如何帮助可持续资源管理？","answer":"Replace non-renewable with renewable resources to extend sustainability","answer_zh":"用可再生资源替代不可再生资源以延长可持续性","explanation":"Substitution: use alternatives. Examples: Solar→fossil fuels, bamboo→plastic, NEWater→imported water. Reduces dependence on limited non-renewables. Singapore heavily uses substitution due to lack of natural resources.","explanation_zh":"替代：使用替代品。示例：太阳能→化石燃料、竹子→塑料、新生水→进口水。减少对有限不可再生资源的依赖。新加坡由于缺乏自然资源而大量使用替代。","hint":"Alternative resources.","hint_zh":"替代资源。"},

        {"id":"ex9-urbanization","type":"short","difficulty":"hard","prompt":"Explain how urbanization increases resource demands.","prompt_zh":"解释城市化如何增加资源需求。","answer":"Concentration of people and activities in cities creates intensive resource consumption","answer_zh":"城市中人口和活动的集中创造了密集的资源消耗","explanation":"Cities concentrate: 1)People (high density) 2)Industries 3)Transport 4)Buildings. All need energy, water, materials. Urban infrastructure needs resources. Singapore: 100% urban, 5.6 million in 728km²=very intensive use.","explanation_zh":"城市集中：1)人（高密度）2)工业 3)交通 4)建筑。所有都需要能源、水、材料。城市基础设施需要资源。新加坡：100%城市，728km²中560万=非常密集使用。","hint":"Density and concentration.","hint_zh":"密度和集中。"},

        {"id":"ex10-singapore-challenge","type":"short","difficulty":"hard","prompt":"Why is sustainable resource management especially important for Singapore?","prompt_zh":"为什么可持续资源管理对新加坡特别重要？","answer":"Small land area and no natural resources mean must manage carefully and rely on imports","answer_zh":"小土地面积和无自然资源意味着必须小心管理并依赖进口","explanation":"Singapore challenges: 1)No natural resources 2)Small land (728km²) 3)High population density 4)Dependent on imports 5)Limited catchment for water. MUST be efficient, innovative, sustainable to survive. Examples: NEWater, vertical farming, solar, reclamation.","explanation_zh":"新加坡挑战：1)无自然资源 2)小土地（728km²）3)高人口密度 4)依赖进口 5)水的集水区有限。必须高效、创新、可持续才能生存。示例：新生水、垂直农业、太阳能、填海。","hint":"Constraints force innovation.","hint_zh":"限制促进创新。"},

        # AO3: Data Interpretation (5)
        {"id":"ex11-resource-classification","type":"mcq","difficulty":"medium","prompt":"Table shows: Water-renewable, Coal-non-renewable, Gold-non-renewable, Wind-renewable. Which pair is correctly classified?","prompt_zh":"表格显示：水-可再生，煤-不可再生，金-不可再生，风-可再生。哪对正确分类？","choices":["Water & Wind (renewable)","Coal & Water (non-renewable)","Gold & Wind (renewable)","All are non-renewable"],"choices_zh":["水和风（可再生）","煤和水（不可再生）","金和风（可再生）","所有都是不可再生"],"answer":0,"explanation":"Check each: Water renews (hydrological cycle)✓ Wind renews (continuous)✓ Coal takes millions of years✓ Gold limited supply✓. Water+Wind=renewable correct.","explanation_zh":"检查每个：水更新（水文循环）✓ 风更新（持续）✓ 煤需要数百万年✓ 金有限供应✓。水+风=可再生正确。","hint":"Which naturally replenish?","hint_zh":"哪些自然补充？"},

        {"id":"ex12-consumption-trend","type":"short","difficulty":"medium","prompt":"Graph shows Singapore's energy consumption doubled from 2000 to 2020. Suggest TWO reasons.","prompt_zh":"图表显示新加坡能源消耗从2000到2020翻倍。建议两个原因。","answer":"Population growth and economic development with more industries","answer_zh":"人口增长和更多工业的经济发展","explanation":"Rising energy use due to: 1)Population: 4M→5.6M (+40%) 2)Economic growth (more industries, data centers) 3)Higher living standards (more AC, cars, electronics) 4)Urbanization (100% urban=intensive use).","explanation_zh":"能源使用上升原因：1)人口：400万→560万（+40%）2)经济增长（更多工业、数据中心）3)更高生活水平（更多空调、汽车、电子产品）4)城市化（100%城市=密集使用）。","hint":"People and economy.","hint_zh":"人口和经济。"},

        {"id":"ex13-pillar-balance","type":"mcq","difficulty":"hard","prompt":"A country bans all logging to protect forests. Economy suffers, people lose jobs. Which pillar is neglected?","prompt_zh":"一个国家禁止所有伐木以保护森林。经济受损，人们失业。哪个支柱被忽视？","choices":["Economic & Social","Environmental","All three balanced","Only Economic"],"choices_zh":["经济和社会","环境","所有三个平衡","仅经济"],"answer":0,"explanation":"Logging ban: Environmental✓ protected. BUT Economic✗ (industry shut down) Social✗ (jobs lost, livelihoods gone). Need balance: selective logging allows jobs+forests. Pure environmental focus harms economy+society.","explanation_zh":"伐木禁令：环境✓保护。但经济✗（产业关闭）社会✗（失业、生计失去）。需要平衡：选择性伐木允许工作+森林。纯环境关注损害经济+社会。","hint":"Consider all three pillars.","hint_zh":"考虑所有三个支柱。"},

        {"id":"ex14-footprint-data","type":"short","difficulty":"hard","prompt":"Data: Singaporean uses 141L water/day, global average 170L. Despite lower use, why does Singapore face water stress?","prompt_zh":"数据：新加坡人每天使用141升水，全球平均170升。尽管使用较低，为什么新加坡面临水压力？","answer":"Small catchment area limits water collection despite high rainfall and efficiency","answer_zh":"小集水区限制水收集尽管降雨高和效率高","explanation":"Not just about consumption rate. Singapore water stress factors: 1)Tiny catchment (728km² land) 2)No rivers from neighbors 3)High density (5.6M people) 4)Must import 40% from Malaysia. Efficiency helps but geography constrains supply.","explanation_zh":"不仅仅是消费率。新加坡水压力因素：1)微小集水区（728km²土地）2)无来自邻国的河流 3)高密度（560万人）4)必须从马来西亚进口40%。效率有帮助但地理限制供应。","hint":"Supply constraint, not demand.","hint_zh":"供应限制，非需求。"},

        {"id":"ex15-strategy-evaluation","type":"short","difficulty":"hard","prompt":"Compare conservation vs substitution for managing non-renewable resources. Which is more effective long-term?","prompt_zh":"比较保护vs替代来管理不可再生资源。哪个长期更有效？","answer":"Substitution because eventually non-renewables will run out regardless of conservation","answer_zh":"替代因为无论如何保护不可再生资源最终都会耗尽","explanation":"Conservation: use less, extend lifespan. Good but TEMPORARY - non-renewables still finite. Substitution: replace with renewables. PERMANENT solution - shifts to unlimited source. Best approach: BOTH - conserve while transitioning to substitutes. Example: Save fossil fuels (conserve) WHILE developing solar (substitute).","explanation_zh":"保护：使用更少，延长寿命。好但暂时 - 不可再生仍然有限。替代：用可再生替代。永久解决方案 - 转向无限来源。最佳方法：两者 - 保护同时过渡到替代品。示例：节约化石燃料（保护）同时开发太阳能（替代）。","hint":"Long-term thinking.","hint_zh":"长期思考。"}
    ]

    return exercises

def main():
    print("=" * 70)
    print("ADDING MISSING SUSTAINABILITY CHAPTER")
    print("=" * 70)

    # Load current geography chapters
    print("\n[1/4] Loading current Geography chapters...")
    with open('chapters/geography-sec1-chapters.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"Current chapters: {len(data['chapters'])}")
    for i, ch in enumerate(data['chapters'], 1):
        print(f"  {i}. {ch['title']}")

    # Create sustainability chapter
    print("\n[2/4] Creating 'Sustainable Resource Management' chapter...")
    sustainability_chapter = create_sustainability_chapter()
    sustainability_exercises = create_sustainability_exercises()
    sustainability_chapter['exercises'] = sustainability_exercises

    print(f"✓ Created chapter with {len(sustainability_chapter['sections'])} sections")
    print(f"✓ Created {len(sustainability_exercises)} exercises")

    # Insert as Chapter 2 (after Introduction, before Water)
    print("\n[3/4] Inserting as Chapter 2 (before specific resources)...")
    data['chapters'].insert(1, sustainability_chapter)

    print("New chapter order:")
    for i, ch in enumerate(data['chapters'], 1):
        print(f"  {i}. {ch['title']} ({len(ch['exercises'])} exercises)")

    # Save updated file
    print("\n[4/4] Saving updated chapters...")
    with open('chapters/geography-sec1-chapters.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 70)
    print("✓ SUCCESS! Sustainability chapter added")
    print("=" * 70)

    total_exercises = sum(len(ch['exercises']) for ch in data['chapters'])
    print(f"\nTotal: {len(data['chapters'])} chapters, {total_exercises} exercises")
    print("\nNext: Re-integrate into main content.json with correct structure")

if __name__ == "__main__":
    main()
