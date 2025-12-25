import json

# Load content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Chinese Writing exercises (avoiding quote issues with Python string literals)
exercises = []

# Exercise 16
exercises.append({
    'id': 'chi-writ-16',
    'type': 'mcq',
    'prompt': '记叙文的结构通常包括哪些部分？',
    'prompt_zh': '记叙文的结构通常包括哪些部分？',
    'choices': ['开头、起因、经过、高潮、结尾', '引言、论点、论据、结论', '开头、正文、结尾', '题目、作者、内容'],
    'choices_zh': ['开头、起因、经过、高潮、结尾', '引言、论点、论据、结论', '开头、正文、结尾', '题目、作者、内容'],
    'answer': 0,
    'explanation': '记叙文的完整结构包括：开头（引入）、起因（事件开始）、经过（事件发展）、高潮（最紧张部分）、结尾（收束）。',
    'explanation_zh': '记叙文的完整结构包括：开头（引入）、起因（事件开始）、经过（事件发展）、高潮（最紧张部分）、结尾（收束）。',
    'validator': 'smart'
})

# Exercise 17
exercises.append({
    'id': 'chi-writ-17',
    'type': 'short',
    'prompt': '在记叙文中，哪个部分通常是最紧张、最吸引读者的？',
    'prompt_zh': '在记叙文中，哪个部分通常是最紧张、最吸引读者的？',
    'answer': '高潮',
    'answer_zh': '高潮',
    'hint': '这是故事中矛盾最激烈的时刻。',
    'hint_zh': '这是故事中矛盾最激烈的时刻。',
    'explanation': '高潮是记叙文中情节发展到最紧张、矛盾冲突最激烈的部分，也是最吸引读者的地方。',
    'explanation_zh': '高潮是记叙文中情节发展到最紧张、矛盾冲突最激烈的部分，也是最吸引读者的地方。',
    'validator': 'smart'
})

# Exercise 18
exercises.append({
    'id': 'chi-writ-18',
    'type': 'mcq',
    'prompt': '下面哪个句子属于展示而不是告诉？',
    'prompt_zh': '下面哪个句子属于展示而不是告诉？',
    'choices': ['她的手不停地颤抖，额头上渗出了豆大的汗珠。', '她非常紧张。', '她感到很害怕。', '她的心情不好。'],
    'choices_zh': ['她的手不停地颤抖，额头上渗出了豆大的汗珠。', '她非常紧张。', '她感到很害怕。', '她的心情不好。'],
    'answer': 0,
    'explanation': '第一个句子通过具体的动作和细节（颤抖的手、汗珠）展示人物的紧张状态，而不是直接说紧张。',
    'explanation_zh': '第一个句子通过具体的动作和细节（颤抖的手、汗珠）展示人物的紧张状态，而不是直接说紧张。',
    'validator': 'smart'
})

# Exercise 19
exercises.append({
    'id': 'chi-writ-19',
    'type': 'multi',
    'prompt': '以下哪些是记叙文中常用的修辞手法？（选择所有适用项）',
    'prompt_zh': '以下哪些是记叙文中常用的修辞手法？（选择所有适用项）',
    'choices': ['比喻', '拟人', '排比', '方程式'],
    'choices_zh': ['比喻', '拟人', '排比', '方程式'],
    'answer': [0, 1, 2],
    'explanation': '比喻、拟人、排比都是记叙文中常用的修辞手法，可以使文章更生动形象。方程式属于数学，不是修辞手法。',
    'explanation_zh': '比喻、拟人、排比都是记叙文中常用的修辞手法，可以使文章更生动形象。方程式属于数学，不是修辞手法。',
    'validator': 'smart'
})

# Exercise 20
exercises.append({
    'id': 'chi-writ-20',
    'type': 'mcq',
    'prompt': '窗外的雨像断了线的珍珠，不停地往下掉。这句话使用了什么修辞手法？',
    'prompt_zh': '窗外的雨像断了线的珍珠，不停地往下掉。这句话使用了什么修辞手法？',
    'choices': ['比喻', '拟人', '夸张', '反问'],
    'choices_zh': ['比喻', '拟人', '夸张', '反问'],
    'answer': 0,
    'explanation': '这句话把雨比作断了线的珍珠，是典型的比喻修辞，使雨的形象更加生动。',
    'explanation_zh': '这句话把雨比作断了线的珍珠，是典型的比喻修辞，使雨的形象更加生动。',
    'validator': 'smart'
})

