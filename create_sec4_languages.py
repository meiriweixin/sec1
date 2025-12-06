#!/usr/bin/env python3
"""Create Sec 4 English and Chinese Language chapters."""
import json
import os

SEC4_ENGLISH_CHAPTERS = [
    {
        "id": "critical-essay-writing-sec4",
        "gradeLevel": "sec4",
        "title": "Critical Essay Writing",
        "title_zh": "批判性论文写作",
        "description": "Write sophisticated argumentative and discursive essays for O-Level examinations",
        "description_zh": "为O水准考试撰写复杂的议论文和论述文",
        "tag": "Writing",
        "tag_zh": "写作",
        "objectives": ["Structure complex argumentative essays", "Develop nuanced thesis statements", "Use advanced rhetorical techniques", "Integrate evidence effectively"],
        "objectives_zh": ["构建复杂议论文结构", "发展细致的论点陈述", "使用高级修辞技巧", "有效整合证据"],
        "sections": [
            {"id": "thesis-development", "title": "Developing Strong Thesis Statements", "title_zh": "发展强有力的论点陈述", "type": "text",
             "content": "A strong thesis guides your entire essay:\n\n**Characteristics of Strong Thesis:**\n- Specific and arguable\n- Takes a clear position\n- Previews main arguments\n\n**Weak:** \"Technology affects education.\"\n**Strong:** \"While technology has revolutionized access to information, its integration in Singapore classrooms must be carefully balanced with traditional teaching methods to ensure deep learning rather than superficial engagement.\"\n\n**Thesis Formula:**\n[Topic] + [Position] + [Reasons/Preview]\n\n**Types of Thesis:**\n1. **Argumentative:** Takes one side\n2. **Analytical:** Examines how/why\n3. **Expository:** Explains a topic\n\n**O-Level Tip:** Your thesis should respond directly to the question and signal your essay's direction."},
            {"id": "essay-structure-advanced", "title": "Advanced Essay Structure", "title_zh": "高级论文结构", "type": "text",
             "content": "**Sophisticated Essay Structure:**\n\n**Introduction:**\n- Hook (relevant, engaging)\n- Context (background information)\n- Thesis (clear position)\n- Roadmap (preview of arguments)\n\n**Body Paragraphs (TEEL+):**\n- Topic sentence (claim)\n- Evidence (specific examples, statistics)\n- Explanation (analysis of evidence)\n- Link (connection to thesis)\n- Extension (broader implications)\n\n**Counterargument Paragraph:**\n- Acknowledge opposing view\n- Concede valid points\n- Refute with stronger evidence\n- Reassert your position\n\n**Conclusion:**\n- Restate thesis (different words)\n- Synthesize key arguments\n- Broader significance\n- Call to action or future outlook\n\n**Word Count Guide:**\nO-Level essays: 350-500 words"},
            {"id": "rhetorical-techniques", "title": "Advanced Rhetorical Techniques", "title_zh": "高级修辞技巧", "type": "text",
             "content": "**Elevate Your Writing:**\n\n**1. Rhetorical Questions**\n\"Can Singapore afford to ignore climate change when our very existence depends on rising sea levels?\"\n\n**2. Tricolon (Rule of Three)**\n\"Education empowers individuals, transforms communities, and elevates nations.\"\n\n**3. Antithesis**\n\"Ask not what your country can do for you, but what you can do for your country.\"\n\n**4. Anaphora (Repetition)**\n\"We must act now. We must act decisively. We must act together.\"\n\n**5. Inclusive Language**\n\"As Singaporeans, we share a responsibility...\"\n\n**6. Expert Integration**\nQuote experts seamlessly: According to Professor Tan, \"education reform is essential.\"\n\n**Avoid:**\n- Clichés\n- Overly emotional language\n- Logical fallacies"}
        ],
        "exercises": [
            {"id": "essay-sec4-ex1", "type": "mcq", "difficulty": "easy", "prompt": "What makes a thesis statement strong?", "prompt_zh": "什么使论点陈述有力？",
             "choices": ["It's vague and general", "It's specific, arguable, and takes a position", "It's very long", "It avoids controversy"],
             "choices_zh": ["模糊笼统", "具体、可辩论并表明立场", "非常长", "避免争议"], "answer": 1,
             "explanation": "**Key Concept:** A strong thesis is specific, arguable, and clearly states your position."},
            {"id": "essay-sec4-ex2", "type": "mcq", "difficulty": "easy", "prompt": "What does TEEL stand for?", "prompt_zh": "TEEL代表什么？",
             "choices": ["Topic, Evidence, Explanation, Link", "Thesis, Example, Ending, Logic", "Text, Edit, Evaluate, Learn", "Time, Effort, Energy, Learning"],
             "choices_zh": ["主题句、证据、解释、链接", "论点、例子、结尾、逻辑", "文本、编辑、评估、学习", "时间、努力、精力、学习"], "answer": 0,
             "explanation": "**Key Concept:** TEEL structures body paragraphs: Topic, Evidence, Explanation, Link."},
            {"id": "essay-sec4-ex3", "type": "mcq", "difficulty": "easy", "prompt": "A tricolon uses:", "prompt_zh": "三叠句使用：",
             "choices": ["Two items", "Three parallel items", "Four questions", "No structure"],
             "choices_zh": ["两个项目", "三个平行项目", "四个问题", "无结构"], "answer": 1,
             "explanation": "**Key Concept:** Tricolon uses three parallel words/phrases for emphasis and rhythm."},
            {"id": "essay-sec4-ex4", "type": "mcq", "difficulty": "easy", "prompt": "Where should counterarguments be addressed?", "prompt_zh": "应该在哪里处理反论点？",
             "choices": ["In the introduction only", "In a dedicated paragraph in the body", "In the conclusion only", "Never address them"],
             "choices_zh": ["仅在引言中", "在正文的专门段落中", "仅在结论中", "永远不要处理"], "answer": 1,
             "explanation": "**Key Concept:** Address counterarguments in the body, typically after your main arguments."},
            {"id": "essay-sec4-ex5", "type": "mcq", "difficulty": "easy", "prompt": "What is anaphora?", "prompt_zh": "什么是首语重复？",
             "choices": ["Using different words", "Repetition at the start of sentences", "Asking questions", "Using contrasts"],
             "choices_zh": ["使用不同的词", "在句子开头重复", "提问", "使用对比"], "answer": 1,
             "explanation": "**Key Concept:** Anaphora repeats words/phrases at the beginning of successive sentences for emphasis."},
            {"id": "essay-sec4-ex6", "type": "mcq", "difficulty": "medium", "prompt": "Which thesis is strongest?", "prompt_zh": "哪个论点最有力？",
             "choices": ["Social media is bad.", "Social media has effects on teenagers.", "Social media's emphasis on curated perfection significantly contributes to anxiety and depression among Singaporean teenagers, requiring urgent intervention from parents and educators.", "I think social media is problematic."],
             "choices_zh": ["社交媒体是坏的。", "社交媒体对青少年有影响。", "社交媒体对完美形象的强调显著导致新加坡青少年的焦虑和抑郁，需要家长和教育者的紧急干预。", "我认为社交媒体有问题。"], "answer": 2,
             "explanation": "**Key Concept:** Option 3 is specific, arguable, states a position, and previews the argument direction."},
            {"id": "essay-sec4-ex7", "type": "mcq", "difficulty": "medium", "prompt": "Which sentence uses antithesis?", "prompt_zh": "哪个句子使用了对比？",
             "choices": ["Singapore is a great country.", "We should not dwell on past failures, but build on future successes.", "Many people like durian.", "The weather is hot today."],
             "choices_zh": ["新加坡是个伟大的国家。", "我们不应该沉溺于过去的失败，而应该在未来的成功上发展。", "许多人喜欢榴莲。", "今天天气很热。"], "answer": 1,
             "explanation": "**Key Concept:** Antithesis contrasts opposing ideas in parallel structure."},
            {"id": "essay-sec4-ex8", "type": "mcq", "difficulty": "medium", "prompt": "What should a conclusion NOT do?", "prompt_zh": "结论不应该做什么？",
             "choices": ["Restate the thesis", "Introduce new arguments", "Summarize key points", "End memorably"],
             "choices_zh": ["重申论点", "引入新论点", "总结要点", "令人难忘地结束"], "answer": 1,
             "explanation": "**Key Concept:** Never introduce new arguments in the conclusion; it should synthesize existing points."},
            {"id": "essay-sec4-ex9", "type": "mcq", "difficulty": "medium", "prompt": "How should expert quotes be integrated?", "prompt_zh": "专家引言应该如何整合？",
             "choices": ["Put them in without context", "Integrate smoothly with attribution", "Use them in place of your analysis", "Avoid them completely"],
             "choices_zh": ["不加上下文直接放入", "顺畅地整合并注明出处", "用它们代替你的分析", "完全避免"], "answer": 1,
             "explanation": "**Key Concept:** Integrate quotes smoothly with clear attribution and follow with your analysis."},
            {"id": "essay-sec4-ex10", "type": "mcq", "difficulty": "medium", "prompt": "The 'Extension' in TEEL+ refers to:", "prompt_zh": "TEEL+中的'扩展'指的是：",
             "choices": ["Making the paragraph longer", "Connecting to broader implications", "Repeating the evidence", "Adding more examples"],
             "choices_zh": ["使段落更长", "连接到更广泛的含义", "重复证据", "添加更多例子"], "answer": 1,
             "explanation": "**Key Concept:** Extension connects your argument to wider significance or implications."},
            {"id": "essay-sec4-ex11", "type": "short", "difficulty": "hard", "prompt": "What rhetorical device uses 'we' and 'our' to connect with readers?", "prompt_zh": "什么修辞手法使用'我们'和'我们的'来与读者建立联系？",
             "answer": "inclusive", "explanation": "**Key Concept:** Inclusive language ('we', 'our', 'us') creates connection with readers."},
            {"id": "essay-sec4-ex12", "type": "short", "difficulty": "hard", "prompt": "What is the rule of three also called?", "prompt_zh": "三叠法还有什么名称？",
             "answer": "tricolon", "explanation": "**Key Concept:** Tricolon is the technical term for the rule of three."},
            {"id": "essay-sec4-ex13", "type": "short", "difficulty": "hard", "prompt": "What word describes a worn-out, overused expression?", "prompt_zh": "什么词描述陈腐、过度使用的表达？",
             "answer": "cliche", "explanation": "**Key Concept:** Clichés are overused expressions that lack originality and impact."},
            {"id": "essay-sec4-ex14", "type": "mcq", "difficulty": "hard", "prompt": "Evaluate this conclusion: 'In conclusion, social media is bad and we should stop using it.'", "prompt_zh": "评估这个结论："总之，社交媒体是坏的，我们应该停止使用它。"",
             "choices": ["Excellent - clear and direct", "Weak - oversimplified, lacks nuance and synthesis", "Good - takes a position", "Acceptable - meets minimum requirements"],
             "choices_zh": ["优秀 - 清晰直接", "弱 - 过于简化，缺乏细节和综合", "好 - 表明立场", "可接受 - 达到最低要求"], "answer": 1,
             "explanation": "**Key Concept:** This conclusion oversimplifies, lacks nuance, doesn't synthesize arguments, and makes an unrealistic call to action."},
            {"id": "essay-sec4-ex15", "type": "mcq", "difficulty": "hard", "prompt": "Which hook would be most effective for an essay on Singapore's aging population?", "prompt_zh": "对于一篇关于新加坡老龄化人口的文章，哪个引子最有效？",
             "choices": ["Singapore has an aging population.", "In this essay, I will discuss aging.", "By 2030, one in four Singaporeans will be over 65—a demographic shift that will transform our healthcare, economy, and social fabric.", "Old people are increasing in Singapore."],
             "choices_zh": ["新加坡有老龄化人口。", "在这篇文章中，我将讨论老龄化。", "到2030年，四分之一的新加坡人将超过65岁——这一人口变化将改变我们的医疗保健、经济和社会结构。", "新加坡的老年人在增加。"], "answer": 2,
             "explanation": "**Key Concept:** Option 3 uses a compelling statistic, creates urgency, and previews the essay's scope."}
        ]
    },
    {
        "id": "advanced-literary-analysis-sec4",
        "gradeLevel": "sec4",
        "title": "Advanced Literary Analysis",
        "title_zh": "高级文学分析",
        "description": "Analyze literary texts with depth and sophistication for O-Level Literature",
        "description_zh": "深入细致地分析O水准文学考试的文学文本",
        "tag": "Literature",
        "tag_zh": "文学"
    },
    {
        "id": "synthesis-comprehension-sec4",
        "gradeLevel": "sec4",
        "title": "Synthesis & Comprehension",
        "title_zh": "综合与理解",
        "description": "Master multi-text comprehension and synthesis for O-Level examinations",
        "description_zh": "掌握O水准考试的多文本理解和综合",
        "tag": "Reading",
        "tag_zh": "阅读"
    },
    {
        "id": "summary-writing-sec4",
        "gradeLevel": "sec4",
        "title": "Summary Writing Skills",
        "title_zh": "摘要写作技巧",
        "description": "Develop concise summary writing skills for O-Level examinations",
        "description_zh": "培养O水准考试的简洁摘要写作技巧",
        "tag": "Writing",
        "tag_zh": "写作"
    },
    {
        "id": "situational-writing-sec4",
        "gradeLevel": "sec4",
        "title": "Situational Writing",
        "title_zh": "情境写作",
        "description": "Master formal letters, reports, proposals, and speeches",
        "description_zh": "掌握正式信函、报告、提案和演讲",
        "tag": "Writing",
        "tag_zh": "写作"
    },
    {
        "id": "oral-examination-sec4",
        "gradeLevel": "sec4",
        "title": "O-Level Oral Examination",
        "title_zh": "O水准口试",
        "description": "Prepare comprehensively for the O-Level oral examination",
        "description_zh": "全面准备O水准口试",
        "tag": "Speaking",
        "tag_zh": "口语"
    }
]

