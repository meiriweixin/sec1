#!/usr/bin/env python3
"""
Create comprehensive lesson content for Sec 3 Science chapters that currently have 0 sections.
Generates 3-4 sections per chapter with Singapore context, proper markdown, and bilingual content.
Aligned with Singapore MOE Sec 3 Science syllabus.
"""

import json
from datetime import datetime

# Lesson content for each chapter (3-4 sections each)
LESSON_CONTENT = {
    "atmosphere-environment": [
        {
            "id": "atmosphere-composition",
            "title": "Composition of the Atmosphere",
            "title_zh": "大气的组成",
            "type": "text",
            "content": """**The Earth's atmosphere** is a mixture of gases that surrounds our planet and makes life possible.

**Major gases in the atmosphere:**

1. **Nitrogen (N₂)** - 78% of air
2. **Oxygen (O₂)** - 21% of air
3. **Argon (Ar)** - 0.9% of air
4. **Carbon dioxide (CO₂)** - 0.04% of air (increasing due to human activities)
5. **Water vapor (H₂O)** - Variable (0-4%)

**Why is this composition important?**

🔹 **Nitrogen**: Dilutes oxygen, prevents rapid combustion
🔹 **Oxygen**: Essential for respiration and combustion
🔹 **Carbon dioxide**: Used by plants for photosynthesis, greenhouse gas
🔹 **Water vapor**: Drives weather patterns, greenhouse gas

**Singapore context:**

Singapore's air quality is monitored by NEA (National Environment Agency) using the PSI (Pollutant Standards Index). During haze periods, particulate matter from forest fires increases, affecting air composition and quality.""",
            "content_zh": """**地球大气层**是包围我们星球的气体混合物，使生命成为可能。

**大气中的主要气体：**

1. **氮气 (N₂)** - 占空气的78%
2. **氧气 (O₂)** - 占空气的21%
3. **氩气 (Ar)** - 占空气的0.9%
4. **二氧化碳 (CO₂)** - 占空气的0.04%（由于人类活动而增加）
5. **水蒸气 (H₂O)** - 可变（0-4%）

**这种组成为何重要？**

🔹 **氮气**：稀释氧气，防止快速燃烧
🔹 **氧气**：呼吸和燃烧所必需
🔹 **二氧化碳**：植物光合作用所用，温室气体
🔹 **水蒸气**：驱动天气模式，温室气体

**新加坡背景：**

新加坡的空气质量由NEA（国家环境局）使用PSI（污染物标准指数）监测。在烟霾期间，森林火灾产生的颗粒物增加，影响空气组成和质量。"""
        },
        {
            "id": "carbon-cycle",
            "title": "The Carbon Cycle",
            "title_zh": "碳循环",
            "type": "text",
            "content": """**The carbon cycle** describes how carbon atoms move between the atmosphere, living organisms, oceans, and Earth's crust.

**Key processes in the carbon cycle:**

1. **Photosynthesis** - Plants absorb CO₂ from air, convert to glucose
   - 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂

2. **Respiration** - Living organisms release CO₂ back to atmosphere
   - C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + energy

3. **Combustion** - Burning fossil fuels and biomass releases CO₂
   - Fuel + O₂ → CO₂ + H₂O + energy

4. **Decomposition** - Bacteria break down dead organisms, releasing CO₂

**Natural balance:**

🔹 Photosynthesis removes CO₂ from air
🔹 Respiration, combustion, decomposition add CO₂ to air
🔹 In nature, these processes are balanced

**Human impact in Singapore:**

🔹 **Deforestation**: Clearing Bukit Timah forest for development reduces CO₂ absorption
🔹 **Vehicles**: Cars on roads release CO₂ (Singapore has ~1 million vehicles)
🔹 **Industry**: Jurong Industrial Estate releases CO₂ from manufacturing
🔹 **Solutions**: Tree planting (1 million trees initiative), public transport (MRT expansion), green buildings""",
            "content_zh": """**碳循环**描述碳原子如何在大气、生物体、海洋和地壳之间移动。

**碳循环的关键过程：**

1. **光合作用** - 植物从空气中吸收CO₂，转化为葡萄糖
   - 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂

2. **呼吸作用** - 生物体将CO₂释放回大气
   - C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + 能量

3. **燃烧** - 燃烧化石燃料和生物质释放CO₂
   - 燃料 + O₂ → CO₂ + H₂O + 能量

4. **分解** - 细菌分解死亡生物体，释放CO₂

**自然平衡：**

🔹 光合作用从空气中去除CO₂
🔹 呼吸、燃烧、分解向空气中添加CO₂
🔹 在自然界中，这些过程是平衡的

**新加坡的人类影响：**

🔹 **森林砍伐**：为发展清除武吉知马森林减少CO₂吸收
🔹 **车辆**：道路上的汽车释放CO₂（新加坡有约100万辆车）
🔹 **工业**：裕廊工业区的制造业释放CO₂
🔹 **解决方案**：植树（100万棵树倡议）、公共交通（地铁扩展）、绿色建筑"""
        },
        {
            "id": "greenhouse-effect",
            "title": "Greenhouse Effect and Climate Change",
            "title_zh": "温室效应与气候变化",
            "type": "text",
            "content": """**The greenhouse effect** is a natural process where certain gases in the atmosphere trap heat from the Sun, warming Earth's surface.

**How it works:**

1. **Sunlight enters** atmosphere and warms Earth's surface
2. **Earth radiates** heat back as infrared radiation
3. **Greenhouse gases** (CO₂, CH₄, H₂O vapor) absorb and re-emit this heat
4. **Heat is trapped** near Earth's surface, warming the planet

**Natural vs. Enhanced greenhouse effect:**

🔹 **Natural**: Keeps Earth at habitable temperature (~15°C average)
🔹 **Enhanced**: Human activities increase greenhouse gas concentrations, causing global warming

**Main greenhouse gases:**

1. **Carbon dioxide (CO₂)** - from burning fossil fuels, deforestation
2. **Methane (CH₄)** - from livestock, rice paddies, landfills
3. **Water vapor (H₂O)** - from evaporation (increases as temperature rises)
4. **Nitrous oxide (N₂O)** - from agriculture, industrial processes

**Climate change impacts on Singapore:**

⚠️ **Rising sea levels**: Low-lying areas (Changi, Tuas) at risk of flooding
⚠️ **Higher temperatures**: Already averaging 27-28°C, projected to increase by 1.4-4.6°C by 2100
⚠️ **More intense rainfall**: Flash floods becoming more frequent
⚠️ **Heat island effect**: Urban areas 2-3°C warmer than surroundings

**Singapore's response:**

✅ **Coastal protection**: Building sea walls, raising land levels
✅ **Green buildings**: Energy-efficient designs reduce emissions
✅ **Public transport**: Expanding MRT to reduce car use
✅ **Solar energy**: SolarNova program installs panels on HDB rooftops
✅ **Tree planting**: 1 million trees initiative increases CO₂ absorption""",
            "content_zh": """**温室效应**是大气中某些气体捕获来自太阳的热量，使地球表面变暖的自然过程。

**它是如何工作的：**

1. **阳光进入**大气层并加热地球表面
2. **地球辐射**热量作为红外辐射返回
3. **温室气体**（CO₂、CH₄、H₂O蒸气）吸收并重新发射这种热量
4. **热量被困**在地球表面附近，使地球变暖

**自然温室效应与增强温室效应：**

🔹 **自然**：将地球保持在适宜居住的温度（平均约15°C）
🔹 **增强**：人类活动增加温室气体浓度，导致全球变暖

**主要温室气体：**

1. **二氧化碳 (CO₂)** - 来自燃烧化石燃料、森林砍伐
2. **甲烷 (CH₄)** - 来自牲畜、稻田、垃圾填埋场
3. **水蒸气 (H₂O)** - 来自蒸发（随温度升高而增加）
4. **一氧化二氮 (N₂O)** - 来自农业、工业过程

**气候变化对新加坡的影响：**

⚠️ **海平面上升**：低洼地区（樟宜、大士）面临洪水风险
⚠️ **温度升高**：目前平均27-28°C，预计到2100年将增加1.4-4.6°C
⚠️ **降雨更强烈**：暴洪变得更加频繁
⚠️ **热岛效应**：城市地区比周围地区温暖2-3°C

**新加坡的应对：**

✅ **海岸保护**：建造海堤，提高土地水平
✅ **绿色建筑**：节能设计减少排放
✅ **公共交通**：扩展地铁以减少汽车使用
✅ **太阳能**：太阳能计划在组屋屋顶安装太阳能板
✅ **植树**：100万棵树倡议增加CO₂吸收"""
        }
    ],

    "biotechnology": [
        {
            "id": "what-is-biotechnology",
            "title": "What is Biotechnology?",
            "title_zh": "什么是生物技术？",
            "type": "text",
            "content": """**Biotechnology** is the use of living organisms, cells, or biological processes to develop products and technologies that improve our lives.

**Key principles:**

🔹 Uses **biological systems** (bacteria, yeast, plants, animals)
🔹 Applies **scientific knowledge** (genetics, biochemistry, molecular biology)
🔹 Creates **useful products** (medicines, food, materials)

**Types of biotechnology:**

1. **Medical biotechnology** - Developing medicines, vaccines, diagnostic tests
2. **Agricultural biotechnology** - Improving crops, pest resistance, yield
3. **Industrial biotechnology** - Producing enzymes, biofuels, biodegradable plastics
4. **Environmental biotechnology** - Cleaning up pollution, waste treatment

**Examples in daily life:**

🔹 **Bread making**: Yeast ferments sugars to produce CO₂ (makes bread rise)
🔹 **Yogurt production**: Bacteria ferment milk lactose to lactic acid
🔹 **Antibiotics**: Penicillin produced by Penicillium mold
🔹 **Insulin**: Genetically modified bacteria produce human insulin for diabetics

**Biotechnology in Singapore:**

Singapore is a biomedical sciences hub in Asia:

🔹 **Biopolis**: Research complex in Buona Vista for biotech companies
🔹 **A*STAR**: Agency for Science, Technology and Research
🔹 **Vaccine production**: Companies like Sanofi produce vaccines locally
🔹 **Stem cell research**: National University Hospital conducts stem cell therapy research""",
            "content_zh": """**生物技术**是使用生物体、细胞或生物过程来开发改善我们生活的产品和技术。

**关键原则：**

🔹 使用**生物系统**（细菌、酵母、植物、动物）
🔹 应用**科学知识**（遗传学、生物化学、分子生物学）
🔹 创造**有用的产品**（药物、食品、材料）

**生物技术的类型：**

1. **医学生物技术** - 开发药物、疫苗、诊断测试
2. **农业生物技术** - 改良作物、抗虫性、产量
3. **工业生物技术** - 生产酶、生物燃料、可生物降解塑料
4. **环境生物技术** - 清理污染、废物处理

**日常生活中的例子：**

🔹 **面包制作**：酵母发酵糖产生CO₂（使面包膨胀）
🔹 **酸奶生产**：细菌发酵牛奶乳糖成乳酸
🔹 **抗生素**：青霉素由青霉菌产生
🔹 **胰岛素**：基因改造细菌产生人类胰岛素供糖尿病患者使用

**新加坡的生物技术：**

新加坡是亚洲生物医学科学中心：

🔹 **启奥城**：武吉知马生物技术公司研究综合体
🔹 **A*STAR**：科学、技术和研究机构
🔹 **疫苗生产**：赛诺菲等公司在本地生产疫苗
🔹 **干细胞研究**：国立大学医院进行干细胞治疗研究"""
        },
        {
            "id": "fermentation",
            "title": "Fermentation and Its Applications",
            "title_zh": "发酵及其应用",
            "type": "text",
            "content": """**Fermentation** is a biological process where microorganisms (bacteria, yeast, mold) break down organic substances in the absence of oxygen.

**Types of fermentation:**

1. **Alcoholic fermentation** (by yeast)
   - Glucose → Ethanol + Carbon dioxide
   - C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂

2. **Lactic acid fermentation** (by bacteria)
   - Glucose → Lactic acid
   - C₆H₁₂O₆ → 2C₃H₆O₃

**Conditions needed for fermentation:**

🔹 **Microorganisms**: Yeast or bacteria
🔹 **Food source**: Sugar (glucose, sucrose)
🔹 **Anaerobic conditions**: Little or no oxygen
🔹 **Warm temperature**: 25-40°C optimal
🔹 **pH control**: Different microorganisms prefer different pH levels

**Commercial applications:**

**Food and beverage:**
🔹 **Bread**: Yeast ferments sugar, CO₂ makes dough rise
🔹 **Beer/wine**: Yeast ferments sugars in grains/grapes to alcohol
🔹 **Yogurt**: Bacteria ferment milk lactose to lactic acid (gives tangy taste)
🔹 **Soy sauce**: Mold and bacteria ferment soybeans
🔹 **Kimchi/sauerkraut**: Lactic acid bacteria preserve vegetables

**Industrial products:**
🔹 **Antibiotics**: Penicillin from Penicillium mold
🔹 **Insulin**: Genetically modified bacteria produce human insulin
🔹 **Bioethanol**: Yeast ferments plant sugars to produce biofuel
🔹 **Enzymes**: Used in detergents, food processing

**Singapore food culture:**

Many traditional Asian foods use fermentation:
🔹 **Tempeh**: Fermented soybean cake (popular in Indonesian cuisine)
🔹 **Fermented beancurd** (腐乳): Used in Chinese cooking
🔹 **Kefir**: Fermented milk drink gaining popularity
🔹 **Kombucha**: Fermented tea beverage sold in cafes""",
            "content_zh": """**发酵**是微生物（细菌、酵母、霉菌）在无氧条件下分解有机物质的生物过程。

**发酵的类型：**

1. **酒精发酵**（由酵母进行）
   - 葡萄糖 → 乙醇 + 二氧化碳
   - C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂

2. **乳酸发酵**（由细菌进行）
   - 葡萄糖 → 乳酸
   - C₆H₁₂O₆ → 2C₃H₆O₃

**发酵所需的条件：**

🔹 **微生物**：酵母或细菌
🔹 **食物来源**：糖（葡萄糖、蔗糖）
🔹 **厌氧条件**：很少或没有氧气
🔹 **温暖温度**：25-40°C最佳
🔹 **pH控制**：不同微生物偏好不同的pH水平

**商业应用：**

**食品和饮料：**
🔹 **面包**：酵母发酵糖，CO₂使面团膨胀
🔹 **啤酒/葡萄酒**：酵母发酵谷物/葡萄中的糖成酒精
🔹 **酸奶**：细菌发酵牛奶乳糖成乳酸（产生酸味）
🔹 **酱油**：霉菌和细菌发酵大豆
🔹 **泡菜/酸菜**：乳酸菌保存蔬菜

**工业产品：**
🔹 **抗生素**：来自青霉菌的青霉素
🔹 **胰岛素**：基因改造细菌产生人类胰岛素
🔹 **生物乙醇**：酵母发酵植物糖产生生物燃料
🔹 **酶**：用于洗涤剂、食品加工

**新加坡饮食文化：**

许多传统亚洲食品使用发酵：
🔹 **天贝**：发酵大豆饼（印尼料理中很受欢迎）
🔹 **腐乳**：用于中国烹饪
🔹 **开菲尔**：发酵牛奶饮料越来越受欢迎
🔹 **康普茶**：咖啡馆出售的发酵茶饮料"""
        },
        {
            "id": "genetic-engineering",
            "title": "Genetic Engineering and GMOs",
            "title_zh": "基因工程与转基因生物",
            "type": "text",
            "content": """**Genetic engineering** is the process of deliberately modifying an organism's DNA to give it new characteristics.

**How genetic engineering works:**

1. **Identify** the desired gene (e.g., insulin gene in humans)
2. **Extract** the gene using restriction enzymes (molecular scissors)
3. **Insert** the gene into a vector (usually a bacterial plasmid)
4. **Transfer** the vector into target organism (bacteria, plant, animal)
5. **Select** successfully modified organisms
6. **Grow** genetically modified organisms (GMOs)

**Applications of genetic engineering:**

**Medicine:**
🔹 **Insulin production**: Bacteria with human insulin gene produce insulin for diabetics
🔹 **Vaccines**: Genetically modified viruses create safer vaccines
🔹 **Gene therapy**: Treating genetic diseases by replacing faulty genes

**Agriculture:**
🔹 **Pest-resistant crops**: Bt corn has gene from bacteria that kills insect pests
🔹 **Herbicide-resistant crops**: Plants survive weed-killer spraying
🔹 **Golden Rice**: Contains vitamin A to prevent blindness in developing countries
🔹 **Longer shelf life**: Tomatoes engineered to ripen more slowly

**Benefits:**

✅ Increased crop yields
✅ Reduced pesticide use
✅ Better nutrition (fortified crops)
✅ Cheaper medicines (mass-produced insulin)
✅ Disease resistance in plants and animals

**Concerns:**

⚠️ Unknown long-term health effects
⚠️ Environmental impact on ecosystems
⚠️ Cross-contamination with non-GMO crops
⚠️ Ethical concerns about "playing God"
⚠️ Corporate control of food supply

**GMOs in Singapore:**

🔹 **Research**: A*STAR conducts GM crop research
🔹 **Food imports**: Many processed foods contain GMO ingredients (soy, corn)
🔹 **Labeling**: No mandatory GMO labeling requirement
🔹 **Safety**: Agri-Food & Veterinary Authority (AVA) evaluates GM food safety""",
            "content_zh": """**基因工程**是故意修改生物体DNA以赋予其新特性的过程。

**基因工程如何工作：**

1. **识别**所需基因（例如，人类中的胰岛素基因）
2. **提取**使用限制酶的基因（分子剪刀）
3. **插入**基因到载体中（通常是细菌质粒）
4. **转移**载体到目标生物体（细菌、植物、动物）
5. **选择**成功修改的生物体
6. **培养**转基因生物（GMO）

**基因工程的应用：**

**医学：**
🔹 **胰岛素生产**：带有人类胰岛素基因的细菌为糖尿病患者产生胰岛素
🔹 **疫苗**：基因改造病毒创造更安全的疫苗
🔹 **基因治疗**：通过替换有缺陷的基因治疗遗传疾病

**农业：**
🔹 **抗虫作物**：Bt玉米具有来自细菌的基因，可杀死昆虫害虫
🔹 **抗除草剂作物**：植物在除草剂喷洒后存活
🔹 **黄金大米**：含有维生素A以防止发展中国家失明
🔹 **更长的保质期**：番茄被改造成更慢成熟

**好处：**

✅ 增加作物产量
✅ 减少农药使用
✅ 更好的营养（强化作物）
✅ 更便宜的药物（大规模生产的胰岛素）
✅ 植物和动物的抗病性

**担忧：**

⚠️ 未知的长期健康影响
⚠️ 对生态系统的环境影响
⚠️ 与非转基因作物的交叉污染
⚠️ 关于"扮演上帝"的伦理担忧
⚠️ 食品供应的企业控制

**新加坡的转基因生物：**

🔹 **研究**：A*STAR进行转基因作物研究
🔹 **食品进口**：许多加工食品含有转基因成分（大豆、玉米）
🔹 **标签**：没有强制性的转基因标签要求
🔹 **安全**：农粮兽医局（AVA）评估转基因食品安全性"""
        }
    ],

    "ecology-human-impact": [
        {
            "id": "ecosystems-biodiversity",
            "title": "Ecosystems and Biodiversity",
            "title_zh": "生态系统与生物多样性",
            "type": "text",
            "content": """**An ecosystem** is a community of living organisms interacting with each other and their non-living environment.

**Components of an ecosystem:**

**Biotic factors** (living):
🔹 **Producers**: Plants, algae (make food via photosynthesis)
🔹 **Consumers**: Animals that eat other organisms
🔹 **Decomposers**: Bacteria, fungi (break down dead organisms)

**Abiotic factors** (non-living):
🔹 Light intensity, temperature, water, pH, oxygen, minerals

**Biodiversity** = variety of living organisms in an ecosystem

**Three levels of biodiversity:**

1. **Genetic diversity**: Variation within a species
2. **Species diversity**: Number of different species in an area
3. **Ecosystem diversity**: Variety of habitats in a region

**Why is biodiversity important?**

✅ **Food security**: Many crops depend on wild relatives for genetic diversity
✅ **Medicine**: Many drugs derived from plants and animals
✅ **Ecosystem services**: Pollination, water purification, climate regulation
✅ **Economic value**: Tourism, recreation, materials
✅ **Intrinsic value**: All species have right to exist

**Singapore's biodiversity:**

Despite being a small island city-state, Singapore has rich biodiversity:

🔹 **Bukit Timah Nature Reserve**: Primary rainforest with over 840 plant species
🔹 **Sungei Buloh Wetland Reserve**: Mangroves, migratory birds (150+ species)
🔹 **Sisters' Islands Marine Park**: Coral reefs with 250+ coral species
🔹 **MacRitchie Reservoir**: Freshwater ecosystem with otters, monitor lizards
🔹 **Pulau Ubin**: Rural island with diverse habitats (forests, mangroves, coastal areas)

**Singapore Biodiversity Index**: Tracks changes in native species populations over time to guide conservation efforts.""",
            "content_zh": """**生态系统**是生物群落与彼此及其非生物环境相互作用的系统。

**生态系统的组成部分：**

**生物因素**（有生命的）：
🔹 **生产者**：植物、藻类（通过光合作用制造食物）
🔹 **消费者**：吃其他生物的动物
🔹 **分解者**：细菌、真菌（分解死亡生物体）

**非生物因素**（无生命的）：
🔹 光照强度、温度、水、pH、氧气、矿物质

**生物多样性** = 生态系统中生物体的多样性

**生物多样性的三个层次：**

1. **遗传多样性**：物种内的变异
2. **物种多样性**：一个地区不同物种的数量
3. **生态系统多样性**：一个地区栖息地的多样性

**为什么生物多样性重要？**

✅ **食品安全**：许多作物依赖野生亲缘物种获得遗传多样性
✅ **医学**：许多药物来源于植物和动物
✅ **生态系统服务**：授粉、水净化、气候调节
✅ **经济价值**：旅游、娱乐、材料
✅ **内在价值**：所有物种都有生存的权利

**新加坡的生物多样性：**

尽管是一个小岛城市国家，新加坡拥有丰富的生物多样性：

🔹 **武吉知马自然保护区**：拥有840多种植物的原始雨林
🔹 **双溪布洛湿地保护区**：红树林、候鸟（150+种）
🔹 **姐妹岛海洋公园**：拥有250+种珊瑚的珊瑚礁
🔹 **麦里芝蓄水池**：淡水生态系统，有水獭、巨蜥
🔹 **乌敏岛**：具有多样栖息地的乡村岛屿（森林、红树林、沿海地区）

**新加坡生物多样性指数**：跟踪本地物种种群随时间的变化，以指导保护工作。"""
        },
        {
            "id": "human-activities-impact",
            "title": "Human Impact on the Environment",
            "title_zh": "人类对环境的影响",
            "type": "text",
            "content": """**Human activities** significantly impact ecosystems and biodiversity worldwide.

**Major threats to ecosystems:**

**1. Habitat destruction**
- **Deforestation**: Clearing forests for agriculture, urban development
- **Urbanization**: Building cities destroys natural habitats
- **Impact**: Species lose homes, food sources, breeding grounds

**2. Pollution**
- **Air pollution**: Smog, acid rain damage plants and animals
- **Water pollution**: Industrial waste, sewage harm aquatic life
- **Soil pollution**: Pesticides, heavy metals contaminate food chains
- **Plastic pollution**: Marine animals ingest or get entangled in plastic

**3. Overexploitation**
- **Overfishing**: Fish populations decline, ecosystem imbalance
- **Illegal wildlife trade**: Poaching threatens endangered species
- **Overharvesting**: Unsustainable logging, hunting

**4. Climate change**
- **Rising temperatures**: Coral bleaching, species migration
- **Sea level rise**: Coastal habitat loss
- **Extreme weather**: Droughts, floods destroy ecosystems

**5. Invasive species**
- **Non-native species**: Outcompete native species for resources
- **No natural predators**: Populations grow unchecked

**Singapore-specific impacts:**

**Challenges:**
🔹 **Land scarcity**: Only 700 km², high population density (8,000/km²)
🔹 **Habitat loss**: 95% of original forests cleared since 1800s
🔹 **Reclaimed land**: 25% of Singapore is reclaimed from sea (affects marine life)
🔹 **Urban heat island**: City 2-3°C warmer than surrounding areas
🔹 **Water pollution**: Marina Bay was heavily polluted until cleanup efforts
🔹 **Air pollution**: Haze from Indonesian forest fires (PSI reaches unhealthy levels)

**Conservation efforts:**
✅ **Nature reserves**: Bukit Timah, Central Catchment protected areas
✅ **Park connector network**: 300+ km of green corridors link habitats
✅ **Tree planting**: 1 million trees initiative (2020-2030)
✅ **Marine protected areas**: Sisters' Islands Marine Park
✅ **NEWater**: Water recycling reduces reliance on imports
✅ **Green buildings**: Mandatory eco-friendly features for new buildings""",
            "content_zh": """**人类活动**对全球生态系统和生物多样性产生重大影响。

**生态系统的主要威胁：**

**1. 栖息地破坏**
- **森林砍伐**：为农业、城市发展清理森林
- **城市化**：建设城市破坏自然栖息地
- **影响**：物种失去家园、食物来源、繁殖地

**2. 污染**
- **空气污染**：烟雾、酸雨损害植物和动物
- **水污染**：工业废物、污水损害水生生物
- **土壤污染**：农药、重金属污染食物链
- **塑料污染**：海洋动物摄入或被塑料缠住

**3. 过度开发**
- **过度捕捞**：鱼类种群下降，生态系统失衡
- **非法野生动物贸易**：偷猎威胁濒危物种
- **过度采伐**：不可持续的伐木、狩猎

**4. 气候变化**
- **温度上升**：珊瑚白化、物种迁移
- **海平面上升**：沿海栖息地丧失
- **极端天气**：干旱、洪水破坏生态系统

**5. 入侵物种**
- **非本地物种**：与本地物种争夺资源
- **没有天敌**：种群不受控制地增长

**新加坡特定影响：**

**挑战：**
🔹 **土地稀缺**：仅700平方公里，人口密度高（8,000/km²）
🔹 **栖息地丧失**：自1800年代以来清除了95%的原始森林
🔹 **填海造地**：25%的新加坡是从海洋填海而来（影响海洋生物）
🔹 **城市热岛**：城市比周围地区温暖2-3°C
🔹 **水污染**：滨海湾在清理工作之前受到严重污染
🔹 **空气污染**：印尼森林火灾的烟霾（PSI达到不健康水平）

**保护工作：**
✅ **自然保护区**：武吉知马、中央集水区保护区
✅ **公园连道网络**：300+公里的绿色走廊连接栖息地
✅ **植树**：100万棵树倡议（2020-2030）
✅ **海洋保护区**：姐妹岛海洋公园
✅ **新生水**：水循环减少对进口的依赖
✅ **绿色建筑**：新建筑必须具有环保功能"""
        },
        {
            "id": "conservation-sustainability",
            "title": "Conservation and Sustainable Living",
            "title_zh": "保护与可持续生活",
            "type": "text",
            "content": """**Conservation** is the protection and management of natural resources and ecosystems to ensure their survival for future generations.

**Conservation strategies:**

**1. Protected areas**
- **Nature reserves**: Legal protection of critical habitats
- **Marine parks**: Protect coral reefs and marine biodiversity
- **Wildlife sanctuaries**: Safe havens for endangered species

**2. Species protection**
- **Captive breeding**: Breed endangered animals in zoos, reintroduce to wild
- **Seed banks**: Store seeds of rare plants for future restoration
- **Anti-poaching laws**: Penalties for illegal hunting/trade

**3. Habitat restoration**
- **Reforestation**: Planting trees to restore forests
- **Wetland restoration**: Recreating mangroves, marshes
- **Coral reef restoration**: Transplanting coral fragments

**4. Sustainable resource use**
- **Sustainable forestry**: Harvest wood at rate forests can regrow
- **Sustainable fishing**: Catch limits, seasonal bans to prevent depletion
- **Renewable energy**: Solar, wind, hydroelectric power

**Sustainable living practices:**

**Reduce, Reuse, Recycle:**
🔹 **Reduce**: Use less, avoid single-use plastics
🔹 **Reuse**: Bring own bags, bottles, containers
🔹 **Recycle**: Sort waste into blue recycling bins

**Energy conservation:**
🔹 Switch off lights and aircon when not in use
🔹 Use LED bulbs (75% less energy than incandescent)
🔹 Take public transport, walk, or cycle

**Water conservation:**
🔹 Take shorter showers (use bucket to save water)
🔹 Fix leaky taps immediately
🔹 Use NEWater for non-drinking purposes

**Sustainable food choices:**
🔹 Buy local produce (reduce transport emissions)
🔹 Eat less meat (livestock farming = high carbon footprint)
🔹 Don't waste food (Singapore wastes 744 million kg food/year)

**Singapore's sustainability initiatives:**

**Singapore Green Plan 2030:**
✅ **City in Nature**: Add 200 hectares of parks by 2030
✅ **Energy Reset**: Install 2 GW of solar power by 2030
✅ **Sustainable Living**: 80% of households within 10 min walk of park
✅ **Green Economy**: Create green jobs, sustainable industries
✅ **Resilient Future**: Coastal protection, climate adaptation

**Zero Waste Nation:**
✅ **Waste-to-energy plants**: 4 incineration plants convert trash to electricity
✅ **Pulau Semakau**: Offshore landfill receives incineration ash
✅ **70% recycling rate goal** by 2030

**Individual actions matter:**
Every Singaporean can contribute to conservation through daily choices. Small changes like using reusable bags, saving water, and recycling properly add up to big environmental impact when millions of people participate.""",
            "content_zh": """**保护**是对自然资源和生态系统的保护和管理，以确保它们为后代生存。

**保护策略：**

**1. 保护区**
- **自然保护区**：对关键栖息地的法律保护
- **海洋公园**：保护珊瑚礁和海洋生物多样性
- **野生动物保护区**：濒危物种的安全避风港

**2. 物种保护**
- **圈养繁殖**：在动物园繁殖濒危动物，重新引入野外
- **种子库**：储存稀有植物的种子以供未来恢复
- **反偷猎法**：非法狩猎/贸易的惩罚

**3. 栖息地恢复**
- **重新造林**：种植树木以恢复森林
- **湿地恢复**：重建红树林、沼泽
- **珊瑚礁恢复**：移植珊瑚碎片

**4. 可持续资源利用**
- **可持续林业**：以森林可再生的速度采伐木材
- **可持续捕鱼**：捕捞限制、季节性禁令以防止枯竭
- **可再生能源**：太阳能、风能、水力发电

**可持续生活实践：**

**减少、重复使用、回收：**
🔹 **减少**：少用，避免一次性塑料
🔹 **重复使用**：自带袋子、瓶子、容器
🔹 **回收**：将废物分类到蓝色回收箱

**节能：**
🔹 不使用时关闭灯和空调
🔹 使用LED灯泡（比白炽灯少75%能量）
🔹 乘坐公共交通、步行或骑自行车

**节水：**
🔹 缩短淋浴时间（使用水桶节水）
🔹 立即修复漏水的水龙头
🔹 将新生水用于非饮用目的

**可持续食品选择：**
🔹 购买本地产品（减少运输排放）
🔹 少吃肉（畜牧业=高碳足迹）
🔹 不要浪费食物（新加坡每年浪费7.44亿公斤食物）

**新加坡的可持续发展倡议：**

**新加坡绿色计划2030：**
✅ **自然之城**：到2030年增加200公顷公园
✅ **能源重置**：到2030年安装2GW太阳能
✅ **可持续生活**：80%的家庭步行10分钟内到达公园
✅ **绿色经济**：创造绿色工作、可持续产业
✅ **韧性未来**：海岸保护、气候适应

**零废物国家：**
✅ **垃圾焚化厂**：4个焚化厂将垃圾转化为电力
✅ **实马高岛**：离岸垃圾填埋场接收焚化灰烬
✅ **70%回收率目标**到2030年

**个人行动很重要：**
每个新加坡人都可以通过日常选择为保护做出贡献。当数百万人参与时，使用可重复使用的袋子、节水和正确回收等小改变会产生巨大的环境影响。"""
        }
    ]
}

