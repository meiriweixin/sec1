import json

# Load current content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find Chinese subject and Grammar Fundamentals chapter
for subject in data['subjects']:
    if subject['id'] == 'chinese':
        for chapter in subject['chapters']:
            if chapter['id'] == 'chinese-grammar-fundamentals':
                # Add 10 new exercises
                new_exercises = [
                    {
                        "id": "grammar-ex6",
                        "type": "mcq",
                        "difficulty": "easy",
                        "prompt": "Which sentence follows the correct word order?",
                        "prompt_zh": "哪个句子的语序是正确的？",
                        "choices": [
                            "I yesterday went to school.",
                            "Yesterday I went to school.",
                            "I went yesterday to school.",
                            "Went I yesterday to school."
                        ],
                        "choices_zh": [
                            "我昨天去了学校。",
                            "昨天我去了学校。",
                            "我去了昨天学校。",
                            "去了我昨天学校。"
                        ],
                        "answer": 1,
                        "explanation": "Time words (like 'yesterday') usually come before the subject or right after it in Chinese.",
                        "explanation_zh": "时间词（如\"昨天\"）通常出现在主语之前或主语之后。"
                    },
                    {
                        "id": "grammar-ex7",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Choose the correct measure word for books (书):",
                        "prompt_zh": "选择正确的量词来修饰\"书\"：",
                        "choices": [
                            "一张书",
                            "一本书",
                            "一条书",
                            "一个书"
                        ],
                        "choices_zh": [
                            "一张书",
                            "一本书",
                            "一条书",
                            "一个书"
                        ],
                        "answer": 1,
                        "explanation": "本 (běn) is the correct measure word for books, magazines, and notebooks.",
                        "explanation_zh": "\"本\"是书、杂志和笔记本的正确量词。"
                    },
                    {
                        "id": "grammar-ex8",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Which sentence correctly uses the '把' construction?",
                        "prompt_zh": "哪个句子正确使用了\"把\"字句？",
                        "choices": [
                            "我把作业写。",
                            "我把作业写完了。",
                            "我作业把写完了。",
                            "我写把作业完了。"
                        ],
                        "choices_zh": [
                            "我把作业写。",
                            "我把作业写完了。",
                            "我作业把写完了。",
                            "我写把作业完了。"
                        ],
                        "answer": 1,
                        "explanation": "The 把 construction follows this pattern: Subject + 把 + Object + Verb + Result/Complement.",
                        "explanation_zh": "\"把\"字句的结构是：主语 + 把 + 宾语 + 动词 + 结果/补语。"
                    },
                    {
                        "id": "grammar-ex9",
                        "type": "drag-order",
                        "difficulty": "medium",
                        "prompt": "Arrange these words in correct order to form a sentence:",
                        "prompt_zh": "按正确顺序排列这些词语，组成一个句子：",
                        "items": ["我", "明天", "去", "图书馆"],
                        "items_zh": ["我", "明天", "去", "图书馆"],
                        "answer": ["我", "明天", "去", "图书馆"],
                        "explanation": "Correct order: Subject + Time + Verb + Place (我明天去图书馆)",
                        "explanation_zh": "正确顺序：主语 + 时间 + 动词 + 地点（我明天去图书馆）"
                    },
                    {
                        "id": "grammar-ex10",
                        "type": "mcq",
                        "difficulty": "hard",
                        "prompt": "Choose the correct complement to complete: 他跑___很快。",
                        "prompt_zh": "选择正确的补语完成句子：他跑___很快。",
                        "choices": [
                            "他跑了很快。",
                            "他跑得很快。",
                            "他跑的很快。",
                            "他跑着很快。"
                        ],
                        "choices_zh": [
                            "他跑了很快。",
                            "他跑得很快。",
                            "他跑的很快。",
                            "他跑着很快。"
                        ],
                        "answer": 1,
                        "explanation": "得 (de) is used to link verbs with complements that describe the manner or result of an action.",
                        "explanation_zh": "\"得\"用于连接动词和描述动作方式或结果的补语。"
                    },
                    {
                        "id": "grammar-ex11",
                        "type": "mcq",
                        "difficulty": "easy",
                        "prompt": "Which measure word is correct for people (人)?",
                        "prompt_zh": "哪个量词适合用来修饰\"人\"？",
                        "choices": [
                            "一只人",
                            "一条人",
                            "一个人",
                            "一本人"
                        ],
                        "choices_zh": [
                            "一只人",
                            "一条人",
                            "一个人",
                            "一本人"
                        ],
                        "answer": 2,
                        "explanation": "个 (gè) is the most common measure word and is often used for people.",
                        "explanation_zh": "\"个\"是最常用的量词，常用于人。"
                    },
                    {
                        "id": "grammar-ex12",
                        "type": "drag-order",
                        "difficulty": "hard",
                        "prompt": "Arrange in correct order: Subject + Time + Place + Verb + Object",
                        "prompt_zh": "按正确顺序排列：主语 + 时间 + 地点 + 动词 + 宾语",
                        "items": ["我", "昨天", "在学校", "看了", "一本书"],
                        "items_zh": ["我", "昨天", "在学校", "看了", "一本书"],
                        "answer": ["我", "昨天", "在学校", "看了", "一本书"],
                        "explanation": "Chinese word order: Subject + Time + Place + Verb + Object",
                        "explanation_zh": "汉语的语序：主语 + 时间 + 地点 + 动词 + 宾语"
                    },
                    {
                        "id": "grammar-ex13",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "What is the correct particle to use for past tense: 我吃___午饭。",
                        "prompt_zh": "选择正确的语气助词表示过去时：我吃___午饭。",
                        "choices": [
                            "我吃的午饭。",
                            "我吃了午饭。",
                            "我吃得午饭。",
                            "我吃着午饭。"
                        ],
                        "choices_zh": [
                            "我吃的午饭。",
                            "我吃了午饭。",
                            "我吃得午饭。",
                            "我吃着午饭。"
                        ],
                        "answer": 1,
                        "explanation": "了 (le) is used to indicate completed action or change of state.",
                        "explanation_zh": "\"了\"用于表示动作的完成或状态的改变。"
                    },
                    {
                        "id": "grammar-ex14",
                        "type": "mcq",
                        "difficulty": "hard",
                        "prompt": "Which sentence correctly uses the 'passive voice' with 被?",
                        "prompt_zh": "哪个句子正确使用了\"被\"字表示被动语态？",
                        "choices": [
                            "我被老师表扬。",
                            "我被老师表扬了。",
                            "我老师被表扬了。",
                            "被我老师表扬了。"
                        ],
                        "choices_zh": [
                            "我被老师表扬。",
                            "我被老师表扬了。",
                            "我老师被表扬了。",
                            "被我老师表扬了。"
                        ],
                        "answer": 1,
                        "explanation": "Passive voice structure: Receiver + 被 + Agent + Verb + (了/other particle)",
                        "explanation_zh": "被动语态结构：受事 + 被 + 施事 + 动词 + （了/其他语气助词）"
                    },
                    {
                        "id": "grammar-ex15",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Choose the correct measure word for fish (鱼):",
                        "prompt_zh": "选择正确的量词来修饰\"鱼\"：",
                        "choices": [
                            "一本鱼",
                            "一条鱼",
                            "一个鱼",
                            "一张鱼"
                        ],
                        "choices_zh": [
                            "一本鱼",
                            "一条鱼",
                            "一个鱼",
                            "一张鱼"
                        ],
                        "answer": 1,
                        "explanation": "条 (tiáo) is the measure word for long, thin objects like fish, rivers, roads, and pants.",
                        "explanation_zh": "\"条\"是用于长而细的物体的量词，如鱼、河流、道路和裤子。"
                    }
                ]

                # Extend existing exercises
                chapter['exercises'].extend(new_exercises)
                print(f"Added {len(new_exercises)} exercises to Grammar Fundamentals")
                print(f"Total exercises now: {len(chapter['exercises'])}")

# Save updated content
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✓ Grammar Fundamentals exercises updated successfully!")
