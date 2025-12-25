import json

# Load content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# ===== CHINESE READING PASSAGES =====

# Passage 1: 中秋节的由来与庆祝方式 (5 questions)
passage1 = """中秋节是华人社会中重要的传统节日之一，通常在农历八月十五日庆祝。这一天，月亮最圆最亮，象征着团圆和美满。

关于中秋节的由来，最著名的传说是嫦娥奔月的故事。相传古时候，天上出现了十个太阳，大地干旱，民不聊生。英雄后羿射下了九个太阳，拯救了百姓。王母娘娘为了奖励他，赐给他一颗长生不老的仙药。然而，后羿的妻子嫦娥误食了仙药，结果飞升到月宫，与后羿永远分离。人们为了纪念这个凄美的故事，每年中秋都会仰望明月，思念远方的亲人。

在新加坡，中秋节的庆祝活动十分热闹。家家户户都会购买月饼，这种圆形的糕点象征着团圆。传统的月饼有莲蓉、豆沙等口味，而现代的月饼则出现了冰皮月饼、榴莲月饼等创新品种。除了吃月饼，孩子们还会提着五颜六色的灯笼游玩，这是中秋节最有特色的活动之一。

牛车水、芳林公园等地方会举办大型的中秋庆典，有舞龙舞狮表演、猜灯谜游戏，还有精彩的文艺演出。这些活动不仅增添了节日的气氛，也让年轻一代更好地了解和传承华族文化。

值得一提的是，中秋节不仅是华人的节日，在新加坡多元文化的社会中，其他族群的朋友也会参与庆祝，一起分享月饼，共度佳节。这体现了新加坡多元种族和谐共处的美好画面。"""

chi_passage1_exercises = [
    {
        'id': 'chi-pass1-q1',
        'type': 'mcq',
        'prompt': f'阅读文章：\n\n{passage1}\n\n问题1：这篇文章的主要目的是什么？',
        'prompt_zh': f'阅读文章：\n\n{passage1}\n\n问题1：这篇文章的主要目的是什么？',
        'choices': ['介绍中秋节的由来和在新加坡的庆祝方式', '批评现代月饼的口味', '解释为什么要射太阳', '宣传旅游景点'],
        'choices_zh': ['介绍中秋节的由来和在新加坡的庆祝方式', '批评现代月饼的口味', '解释为什么要射太阳', '宣传旅游景点'],
        'answer': 0,
        'explanation': '文章介绍了中秋节的传说由来、月饼文化、庆祝活动等，重点在于完整呈现中秋节在新加坡的意义和庆祝方式。',
        'explanation_zh': '文章介绍了中秋节的传说由来、月饼文化、庆祝活动等，重点在于完整呈现中秋节在新加坡的意义和庆祝方式。',
        'validator': 'smart'
    },
    {
        'id': 'chi-pass1-q2',
        'type': 'short',
        'prompt': '问题2：根据文章，中秋节在农历哪一天庆祝？',
        'prompt_zh': '问题2：根据文章，中秋节在农历哪一天庆祝？',
        'answer': '八月十五',
        'answer_zh': '八月十五',
        'hint': '看第一段。',
        'hint_zh': '看第一段。',
        'explanation': '文章第一段明确指出中秋节在农历八月十五日庆祝。',
        'explanation_zh': '文章第一段明确指出中秋节在农历八月十五日庆祝。',
        'validator': 'smart'
    },
    {
        'id': 'chi-pass1-q3',
        'type': 'mcq',
        'prompt': '问题3：嫦娥为什么飞到月宫？',
        'prompt_zh': '问题3：嫦娥为什么飞到月宫？',
        'choices': ['误食了长生不老的仙药', '后羿射下太阳后被惩罚', '想要逃离地球', '王母娘娘命令她去'],
        'choices_zh': ['误食了长生不老的仙药', '后羿射下太阳后被惩罚', '想要逃离地球', '王母娘娘命令她去'],
        'answer': 0,
        'explanation': '文章提到嫦娥误食了仙药，结果飞升到月宫。',
        'explanation_zh': '文章提到嫦娥误食了仙药，结果飞升到月宫。',
        'validator': 'smart'
    },
    {
        'id': 'chi-pass1-q4',
        'type': 'multi',
        'prompt': '问题4：文章提到了哪些庆祝中秋节的活动？（选择所有适用项）',
        'prompt_zh': '问题4：文章提到了哪些庆祝中秋节的活动？（选择所有适用项）',
        'choices': ['吃月饼', '提灯笼', '舞龙舞狮', '赛龙舟'],
        'choices_zh': ['吃月饼', '提灯笼', '舞龙舞狮', '赛龙舟'],
        'answer': [0, 1, 2],
        'explanation': '文章提到吃月饼、提灯笼、舞龙舞狮等活动。赛龙舟是端午节的活动，不是中秋节。',
        'explanation_zh': '文章提到吃月饼、提灯笼、舞龙舞狮等活动。赛龙舟是端午节的活动，不是中秋节。',
        'validator': 'smart'
    },
    {
        'id': 'chi-pass1-q5',
        'type': 'short',
        'prompt': '问题5：根据文章最后一段，中秋节在新加坡体现了什么特点？',
        'prompt_zh': '问题5：根据文章最后一段，中秋节在新加坡体现了什么特点？',
        'answer': '多元种族和谐共处',
        'answer_zh': '多元种族和谐共处',
        'hint': '看最后一句话。',
        'hint_zh': '看最后一句话。',
        'explanation': '文章最后提到其他族群也参与庆祝，体现了新加坡多元种族和谐共处的美好画面。',
        'explanation_zh': '文章最后提到其他族群也参与庆祝，体现了新加坡多元种族和谐共处的美好画面。',
        'validator': 'smart'
    }
]

