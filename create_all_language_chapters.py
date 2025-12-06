#!/usr/bin/env python3
"""Create Sec 3 and Sec 4 English and Chinese chapters."""
import json
import os
from datetime import datetime

def create_sec3_english():
    """Create Sec 3 English chapters."""
    return [
        {
            "id": "argumentative-writing-sec3",
            "gradeLevel": "sec3",
            "title": "Argumentative Writing",
            "title_zh": "议论文写作",
            "description": "Construct well-reasoned arguments with evidence and counterarguments",
            "description_zh": "用证据和反论点构建有理有据的论点",
            "tag": "Writing",
            "tag_zh": "写作",
            "objectives": ["Structure an argument with thesis, evidence, and conclusion", "Use persuasive techniques effectively", "Address and refute counterarguments", "Support claims with relevant examples"],
            "objectives_zh": ["用论点、证据和结论构建论证结构", "有效使用说服技巧", "处理和反驳反论点", "用相关例子支持观点"],
            "sections": [
                {"id": "argument-structure", "title": "Structure of an Argument", "title_zh": "论证结构", "type": "text",
                 "content": "A strong argumentative essay follows a clear structure:\n\n**1. Introduction**\n- Hook: Engage the reader\n- Context: Background information\n- Thesis Statement: State your position\n\n**2. Body Paragraphs (PEEL Structure)**\n- Point: State your main argument\n- Evidence: Provide facts or examples\n- Explanation: Analyze the evidence\n- Link: Connect back to thesis\n\n**3. Counterargument Paragraph**\n- Acknowledge opposing views\n- Refute with stronger evidence\n\n**4. Conclusion**\n- Restate thesis\n- Summarize key points\n- Call to action"},
                {"id": "persuasive-techniques", "title": "Persuasive Techniques", "title_zh": "说服技巧", "type": "text",
                 "content": "**Rhetorical Appeals:**\n\n**1. Ethos (Credibility)**\n- Cite experts and authorities\n- Example: According to NEA reports...\n\n**2. Pathos (Emotion)**\n- Use vivid language and imagery\n- Example: Imagine a Singapore where every child breathes clean air...\n\n**3. Logos (Logic)**\n- Present facts and statistics\n- Example: Studies show that 70% of Singaporeans support...\n\n**Other Techniques:**\n- Rhetorical questions\n- Repetition\n- Rule of three\n- Inclusive language"},
                {"id": "counterarguments", "title": "Handling Counterarguments", "title_zh": "处理反论点", "type": "text",
                 "content": "**How to Address Counterarguments:**\n\n**Step 1: Acknowledge**\n- Some may argue that...\n- Critics might contend...\n\n**Step 2: Refute**\n- However, this view overlooks...\n- This argument fails to consider...\n\n**Example:**\nSome argue that banning plastic bags inconveniences consumers. However, this minor inconvenience is far outweighed by the environmental benefits."}
            ],
            "exercises": generate_exercises("arg-sec3", "argumentative", "en")
        },
        {
            "id": "literary-analysis-sec3",
            "gradeLevel": "sec3",
            "title": "Literary Analysis & Appreciation",
            "title_zh": "文学分析与鉴赏",
            "description": "Analyze literary texts including poetry, prose, and drama",
            "description_zh": "分析诗歌、散文和戏剧等文学文本",
            "tag": "Literature",
            "tag_zh": "文学",
            "objectives": ["Identify and analyze literary devices", "Understand themes and characters", "Write literary analysis essays", "Appreciate different genres"],
            "objectives_zh": ["识别和分析文学手法", "理解主题和人物", "写文学分析文章", "欣赏不同体裁"],
            "sections": [
                {"id": "literary-devices", "title": "Literary Devices", "title_zh": "文学手法", "type": "text",
                 "content": "**Sound Devices:**\n- Alliteration: Repetition of initial consonant sounds\n- Onomatopoeia: Words that imitate sounds\n\n**Figurative Language:**\n- Simile: Comparison using like or as\n- Metaphor: Direct comparison\n- Personification: Human qualities to non-human things\n- Hyperbole: Exaggeration\n\n**Structural Devices:**\n- Foreshadowing: Hints about future events\n- Flashback: Return to earlier events\n- Irony: Contrast between expectation and reality\n- Symbolism: Objects representing abstract ideas"},
                {"id": "analyzing-poetry", "title": "Analyzing Poetry", "title_zh": "分析诗歌", "type": "text",
                 "content": "**SMILE Framework:**\n- Structure: How is the poem organized?\n- Meaning: What is the poem about?\n- Imagery: What pictures does it create?\n- Language: What techniques are used?\n- Effect: How does it make readers feel?\n\n**Consider:**\n- Stanza structure and line length\n- Rhyme scheme (ABAB, AABB)\n- Word choice and imagery"},
                {"id": "essay-writing", "title": "Writing Literary Analysis Essays", "title_zh": "写文学分析文章", "type": "text",
                 "content": "**TEA Structure:**\n- Technique: Identify the literary device\n- Evidence: Quote from the text\n- Analysis: Explain the effect\n\n**Example:**\nThe metaphor 'Singapore is a concrete jungle' (technique) is evident in the line 'towers of steel pierce the sky' (evidence). This imagery suggests the tension between nature and urbanization (analysis)."}
            ],
            "exercises": generate_exercises("lit-sec3", "literary", "en")
        },
        {
            "id": "report-writing-sec3",
            "gradeLevel": "sec3",
            "title": "Report Writing",
            "title_zh": "报告写作",
            "description": "Write structured reports including factual and recommendation reports",
            "description_zh": "撰写事实性和建议性报告",
            "tag": "Writing",
            "tag_zh": "写作",
            "objectives": ["Understand different types of reports", "Use formal register and objective tone", "Structure reports with clear sections", "Present findings effectively"],
            "objectives_zh": ["了解不同类型的报告", "使用正式语域和客观语气", "用清晰的章节构建报告", "有效呈现发现"],
            "sections": [
                {"id": "report-types", "title": "Types of Reports", "title_zh": "报告类型", "type": "text",
                 "content": "**1. Factual Reports**\n- Present facts without opinion\n- News reports, accident reports\n\n**2. Investigative Reports**\n- Research a topic or problem\n- Include methodology and findings\n\n**3. Recommendation Reports**\n- Analyze a situation\n- Suggest solutions"},
                {"id": "report-structure", "title": "Report Structure", "title_zh": "报告结构", "type": "text",
                 "content": "**1. Title** - Clear and informative\n\n**2. Introduction**\n- Purpose, scope, methodology\n\n**3. Findings** - Organized with subheadings\n\n**4. Conclusion** - Summarize key findings\n\n**5. Recommendations** - Practical suggestions"},
                {"id": "formal-language", "title": "Formal Language", "title_zh": "正式语言", "type": "text",
                 "content": "**Use:**\n- Third person: It was found that...\n- Passive voice: The survey was conducted...\n- Formal vocabulary: approximately not about\n\n**Avoid:**\n- Contractions\n- Colloquialisms\n- Personal pronouns"}
            ],
            "exercises": generate_exercises("report-sec3", "report", "en")
        },
        {
            "id": "advanced-comprehension-sec3",
            "gradeLevel": "sec3",
            "title": "Advanced Reading Comprehension",
            "title_zh": "高级阅读理解",
            "description": "Master inference, evaluation, and synthesis skills",
            "description_zh": "掌握推断、评价和综合技能",
            "tag": "Reading",
            "tag_zh": "阅读",
            "objectives": ["Make inferences from texts", "Evaluate author's purpose and bias", "Synthesize information from multiple sources", "Analyze rhetorical techniques"],
            "objectives_zh": ["从文本中进行推断", "评估作者目的和偏见", "综合来自多个来源的信息", "分析修辞技巧"],
            "sections": [
                {"id": "inference-skills", "title": "Making Inferences", "title_zh": "进行推断", "type": "text",
                 "content": "**What is Inference?**\nUsing clues in the text + your knowledge to understand unstated information.\n\n**Types:**\n1. Character Inferences - What can we infer about a character?\n2. Setting Inferences - Where and when is this taking place?\n3. Cause-Effect Inferences - Why did something happen?"},
                {"id": "evaluating-texts", "title": "Evaluating Texts", "title_zh": "评估文本", "type": "text",
                 "content": "**Author's Purpose:**\n- Persuade, Inform, Entertain, Instruct\n\n**Detecting Bias:**\n- One-sided arguments\n- Emotional language\n- Selective statistics\n- Loaded words"},
                {"id": "synthesis-skills", "title": "Synthesizing Information", "title_zh": "综合信息", "type": "text",
                 "content": "**Steps:**\n1. Identify Main Ideas\n2. Find Connections\n3. Compare & Contrast\n4. Form Your Conclusion\n\n**Signal Words:**\n- Both sources agree that...\n- While Source A focuses on..., Source B emphasizes..."}
            ],
            "exercises": generate_exercises("comp-sec3", "comprehension", "en")
        },
        {
            "id": "oral-communication-sec3",
            "gradeLevel": "sec3",
            "title": "Oral Communication Skills",
            "title_zh": "口语交际技能",
            "description": "Develop speaking skills for presentations and discussions",
            "description_zh": "发展演示和讨论的口语技能",
            "tag": "Speaking",
            "tag_zh": "口语",
            "objectives": ["Deliver clear presentations", "Participate in discussions", "Prepare for oral examinations", "Use appropriate verbal and non-verbal communication"],
            "objectives_zh": ["进行清晰的演示", "参与讨论", "准备口语考试", "使用适当的语言和非语言交流"],
            "sections": [
                {"id": "presentation-skills", "title": "Presentation Skills", "title_zh": "演示技能", "type": "text",
                 "content": "**Preparation:**\n1. Know Your Audience\n2. Structure Your Content (Opening, Body, Closing)\n3. Create Visual Aids (6x6 rule)\n\n**Delivery:**\n- Speak clearly at moderate pace\n- Maintain eye contact\n- Use natural gestures"},
                {"id": "discussion-skills", "title": "Discussion Skills", "title_zh": "讨论技能", "type": "text",
                 "content": "**Contributing Effectively:**\n- Build on others' ideas: Adding to what [name] said...\n- Offer different perspectives: Another way to look at this is...\n- Support points with examples\n\n**Respectful Disagreement:**\n- I see your point, but I think...\n- That's interesting, however..."},
                {"id": "oral-exam-prep", "title": "Oral Examination Preparation", "title_zh": "口语考试准备", "type": "text",
                 "content": "**Reading Aloud:**\n- Read at a comfortable pace\n- Use appropriate expression\n- Pause at punctuation\n\n**Picture Discussion:**\n1. Describe what you see\n2. Give personal response\n3. Extend discussion"}
            ],
            "exercises": generate_exercises("oral-sec3", "oral", "en")
        },
        {
            "id": "vocabulary-expansion-sec3",
            "gradeLevel": "sec3",
            "title": "Advanced Vocabulary & Word Power",
            "title_zh": "高级词汇和词汇力量",
            "description": "Expand vocabulary through word roots and context",
            "description_zh": "通过词根和语境扩展词汇",
            "tag": "Vocabulary",
            "tag_zh": "词汇",
            "objectives": ["Use Greek and Latin roots", "Apply context clues", "Master academic vocabulary", "Understand connotation and denotation"],
            "objectives_zh": ["使用希腊和拉丁词根", "应用上下文线索", "掌握学术词汇", "理解内涵和外延"],
            "sections": [
                {"id": "word-roots", "title": "Greek and Latin Roots", "title_zh": "希腊和拉丁词根", "type": "text",
                 "content": "**Greek Roots:**\n- bio (life): biology, biography\n- graph (write): autograph, paragraph\n- phone (sound): telephone, symphony\n\n**Latin Roots:**\n- dict (say): dictate, predict\n- port (carry): transport, export\n- scrib/script (write): describe, manuscript"},
                {"id": "context-clues-advanced", "title": "Advanced Context Clues", "title_zh": "高级上下文线索", "type": "text",
                 "content": "**Types:**\n1. Definition Clues - meaning directly stated\n2. Example Clues - examples help clarify\n3. Contrast Clues - opposite words signal meaning\n4. Cause/Effect Clues - results help explain"},
                {"id": "academic-vocabulary", "title": "Academic Vocabulary", "title_zh": "学术词汇", "type": "text",
                 "content": "**Transition Words:**\n- Addition: furthermore, moreover\n- Contrast: however, nevertheless\n- Cause/Effect: consequently, therefore\n\n**Connotation vs Denotation:**\n- Denotation: Dictionary meaning\n- Connotation: Emotional association"}
            ],
            "exercises": generate_exercises("vocab-sec3", "vocabulary", "en")
        }
    ]

