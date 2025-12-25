"""
Add more Reading Comprehension and Writing exercises for English and Chinese Sec 1
"""
import json
from datetime import datetime

# Load content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create backup
backup_name = f"src/data/content-backup-language-exercises-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
with open(backup_name, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"✅ Backup created: {backup_name}")

# ============================================================
# ENGLISH - Additional Reading Comprehension Exercises (15)
# ============================================================
english_reading_exercises = [
    # Passage-based comprehension (Singapore context)
    {
        "id": "eng-read-16",
        "type": "mcq",
        "prompt": "Read the passage:\n\n\"The Singapore Botanic Gardens, established in 1859, is the only tropical garden to be honoured as a UNESCO World Heritage Site. Spanning 82 hectares, it houses more than 10,000 species of plants. The Gardens played a crucial role in introducing rubber cultivation to Southeast Asia, which transformed the region's economy.\"\n\nWhat is the main purpose of this passage?",
        "prompt_zh": "阅读文章后回答问题。这篇文章的主要目的是什么？",
        "choices": [
            "To describe the history and significance of the Singapore Botanic Gardens",
            "To explain how rubber is cultivated",
            "To list all UNESCO World Heritage Sites",
            "To compare tropical and temperate gardens"
        ],
        "answer": 0,
        "explanation": "The passage focuses on the history (established 1859), significance (UNESCO World Heritage Site), and impact (rubber cultivation) of the Singapore Botanic Gardens.",
        "validator": "smart"
    },
    {
        "id": "eng-read-17",
        "type": "short",
        "prompt": "Based on the passage about Singapore Botanic Gardens, what economic impact did the Gardens have on Southeast Asia?",
        "prompt_zh": "根据新加坡植物园的文章，植物园对东南亚有什么经济影响？",
        "answer": "introduced rubber cultivation",
        "answer_zh": "引进橡胶种植",
        "hint": "Look for information about how the Gardens 'transformed' the region.",
        "explanation": "The passage states that the Gardens 'played a crucial role in introducing rubber cultivation to Southeast Asia, which transformed the region's economy.'",
        "validator": "smart"
    },
    {
        "id": "eng-read-18",
        "type": "mcq",
        "prompt": "Read the passage:\n\n\"Hawker centres are the heart of Singapore's food culture. These open-air food courts offer a dizzying array of local dishes at affordable prices. From chicken rice to laksa, each stall specializes in perfecting a single dish, often passed down through generations. In 2020, Singapore's hawker culture was inscribed on UNESCO's Representative List of the Intangible Cultural Heritage of Humanity.\"\n\nWhat can you infer about hawker stall owners from this passage?",
        "prompt_zh": "从这篇文章中，你能推断出小贩摊主什么信息？",
        "choices": [
            "They typically focus on mastering one dish rather than offering many",
            "They all serve chicken rice and laksa",
            "They only cook for tourists",
            "They have formal culinary training"
        ],
        "answer": 0,
        "explanation": "The passage states 'each stall specializes in perfecting a single dish', implying stall owners focus on mastering one dish.",
        "validator": "smart"
    },
    {
        "id": "eng-read-19",
        "type": "multi",
        "prompt": "Based on the hawker centre passage, which statements are TRUE? (Select all that apply)",
        "prompt_zh": "根据小贩中心文章，哪些陈述是正确的？（选择所有适用的）",
        "choices": [
            "Hawker centres are an important part of Singapore's culture",
            "Food at hawker centres is generally affordable",
            "UNESCO recognized Singapore's hawker culture",
            "Hawker centres are indoor facilities"
        ],
        "answer": [0, 1, 2],
        "explanation": "The passage confirms: hawker centres are 'the heart of Singapore's food culture' (important), offer food 'at affordable prices', and were 'inscribed on UNESCO's Representative List'. However, they are described as 'open-air', not indoor.",
        "validator": "smart"
    },
    {
        "id": "eng-read-20",
        "type": "mcq",
        "prompt": "Read the passage:\n\n\"Mr. Tan adjusted his spectacles and peered at the old photograph. The kampong where he grew up was unrecognizable now—gleaming HDB flats stood where attap houses once clustered. He remembered catching spiders in the lalang grass, swimming in the monsoon drains after heavy rains. His grandchildren would never know that world, he thought with a bittersweet smile.\"\n\nWhat is the author's tone in this passage?",
        "prompt_zh": "这篇文章作者的语气是什么？",
        "choices": [
            "Nostalgic and reflective",
            "Angry and resentful",
            "Excited and optimistic",
            "Confused and uncertain"
        ],
        "answer": 0,
        "explanation": "Words like 'bittersweet smile', memories of childhood activities, and the contrast between past and present suggest a nostalgic, reflective tone.",
        "validator": "smart"
    },
    {
        "id": "eng-read-21",
        "type": "short",
        "prompt": "In the passage about Mr. Tan, what word shows he has mixed feelings about the changes?",
        "prompt_zh": "在关于陈先生的文章中，哪个词表明他对变化有复杂的感受？",
        "answer": "bittersweet",
        "answer_zh": "苦乐参半",
        "hint": "Look for a word that combines both positive and negative emotions.",
        "explanation": "'Bittersweet' means experiencing both happiness and sadness simultaneously, perfectly capturing Mr. Tan's mixed feelings.",
        "validator": "smart"
    },
    {
        "id": "eng-read-22",
        "type": "mcq",
        "prompt": "Read the passage:\n\n\"The Merlion, Singapore's iconic half-lion, half-fish statue, symbolizes the nation's origins. The lion head represents Singapura—the original Sanskrit name meaning 'Lion City'—while the fish body acknowledges Singapore's history as a fishing village called Temasek. Standing 8.6 meters tall at Marina Bay, this mythical creature has become synonymous with Singapore itself.\"\n\nWhat is the relationship between the Merlion's design and Singapore's history?",
        "prompt_zh": "鱼尾狮的设计与新加坡的历史有什么关系？",
        "choices": [
            "Each part of the Merlion represents a different period in Singapore's past",
            "The Merlion was designed to attract tourists",
            "The Merlion is based on an ancient local legend",
            "The Merlion was created to replace an older monument"
        ],
        "answer": 0,
        "explanation": "The lion head represents the 'Lion City' (Singapura) name, while the fish body represents the fishing village (Temasek) history—two different historical periods.",
        "validator": "smart"
    },
    {
        "id": "eng-read-23",
        "type": "drag-order",
        "prompt": "Arrange these events from the Merlion passage in chronological order:",
        "prompt_zh": "按时间顺序排列鱼尾狮文章中的这些事件：",
        "items": [
            "Singapore was a fishing village called Temasek",
            "The place was named Singapura (Lion City)",
            "The Merlion statue was built at Marina Bay"
        ],
        "answer": [
            "Singapore was a fishing village called Temasek",
            "The place was named Singapura (Lion City)",
            "The Merlion statue was built at Marina Bay"
        ],
        "explanation": "Chronologically: Temasek (ancient fishing village) → Singapura (later name) → Merlion (modern statue)."
    },
    {
        "id": "eng-read-24",
        "type": "mcq",
        "prompt": "Read the passage:\n\n\"'Singlish,' Singapore's unique English-based creole, blends English with Malay, Hokkien, Teochew, Cantonese, and Tamil. While the government promotes Standard English through the 'Speak Good English Movement,' many Singaporeans view Singlish as a beloved marker of local identity. Phrases like 'can lah' and 'alamak' pepper everyday conversations, creating a linguistic tapestry that reflects the nation's multicultural heritage.\"\n\nWhat is the author's perspective on Singlish?",
        "prompt_zh": "作者对新加坡式英语的看法是什么？",
        "choices": [
            "Balanced—acknowledging both official concerns and cultural value",
            "Strongly negative—Singlish should be eliminated",
            "Strongly positive—Singlish is better than Standard English",
            "Indifferent—the author has no opinion"
        ],
        "answer": 0,
        "explanation": "The author presents both the government's promotion of Standard English AND Singaporeans' view of Singlish as 'beloved', showing a balanced perspective.",
        "validator": "smart"
    },
    {
        "id": "eng-read-25",
        "type": "short",
        "prompt": "According to the Singlish passage, what metaphor does the author use to describe the mix of languages?",
        "prompt_zh": "根据新加坡式英语的文章，作者用什么比喻来描述语言的混合？",
        "answer": "linguistic tapestry",
        "answer_zh": "语言织锦",
        "hint": "Look for a phrase that compares the language mix to something woven together.",
        "explanation": "The author uses 'linguistic tapestry' to describe how different languages are woven together in Singlish.",
        "validator": "smart"
    },
    {
        "id": "eng-read-26",
        "type": "mcq",
        "prompt": "Read the passage:\n\n\"Every August 9th, Singapore celebrates National Day with a grand parade, spectacular fireworks, and heartfelt renditions of patriotic songs. The Red Lions parachute team descends from the sky, fighter jets roar overhead in formation, and citizens wave the national flag. Yet beyond the pageantry, the day serves as a reminder of the nation's journey from a small colonial outpost to a thriving global city.\"\n\nWhat is the author suggesting about National Day?",
        "prompt_zh": "作者对国庆节有什么暗示？",
        "choices": [
            "It has both celebratory and reflective purposes",
            "It is only about entertainment and shows",
            "It celebrates Singapore's colonial past",
            "It is becoming less popular"
        ],
        "answer": 0,
        "explanation": "The phrase 'Yet beyond the pageantry' signals that National Day is more than just celebration—it's also 'a reminder of the nation's journey.'",
        "validator": "smart"
    },
    {
        "id": "eng-read-27",
        "type": "multi",
        "prompt": "From the National Day passage, which activities are mentioned? (Select all that apply)",
        "prompt_zh": "从国庆节文章中，提到了哪些活动？（选择所有适用的）",
        "choices": [
            "Parachute team performance",
            "Fireworks display",
            "Fighter jet flyover",
            "Marathon race"
        ],
        "answer": [0, 1, 2],
        "explanation": "The passage mentions: Red Lions parachute team, fireworks, and fighter jets. A marathon is not mentioned.",
        "validator": "smart"
    },
    {
        "id": "eng-read-28",
        "type": "mcq",
        "prompt": "Read the passage:\n\n\"Climate change poses an existential threat to Singapore. As a low-lying island nation, rising sea levels could submerge significant portions of the coastline. The government has pledged $100 billion over the next century for coastal protection measures, including sea walls and land reclamation. However, experts warn that adaptation alone is insufficient—global cooperation to reduce emissions remains essential.\"\n\nWhat is the main argument of this passage?",
        "prompt_zh": "这篇文章的主要论点是什么？",
        "choices": [
            "Singapore must both adapt locally and support global climate action",
            "Singapore's coastal protection is already sufficient",
            "Climate change only affects Singapore's coastline",
            "The government should spend more than $100 billion"
        ],
        "answer": 0,
        "explanation": "The passage presents Singapore's adaptation efforts BUT concludes that 'adaptation alone is insufficient—global cooperation to reduce emissions remains essential.'",
        "validator": "smart"
    },
    {
        "id": "eng-read-29",
        "type": "short",
        "prompt": "In the climate change passage, what phrase indicates that climate change is a severe threat?",
        "prompt_zh": "在气候变化文章中，哪个短语表明气候变化是严重威胁？",
        "answer": "existential threat",
        "answer_zh": "生存威胁",
        "hint": "Look for a phrase at the beginning that describes the level of danger.",
        "explanation": "'Existential threat' means a threat to existence itself—the most severe type of danger possible.",
        "validator": "smart"
    },
    {
        "id": "eng-read-30",
        "type": "match",
        "prompt": "Match each reading skill with its definition:",
        "prompt_zh": "将每个阅读技能与其定义匹配：",
        "pairs": [
            {"left": "Inference", "left_zh": "推断", "right": "Drawing conclusions from clues", "right_zh": "从线索中得出结论"},
            {"left": "Main Idea", "left_zh": "主旨", "right": "The central message of a text", "right_zh": "文本的中心信息"},
            {"left": "Tone", "left_zh": "语气", "right": "The author's attitude", "right_zh": "作者的态度"},
            {"left": "Evidence", "left_zh": "证据", "right": "Facts that support a claim", "right_zh": "支持观点的事实"}
        ],
        "explanation": "These are fundamental reading comprehension skills: inference (reading between the lines), main idea (central point), tone (author's attitude), and evidence (supporting facts)."
    }
]

