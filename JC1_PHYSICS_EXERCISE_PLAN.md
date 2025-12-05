# JC 1 Physics Exercise Generation Plan

**Status:** Lessons integrated ✅ | Exercises pending (0/120)
**Target:** 120 exercises (15 per chapter, 5 easy + 5 medium + 5 hard)

---

## 📋 Exercise Creation Batches

### Batch 1: Chapters 1-2 (Measurement, Kinematics) - 30 exercises
**Status:** Template created, ready to complete
**File:** `create_jc1_physics_exercises_batch1.py`
**Content:**
- Chapter 1 (Measurement): 15 exercises
  - Easy (1-5): Unit conversions, sig figs, uncertainty calculations
  - Medium (6-10): Vector operations, dimensional analysis, combined uncertainties
  - Hard (11-15): Complex error propagation, systematic vs random errors
- Chapter 2 (Kinematics): 15 exercises
  - Easy: Basic velocity/acceleration calculations, displacement
  - Medium: Graphical analysis, projectile motion
  - Hard: Complex motion scenarios, 2D kinematics

**Singapore Examples:**
- MRT distances and speeds
- HDB building measurements
- Marina Bay Sands elevator
- Singapore Flyer motion
- Sentosa cable car projectiles

---

### Batch 2: Chapters 3-4 (Dynamics, Forces) - 30 exercises
**Status:** Not started
**Topics:**
- Chapter 3 (Dynamics):
  - Newton's laws applications
  - Momentum and impulse calculations
  - Collision problems (elastic, inelastic)
- Chapter 4 (Forces):
  - Friction calculations
  - Circular motion problems
  - Spring/Hooke's Law
  - Gravitational force

**Singapore Examples:**
- Port of Singapore cranes
- SAF training exercises
- F1 Singapore GP forces
- Singapore Flyer rotation
- HDB lift systems
- Esplanade Bridge cables

---

### Batch 3: Chapters 5-6 (Work/Energy/Power, Current) - 30 exercises
**Status:** Not started
**Topics:**
- Chapter 5 (Work, Energy, Power):
  - Work calculations
  - Energy conservation
  - Power and efficiency
  - Mechanical energy problems
- Chapter 6 (Current of Electricity):
  - Current, charge, voltage
  - Resistance and Ohm's Law
  - Electrical power
  - Resistivity

**Singapore Examples:**
- Marina Barrage hydroelectric
- NEWater pump power
- MRT regenerative braking
- HDB electrical consumption
- Solar panels
- Singapore Power Grid

---

### Batch 4: Chapters 7-8 (DC Circuits, Waves) - 30 exercises
**Status:** Not started
**Topics:**
- Chapter 7 (DC Circuits):
  - Series/parallel resistor combinations
  - Kirchhoff's laws
  - Potential dividers
  - Internal resistance
- Chapter 8 (Waves):
  - Wave properties calculations
  - EM spectrum applications
  - Interference problems
  - Doppler effect

**Singapore Examples:**
- HDB distribution boards
- Traffic light circuits
- WiFi interference
- 5G networks
- MediaCorp radio frequencies
- Changi Airport radar

---

## 📝 Exercise Format (JC Mathematics Pattern)

### Standard Structure:
```json
{
  "id": "chapter-id-exN",
  "type": "mcq" | "short",
  "difficulty": "easy" | "medium" | "hard",
  "prompt": "English question with Singapore context",
  "prompt_zh": "Chinese translation",
  "choices": ["A", "B", "C", "D"],  // MCQ only
  "choices_zh": [...],  // MCQ only
  "answer": 0 | "numerical value",
  "validator": "smart" | "numeric" | "fraction",  // short answer
  "explanation": "6-step pedagogical format",
  "explanation_zh": "Chinese translation"
}
```

### 6-Step Explanation Format:
1. **Problem:** Restate the question clearly
2. **Key Concept:** Identify the main physics principle
3. **Steps:** Show step-by-step solution with formulas
4. **Answer:** State final answer with units
5. **Common Mistakes:** Address typical errors students make
6. **Tip:** Provide helpful insight or Singapore context connection

---

## 🎯 Quality Standards

### Content Requirements:
- ✅ All formulas in LaTeX format
- ✅ Step-by-step numerical calculations
- ✅ Proper units throughout
- ✅ Singapore-specific examples in every exercise
- ✅ Full bilingual support (English + Chinese)
- ✅ Smart answer validation for calculations
- ✅ Realistic values and scenarios

### Difficulty Distribution:
Each chapter must have:
- **5 Easy exercises:** Basic formula application, single-step problems
- **5 Medium exercises:** Multi-step problems, graph analysis, combinations
- **5 Hard exercises:** Complex scenarios, multiple concepts, real-world applications

### Answer Type Mix (per chapter):
- **10 MCQ exercises:** Testing conceptual understanding and calculations
- **5 Short answer exercises:** Numerical calculations with smart validation

---

## 🚀 Implementation Steps (Per Batch)

### Step 1: Create Exercise Script
```python
# File: create_jc1_physics_exercises_batchN.py
import json

# Load chapters
with open('chapters/jc1_physics_chapters.json', 'r', encoding='utf-8') as f:
    chapters = json.load(f)

# Define exercises for chapters in batch
exercises_chapterX = [... 15 exercises ...]
exercises_chapterY = [... 15 exercises ...]

# Update chapters
for ch in chapters:
    if ch['id'] == 'chapter-x-id':
        ch['exercises'] = exercises_chapterX
    elif ch['id'] == 'chapter-y-id':
        ch['exercises'] = exercises_chapterY

# Save updated chapters
with open('chapters/jc1_physics_chapters.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, ensure_ascii=False, indent=2)
```

