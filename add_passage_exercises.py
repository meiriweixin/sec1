import json
from datetime import datetime

# Create backup
backup_path = f"src/data/content-backup-passages-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open(backup_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"✓ Backup created: {backup_path}")

# ===== ENGLISH READING PASSAGES =====

# Passage 1: Marina Bay Sands (5 questions)
passage1 = """Marina Bay Sands is one of Singapore's most iconic landmarks. Completed in 2010, this integrated resort features three 55-story towers topped by a massive rooftop terrace called the SkyPark. The SkyPark, which resembles a ship, spans all three towers and includes an infinity pool, gardens, and observation deck with breathtaking views of the city skyline.

The resort cost approximately S$8 billion to build, making it one of the world's most expensive buildings. It houses a luxury hotel with 2,560 rooms, a massive shopping mall with over 300 stores, a museum, theaters, and one of Asia's largest casinos. The building's unique architecture has made it instantly recognizable worldwide.

What makes Marina Bay Sands truly special is how it transformed Singapore's waterfront. Before its construction, Marina Bay was relatively quiet. Now, it serves as the centerpiece of Singapore's downtown area, hosting major events like the Formula One night race and National Day celebrations. The light and water show, Spectra, performed nightly at the Event Plaza, attracts thousands of visitors.

However, the development has not been without controversy. Environmental groups initially opposed the project, concerned about its impact on marine life in Marina Bay. Critics also questioned whether Singapore needed such an expensive casino resort. Despite these concerns, Marina Bay Sands has become a significant contributor to Singapore's tourism industry, attracting millions of visitors annually."""

eng_passage1_exercises = [
    {
        'id': 'eng-pass1-q1',
        'type': 'mcq',
        'prompt': f'Read the passage:\n\n{passage1}\n\nQuestion 1: What is the main purpose of this passage?',
        'prompt_zh': f'Read the passage:\n\n{passage1}\n\nQuestion 1: What is the main purpose of this passage?',
        'choices': [
            'To describe Marina Bay Sands and its impact on Singapore',
            'To criticize the construction of expensive buildings',
            'To promote tourism to Singapore',
            'To explain how casinos operate in Asia'
        ],
        'choices_zh': [
            'To describe Marina Bay Sands and its impact on Singapore',
            'To criticize the construction of expensive buildings',
            'To promote tourism to Singapore',
            'To explain how casinos operate in Asia'
        ],
        'answer': 0,
        'explanation': 'The passage provides a comprehensive overview of Marina Bay Sands, covering its features, cost, significance, and impact on Singapore, making option A the main purpose.',
        'explanation_zh': 'The passage provides a comprehensive overview of Marina Bay Sands, covering its features, cost, significance, and impact on Singapore, making option A the main purpose.',
        'validator': 'smart'
    },
    {
        'id': 'eng-pass1-q2',
        'type': 'short',
        'prompt': 'Question 2: According to the passage, what is the SkyPark compared to in terms of its appearance?',
        'prompt_zh': 'Question 2: According to the passage, what is the SkyPark compared to in terms of its appearance?',
        'answer': 'a ship',
        'answer_zh': 'a ship',
        'hint': 'Look for a comparison in the first paragraph.',
        'hint_zh': 'Look for a comparison in the first paragraph.',
        'explanation': 'The passage states that the SkyPark resembles a ship.',
        'explanation_zh': 'The passage states that the SkyPark resembles a ship.',
        'validator': 'smart'
    },
    {
        'id': 'eng-pass1-q3',
        'type': 'mcq',
        'prompt': 'Question 3: What can be inferred about Marina Bay before Marina Bay Sands was built?',
        'prompt_zh': 'Question 3: What can be inferred about Marina Bay before Marina Bay Sands was built?',
        'choices': [
            'It was less active and not a major attraction',
            'It was the busiest area in Singapore',
            'It already hosted Formula One races',
            'It had many expensive hotels'
        ],
        'choices_zh': [
            'It was less active and not a major attraction',
            'It was the busiest area in Singapore',
            'It already hosted Formula One races',
            'It had many expensive hotels'
        ],
        'answer': 0,
        'explanation': 'The passage states that Marina Bay was relatively quiet before construction, implying it was less active.',
        'explanation_zh': 'The passage states that Marina Bay was relatively quiet before construction, implying it was less active.',
        'validator': 'smart'
    },
    {
        'id': 'eng-pass1-q4',
        'type': 'multi',
        'prompt': 'Question 4: Which concerns about the project are mentioned in the passage? (Select all that apply)',
        'prompt_zh': 'Question 4: Which concerns about the project are mentioned in the passage? (Select all that apply)',
        'choices': [
            'Environmental impact on marine life',
            'The need for an expensive casino resort',
            'Traffic congestion',
            'Safety concerns about the building design'
        ],
        'choices_zh': [
            'Environmental impact on marine life',
            'The need for an expensive casino resort',
            'Traffic congestion',
            'Safety concerns about the building design'
        ],
        'answer': [0, 1],
        'explanation': 'The passage mentions environmental groups concerned about marine life and critics questioning the need for an expensive casino resort. Traffic and safety are not mentioned.',
        'explanation_zh': 'The passage mentions environmental groups concerned about marine life and critics questioning the need for an expensive casino resort. Traffic and safety are not mentioned.',
        'validator': 'smart'
    },
    {
        'id': 'eng-pass1-q5',
        'type': 'mcq',
        'prompt': 'Question 5: What is the author\'s overall tone toward Marina Bay Sands?',
        'prompt_zh': 'Question 5: What is the author\'s overall tone toward Marina Bay Sands?',
        'choices': [
            'Balanced - presenting both benefits and concerns',
            'Completely positive - only praising the building',
            'Highly critical - focusing on problems',
            'Neutral - providing only facts without opinion'
        ],
        'choices_zh': [
            'Balanced - presenting both benefits and concerns',
            'Completely positive - only praising the building',
            'Highly critical - focusing on problems',
            'Neutral - providing only facts without opinion'
        ],
        'answer': 0,
        'explanation': 'The author presents both positive aspects (iconic landmark, tourism benefits) and concerns (environmental impact, controversy), showing a balanced perspective.',
        'explanation_zh': 'The author presents both positive aspects (iconic landmark, tourism benefits) and concerns (environmental impact, controversy), showing a balanced perspective.',
        'validator': 'smart'
    }
]

