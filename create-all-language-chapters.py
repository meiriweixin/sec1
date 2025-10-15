import json
import os

# Create chapters directory
os.makedirs('chapters', exist_ok=True)

# English Chapter 3: Sentence Construction
sentence_construction = {
    "id": "sentence-construction",
    "title": "Sentence Construction",
    "title_zh": "句子构造",
    "description": "Build strong sentences by avoiding fragments and run-ons",
    "description_zh": "通过避免片段和连写句构建强句子",
    "objectives": ["Identify sentence fragments", "Fix run-on sentences", "Use sentence variety"],
    "objectives_zh": ["识别句子片段", "修正连写句", "使用句子多样性"],
    "sections": [
        {
            "id": "fragments",
            "type": "text",
            "title": "Avoiding Sentence Fragments",
            "title_zh": "避免句子片段",
            "content": "A **sentence fragment** is an incomplete sentence missing a subject, verb, or complete thought.\n\n**Examples of Fragments:**\n- ❌ Because it was raining.\n- ❌ The tall building near my school.\n- ❌ Running down the street.\n\n**How to Fix:**\n1. Add missing subject or verb\n2. Connect to a complete sentence\n3. Remove subordinating conjunction\n\n**Fixed:**\n- ✅ Because it was raining, we stayed inside.\n- ✅ The tall building near my school is new.\n- ✅ The boy was running down the street.",
            "content_zh": "**句子片段**是缺少主语、动词或完整思想的不完整句子。\n\n**片段例子：**\n- ❌ 因为下雨。\n- ❌ 我学校附近的高楼。\n- ❌ 沿着街道跑。\n\n**如何修正：**\n1. 添加缺少的主语或动词\n2. 连接到完整句子\n3. 删除从属连词\n\n**修正后：**\n- ✅ 因为下雨，我们待在室内。\n- ✅ 我学校附近的高楼是新的。\n- ✅ 男孩沿着街道跑。"
        },
        {
            "id": "run-ons",
            "type": "text",
            "title": "Fixing Run-on Sentences",
            "title_zh": "修正连写句",
            "content": "**Run-on sentences** join two complete sentences incorrectly.\n\n**Types:**\n\n**1. Fused Sentences** (no punctuation)\n- ❌ I love durian my sister hates it.\n\n**2. Comma Splice** (only comma)\n- ❌ I love durian, my sister hates it.\n\n**How to Fix:**\n\n**Method 1:** Period\n- ✅ I love durian. My sister hates it.\n\n**Method 2:** Comma + Coordinating Conjunction\n- ✅ I love durian, but my sister hates it.\n\n**Method 3:** Semicolon\n- ✅ I love durian; my sister hates it.\n\n**Method 4:** Subordinating Conjunction\n- ✅ Although I love durian, my sister hates it.",
            "content_zh": "**连写句**不正确地连接两个完整句子。\n\n**类型：**\n\n**1. 融合句**（没有标点）\n- ❌ 我爱榴莲我姐姐讨厌它。\n\n**2. 逗号错误**（只有逗号）\n- ❌ 我爱榴莲，我姐姐讨厌它。\n\n**如何修正：**\n\n**方法1：**句号\n- ✅ 我爱榴莲。我姐姐讨厌它。\n\n**方法2：**逗号+并列连词\n- ✅ 我爱榴莲，但我姐姐讨厌它。\n\n**方法3：**分号\n- ✅ 我爱榴莲；我姐姐讨厌它。\n\n**方法4：**从属连词\n- ✅ 虽然我爱榴莲，我姐姐讨厌它。"
        },
        {
            "id": "variety",
            "type": "text",
            "title": "Sentence Variety",
            "title_zh": "句子多样性",
            "content": "Use different sentence types for better writing.\n\n**Vary Sentence Length:**\n- Short: It was hot.\n- Medium: The weather was extremely hot today.\n- Long: Because the weather was extremely hot today, we decided to stay indoors and use the air conditioning.\n\n**Vary Sentence Beginnings:**\n- Subject: The students worked hard.\n- Adverb: Yesterday, the students worked hard.\n- Prepositional phrase: In the library, the students worked hard.\n- Dependent clause: While preparing for exams, the students worked hard.\n\n**Vary Sentence Types:**\n- Simple: I went to school.\n- Compound: I went to school, and I studied hard.\n- Complex: Because I studied hard, I passed the exam.",
            "content_zh": "使用不同的句子类型以获得更好的写作。\n\n**变化句子长度：**\n- 短：天气热。\n- 中：今天天气非常热。\n- 长：因为今天天气非常热，我们决定待在室内使用空调。\n\n**变化句子开头：**\n- 主语：学生们努力学习。\n- 副词：昨天，学生们努力学习。\n- 介词短语：在图书馆，学生们努力学习。\n- 从属子句：在准备考试时，学生们努力学习。\n\n**变化句子类型：**\n- 简单：我去上学。\n- 并列：我去上学，我努力学习。\n- 复杂：因为我努力学习，我通过了考试。"
        }
    ],
    "exercises": [
        {"id": "ex1", "type": "mcq", "question": "Which is a sentence fragment?", "question_zh": "哪个是句子片段？",
         "choices": ["Because it was late.", "It was late.", "I went home because it was late.", "It was late, so I went home."],
         "choices_zh": ["因为很晚了。", "很晚了。", "我回家因为很晚了。", "很晚了，所以我回家了。"],
         "answer": 0, "explanation": "Missing main clause after 'Because'.", "explanation_zh": "'Because'后面缺少主句。"},
        {"id": "ex2", "type": "mcq", "question": "Which fixes this run-on? 'I like pizza my brother likes pasta'",
         "question_zh": "哪个修正了这个连写句？'我喜欢披萨我哥哥喜欢意大利面'",
         "choices": ["I like pizza my brother likes pasta.", "I like pizza, my brother likes pasta.",
                    "I like pizza, but my brother likes pasta.", "I like pizza my brother, likes pasta."],
         "choices_zh": ["我喜欢披萨我哥哥喜欢意大利面。", "我喜欢披萨，我哥哥喜欢意大利面。",
                       "我喜欢披萨，但我哥哥喜欢意大利面。", "我喜欢披萨我哥哥，喜欢意大利面。"],
         "answer": 2, "explanation": "Use comma + coordinating conjunction.", "explanation_zh": "使用逗号+并列连词。"},
        {"id": "ex3", "type": "short", "question": "Fix: 'Walking to school.'", "question_zh": "修正：'走到学校。'",
         "answer": "I was walking to school.", "validator": "exact", "explanation": "Add subject and helping verb.",
         "explanation_zh": "添加主语和助动词。"},
        {"id": "ex4", "type": "mcq", "question": "What's wrong? 'I studied hard, I passed the exam.'",
         "question_zh": "有什么问题？'我努力学习，我通过了考试。'",
         "choices": ["Sentence fragment", "Comma splice", "Nothing wrong", "Wrong verb tense"],
         "choices_zh": ["句子片段", "逗号错误", "没有问题", "动词时态错误"],
         "answer": 1, "explanation": "Two sentences joined only with comma.", "explanation_zh": "两个句子只用逗号连接。"},
        {"id": "ex5", "type": "mcq", "question": "Best sentence variety?", "question_zh": "最好的句子多样性？",
         "choices": ["All short sentences", "All long sentences", "Mix of short and long", "Only compound sentences"],
         "choices_zh": ["全部短句", "全部长句", "短句和长句混合", "只有并列句"],
         "answer": 2, "explanation": "Variety makes writing more interesting.", "explanation_zh": "多样性使写作更有趣。"}
    ]
}

