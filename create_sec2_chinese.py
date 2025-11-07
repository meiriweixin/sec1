import json
from datetime import datetime

# Secondary 2 Chinese chapters following Singapore MOE syllabus
sec2_chinese_chapters = [
    {
        "id": "advanced-grammar-sec2",
        "gradeLevel": "sec2",
        "title": "Advanced Grammar Structures",
        "title_zh": "高级语法结构",
        "description": "Master complex sentence patterns including compound sentences, transitional phrases, and advanced grammatical structures",
        "description_zh": "掌握复杂句型，包括复句、关联词语和高级语法结构",
        "tag": "Grammar",
        "tag_zh": "语法",
        "objectives": [
            "Construct compound sentences using conjunctions",
            "Use transitional phrases correctly (不但...而且, 虽然...但是, 因为...所以)",
            "Master advanced word order in complex sentences",
            "Apply passive voice and causative structures"
        ],
        "objectives_zh": [
            "使用关联词构建复句",
            "正确使用关联词语（不但...而且，虽然...但是，因为...所以）",
            "掌握复杂句子的高级语序",
            "应用被动句和使动句"
        ],
        "sections": [
            {
                "id": "compound-sentences",
                "title": "Compound Sentences with Conjunctions",
                "title_zh": "关联词语与复句",
                "type": "text",
                "content": "复句是由两个或多个分句组成的句子，用关联词连接。\n\n常用关联词组：\n1. 递进关系：不但...而且...\n   例：新加坡不但是花园城市，而且是智慧国。\n\n2. 转折关系：虽然...但是...\n   例：虽然天气很热，但是我们还是要上体育课。\n\n3. 因果关系：因为...所以...\n   例：因为地铁坏了，所以我迟到了。\n\n4. 条件关系：只要...就...\n   例：只要努力学习，就能取得好成绩。\n\n5. 假设关系：如果...就...\n   例：如果明天下雨，运动会就取消。"
            },
            {
                "id": "passive-causative",
                "title": "Passive and Causative Structures",
                "title_zh": "被动句与使动句",
                "type": "text",
                "content": "被动句：表示主语是动作的承受者\n结构：被/让/叫 + 施事者 + 动词\n例：\n- 书被弟弟撕破了。\n- 我的手机让同学借走了。\n- 妈妈叫老师批评了。\n\n使动句：表示使别人做某事\n结构：使/让/叫 + 某人 + 动词\n例：\n- 老师让我们写作文。\n- 这个消息使大家很高兴。\n- 妈妈叫我去买菜。\n\n注意：被动句强调承受，使动句强调施加。"
            },
            {
                "id": "complex-word-order",
                "title": "Complex Word Order",
                "title_zh": "复杂语序",
                "type": "text",
                "content": "复杂句子的语序规则：\n\n1. 多个状语的顺序：\n   时间 + 地点 + 方式 + 动词\n   例：我昨天在图书馆认真地复习功课。\n\n2. 定语的位置：\n   形容词定语在前，名词定语在后\n   例：一本有趣的历史书（形容词）\n   例：新加坡的历史（名词）\n\n3. 补语的位置：\n   动词 + 补语（结果/程度/可能）\n   例：他跑得很快。（程度补语）\n   例：我听懂了。（结果补语）\n   例：这本书看得完吗？（可能补语）"
            }
        ],
        "exercises": []
    },
    {
        "id": "reading-comprehension-advanced-sec2",
        "gradeLevel": "sec2",
        "title": "Advanced Reading Comprehension",
        "title_zh": "高级阅读理解",
        "description": "Develop skills in analyzing longer passages, understanding implicit meanings, and making inferences from complex Chinese texts",
        "description_zh": "培养分析较长文章、理解隐含意义和从复杂中文文本推理的能力",
        "tag": "Reading",
        "tag_zh": "阅读",
        "objectives": [
            "Analyze author's writing techniques and their effects",
            "Identify main ideas and supporting details in longer passages",
            "Make inferences based on context clues",
            "Understand rhetorical devices (比喻、拟人、排比、设问)"
        ],
        "objectives_zh": [
            "分析作者的写作手法及其效果",
            "识别较长文章中的主要观点和支持细节",
            "根据上下文线索进行推理",
            "理解修辞手法（比喻、拟人、排比、设问）"
        ],
        "sections": [
            {
                "id": "rhetorical-devices",
                "title": "Rhetorical Devices",
                "title_zh": "修辞手法",
                "type": "text",
                "content": "常见修辞手法：\n\n1. 比喻：用相似的事物比拟\n   例：新加坡像一颗璀璨的明珠。\n   作用：使描写更生动形象\n\n2. 拟人：把物当作人来写\n   例：春风轻轻地抚摸着大地。\n   作用：使事物更有感情\n\n3. 排比：三个或以上结构相似的句子\n   例：我们要爱护环境，保护地球，珍惜资源。\n   作用：增强语气，使表达更有力\n\n4. 设问：自问自答\n   例：新加坡为什么能成功？因为人民团结努力。\n   作用：引起读者思考\n\n5. 反问：用疑问句表达肯定或否定\n   例：这难道不是我们应该做的吗？\n   作用：加强语气"
            },
            {
                "id": "inference-skills",
                "title": "Making Inferences",
                "title_zh": "推理技巧",
                "type": "text",
                "content": "推理是根据文章信息得出结论的能力。\n\n推理步骤：\n1. 仔细阅读相关段落\n2. 找出关键词和线索\n3. 结合上下文和常识\n4. 得出合理结论\n\n例：李明看着窗外的大雨，叹了口气，放下了足球。\n推理：李明原本想踢足球，但因为下雨而放弃了。\n\n线索词：\n- 因果关系：因此、所以、于是\n- 转折关系：但是、可是、然而\n- 情感词：高兴、失望、担心\n- 动作描写：叹气、皱眉、微笑"
            },
            {
                "id": "analyzing-techniques",
                "title": "Analyzing Writing Techniques",
                "title_zh": "分析写作手法",
                "type": "text",
                "content": "分析写作手法的方法：\n\n1. 描写方法：\n   - 外貌描写：描写人物长相\n   - 动作描写：描写人物行为\n   - 语言描写：写人物说的话\n   - 心理描写：写人物想法\n   例：他紧紧地握着拳头，咬着嘴唇。（动作描写表现紧张）\n\n2. 记叙顺序：\n   - 顺叙：按时间顺序\n   - 倒叙：从结果写起\n   - 插叙：中间插入回忆\n\n3. 表达效果：\n   分析手法如何帮助表达主题\n   例：用对比手法突出人物性格变化"
            }
        ],
        "exercises": []
    },
    {
        "id": "composition-narrative-sec2",
        "gradeLevel": "sec2",
        "title": "Advanced Narrative Composition",
        "title_zh": "高级记叙文写作",
        "description": "Master advanced narrative techniques including detailed descriptions, dialogue, character development, and plot structure",
        "description_zh": "掌握高级记叙文技巧，包括细节描写、对话、人物塑造和情节结构",
        "tag": "Writing",
        "tag_zh": "写作",
        "objectives": [
            "Use detailed descriptions to bring stories to life",
            "Write effective dialogue that reveals character",
            "Structure narratives with clear beginning, development, climax, and resolution",
            "Apply writing techniques learned in reading comprehension"
        ],
        "objectives_zh": [
            "运用细节描写使故事生动",
            "写出能展现人物性格的对话",
            "运用清晰的开端、发展、高潮、结局结构记叙文",
            "应用阅读理解中学到的写作手法"
        ],
        "sections": [
            {
                "id": "detailed-descriptions",
                "title": "Detailed Descriptions",
                "title_zh": "细节描写",
                "type": "text",
                "content": "好的记叙文需要生动的细节描写。\n\n1. 人物描写：\n   - 外貌：高矮胖瘦、五官特征\n   - 动作：走路姿态、手势表情\n   - 语言：说话方式、口头禅\n   - 心理：内心想法、情感变化\n\n例：糟糕的描写：他很生气。\n好的描写：他的脸涨得通红，双手紧握成拳，眼睛瞪得大大的，呼吸急促。\n\n2. 环境描写：\n   - 自然环境：天气、景色\n   - 社会环境：时代背景、风俗\n\n例：烈日当空，知了在树上不停地叫，小贩的叫卖声此起彼伏。（新加坡小贩中心场景）\n\n3. 细节作用：\n   - 使情节更真实\n   - 突出人物性格\n   - 烘托气氛"
            },
            {
                "id": "effective-dialogue",
                "title": "Writing Dialogue",
                "title_zh": "对话写作",
                "type": "text",
                "content": "对话能展现人物性格和推动情节发展。\n\n对话写作要点：\n\n1. 符合人物身份：\n   - 老师：温和、耐心\n   - 学生：活泼、好奇\n   - 长辈：关心、教导\n\n例：\n\"孩子，考试不要紧张，尽力就好。\"妈妈温柔地说。\n\"可是我好担心啊！\"我咬着嘴唇。\n\n2. 对话格式：\n   - 说话内容用引号\n   - 提示语在前、中、后都可以\n   - 每人说话另起一段\n\n3. 提示语的变化：\n   不要只用\"说\"，可以用：\n   - 问、答、喊、叫、笑着说\n   - 小声说、大声说、生气地说\n\n4. 对话要自然，符合生活实际。"
            },
            {
                "id": "plot-structure",
                "title": "Plot Structure",
                "title_zh": "情节结构",
                "type": "text",
                "content": "完整的记叙文有清晰的情节结构：\n\n1. 开端：\n   - 交代时间、地点、人物、事件起因\n   - 可以用环境描写或对话开头\n   例：那是一个炎热的下午，我和同学约好去图书馆温习功课。\n\n2. 发展：\n   - 事情经过，矛盾展开\n   - 详细描写过程\n\n3. 高潮：\n   - 矛盾最激烈的时刻\n   - 情节的转折点\n   - 详细描写，运用各种描写手法\n\n4. 结局：\n   - 事情的结果\n   - 点明中心思想\n   - 可以写感受或启示\n\n布局技巧：\n- 详略得当：重点部分详写\n- 过渡自然：用过渡句连接\n- 首尾呼应：结尾回应开头"
            }
        ],
        "exercises": []
    },
    {
        "id": "idioms-proverbs-advanced-sec2",
        "gradeLevel": "sec2",
        "title": "Advanced Idioms & Classical References",
        "title_zh": "高级成语与典故",
        "description": "Learn advanced idioms, proverbs, classical references, and their appropriate usage in writing and speech",
        "description_zh": "学习高级成语、俗语、典故及其在写作和口语中的恰当运用",
        "tag": "Vocabulary",
        "tag_zh": "词汇",
        "objectives": [
            "Master 40+ advanced idioms and their meanings",
            "Understand the origins and stories behind idioms (典故)",
            "Use idioms appropriately in context",
            "Distinguish between similar idioms"
        ],
        "objectives_zh": [
            "掌握40个以上高级成语及其含义",
            "理解成语背后的典故和故事",
            "在语境中恰当运用成语",
            "区分相似成语"
        ],
        "sections": [
            {
                "id": "advanced-idioms",
                "title": "Advanced Idioms",
                "title_zh": "高级成语",
                "type": "text",
                "content": "中二水平常用成语：\n\n1. 描写学习态度：\n   - 锲而不舍：坚持不懈地努力\n   - 废寝忘食：专心学习，忘记吃饭睡觉\n   - 悬梁刺股：形容刻苦学习\n   - 凿壁偷光：形容勤奋学习\n\n2. 描写人物品质：\n   - 大公无私：办事公正，没有私心\n   - 舍己为人：为了别人牺牲自己\n   - 拾金不昧：捡到钱财不据为己有\n   - 见义勇为：看到正义的事勇敢去做\n\n3. 描写团队合作：\n   - 众志成城：大家团结一致\n   - 同舟共济：一起度过困难\n   - 齐心协力：大家一起努力\n   - 集思广益：集中大家的智慧\n\n4. 描写变化发展：\n   - 日新月异：每天都有新变化\n   - 焕然一新：改变很大，像新的一样\n   - 突飞猛进：进步很快\n   - 脱胎换骨：彻底改变\n\n运用示例：\n新加坡在建国后的几十年里发展日新月异，从第三世界国家脱胎换骨成为发达国家。"
            },
            {
                "id": "idiom-stories",
                "title": "Stories Behind Idioms",
                "title_zh": "成语典故",
                "type": "text",
                "content": "了解成语背后的故事能帮助记忆和运用。\n\n1. 画蛇添足：\n   故事：古代有人画蛇比赛，有个人先画完，又给蛇添上脚，结果反而输了。\n   意思：做了多余的事，反而不好。\n   用法：报告已经很完整了，不要画蛇添足了。\n\n2. 守株待兔：\n   故事：农夫看到兔子撞树而死，就天天等在那里，希望再有兔子送上门。\n   意思：不努力工作，只想靠运气。\n   用法：学习要努力，不能守株待兔等好成绩。\n\n3. 亡羊补牢：\n   故事：羊丢了，赶快修好羊圈，还不算晚。\n   意思：犯了错误后及时改正。\n   用法：这次考试没考好，亡羊补牢，下次要更努力。\n\n4. 熟能生巧：\n   故事：卖油翁把油从钱孔倒入瓶中，滴油不漏，因为练习多了。\n   意思：做得多了就会熟练。\n   用法：写作文要熟能生巧，多写多练。"
            },
            {
                "id": "using-idioms",
                "title": "Using Idioms Correctly",
                "title_zh": "成语运用",
                "type": "text",
                "content": "正确运用成语的方法：\n\n1. 理解准确意思：\n   错误：他学习很好，真是守株待兔。❌\n   正确：他学习很好，真是锲而不舍的结果。✓\n\n2. 注意感情色彩：\n   - 褒义：大公无私、舍己为人\n   - 贬义：自私自利、见利忘义\n   - 中性：日新月异、络绎不绝\n\n3. 注意搭配对象：\n   - 形容人：才华横溢、德高望重\n   - 形容景色：鸟语花香、山清水秀\n   - 形容气势：气势磅礴、波澜壮阔\n\n4. 避免重复：\n   错误：他的成绩突飞猛进地进步了。❌（\"进\"重复）\n   正确：他的成绩突飞猛进。✓\n\n5. 区分近义成语：\n   - 一丝不苟 vs 精益求精\n   - 目不转睛 vs 聚精会神\n   - 恍然大悟 vs 茅塞顿开"
            }
        ],
        "exercises": []
    },
    {
        "id": "practical-writing-sec2",
        "gradeLevel": "sec2",
        "title": "Practical Writing",
        "title_zh": "实用文写作",
        "description": "Master practical writing formats including formal letters, notices, reports, and emails relevant to Singapore context",
        "description_zh": "掌握实用文格式，包括正式书信、通知、报告和电邮，符合新加坡语境",
        "tag": "Writing",
        "tag_zh": "写作",
        "objectives": [
            "Write formal letters with correct format",
            "Compose clear and effective notices",
            "Write structured reports for school activities",
            "Use appropriate tone and language for different purposes"
        ],
        "objectives_zh": [
            "按照正确格式书写正式书信",
            "撰写清晰有效的通知",
            "为学校活动撰写结构化报告",
            "根据不同目的使用恰当的语气和语言"
        ],
        "sections": [
            {
                "id": "formal-letters",
                "title": "Formal Letters",
                "title_zh": "正式书信",
                "type": "text",
                "content": "正式书信格式：\n\n1. 称呼：\n   - 尊敬的校长：\n   - 敬爱的老师：\n   - 亲爱的家长：\n\n2. 正文：\n   - 开头：问候或说明写信目的\n   - 主体：详细说明内容，分段写\n   - 结尾：表达愿望或请求\n\n3. 结束语：\n   - 此致\n   - 敬礼！（另起一行，顶格写）\n\n4. 署名和日期：\n   - 学生：XXX\n   - 2025年1月5日\n\n完整示例：\n\n尊敬的校长：\n\n    您好！我是中二（1）班的学生李明。我写这封信是想建议学校增设华文阅读角。\n\n    我发现很多同学对华文阅读很有兴趣，但图书馆的华文书籍不多。如果能设立阅读角，摆放更多华文读物，相信能提高同学们的华文水平。\n\n    希望校长能考虑我的建议。\n\n此致\n敬礼！\n\n                                    学生：李明\n                                    2025年1月5日"
            },
            {
                "id": "notices-reports",
                "title": "Notices and Reports",
                "title_zh": "通知与报告",
                "type": "text",
                "content": "通知的格式：\n\n标题：通知\n\n正文：\n- 说明事项（5W1H：何时、何地、何事、何人、为何、如何）\n- 语言简洁明了\n- 重点信息突出\n\n落款：\n- 发通知的单位\n- 日期\n\n示例：\n\n通知\n\n    为了提高同学们的华文水平，学校将于本月20日（星期六）上午9点在礼堂举办华文演讲比赛。欢迎中一至中三的同学踊跃报名参加。\n\n    报名截止日期：本月15日\n    报名地点：华文部办公室\n\n                                    华文部\n                                    2025年1月5日\n\n---\n\n活动报告的结构：\n\n1. 标题：XX活动报告\n2. 基本信息：日期、地点、参与人数\n3. 活动内容：详细描述活动过程\n4. 活动成果：取得的效果\n5. 总结：收获和建议\n\n语言特点：\n- 客观、准确\n- 条理清晰\n- 数据具体"
            },
            {
                "id": "email-writing",
                "title": "Email Writing",
                "title_zh": "电邮写作",
                "type": "text",
                "content": "电子邮件写作要点：\n\n1. 主题栏（Subject）：\n   - 简洁明了，说明邮件目的\n   - 例：关于华文作业的询问\n\n2. 称呼：\n   - 正式：尊敬的XX老师\n   - 半正式：XX老师好\n\n3. 正文：\n   开头段：\n   - 问候\n   - 说明写信目的\n   例：您好！我是中二（3）班的学生张伟。我想询问关于华文作业的问题。\n\n   主体段：\n   - 详细说明\n   - 分点列出（如有多个问题）\n\n   结尾段：\n   - 表示感谢\n   - 期待回复\n   例：谢谢老师的帮助。期待您的回复。\n\n4. 结束语：\n   - 祝：工作顺利！\n   - 学生：张伟\n\n5. 注意事项：\n   - 语气礼貌\n   - 简洁清晰\n   - 检查错别字\n   - 附件说明清楚"
            }
        ],
        "exercises": []
    },
    {
        "id": "oral-communication-sec2",
        "gradeLevel": "sec2",
        "title": "Oral Communication & Discussion",
        "title_zh": "口语交际与讨论",
        "description": "Develop oral communication skills including presenting ideas, participating in discussions, and expressing opinions clearly",
        "description_zh": "培养口语交际能力，包括陈述观点、参与讨论和清晰表达意见",
        "tag": "Speaking",
        "tag_zh": "口语",
        "objectives": [
            "Present ideas clearly and logically in Chinese",
            "Participate effectively in group discussions",
            "Express and support opinions with reasons",
            "Use appropriate language for formal and informal situations"
        ],
        "objectives_zh": [
            "用华语清晰有逻辑地陈述观点",
            "有效参与小组讨论",
            "表达观点并提供理由支持",
            "在正式和非正式场合使用恰当的语言"
        ],
        "sections": [
            {
                "id": "presentation-skills",
                "title": "Presentation Skills",
                "title_zh": "演讲技巧",
                "type": "text",
                "content": "华文演讲的准备和技巧：\n\n1. 准备阶段：\n   - 确定主题和观点\n   - 收集资料和例子\n   - 列出要点\n   - 准备开头和结尾\n\n2. 演讲结构：\n   开头：\n   - 问候听众\n   - 介绍主题\n   - 引起兴趣（问题、故事、数据）\n   例：大家好！今天我要谈的是环保的重要性。你们知道新加坡每天产生多少垃圾吗？\n\n   主体：\n   - 分点说明（第一、第二、第三）\n   - 每点都有例子或数据支持\n   - 使用过渡语（首先、其次、此外、最后）\n\n   结尾：\n   - 总结要点\n   - 呼吁行动或提出希望\n   - 感谢听众\n   例：总而言之，环保需要大家一起努力。让我们从今天开始，从小事做起。谢谢大家！\n\n3. 演讲技巧：\n   - 语速适中，吐字清晰\n   - 声音洪亮，有抑扬顿挫\n   - 眼神交流，不要只看稿子\n   - 适当的手势和表情\n   - 自信、自然"
            },
            {
                "id": "discussion-skills",
                "title": "Discussion Skills",
                "title_zh": "讨论技巧",
                "type": "text",
                "content": "参与小组讨论的技巧：\n\n1. 表达观点：\n   - 我认为...\n   - 在我看来...\n   - 依我之见...\n   - 我的看法是...\n\n2. 表示同意：\n   - 我同意你的观点。\n   - 我也这么认为。\n   - 你说得很对。\n   - 这个想法不错。\n\n3. 表示不同意见（礼貌地）：\n   - 我有不同的看法。\n   - 我不太同意，因为...\n   - 这个观点值得商榷。\n   - 或许我们可以从另一个角度看...\n\n4. 提出建议：\n   - 我建议...\n   - 不如我们...\n   - 也许可以...\n   - 我们是否可以...\n\n5. 总结讨论：\n   - 综合大家的意见...\n   - 总的来说...\n   - 我们达成的共识是...\n\n讨论态度：\n   - 认真倾听别人的发言\n   - 不打断别人\n   - 尊重不同意见\n   - 积极参与，不沉默\n   - 理性分析，有理有据"
            },
            {
                "id": "situational-communication",
                "title": "Situational Communication",
                "title_zh": "情景交际",
                "type": "text",
                "content": "不同情景的交际用语：\n\n1. 求助：\n   - 请问，您能帮我一个忙吗？\n   - 不好意思，我想请教您一个问题。\n   - 麻烦您了。\n\n2. 道歉：\n   - 对不起，是我的错。\n   - 真不好意思，给您添麻烦了。\n   - 请原谅。\n\n3. 感谢：\n   - 谢谢您的帮助。\n   - 太感谢您了。\n   - 您真是帮了大忙。\n\n4. 请求许可：\n   - 我可以...吗？\n   - 能否让我...？\n   - 不知道方不方便...？\n\n5. 拒绝（礼貌）：\n   - 对不起，恐怕不行。\n   - 很抱歉，我可能帮不了您。\n   - 不好意思，我有其他安排。\n\n6. 邀请：\n   - 周末有空吗？我们一起去图书馆吧。\n   - 不知道你有没有兴趣参加...？\n   - 我想邀请你...\n\n新加坡语境示例：\n- 在组屋楼下遇到邻居：早安！今天天气真好。\n- 在小贩中心：老板，麻烦来一份鸡饭。\n- 在学校向老师请教：老师，这道题我不太明白，能不能请您再解释一下？"
            }
        ],
        "exercises": []
    }
]

# Save to JSON file
with open('chapters/sec2-chinese-chapters.json', 'w', encoding='utf-8') as f:
    json.dump(sec2_chinese_chapters, f, ensure_ascii=False, indent=2)

print(f"Created {len(sec2_chinese_chapters)} Secondary 2 Chinese chapters")
print("Chapters:", [ch['title_zh'] for ch in sec2_chinese_chapters])
