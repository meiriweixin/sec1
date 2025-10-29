import json
import shutil
from datetime import datetime

# Create backup
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
backup_path = f'src/data/content-backup-{timestamp}.json'
shutil.copy('src/data/content.json', backup_path)
print(f'✅ Backup created: {backup_path}')

# Load existing content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find Science subject
science = None
for subject in data['subjects']:
    if subject['id'] == 'science':
        science = subject
        break

print(f'\n📚 Current Science chapters: {len(science["chapters"])}')

# Create Electrical Systems chapter (English only, minimal content)
electrical_systems = {
    "id": "electrical-systems",
    "title": "Electrical Systems",
    "title_zh": "电路系统",
    "gradeLevel": "sec1",
    "tag": "Physics",
    "tag_zh": "物理",
    "description": "Understanding current, voltage, resistance, and electrical circuits",
    "description_zh": "理解电流、电压、电阻和电路",
    "objectives": [
        "Understand current, voltage, and resistance",
        "Draw circuit diagrams",
        "Explain effects of electric current",
        "Calculate electrical power and energy",
        "Identify electrical hazards"
    ],
    "objectives_zh": ["英文版本"],
    "sections": [
        {
            "type": "text",
            "content": "# Electrical Systems\n\nElectricity powers our modern world.\n\n## Current, Voltage, Resistance\n\n- **Current (I)**: Flow of electrons, measured in Amperes (A)\n- **Voltage (V)**: Electrical push, measured in Volts (V)\n- **Resistance (R)**: Opposition to current, measured in Ohms (Ω)\n\n## Singapore Context\nHDB flats use 230V AC electricity.",
            "content_zh": "英文版本"
        }
    ],
    "exercises": [
        {
            "id": "elec-ex1",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "What is the SI unit for electric current?",
            "prompt_zh": "电流的单位是什么？",
            "choices": ["Ampere", "Volt", "Ohm", "Watt"],
            "choices_zh": ["安培", "伏特", "欧姆", "瓦特"],
            "answer": 0,
            "explanation": "Electric current is measured in Amperes (A).",
            "explanation_zh": "电流用安培测量"
        }
    ]
}

# Create Physical Properties chapter
physical_properties = {
    "id": "physical-properties",
    "title": "Physical Properties of Matter",
    "title_zh": "物质的物理性质",
    "gradeLevel": "sec1",
    "tag": "Chemistry",
    "tag_zh": "化学",
    "description": "Identifying materials by physical properties",
    "description_zh": "通过物理性质识别材料",
    "objectives": [
        "Identify materials by physical properties",
        "Understand conductivity",
        "Calculate density",
        "Measure properties accurately"
    ],
    "objectives_zh": ["英文版本"],
    "sections": [
        {
            "type": "text",
            "content": "# Physical Properties\n\nPhysical properties help identify materials.\n\n## Key Properties\n\n1. **Electrical Conductivity**: Can it conduct electricity?\n2. **Thermal Conductivity**: Can it conduct heat?\n3. **Density**: Mass per unit volume\n\n## Density Formula\n\nDensity = Mass / Volume\n\n## Singapore Examples\n- HDB buildings use steel (strong)\n- MRT tracks use steel (hard)\n- Water pipes use PVC (doesn't rust)",
            "content_zh": "英文版本"
        }
    ],
    "exercises": [
        {
            "id": "phys-ex1",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "Which is a physical property?",
            "prompt_zh": "哪个是物理性质？",
            "choices": ["Flammability", "Density", "Reactivity", "Rusting"],
            "choices_zh": ["可燃性", "密度", "反应性", "生锈"],
            "answer": 1,
            "explanation": "Density is a physical property.",
            "explanation_zh": "密度是物理性质"
        }
    ]
}

print('✅ Created both chapters (minimal English-only versions)')

# Insert Physical Properties after scientific-methods (index 1)
science['chapters'].insert(1, physical_properties)
print(f'✅ Inserted Physical Properties at index 1')

# Find digestive-system and insert Electrical Systems before it
digestive_index = None
for i, ch in enumerate(science['chapters']):
    if ch['id'] == 'digestive-system':
        digestive_index = i
        break

if digestive_index:
    science['chapters'].insert(digestive_index, electrical_systems)
    print(f'✅ Inserted Electrical Systems at index {digestive_index}')
else:
    science['chapters'].append(electrical_systems)
    print('✅ Appended Electrical Systems at end')

# Save
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'\n🎉 SUCCESS! Integrated 2 new chapters')
print(f'📊 Total Science chapters: {len(science["chapters"])}')
print('\n💡 Note: Chinese content shows "英文版本" placeholder')
print('   You can add full Chinese translations later')