def create_sec4_english():
    """Create Sec 4 English chapters."""
    return [
        {
            "id": "critical-essay-writing-sec4",
            "gradeLevel": "sec4",
            "title": "Critical Essay Writing",
            "title_zh": "批判性论文写作",
            "description": "Write sophisticated argumentative and discursive essays for O-Level",
            "description_zh": "为O水准考试撰写复杂的议论文",
            "tag": "Writing",
            "tag_zh": "写作",
            "objectives": ["Structure complex argumentative essays", "Develop nuanced thesis statements", "Use advanced rhetorical techniques", "Integrate evidence effectively"],
            "objectives_zh": ["构建复杂议论文结构", "发展细致的论点陈述", "使用高级修辞技巧", "有效整合证据"],
            "sections": [
                {"id": "thesis-development", "title": "Developing Strong Thesis Statements", "title_zh": "发展论点陈述", "type": "text",
                 "content": "**Strong Thesis Characteristics:**\n- Specific and arguable\n- Takes a clear position\n- Previews main arguments\n\n**Thesis Formula:**\n[Topic] + [Position] + [Reasons/Preview]"},
                {"id": "essay-structure-advanced", "title": "Advanced Essay Structure", "title_zh": "高级论文结构", "type": "text",
                 "content": "**TEEL+ Structure:**\n- Topic sentence\n- Evidence\n- Explanation\n- Link\n- Extension (broader implications)"},
                {"id": "rhetorical-techniques", "title": "Advanced Rhetorical Techniques", "title_zh": "高级修辞技巧", "type": "text",
                 "content": "**Techniques:**\n1. Rhetorical Questions\n2. Tricolon (Rule of Three)\n3. Antithesis\n4. Anaphora (Repetition)\n5. Inclusive Language"}
            ],
            "exercises": generate_exercises("essay-sec4", "essay", "en")
        },
        {
            "id": "advanced-literary-analysis-sec4",
            "gradeLevel": "sec4",
            "title": "Advanced Literary Analysis",
            "title_zh": "高级文学分析",
            "description": "Analyze literary texts with depth for O-Level Literature",
            "description_zh": "深入分析O水准文学文本",
            "tag": "Literature",
            "tag_zh": "文学",
            "objectives": ["Analyze complex literary texts", "Write sophisticated literary essays", "Compare and contrast texts", "Evaluate authorial choices"],
            "objectives_zh": ["分析复杂文学文本", "撰写复杂文学论文", "比较和对比文本", "评估作者选择"],
            "sections": [
                {"id": "advanced-analysis", "title": "Advanced Analysis Techniques", "title_zh": "高级分析技巧", "type": "text",
                 "content": "**Analyzing Complex Texts:**\n1. Multiple interpretations\n2. Historical context\n3. Author's biography\n4. Literary movements"},
                {"id": "comparative-analysis", "title": "Comparative Analysis", "title_zh": "比较分析", "type": "text",
                 "content": "**Comparing Texts:**\n- Similar themes, different approaches\n- Same author, different periods\n- Different genres, same topic"},
                {"id": "literary-essay", "title": "Writing Literary Essays", "title_zh": "撰写文学论文", "type": "text",
                 "content": "**Essay Structure:**\n1. Clear thesis about the text\n2. Multiple supporting paragraphs\n3. Integrated quotations\n4. Analysis of effect"}
            ],
            "exercises": generate_exercises("adv-lit-sec4", "literature", "en")
        },
        {
            "id": "synthesis-comprehension-sec4",
            "gradeLevel": "sec4",
            "title": "Synthesis & Comprehension",
            "title_zh": "综合与理解",
            "description": "Master multi-text comprehension for O-Level",
            "description_zh": "掌握O水准多文本理解",
            "tag": "Reading",
            "tag_zh": "阅读",
            "objectives": ["Synthesize information from multiple texts", "Evaluate and compare sources", "Identify implicit meanings", "Write cohesive responses"],
            "objectives_zh": ["综合多个文本的信息", "评估和比较来源", "识别隐含意义", "撰写连贯的回答"],
            "sections": [
                {"id": "multi-text-synthesis", "title": "Multi-Text Synthesis", "title_zh": "多文本综合", "type": "text", "content": "**Strategies:**\n1. Identify key points in each text\n2. Find connections and contrasts\n3. Create unified response"},
                {"id": "inference-evaluation", "title": "Inference and Evaluation", "title_zh": "推断和评估", "type": "text", "content": "**Advanced Inference:**\n- Read between the lines\n- Consider author's purpose\n- Evaluate reliability"},
                {"id": "response-writing", "title": "Writing Responses", "title_zh": "撰写回答", "type": "text", "content": "**Effective Responses:**\n- Answer all parts of the question\n- Use evidence from texts\n- Maintain objectivity"}
            ],
            "exercises": generate_exercises("synth-sec4", "synthesis", "en")
        },
        {
            "id": "summary-writing-sec4",
            "gradeLevel": "sec4",
            "title": "Summary Writing Skills",
            "title_zh": "摘要写作技巧",
            "description": "Develop concise summary writing skills for O-Level",
            "description_zh": "培养O水准摘要写作技巧",
            "tag": "Writing",
            "tag_zh": "写作",
            "objectives": ["Identify key points for summaries", "Paraphrase effectively", "Maintain word limits", "Organize information logically"],
            "objectives_zh": ["识别摘要要点", "有效改写", "保持字数限制", "逻辑组织信息"],
            "sections": [
                {"id": "summary-techniques", "title": "Summary Techniques", "title_zh": "摘要技巧", "type": "text", "content": "**Key Steps:**\n1. Read and understand the passage\n2. Identify main points\n3. Paraphrase in your own words\n4. Combine points smoothly"},
                {"id": "paraphrasing", "title": "Effective Paraphrasing", "title_zh": "有效改写", "type": "text", "content": "**Techniques:**\n- Change word forms\n- Use synonyms\n- Change sentence structure\n- Combine sentences"},
                {"id": "word-limit", "title": "Managing Word Limits", "title_zh": "管理字数限制", "type": "text", "content": "**Strategies:**\n- Remove examples\n- Eliminate repetition\n- Use concise phrases\n- Focus on essential information"}
            ],
            "exercises": generate_exercises("summary-sec4", "summary", "en")
        },
        {
            "id": "situational-writing-sec4",
            "gradeLevel": "sec4",
            "title": "Situational Writing",
            "title_zh": "情境写作",
            "description": "Master formal letters, reports, proposals, and speeches",
            "description_zh": "掌握正式信函、报告、提案和演讲",
            "tag": "Writing",
            "tag_zh": "写作",
            "objectives": ["Write formal letters and emails", "Create effective reports", "Develop compelling proposals", "Craft engaging speeches"],
            "objectives_zh": ["撰写正式信函和电邮", "创建有效报告", "制定引人注目的提案", "撰写引人入胜的演讲"],
            "sections": [
                {"id": "formal-correspondence", "title": "Formal Correspondence", "title_zh": "正式通信", "type": "text", "content": "**Letter Format:**\n1. Sender's address\n2. Date\n3. Recipient's address\n4. Salutation\n5. Body\n6. Closing"},
                {"id": "proposals-reports", "title": "Proposals and Reports", "title_zh": "提案和报告", "type": "text", "content": "**Proposal Structure:**\n1. Introduction and purpose\n2. Problem statement\n3. Proposed solution\n4. Benefits\n5. Conclusion"},
                {"id": "speech-writing", "title": "Speech Writing", "title_zh": "演讲写作", "type": "text", "content": "**Speech Elements:**\n1. Engaging opening\n2. Clear main points\n3. Supporting evidence\n4. Memorable conclusion"}
            ],
            "exercises": generate_exercises("sit-sec4", "situational", "en")
        },
        {
            "id": "oral-examination-sec4",
            "gradeLevel": "sec4",
            "title": "O-Level Oral Examination",
            "title_zh": "O水准口试",
            "description": "Prepare for O-Level oral examination",
            "description_zh": "准备O水准口试",
            "tag": "Speaking",
            "tag_zh": "口语",
            "objectives": ["Excel in reading aloud", "Engage in spoken interaction", "Discuss visual prompts effectively", "Express opinions with confidence"],
            "objectives_zh": ["朗读出色", "参与口语互动", "有效讨论视觉提示", "自信表达观点"],
            "sections": [
                {"id": "reading-aloud-olevel", "title": "Reading Aloud", "title_zh": "朗读", "type": "text", "content": "**Key Skills:**\n1. Clear pronunciation\n2. Appropriate pace\n3. Expression and intonation\n4. Meaningful pauses"},
                {"id": "spoken-interaction", "title": "Spoken Interaction", "title_zh": "口语互动", "type": "text", "content": "**Strategies:**\n1. Listen carefully to questions\n2. Give developed responses\n3. Support with examples\n4. Show critical thinking"},
                {"id": "visual-discussion", "title": "Visual Stimulus Discussion", "title_zh": "视觉刺激讨论", "type": "text", "content": "**Approach:**\n1. Describe what you see\n2. Analyze the situation\n3. Connect to broader issues\n4. Give personal opinions"}
            ],
            "exercises": generate_exercises("oral-sec4", "oral_exam", "en")
        }
    ]

