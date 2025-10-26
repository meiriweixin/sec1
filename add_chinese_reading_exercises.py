import json

# Load current content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find Chinese subject and Reading Comprehension chapter
for subject in data['subjects']:
    if subject['id'] == 'chinese':
        for chapter in subject['chapters']:
            if chapter['id'] == 'chinese-reading-comprehension':
                # Add 14 new exercises
                new_exercises = [
                    {
                        "id": "reading-ex2",
                        "type": "mcq",
                        "difficulty": "easy",
                        "prompt": "Read: 新加坡是一个多元文化的国家。What is the main idea?",
                        "prompt_zh": "阅读：新加坡是一个多元文化的国家。主要意思是什么？",
                        "choices": [
                            "Singapore is a small country",
                            "Singapore is multicultural",
                            "Singapore is hot",
                            "Singapore is an island"
                        ],
                        "choices_zh": [
                            "新加坡是一个小国家",
                            "新加坡是多元文化的",
                            "新加坡很热",
                            "新加坡是一个岛屿"
                        ],
                        "answer": 1,
                        "explanation": "The main idea is stated directly: Singapore is multicultural.",
                        "explanation_zh": "主要意思直接陈述：新加坡是多元文化的。"
                    },
                    {
                        "id": "reading-ex3",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Read: 虽然天气很热，但是他还是坚持跑步。What can we infer about him?",
                        "prompt_zh": "阅读：虽然天气很热，但是他还是坚持跑步。我们可以推断他的什么特质？",
                        "choices": [
                            "He is lazy",
                            "He is determined/persistent",
                            "He dislikes running",
                            "He is cold"
                        ],
                        "choices_zh": [
                            "他很懒",
                            "他很坚定/有毅力",
                            "他不喜欢跑步",
                            "他很冷"
                        ],
                        "answer": 1,
                        "explanation": "Despite the heat, he persists - this shows determination.",
                        "explanation_zh": "尽管很热，他还是坚持——这显示了决心。"
                    },
                    {
                        "id": "reading-ex4",
                        "type": "mcq",
                        "difficulty": "easy",
                        "prompt": "What is a transition word in this sentence: 我喜欢数学，因为它很有趣。",
                        "prompt_zh": "这个句子中的过渡词是什么：我喜欢数学，因为它很有趣。",
                        "choices": [
                            "我",
                            "喜欢",
                            "因为",
                            "有趣"
                        ],
                        "choices_zh": [
                            "我",
                            "喜欢",
                            "因为",
                            "有趣"
                        ],
                        "answer": 2,
                        "explanation": "因为 (because) is a transition word showing cause and effect.",
                        "explanation_zh": "\"因为\"是表示因果关系的过渡词。"
                    },
                    {
                        "id": "reading-ex5",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Read: 小明每天早上六点起床，然后去公园跑步。接着，他回家吃早餐。What time does he wake up?",
                        "prompt_zh": "阅读：小明每天早上六点起床，然后去公园跑步。接着，他回家吃早餐。他几点起床？",
                        "choices": [
                            "5:00 AM",
                            "6:00 AM",
                            "7:00 AM",
                            "8:00 AM"
                        ],
                        "choices_zh": [
                            "早上5点",
                            "早上6点",
                            "早上7点",
                            "早上8点"
                        ],
                        "answer": 1,
                        "explanation": "The text clearly states he wakes up at 6 o'clock in the morning.",
                        "explanation_zh": "文中明确说明他早上六点起床。"
                    },
                    {
                        "id": "reading-ex6",
                        "type": "drag-order",
                        "difficulty": "medium",
                        "prompt": "Arrange Xiao Ming's morning routine in order:",
                        "prompt_zh": "按顺序排列小明的早晨日程：",
                        "items": ["起床", "去公园跑步", "回家", "吃早餐"],
                        "items_zh": ["起床", "去公园跑步", "回家", "吃早餐"],
                        "answer": ["起床", "去公园跑步", "回家", "吃早餐"],
                        "explanation": "The sequence is: wake up → go to park → return home → eat breakfast.",
                        "explanation_zh": "顺序是：起床 → 去公园 → 回家 → 吃早餐。"
                    },
                    {
                        "id": "reading-ex7",
                        "type": "mcq",
                        "difficulty": "hard",
                        "prompt": "Read: 李老师对学生很严格，但学生们都很尊敬他。What does 但 indicate?",
                        "prompt_zh": "阅读：李老师对学生很严格，但学生们都很尊敬他。\"但\"表示什么？",
                        "choices": [
                            "Agreement",
                            "Contrast/Opposition",
                            "Sequence",
                            "Cause"
                        ],
                        "choices_zh": [
                            "一致",
                            "对比/转折",
                            "顺序",
                            "原因"
                        ],
                        "answer": 1,
                        "explanation": "但 (but) shows contrast - despite being strict, students respect him.",
                        "explanation_zh": "\"但\"（但是）表示对比——尽管严格，学生们还是尊敬他。"
                    },
                    {
                        "id": "reading-ex8",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Read: 我的朋友小华住在乌节路附近。她每天乘地铁上学。What do we know about Xiao Hua?",
                        "prompt_zh": "阅读：我的朋友小华住在乌节路附近。她每天乘地铁上学。我们了解小华的什么？",
                        "choices": [
                            "She lives near Orchard Road and takes MRT to school",
                            "She lives far from school",
                            "She drives to school",
                            "She doesn't go to school"
                        ],
                        "choices_zh": [
                            "她住在乌节路附近，乘地铁上学",
                            "她住得离学校很远",
                            "她开车上学",
                            "她不上学"
                        ],
                        "answer": 0,
                        "explanation": "The text states she lives near Orchard Road and takes MRT to school.",
                        "explanation_zh": "文中说明她住在乌节路附近，乘地铁上学。"
                    },
                    {
                        "id": "reading-ex9",
                        "type": "mcq",
                        "difficulty": "easy",
                        "prompt": "What does 接着 mean in: 我做完作业，接着看电视。",
                        "prompt_zh": "在这个句子中\"接着\"是什么意思：我做完作业，接着看电视。",
                        "choices": [
                            "But",
                            "Because",
                            "Then/Next",
                            "Although"
                        ],
                        "choices_zh": [
                            "但是",
                            "因为",
                            "然后/接下来",
                            "虽然"
                        ],
                        "answer": 2,
                        "explanation": "接着 means 'then' or 'next', showing sequence of actions.",
                        "explanation_zh": "\"接着\"表示\"然后\"或\"接下来\"，显示动作的顺序。"
                    },
                    {
                        "id": "reading-ex10",
                        "type": "mcq",
                        "difficulty": "hard",
                        "prompt": "Read: 新加坡的小贩中心不仅提供美食，还是人们社交的地方。What is the author's purpose?",
                        "prompt_zh": "阅读：新加坡的小贩中心不仅提供美食，还是人们社交的地方。作者的目的是什么？",
                        "choices": [
                            "To describe hawker centers only as food places",
                            "To show hawker centers have dual purposes: food and socializing",
                            "To criticize hawker centers",
                            "To compare hawker centers with restaurants"
                        ],
                        "choices_zh": [
                            "只描述小贩中心是美食场所",
                            "展示小贩中心有双重目的：美食和社交",
                            "批评小贩中心",
                            "比较小贩中心和餐厅"
                        ],
                        "answer": 1,
                        "explanation": "不仅...还 structure shows hawker centers serve both purposes.",
                        "explanation_zh": "\"不仅...还\"结构表示小贩中心有两个目的。"
                    },
                    {
                        "id": "reading-ex11",
                        "type": "match",
                        "difficulty": "medium",
                        "prompt": "Match the transition words with their functions:",
                        "prompt_zh": "将过渡词与其功能配对：",
                        "pairs": [
                            {
                                "left": "因为",
                                "left_zh": "因为",
                                "right": "Shows cause/reason",
                                "right_zh": "表示原因"
                            },
                            {
                                "left": "但是",
                                "left_zh": "但是",
                                "right": "Shows contrast",
                                "right_zh": "表示对比"
                            },
                            {
                                "left": "所以",
                                "left_zh": "所以",
                                "right": "Shows result",
                                "right_zh": "表示结果"
                            },
                            {
                                "left": "虽然",
                                "left_zh": "虽然",
                                "right": "Shows concession",
                                "right_zh": "表示让步"
                            }
                        ],
                        "explanation": "Different transition words show different logical relationships.",
                        "explanation_zh": "不同的过渡词显示不同的逻辑关系。"
                    },
                    {
                        "id": "reading-ex12",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Read: 虽然雨下得很大，但是运动会还是照常进行。What does this tell us?",
                        "prompt_zh": "阅读：虽然雨下得很大，但是运动会还是照常进行。这告诉我们什么？",
                        "choices": [
                            "The sports day was cancelled",
                            "The sports day continued despite heavy rain",
                            "It didn't rain during sports day",
                            "The sports day was postponed"
                        ],
                        "choices_zh": [
                            "运动会被取消了",
                            "尽管大雨，运动会还是继续进行",
                            "运动会期间没有下雨",
                            "运动会被推迟了"
                        ],
                        "answer": 1,
                        "explanation": "虽然...但是 structure shows that despite the rain, sports day continued.",
                        "explanation_zh": "\"虽然...但是\"结构表示尽管下雨，运动会还是继续。"
                    },
                    {
                        "id": "reading-ex13",
                        "type": "mcq",
                        "difficulty": "easy",
                        "prompt": "Read: 我很喜欢阅读，尤其是科幻小说。What does 尤其 emphasize?",
                        "prompt_zh": "阅读：我很喜欢阅读，尤其是科幻小说。\"尤其\"强调什么？",
                        "choices": [
                            "Dislike of reading",
                            "Particular preference for science fiction",
                            "Dislike of science fiction",
                            "No preference"
                        ],
                        "choices_zh": [
                            "不喜欢阅读",
                            "特别喜欢科幻小说",
                            "不喜欢科幻小说",
                            "没有偏好"
                        ],
                        "answer": 1,
                        "explanation": "尤其 (especially) emphasizes a particular preference within a general liking.",
                        "explanation_zh": "\"尤其\"（特别）在一般喜好中强调特别的偏好。"
                    },
                    {
                        "id": "reading-ex14",
                        "type": "mcq",
                        "difficulty": "hard",
                        "prompt": "Read: 新加坡虽小，却拥有丰富的文化遗产。What literary device is used?",
                        "prompt_zh": "阅读：新加坡虽小，却拥有丰富的文化遗产。使用了什么修辞手法？",
                        "choices": [
                            "Metaphor",
                            "Contrast/Juxtaposition",
                            "Personification",
                            "Repetition"
                        ],
                        "choices_zh": [
                            "比喻",
                            "对比/并列",
                            "拟人",
                            "重复"
                        ],
                        "answer": 1,
                        "explanation": "The sentence contrasts Singapore's small size with its rich cultural heritage.",
                        "explanation_zh": "这个句子将新加坡的小面积与丰富的文化遗产进行对比。"
                    },
                    {
                        "id": "reading-ex15",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Read: 李明不但学习好，而且体育也很棒。What can we conclude?",
                        "prompt_zh": "阅读：李明不但学习好，而且体育也很棒。我们可以得出什么结论？",
                        "choices": [
                            "Li Ming is only good at studies",
                            "Li Ming is only good at sports",
                            "Li Ming excels in both studies and sports",
                            "Li Ming is not good at anything"
                        ],
                        "choices_zh": [
                            "李明只擅长学习",
                            "李明只擅长体育",
                            "李明在学习和体育方面都很出色",
                            "李明什么都不擅长"
                        ],
                        "answer": 2,
                        "explanation": "不但...而且 structure shows Li Ming excels in both areas.",
                        "explanation_zh": "\"不但...而且\"结构表示李明在两个方面都很出色。"
                    }
                ]

                # Extend existing exercises
                chapter['exercises'].extend(new_exercises)
                print(f"Added {len(new_exercises)} exercises to Reading Comprehension")
                print(f"Total exercises now: {len(chapter['exercises'])}")

# Save updated content
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✓ Reading Comprehension exercises updated successfully!")
