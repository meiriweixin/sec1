#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create all 6 Chinese Language (华文) chapters with full bilingual support
"""

import json
import os

# Create chapters directory if it doesn't exist
os.makedirs('chapters', exist_ok=True)

# Chapter 1: Grammar Fundamentals (语法基础)
grammar_fundamentals = {
    "id": "chinese-grammar-fundamentals",
    "title": "Grammar Fundamentals (语法基础)",
    "title_zh": "语法基础",
    "description": "Master fundamental Chinese grammar including sentence structure, measure words, and word order",
    "description_zh": "掌握中文语法基础，包括句子结构、量词和词序",
    "objectives": [
        "Understand Subject-Verb-Object (主谓宾) sentence structure",
        "Master the use of measure words (量词)",
        "Apply correct word order in Chinese sentences",
        "Recognize and use common sentence patterns"
    ],
    "objectives_zh": [
        "理解主谓宾句子结构",
        "掌握量词的使用",
        "应用中文句子中的正确词序",
        "识别和使用常见句型"
    ],
    "sections": [
        {
            "id": "sentence-structure",
            "type": "text",
            "title": "Sentence Structure (主谓宾)",
            "title_zh": "句子结构（主谓宾）",
            "content": """**Basic Chinese Sentence Pattern: Subject (主语) + Verb (谓语) + Object (宾语)**

The most basic sentence structure in Chinese follows the Subject-Verb-Object pattern.

**Examples:**
- 我 (I) + 吃 (eat) + 饭 (rice) = 我吃饭。
- 他 (he) + 看 (read) + 书 (book) = 他看书。
- 我们 (we) + 学 (study) + 中文 (Chinese) = 我们学中文。

**With Time Expression:**
Time words usually come after the subject or at the beginning.

- 我**今天**吃饭。(I eat today.)
- **今天**我吃饭。(Today I eat.)

**With Place Expression:**
Place words come before the verb.

- 我**在学校**学中文。(I study Chinese at school.)
- 他**在图书馆**看书。(He reads books in the library.)

**Singapore Context:**
- 我在新加坡学习。(I study in Singapore.)
- 我们在小贩中心吃饭。(We eat at the hawker centre.)""",
            "content_zh": """**基本中文句型：主语 + 谓语 + 宾语**

中文最基本的句子结构遵循主谓宾模式。

**例子：**
- 我（主语）+ 吃（谓语）+ 饭（宾语）= 我吃饭。
- 他（主语）+ 看（谓语）+ 书（宾语）= 他看书。
- 我们（主语）+ 学（谓语）+ 中文（宾语）= 我们学中文。

**带时间状语：**
时间词通常放在主语后或句首。

- 我**今天**吃饭。
- **今天**我吃饭。

**带地点状语：**
地点词放在动词前。

- 我**在学校**学中文。
- 他**在图书馆**看书。

**新加坡语境：**
- 我在新加坡学习。
- 我们在小贩中心吃饭。"""
        },
        {
            "id": "measure-words",
            "type": "text",
            "title": "Measure Words (量词)",
            "title_zh": "量词",
            "content": """**What are Measure Words?**
In Chinese, you cannot say "one book" directly. You must use a measure word between the number and the noun: "一**本**书" (one **[measure word]** book).

**Common Measure Words:**

**个 (gè)** - General measure word
- 一个人 (one person)
- 两个苹果 (two apples)
- 三个问题 (three questions)

**本 (běn)** - Books, notebooks
- 一本书 (one book)
- 两本杂志 (two magazines)

**张 (zhāng)** - Flat objects (paper, tables, beds)
- 一张纸 (one piece of paper)
- 三张桌子 (three tables)
- 一张床 (one bed)

**件 (jiàn)** - Clothing, matters
- 一件衣服 (one piece of clothing)
- 两件事 (two matters)

**支 (zhī)** - Long thin objects (pens, pencils)
- 一支笔 (one pen)
- 两支铅笔 (two pencils)

**条 (tiáo)** - Long flexible objects (roads, rivers, fish)
- 一条路 (one road)
- 一条河 (one river)
- 一条鱼 (one fish)

**只 (zhī)** - Animals, one of a pair
- 一只猫 (one cat)
- 两只鸟 (two birds)
- 一只手 (one hand)

**Singapore Examples:**
- 一**碗**叻沙 (one bowl of laksa)
- 两**杯**咖啡 (two cups of coffee)
- 三**张**组屋 (three HDB flats) - Note: In Singapore, we often say 三**个**组屋""",
            "content_zh": """**什么是量词？**
在中文中，你不能直接说"一书"。你必须在数字和名词之间使用量词："一**本**书"。

**常用量词：**

**个（gè）** - 通用量词
- 一个人
- 两个苹果
- 三个问题

**本（běn）** - 书、笔记本
- 一本书
- 两本杂志