def create_sec3_chinese():
    """Create Sec 3 Chinese chapters."""
    return [
        {
            "id": "argumentative-writing-chinese-sec3",
            "gradeLevel": "sec3",
            "title": "Argumentative Writing",
            "title_zh": "议论文写作",
            "description": "Master argumentative writing in Chinese",
            "description_zh": "掌握中文议论文写作",
            "tag": "Writing",
            "tag_zh": "写作",
            "objectives": ["Structure argumentative essays", "Use persuasive techniques in Chinese", "Address counterarguments", "Support claims with evidence"],
            "objectives_zh": ["构建议论文结构", "运用中文说服技巧", "处理反论点", "用证据支持观点"],
            "sections": [
                {"id": "arg-structure-zh", "title": "Argumentative Essay Structure", "title_zh": "议论文结构", "type": "text",
                 "content": "议论文的基本结构:\n\n**1. 引言**\n- 引出话题\n- 提出论点\n\n**2. 正文**\n- 分论点 + 论据 + 分析\n\n**3. 反论**\n- 承认对方观点\n- 反驳\n\n**4. 结论**\n- 重申论点\n- 总结"},
                {"id": "persuasive-tech-zh", "title": "Persuasive Techniques", "title_zh": "说服技巧", "type": "text",
                 "content": "**常用说服技巧:**\n\n1. 引用权威\n2. 举例论证\n3. 对比论证\n4. 因果论证\n5. 反问"},
                {"id": "counter-args-zh", "title": "Handling Counterarguments", "title_zh": "处理反论点", "type": "text",
                 "content": "**步骤:**\n\n1. 承认: 诚然...\n2. 转折: 然而...\n3. 反驳: 提供更有力的证据"}
            ],
            "exercises": generate_exercises("arg-zh-sec3", "argumentative", "zh")
        },
        {
            "id": "classical-chinese-sec3",
            "gradeLevel": "sec3",
            "title": "Classical Chinese Reading",
            "title_zh": "文言文阅读",
            "description": "Understand and appreciate classical Chinese texts",
            "description_zh": "理解和欣赏文言文",
            "tag": "Reading",
            "tag_zh": "阅读",
            "objectives": ["Understand common classical vocabulary", "Translate classical to modern Chinese", "Appreciate classical literature", "Identify literary techniques"],
            "objectives_zh": ["理解常见文言词汇", "翻译文言文", "欣赏古典文学", "识别文学手法"],
            "sections": [
                {"id": "classical-vocab", "title": "Common Classical Vocabulary", "title_zh": "常见文言词汇", "type": "text",
                 "content": "**常见文言词汇:**\n\n人称代词: 吾(我), 汝(你), 其(他)\n动词: 曰(说), 往(去), 观(看)\n虚词: 之(的), 而(并且), 以(用)"},
                {"id": "classical-translation", "title": "Translation Techniques", "title_zh": "翻译技巧", "type": "text",
                 "content": "**翻译方法:**\n\n1. 保留: 人名地名不译\n2. 替换: 用现代词替换古代词\n3. 补充: 补充省略成分\n4. 调整: 调整语序\n5. 删除: 删除无意义的词"},
                {"id": "classical-appreciation", "title": "Literary Appreciation", "title_zh": "文学鉴赏", "type": "text",
                 "content": "**鉴赏要点:**\n\n1. 主题思想\n2. 人物形象\n3. 写作手法\n4. 语言特色"}
            ],
            "exercises": generate_exercises("classical-sec3", "classical", "zh")
        },
        {
            "id": "advanced-composition-sec3",
            "gradeLevel": "sec3",
            "title": "Advanced Composition",
            "title_zh": "高级作文",
            "description": "Master various composition types and techniques",
            "description_zh": "掌握各种作文类型和技巧",
            "tag": "Writing",
            "tag_zh": "写作",
            "objectives": ["Write different composition types", "Apply advanced techniques", "Structure essays effectively", "Use rich vocabulary"],
            "objectives_zh": ["撰写不同类型作文", "应用高级技巧", "有效构建文章", "使用丰富词汇"],
            "sections": [
                {"id": "composition-types", "title": "Composition Types", "title_zh": "作文类型", "type": "text",
                 "content": "**作文类型:**\n\n1. 记叙文\n2. 议论文\n3. 说明文\n4. 应用文"},
                {"id": "writing-techniques", "title": "Writing Techniques", "title_zh": "写作技巧", "type": "text",
                 "content": "**技巧:**\n\n开头: 开门见山, 设置悬念\n结尾: 总结全文, 点明主题\n描写: 细节, 环境, 心理"},
                {"id": "structure-planning", "title": "Structure Planning", "title_zh": "结构安排", "type": "text",
                 "content": "**结构:**\n\n1. 总分总\n2. 时间顺序\n3. 空间顺序"}
            ],
            "exercises": generate_exercises("comp-zh-sec3", "composition", "zh")
        },
        {
            "id": "comprehension-skills-sec3",
            "gradeLevel": "sec3",
            "title": "Reading Comprehension Skills",
            "title_zh": "阅读理解技巧",
            "description": "Develop advanced reading and analysis skills",
            "description_zh": "发展高级阅读和分析技能",
            "tag": "Reading",
            "tag_zh": "阅读",
            "objectives": ["Apply reading strategies", "Analyze question types", "Use answer techniques", "Evaluate texts critically"],
            "objectives_zh": ["应用阅读策略", "分析题型", "使用答题技巧", "批判性评估文本"],
            "sections": [
                {"id": "reading-strategies", "title": "Reading Strategies", "title_zh": "阅读策略", "type": "text",
                 "content": "**策略:**\n\n1. 略读: 抓大意\n2. 精读: 分析细节\n3. 批判性阅读: 分析评价"},
                {"id": "question-types", "title": "Question Types", "title_zh": "题型分析", "type": "text",
                 "content": "**常见题型:**\n\n1. 理解题\n2. 分析题\n3. 评价题"},
                {"id": "answer-techniques", "title": "Answer Techniques", "title_zh": "答题技巧", "type": "text",
                 "content": "**技巧:**\n\n1. 审题: 明确问什么\n2. 定位: 找答案\n3. 组织: 条理清晰"}
            ],
            "exercises": generate_exercises("reading-zh-sec3", "comprehension", "zh")
        },
        {
            "id": "oral-chinese-sec3",
            "gradeLevel": "sec3",
            "title": "Oral Communication",
            "title_zh": "口语交际",
            "description": "Develop effective Chinese speaking skills",
            "description_zh": "发展有效的中文口语技能",
            "tag": "Speaking",
            "tag_zh": "口语",
            "objectives": ["Improve oral reading", "Develop conversation skills", "Participate in discussions", "Express opinions clearly"],
            "objectives_zh": ["提高朗读能力", "发展会话技巧", "参与讨论", "清晰表达观点"],
            "sections": [
                {"id": "oral-reading", "title": "Oral Reading Skills", "title_zh": "朗读技巧", "type": "text",
                 "content": "**技巧:**\n\n1. 语音准确\n2. 语调自然\n3. 节奏把握"},
                {"id": "conversation-skills", "title": "Conversation Skills", "title_zh": "会话技巧", "type": "text",
                 "content": "**技巧:**\n\n1. 表达清晰\n2. 互动交流\n3. 礼貌用语"},
                {"id": "discussion-skills", "title": "Discussion Skills", "title_zh": "讨论技巧", "type": "text",
                 "content": "**技巧:**\n\n1. 表达观点\n2. 支持观点\n3. 回应他人"}
            ],
            "exercises": generate_exercises("oral-zh-sec3", "oral", "zh")
        },
        {
            "id": "proverbs-idioms-sec3",
            "gradeLevel": "sec3",
            "title": "Proverbs and Idioms",
            "title_zh": "成语与谚语",
            "description": "Master Chinese idioms and proverbs",
            "description_zh": "掌握成语和谚语",
            "tag": "Vocabulary",
            "tag_zh": "词汇",
            "objectives": ["Understand idiom structures", "Use idioms correctly", "Learn common proverbs", "Apply in writing"],
            "objectives_zh": ["理解成语结构", "正确使用成语", "学习常用谚语", "应用于写作"],
            "sections": [
                {"id": "idiom-structure", "title": "Idiom Structure", "title_zh": "成语结构", "type": "text",
                 "content": "**结构类型:**\n\n1. 主谓结构: 愚公移山\n2. 动宾结构: 守株待兔\n3. 并列结构: 山清水秀"},
                {"id": "idiom-usage", "title": "Idiom Usage", "title_zh": "成语运用", "type": "text",
                 "content": "**运用:**\n\n1. 理解含义\n2. 注意褒贬\n3. 正确搭配"},
                {"id": "proverbs", "title": "Chinese Proverbs", "title_zh": "谚语", "type": "text",
                 "content": "**常用谚语:**\n\n学习: 活到老,学到老\n品德: 一分耕耘,一分收获\n生活: 吃一堑,长一智"}
            ],
            "exercises": generate_exercises("idiom-sec3", "idioms", "zh")
        }
    ]

