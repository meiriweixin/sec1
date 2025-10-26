import json

# Load current content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find Chinese subject and Composition Writing chapter
for subject in data['subjects']:
    if subject['id'] == 'chinese':
        for chapter in subject['chapters']:
            if chapter['id'] == 'chinese-composition-writing':
                # Add 14 new exercises
                new_exercises = [
                    {
                        "id": "comp-ex2",
                        "type": "mcq",
                        "difficulty": "easy",
                        "prompt": "Which is the best opening sentence for a narrative essay?",
                        "prompt_zh": "哪个是记叙文最好的开头句？",
                        "choices": [
                            "This is a story.",
                            "I will tell you about my day.",
                            "The sun was setting over Marina Bay as I stepped off the MRT.",
                            "Let me begin."
                        ],
                        "choices_zh": [
                            "这是一个故事。",
                            "我会告诉你我的一天。",
                            "当我走出地铁站时，太阳正在滨海湾落下。",
                            "让我开始吧。"
                        ],
                        "answer": 2,
                        "explanation": "A good opening sets the scene and captures attention with vivid details.",
                        "explanation_zh": "好的开头要设定场景，用生动的细节吸引注意力。"
                    },
                    {
                        "id": "comp-ex3",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "What is the 5W1H method for planning essays?",
                        "prompt_zh": "写作规划的5W1H方法是什么？",
                        "choices": [
                            "Who, Where, Why, When, What, How",
                            "Writing, Words, Wonder, Wisdom, Work, Help",
                            "Week, Weather, Water, Wind, Wood, House",
                            "Want, Will, Would, Was, Were, Has"
                        ],
                        "choices_zh": [
                            "谁、哪里、为什么、何时、什么、如何",
                            "写作、词语、惊奇、智慧、工作、帮助",
                            "周、天气、水、风、木、房子",
                            "想要、将要、会、是、曾经、有"
                        ],
                        "answer": 0,
                        "explanation": "5W1H stands for: Who, What, When, Where, Why, How - key elements for planning.",
                        "explanation_zh": "5W1H代表：谁、什么、何时、哪里、为什么、如何——计划的关键要素。"
                    },
                    {
                        "id": "comp-ex4",
                        "type": "drag-order",
                        "difficulty": "medium",
                        "prompt": "Arrange these narrative essay elements in typical order:",
                        "prompt_zh": "按典型顺序排列这些记叙文要素：",
                        "items": ["开头", "起因", "经过", "高潮", "结尾"],
                        "items_zh": ["开头", "起因", "经过", "高潮", "结尾"],
                        "answer": ["开头", "起因", "经过", "高潮", "结尾"],
                        "explanation": "Typical narrative structure: Introduction, Rising Action, Development, Climax, Ending.",
                        "explanation_zh": "典型的记叙文结构：开头、起因、经过、高潮、结尾。"
                    },
                    {
                        "id": "comp-ex5",
                        "type": "mcq",
                        "difficulty": "easy",
                        "prompt": "Which descriptive technique is most effective?",
                        "prompt_zh": "哪种描写技巧最有效？",
                        "choices": [
                            "He was happy.",
                            "He smiled broadly, his eyes sparkling with joy.",
                            "He felt good.",
                            "He was in a good mood."
                        ],
                        "choices_zh": [
                            "他很高兴。",
                            "他笑容满面，眼睛里闪烁着喜悦。",
                            "他感觉很好。",
                            "他心情很好。"
                        ],
                        "answer": 1,
                        "explanation": "Show, don't tell - use specific details and actions to convey emotions.",
                        "explanation_zh": "展示，而不是告诉——用具体的细节和动作来传达情感。"
                    },
                    {
                        "id": "comp-ex6",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Choose the best transition word to connect these sentences: 我想去图书馆。___我要先完成作业。",
                        "prompt_zh": "选择最好的连接词来连接这些句子：我想去图书馆。___我要先完成作业。",
                        "choices": [
                            "但是",
                            "因此",
                            "然后",
                            "或者"
                        ],
                        "choices_zh": [
                            "但是",
                            "因此",
                            "然后",
                            "或者"
                        ],
                        "answer": 0,
                        "explanation": "但是 (but) shows contrast between wanting to go and needing to finish homework first.",
                        "explanation_zh": "\"但是\"（但是）表示想去和需要先完成作业之间的对比。"
                    },
                    {
                        "id": "comp-ex7",
                        "type": "match",
                        "difficulty": "medium",
                        "prompt": "Match the writing techniques with their purposes:",
                        "prompt_zh": "将写作技巧与其目的配对：",
                        "pairs": [
                            {
                                "left": "比喻",
                                "left_zh": "比喻",
                                "right": "Make comparisons clearer",
                                "right_zh": "使比较更清晰"
                            },
                            {
                                "left": "拟人",
                                "left_zh": "拟人",
                                "right": "Give human qualities to objects",
                                "right_zh": "赋予物体人的特质"
                            },
                            {
                                "left": "夸张",
                                "left_zh": "夸张",
                                "right": "Emphasize for effect",
                                "right_zh": "强调效果"
                            },
                            {
                                "left": "排比",
                                "left_zh": "排比",
                                "right": "Create rhythm and emphasis",
                                "right_zh": "创造节奏和强调"
                            }
                        ],
                        "explanation": "Different rhetorical devices serve different purposes in writing.",
                        "explanation_zh": "不同的修辞手法在写作中有不同的作用。"
                    },
                    {
                        "id": "comp-ex8",
                        "type": "mcq",
                        "difficulty": "hard",
                        "prompt": "Which sentence uses personification (拟人) effectively?",
                        "prompt_zh": "哪个句子有效地使用了拟人？",
                        "choices": [
                            "The tree is tall.",
                            "The old tree stood silently.",
                            "The ancient tree stretched its arms, welcoming the morning sun.",
                            "There is a tree in the park."
                        ],
                        "choices_zh": [
                            "树很高。",
                            "老树静静地站着。",
                            "古老的树伸展着双臂，欢迎晨曦。",
                            "公园里有一棵树。"
                        ],
                        "answer": 2,
                        "explanation": "Personification gives human qualities (arms, welcoming) to non-human objects.",
                        "explanation_zh": "拟人赋予非人类物体（手臂、欢迎）人的特质。"
                    },
                    {
                        "id": "comp-ex9",
                        "type": "mcq",
                        "difficulty": "easy",
                        "prompt": "What should a good conclusion do?",
                        "prompt_zh": "好的结尾应该做什么？",
                        "choices": [
                            "Introduce new topics",
                            "Summarize and reflect on the main points",
                            "Ask many questions",
                            "Change the subject completely"
                        ],
                        "choices_zh": [
                            "引入新话题",
                            "总结并反思要点",
                            "提出很多问题",
                            "完全改变主题"
                        ],
                        "answer": 1,
                        "explanation": "A good conclusion summarizes the main points and provides reflection or insight.",
                        "explanation_zh": "好的结尾总结要点并提供反思或见解。"
                    },
                    {
                        "id": "comp-ex10",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Which sentence best describes the Singapore hawker center atmosphere?",
                        "prompt_zh": "哪个句子最好地描述了新加坡小贩中心的氛围？",
                        "choices": [
                            "The hawker center was crowded.",
                            "Many people were eating.",
                            "The air was thick with aromatic spices, the clatter of plates mixing with cheerful chatter.",
                            "It was a food court."
                        ],
                        "choices_zh": [
                            "小贩中心很拥挤。",
                            "很多人在吃东西。",
                            "空气中弥漫着浓郁的香料味，盘子的碰撞声与欢快的聊天声混合在一起。",
                            "这是一个美食广场。"
                        ],
                        "answer": 2,
                        "explanation": "Use sensory details (smell, sound) to create vivid descriptions.",
                        "explanation_zh": "使用感官细节（气味、声音）来创造生动的描述。"
                    },
                    {
                        "id": "comp-ex11",
                        "type": "drag-order",
                        "difficulty": "hard",
                        "prompt": "Arrange these sentences to form a coherent paragraph:",
                        "prompt_zh": "排列这些句子以形成连贯的段落：",
                        "items": [
                            "我决定去图书馆学习。",
                            "考试下周就要到了。",
                            "在图书馆里，我专心复习功课。",
                            "经过几个小时的努力，我终于掌握了所有内容。"
                        ],
                        "items_zh": [
                            "我决定去图书馆学习。",
                            "考试下周就要到了。",
                            "在图书馆里，我专心复习功课。",
                            "经过几个小时的努力，我终于掌握了所有内容。"
                        ],
                        "answer": [
                            "考试下周就要到了。",
                            "我决定去图书馆学习。",
                            "在图书馆里，我专心复习功课。",
                            "经过几个小时的努力，我终于掌握了所有内容。"
                        ],
                        "explanation": "Logical order: Reason → Decision → Action → Result.",
                        "explanation_zh": "逻辑顺序：原因 → 决定 → 行动 → 结果。"
                    },
                    {
                        "id": "comp-ex12",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Which metaphor (比喻) is most appropriate for describing a busy city?",
                        "prompt_zh": "哪个比喻最适合描述繁忙的城市？",
                        "choices": [
                            "The city was busy.",
                            "The city was like a sleeping cat.",
                            "The city pulsed like a living organism, its streets flowing with endless streams of people.",
                            "The city was quiet."
                        ],
                        "choices_zh": [
                            "城市很繁忙。",
                            "城市像一只睡觉的猫。",
                            "城市像一个活的有机体一样跳动，街道上流动着无尽的人流。",
                            "城市很安静。"
                        ],
                        "answer": 2,
                        "explanation": "An effective metaphor compares the city to a living organism to show constant movement.",
                        "explanation_zh": "有效的比喻将城市比作活的有机体，以显示不断的运动。"
                    },
                    {
                        "id": "comp-ex13",
                        "type": "mcq",
                        "difficulty": "easy",
                        "prompt": "What is the main purpose of a narrative essay?",
                        "prompt_zh": "记叙文的主要目的是什么？",
                        "choices": [
                            "To argue a point",
                            "To tell a story or describe an experience",
                            "To explain how to do something",
                            "To compare two things"
                        ],
                        "choices_zh": [
                            "争论一个观点",
                            "讲述一个故事或描述一个经历",
                            "解释如何做某事",
                            "比较两件事"
                        ],
                        "answer": 1,
                        "explanation": "A narrative essay tells a story or describes an experience in an engaging way.",
                        "explanation_zh": "记叙文以引人入胜的方式讲述故事或描述经历。"
                    },
                    {
                        "id": "comp-ex14",
                        "type": "mcq",
                        "difficulty": "hard",
                        "prompt": "Which paragraph structure is best for Chinese composition?",
                        "prompt_zh": "哪种段落结构最适合中文作文？",
                        "choices": [
                            "All sentences about different topics",
                            "Topic sentence + Supporting details + Conclusion",
                            "Only questions",
                            "Random thoughts"
                        ],
                        "choices_zh": [
                            "所有句子都关于不同的话题",
                            "主题句 + 支撑细节 + 结论",
                            "只有问题",
                            "随机想法"
                        ],
                        "answer": 1,
                        "explanation": "Good paragraphs have a clear topic sentence, supporting details, and a concluding sentence.",
                        "explanation_zh": "好的段落有明确的主题句、支撑细节和结论句。"
                    },
                    {
                        "id": "comp-ex15",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Which dialogue format is correct in Chinese writing?",
                        "prompt_zh": "中文写作中哪种对话格式是正确的？",
                        "choices": [
                            "\"你好吗？\"他问。",
                            "你好吗？他问。",
                            "\"你好吗？他问。",
                            "你好吗？\"他问。"
                        ],
                        "choices_zh": [
                            "\"你好吗？\"他问。",
                            "你好吗？他问。",
                            "\"你好吗？他问。",
                            "你好吗？\"他问。"
                        ],
                        "answer": 0,
                        "explanation": "Dialogue should be enclosed in quotation marks with punctuation inside.",
                        "explanation_zh": "对话应该用引号括起来，标点符号在引号内。"
                    }
                ]

                # Extend existing exercises
                chapter['exercises'].extend(new_exercises)
                print(f"Added {len(new_exercises)} exercises to Composition Writing")
                print(f"Total exercises now: {len(chapter['exercises'])}")

# Save updated content
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✓ Composition Writing exercises updated successfully!")
