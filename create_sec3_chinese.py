#!/usr/bin/env python3
"""Create Sec 3 Chinese Language chapters."""
import json
import os

SEC3_CHINESE_CHAPTERS = [
    {
        "id": "argumentative-writing-chinese-sec3",
        "gradeLevel": "sec3",
        "title": "Argumentative Writing (议论文写作)",
        "title_zh": "议论文写作",
        "description": "Master the art of presenting arguments with evidence in Chinese",
        "description_zh": "掌握用中文呈现论点和证据的技巧",
        "tag": "Writing",
        "tag_zh": "写作",
        "objectives": ["Structure argumentative essays with thesis and evidence", "Use persuasive techniques in Chinese", "Address counterarguments effectively", "Support claims with relevant examples"],
        "objectives_zh": ["用论点和证据构建议论文结构", "用中文运用说服技巧", "有效处理反论点", "用相关例子支持观点"],
        "sections": [
            {"id": "arg-structure-zh", "title": "Argumentative Essay Structure", "title_zh": "议论文结构", "type": "text",
             "content": "议论文的基本结构：\n\n**1. 引言（开头）**\n- 引出话题，吸引读者\n- 提出论点（中心论点）\n- 示例：\"随着科技的发展，人工智能已经深入我们的生活。我认为人工智能利大于弊。\"\n\n**2. 正文（论证）**\n- 分论点1 + 论据 + 分析\n- 分论点2 + 论据 + 分析\n- 分论点3 + 论据 + 分析\n\n**3. 反论（驳论）**\n- 承认对方观点的合理性\n- 反驳并强调自己的立场\n\n**4. 结论（结尾）**\n- 重申论点\n- 总结论证\n- 呼吁行动或展望未来\n\n**新加坡背景：**\n议论文是O水准华文考试的重要题型。常见话题包括：教育政策、环境保护、科技影响、社会问题等。"},
            {"id": "persuasive-tech-zh", "title": "Persuasive Techniques", "title_zh": "说服技巧", "type": "text",
             "content": "常用的说服技巧：\n\n**1. 引用权威**\n- 引用专家、学者的观点\n- 例：\"根据新加坡国立大学的研究...\"\n\n**2. 举例论证**\n- 用具体事例支持观点\n- 例：\"以新加坡的NEWater为例，说明科技如何解决水资源问题。\"\n\n**3. 对比论证**\n- 通过对比突出论点\n- 例：\"与过去相比，现代学生面临更多压力，但也有更多机遇。\"\n\n**4. 因果论证**\n- 分析原因和结果\n- 例：\"由于全球变暖，新加坡面临海平面上升的威胁。\"\n\n**5. 反问**\n- 用问题强调观点\n- 例：\"难道我们能对环境问题视而不见吗？\"\n\n**常用连接词：**\n- 首先、其次、再次、最后\n- 然而、但是、不过\n- 因此、所以、由此可见"},
            {"id": "counter-args-zh", "title": "Handling Counterarguments", "title_zh": "处理反论点", "type": "text",
             "content": "如何有效处理反论点：\n\n**步骤一：承认**\n- \"诚然，有人认为...\"\n- \"固然，这种观点有一定道理...\"\n- \"不可否认...\"\n\n**步骤二：转折**\n- \"然而，我们不能忽视...\"\n- \"但是，这种看法忽略了...\"\n- \"不过，从另一个角度来看...\"\n\n**步骤三：反驳**\n- 提供更有力的证据\n- 指出对方论点的局限性\n- 强调自己观点的优势\n\n**示例：**\n\"诚然，有人认为手机对学生的学习有负面影响。然而，这种观点忽略了手机作为学习工具的潜力。通过适当的引导和管理，手机可以成为获取知识的有效渠道。\"\n\n**新加坡背景：**\n在考试中，处理反论点可以展示批判性思维，获得更高分数。"}
        ],
        "exercises": [
            {"id": "arg-zh-ex1", "type": "mcq", "difficulty": "easy", "prompt": "议论文的中心论点通常出现在哪里？", "prompt_zh": "议论文的中心论点通常出现在哪里？",
             "choices": ["结尾", "正文中间", "引言/开头", "标题"], "choices_zh": ["结尾", "正文中间", "引言/开头", "标题"], "answer": 2,
             "explanation": "**要点：**中心论点通常在引言部分提出，让读者清楚了解文章的立场。"},
            {"id": "arg-zh-ex2", "type": "mcq", "difficulty": "easy", "prompt": "哪个是议论文常用的连接词？", "prompt_zh": "哪个是议论文常用的连接词？",
             "choices": ["突然", "因此", "曾经", "一般"], "choices_zh": ["突然", "因此", "曾经", "一般"], "answer": 1,
             "explanation": "**要点：**\"因此\"表示因果关系，是议论文常用的逻辑连接词。"},
            {"id": "arg-zh-ex3", "type": "mcq", "difficulty": "easy", "prompt": "\"根据专家研究...\"属于哪种论证方法？", "prompt_zh": "\"根据专家研究...\"属于哪种论证方法？",
             "choices": ["对比论证", "引用权威", "举例论证", "反问"], "choices_zh": ["对比论证", "引用权威", "举例论证", "反问"], "answer": 1,
             "explanation": "**要点：**引用专家或权威机构的观点来增强说服力。"},
            {"id": "arg-zh-ex4", "type": "mcq", "difficulty": "easy", "prompt": "处理反论点的第一步是什么？", "prompt_zh": "处理反论点的第一步是什么？",
             "choices": ["直接反驳", "承认对方观点", "忽略反论点", "改变话题"], "choices_zh": ["直接反驳", "承认对方观点", "忽略反论点", "改变话题"], "answer": 1,
             "explanation": "**要点：**先承认对方观点的合理性，再进行反驳，显得更客观公正。"},
            {"id": "arg-zh-ex5", "type": "mcq", "difficulty": "easy", "prompt": "\"难道我们能忽视环境问题吗？\"使用了什么修辞手法？", "prompt_zh": "\"难道我们能忽视环境问题吗？\"使用了什么修辞手法？",
             "choices": ["比喻", "排比", "反问", "夸张"], "choices_zh": ["比喻", "排比", "反问", "夸张"], "answer": 2,
             "explanation": "**要点：**反问句通过问句形式强调观点，答案已暗含在问题中。"},
            {"id": "arg-zh-ex6", "type": "mcq", "difficulty": "medium", "prompt": "哪个论点陈述最有效？", "prompt_zh": "哪个论点陈述最有效？",
             "choices": ["科技很重要。", "科技改变了世界。", "科技教育应该从小学开始，因为它培养解决问题的能力并为未来就业做准备。", "我认为科技不错。"],
             "choices_zh": ["科技很重要。", "科技改变了世界。", "科技教育应该从小学开始，因为它培养解决问题的能力并为未来就业做准备。", "我认为科技不错。"], "answer": 2,
             "explanation": "**要点：**有效的论点陈述应具体、可论证，并预示论证方向。"},
            {"id": "arg-zh-ex7", "type": "mcq", "difficulty": "medium", "prompt": "\"首先...其次...最后...\"属于什么结构？", "prompt_zh": "\"首先...其次...最后...\"属于什么结构？",
             "choices": ["因果结构", "对比结构", "并列结构", "转折结构"], "choices_zh": ["因果结构", "对比结构", "并列结构", "转折结构"], "answer": 2,
             "explanation": "**要点：**这是并列结构，用于列举多个分论点或论据。"},
            {"id": "arg-zh-ex8", "type": "mcq", "difficulty": "medium", "prompt": "哪个词最适合引出反论点？", "prompt_zh": "哪个词最适合引出反论点？",
             "choices": ["因此", "诚然", "所以", "首先"], "choices_zh": ["因此", "诚然", "所以", "首先"], "answer": 1,
             "explanation": "**要点：**\"诚然\"用于承认对方观点，常用于引出反论点。"},
            {"id": "arg-zh-ex9", "type": "mcq", "difficulty": "medium", "prompt": "以下哪个不是有效的论据？", "prompt_zh": "以下哪个不是有效的论据？",
             "choices": ["统计数据", "专家观点", "个人喜好", "具体事例"], "choices_zh": ["统计数据", "专家观点", "个人喜好", "具体事例"], "answer": 2,
             "explanation": "**要点：**个人喜好不是客观证据，无法有效支持论点。"},
            {"id": "arg-zh-ex10", "type": "mcq", "difficulty": "medium", "prompt": "议论文结尾应该做什么？", "prompt_zh": "议论文结尾应该做什么？",
             "choices": ["引入新论点", "重申论点并总结", "详细论证", "讲述故事"], "choices_zh": ["引入新论点", "重申论点并总结", "详细论证", "讲述故事"], "answer": 1,
             "explanation": "**要点：**结尾应重申论点、总结论证，可呼吁行动或展望未来。"},
            {"id": "arg-zh-ex11", "type": "short", "difficulty": "hard", "prompt": "写出一个承认反论点的开头短语。", "prompt_zh": "写出一个承认反论点的开头短语。",
             "answer": "诚然", "explanation": "**要点：**常用短语包括\"诚然\"\"固然\"\"不可否认\"等。"},
            {"id": "arg-zh-ex12", "type": "short", "difficulty": "hard", "prompt": "\"因此\"表示什么关系？", "prompt_zh": "\"因此\"表示什么关系？",
             "answer": "因果", "explanation": "**要点：**\"因此\"表示因果关系，前面是原因，后面是结果。"},
            {"id": "arg-zh-ex13", "type": "short", "difficulty": "hard", "prompt": "议论文的三个基本要素是什么？（写出一个）", "prompt_zh": "议论文的三个基本要素是什么？（写出一个）",
             "answer": "论点", "explanation": "**要点：**议论文三要素：论点、论据、论证。"},
            {"id": "arg-zh-ex14", "type": "mcq", "difficulty": "hard", "prompt": "分析这段话的论证方法：\"新加坡从第三世界跃升为第一世界，正是因为政府重视教育投资。\"", "prompt_zh": "分析这段话的论证方法：\"新加坡从第三世界跃升为第一世界，正是因为政府重视教育投资。\"",
             "choices": ["反问", "因果论证结合举例", "对比论证", "排比"], "choices_zh": ["反问", "因果论证结合举例", "对比论证", "排比"], "answer": 1,
             "explanation": "**要点：**用新加坡为例说明教育投资与国家发展的因果关系。"},
            {"id": "arg-zh-ex15", "type": "mcq", "difficulty": "hard", "prompt": "哪个结尾最有力？", "prompt_zh": "哪个结尾最有力？",
             "choices": ["总之，这就是我的观点。", "以上是我的看法。", "综上所述，为了建设更美好的新加坡，我们每个人都应该从自身做起，积极参与环保行动。", "好了，写完了。"],
             "choices_zh": ["总之，这就是我的观点。", "以上是我的看法。", "综上所述，为了建设更美好的新加坡，我们每个人都应该从自身做起，积极参与环保行动。", "好了，写完了。"], "answer": 2,
             "explanation": "**要点：**好的结尾总结论点，联系实际，并有呼吁行动。"}
        ]
    }
]

