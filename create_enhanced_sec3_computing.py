#!/usr/bin/env python3
"""
Create enhanced Sec 3 Computing chapters with detailed sections.
Expands minimal 1-section chapters into comprehensive 3-section chapters.
"""

import json
import os
from datetime import datetime

chapters_dir = "chapters"
os.makedirs(chapters_dir, exist_ok=True)

# Enhanced Sec 3 Computing chapters (complete rewrite with proper structure)
enhanced_chapters = [
    {
        "id": "introduction-to-computing",
        "title": "Introduction to Computing",
        "title_zh": "计算导论",
        "gradeLevel": "sec3",
        "description": "Understanding computer systems, hardware, software, and computing careers",
        "description_zh": "了解计算机系统、硬件、软件和计算职业",
        "objectives": [
            "Identify main computer hardware components",
            "Distinguish between system and application software",
            "Understand computing's role in Singapore's Smart Nation",
            "Explore career opportunities in computing"
        ],
        "objectives_zh": [
            "识别主要计算机硬件组件",
            "区分系统软件和应用软件",
            "了解计算在新加坡智慧国家中的作用",
            "探索计算领域的职业机会"
        ],
        "sections": [
            {
                "id": "computer-systems",
                "type": "text",
                "title": "Computer Hardware & Software",
                "title_zh": "计算机硬件与软件",
                "content": "**Computer systems** consist of hardware (physical components) and software (programs and data).\n\n**Main hardware components:**\n\n1. **CPU (Central Processing Unit)**: The \"brain\" that executes instructions\n2. **RAM (Random Access Memory)**: Temporary storage for running programs\n3. **Storage devices**: Hard drive (HDD) or solid-state drive (SSD) for permanent data\n4. **Input devices**: Keyboard, mouse, touchscreen, camera, microphone\n5. **Output devices**: Monitor, printer, speakers, headphones\n\n**Software categories:**\n\n**System software**: Manages hardware and provides platform for applications\n- Operating systems: Windows, macOS, Linux, Android, iOS\n- Device drivers: Enable hardware to communicate with OS\n- Utilities: Antivirus, disk cleanup, backup tools\n\n**Application software**: Programs for specific user tasks\n- Productivity: Microsoft Office, Google Workspace\n- Communication: WhatsApp, Zoom, email clients\n- Entertainment: Games, streaming apps, media players\n- Education: Learning management systems, digital textbooks\n\n**Singapore context:**\n\nSingapore's Smart Nation initiative relies on computing infrastructure - from NEWater plant automation to MRT train control systems, from TraceTogether to SkillsFuture digital platforms.",
                "content_zh": "**计算机系统**由硬件（物理组件）和软件（程序和数据）组成。\n\n**主要硬件组件：**\n\n1. **CPU（中央处理器）**："大脑"，执行指令\n2. **RAM（随机存取内存）**：运行程序的临时存储\n3. **存储设备**：硬盘（HDD）或固态硬盘（SSD），用于永久数据\n4. **输入设备**：键盘、鼠标、触摸屏、摄像头、麦克风\n5. **输出设备**：显示器、打印机、扬声器、耳机\n\n**软件类别：**\n\n**系统软件**：管理硬件并为应用程序提供平台\n- 操作系统：Windows、macOS、Linux、Android、iOS\n- 设备驱动程序：使硬件与操作系统通信\n- 实用程序：防病毒、磁盘清理、备份工具\n\n**应用软件**：特定用户任务的程序\n- 生产力：Microsoft Office、Google Workspace\n- 通信：WhatsApp、Zoom、电子邮件客户端\n- 娱乐：游戏、流媒体应用、媒体播放器\n- 教育：学习管理系统、数字教科书\n\n**新加坡情境：**\n\n新加坡的智慧国家倡议依赖于计算基础设施——从新生水厂自动化到地铁列车控制系统，从TraceTogether到SkillsFuture数字平台。"
            },
            {
                "id": "computing-society",
                "type": "text",
                "title": "Computing in Society & Smart Nation",
                "title_zh": "计算在社会中的应用与智慧国家",
                "content": "Computing has transformed how we live, work, learn, and communicate in Singapore.\n\n**Smart Nation initiatives:**\n\n**1. E-Government services**\n- Singpass: Digital identity for government services\n- MyInfo: Auto-fill personal data for online applications\n- GoBusiness: One-stop portal for business licenses\n- HealthHub: Access medical records and appointments\n\n**2. Cashless payments**\n- PayNow: Instant bank transfers using mobile number\n- GrabPay, PayLah!, FavePay: Digital wallets\n- NETS, credit/debit cards with contactless payment\n- QR code payments at hawker centers and shops\n\n**3. Smart mobility**\n- Autonomous vehicles: Self-driving bus trials\n- MyTransport app: Real-time bus/train arrival info\n- ERP 2.0: Satellite-based road pricing\n- Grab, Gojek, Ryde: Ride-hailing platforms\n\n**4. Healthcare technology**\n- Telemedicine: Online doctor consultations\n- TraceTogether: COVID-19 contact tracing\n- HealthTech devices: Wearables monitoring vital signs\n- Electronic health records across hospitals\n\n**5. Education technology**\n- Student Learning Space (SLS)\n- Home-based learning platforms\n- Digital literacy programs\n- Online assessments and e-examinations\n\n**Impact on jobs:**\n\nComputing creates new careers while automating routine tasks. Future-ready skills include programming, data analysis, cybersecurity, AI/ML, and digital design.",
                "content_zh": "计算改变了我们在新加坡生活、工作、学习和交流的方式。\n\n**智慧国家倡议：**\n\n**1. 电子政府服务**\n- Singpass：政府服务的数字身份\n- MyInfo：在线申请的个人数据自动填充\n- GoBusiness：商业许可证一站式门户\n- HealthHub：访问医疗记录和预约\n\n**2. 无现金支付**\n- PayNow：使用手机号码即时银行转账\n- GrabPay、PayLah!、FavePay：数字钱包\n- NETS、信用卡/借记卡非接触式支付\n- 小贩中心和商店的二维码支付\n\n**3. 智能出行**\n- 自动驾驶车辆：自动驾驶巴士试验\n- MyTransport应用：实时公交/地铁到达信息\n- ERP 2.0：基于卫星的道路收费\n- Grab、Gojek、Ryde：叫车平台\n\n**4. 医疗技术**\n- 远程医疗：在线医生咨询\n- TraceTogether：COVID-19接触者追踪\n- 健康科技设备：监测生命体征的可穿戴设备\n- 医院间的电子健康记录\n\n**5. 教育技术**\n- 学生学习平台（SLS）\n- 家庭学习平台\n- 数字素养计划\n- 在线评估和电子考试\n\n**对工作的影响：**\n\n计算创造新职业，同时自动化常规任务。未来就绪技能包括编程、数据分析、网络安全、AI/ML和数字设计。"
            },
            {
                "id": "computing-careers",
                "type": "text",
                "title": "Careers in Computing",
                "title_zh": "计算领域的职业",
                "content": "The computing industry offers diverse and well-paying career paths in Singapore.\n\n**Software development:**\n\n1. **Software Engineer**: Design and build applications\n2. **Web Developer**: Create websites and web applications\n3. **Mobile App Developer**: Build iOS/Android apps\n4. **Game Developer**: Design interactive games\n5. **Full-Stack Developer**: Work on both frontend and backend\n\n**Data & AI:**\n\n1. **Data Scientist**: Analyze large datasets for insights\n2. **Machine Learning Engineer**: Build AI models\n3. **Data Analyst**: Transform data into business decisions\n4. **AI Researcher**: Develop new AI algorithms\n\n**Cybersecurity:**\n\n1. **Security Analyst**: Protect systems from cyber threats\n2. **Ethical Hacker**: Find vulnerabilities before attackers do\n3. **Security Consultant**: Advise organizations on security\n\n**Other computing careers:**\n\n1. **UX/UI Designer**: Design user-friendly interfaces\n2. **DevOps Engineer**: Automate software deployment\n3. **Cloud Architect**: Design cloud infrastructure\n4. **Database Administrator**: Manage data systems\n5. **IT Support Specialist**: Help users solve technical issues\n\n**Skills needed:**\n\n- **Technical skills**: Programming languages (Python, Java, JavaScript), databases, cloud platforms\n- **Soft skills**: Problem-solving, teamwork, communication, continuous learning\n- **Domain knowledge**: Understanding of business, finance, healthcare, or other industries\n\n**Education paths in Singapore:**\n\n- O-Level Computing → Polytechnic Diploma (IT, Cybersecurity, AI)\n- A-Level Computing → University (Computer Science, Information Systems)\n- ITE courses → Specialist diplomas\n- Online courses and certifications (Coursera, Udemy, AWS, Google)\n\n**Salary range:** Entry-level: $3,000-$4,500/month, Experienced: $6,000-$15,000+/month",
                "content_zh": "计算行业在新加坡提供多样化且高薪的职业道路。\n\n**软件开发：**\n\n1. **软件工程师**：设计和构建应用程序\n2. **网页开发人员**：创建网站和网络应用\n3. **移动应用开发人员**：构建iOS/Android应用\n4. **游戏开发人员**：设计互动游戏\n5. **全栈开发人员**：前端和后端都工作\n\n**数据与AI：**\n\n1. **数据科学家**：分析大型数据集以获得洞察\n2. **机器学习工程师**：构建AI模型\n3. **数据分析师**：将数据转化为商业决策\n4. **AI研究员**：开发新的AI算法\n\n**网络安全：**\n\n1. **安全分析师**：保护系统免受网络威胁\n2. **道德黑客**：在攻击者之前发现漏洞\n3. **安全顾问**：为组织提供安全建议\n\n**其他计算职业：**\n\n1. **UX/UI设计师**：设计用户友好的界面\n2. **DevOps工程师**：自动化软件部署\n3. **云架构师**：设计云基础设施\n4. **数据库管理员**：管理数据系统\n5. **IT支持专员**：帮助用户解决技术问题\n\n**所需技能：**\n\n- **技术技能**：编程语言（Python、Java、JavaScript）、数据库、云平台\n- **软技能**：问题解决、团队合作、沟通、持续学习\n- **领域知识**：对商业、金融、医疗保健或其他行业的理解\n\n**新加坡的教育途径：**\n\n- O水准计算→理工学院文凭（IT、网络安全、AI）\n- A水准计算→大学（计算机科学、信息系统）\n- ITE课程→专业文凭\n- 在线课程和认证（Coursera、Udemy、AWS、Google）\n\n**薪资范围：**入门级：$3,000-$4,500/月，经验丰富：$6,000-$15,000+/月"
            }
        ],
        "exercises": []  # Keep existing exercises
    },

    {
        "id": "computational-thinking",
        "title": "Computational Thinking",
        "title_zh": "计算思维",
        "gradeLevel": "sec3",
        "description": "Learn problem-solving techniques: decomposition, patterns, abstraction, algorithms",
        "description_zh": "学习问题解决技术：分解、模式、抽象、算法",
        "objectives": [
            "Apply decomposition to break down complex problems",
            "Recognize patterns in data and problems",
            "Use abstraction to simplify problems",
            "Design algorithms for systematic solutions"
        ],
        "objectives_zh": [
            "应用分解将复杂问题分解",
            "识别数据和问题中的模式",
            "使用抽象简化问题",
            "为系统解决方案设计算法"
        ],
        "sections": [
            {
                "id": "decomposition-patterns",
                "type": "text",
                "title": "Decomposition & Pattern Recognition",
                "title_zh": "分解与模式识别",
                "content": "**Decomposition** breaks complex problems into smaller, manageable sub-problems.\n\n**Steps for decomposition:**\n\n1. Understand the overall problem\n2. Identify major components or tasks\n3. Break each component into smaller steps\n4. Organize steps in logical order\n5. Solve each sub-problem independently\n6. Combine solutions\n\n**Example: Organizing a school event at Marina Bay**\n\nMain problem: Organize class outing\n\nSub-problems:\n- **Transport**: Book bus, plan route, calculate travel time\n- **Venue**: Reserve space, check opening hours, book tickets\n- **Budget**: Calculate costs (transport + tickets + food)\n- **Schedule**: Create timeline, allocate time for activities\n- **Food**: Find halal options, book restaurants, consider dietary needs\n- **Safety**: Emergency contacts, first aid kit, buddy system\n\n**Pattern Recognition** identifies similarities to reuse proven solutions.\n\n**Types of patterns:**\n\n1. **Repeating sequences**: 2, 4, 6, 8... (even numbers)\n2. **Similar structures**: All hawker centers have similar layout (food stalls around seating area)\n3. **Common algorithms**: Searching, sorting, counting occur in many problems\n4. **Problem types**: Optimization (shortest path, minimum cost)\n\n**Singapore examples:**\n\n- **MRT fare calculation**: Base fare + distance-based increment (pattern applies to taxis, ERP too)\n- **HDB block numbering**: Patterns help locate addresses\n- **School timetable**: Weekly recurring pattern\n- **Bus routes**: Numbered patterns (1-99: trunk services, 100-199: feeder services)",
                "content_zh": "**分解**将复杂问题分解为更小、可管理的子问题。\n\n**分解步骤：**\n\n1. 理解整体问题\n2. 确定主要组件或任务\n3. 将每个组件分解为更小的步骤\n4. 按逻辑顺序组织步骤\n5. 独立解决每个子问题\n6. 组合解决方案\n\n**例子：在滨海湾组织学校活动**\n\n主要问题：组织班级郊游\n\n子问题：\n- **交通**：预订巴士、规划路线、计算旅行时间\n- **场地**：预订空间、检查开放时间、预订门票\n- **预算**：计算成本（交通+门票+食物）\n- **时间表**：创建时间线、为活动分配时间\n- **食物**：找清真选项、预订餐厅、考虑饮食需求\n- **安全**：紧急联系人、急救箱、伙伴系统\n\n**模式识别**识别相似性以重用已验证的解决方案。\n\n**模式类型：**\n\n1. **重复序列**：2、4、6、8...（偶数）\n2. **相似结构**：所有小贩中心布局相似（食物摊位围绕座位区）\n3. **常见算法**：搜索、排序、计数在许多问题中出现\n4. **问题类型**：优化（最短路径、最小成本）\n\n**新加坡例子：**\n\n- **地铁票价计算**：基本票价+基于距离的增量（模式也适用于出租车、ERP）\n- **HDB组屋编号**：模式帮助定位地址\n- **学校时间表**：每周重复模式\n- **公交路线**：编号模式（1-99：主干服务，100-199：接驳服务）"
            },
            {
                "id": "abstraction",
                "type": "text",
                "title": "Abstraction",
                "title_zh": "抽象",
                "content": "**Abstraction** focuses on important information while hiding unnecessary details.\n\n**Why use abstraction?**\n\n- Simplifies complex systems\n- Makes problems easier to understand\n- Allows focus on essential features\n- Hides implementation details\n\n**Levels of abstraction:**\n\n**High-level abstraction**: General concepts\n- \"Send a message\" (don't need to know about network protocols)\n- \"Search on Google\" (don't see complex ranking algorithms)\n\n**Mid-level abstraction**: More specific but still abstract\n- \"Type message → Select contact → Press send\"\n- \"Enter search terms → Click search → View results\"\n\n**Low-level abstraction**: Technical implementation\n- Network packets, TCP/IP protocols, encryption\n- Web crawlers, PageRank algorithm, data centers\n\n**Real-world examples:**\n\n**1. ATM machine**\n- High-level: \"Withdraw cash\"\n- You see: Insert card → Enter PIN → Select amount → Take cash\n- Hidden: Card reader, PIN encryption, bank database connection, cash dispenser mechanism, transaction logging\n\n**2. Using Grab app**\n- High-level: \"Book a ride\"\n- You see: Set pickup/dropoff → Choose car type → Confirm → Track driver\n- Hidden: GPS algorithms, driver matching system, fare calculation, payment processing, database updates\n\n**3. Online shopping (Lazada/Shopee)**\n- High-level: \"Buy a product\"\n- You see: Browse → Add to cart → Checkout → Pay → Track delivery\n- Hidden: Inventory systems, recommendation algorithms, payment gateways, logistics network, seller notifications\n\n**Abstraction in programming:**\n\n- **Functions**: Name a set of instructions (e.g., `calculate_gst(price)` hides the formula)\n- **Libraries**: Use complex features without knowing internal code\n- **APIs**: Interact with services without seeing their implementation",
                "content_zh": "**抽象**关注重要信息，同时隐藏不必要的细节。\n\n**为什么使用抽象？**\n\n- 简化复杂系统\n- 使问题更容易理解\n- 允许关注基本特征\n- 隐藏实现细节\n\n**抽象级别：**\n\n**高级抽象**：一般概念\n- "发送消息"（无需了解网络协议）\n- "在Google上搜索"（看不到复杂的排名算法）\n\n**中级抽象**：更具体但仍然抽象\n- "输入消息→选择联系人→按发送"\n- "输入搜索词→点击搜索→查看结果"\n\n**低级抽象**：技术实现\n- 网络数据包、TCP/IP协议、加密\n- 网络爬虫、PageRank算法、数据中心\n\n**实际例子：**\n\n**1. ATM机器**\n- 高级："取现"\n- 你看到：插卡→输入PIN→选择金额→取现金\n- 隐藏：读卡器、PIN加密、银行数据库连接、现金分配机制、交易记录\n\n**2. 使用Grab应用**\n- 高级："预订行程"\n- 你看到：设置上车/下车→选择车型→确认→跟踪司机\n- 隐藏：GPS算法、司机匹配系统、票价计算、支付处理、数据库更新\n\n**3. 在线购物（Lazada/Shopee）**\n- 高级："购买产品"\n- 你看到：浏览→加入购物车→结账→支付→跟踪配送\n- 隐藏：库存系统、推荐算法、支付网关、物流网络、卖家通知\n\n**编程中的抽象：**\n\n- **函数**：命名一组指令（例如，`calculate_gst(price)`隐藏公式）\n- **库**：使用复杂功能而不知道内部代码\n- **API**：与服务交互而看不到其实现"
            },
            {
                "id": "algorithms",
                "type": "text",
                "title": "Algorithms",
                "title_zh": "算法",
                "content": "**Algorithm** is a step-by-step procedure to solve a problem or complete a task.\n\n**Good algorithm characteristics:**\n\n1. **Clear**: Each step is unambiguous\n2. **Finite**: Has a definite end\n3. **Effective**: Each step is achievable\n4. **Input/Output**: Takes input, produces output\n5. **General**: Works for all valid inputs\n\n**Algorithm representations:**\n\n**1. Natural language** (everyday words)\n```\nAlgorithm: Make kaya toast\n1. Toast 2 slices of bread\n2. Spread butter on both slices\n3. Spread kaya on both slices\n4. Put slices together\n5. Cut diagonally\n```\n\n**2. Pseudocode** (structured English)\n```\nAlgorithm: Find maximum number in list\nINPUT: list of numbers\nOUTPUT: largest number\n\nmax = first number in list\nFOR each number in list:\n    IF number > max THEN:\n        max = number\nRETURN max\n```\n\n**3. Flowchart** (visual diagram with symbols)\n- Oval: Start/End\n- Rectangle: Process\n- Diamond: Decision\n- Arrow: Flow direction\n\n**Common algorithms in daily life:**\n\n**1. Recipe** (cooking algorithm)\n- Input: Ingredients\n- Steps: Preparation, cooking, plating\n- Output: Finished dish\n\n**2. Morning routine**\n- Wake up → Shower → Dress → Breakfast → Pack bag → Go to school\n\n**3. Bus route** (navigation algorithm)\n- Input: Start location, destination\n- Steps: Walk to bus stop → Board bus → Ride → Alight → Walk to destination\n- Output: Arrive at destination\n\n**4. EZ-Link card top-up**\n- Insert card → Select top-up amount → Insert cash/card → Wait for confirmation → Remove card\n\n**Singapore computing algorithms:**\n\n- **TraceTogether**: Bluetooth proximity detection + contact matching\n- **Singpass face verification**: Facial recognition + liveness detection\n- **GrabFood delivery**: Restaurant matching + driver allocation + route optimization\n- **HDB flat application**: Eligibility check + balloting + queue management",
                "content_zh": "**算法**是解决问题或完成任务的逐步过程。\n\n**好算法的特征：**\n\n1. **清晰**：每个步骤明确无误\n2. **有限**：有明确的结束\n3. **有效**：每个步骤可实现\n4. **输入/输出**：接受输入，产生输出\n5. **通用**：对所有有效输入都有效\n\n**算法表示：**\n\n**1. 自然语言**（日常用语）\n```\n算法：制作咖椰吐司\n1. 烤2片面包\n2. 在两片上涂黄油\n3. 在两片上涂咖椰\n4. 将两片合在一起\n5. 对角切开\n```\n\n**2. 伪代码**（结构化英语）\n```\n算法：在列表中查找最大数\n输入：数字列表\n输出：最大数字\n\nmax = 列表中的第一个数字\n对于列表中的每个数字：\n    如果数字 > max 那么：\n        max = 数字\n返回 max\n```\n\n**3. 流程图**（带符号的可视化图表）\n- 椭圆：开始/结束\n- 矩形：处理\n- 菱形：决策\n- 箭头：流向\n\n**日常生活中的常见算法：**\n\n**1. 食谱**（烹饪算法）\n- 输入：食材\n- 步骤：准备、烹饪、摆盘\n- 输出：完成的菜肴\n\n**2. 早晨例行公事**\n- 醒来→洗澡→穿衣→早餐→收拾书包→去学校\n\n**3. 公交路线**（导航算法）\n- 输入：起始位置、目的地\n- 步骤：走到公交站→上车→乘坐→下车→走到目的地\n- 输出：到达目的地\n\n**4. EZ-Link卡充值**\n- 插卡→选择充值金额→插入现金/卡→等待确认→取卡\n\n**新加坡计算算法：**\n\n- **TraceTogether**：蓝牙邻近检测+接触匹配\n- **Singpass面部验证**：面部识别+活体检测\n- **GrabFood配送**：餐厅匹配+司机分配+路线优化\n- **HDB公寓申请**：资格检查+抽签+队列管理"
            }
        ],
        "exercises": []  # Keep existing exercises
    }
]

# Save enhanced chapters
print("Creating enhanced Sec 3 Computing chapters...\n")

for chapter in enhanced_chapters[:2]:  # First 2 chapters for now
    filename = f"sec3-computing-{chapter['id']}.json"
    filepath = os.path.join(chapters_dir, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(chapter, f, ensure_ascii=False, indent=2)

    print(f"✓ Created: {chapter['title']} ({len(chapter['sections'])} sections)")
    print(f"  File: {filename}")

print("\n" + "="*60)
print("✅ Enhanced Sec 3 Computing chapters created!")
print("="*60)
print("\nNext: Create remaining 4 chapters and integrate all into content.json")