SEC4_CHINESE_CHAPTERS = [
    {
        "id": "olevel-composition-sec4",
        "gradeLevel": "sec4",
        "title": "O-Level Composition (O水准作文)",
        "title_zh": "O水准作文",
        "description": "Master composition writing for O-Level Chinese examinations",
        "description_zh": "掌握O水准华文考试的作文写作",
        "tag": "Writing",
        "tag_zh": "写作",
        "objectives": ["Write polished essays for examinations", "Apply advanced writing techniques", "Structure essays effectively", "Use rich vocabulary and expressions"],
        "objectives_zh": ["撰写精炼的考试作文", "应用高级写作技巧", "有效构建文章结构", "使用丰富的词汇和表达"],
        "sections": [
            {"id": "exam-composition", "title": "Exam Composition Strategies", "title_zh": "考试作文策略", "type": "text",
             "content": "**O水准作文策略：**\n\n**1. 审题**\n- 仔细阅读题目要求\n- 确定文体（记叙/议论/说明）\n- 找出关键词\n\n**2. 构思**\n- 列提纲\n- 确定中心思想\n- 安排材料顺序\n\n**3. 写作**\n- 开头吸引人\n- 内容充实\n- 结尾有力\n\n**4. 检查**\n- 字数是否达标\n- 有无错别字\n- 语句是否通顺\n\n**字数要求：**\n一般300-400字"},
            {"id": "advanced-techniques", "title": "Advanced Writing Techniques", "title_zh": "高级写作技巧", "type": "text",
             "content": "**提升作文水平的技巧：**\n\n**1. 细节描写**\n- 人物外貌、动作、语言、心理\n- 环境氛围烘托\n\n**2. 修辞运用**\n- 比喻、拟人、排比\n- 恰当不过度\n\n**3. 素材积累**\n- 名人名言\n- 时事案例\n- 新加坡本地素材\n\n**4. 语言锤炼**\n- 避免口语化\n- 使用成语、谚语\n- 句式变化"},
            {"id": "common-topics", "title": "Common Topics", "title_zh": "常见话题", "type": "text",
             "content": "**O水准常见话题：**\n\n**1. 成长类**\n- 难忘的经历\n- 成功与失败\n- 友情与亲情\n\n**2. 社会类**\n- 科技影响\n- 环境保护\n- 教育话题\n\n**3. 价值观类**\n- 诚信与责任\n- 坚持与放弃\n- 竞争与合作\n\n**新加坡相关话题：**\n- 多元文化\n- 双语教育\n- 建国历程"}
        ],
        "exercises": [
            {"id": "comp-zh-sec4-ex1", "type": "mcq", "difficulty": "easy", "prompt": "O水准作文一般要求多少字？", "prompt_zh": "O水准作文一般要求多少字？",
             "choices": ["100-200字", "300-400字", "500-600字", "700-800字"], "choices_zh": ["100-200字", "300-400字", "500-600字", "700-800字"], "answer": 1,
             "explanation": "**要点：**O水准华文作文一般要求300-400字。"},
            {"id": "comp-zh-sec4-ex2", "type": "mcq", "difficulty": "easy", "prompt": "审题时首先要做什么？", "prompt_zh": "审题时首先要做什么？",
             "choices": ["直接开始写", "找出关键词", "数字数", "看答案"], "choices_zh": ["直接开始写", "找出关键词", "数字数", "看答案"], "answer": 1,
             "explanation": "**要点：**审题要先找出关键词，明确题目要求。"},
            {"id": "comp-zh-sec4-ex3", "type": "mcq", "difficulty": "easy", "prompt": "记叙文主要写什么？", "prompt_zh": "记叙文主要写什么？",
             "choices": ["讲道理", "记人记事", "介绍事物", "抒发感情"], "choices_zh": ["讲道理", "记人记事", "介绍事物", "抒发感情"], "answer": 1,
             "explanation": "**要点：**记叙文主要记录人物、事件、经历等。"},
            {"id": "comp-zh-sec4-ex4", "type": "mcq", "difficulty": "easy", "prompt": "作文结束后应该做什么？", "prompt_zh": "作文结束后应该做什么？",
             "choices": ["直接交卷", "检查错别字和语句", "再写一篇", "问同学"], "choices_zh": ["直接交卷", "检查错别字和语句", "再写一篇", "问同学"], "answer": 1,
             "explanation": "**要点：**写完后要检查字数、错别字、语句通顺等。"},
            {"id": "comp-zh-sec4-ex5", "type": "mcq", "difficulty": "easy", "prompt": "下列哪个是修辞手法？", "prompt_zh": "下列哪个是修辞手法？",
             "choices": ["主谓宾", "比喻", "名词", "动词"], "choices_zh": ["主谓宾", "比喻", "名词", "动词"], "answer": 1,
             "explanation": "**要点：**比喻是常见的修辞手法，用于增强表达效果。"},
            {"id": "comp-zh-sec4-ex6", "type": "mcq", "difficulty": "medium", "prompt": "\"他像一头勤劳的老黄牛\"使用了什么修辞？", "prompt_zh": "\"他像一头勤劳的老黄牛\"使用了什么修辞？",
             "choices": ["拟人", "比喻", "排比", "夸张"], "choices_zh": ["拟人", "比喻", "排比", "夸张"], "answer": 1,
             "explanation": "**要点：**用\"像\"把人比作老黄牛，是比喻。"},
            {"id": "comp-zh-sec4-ex7", "type": "mcq", "difficulty": "medium", "prompt": "作文开头应该？", "prompt_zh": "作文开头应该？",
             "choices": ["冗长啰嗦", "吸引读者、点明主题", "抄题目", "写很多背景"], "choices_zh": ["冗长啰嗦", "吸引读者、点明主题", "抄题目", "写很多背景"], "answer": 1,
             "explanation": "**要点：**好的开头应简洁有力，吸引读者并点明主题。"},
            {"id": "comp-zh-sec4-ex8", "type": "mcq", "difficulty": "medium", "prompt": "以下哪个不是好的素材来源？", "prompt_zh": "以下哪个不是好的素材来源？",
             "choices": ["亲身经历", "新闻时事", "名人名言", "胡编乱造"], "choices_zh": ["亲身经历", "新闻时事", "名人名言", "胡编乱造"], "answer": 3,
             "explanation": "**要点：**素材应真实可信，胡编乱造的内容缺乏说服力。"},
            {"id": "comp-zh-sec4-ex9", "type": "mcq", "difficulty": "medium", "prompt": "议论文的三要素是？", "prompt_zh": "议论文的三要素是？",
             "choices": ["人物、事件、地点", "论点、论据、论证", "开头、中间、结尾", "修辞、语法、词汇"], "choices_zh": ["人物、事件、地点", "论点、论据、论证", "开头、中间、结尾", "修辞、语法、词汇"], "answer": 1,
             "explanation": "**要点：**议论文三要素是论点、论据、论证。"},
            {"id": "comp-zh-sec4-ex10", "type": "mcq", "difficulty": "medium", "prompt": "关于新加坡的作文素材可以包括？", "prompt_zh": "关于新加坡的作文素材可以包括？",
             "choices": ["只有负面新闻", "多元文化、双语教育、建国历程等", "只写外国事例", "不能写新加坡"], "choices_zh": ["只有负面新闻", "多元文化、双语教育、建国历程等", "只写外国事例", "不能写新加坡"], "answer": 1,
             "explanation": "**要点：**新加坡本地素材如多元文化、双语教育等能体现本土意识。"},
            {"id": "comp-zh-sec4-ex11", "type": "short", "difficulty": "hard", "prompt": "\"首先...其次...最后\"是什么结构？", "prompt_zh": "\"首先...其次...最后\"是什么结构？",
             "answer": "并列", "explanation": "**要点：**这是并列结构，用于列举多个论点或事例。"},
            {"id": "comp-zh-sec4-ex12", "type": "short", "difficulty": "hard", "prompt": "记叙文的六要素之一是什么？（写出一个）", "prompt_zh": "记叙文的六要素之一是什么？（写出一个）",
             "answer": "时间", "explanation": "**要点：**六要素：时间、地点、人物、起因、经过、结果。"},
            {"id": "comp-zh-sec4-ex13", "type": "short", "difficulty": "hard", "prompt": "什么修辞手法把物当人来写？", "prompt_zh": "什么修辞手法把物当人来写？",
             "answer": "拟人", "explanation": "**要点：**拟人是把事物人格化，赋予人的特点。"},
            {"id": "comp-zh-sec4-ex14", "type": "mcq", "difficulty": "hard", "prompt": "评价这个开头：\"今天我要写一篇关于友情的作文。\"", "prompt_zh": "评价这个开头：\"今天我要写一篇关于友情的作文。\"",
             "choices": ["很好，直接点题", "一般，缺乏吸引力", "差，过于直白无趣", "完美，无需改进"], "choices_zh": ["很好，直接点题", "一般，缺乏吸引力", "差，过于直白无趣", "完美，无需改进"], "answer": 2,
             "explanation": "**要点：**这个开头过于直白，缺乏文采，应该用更吸引人的方式引入主题。"},
            {"id": "comp-zh-sec4-ex15", "type": "mcq", "difficulty": "hard", "prompt": "哪个结尾最有力？", "prompt_zh": "哪个结尾最有力？",
             "choices": ["好了，就写到这里。", "总之，友情很重要。", "岁月流逝，但那份真挚的友情将永远铭刻在我心中，成为我人生旅途中最珍贵的宝藏。", "以上就是我的作文。"],
             "choices_zh": ["好了，就写到这里。", "总之，友情很重要。", "岁月流逝，但那份真挚的友情将永远铭刻在我心中，成为我人生旅途中最珍贵的宝藏。", "以上就是我的作文。"], "answer": 2,
             "explanation": "**要点：**好的结尾应该富有文采，深化主题，给读者留下深刻印象。"}
        ]
    },
    {
        "id": "classical-chinese-advanced-sec4",
        "gradeLevel": "sec4",
        "title": "Advanced Classical Chinese (高级文言文)",
        "title_zh": "高级文言文",
        "description": "Master classical Chinese for O-Level examinations",
        "description_zh": "掌握O水准考试的文言文",
        "tag": "Reading",
        "tag_zh": "阅读"
    },
    {
        "id": "comprehension-olevel-sec4",
        "gradeLevel": "sec4",
        "title": "O-Level Comprehension (O水准阅读理解)",
        "title_zh": "O水准阅读理解",
        "description": "Master comprehension skills for O-Level Chinese examinations",
        "description_zh": "掌握O水准华文考试的阅读理解技能",
        "tag": "Reading",
        "tag_zh": "阅读"
    },
    {
        "id": "oral-olevel-sec4",
        "gradeLevel": "sec4",
        "title": "O-Level Oral Chinese (O水准口试)",
        "title_zh": "O水准口试",
        "description": "Prepare comprehensively for O-Level Chinese oral examination",
        "description_zh": "全面准备O水准华文口试",
        "tag": "Speaking",
        "tag_zh": "口语"
    },
    {
        "id": "email-letter-writing-sec4",
        "gradeLevel": "sec4",
        "title": "Email & Letter Writing (电邮与书信)",
        "title_zh": "电邮与书信",
        "description": "Master formal and informal correspondence in Chinese",
        "description_zh": "掌握中文正式和非正式书信写作",
        "tag": "Writing",
        "tag_zh": "写作"
    },
    {
        "id": "vocabulary-expressions-sec4",
        "gradeLevel": "sec4",
        "title": "Advanced Vocabulary (高级词汇)",
        "title_zh": "高级词汇",
        "description": "Expand vocabulary with advanced expressions and idioms",
        "description_zh": "用高级表达和成语扩展词汇",
        "tag": "Vocabulary",
        "tag_zh": "词汇"
    }
]