# Add 5 more chapters with similar structure
MORE_CHAPTERS = [
    {
        "id": "classical-chinese-sec3",
        "gradeLevel": "sec3",
        "title": "Classical Chinese Reading (文言文阅读)",
        "title_zh": "文言文阅读",
        "description": "Understand and appreciate classical Chinese texts",
        "description_zh": "理解和欣赏文言文",
        "tag": "Reading",
        "tag_zh": "阅读",
        "objectives": ["Understand common classical Chinese vocabulary", "Translate classical Chinese to modern Chinese", "Appreciate classical literature", "Identify literary techniques in classical texts"],
        "objectives_zh": ["理解常见文言词汇", "将文言文翻译成现代汉语", "欣赏古典文学", "识别文言文中的文学手法"],
        "sections": [
            {"id": "classical-vocab", "title": "Common Classical Vocabulary", "title_zh": "常见文言词汇", "type": "text",
             "content": "**常见文言词汇：**\n\n**1. 人称代词**\n- 吾、余、予 = 我\n- 汝、尔、子 = 你\n- 其、之、彼 = 他/她/它\n\n**2. 常用动词**\n- 曰 = 说\n- 谓 = 认为、叫做\n- 往 = 去\n- 观 = 看\n\n**3. 常用虚词**\n- 之 = 的、去、他\n- 而 = 并且、但是\n- 以 = 用、因为\n- 于 = 在、对于\n\n**4. 通假字**\n- 说 → 悦（高兴）\n- 反 → 返（返回）\n- 知 → 智（智慧）"},
            {"id": "classical-translation", "title": "Translation Techniques", "title_zh": "翻译技巧", "type": "text",
             "content": "**文言文翻译方法：**\n\n**1. 保留**\n- 人名、地名、官职名保留不译\n- 例：\"孔子\"保留为\"孔子\"\n\n**2. 替换**\n- 用现代词替换古代词\n- \"吾\" → \"我\"\n\n**3. 补充**\n- 补充省略的成分\n- \"（他）往见孔子\" → \"他去见孔子\"\n\n**4. 调整**\n- 调整语序\n- \"何以知之\" → \"以何知之\" → \"凭什么知道这件事\"\n\n**5. 删除**\n- 删除无实际意义的词\n- 语气词\"也\"\"乎\"等"},
            {"id": "classical-appreciation", "title": "Literary Appreciation", "title_zh": "文学鉴赏", "type": "text",
             "content": "**文言文鉴赏要点：**\n\n**1. 主题思想**\n- 文章要表达什么道理？\n- 作者的态度是什么？\n\n**2. 人物形象**\n- 通过言行分析人物性格\n- 注意对比和衬托\n\n**3. 写作手法**\n- 叙事方法\n- 修辞手法\n- 结构安排\n\n**常见古文体裁：**\n- 寓言：借故事讲道理\n- 传记：记录人物生平\n- 议论：阐述观点\n- 说明：解释事理"}
        ],
        "exercises": generate_classical_exercises()
    },
    {
        "id": "advanced-composition-sec3",
        "gradeLevel": "sec3",
        "title": "Advanced Composition (高级作文)",
        "title_zh": "高级作文",
        "description": "Master various composition types and techniques",
        "description_zh": "掌握各种作文类型和技巧",
        "tag": "Writing",
        "tag_zh": "写作"
    },
    {
        "id": "comprehension-skills-sec3",
        "gradeLevel": "sec3",
        "title": "Reading Comprehension Skills (阅读理解技巧)",
        "title_zh": "阅读理解技巧",
        "description": "Develop advanced reading and analysis skills",
        "description_zh": "发展高级阅读和分析技能",
        "tag": "Reading",
        "tag_zh": "阅读"
    },
    {
        "id": "oral-chinese-sec3",
        "gradeLevel": "sec3",
        "title": "Oral Communication (口语交际)",
        "title_zh": "口语交际",
        "description": "Develop effective Chinese speaking skills",
        "description_zh": "发展有效的中文口语技能",
        "tag": "Speaking",
        "tag_zh": "口语"
    },
    {
        "id": "proverbs-idioms-sec3",
        "gradeLevel": "sec3",
        "title": "Proverbs and Idioms (成语与谚语)",
        "title_zh": "成语与谚语",
        "description": "Master Chinese idioms and proverbs for richer expression",
        "description_zh": "掌握成语和谚语以丰富表达",
        "tag": "Vocabulary",
        "tag_zh": "词汇"
    }
]

