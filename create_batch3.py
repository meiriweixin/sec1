#!/usr/bin/env python3
"""Batch 3: Work/Energy/Power + Current Electricity (20 exercises)"""
import json

with open('chapters/jc1_physics_chapters.json', 'r', encoding='utf-8') as f:
    chapters = json.load(f)

# Work, Energy, Power - 10 exercises (3 easy + 4 medium + 3 hard)
work_energy = [
    {"id": "wep-jc1-ex1", "type": "mcq", "difficulty": "easy", "prompt": "A force of 10N moves an object 5m in the direction of force. Work done?", "prompt_zh": "10牛顿的力使物体沿力方向移动5米。做功？", "choices": ["2 J", "15 J", "50 J", "500 J"], "choices_zh": ["2焦耳", "15焦耳", "50焦耳", "500焦耳"], "answer": 2, "explanation": "W=F·d=10×5=50J. HDB lifts do work!", "explanation_zh": "W=F·d=10×5=50焦耳。组屋电梯做功！"},
    {"id": "wep-jc1-ex2", "type": "short", "difficulty": "easy", "prompt": "A 2kg ball moving at 10m/s. Calculate kinetic energy.", "prompt_zh": "2千克球以10米/秒移动。计算动能。", "answer": "100", "validator": "numeric", "explanation": "KE=½mv²=½(2)(100)=100J. Football kinetic energy!", "explanation_zh": "KE=½mv²=½(2)(100)=100焦耳。足球动能！"},
    {"id": "wep-jc1-ex3", "type": "mcq", "difficulty": "easy", "prompt": "Lifting 5kg box 2m high, g=10m/s². Potential energy gained?", "prompt_zh": "举起5千克箱子2米高，g=10米/秒²。获得势能？", "choices": ["10 J", "50 J", "100 J", "200 J"], "choices_zh": ["10焦耳", "50焦耳", "100焦耳", "200焦耳"], "answer": 2, "explanation": "PE=mgh=5×10×2=100J. HDB movers know this!", "explanation_zh": "PE=mgh=5×10×2=100焦耳。组屋搬家工人知道！"},
    {"id": "wep-jc1-ex4", "type": "short", "difficulty": "medium", "prompt": "Machine does 500J work in 10s. Calculate power output.", "prompt_zh": "机器在10秒内做500焦耳功。计算功率输出。", "answer": "50", "validator": "numeric", "explanation": "P=W/t=500/10=50W. Motor power!", "explanation_zh": "P=W/t=500/10=50瓦。电机功率！"},
    {"id": "wep-jc1-ex5", "type": "mcq", "difficulty": "medium", "prompt": "Ball dropped from 20m, g=10m/s². Speed just before hitting ground?", "prompt_zh": "球从20米落下，g=10米/秒²。落地前速度？", "choices": ["10 m/s", "14 m/s", "20 m/s", "200 m/s"], "choices_zh": ["10米/秒", "14米/秒", "20米/秒", "200米/秒"], "answer": 2, "explanation": "PE→KE: mgh=½mv², v=√(2gh)=√(400)=20m/s. Free fall!", "explanation_zh": "PE→KE：mgh=½mv²，v=√(2gh)=√(400)=20米/秒。自由落体！"},
    {"id": "wep-jc1-ex6", "type": "short", "difficulty": "medium", "prompt": "A 1000kg car accelerates from 10m/s to 20m/s. Work done by engine?", "prompt_zh": "1000千克车从10米/秒加速到20米/秒。发动机做功？", "answer": "150000", "validator": "numeric", "explanation": "W=ΔKE=½m(v²-u²)=½(1000)(400-100)=150000J. Car acceleration!", "explanation_zh": "W=ΔKE=½m(v²-u²)=½(1000)(400-100)=150000焦耳。汽车加速！"},
    {"id": "wep-jc1-ex7", "type": "mcq", "difficulty": "medium", "prompt": "Efficiency = (useful output/total input)×100%. Machine: 400J in, 300J useful out. Efficiency?", "prompt_zh": "效率=(有用输出/总输入)×100%。机器：400焦耳输入，300焦耳有用输出。效率？", "choices": ["25%", "50%", "75%", "133%"], "choices_zh": ["25%", "50%", "75%", "133%"], "answer": 2, "explanation": "η=(300/400)×100%=75%. NEWater pumps ~85% efficient!", "explanation_zh": "η=(300/400)×100%=75%。新生水泵约85%效率！"},
    {"id": "wep-jc1-ex8", "type": "short", "difficulty": "hard", "prompt": "A 50kg student climbs 10m stairs in 20s, g=10m/s². Calculate power developed.", "prompt_zh": "50千克学生20秒爬10米楼梯，g=10米/秒²。计算产生功率。", "answer": "250", "validator": "numeric", "explanation": "W=mgh=50×10×10=5000J. P=W/t=5000/20=250W. HDB stairs workout!", "explanation_zh": "W=mgh=50×10×10=5000焦耳。P=W/t=5000/20=250瓦。组屋楼梯锻炼！"},
    {"id": "wep-jc1-ex9", "type": "mcq", "difficulty": "hard", "prompt": "Spring constant k=100N/m compressed 0.2m. Elastic potential energy stored?", "prompt_zh": "弹簧常数k=100牛顿/米压缩0.2米。储存弹性势能？", "choices": ["2 J", "4 J", "10 J", "20 J"], "choices_zh": ["2焦耳", "4焦耳", "10焦耳", "20焦耳"], "answer": 0, "explanation": "EPE=½kx²=½(100)(0.04)=2J. Springs store energy!", "explanation_zh": "EPE=½kx²=½(100)(0.04)=2焦耳。弹簧储存能量！"},
    {"id": "wep-jc1-ex10", "type": "short", "difficulty": "hard", "prompt": "Block slides down frictionless 5m incline (30°), g=10m/s², sin30°=0.5. Final speed?", "prompt_zh": "块沿无摩擦5米斜面下滑（30°），g=10米/秒²，sin30°=0.5。最终速度？", "answer": "7.07", "validator": "numeric", "explanation": "Height h=5×sin30°=2.5m. PE→KE: mgh=½mv², v=√(2gh)=√(50)≈7.07m/s. Slides!", "explanation_zh": "高度h=5×sin30°=2.5米。PE→KE：mgh=½mv²，v=√(2gh)=√(50)≈7.07米/秒。滑梯！"}
]

