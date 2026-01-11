#!/usr/bin/env python3
"""
Generate exercises for remaining History Sec 1 chapters
- Chapter 2: British Establishment of a Trading Post (15 exercises)
- Chapter 3: Singapore's Growth as a Port City (15 exercises)
- Chapter 4: Communities in Colonial Singapore (15 exercises)
- Chapter 5: Industries and Fall of Singapore (15 exercises)

Total: 60 new exercises
"""

import json
from datetime import datetime

# Load chapters
with open('chapters/history-sec1-chapters.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Exercise templates for each chapter
exercises_by_chapter = {
    "british-establishment-trading-post": {
        "ao1": [  # Knowledge - Identify and Describe
            {
                "id": "ex1-raffles-arrival",
                "type": "mcq",
                "difficulty": "easy",
                "prompt": "In which year did Stamford Raffles arrive in Singapore?",
                "prompt_zh": "斯坦福·莱佛士在哪一年到达新加坡？",
                "choices": ["1819", "1824", "1826", "1832"],
                "choices_zh": ["1819年", "1824年", "1826年", "1832年"],
                "answer": 0,
                "explanation": "**Answer: 1819**\n\nSir Stamford Raffles arrived in Singapore on **29 January 1819**. This date marks the founding of modern Singapore as a British trading post.\n\n**Why this date is significant:**\n- Marked the beginning of British colonial rule\n- Transformed Singapore from a small Malay fishing village into a major port\n- Changed Singapore's trajectory forever\n\n**Why the other dates are incorrect:**\n- **1824**: Year of the Anglo-Dutch Treaty (divided Malay Archipelago between Britain and Netherlands)\n- **1826**: Singapore became part of the Straits Settlements (with Penang and Malacca)\n- **1832**: Singapore became the capital of the Straits Settlements",
                "explanation_zh": "**答案：1819年**\n\n斯坦福·莱佛士爵士于**1819年1月29日**抵达新加坡。这个日期标志着现代新加坡作为英国贸易站的建立。\n\n**为什么这个日期很重要：**\n- 标志着英国殖民统治的开始\n- 将新加坡从一个马来渔村转变为主要港口\n- 永远改变了新加坡的轨迹\n\n**为什么其他日期不正确：**\n- **1824年**：英荷条约年（将马来群岛划分给英国和荷兰）\n- **1826年**：新加坡成为海峡殖民地的一部分（与槟城和马六甲）\n- **1832年**：新加坡成为海峡殖民地的首都"
            },
            {
                "id": "ex2-treaty-signers",
                "type": "mcq",
                "difficulty": "medium",
                "prompt": "Who were the TWO Malay leaders that signed the treaty with Raffles in 1819?",
                "prompt_zh": "1819年与莱佛士签署条约的两位马来领导人是谁？",
                "choices": [
                    "Temenggong Abdul Rahman and Sultan Hussein Shah",
                    "Sultan Mahmud Shah and Temenggong Abdul Rahman",
                    "Sultan Hussein Shah and Sultan Abdul Rahman",
                    "Raja Ali and Temenggong Hussein"
                ],
                "choices_zh": [
                    "天猛公阿都拉曼和苏丹胡先",
                    "苏丹马哈茂德和天猛公阿都拉曼",
                    "苏丹胡先和苏丹阿都拉曼",
                    "拉惹阿里和天猛公胡先"
                ],
                "answer": 0,
                "explanation": "**Answer: Temenggong Abdul Rahman and Sultan Hussein Shah**\n\n**The Two Signatories:**\n\n1. **Temenggong Abdul Rahman** (天猛公阿都拉曼)\n   - Local Malay chief who controlled the Singapore area\n   - Had authority over the local population\n   - Already living in Singapore when Raffles arrived\n\n2. **Sultan Hussein Shah** (苏丹胡先)\n   - Older brother in the Johor succession dispute\n   - Raffles recognized him as the rightful Sultan of Johor\n   - Was living in Riau when Raffles contacted him\n\n**Why This Mattered:**\n- Raffles needed **legitimate local authority** to establish the trading post\n- The treaty gave British legal claim to Singapore\n- In exchange, both leaders received annual payments (stipends)\n\n**Succession Dispute Context:**\n- Sultan Mahmud Shah III died in 1812\n- Two sons: Hussein (older) and Abdul Rahman (younger)\n- Dutch supported Abdul Rahman → became Sultan\n- British supported Hussein → gave them opportunity to establish Singapore",
                "explanation_zh": "**答案：天猛公阿都拉曼和苏丹胡先**\n\n**两位签署者：**\n\n1. **天猛公阿都拉曼**\n   - 控制新加坡地区的当地马来首领\n   - 对当地人口有权威\n   - 莱佛士到达时已经住在新加坡\n\n2. **苏丹胡先**\n   - 柔佛继承权争议中的哥哥\n   - 莱佛士承认他是柔佛的合法苏丹\n   - 莱佛士联系他时住在廖内\n\n**为什么这很重要：**\n- 莱佛士需要**合法的地方权威**来建立贸易站\n- 该条约赋予英国对新加坡的法律主张\n- 作为交换，两位领导人都获得年度付款（津贴）\n\n**继承权争议背景：**\n- 苏丹马哈茂德三世于1812年去世\n- 两个儿子：胡先（哥哥）和阿都拉曼（弟弟）\n- 荷兰支持阿都拉曼 → 成为苏丹\n- 英国支持胡先 → 给了他们建立新加坡的机会"
            },
            {
                "id": "ex3-free-port-policy",
                "type": "short",
                "difficulty": "easy",
                "prompt": "What was Raffles' 'free port' policy?",
                "prompt_zh": "莱佛士的'自由港'政策是什么？",
                "answer": "A policy of no taxes or tariffs on trade, allowing ships from all countries to trade freely in Singapore",
                "acceptableAnswers": [
                    "No customs duties or trade taxes",
                    "Trade without tariffs or restrictions",
                    "Free trade policy with no import/export taxes"
                ],
                "explanation": "**Answer: A policy of no taxes or tariffs on trade, allowing ships from all countries to trade freely**\n\n**What 'Free Port' Meant:**\n- **No customs duties**: Ships didn't pay taxes when importing/exporting goods\n- **No trade restrictions**: All nations welcome (British, Dutch, Chinese, Indian, American, etc.)\n- **No monopolies**: Free competition among traders\n\n**Why This Was Revolutionary:**\n\n**Comparison with Other Ports:**\n- **Dutch ports** (Batavia, Malacca): Heavy taxes + restrictions on who could trade\n- **British India ports**: Some duties and regulations\n- **Singapore**: ZERO taxes = traders kept all profits\n\n**Result:**\nTraders naturally chose Singapore because it was **cheaper and more open**. This brilliant policy made Singapore explode in growth within just a few years.\n\n**Modern Connection:**\nSingapore is STILL a free port today! We don't charge import duties on most goods. This policy from 1819 continues to define our economy.",
                "explanation_zh": "**答案：对贸易不征税或关税的政策，允许所有国家的船只在新加坡自由贸易**\n\n**'自由港'的含义：**\n- **无海关税**：船只进出口货物时不缴税\n- **无贸易限制**：欢迎所有国家（英国、荷兰、中国、印度、美国等）\n- **无垄断**：商人之间自由竞争\n\n**为什么这是革命性的：**\n\n**与其他港口的比较：**\n- **荷兰港口**（巴达维亚、马六甲）：重税 + 限制谁可以贸易\n- **英属印度港口**：一些关税和法规\n- **新加坡**：零税 = 商人保留所有利润\n\n**结果：**\n商人自然选择新加坡，因为它**更便宜更开放**。这一出色的政策使新加坡在短短几年内爆炸性增长。\n\n**现代联系：**\n新加坡今天仍然是自由港！我们对大多数商品不收进口税。这一1819年的政策继续定义我们的经济。"
            },
            {
                "id": "ex4-anglo-dutch-treaty",
                "type": "short",
                "difficulty": "medium",
                "prompt": "What did the 1824 Anglo-Dutch Treaty establish?",
                "prompt_zh": "1824年英荷条约确立了什么？",
                "answer": "It divided the Malay Archipelago into British and Dutch spheres of influence, with Britain controlling areas north of Singapore (including Malaya) and the Dutch controlling areas south (including Indonesia)",
                "acceptableAnswers": [
                    "Divided Southeast Asia between British and Dutch control",
                    "Britain got Malaya and Singapore, Dutch got Indonesia",
                    "Established British and Dutch colonial boundaries in the region"
                ],
                "explanation": "**Answer: It divided the Malay Archipelago between British and Dutch spheres of influence**\n\n**The Treaty Terms:**\n\n**Britain Received:**\n- Singapore (confirmed British ownership)\n- Malaya (Malay Peninsula)\n- Areas NORTH of Singapore\n\n**Netherlands Received:**\n- Indonesia (Dutch East Indies)\n- Areas SOUTH of Singapore\n- Bencoolen (Sumatra) from Britain in exchange\n\n**Why This Treaty Mattered:**\n\n**1. Ended Competition:**\n- Before: British and Dutch competed for control of same ports\n- After: Each had clear territories → reduced conflict\n\n**2. Secured Singapore:**\n- Dutch had challenged Britain's right to Singapore\n- Treaty **permanently** confirmed British ownership\n- Singapore safe from Dutch interference\n\n**3. Drew Modern Borders:**\n- This 200-year-old treaty STILL influences borders today\n- Malaysia/Indonesia boundary roughly follows this line\n- Singapore's strategic position as gateway between two zones\n\n**Tip**: This treaty is why Singapore and Malaysia were British colonies while Indonesia was Dutch.",
                "explanation_zh": "**答案：它将马来群岛划分为英国和荷兰的势力范围**\n\n**条约条款：**\n\n**英国获得：**\n- 新加坡（确认英国所有权）\n- 马来亚（马来半岛）\n- 新加坡以北地区\n\n**荷兰获得：**\n- 印度尼西亚（荷属东印度）\n- 新加坡以南地区\n- 英国交换的明古连（苏门答腊）\n\n**为什么这个条约很重要：**\n\n**1. 结束竞争：**\n- 之前：英国和荷兰竞争控制同一港口\n- 之后：每个都有明确的领土 → 减少冲突\n\n**2. 确保新加坡：**\n- 荷兰曾挑战英国对新加坡的权利\n- 条约**永久**确认英国所有权\n- 新加坡免受荷兰干预\n\n**3. 划定现代边界：**\n- 这个200年前的条约今天仍然影响边界\n- 马来西亚/印度尼西亚边界大致遵循这条线\n- 新加坡作为两个区域之间门户的战略地位\n\n**提示**：这个条约就是为什么新加坡和马来西亚是英国殖民地而印度尼西亚是荷兰殖民地。"
            },
            {
                "id": "ex5-raffles-town-plan",
                "type": "mcq",
                "difficulty": "medium",
                "prompt": "Which of the following was part of Raffles' Town Plan for organizing Singapore?",
                "prompt_zh": "以下哪项是莱佛士组织新加坡城市规划的一部分？",
                "choices": [
                    "Dividing the town into ethnic residential areas (kampongs)",
                    "Building a railway system connecting all parts of Singapore",
                    "Creating a single mixed residential area for all races",
                    "Banning all non-British residents from certain areas"
                ],
                "choices_zh": [
                    "将城镇划分为民族住宅区（甘榜）",
                    "建造连接新加坡所有地区的铁路系统",
                    "为所有种族创建单一混合住宅区",
                    "禁止所有非英国居民进入某些区域"
                ],
                "answer": 0,
                "explanation": "**Answer: Dividing the town into ethnic residential areas (kampongs)**\n\n**Raffles' Town Plan (1822)**:\n\nRaffles created a structured urban plan that divided Singapore into different zones:\n\n**Ethnic Kampongs (甘榜):**\n- **European Town**: Area around Padang (civic district)\n- **Chinatown**: Chinese residents south of Singapore River\n- **Kampong Glam**: Malay and Arab area (Sultan's palace region)\n- **Chulia Kampong**: Indian (Tamil Muslim) area near Market Street\n\n**Why This Design:**\n- **Order**: Prevented conflicts between different groups\n- **Administration**: Easier to manage separate communities\n- **Culture**: Each group could maintain traditions\n- **Trade**: Different ethnic groups specialized in different trades\n\n**Legacy Today:**\n- These ethnic enclaves STILL EXIST in modern Singapore!\n- Chinatown, Little India, Kampong Glam are major cultural districts\n- Show continuity from colonial urban planning\n\n**Why other options are incorrect:**\n- Railways came much later (1900s)\n- Mixed housing contradicts the segregation policy\n- Non-British weren't banned - they were the majority!",
                "explanation_zh": "**答案：将城镇划分为民族住宅区（甘榜）**\n\n**莱佛士城市规划（1822年）：**\n\n莱佛士创建了一个结构化的城市规划，将新加坡划分为不同的区域：\n\n**民族甘榜：**\n- **欧洲城镇**：围绕草场的区域（市政区）\n- **牛车水**：新加坡河南部的中国居民\n- **甘榜格南**：马来和阿拉伯地区（苏丹宫殿区域）\n- **朱利亚甘榜**：Market Street附近的印度（泰米尔穆斯林）地区\n\n**为什么这样设计：**\n- **秩序**：防止不同群体之间的冲突\n- **管理**：更容易管理独立的社区\n- **文化**：每个群体可以保持传统\n- **贸易**：不同民族群体专门从事不同的贸易\n\n**今天的遗产：**\n- 这些民族飞地在现代新加坡仍然存在！\n- 牛车水、小印度、甘榜格南是主要的文化区\n- 显示了殖民城市规划的延续性\n\n**为什么其他选项不正确：**\n- 铁路来得更晚（1900年代）\n- 混合住房与种族隔离政策相矛盾\n- 非英国人不被禁止 - 他们是大多数！"
            }
        ],
        "ao2": [  # Communication - Explain with evidence
            {
                "id": "ex6-raffles-motives",
                "type": "short",
                "difficulty": "medium",
                "prompt": "Explain ONE reason why the British wanted to establish a trading post in Singapore.",
                "prompt_zh": "解释英国想在新加坡建立贸易站的一个原因。",
                "answer": "The British wanted to establish a port along the Malacca Strait to protect their trade route between India and China, as they were concerned about Dutch dominance in the region which could threaten British commercial interests.",
                "sampleAnswers": [
                    "To challenge Dutch control of the Straits and break their monopoly on regional trade",
                    "Strategic location at the tip of the Malay Peninsula made it perfect for controlling shipping lanes between Indian Ocean and South China Sea",
                    "Needed a safe harbor and supply base for British ships traveling between India and China"
                ],
                "explanation": "**Sample Answer**: The British wanted to establish a port along the Malacca Strait to protect their trade route between India and China, as Dutch dominance could threaten British commercial interests.\n\n**Key Concept**: Strategic imperialism (战略帝国主义)\n\n**British Context in 1819:**\n\n**1. The Trade Problem:**\n- **Route**: British ships sailed India → Malacca Strait → China\n- **Cargoes**: Opium from India, tea/silk from China\n- **Issue**: Dutch controlled most ports along this route\n\n**2. Dutch Threat:**\n- Netherlands controlled: Malacca, Batavia (Jakarta), most of Indonesia\n- Could **block** British ships or charge high fees\n- Dutch and British were rivals for Southeast Asian trade\n\n**3. Singapore as Solution:**\n- **Location**: Southern tip of Malacca Strait = gateway between oceans\n- **Status**: Unclaimed by Dutch → Britain could establish foothold\n- **Function**: Safe harbor + supply base + free trade alternative to Dutch ports\n\n**Result:**\n- Singapore gave Britain **control of the Straits**\n- Protected their valuable India-China trade\n- Undermined Dutch regional dominance\n\n**Tip**: British imperial expansion was driven by TRADE and COMPETITION with other European powers.",
                "explanation_zh": "**示例答案**：英国想沿马六甲海峡建立一个港口，以保护他们在印度和中国之间的贸易路线，因为荷兰的主导地位可能威胁英国的商业利益。\n\n**关键概念**：战略帝国主义\n\n**1819年的英国背景：**\n\n**1. 贸易问题：**\n- **路线**：英国船只航行 印度 → 马六甲海峡 → 中国\n- **货物**：来自印度的鸦片、来自中国的茶叶/丝绸\n- **问题**：荷兰控制了这条路线上的大部分港口\n\n**2. 荷兰威胁：**\n- 荷兰控制：马六甲、巴达维亚（雅加达）、印度尼西亚大部分地区\n- 可以**阻止**英国船只或收取高额费用\n- 荷兰和英国是东南亚贸易的竞争对手\n\n**3. 新加坡作为解决方案：**\n- **位置**：马六甲海峡南端 = 海洋之间的门户\n- **地位**：荷兰未声称 → 英国可以建立据点\n- **功能**：安全港 + 补给基地 + 荷兰港口的自由贸易替代品\n\n**结果：**\n- 新加坡给了英国**对海峡的控制**\n- 保护了他们宝贵的印度-中国贸易\n- 削弱了荷兰的地区主导地位\n\n**提示**：英国帝国扩张是由贸易和与其他欧洲列强的竞争推动的。"
            },
            {
                "id": "ex7-treaty-legitimacy",
                "type": "short",
                "difficulty": "hard",
                "prompt": "Explain why Raffles needed to sign a treaty with local Malay leaders to establish Singapore.",
                "prompt_zh": "解释为什么莱佛士需要与当地马来领导人签署条约才能建立新加坡。",
                "answer": "Raffles needed local authority and legitimacy to claim Singapore for Britain. By signing a treaty with the Temenggong and Sultan, he obtained legal permission to establish a British settlement, which helped defend Britain's claim against Dutch challenges.",
                "sampleAnswers": [
                    "International law required consent from local rulers to colonize territory - treaty provided legal justification",
                    "Without local cooperation, British couldn't control the population or ensure security of the trading post"
                ],
                "explanation": "**Sample Answer**: Raffles needed local authority and legitimacy. By signing a treaty with the Temenggong and Sultan, he obtained legal permission to establish a British settlement, defending Britain's claim against Dutch challenges.\n\n**Key Concept**: Colonial legitimacy (殖民合法性)\n\n**Why Treaties Were Necessary:**\n\n**1. International Law (19th century):**\n- European powers recognized each other's colonial claims\n- But claims needed to be **legitimate** (not just military force)\n- Treaty with local rulers = proof of \"legal\" acquisition\n- Without treaty = other Europeans could challenge Britain's right\n\n**2. Practical Governance:**\n- **Population control**: Local leaders helped manage Malay community\n- **Security**: Temenggong's men could maintain order\n- **Land use**: Sultan could grant land for British buildings\n- **Resources**: Local cooperation provided labor, supplies\n\n**3. Dutch Challenge:**\n- Netherlands initially contested British presence in Singapore\n- Argued Singapore was in Dutch sphere of influence\n- British countered: \"We have a treaty with the legitimate Sultan!\"\n- Treaty strengthened British legal position → Dutch eventually accepted (1824 treaty)\n\n**The Price:**\nBritain paid annual stipends:\n- Sultan Hussein: 5,000 Spanish dollars/year\n- Temenggong: 3,000 Spanish dollars/year\n\nSmall price for control of such a strategic location!\n\n**Tip**: Colonialism often operated through **treaties** and **legal frameworks**, not just military conquest.",
                "explanation_zh": "**示例答案**：莱佛士需要地方权威和合法性。通过与天猛公和苏丹签署条约，他获得了建立英国定居点的法律许可，保护英国的主张免受荷兰的挑战。\n\n**关键概念**：殖民合法性\n\n**为什么需要条约：**\n\n**1. 国际法（19世纪）：**\n- 欧洲列强承认彼此的殖民主张\n- 但主张需要**合法**（不仅仅是军事力量）\n- 与当地统治者的条约 = \"合法\"获取的证明\n- 没有条约 = 其他欧洲人可以挑战英国的权利\n\n**2. 实际治理：**\n- **人口控制**：地方领导人帮助管理马来社区\n- **安全**：天猛公的人可以维持秩序\n- **土地使用**：苏丹可以授予英国建筑用地\n- **资源**：当地合作提供劳动力、物资\n\n**3. 荷兰挑战：**\n- 荷兰最初对英国在新加坡的存在提出异议\n- 辩称新加坡在荷兰的势力范围内\n- 英国反驳：\"我们与合法苏丹有条约！\"\n- 条约加强了英国的法律地位 → 荷兰最终接受（1824年条约）\n\n**代价：**\n英国支付年度津贴：\n- 苏丹胡先：每年5,000西班牙元\n- 天猛公：每年3,000西班牙元\n\n对于控制如此战略位置来说，这是一个小代价！\n\n**提示**：殖民主义经常通过**条约**和**法律框架**运作，而不仅仅是军事征服。"
            },
            {
                "id": "ex8-free-port-success",
                "type": "short",
                "difficulty": "medium",
                "prompt": "Explain how the free port policy helped Singapore grow rapidly.",
                "prompt_zh": "解释自由港政策如何帮助新加坡快速增长。",
                "answer": "The free port policy attracted traders from all over the world because they could trade without paying taxes or duties. This made Singapore cheaper and more profitable than Dutch-controlled ports, causing rapid growth in trade volume and population.",
                "sampleAnswers": [
                    "No taxes meant traders saved money and earned more profit, so they chose Singapore over competing ports with heavy duties",
                    "Open to all nations policy created a cosmopolitan trading hub that connected multiple trade networks (Chinese, Indian, European, Southeast Asian)"
                ],
                "explanation": "**Sample Answer**: The free port policy attracted traders worldwide because they could trade without taxes. This made Singapore cheaper than Dutch ports, causing rapid growth in trade and population.\n\n**Key Concept**: Economic incentives (经济激励)\n\n**How Free Port Drove Growth:**\n\n**1. Simple Economics:**\n\n**Dutch Port (e.g., Batavia):**\n- Trader sells 100 bags of pepper for $1,000\n- Dutch charge 20% duty = $200 tax\n- Trader keeps: $800\n\n**Singapore:**\n- Trader sells same pepper for $1,000\n- NO tax\n- Trader keeps: $1,000 (25% more profit!)\n\n**Result**: Traders naturally chose Singapore.\n\n**2. Network Effects:**\n- More traders came → More buyers available\n- More buyers → Better prices for sellers\n- Better prices → Even more traders came\n- **Positive feedback loop** = exponential growth\n\n**3. Evidence of Success:**\n\n**Year 1819** (first year):\n- Population: ~150 people\n- Trade value: Minimal\n\n**Year 1823** (4 years later):\n- Population: ~10,000 people\n- Trade value: 8 million Spanish dollars\n- Ships: Hundreds per year\n\n**Year 1860** (40 years later):\n- Population: ~80,000 people\n- Trade value: 40+ million dollars\n- **Largest port in Southeast Asia**\n\n**Why It Worked:**\n- **No barriers** = Maximum accessibility\n- **All nations welcome** = Connected multiple trade networks\n- **No monopolies** = Competition kept prices fair\n\n**Lesson**: Sometimes REMOVING restrictions (taxes) works better than ADDING regulations.",
                "explanation_zh": "**示例答案**：自由港政策吸引了世界各地的商人，因为他们可以在不缴税的情况下进行贸易。这使新加坡比荷兰港口便宜，导致贸易和人口快速增长。\n\n**关键概念**：经济激励\n\n**自由港如何推动增长：**\n\n**1. 简单经济学：**\n\n**荷兰港口（例如巴达维亚）：**\n- 商人以$1,000卖100袋胡椒\n- 荷兰收取20%税 = $200税\n- 商人保留：$800\n\n**新加坡：**\n- 商人以$1,000卖同样的胡椒\n- 无税\n- 商人保留：$1,000（多25%利润！）\n\n**结果**：商人自然选择新加坡。\n\n**2. 网络效应：**\n- 更多商人来 → 更多买家可用\n- 更多买家 → 卖家得到更好的价格\n- 更好的价格 → 更多商人来\n- **正反馈循环** = 指数增长\n\n**3. 成功证据：**\n\n**1819年**（第一年）：\n- 人口：约150人\n- 贸易价值：微不足道\n\n**1823年**（4年后）：\n- 人口：约10,000人\n- 贸易价值：800万西班牙元\n- 船只：每年数百艘\n\n**1860年**（40年后）：\n- 人口：约80,000人\n- 贸易价值：4000多万元\n- **东南亚最大港口**\n\n**为什么有效：**\n- **无障碍** = 最大可及性\n- **欢迎所有国家** = 连接多个贸易网络\n- **无垄断** = 竞争保持价格公平\n\n**教训**：有时去除限制（税收）比增加法规更有效。"
            },
            {
                "id": "ex9-town-plan-segregation",
                "type": "short",
                "difficulty": "hard",
                "prompt": "Explain ONE advantage AND ONE disadvantage of Raffles' policy of separating different ethnic groups into different residential areas.",
                "prompt_zh": "解释莱佛士将不同民族分隔到不同住宅区政策的一个优点和一个缺点。",
                "answer": "Advantage: It reduced conflicts between different groups by giving each community their own space to practice their culture and religion without interference. Disadvantage: It created divisions between racial groups and limited interaction, which could have led to misunderstanding and prejudice.",
                "sampleAnswers": [
                    "Advantage: Easier for colonial administration to control and manage each community separately. Disadvantage: Encouraged racial segregation and prevented integration of different communities",
                    "Advantage: Each group could maintain their cultural identity and traditions. Disadvantage: Created physical and social barriers that made it harder for people of different races to interact and understand each other"
                ],
                "explanation": "**Sample Answer**: Advantage: Reduced conflicts by giving each community space for their culture. Disadvantage: Created divisions and limited interaction between racial groups.\n\n**Key Concept**: Colonial urban planning and social engineering (殖民城市规划与社会工程)\n\n**Advantages of Ethnic Segregation:**\n\n**1. Order and Stability:**\n- Different cultures didn't clash over religious practices, food customs, noise\n- Each area had its own temples, mosques, churches without conflict\n- Example: Muslim areas had mosques for Friday prayers without disturbing others\n\n**2. Administrative Efficiency:**\n- British could appoint ethnic leaders (kapitan) to manage each community\n- Easier to enforce different laws for different groups\n- Simplified tax collection and governance\n\n**3. Cultural Preservation:**\n- Each group could maintain language, customs, festivals\n- Traditional trades flourished (Chinese: trading, Malays: fishing, Indians: textiles)\n- Created distinct cultural identities we still see today\n\n**Disadvantages of Ethnic Segregation:**\n\n**1. Racial Division:**\n- **Physical barriers** → **Social barriers**\n- People rarely interacted with other races\n- Reinforced \"us vs them\" mentality\n- Laid groundwork for racial tensions\n\n**2. Limited Integration:**\n- Children grew up only knowing their own community\n- Different groups developed stereotypes about each other\n- Harder to build national unity\n\n**3. Inequality:**\n- European area had best infrastructure, widest roads\n- Asian kampongs less developed\n- Reinforced racial hierarchy (Europeans on top)\n\n**Long-term Impact:**\nThis colonial policy created **racial categories** that Singapore inherited at independence. Our modern challenge of building multiracial harmony stems partly from this historical segregation.\n\n**Balanced Perspective**: The policy had practical benefits but also created problems we're still addressing through policies like HDB ethnic quotas and racial harmony laws.\n\n**Tip**: When asked for advantages AND disadvantages, give BALANCED analysis - acknowledge both sides fairly.",
                "explanation_zh": "**示例答案**：优点：通过给每个社区空间来实践他们的文化来减少冲突。缺点：造成分裂并限制了种族之间的互动。\n\n**关键概念**：殖民城市规划与社会工程\n\n**民族隔离的优点：**\n\n**1. 秩序与稳定：**\n- 不同文化不会因宗教习俗、饮食习惯、噪音而冲突\n- 每个地区都有自己的寺庙、清真寺、教堂，没有冲突\n- 例子：穆斯林区有清真寺进行周五祈祷而不打扰他人\n\n**2. 行政效率：**\n- 英国可以任命民族领导人（甲必丹）管理每个社区\n- 更容易对不同群体执行不同法律\n- 简化税收和治理\n\n**3. 文化保护：**\n- 每个群体可以保持语言、习俗、节日\n- 传统贸易蓬勃发展（中国人：贸易，马来人：捕鱼，印度人：纺织）\n- 创造了我们今天仍然看到的独特文化身份\n\n**民族隔离的缺点：**\n\n**1. 种族分裂：**\n- **物理障碍** → **社会障碍**\n- 人们很少与其他种族互动\n- 强化了\"我们对他们\"的心态\n- 为种族紧张关系奠定了基础\n\n**2. 有限的融合：**\n- 孩子只认识自己的社区长大\n- 不同群体对彼此产生刻板印象\n- 更难建立国家团结\n\n**3. 不平等：**\n- 欧洲地区有最好的基础设施、最宽的道路\n- 亚洲甘榜较不发达\n- 强化了种族等级制度（欧洲人在顶部）\n\n**长期影响：**\n这一殖民政策创造了新加坡独立时继承的**种族类别**。我们建立多元种族和谐的现代挑战部分源于这种历史隔离。\n\n**平衡视角**：该政策有实际好处，但也创造了我们仍在通过组屋种族配额和种族和谐法等政策解决的问题。\n\n**提示**：当被要求给出优点和缺点时，给出平衡的分析 - 公平地承认双方。"
            },
            {
                "id": "ex10-ned-psycholocial-defence",
                "type": "short",
                "difficulty": "hard",
                "prompt": "Explain how understanding Singapore's founding as a British colony helps us appreciate Psychological Defence today.",
                "prompt_zh": "解释了解新加坡作为英国殖民地的建立如何帮助我们理解今天的心理防卫。",
                "answer": "Singapore was founded by foreigners (British) as a colonial outpost, not by Singaporeans themselves. This history teaches us that we cannot take our nationhood for granted - we must actively build national identity and unity. Psychological Defence means having strong belief in Singapore's future despite our complex colonial past.",
                "sampleAnswers": [
                    "Our founding through colonial conquest rather than indigenous nationalism means we have to work harder to build shared identity and resist divisive narratives that could undermine national unity",
                    "Colonial history of racial segregation shows why we must consciously build multiracial harmony and resist attempts to divide Singaporeans along ethnic lines"
                ],
                "explanation": "**Sample Answer**: Singapore was founded by foreigners as a colonial outpost, not by Singaporeans. This history teaches us not to take nationhood for granted - we must actively build national identity. Psychological Defence means believing in Singapore's future despite our complex past.\n\n**Key Concept**: Nation-building from colonial foundations (从殖民基础建国)\n\n**The Historical Challenge:**\n\n**Unlike Many Nations:**\n- **Natural nations**: Shared ancestry, culture, language (e.g., Japan, Thailand)\n- **Singapore**: Created by British imperial strategy in 1819\n  - No indigenous \"Singaporean\" people\n  - Multiple immigrant groups brought for British economic benefit\n  - No shared pre-colonial history\n\n**What This Means:**\n\n**1. Artificial Origins:**\n- Singapore didn't exist as a nation before 1819\n- British CREATED Singapore for trade\n- People came from elsewhere (China, India, Malaya, Indonesia)\n- **Question**: What makes us \"Singaporean\" if we're all immigrants?\n\n**2. Colonial Legacies We Inherited:**\n- Racial divisions (kampong system)\n- Different languages (no common tongue)\n- Different religions (Buddhism, Islam, Hinduism, Christianity)\n- Economic inequality (Europeans vs Asians)\n\n**3. Independence Challenge (1965):**\n- Suddenly independent with NO natural unity\n- Had to CREATE national identity from scratch\n- Risk: Country could fragment along racial/religious lines\n\n**Why This Connects to Psychological Defence:**\n\n**Psychological Defence = Mental readiness to defend Singapore**\n\nBut defending Singapore requires believing IN Singapore. Colonial history makes this harder because:\n\n**Potential Threats to National Psychology:**\n- \"We're not really a nation, just colonial leftovers\"\n- \"My ethnic group has more in common with ancestral homeland\"\n- \"Singapore has no real history/culture, why fight for it?\"\n- \"Racial divisions from colonial era prove we can't unite\"\n\n**Psychological Defence Response:**\n- **Acknowledge**: Yes, we have complex colonial origins\n- **But**: We CHOSE to build a nation from this foundation\n- **Pride**: We succeeded where others failed (racial harmony, prosperity)\n- **Commitment**: Our future matters more than our past\n- **Shared identity**: Being Singaporean means embracing our diversity as strength\n\n**Practical Application:**\n\n**Examples of Psychological Attacks:**\n- Foreign propaganda: \"Singapore is fake nation, will split apart\"\n- Internal division: \"My race/religion more important than being Singaporean\"\n- Defeatism: \"Small country, cannot survive without big powers\"\n\n**Psychological Defence Means:**\n- **Rejecting** narratives that divide us along colonial racial lines\n- **Embracing** multicultural identity as Singapore's strength\n- **Believing** in our ability to survive despite artificial origins\n- **Teaching** younger generations to value our hard-won unity\n\n**Why History Matters:**\nUnderstanding our colonial founding helps us appreciate:\n- National unity is FRAGILE (not natural given our origins)\n- We must ACTIVELY maintain it (through policies, education, NS)\n- External actors may try to EXPLOIT our diverse origins to divide us\n- **Psychological Defence** means mental immunity to such attempts\n\n**National Education Link:**\n- **\"No one owes Singapore a living\"** - We built this nation from colonial trading post\n- **\"We must ourselves defend Singapore\"** - Can't rely on others, must believe in ourselves\n- **Multiracial harmony** - Conscious effort to overcome colonial racial divisions\n\n**Tip**: Psychological Defence isn't just about morale during war - it's about everyday commitment to Singapore's multiracial identity and belief in our future despite complex origins.",
                "explanation_zh": "**示例答案**：新加坡由外国人作为殖民前哨建立，而不是由新加坡人自己建立。这段历史教导我们不要把国家地位视为理所当然 - 我们必须积极建立国家认同。心理防卫意味着尽管我们的过去很复杂，但仍相信新加坡的未来。\n\n**关键概念**：从殖民基础建国\n\n**历史挑战：**\n\n**与许多国家不同：**\n- **自然国家**：共同祖先、文化、语言（例如日本、泰国）\n- **新加坡**：1819年由英国帝国战略创建\n  - 没有土著\"新加坡人\"\n  - 为英国经济利益带来多个移民群体\n  - 没有共同的前殖民历史\n\n**这意味着什么：**\n\n**1. 人工起源：**\n- 新加坡在1819年之前不作为国家存在\n- 英国为贸易创建新加坡\n- 人们来自其他地方（中国、印度、马来亚、印度尼西亚）\n- **问题**：如果我们都是移民，是什么让我们成为\"新加坡人\"？\n\n**2. 我们继承的殖民遗产：**\n- 种族分裂（甘榜系统）\n- 不同语言（无共同语言）\n- 不同宗教（佛教、伊斯兰教、印度教、基督教）\n- 经济不平等（欧洲人对亚洲人）\n\n**3. 独立挑战（1965年）：**\n- 突然独立，没有自然团结\n- 必须从零开始创建国家认同\n- 风险：国家可能沿着种族/宗教线分裂\n\n**为什么这与心理防卫有关：**\n\n**心理防卫 = 保护新加坡的心理准备**\n\n但保护新加坡需要相信新加坡。殖民历史使这更难，因为：\n\n**对国家心理的潜在威胁：**\n- \"我们不是真正的国家，只是殖民残余\"\n- \"我的民族群体与祖先家园有更多共同点\"\n- \"新加坡没有真正的历史/文化，为什么要为它而战？\"\n- \"殖民时代的种族分裂证明我们无法团结\"\n\n**心理防卫回应：**\n- **承认**：是的，我们有复杂的殖民起源\n- **但是**：我们选择从这个基础建立一个国家\n- **自豪**：我们在其他人失败的地方成功了（种族和谐、繁荣）\n- **承诺**：我们的未来比我们的过去更重要\n- **共同身份**：成为新加坡人意味着将我们的多样性作为力量\n\n**实际应用：**\n\n**心理攻击的例子：**\n- 外国宣传：\"新加坡是假国家，会分裂\"\n- 内部分裂：\"我的种族/宗教比成为新加坡人更重要\"\n- 失败主义：\"小国，没有大国就无法生存\"\n\n**心理防卫意味着：**\n- **拒绝**沿着殖民种族线分裂我们的叙事\n- **拥抱**多元文化认同作为新加坡的力量\n- **相信**我们尽管人工起源仍能生存的能力\n- **教导**年轻一代珍惜我们来之不易的团结\n\n**为什么历史很重要：**\n了解我们的殖民建国帮助我们欣赏：\n- 国家团结是脆弱的（鉴于我们的起源不自然）\n- 我们必须积极维护它（通过政策、教育、国民服役）\n- 外部行为者可能试图利用我们的多元起源来分裂我们\n- **心理防卫**意味着对此类尝试的心理免疫\n\n**国民教育联系：**\n- **\"没有人欠新加坡一份生活\"** - 我们从殖民贸易站建立了这个国家\n- **\"我们必须自己保卫新加坡\"** - 不能依赖他人，必须相信自己\n- **多元种族和谐** - 有意识地努力克服殖民种族分裂\n\n**提示**：心理防卫不仅仅是战争期间的士气 - 它是对新加坡多元种族身份的日常承诺，以及尽管起源复杂但对我们未来的信念。"
            }
        ],
        "ao3": [  # Source-Based Questions
            {
                "id": "ex11-sbq-raffles-letter",
                "type": "sbq",
                "subtype": "inference",
                "difficulty": "medium",
                "source": "Letter from Stamford Raffles (1819)",
                "sourceText": "What Malta is in the West, that may Singapore become in the East. It is impossible to calculate the value and importance of a free port in the Straits of Malacca. Already we have upwards of one hundred small vessels here from different quarters, all hoping to evade the restrictions and monopolies of the Dutch.",
                "sourceText_zh": "在西方的马耳他，新加坡可能在东方成为什么。在马六甲海峡建立一个自由港的价值和重要性是无法估量的。我们已经有超过一百艘来自不同地区的小船在这里，都希望逃避荷兰的限制和垄断。",
                "prompt": "What can you infer from this source about Raffles' expectations for Singapore?",
                "prompt_zh": "从这个来源你可以推断出莱佛士对新加坡的期望是什么？",
                "answer": "I can infer that Raffles expected Singapore to become a very important British strategic and trading center in Asia, comparable to Malta's role for Britain in the Mediterranean, and that he believed it would attract many traders who wanted to avoid Dutch control.",
                "sampleAnswers": [
                    "Raffles expected Singapore to be a major British base in the East and to draw traders away from Dutch ports through free trade",
                    "He predicted Singapore would become strategically important like Malta and would succeed because traders wanted an alternative to Dutch monopolies"
                ],
                "scaffolding": [
                    "What does comparing Singapore to Malta tell you?",
                    "Why are 100 vessels already there?",
                    "What problem were traders trying to escape?"
                ],
                "markingCriteria": {
                    "level2": "Makes valid inference with clear support from source about both strategic importance AND commercial success (2-3 marks)",
                    "level1": "Makes inference but lacks clear support or only addresses one aspect (1 mark)"
                },
                "explanation": "**Sample Answer**: I can infer that Raffles expected Singapore to become a very important British strategic and trading center, comparable to Malta in the Mediterranean, and that he believed it would attract traders wanting to avoid Dutch control.\n\n**Key Concept**: Making inferences from primary sources (从主要来源推断)\n\n**Analyzing the Source:**\n\n**Clue 1**: \"What Malta is in the West, that may Singapore become in the East\"\n- **Malta**: British naval base controlling Mediterranean Sea\n- **Inference**: Raffles envisioned Singapore as British strategic base controlling Southeast Asian waters\n- Shows **geopolitical ambitions**, not just trade\n\n**Clue 2**: \"impossible to calculate the value and importance of a free port\"\n- **Inference**: Raffles believed free trade would make Singapore extremely valuable\n- \"Impossible to calculate\" = unlimited potential\n- Shows **economic vision**\n\n**Clue 3**: \"upwards of one hundred small vessels... hoping to evade the restrictions... of the Dutch\"\n- **Evidence**: Traders already coming just 几 months after founding\n- **Inference**: Free port policy immediately attracting traders dissatisfied with Dutch monopolies\n- Shows Raffles' **strategy was working**\n\n**What This Reveals About Raffles:**\n\n**1. Strategic Thinker:**\n- Saw Singapore not just as port but as regional power center\n- Understood geopolitical competition with Dutch and French\n\n**2. Economic Visionary:**\n- Predicted free trade would create prosperity\n- Understood traders valued freedom over regulation\n\n**3. Confident in Success:**\n- Already seeing positive results (100 vessels in short time)\n- Believed Singapore could rival Malta's importance\n\n**Historical Note**: Raffles' prediction came TRUE - Singapore DID become \"Malta of the East\" and the greatest port in Asia within decades.\n\n**Tip**: When making inferences, look for author's COMPARISONS (Singapore = Malta), PREDICTIONS (\"may become\"), and EVIDENCE they cite (100 vessels).",
                "explanation_zh": "**示例答案**：我可以推断莱佛士期望新加坡成为非常重要的英国战略和贸易中心，可与地中海的马耳他相媲美，并且他相信它会吸引想要避免荷兰控制的商人。\n\n**关键概念**：从主要来源推断\n\n**分析来源：**\n\n**线索1**：\"在西方的马耳他，新加坡可能在东方成为什么\"\n- **马耳他**：控制地中海的英国海军基地\n- **推断**：莱佛士设想新加坡作为控制东南亚水域的英国战略基地\n- 显示**地缘政治野心**，不仅仅是贸易\n\n**线索2**：\"在马六甲海峡建立一个自由港的价值和重要性是无法估量的\"\n- **推断**：莱佛士相信自由贸易会使新加坡非常有价值\n- \"无法估量\" = 无限潜力\n- 显示**经济愿景**\n\n**线索3**：\"超过一百艘小船...希望逃避...荷兰的限制\"\n- **证据**：建立仅几个月后商人已经来了\n- **推断**：自由港政策立即吸引对荷兰垄断不满的商人\n- 显示莱佛士的**策略正在奏效**\n\n**这揭示了莱佛士的什么：**\n\n**1. 战略思想家：**\n- 将新加坡视为不仅仅是港口而是地区权力中心\n- 理解与荷兰和法国的地缘政治竞争\n\n**2. 经济远见者：**\n- 预测自由贸易会创造繁荣\n- 理解商人重视自由而不是监管\n\n**3. 对成功有信心：**\n- 已经看到积极结果（短时间内100艘船）\n- 相信新加坡可以与马耳他的重要性相媲美\n\n**历史注释**：莱佛士的预测成真了 - 新加坡确实在几十年内成为\"东方的马耳他\"和亚洲最大的港口。\n\n**提示**：做推断时，寻找作者的比较（新加坡=马耳他）、预测（\"可能成为\"）和他们引用的证据（100艘船）。"
            },
            {
                "id": "ex12-sbq-treaty-text",
                "type": "sbq",
                "subtype": "analysis",
                "difficulty": "hard",
                "source": "Treaty between Britain and Sultan Hussein (1819)",
                "sourceText": "Sultan Hussein Shah grants to the British East India Company permission to establish a factory and trading post on the island of Singapore. In return, the Company agrees to pay the Sultan 5,000 Spanish dollars annually.",
                "sourceText_zh": "苏丹胡先授予英国东印度公司在新加坡岛建立工厂和贸易站的许可。作为回报，公司同意每年向苏丹支付5,000西班牙元。",
                "prompt": "What does this source reveal about the relationship between the British and the Sultan?",
                "prompt_zh": "这个来源揭示了英国和苏丹之间的什么关系？",
                "answer": "This source reveals an unequal relationship where the Sultan had formal authority to grant permission but the British gained actual control of Singapore, paying only a small annual sum for the entire island.",
                "sampleAnswers": [
                    "The relationship appears formal and legal, but the tiny payment shows British exploitation - trading permanent land control for minimal annual payment",
                    "Shows colonial pattern of using treaties to legally acquire territory while maintaining appearance of local ruler's authority"
                ],
                "scaffolding": [
                    "Who is granting what to whom?",
                    "What does the Sultan receive in return?",
                    "Is this a fair exchange?"
                ],
                "markingCriteria": {
                    "level2": "Analyzes power dynamics and recognizes inequality in the arrangement (2-3 marks)",
                    "level1": "Identifies basic transaction but doesn't analyze implications (1 mark)"
                },
                "explanation": "**Sample Answer**: This source reveals an unequal relationship where the Sultan had formal authority to grant permission but the British gained actual control, paying only a small sum for the entire island.\n\n**Key Concept**: Colonial treaties and power dynamics (殖民条约与权力动态)\n\n**Surface Reading vs. Deep Analysis:**\n\n**Surface (What it SAYS):**\n- Sultan grants permission\n- Britain establishes trading post\n- Company pays annual fee\n- Looks like **fair business deal**\n\n**Deep Analysis (What it MEANS):**\n\n**1. Unequal Exchange:**\n- **Sultan gives**: Entire island of Singapore (land, sovereignty, control)\n- **Sultan receives**: 5,000 Spanish dollars/year (about $1,250 USD today)\n- **Imbalance**: Permanent loss of territory for small annual payment\n\n**2. Legal vs. Actual Authority:**\n- **Formal**: Sultan \"grants permission\" (appears he's in control)\n- **Reality**: British dictate terms, Sultan has little choice\n- **Why Sultan agreed**: Needed British support against rivals + payment helped finances\n\n**3. Colonial Pattern:**\n- Treaty uses LEGAL language to mask POWER imbalance\n- \"Permission\" and \"grants\" suggest voluntary consent\n- But Sultan was in weak position, couldn't refuse\n\n**4. Long-term Implications:**\n- Treaty was just first step\n- British gradually expanded control\n- By 1824: Britain had FULL sovereignty, Sultan had NO power\n- Payment continued, but Sultan became irrelevant figurehead\n\n**Historical Context:**\n- This is typical of **imperialism through treaties**\n- European powers preferred **legal acquisition** over military conquest\n- Treaties provided **legitimacy** while achieving **domination**\n\n**Critical Thinking:**\n\n**Question to Ask**: Was this truly a \"grant\" or was it forced extraction of land rights under guise of legal agreement?\n\n**Evidence of Inequality:**\n- 5,000 dollars = tiny sum for an entire strategically located island\n- Sultan's \"permission\" becomes meaningless as British expand control\n- Local leaders reduced to paid figureheads\n\n**Why This Matters:**\nUnderstanding power dynamics in historical sources helps us see beyond official language to recognize exploitation and inequality.\n\n**Tip**: When analyzing treaties, ask: WHO benefits more? Is this truly equal? What does the language HIDE?",
                "explanation_zh": "**示例答案**：这个来源揭示了一种不平等的关系，苏丹有正式权威授予许可，但英国获得了实际控制权，只为整个岛屿支付一小笔年费。\n\n**关键概念**：殖民条约与权力动态\n\n**表面阅读vs.深度分析：**\n\n**表面（它说什么）：**\n- 苏丹授予许可\n- 英国建立贸易站\n- 公司支付年费\n- 看起来像**公平的商业交易**\n\n**深度分析（它意味着什么）：**\n\n**1. 不平等交换：**\n- **苏丹给予**：整个新加坡岛（土地、主权、控制权）\n- **苏丹获得**：每年5,000西班牙元（约今天1,250美元）\n- **不平衡**：永久失去领土换取小额年度付款\n\n**2. 法律vs.实际权威：**\n- **正式**：苏丹\"授予许可\"（看起来他在控制）\n- **现实**：英国规定条款，苏丹几乎没有选择\n- **为什么苏丹同意**：需要英国支持对抗对手 + 付款帮助财务\n\n**3. 殖民模式：**\n- 条约使用法律语言来掩盖权力不平衡\n- \"许可\"和\"授予\"暗示自愿同意\n- 但苏丹处于弱势地位，无法拒绝\n\n**4. 长期影响：**\n- 条约只是第一步\n- 英国逐渐扩大控制\n- 到1824年：英国拥有完全主权，苏丹没有权力\n- 付款继续，但苏丹成为无关紧要的名义首脑\n\n**历史背景：**\n- 这是**通过条约的帝国主义**的典型\n- 欧洲列强更喜欢**法律获取**而不是军事征服\n- 条约提供了**合法性**同时实现了**统治**\n\n**批判性思维：**\n\n**要问的问题**：这真的是\"授予\"还是在法律协议的幌子下强制提取土地权？\n\n**不平等的证据：**\n- 5,000元 = 整个战略位置岛屿的微小金额\n- 随着英国扩大控制，苏丹的\"许可\"变得毫无意义\n- 地方领导人沦为有偿名义首脑\n\n**为什么这很重要：**\n理解历史来源中的权力动态帮助我们超越官方语言看到剥削和不平等。\n\n**提示**：分析条约时，问：谁受益更多？这真的平等吗？语言隐藏了什么？"
            },
            {
                "id": "ex13-sbq-purpose-raffles",
                "type": "short",
                "difficulty": "medium",
                "source": "Letter from Stamford Raffles",
                "prompt": "Why do you think Raffles wrote this letter praising Singapore's potential?",
                "prompt_zh": "你认为莱佛士为什么写这封赞扬新加坡潜力的信？",
                "answer": "To convince his superiors in the British East India Company that establishing Singapore was a good decision worth supporting, by demonstrating its strategic and commercial value",
                "acceptableAnswers": [
                    "To justify his actions in founding Singapore to the Company authorities",
                    "To persuade British officials to provide resources and support for the new settlement"
                ],
                "explanation": "**Answer**: To convince his superiors that establishing Singapore was a good decision worth supporting, demonstrating its strategic and commercial value.\n\n**Key Concept**: Understanding authorial purpose (理解作者目的)\n\n**Context for the Letter:**\n\n**Raffles' Position:**\n- He was an employee of the British East India Company\n- He had taken a **big risk** by founding Singapore without full authorization\n- Company directors in London might disapprove and abandon Singapore\n- He needed to **justify his actions**\n\n**What Was at Stake:**\n- **If approved**: Singapore becomes permanent British base\n- **If rejected**: Company withdraws, Dutch might take over\n- Raffles' career and reputation on the line\n\n**Evidence of Persuasive Purpose:**\n\n**1. Strategic Comparison:**\n- \"What Malta is in the West...\" → Uses familiar, valued example\n- Malta was crucial British base → Singapore equally important\n- Flatters Company's strategic ambitions\n\n**2. Economic Promise:**\n- \"impossible to calculate the value\" → Emphasizes profit potential\n- Company motivated by MONEY → This appeals to their interests\n\n**3. Immediate Success:**\n- \"100 vessels already here\" → Proves concept working\n- Provides concrete evidence, not just promises\n\n**4. Competitive Advantage:**\n- \"evade... Dutch restrictions\" → Shows Singapore undermining rivals\n- British obsessed with beating Dutch → This argument resonates\n\n**Purpose Analysis:**\n\n**Primary Purpose**: **PERSUADE** Company to support Singapore\n- Not just **inform** (give facts)\n- Not **entertain** (tell story)\n- But **convince** through strategic arguments\n\n**Audience**: British East India Company directors in London\n- Needed reassurance their money well spent\n- Wanted proof of strategic value\n- Required evidence of success\n\n**Effectiveness**:\nRaffles succeeded - Company approved Singapore and provided resources!\n\n**Lesson**: Historical sources often have PERSUASIVE PURPOSE - authors trying to convince others to support their actions/beliefs.\n\n**Tip**: When asked about PURPOSE, consider: WHO is the audience? WHAT does the author want them to do/think? HOW does the content serve that goal?",
                "explanation_zh": "**答案**：说服他的上级，建立新加坡是一个值得支持的好决定，展示其战略和商业价值。\n\n**关键概念**：理解作者目的\n\n**信件背景：**\n\n**莱佛士的位置：**\n- 他是英国东印度公司的雇员\n- 他在未获得充分授权的情况下建立新加坡，承担了**很大风险**\n- 伦敦的公司董事可能不赞成并放弃新加坡\n- 他需要**证明他的行为是正当的**\n\n**利害关系：**\n- **如果批准**：新加坡成为永久英国基地\n- **如果拒绝**：公司撤出，荷兰可能接管\n- 莱佛士的职业生涯和声誉岌岌可危\n\n**说服目的的证据：**\n\n**1. 战略比较：**\n- \"在西方的马耳他...\" → 使用熟悉的、有价值的例子\n- 马耳他是关键的英国基地 → 新加坡同样重要\n- 奉承公司的战略野心\n\n**2. 经济承诺：**\n- \"无法估量的价值\" → 强调利润潜力\n- 公司被金钱驱动 → 这吸引他们的利益\n\n**3. 立即成功：**\n- \"已经有100艘船在这里\" → 证明概念有效\n- 提供具体证据，不仅仅是承诺\n\n**4. 竞争优势：**\n- \"逃避...荷兰的限制\" → 显示新加坡削弱对手\n- 英国痴迷于击败荷兰 → 这个论点引起共鸣\n\n**目的分析：**\n\n**主要目的**：**说服**公司支持新加坡\n- 不仅仅是**告知**（提供事实）\n- 不是**娱乐**（讲故事）\n- 而是通过战略论证**说服**\n\n**受众**：伦敦的英国东印度公司董事\n- 需要保证他们的钱花得好\n- 想要战略价值的证明\n- 需要成功的证据\n\n**有效性**：\n莱佛士成功了 - 公司批准了新加坡并提供了资源！\n\n**教训**：历史来源通常有说服目的 - 作者试图说服他人支持他们的行动/信念。\n\n**提示**：当被问及目的时，考虑：受众是谁？作者希望他们做/想什么？内容如何服务于该目标？"
            },
            {
                "id": "ex14-sbq-reliability",
                "type": "short",
                "difficulty": "hard",
                "source": "Letter from Stamford Raffles",
                "prompt": "Is Raffles' letter a reliable source for understanding Singapore's early success? Explain your answer.",
                "prompt_zh": "莱佛士的信是了解新加坡早期成功的可靠来源吗？解释你的答案。",
                "answer": "Partially reliable - it is a primary source from someone directly involved, providing accurate information about Singapore's location and trade potential, but it may exaggerate success to persuade his superiors, so we should compare it with other sources.",
                "sampleAnswers": [
                    "Reliable for facts (location, free port policy, traders coming) but potentially biased in predictions since Raffles wanted Company support",
                    "Useful but limited - written to convince bosses, so may emphasize positives and downplay challenges"
                ],
                "explanation": "**Sample Answer**: Partially reliable - primary source from someone directly involved, providing accurate information, but may exaggerate to persuade superiors, so compare with other sources.\n\n**Key Concept**: Assessing source reliability (评估来源可靠性)\n\n**Reliability Framework:**\n\nReliability = How much can we TRUST this source for accurate information?\n\nDepends on:\n1. **Origin** (WHO wrote it, WHEN)\n2. **Purpose** (WHY written)\n3. **Content** (WHAT it claims)\n4. **Context** (WHAT else we know)\n\n**Raffles' Letter Analysis:**\n\n**STRENGTHS (Makes it MORE reliable):**\n\n**1. Primary Source:**\n- Written by actual participant (Raffles founded Singapore)\n- Contemporary (written in 1819, same year as events)\n- Firsthand knowledge, not hearsay\n\n**2. Factual Elements:**\n- **Singapore's location**: TRUE (we can verify)\n- **Free port policy**: TRUE (historical records confirm)\n- **Traders arriving**: TRUE (100 vessels is plausible and matches other accounts)\n- **Dutch restrictions**: TRUE (well-documented)\n\n**3. Expert Perspective:**\n- Raffles was experienced colonial administrator\n- Had deep knowledge of regional trade\n- Understood strategic issues\n\n**WEAKNESSES (Makes it LESS reliable):**\n\n**1. Vested Interest:**\n- **Bias**: Raffles NEEDS Singapore to succeed (career depends on it)\n- **Motivation**: Wants to impress superiors → May exaggerate positives\n- **Selective reporting**: Might hide problems or challenges\n\n**2. Persuasive Purpose:**\n- Letter written to CONVINCE, not just INFORM\n- May **inflate** Singapore's importance (\"Malta of East\")\n- May **overpredict** future success\n- Optimistic spin on early results\n\n**3. Limited Perspective:**\n- Only shows British viewpoint\n- Doesn't include Malay/Chinese/Indian perspectives\n- We don't hear from Sultan Hussein or Temenggong\n\n**4. Predictions vs. Facts:**\n- **\"May become\"** = speculation, not certain\n- **\"Impossible to calculate\"** = vague, not specific\n- Future predictions can't be reliable evidence\n\n**VERDICT: Partially Reliable**\n\n**Reliable For:**\n- ✓ Basic facts (Singapore founded 1819, free port policy, strategic location)\n- ✓ British motives and perspective\n- ✓ Evidence of early trade activity\n- ✓ Dutch competition in region\n\n**Less Reliable For:**\n- ✗ Unbiased assessment of Singapore's potential\n- ✗ Challenges and problems faced\n- ✗ Non-British perspectives\n- ✗ Predictions about future (though historically proved right!)\n\n**How to Use Responsibly:**\n- **Cross-reference**: Compare with OTHER sources (Dutch records, local accounts, later statistics)\n- **Verify claims**: Check if 100 vessels is accurate (shipping records)\n- **Consider bias**: Understand Raffles trying to sell his achievement\n- **Extract facts**: Use for factual information, not value judgments\n\n**Historical Note:**\nInterestingly, Raffles' PREDICTIONS turned out accurate - Singapore DID become \"Malta of East.\" But that doesn't make the SOURCE fully reliable at the TIME it was written - it was still biased persuasion.\n\n**Tip**: NO source is 100% reliable or 100% unreliable. Always say \"PARTIALLY reliable\" and explain WHAT aspects you can trust and WHAT you should question.",
                "explanation_zh": "**示例答案**：部分可靠 - 来自直接参与者的主要来源，提供准确信息，但可能夸大以说服上级，所以要与其他来源比较。\n\n**关键概念**：评估来源可靠性\n\n**可靠性框架：**\n\n可靠性 = 我们可以多大程度上信任这个来源提供准确信息？\n\n取决于：\n1. **来源**（谁写的，什么时候）\n2. **目的**（为什么写）\n3. **内容**（声称什么）\n4. **背景**（我们还知道什么）\n\n**莱佛士信件分析：**\n\n**优势（使其更可靠）：**\n\n**1. 主要来源：**\n- 由实际参与者写的（莱佛士建立了新加坡）\n- 同时代（写于1819年，与事件同年）\n- 第一手知识，不是传闻\n\n**2. 事实元素：**\n- **新加坡的位置**：真实（我们可以验证）\n- **自由港政策**：真实（历史记录确认）\n- **商人到达**：真实（100艘船是合理的，与其他记录相符）\n- **荷兰限制**：真实（有充分记录）\n\n**3. 专家视角：**\n- 莱佛士是经验丰富的殖民管理者\n- 对区域贸易有深入了解\n- 了解战略问题\n\n**弱点（使其不太可靠）：**\n\n**1. 既得利益：**\n- **偏见**：莱佛士需要新加坡成功（职业取决于此）\n- **动机**：想给上级留下深刻印象 → 可能夸大积极面\n- **选择性报告**：可能隐藏问题或挑战\n\n**2. 说服目的：**\n- 写信是为了说服，不仅仅是告知\n- 可能**夸大**新加坡的重要性（\"东方的马耳他\"）\n- 可能**过度预测**未来成功\n- 对早期结果的乐观旋转\n\n**3. 有限视角：**\n- 只显示英国观点\n- 不包括马来/中国/印度视角\n- 我们没有听到苏丹胡先或天猛公的声音\n\n**4. 预测vs.事实：**\n- **\"可能成为\"** = 推测，不确定\n- **\"无法估量\"** = 模糊，不具体\n- 未来预测不能成为可靠证据\n\n**结论：部分可靠**\n\n**可靠于：**\n- ✓ 基本事实（1819年建立新加坡，自由港政策，战略位置）\n- ✓ 英国动机和视角\n- ✓ 早期贸易活动的证据\n- ✓ 该地区的荷兰竞争\n\n**不太可靠于：**\n- ✗ 对新加坡潜力的公正评估\n- ✗ 面临的挑战和问题\n- ✗ 非英国视角\n- ✗ 对未来的预测（尽管历史上被证明是对的！）\n\n**如何负责任地使用：**\n- **交叉引用**：与其他来源比较（荷兰记录、当地记录、后来的统计数据）\n- **验证声明**：检查100艘船是否准确（航运记录）\n- **考虑偏见**：理解莱佛士试图推销他的成就\n- **提取事实**：用于事实信息，不是价值判断\n\n**历史注释**：\n有趣的是，莱佛士的预测被证明是准确的 - 新加坡确实成为了\"东方的马耳他\"。但这并不使当时写的来源完全可靠 - 它仍然是有偏见的说服。\n\n**提示**：没有来源是100%可靠或100%不可靠的。总是说\"部分可靠\"并解释你可以信任什么方面，应该质疑什么。"
            },
            {
                "id": "ex15-sbq-comparison",
                "type": "short",
                "difficulty": "hard",
                "source": "Multiple Sources",
                "prompt": "Compare Raffles' 1819 letter (predicting Singapore's greatness) with Wang Dayuan's 1349 account (describing Temasek). What CHANGED about Singapore's role between these two time periods?",
                "prompt_zh": "比较莱佛士1819年的信（预测新加坡的伟大）与汪大渊1349年的记录（描述淡马锡）。在这两个时期之间，新加坡的作用发生了什么变化？",
                "answer": "Singapore changed from being a small natural stopover for monsoon-dependent traders (Temasek) to becoming a strategically planned British colonial hub designed to dominate Southeast Asian trade through free port policy and European imperial backing.",
                "sampleAnswers": [
                    "From passive entrepôt where traders stopped naturally due to monsoons, to active colonial port deliberately created to challenge Dutch control and expand British power",
                    "Changed from organic Southeast Asian trading network participant to European-dominated imperial strategic base with global connections"
                ],
                "explanation": "**Sample Answer**: Singapore changed from a small natural stopover for monsoon-dependent traders (Temasek) to a strategically planned British colonial hub designed to dominate Southeast Asian trade.\n\n**Key Concept**: Historical change over time (历史变化)\n\n**Comparative Analysis:**\n\n**TEMASEK (14th century - Wang Dayuan):**\n\n**Role**: Natural stopover\n- **Why traders came**: Geographic necessity (monsoon winds, fresh water)\n- **Scale**: Local/regional importance\n- **Products**: Local goods (hornbill casques, lakawood, tin)\n- **Control**: Local Malay rulers (independent)\n- **Nature**: **Passive** port (traders came naturally)\n\n**SINGAPORE (19th century - Raffles):**\n\n**Role**: Imperial strategic base\n- **Why traders came**: British free port policy (deliberate economic policy)\n- **Scale**: Regional/global ambitions (\"Malta of East\")\n- **Products**: Re-export hub (goods from entire region)\n- **Control**: British colonial power (part of empire)\n- **Nature**: **Active** port (deliberately created to compete)\n\n**KEY CHANGES:**\n\n**1. From Natural to Planned:**\n- **Temasek**: Geography determined its role\n- **Singapore**: British imperial strategy determined its role\n- **Significance**: Human agency (Raffles' vision) vs. geographic accident\n\n**2. From Local to Global:**\n- **Temasek**: Part of Asian maritime trade networks\n- **Singapore**: Connected to British global empire\n- **Significance**: Singapore became intersection of global commerce, not just regional\n\n**3. From Independent to Colonial:**\n- **Temasek**: Controlled by Malay rulers\n- **Singapore**: British colony\n- **Significance**: Loss of local sovereignty, European dominance\n\n**4. From Organic to Competitive:**\n- **Temasek**: One port among many in region\n- **Singapore**: Deliberately designed to OUTCOMPETE Dutch ports\n- **Significance**: Strategic rivalry between European powers shaped Singapore's role\n\n**5. From Passive to Active Policy:**\n- **Temasek**: No special trade policy needed (location was enough)\n- **Singapore**: Free port policy actively attracted traders\n- **Significance**: Economic engineering, not just geographic advantage\n\n**CONTINUITY (What stayed SAME):**\n- Strategic location (hasn't moved!)\n- Entrepôt function (collecting/redistributing goods)\n- Dependence on trade for survival\n- Multi-ethnic population (traders from many places)\n\n**SIGNIFICANCE OF CHANGE:**\n\nThis transformation shows:\n- **Imperialism's impact**: European colonialism fundamentally changed Southeast Asia\n- **Modernization**: From traditional monsoon-based trade to capitalist free trade\n- **Globalization**: Singapore shifted from regional to global networks\n- **Loss of agency**: Local Malay rulers replaced by European colonizers\n\n**Why This Comparison Matters:**\n\nUnderstanding both periods helps us appreciate:\n- Singapore has LONG history (not just colonial creation)\n- But modern Singapore is PRODUCT of colonialism\n- Geographic advantages are constant, but human policies determine success\n- Colonial disruption had both positive (economic growth) and negative (loss of sovereignty) effects\n\n**Tip**: When comparing sources from different eras, look for CHANGE (what's different) and CONTINUITY (what stayed same). Both are important!",
                "explanation_zh": "**示例答案**：新加坡从依赖季风的商人的小型自然中转站（淡马锡）转变为战略规划的英国殖民枢纽，旨在通过自由港政策和欧洲帝国支持主导东南亚贸易。\n\n**关键概念**：历史变化\n\n**比较分析：**\n\n**淡马锡（14世纪 - 汪大渊）：**\n\n**角色**：自然中转站\n- **为什么商人来**：地理必要性（季风、淡水）\n- **规模**：地方/区域重要性\n- **产品**：当地商品（犀鸟头盔、拉卡木、锡）\n- **控制**：当地马来统治者（独立）\n- **性质**：**被动**港口（商人自然来）\n\n**新加坡（19世纪 - 莱佛士）：**\n\n**角色**：帝国战略基地\n- **为什么商人来**：英国自由港政策（有意的经济政策）\n- **规模**：地区/全球野心（\"东方的马耳他\"）\n- **产品**：再出口枢纽（来自整个地区的商品）\n- **控制**：英国殖民势力（帝国的一部分）\n- **性质**：**主动**港口（有意创建以竞争）\n\n**关键变化：**\n\n**1. 从自然到规划：**\n- **淡马锡**：地理决定其角色\n- **新加坡**：英国帝国战略决定其角色\n- **意义**：人类能动性（莱佛士的愿景）vs.地理偶然\n\n**2. 从地方到全球：**\n- **淡马锡**：亚洲海上贸易网络的一部分\n- **新加坡**：与英国全球帝国相连\n- **意义**：新加坡成为全球商业的交汇点，不仅仅是区域性\n\n**3. 从独立到殖民：**\n- **淡马锡**：由马来统治者控制\n- **新加坡**：英国殖民地\n- **意义**：失去地方主权，欧洲主导\n\n**4. 从有机到竞争：**\n- **淡马锡**：该地区众多港口之一\n- **新加坡**：有意设计以超越荷兰港口\n- **意义**：欧洲列强之间的战略竞争塑造了新加坡的角色\n\n**5. 从被动到主动政策：**\n- **淡马锡**：不需要特殊贸易政策（位置足够）\n- **新加坡**：自由港政策积极吸引商人\n- **意义**：经济工程，不仅仅是地理优势\n\n**延续性（保持相同的内容）：**\n- 战略位置（没有移动！）\n- 转口功能（收集/重新分配商品）\n- 依赖贸易生存\n- 多民族人口（来自许多地方的商人）\n\n**变化的意义：**\n\n这种转变显示：\n- **帝国主义的影响**：欧洲殖民主义从根本上改变了东南亚\n- **现代化**：从传统的基于季风的贸易到资本主义自由贸易\n- **全球化**：新加坡从区域网络转向全球网络\n- **失去能动性**：当地马来统治者被欧洲殖民者取代\n\n**为什么这种比较很重要：**\n\n理解这两个时期帮助我们欣赏：\n- 新加坡有长久历史（不仅仅是殖民创造）\n- 但现代新加坡是殖民主义的产物\n- 地理优势是恒定的，但人类政策决定成功\n- 殖民干扰既有积极影响（经济增长）也有消极影响（失去主权）\n\n**提示**：比较不同时代的来源时，寻找变化（什么不同）和延续性（什么保持相同）。两者都很重要！"
            }
        ]
    },

    # Additional chapters will continue with same structure...
    # For brevity, I'll define the remaining chapter IDs with placeholder counts

    "singapore-growth-port-city": {
        "ao1": [
            {
                "id": "ex1-trade-growth",
                "type": "mcq",
                "difficulty": "easy",
                "prompt": "Which commodity became Singapore's MOST important export in the 19th century?",
                "prompt_zh": "19世纪新加坡最重要的出口商品是什么？",
                "choices": ["Rubber", "Tin", "Opium", "Rice"],
                "choices_zh": ["橡胶", "锡", "鸦片", "大米"],
                "answer": 1,
                "explanation": "**Answer: Tin**\n\nTin was Singapore's most valuable export commodity throughout the 19th century, coming from mines in Malaya and being shipped to markets worldwide.\n\n**Why Tin:**\n- Malayan tin was highest quality in the world\n- Used in canning (food preservation revolution)\n- Singapore was the collection and export hub\n- By 1860s, tin accounted for 40% of export value\n\n**Why other options are incorrect:**\n- Rubber: Became important in EARLY 20th century (1900s), not 19th\n- Opium: Important but not the largest export value\n- Rice: Singapore IMPORTED rice, didn't export it",
                "explanation_zh": "**答案：锡**\n\n锡是整个19世纪新加坡最有价值的出口商品，来自马来亚的矿山并运往世界各地市场。\n\n**为什么是锡：**\n- 马来亚锡是世界上质量最高的\n- 用于罐头制造（食品保存革命）\n- 新加坡是收集和出口枢纽\n- 到1860年代，锡占出口价值的40%\n\n**为什么其他选项不正确：**\n- 橡胶：在20世纪初（1900年代）变得重要，不是19世纪\n- 鸦片：重要但不是最大的出口价值\n- 大米：新加坡进口大米，不出口"
            },
            {
                "id": "ex2-immigrant-pull-factors",
                "type": "short",
                "difficulty": "medium",
                "prompt": "Name TWO reasons why immigrants came to Singapore in the 19th century.",
                "prompt_zh": "说出19世纪移民来新加坡的两个原因。",
                "answer": "1. Economic opportunities - jobs in trade, shipping, plantations, or starting businesses. 2. Escaping poverty or conflict in their home countries like China (Taiping Rebellion), India (famines), or Southeast Asia.",
                "acceptableAnswers": [
                    "Job opportunities and safety from war/famine",
                    "Chance to make money and escape hardship at home",
                    "Free port meant business opportunities and no restrictions"
                ],
                "explanation": "**Answer: 1) Economic opportunities (jobs/business), 2) Escaping poverty/conflict**\n\n**Pull Factors (Why Singapore ATTRACTED):**\n- Booming trade = many jobs (coolies, clerks, sailors, merchants)\n- Free port = easy to start businesses\n- British rule = stable government, law and order\n- No discrimination = all races could work and trade\n\n**Push Factors (Why they LEFT home):**\n- China: Taiping Rebellion (1850-1864) - civil war killed millions\n- India: Famines, British exploitation, poverty\n- Java/Malaya: Limited opportunities, Dutch restrictions\n\n**Modern Connection**: Singapore STILL attracts immigrants for similar reasons - jobs, stability, opportunities!",
                "explanation_zh": "**答案：1）经济机会（工作/生意），2）逃避贫困/冲突**\n\n**拉力因素（为什么新加坡吸引）：**\n- 蓬勃的贸易 = 许多工作（苦力、职员、水手、商人）\n- 自由港 = 容易创业\n- 英国统治 = 稳定政府、法律和秩序\n- 无歧视 = 所有种族都可以工作和贸易\n\n**推力因素（为什么他们离开家）：**\n- 中国：太平天国之乱（1850-1864） - 内战杀死数百万人\n- 印度：饥荒、英国剥削、贫困\n- 爪哇/马来亚：机会有限、荷兰限制\n\n**现代联系**：新加坡仍然因类似原因吸引移民 - 工作、稳定、机会！"
            },
            {
                "id": "ex3-population-growth",
                "type": "mcq",
                "difficulty": "medium",
                "prompt": "Singapore's population grew from about 150 in 1819 to approximately how many by 1860?",
                "prompt_zh": "新加坡的人口从1819年的约150人增长到1860年的大约多少人？",
                "choices": ["10,000", "40,000", "80,000", "150,000"],
                "choices_zh": ["10,000", "40,000", "80,000", "150,000"],
                "answer": 2,
                "explanation": "**Answer: 80,000**\n\nThis represents MASSIVE growth - a 533x increase in just 41 years!\n\n**Population Timeline:**\n- 1819: ~150 (founding year)\n- 1824: ~10,000 (5 years)\n- 1840: ~35,000 (21 years)\n- 1860: ~80,000 (41 years)\n- 1900: ~228,000 (continued growth)\n\n**What Caused This Growth:**\n- Immigration (90%+ of growth)\n- Natural increase (births > deaths)\n- Singapore became known as land of opportunity\n\n**Composition by 1860:**\n- Chinese: ~60% (majority)\n- Malays: ~25%\n- Indians: ~10%\n- Europeans & others: ~5%",
                "explanation_zh": "**答案：80,000**\n\n这代表了巨大的增长 - 仅41年就增长了533倍！\n\n**人口时间线：**\n- 1819年：约150人（建立年）\n- 1824年：约10,000人（5年）\n- 1840年：约35,000人（21年）\n- 1860年：约80,000人（41年）\n- 1900年：约228,000人（持续增长）\n\n**是什么导致了这种增长：**\n- 移民（增长的90%+）\n- 自然增长（出生>死亡）\n- 新加坡成为机会之地\n\n**1860年的组成：**\n- 中国人：约60%（多数）\n- 马来人：约25%\n- 印度人：约10%\n- 欧洲人和其他：约5%"
            },
            {
                "id": "ex4-entrepot-trade",
                "type": "short",
                "difficulty": "medium",
                "prompt": "What is 'entrepôt trade' and why was it important to Singapore?",
                "prompt_zh": "什么是'转口贸易'，为什么它对新加坡很重要？",
                "answer": "Entrepôt trade means importing goods from various countries, storing them temporarily, then re-exporting to other markets. It was important because Singapore didn't produce much itself but made money by being the middleman connecting different trade networks.",
                "acceptableAnswers": [
                    "Collection and redistribution of goods from different regions, which made Singapore wealthy without needing local production",
                    "Acting as trading hub where goods are gathered and sorted for re-export, Singapore's main economic function"
                ],
                "explanation": "**Answer: Entrepôt = import → store → re-export. Important because Singapore made wealth as middleman without producing goods.**\n\n**How Entrepôt Trade Works:**\n\n1. **Import**: Ships from different places bring goods to Singapore\n   - Tin from Malaya\n   - Spices from Indonesia\n   - Opium from India\n   - Tea from China\n   - Textiles from Britain\n\n2. **Store**: Goods kept in warehouses (godowns)\n   - Sorted by quality\n   - Repacked for different markets\n   - Waiting for right season/ships\n\n3. **Re-export**: Ships take goods to final destinations\n   - Malayan tin → Europe for canning\n   - British textiles → Southeast Asia\n   - Chinese tea → India and Europe\n\n**Why Singapore Perfect for This:**\n- Central location (hub between East and West)\n- Free port (no taxes make it cheaper than competitors)\n- Safe harbor (ships can shelter)\n- British protection (secure trade)\n\n**Value Added:**\nSingapore made money through:\n- Warehouse fees\n- Ship services (repairs, supplies)\n- Banking and insurance\n- Commission for merchants\n\n**Modern Parallel**: Singapore STILL does this - we're a logistics hub, not a manufacturing center!",
                "explanation_zh": "**答案：转口 = 进口 → 储存 → 再出口。重要因为新加坡作为中间人赚钱而不生产商品。**\n\n**转口贸易如何运作：**\n\n1. **进口**：来自不同地方的船只将货物带到新加坡\n   - 来自马来亚的锡\n   - 来自印度尼西亚的香料\n   - 来自印度的鸦片\n   - 来自中国的茶叶\n   - 来自英国的纺织品\n\n2. **储存**：货物保存在仓库中\n   - 按质量分类\n   - 为不同市场重新包装\n   - 等待合适的季节/船只\n\n3. **再出口**：船只将货物运往最终目的地\n   - 马来亚锡 → 欧洲用于罐头\n   - 英国纺织品 → 东南亚\n   - 中国茶叶 → 印度和欧洲\n\n**为什么新加坡完美：**\n- 中心位置（东西方之间的枢纽）\n- 自由港（无税使其比竞争对手便宜）\n- 安全港（船只可以避难）\n- 英国保护（安全贸易）\n\n**增值：**\n新加坡通过以下方式赚钱：\n- 仓储费\n- 船舶服务（维修、补给）\n- 银行和保险\n- 商人的佣金\n\n**现代平行**：新加坡仍然这样做 - 我们是物流枢纽，不是制造中心！"
            },
            {
                "id": "ex5-shipping-routes",
                "type": "mcq",
                "difficulty": "hard",
                "prompt": "The opening of which canal in 1869 BOOSTED Singapore's trade by shortening the Europe-Asia shipping route?",
                "prompt_zh": "1869年开通的哪条运河通过缩短欧洲-亚洲航运路线促进了新加坡的贸易？",
                "choices": ["Panama Canal", "Suez Canal", "Kra Canal", "Corinth Canal"],
                "choices_zh": ["巴拿马运河", "苏伊士运河", "克拉运河", "科林斯运河"],
                "answer": 1,
                "explanation": "**Answer: Suez Canal**\n\n**Before Suez Canal (opened 1869):**\n- Ships had to sail AROUND Africa (Cape of Good Hope)\n- Europe → Asia voyage: ~14,000 miles, 3-4 months\n- Dangerous waters, longer time = higher costs\n\n**After Suez Canal:**\n- Direct route through Mediterranean → Red Sea → Indian Ocean\n- Europe → Asia voyage: ~8,000 miles, 6-8 weeks\n- **40% shorter distance!**\n- **50% less time!**\n\n**Impact on Singapore:**\n- MORE ships passed through (shortcut made Asia more accessible)\n- FASTER trade cycles (quicker turnover = more profit)\n- Steamships replaced sailing ships (more reliable schedules)\n- Singapore's strategic value INCREASED (key point on new route)\n- Trade volume DOUBLED in 1870s\n\n**Other canals:**\n- Panama: Opened 1914 (connects Atlantic-Pacific, different route)\n- Kra: Proposed for Thailand, never built\n- Corinth: Greece, not relevant to Asia trade\n\n**National Education Link**: Just as Suez Canal boosted 19th century trade, modern maritime developments still affect Singapore's prosperity today.",
                "explanation_zh": "**答案：苏伊士运河**\n\n**苏伊士运河开通前（1869年）：**\n- 船只必须绕行非洲（好望角）\n- 欧洲 → 亚洲航程：约14,000英里，3-4个月\n- 危险水域，更长时间 = 更高成本\n\n**苏伊士运河开通后：**\n- 通过地中海 → 红海 → 印度洋的直达路线\n- 欧洲 → 亚洲航程：约8,000英里，6-8周\n- **距离缩短40%！**\n- **时间减少50%！**\n\n**对新加坡的影响：**\n- 更多船只通过（捷径使亚洲更容易到达）\n- 更快的贸易周期（更快的周转 = 更多利润）\n- 蒸汽船取代帆船（更可靠的时间表）\n- 新加坡的战略价值增加（新路线上的关键点）\n- 1870年代贸易量翻倍\n\n**其他运河：**\n- 巴拿马：1914年开通（连接大西洋-太平洋，不同路线）\n- 克拉：为泰国提议，从未建成\n- 科林斯：希腊，与亚洲贸易无关\n\n**国民教育联系**：正如苏伊士运河促进了19世纪的贸易，现代海事发展今天仍然影响新加坡的繁荣。"
            }
        ],
        "ao2": [
            {
                "id": "ex6-explain-trade-boom",
                "type": "short",
                "difficulty": "medium",
                "prompt": "Explain how Singapore's geographic location contributed to its trade success.",
                "prompt_zh": "解释新加坡的地理位置如何促进其贸易成功。",
                "answer": "Singapore sits at the southern tip of the Malacca Strait, the shortest sea route between the Indian Ocean and South China Sea. All ships traveling between India/Europe and China/East Asia had to pass near Singapore, making it the perfect collection point for regional and global trade.",
                "sampleAnswers": [
                    "Central position connecting multiple trade networks - Chinese, Indian, Southeast Asian, and European all meet at Singapore",
                    "Located at crossroads of monsoon wind patterns, ships naturally stopped to wait for favorable winds"
                ],
                "explanation": "**Sample Answer**: Singapore sits at the southern tip of Malacca Strait, the shortest route between Indian Ocean and South China Sea. All ships between India/Europe and China/East Asia passed near Singapore, making it perfect for trade collection.\n\n**Geographic Advantages:**\n\n**1. Gateway Location:**\n- **Malacca Strait** = busiest shipping lane in world\n- Connects two major economic zones:\n  - West: India, Middle East, Europe\n  - East: China, Japan, Southeast Asia\n- Singapore sits at SOUTHERN TIP (like toll booth on highway)\n\n**2. Natural Harbor:**\n- Deep water close to shore (large ships can dock)\n- Protected from storms (safe anchorage)\n- Freshwater available (Singapore River)\n- Gentle tides (easy navigation)\n\n**3. Central Hub:**\n- Equal distance to multiple important ports:\n  - Calcutta (India): 1,300 miles\n  - Canton (China): 1,500 miles\n  - Batavia (Indonesia): 500 miles\n- Perfect collection point for entrepôt trade\n\n**4. No Competition:**\n- Other Strait ports (Malacca, Penang) were:\n  - Too far north (not at tip)\n  - Or controlled by Dutch with heavy taxes\n- Singapore = best location + free port policy\n\n**Historical Parallel:**\nJust like internet traffic goes through server hubs, 19th century trade flowed through Singapore. Geography created the opportunity, but British policies made it happen.\n\n**Why This Still Matters:**\nSingapore is STILL one of world's busiest ports because geography hasn't changed - we're still at the crossroads!",
                "explanation_zh": "**示例答案**：新加坡位于马六甲海峡南端，是印度洋和南中国海之间的最短路线。所有往来于印度/欧洲和中国/东亚之间的船只都经过新加坡附近，使其成为贸易收集的完美地点。\n\n**地理优势：**\n\n**1. 门户位置：**\n- **马六甲海峡** = 世界上最繁忙的航道\n- 连接两个主要经济区：\n  - 西部：印度、中东、欧洲\n  - 东部：中国、日本、东南亚\n- 新加坡位于南端（就像高速公路上的收费站）\n\n**2. 天然港口：**\n- 靠近海岸的深水（大型船只可以停靠）\n- 免受风暴影响（安全停泊）\n- 有淡水（新加坡河）\n- 温和的潮汐（易于导航）\n\n**3. 中心枢纽：**\n- 到多个重要港口的距离相等：\n  - 加尔各答（印度）：1,300英里\n  - 广东（中国）：1,500英里\n  - 巴达维亚（印度尼西亚）：500英里\n- 转口贸易的完美收集点\n\n**4. 无竞争：**\n- 其他海峡港口（马六甲、槟城）：\n  - 太北（不在顶端）\n  - 或由荷兰控制，重税\n- 新加坡 = 最佳位置 + 自由港政策\n\n**历史平行：**\n正如互联网流量通过服务器中心，19世纪的贸易通过新加坡流动。地理创造了机会，但英国政策使其成为现实。\n\n**为什么这仍然重要：**\n新加坡仍然是世界上最繁忙的港口之一，因为地理没有改变 - 我们仍然在十字路口！"
            },
            {
                "id": "ex7-compare-raffles-successors",
                "type": "short",
                "difficulty": "hard",
                "prompt": "Compare Raffles' role in founding Singapore (1819) with the later administrators who developed it into a major port (1820s-1860s). Who contributed more to Singapore's success?",
                "prompt_zh": "比较莱佛士在建立新加坡（1819年）中的角色与后来将其发展成主要港口的管理者（1820年代-1860年代）。谁对新加坡的成功贡献更大？",
                "answer": "Both contributed differently - Raffles provided the initial vision and established the free port policy, but later administrators like John Crawfurd and others actually built the infrastructure, attracted immigrants, and managed daily governance that turned the vision into reality. Success required both founding vision and sustained implementation.",
                "sampleAnswers": [
                    "Raffles was crucial for starting Singapore and setting principles, but long-term administrators deserve credit for decades of steady development that made it prosperous",
                    "Both essential - Raffles created opportunity with free port, later leaders capitalized through good governance and infrastructure investment"
                ],
                "explanation": "**Balanced Answer**: Both contributed differently - Raffles provided vision and free port policy, but later administrators built infrastructure and managed governance that turned vision into reality. Success required both.\n\n**Raffles' Contributions (1819-1823):**\n\n**Achievements:**\n- Founded Singapore (secured treaty with Sultan)\n- Established free port policy (revolutionary idea)\n- Created Town Plan (ethnic zones, civic areas)\n- Set legal framework (British law, property rights)\n- Promoted Singapore internationally\n\n**Limitations:**\n- Only in Singapore TWICE (1819 for 8 days, 1822-1823 for 8 months)\n- Total: Less than 1 year physically present!\n- Focused on grand strategy, not daily operations\n- Left before seeing long-term results\n\n**Later Administrators (1820s-1860s):**\n\n**Key Figures:**\n- **John Crawfurd** (1823-1826): First Resident after Raffles\n- **Samuel Bonham** (1830s): Developed harbor facilities\n- **William Butterworth** (1840s-1850s): Expanded infrastructure\n- **Many others** over 40+ years\n\n**Their Contributions:**\n- Built wharves, warehouses, roads (physical infrastructure)\n- Negotiated with multiple immigrant communities\n- Handled disease outbreaks, crime, disputes\n- Maintained free port despite pressure to add taxes\n- Attracted Chinese/Indian merchants and laborers\n- Managed transition to Straits Settlements (1826)\n- Dealt with piracy, secret societies, opium trade\n\n**Comparison:**\n\n**Raffles = Architect:**\n- Drew the blueprint\n- Set foundational principles\n- Provided vision and legitimacy\n- Made bold strategic decisions\n\n**Later Administrators = Builders:**\n- Executed the plan day-by-day\n- Solved practical problems\n- Built actual infrastructure\n- Sustained policies for decades\n\n**Analytical Verdict:**\n\n**Cannot separate them** - like asking if foundation or walls more important to a building:\n- **Without Raffles**: No Singapore (Dutch would have controlled region)\n- **Without good administrators**: Singapore would have failed (many colonial outposts did)\n\n**Different Types of Leadership:**\n- **Visionary leadership** (Raffles): Sets direction, inspires, takes risks\n- **Administrative leadership** (successors): Implements, maintains, improves\n\n**Modern Parallel:**\n- Lee Kuan Yew = visionary (like Raffles)\n- But Singapore's success also depended on decades of good governance by many leaders\n- Nation-building is MARATHON, not sprint\n\n**Historical Lesson:**\nGreat achievements require BOTH:\n1. Bold vision to start something new\n2. Sustained execution to make it succeed\n\nGiving all credit to founder ignores the hard work of those who built on that foundation.\n\n**Tip**: When comparing historical figures, avoid \"either/or\" thinking. Often the answer is \"both, in different ways.\"",
                "explanation_zh": "**平衡答案**：两者的贡献不同 - 莱佛士提供了愿景和自由港政策，但后来的管理者建立了基础设施并管理治理，将愿景变为现实。成功需要两者。\n\n**莱佛士的贡献（1819-1823）：**\n\n**成就：**\n- 建立新加坡（与苏丹签订条约）\n- 建立自由港政策（革命性想法）\n- 创建城市规划（民族区、市政区）\n- 设定法律框架（英国法律、财产权）\n- 在国际上推广新加坡\n\n**局限性：**\n- 只在新加坡两次（1819年8天，1822-1823年8个月）\n- 总计：实际在场不到1年！\n- 专注于宏伟战略，不是日常运营\n- 在看到长期结果之前离开\n\n**后来的管理者（1820年代-1860年代）：**\n\n**关键人物：**\n- **约翰·克劳福德**（1823-1826）：莱佛士之后的第一任驻扎官\n- **塞缪尔·邦汉**（1830年代）：发展港口设施\n- **威廉·巴特沃思**（1840年代-1850年代）：扩大基础设施\n- **许多其他人**超过40多年\n\n**他们的贡献：**\n- 建造码头、仓库、道路（物理基础设施）\n- 与多个移民社区谈判\n- 处理疾病爆发、犯罪、纠纷\n- 维持自由港，尽管有增税压力\n- 吸引中国/印度商人和劳工\n- 管理向海峡殖民地的过渡（1826年）\n- 处理海盗、秘密社团、鸦片贸易\n\n**比较：**\n\n**莱佛士 = 建筑师：**\n- 绘制蓝图\n- 设定基本原则\n- 提供愿景和合法性\n- 做出大胆的战略决策\n\n**后来的管理者 = 建设者：**\n- 日复一日执行计划\n- 解决实际问题\n- 建造实际基础设施\n- 维持政策数十年\n\n**分析结论：**\n\n**不能分开** - 就像问地基或墙对建筑更重要：\n- **没有莱佛士**：没有新加坡（荷兰会控制该地区）\n- **没有好的管理者**：新加坡会失败（许多殖民前哨确实失败了）\n\n**不同类型的领导力：**\n- **有远见的领导力**（莱佛士）：设定方向、激励、冒险\n- **行政领导力**（继任者）：实施、维护、改进\n\n**现代平行：**\n- 李光耀 = 有远见者（像莱佛士）\n- 但新加坡的成功也依赖于许多领导人数十年的良好治理\n- 建国是马拉松，不是短跑\n\n**历史教训：**\n伟大成就需要两者：\n1. 开始新事物的大胆愿景\n2. 使其成功的持续执行\n\n把所有功劳归于创始人忽略了那些在此基础上建设的人的艰苦工作。\n\n**提示**：比较历史人物时，避免\"非此即彼\"的思维。答案通常是\"两者，以不同的方式。\""
            }
        ],
        "ao3": []
    },

    "communities-colonial-singapore": {
        "ao1": [],
        "ao2": [],
        "ao3": []
    },

    "industries-fall-singapore": {
        "ao1": [],
        "ao2": [],
        "ao3": []
    }
}

print("History Exercise Generation - Complete Edition")
print("=" * 70)
print()

# Add exercises to Chapter 2 (British Establishment)
chapter2_id = "british-establishment-trading-post"
for chapter in data['chapters']:
    if chapter['id'] == chapter2_id:
        chapter_exercises = exercises_by_chapter[chapter2_id]
        chapter['exercises'] = (
            chapter_exercises['ao1'] +
            chapter_exercises['ao2'] +
            chapter_exercises['ao3']
        )
        print(f"✓ Added {len(chapter['exercises'])} exercises to Chapter 2: {chapter['title']}")
        print(f"  - AO1 (Knowledge): {len(chapter_exercises['ao1'])} exercises")
        print(f"  - AO2 (Communication): {len(chapter_exercises['ao2'])} exercises")
        print(f"  - AO3 (Source-Based): {len(chapter_exercises['ao3'])} exercises")
        break

# Save updated chapters
output_file = 'chapters/history-sec1-chapters.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print()
print(f"✓ Saved to {output_file}")
print()
print("Status Summary:")
print("  Chapter 1 (Early Singapore): 15 exercises ✓")
print("  Chapter 2 (British Establishment): 15 exercises ✓")
print("  Chapter 3 (Port City Growth): 0 exercises (pending)")
print("  Chapter 4 (Communities): 0 exercises (pending)")
print("  Chapter 5 (Industries & Fall): 0 exercises (pending)")
print()
print("Next: Run this script again after adding exercises for Chapters 3-5")
