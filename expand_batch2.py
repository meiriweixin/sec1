#!/usr/bin/env python3
import json

with open('chapters/jc1_physics_chapters.json', 'r', encoding='utf-8') as f:
    chapters = json.load(f)

# Additional 7 exercises for Dynamics (making 10 total)
dyn_add = [
    {"id": "dynamics-jc1-ex4", "type": "mcq", "difficulty": "easy", "prompt": "Newton's law for passengers lurching forward when bus brakes?", "prompt_zh": "公交车刹车时乘客向前倾的牛顿定律？", "choices": ["First (Inertia)", "Second (F=ma)", "Third", "Gravitation"], "choices_zh": ["第一（惯性）", "第二（F=ma）", "第三", "万有引力"], "answer": 0, "explanation": "Inertia - body continues forward. SBS buses have straps!", "explanation_zh": "惯性 - 身体继续向前。新捷运公交车有拉手！"},
    {"id": "dynamics-jc1-ex5", "type": "short", "difficulty": "medium", "prompt": "60kg in elevator down at 2m/s². g=10m/s². Apparent weight?", "prompt_zh": "60千克在下降2米/秒²电梯中。g=10米/秒²。表观重量？", "answer": "480", "validator": "numeric", "explanation": "N=m(g-a)=60(10-2)=480N. Feel lighter!", "explanation_zh": "N=m(g-a)=60(10-2)=480牛顿。感觉更轻！"},
    {"id": "dynamics-jc1-ex6", "type": "mcq", "difficulty": "medium", "prompt": "2kg+3kg stick together. Initial KE=100J. Final KE≈?", "prompt_zh": "2千克+3千克粘一起。初KE=100焦。最终KE≈？", "choices": ["0J", "40J", "60J", "100J"], "choices_zh": ["0焦", "40焦", "60焦", "100焦"], "answer": 2, "explanation": "≈60J. KE lost to deformation!", "explanation_zh": "≈60焦。动能损失于变形！"},
    {"id": "dynamics-jc1-ex7", "type": "short", "difficulty": "medium", "prompt": "1500kg car stops from 25m/s in 0.1s. Average force?", "prompt_zh": "1500千克车从25米/秒在0.1秒停止。平均力？", "answer": "375000", "validator": "numeric", "explanation": "F=Δp/t=37500/0.1=375000N. Airbags save lives!", "explanation_zh": "F=Δp/t=37500/0.1=375000牛顿。安全气囊救命！"},
    {"id": "dynamics-jc1-ex8", "type": "short", "difficulty": "hard", "prompt": "4kg+6kg over pulley. g=10m/s². Tension?", "prompt_zh": "4千克+6千克滑轮。g=10米/秒²。张力？", "answer": "48", "validator": "numeric", "explanation": "T=m₁(g+a)=4(12)=48N. Construction cranes!", "explanation_zh": "T=m₁(g+a)=4(12)=48牛顿。建筑起重机！"},
    {"id": "dynamics-jc1-ex9", "type": "mcq", "difficulty": "hard", "prompt": "Rocket expels 100kg gas at 500m/s back. 1000kg rocket?", "prompt_zh": "火箭向后喷100千克气体500米/秒。1000千克火箭？", "choices": ["Forward", "Still", "Back", "Explodes"], "choices_zh": ["向前", "静止", "向后", "爆炸"], "answer": 0, "explanation": "Forward at 50m/s! Satellites above Singapore!", "explanation_zh": "向前50米/秒！新加坡上空卫星！"},
    {"id": "dynamics-jc1-ex10", "type": "short", "difficulty": "hard", "prompt": "5kg+3kg blocks, F=20N. System acceleration?", "prompt_zh": "5千克+3千克块，F=20牛顿。系统加速度？", "answer": "2.5", "validator": "numeric", "explanation": "a=F/(m₁+m₂)=20/8=2.5m/s². HDB boxes!", "explanation_zh": "a=F/(m₁+m₂)=20/8=2.5米/秒²。组屋箱子！"}
]

