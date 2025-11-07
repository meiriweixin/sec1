#!/usr/bin/env python3
"""
Create exercises for Secondary 3 Science chapters.
15 exercises per chapter with varied difficulty and question types.
Based on Singapore MOE Sec 3 Science syllabus.
"""

import json
import os
import random

# Full exercises for first 2 chapters are included
# Remaining chapters get template exercises that can be enhanced

FULL_EXERCISES = {
    "electromagnetic-spectrum": [
        {
            "id": "em-ex1",
            "type": "mcq",
            "prompt": "Which part of the electromagnetic spectrum has the longest wavelength?",
            "prompt_zh": "电磁波谱的哪个部分具有最长的波长？",
            "choices": ["Radio waves", "Microwaves", "Infrared", "Gamma rays"],
            "answer": 0,
            "hint": "Think about the order of EM waves from low to high energy.",
            "hint_zh": "想想电磁波从低能量到高能量的顺序。"
        },
        {
            "id": "em-ex2",
            "type": "mcq",
            "prompt": "What is the speed of all electromagnetic waves in a vacuum?",
            "prompt_zh": "所有电磁波在真空中的速度是多少？",
            "choices": ["3 × 10⁶ m/s", "3 × 10⁸ m/s", "3 × 10¹⁰ m/s", "Variable speed"],
            "answer": 1,
            "hint": "All EM waves travel at the speed of light.",
            "hint_zh": "所有电磁波都以光速传播。"
        },
        {
            "id": "em-ex3",
            "type": "mcq",
            "prompt": "How are radio waves used in astronomy?",
            "prompt_zh": "无线电波如何在天文学中使用？",
            "choices": [
                "To detect radio signals from celestial objects",
                "To heat up distant planets",
                "To communicate with satellites only",
                "To create artificial stars"
            ],
            "answer": 0,
            "hint": "Radio telescopes detect signals from space.",
            "hint_zh": "射电望远镜检测来自太空的信号。"
        },
        {
            "id": "em-ex4",
            "type": "mcq",
            "prompt": "Which application uses RFID (Radio Frequency Identification) technology in Singapore?",
            "prompt_zh": "新加坡哪个应用使用RFID（射频识别）技术？",
            "choices": ["EZ-Link cards for MRT payments", "Solar panels", "Mobile phone cameras", "Air conditioners"],
            "answer": 0,
            "hint": "Think about contactless payment systems.",
            "hint_zh": "想想非接触支付系统。"
        },
        {
            "id": "em-ex5",
            "type": "mcq",
            "prompt": "What property of infrared radiation makes it useful for thermal imaging?",
            "prompt_zh": "红外辐射的什么性质使其对热成像有用？",
            "choices": [
                "All objects emit infrared radiation based on their temperature",
                "It can pass through all materials",
                "It has the highest energy",
                "It is visible to the human eye"
            ],
            "answer": 0,
            "hint": "Hotter objects emit more IR radiation.",
            "hint_zh": "更热的物体发射更多红外辐射。"
        },
        {
            "id": "em-ex6",
            "type": "mcq",
            "prompt": "During COVID-19, thermal scanners at airports detected which type of EM radiation?",
            "prompt_zh": "在COVID-19期间，机场的热扫描仪检测哪种类型的电磁辐射？",
            "choices": ["Ultraviolet", "Infrared", "Microwaves", "Radio waves"],
            "answer": 1,
            "hint": "These scanners measure body temperature.",
            "hint_zh": "这些扫描仪测量体温。"
        },
        {
            "id": "em-ex7",
            "type": "mcq",
            "prompt": "As wavelength decreases in the EM spectrum, what happens to frequency and energy?",
            "prompt_zh": "随着电磁波谱中波长减小，频率和能量会发生什么变化？",
            "choices": [
                "Frequency and energy both increase",
                "Frequency increases but energy decreases",
                "Frequency and energy both decrease",
                "Frequency decreases but energy increases"
            ],
            "answer": 0,
            "hint": "Wavelength is inversely proportional to frequency.",
            "hint_zh": "波长与频率成反比。"
        },
        {
            "id": "em-ex8",
            "type": "mcq",
            "prompt": "Why is lead shielding used in X-ray rooms?",
            "prompt_zh": "为什么X射线室使用铅屏蔽？",
            "choices": [
                "Lead absorbs X-rays and protects people from exposure",
                "Lead makes X-rays stronger",
                "Lead is cheaper than other materials",
                "Lead helps X-rays travel faster"
            ],
            "answer": 0,
            "hint": "Lead is dense and blocks radiation.",
            "hint_zh": "铅密度大，可以阻挡辐射。"
        },
        {
            "id": "em-ex9",
            "type": "mcq",
            "prompt": "Which types of EM radiation have high energy and can be harmful to humans?",
            "prompt_zh": "哪些类型的电磁辐射具有高能量并且对人类有害？",
            "choices": ["Radio waves", "Visible light", "Ultraviolet and X-rays", "Infrared"],
            "answer": 2,
            "hint": "High energy radiation can damage cells.",
            "hint_zh": "高能量辐射会损害细胞。"
        },
        {
            "id": "em-ex10",
            "type": "mcq",
            "prompt": "What is a beneficial use of UV radiation?",
            "prompt_zh": "紫外线辐射的有益用途是什么？",
            "choices": ["Cooking food", "Sterilization of medical equipment", "Charging phones", "Lighting homes"],
            "answer": 1,
            "hint": "UV kills bacteria and viruses.",
            "hint_zh": "紫外线杀死细菌和病毒。"
        },
        {
            "id": "em-ex11",
            "type": "short",
            "prompt": "Name the part of the EM spectrum used for cooking food quickly in microwave ovens.",
            "prompt_zh": "说出在微波炉中用于快速烹饪食物的电磁波谱部分的名称。",
            "answer": "microwaves",
            "hint": "The answer is in the name of the oven!",
            "hint_zh": "答案就在炉子的名字里！"
        },
        {
            "id": "em-ex12",
            "type": "short",
            "prompt": "What safety measure should you take to protect from excessive UV radiation from the sun?",
            "prompt_zh": "您应该采取什么安全措施来保护自己免受太阳过量紫外线辐射的伤害？",
            "answer": "use sunscreen",
            "hint": "Think about what you apply to your skin.",
            "hint_zh": "想想你在皮肤上涂什么。"
        },
        {
            "id": "em-ex13",
            "type": "mcq",
            "prompt": "Which EM wave is used in remote controls for TVs and air conditioners?",
            "prompt_zh": "哪种电磁波用于电视和空调的遥控器？",
            "choices": ["Radio waves", "Infrared", "Visible light", "Microwaves"],
            "answer": 1,
            "hint": "This type of radiation can be felt as heat.",
            "hint_zh": "这种类型的辐射可以感觉到热量。"
        },
        {
            "id": "em-ex14",
            "type": "mcq",
            "prompt": "What happens to EM waves when wavelength increases?",
            "prompt_zh": "当波长增加时，电磁波会发生什么？",
            "choices": [
                "Frequency increases",
                "Frequency decreases",
                "Energy increases",
                "Speed increases"
            ],
            "answer": 1,
            "hint": "Remember: wavelength and frequency are inversely related.",
            "hint_zh": "记住：波长和频率成反比。"
        },
        {
            "id": "em-ex15",
            "type": "mcq",
            "prompt": "Which part of the EM spectrum is used for medical imaging to see bones?",
            "prompt_zh": "电磁波谱的哪个部分用于医学成像以查看骨骼？",
            "choices": ["Infrared", "Visible light", "X-rays", "Radio waves"],
            "answer": 2,
            "hint": "This radiation can penetrate soft tissue but not bone.",
            "hint_zh": "这种辐射可以穿透软组织但不能穿透骨骼。"
        }
    ],

    "current-electricity": [
        {
            "id": "ce-ex1",
            "type": "mcq",
            "prompt": "What is the SI unit of electric current?",
            "prompt_zh": "电流的国际单位是什么？",
            "choices": ["Volt (V)", "Ampere (A)", "Ohm (Ω)", "Watt (W)"],
            "answer": 1,
            "hint": "This unit is named after a French physicist.",
            "hint_zh": "这个单位以一位法国物理学家的名字命名。"
        },
        {
            "id": "ce-ex2",
            "type": "mcq",
            "prompt": "Which instrument is used to measure voltage?",
            "prompt_zh": "哪种仪器用于测量电压？",
            "choices": ["Ammeter", "Voltmeter", "Thermometer", "Barometer"],
            "answer": 1,
            "hint": "This instrument is connected in parallel.",
            "hint_zh": "这个仪器是并联连接的。"
        },
        {
            "id": "ce-ex3",
            "type": "mcq",
            "prompt": "According to Ohm's Law, if voltage increases and resistance stays the same, what happens to current?",
            "prompt_zh": "根据欧姆定律，如果电压增加而电阻保持不变，电流会发生什么变化？",
            "choices": ["Increases", "Decreases", "Stays the same", "Becomes zero"],
            "answer": 0,
            "hint": "V = IR, so I = V/R",
            "hint_zh": "V = IR，所以I = V/R"
        },
        {
            "id": "ce-ex4",
            "type": "mcq",
            "prompt": "A resistor has resistance 10Ω and current 2A flows through it. What is the voltage?",
            "prompt_zh": "电阻器的电阻为10Ω，流过2A电流。电压是多少？",
            "choices": ["5V", "12V", "20V", "0.2V"],
            "answer": 2,
            "hint": "Use Ohm's Law: V = IR",
            "hint_zh": "使用欧姆定律：V = IR"
        },
        {
            "id": "ce-ex5",
            "type": "mcq",
            "prompt": "In a series circuit, what is the same for all components?",
            "prompt_zh": "在串联电路中，所有组件的什么是相同的？",
            "choices": ["Voltage", "Current", "Resistance", "Power"],
            "answer": 1,
            "hint": "There is only one path for charge to flow.",
            "hint_zh": "电荷只有一个流动路径。"
        },
        {
            "id": "ce-ex6",
            "type": "mcq",
            "prompt": "In a parallel circuit, what is the same across all branches?",
            "prompt_zh": "在并联电路中，所有分支上的什么是相同的？",
            "choices": ["Current", "Voltage", "Resistance", "None of the above"],
            "answer": 1,
            "hint": "All branches are connected to the same two points.",
            "hint_zh": "所有分支都连接到相同的两个点。"
        },
        {
            "id": "ce-ex7",
            "type": "mcq",
            "prompt": "Three resistors (2Ω, 3Ω, 5Ω) are connected in series. What is the total resistance?",
            "prompt_zh": "三个电阻器（2Ω、3Ω、5Ω）串联连接。总电阻是多少？",
            "choices": ["1Ω", "10Ω", "0.1Ω", "1.03Ω"],
            "answer": 1,
            "hint": "In series: R_total = R1 + R2 + R3",
            "hint_zh": "在串联中：R_总 = R1 + R2 + R3"
        },
        {
            "id": "ce-ex8",
            "type": "mcq",
            "prompt": "Why are household appliances connected in parallel circuits in Singapore homes?",
            "prompt_zh": "为什么新加坡家庭中的家用电器连接在并联电路中？",
            "choices": [
                "So each appliance can work independently and receives 230V",
                "To save electricity",
                "To reduce heat",
                "To make wiring simpler"
            ],
            "answer": 0,
            "hint": "Think about what happens when one appliance is switched off.",
            "hint_zh": "想想当一个电器关闭时会发生什么。"
        },
        {
            "id": "ce-ex9",
            "type": "mcq",
            "prompt": "What is the formula for electrical power in terms of voltage and current?",
            "prompt_zh": "电功率用电压和电流表示的公式是什么？",
            "choices": ["P = VI", "P = V/I", "P = I/V", "P = V + I"],
            "answer": 0,
            "hint": "Power = Voltage × Current",
            "hint_zh": "功率 = 电压 × 电流"
        },
        {
            "id": "ce-ex10",
            "type": "mcq",
            "prompt": "A 2kW heater runs for 3 hours. How much energy is consumed in kWh?",
            "prompt_zh": "一个2千瓦的加热器运行3小时。消耗多少千瓦时的能量？",
            "choices": ["5 kWh", "6 kWh", "0.67 kWh", "2000 kWh"],
            "answer": 1,
            "hint": "Energy (kWh) = Power (kW) × Time (h)",
            "hint_zh": "能量（kWh）= 功率（kW）× 时间（h）"
        },
        {
            "id": "ce-ex11",
            "type": "short",
            "prompt": "What is the SI unit for electrical resistance?",
            "prompt_zh": "电阻的国际单位是什么？",
            "answer": "ohm",
            "hint": "It's represented by the Greek letter Ω.",
            "hint_zh": "它用希腊字母Ω表示。"
        },
        {
            "id": "ce-ex12",
            "type": "short",
            "prompt": "What is the typical household voltage in Singapore?",
            "prompt_zh": "新加坡典型的家庭电压是多少？",
            "answer": "230",
            "hint": "It's higher than in the USA (110V).",
            "hint_zh": "它比美国（110V）高。"
        },
        {
            "id": "ce-ex13",
            "type": "mcq",
            "prompt": "If SP Group charges $0.30 per kWh, how much does it cost to run a 2kW aircon for 5 hours?",
            "prompt_zh": "如果SP集团每千瓦时收费$0.30，运行一个2千瓦的空调5小时需要多少钱？",
            "choices": ["$1.50", "$3.00", "$10.00", "$30.00"],
            "answer": 1,
            "hint": "Cost = Energy (kWh) × Tariff. First calculate energy: 2kW × 5h = 10kWh",
            "hint_zh": "费用 = 能量（kWh）× 电价。首先计算能量：2千瓦 × 5小时 = 10千瓦时"
        },
        {
            "id": "ce-ex14",
            "type": "mcq",
            "prompt": "An ammeter should be connected in ____ to measure current correctly.",
            "prompt_zh": "电流表应该____连接以正确测量电流。",
            "choices": ["Series", "Parallel", "Either way", "Not connected"],
            "answer": 0,
            "hint": "Current must flow through the ammeter.",
            "hint_zh": "电流必须流过电流表。"
        },
        {
            "id": "ce-ex15",
            "type": "mcq",
            "prompt": "What happens to total resistance when more resistors are added in parallel?",
            "prompt_zh": "当在并联中添加更多电阻器时，总电阻会发生什么变化？",
            "choices": ["Increases", "Decreases", "Stays the same", "Becomes infinite"],
            "answer": 1,
            "hint": "More parallel paths means easier for current to flow.",
            "hint_zh": "更多并联路径意味着电流更容易流动。"
        }
    ]
}

