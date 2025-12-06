#!/usr/bin/env python3
"""Add A-Level Exam Prep chapters for GP, Biology, and Economics."""
import json
from datetime import datetime

# A-Level GP Exam Prep
GP_ALEVEL_CHAPTERS = [
    {
        "id": "alevel-gp-paper1-prep",
        "title": "A-Level GP Paper 1: Essay",
        "title_zh": "A水准GP试卷一：论文",
        "gradeLevel": "alevel",
        "description": "Master essay writing for A-Level General Paper",
        "description_zh": "掌握A水准通识论文写作",
        "objectives": ["Write sophisticated argumentative essays", "Manage time effectively", "Demonstrate critical thinking"],
        "objectives_zh": ["写出复杂的议论文", "有效管理时间", "展示批判性思维"],
        "sections": [
            {"id": "gp-p1-1", "type": "text", "title": "Paper 1 Overview", "title_zh": "试卷一概述",
             "content": "**A-Level GP Paper 1 (1.5 hours):**\n\n- Choose 1 from 12 questions\n- Write 500-800 words\n- Worth 50% of GP grade\n\n**Question types:**\n1. Discuss/To what extent\n2. Evaluate/Assess\n3. Compare/Contrast\n4. Cause and effect\n5. Problem-solution"},
            {"id": "gp-p1-2", "type": "text", "title": "Essay Structure", "title_zh": "论文结构",
             "content": "**Winning structure:**\n\n**Introduction (10%):**\n- Hook/context\n- Define key terms\n- Clear thesis\n\n**Body paragraphs (75%):**\n- PEEL structure\n- 3-4 well-developed arguments\n- Address counterarguments\n\n**Conclusion (15%):**\n- Restate thesis\n- Synthesize arguments\n- Wider implications"},
            {"id": "gp-p1-3", "type": "text", "title": "Exam Strategies", "title_zh": "考试策略",
             "content": "**Time allocation:**\n- 5 min: Choose question, brainstorm\n- 10 min: Plan essay structure\n- 65 min: Write essay\n- 10 min: Proofread\n\n**Tips:**\n- Answer the question directly\n- Use specific examples\n- Show nuanced thinking\n- Avoid clichés and generalizations"}
        ],
        "exercises": []
    },
    {
        "id": "alevel-gp-paper2-prep",
        "title": "A-Level GP Paper 2: Comprehension",
        "title_zh": "A水准GP试卷二：理解",
        "gradeLevel": "alevel",
        "description": "Master comprehension and AQ for A-Level GP",
        "description_zh": "掌握A水准GP理解和应用题",
        "objectives": ["Answer comprehension questions accurately", "Write effective summaries", "Excel at Application Question"],
        "objectives_zh": ["准确回答理解问题", "写有效摘要", "擅长应用题"],
        "sections": [
            {"id": "gp-p2-1", "type": "text", "title": "Paper 2 Overview", "title_zh": "试卷二概述",
             "content": "**A-Level GP Paper 2 (1.5 hours):**\n\n- 2 passages on related theme\n- Short answer questions (25 marks)\n- Summary (8 marks)\n- Application Question (10 marks)\n- Total: 50% of GP grade"},
            {"id": "gp-p2-2", "type": "text", "title": "Question Types", "title_zh": "题型",
             "content": "**Types of questions:**\n\n1. **Literal**: Find information directly\n2. **Inference**: Read between the lines\n3. **Vocabulary in context**: Word meanings\n4. **Language use**: Analyze effects\n5. **Comparison**: Between passages\n6. **Summary**: Condense key points\n7. **AQ**: Apply and evaluate"},
            {"id": "gp-p2-3", "type": "text", "title": "AQ Strategy", "title_zh": "应用题策略",
             "content": "**Application Question (10 marks):**\n\n**Structure:**\n1. Address the requirement (2 marks)\n2. Reference Passage A (2-3 marks)\n3. Reference Passage B (2-3 marks)\n4. Own examples (2-3 marks)\n5. Evaluation/conclusion (1-2 marks)\n\n**Key:** Balance passage references with own knowledge"}
        ],
        "exercises": []
    },
    {
        "id": "alevel-gp-exam-strategies",
        "title": "A-Level GP: Exam Strategies",
        "title_zh": "A水准GP：考试策略",
        "gradeLevel": "alevel",
        "description": "Comprehensive strategies for A-Level GP success",
        "description_zh": "A水准GP成功的综合策略",
        "objectives": ["Prepare effectively for GP exams", "Avoid common mistakes", "Maximize marks"],
        "objectives_zh": ["有效准备GP考试", "避免常见错误", "最大化分数"],
        "sections": [
            {"id": "gp-strat-1", "type": "text", "title": "Common Mistakes", "title_zh": "常见错误",
             "content": "**Paper 1 mistakes:**\n- Not answering the question\n- Weak/no examples\n- Poor structure\n- Running out of time\n- Oversimplification\n\n**Paper 2 mistakes:**\n- Lifting from passage\n- Missing AQ requirements\n- Exceeding word limits\n- Incomplete answers"},
            {"id": "gp-strat-2", "type": "text", "title": "Building Content", "title_zh": "建立内容",
             "content": "**Example bank topics:**\n\n- Science & Technology\n- Environment\n- Politics & Governance\n- Arts & Culture\n- Society & Ethics\n- Media & Communication\n\n**Sources:**\n- The Straits Times\n- CNA\n- The Economist\n- BBC, Guardian"},
            {"id": "gp-strat-3", "type": "text", "title": "Final Preparation", "title_zh": "最后准备",
             "content": "**Last week before exam:**\n\n1. Review essay outlines\n2. Update example bank\n3. Practice timed essays\n4. Review vocabulary\n5. Rest well before exam\n\n**On exam day:**\n- Read questions carefully\n- Plan before writing\n- Budget time strictly\n- Check your work"}
        ],
        "exercises": []
    }
]