**张（zhāng）** - 扁平物体（纸、桌子、床）
- 一张纸
- 三张桌子
- 一张床

**件（jiàn）** - 衣服、事情
- 一件衣服
- 两件事

**支（zhī）** - 细长物体（笔）
- 一支笔
- 两支铅笔

**条（tiáo）** - 细长柔软物体（路、河、鱼）
- 一条路
- 一条河
- 一条鱼

**只（zhī）** - 动物、成对物体之一
- 一只猫
- 两只鸟
- 一只手

**新加坡例子：**
- 一**碗**叻沙
- 两**杯**咖啡
- 三**个**组屋"""
        },
        {
            "id": "word-order",
            "type": "text",
            "title": "Word Order Rules",
            "title_zh": "词序规则",
            "content": """**Standard Word Order in Chinese:**

**1. Time + Subject + Place + Manner + Verb + Object**

- (今天) + 我 + (在学校) + (认真地) + 学习 + 中文
- (Today) + I + (at school) + (seriously) + study + Chinese

**2. Time Position:**
- ✅ 我**昨天**去了图书馆。(I went to the library yesterday.)
- ✅ **昨天**我去了图书馆。(Yesterday I went to the library.)
- ❌ 我去了图书馆**昨天**。(WRONG in Chinese!)

**3. Place Before Verb:**
- ✅ 我**在家**吃饭。(I eat at home.)
- ❌ 我吃饭**在家**。(WRONG!)

**4. Manner Before Verb:**
- ✅ 他**慢慢地**走。(He walks slowly.)
- ❌ 他走**慢慢地**。(WRONG!)

**5. Duration After Verb:**
- ✅ 我学了**两年**中文。(I studied Chinese for two years.)
- ❌ 我学中文**两年**了。(Less common)

**Question Words Stay in Place:**
Unlike English, question words don't move to the front.

- English: **What** do you eat? (What moves to front)
- Chinese: 你吃**什么**？(What stays in object position)

**Singapore Context:**
- 我**每天**在新加坡**坐地铁**。(I take the MRT in Singapore every day.)
- 我们**通常**在小贩中心**吃午饭**。(We usually eat lunch at hawker centres.)""",
            "content_zh": """**中文标准词序：**

**1. 时间 + 主语 + 地点 + 方式 + 动词 + 宾语**

- （今天）+ 我 + （在学校）+ （认真地）+ 学习 + 中文

**2. 时间位置：**
- ✅ 我**昨天**去了图书馆。
- ✅ **昨天**我去了图书馆。
- ❌ 我去了图书馆**昨天**。（错误！）

**3. 地点在动词前：**
- ✅ 我**在家**吃饭。
- ❌ 我吃饭**在家**。（错误！）

**4. 方式在动词前：**
- ✅ 他**慢慢地**走。
- ❌ 他走**慢慢地**。（错误！）

**5. 时量在动词后：**
- ✅ 我学了**两年**中文。
- ❌ 我学中文**两年**了。（较少用）

**疑问词保持原位：**
与英语不同，疑问词不移到句首。

- 英语：**What** do you eat?（What移到前面）
- 中文：你吃**什么**？（什么保持在宾语位置）

