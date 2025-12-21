import json

# Create Humanities subject with chapters
humanities_subject = {
    "id": "humanities",
    "title": "Humanities",
    "title_zh": "人文",
    "description": "History and Geography for Secondary 1",
    "description_zh": "中一历史与地理",
    "color": "from-amber-500 to-orange-600",
    "chapters": []
}

# Chapter 1: Understanding History
ch1 = {
    "id": "understanding-history",
    "title": "Understanding History",
    "title_zh": "理解历史",
    "gradeLevel": "sec1",
    "tag": "History",
    "tag_zh": "历史",
    "description": "What is history and how do historians work?",
    "description_zh": "什么是历史？历史学家如何工作？",
    "objectives": [
        "Understand what history is and why it matters",
        "Learn about historical sources and evidence",
        "Develop skills in analyzing historical perspectives"
    ],
    "objectives_zh": [
        "理解什么是历史及其重要性",
        "学习历史资料和证据",
        "培养分析历史观点的技能"
    ],
    "sections": [],
    "exercises": []
}

# Add sections to Chapter 1
ch1["sections"] = [
    {
        "id": "what-is-history",
        "type": "text",
        "title": "What is History?",
        "title_zh": "什么是历史？",
        "content": "History is the study of the past. It helps us understand how people lived, what they believed, and how societies changed over time.\n\nLearn from the past, understand the present, and preserve our heritage.",
        "content_zh": "历史是对过去的研究。它帮助我们了解人们如何生活、他们的信仰以及社会如何随时间变化。\n\n从过去学习，理解现在，保护我们的遗产。"
    }
]

# Chapter 2: Early Southeast Asia
ch2 = {
    "id": "early-southeast-asia",
    "title": "Early Southeast Asia",
    "title_zh": "早期东南亚",
    "gradeLevel": "sec1",
    "tag": "History",
    "tag_zh": "历史",
    "description": "Ancient civilizations and trade in Southeast Asia",
    "description_zh": "东南亚的古代文明和贸易",
    "objectives": [
        "Understand early Southeast Asian kingdoms",
        "Learn about maritime trade routes",
        "Explore cultural influences from India and China"
    ],
    "objectives_zh": [
        "了解早期东南亚王国",
        "学习海上贸易路线",
        "探索来自印度和中国的文化影响"
    ],
    "sections": [],
    "exercises": []
}

# Chapter 3: Physical Geography
ch3 = {
    "id": "physical-geography",
    "title": "Introduction to Physical Geography",
    "title_zh": "自然地理导论",
    "gradeLevel": "sec1",
    "tag": "Geography",
    "tag_zh": "地理",
    "description": "Understanding Earth's physical features and processes",
    "description_zh": "了解地球的自然特征和过程",
    "objectives": [
        "Learn about Earth's structure and landforms",
        "Understand weather and climate patterns",
        "Explore natural resources and ecosystems"
    ],
    "objectives_zh": [
        "了解地球结构和地貌",
        "理解天气和气候模式",
        "探索自然资源和生态系统"
    ],
    "sections": [],
    "exercises": []
}

# Chapter 4: Map Skills
ch4 = {
    "id": "map-skills",
    "title": "Map Reading and Geographic Skills",
    "title_zh": "地图阅读和地理技能",
    "gradeLevel": "sec1",
    "tag": "Geography",
    "tag_zh": "地理",
    "description": "Learn to read maps, use coordinates, and understand scale",
    "description_zh": "学习阅读地图、使用坐标和理解比例尺",
    "objectives": [
        "Read and interpret different types of maps",
        "Use latitude and longitude coordinates",
        "Calculate distance using map scale",
        "Understand map symbols and legends"
    ],
    "objectives_zh": [
        "阅读和解释不同类型的地图",
        "使用经纬度坐标",
        "使用地图比例尺计算距离",
        "理解地图符号和图例"
    ],
    "sections": [],
    "exercises": []
}

# Add chapters to subject
humanities_subject["chapters"] = [ch1, ch2, ch3, ch4]

# Save to file
output = {"subjects": [humanities_subject]}
with open("chapters/sec1_humanities_chapters.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"✅ Created Sec 1 Humanities with {len(humanities_subject['chapters'])} chapters")
for ch in humanities_subject["chapters"]:
    print(f"  - {ch['title']} ({ch['tag']})")