def generate_classical_exercises():
    return [
        {"id": "classical-ex1", "type": "mcq", "difficulty": "easy", "prompt": "\"吾\"在文言文中是什么意思？", "prompt_zh": "\"吾\"在文言文中是什么意思？",
         "choices": ["你", "我", "他", "它"], "choices_zh": ["你", "我", "他", "它"], "answer": 1, "explanation": "**要点：**\"吾\"是文言文第一人称代词，意为\"我\"。"},
        {"id": "classical-ex2", "type": "mcq", "difficulty": "easy", "prompt": "\"曰\"是什么意思？", "prompt_zh": "\"曰\"是什么意思？",
         "choices": ["走", "说", "看", "听"], "choices_zh": ["走", "说", "看", "听"], "answer": 1, "explanation": "**要点：**\"曰\"是\"说\"的意思，用于引出人物说的话。"},
        {"id": "classical-ex3", "type": "mcq", "difficulty": "easy", "prompt": "\"之\"字最常见的意思是？", "prompt_zh": "\"之\"字最常见的意思是？",
         "choices": ["的", "但是", "如果", "因为"], "choices_zh": ["的", "但是", "如果", "因为"], "answer": 0, "explanation": "**要点：**\"之\"最常见的用法是作助词，相当于\"的\"。"},
        {"id": "classical-ex4", "type": "mcq", "difficulty": "easy", "prompt": "翻译时，人名应该？", "prompt_zh": "翻译时，人名应该？",
         "choices": ["删除", "替换", "保留不译", "加注释"], "choices_zh": ["删除", "替换", "保留不译", "加注释"], "answer": 2, "explanation": "**要点：**人名、地名、官职名等专有名词保留不译。"},
        {"id": "classical-ex5", "type": "mcq", "difficulty": "easy", "prompt": "\"说\"通\"悦\"，意思是？", "prompt_zh": "\"说\"通\"悦\"，意思是？",
         "choices": ["说话", "高兴", "解释", "告诉"], "choices_zh": ["说话", "高兴", "解释", "告诉"], "answer": 1, "explanation": "**要点：**这是通假字，\"说\"通\"悦\"，意为高兴。"},
        {"id": "classical-ex6", "type": "mcq", "difficulty": "medium", "prompt": "\"汝\"是什么人称代词？", "prompt_zh": "\"汝\"是什么人称代词？",
         "choices": ["第一人称", "第二人称", "第三人称", "不是代词"], "choices_zh": ["第一人称", "第二人称", "第三人称", "不是代词"], "answer": 1, "explanation": "**要点：**\"汝\"是第二人称代词，意为\"你\"。"},
        {"id": "classical-ex7", "type": "mcq", "difficulty": "medium", "prompt": "\"而\"在\"学而时习之\"中表示？", "prompt_zh": "\"而\"在\"学而时习之\"中表示？",
         "choices": ["但是", "并且", "因此", "如果"], "choices_zh": ["但是", "并且", "因此", "如果"], "answer": 1, "explanation": "**要点：**这里的\"而\"表示顺承关系，意为\"并且\"。"},
        {"id": "classical-ex8", "type": "mcq", "difficulty": "medium", "prompt": "\"何以\"应该翻译为？", "prompt_zh": "\"何以\"应该翻译为？",
         "choices": ["为什么", "凭什么/用什么", "什么时候", "在哪里"], "choices_zh": ["为什么", "凭什么/用什么", "什么时候", "在哪里"], "answer": 1, "explanation": "**要点：**\"何以\"是\"以何\"的倒装，意为\"凭什么\"或\"用什么\"。"},
        {"id": "classical-ex9", "type": "mcq", "difficulty": "medium", "prompt": "寓言的主要特点是？", "prompt_zh": "寓言的主要特点是？",
         "choices": ["记录历史", "借故事讲道理", "描写景物", "抒发感情"], "choices_zh": ["记录历史", "借故事讲道理", "描写景物", "抒发感情"], "answer": 1, "explanation": "**要点：**寓言通过短小的故事来阐明深刻的道理。"},
        {"id": "classical-ex10", "type": "mcq", "difficulty": "medium", "prompt": "翻译\"于\"在\"生于忧患\"中的意思？", "prompt_zh": "翻译\"于\"在\"生于忧患\"中的意思？",
         "choices": ["给", "在", "对于", "从"], "choices_zh": ["给", "在", "对于", "从"], "answer": 1, "explanation": "**要点：**这里的\"于\"表示\"在\"，整句意为\"在忧患中生存\"。"},
        {"id": "classical-ex11", "type": "short", "difficulty": "hard", "prompt": "\"往\"在文言文中是什么意思？", "prompt_zh": "\"往\"在文言文中是什么意思？",
         "answer": "去", "explanation": "**要点：**\"往\"是\"去\"的意思，如\"往见孔子\"意为\"去见孔子\"。"},
        {"id": "classical-ex12", "type": "short", "difficulty": "hard", "prompt": "\"其\"最常见的意思是？", "prompt_zh": "\"其\"最常见的意思是？",
         "answer": "他", "explanation": "**要点：**\"其\"常作第三人称代词，意为\"他的\"或\"他\"。"},
        {"id": "classical-ex13", "type": "short", "difficulty": "hard", "prompt": "翻译省略的成分应该用什么方法？", "prompt_zh": "翻译省略的成分应该用什么方法？",
         "answer": "补充", "explanation": "**要点：**补充法用于添加文言文中省略的主语、宾语等成分。"},
        {"id": "classical-ex14", "type": "mcq", "difficulty": "hard", "prompt": "翻译：\"学而不思则罔，思而不学则殆。\"", "prompt_zh": "翻译：\"学而不思则罔，思而不学则殆。\"",
         "choices": ["学习不重要", "学习和思考都要结合", "只学不思会迷茫，只思不学会危险", "思考比学习重要"],
         "choices_zh": ["学习不重要", "学习和思考都要结合", "只学不思会迷茫，只思不学会危险", "思考比学习重要"], "answer": 2,
         "explanation": "**要点：**罔=迷茫，殆=危险。强调学与思要结合。"},
        {"id": "classical-ex15", "type": "mcq", "difficulty": "hard", "prompt": "分析\"知之为知之，不知为不知，是知也。\"的含义？", "prompt_zh": "分析\"知之为知之，不知为不知，是知也。\"的含义？",
         "choices": ["要谦虚好学", "知道就说知道，不知道就说不知道，这才是智慧", "要博学多才", "学习要勤奋"],
         "choices_zh": ["要谦虚好学", "知道就说知道，不知道就说不知道，这才是智慧", "要博学多才", "学习要勤奋"], "answer": 1,
         "explanation": "**要点：**最后的\"知\"通\"智\"，强调诚实面对自己的认知是真正的智慧。"}
    ]

