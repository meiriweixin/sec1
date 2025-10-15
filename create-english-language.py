import json

# Create English Language subject with all 6 chapters
english_subject = {
    "id": "english",
    "title": "English Language",
    "title_zh": "英语",
    "description": "Master English grammar, vocabulary, writing, and comprehension skills",
    "description_zh": "掌握英语语法、词汇、写作和理解技能",
    "color": "from-blue-500 to-indigo-600",
    "chapters": []
}

# Chapter 1: Grammar Foundations
grammar_chapter = {
    "id": "grammar-foundations",
    "title": "Grammar Foundations",
    "title_zh": "语法基础",
    "description": "Learn the building blocks of English grammar including parts of speech and sentence structure",
    "description_zh": "学习英语语法的基本组成部分，包括词性和句子结构",
    "objectives": [
        "Identify and use the 8 parts of speech correctly",
        "Understand basic sentence structure (Subject-Verb-Object)",
        "Apply subject-verb agreement rules",
        "Recognize and fix common grammar errors"
    ],
    "objectives_zh": [
        "正确识别和使用8种词性",
        "理解基本句子结构（主语-动词-宾语）",
        "应用主谓一致规则",
        "识别和修正常见语法错误"
    ],
    "sections": [
        {
            "id": "parts-of-speech",
            "type": "text",
            "title": "Parts of Speech",
            "title_zh": "词性",
            "content": """Understanding the **8 parts of speech** is essential for building strong grammar skills. Each word in English belongs to one of these categories.

**1. Nouns** - Names of people, places, things, or ideas
- **Common nouns**: book, city, teacher (general)
- **Proper nouns**: Singapore, Maria, Monday (specific, capitalized)
- **Abstract nouns**: happiness, freedom, love (ideas/feelings)
- **Collective nouns**: team, family, class (groups)

**Example**: *The **teacher** from **Singapore** showed **kindness** to her **class**.*

**2. Pronouns** - Replace nouns to avoid repetition
- **Personal**: I, you, he, she, it, we, they
- **Possessive**: my, your, his, her, its, our, their
- **Demonstrative**: this, that, these, those
- **Relative**: who, which, that, whom, whose

**Example**: *Sarah loves **her** dog. **She** takes **it** to the park every day.*

**3. Verbs** - Action or state of being words
- **Action verbs**: run, eat, study, think
- **Linking verbs**: am, is, are, was, were, seem, become
- **Helping verbs**: can, will, have, should, must

**Example**: *The students **are studying** hard. They **will pass** their exams.*

**4. Adjectives** - Describe nouns or pronouns
- Tell us: what kind, which one, how many
- Can be comparative (taller) or superlative (tallest)

**Example**: *The **beautiful**, **tall** building has **three** floors.*

**5. Adverbs** - Describe verbs, adjectives, or other adverbs
- Often end in -ly: quickly, carefully, happily
- Tell us: how, when, where, how often, to what extent

**Example**: *She **carefully** opened the door **very** **quietly**.*

**6. Prepositions** - Show relationships between words
- **Place**: in, on, at, under, above, between
- **Time**: before, after, during, until
- **Direction**: to, from, into, through

**Example**: *The book is **on** the table **in** the classroom.*

**7. Conjunctions** - Connect words, phrases, or clauses
- **Coordinating**: and, but, or, nor, for, yet, so (FANBOYS)
- **Subordinating**: because, although, if, when, while, since
- **Correlative**: both...and, either...or, neither...nor

**Example**: *I want to go **but** I have homework. I'll go **after** I finish.*

**8. Interjections** - Express emotions or exclamations
- Wow! Oh! Ouch! Hey! Hurray!

**Example**: ***Wow!** That's amazing!*

**Singapore Context:**
In Singapore, we use English daily at school, at hawker centers, and on MRT signs. Understanding parts of speech helps you communicate clearly in Singlish and formal English!""",
            "content_zh": """理解**8种词性**对建立强大的语法技能至关重要。英语中的每个单词都属于这些类别之一。

**1. 名词** - 人、地方、事物或想法的名称
- **普通名词**：book（书）、city（城市）、teacher（老师）（一般）
- **专有名词**：Singapore（新加坡）、Maria（玛丽亚）、Monday（星期一）（特定，大写）
- **抽象名词**：happiness（幸福）、freedom（自由）、love（爱）（想法/感觉）
- **集体名词**：team（团队）、family（家庭）、class（班级）（群体）

**例子**：*来自**新加坡**的**老师**对她的**班级**表现出**善意**。*

**2. 代词** - 替换名词以避免重复
- **人称代词**：I（我）、you（你）、he（他）、she（她）、it（它）、we（我们）、they（他们）
- **所有格代词**：my（我的）、your（你的）、his（他的）、her（她的）、its（它的）、our（我们的）、their（他们的）
- **指示代词**：this（这个）、that（那个）、these（这些）、those（那些）
- **关系代词**：who（谁）、which（哪个）、that（那个）、whom（谁）、whose（谁的）

**例子**：*莎拉爱**她的**狗。**她**每天带**它**去公园。*

**3. 动词** - 动作或状态词
- **动作动词**：run（跑）、eat（吃）、study（学习）、think（思考）
- **连系动词**：am（是）、is（是）、are（是）、was（是）、were（是）、seem（似乎）、become（成为）
- **助动词**：can（能）、will（将）、have（有）、should（应该）、must（必须）

**例子**：*学生们**正在努力学习**。他们**将通过**考试。*

**4. 形容词** - 描述名词或代词
- 告诉我们：什么类型、哪一个、多少
- 可以是比较级（taller更高）或最高级（tallest最高）

**例子**：***漂亮的**、**高的**建筑有**三**层楼。*

**5. 副词** - 描述动词、形容词或其他副词
- 通常以-ly结尾：quickly（快速地）、carefully（小心地）、happily（快乐地）
- 告诉我们：如何、何时、哪里、多久一次、到什么程度

**例子**：*她**小心地**打开门，**非常****安静地**。*

**6. 介词** - 显示单词之间的关系
- **地点**：in（在...里）、on（在...上）、at（在）、under（在...下）、above（在...上）、between（在...之间）
- **时间**：before（之前）、after（之后）、during（期间）、until（直到）
- **方向**：to（到）、from（从）、into（进入）、through（通过）

**例子**：*书**在**教室**里**的桌子**上**。*

**7. 连词** - 连接单词、短语或从句
- **并列连词**：and（和）、but（但是）、or（或者）、nor（也不）、for（因为）、yet（然而）、so（所以）（FANBOYS）
- **从属连词**：because（因为）、although（尽管）、if（如果）、when（当）、while（当）、since（自从）
- **关联连词**：both...and（既...又）、either...or（要么...要么）、neither...nor（既不...也不）

**例子**：*我想去**但是**我有家庭作业。我会在我完成**之后**去。*

**8. 感叹词** - 表达情感或感叹
- Wow!（哇！）Oh!（哦！）Ouch!（哎哟！）Hey!（嘿！）Hurray!（万岁！）

**例子**：***哇！**太棒了！*

**新加坡背景：**
在新加坡，我们每天在学校、小贩中心和地铁标志上使用英语。理解词性可以帮助你在新加坡式英语和正式英语中清晰地交流！"""
        },
        {
            "id": "sentence-structure",
            "type": "text",
            "title": "Basic Sentence Structure",
            "title_zh": "基本句子结构",
            "content": """Every complete sentence in English needs two essential parts: a **subject** and a **verb**. Understanding sentence structure helps you write clearly and correctly.

**Basic Sentence Pattern: Subject + Verb + Object (S-V-O)**

**Subject** - Who or what the sentence is about
**Verb** - The action or state of being
**Object** - Receives the action (not always present)

**Examples:**
- **Birds** (S) **sing** (V).
- **The student** (S) **completed** (V) **the homework** (O).
- **Singapore** (S) **is** (V) **a beautiful country** (O).

**Types of Sentences by Structure:**

**1. Simple Sentences** - One independent clause (one S-V)
- Contains one complete thought
- Can have compound subjects or verbs

**Examples:**
- The cat sleeps. (basic)
- My brother and I walked to school. (compound subject)
- She danced and sang. (compound verb)
- The hawker center near my house sells delicious chicken rice. (long but still simple)

**2. Compound Sentences** - Two independent clauses joined by a conjunction
- Use FANBOYS (for, and, nor, but, or, yet, so)
- Each clause can stand alone

**Examples:**
- I like laksa, **but** my friend prefers ramen.
- The sun was shining, **so** we went to the beach.
- She studied hard, **and** she passed the exam.

**3. Complex Sentences** - One independent clause + one or more dependent clauses
- Dependent clause starts with subordinating conjunction
- Cannot stand alone

**Examples:**
- **Because it was raining**, we stayed indoors. (dependent + independent)
- We went to the library **after school ended**. (independent + dependent)
- **Although I was tired**, I finished my homework **before dinner**. (dependent + independent + dependent)

**4. Compound-Complex Sentences** - Two or more independent clauses + at least one dependent clause

**Example:**
- **Although it was late**, I called my friend, **and** we talked for an hour.

**Subject Types:**

**Simple Subject** - Main noun/pronoun
- *The tall boy* runs fast. (Subject: **boy**)

**Complete Subject** - All words describing the subject
- ***The tall boy from my class*** runs fast.

**Compound Subject** - Two or more subjects sharing same verb
- ***Sarah and Tom*** went to the movies.

**Verb Types:**

**Action Verbs** - Show action
- run, jump, think, write, eat

**Linking Verbs** - Connect subject to description
- am, is, are, was, were, seem, appear, become
- The food **is** delicious.

**Helping Verbs** - Help main verb
- can, will, should, must, have, has, had
- She **has finished** her work.

**Common Sentence Errors to Avoid:**

**❌ Sentence Fragment** - Incomplete thought
- *Because I was tired.* (What happened?)
- ✅ Fix: *Because I was tired, I went to bed early.*

**❌ Run-on Sentence** - Two sentences joined incorrectly
- *I love reading books I go to the library often.*
- ✅ Fix: *I love reading books, so I go to the library often.*

**❌ Comma Splice** - Two sentences joined only with comma
- *It was raining, we stayed home.*
- ✅ Fix: *It was raining, so we stayed home.*

**Singapore Context:**
When writing formal emails to teachers or applications for scholarships, using proper sentence structure shows professionalism. In casual conversation at the canteen, we might say "Can lah!" but in essays, write complete sentences like "Yes, that is possible."""",
            "content_zh": """英语中的每个完整句子都需要两个基本部分：**主语**和**动词**。理解句子结构可以帮助你清晰正确地写作。

**基本句子模式：主语 + 动词 + 宾语（S-V-O）**

**主语** - 句子讲述的是谁或什么
**动词** - 动作或状态
**宾语** - 接受动作（并非总是存在）

**例子：**
- **鸟儿** (S) **唱歌** (V)。
- **学生** (S) **完成了** (V) **家庭作业** (O)。
- **新加坡** (S) **是** (V) **一个美丽的国家** (O)。

**按结构分类的句子类型：**

**1. 简单句** - 一个独立子句（一个S-V）
- 包含一个完整的思想
- 可以有复合主语或动词

**例子：**
- 猫睡觉。（基本）
- 我和我哥哥走到学校。（复合主语）
- 她跳舞和唱歌。（复合动词）
- 我家附近的小贩中心卖美味的海南鸡饭。（长但仍然简单）

**2. 并列句** - 两个由连词连接的独立子句
- 使用FANBOYS（for, and, nor, but, or, yet, so）
- 每个子句都可以独立存在

**例子：**
- 我喜欢叻沙，**但是**我的朋友更喜欢拉面。
- 阳光明媚，**所以**我们去了海滩。
- 她努力学习，**并且**她通过了考试。

**3. 复杂句** - 一个独立子句 + 一个或多个从属子句
- 从属子句以从属连词开头
- 不能独立存在

**例子：**
- **因为下雨**，我们待在室内。（从属 + 独立）
- 我们放学后去了图书馆。（独立 + 从属）
- **虽然我很累**，我在晚餐前完成了我的家庭作业。（从属 + 独立 + 从属）

**4. 复合复杂句** - 两个或更多独立子句 + 至少一个从属子句

**例子：**
- **虽然很晚了**，我给我的朋友打了电话，**并且**我们聊了一个小时。

**主语类型：**

**简单主语** - 主要名词/代词
- *高个子男孩*跑得很快。（主语：**男孩**）

**完整主语** - 所有描述主语的词
- ***我班上的高个子男孩***跑得很快。

**复合主语** - 两个或更多主语共享同一个动词
- ***莎拉和汤姆***去看电影了。

**动词类型：**

**动作动词** - 显示动作
- 跑、跳、思考、写、吃

**连系动词** - 连接主语和描述
- am, is, are, was, were, seem, appear, become
- 食物**很**美味。

**助动词** - 帮助主要动词
- can, will, should, must, have, has, had
- 她**已经完成了**她的工作。

**要避免的常见句子错误：**

**❌ 句子片段** - 不完整的思想
- *因为我很累。*（发生了什么？）
- ✅ 修正：*因为我很累，我早早睡了。*

**❌ 连写句** - 两个句子错误地连接
- *我喜欢读书我经常去图书馆。*
- ✅ 修正：*我喜欢读书，所以我经常去图书馆。*

**❌ 逗号错误** - 两个句子只用逗号连接
- *下雨了，我们待在家里。*
- ✅ 修正：*下雨了，所以我们待在家里。*

**新加坡背景：**
当给老师写正式邮件或申请奖学金时，使用正确的句子结构显示专业性。在食堂的随意对话中，我们可能会说"Can lah!"但在论文中，写完整的句子如"Yes, that is possible.""""
        },
        {
            "id": "subject-verb-agreement",
            "type": "text",
            "title": "Subject-Verb Agreement",
            "title_zh": "主谓一致",
            "content": """**Subject-verb agreement** means the subject and verb in a sentence must match in number. If the subject is singular, the verb must be singular. If the subject is plural, the verb must be plural.

**Basic Rules:**

**Rule 1: Singular subjects take singular verbs**
- The student **walks** to school. ✅
- The student **walk** to school. ❌

**Rule 2: Plural subjects take plural verbs**
- The students **walk** to school. ✅
- The students **walks** to school. ❌

**Present Tense Singular Verbs:**
- Add -s or -es to most verbs for third person singular (he, she, it)
- I/you/we/they walk → he/she/it walk**s**
- I/you/we/they watch → he/she/it watch**es**

**Tricky Situations:**

**1. Compound Subjects with AND**
Use **plural** verb
- Tom **and** Sarah **are** friends. ✅
- Both **are** important. ✅

**2. Compound Subjects with OR/NOR**
Verb agrees with the **closest** subject
- Neither the teacher **nor** the students **are** ready. ✅
- Neither the students **nor** the teacher **is** ready. ✅
- Either you **or** I **am** going. ✅

**3. Collective Nouns**
Usually **singular** when acting as one unit
- The team **is** playing well. ✅ (team as a unit)
- The team **are** arguing among themselves. ✅ (individual members)

**Common collective nouns:**
- family, team, group, class, committee, audience, crowd

**4. Indefinite Pronouns**

**Always Singular:**
- each, every, everyone, everybody, everything
- anyone, anybody, anything
- someone, somebody, something
- no one, nobody, nothing
- either, neither

**Examples:**
- Everyone **is** ready. ✅
- Somebody **has** my book. ✅
- Neither **looks** good. ✅

**Always Plural:**
- both, few, many, several
- Both **are** correct. ✅
- Many **have** arrived. ✅

**Depends on Context:**
- all, any, more, most, none, some
- Some of the cake **is** gone. ✅ (cake = singular)
- Some of the students **are** absent. ✅ (students = plural)

**5. Words Between Subject and Verb**
The verb agrees with the **subject**, not words in between

- The box of chocolates **is** on the table. ✅ (subject: box)
- The students in my class **are** smart. ✅ (subject: students)
- The bouquet of flowers **smells** wonderful. ✅ (subject: bouquet)

**6. Inverted Sentences**
Find the real subject first

- There **are** many students. ✅ (subject: students)
- Here **is** your book. ✅ (subject: book)
- Where **are** the keys? ✅ (subject: keys)

**7. Titles and Names**
Always **singular**

- *The Lord of the Rings* **is** my favorite book. ✅
- Singapore Math **is** challenging. ✅
- The United States **is** large. ✅ (one country)

**8. Money, Time, Distance**
Usually **singular** when referring to a unit

- Five dollars **is** enough. ✅
- Two hours **seems** long. ✅
- Ten kilometers **is** far. ✅

**Common Errors:**

**❌ The list of items are on the table.**
✅ The list of items **is** on the table. (subject: list)

**❌ One of my friends are coming.**
✅ One of my friends **is** coming. (subject: one)

**❌ The team are winning.**
✅ The team **is** winning. (team as unit)

**❌ Each of the students have a book.**
✅ Each of the students **has** a book. (subject: each)

**❌ Neither of them are right.**
✅ Neither of them **is** right. (subject: neither)

**Singapore Context:**
In Singapore, we sometimes hear "The price very cheap" in Singlish, but in formal English, we write "The price **is** very cheap." For PSLE and O-Level exams, always use proper subject-verb agreement!

**Practice Tip:**
1. Find the subject
2. Determine if it's singular or plural
3. Match the verb accordingly
4. Ignore words between subject and verb""",
            "content_zh": """**主谓一致**意味着句子中的主语和动词必须在数量上匹配。如果主语是单数，动词必须是单数。如果主语是复数，动词必须是复数。

**基本规则：**

**规则1：单数主语用单数动词**
- 学生**走**到学校。✅
- 学生**走们**到学校。❌

**规则2：复数主语用复数动词**
- 学生们**走**到学校。✅
- 学生们**走**到学校。❌

**现在时单数动词：**
- 对于第三人称单数（he, she, it），大多数动词加-s或-es
- I/you/we/they walk → he/she/it walk**s**
- I/you/we/they watch → he/she/it watch**es**

**棘手情况：**

**1. 用AND连接的复合主语**
使用**复数**动词
- Tom **和** Sarah **是**朋友。✅
- 两者**都是**重要的。✅

**2. 用OR/NOR连接的复合主语**
动词与**最近的**主语一致
- 老师**和**学生们**都没有**准备好。✅
- 学生们**和**老师**都没有**准备好。✅
- **要么**你**要么**我**去**。✅

**3. 集体名词**
通常作为一个单位时用**单数**
- 团队**正在**表现良好。✅（团队作为一个单位）
- 团队成员**正在**争论。✅（个别成员）

**常见集体名词：**
- family（家庭）、team（团队）、group（组）、class（班级）、committee（委员会）、audience（观众）、crowd（人群）

**4. 不定代词**

**总是单数：**
- each（每个）、every（每一个）、everyone（每个人）、everybody（每个人）、everything（一切）
- anyone（任何人）、anybody（任何人）、anything（任何事）
- someone（某人）、somebody（某人）、something（某事）
- no one（没有人）、nobody（没有人）、nothing（没有什么）
- either（任何一个）、neither（两者都不）

**例子：**
- 每个人**都**准备好了。✅
- 有人**拿了**我的书。✅
- 两者**都不**好看。✅

**总是复数：**
- both（两者）、few（少数）、many（许多）、several（几个）
- 两者**都**正确。✅
- 许多人**已经**到达。✅

**取决于上下文：**
- all（所有）、any（任何）、more（更多）、most（大多数）、none（没有）、some（一些）
- 一些蛋糕**被吃掉了**。✅（蛋糕 = 单数）
- 一些学生**缺席了**。✅（学生 = 复数）

**5. 主语和动词之间的词**
动词与**主语**一致，而不是中间的词

- 巧克力盒子**在**桌子上。✅（主语：盒子）
- 我班上的学生**很**聪明。✅（主语：学生）
- 花束**闻起来**很香。✅（主语：花束）

**6. 倒装句**
先找到真正的主语

- **有**许多学生。✅（主语：学生）
- **这是**你的书。✅（主语：书）
- 钥匙**在哪里**？✅（主语：钥匙）

**7. 标题和名称**
总是**单数**

- *指环王* **是**我最喜欢的书。✅
- 新加坡数学**很**有挑战性。✅
- 美国**很**大。✅（一个国家）

**8. 金钱、时间、距离**
通常作为一个单位时用**单数**

- 五美元**就足够了**。✅
- 两小时**似乎**很长。✅
- 十公里**很**远。✅

**常见错误：**

**❌ 项目列表在桌子上。**
✅ 项目列表**在**桌子上。（主语：列表）

**❌ 我的一个朋友要来。**
✅ 我的一个朋友**要来**。（主语：一个）

**❌ 团队正在获胜。**
✅ 团队**正在**获胜。（团队作为单位）

**❌ 每个学生都有一本书。**
✅ 每个学生**都有**一本书。（主语：每个）

**❌ 他们两个都不对。**
✅ 他们两个**都不对**。（主语：两者都不）

**新加坡背景：**
在新加坡，我们有时会在新加坡式英语中听到"The price very cheap"，但在正式英语中，我们写"The price **is** very cheap。"对于PSLE和O-Level考试，始终使用正确的主谓一致！

**练习提示：**
1. 找到主语
2. 确定它是单数还是复数
3. 相应地匹配动词
4. 忽略主语和动词之间的词"""
        }
    ],
    "exercises": [
        {
            "id": "ex1",
            "type": "mcq",
            "question": "Identify the part of speech of the underlined word: The **beautiful** garden has many flowers.",
            "question_zh": "识别下划线单词的词性：**美丽的**花园有许多花。",
            "choices": ["Noun", "Verb", "Adjective", "Adverb"],
            "choices_zh": ["名词", "动词", "形容词", "副词"],
            "answer": 2,
            "explanation": "'Beautiful' is an adjective because it describes the noun 'garden', telling us what kind of garden it is.",
            "explanation_zh": "'Beautiful'是形容词，因为它描述名词'garden'，告诉我们是什么样的花园。"
        },
        {
            "id": "ex2",
            "type": "mcq",
            "question": "Which sentence has correct subject-verb agreement?",
            "question_zh": "哪个句子具有正确的主谓一致？",
            "choices": [
                "The list of names are on the board.",
                "The list of names is on the board.",
                "The list of names be on the board.",
                "The lists of name is on the board."
            ],
            "choices_zh": [
                "名单在黑板上。（错误）",
                "名单在黑板上。（正确）",
                "名单在黑板上。（错误）",
                "名单在黑板上。（错误）"
            ],
            "answer": 1,
            "explanation": "The subject is 'list' (singular), not 'names'. Therefore, we use the singular verb 'is'. Don't be confused by words between the subject and verb.",
            "explanation_zh": "主语是'list'（单数），而不是'names'。因此，我们使用单数动词'is'。不要被主语和动词之间的词混淆。"
        },
        {
            "id": "ex3",
            "type": "mcq",
            "question": "What type of sentence is this? 'I wanted to go to the movies, but I had too much homework.'",
            "question_zh": "这是什么类型的句子？'我想去看电影，但我有太多家庭作业。'",
            "choices": ["Simple sentence", "Compound sentence", "Complex sentence", "Compound-complex sentence"],
            "choices_zh": ["简单句", "并列句", "复杂句", "复合复杂句"],
            "answer": 1,
            "explanation": "This is a compound sentence because it has two independent clauses ('I wanted to go to the movies' and 'I had too much homework') joined by the coordinating conjunction 'but'.",
            "explanation_zh": "这是一个并列句，因为它有两个独立子句（'我想去看电影'和'我有太多家庭作业'），由并列连词'but'连接。"
        },
        {
            "id": "ex4",
            "type": "mcq",
            "question": "Which sentence is correct?",
            "question_zh": "哪个句子是正确的？",
            "choices": [
                "Everyone have finished their homework.",
                "Everyone has finished their homework.",
                "Everyone are finished their homework.",
                "Everyone were finished their homework."
            ],
            "choices_zh": [
                "每个人都完成了他们的家庭作业。（错误）",
                "每个人都完成了他们的家庭作业。（正确）",
                "每个人都完成了他们的家庭作业。（错误）",
                "每个人都完成了他们的家庭作业。（错误）"
            ],
            "answer": 1,
            "explanation": "'Everyone' is a singular indefinite pronoun, so it requires the singular verb 'has', not 'have'.",
            "explanation_zh": "'Everyone'是一个单数不定代词，所以它需要单数动词'has'，而不是'have'。"
        },
        {
            "id": "ex5",
            "type": "short",
            "question": "Identify the complete subject in this sentence: 'The tall boy from my class won the race.'",
            "question_zh": "识别这个句子中的完整主语：'我班上的高个子男孩赢得了比赛。'",
            "answer": "The tall boy from my class",
            "validator": "exact",
            "explanation": "The complete subject includes all the words that describe who or what the sentence is about: 'The tall boy from my class'. The simple subject is just 'boy'.",
            "explanation_zh": "完整主语包括描述句子讲述的是谁或什么的所有词：'我班上的高个子男孩'。简单主语只是'男孩'。"
        }
    ]
}

# Save the chapter
with open('grammar-foundations-chapter.json', 'w', encoding='utf-8') as f:
    json.dump(grammar_chapter, f, indent=2, ensure_ascii=False)

print('Grammar Foundations chapter created!')
print(f'Sections: {len(grammar_chapter["sections"])}')
print(f'Exercises: {len(grammar_chapter["exercises"])}')