# A-Level Biology Exam Prep
BIOLOGY_ALEVEL_CHAPTERS = [
    {
        "id": "alevel-biology-paper1-prep",
        "title": "A-Level H2 Biology Paper 1: MCQ",
        "title_zh": "A水准H2生物试卷一：选择题",
        "gradeLevel": "alevel",
        "description": "Multiple choice strategies for H2 Biology",
        "description_zh": "H2生物选择题策略",
        "objectives": ["Master MCQ techniques", "Understand common question patterns", "Avoid common traps"],
        "objectives_zh": ["掌握选择题技巧", "理解常见题型", "避免常见陷阱"],
        "sections": [
            {"id": "bio-p1-1", "type": "text", "title": "Paper 1 Overview", "title_zh": "试卷一概述",
             "content": "**H2 Biology Paper 1:**\n- 30 MCQ questions\n- 1 hour duration\n- 30 marks (15% of total)\n\n**Topics covered:**\n- Cell biology\n- Molecular biology\n- Genetics\n- Physiology\n- Ecology & Evolution"},
            {"id": "bio-p1-2", "type": "text", "title": "MCQ Strategies", "title_zh": "选择题策略",
             "content": "**Approach:**\n1. Read stem carefully\n2. Identify key terms\n3. Eliminate wrong options\n4. Choose best answer\n\n**Time management:**\n- 2 minutes per question\n- Flag difficult questions\n- Return to flagged questions"},
            {"id": "bio-p1-3", "type": "text", "title": "Common Topics", "title_zh": "常见主题",
             "content": "**High-frequency topics:**\n\n- Cell membrane transport\n- Enzyme kinetics\n- DNA replication/transcription\n- Genetic crosses\n- Photosynthesis/respiration\n- Nervous/hormonal control\n- Immunity\n- Evolution mechanisms"}
        ],
        "exercises": []
    },
    {
        "id": "alevel-biology-paper2-prep",
        "title": "A-Level H2 Biology Paper 2: Structured",
        "title_zh": "A水准H2生物试卷二：结构题",
        "gradeLevel": "alevel",
        "description": "Structured question techniques for H2 Biology",
        "description_zh": "H2生物结构题技巧",
        "objectives": ["Answer structured questions effectively", "Interpret data and diagrams", "Write clear explanations"],
        "objectives_zh": ["有效回答结构题", "解读数据和图表", "写清晰的解释"],
        "sections": [
            {"id": "bio-p2-1", "type": "text", "title": "Paper 2 Overview", "title_zh": "试卷二概述",
             "content": "**H2 Biology Paper 2:**\n- Structured questions\n- 2 hours duration\n- 100 marks (40% of total)\n\n**Question types:**\n- Data analysis\n- Diagram interpretation\n- Explain/describe\n- Compare/contrast"},
            {"id": "bio-p2-2", "type": "text", "title": "Answering Techniques", "title_zh": "答题技巧",
             "content": "**Key skills:**\n\n1. **Read mark allocation** - 1 mark ≈ 1 point\n2. **Use scientific terminology** accurately\n3. **Be specific** - avoid vague answers\n4. **Structure answers** logically\n5. **Answer what is asked** - compare means both similarities and differences"},
            {"id": "bio-p2-3", "type": "text", "title": "Data Analysis", "title_zh": "数据分析",
             "content": "**Analyzing graphs/tables:**\n\n1. Identify variables (independent, dependent)\n2. Describe trends with data\n3. Quote specific values\n4. Explain biological significance\n5. Note anomalies if present"}
        ],
        "exercises": []
    },
    {
        "id": "alevel-biology-paper3-prep",
        "title": "A-Level H2 Biology Paper 3: Free Response",
        "title_zh": "A水准H2生物试卷三：自由作答",
        "gradeLevel": "alevel",
        "description": "Long answer and planning questions for H2 Biology",
        "description_zh": "H2生物长答题和计划题",
        "objectives": ["Write comprehensive essay answers", "Design experiments", "Apply biological concepts"],
        "objectives_zh": ["写全面的论文答案", "设计实验", "应用生物概念"],
        "sections": [
            {"id": "bio-p3-1", "type": "text", "title": "Paper 3 Overview", "title_zh": "试卷三概述",
             "content": "**H2 Biology Paper 3:**\n- Section A: Structured (60 marks)\n- Section B: Essay (25 marks)\n- 2 hours duration\n- 85 marks (45% of total)"},
            {"id": "bio-p3-2", "type": "text", "title": "Essay Writing", "title_zh": "论文写作",
             "content": "**Essay structure:**\n\n1. **Introduction**: Define key terms, outline scope\n2. **Body**: Organized paragraphs with examples\n3. **Conclusion**: Summarize key points\n\n**Tips:**\n- Use diagrams where relevant\n- Include specific examples\n- Show depth of understanding"},
            {"id": "bio-p3-3", "type": "text", "title": "Experimental Design", "title_zh": "实验设计",
             "content": "**Planning experiments:**\n\n1. State hypothesis\n2. Identify variables (IV, DV, controlled)\n3. Describe method step-by-step\n4. Explain controls\n5. Describe measurements\n6. Consider reliability/validity"}
        ],
        "exercises": []
    }
]