**新加坡语境：**
- 我**每天**在新加坡**坐地铁**。
- 我们**通常**在小贩中心**吃午饭**。"""
        }
    ],
    "exercises": [
        {
            "id": "ex1",
            "type": "drag-order",
            "question": "Arrange these words in correct order: 我 / 在学校 / 学习 / 认真地 / 中文",
            "question_zh": "将这些词排列成正确的顺序：我 / 在学校 / 学习 / 认真地 / 中文",
            "items": ["我", "在学校", "认真地", "学习", "中文"],
            "correctOrder": ["我", "在学校", "认真地", "学习", "中文"],
            "explanation": "Correct order: Subject + Place + Manner + Verb + Object",
            "explanation_zh": "正确顺序：主语 + 地点 + 方式 + 动词 + 宾语"
        },
        {
            "id": "ex2",
            "type": "mcq",
            "question": "Choose the correct measure word: 一___书",
            "question_zh": "选择正确的量词：一___书",
            "choices": ["个", "本", "张", "支"],
            "choices_zh": ["个", "本", "张", "支"],
            "answer": 1,
            "explanation": "Books use the measure word '本' (běn)",
            "explanation_zh": "书用量词'本'"
        },
        {
            "id": "ex3",
            "type": "mcq",
            "question": "Which sentence has correct word order?",
            "question_zh": "哪个句子的词序正确？",
            "choices": [
                "我去了图书馆昨天。",
                "昨天我去了图书馆。",
                "我昨天了去图书馆。",
                "图书馆我去了昨天。"
            ],
            "choices_zh": [
                "我去了图书馆昨天。",
                "昨天我去了图书馆。",
                "我昨天了去图书馆。",
                "图书馆我去了昨天。"
            ],
            "answer": 1,
            "explanation": "Time expressions can come at the beginning or after the subject, but not at the end.",
            "explanation_zh": "时间状语可以放在句首或主语后，但不能放在句尾。"
        },
        {
            "id": "ex4",
            "type": "mcq",
            "question": "Choose the correct sentence:",
            "question_zh": "选择正确的句子：",
            "choices": [
                "我吃饭在家。",
                "我在家吃饭。",
                "在家我吃饭。",
                "吃饭我在家。"
            ],
            "choices_zh": [
                "我吃饭在家。",
                "我在家吃饭。",
                "在家我吃饭。",
                "吃饭我在家。"
            ],
            "answer": 1,
            "explanation": "Place expressions come before the verb: 我在家吃饭",
            "explanation_zh": "地点状语放在动词前：我在家吃饭"
        },
        {
            "id": "ex5",
            "type": "short",
            "question": "Fill in the correct measure word: 三___猫",
            "question_zh": "填入正确的量词：三___猫",
            "answer": "只",
            "validator": "exact",
            "explanation": "Animals use the measure word '只' (zhī)",
            "explanation_zh": "动物用量词'只'"
        }
    ]
}

# Chapter 2: Vocabulary Building (词汇积累)
vocabulary_building = {
    "id": "chinese-vocabulary-building",
    "title": "Vocabulary Building (词汇积累)",
    "title_zh": "词汇积累",
    "description": "Build your Chinese vocabulary through word combinations, radicals, and character analysis",
    "description_zh": "通过词语搭配、部首和字形分析来积累中文词汇",
    "objectives": [
        "Master common word combinations (词语搭配)",
        "Understand radicals and their meanings (部首)",
        "Analyze character components to remember words",
        "Expand vocabulary in context"
    ],
    "objectives_zh": [
        "掌握常见词语搭配",
        "理解部首及其含义",
        "分析字形组成以记忆词语",
        "在语境中扩展词汇"
    ],
    "sections": [
        {
            "id": "word-combinations",
            "type": "text",
            "title": "Word Combinations (词语搭配)",
            "title_zh": "词语搭配",
            "content": """**What is Word Combination?**
In Chinese, certain words naturally go together. Learning these combinations helps you speak and write more naturally.

**Verb + Noun Combinations:**

**做 (do)**
- 做作业 (do homework)
- 做饭 (cook)
- 做运动 (do sports)
- 做决定 (make a decision)

**打 (hit/play)**
- 打球 (play ball)
- 打电话 (make a phone call)
- 打工 (work part-time)
- 打扫 (clean)

**上 (go to/attend)**
- 上学 (go to school)
- 上课 (attend class)
- 上网 (go online)
- 上班 (go to work)

**Adjective + Noun Combinations:**

**重要的 (important)**
- 重要的事情 (important matter)
- 重要的人物 (important person)
- 重要的决定 (important decision)

**美丽的 (beautiful)**
- 美丽的风景 (beautiful scenery)
- 美丽的花朵 (beautiful flowers)

**Singapore Context:**
- 坐地铁 (take the MRT)
- 吃辣椒螃蟹 (eat chilli crab)
- 去牛车水 (go to Chinatown)""",
            "content_zh": """**什么是词语搭配？**
在中文中，某些词语自然地搭配在一起。学习这些搭配有助于你更自然地说和写。

**动词 + 名词搭配：**

**做**
- 做作业
- 做饭
- 做运动
- 做决定

**打**
- 打球
- 打电话
- 打工
- 打扫

**上**
- 上学
- 上课
- 上网
- 上班

**形容词 + 名词搭配：**

**重要的**
- 重要的事情
- 重要的人物
- 重要的决定

**美丽的**
- 美丽的风景
- 美丽的花朵

**新加坡语境：**
- 坐地铁
- 吃辣椒螃蟹
- 去牛车水"""
        },
        {
            "id": "radicals",
            "type": "text",
            "title": "Radicals (部首)",
            "title_zh": "部首",
            "content": """**What are Radicals?**
Radicals are components of Chinese characters that often indicate meaning or pronunciation. Understanding radicals helps you guess the meaning of unfamiliar characters and remember characters better.

**Common Radicals and Their Meanings:**

**氵(水) - Water radical**
- 河 (river)
- 海 (sea)
- 湖 (lake)
- 汗 (sweat)
- 游 (swim)

**讠(言) - Speech radical**
- 说 (speak)
- 话 (words)
- 语 (language)
- 谢 (thank)
- 请 (please/invite)

**亻(人) - Person radical**
- 你 (you)
- 他 (he)
- 们 (plural marker)
- 休 (rest)
- 体 (body)

