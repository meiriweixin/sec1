import json

# Load file
with open("chapters/sec1_humanities_chapters.json", "r", encoding="utf-8") as f:
    data = json.load(f)

humanities = data["subjects"][0]

# The first file (create_sec1_humanities.py) already has the full content for Chapter 2
# Let me load that original comprehensive content

# CHAPTER 2: Early Southeast Asia - Full sections from original design
ch2_sections = [
    {
        "id": "ancient-kingdoms",
        "type": "text",
        "title": "Ancient Kingdoms of Southeast Asia",
        "title_zh": "东南亚的古代王国",
        "content": """**Major Early Kingdoms (300-1500 CE)**

**1. Srivijaya Empire (7th-13th century)**
- **Location**: Sumatra (modern-day Indonesia)
- **Power**: Controlled the Straits of Malacca
- **Economy**: Maritime trade and piracy control
- **Religion**: Mahayana Buddhism
- **Legacy**: Influenced Malay language and culture

**2. Majapahit Empire (13th-16th century)**
- **Location**: Java (modern-day Indonesia)
- **Peak**: 1350 CE under King Hayam Wuruk
- **Territory**: Controlled much of maritime Southeast Asia including early Singapore (Temasek)
- **Religion**: Hinduism-Buddhism blend
- **Evidence**: Archaeological findings at Fort Canning Hill in Singapore

**3. Angkor Empire (9th-15th century)**
- **Location**: Cambodia
- **Famous site**: Angkor Wat temple complex
- **Achievement**: Advanced irrigation and engineering
- **Religion**: Hinduism, later Buddhism

**Connection to Singapore**

Singapore (known as **Temasek** in ancient times) was:
- A minor trading outpost under Srivijaya influence
- Later part of the Majapahit trading network
- Mentioned in Chinese texts as early as 3rd century CE
- Named 'Singapura' (Lion City) around 1299 CE by a Srivijayan prince

**Archaeological Evidence**

Excavations at Fort Canning and Empress Place have found:
- Chinese ceramics from Song and Yuan dynasties
- Indian glass beads
- Javanese goldwork
- Evidence of a 14th-century settlement""",
        "content_zh": """**主要早期王国（公元300-1500年）**

**1. 室利佛逝帝国（7-13世纪）**
- **地点**：苏门答腊（今印度尼西亚）
- **权力**：控制马六甲海峡
- **经济**：海上贸易和海盗控制
- **宗教**：大乘佛教
- **遗产**：影响马来语言和文化

**2. 满者伯夷帝国（13-16世纪）**
- **地点**：爪哇（今印度尼西亚）
- **巅峰**：1350年在哈亚姆·乌鲁克国王统治下
- **领土**：控制大部分海洋东南亚，包括早期新加坡（淡马锡）
- **宗教**：印度教-佛教融合
- **证据**：新加坡福康宁山的考古发现

**3. 吴哥帝国（9-15世纪）**
- **地点**：柬埔寨
- **著名遗址**：吴哥窟寺庙群
- **成就**：先进的灌溉和工程
- **宗教**：印度教，后来是佛教

**与新加坡的联系**

新加坡（古代称为**淡马锡**）是：
- 室利佛逝影响下的小型贸易站
- 后来成为满者伯夷贸易网络的一部分
- 中国文献早在公元3世纪就提到
- 约1299年被室利佛逝王子命名为"狮城"

**考古证据**

福康宁和皇后坊的挖掘发现了：
- 宋朝和元朝的中国陶瓷
- 印度玻璃珠
- 爪哇金工艺品
- 14世纪定居点的证据"""
    },
    {
        "id": "maritime-trade",
        "type": "text",
        "title": "Maritime Trade Routes",
        "title_zh": "海上贸易路线",
        "content": """**The Ancient Maritime Silk Road**

**What was traded?**

**From China:**
- Silk fabrics
- Porcelain and ceramics
- Tea
- Paper

**From India:**
- Cotton textiles
- Spices (pepper, cardamom)
- Precious stones
- Religious texts

**From Southeast Asia:**
- Spices (cloves, nutmeg from Moluccas)
- Aromatic woods
- Gold and tin
- Forest products (camphor, resins)

**From Middle East/Arabia:**
- Frankincense and myrrh
- Glassware
- Carpets
- Horses

**Key Trade Routes**

1. **Southern Route**: China → Vietnam → Malacca Straits → India → Middle East
2. **Northern Route**: China → Philippines → Borneo → Java → India

**Strategic Importance of Singapore/Temasek**

- Located at the southern tip of the Malay Peninsula
- Natural harbor for monsoon-dependent ships
- Controlled access between Indian Ocean and South China Sea
- Provided fresh water and supplies for traders

**Monsoon Winds**

Traders relied on predictable monsoon patterns:
- **Northeast monsoon** (November-March): Ships sailed from China to Southeast Asia
- **Southwest monsoon** (May-September): Return journey from Southeast Asia to China
- Ships would wait months in ports like Temasek for wind changes

**Cultural Exchange**

Trade brought more than goods:
- **Religion**: Buddhism and Hinduism from India
- **Language**: Sanskrit words in Malay
- **Architecture**: Temple designs
- **Technology**: Shipbuilding techniques, navigation tools

**Singapore's Modern Legacy**

Today, Singapore remains one of the world's busiest ports, continuing its ancient role as a trading hub. The Port of Singapore handles over 37 million containers annually, making it the second-busiest container port globally.""",
        "content_zh": """**古代海上丝绸之路**

**交易什么？**

**来自中国：**
- 丝绸织物
- 瓷器和陶瓷
- 茶
- 纸

**来自印度：**
- 棉织品
- 香料（胡椒、豆蔻）
- 宝石
- 宗教文献

**来自东南亚：**
- 香料（来自摩鹿加群岛的丁香、肉豆蔻）
- 芳香木材
- 黄金和锡
- 森林产品（樟脑、树脂）

**来自中东/阿拉伯：**
- 乳香和没药
- 玻璃器皿
- 地毯
- 马匹

**主要贸易路线**

1. **南线**：中国 → 越南 → 马六甲海峡 → 印度 → 中东
2. **北线**：中国 → 菲律宾 → 婆罗洲 → 爪哇 → 印度

**新加坡/淡马锡的战略重要性**

- 位于马来半岛南端
- 依赖季风的船只的天然港口
- 控制印度洋和南中国海之间的通道
- 为贸易商提供淡水和补给

**季风**

贸易商依赖可预测的季风模式：
- **东北季风**（11月-3月）：船只从中国航行到东南亚
- **西南季风**（5月-9月）：从东南亚返回中国
- 船只会在淡马锡等港口等待数月以等待风向变化

**文化交流**

贸易带来的不仅是商品：
- **宗教**：来自印度的佛教和印度教
- **语言**：马来语中的梵语词汇
- **建筑**：寺庙设计
- **技术**：造船技术、导航工具

**新加坡的现代遗产**

今天，新加坡仍然是世界上最繁忙的港口之一，延续其作为贸易枢纽的古老角色。新加坡港每年处理超过3700万个集装箱，使其成为全球第二繁忙的集装箱港口。"""
    },
    {
        "id": "cultural-influences",
        "type": "text",
        "title": "Indian and Chinese Influences",
        "title_zh": "印度和中国的影响",
        "content": """**Indian Cultural Influence (Indianization)**

**Religion and Philosophy:**
- Hinduism and Buddhism spread through trade and missionary activity
- Sanskrit became the language of religion and scholarship
- Concept of divine kingship (god-kings)

**Architecture:**
- Temple construction techniques
- Use of stone monuments
- Borobudur (Java) and Angkor Wat (Cambodia) show Indian influence

**Literature and Arts:**
- Indian epics (Ramayana, Mahabharata) adapted locally
- Sanskrit writing system influenced local scripts
- Classical dance forms

**Political Systems:**
- Concepts of kingship and statecraft
- Administrative organization
- Legal codes based on Indian models

**Chinese Cultural Influence (Sinicization)**

**Trade and Economics:**
- Chinese merchants established communities in port cities
- Introduction of Chinese coinage systems
- Ceramic technology and production

**Technology:**
- Shipbuilding techniques (junk ships)
- Navigation tools (compass)
- Agricultural methods (wet rice cultivation)

**Philosophy and Governance:**
- Confucian values in some kingdoms
- Tributary system (smaller kingdoms paid tribute to Chinese emperors)
- Civil service examination concepts

**Cultural Artifacts:**
- Chinese ceramics highly valued
- Porcelain used as status symbols
- Chinese motifs in local art

**Synthesis in Southeast Asia**

Southeast Asian societies didn't simply copy Indian or Chinese culture. Instead, they created unique blends:

**Example: Javanese Wayang Kulit (Shadow Puppets)**
- Uses Indian epic stories (Ramayana)
- But adapted with local characters and humor
- Performance style unique to Java
- Shows selective adoption and creative adaptation

**Singapore's Multicultural Heritage**

This ancient pattern of cultural blending continues today:
- **Little India**: Hindu temples, Indian cuisine, traditional music
- **Chinatown**: Chinese temples, clan associations, TCM shops
- **Kampong Glam**: Malay-Muslim culture, Sultan Mosque
- All coexisting in one small island, just like ancient trading ports

**Archaeological Evidence in Singapore**

Findings at Fort Canning show cultural mixing:
- Gold ornaments with Hindu-Buddhist motifs
- Chinese ceramics for daily use
- Islamic gravestones from 14th century
- Shows Singapore was always a multicultural crossroads""",
        "content_zh": """**印度文化影响（印度化）**

**宗教和哲学：**
- 印度教和佛教通过贸易和传教活动传播
- 梵语成为宗教和学术语言
- 神圣王权概念（神王）

**建筑：**
- 寺庙建筑技术
- 石碑的使用
- 婆罗浮屠（爪哇）和吴哥窟（柬埔寨）显示印度影响

**文学和艺术：**
- 印度史诗（罗摩衍那、摩诃婆罗多）的本地改编
- 梵文书写系统影响本地文字
- 古典舞蹈形式

**政治制度：**
- 王权和治国理念
- 行政组织
- 基于印度模式的法律法规

**中国文化影响（中国化）**

**贸易和经济：**
- 中国商人在港口城市建立社区
- 引入中国货币系统
- 陶瓷技术和生产

**技术：**
- 造船技术（帆船）
- 导航工具（指南针）
- 农业方法（水稻种植）

**哲学和治理：**
- 一些王国的儒家价值观
- 朝贡制度（较小王国向中国皇帝进贡）
- 科举考试概念

**文化文物：**
- 中国陶瓷高度重视
- 瓷器用作身份象征
- 本地艺术中的中国图案

**东南亚的综合**

东南亚社会不是简单地复制印度或中国文化。相反，他们创造了独特的融合：

**例子：爪哇皮影戏**
- 使用印度史诗故事（罗摩衍那）
- 但加入本地角色和幽默进行改编
- 爪哇独特的表演风格
- 显示选择性采用和创造性改编

**新加坡的多元文化遗产**

这种古老的文化融合模式今天仍在继续：
- **小印度**：印度庙宇、印度美食、传统音乐
- **牛车水**：中国庙宇、宗乡会馆、中药店
- **甘榜格南**：马来-穆斯林文化、苏丹回教堂
- 所有这些都共存于一个小岛上，就像古代贸易港口

**新加坡的考古证据**

福康宁的发现显示文化融合：
- 带有印度教-佛教图案的金饰品
- 日常使用的中国陶瓷
- 14世纪的伊斯兰墓碑
- 显示新加坡一直是多元文化的十字路口"""
    }
]

humanities["chapters"][1]["sections"] = ch2_sections
print("✅ Completed Chapter 2: Early Southeast Asia (3 sections)")

# Save progress
with open("chapters/sec1_humanities_chapters.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved progress. Now adding Chapter 3 and 4 sections...")