# Passage 2: 新加坡的水资源管理 (5 questions)
passage2 = """新加坡是一个面积小、人口密集的岛国，自然资源匮乏，尤其是水资源。建国初期，新加坡完全依赖马来西亚供应淡水。然而，为了实现水源自给自足，新加坡政府制定了长远的水资源管理策略，发展出被称为四大水喉的多元化供水系统。

第一个水喉是本地集水区。新加坡建造了17个蓄水池来收集雨水，这些蓄水池覆盖了全岛三分之二的土地面积。最新建成的滨海堤坝不仅防洪，还将滨海湾变成了淡水蓄水池，大大增加了本地的水源供应。

第二个水喉是进口水。虽然新加坡努力减少对外依赖，但根据1961年和1962年签订的协议，马来西亚仍然向新加坡供应原水。这些协议将在2061年到期，因此新加坡必须在此之前实现完全的水源独立。

第三个水喉是新生水（NEWater）。这是新加坡最引以为豪的创新。新生水是经过先进技术处理的再生水，纯净度甚至超过自来水。目前，新生水主要供应给工厂使用，也混合到蓄水池中，补充饮用水的来源。到2060年，新生水预计将满足新加坡50%的用水需求。

第四个水喉是海水淡化。利用先进的逆渗透技术，新加坡将海水转化为饮用水。虽然淡化过程耗能较高，但它确保了新加坡即使在干旱时期也能有稳定的水源供应。

通过这四大水喉，新加坡正在逐步实现水源的可持续发展。政府也大力推广节约用水的意识，鼓励居民珍惜每一滴水。新加坡的水资源管理经验，已成为许多缺水国家学习的典范。"""