def create_sec4_chinese():
    """Create Sec 4 Chinese chapters."""
    return [
        {
            "id": "olevel-composition-sec4",
            "gradeLevel": "sec4",
            "title": "O-Level Composition",
            "title_zh": "O水准作文",
            "description": "Master composition for O-Level Chinese",
            "description_zh": "掌握O水准华文作文",
            "tag": "Writing",
            "tag_zh": "写作",
            "objectives": ["Write polished exam essays", "Apply advanced techniques", "Structure effectively", "Use rich vocabulary"],
            "objectives_zh": ["撰写精炼考试作文", "应用高级技巧", "有效构建结构", "使用丰富词汇"],
            "sections": [
                {"id": "exam-composition", "title": "Exam Composition Strategies", "title_zh": "考试作文策略", "type": "text",
                 "content": "**策略:**\n\n1. 审题\n2. 构思\n3. 写作\n4. 检查\n\n字数: 300-400字"},
                {"id": "advanced-techniques", "title": "Advanced Writing Techniques", "title_zh": "高级写作技巧", "type": "text",
                 "content": "**技巧:**\n\n1. 细节描写\n2. 修辞运用\n3. 素材积累\n4. 语言锤炼"},
                {"id": "common-topics", "title": "Common Topics", "title_zh": "常见话题", "type": "text",
                 "content": "**话题:**\n\n1. 成长类\n2. 社会类\n3. 价值观类"}
            ],
            "exercises": generate_exercises("comp-zh-sec4", "composition", "zh")
        },
        {
            "id": "classical-chinese-advanced-sec4",
            "gradeLevel": "sec4",
            "title": "Advanced Classical Chinese",
            "title_zh": "高级文言文",
            "description": "Master classical Chinese for O-Level",
            "description_zh": "掌握O水准文言文",
            "tag": "Reading",
            "tag_zh": "阅读",
            "objectives": ["Analyze complex classical texts", "Apply translation skills", "Appreciate literary beauty", "Answer exam questions"],
            "objectives_zh": ["分析复杂文言文", "应用翻译技巧", "欣赏文学之美", "回答考试问题"],
            "sections": [
                {"id": "advanced-vocab", "title": "Advanced Classical Vocabulary", "title_zh": "高级文言词汇", "type": "text",
                 "content": "**高级词汇:**\n\n多义词, 通假字, 词类活用"},
                {"id": "analysis-techniques", "title": "Analysis Techniques", "title_zh": "分析技巧", "type": "text",
                 "content": "**技巧:**\n\n理解大意, 分析人物, 赏析语言"},
                {"id": "exam-strategies", "title": "Exam Strategies", "title_zh": "考试策略", "type": "text",
                 "content": "**策略:**\n\n翻译题, 理解题, 赏析题"}
            ],
            "exercises": generate_exercises("adv-classical-sec4", "classical", "zh")
        },
        {
            "id": "comprehension-olevel-sec4",
            "gradeLevel": "sec4",
            "title": "O-Level Comprehension",
            "title_zh": "O水准阅读理解",
            "description": "Master comprehension for O-Level Chinese",
            "description_zh": "掌握O水准阅读理解",
            "tag": "Reading",
            "tag_zh": "阅读",
            "objectives": ["Answer comprehension questions", "Analyze texts effectively", "Apply reading strategies", "Write clear responses"],
            "objectives_zh": ["回答理解问题", "有效分析文本", "应用阅读策略", "撰写清晰回答"],
            "sections": [
                {"id": "question-analysis", "title": "Question Analysis", "title_zh": "题目分析", "type": "text",
                 "content": "**题型:**\n\n理解题, 分析题, 应用题"},
                {"id": "answer-strategies", "title": "Answer Strategies", "title_zh": "答题策略", "type": "text",
                 "content": "**策略:**\n\n审题, 定位, 组织"},
                {"id": "practice-tips", "title": "Practice Tips", "title_zh": "练习技巧", "type": "text",
                 "content": "**技巧:**\n\n多做真题, 分析错误, 总结规律"}
            ],
            "exercises": generate_exercises("comp-olevel-sec4", "comprehension", "zh")
        },
        {
            "id": "oral-olevel-sec4",
            "gradeLevel": "sec4",
            "title": "O-Level Oral Chinese",
            "title_zh": "O水准口试",
            "description": "Prepare for O-Level Chinese oral",
            "description_zh": "准备O水准华文口试",
            "tag": "Speaking",
            "tag_zh": "口语",
            "objectives": ["Excel in oral reading", "Engage in conversation", "Discuss topics effectively", "Express views confidently"],
            "objectives_zh": ["朗读出色", "参与会话", "有效讨论话题", "自信表达观点"],
            "sections": [
                {"id": "oral-reading-olevel", "title": "Oral Reading", "title_zh": "朗读", "type": "text",
                 "content": "**技巧:**\n\n准确, 流利, 有感情"},
                {"id": "conversation-olevel", "title": "Conversation", "title_zh": "会话", "type": "text",
                 "content": "**技巧:**\n\n听懂问题, 回答完整, 有条理"},
                {"id": "discussion-olevel", "title": "Discussion", "title_zh": "讨论", "type": "text",
                 "content": "**技巧:**\n\n表达观点, 举例说明, 总结陈词"}
            ],
            "exercises": generate_exercises("oral-olevel-sec4", "oral", "zh")
        },
        {
            "id": "email-letter-writing-sec4",
            "gradeLevel": "sec4",
            "title": "Email & Letter Writing",
            "title_zh": "电邮与书信",
            "description": "Master formal and informal correspondence",
            "description_zh": "掌握正式和非正式书信",
            "tag": "Writing",
            "tag_zh": "写作",
            "objectives": ["Write formal emails", "Compose formal letters", "Use appropriate language", "Follow conventions"],
            "objectives_zh": ["撰写正式电邮", "撰写正式信函", "使用适当语言", "遵循格式"],
            "sections": [
                {"id": "email-format", "title": "Email Format", "title_zh": "电邮格式", "type": "text",
                 "content": "**格式:**\n\n收件人, 主题, 正文, 签名"},
                {"id": "letter-format", "title": "Letter Format", "title_zh": "信函格式", "type": "text",
                 "content": "**格式:**\n\n称呼, 正文, 祝福语, 签名"},
                {"id": "language-register", "title": "Language Register", "title_zh": "语言层次", "type": "text",
                 "content": "**语言:**\n\n正式: 敬语, 书面语\n非正式: 口语化"}
            ],
            "exercises": generate_exercises("email-sec4", "email", "zh")
        },
        {
            "id": "vocabulary-expressions-sec4",
            "gradeLevel": "sec4",
            "title": "Advanced Vocabulary",
            "title_zh": "高级词汇",
            "description": "Expand vocabulary with advanced expressions",
            "description_zh": "用高级表达扩展词汇",
            "tag": "Vocabulary",
            "tag_zh": "词汇",
            "objectives": ["Learn advanced idioms", "Use sophisticated expressions", "Expand vocabulary range", "Apply in writing"],
            "objectives_zh": ["学习高级成语", "使用复杂表达", "扩展词汇范围", "应用于写作"],
            "sections": [
                {"id": "advanced-idioms", "title": "Advanced Idioms", "title_zh": "高级成语", "type": "text",
                 "content": "**成语:**\n\n四字成语, 典故成语, 褒贬义"},
                {"id": "expressions", "title": "Sophisticated Expressions", "title_zh": "复杂表达", "type": "text",
                 "content": "**表达:**\n\n书面语, 雅词, 修辞"},
                {"id": "application", "title": "Application in Writing", "title_zh": "写作应用", "type": "text",
                 "content": "**应用:**\n\n恰当使用, 避免堆砌, 符合语境"}
            ],
            "exercises": generate_exercises("vocab-zh-sec4", "vocabulary", "zh")
        }
    ]

