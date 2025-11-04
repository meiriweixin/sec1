"""
Create Secondary 1 Computing chapters
Foundation level - introduces computing concepts before Sec 2
Aligned with Singapore MOE Computing syllabus for Sec 1
"""

import json

sec1_computing_chapters = [
    {
        "id": "digital-devices-sec1",
        "gradeLevel": "sec1",
        "title": "Digital Devices & Systems",
        "title_zh": "数字设备与系统",
        "description": "Computer hardware, input/output devices, and how computers work",
        "description_zh": "计算机硬件、输入输出设备以及计算机的工作原理",
        "tag": "Computer Fundamentals",
        "tag_zh": "计算机基础",
        "objectives": [
            "Identify computer hardware components",
            "Understand input and output devices",
            "Explain how computers process data",
            "Recognize different types of computing devices"
        ],
        "objectives_zh": [
            "识别计算机硬件组件",
            "了解输入和输出设备",
            "解释计算机如何处理数据",
            "识别不同类型的计算设备"
        ],
        "sections": [
            {
                "id": "computer-components",
                "type": "text",
                "title": "Main Computer Components",
                "title_zh": "计算机主要组件",
                "content": "CPU (Central Processing Unit) is the brain - processes instructions. RAM (Random Access Memory) is temporary storage - holds data while computer is on. Storage (Hard Drive/SSD) is permanent storage - saves files. Motherboard connects all components. Example: Singapore student doing homework - CPU processes calculations, RAM holds open documents, storage saves completed work."
            },
            {
                "id": "input-output-devices",
                "type": "text",
                "title": "Input & Output Devices",
                "title_zh": "输入输出设备",
                "content": "Input devices send data TO computer: Keyboard (text), Mouse (pointing), Microphone (sound), Camera (images/video), Scanner (documents). Output devices receive data FROM computer: Monitor (display), Printer (paper), Speakers (sound), Headphones (audio). Some devices are both: Touchscreen (input touch, output display), VR headset. Singapore schools use interactive whiteboards - both input and output."
            },
            {
                "id": "how-computers-work",
                "type": "text",
                "title": "How Computers Process Data",
                "title_zh": "计算机如何处理数据",
                "content": "Input-Process-Output cycle: 1) Input: User enters data (keyboard/mouse), 2) Process: CPU executes instructions using RAM, 3) Output: Results displayed or saved. Example: Singapore student searches online - Input: Type 'Singapore history', Process: Computer sends request to Google servers, retrieves results, Output: Display search results on screen. Everything happens in milliseconds!"
            },
            {
                "id": "types-of-devices",
                "type": "text",
                "title": "Types of Computing Devices",
                "title_zh": "计算设备类型",
                "content": "Desktop computers: Powerful, stationary, used at home/office. Laptops: Portable, built-in screen/keyboard. Tablets: Touchscreen, very portable (iPad, Samsung Tab). Smartphones: Pocket-sized, always connected. Servers: Powerful computers that provide services to many users. Embedded systems: Computers in other devices (car, washing machine, ATM). Singapore widely uses smartphones for payments, government services via Singpass app."
            }
        ],
        "exercises": []
    },

    {
        "id": "intro-algorithms-sec1",
        "gradeLevel": "sec1",
        "title": "Introduction to Algorithms",
        "title_zh": "算法入门",
        "description": "Understanding sequences, patterns, and step-by-step instructions",
        "description_zh": "理解序列、模式和分步指令",
        "tag": "Computational Thinking",
        "tag_zh": "计算思维",
        "objectives": [
            "Understand what an algorithm is",
            "Follow step-by-step instructions",
            "Identify patterns and sequences",
            "Solve simple problems systematically"
        ],
        "objectives_zh": [
            "理解什么是算法",
            "遵循分步指令",
            "识别模式和序列",
            "系统地解决简单问题"
        ],
        "sections": [
            {
                "id": "what-is-algorithm",
                "type": "text",
                "title": "What is an Algorithm?",
                "title_zh": "什么是算法？",
                "content": "Algorithm = step-by-step instructions to complete a task. Like a recipe for cooking! Example: Making Milo - 1) Boil water, 2) Put 3 spoons Milo in cup, 3) Pour hot water, 4) Stir, 5) Enjoy! Algorithms must be: Clear (no confusion), Ordered (correct sequence), Finite (must end). Singapore traffic lights use algorithms to control light changes based on traffic flow and time."
            },
            {
                "id": "sequences",
                "type": "text",
                "title": "Sequences & Patterns",
                "title_zh": "序列与模式",
                "content": "Sequence is ordered list: 2, 4, 6, 8 (adding 2 each time). Pattern is repeating design: Red, Blue, Red, Blue. Finding patterns helps solve problems faster. Example: Singapore bus numbers - 14, 14A, 14e follow pattern (same route, different stops). Number patterns: 5, 10, 15, 20 (multiply by 5). Understanding patterns is key to computational thinking."
            },
            {
                "id": "decomposition",
                "type": "text",
                "title": "Breaking Down Problems",
                "title_zh": "分解问题",
                "content": "Decomposition means breaking big problem into smaller parts. Example: Planning trip to Sentosa - Big problem: 'Get to Sentosa'. Smaller parts: 1) Check MRT route, 2) Take MRT to HarbourFront, 3) Board Sentosa Express, 4) Choose destination station. Each small part is easier to solve than the whole problem. Singapore school projects often use decomposition - divide work among team members."
            },
            {
                "id": "abstraction",
                "type": "text",
                "title": "Focus on What Matters",
                "title_zh": "关注重要内容",
                "content": "Abstraction means ignoring unnecessary details, focusing on important information. Example: Singapore MRT map - Shows stations and lines, but NOT exact distances or street names. That's abstraction - only essential info shown. When giving directions: 'Take Red Line to Orchard, then Green Line to Bugis' - abstract (simple). Not: 'Travel 2.3km northeast, turn at 103.8° heading...' - too detailed. Abstraction makes problems simpler."
            }
        ],
        "exercises": []
    },

    {
        "id": "block-programming-sec1",
        "gradeLevel": "sec1",
        "title": "Block-Based Programming",
        "title_zh": "积木式编程",
        "description": "Introduction to programming using visual blocks (Scratch/Blockly)",
        "description_zh": "使用可视化积木（Scratch/Blockly）介绍编程",
        "tag": "Programming",
        "tag_zh": "编程",
        "objectives": [
            "Create programs using visual blocks",
            "Understand sequence, selection, and repetition",
            "Debug simple programs",
            "Design interactive projects"
        ],
        "objectives_zh": [
            "使用可视化积木创建程序",
            "理解顺序、选择和重复",
            "调试简单程序",
            "设计交互式项目"
        ],
        "sections": [
            {
                "id": "block-programming-intro",
                "type": "text",
                "title": "What is Block Programming?",
                "title_zh": "什么是积木式编程？",
                "content": "Block programming uses colorful blocks instead of typing code. Snap blocks together like LEGO! Popular tools: Scratch (MIT), Blockly (Google), Code.org. Blocks include: Motion (move sprite), Looks (change appearance), Sound (play music), Events (when clicked), Control (if/repeat). Example: Make Singapore Merlion sprite move - 'When green flag clicked' + 'Move 10 steps' + 'Say Hello for 2 seconds'. No typing errors, focus on logic!"
            },
            {
                "id": "sequence-blocks",
                "type": "text",
                "title": "Sequence - Order Matters",
                "title_zh": "顺序 - 顺序很重要",
                "content": "Sequence = blocks run in order from top to bottom. Example: Singapore flag animation - 1) Set background to red, 2) Draw white crescent, 3) Draw 5 stars, 4) Play national anthem. If order wrong (anthem before drawing), looks strange! Programs execute one instruction at a time, in sequence. Practice: Create program to introduce yourself - 1) Say name, 2) Show age, 3) Say school, 4) Say hobby."
            },
            {
                "id": "loops-repetition",
                "type": "text",
                "title": "Loops - Repetition",
                "title_zh": "循环 - 重复",
                "content": "Loops repeat actions. 'Repeat 10' block runs code 10 times. 'Forever' loop runs continuously. Example: Draw square - Repeat 4 times: Move 50 steps, Turn 90 degrees. Without loop, need to write same code 4 times! Singapore EZ-Link card tapping - Loop checks: While balance > 0, allow entry. 'Repeat until' loops until condition is true. Use loops to avoid repetitive code."
            },
            {
                "id": "conditions-selection",
                "type": "text",
                "title": "If-Then - Making Decisions",
                "title_zh": "If-Then - 做决定",
                "content": "If-Then blocks make decisions. Structure: 'If condition Then action'. Example: Singapore weather program - 'If temperature > 30, Say Very Hot!, Else Say Pleasant'. Conditions use comparisons: = (equal), > (greater), < (less). Combination: 'If raining AND temperature < 25, Say Cold rain'. Singapore school attendance - 'If student present, Mark attendance, Else Send absence alert'. Computers make millions of if-then decisions per second."
            }
        ],
        "exercises": []
    },

    {
        "id": "digital-data-sec1",
        "gradeLevel": "sec1",
        "title": "Digital Data & Files",
        "title_zh": "数字数据与文件",
        "description": "Understanding how computers store and organize data",
        "description_zh": "理解计算机如何存储和组织数据",
        "tag": "Data & Information",
        "tag_zh": "数据与信息",
        "objectives": [
            "Understand binary basics",
            "Recognize different file types",
            "Organize files and folders",
            "Understand file sizes and storage"
        ],
        "objectives_zh": [
            "理解二进制基础",
            "识别不同文件类型",
            "组织文件和文件夹",
            "理解文件大小和存储"
        ],
        "sections": [
            {
                "id": "binary-basics",
                "type": "text",
                "title": "Binary - Computer Language",
                "title_zh": "二进制 - 计算机语言",
                "content": "Computers only understand 0 and 1 (binary). Why? Electronics work with ON (1) or OFF (0). Bit = one binary digit (0 or 1). Byte = 8 bits. Example: Letter 'A' = 01000001 in binary. Numbers: 0=0, 1=1, 2=10, 3=11, 4=100. Everything in computer (text, images, videos, music) is stored as 0s and 1s! Singapore NRIC contains letters and numbers - all converted to binary for storage."
            },
            {
                "id": "file-types",
                "type": "text",
                "title": "Common File Types",
                "title_zh": "常见文件类型",
                "content": "Files have extensions showing type. Documents: .docx (Word), .pdf (Adobe), .txt (plain text). Images: .jpg/.jpeg (photos), .png (graphics with transparency), .gif (animations). Videos: .mp4, .avi, .mov. Audio: .mp3, .wav. Programs: .exe (Windows). Compressed: .zip (multiple files). Singapore government forms often in .pdf format. Each type needs specific program to open - can't open .docx with media player!"
            },
            {
                "id": "file-organization",
                "type": "text",
                "title": "Files & Folders",
                "title_zh": "文件与文件夹",
                "content": "Folders (directories) organize files. Like filing cabinet! Good structure: School/ → Math/, Science/, English/ → each has assignments/. Path shows location: C:/Users/Student/Documents/School/Math/Homework.docx. Root folder is top level (C: on Windows). Use meaningful names: 'Math_Homework_Week5.docx' not 'untitled123.docx'. Singapore students organize by subject and term for easy retrieval. Backup important files to cloud (Google Drive, OneDrive) or external drive."
            },
            {
                "id": "storage-sizes",
                "type": "text",
                "title": "File Sizes & Storage",
                "title_zh": "文件大小与存储",
                "content": "Storage measured in bytes: Byte < KB (1000 bytes) < MB (1000 KB) < GB (1000 MB) < TB (1000 GB). Text file: ~10 KB. Photo: ~5 MB. Song: ~5 MB. Movie: ~2 GB. Typical phone: 64-256 GB storage. Cloud storage: Google Drive 15 GB free. Large files take longer to transfer. Singapore students submit assignments online - check file size limits (often 10-25 MB). Compress large files to .zip to reduce size."
            }
        ],
        "exercises": []
    },

    {
        "id": "internet-safety-sec1",
        "gradeLevel": "sec1",
        "title": "Internet & Online Safety",
        "title_zh": "互联网与在线安全",
        "description": "How the internet works and staying safe online",
        "description_zh": "互联网如何工作以及在线安全",
        "tag": "Networks & Safety",
        "tag_zh": "网络与安全",
        "objectives": [
            "Understand how the internet works",
            "Practice safe online behavior",
            "Identify online threats",
            "Protect personal information"
        ],
        "objectives_zh": [
            "理解互联网如何工作",
            "实践安全的在线行为",
            "识别在线威胁",
            "保护个人信息"
        ],
        "sections": [
            {
                "id": "how-internet-works",
                "type": "text",
                "title": "How the Internet Works",
                "title_zh": "互联网如何工作",
                "content": "Internet = worldwide network of connected computers. When you visit website: 1) Type URL (www.moe.gov.sg), 2) Computer sends request through router, 3) Request travels through many routers worldwide, 4) Reaches web server, 5) Server sends webpage back to you. All in milliseconds! IP address is computer's location (like postal code). DNS translates website names to IP addresses. Singapore has excellent internet infrastructure - fast fiber broadband connections."
            },
            {
                "id": "online-safety",
                "type": "text",
                "title": "Staying Safe Online",
                "title_zh": "在线保持安全",
                "content": "Online safety rules: 1) Never share passwords, 2) Don't give personal info (NRIC, address, phone) to strangers, 3) Think before posting - internet is permanent, 4) Tell adult if something uncomfortable, 5) Use privacy settings on social media. Strong passwords: 8+ characters, mix letters/numbers/symbols, different for each site. Example: 'S1ng@p0re#2024' (but don't use this - make your own!). Singapore Cyber Security Agency (CSA) provides safety resources."
            },
            {
                "id": "online-threats",
                "type": "text",
                "title": "Common Online Threats",
                "title_zh": "常见在线威胁",
                "content": "Cyberbullying: Mean messages, spreading rumors online - report to adults/teachers. Phishing: Fake emails/messages trying to steal passwords - don't click suspicious links. Malware/Viruses: Harmful software - use antivirus, don't download from untrusted sources. Scams: Too-good-to-be-true offers - 'Win free iPhone!' likely fake. Identity theft: Someone pretends to be you - protect personal info. Singapore Police Force website (scamalert.sg) lists current scams to watch for."
            },
            {
                "id": "digital-footprint",
                "type": "text",
                "title": "Your Digital Footprint",
                "title_zh": "你的数字足迹",
                "content": "Digital footprint = trail of data you leave online. Everything you post, like, share stays online - maybe forever! Future employers, schools can search your name. Tips: 1) Google yourself - see what others find, 2) Set social media to private, 3) Don't post anything embarrassing, 4) Be kind online - messages can be screenshot, 5) Think: Would I want teachers/parents to see this? Singapore schools emphasize positive digital citizenship. Remember: 'What happens online, stays online.'"
            }
        ],
        "exercises": []
    },

    {
        "id": "productivity-tools-sec1",
        "gradeLevel": "sec1",
        "title": "Digital Productivity Tools",
        "title_zh": "数字生产力工具",
        "description": "Using word processors, presentations, and collaboration tools",
        "description_zh": "使用文字处理器、演示文稿和协作工具",
        "tag": "Digital Tools",
        "tag_zh": "数字工具",
        "objectives": [
            "Create documents and presentations",
            "Use spreadsheets for simple calculations",
            "Collaborate using cloud tools",
            "Present information effectively"
        ],
        "objectives_zh": [
            "创建文档和演示文稿",
            "使用电子表格进行简单计算",
            "使用云工具协作",
            "有效呈现信息"
        ],
        "sections": [
            {
                "id": "word-processing",
                "type": "text",
                "title": "Word Processing",
                "title_zh": "文字处理",
                "content": "Word processors create documents: Microsoft Word, Google Docs, Pages. Features: Font styles (bold, italic, underline), Headings (Title, Heading 1, 2), Lists (bullets, numbers), Images, Tables, Spell check. Formatting tips: Use consistent fonts, Clear headings for sections, Align text (left/center/right), Save frequently! Singapore students use Google Docs for group assignments - multiple people edit simultaneously. Export to PDF for submitting assignments."
            },
            {
                "id": "presentations",
                "type": "text",
                "title": "Creating Presentations",
                "title_zh": "创建演示文稿",
                "content": "Presentation software: PowerPoint, Google Slides, Keynote. Each slide = one idea. Good presentations: 1) Clear title on each slide, 2) Large text (not tiny!), 3) Few words (use images), 4) Consistent colors/fonts, 5) Animations sparingly. 6-6 rule: Max 6 lines per slide, 6 words per line. Singapore students present projects using slides. Practice speaking skills - don't just read slides! Engage audience with questions, videos, demos."
            },
            {
                "id": "spreadsheets-basics",
                "type": "text",
                "title": "Introduction to Spreadsheets",
                "title_zh": "电子表格入门",
                "content": "Spreadsheets organize data in rows and columns: Excel, Google Sheets. Cell = one box (A1, B2, C3). Enter data or formulas. Simple formulas: =A1+A2 (addition), =SUM(A1:A10) (add range), =AVERAGE(B1:B5). Example: Track pocket money - Column A: Date, Column B: Amount received, Column C: Amount spent, Column D: Balance (=B-C). Singapore students use for budgeting, science data recording, math calculations. Charts visualize data (bar, pie, line graphs)."
            },
            {
                "id": "collaboration-tools",
                "type": "text",
                "title": "Collaborating Online",
                "title_zh": "在线协作",
                "content": "Cloud tools enable teamwork: Google Workspace (Docs, Sheets, Slides), Microsoft 365, Zoom, Google Meet. Share documents - multiple people edit simultaneously. See who's editing in real-time. Comment/suggest features for feedback. Video calls for group discussions. Singapore schools use Google Classroom and Microsoft Teams for online learning. Best practices: 1) Communicate clearly, 2) Respect others' ideas, 3) Complete your part on time, 4) Check spelling/grammar before sharing, 5) Use appropriate language and tone."
            }
        ],
        "exercises": []
    }
]