# Continue with remaining chapters in next part...
# (Due to length, this shows the pattern. I'll create the complete content for all 11 chapters)

def main():
    content_file = "src/data/content.json"
    backup_file = f"src/data/content-backup-sec3-lessons-{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    print("="*70)
    print("CREATING SEC 3 SCIENCE LESSON CONTENT")
    print("="*70)

    # Read content
    print("\nReading content.json...")
    with open(content_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Backup
    print(f"Creating backup: {backup_file}")
    with open(backup_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Find science subject
    science = next(s for s in data['subjects'] if s['id'] == 'science')

    chapters_updated = 0
    sections_added = 0

    for chapter in science['chapters']:
        chapter_id = chapter['id']

        if chapter_id in LESSON_CONTENT:
            # Add sections to this chapter
            new_sections = LESSON_CONTENT[chapter_id]
            chapter['sections'] = new_sections
            chapters_updated += 1
            sections_added += len(new_sections)
            print(f"✓ Added {len(new_sections)} sections to: {chapter['title']}")

    # Save
    print(f"\nSaving updated content...")
    with open(content_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("\n" + "="*70)
    print("✅ LESSON CONTENT CREATION COMPLETE")
    print("="*70)
    print(f"Chapters updated: {chapters_updated}")
    print(f"Sections added: {sections_added}")
    print(f"\nBackup saved: {backup_file}")
    print("\nNote: This script covers first 3 chapters. Run complete version for all 11.")

if __name__ == '__main__':
    main()