# ============================================================
# ENGLISH - Additional Writing Exercises (15)
# ============================================================
english_writing_exercises = [
    {
        "id": "eng-write-16",
        "type": "mcq",
        "prompt": "You are writing a narrative essay about your first day at secondary school. Which opening would be MOST engaging?",
        "prompt_zh": "你正在写一篇关于中学第一天的记叙文。哪个开头最吸引人？",
        "choices": [
            "My heart pounded like a drum as I stepped through the towering gates of Raffles Secondary.",
            "My first day of secondary school was on January 2nd.",
            "I am going to tell you about my first day at secondary school.",
            "Secondary school is very different from primary school."
        ],
        "answer": 0,
        "explanation": "The first option uses vivid imagery ('heart pounded like a drum'), sensory details, and creates immediate tension—all hallmarks of an engaging narrative opening.",
        "validator": "smart"
    },
    {
        "id": "eng-write-17",
        "type": "short",
        "prompt": "Rewrite this 'telling' sentence as a 'showing' sentence: 'Sarah was very nervous.'",
        "prompt_zh": "将这个'告诉'句子改写为'展示'句子：'Sarah非常紧张。'",
        "answer": "Sarah's hands trembled",
        "answer_zh": "Sarah的手在颤抖",
        "hint": "Describe physical signs of nervousness instead of stating the emotion.",
        "explanation": "Showing uses physical details (trembling hands, sweating, pacing) instead of directly stating emotions. Examples: 'Sarah's hands trembled as she gripped her pencil' or 'Sarah wiped her sweaty palms on her skirt.'",
        "validator": "smart"
    },
    {
        "id": "eng-write-18",
        "type": "mcq",
        "prompt": "Which transition word best shows CONTRAST between two ideas?",
        "prompt_zh": "哪个过渡词最能表示两个想法之间的对比？",
        "choices": [
            "However",
            "Furthermore",
            "Similarly",
            "Therefore"
        ],
        "answer": 0,
        "explanation": "'However' signals contrast. 'Furthermore' adds information, 'Similarly' shows comparison, and 'Therefore' shows cause-effect.",
        "validator": "smart"
    },
    {
        "id": "eng-write-19",
        "type": "drag-order",
        "prompt": "Arrange these parts of a narrative essay in the correct order:",
        "prompt_zh": "按正确顺序排列记叙文的这些部分：",
        "items": [
            "Exposition (setting and characters)",
            "Rising action (conflict develops)",
            "Climax (turning point)",
            "Falling action (events after climax)",
            "Resolution (conclusion)"
        ],
        "answer": [
            "Exposition (setting and characters)",
            "Rising action (conflict develops)",
            "Climax (turning point)",
            "Falling action (events after climax)",
            "Resolution (conclusion)"
        ],
        "explanation": "This is the classic narrative arc structure taught in Secondary English."
    },
    {
        "id": "eng-write-20",
        "type": "mcq",
        "prompt": "You need to write a persuasive essay about reducing plastic use. Which thesis statement is STRONGEST?",
        "prompt_zh": "你需要写一篇关于减少塑料使用的议论文。哪个论点最有力？",
        "choices": [
            "Singapore should ban single-use plastics because they harm marine life, clog drains causing floods, and can be replaced by sustainable alternatives.",
            "Plastic is bad for the environment.",
            "Many countries are banning plastic bags.",
            "I think we should use less plastic."
        ],
        "answer": 0,
        "explanation": "A strong thesis is specific, arguable, and previews the main supporting points. The first option clearly states the position (ban single-use plastics) and gives three reasons.",
        "validator": "smart"
    },
    {
        "id": "eng-write-21",
        "type": "short",
        "prompt": "Write a topic sentence for a paragraph about the benefits of reading books.",
        "prompt_zh": "为一段关于阅读书籍好处的文字写一个主题句。",
        "answer": "reading offers many benefits",
        "answer_zh": "阅读有很多好处",
        "hint": "A topic sentence should state the main idea of the paragraph.",
        "explanation": "Good topic sentences might include: 'Reading regularly offers numerous benefits for students' or 'Books are powerful tools for expanding knowledge and imagination.'",
        "validator": "smart"
    },
    {
        "id": "eng-write-22",
        "type": "mcq",
        "prompt": "Which sentence uses the MOST precise vocabulary?",
        "prompt_zh": "哪个句子使用了最精确的词汇？",
        "choices": [
            "The exhausted athlete staggered across the finish line.",
            "The tired athlete walked across the finish line.",
            "The athlete went across the finish line.",
            "The athlete finished the race."
        ],
        "answer": 0,
        "explanation": "'Exhausted' is more precise than 'tired', and 'staggered' paints a clearer picture than 'walked' or 'went'. Precise vocabulary creates vivid imagery.",
        "validator": "smart"
    },
    {
        "id": "eng-write-23",
        "type": "multi",
        "prompt": "Which of these are effective ways to conclude a narrative essay? (Select all that apply)",
        "prompt_zh": "以下哪些是结束记叙文的有效方式？（选择所有适用的）",
        "choices": [
            "Reflect on the lesson learned from the experience",
            "Circle back to an image or idea from the opening",
            "Write 'The End' at the bottom",
            "End with dialogue that captures the moment"
        ],
        "answer": [0, 1, 3],
        "explanation": "Effective conclusions reflect on meaning, create circularity with the opening, or use powerful final moments. Simply writing 'The End' is not a sophisticated technique.",
        "validator": "smart"
    },
    {
        "id": "eng-write-24",
        "type": "mcq",
        "prompt": "You are describing a thunderstorm for a descriptive essay. Which uses the BEST sensory details?",
        "prompt_zh": "你正在为一篇描写文描述雷暴。哪个使用了最好的感官细节？",
        "choices": [
            "Lightning crackled across the charcoal sky, followed by thunder that rattled the windows and shook my chest.",
            "There was lightning and thunder during the storm.",
            "The storm was very loud and scary.",
            "It rained heavily that day."
        ],
        "answer": 0,
        "explanation": "The first option engages multiple senses: sight (lightning, charcoal sky), sound (crackled, rattled), and touch (shook my chest). This creates immersive writing.",
        "validator": "smart"
    },
    {
        "id": "eng-write-25",
        "type": "short",
        "prompt": "What is the purpose of a 'hook' in essay writing?",
        "prompt_zh": "文章写作中'引子'的目的是什么？",
        "answer": "capture reader attention",
        "answer_zh": "吸引读者注意力",
        "hint": "Think about what a fishing hook does—it catches something!",
        "explanation": "A hook captures the reader's attention and makes them want to continue reading. It can be a question, quote, surprising fact, or vivid scene.",
        "validator": "smart"
    },
    {
        "id": "eng-write-26",
        "type": "mcq",
        "prompt": "Which revision improves this wordy sentence? Original: 'In my personal opinion, I think that the food at the hawker centre was very delicious and tasty.'",
        "prompt_zh": "哪个修改改进了这个冗长的句子？原句：'在我个人看来，我认为小贩中心的食物非常美味可口。'",
        "choices": [
            "The hawker centre's food was delicious.",
            "I personally think the food was very, very good.",
            "In my opinion, I believe the food tasted very delicious.",
            "The food was delicious and tasty in my opinion."
        ],
        "answer": 0,
        "explanation": "The revision removes redundancy: 'personal opinion' and 'I think' mean the same thing, 'delicious' and 'tasty' are redundant. Concise writing is stronger.",
        "validator": "smart"
    },
    {
        "id": "eng-write-27",
        "type": "match",
        "prompt": "Match each type of figurative language with its example:",
        "prompt_zh": "将每种修辞手法与其例子匹配：",
        "pairs": [
            {"left": "Simile", "left_zh": "明喻", "right": "Her smile was like sunshine", "right_zh": "她的微笑像阳光"},
            {"left": "Metaphor", "left_zh": "暗喻", "right": "Time is money", "right_zh": "时间就是金钱"},
            {"left": "Personification", "left_zh": "拟人", "right": "The wind whispered secrets", "right_zh": "风在低语秘密"},
            {"left": "Onomatopoeia", "left_zh": "拟声词", "right": "The bees buzzed loudly", "right_zh": "蜜蜂嗡嗡响"}
        ],
        "explanation": "Simile uses 'like' or 'as', metaphor directly equates, personification gives human qualities to non-human things, onomatopoeia mimics sounds."
    },
    {
        "id": "eng-write-28",
        "type": "mcq",
        "prompt": "You are writing a formal letter to your principal requesting a new CCA. Which greeting is appropriate?",
        "prompt_zh": "你正在给校长写一封正式信函请求新的课外活动。哪个问候语是恰当的？",
        "choices": [
            "Dear Mr/Mrs [Principal's name],",
            "Hey Principal!",
            "Hi there,",
            "To whoever reads this,"
        ],
        "answer": 0,
        "explanation": "Formal letters require appropriate salutations. 'Dear Mr/Mrs [Name]' is the standard formal greeting for letters to authority figures.",
        "validator": "smart"
    },
    {
        "id": "eng-write-29",
        "type": "drag-order",
        "prompt": "Arrange these steps for the writing process in the correct order:",
        "prompt_zh": "按正确顺序排列写作过程的这些步骤：",
        "items": [
            "Brainstorm and plan ideas",
            "Write the first draft",
            "Revise for content and organization",
            "Edit for grammar and spelling",
            "Publish or submit final version"
        ],
        "answer": [
            "Brainstorm and plan ideas",
            "Write the first draft",
            "Revise for content and organization",
            "Edit for grammar and spelling",
            "Publish or submit final version"
        ],
        "explanation": "The writing process: prewriting (brainstorm) → drafting → revising (big picture) → editing (details) → publishing."
    },
    {
        "id": "eng-write-30",
        "type": "short",
        "prompt": "What is the difference between 'revising' and 'editing' in writing?",
        "prompt_zh": "写作中'修改'和'编辑'有什么区别？",
        "answer": "revising focuses on content, editing on grammar",
        "answer_zh": "修改关注内容，编辑关注语法",
        "hint": "Think about big-picture changes vs. small details.",
        "explanation": "Revising focuses on content, organization, and ideas (big picture). Editing focuses on grammar, spelling, and punctuation (details).",
        "validator": "smart"
    }
]