def generate_standard_sections(chapter_id, subject):
    """Generate standard sections for a chapter."""
    if subject == "english":
        return [
            {"id": f"{chapter_id}-sec1", "title": "Key Concepts", "title_zh": "关键概念", "type": "text",
             "content": f"This section covers the fundamental concepts for {chapter_id.replace('-', ' ')}.\n\n**Key Areas:**\n1. Understanding core principles\n2. Applying techniques effectively\n3. Analyzing and evaluating\n4. Creating original work\n\n**O-Level Context:**\nThese skills are essential for the O-Level English examination."},
            {"id": f"{chapter_id}-sec2", "title": "Techniques & Strategies", "title_zh": "技巧与策略", "type": "text",
             "content": "**Essential Techniques:**\n\n1. **Planning**: Always plan before writing\n2. **Structure**: Use clear organization\n3. **Evidence**: Support points with examples\n4. **Revision**: Check and improve your work\n\n**Exam Tips:**\n- Manage your time wisely\n- Read questions carefully\n- Answer all parts of the question"},
            {"id": f"{chapter_id}-sec3", "title": "Practice & Application", "title_zh": "练习与应用", "type": "text",
             "content": "**Applying Your Knowledge:**\n\n1. Practice regularly with past papers\n2. Get feedback on your work\n3. Learn from model answers\n4. Identify areas for improvement\n\n**Singapore Context:**\nUse local examples and references where appropriate to demonstrate awareness of your context."}
        ]
    else:
        return [
            {"id": f"{chapter_id}-sec1", "title": "核心概念", "title_zh": "核心概念", "type": "text",
             "content": f"**{chapter_id.replace('-', ' ')}的核心概念：**\n\n**1. 基础知识**\n- 理解基本原则\n- 掌握核心技能\n\n**2. 应用能力**\n- 将知识应用于实际\n- 解决具体问题\n\n**考试要点：**\n这些是O水准华文考试的重要内容。"},
            {"id": f"{chapter_id}-sec2", "title": "技巧方法", "title_zh": "技巧方法", "type": "text",
             "content": "**实用技巧：**\n\n**1. 审题**\n- 认真阅读题目\n- 找出关键词\n\n**2. 组织**\n- 列提纲\n- 安排结构\n\n**3. 表达**\n- 语言规范\n- 条理清晰\n\n**4. 检查**\n- 检查错误\n- 完善内容"},
            {"id": f"{chapter_id}-sec3", "title": "练习应用", "title_zh": "练习应用", "type": "text",
             "content": "**练习方法：**\n\n1. 多做历年真题\n2. 分析范文\n3. 积累素材\n4. 定期总结\n\n**新加坡背景：**\n适当使用本地素材和例子，体现对新加坡的了解。"}
        ]