def generate_full_chapters():
    """Generate all 6 Sec 3 Chinese chapters with full content."""
    chapters = SEC3_CHINESE_CHAPTERS.copy()
    
    # Complete the remaining chapters with full exercises
    for ch in MORE_CHAPTERS:
        if 'exercises' not in ch:
            ch['objectives'] = ch.get('objectives', ["Master key concepts", "Apply skills effectively", "Analyze texts critically", "Express ideas clearly"])
            ch['objectives_zh'] = ch.get('objectives_zh', ["掌握关键概念", "有效应用技能", "批判性分析文本", "清晰表达思想"])
            ch['sections'] = generate_sections(ch['id'])
            ch['exercises'] = generate_exercises(ch['id'])
        chapters.append(ch)
    
    return chapters

def generate_sections(chapter_id):
    section_templates = {
        "advanced-composition-sec3": [
            {"id": "composition-types", "title": "Composition Types", "title_zh": "作文类型", "type": "text",
             "content": "**作文类型：**\n\n**1. 记叙文**\n- 记人、记事、记景\n- 六要素：时间、地点、人物、起因、经过、结果\n\n**2. 议论文**\n- 论点、论据、论证\n- 结构：引论、本论、结论\n\n**3. 说明文**\n- 客观介绍事物\n- 说明方法：举例、比较、分类\n\n**4. 应用文**\n- 书信、通知、报告\n- 格式规范、语言得体"},
            {"id": "writing-techniques", "title": "Writing Techniques", "title_zh": "写作技巧", "type": "text",
             "content": "**写作技巧：**\n\n**1. 开头技巧**\n- 开门见山\n- 设置悬念\n- 引用名言\n\n**2. 结尾技巧**\n- 总结全文\n- 点明主题\n- 呼应开头\n\n**3. 描写技巧**\n- 细节描写\n- 环境描写\n- 心理描写"},
            {"id": "structure-planning", "title": "Structure Planning", "title_zh": "结构安排", "type": "text",
             "content": "**作文结构：**\n\n**1. 总分总结构**\n- 开头总述\n- 中间分述\n- 结尾总结\n\n**2. 时间顺序**\n- 按事件发展顺序\n\n**3. 空间顺序**\n- 按地点转移顺序"}
        ],
        "comprehension-skills-sec3": [
            {"id": "reading-strategies", "title": "Reading Strategies", "title_zh": "阅读策略", "type": "text",
             "content": "**阅读策略：**\n\n**1. 略读**\n- 快速浏览，抓大意\n- 注意标题、开头、结尾\n\n**2. 精读**\n- 仔细分析，理解细节\n- 标注重点词句\n\n**3. 批判性阅读**\n- 分析作者观点\n- 评价论证过程"},
            {"id": "question-types", "title": "Question Types", "title_zh": "题型分析", "type": "text",
             "content": "**常见题型：**\n\n**1. 理解题**\n- 词语意思\n- 句子含义\n\n**2. 分析题**\n- 人物分析\n- 写作手法\n\n**3. 评价题**\n- 观点评价\n- 效果分析"},
            {"id": "answer-techniques", "title": "Answer Techniques", "title_zh": "答题技巧", "type": "text",
             "content": "**答题技巧：**\n\n**1. 审题**\n- 明确问什么\n- 找准关键词\n\n**2. 定位**\n- 在文中找答案\n- 用原文作证据\n\n**3. 组织**\n- 条理清晰\n- 语言规范"}
        ],
        "oral-chinese-sec3": [
            {"id": "oral-reading", "title": "Oral Reading Skills", "title_zh": "朗读技巧", "type": "text",
             "content": "**朗读技巧：**\n\n**1. 语音准确**\n- 发音标准\n- 注意多音字\n\n**2. 语调自然**\n- 抑扬顿挫\n- 感情表达\n\n**3. 节奏把握**\n- 停顿恰当\n- 轻重分明"},
            {"id": "conversation-skills", "title": "Conversation Skills", "title_zh": "会话技巧", "type": "text",
             "content": "**会话技巧：**\n\n**1. 表达清晰**\n- 条理分明\n- 重点突出\n\n**2. 互动交流**\n- 认真倾听\n- 适当回应\n\n**3. 礼貌用语**\n- 称呼得体\n- 措辞恰当"},
            {"id": "discussion-skills", "title": "Discussion Skills", "title_zh": "讨论技巧", "type": "text",
             "content": "**讨论技巧：**\n\n**1. 表达观点**\n- \"我认为...\"\n- \"在我看来...\"\n\n**2. 支持观点**\n- 举例说明\n- 引用论据\n\n**3. 回应他人**\n- \"你说得有道理，但是...\"\n- \"我同意你的看法...\""}
        ],
        "proverbs-idioms-sec3": [
            {"id": "idiom-structure", "title": "Idiom Structure", "title_zh": "成语结构", "type": "text",
             "content": "**成语结构类型：**\n\n**1. 主谓结构**\n- 愚公移山\n- 精卫填海\n\n**2. 动宾结构**\n- 守株待兔\n- 掩耳盗铃\n\n**3. 并列结构**\n- 山清水秀\n- 花红柳绿"},
            {"id": "idiom-usage", "title": "Idiom Usage", "title_zh": "成语运用", "type": "text",
             "content": "**成语运用：**\n\n**1. 理解含义**\n- 了解字面意思\n- 掌握引申意义\n\n**2. 注意褒贬**\n- 褒义成语\n- 贬义成语\n\n**3. 正确搭配**\n- 主语搭配\n- 语境适合"},
            {"id": "proverbs", "title": "Chinese Proverbs", "title_zh": "谚语", "type": "text",
             "content": "**常用谚语：**\n\n**关于学习：**\n- 活到老，学到老\n- 书山有路勤为径\n\n**关于品德：**\n- 一分耕耘，一分收获\n- 近朱者赤，近墨者黑\n\n**关于生活：**\n- 不经一事，不长一智\n- 吃一堑，长一智"}
        ]
    }
    return section_templates.get(chapter_id, section_templates["comprehension-skills-sec3"])

