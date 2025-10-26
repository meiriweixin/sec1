import json

# Load current content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find Chinese subject and Vocabulary Building chapter
for subject in data['subjects']:
    if subject['id'] == 'chinese':
        for chapter in subject['chapters']:
            if chapter['id'] == 'chinese-vocabulary-building':
                # Add 11 new exercises
                new_exercises = [
                    {
                        "id": "vocab-ex5",
                        "type": "mcq",
                        "difficulty": "easy",
                        "prompt": "Which word best completes: 图书___",
                        "prompt_zh": "哪个词最适合完成：图书___",
                        "choices": [
                            "馆",
                            "管",
                            "官",
                            "关"
                        ],
                        "choices_zh": [
                            "馆",
                            "管",
                            "官",
                            "关"
                        ],
                        "answer": 0,
                        "explanation": "馆 means 'hall' or 'building', forming 图书馆 (library).",
                        "explanation_zh": "\"馆\"表示\"建筑物\"，组成\"图书馆\"（图书馆）。"
                    },
                    {
                        "id": "vocab-ex6",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "What does the radical 木 (wood) suggest about the character 林?",
                        "prompt_zh": "部首\"木\"（树木）对\"林\"这个字有什么提示？",
                        "choices": [
                            "It relates to animals",
                            "It relates to plants/trees",
                            "It relates to water",
                            "It relates to fire"
                        ],
                        "choices_zh": [
                            "与动物有关",
                            "与植物/树木有关",
                            "与水有关",
                            "与火有关"
                        ],
                        "answer": 1,
                        "explanation": "林 (forest) contains two 木 (wood/tree) radicals, indicating it relates to trees.",
                        "explanation_zh": "\"林\"（森林）包含两个\"木\"（木/树），表示与树木有关。"
                    },
                    {
                        "id": "vocab-ex7",
                        "type": "match",
                        "difficulty": "medium",
                        "prompt": "Match the words with their meanings:",
                        "prompt_zh": "将词语与意思配对：",
                        "pairs": [
                            {
                                "left": "美丽",
                                "left_zh": "美丽",
                                "right": "Beautiful",
                                "right_zh": "美丽的"
                            },
                            {
                                "left": "聪明",
                                "left_zh": "聪明",
                                "right": "Intelligent",
                                "right_zh": "聪明的"
                            },
                            {
                                "left": "勤劳",
                                "left_zh": "勤劳",
                                "right": "Hardworking",
                                "right_zh": "勤劳的"
                            },
                            {
                                "left": "诚实",
                                "left_zh": "诚实",
                                "right": "Honest",
                                "right_zh": "诚实的"
                            }
                        ],
                        "explanation": "These are common adjectives used to describe people's qualities.",
                        "explanation_zh": "这些是常用来描述人的品质的形容词。"
                    },
                    {
                        "id": "vocab-ex8",
                        "type": "mcq",
                        "difficulty": "easy",
                        "prompt": "Which word means 'environment'?",
                        "prompt_zh": "哪个词的意思是\"环境\"？",
                        "choices": [
                            "环境",
                            "环经",
                            "换境",
                            "幻境"
                        ],
                        "choices_zh": [
                            "环境",
                            "环经",
                            "换境",
                            "幻境"
                        ],
                        "answer": 0,
                        "explanation": "环境 means 'environment' or 'surroundings'.",
                        "explanation_zh": "\"环境\"的意思是\"周围的情况和条件\"。"
                    },
                    {
                        "id": "vocab-ex9",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "What is the opposite of 快乐 (happy)?",
                        "prompt_zh": "\"快乐\"（快乐）的反义词是什么？",
                        "choices": [
                            "高兴",
                            "伤心",
                            "开心",
                            "欢喜"
                        ],
                        "choices_zh": [
                            "高兴",
                            "伤心",
                            "开心",
                            "欢喜"
                        ],
                        "answer": 1,
                        "explanation": "伤心 (sad) is the opposite of 快乐 (happy).",
                        "explanation_zh": "\"伤心\"（悲伤）是\"快乐\"的反义词。"
                    },
                    {
                        "id": "vocab-ex10",
                        "type": "mcq",
                        "difficulty": "hard",
                        "prompt": "Which word correctly uses the radical 讠(speech)?",
                        "prompt_zh": "哪个词正确使用了部首\"讠\"（言语）？",
                        "choices": [
                            "说话",
                            "话说",
                            "话讠",
                            "讠说"
                        ],
                        "choices_zh": [
                            "说话",
                            "话说",
                            "话讠",
                            "讠说"
                        ],
                        "answer": 0,
                        "explanation": "说话 (speak) contains 讠radical in 说, indicating it relates to speech.",
                        "explanation_zh": "\"说话\"中的\"说\"包含\"讠\"部首，表示与言语有关。"
                    },
                    {
                        "id": "vocab-ex11",
                        "type": "drag-order",
                        "difficulty": "medium",
                        "prompt": "Arrange these characters by stroke count (fewest to most):",
                        "prompt_zh": "按笔画数排列这些字（从少到多）：",
                        "items": ["人", "木", "林", "森"],
                        "items_zh": ["人", "木", "林", "森"],
                        "answer": ["人", "木", "林", "森"],
                        "explanation": "人 (2 strokes), 木 (4 strokes), 林 (8 strokes), 森 (12 strokes)",
                        "explanation_zh": "人（2画）、木（4画）、林（8画）、森（12画）"
                    },
                    {
                        "id": "vocab-ex12",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Which word pair are synonyms?",
                        "prompt_zh": "哪对词是同义词？",
                        "choices": [
                            "快乐 - 伤心",
                            "美丽 - 漂亮",
                            "大 - 小",
                            "黑 - 白"
                        ],
                        "choices_zh": [
                            "快乐 - 伤心",
                            "美丽 - 漂亮",
                            "大 - 小",
                            "黑 - 白"
                        ],
                        "answer": 1,
                        "explanation": "美丽 and 漂亮 both mean 'beautiful'.",
                        "explanation_zh": "\"美丽\"和\"漂亮\"都表示\"好看\"的意思。"
                    },
                    {
                        "id": "vocab-ex13",
                        "type": "mcq",
                        "difficulty": "easy",
                        "prompt": "What does the character 友 mean in 朋友?",
                        "prompt_zh": "\"朋友\"中的\"友\"是什么意思？",
                        "choices": [
                            "Enemy",
                            "Friend",
                            "Teacher",
                            "Student"
                        ],
                        "choices_zh": [
                            "敌人",
                            "朋友",
                            "老师",
                            "学生"
                        ],
                        "answer": 1,
                        "explanation": "友 means 'friend', and 朋友 means 'friends'.",
                        "explanation_zh": "\"友\"表示\"朋友\"，\"朋友\"是指\"好友\"。"
                    },
                    {
                        "id": "vocab-ex14",
                        "type": "mcq",
                        "difficulty": "hard",
                        "prompt": "Which compound word means 'Singapore'?",
                        "prompt_zh": "哪个复合词的意思是\"新加坡\"？",
                        "choices": [
                            "新加坡",
                            "心加坡",
                            "辛加坡",
                            "信加坡"
                        ],
                        "choices_zh": [
                            "新加坡",
                            "心加坡",
                            "辛加坡",
                            "信加坡"
                        ],
                        "answer": 0,
                        "explanation": "新加坡 is the Chinese name for Singapore.",
                        "explanation_zh": "\"新加坡\"是新加坡的中文名称。"
                    },
                    {
                        "id": "vocab-ex15",
                        "type": "match",
                        "difficulty": "medium",
                        "prompt": "Match the Chinese words with their English meanings:",
                        "prompt_zh": "将中文词语与英文意思配对：",
                        "pairs": [
                            {
                                "left": "学校",
                                "left_zh": "学校",
                                "right": "School",
                                "right_zh": "学校"
                            },
                            {
                                "left": "医院",
                                "left_zh": "医院",
                                "right": "Hospital",
                                "right_zh": "医院"
                            },
                            {
                                "left": "银行",
                                "left_zh": "银行",
                                "right": "Bank",
                                "right_zh": "银行"
                            },
                            {
                                "left": "公园",
                                "left_zh": "公园",
                                "right": "Park",
                                "right_zh": "公园"
                            }
                        ],
                        "explanation": "These are common place names in Singapore.",
                        "explanation_zh": "这些是新加坡常见的地点名称。"
                    }
                ]

                # Extend existing exercises
                chapter['exercises'].extend(new_exercises)
                print(f"Added {len(new_exercises)} exercises to Vocabulary Building")
                print(f"Total exercises now: {len(chapter['exercises'])}")

# Save updated content
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✓ Vocabulary Building exercises updated successfully!")