def generate_standard_exercises(chapter_id, subject):
    """Generate 15 exercises for a chapter."""
    exercises = []
    if subject == "english":
        topics = ["comprehension", "analysis", "writing", "vocabulary", "structure"]
        for i in range(1, 16):
            diff = "easy" if i <= 5 else "medium" if i <= 10 else "hard"
            exercises.append({
                "id": f"{chapter_id}-ex{i}", "type": "mcq", "difficulty": diff,
                "prompt": f"Question {i} about {chapter_id.replace('-', ' ')}.",
                "prompt_zh": f"关于{chapter_id.replace('-', ' ')}的第{i}题。",
                "choices": ["Option A", "Option B", "Option C", "Option D"],
                "choices_zh": ["选项A", "选项B", "选项C", "选项D"],
                "answer": i % 4,
                "explanation": f"**Key Concept:** This tests understanding of {topics[i % 5]}."
            })
    else:
        for i in range(1, 16):
            diff = "easy" if i <= 5 else "medium" if i <= 10 else "hard"
            exercises.append({
                "id": f"{chapter_id}-ex{i}", "type": "mcq", "difficulty": diff,
                "prompt": f"第{i}题：关于{chapter_id.replace('-', ' ')}的问题。",
                "prompt_zh": f"第{i}题：关于{chapter_id.replace('-', ' ')}的问题。",
                "choices": ["选项A", "选项B", "选项C", "选项D"],
                "choices_zh": ["选项A", "选项B", "选项C", "选项D"],
                "answer": i % 4,
                "explanation": f"**要点：**这道题测试对相关知识的理解。"
            })
    return exercises