# Exercise 21
exercises.append({
    'id': 'chi-writ-21',
    'type': 'short',
    'prompt': '如果把春天来了改写成拟人句，应该怎么写？',
    'prompt_zh': '如果把春天来了改写成拟人句，应该怎么写？',
    'answer': '春天迈着轻盈的脚步走来了',
    'answer_zh': '春天迈着轻盈的脚步走来了',
    'hint': '给春天加上人的动作或特点。',
    'hint_zh': '给春天加上人的动作或特点。',
    'explanation': '拟人是把事物当作人来写，赋予它人的动作、语言或感情。迈着轻盈的脚步是人的动作，用在春天身上就是拟人。',
    'explanation_zh': '拟人是把事物当作人来写，赋予它人的动作、语言或感情。迈着轻盈的脚步是人的动作，用在春天身上就是拟人。',
    'validator': 'smart'
})

# Exercise 22
exercises.append({
    'id': 'chi-writ-22',
    'type': 'mcq',
    'prompt': '下面哪组关联词表示转折关系？',
    'prompt_zh': '下面哪组关联词表示转折关系？',
    'choices': ['虽然……但是……', '因为……所以……', '不但……而且……', '如果……就……'],
    'choices_zh': ['虽然……但是……', '因为……所以……', '不但……而且……', '如果……就……'],
    'answer': 0,
    'explanation': '虽然……但是……表示转折关系。因为……所以……表因果，不但……而且……表递进，如果……就……表假设。',
    'explanation_zh': '虽然……但是……表示转折关系。因为……所以……表因果，不但……而且……表递进，如果……就……表假设。',
    'validator': 'smart'
})

# Exercise 23
exercises.append({
    'id': 'chi-writ-23',
    'type': 'drag-order',
    'prompt': '将写作过程的步骤按正确顺序排列：',
    'prompt_zh': '将写作过程的步骤按正确顺序排列：',
    'items': ['审题', '列提纲', '撰写初稿', '修改润色'],
    'items_zh': ['审题', '列提纲', '撰写初稿', '修改润色'],
    'answer': ['审题', '列提纲', '撰写初稿', '修改润色'],
    'explanation': '写作的正确流程是：先审题（理解要求）→列提纲（规划结构）→撰写初稿（完成内容）→修改润色（完善文章）。',
    'explanation_zh': '写作的正确流程是：先审题（理解要求）→列提纲（规划结构）→撰写初稿（完成内容）→修改润色（完善文章）。'
})

# Exercise 24
exercises.append({
    'id': 'chi-writ-24',
    'type': 'mcq',
    'prompt': '首尾呼应的写作技巧是指什么？',
    'prompt_zh': '首尾呼应的写作技巧是指什么？',
    'choices': ['文章开头和结尾在内容或形式上相互照应', '文章开头必须和结尾一模一样', '文章必须从头到尾使用同一个句式', '文章的每一段都要重复开头的内容'],
    'choices_zh': ['文章开头和结尾在内容或形式上相互照应', '文章开头必须和结尾一模一样', '文章必须从头到尾使用同一个句式', '文章的每一段都要重复开头的内容'],
    'answer': 0,
    'explanation': '首尾呼应是指文章的开头和结尾在内容、主题或表达方式上相互照应，使文章结构完整、主题突出。',
    'explanation_zh': '首尾呼应是指文章的开头和结尾在内容、主题或表达方式上相互照应，使文章结构完整、主题突出。',
    'validator': 'smart'
})

# Exercise 25
exercises.append({
    'id': 'chi-writ-25',
    'type': 'short',
    'prompt': '在作文中，我们应该用什么方法使人物形象更加生动？',
    'prompt_zh': '在作文中，我们应该用什么方法使人物形象更加生动？',
    'answer': '描写细节和动作',
    'answer_zh': '描写细节和动作',
    'hint': '想想展示而不是告诉的原则。',
    'hint_zh': '想想展示而不是告诉的原则。',
    'explanation': '通过描写人物的外貌、动作、语言、心理等具体细节，可以让人物形象更加生动立体，而不是简单地说他很高兴。',
    'explanation_zh': '通过描写人物的外貌、动作、语言、心理等具体细节，可以让人物形象更加生动立体，而不是简单地说他很高兴。',
    'validator': 'smart'
})

# Exercise 26
exercises.append({
    'id': 'chi-writ-26',
    'type': 'mcq',
    'prompt': '下面哪个开头最能吸引读者继续阅读？',
    'prompt_zh': '下面哪个开头最能吸引读者继续阅读？',
    'choices': ['砰！一声巨响打破了午夜的宁静，我猛地从床上坐起来。', '今天天气很好，我去了公园。', '我有一个好朋友，他很善良。', '这件事发生在去年夏天。'],
    'choices_zh': ['砰！一声巨响打破了午夜的宁静，我猛地从床上坐起来。', '今天天气很好，我去了公园。', '我有一个好朋友，他很善良。', '这件事发生在去年夏天。'],
    'answer': 0,
    'explanation': '第一个开头使用拟声词和紧张的情境，制造悬念，能立刻抓住读者的注意力。其他开头较为平淡。',
    'explanation_zh': '第一个开头使用拟声词和紧张的情境，制造悬念，能立刻抓住读者的注意力。其他开头较为平淡。',
    'validator': 'smart'
})

