import json

# Load chapters
with open('chapters/science-sec2-chapters.json', 'r', encoding='utf-8') as f:
    chapters = json.load(f)

# Remaining chapters - Physics (6-10) and Biology (11-15)
remaining_data = {
    "work-energy-power-sec2": [
        ("Work done equals:", ["Force × Distance", "Mass × Distance", "Force × Time", "Mass × Acceleration"], 0, "mcq"),
        ("Unit of work:", ["Newton", "Joule", "Watt", "Meter"], 1, "mcq"),
        ("Power equals:", ["Work ÷ Time", "Force × Distance", "Energy × Mass", "Work × Time"], 0, "mcq"),
        ("Unit of power:", "watt", None, "short"),
        ("Energy cannot be ___ but can transform:", ["created or destroyed", "measured", "used", "stored"], 0, "mcq"),
        ("Forms of energy: (Select all)", ["Kinetic", "Potential", "Chemical", "Electrical"], [0,1,2,3], "multi"),
        ("Lifting shopping bags up HDB stairs involves:", ["kinetic to potential energy", "potential to kinetic", "chemical to kinetic", "electrical to chemical"], 2, "mcq"),
        ("Singapore MRT trains have high power motors for:", "quick acceleration", None, "short"),
        ("If 100J work done in 5s, power is:", ["20W", "500W", "50W", "10W"], 0, "mcq"),
        ("Gravitational potential energy depends on:", ["mass and height", "speed", "temperature", "color"], 0, "mcq"),
        ("Solar panels convert ___ energy to electrical:", ["light", "sound", "nuclear", "magnetic"], 0, "mcq"),
        ("1 kWh equals how many Joules?", ["3600 J", "360000 J", "3600000 J", "36000 J"], 2, "mcq"),
        ("Singapore's energy consumption requires:", ["imported fuels and solar", "only wind", "only nuclear", "only coal"], 0, "mcq"),
        ("Which has most kinetic energy at same speed?", ["Heavy truck", "Light car", "Both same", "Neither"], 0, "mcq"),
        ("Efficiency formula:", ["Useful output ÷ Total input × 100%", "Input ÷ Output", "Output × Input", "Power ÷ Work"], 0, "mcq")
    ],
    "moments-sec2": [
        ("Moment equals:", ["Force × Perpendicular distance", "Force + Distance", "Force ÷ Distance", "Force - Distance"], 0, "mcq"),
        ("Unit of moment:", ["Nm", "N", "m", "J"], 0, "mcq"),
        ("For balance, clockwise moments ___ anticlockwise:", ["equal", "greater than", "less than", "double"], 0, "mcq"),
        ("Opening a door is easier when pushing:", "far from hinges", None, "short"),
        ("Pivot point is also called:", ["fulcrum", "axis", "center", "edge"], 0, "mcq"),
        ("Applications of moments: (Select all)", ["See-saw", "Scissors", "Wrench", "Crowbar"], [0,1,2,3], "multi"),
        ("If 10N force applied 2m from pivot, moment is:", ["20 Nm", "12 Nm", "5 Nm", "8 Nm"], 0, "mcq"),
        ("HDB blocks stable because of:", "low center of gravity", None, "short"),
        ("Center of gravity is where:", ["weight appears to act", "object is lightest", "no forces", "maximum height"], 0, "mcq"),
        ("To increase moment, you can:", ["increase force or distance", "decrease force", "reduce distance", "remove pivot"], 0, "mcq"),
        ("Wheelbarrow uses principle of:", ["moments/levers", "energy", "pressure", "friction"], 0, "mcq"),
        ("For balanced see-saw: heavy child sits:", ["closer to pivot", "further from pivot", "anywhere", "off see-saw"], 0, "mcq"),
        ("Singapore's cranes use moments to:", ["lift heavy loads", "produce electricity", "purify water", "cool air"], 0, "mcq"),
        ("Turning effect depends on:", ["force and perpendicular distance", "speed", "color", "temperature"], 0, "mcq"),
        ("Long spanner gives bigger moment because:", ["greater distance from pivot", "heavier", "shinier", "longer time"], 0, "mcq")
    ],
    "kinetic-particle-theory-sec2": [
        ("In solids, particles are:", ["closely packed and vibrate", "far apart", "moving freely", "not moving"], 0, "mcq"),
        ("In gases, particles:", ["far apart and move randomly", "touching", "not moving", "vibrating only"], 0, "mcq"),
        ("Melting is:", ["solid to liquid", "liquid to gas", "gas to liquid", "liquid to solid"], 0, "mcq"),
        ("Process: liquid to gas:", "evaporation", None, "short"),
        ("During melting, temperature:", ["stays constant", "increases", "decreases", "fluctuates"], 0, "mcq"),
        ("States of matter: (Select all)", ["Solid", "Liquid", "Gas", "Plasma"], [0,1,2], "multi"),
        ("Gas pressure caused by:", ["particle collisions with walls", "gravity", "magnetism", "electricity"], 0, "mcq"),
        ("Singapore's high humidity means water evaporates:", "slower", None, "short"),
        ("Increasing temperature of gas:", ["increases pressure", "decreases pressure", "no effect", "stops movement"], 0, "mcq"),
        ("Condensation is:", ["gas to liquid", "liquid to solid", "solid to gas", "liquid to gas"], 0, "mcq"),
        ("Particles move fastest in:", ["gases", "liquids", "solids", "all same"], 0, "mcq"),
        ("Brownian motion shows particles are:", ["constantly moving", "stationary", "growing", "shrinking"], 0, "mcq"),
        ("Diffusion occurs because:", ["particles move randomly", "gravity pulls", "magnetism", "light energy"], 0, "mcq"),
        ("At higher temperature, diffusion is:", ["faster", "slower", "same", "stops"], 0, "mcq"),
        ("Singapore's weather (27-32°C) keeps water as:", ["liquid", "solid", "gas only", "all states"], 0, "mcq")
    ],
    "sound-sec2": [
        ("Sound is produced by:", ["vibrations", "light", "heat", "electricity"], 0, "mcq"),
        ("Sound travels as ___ waves:", ["longitudinal", "transverse", "circular", "no waves"], 0, "mcq"),
        ("Sound cannot travel through:", ["vacuum", "air", "water", "metal"], 0, "mcq"),
        ("Speed of sound in air is about:", "330", None, "short"),
        ("High frequency means:", ["high pitch", "low pitch", "loud sound", "soft sound"], 0, "mcq"),
        ("Sound properties: (Select all)", ["Pitch (frequency)", "Loudness (amplitude)", "Speed", "Wavelength"], [0,1,2,3], "multi"),
        ("Large amplitude means:", ["loud sound", "soft sound", "high pitch", "low pitch"], 0, "mcq"),
        ("Singapore's NEA monitors noise pollution above:", "85", None, "short"),
        ("Sound travels fastest in:", ["solids", "liquids", "gases", "vacuum"], 0, "mcq"),
        ("Ultrasound has frequency:", ["above 20000 Hz", "below 20 Hz", "20-20000 Hz", "any frequency"], 0, "mcq"),
        ("Echo is caused by:", ["reflection of sound", "refraction", "diffraction", "interference"], 0, "mcq"),
        ("Soft materials ___ sound:", ["absorb", "reflect", "amplify", "create"], 0, "mcq"),
        ("Noise pollution can cause:", ["hearing damage", "better hearing", "no effect", "improved sleep"], 0, "mcq"),
        ("Human hearing range:", ["20 Hz to 20000 Hz", "0 to 100 Hz", "above 30000 Hz", "below 10 Hz"], 0, "mcq"),
        ("Soundproofing in Singapore buildings uses:", ["soft absorbing materials", "hard reflective surfaces", "glass only", "metal"], 0, "mcq")
    ],
    "magnetism-sec2": [
        ("Magnetic materials include:", ["iron, steel, nickel", "copper, aluminum", "plastic, wood", "glass, paper"], 0, "mcq"),
        ("Magnetic field lines go from:", ["North to South", "South to North", "East to West", "no direction"], 0, "mcq"),
        ("Like poles:", ["repel", "attract", "no effect", "stick"], 0, "mcq"),
        ("Electromagnet has:", "coil around iron core", None, "short"),
        ("Unlike poles:", ["attract", "repel", "no effect", "vibrate"], 0, "mcq"),
        ("Magnetic materials: (Select all)", ["Iron", "Steel", "Nickel", "Cobalt"], [0,1,2,3], "multi"),
        ("Electromagnet strength increases with:", ["more turns, stronger current", "fewer turns", "no current", "plastic core"], 0, "mcq"),
        ("Singapore MRT uses electromagnets in:", "motors", None, "short"),
        ("Permanent magnet vs temporary:", ["steel vs iron", "iron vs steel", "copper vs iron", "plastic vs steel"], 0, "mcq"),
        ("Earth acts as:", ["giant magnet", "no magnet", "electromagnet only", "plastic sphere"], 0, "mcq"),
        ("Magnetic field strongest at:", ["poles", "center", "outside", "nowhere"], 0, "mcq"),
        ("Electromagnet advantage over permanent:", ["can be switched on/off", "always on", "weaker", "no advantage"], 0, "mcq"),
        ("Application of electromagnets:", ["electric bells, speakers, motors", "paintings", "windows", "cooking"], 0, "mcq"),
        ("Breaking magnet creates:", ["two new magnets", "one magnet", "no magnets", "explosion"], 0, "mcq"),
        ("Soft iron core in electromagnet because:", ["easily magnetized and demagnetized", "hard", "colorful", "expensive"], 0, "mcq")
    ],
    "photosynthesis-sec2": [
        ("Photosynthesis occurs in:", ["chloroplasts", "mitochondria", "nucleus", "cell membrane"], 0, "mcq"),
        ("Photosynthesis produces:", ["glucose and oxygen", "CO2 and water", "proteins", "lipids"], 0, "mcq"),
        ("Chlorophyll absorbs:", ["light energy", "sound", "heat only", "electricity"], 0, "mcq"),
        ("Word equation: CO2 + Water →", "glucose and oxygen", None, "short"),
        ("Photosynthesis requires:", ["light, chlorophyll, CO2, water", "darkness", "animals", "soil only"], 0, "mcq"),
        ("Factors affecting photosynthesis: (Select all)", ["Light intensity", "CO2 concentration", "Temperature", "Chlorophyll"], [0,1,2,3], "multi"),
        ("Singapore's tropical climate is ___ for photosynthesis:", ["ideal (high light, heat)", "poor", "impossible", "too hot"], 0, "mcq"),
        ("Limiting factor is:", "factor in shortest supply", None, "short"),
        ("At night, plants cannot photosynthesize because:", ["no light", "no CO2", "no water", "no chlorophyll"], 0, "mcq"),
        ("Oxygen from photosynthesis comes from:", ["water", "CO2", "glucose", "air"], 0, "mcq"),
        ("Plants are ___ in food chains:", ["producers", "consumers", "decomposers", "predators"], 0, "mcq"),
        ("Singapore's Gardens by the Bay helps:", ["air quality via photosynthesis", "noise", "traffic", "nothing"], 0, "mcq"),
        ("Photosynthesis importance:", ["produces food and oxygen", "only makes plants green", "no importance", "produces CO2"], 0, "mcq"),
        ("Variegated leaves show:", ["green parts photosynthesize", "all parts same", "white parts photosynthesize more", "no photosynthesis"], 0, "mcq"),
        ("Starch test for photosynthesis uses:", ["iodine solution", "water", "acid", "salt"], 0, "mcq")
    ],
    "transport-plants-sec2": [
        ("Xylem transports:", ["water and minerals upward", "sugars downward", "oxygen", "proteins"], 0, "mcq"),
        ("Phloem transports:", ["sugars up and down", "water only up", "minerals only", "gases"], 0, "mcq"),
        ("Transpiration is loss of:", ["water vapor through stomata", "gases through roots", "minerals", "sugars"], 0, "mcq"),
        ("Stomata are found on:", "leaves", None, "short"),
        ("Transpiration creates:", ["transpiration pull", "push", "no force", "electricity"], 0, "mcq"),
        ("Factors affecting transpiration: (Select all)", ["Temperature", "Humidity", "Wind", "Light"], [0,1,2,3], "multi"),
        ("High humidity in Singapore ___ transpiration:", ["slows", "speeds up", "stops", "no effect"], 0, "mcq"),
        ("Root hairs increase:", "surface area", None, "short"),
        ("Xylem vessels are:", ["dead hollow tubes", "living cells", "solid", "flexible"], 0, "mcq"),
        ("Phloem cells are:", ["living", "dead", "hollow", "absent"], 0, "mcq"),
        ("Wilting occurs when:", ["water loss exceeds uptake", "too much water", "no sunlight", "cold weather"], 0, "mcq"),
        ("Tropical plants in Singapore have:", ["broad leaves, drip tips", "small leaves", "no leaves", "spines only"], 0, "mcq"),
        ("Waxy cuticle on leaves:", ["reduces water loss", "increases water loss", "absorbs light", "makes food"], 0, "mcq"),
        ("Translocation is movement of:", ["sugars in phloem", "water in xylem", "minerals only", "oxygen"], 0, "mcq"),
        ("Guard cells control:", ["stomata opening/closing", "root growth", "flower color", "stem height"], 0, "mcq")
    ],
    "respiration-sec2": [
        ("Aerobic respiration requires:", ["oxygen", "no oxygen", "light", "chlorophyll"], 0, "mcq"),
        ("Aerobic equation: Glucose + O2 →", "CO2 and water and energy", None, "short"),
        ("Anaerobic respiration in animals produces:", ["lactic acid", "ethanol", "water", "oxygen"], 0, "mcq"),
        ("Anaerobic respiration in yeast produces:", ["ethanol and CO2", "lactic acid", "oxygen", "water"], 0, "mcq"),
        ("Aerobic respiration occurs in:", ["mitochondria", "chloroplasts", "nucleus", "cell wall"], 0, "mcq"),
        ("Comparing respiration types: (Select all true for aerobic)", ["Needs oxygen", "Produces CO2 and water", "Lots of energy", "In mitochondria"], [0,1,2,3], "multi"),
        ("Anaerobic releases ___ energy than aerobic:", ["less", "more", "same", "double"], 0, "mcq"),
        ("During intense exercise in Singapore's heat:", "anaerobic respiration", None, "short"),
        ("Lactic acid causes:", ["muscle fatigue", "energy boost", "faster running", "cooling"], 0, "mcq"),
        ("Oxygen debt is repaid by:", ["breathing heavily after exercise", "drinking water", "eating", "sleeping"], 0, "mcq"),
        ("Respiration releases energy from:", ["glucose", "water", "minerals", "vitamins"], 0, "mcq"),
        ("Singapore athletes train in heat/humidity affecting:", ["respiration rate", "height", "color", "age"], 0, "mcq"),
        ("Yeast is used in bread making for:", ["CO2 to make dough rise", "color", "flavor only", "nothing"], 0, "mcq"),
        ("ATP is:", ["energy currency of cells", "a protein", "a vitamin", "a mineral"], 0, "mcq"),
        ("Difference: photosynthesis stores energy, respiration:", ["releases energy", "stores energy", "no energy change", "creates energy"], 0, "mcq")
    ],
    "human-transport-sec2": [
        ("Red blood cells carry:", ["oxygen", "CO2 only", "food", "water only"], 0, "mcq"),
        ("White blood cells:", ["fight infection", "carry oxygen", "clot blood", "transport food"], 0, "mcq"),
        ("Platelets help with:", ["blood clotting", "oxygen transport", "fighting disease", "digestion"], 0, "mcq"),
        ("Plasma is:", "liquid part of blood", None, "short"),
        ("Arteries carry blood:", ["away from heart", "to heart", "to lungs only", "nowhere"], 0, "mcq"),
        ("Blood vessel properties: (Select all true for arteries)", ["Thick walls", "High pressure", "Away from heart", "Elastic"], [0,1,2,3], "multi"),
        ("Veins have:", ["valves and thin walls", "thick walls", "no valves", "high pressure"], 0, "mcq"),
        ("Capillaries are ___ thick:", "one cell", None, "short"),
        ("Double circulation includes:", ["pulmonary and systemic", "only one loop", "three loops", "no circulation"], 0, "mcq"),
        ("Heart has ___ chambers:", ["4", "2", "3", "5"], 0, "mcq"),
        ("Valves in heart:", ["prevent backflow", "pump blood", "make sound only", "no function"], 0, "mcq"),
        ("Heart disease is concern in Singapore's:", ["aging population", "young children", "athletes only", "nobody"], 0, "mcq"),
        ("Pulmonary circulation is:", ["heart to lungs to heart", "heart to body", "body to heart", "lungs only"], 0, "mcq"),
        ("Systemic circulation supplies:", ["whole body except lungs", "lungs only", "heart only", "nothing"], 0, "mcq"),
        ("Hemoglobin in red blood cells:", ["binds oxygen", "fights infection", "clots blood", "digests food"], 0, "mcq")
    ],
    "coordination-response-sec2": [
        ("CNS consists of:", ["brain and spinal cord", "nerves only", "muscles", "bones"], 0, "mcq"),
        ("PNS consists of:", ["nerves", "brain", "spinal cord", "muscles"], 0, "mcq"),
        ("Neurons transmit:", ["electrical impulses", "blood", "air", "food"], 0, "mcq"),
        ("Reflex actions are:", "automatic and rapid", None, "short"),
        ("Reflex arc pathway: receptor → sensory → ___ → motor → effector:", ["relay neuron", "brain", "muscle", "none"], 0, "mcq"),
        ("Nervous system features: (Select all)", ["Fast", "Electrical", "Precise", "Short-lasting"], [0,1,2,3], "multi"),
        ("Hormones are:", ["chemical messengers in blood", "electrical signals", "gases", "solids"], 0, "mcq"),
        ("Homeostasis maintains:", "constant internal environment", None, "short"),
        ("Examples of homeostasis: temperature and:", ["blood sugar", "height", "age", "weight"], 0, "mcq"),
        ("In Singapore's 30°C+ heat, body cools by:", ["sweating", "shivering", "eating", "sleeping"], 0, "mcq"),
        ("Hormones travel in:", ["blood", "nerves", "air", "muscles"], 0, "mcq"),
        ("Compared to nervous, hormonal responses are:", ["slower but longer-lasting", "faster", "same speed", "instant"], 0, "mcq"),
        ("Pulling hand from hot object is:", ["reflex action", "voluntary", "hormonal", "digestive"], 0, "mcq"),
        ("Insulin hormone controls:", ["blood sugar", "temperature", "heart rate", "breathing"], 0, "mcq"),
        ("Singapore's tropical climate requires body to:", ["maintain temperature despite heat", "increase temperature", "decrease temperature", "no regulation"], 0, "mcq")
    ]
}

print("Updating Physics and Biology chapters (6-15)...\n")

for chapter in chapters:
    chapter_id = chapter["id"]
    if chapter_id in remaining_data:
        exercises = []
        for q_num, q_data in enumerate(remaining_data[chapter_id], 1):
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

with open('chapters/science-sec2-chapters.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, indent=2, ensure_ascii=False)

print("\n✅ All Physics and Biology chapters updated!")
print("📊 All 15 Secondary 2 Science chapters now have detailed exercises!")