# English Chapter 4: Narrative Writing
narrative_writing = {
    "id": "narrative-writing",
    "title": "Narrative Writing",
    "title_zh": "叙事写作",
    "description": "Master storytelling techniques and narrative structure",
    "description_zh": "掌握讲故事技巧和叙事结构",
    "objectives": ["Understand story structure", "Use descriptive language", "Apply 'show don't tell'"],
    "objectives_zh": ["理解故事结构", "使用描述性语言", "应用'展示而非叙述'"],
    "sections": [
        {
            "id": "story-structure",
            "type": "text",
            "title": "Story Structure",
            "title_zh": "故事结构",
            "content": "**Five-Part Story Structure:**\n\n**1. Exposition** - Introduction\n- Introduce characters, setting, situation\n- Example: 'It was a hot afternoon in Singapore. Ahmad waited nervously at the bus stop.'\n\n**2. Rising Action** - Build tension\n- Events leading to climax\n- Complications arise\n- Example: 'He realized he had forgotten his wallet.'\n\n**3. Climax** - Turning point\n- Most exciting/intense moment\n- Main conflict confronted\n- Example: 'The bus arrived. Ahmad had to decide.'\n\n**4. Falling Action** - After climax\n- Consequences unfold\n- Example: 'He explained his situation to the bus driver.'\n\n**5. Resolution** - Ending\n- Conflict resolved\n- Example: 'The kind driver let him board and Ahmad promised to pay tomorrow.'",
            "content_zh": "**五部分故事结构：**\n\n**1. 开端** - 介绍\n- 介绍人物、环境、情况\n- 例子：'新加坡的一个炎热下午。Ahmad在公交站紧张地等待。'\n\n**2. 上升动作** - 建立紧张感\n- 导致高潮的事件\n- 出现复杂情况\n- 例子：'他意识到他忘记了钱包。'\n\n**3. 高潮** - 转折点\n- 最激动人心/紧张的时刻\n- 主要冲突面对\n- 例子：'公交车到了。Ahmad必须决定。'\n\n**4. 下降动作** - 高潮之后\n- 后果展开\n- 例子：'他向司机解释了他的情况。'\n\n**5. 结局** - 结束\n- 冲突解决\n- 例子：'善良的司机让他上车，Ahmad承诺明天付款。'"
        },
        {
            "id": "descriptive-language",
            "type": "text",
            "title": "Descriptive Language",
            "title_zh": "描述性语言",
            "content": "**Use the Five Senses:**\n\n**Sight:** colors, shapes, sizes\n- The golden sunset painted the sky orange.\n\n**Sound:** loud, soft, musical, harsh\n- The hawker center buzzed with chatter.\n\n**Smell:** fragrant, pungent, fresh\n- The aroma of chicken rice filled the air.\n\n**Touch:** smooth, rough, hot, cold\n- The humid air clung to my skin.\n\n**Taste:** sweet, sour, bitter, salty\n- The tangy lime juice made me pucker.\n\n**Strong Verbs:**\n- Weak: walked slowly → Strong: trudged\n- Weak: looked quickly → Strong: glanced\n- Weak: said loudly → Strong: shouted\n\n**Specific Nouns:**\n- General: flower → Specific: orchid\n- General: building → Specific: HDB flat\n- General: food → Specific: laksa",
            "content_zh": "**使用五感：**\n\n**视觉：**颜色、形状、大小\n- 金色的日落将天空涂成橙色。\n\n**听觉：**大声、柔和、悦耳、刺耳\n- 小贩中心充满了喋喋不休的声音。\n\n**嗅觉：**芬芳、刺鼻、新鲜\n- 鸡饭的香味充满了空气。\n\n**触觉：**光滑、粗糙、热、冷\n- 潮湿的空气粘在我的皮肤上。\n\n**味觉：**甜、酸、苦、咸\n- 酸的青柠汁让我皱眉。\n\n**强动词：**\n- 弱：慢慢走 → 强：跋涉\n- 弱：快速看 → 强：瞥见\n- 弱：大声说 → 强：喊叫\n\n**具体名词：**\n- 一般：花 → 具体：兰花\n- 一般：建筑 → 具体：组屋\n- 一般：食物 → 具体：叻沙"
        },
        {
            "id": "show-dont-tell",
            "type": "text",
            "title": "Show, Don't Tell",
            "title_zh": "展示，而非叙述",
            "content": "**Show** readers what's happening through actions, dialogue, and details.\n\n**Telling vs Showing:**\n\n**Tell:** She was nervous.\n**Show:** Her hands trembled as she clutched her exam paper.\n\n**Tell:** He was angry.\n**Show:** His face turned red, and he clenched his fists.\n\n**Tell:** The hawker center was busy.\n**Show:** People jostled for tables while vendors shouted orders over the sizzle of woks.\n\n**Tell:** It was hot.\n**Show:** Sweat dripped down my back as I fanned myself with a newspaper.\n\n**Techniques:**\n1. Use action verbs\n2. Include sensory details\n3. Add dialogue\n4. Describe body language\n5. Show reactions\n\n**Singapore Example:**\n**Tell:** The MRT was crowded.\n**Show:** Bodies pressed together as the doors struggled to close, and the automated voice warned, 'Please move to the center of the train.'",
            "content_zh": "通过动作、对话和细节向读者**展示**正在发生的事情。\n\n**叙述与展示：**\n\n**叙述：**她很紧张。\n**展示：**她紧握试卷时手在颤抖。\n\n**叙述：**他很生气。\n**展示：**他的脸变红了，他握紧了拳头。\n\n**叙述：**小贩中心很忙。\n**展示：**人们争夺桌子，小贩在炒锅的嘶嘶声中喊订单。\n\n**叙述：**天气很热。\n**展示：**汗水顺着我的背流下，我用报纸扇着自己。\n\n**技巧：**\n1. 使用动作动词\n2. 包括感官细节\n3. 添加对话\n4. 描述肢体语言\n5. 展示反应\n\n**新加坡例子：**\n**叙述：**地铁很拥挤。\n**展示：**身体挤在一起，门难以关闭，自动语音警告'请移动到列车中央。'"
        }
    ],
    "exercises": [
        {"id": "ex1", "type": "mcq", "question": "What is the climax?", "question_zh": "什么是高潮？",
         "choices": ["Introduction", "Turning point", "Ending", "Beginning conflict"],
         "choices_zh": ["介绍", "转折点", "结局", "开始冲突"],
         "answer": 1, "explanation": "Climax is the most intense moment.", "explanation_zh": "高潮是最紧张的时刻。"},
        {"id": "ex2", "type": "mcq", "question": "Which shows, not tells? 'He was tired.'",
         "question_zh": "哪个展示而非叙述？'他很累。'",
         "choices": ["He was very tired.", "He felt tired.", "His eyes drooped and he yawned.", "He said he was tired."],
         "choices_zh": ["他非常累。", "他感到累。", "他的眼睛下垂，他打哈欠。", "他说他很累。"],
         "answer": 2, "explanation": "Shows tiredness through actions.", "explanation_zh": "通过动作展示疲倦。"},
        {"id": "ex3", "type": "mcq", "question": "Best descriptive language?", "question_zh": "最好的描述性语言？",
         "choices": ["The food was good.", "The food tasted nice.", "The spicy laksa warmed my throat.", "I liked the food."],
         "choices_zh": ["食物很好。", "食物很好吃。", "辣的叻沙温暖了我的喉咙。", "我喜欢食物。"],
         "answer": 2, "explanation": "Uses specific details and sensory language.", "explanation_zh": "使用具体细节和感官语言。"},
        {"id": "ex4", "type": "mcq", "question": "What comes after rising action?", "question_zh": "上升动作之后是什么？",
         "choices": ["Exposition", "Climax", "Resolution", "Characters"],
         "choices_zh": ["开端", "高潮", "结局", "人物"],
         "answer": 1, "explanation": "Climax follows rising action.", "explanation_zh": "高潮跟随上升动作。"},
        {"id": "ex5", "type": "short", "question": "Rewrite showing: 'She was happy.'", "question_zh": "重写展示：'她很高兴。'",
         "answer": "She smiled brightly and jumped with joy.", "validator": "exact",
         "explanation": "Show happiness through actions.", "explanation_zh": "通过动作展示快乐。"}
    ]
}

# Save these two chapters
with open('chapters/english-sentence-construction.json', 'w', encoding='utf-8') as f:
    json.dump(sentence_construction, f, indent=2, ensure_ascii=False)

with open('chapters/english-narrative-writing.json', 'w', encoding='utf-8') as f:
    json.dump(narrative_writing, f, indent=2, ensure_ascii=False)

print('Created chapters 3-4!')
print('Creating chapters 5-6...')