# ============================================================
# CHINESE - Additional Reading Comprehension Exercises (15)
# ============================================================
chinese_reading_exercises = [
    {
        "id": "chi-read-16",
        "type": "mcq",
        "prompt": "阅读短文：\n\n"新加坡虽然面积不大，却是一个多元文化的国家。华人、马来人、印度人和其他族群和谐共处，各自保留着独特的传统习俗。每年的农历新年、开斋节、屠妖节等节日，都让这个小岛充满了欢乐的气氛。"\n\n这篇短文的主旨是什么？",
        "prompt_zh": "阅读短文后回答问题。这篇短文的主旨是什么？",
        "choices": [
            "新加坡是一个多元文化和谐共处的国家",
            "新加坡的面积很小",
            "新加坡只有华人和马来人",
            "新加坡的节日太多了"
        ],
        "answer": 0,
        "explanation": "短文强调新加坡虽小但多元文化和谐共处，各族群保留传统，这是主旨。",
        "validator": "smart"
    },
    {
        "id": "chi-read-17",
        "type": "short",
        "prompt": "根据上面的短文，新加坡有哪些主要族群？请列出至少两个。",
        "prompt_zh": "根据短文，新加坡有哪些主要族群？",
        "answer": "华人、马来人、印度人",
        "answer_zh": "华人、马来人、印度人",
        "hint": "短文中提到了三个主要族群。",
        "explanation": "短文明确提到：华人、马来人、印度人和其他族群。",
        "validator": "smart"
    },
    {
        "id": "chi-read-18",
        "type": "mcq",
        "prompt": "阅读短文：\n\n"阿明从小就对烹饪充满热情。每天放学后，他都会帮妈妈准备晚餐。从洗菜、切菜到调味，他样样在行。妈妈常说：'阿明的厨艺比我还好呢！'虽然同学们都在玩电子游戏，但阿明更喜欢尝试新的食谱。"\n\n从短文中，我们可以推断阿明是一个怎样的人？",
        "prompt_zh": "从短文中，我们可以推断阿明是一个怎样的人？",
        "choices": [
            "有耐心、专注于自己兴趣的人",
            "只会玩电子游戏的人",
            "不愿意帮助家人的人",
            "对学习没有兴趣的人"
        ],
        "answer": 0,
        "explanation": "阿明每天坚持帮忙做饭，不随大流玩游戏，专注于烹饪兴趣，说明他有耐心且专注。",
        "validator": "smart"
    },
    {
        "id": "chi-read-19",
        "type": "short",
        "prompt": "短文中，妈妈对阿明的厨艺有什么评价？",
        "prompt_zh": "短文中，妈妈对阿明的厨艺有什么评价？",
        "answer": "比妈妈还好",
        "answer_zh": "比妈妈还好",
        "hint": "找出妈妈说的话。",
        "explanation": "妈妈说：'阿明的厨艺比我还好呢！'这是对阿明的高度评价。",
        "validator": "smart"
    },
    {
        "id": "chi-read-20",
        "type": "mcq",
        "prompt": "阅读短文：\n\n"环保是每个人的责任。在新加坡，我们可以通过简单的行动来保护环境：自带购物袋、减少使用一次性餐具、节约用水用电。虽然这些都是小事，但如果每个人都这样做，就能产生巨大的影响。"\n\n作者写这篇短文的目的是什么？",
        "prompt_zh": "作者写这篇短文的目的是什么？",
        "choices": [
            "呼吁大家采取行动保护环境",
            "批评人们不环保的行为",
            "介绍新加坡的环保法律",
            "讨论环保的缺点"
        ],
        "answer": 0,
        "explanation": "作者通过列举具体行动并强调'每个人都这样做'能产生巨大影响，目的是呼吁行动。",
        "validator": "smart"
    },
    {
        "id": "chi-read-21",
        "type": "multi",
        "prompt": "根据环保短文，以下哪些是文中提到的环保行动？（选择所有适用的）",
        "prompt_zh": "根据环保短文，以下哪些是文中提到的环保行动？",
        "choices": [
            "自带购物袋",
            "减少使用一次性餐具",
            "节约用水用电",
            "购买电动汽车"
        ],
        "answer": [0, 1, 2],
        "explanation": "短文提到：自带购物袋、减少使用一次性餐具、节约用水用电。购买电动汽车未被提及。",
        "validator": "smart"
    },
    {
        "id": "chi-read-22",
        "type": "mcq",
        "prompt": "阅读短文：\n\n"老王的杂货店已经开了五十年了。虽然附近开了好几家超市，生意大不如前，但老王仍然坚持每天早起开店。他说：'这不只是一门生意，更是邻居们的回忆。小时候在这里买糖果的孩子，现在都带着自己的孩子来了。'"\n\n'这不只是一门生意'这句话说明了什么？",
        "prompt_zh": "'这不只是一门生意'这句话说明了什么？",
        "choices": [
            "杂货店对老王和邻居们有特殊的情感价值",
            "老王的生意非常赚钱",
            "老王想要关闭杂货店",
            "超市比杂货店更好"
        ],
        "answer": 0,
        "explanation": "老王强调杂货店是'邻居们的回忆'，说明它的价值超越了商业利益，具有情感意义。",
        "validator": "smart"
    },
    {
        "id": "chi-read-23",
        "type": "short",
        "prompt": "老王的杂货店经营了多少年？",
        "prompt_zh": "老王的杂货店经营了多少年？",
        "answer": "五十年",
        "answer_zh": "五十年",
        "hint": "这是一个数字答案。",
        "explanation": "短文开头说'老王的杂货店已经开了五十年了'。",
        "validator": "smart"
    },
    {
        "id": "chi-read-24",
        "type": "mcq",
        "prompt": "阅读诗歌：\n\n"静夜思 - 李白\n床前明月光，疑是地上霜。\n举头望明月，低头思故乡。"\n\n这首诗表达了诗人什么样的情感？",
        "prompt_zh": "这首诗表达了诗人什么样的情感？",
        "choices": [
            "思念家乡的情感",
            "喜欢月亮的情感",
            "害怕黑夜的情感",
            "讨厌旅行的情感"
        ],
        "answer": 0,
        "explanation": "最后一句'低头思故乡'直接表达了思乡之情。整首诗通过月光引发对家乡的思念。",
        "validator": "smart"
    },
    {
        "id": "chi-read-25",
        "type": "short",
        "prompt": "在《静夜思》中，诗人把月光比作什么？",
        "prompt_zh": "在《静夜思》中，诗人把月光比作什么？",
        "answer": "霜",
        "answer_zh": "霜",
        "hint": "看第二句'疑是地上____'。",
        "explanation": "'疑是地上霜'——诗人把明亮的月光比作地上的白霜。",
        "validator": "smart"
    },
    {
        "id": "chi-read-26",
        "type": "mcq",
        "prompt": "阅读短文：\n\n"智能手机虽然给我们的生活带来了便利，但也带来了一些问题。许多青少年沉迷于手机游戏，影响了学习和睡眠。有些人在聚会时只顾着看手机，忽略了身边的朋友。因此，我们应该学会合理使用手机，而不是被手机控制。"\n\n作者对智能手机的态度是什么？",
        "prompt_zh": "作者对智能手机的态度是什么？",
        "choices": [
            "既肯定其便利性，也指出其问题",
            "完全支持使用智能手机",
            "完全反对使用智能手机",
            "认为智能手机与自己无关"
        ],
        "answer": 0,
        "explanation": "作者先说'给我们的生活带来了便利'，又说'也带来了一些问题'，态度是客观平衡的。",
        "validator": "smart"
    },
    {
        "id": "chi-read-27",
        "type": "drag-order",
        "prompt": "按照逻辑顺序排列这些阅读步骤：",
        "prompt_zh": "按照逻辑顺序排列这些阅读步骤：",
        "items": [
            "快速浏览全文，了解大意",
            "仔细阅读，理解细节",
            "找出关键词和主题句",
            "总结文章的主旨"
        ],
        "answer": [
            "快速浏览全文，了解大意",
            "仔细阅读，理解细节",
            "找出关键词和主题句",
            "总结文章的主旨"
        ],
        "explanation": "阅读步骤：先整体浏览→细读理解→找关键信息→总结归纳。"
    },
    {
        "id": "chi-read-28",
        "type": "mcq",
        "prompt": "阅读短文：\n\n"小美每天清晨五点就起床练习小提琴。邻居们有时会抱怨太早，但小美的父母总是支持她的梦想。经过多年的努力，小美终于在全国比赛中获得了金奖。站在领奖台上，她热泪盈眶地说：'这个奖属于所有支持我的人。'"\n\n从小美的故事中，我们可以学到什么道理？",
        "prompt_zh": "从小美的故事中，我们可以学到什么道理？",
        "choices": [
            "坚持不懈和家人的支持是成功的关键",
            "音乐不需要练习",
            "邻居的意见最重要",
            "比赛获奖是唯一的成功"
        ],
        "answer": 0,
        "explanation": "小美每天坚持练习（坚持不懈），父母支持她的梦想（家人支持），最终成功——这说明两者都很重要。",
        "validator": "smart"
    },
    {
        "id": "chi-read-29",
        "type": "short",
        "prompt": "小美最终获得了什么奖项？",
        "prompt_zh": "小美最终获得了什么奖项？",
        "answer": "金奖",
        "answer_zh": "金奖",
        "hint": "在'全国比赛中获得了____'。",
        "explanation": "短文说'在全国比赛中获得了金奖'。",
        "validator": "smart"
    },
    {
        "id": "chi-read-30",
        "type": "match",
        "prompt": "将阅读理解技巧与其描述匹配：",
        "prompt_zh": "将阅读理解技巧与其描述匹配：",
        "pairs": [
            {"left": "找主旨", "left_zh": "找主旨", "right": "理解文章的中心思想", "right_zh": "理解文章的中心思想"},
            {"left": "推断", "left_zh": "推断", "right": "根据线索得出结论", "right_zh": "根据线索得出结论"},
            {"left": "分析语气", "left_zh": "分析语气", "right": "理解作者的态度和情感", "right_zh": "理解作者的态度和情感"},
            {"left": "找证据", "left_zh": "找证据", "right": "从文中寻找支持观点的信息", "right_zh": "从文中寻找支持观点的信息"}
        ],
        "explanation": "这些是基本的阅读理解技巧：找主旨、推断、分析语气、找证据。"
    }
]

