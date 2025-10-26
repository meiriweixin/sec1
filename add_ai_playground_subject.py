import json

# Load current content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Check if AI Playground already exists
ai_exists = any(subject['id'] == 'ai-playground' for subject in data['subjects'])

if not ai_exists:
    # Add AI Playground as a subject
    ai_playground_subject = {
        "id": "ai-playground",
        "title": "AI Playground",
        "title_zh": "AI 游乐场",
        "description": "Explore AI through hands-on activities with text, images, music, video, and code",
        "description_zh": "通过文本、图像、音乐、视频和代码的实践活动探索人工智能",
        "color": "purple",
        "isAIPlayground": True,
        "chapters": []  # AI Playground uses ai-modules.json instead
    }

    data['subjects'].append(ai_playground_subject)

    # Save updated content
    with open('src/data/content.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("✓ Added AI Playground subject to content.json")
    print(f"Total subjects: {len(data['subjects'])}")
else:
    print("AI Playground subject already exists in content.json")