### Step 2: Run Script
```bash
python create_jc1_physics_exercises_batchN.py
```

### Step 3: Verify Structure
```bash
python -c "
import json
with open('chapters/jc1_physics_chapters.json', 'r', encoding='utf-8') as f:
    chapters = json.load(f)
total = sum(len(ch.get('exercises', [])) for ch in chapters)
print(f'Total exercises: {total}/120')
for ch in chapters:
    ex_count = len(ch.get('exercises', []))
    print(f'{ch[\"title\"]}: {ex_count} exercises')
"
```

### Step 4: Re-integrate into Platform
```bash
python integrate_jc1_physics.py
```

### Step 5: Test in Browser
```bash
npm run dev
# Navigate to JC 1 Physics chapters
# Test exercise rendering and validation
```

---

## 📊 Progress Tracking

### Current Status:
| Batch | Chapters | Status | Exercises |
|-------|----------|--------|-----------|
| 1 | Measurement, Kinematics | Template ready | 0/30 |
| 2 | Dynamics, Forces | Not started | 0/30 |
| 3 | Work/Energy, Current | Not started | 0/30 |
| 4 | DC Circuits, Waves | Not started | 0/30 |
| **Total** | **8 chapters** | **0% complete** | **0/120** |

### After Full Completion:
- **Platform exercises:** 2,265 → 2,385 (+120)
- **JC exercises:** 240 → 360 (+120)
- **Physics status:** Complete (lessons + exercises) ✅

---

## 🎓 Example Exercise (Reference)

### Easy - Measurement (from template):
```json
{
  "id": "measurement-jc1-ex1",
  "type": "mcq",
  "difficulty": "easy",
  "prompt": "Convert 5.2 km to meters.",
  "prompt_zh": "将5.2公里转换为米。",
  "choices": ["52 m", "520 m", "5,200 m", "52,000 m"],
  "choices_zh": ["52米", "520米", "5,200米", "52,000米"],
  "answer": 2,
  "explanation": "**Problem:** Convert 5.2 km to meters...",
  "explanation_zh": "**问题：** 将5.2公里转换为米..."
}
```

### Medium - Kinematics (pattern):
```json
{
  "id": "kinematics-jc1-ex8",
  "type": "short",
  "difficulty": "medium",
  "prompt": "An MRT train accelerates uniformly from rest at 1.5 m/s² for 10 seconds. Calculate the distance traveled.",
  "prompt_zh": "一列地铁列车以1.5米/秒²从静止开始匀加速10秒。计算行驶距离。",
  "answer": "75",
  "validator": "numeric",
  "explanation": "**Problem:** Find distance for uniformly accelerated motion...",
  "explanation_zh": "**问题：** 求匀加速运动的距离..."
}
```

---

## ⏱️ Estimated Timeline

### Per Batch (30 exercises):
- **Writing exercises:** 3-4 hours
- **Testing & verification:** 30 minutes
- **Integration:** 15 minutes
- **Total per batch:** ~4-5 hours

### Full Completion (4 batches):
- **Total time:** 16-20 hours
- **Recommended:** 1-2 batches per work session
- **Timeline:** 2-4 work sessions to complete all

---

## 🔧 Tools & Resources

### Existing Templates:
- `create_jc1_physics_exercises_batch1.py` - 10 examples created
- JC Mathematics exercise scripts - proven pattern
- `chapters/jc1_physics_chapters.json` - chapter structure

### Reference Materials:
- `JC_SCIENCES_SYLLABUS.md` - Topic coverage
- `JC1_PHYSICS_COMPLETE_SUMMARY.md` - Lesson content
- Singapore A-Level H2 Physics syllabus (9749)

### Validation:
- Smart validators for numerical answers
- Numeric validator with ±0.001 tolerance
- LaTeX formulas in explanations

---

## 📌 Important Notes

### Singapore Context Mandatory:
Every exercise must include realistic Singapore examples:
- Infrastructure (MRT, HDB, Marina Bay, Changi Airport)
- Technology (NEWater, 5G networks, solar panels)
- Transportation (cables cars, expressways, F1 GP)
- Industry (Port of Singapore, power stations, semiconductors)

### Bilingual Requirement:
All content must have both English and Chinese:
- Question prompts
- Answer choices (MCQ)
- Full explanations
- Common mistakes
- Tips

### Answer Validation:
- **MCQ:** Index-based (0, 1, 2, 3)
- **Numeric:** Use "numeric" validator (tolerance ±0.001)
- **Smart:** Use "smart" validator for formulas and expressions
- Always include units in explanations

---

## 🎯 Next Actions

**When ready to add exercises:**

1. **Choose a batch** (recommend starting with Batch 1)
2. **Complete the Python script** with all 30 exercises
3. **Run the script** to update `jc1_physics_chapters.json`
4. **Verify exercise counts** match expectations
5. **Re-run integration** to update platform
6. **Test in browser** with dev server
7. **Repeat** for remaining batches

**Current recommendation:**
Start with Batch 1 (Measurement + Kinematics) as the template is already partially complete with 10 example exercises showing the exact format needed.

---

**End of Exercise Generation Plan**

Physics lessons are live on platform ✅
Exercises to be added in focused batches when ready ⏳