# A-Level Economics Exam Prep
ECON_ALEVEL_CHAPTERS = [
    {
        "id": "alevel-econ-paper1-prep",
        "title": "A-Level H2 Econ Paper 1: Case Study",
        "title_zh": "A水准H2经济试卷一：案例研究",
        "gradeLevel": "alevel",
        "description": "Case study analysis for H2 Economics",
        "description_zh": "H2经济案例研究分析",
        "objectives": ["Analyze economic case studies", "Apply concepts to real data", "Write effective responses"],
        "objectives_zh": ["分析经济案例研究", "将概念应用于真实数据", "写有效回答"],
        "sections": [
            {"id": "econ-p1-1", "type": "text", "title": "Paper 1 Overview", "title_zh": "试卷一概述",
             "content": "**H2 Economics Paper 1:**\n- 2 case studies\n- 2 hours 15 minutes\n- 60 marks (40% of total)\n\n**Each case study:**\n- Real-world economic data\n- Multiple questions (a to e/f)\n- Mix of explain, analyze, discuss"},
            {"id": "econ-p1-2", "type": "text", "title": "Question Types", "title_zh": "题型",
             "content": "**Types of questions:**\n\n1. **Explain** (4-6 marks): Define and elaborate\n2. **Analyze** (6-8 marks): Use diagrams, cause-effect\n3. **Discuss/Evaluate** (8-10 marks): Arguments for/against, judgment\n\n**Use the data!** Reference figures, trends, changes"},
            {"id": "econ-p1-3", "type": "text", "title": "Diagram Skills", "title_zh": "图表技能",
             "content": "**Essential diagrams:**\n\n- Demand and supply curves\n- PPC (Production Possibilities Curve)\n- Cost curves (AC, MC)\n- AD-AS model\n- Market structures (PC, monopoly, etc.)\n\n**Always:**\n- Label axes\n- Show shifts with arrows\n- Explain diagram in words"}
        ],
        "exercises": []
    },
    {
        "id": "alevel-econ-paper2-prep",
        "title": "A-Level H2 Econ Paper 2: Essays",
        "title_zh": "A水准H2经济试卷二：论文",
        "gradeLevel": "alevel",
        "description": "Essay writing for H2 Economics",
        "description_zh": "H2经济论文写作",
        "objectives": ["Write structured economics essays", "Develop balanced arguments", "Apply economic analysis"],
        "objectives_zh": ["写结构化的经济论文", "发展平衡的论点", "应用经济分析"],
        "sections": [
            {"id": "econ-p2-1", "type": "text", "title": "Paper 2 Overview", "title_zh": "试卷二概述",
             "content": "**H2 Economics Paper 2:**\n- 3 essays from 6 questions\n- 2 hours 15 minutes\n- 75 marks (60% of total)\n- 25 marks per essay"},
            {"id": "econ-p2-2", "type": "text", "title": "Essay Structure", "title_zh": "论文结构",
             "content": "**25-mark essay structure:**\n\n**Introduction (2-3 marks)**\n- Define key terms\n- State thesis\n\n**Body (18-20 marks)**\n- 3-4 well-developed arguments\n- Use diagrams\n- Singapore examples\n- Counter-arguments\n\n**Conclusion (2-3 marks)**\n- Summarize\n- Make judgment\n- Qualify if needed"},
            {"id": "econ-p2-3", "type": "text", "title": "Evaluation Skills", "title_zh": "评价技能",
             "content": "**How to evaluate:**\n\n1. Consider different perspectives\n2. Weigh costs vs benefits\n3. Short-run vs long-run\n4. Different stakeholders\n5. Singapore context\n6. Make justified judgment\n\n**Signal words:**\n- 'However...'\n- 'On the other hand...'\n- 'The extent depends on...'"}
        ],
        "exercises": []
    },
    {
        "id": "alevel-econ-exam-strategies",
        "title": "A-Level H2 Econ: Exam Strategies",
        "title_zh": "A水准H2经济：考试策略",
        "gradeLevel": "alevel",
        "description": "Comprehensive strategies for H2 Economics success",
        "description_zh": "H2经济成功的综合策略",
        "objectives": ["Prepare effectively for economics exams", "Manage time in exams", "Maximize marks"],
        "objectives_zh": ["有效准备经济考试", "考试时间管理", "最大化分数"],
        "sections": [
            {"id": "econ-strat-1", "type": "text", "title": "Time Management", "title_zh": "时间管理",
             "content": "**Paper 1 (2h 15min):**\n- Case Study 1: 1 hour\n- Case Study 2: 1 hour\n- Review: 15 min\n\n**Paper 2 (2h 15min):**\n- 45 min per essay\n- Include planning time\n- Leave 5 min for review"},
            {"id": "econ-strat-2", "type": "text", "title": "Common Mistakes", "title_zh": "常见错误",
             "content": "**Avoid these errors:**\n\n1. Not using data in CSQ\n2. Missing diagrams\n3. One-sided arguments\n4. Not answering the question\n5. Poor time allocation\n6. Forgetting Singapore context\n7. Superficial evaluation"},
            {"id": "econ-strat-3", "type": "text", "title": "Revision Tips", "title_zh": "复习建议",
             "content": "**Effective revision:**\n\n1. Practice past papers under timed conditions\n2. Learn key diagrams by heart\n3. Build example bank (Singapore focus)\n4. Understand policy trade-offs\n5. Review mark schemes\n6. Get feedback on practice essays"}
        ],
        "exercises": []
    }
]

