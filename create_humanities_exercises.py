import json

# Load the chapters
with open("chapters/sec1_humanities_chapters.json", "r", encoding="utf-8") as f:
    data = json.load(f)

humanities = data["subjects"][0]

# CHAPTER 1: Understanding History - Exercises
ch1_exercises = [
    {
        "id": "hist1-ex1",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "What is history?",
        "prompt_zh": "什么是历史？",
        "choices": [
            "The study of the past",
            "The study of mathematics",
            "The study of languages",
            "The study of future predictions"
        ],
        "choices_zh": [
            "对过去的研究",
            "对数学的研究",
            "对语言的研究",
            "对未来预测的研究"
        ],
        "answer": 0,
        "explanation": "History is the study of the past, helping us understand how people lived, what they believed, and how societies changed over time.",
        "explanation_zh": "历史是对过去的研究，帮助我们了解人们如何生活、他们的信仰以及社会如何随时间变化。"
    },
    {
        "id": "hist1-ex2",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "Which of the following is a PRIMARY source?",
        "prompt_zh": "以下哪项是第一手资料？",
        "choices": [
            "A diary written during World War II",
            "A history textbook about World War II",
            "A documentary film about World War II",
            "A museum exhibition about World War II"
        ],
        "choices_zh": [
            "二战期间写的日记",
            "关于二战的历史教科书",
            "关于二战的纪录片",
            "关于二战的博物馆展览"
        ],
        "answer": 0,
        "explanation": "A diary written during World War II is a primary source because it was created at the time by someone who experienced the events first-hand.",
        "explanation_zh": "二战期间写的日记是第一手资料，因为它是由经历事件的人在当时创建的。"
    },
    {
        "id": "hist1-ex3",
        "type": "mcq",
        "difficulty": "medium",
        "prompt": "Why do historians study multiple perspectives of the same historical event?",
        "prompt_zh": "为什么历史学家要研究同一历史事件的多种观点？",
        "choices": [
            "To get a more complete and balanced understanding",
            "Because they cannot find enough sources",
            "To make history more complicated",
            "To prove one side is always wrong"
        ],
        "choices_zh": [
            "为了获得更完整和平衡的理解",
            "因为他们找不到足够的资料",
            "为了让历史更复杂",
            "为了证明一方总是错的"
        ],
        "answer": 0,
        "explanation": "Historians study multiple perspectives to avoid oversimplified narratives and gain a complete, balanced understanding of historical events.",
        "explanation_zh": "历史学家研究多种观点以避免过于简化的叙述，并获得对历史事件的完整、平衡的理解。"
    },
    {
        "id": "hist1-ex4",
        "type": "short",
        "difficulty": "medium",
        "prompt": "What is the difference between a primary source and a secondary source?",
        "prompt_zh": "第一手资料和第二手资料有什么区别？",
        "answer": "Primary sources are original evidence from the time period, while secondary sources are analyses written later by historians",
        "answer_zh": "第一手资料是来自该时期的原始证据，而第二手资料是历史学家后来撰写的分析",
        "validator": "smart",
        "explanation": "Primary sources (letters, artifacts, photos) are first-hand evidence, while secondary sources (textbooks, documentaries) are interpretations created after the fact.",
        "explanation_zh": "第一手资料（信件、文物、照片）是直接证据，而第二手资料（教科书、纪录片）是事后创建的解释。"
    },
    {
        "id": "hist1-ex5",
        "type": "mcq",
        "difficulty": "hard",
        "prompt": "During the Japanese Occupation of Singapore (1942-1945), different communities had different experiences. Why is it important to understand ALL these perspectives?",
        "prompt_zh": "在日本占领新加坡期间（1942-1945），不同社区有不同的经历。为什么理解所有这些观点很重要？",
        "choices": [
            "It helps us develop empathy and appreciate Singapore's multicultural society",
            "It makes the story longer and more interesting",
            "It proves one community suffered more than others",
            "It is required by the textbook"
        ],
        "choices_zh": [
            "它帮助我们培养同理心并欣赏新加坡的多元文化社会",
            "它使故事更长更有趣",
            "它证明一个社区比其他社区受苦更多",
            "这是教科书的要求"
        ],
        "answer": 0,
        "explanation": "Understanding multiple perspectives helps us develop empathy, make balanced judgments, and appreciate Singapore's diverse multicultural heritage.",
        "explanation_zh": "理解多种观点帮助我们培养同理心，做出平衡的判断，并欣赏新加坡多元的多元文化遗产。"
    }
]