def generate_exercises(prefix, topic, lang):
    """Generate 15 exercises for a chapter."""
    exercises = []
    if lang == "en":
        prompts = [
            (f"Question about {topic} concept 1", ["Option A", "Option B", "Option C", "Option D"], 1, "easy"),
            (f"Question about {topic} concept 2", ["Option A", "Option B", "Option C", "Option D"], 2, "easy"),
            (f"Question about {topic} concept 3", ["Option A", "Option B", "Option C", "Option D"], 0, "easy"),
            (f"Question about {topic} concept 4", ["Option A", "Option B", "Option C", "Option D"], 3, "easy"),
            (f"Question about {topic} concept 5", ["Option A", "Option B", "Option C", "Option D"], 1, "easy"),
            (f"Application of {topic} skill 1", ["Choice A", "Choice B", "Choice C", "Choice D"], 2, "medium"),
            (f"Application of {topic} skill 2", ["Choice A", "Choice B", "Choice C", "Choice D"], 0, "medium"),
            (f"Application of {topic} skill 3", ["Choice A", "Choice B", "Choice C", "Choice D"], 1, "medium"),
            (f"Application of {topic} skill 4", ["Choice A", "Choice B", "Choice C", "Choice D"], 3, "medium"),
            (f"Application of {topic} skill 5", ["Choice A", "Choice B", "Choice C", "Choice D"], 2, "medium"),
            (f"Advanced {topic} analysis 1", ["Answer A", "Answer B", "Answer C", "Answer D"], 1, "hard"),
            (f"Advanced {topic} analysis 2", ["Answer A", "Answer B", "Answer C", "Answer D"], 0, "hard"),
            (f"Advanced {topic} analysis 3", ["Answer A", "Answer B", "Answer C", "Answer D"], 2, "hard"),
            (f"Advanced {topic} analysis 4", ["Answer A", "Answer B", "Answer C", "Answer D"], 3, "hard"),
            (f"Advanced {topic} analysis 5", ["Answer A", "Answer B", "Answer C", "Answer D"], 1, "hard"),
        ]
    else:
        prompts = [
            (f"关于{topic}概念1的问题", ["选项A", "选项B", "选项C", "选项D"], 1, "easy"),
            (f"关于{topic}概念2的问题", ["选项A", "选项B", "选项C", "选项D"], 2, "easy"),
            (f"关于{topic}概念3的问题", ["选项A", "选项B", "选项C", "选项D"], 0, "easy"),
            (f"关于{topic}概念4的问题", ["选项A", "选项B", "选项C", "选项D"], 3, "easy"),
            (f"关于{topic}概念5的问题", ["选项A", "选项B", "选项C", "选项D"], 1, "easy"),
            (f"{topic}技能应用1", ["选项A", "选项B", "选项C", "选项D"], 2, "medium"),
            (f"{topic}技能应用2", ["选项A", "选项B", "选项C", "选项D"], 0, "medium"),
            (f"{topic}技能应用3", ["选项A", "选项B", "选项C", "选项D"], 1, "medium"),
            (f"{topic}技能应用4", ["选项A", "选项B", "选项C", "选项D"], 3, "medium"),
            (f"{topic}技能应用5", ["选项A", "选项B", "选项C", "选项D"], 2, "medium"),
            (f"高级{topic}分析1", ["答案A", "答案B", "答案C", "答案D"], 1, "hard"),
            (f"高级{topic}分析2", ["答案A", "答案B", "答案C", "答案D"], 0, "hard"),
            (f"高级{topic}分析3", ["答案A", "答案B", "答案C", "答案D"], 2, "hard"),
            (f"高级{topic}分析4", ["答案A", "答案B", "答案C", "答案D"], 3, "hard"),
            (f"高级{topic}分析5", ["答案A", "答案B", "答案C", "答案D"], 1, "hard"),
        ]
    
    for i, (prompt, choices, answer, diff) in enumerate(prompts, 1):
        exercises.append({
            "id": f"{prefix}-ex{i}",
            "type": "mcq",
            "difficulty": diff,
            "prompt": prompt,
            "prompt_zh": prompt if lang == "zh" else f"中文: {prompt}",
            "choices": choices,
            "choices_zh": choices,
            "answer": answer,
            "explanation": f"Key concept about {topic}." if lang == "en" else f"关于{topic}的要点."
        })
    
    return exercises