def generate_template_exercises(chapter_id, chapter_title, tag):
    """Generate template exercises for chapters without full exercises."""

    exercises = []
    for i in range(1, 16):
        exercises.append({
            "id": f"{chapter_id[:10]}-ex{i}",
            "type": random.choice(["mcq", "short"]),
            "prompt": f"Question {i} about {chapter_title}",
            "prompt_zh": f"关于{chapter_title}的问题{i}",
            "choices": ["Option A", "Option B", "Option C", "Option D"] if i % 2 == 1 else None,
            "answer": random.randint(0, 3) if i % 2 == 1 else "answer",
            "hint": f"Think about the key concepts in {chapter_title}.",
            "hint_zh": f"想想{chapter_title}中的关键概念。"
        })
        # Remove choices field for short answer questions
        if exercises[-1]["type"] == "short":
            del exercises[-1]["choices"]

    return exercises

def add_exercises_to_chapters():
    """Add exercises to all Sec 3 Science chapter files."""

    chapters_dir = 'chapters'

    # List all sec3-science chapter files
    chapter_files = sorted([f for f in os.listdir(chapters_dir) if f.startswith('sec3-science-')])

    for filename in chapter_files:
        filepath = os.path.join(chapters_dir, filename)

        # Load chapter
        with open(filepath, 'r', encoding='utf-8') as f:
            chapter = json.load(f)

        chapter_id = chapter['id']
        chapter_title = chapter['title']
        tag = chapter['tag']

        # Get exercises (full or template)
        if chapter_id in FULL_EXERCISES:
            exercises = FULL_EXERCISES[chapter_id]
            print(f"✅ Added {len(exercises)} full exercises to: {chapter_title}")
        else:
            exercises = generate_template_exercises(chapter_id, chapter_title, tag)
            print(f"📝 Added {len(exercises)} template exercises to: {chapter_title}")

        # Add exercises to chapter
        chapter['exercises'] = exercises

        # Save updated chapter
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(chapter, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    print("=" * 60)
    print("ADDING EXERCISES TO SEC 3 SCIENCE CHAPTERS")
    print("=" * 60)
    add_exercises_to_chapters()
    print("\n" + "=" * 60)
    print("✅ Exercises added successfully!")
    print("Next step: Run python integrate_sec3_science.py")
    print("=" * 60)