# Add more exercises for Chapter 1 (total 15)
ch1_exercises.extend([
    {
        "id": "hist1-ex6",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "What does the Singapore Oral History Centre collect?",
        "prompt_zh": "新加坡口述历史中心收集什么？",
        "choices": [
            "First-hand accounts from Singaporeans",
            "Ancient artifacts",
            "Old buildings",
            "Foreign documents"
        ],
        "choices_zh": [
            "新加坡人的第一手资料",
            "古代文物",
            "旧建筑",
            "外国文件"
        ],
        "answer": 0,
        "explanation": "The Oral History Centre has recorded over 4,000 interviews with pioneers, war survivors, and everyday Singaporeans.",
        "explanation_zh": "口述历史中心已记录超过4,000个与先驱者、战争幸存者和普通新加坡人的访谈。"
    },
    {
        "id": "hist1-ex7",
        "type": "short",
        "difficulty": "medium",
        "prompt": "Give an example of how studying history helps us make better decisions today.",
        "prompt_zh": "举例说明学习历史如何帮助我们今天做出更好的决策。",
        "answer": "Learning from past mistakes",
        "answer_zh": "从过去的错误中学习",
        "validator": "smart",
        "explanation": "By understanding past mistakes and successes, we can make more informed decisions and avoid repeating errors.",
        "explanation_zh": "通过理解过去的错误和成功，我们可以做出更明智的决策并避免重复错误。"
    },
    {
        "id": "hist1-ex8",
        "type": "mcq",
        "difficulty": "medium",
        "prompt": "When evaluating a historical source, which question should you ask?",
        "prompt_zh": "评估历史资料时，你应该问哪个问题？",
        "choices": [
            "All of the above",
            "Who created it?",
            "When was it created?",
            "Why was it created?"
        ],
        "choices_zh": [
            "以上所有",
            "谁创建的？",
            "何时创建？",
            "为何创建？"
        ],
        "answer": 0,
        "explanation": "When evaluating sources, historians ask: who, when, why, and whether it is reliable by cross-checking with other sources.",
        "explanation_zh": "评估资料时，历史学家会问：谁、何时、为何，以及通过与其他资料交叉核对是否可靠。"
    },
    {
        "id": "hist1-ex9",
        "type": "mcq",
        "difficulty": "hard",
        "prompt": "Different accounts of Raffles' founding of Singapore emphasize different aspects. Which is the BEST approach for historians?",
        "prompt_zh": "关于莱佛士建立新加坡的不同记载强调不同方面。哪种是历史学家的最佳方法？",
        "choices": [
            "Consider all perspectives to get the complete picture",
            "Only trust British records",
            "Only trust local chronicles",
            "Ignore contradictory accounts"
        ],
        "choices_zh": [
            "考虑所有观点以获得完整画面",
            "只信任英国记录",
            "只信任当地编年史",
            "忽略矛盾的记载"
        ],
        "answer": 0,
        "explanation": "Historians must consider all perspectives (British, Malay, Chinese accounts) to understand the full story of Singapore's founding.",
        "explanation_zh": "历史学家必须考虑所有观点（英国、马来、中国记载）以理解新加坡建国的完整故事。"
    },
    {
        "id": "hist1-ex10",
        "type": "short",
        "difficulty": "easy",
        "prompt": "Name one type of visual historical source.",
        "prompt_zh": "说出一种视觉历史资料。",
        "answer": "photograph",
        "answer_zh": "照片",
        "validator": "smart",
        "explanation": "Visual sources include photographs, paintings, posters, and maps that provide evidence about the past.",
        "explanation_zh": "视觉资料包括照片、绘画、海报和地图，它们提供关于过去的证据。"
    },
    {
        "id": "hist1-ex11",
        "type": "drag-order",
        "difficulty": "medium",
        "prompt": "Arrange the steps for analyzing a historical source in order:",
        "prompt_zh": "按顺序排列分析历史资料的步骤：",
        "items": [
            "Who created it?",
            "When was it created?",
            "Why was it created?",
            "Is it reliable?"
        ],
        "items_zh": [
            "谁创建的？",
            "何时创建？",
            "为何创建？",
            "可靠吗？"
        ],
        "answer": [
            "Who created it?",
            "When was it created?",
            "Why was it created?",
            "Is it reliable?"
        ],
        "explanation": "When analyzing sources, historians first identify who and when, then understand why it was created, and finally evaluate its reliability.",
        "explanation_zh": "分析资料时，历史学家首先确定谁和何时，然后理解为何创建，最后评估其可靠性。"
    },
    {
        "id": "hist1-ex12",
        "type": "mcq",
        "difficulty": "medium",
        "prompt": "Fort Canning archaeological excavations found artifacts from different time periods. What does this show?",
        "prompt_zh": "福康宁考古挖掘发现了不同时期的文物。这说明什么？",
        "choices": [
            "Singapore has been home to many cultures throughout history",
            "The site was only used during colonial times",
            "Ancient artifacts are not valuable",
            "Only British artifacts are found there"
        ],
        "choices_zh": [
            "新加坡在历史上一直是许多文化的家园",
            "该遗址仅在殖民时期使用",
            "古代文物没有价值",
            "那里只发现英国文物"
        ],
        "answer": 0,
        "explanation": "Fort Canning excavations uncovered 14th-century Majapahit artifacts, British colonial structures, and Japanese fortifications, showing Singapore's multicultural past.",
        "explanation_zh": "福康宁挖掘发现了14世纪满者伯夷文物、英国殖民建筑和日本工事，显示了新加坡的多元文化过去。"
    },
    {
        "id": "hist1-ex13",
        "type": "short",
        "difficulty": "hard",
        "prompt": "Why is it important to cross-check historical sources?",
        "prompt_zh": "为什么交叉核对历史资料很重要？",
        "answer": "to verify reliability and accuracy",
        "answer_zh": "验证可靠性和准确性",
        "validator": "smart",
        "explanation": "Cross-checking sources helps historians verify information, detect bias, and ensure accuracy before drawing conclusions.",
        "explanation_zh": "交叉核对资料帮助历史学家验证信息、检测偏见并在得出结论前确保准确性。"
    },
    {
        "id": "hist1-ex14",
        "type": "mcq",
        "difficulty": "easy",
        "prompt": "Which is an example of a secondary source?",
        "prompt_zh": "哪个是第二手资料的例子？",
        "choices": [
            "A history textbook",
            "A soldier's letter from war",
            "An ancient coin",
            "A newspaper from 1945"
        ],
        "choices_zh": [
            "历史教科书",
            "士兵的战争信件",
            "古代硬币",
            "1945年的报纸"
        ],
        "answer": 0,
        "explanation": "A history textbook is a secondary source because it is written later by historians who analyze primary sources.",
        "explanation_zh": "历史教科书是第二手资料，因为它是由历史学家后来分析第一手资料撰写的。"
    },
    {
        "id": "hist1-ex15",
        "type": "mcq",
        "difficulty": "hard",
        "prompt": "If you find contradictory information in two historical sources about the same event, what should you do?",
        "prompt_zh": "如果你在两个关于同一事件的历史资料中发现矛盾信息，你应该怎么做？",
        "choices": [
            "Investigate both sources, check their reliability, and seek additional sources",
            "Always believe the older source",
            "Always believe the newer source",
            "Ignore both sources"
        ],
        "choices_zh": [
            "调查两个资料，检查其可靠性，并寻找其他资料",
            "总是相信较旧的资料",
            "总是相信较新的资料",
            "忽略两个资料"
        ],
        "answer": 0,
        "explanation": "When sources contradict, historians investigate both, evaluate their reliability, and look for additional sources to clarify the truth.",
        "explanation_zh": "当资料矛盾时，历史学家会调查两者，评估其可靠性，并寻找其他资料来澄清真相。"
    }
])

# Add exercises to Chapter 1
humanities["chapters"][0]["exercises"] = ch1_exercises

print(f"✅ Created {len(ch1_exercises)} exercises for Chapter 1: Understanding History")

# Save updated file
with open("chapters/sec1_humanities_chapters.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Saved to chapters/sec1_humanities_chapters.json")