chi_passage2_exercises = [
    {
        'id': 'chi-pass2-q1',
        'type': 'mcq',
        'prompt': f'阅读文章：\n\n{passage2}\n\n问题1：新加坡为什么需要发展多元化的供水系统？',
        'prompt_zh': f'阅读文章：\n\n{passage2}\n\n问题1：新加坡为什么需要发展多元化的供水系统？',
        'choices': ['因为面积小、人口密集、自然水资源匮乏', '因为马来西亚的水质不好', '因为要建造更多游泳池', '因为新加坡想出口水资源'],
        'choices_zh': ['因为面积小、人口密集、自然水资源匮乏', '因为马来西亚的水质不好', '因为要建造更多游泳池', '因为新加坡想出口水资源'],
        'answer': 0,
        'explanation': '文章开头明确指出新加坡面积小、人口密集、自然资源（特别是水资源）匮乏，因此需要发展多元供水。',
        'explanation_zh': '文章开头明确指出新加坡面积小、人口密集、自然资源（特别是水资源）匮乏，因此需要发展多元供水。',
        'validator': 'smart'
    },
    {
        'id': 'chi-pass2-q2',
        'type': 'short',
        'prompt': '问题2：新加坡的四大水喉是什么？（列出所有四个）',
        'prompt_zh': '问题2：新加坡的四大水喉是什么？（列出所有四个）',
        'answer': '本地集水区、进口水、新生水、海水淡化',
        'answer_zh': '本地集水区、进口水、新生水、海水淡化',
        'hint': '文章分别介绍了四个水源。',
        'hint_zh': '文章分别介绍了四个水源。',
        'explanation': '文章依次介绍了本地集水区、进口水、新生水（NEWater）和海水淡化四大水喉。',
        'explanation_zh': '文章依次介绍了本地集水区、进口水、新生水（NEWater）和海水淡化四大水喉。',
        'validator': 'smart'
    },
    {
        'id': 'chi-pass2-q3',
        'type': 'mcq',
        'prompt': '问题3：根据文章，新生水（NEWater）有什么特点？',
        'prompt_zh': '问题3：根据文章，新生水（NEWater）有什么特点？',
        'choices': ['纯净度超过自来水的再生水', '直接从海里抽取的海水', '从马来西亚进口的水', '只能用来浇花的水'],
        'choices_zh': ['纯净度超过自来水的再生水', '直接从海里抽取的海水', '从马来西亚进口的水', '只能用来浇花的水'],
        'answer': 0,
        'explanation': '文章明确说明新生水是经过先进技术处理的再生水，纯净度甚至超过自来水。',
        'explanation_zh': '文章明确说明新生水是经过先进技术处理的再生水，纯净度甚至超过自来水。',
        'validator': 'smart'
    },
    {
        'id': 'chi-pass2-q4',
        'type': 'short',
        'prompt': '问题4：到2060年，新生水预计将满足新加坡多少比例的用水需求？',
        'prompt_zh': '问题4：到2060年，新生水预计将满足新加坡多少比例的用水需求？',
        'answer': '50%',
        'answer_zh': '50%',
        'hint': '在介绍新生水的段落中寻找百分比。',
        'hint_zh': '在介绍新生水的段落中寻找百分比。',
        'explanation': '文章提到到2060年，新生水预计将满足新加坡50%的用水需求。',
        'explanation_zh': '文章提到到2060年，新生水预计将满足新加坡50%的用水需求。',
        'validator': 'smart'
    },
    {
        'id': 'chi-pass2-q5',
        'type': 'mcq',
        'prompt': '问题5：文章对新加坡水资源管理的态度是什么？',
        'prompt_zh': '问题5：文章对新加坡水资源管理的态度是什么？',
        'choices': ['积极赞赏，认为值得其他国家学习', '批评政府做得不够好', '认为完全依赖马来西亚更好', '对未来感到悲观'],
        'choices_zh': ['积极赞赏，认为值得其他国家学习', '批评政府做得不够好', '认为完全依赖马来西亚更好', '对未来感到悲观'],
        'answer': 0,
        'explanation': '文章最后指出新加坡的水资源管理经验已成为许多缺水国家学习的典范，显示积极赞赏的态度。',
        'explanation_zh': '文章最后指出新加坡的水资源管理经验已成为许多缺水国家学习的典范，显示积极赞赏的态度。',
        'validator': 'smart'
    }
]

# Find Chinese Reading Comprehension chapter
chinese = next((s for s in data['subjects'] if s['id'] == 'chinese'), None)
chi_read_ch = next((c for c in chinese['chapters']
                    if c['id'] == 'chinese-reading-comprehension' and c.get('gradeLevel') == 'sec1'), None)

print(f"\nCurrent Chinese Reading Comprehension: {len(chi_read_ch['exercises'])} exercises")

# Add exercises
chi_read_ch['exercises'].extend(chi_passage1_exercises)
chi_read_ch['exercises'].extend(chi_passage2_exercises)

print(f"Added 10 passage-based exercises (2 passages × 5 questions)")
print(f"New count: {len(chi_read_ch['exercises'])} exercises")

# Save
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n✓ Chinese passage exercises integrated!")
print(f"\n" + "="*60)
print("PASSAGE-BASED EXERCISES COMPLETE")
print("="*60)
print(f"English Reading Comprehension: {len(chi_read_ch['exercises']) - 10 + 10} exercises (with 2 passages)")
print(f"Chinese Reading Comprehension: {len(chi_read_ch['exercises'])} exercises (with 2 passages)")
print("="*60)
