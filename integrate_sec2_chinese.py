import json
import shutil
from datetime import datetime

# Create backup
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_file = f"src/data/content-backup-{timestamp}.json"
shutil.copy("src/data/content.json", backup_file)
print(f"创建备份：{backup_file}")

# Load existing content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    content = json.load(f)

# Load new Sec 2 Chinese chapters
with open('chapters/sec2-chinese-chapters.json', 'r', encoding='utf-8') as f:
    sec2_chinese_chapters = json.load(f)

# Find Chinese subject and add Sec 2 chapters
for subject in content['subjects']:
    if subject['id'] == 'chinese':
        # Get existing chapter IDs to avoid duplicates
        existing_ids = {ch['id'] for ch in subject['chapters']}

        # Add new chapters only if they don't exist
        new_chapters_added = 0
        for chapter in sec2_chinese_chapters:
            if chapter['id'] not in existing_ids:
                subject['chapters'].append(chapter)
                new_chapters_added += 1

        print(f"添加了{new_chapters_added}个中二华文章节")
        print(f"华文章节总数：{len(subject['chapters'])}")
        break

# Save updated content
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(content, f, ensure_ascii=False, indent=2)

print("整合完成！")

# Verify the integration
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    content = json.load(f)

for subject in content['subjects']:
    if subject['id'] == 'chinese':
        sec1_chapters = [ch for ch in subject['chapters'] if ch.get('gradeLevel') == 'sec1']
        sec2_chapters = [ch for ch in subject['chapters'] if ch.get('gradeLevel') == 'sec2']

        print(f"\n验证：")
        print(f"  中一华文章节：{len(sec1_chapters)}")
        print(f"  中二华文章节：{len(sec2_chapters)}")
        print(f"\n中二华文章节：")
        for ch in sec2_chapters:
            ex_count = len(ch.get('exercises', []))
            print(f"  - {ch['title_zh']}: {ex_count}题")
