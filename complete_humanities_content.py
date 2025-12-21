import json

# Load existing file
with open("chapters/sec1_humanities_chapters.json", "r", encoding="utf-8") as f:
    data = json.load(f)

humanities = data["subjects"][0]

# Complete sections for Chapter 1: Understanding History
ch1_sections = [
    {
        "id": "what-is-history",
        "type": "text",
        "title": "What is History?",
        "title_zh": "什么是历史？",
        "content": """**What is History?**

History is the study of the past. It helps us understand how people lived, what they believed, and how societies changed over time.

**Why Study History?**

1. **Learn from the past**: Understanding past mistakes helps us make better decisions today
2. **Understand the present**: Many current issues have historical roots
3. **Preserve our heritage**: History keeps our cultural identity alive
4. **Develop critical thinking**: Analyzing historical evidence teaches us to question and evaluate information

**Example: Singapore's History**

Singapore's transformation from a small fishing village to a modern global city took only 200 years. By studying this journey, we understand:
- How our ancestors overcame challenges
- Why certain policies were adopted
- How different communities contributed to nation-building

**Key Terms:**
- **Primary source**: Original evidence from the time period (letters, artifacts, photos)
- **Secondary source**: Analysis written later by historians (textbooks, documentaries)
- **Perspective**: Different viewpoints on the same historical event""",
        "content_zh": """**什么是历史？**

历史是对过去的研究。它帮助我们了解人们如何生活、他们的信仰以及社会如何随时间变化。

**为什么学习历史？**

1. **从过去学习**：理解过去的错误帮助我们今天做出更好的决策
2. **理解现在**：许多当前问题都有历史根源
3. **保护我们的遗产**：历史保持我们的文化认同
4. **培养批判性思维**：分析历史证据教会我们质疑和评估信息

**例子：新加坡的历史**

新加坡从一个小渔村转变为现代化全球城市仅用了200年。通过研究这段旅程，我们理解：
- 我们的祖先如何克服挑战
- 为什么采取某些政策
- 不同社区如何为建国做出贡献

**关键术语：**
- **第一手资料**：来自该时期的原始证据（信件、文物、照片）
- **第二手资料**：历史学家后来撰写的分析（教科书、纪录片）
- **观点**：对同一历史事件的不同看法"""
    },
    {
        "id": "historical-sources",
        "type": "text",
        "title": "Historical Sources and Evidence",
        "title_zh": "历史资料和证据",
        "content": """**Types of Historical Sources**

**Primary Sources** (First-hand evidence):
- **Written records**: Diaries, letters, official documents, newspapers
- **Visual sources**: Photographs, paintings, posters, maps
- **Physical artifacts**: Tools, pottery, buildings, coins
- **Oral testimony**: Interviews with people who experienced events

**Secondary Sources** (Second-hand analysis):
- History textbooks
- Documentary films
- Biographies written by historians
- Museum exhibitions

**Evaluating Sources**

When analyzing historical sources, ask:

1. **Who created it?** (Author's background and bias)
2. **When was it created?** (Time period and context)
3. **Why was it created?** (Purpose: inform, persuade, entertain?)
4. **Is it reliable?** (Cross-check with other sources)

**Example: Raffles' Founding of Singapore**

Different sources tell different stories:
- **British records** emphasize Raffles' vision and leadership
- **Malay chronicles** highlight the Sultan's role and local context
- **Chinese accounts** focus on immigrant experiences

Historians must consider ALL perspectives to get the complete picture.

**Singapore Example: Oral History Centre**

The National Archives of Singapore has recorded over 4,000 oral history interviews. These first-hand accounts from pioneers, war survivors, and everyday Singaporeans provide invaluable insights into our nation's development.""",
        "content_zh": """**历史资料的类型**

**第一手资料**（直接证据）：
- **书面记录**：日记、信件、官方文件、报纸
- **视觉资料**：照片、绘画、海报、地图
- **实物文物**：工具、陶器、建筑物、硬币
- **口述证词**：对经历事件的人的采访

**第二手资料**（间接分析）：
- 历史教科书
- 纪录片
- 历史学家撰写的传记
- 博物馆展览

**评估资料**

分析历史资料时，要问：

1. **谁创建的？**（作者的背景和偏见）
2. **何时创建？**（时期和背景）
3. **为何创建？**（目的：告知、说服、娱乐？）
4. **可靠吗？**（与其他资料交叉核对）

**例子：莱佛士建立新加坡**

不同资料讲述不同故事：
- **英国记录**强调莱佛士的远见和领导力
- **马来编年史**突出苏丹的角色和当地背景
- **中国记录**关注移民经历

历史学家必须考虑所有观点才能得到完整的画面。

**新加坡例子：口述历史中心**

新加坡国家档案馆已记录超过4,000个口述历史访谈。这些来自先驱者、战争幸存者和普通新加坡人的第一手资料为我们国家的发展提供了宝贵的见解。"""
    },
    {
        "id": "multiple-perspectives",
        "type": "text",
        "title": "Multiple Perspectives in History",
        "title_zh": "历史中的多重观点",
        "content": """**Why Different Perspectives Matter**

The same historical event can be viewed differently depending on:
- **Nationality**: British vs. local perspectives on colonialism
- **Social class**: Elite vs. common people's experiences
- **Gender**: Men's vs. women's roles in society
- **Time period**: How views change over generations

**Example: Japanese Occupation of Singapore (1942-1945)**

**Perspective 1: British Military**
- Focus on military defeat and strategic failures
- Emphasis on eventually reclaiming the colony

**Perspective 2: Local Chinese Community**
- Experienced Sook Ching massacre and persecution
- Remembers suffering and resistance efforts

**Perspective 3: Local Malay Community**
- Different treatment under Japanese rule
- Some administrative cooperation

**Perspective 4: Local Indian Community**
- Indian National Army formation
- Complex feelings about Japanese promises of Indian independence

**Learning from Multiple Perspectives**

Understanding different viewpoints helps us:
1. Develop empathy and tolerance
2. Avoid oversimplified narratives
3. Make balanced judgments
4. Appreciate Singapore's multicultural society

**Activity: Fort Canning Excavations**

Archaeological digs at Fort Canning Hill have uncovered:
- 14th-century Majapahit artifacts (pre-colonial Singapore)
- British colonial-era structures
- Japanese military fortifications

Each layer tells a different story of Singapore's past, showing how our island has been home to many cultures throughout history.""",
        "content_zh": """**为什么不同观点很重要**

同一历史事件可以根据以下因素有不同看法：
- **国籍**：英国vs.当地对殖民主义的看法
- **社会阶层**：精英vs.普通人的经历
- **性别**：男性vs.女性在社会中的角色
- **时期**：观点如何随代际变化

**例子：日本占领新加坡（1942-1945）**

**观点1：英国军方**
- 关注军事失败和战略失误
- 强调最终收复殖民地

**观点2：本地华人社区**
- 经历了肃清大屠杀和迫害
- 记住苦难和抵抗努力

**观点3：本地马来社区**
- 在日本统治下受到不同对待
- 一些行政合作

**观点4：本地印度社区**
- 印度国民军的成立
- 对日本承诺印度独立的复杂感受

**从多重观点学习**

理解不同观点帮助我们：
1. 培养同理心和宽容
2. 避免过于简化的叙述
3. 做出平衡的判断
4. 欣赏新加坡的多元文化社会

**活动：福康宁山发掘**

福康宁山的考古挖掘发现了：
- 14世纪满者伯夷文物（殖民前新加坡）
- 英国殖民时期建筑
- 日本军事工事

每一层都讲述了新加坡过去的不同故事，展示了我们的岛屿在历史上如何成为许多文化的家园。"""
    }
]

humanities["chapters"][0]["sections"] = ch1_sections

print("✅ Completed Chapter 1: Understanding History (3 sections)")
print("   Now creating sections for remaining chapters...")

# Save after each chapter to avoid losing progress
with open("chapters/sec1_humanities_chapters.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