# Current Electricity - 10 exercises
current_elec = [
    {"id": "current-jc1-ex1", "type": "mcq", "difficulty": "easy", "prompt": "Current I = Q/t. If 10C charge flows in 2s, current?", "prompt_zh": "电流I = Q/t。如果10库仑电荷在2秒内流动，电流？", "choices": ["2 A", "5 A", "12 A", "20 A"], "choices_zh": ["2安培", "5安培", "12安培", "20安培"], "answer": 1, "explanation": "I=Q/t=10/2=5A. HDB electrical current!", "explanation_zh": "I=Q/t=10/2=5安培。组屋电流！"},
    {"id": "current-jc1-ex2", "type": "short", "difficulty": "easy", "prompt": "Voltage 12V, resistance 4Ω. Using Ohm's Law V=IR, find current.", "prompt_zh": "电压12伏，电阻4欧姆。用欧姆定律V=IR，求电流。", "answer": "3", "validator": "numeric", "explanation": "I=V/R=12/4=3A. Basic circuit!", "explanation_zh": "I=V/R=12/4=3安培。基本电路！"},
    {"id": "current-jc1-ex3", "type": "mcq", "difficulty": "easy", "prompt": "Power P=VI. If V=10V and I=2A, power?", "prompt_zh": "功率P=VI。如果V=10伏和I=2安培，功率？", "choices": ["5 W", "12 W", "20 W", "100 W"], "choices_zh": ["5瓦", "12瓦", "20瓦", "100瓦"], "answer": 2, "explanation": "P=VI=10×2=20W. Light bulb power!", "explanation_zh": "P=VI=10×2=20瓦。灯泡功率！"},
    {"id": "current-jc1-ex4", "type": "short", "difficulty": "medium", "prompt": "Wire length 2m, cross-section 0.5mm², resistivity ρ=1.7×10⁻⁸Ωm. Resistance R=ρL/A?", "prompt_zh": "导线长2米，横截面0.5平方毫米，电阻率ρ=1.7×10⁻⁸欧姆米。电阻R=ρL/A？", "answer": "0.068", "validator": "numeric", "explanation": "A=0.5×10⁻⁶m². R=(1.7×10⁻⁸×2)/(0.5×10⁻⁶)=0.068Ω. Copper wire!", "explanation_zh": "A=0.5×10⁻⁶平方米。R=(1.7×10⁻⁸×2)/(0.5×10⁻⁶)=0.068欧姆。铜线！"},
    {"id": "current-jc1-ex5", "type": "mcq", "difficulty": "medium", "prompt": "A 100W bulb runs for 5 hours. Energy consumed in kWh?", "prompt_zh": "100瓦灯泡运行5小时。消耗能量（千瓦时）？", "choices": ["0.5 kWh", "5 kWh", "50 kWh", "500 kWh"], "choices_zh": ["0.5千瓦时", "5千瓦时", "50千瓦时", "500千瓦时"], "answer": 0, "explanation": "E=Pt=0.1kW×5h=0.5kWh. SP bills in kWh!", "explanation_zh": "E=Pt=0.1千瓦×5小时=0.5千瓦时。新加坡电力账单用千瓦时！"},
    {"id": "current-jc1-ex6", "type": "short", "difficulty": "medium", "prompt": "12V battery delivers 3A for 10min. Total charge transferred?", "prompt_zh": "12伏电池提供3安培10分钟。转移总电荷？", "answer": "1800", "validator": "numeric", "explanation": "Q=It=3×(10×60)=1800C. Battery capacity!", "explanation_zh": "Q=It=3×(10×60)=1800库仑。电池容量！"},
    {"id": "current-jc1-ex7", "type": "mcq", "difficulty": "medium", "prompt": "Resistance of wire at 20°C is 10Ω. Temperature increases, resistance:", "prompt_zh": "20°C时导线电阻10欧姆。温度升高，电阻：", "choices": ["Decreases", "Stays same", "Increases", "Becomes zero"], "choices_zh": ["减少", "保持不变", "增加", "变为零"], "answer": 2, "explanation": "R increases with temperature (more collisions). Singapore heat affects wires!", "explanation_zh": "R随温度增加（更多碰撞）。新加坡热影响电线！"},
    {"id": "current-jc1-ex8", "type": "short", "difficulty": "hard", "prompt": "Electric kettle 230V draws 8A. Time to transfer 1.8×10⁶J energy?", "prompt_zh": "230伏电热水壶吸取8安培。传输1.8×10⁶焦耳能量的时间？", "answer": "978", "validator": "numeric", "explanation": "P=VI=230×8=1840W. t=E/P=1.8×10⁶/1840≈978s≈16min. Boil water!", "explanation_zh": "P=VI=230×8=1840瓦。t=E/P=1.8×10⁶/1840≈978秒≈16分钟。烧水！"},
    {"id": "current-jc1-ex9", "type": "mcq", "difficulty": "hard", "prompt": "Two resistors 6Ω and 3Ω in parallel. Equivalent resistance?", "prompt_zh": "两个电阻6欧姆和3欧姆并联。等效电阻？", "choices": ["1 Ω", "2 Ω", "3 Ω", "9 Ω"], "choices_zh": ["1欧姆", "2欧姆", "3欧姆", "9欧姆"], "answer": 1, "explanation": "1/R=1/6+1/3=1/6+2/6=3/6=1/2, R=2Ω. Parallel circuits!", "explanation_zh": "1/R=1/6+1/3=1/6+2/6=3/6=1/2，R=2欧姆。并联电路！"},
    {"id": "current-jc1-ex10", "type": "short", "difficulty": "hard", "prompt": "HDB uses 500kWh/month. At $0.25/kWh, monthly cost?", "prompt_zh": "组屋每月使用500千瓦时。按每千瓦时$0.25，月费？", "answer": "125", "validator": "numeric", "explanation": "Cost=500×0.25=$125. SP Group bills!", "explanation_zh": "费用=500×0.25=$125。新加坡电力集团账单！"}
]

for ch in chapters:
    if ch['id'] == 'work-energy-power-jc1-physics':
        ch['exercises'] = work_energy
        print(f"✓ Added {len(work_energy)} exercises to Work/Energy/Power")
    elif ch['id'] == 'current-electricity-jc1-physics':
        ch['exercises'] = current_elec
        print(f"✓ Added {len(current_elec)} exercises to Current Electricity")

with open('chapters/jc1_physics_chapters.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, ensure_ascii=False, indent=2)

print("\n✅ Batch 3 Complete: 20 exercises added")
