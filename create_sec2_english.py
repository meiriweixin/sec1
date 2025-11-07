import json
from datetime import datetime

# Secondary 2 English chapters following Singapore MOE syllabus
sec2_english_chapters = [
    {
        "id": "complex-sentences-sec2",
        "gradeLevel": "sec2",
        "title": "Complex Sentences & Clauses",
        "title_zh": "复杂句和从句",
        "description": "Master dependent and independent clauses, subordinating conjunctions, and sentence variety for more sophisticated writing",
        "description_zh": "掌握从属和独立从句、从属连词以及句式变化，提升写作水平",
        "tag": "Grammar",
        "tag_zh": "语法",
        "objectives": [
            "Identify independent and dependent clauses",
            "Use subordinating conjunctions correctly (although, because, while, unless)",
            "Combine simple sentences into complex sentences",
            "Avoid sentence fragments and run-ons with complex structures"
        ],
        "objectives_zh": [
            "识别独立从句和从属从句",
            "正确使用从属连词（although, because, while, unless）",
            "将简单句组合成复杂句",
            "避免复杂结构中的句子片段和连写句"
        ],
        "sections": [
            {
                "id": "independent-dependent-clauses",
                "title": "Independent vs. Dependent Clauses",
                "title_zh": "独立从句与从属从句",
                "type": "text",
                "content": "An independent clause can stand alone as a complete sentence. It has a subject and verb: The MRT train arrived.\n\nA dependent clause cannot stand alone. It begins with a subordinating conjunction: Although the MRT train arrived (incomplete - what happened?).\n\nWhen combined: Although the MRT train arrived, we missed it because we were late."
            },
            {
                "id": "subordinating-conjunctions",
                "title": "Subordinating Conjunctions",
                "title_zh": "从属连词",
                "type": "text",
                "content": "Common subordinating conjunctions: although, because, since, while, when, if, unless, until, after, before.\n\nThey show relationships:\n- Cause/Effect: because, since\n- Contrast: although, while\n- Condition: if, unless\n- Time: when, after, before, until\n\nExample: Unless it rains, the NEA will lift the haze advisory."
            },
            {
                "id": "sentence-variety",
                "title": "Creating Sentence Variety",
                "title_zh": "句式变化",
                "type": "text",
                "content": "Vary your sentence structure:\n1. Start with dependent clause: While studying at the National Library, I discovered a new interest.\n2. Start with independent clause: I discovered a new interest while studying at the National Library.\n3. Use multiple dependent clauses: When the exam ended, I felt relieved because I had prepared well.\n\nGood writers mix simple, compound, and complex sentences."
            }
        ],
        "exercises": []
    },
    {
        "id": "active-passive-voice-sec2",
        "gradeLevel": "sec2",
        "title": "Active & Passive Voice",
        "title_zh": "主动语态与被动语态",
        "description": "Understand when and how to use active and passive voice for different purposes in formal and informal writing",
        "description_zh": "理解在正式和非正式写作中何时以及如何使用主动和被动语态",
        "tag": "Grammar",
        "tag_zh": "语法",
        "objectives": [
            "Distinguish between active and passive voice",
            "Transform sentences from active to passive and vice versa",
            "Recognize when passive voice is appropriate (scientific writing, formal reports)",
            "Strengthen writing by using active voice when suitable"
        ],
        "objectives_zh": [
            "区分主动语态和被动语态",
            "将句子从主动语态转换为被动语态，反之亦然",
            "识别何时适合使用被动语态（科学写作、正式报告）",
            "在适当时使用主动语态加强写作"
        ],
        "sections": [
            {
                "id": "active-vs-passive",
                "title": "Active vs. Passive Voice",
                "title_zh": "主动语态与被动语态",
                "type": "text",
                "content": "Active voice: Subject performs the action.\nThe teacher marked the exam papers.\n\nPassive voice: Subject receives the action.\nThe exam papers were marked by the teacher.\n\nPassive voice structure: [Object] + be verb + past participle + (by + agent)\nThe agent (by the teacher) can be omitted if unknown or unimportant."
            },
            {
                "id": "when-to-use-passive",
                "title": "When to Use Passive Voice",
                "title_zh": "何时使用被动语态",
                "type": "text",
                "content": "Use passive voice when:\n1. The action is more important than who did it: The Singapore Flyer was built in 2008.\n2. The doer is unknown: My bicycle was stolen.\n3. In scientific/formal writing: The solution was heated to 60 degrees C.\n4. To be tactful: A mistake was made (instead of You made a mistake).\n\nAvoid passive voice when it makes writing unclear or wordy."
            },
            {
                "id": "transforming-voice",
                "title": "Transforming Between Voices",
                "title_zh": "语态转换",
                "type": "text",
                "content": "Active to Passive transformation:\n1. Active: The NEA monitors air quality.\n2. Identify object (air quality) and make it the subject\n3. Add correct be verb + past participle\n4. Passive: Air quality is monitored by the NEA.\n\nPassive to Active:\n1. Passive: The hawker center was renovated by HDB.\n2. Make the agent (HDB) the subject\n3. Active: HDB renovated the hawker center."
            }
        ],
        "exercises": []
    },
    {
        "id": "persuasive-writing-sec2",
        "gradeLevel": "sec2",
        "title": "Persuasive Writing & Argumentation",
        "title_zh": "说服性写作与论证",
        "description": "Develop skills in building logical arguments, using evidence effectively, and writing persuasive essays",
        "description_zh": "培养构建逻辑论证、有效使用证据和撰写说服性文章的技能",
        "tag": "Writing",
        "tag_zh": "写作",
        "objectives": [
            "Structure persuasive essays with clear thesis statements",
            "Use evidence, examples, and reasoning to support arguments",
            "Address counterarguments effectively",
            "Employ persuasive techniques (ethos, pathos, logos)"
        ],
        "objectives_zh": [
            "用清晰的论点陈述组织说服性文章",
            "使用证据、例子和推理支持论点",
            "有效处理反驳论点",
            "运用说服技巧（信誉、情感、逻辑）"
        ],
        "sections": [
            {
                "id": "persuasive-essay-structure",
                "title": "Persuasive Essay Structure",
                "title_zh": "说服性文章结构",
                "type": "text",
                "content": "Persuasive essay structure:\n\n1. Introduction:\n   - Hook (question, statistic, anecdote)\n   - Background context\n   - Thesis statement (your position)\n\n2. Body Paragraphs (2-3):\n   - Topic sentence (one reason)\n   - Evidence (facts, statistics, examples)\n   - Explanation of how evidence supports thesis\n   - Transition to next paragraph\n\n3. Counterargument Paragraph:\n   - Acknowledge opposing view\n   - Refute with evidence\n\n4. Conclusion:\n   - Restate thesis\n   - Summarize main points\n   - Call to action or final thought"
            },
            {
                "id": "using-evidence",
                "title": "Using Evidence Effectively",
                "title_zh": "有效使用证据",
                "type": "text",
                "content": "Strong evidence includes:\n- Statistics: According to NEA, recycling rates in Singapore increased to 61% in 2022.\n- Expert opinions: Dr. Lee from NUS states that...\n- Real examples: When Tampines implemented the zero-waste initiative...\n- Personal anecdotes (use sparingly): Last year at my school...\n\nAlways:\n1. Introduce evidence with a signal phrase\n2. Explain how it supports your point\n3. Cite sources when using external information"
            },
            {
                "id": "persuasive-techniques",
                "title": "Persuasive Techniques",
                "title_zh": "说服技巧",
                "type": "text",
                "content": "Three persuasive appeals:\n\n1. Ethos (Credibility):\n   - Show expertise or trustworthiness\n   - As a student who uses public transport daily...\n\n2. Pathos (Emotion):\n   - Appeal to feelings\n   - Imagine if every Singaporean household reduced plastic waste...\n\n3. Logos (Logic):\n   - Use facts and reasoning\n   - If we increase bus frequency by 20%, waiting times will decrease proportionally.\n\nBalance all three for effective persuasion."
            }
        ],
        "exercises": []
    },
    {
        "id": "descriptive-expository-writing-sec2",
        "gradeLevel": "sec2",
        "title": "Descriptive & Expository Writing",
        "title_zh": "描写文与说明文",
        "description": "Master techniques for vivid descriptive writing and clear expository writing to inform and explain",
        "description_zh": "掌握生动描写和清晰说明的技巧，以告知和解释",
        "tag": "Writing",
        "tag_zh": "写作",
        "objectives": [
            "Use sensory details and figurative language in descriptive writing",
            "Organize expository essays with clear topic sentences and transitions",
            "Distinguish between description and explanation",
            "Write clear process explanations and compare-contrast essays"
        ],
        "objectives_zh": [
            "在描写文中使用感官细节和比喻语言",
            "用清晰的主题句和过渡词组织说明文",
            "区分描写和解释",
            "撰写清晰的过程说明和比较对比文章"
        ],
        "sections": [
            {
                "id": "sensory-details",
                "title": "Sensory Details & Imagery",
                "title_zh": "感官细节与意象",
                "type": "text",
                "content": "Descriptive writing appeals to the five senses:\n\n- Sight: The durian's spiky green shell glistened under the market lights.\n- Sound: Hawkers shouted their prices above the sizzling of woks.\n- Smell: The aroma of freshly fried carrot cake filled the air.\n- Taste: The kaya toast was sweet and creamy with a hint of pandan.\n- Touch: The humid air clung to my skin as I walked through the MRT station.\n\nShow, don't tell: Instead of It was hot, write Sweat trickled down my back as I waited for the bus."
            },
            {
                "id": "figurative-language",
                "title": "Figurative Language",
                "title_zh": "比喻语言",
                "type": "text",
                "content": "Enhance descriptions with:\n\n1. Simile (using like or as):\n   The MRT platform was as crowded as a hawker center at lunchtime.\n\n2. Metaphor (direct comparison):\n   Orchard Road is a river of shoppers on weekends.\n\n3. Personification (giving human qualities to objects):\n   The afternoon sun beat down mercilessly on the concrete.\n\n4. Hyperbole (exaggeration):\n   I have told you a million times to bring your EZ-Link card!\n\nUse figuratively language purposefully, not excessively."
            },
            {
                "id": "expository-essay-structure",
                "title": "Expository Essay Structure",
                "title_zh": "说明文结构",
                "type": "text",
                "content": "Expository writing explains or informs:\n\nTypes:\n1. Process: How to apply for a student Concession Card\n2. Cause-Effect: Why Singapore experiences haze from neighboring countries\n3. Compare-Contrast: Public vs. Private schools in Singapore\n4. Problem-Solution: Addressing food waste in school canteens\n\nStructure:\n- Introduction with clear thesis\n- Body paragraphs with topic sentences\n- Strong transitions (Furthermore, In addition, However, Consequently)\n- Factual, objective tone\n- Conclusion summarizing main points"
            }
        ],
        "exercises": []
    },
    {
        "id": "literary-devices-sec2",
        "gradeLevel": "sec2",
        "title": "Literary Devices & Analysis",
        "title_zh": "文学手法与分析",
        "description": "Identify and analyze literary devices including symbolism, irony, foreshadowing, and theme in literature",
        "description_zh": "识别和分析文学手法，包括象征、讽刺、伏笔和主题",
        "tag": "Reading",
        "tag_zh": "阅读",
        "objectives": [
            "Identify symbolism, irony, and foreshadowing in texts",
            "Analyze how literary devices contribute to theme and meaning",
            "Distinguish between different types of irony",
            "Write analytical paragraphs using textual evidence"
        ],
        "objectives_zh": [
            "识别文本中的象征、讽刺和伏笔",
            "分析文学手法如何促进主题和意义",
            "区分不同类型的讽刺",
            "使用文本证据撰写分析段落"
        ],
        "sections": [
            {
                "id": "symbolism",
                "title": "Symbolism",
                "title_zh": "象征手法",
                "type": "text",
                "content": "A symbol is something that represents something else beyond its literal meaning.\n\nCommon symbols:\n- Weather: Storm = conflict, sunshine = hope\n- Colors: Red = danger/passion, white = purity\n- Objects: Keys = freedom, walls = barriers\n\nExample: In a story about Singapore's independence, the national flag might symbolize unity and hope for the future.\n\nTo analyze symbolism:\n1. Identify the symbol\n2. Consider its literal meaning\n3. Determine its deeper significance\n4. Connect to the story's theme"
            },
            {
                "id": "irony-types",
                "title": "Types of Irony",
                "title_zh": "讽刺的类型",
                "type": "text",
                "content": "Three types of irony:\n\n1. Verbal Irony: Saying the opposite of what you mean\n   - What lovely weather! (said during a thunderstorm)\n   - Includes sarcasm\n\n2. Situational Irony: Outcome opposite of what is expected\n   - A fire station burns down\n   - A student who never studies tops the class\n\n3. Dramatic Irony: Audience knows something characters do not\n   - In a story, readers know the helpful stranger is actually a thief, but the character trusts him\n\nIrony often reveals theme or creates humor."
            },
            {
                "id": "foreshadowing-theme",
                "title": "Foreshadowing & Theme",
                "title_zh": "伏笔与主题",
                "type": "text",
                "content": "Foreshadowing: Hints about future events\n- Dark clouds gathering = trouble ahead\n- A character's warning = danger coming\n- Repeated images = significance later\n\nExample: As he pocketed the extra change, he did not notice the security camera above. (foreshadows getting caught)\n\nTheme: Central message or lesson\n- Not the same as topic (topic = friendship, theme = True friends support each other in difficult times)\n- Often universal and stated as a complete sentence\n- Revealed through characters' actions, conflicts, and resolutions\n\nSingapore literature often explores themes of multiculturalism, family expectations, and identity."
            }
        ],
        "exercises": []
    },
    {
        "id": "critical-reading-sec2",
        "gradeLevel": "sec2",
        "title": "Critical Reading & Inference",
        "title_zh": "批判性阅读与推理",
        "description": "Develop advanced comprehension skills including making inferences, drawing conclusions, and evaluating author's purpose and perspective",
        "description_zh": "培养高级理解技能，包括推理、得出结论以及评估作者的目的和观点",
        "tag": "Reading",
        "tag_zh": "阅读",
        "objectives": [
            "Make logical inferences based on textual evidence",
            "Evaluate author's perspective and bias",
            "Distinguish between fact and opinion",
            "Analyze author's tone and purpose (inform, persuade, entertain)"
        ],
        "objectives_zh": [
            "基于文本证据进行逻辑推理",
            "评估作者的观点和偏见",
            "区分事实和观点",
            "分析作者的语气和目的（告知、说服、娱乐）"
        ],
        "sections": [
            {
                "id": "making-inferences",
                "title": "Making Inferences",
                "title_zh": "推理",
                "type": "text",
                "content": "An inference is a logical conclusion based on evidence and reasoning.\n\nText: Sarah slammed her locker shut and stomped down the hallway, ignoring her friends' greetings.\n\nInference: Sarah is angry or upset about something.\n\nTo make good inferences:\n1. Look for clues (actions, dialogue, descriptions)\n2. Use prior knowledge\n3. Ask What does this suggest?\n4. Support inference with evidence from text\n\nAvoid: Wild guesses without textual support"
            },
            {
                "id": "fact-vs-opinion",
                "title": "Fact vs. Opinion",
                "title_zh": "事实与观点",
                "type": "text",
                "content": "Fact: Can be verified or proven\n- Singapore gained independence in 1965. (checkable)\n- The Merlion is located at Marina Bay. (verifiable)\n\nOpinion: Personal belief or judgment\n- Singapore is the best country in Southeast Asia. (subjective)\n- Chicken rice is delicious. (personal taste)\n\nWatch for opinion markers:\n- I think, I believe, in my opinion\n- Should, ought to, must\n- Adjectives (best, worst, beautiful, terrible)\n\nCritical readers distinguish facts from opinions to evaluate arguments."
            },
            {
                "id": "authors-purpose-tone",
                "title": "Author's Purpose & Tone",
                "title_zh": "作者的目的与语气",
                "type": "text",
                "content": "Author's Purpose:\n1. Inform: Provide facts (textbooks, news articles)\n2. Persuade: Convince readers (editorials, advertisements)\n3. Entertain: Amuse or engage (stories, poems)\n\nAuthor's Tone (attitude toward subject):\n- Formal vs. Informal\n- Serious, humorous, sarcastic, sympathetic, critical\n\nClues to tone:\n- Word choice (diction)\n- Sentence structure\n- Details included/excluded\n\nExample: A news article about youth volunteerism using words like inspiring and commendable has an approving tone.\n\nBias: Unfair preference for or against something. Look for one-sided arguments and loaded language."
            }
        ],
        "exercises": []
    }
]

# Save to JSON file
with open('chapters/sec2-english-chapters.json', 'w', encoding='utf-8') as f:
    json.dump(sec2_english_chapters, f, ensure_ascii=False, indent=2)

print(f"Created {len(sec2_english_chapters)} Secondary 2 English chapters")
print("Chapters:", [ch['title'] for ch in sec2_english_chapters])