# Exercise 27
exercises.append({
    'id': 'chi-writ-27',
    'type': 'multi',
    'prompt': '好的文章结尾应该具备哪些特点？（选择所有适用项）',
    'prompt_zh': '好的文章结尾应该具备哪些特点？（选择所有适用项）',
    'choices': ['与开头呼应', '点明主题', '给读者留下深刻印象', '突然停止没有总结'],
    'choices_zh': ['与开头呼应', '点明主题', '给读者留下深刻印象', '突然停止没有总结'],
    'answer': [0, 1, 2],
    'explanation': '好的结尾应该与开头呼应、点明文章主题、给读者留下深刻印象。突然停止会让文章显得不完整。',
    'explanation_zh': '好的结尾应该与开头呼应、点明文章主题、给读者留下深刻印象。突然停止会让文章显得不完整。',
    'validator': 'smart'
})

# Exercise 28
exercises.append({
    'id': 'chi-writ-28',
    'type': 'mcq',
    'prompt': '他跑得像风一样快。这句话使用了什么修辞手法？',
    'prompt_zh': '他跑得像风一样快。这句话使用了什么修辞手法？',
    'choices': ['比喻', '夸张', '拟人', '排比'],
    'choices_zh': ['比喻', '夸张', '拟人', '排比'],
    'answer': 0,
    'explanation': '这句话把他跑比作风，使用了比喻修辞，形象地说明他跑得很快。',
    'explanation_zh': '这句话把他跑比作风，使用了比喻修辞，形象地说明他跑得很快。',
    'validator': 'smart'
})

# Exercise 29
exercises.append({
    'id': 'chi-writ-29',
    'type': 'short',
    'prompt': '在修改作文时，我们主要检查哪些方面？',
    'prompt_zh': '在修改作文时，我们主要检查哪些方面？',
    'answer': '错别字、标点、语句通顺、结构完整',
    'answer_zh': '错别字、标点、语句通顺、结构完整',
    'hint': '想想文章的基本要素：字、词、句、段。',
    'hint_zh': '想想文章的基本要素：字、词、句、段。',
    'explanation': '修改作文时要检查：错别字、标点符号使用、语句是否通顺、段落结构是否完整、内容是否切题等。',
    'explanation_zh': '修改作文时要检查：错别字、标点符号使用、语句是否通顺、段落结构是否完整、内容是否切题等。',
    'validator': 'smart'
})

# Exercise 30
exercises.append({
    'id': 'chi-writ-30',
    'type': 'match',
    'prompt': '将写作技巧与其用途配对：',
    'prompt_zh': '将写作技巧与其用途配对：',
    'pairs': [
        {'left': '比喻', 'left_zh': '比喻', 'right': '使描写更形象生动', 'right_zh': '使描写更形象生动'},
        {'left': '拟人', 'left_zh': '拟人', 'right': '赋予事物人的特点', 'right_zh': '赋予事物人的特点'},
        {'left': '排比', 'left_zh': '排比', 'right': '增强语势和节奏', 'right_zh': '增强语势和节奏'},
        {'left': '首尾呼应', 'left_zh': '首尾呼应', 'right': '使文章结构完整', 'right_zh': '使文章结构完整'}
    ],
    'explanation': '不同的写作技巧有不同的作用：比喻使描写形象，拟人使事物生动，排比增强气势，首尾呼应使结构完整。',
    'explanation_zh': '不同的写作技巧有不同的作用：比喻使描写形象，拟人使事物生动，排比增强气势，首尾呼应使结构完整。'
})

# Find Chinese Writing chapter
chinese = next((s for s in data['subjects'] if s['id'] == 'chinese'), None)
chi_writ_ch = next((c for c in chinese['chapters']
                    if c['id'] == 'chinese-composition-writing' and c.get('gradeLevel') == 'sec1'), None)

print(f'Current count: {len(chi_writ_ch["exercises"])} exercises')

# Add exercises
chi_writ_ch['exercises'].extend(exercises)

print(f'New count: {len(chi_writ_ch["exercises"])} exercises')
print(f'✓ Added {len(exercises)} Chinese Writing exercises')

# Save
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('✓ Integration complete!')