# Passage 2: Singapore's Education System (5 questions)
passage2 = """Singapore's education system is widely recognized as one of the best in the world. Students consistently rank at the top in international assessments like PISA (Programme for International Student Assessment) in mathematics, science, and reading. This success did not happen by accident—it is the result of careful planning, significant investment, and a strong emphasis on teacher quality.

The journey through Singapore's education begins with six years of primary school, followed by four to five years of secondary school. Students then have various pathways: Junior Colleges for pre-university education, polytechnics for diploma courses, or the Institute of Technical Education (ITE) for technical skills. This multiple-pathway system ensures that students can pursue education suited to their strengths and interests.

One distinctive feature of Singapore's system is its bilingual policy. All students learn English as the medium of instruction and their Mother Tongue (Chinese, Malay, or Tamil) as a second language. This policy aims to keep students connected to their cultural roots while equipping them with English proficiency for the global economy. However, some educators argue that the emphasis on two languages creates excessive pressure on students.

Despite international acclaim, the system faces criticism domestically. Many parents and students complain about the intense pressure to excel academically. The competition for places in top schools is fierce, leading some families to spend heavily on private tuition. In recent years, the Ministry of Education has taken steps to reduce this pressure, introducing more flexible assessment methods and reducing the emphasis on examinations.

Looking ahead, Singapore's education system continues to evolve. There is growing recognition that 21st-century skills like creativity, critical thinking, and collaboration are as important as academic excellence. The challenge for Singapore is to maintain its academic standards while fostering a more holistic approach to education."""

