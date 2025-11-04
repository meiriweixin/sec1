import json

# Load existing chapters
with open('chapters/science-sec2-chapters.json', 'r', encoding='utf-8') as f:
    chapters = json.load(f)

# Exercise data for first 5 chapters (Chemistry)
exercise_data = {
    "chemical-changes-sec2": [
        ("Which of the following is a chemical change?", ["Melting ice", "Boiling water", "Burning wood", "Dissolving sugar"], 2, "mcq"),
        ("What is a sign of a chemical reaction?", ["Change in shape", "Change in color", "Change in size", "Change in position"], 1, "mcq"),
        ("Is rusting a physical or chemical change?", "chemical", None, "short"),
        ("Which process is reversible?", ["Burning paper", "Freezing water", "Cooking an egg", "Baking a cake"], 1, "mcq"),
        ("What happens to the total mass in a chemical reaction?", ["It increases", "It decreases", "It stays the same", "It doubles"], 2, "mcq"),
        ("Which are signs of chemical reactions? (Select all)", ["Gas bubbles produced", "Temperature change", "Change in state", "Precipitate forms"], [0,1,3], "multi"),
        ("In Singapore's humid climate, which would rust fastest?", ["Painted iron gate", "Galvanized steel pole", "Unpainted iron railing near the sea", "Stainless steel handrail"], 2, "mcq"),
        ("If 10g of Mg reacts with O2 to form 16g of MgO, how much oxygen was used? (grams)", "6", None, "short"),
        ("Which equation shows a chemical change?", ["Ice → Water", "Iron + Oxygen → Iron oxide", "Sugar + Water → Sugar solution", "Steam → Water"], 1, "mcq"),
        ("Why does food spoil faster in Singapore?", ["Higher humidity only", "Higher temperature speeds up chemical reactions", "More bacteria", "Different food"], 1, "mcq"),
        ("5g copper carbonate heated leaves 3.2g copper oxide. Mass of gas released?", ["1.8g", "2.0g", "8.2g", "Cannot determine"], 0, "mcq"),
        ("Which increase rusting rate in Singapore? (Select all)", ["High humidity (80-90%)", "Salt spray from sea", "High temperature (30°C+)", "Low oxygen"], [0,1,2], "multi"),
        ("Process where solid changes directly to gas:", "sublimation", None, "short"),
        ("In closed system, 20g reactants react. Mass of products?", ["Less than 20g", "Exactly 20g", "More than 20g", "Cannot determine"], 1, "mcq"),
        ("Which statement is FALSE?", ["Physical changes are reversible", "Chemical changes involve energy", "Physical changes never involve energy", "Chemical changes form new substances"], 2, "mcq")
    ],

    "oxidation-reduction-sec2": [
        ("What is oxidation?", ["Gain of oxygen", "Loss of oxygen", "Gain of hydrogen", "Loss of nitrogen"], 0, "mcq"),
        ("Which gas is needed for combustion?", ["Nitrogen", "Oxygen", "Carbon dioxide", "Hydrogen"], 1, "mcq"),
        ("Chemical symbol for oxygen:", "O2", None, "short"),
        ("What forms when iron rusts?", ["Iron sulfate", "Iron chloride", "Iron oxide", "Iron carbonate"], 2, "mcq"),
        ("Complete combustion of methane (CH4):", ["CH₄ → C + H₂", "CH₄ + O₂ → CO + H₂O", "CH₄ + 2O₂ → CO₂ + 2H₂O", "CH₄ → CH₃ + H"], 2, "mcq"),
        ("What is needed for rusting? (Select all)", ["Water", "Oxygen", "Carbon dioxide", "High temperature"], [0,1], "multi"),
        ("Why do coastal structures rust faster in Singapore?", ["Salt water speeds up rusting", "More oxygen", "Lower temperature", "Less pollution"], 0, "mcq"),
        ("Toxic gas from incomplete combustion:", ["CO₂", "CO", "O₂", "N₂"], 1, "mcq"),
        ("Which prevent rusting? (Select all)", ["Painting", "Oiling", "Galvanizing", "Heating"], [0,1,2], "multi"),
        ("Besides CO2, what forms in complete combustion of hydrocarbons?", "water", None, "short"),
        ("In Iron + Oxygen → Iron oxide:", ["Iron oxidized only", "Oxygen reduced only", "Both oxidation and reduction", "Neither"], 2, "mcq"),
        ("Why is incomplete combustion dangerous indoors?", ["Produces heat", "Produces toxic CO", "Uses oxygen", "Produces light"], 1, "mcq"),
        ("Process where reactive metal protects less reactive metal:", "sacrificial protection", None, "short"),
        ("In 2H2O2 → 2H2O + O2, which is both oxidized and reduced?", ["Water", "Oxygen", "Hydrogen peroxide", "None"], 2, "mcq"),
        ("How does Singapore's high humidity affect rusting?", ["More H₂O for reaction", "Blocks oxygen", "Cools metal", "Removes rust"], 0, "mcq")
    ],

    "rate-of-reaction-sec2": [
        ("What is rate of reaction?", ["Speed of chemical change", "Amount of products", "Type of reaction", "Color"], 0, "mcq"),
        ("Higher temperature ___ reaction rate:", ["increases", "decreases", "no effect", "varies"], 0, "mcq"),
        ("How to measure reaction rate?", ["Color only", "Volume of gas produced", "Smell", "Taste"], 1, "mcq"),
        ("In Singapore's 30°C climate, reactions are:", ["slower", "faster", "same", "stopped"], 1, "mcq"),
        ("What is a catalyst?", ["Speeds reactions without being used", "Slows reactions", "Stops reactions", "Changes products"], 0, "mcq"),
        ("Factors affecting rate: (Select all)", ["Temperature", "Concentration", "Surface area", "Catalyst"], [0,1,2,3], "multi"),
        ("Powdered sugar dissolves faster because:", ["Higher surface area", "Sweeter", "Different chemical", "Lower mass"], 0, "mcq"),
        ("Why does food spoil faster in hot Singapore?", "higher temperature increases reaction rate", None, "short"),
        ("At higher concentration, particles:", ["collide less", "collide more", "same rate", "never collide"], 1, "mcq"),
        ("Which increases rate?", ["Large lump", "Powder", "Same", "Neither"], 1, "mcq"),
        ("Enzymes act as:", ["catalysts", "reactants", "products", "inhibitors"], 0, "mcq"),
        ("If temperature increases 10°C, rate typically:", ["doubles", "halves", "same", "zero"], 0, "mcq"),
        ("Singapore's petrochemical industry uses catalysts to:", ["speed production", "cool reactions", "stop reactions", "change colors"], 0, "mcq"),
        ("Which does NOT affect rate?", ["Temperature", "Concentration", "Container color", "Surface area"], 2, "mcq"),
        ("Catalyst works by:", ["Lowering activation energy", "Raising temperature", "Increasing concentration", "Adding reactants"], 0, "mcq")
    ],

    "reactivity-series-sec2": [
        ("Most reactive metal:", ["Gold", "Iron", "Potassium", "Copper"], 2, "mcq"),
        ("Least reactive metal:", ["Zinc", "Platinum", "Magnesium", "Aluminium"], 1, "mcq"),
        ("Can zinc displace copper from copper sulfate?", "yes", None, "short"),
        ("More reactive metal can:", ["displace less reactive", "displace any", "displace none", "displace iron only"], 0, "mcq"),
        ("Which reacts with cold water?", ["Copper", "Silver", "Calcium", "Gold"], 2, "mcq"),
        ("Metals above carbon extracted by:", ["heating with carbon", "electrolysis", "found native", "using water"], 1, "mcq"),
        ("Iron + Copper sulfate →", ["No reaction", "Iron sulfate + Copper", "Iron oxide", "Copper oxide"], 1, "mcq"),
        ("Metals extracted by carbon reduction:", ["Very reactive", "Moderately reactive", "Unreactive", "All"], 1, "mcq"),
        ("Gold found native because:", ["Very unreactive", "Very reactive", "Magnetic", "Colorful"], 0, "mcq"),
        ("Order most to least reactive:", ["Mg, Fe, Cu", "Cu, Fe, Mg", "Fe, Cu, Mg", "Cu, Mg, Fe"], 0, "mcq"),
        ("Copper + Zinc sulfate →", ["Copper displaces zinc", "No reaction", "Explosion", "Color change"], 1, "mcq"),
        ("Singapore imports aluminum extracted by:", "electrolysis", None, "short"),
        ("Most vigorous with dilute acid:", ["Copper", "Silver", "Magnesium", "Gold"], 2, "mcq"),
        ("Reactivity series predicts:", ["displacement reactions", "color", "density", "melting point"], 0, "mcq"),
        ("Lead + Copper sulfate →", ["No reaction", "Lead sulfate + Copper", "Lead oxide", "Lead chloride"], 1, "mcq")
    ],

    "chemical-bonding-sec2": [
        ("What is ionic bonding?", ["Transfer of electrons", "Sharing electrons", "Magnetic attraction", "Gravity"], 0, "mcq"),
        ("What is covalent bonding?", ["Sharing electrons", "Transferring electrons", "Losing protons", "Gaining neutrons"], 0, "mcq"),
        ("Which forms ionic bonds?", ["Metal + Non-metal", "Non-metal + Non-metal", "Metal + Metal", "Hydrogen only"], 0, "mcq"),
        ("Table salt (NaCl) is:", ["ionic", "covalent", "metallic", "hydrogen"], 0, "mcq"),
        ("Water (H2O) has ___ bonds:", "covalent", None, "short"),
        ("Ionic compound properties: (Select all)", ["High melting point", "Conduct when molten", "Brittle", "Soluble in water"], [0,1,2,3], "multi"),
        ("Covalent compounds have:", ["Low melting points", "High melting points", "Conduct electricity", "Are metals"], 0, "mcq"),
        ("Natural gas (CH4) has:", ["ionic bonds", "covalent bonds", "no bonds", "metallic bonds"], 1, "mcq"),
        ("Sodium forms Na+ by losing how many electrons?", "1", None, "short"),
        ("Ionic compounds conduct when:", ["solid", "molten or dissolved", "never", "always"], 1, "mcq"),
        ("Which is covalent?", ["NaCl", "MgO", "CO₂", "CaCl₂"], 2, "mcq"),
        ("Ions held by:", ["electrostatic attraction", "gravity", "magnetism", "nuclear force"], 0, "mcq"),
        ("Diamond is very hard because of:", ["strong covalent bonds", "ionic bonds", "weak forces", "metallic bonds"], 0, "mcq"),
        ("Magnesium forms Mg2+ by:", ["losing 2 electrons", "gaining 2 electrons", "sharing 2 electrons", "splitting"], 0, "mcq"),
        ("Which conducts as solid?", ["Salt (NaCl)", "Sugar", "Copper wire", "Plastic"], 2, "mcq")
    ]
}

