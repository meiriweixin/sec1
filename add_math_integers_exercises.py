import json

# Load current content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find Math subject and Integers & Rational Numbers chapter
for subject in data['subjects']:
    if subject['id'] == 'math':
        for chapter in subject['chapters']:
            if chapter['id'] == 'integers-rational-numbers':
                # Add 1 new exercise
                new_exercises = [
                    {
                        "id": "int-ex15",
                        "type": "mcq",
                        "difficulty": "hard",
                        "prompt": "A submarine is at -350m. It descends another 180m, then rises 95m. What is its final depth?",
                        "prompt_zh": "一艘潜水艇在-350米处。它再下降180米，然后上升95米。它的最终深度是多少？",
                        "choices": [
                            "-435m",
                            "-255m",
                            "-625m",
                            "-165m"
                        ],
                        "choices_zh": [
                            "-435米",
                            "-255米",
                            "-625米",
                            "-165米"
                        ],
                        "answer": 0,
                        "explanation": "Start: -350, descend 180: -350 - 180 = -530, rise 95: -530 + 95 = -435m",
                        "explanation_zh": "开始：-350，下降180：-350 - 180 = -530，上升95：-530 + 95 = -435米"
                    }
                ]

                # Extend existing exercises
                chapter['exercises'].extend(new_exercises)
                print(f"Added {len(new_exercises)} exercise to Integers & Rational Numbers")
                print(f"Total exercises now: {len(chapter['exercises'])}")

# Save updated content
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✓ Integers & Rational Numbers exercises updated successfully!")