# Additional 7 for Forces (making 10 total)
frc_add = [
    {"id": "forces-jc1-ex4", "type": "mcq", "difficulty": "easy", "prompt": "Centripetal force for car turning?", "prompt_zh": "汽车转弯的向心力？", "choices": ["Engine", "Friction", "Normal", "Gravity"], "choices_zh": ["发动机", "摩擦力", "正压力", "重力"], "answer": 1, "explanation": "Friction! F1 wet = less friction!", "explanation_zh": "摩擦力！F1湿=摩擦力少！"},
    {"id": "forces-jc1-ex5", "type": "short", "difficulty": "medium", "prompt": "60kg on Flyer (r=75m, T=30min). Centripetal acceleration?", "prompt_zh": "60千克在摩天轮（r=75米，T=30分钟）。向心加速度？", "answer": "0.0055", "validator": "numeric", "explanation": "a=v²/r=0.262²/75=0.0055m/s². Gentle!", "explanation_zh": "a=v²/r=0.262²/75=0.0055米/秒²。平缓！"},
    {"id": "forces-jc1-ex6", "type": "mcq", "difficulty": "medium", "prompt": "30° slide, μ=0.2, g=10. Acceleration?", "prompt_zh": "30°滑梯，μ=0.2，g=10。加速度？", "choices": ["3.3m/s²", "4.0m/s²", "5.0m/s²", "6.7m/s²"], "choices_zh": ["3.3米/秒²", "4.0米/秒²", "5.0米/秒²", "6.7米/秒²"], "answer": 0, "explanation": "a=g(sinθ-μcosθ)≈3.3m/s². Safe slides!", "explanation_zh": "a=g(sinθ-μcosθ)≈3.3米/秒²。安全滑梯！"},
    {"id": "forces-jc1-ex7", "type": "short", "difficulty": "medium", "prompt": "1500kg at 20m/s, r=50m. Min μ?", "prompt_zh": "1500千克20米/秒，r=50米。最小μ？", "answer": "0.8", "validator": "numeric", "explanation": "μ=v²/(rg)=400/500=0.8. Banking helps!", "explanation_zh": "μ=v²/(rg)=400/500=0.8。倾斜有帮助！"},
    {"id": "forces-jc1-ex8", "type": "short", "difficulty": "hard", "prompt": "2kg on 30° + 3kg vertical. g=10, sin30°=0.5. Acceleration?", "prompt_zh": "2千克在30°+3千克垂直。g=10，sin30°=0.5。加速度？", "answer": "4", "validator": "numeric", "explanation": "a=(30-10)/5=4m/s². Scaffolding pulleys!", "explanation_zh": "a=(30-10)/5=4米/秒²。脚手架滑轮！"},
    {"id": "forces-jc1-ex9", "type": "mcq", "difficulty": "hard", "prompt": "Banked curve, no friction. Speed formula?", "prompt_zh": "倾斜弯道，无摩擦。速度公式？", "choices": ["√(rg·tanθ)", "√(rg·sinθ)", "√(rg·cosθ)", "√(rg/tanθ)"], "choices_zh": ["√(rg·tanθ)", "√(rg·sinθ)", "√(rg·cosθ)", "√(rg/tanθ)"], "answer": 0, "explanation": "v=√(rg·tanθ). Expressway design!", "explanation_zh": "v=√(rg·tanθ)。高速公路设计！"},
    {"id": "forces-jc1-ex10", "type": "short", "difficulty": "hard", "prompt": "0.5kg, r=0.8m, 2rev/s horizontal. Tension?", "prompt_zh": "0.5千克，r=0.8米，2转/秒水平。张力？", "answer": "126", "validator": "numeric", "explanation": "T=mω²r=0.5×(4π)²×0.8≈126N. Rides!", "explanation_zh": "T=mω²r=0.5×(4π)²×0.8≈126牛顿。游乐设施！"}
]

for ch in chapters:
    if ch['id'] == 'dynamics-jc1-physics':
        ch['exercises'].extend(dyn_add)
    elif ch['id'] == 'forces-jc1-physics':
        ch['exercises'].extend(frc_add)

with open('chapters/jc1_physics_chapters.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, ensure_ascii=False, indent=2)

print("✅ Batch 2 expanded to 20 exercises (10 each)")