# ============================================================
# CHINESE - Additional Writing Exercises (15)
# ============================================================
chinese_writing_exercises = [
    {
        "id": "chi-write-16",
        "type": "mcq",
        "prompt": "写记叙文时，以下哪个开头最能吸引读者？",
        "prompt_zh": "写记叙文时，以下哪个开头最能吸引读者？",
        "choices": [
            ""砰！"门被重重地摔上，整个屋子都在颤抖。",
            "今天我要写一件难忘的事。",
            "这是一个关于友谊的故事。",
            "我记得有一天发生了一件事。"
        ],
        "answer": 0,
        "explanation": "第一个选项使用拟声词和动作描写，制造悬念，能立即抓住读者的注意力。",
        "validator": "smart"
    },
    {
        "id": "chi-write-17",
        "type": "short",
        "prompt": "将这个'告诉'句子改写成'展示'句子：'他很生气。'",
        "prompt_zh": "将这个'告诉'句子改写成'展示'句子：'他很生气。'",
        "answer": "他握紧拳头",
        "answer_zh": "他握紧拳头",
        "hint": "用动作或表情来表现生气，而不是直接说。",
        "explanation": "展示句子用具体的动作描写来表现情感，例如：'他握紧拳头，太阳穴上的青筋跳动着。'",
        "validator": "smart"
    },
    {
        "id": "chi-write-18",
        "type": "mcq",
        "prompt": ""虽然......但是......"这个关联词表示什么关系？",
        "prompt_zh": ""虽然......但是......"这个关联词表示什么关系？",
        "choices": [
            "转折关系",
            "因果关系",
            "并列关系",
            "递进关系"
        ],
        "answer": 0,
        "explanation": "'虽然......但是......'表示转折，前后意思相反或有变化。",
        "validator": "smart"
    },
    {
        "id": "chi-write-19",
        "type": "drag-order",
        "prompt": "按正确顺序排列记叙文的结构：",
        "prompt_zh": "按正确顺序排列记叙文的结构：",
        "items": [
            "开头（引起兴趣）",
            "起因（事情的起因）",
            "经过（事情的发展）",
            "高潮（最紧张的部分）",
            "结尾（总结或感悟）"
        ],
        "answer": [
            "开头（引起兴趣）",
            "起因（事情的起因）",
            "经过（事情的发展）",
            "高潮（最紧张的部分）",
            "结尾（总结或感悟）"
        ],
        "explanation": "记叙文的基本结构：开头→起因→经过→高潮→结尾。"
    },
    {
        "id": "chi-write-20",
        "type": "mcq",
        "prompt": "以下哪个句子使用了比喻的修辞手法？",
        "prompt_zh": "以下哪个句子使用了比喻的修辞手法？",
        "choices": [
            "妈妈的爱像温暖的阳光，照耀着我成长。",
            "风呼呼地吹着。",
            "他跑得很快。",
            "花园里有很多花。"
        ],
        "answer": 0,
        "explanation": "比喻使用'像''如同''仿佛'等词把一种事物比作另一种事物。这里把妈妈的爱比作阳光。",
        "validator": "smart"
    },
    {
        "id": "chi-write-21",
        "type": "short",
        "prompt": "用一个比喻句描写'时间过得很快'。",
        "prompt_zh": "用一个比喻句描写'时间过得很快'。",
        "answer": "时间像流水",
        "answer_zh": "时间像流水",
        "hint": "用'像'或'如同'把时间比作某种快速流动的东西。",
        "explanation": "例如：'时间像流水一样一去不复返。''时间如白驹过隙，转眼即逝。'",
        "validator": "smart"
    },
    {
        "id": "chi-write-22",
        "type": "mcq",
        "prompt": "写作文时，以下哪种方法能让文章更生动？",
        "prompt_zh": "写作文时，以下哪种方法能让文章更生动？",
        "choices": [
            "加入对话、动作和心理描写",
            "只写事情的经过",
            "使用很多'然后'来连接句子",
            "把每件事都写得很简短"
        ],
        "answer": 0,
        "explanation": "对话让人物活起来，动作描写让场景更真实，心理描写让读者了解人物感受——这些都能让文章更生动。",
        "validator": "smart"
    },
    {
        "id": "chi-write-23",
        "type": "multi",
        "prompt": "以下哪些是记叙文中有效的结尾方式？（选择所有适用的）",
        "prompt_zh": "以下哪些是记叙文中有效的结尾方式？",
        "choices": [
            "总结文章的主题或道理",
            "呼应开头，首尾呼应",
            "写'完'或'结束'",
            "以发人深省的问题结尾"
        ],
        "answer": [0, 1, 3],
        "explanation": "好的结尾可以总结主题、呼应开头或引发思考。简单写'完'不是好的结尾方式。",
        "validator": "smart"
    },
    {
        "id": "chi-write-24",
        "type": "mcq",
        "prompt": "以下哪个句子的描写更加具体生动？",
        "prompt_zh": "以下哪个句子的描写更加具体生动？",
        "choices": [
            "外婆用布满皱纹的手轻轻抚摸我的头发，眼里闪着慈爱的光芒。",
            "外婆很爱我。",
            "外婆对我很好。",
            "我有一个好外婆。"
        ],
        "answer": 0,
        "explanation": "第一个选项通过具体的动作（轻轻抚摸）和细节描写（布满皱纹的手、慈爱的光芒）来展现外婆的爱，更加生动。",
        "validator": "smart"
    },
    {
        "id": "chi-write-25",
        "type": "short",
        "prompt": "作文中的'过渡句'有什么作用？",
        "prompt_zh": "作文中的'过渡句'有什么作用？",
        "answer": "连接段落",
        "answer_zh": "连接段落",
        "hint": "想想'过渡'这个词的意思——从一个地方到另一个地方。",
        "explanation": "过渡句的作用是承上启下，连接前后段落，使文章更加连贯流畅。",
        "validator": "smart"
    },
    {
        "id": "chi-write-26",
        "type": "mcq",
        "prompt": "修改病句：'我们要善于发现问题和解决问题的能力。'",
        "prompt_zh": "修改病句：'我们要善于发现问题和解决问题的能力。'",
        "choices": [
            "我们要培养发现问题和解决问题的能力。",
            "我们要善于发现问题和解决问题。",
            "以上两种修改都正确",
            "原句没有问题"
        ],
        "answer": 2,
        "explanation": "原句搭配不当：'善于'后面应接动词（发现和解决），或改为'培养......能力'。两种修改都正确。",
        "validator": "smart"
    },
    {
        "id": "chi-write-27",
        "type": "match",
        "prompt": "将修辞手法与其例子匹配：",
        "prompt_zh": "将修辞手法与其例子匹配：",
        "pairs": [
            {"left": "比喻", "left_zh": "比喻", "right": "月亮像一个银盘", "right_zh": "月亮像一个银盘"},
            {"left": "拟人", "left_zh": "拟人", "right": "花儿在微笑", "right_zh": "花儿在微笑"},
            {"left": "排比", "left_zh": "排比", "right": "她笑了，笑得灿烂，笑得开心，笑得甜美", "right_zh": "她笑了，笑得灿烂，笑得开心，笑得甜美"},
            {"left": "夸张", "left_zh": "夸张", "right": "他的声音震耳欲聋", "right_zh": "他的声音震耳欲聋"}
        ],
        "explanation": "比喻用'像'比较，拟人赋予人的特征，排比使用相似结构，夸张放大描述。"
    },
    {
        "id": "chi-write-28",
        "type": "mcq",
        "prompt": "写一篇关于'难忘的经历'的作文，以下哪个题目最能吸引读者？",
        "prompt_zh": "写一篇关于'难忘的经历'的作文，以下哪个题目最能吸引读者？",
        "choices": [
            "那一刻，我长大了",
            "难忘的经历",
            "一件难忘的事",
            "我的经历"
        ],
        "answer": 0,
        "explanation": "'那一刻，我长大了'更有感情色彩和画面感，暗示了成长和转变，比直接说'难忘的经历'更有吸引力。",
        "validator": "smart"
    },
    {
        "id": "chi-write-29",
        "type": "drag-order",
        "prompt": "按正确顺序排列写作步骤：",
        "prompt_zh": "按正确顺序排列写作步骤：",
        "items": [
            "审题和确定主题",
            "列出提纲和组织结构",
            "撰写初稿",
            "修改和润色",
            "检查语法和标点"
        ],
        "answer": [
            "审题和确定主题",
            "列出提纲和组织结构",
            "撰写初稿",
            "修改和润色",
            "检查语法和标点"
        ],
        "explanation": "写作步骤：审题→列提纲→写初稿→修改内容→检查细节。"
    },
    {
        "id": "chi-write-30",
        "type": "short",
        "prompt": "什么是'首尾呼应'？",
        "prompt_zh": "什么是'首尾呼应'？",
        "answer": "结尾回应开头",
        "answer_zh": "结尾回应开头",
        "hint": "想想'呼应'的意思——一个'呼'，一个'应'。",
        "explanation": "首尾呼应是指文章的结尾与开头相呼应，使文章结构完整，浑然一体。",
        "validator": "smart"
    }
]