def generate_exam_exercises(chapter_id, topic, count=15):
    """Generate exam prep exercises."""
    exercises = []
    diffs = ['easy'] * 5 + ['medium'] * 5 + ['hard'] * 5
    
    templates = [
        (f"What is the recommended approach for {topic} questions?", ["Structured approach with evidence", "Random guessing", "Skip difficult parts", "Copy from notes"], 0),
        (f"In {topic}, what should you do first?", ["Read and understand the question", "Start writing immediately", "Look at other questions", "Panic"], 0),
        (f"How should you allocate time for {topic}?", ["Based on marks allocation", "Equal time for all", "More time for favorites", "No planning needed"], 0),
        (f"What is a common mistake in {topic}?", ["Not answering the question directly", "Writing too much", "Using diagrams", "Giving examples"], 0),
        (f"For {topic}, what demonstrates critical thinking?", ["Analyzing multiple perspectives", "Giving one opinion", "Copying definitions", "Writing longer answers"], 0),
    ]
    
    for i in range(count):
        template = templates[i % len(templates)]
        exercises.append({
            "id": f"{chapter_id}-ex{i+1}",
            "type": "mcq",
            "difficulty": diffs[i],
            "prompt": template[0],
            "prompt_zh": f"中文: {template[0]}",
            "choices": template[1],
            "choices_zh": template[1],
            "answer": template[2],
            "explanation": f"Key exam strategy for {topic}."
        })
    return exercises

