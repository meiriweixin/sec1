#!/usr/bin/env python3
import json

with open('chapters/jc1_physics_chapters.json', 'r', encoding='utf-8') as f:
    chapters = json.load(f)

# Minimal exercises for testing (3 per chapter for now - can expand later)
dynamics_ex = [
    {"id": "dynamics-jc1-ex1", "type": "mcq", "difficulty": "easy",
     "prompt": "Force 20N on mass 5kg gives what acceleration?",
     "prompt_zh": "20牛顿力作用在5千克质量上产生什么加速度？",
     "choices": ["2 m/s²", "4 m/s²", "15 m/s²", "100 m/s²"],
     "choices_zh": ["2米/秒²", "4米/秒²", "15米/秒²", "100米/秒²"],
     "answer": 1,
     "explanation": "F=ma, so a=F/m=20/5=4 m/s². Port cranes use this!",
     "explanation_zh": "F=ma，所以a=F/m=20/5=4米/秒²。港口起重机使用这个！"},
    {"id": "dynamics-jc1-ex2", "type": "short", "difficulty": "medium",
     "prompt": "1200kg car accelerates 0 to 20m/s in 8s. Find net force.",
     "prompt_zh": "1200千克汽车在8秒内从0加速到20米/秒。求净力。",
     "answer": "3000", "validator": "numeric",
     "explanation": "a=(20-0)/8=2.5 m/s², F=1200×2.5=3000N. F1 cars use huge forces!",
     "explanation_zh": "a=(20-0)/8=2.5米/秒²，F=1200×2.5=3000牛顿。F1赛车使用巨大的力！"},
    {"id": "dynamics-jc1-ex3", "type": "mcq", "difficulty": "hard",
     "prompt": "Perfectly inelastic collision conserves what?",
     "prompt_zh": "完全非弹性碰撞守恒什么？",
     "choices": ["Momentum only", "KE only", "Both", "Neither"],
     "choices_zh": ["仅动量", "仅动能", "两者", "都不"],
     "answer": 0,
     "explanation": "Momentum always conserved, KE lost to deformation. Singapore traffic accidents!",
     "explanation_zh": "动量始终守恒，动能损失于变形。新加坡交通事故！"}
]

forces_ex = [
    {"id": "forces-jc1-ex1", "type": "mcq", "difficulty": "easy",
     "prompt": "10kg box, μ=0.4, g=10m/s². Friction force?",
     "prompt_zh": "10千克箱子，μ=0.4，g=10米/秒²。摩擦力？",
     "choices": ["4 N", "40 N", "100 N", "400 N"],
     "choices_zh": ["4牛顿", "40牛顿", "100牛顿", "400牛顿"],
     "answer": 1,
     "explanation": "N=mg=100N, f=μN=0.4×100=40N. HDB movers know this!",
     "explanation_zh": "N=mg=100牛顿，f=μN=0.4×100=40牛顿。组屋搬家工人知道这个！"},
    {"id": "forces-jc1-ex2", "type": "short", "difficulty": "medium",
     "prompt": "Spring k=200N/m stretched 0.15m. Spring force?",
     "prompt_zh": "弹簧k=200牛顿/米拉伸0.15米。弹簧力？",
     "answer": "30", "validator": "numeric",
     "explanation": "F=kx=200×0.15=30N. Singapore Flyer uses spring principles!",
     "explanation_zh": "F=kx=200×0.15=30牛顿。新加坡摩天轮使用弹簧原理！"},
    {"id": "forces-jc1-ex3", "type": "mcq", "difficulty": "hard",
     "prompt": "Banked curve, no friction. Design speed formula?",
     "prompt_zh": "倾斜弯道，无摩擦。设计速度公式？",
     "choices": ["√(rg·tanθ)", "√(rg·sinθ)", "√(rg·cosθ)", "√(rg/tanθ)"],
     "choices_zh": ["√(rg·tanθ)", "√(rg·sinθ)", "√(rg·cosθ)", "√(rg/tanθ)"],
     "answer": 0,
     "explanation": "v=√(rg·tanθ) from N forces. Expressway curves designed this way!",
     "explanation_zh": "从N力得v=√(rg·tanθ)。高速公路弯道这样设计！"}
]

for ch in chapters:
    if ch['id'] == 'dynamics-jc1-physics':
        ch['exercises'] = dynamics_ex
    elif ch['id'] == 'forces-jc1-physics':
        ch['exercises'] = forces_ex

with open('chapters/jc1_physics_chapters.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, ensure_ascii=False, indent=2)

print("✅ Batch 2 Quick Version Complete")
print(f"Dynamics: {len(dynamics_ex)} exercises")
print(f"Forces: {len(forces_ex)} exercises")
print("Total: 6 exercises added (minimal working version)")