print(f"📚 Creating {len(sec1_computing_chapters)} Secondary 1 Computing chapters...")
print(f"   Computer Fundamentals: {sum(1 for ch in sec1_computing_chapters if ch['tag'] == 'Computer Fundamentals')}")
print(f"   Computational Thinking: {sum(1 for ch in sec1_computing_chapters if ch['tag'] == 'Computational Thinking')}")
print(f"   Programming: {sum(1 for ch in sec1_computing_chapters if ch['tag'] == 'Programming')}")
print(f"   Data & Information: {sum(1 for ch in sec1_computing_chapters if ch['tag'] == 'Data & Information')}")
print(f"   Networks & Safety: {sum(1 for ch in sec1_computing_chapters if ch['tag'] == 'Networks & Safety')}")
print(f"   Digital Tools: {sum(1 for ch in sec1_computing_chapters if ch['tag'] == 'Digital Tools')}")

# Save
with open('chapters/computing-sec1-chapters.json', 'w', encoding='utf-8') as f:
    json.dump(sec1_computing_chapters, f, indent=2, ensure_ascii=False)

print(f"\n✅ Created {len(sec1_computing_chapters)} chapters")
print(f"📁 Saved to: chapters/computing-sec1-chapters.json")
print(f"\n⚠️ Note: Exercises need to be added separately")