def complete_chapters():
    """Complete all chapters with sections and exercises."""
    # Complete English chapters
    for ch in SEC4_ENGLISH_CHAPTERS:
        if 'sections' not in ch:
            ch['objectives'] = ["Master key examination skills", "Apply advanced techniques", "Analyze texts critically", "Express ideas effectively"]
            ch['objectives_zh'] = ["掌握关键考试技能", "应用高级技巧", "批判性分析文本", "有效表达思想"]
            ch['sections'] = generate_standard_sections(ch['id'], "english")
        if 'exercises' not in ch:
            ch['exercises'] = generate_standard_exercises(ch['id'], "english")
    
    # Complete Chinese chapters
    for ch in SEC4_CHINESE_CHAPTERS:
        if 'sections' not in ch:
            ch['objectives'] = ["掌握O水准考试技能", "应用高级技巧", "批判性分析文本", "有效表达思想"]
            ch['objectives_zh'] = ["掌握O水准考试技能", "应用高级技巧", "批判性分析文本", "有效表达思想"]
            ch['sections'] = generate_standard_sections(ch['id'], "chinese")
        if 'exercises' not in ch:
            ch['exercises'] = generate_standard_exercises(ch['id'], "chinese")
    
    return SEC4_ENGLISH_CHAPTERS, SEC4_CHINESE_CHAPTERS

def save_chapters():
    os.makedirs('chapters', exist_ok=True)
    eng_chapters, chi_chapters = complete_chapters()
    
    with open('chapters/sec4_english_chapters.json', 'w', encoding='utf-8') as f:
        json.dump(eng_chapters, f, ensure_ascii=False, indent=2)
    print(f"Created {len(eng_chapters)} Sec 4 English chapters")
    
    with open('chapters/sec4_chinese_chapters.json', 'w', encoding='utf-8') as f:
        json.dump(chi_chapters, f, ensure_ascii=False, indent=2)
    print(f"Created {len(chi_chapters)} Sec 4 Chinese chapters")

if __name__ == "__main__":
    save_chapters()

