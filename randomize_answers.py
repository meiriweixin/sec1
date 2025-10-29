import json
import random

# Set seed for reproducibility but get different results each time
random.seed()

with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('🔄 Randomizing MCQ answers across all chapters...')
print()

total_randomized = 0

for subject in data['subjects']:
    if subject['id'] == 'ai-playground':
        continue

    for chapter in subject.get('chapters', []):
        chapter_randomized = 0

        for ex in chapter.get('exercises', []):
            if ex['type'] == 'mcq':
                # Store original data
                old_choices = ex['choices'][:]
                old_answer = ex['answer']
                correct_choice = old_choices[old_answer]

                # Create list of indices and shuffle
                indices = list(range(len(old_choices)))
                random.shuffle(indices)

                # Reorder choices
                ex['choices'] = [old_choices[i] for i in indices]

                # Reorder Chinese choices if they exist
                if 'choices_zh' in ex:
                    old_choices_zh = ex['choices_zh'][:]
                    ex['choices_zh'] = [old_choices_zh[i] for i in indices]

                # Find new position of correct answer
                ex['answer'] = ex['choices'].index(correct_choice)

                if ex['answer'] != old_answer:
                    chapter_randomized += 1
                    total_randomized += 1

        if chapter_randomized > 0:
            title = chapter['title'][:50]
            print(f'  ✅ {title:50} | Randomized {chapter_randomized} answers')

# Save
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print()
print(f'✨ Successfully randomized {total_randomized} MCQ answers across all chapters!')
