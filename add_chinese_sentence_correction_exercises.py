import json

# Load current content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find Chinese subject and Sentence Correction chapter
for subject in data['subjects']:
    if subject['id'] == 'chinese':
        for chapter in subject['chapters']:
            if chapter['id'] == 'chinese-sentence-correction':
                # Add 14 new exercises
                new_exercises = [
                    {
                        "id": "correction-ex2",
                        "type": "mcq",
                        "difficulty": "easy",
                        "prompt": "Which sentence has a word order error?",
                        "prompt_zh": "哪个句子有语序错误？",
                        "choices": [
                            "我昨天去了学校。",
                            "我去了昨天学校。",
                            "昨天我去了学校。",
                            "我去学校了昨天。"
                        ],
                        "choices_zh": [
                            "我昨天去了学校。",
                            "我去了昨天学校。",
                            "昨天我去了学校。",
                            "我去学校了昨天。"
                        ],
                        "answer": 1,
                        "explanation": "Time words should come before or after the subject, not after the verb.",
                        "explanation_zh": "时间词应该在主语之前或之后，不应在动词之后。"
                    },
                    {
                        "id": "correction-ex3",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Identify the sentence with incorrect word collocation:",
                        "prompt_zh": "找出词语搭配不当的句子：",
                        "choices": [
                            "提高水平",
                            "改进方法",
                            "增加人数",
                            "提高人数"
                        ],
                        "choices_zh": [
                            "提高水平",
                            "改进方法",
                            "增加人数",
                            "提高人数"
                        ],
                        "answer": 3,
                        "explanation": "We say 增加人数 (increase number), not 提高人数. 提高 is used with quality/level.",
                        "explanation_zh": "应该说\"增加人数\"，不是\"提高人数\"。\"提高\"用于质量/水平。"
                    },
                    {
                        "id": "correction-ex4",
                        "type": "mcq",
                        "difficulty": "easy",
                        "prompt": "Which sentence is missing a subject?",
                        "prompt_zh": "哪个句子缺少主语？",
                        "choices": [
                            "我喜欢读书。",
                            "他每天跑步。",
                            "喜欢吃榴莲。",
                            "老师在教室里。"
                        ],
                        "choices_zh": [
                            "我喜欢读书。",
                            "他每天跑步。",
                            "喜欢吃榴莲。",
                            "老师在教室里。"
                        ],
                        "answer": 2,
                        "explanation": "The sentence needs to specify WHO likes to eat durian.",
                        "explanation_zh": "句子需要说明是谁喜欢吃榴莲。"
                    },
                    {
                        "id": "correction-ex5",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Find the sentence with redundant words:",
                        "prompt_zh": "找出有多余词语的句子：",
                        "choices": [
                            "我大约三点左右回家。",
                            "我三点回家。",
                            "我大约三点回家。",
                            "我三点左右回家。"
                        ],
                        "choices_zh": [
                            "我大约三点左右回家。",
                            "我三点回家。",
                            "我大约三点回家。",
                            "我三点左右回家。"
                        ],
                        "answer": 0,
                        "explanation": "大约 and 左右 both mean 'approximately' - using both is redundant.",
                        "explanation_zh": "\"大约\"和\"左右\"都表示\"大概\"——两者同时使用是多余的。"
                    },
                    {
                        "id": "correction-ex6",
                        "type": "mcq",
                        "difficulty": "hard",
                        "prompt": "Which sentence has a logical contradiction?",
                        "prompt_zh": "哪个句子有逻辑矛盾？",
                        "choices": [
                            "新加坡的天气很热。",
                            "他跑得很快，所以最后到达。",
                            "图书馆很安静。",
                            "学生们在认真学习。"
                        ],
                        "choices_zh": [
                            "新加坡的天气很热。",
                            "他跑得很快，所以最后到达。",
                            "图书馆很安静。",
                            "学生们在认真学习。"
                        ],
                        "answer": 1,
                        "explanation": "If he runs fast, he should arrive first, not last. This is a logical error.",
                        "explanation_zh": "如果他跑得快，应该最先到达，不是最后。这是逻辑错误。"
                    },
                    {
                        "id": "correction-ex7",
                        "type": "match",
                        "difficulty": "medium",
                        "prompt": "Match the error types with examples:",
                        "prompt_zh": "将错误类型与例子配对：",
                        "pairs": [
                            {
                                "left": "Word order error",
                                "left_zh": "语序错误",
                                "right": "我去了昨天学校",
                                "right_zh": "我去了昨天学校"
                            },
                            {
                                "left": "Missing component",
                                "left_zh": "成分残缺",
                                "right": "喜欢吃榴莲",
                                "right_zh": "喜欢吃榴莲"
                            },
                            {
                                "left": "Redundancy",
                                "left_zh": "成分赘余",
                                "right": "大约三点左右",
                                "right_zh": "大约三点左右"
                            },
                            {
                                "left": "Wrong collocation",
                                "left_zh": "搭配不当",
                                "right": "提高人数",
                                "right_zh": "提高人数"
                            }
                        ],
                        "explanation": "Different types of sentence errors require different correction methods.",
                        "explanation_zh": "不同类型的句子错误需要不同的修改方法。"
                    },
                    {
                        "id": "correction-ex8",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Correct this sentence: 他把书放在了桌子。",
                        "prompt_zh": "修改这个句子：他把书放在了桌子。",
                        "choices": [
                            "他把书放桌子。",
                            "他把书放在桌子上。",
                            "他书放在桌子。",
                            "他放书桌子。"
                        ],
                        "choices_zh": [
                            "他把书放桌子。",
                            "他把书放在桌子上。",
                            "他书放在桌子。",
                            "他放书桌子。"
                        ],
                        "answer": 1,
                        "explanation": "Need to add 上 (on) to complete the location phrase 在桌子上.",
                        "explanation_zh": "需要加\"上\"来完成位置短语\"在桌子上\"。"
                    },
                    {
                        "id": "correction-ex9",
                        "type": "mcq",
                        "difficulty": "easy",
                        "prompt": "Which sentence uses the wrong measure word?",
                        "prompt_zh": "哪个句子使用了错误的量词？",
                        "choices": [
                            "一本书",
                            "一条鱼",
                            "一张桌子",
                            "一本人"
                        ],
                        "choices_zh": [
                            "一本书",
                            "一条鱼",
                            "一张桌子",
                            "一本人"
                        ],
                        "answer": 3,
                        "explanation": "People use 个 as the measure word, not 本 (which is for books).",
                        "explanation_zh": "人用\"个\"作量词，不是\"本\"（本是用于书的）。"
                    },
                    {
                        "id": "correction-ex10",
                        "type": "mcq",
                        "difficulty": "hard",
                        "prompt": "Identify the ambiguous sentence:",
                        "prompt_zh": "找出有歧义的句子：",
                        "choices": [
                            "我看见他和他的朋友在公园。",
                            "我和他的朋友在公园看见他。",
                            "他在公园看见我和我的朋友。",
                            "我看见他的朋友和他在公园。"
                        ],
                        "choices_zh": [
                            "我看见他和他的朋友在公园。",
                            "我和他的朋友在公园看见他。",
                            "他在公园看见我和我的朋友。",
                            "我看见他的朋友和他在公园。"
                        ],
                        "answer": 1,
                        "explanation": "Unclear if \"his friend\" refers to the speaker's friend or the other person's friend.",
                        "explanation_zh": "不清楚\"他的朋友\"指的是说话者的朋友还是另一个人的朋友。"
                    },
                    {
                        "id": "correction-ex11",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Correct: 新加坡的小贩中心有很美味的食物。",
                        "prompt_zh": "修改：新加坡的小贩中心有很美味的食物。",
                        "choices": [
                            "新加坡的小贩中心有美味的食物。",
                            "新加坡的小贩中心食物很美味。",
                            "Both A and B are correct",
                            "The original is correct"
                        ],
                        "choices_zh": [
                            "新加坡的小贩中心有美味的食物。",
                            "新加坡的小贩中心食物很美味。",
                            "A和B都正确",
                            "原句正确"
                        ],
                        "answer": 2,
                        "explanation": "很 should not be used before 美味 when it modifies a noun. Remove 很 or restructure.",
                        "explanation_zh": "当修饰名词时，\"美味\"前不应该用\"很\"。去掉\"很\"或重组句子。"
                    },
                    {
                        "id": "correction-ex12",
                        "type": "mcq",
                        "difficulty": "easy",
                        "prompt": "Which sentence has incorrect punctuation?",
                        "prompt_zh": "哪个句子的标点符号不正确？",
                        "choices": [
                            "他说：\"我很高兴。\"",
                            "他说\"我很高兴。\"",
                            "\"我很高兴。\"他说。",
                            "他说，\"我很高兴。\""
                        ],
                        "choices_zh": [
                            "他说：\"我很高兴。\"",
                            "他说\"我很高兴。\"",
                            "\"我很高兴。\"他说。",
                            "他说，\"我很高兴。\""
                        ],
                        "answer": 1,
                        "explanation": "Need a colon (:) or comma (,) before direct speech.",
                        "explanation_zh": "直接引语前需要冒号（：）或逗号（，）。"
                    },
                    {
                        "id": "correction-ex13",
                        "type": "drag-order",
                        "difficulty": "medium",
                        "prompt": "Rearrange to form a correct sentence:",
                        "prompt_zh": "重新排列以形成正确的句子：",
                        "items": ["我", "昨天", "在图书馆", "看了", "一本书"],
                        "items_zh": ["我", "昨天", "在图书馆", "看了", "一本书"],
                        "answer": ["我", "昨天", "在图书馆", "看了", "一本书"],
                        "explanation": "Correct order: Subject + Time + Place + Verb + Object.",
                        "explanation_zh": "正确顺序：主语 + 时间 + 地点 + 动词 + 宾语。"
                    },
                    {
                        "id": "correction-ex14",
                        "type": "mcq",
                        "difficulty": "hard",
                        "prompt": "Find the sentence with improper verb-object collocation:",
                        "prompt_zh": "找出动宾搭配不当的句子：",
                        "choices": [
                            "提高质量",
                            "改善环境",
                            "解决困难",
                            "增加速度"
                        ],
                        "choices_zh": [
                            "提高质量",
                            "改善环境",
                            "解决困难",
                            "增加速度"
                        ],
                        "answer": 2,
                        "explanation": "Should say 克服困难 (overcome difficulties), not 解决困难. 解决 is for problems.",
                        "explanation_zh": "应该说\"克服困难\"，不是\"解决困难\"。\"解决\"用于问题。"
                    },
                    {
                        "id": "correction-ex15",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Correct this Singapore context sentence: 我每天坐地铁去乌节路的学校上课。",
                        "prompt_zh": "修改这个新加坡情境句子：我每天坐地铁去乌节路的学校上课。",
                        "choices": [
                            "The sentence is correct",
                            "我每天坐地铁去在乌节路的学校上课",
                            "我每天坐地铁到乌节路的学校上课",
                            "我每天地铁去乌节路的学校上课"
                        ],
                        "choices_zh": [
                            "句子是正确的",
                            "我每天坐地铁去在乌节路的学校上课",
                            "我每天坐地铁到乌节路的学校上课",
                            "我每天地铁去乌节路的学校上课"
                        ],
                        "answer": 2,
                        "explanation": "When destination is specified, use 到 (to/arrive at) instead of 去 (go).",
                        "explanation_zh": "当目的地明确时，用\"到\"（到达）而不是\"去\"。"
                    }
                ]

                # Extend existing exercises
                chapter['exercises'].extend(new_exercises)
                print(f"Added {len(new_exercises)} exercises to Sentence Correction")
                print(f"Total exercises now: {len(chapter['exercises'])}")

# Save updated content
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✓ Sentence Correction exercises updated successfully!")
