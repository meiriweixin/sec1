import json

# Load current content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find Chinese subject and Idioms & Proverbs chapter
for subject in data['subjects']:
    if subject['id'] == 'chinese':
        for chapter in subject['chapters']:
            if chapter['id'] == 'chinese-idioms-proverbs':
                # Add 14 new exercises
                new_exercises = [
                    {
                        "id": "idiom-ex2",
                        "type": "mcq",
                        "difficulty": "easy",
                        "prompt": "What does the idiom 守株待兔 mean?",
                        "prompt_zh": "成语\"守株待兔\"是什么意思？",
                        "choices": [
                            "Waiting passively for good luck",
                            "Working very hard",
                            "Being very clever",
                            "Running very fast"
                        ],
                        "choices_zh": [
                            "被动等待好运",
                            "非常努力工作",
                            "非常聪明",
                            "跑得很快"
                        ],
                        "answer": 0,
                        "explanation": "This idiom means waiting passively for opportunities instead of actively pursuing them.",
                        "explanation_zh": "这个成语意思是被动等待机会，而不是主动追求。"
                    },
                    {
                        "id": "idiom-ex3",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Which idiom means 'to add unnecessary embellishments'?",
                        "prompt_zh": "哪个成语的意思是\"添加不必要的装饰\"？",
                        "choices": [
                            "画蛇添足",
                            "对牛弹琴",
                            "亡羊补牢",
                            "一举两得"
                        ],
                        "choices_zh": [
                            "画蛇添足",
                            "对牛弹琴",
                            "亡羊补牢",
                            "一举两得"
                        ],
                        "answer": 0,
                        "explanation": "画蛇添足 literally means 'drawing legs on a snake' - doing something unnecessary.",
                        "explanation_zh": "\"画蛇添足\"字面意思是\"给蛇画腿\"——做不必要的事情。"
                    },
                    {
                        "id": "idiom-ex4",
                        "type": "mcq",
                        "difficulty": "easy",
                        "prompt": "What does 一举两得 mean?",
                        "prompt_zh": "\"一举两得\"是什么意思？",
                        "choices": [
                            "Kill two birds with one stone",
                            "One is better than two",
                            "Two heads are better than one",
                            "One step at a time"
                        ],
                        "choices_zh": [
                            "一石二鸟",
                            "一比二好",
                            "三个臭皮匠胜过一个诸葛亮",
                            "一步一个脚印"
                        ],
                        "answer": 0,
                        "explanation": "一举两得 means achieving two objectives with one action.",
                        "explanation_zh": "\"一举两得\"意思是用一个行动达到两个目标。"
                    },
                    {
                        "id": "idiom-ex5",
                        "type": "match",
                        "difficulty": "medium",
                        "prompt": "Match the idioms with their meanings:",
                        "prompt_zh": "将成语与其意思配对：",
                        "pairs": [
                            {
                                "left": "对牛弹琴",
                                "left_zh": "对牛弹琴",
                                "right": "Talking to the wrong audience",
                                "right_zh": "对错误的听众说话"
                            },
                            {
                                "left": "亡羊补牢",
                                "left_zh": "亡羊补牢",
                                "right": "Better late than never",
                                "right_zh": "迟到总比不到好"
                            },
                            {
                                "left": "半途而废",
                                "left_zh": "半途而废",
                                "right": "Give up halfway",
                                "right_zh": "中途放弃"
                            },
                            {
                                "left": "水滴石穿",
                                "left_zh": "水滴石穿",
                                "right": "Persistence pays off",
                                "right_zh": "坚持就会成功"
                            }
                        ],
                        "explanation": "These idioms teach important life lessons.",
                        "explanation_zh": "这些成语教给我们重要的人生道理。"
                    },
                    {
                        "id": "idiom-ex6",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Which idiom describes someone who is very hardworking?",
                        "prompt_zh": "哪个成语形容一个人非常勤奋？",
                        "choices": [
                            "好逸恶劳",
                            "废寝忘食",
                            "坐享其成",
                            "游手好闲"
                        ],
                        "choices_zh": [
                            "好逸恶劳",
                            "废寝忘食",
                            "坐享其成",
                            "游手好闲"
                        ],
                        "answer": 1,
                        "explanation": "废寝忘食 means forgetting to eat and sleep because of hard work.",
                        "explanation_zh": "\"废寝忘食\"意思是因为努力工作而忘记吃饭和睡觉。"
                    },
                    {
                        "id": "idiom-ex7",
                        "type": "mcq",
                        "difficulty": "hard",
                        "prompt": "Complete the idiom: 三人行，必有我___",
                        "prompt_zh": "完成这个成语：三人行，必有我___",
                        "choices": [
                            "友",
                            "师",
                            "同",
                            "伴"
                        ],
                        "choices_zh": [
                            "友",
                            "师",
                            "同",
                            "伴"
                        ],
                        "answer": 1,
                        "explanation": "三人行，必有我师 means 'among three people, one must be my teacher' - we can learn from everyone.",
                        "explanation_zh": "\"三人行，必有我师\"意思是三个人中一定有可以做我老师的——我们可以向每个人学习。"
                    },
                    {
                        "id": "idiom-ex8",
                        "type": "mcq",
                        "difficulty": "easy",
                        "prompt": "What does 井底之蛙 (frog at the bottom of a well) mean?",
                        "prompt_zh": "\"井底之蛙\"（井底的青蛙）是什么意思？",
                        "choices": [
                            "Someone with a narrow perspective",
                            "Someone who lives underground",
                            "Someone who likes frogs",
                            "Someone who digs wells"
                        ],
                        "choices_zh": [
                            "视野狭窄的人",
                            "住在地下的人",
                            "喜欢青蛙的人",
                            "挖井的人"
                        ],
                        "answer": 0,
                        "explanation": "井底之蛙 describes someone with limited knowledge or narrow perspective.",
                        "explanation_zh": "\"井底之蛙\"形容知识有限或视野狭窄的人。"
                    },
                    {
                        "id": "idiom-ex9",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Which idiom means 'practice makes perfect'?",
                        "prompt_zh": "哪个成语的意思是\"熟能生巧\"？",
                        "choices": [
                            "熟能生巧",
                            "一鸣惊人",
                            "一日千里",
                            "一步登天"
                        ],
                        "choices_zh": [
                            "熟能生巧",
                            "一鸣惊人",
                            "一日千里",
                            "一步登天"
                        ],
                        "answer": 0,
                        "explanation": "熟能生巧 literally means 'familiarity breeds skill'.",
                        "explanation_zh": "\"熟能生巧\"字面意思是\"熟练了就能产生技巧\"。"
                    },
                    {
                        "id": "idiom-ex10",
                        "type": "match",
                        "difficulty": "hard",
                        "prompt": "Match these Singapore-relevant idioms with their meanings:",
                        "prompt_zh": "将这些与新加坡相关的成语与其意思配对：",
                        "pairs": [
                            {
                                "left": "同舟共济",
                                "left_zh": "同舟共济",
                                "right": "Work together in difficult times",
                                "right_zh": "困难时期共同合作"
                            },
                            {
                                "left": "多元共存",
                                "left_zh": "多元共存",
                                "right": "Diversity and coexistence",
                                "right_zh": "多样性与共存"
                            },
                            {
                                "left": "和衷共济",
                                "left_zh": "和衷共济",
                                "right": "Unity of purpose",
                                "right_zh": "目标一致"
                            }
                        ],
                        "explanation": "These idioms reflect Singapore's values of unity and diversity.",
                        "explanation_zh": "这些成语反映了新加坡团结和多元化的价值观。"
                    },
                    {
                        "id": "idiom-ex11",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "What does 百闻不如一见 mean?",
                        "prompt_zh": "\"百闻不如一见\"是什么意思？",
                        "choices": [
                            "Seeing once is better than hearing a hundred times",
                            "Hearing is better than seeing",
                            "One hundred is more than one",
                            "Listening carefully is important"
                        ],
                        "choices_zh": [
                            "看一次比听一百次好",
                            "听比看好",
                            "一百比一多",
                            "认真听很重要"
                        ],
                        "answer": 0,
                        "explanation": "This idiom means 'seeing is believing' - direct experience is better than hearsay.",
                        "explanation_zh": "这个成语意思是\"眼见为实\"——直接经验比道听途说好。"
                    },
                    {
                        "id": "idiom-ex12",
                        "type": "mcq",
                        "difficulty": "hard",
                        "prompt": "Which idiom describes 'turning a crisis into an opportunity'?",
                        "prompt_zh": "哪个成语形容\"化危机为机遇\"？",
                        "choices": [
                            "转危为安",
                            "雪上加霜",
                            "落井下石",
                            "火上浇油"
                        ],
                        "choices_zh": [
                            "转危为安",
                            "雪上加霜",
                            "落井下石",
                            "火上浇油"
                        ],
                        "answer": 0,
                        "explanation": "转危为安 means turning danger into safety.",
                        "explanation_zh": "\"转危为安\"意思是化危险为安全。"
                    },
                    {
                        "id": "idiom-ex13",
                        "type": "mcq",
                        "difficulty": "easy",
                        "prompt": "What does 积少成多 mean?",
                        "prompt_zh": "\"积少成多\"是什么意思？",
                        "choices": [
                            "Many small things add up",
                            "Less is more",
                            "More is less",
                            "Small is beautiful"
                        ],
                        "choices_zh": [
                            "许多小东西积累起来",
                            "少即是多",
                            "多即是少",
                            "小即美"
                        ],
                        "answer": 0,
                        "explanation": "积少成多 means small amounts can accumulate to large amounts.",
                        "explanation_zh": "\"积少成多\"意思是少量积累可以变成大量。"
                    },
                    {
                        "id": "idiom-ex14",
                        "type": "mcq",
                        "difficulty": "medium",
                        "prompt": "Which idiom means 'to help someone when they are in need'?",
                        "prompt_zh": "哪个成语的意思是\"在别人需要时帮助他们\"？",
                        "choices": [
                            "落井下石",
                            "雪中送炭",
                            "锦上添花",
                            "趁火打劫"
                        ],
                        "choices_zh": [
                            "落井下石",
                            "雪中送炭",
                            "锦上添花",
                            "趁火打劫"
                        ],
                        "answer": 1,
                        "explanation": "雪中送炭 literally means 'sending charcoal in snow' - helping when most needed.",
                        "explanation_zh": "\"雪中送炭\"字面意思是\"在雪中送炭\"——在最需要时提供帮助。"
                    },
                    {
                        "id": "idiom-ex15",
                        "type": "drag-order",
                        "difficulty": "hard",
                        "prompt": "Arrange the story sequence of 守株待兔:",
                        "prompt_zh": "按\"守株待兔\"的故事顺序排列：",
                        "items": [
                            "A farmer saw a rabbit hit a tree",
                            "He waited by the tree daily",
                            "The rabbit died from the impact",
                            "His fields became barren"
                        ],
                        "items_zh": [
                            "农夫看到兔子撞树",
                            "他每天在树旁等待",
                            "兔子撞死了",
                            "他的田地荒芜了"
                        ],
                        "answer": [
                            "A farmer saw a rabbit hit a tree",
                            "The rabbit died from the impact",
                            "He waited by the tree daily",
                            "His fields became barren"
                        ],
                        "explanation": "This story teaches us not to rely on luck instead of hard work.",
                        "explanation_zh": "这个故事告诉我们不要依赖运气而不努力工作。"
                    }
                ]

                # Extend existing exercises
                chapter['exercises'].extend(new_exercises)
                print(f"Added {len(new_exercises)} exercises to Idioms & Proverbs")
                print(f"Total exercises now: {len(chapter['exercises'])}")

# Save updated content
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✓ Idioms & Proverbs exercises updated successfully!")