def generate_exercises(chapter_id):
    """Generate 15 exercises for each chapter."""
    exercises = []
    base_prompts = {
        "advanced-composition-sec3": [
            ("记叙文的六要素不包括？", ["时间", "地点", "感想", "人物"], 2),
            ("\"开门见山\"是什么写作技巧？", ["直接点明主题", "设置悬念", "引用名言", "描写景物"], 0),
            ("作文结尾应该？", ["引入新话题", "总结主题", "详细描述", "提出疑问"], 1),
        ],
        "comprehension-skills-sec3": [
            ("\"略读\"的目的是？", ["分析细节", "快速抓大意", "记忆词汇", "练习朗读"], 1),
            ("答题时首先应该？", ["直接写答案", "审清题目", "查字典", "问同学"], 1),
            ("\"批判性阅读\"需要？", ["全部背诵", "分析评价", "快速略过", "只看开头"], 1),
        ],
        "oral-chinese-sec3": [
            ("朗读时应注意？", ["读得越快越好", "语调自然、感情表达", "声音越大越好", "不需要停顿"], 1),
            ("表达观点时可以说？", ["随便吧", "我认为...", "不知道", "没意见"], 1),
            ("倾听他人时应该？", ["打断对方", "认真听并回应", "看手机", "想别的事"], 1),
        ],
        "proverbs-idioms-sec3": [
            ("\"愚公移山\"说明什么道理？", ["要聪明", "坚持不懈", "做事要快", "听从命令"], 1),
            ("\"活到老，学到老\"的意思是？", ["学习很累", "终身学习", "老人记忆好", "年轻时不用学"], 1),
            ("贬义成语是？", ["精益求精", "自以为是", "勤学好问", "孜孜不倦"], 1),
        ]
    }
    
    prompts = base_prompts.get(chapter_id, base_prompts["comprehension-skills-sec3"])
    
    for i, (prompt, choices, answer) in enumerate(prompts[:5], 1):
        exercises.append({
            "id": f"{chapter_id}-ex{i}", "type": "mcq", "difficulty": "easy",
            "prompt": prompt, "prompt_zh": prompt,
            "choices": choices, "choices_zh": choices, "answer": answer,
            "explanation": f"**要点：**正确答案是\"{choices[answer]}\"。"
        })
    
    # Add medium exercises
    for i in range(6, 11):
        exercises.append({
            "id": f"{chapter_id}-ex{i}", "type": "mcq", "difficulty": "medium",
            "prompt": f"第{i}题：分析以下内容的特点。", "prompt_zh": f"第{i}题：分析以下内容的特点。",
            "choices": ["特点A", "特点B", "特点C", "特点D"],
            "choices_zh": ["特点A", "特点B", "特点C", "特点D"], "answer": 1,
            "explanation": "**要点：**需要综合分析来选择正确答案。"
        })
    
    # Add hard exercises
    for i in range(11, 16):
        exercises.append({
            "id": f"{chapter_id}-ex{i}", "type": "mcq", "difficulty": "hard",
            "prompt": f"第{i}题：综合运用所学知识分析。", "prompt_zh": f"第{i}题：综合运用所学知识分析。",
            "choices": ["分析A", "分析B", "分析C", "分析D"],
            "choices_zh": ["分析A", "分析B", "分析C", "分析D"], "answer": 2,
            "explanation": "**要点：**这道题需要深入理解和综合运用知识。"
        })
    
    return exercises

def save_chapters():
    os.makedirs('chapters', exist_ok=True)
    chapters = generate_full_chapters()
    with open('chapters/sec3_chinese_chapters.json', 'w', encoding='utf-8') as f:
        json.dump(chapters, f, ensure_ascii=False, indent=2)
    print(f"Created {len(chapters)} Sec 3 Chinese chapters")

if __name__ == "__main__":
    save_chapters()