**木 - Wood/tree radical**
- 树 (tree)
- 林 (forest)
- 桌 (table)
- 椅 (chair)
- 果 (fruit)

**心/忄- Heart radical (emotions)**
- 想 (think)
- 念 (miss/think of)
- 忙 (busy)
- 快 (quick/happy)
- 怕 (afraid)

**手/扌- Hand radical (actions)**
- 打 (hit)
- 拿 (take)
- 把 (hold)
- 推 (push)
- 拉 (pull)

**口 - Mouth radical**
- 吃 (eat)
- 喝 (drink)
- 唱 (sing)
- 叫 (call)
- 吗 (question particle)

**Using Radicals to Remember:**
- 游 (swim) = 氵(water) + 方向 → Swimming in water
- 说 (speak) = 讠(speech) + 兑 → Using speech to speak
- 想 (think) = 相 (mutual) + 心 (heart) → Thinking with your heart""",
            "content_zh": """**什么是部首？**
部首是汉字的组成部分，通常表示意义或读音。理解部首有助于你猜测生字的意思，更好地记住汉字。

**常见部首及其含义：**

**氵（水）- 水部**
- 河
- 海
- 湖
- 汗
- 游

**讠（言）- 言字旁**
- 说
- 话
- 语
- 谢
- 请

**亻（人）- 单人旁**
- 你
- 他
- 们
- 休
- 体

**木 - 木字旁**
- 树
- 林
- 桌
- 椅
- 果

**心/忄- 心字底/竖心旁（情感）**
- 想
- 念
- 忙
- 快
- 怕

**手/扌- 提手旁（动作）**
- 打
- 拿
- 把
- 推
- 拉

**口 - 口字旁**
- 吃
- 喝
- 唱
- 叫
- 吗

**用部首记忆：**
- 游 = 氵（水）+ 方向 → 在水中游
- 说 = 讠（言）+ 兑 → 用言语说
- 想 = 相 + 心 → 用心想"""
        }
    ],
    "exercises": [
        {
            "id": "ex1",
            "type": "match",
            "question": "Match the words with their correct combinations:",
            "question_zh": "将词语与其正确的搭配连线：",
            "pairs": [
                {"left": "做", "right": "作业", "left_zh": "做", "right_zh": "作业"},
                {"left": "打", "right": "电话", "left_zh": "打", "right_zh": "电话"},
                {"left": "上", "right": "学", "left_zh": "上", "right_zh": "学"}
            ],
            "explanation": "做作业 (do homework), 打电话 (make a phone call), 上学 (go to school)",
            "explanation_zh": "做作业、打电话、上学是常见的动词搭配"
        },
        {
            "id": "ex2",
            "type": "mcq",
            "question": "Which radical indicates 'water'?",
            "question_zh": "哪个部首表示'水'？",
            "choices": ["氵", "讠", "亻", "木"],
            "choices_zh": ["氵", "讠", "亻", "木"],
            "answer": 0,
            "explanation": "氵is the water radical, found in characters like 河 (river) and 海 (sea)",
            "explanation_zh": "氵是水部，出现在河、海等字中"
        },
        {
            "id": "ex3",
            "type": "mcq",
            "question": "What does the radical 讠(言) typically indicate?",
            "question_zh": "部首讠（言）通常表示什么？",
            "choices": [
                "Water-related meanings",
                "Speech or language-related meanings",
                "Tree or wood-related meanings",
                "Emotion-related meanings"
            ],
            "choices_zh": [
                "与水有关的意思",
                "与言语或语言有关的意思",
                "与树木有关的意思",
                "与情感有关的意思"
            ],
            "answer": 1,
            "explanation": "讠(言) indicates speech or language, as in 说 (speak) and 语 (language)",
            "explanation_zh": "讠（言）表示言语或语言，如说、语等字"
        },
        {
            "id": "ex4",
            "type": "short",
            "question": "What radical would you find in characters related to emotions?",
            "question_zh": "在与情感有关的字中，你会找到什么部首？",
            "answer": "心",
            "validator": "exact",
            "explanation": "心 (heart) radical appears in emotion-related characters like 想 (think) and 怕 (afraid)",
            "explanation_zh": "心（心）部首出现在情感相关的字中，如想、怕"
        }
    ]
}

# Save all chapters
chapters = [
    ('grammar-fundamentals', grammar_fundamentals),
    ('vocabulary-building', vocabulary_building)
]

for filename, chapter_data in chapters:
    filepath = f'chapters/chinese-{filename}.json'
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(chapter_data, f, ensure_ascii=False, indent=2)
    print(f"✅ Created {filepath}")

print(f"\n✨ Successfully created {len(chapters)} Chinese language chapters!")
print("\nNext steps:")
print("1. Run integrate-language-subjects.py to add both English and Chinese language subjects to content.json")