eng_passage2_exercises = [
    {
        'id': 'eng-pass2-q1',
        'type': 'mcq',
        'prompt': f'Read the passage:\n\n{passage2}\n\nQuestion 1: According to the passage, why is Singapore\'s education system successful?',
        'prompt_zh': f'Read the passage:\n\n{passage2}\n\nQuestion 1: According to the passage, why is Singapore\'s education system successful?',
        'choices': [
            'Careful planning, investment, and focus on teacher quality',
            'Long school hours and strict discipline',
            'Expensive private tuition centers',
            'Natural talent of Singaporean students'
        ],
        'choices_zh': [
            'Careful planning, investment, and focus on teacher quality',
            'Long school hours and strict discipline',
            'Expensive private tuition centers',
            'Natural talent of Singaporean students'
        ],
        'answer': 0,
        'explanation': 'The passage explicitly states that success is the result of careful planning, significant investment, and a strong emphasis on teacher quality.',
        'explanation_zh': 'The passage explicitly states that success is the result of careful planning, significant investment, and a strong emphasis on teacher quality.',
        'validator': 'smart'
    },
    {
        'id': 'eng-pass2-q2',
        'type': 'short',
        'prompt': 'Question 2: What are the three pathways students can take after secondary school?',
        'prompt_zh': 'Question 2: What are the three pathways students can take after secondary school?',
        'answer': 'Junior Colleges, polytechnics, ITE',
        'answer_zh': 'Junior Colleges, polytechnics, ITE',
        'hint': 'Look in the second paragraph for the three options.',
        'hint_zh': 'Look in the second paragraph for the three options.',
        'explanation': 'The passage lists Junior Colleges (pre-university), polytechnics (diploma courses), and ITE (technical skills) as the three pathways.',
        'explanation_zh': 'The passage lists Junior Colleges (pre-university), polytechnics (diploma courses), and ITE (technical skills) as the three pathways.',
        'validator': 'smart'
    },
    {
        'id': 'eng-pass2-q3',
        'type': 'mcq',
        'prompt': 'Question 3: What is the purpose of the bilingual policy?',
        'prompt_zh': 'Question 3: What is the purpose of the bilingual policy?',
        'choices': [
            'To maintain cultural connections while providing global English proficiency',
            'To make students study harder',
            'To prepare students for overseas education',
            'To compete with other countries'
        ],
        'choices_zh': [
            'To maintain cultural connections while providing global English proficiency',
            'To make students study harder',
            'To prepare students for overseas education',
            'To compete with other countries'
        ],
        'answer': 0,
        'explanation': 'The passage states the policy aims to keep students connected to cultural roots while equipping them with English proficiency for the global economy.',
        'explanation_zh': 'The passage states the policy aims to keep students connected to cultural roots while equipping them with English proficiency for the global economy.',
        'validator': 'smart'
    },
    {
        'id': 'eng-pass2-q4',
        'type': 'multi',
        'prompt': 'Question 4: What criticisms of the education system are mentioned? (Select all that apply)',
        'prompt_zh': 'Question 4: What criticisms of the education system are mentioned? (Select all that apply)',
        'choices': [
            'Intense academic pressure on students',
            'Fierce competition for top schools',
            'Poor quality teachers',
            'Lack of technology in classrooms'
        ],
        'choices_zh': [
            'Intense academic pressure on students',
            'Fierce competition for top schools',
            'Poor quality teachers',
            'Lack of technology in classrooms'
        ],
        'answer': [0, 1],
        'explanation': 'The passage mentions intense pressure to excel and fierce competition for top schools. Teacher quality is actually cited as a strength, and technology is not discussed.',
        'explanation_zh': 'The passage mentions intense pressure to excel and fierce competition for top schools. Teacher quality is actually cited as a strength, and technology is not discussed.',
        'validator': 'smart'
    },
    {
        'id': 'eng-pass2-q5',
        'type': 'short',
        'prompt': 'Question 5: According to the passage, what skills are becoming as important as academic excellence?',
        'prompt_zh': 'Question 5: According to the passage, what skills are becoming as important as academic excellence?',
        'answer': 'creativity, critical thinking, collaboration',
        'answer_zh': 'creativity, critical thinking, collaboration',
        'hint': 'Look in the final paragraph for 21st-century skills.',
        'hint_zh': 'Look in the final paragraph for 21st-century skills.',
        'explanation': 'The passage lists creativity, critical thinking, and collaboration as important 21st-century skills.',
        'explanation_zh': 'The passage lists creativity, critical thinking, and collaboration as important 21st-century skills.',
        'validator': 'smart'
    }
]

# Find English Reading Comprehension chapter
english = next((s for s in data['subjects'] if s['id'] == 'english'), None)
eng_read_ch = next((c for c in english['chapters']
                    if c['id'] == 'reading-comprehension' and c.get('gradeLevel') == 'sec1'), None)

print(f"\nCurrent English Reading Comprehension: {len(eng_read_ch['exercises'])} exercises")

# Add exercises
eng_read_ch['exercises'].extend(eng_passage1_exercises)
eng_read_ch['exercises'].extend(eng_passage2_exercises)

print(f"Added 10 passage-based exercises (2 passages × 5 questions)")
print(f"New count: {len(eng_read_ch['exercises'])} exercises")

# Save
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n✓ English passage exercises integrated!")
print(f"✓ Backup: {backup_path}")
print(f"\nNext: Creating Chinese passage exercises...")