def main():
    """Create all chapters and integrate into content.json."""
    print("=" * 60)
    print("Creating Sec 3 and Sec 4 English and Chinese chapters")
    print("=" * 60)
    
    # Create chapters directory
    os.makedirs('chapters', exist_ok=True)
    
    # Create all chapters
    sec3_eng = create_sec3_english()
    sec4_eng = create_sec4_english()
    sec3_chi = create_sec3_chinese()
    sec4_chi = create_sec4_chinese()
    
    print(f"\nCreated:")
    print(f"  - Sec 3 English: {len(sec3_eng)} chapters")
    print(f"  - Sec 4 English: {len(sec4_eng)} chapters")
    print(f"  - Sec 3 Chinese: {len(sec3_chi)} chapters")
    print(f"  - Sec 4 Chinese: {len(sec4_chi)} chapters")
    
    # Load content.json
    print("\nLoading content.json...")
    with open('src/data/content.json', 'r', encoding='utf-8') as f:
        content = json.load(f)
    
    # Create backup
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = f'src/data/content-backup-languages-{timestamp}.json'
    with open(backup_path, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    print(f"Created backup: {backup_path}")
    
    # Find subjects
    english_subject = None
    chinese_subject = None
    for subject in content['subjects']:
        if subject['id'] == 'english':
            english_subject = subject
        elif subject['id'] == 'chinese':
            chinese_subject = subject
    
    if not english_subject or not chinese_subject:
        print("ERROR: Could not find English or Chinese subject!")
        return
    
    # Get existing chapter IDs
    existing_eng_ids = {ch['id'] for ch in english_subject['chapters']}
    existing_chi_ids = {ch['id'] for ch in chinese_subject['chapters']}
    
    # Add new chapters
    added = {"eng3": 0, "eng4": 0, "chi3": 0, "chi4": 0}
    
    for ch in sec3_eng:
        if ch['id'] not in existing_eng_ids:
            english_subject['chapters'].append(ch)
            added["eng3"] += 1
    
    for ch in sec4_eng:
        if ch['id'] not in existing_eng_ids:
            english_subject['chapters'].append(ch)
            added["eng4"] += 1
    
    for ch in sec3_chi:
        if ch['id'] not in existing_chi_ids:
            chinese_subject['chapters'].append(ch)
            added["chi3"] += 1
    
    for ch in sec4_chi:
        if ch['id'] not in existing_chi_ids:
            chinese_subject['chapters'].append(ch)
            added["chi4"] += 1
    
    # Save updated content
    print("\nSaving updated content.json...")
    with open('src/data/content.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    
    # Summary
    print("\n" + "=" * 60)
    print("INTEGRATION COMPLETE!")
    print("=" * 60)
    print(f"\nChapters added:")
    print(f"  - Sec 3 English: {added['eng3']}")
    print(f"  - Sec 4 English: {added['eng4']}")
    print(f"  - Sec 3 Chinese: {added['chi3']}")
    print(f"  - Sec 4 Chinese: {added['chi4']}")
    print(f"\nTotal English chapters: {len(english_subject['chapters'])}")
    print(f"Total Chinese chapters: {len(chinese_subject['chapters'])}")
    
    total_exercises = sum(len(ch.get('exercises', [])) for ch in sec3_eng + sec4_eng + sec3_chi + sec4_chi)
    print(f"\nTotal new exercises: {total_exercises}")

if __name__ == "__main__":
    main()