print("Updating exercises for Chemistry chapters (1-5)...\n")

for chapter in chapters:
    chapter_id = chapter["id"]
    if chapter_id in exercise_data:
        exercises = []
        for q_num, q_data in enumerate(exercise_data[chapter_id], 1):
            difficulty = "easy" if q_num <= 5 else ("medium" if q_num <= 10 else "hard")

            prompt, choices_or_answer, answer_or_none, q_type = q_data

            if q_type == "short":
                exercise = {
                    "id": f"{chapter_id.replace('-sec2', '')}-q{q_num}",
                    "type": "short",
                    "difficulty": difficulty,
                    "prompt": prompt,
                    "prompt_zh": f"[{chapter['title']} - 问题 {q_num}]",
                    "answer": choices_or_answer,
                    "validator": "exact",
                    "hint": "Review the section notes.",
                    "hint_zh": "查看章节注释。"
                }
            elif q_type == "multi":
                exercise = {
                    "id": f"{chapter_id.replace('-sec2', '')}-q{q_num}",
                    "type": "multi",
                    "difficulty": difficulty,
                    "prompt": prompt,
                    "prompt_zh": f"[{chapter['title']} - 问题 {q_num}]",
                    "choices": choices_or_answer,
                    "answers": answer_or_none,
                    "hint": "Select all correct answers.",
                    "hint_zh": "选择所有正确答案。"
                }
            else:  # mcq
                exercise = {
                    "id": f"{chapter_id.replace('-sec2', '')}-q{q_num}",
                    "type": "mcq",
                    "difficulty": difficulty,
                    "prompt": prompt,
                    "prompt_zh": f"[{chapter['title']} - 问题 {q_num}]",
                    "choices": choices_or_answer,
                    "answer": answer_or_none,
                    "hint": "Think about the key concepts.",
                    "hint_zh": "想想关键概念。"
                }

            exercises.append(exercise)

        chapter["exercises"] = exercises
        print(f"✓ {chapter['title']}: {len(exercises)} exercises updated")

# Save
with open('chapters/science-sec2-chapters.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, indent=2, ensure_ascii=False)

print("\n✅ Chemistry chapters updated successfully!")