# ============================================================
# Add exercises to the subjects
# ============================================================
def add_exercises_to_chapter(subject_id, chapter_id, new_exercises):
    """Add exercises to a specific chapter"""
    subject = next((s for s in data['subjects'] if s['id'] == subject_id), None)
    if not subject:
        print(f"❌ Subject {subject_id} not found!")
        return 0

    chapter = next((c for c in subject['chapters'] if c['id'] == chapter_id), None)
    if not chapter:
        print(f"❌ Chapter {chapter_id} not found in {subject_id}!")
        return 0

    # Add new exercises
    existing_ids = {e['id'] for e in chapter.get('exercises', [])}
    added = 0
    for ex in new_exercises:
        if ex['id'] not in existing_ids:
            chapter['exercises'].append(ex)
            added += 1

    print(f"✅ Added {added} exercises to {subject['title']} - {chapter['title']}")
    return added

# Add English exercises
print("\n" + "="*60)
print("Adding English Language Exercises")
print("="*60)
add_exercises_to_chapter('english', 'reading-comprehension', english_reading_exercises)
add_exercises_to_chapter('english', 'narrative-writing', english_writing_exercises)

# Add Chinese exercises
print("\n" + "="*60)
print("Adding Chinese Language Exercises")
print("="*60)
add_exercises_to_chapter('chinese', 'reading-comprehension', chinese_reading_exercises)
add_exercises_to_chapter('chinese', 'composition-writing', chinese_writing_exercises)

# Save updated content
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\n" + "="*60)
print("✅ All exercises added successfully!")
print("="*60)

# Final summary
print("\nFinal Summary:")
for subj_id in ['english', 'chinese']:
    subj = next((s for s in data['subjects'] if s['id'] == subj_id), None)
    if subj:
        print(f"\n{subj['title']}:")
        sec1_chapters = [ch for ch in subj['chapters'] if ch.get('gradeLevel') == 'sec1']
        for ch in sec1_chapters:
            if 'reading' in ch['id'].lower() or 'writing' in ch['id'].lower() or 'composition' in ch['id'].lower() or 'narrative' in ch['id'].lower():
                print(f"  {ch['title']}: {len(ch.get('exercises', []))} exercises")
