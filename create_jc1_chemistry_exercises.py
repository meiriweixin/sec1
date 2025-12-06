#!/usr/bin/env python3
"""
Generate exercises for JC1 Chemistry (H2 Level)
15 exercises per chapter × 8 chapters = 120 exercises total
Difficulty: 5 easy, 5 medium, 5 hard per chapter
"""
import json

# Exercise distribution: 5 easy + 5 medium + 5 hard = 15 per chapter

jc1_chemistry_exercises = {
    "atomic-structure-jc1-chem": [
        # Easy (5)
        {
            "id": "atom-struct-ex1",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "The electronic configuration of sodium (Na, Z=11) is:",
            "prompt_zh": "钠（Na，Z=11）的电子构型是：",
            "choices": ["1s² 2s² 2p⁶ 3s¹", "1s² 2s² 2p⁶ 3p¹", "1s² 2s² 2p⁵ 3s²", "1s² 2s² 2p⁶"],
            "choices_zh": ["1s² 2s² 2p⁶ 3s¹", "1s² 2s² 2p⁶ 3p¹", "1s² 2s² 2p⁵ 3s²", "1s² 2s² 2p⁶"],
            "answer": 0,
            "explanation": "**Problem:** Write electronic configuration for sodium (Z=11).\n\n**Key Concept:** Aufbau principle—electrons fill orbitals from lowest to highest energy: 1s < 2s < 2p < 3s.\n\n**Steps:**\n1. Total electrons = 11\n2. Fill orbitals: 1s² (2) + 2s² (4) + 2p⁶ (10) + 3s¹ (11)\n3. Configuration: 1s² 2s² 2p⁶ 3s¹\n\n**Answer:** 1s² 2s² 2p⁶ 3s¹\n\n**Common Mistakes:** Filling 3p before 3s (violates energy order).\n\n**Tip:** Remember s orbitals fill before p orbitals at the same energy level.",
            "explanation_zh": "**问题：** 写出钠（Z=11）的电子构型。\n\n**关键概念：** 构建原理—电子从低到高能级填充轨道：1s < 2s < 2p < 3s。\n\n**步骤：**\n1. 总电子数 = 11\n2. 填充轨道：1s² (2) + 2s² (4) + 2p⁶ (10) + 3s¹ (11)\n3. 构型：1s² 2s² 2p⁶ 3s¹\n\n**答案：** 1s² 2s² 2p⁶ 3s¹\n\n**常见错误：** 在3s之前填充3p（违反能级顺序）。\n\n**提示：** 记住在同一能级上s轨道先于p轨道填充。"
        },
        {
            "id": "atom-struct-ex2",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "Which element has the highest first ionization energy?",
            "prompt_zh": "哪个元素的第一电离能最高？",
            "choices": ["Li", "Na", "K", "He"],
            "choices_zh": ["Li", "Na", "K", "He"],
            "answer": 3,
            "explanation": "**Problem:** Compare first ionization energies of Li, Na, K, and He.\n\n**Key Concept:** Ionization energy increases across a period and decreases down a group. Noble gases have highest IE.\n\n**Steps:**\n1. He is a noble gas (Group 18) with complete shell\n2. Li, Na, K are Group 1 with one valence electron\n3. Smaller atoms (He) have higher IE than larger atoms (K)\n4. He has highest IE of all elements\n\n**Answer:** He (2372 kJ/mol)\n\n**Common Mistakes:** Choosing Li because it's smallest alkali metal (but He is smaller).\n\n**Tip:** Noble gases always have highest IE in their period due to stable electron configuration.",
            "explanation_zh": "**问题：** 比较Li、Na、K和He的第一电离能。\n\n**关键概念：** 电离能沿周期增加，沿族减小。稀有气体具有最高IE。\n\n**步骤：**\n1. He是稀有气体（第18族）具有完整电子壳层\n2. Li、Na、K是第1族具有一个价电子\n3. 较小原子（He）比较大原子（K）具有更高IE\n4. He具有所有元素中最高的IE\n\n**答案：** He（2372 kJ/mol）\n\n**常见错误：** 选择Li因为它是最小的碱金属（但He更小）。\n\n**提示：** 稀有气体由于稳定的电子构型在其周期中总是具有最高IE。"
        },
        {
            "id": "atom-struct-ex3",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "Atomic radius generally increases when moving:",
            "prompt_zh": "原子半径通常在以下情况下增加：",
            "choices": ["Across a period from left to right", "Down a group", "From metals to non-metals", "Towards noble gases"],
            "choices_zh": ["沿周期从左到右", "沿族向下", "从金属到非金属", "向稀有气体"],
            "answer": 1,
            "explanation": "**Problem:** Identify trend for increasing atomic radius.\n\n**Key Concept:** Atomic radius increases down a group (more shells) and decreases across a period (higher nuclear charge).\n\n**Steps:**\n1. Down group: Additional electron shells → larger radius\n2. Across period: Same shells but more protons → stronger pull → smaller radius\n3. Example: Li (152 pm) < Na (186 pm) < K (227 pm)\n\n**Answer:** Down a group\n\n**Common Mistakes:** Confusing with ionization energy trend (opposite direction).\n\n**Tip:** More shells = bigger atom. More protons (same shell) = smaller atom.",
            "explanation_zh": "**问题：** 确定原子半径增加的趋势。\n\n**关键概念：** 原子半径沿族向下增加（更多壳层）并沿周期减小（更高核电荷）。\n\n**步骤：**\n1. 沿族向下：额外电子壳层→更大半径\n2. 沿周期：相同壳层但更多质子→更强拉力→更小半径\n3. 例子：Li（152 pm）< Na（186 pm）< K（227 pm）\n\n**答案：** 沿族向下\n\n**常见错误：** 与电离能趋势混淆（相反方向）。\n\n**提示：** 更多壳层=更大原子。更多质子（相同壳层）=更小原子。"
        },
        {
            "id": "atom-struct-ex4",
            "type": "short",
            "difficulty": "easy",
            "prompt": "Write the electronic configuration of Cl⁻ (chloride ion).",
            "prompt_zh": "写出Cl⁻（氯离子）的电子构型。",
            "answer": "[Ar] or 1s² 2s² 2p⁶ 3s² 3p⁶",
            "answer_zh": "[Ar] 或 1s² 2s² 2p⁶ 3s² 3p⁶",
            "validator": "smart",
            "explanation": "**Problem:** Determine electronic configuration of Cl⁻.\n\n**Key Concept:** Anions gain electrons. Cl (Z=17) gains 1 electron to form Cl⁻ (18 electrons).\n\n**Steps:**\n1. Cl has 17 electrons: [Ne] 3s² 3p⁵\n2. Cl⁻ gains 1 electron: [Ne] 3s² 3p⁶\n3. This equals [Ar] (argon configuration)\n4. Full configuration: 1s² 2s² 2p⁶ 3s² 3p⁶\n\n**Answer:** [Ar] or 1s² 2s² 2p⁶ 3s² 3p⁶\n\n**Common Mistakes:** Removing electron instead of adding (Cl⁻ is negative).\n\n**Tip:** Negative ions gain electrons to achieve noble gas configuration.",
            "explanation_zh": "**问题：** 确定Cl⁻的电子构型。\n\n**关键概念：** 阴离子获得电子。Cl（Z=17）获得1个电子形成Cl⁻（18个电子）。\n\n**步骤：**\n1. Cl有17个电子：[Ne] 3s² 3p⁵\n2. Cl⁻获得1个电子：[Ne] 3s² 3p⁶\n3. 这等于[Ar]（氩构型）\n4. 完整构型：1s² 2s² 2p⁶ 3s² 3p⁶\n\n**答案：** [Ar] 或 1s² 2s² 2p⁶ 3s² 3p⁶\n\n**常见错误：** 移除电子而不是添加（Cl⁻是负的）。\n\n**提示：** 负离子获得电子以达到稀有气体构型。"
        },
        {
            "id": "atom-struct-ex5",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "Which property increases from left to right across Period 3?",
            "prompt_zh": "哪个性质从左到右在第3周期增加？",
            "choices": ["Atomic radius", "Metallic character", "Electronegativity", "Number of electron shells"],
            "choices_zh": ["原子半径", "金属性", "电负性", "电子壳层数"],
            "answer": 2,
            "explanation": "**Problem:** Identify property that increases across Period 3 (Na to Ar).\n\n**Key Concept:** Electronegativity increases across a period as nuclear charge increases.\n\n**Steps:**\n1. Atomic radius: Decreases (more protons pull electrons closer)\n2. Metallic character: Decreases (metals → metalloids → non-metals)\n3. Electronegativity: Increases (stronger pull on bonding electrons)\n4. Electron shells: Constant (all Period 3 elements have 3 shells)\n\n**Answer:** Electronegativity (Na: 0.9 → Cl: 3.0)\n\n**Common Mistakes:** Confusing with atomic radius (decreases across period).\n\n**Tip:** Higher nuclear charge → stronger pull on electrons → higher electronegativity.",
            "explanation_zh": "**问题：** 确定在第3周期中增加的性质（Na到Ar）。\n\n**关键概念：** 电负性随着核电荷增加沿周期增加。\n\n**步骤：**\n1. 原子半径：减小（更多质子将电子拉近）\n2. 金属性：减小（金属→类金属→非金属）\n3. 电负性：增加（对成键电子的更强拉力）\n4. 电子壳层：恒定（所有第3周期元素都有3个壳层）\n\n**答案：** 电负性（Na：0.9→Cl：3.0）\n\n**常见错误：** 与原子半径混淆（沿周期减小）。\n\n**提示：** 更高核电荷→对电子的更强拉力→更高电负性。"
        }
    ]
}

# Save to file (will add more chapters)
print("Creating JC1 Chemistry exercises...")
print("Chapter 1: Atomic Structure - 5/15 exercises created")
print("\nContinuing with remaining chapters and exercises...")