def main():
    print("=" * 70)
    print("Adding A-Level Exam Prep for GP, Biology, Economics")
    print("=" * 70)
    
    with open('src/data/content.json', 'r', encoding='utf-8') as f:
        content = json.load(f)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = f'src/data/content-backup-alevel-{timestamp}.json'
    with open(backup_path, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    print(f"Created backup: {backup_path}")
    
    subjects_map = {s['id']: s for s in content['subjects']}
    
    # Add GP A-Level chapters
    print("\nAdding GP A-Level Exam Prep...")
    if 'gp' in subjects_map:
        for ch in GP_ALEVEL_CHAPTERS:
            ch['exercises'] = generate_exam_exercises(ch['id'], ch['title'])
            subjects_map['gp']['chapters'].append(ch)
            print(f"   Added: {ch['title']}")
    
    # Add Biology A-Level chapters
    print("\nAdding Biology A-Level Exam Prep...")
    if 'biology-jc' in subjects_map:
        for ch in BIOLOGY_ALEVEL_CHAPTERS:
            ch['exercises'] = generate_exam_exercises(ch['id'], ch['title'])
            subjects_map['biology-jc']['chapters'].append(ch)
            print(f"   Added: {ch['title']}")
    
    # Add Economics A-Level chapters
    print("\nAdding Economics A-Level Exam Prep...")
    if 'economics-jc' in subjects_map:
        for ch in ECON_ALEVEL_CHAPTERS:
            ch['exercises'] = generate_exam_exercises(ch['id'], ch['title'])
            subjects_map['economics-jc']['chapters'].append(ch)
            print(f"   Added: {ch['title']}")
    
    with open('src/data/content.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    
    print("\n" + "=" * 70)
    print("COMPLETE!")
    print("=" * 70)
    print("\nAdded A-Level Exam Prep:")
    print("  - 3 GP chapters (Paper 1 Essay, Paper 2 Comprehension, Strategies)")
    print("  - 3 Biology chapters (Paper 1 MCQ, Paper 2 Structured, Paper 3 Free Response)")
    print("  - 3 Economics chapters (Paper 1 Case Study, Paper 2 Essays, Strategies)")

if __name__ == "__main__":
    main()

