#!/usr/bin/env python3
"""
Enhance Science sections with Singapore-specific context and examples.
Expands minimal sections and adds local real-world applications.
"""

import json
from datetime import datetime

# Singapore-specific content enhancements for Science topics
SINGAPORE_ENHANCEMENTS = {
    # Physics topics
    "light-reflection": {
        "addition": "\n\n**Singapore Applications:**\n\n🔹 **Marina Bay Sands SkyPark**: Uses reflective glass to reduce heat while maintaining views\n🔹 **Singapore Flyer**: Capsules designed with anti-reflective glass for clear photography\n🔹 **Solar panels on HDB rooftops**: Positioned to maximize light reflection and energy capture"
    },

    "heat-temperature": {
        "addition": "\n\n**Singapore Context:**\n\n🔹 **Tropical climate**: Average temperature 27-28°C year-round\n🔹 **Urban heat island effect**: City center 2-3°C warmer than surrounding areas\n🔹 **Cooling systems**: All HDB flats, MRT stations, and buildings use air conditioning\n🔹 **Heat index**: Combines temperature and humidity for \"feels like\" temperature"
    },

    "forces-motion": {
        "addition": "\n\n**Singapore Examples:**\n\n🔹 **MRT trains**: Use friction brakes and regenerative braking to slow down\n🔹 **Singapore Grand Prix**: F1 cars experience forces during acceleration and turns\n🔹 **Changi Airport**: Aircraft require thrust force to overcome air resistance\n🔹 **Sentosa cable cars**: Tension force in cables supports car weight"
    },

    "energy-forms": {
        "addition": "\n\n**Energy in Singapore:**\n\n🔹 **Solar energy**: HDB rooftops with solar panels (SolarNova program)\n🔹 **Tidal energy**: Research at Marina Barrage for future potential\n🔹 **Waste-to-energy**: Incineration plants convert trash to electricity\n🔹 **Energy efficiency**: Green buildings with energy-saving features"
    },

    # Chemistry topics
    "states-matter": {
        "addition": "\n\n**States of Matter in Singapore:**\n\n🔹 **Solid**: Ice cubes in drinks, concrete in buildings\n🔹 **Liquid**: Water in reservoirs (Marina Barrage, MacRitchie), tropical rain\n🔹 **Gas**: Water vapor in humid air (average 84% humidity), exhaust from vehicles\n\n**Singapore example**: Morning dew on grass (gas→liquid condensation)"
    },

    "diffusion": {
        "addition": "\n\n**Diffusion Examples in Singapore:**\n\n🔹 **Hawker centers**: Aroma of cooking food spreads through air particles\n🔹 **Kopi mixing**: Sugar dissolves and diffuses in hot coffee\n🔹 **Air fresheners**: Scent particles diffuse throughout rooms\n🔹 **Haze**: Smoke particles from fires diffuse across region"
    },

    "pure-substances": {
        "addition": "\n\n**Singapore Context:**\n\n**Pure substances:**\n🔹 Distilled water from NEWater plants\n🔹 Table salt (sodium chloride)\n🔹 Gold in jewelry at mustafa Centre\n\n**Mixtures:**\n🔹 Tap water (water + minerals + chlorine)\n🔹 Air (nitrogen + oxygen + others)\n🔹 Kaya toast (bread + kaya + butter)"
    },

    "water-purification": {
        "addition": "\n\n**Singapore's Water Story:**\n\n**NEWater Process:**\n1. **Microfiltration**: Removes suspended solids\n2. **Reverse osmosis**: Removes dissolved salts and bacteria\n3. **UV disinfection**: Kills remaining microorganisms\n\n**Four National Taps:**\n🔹 Local catchment water (17 reservoirs)\n🔹 Imported water from Johor\n🔹 NEWater (recycled water)\n🔹 Desalinated water\n\n**Marina Barrage**: Freshwater reservoir and flood control"
    },

    # Biology topics
    "cell-structure": {
        "addition": "\n\n**Cells in Singapore Context:**\n\n🔹 **Plant cells**: Orchid cells (Singapore's national flower)\n🔹 **Animal cells**: Cells in chicken rice, fish from fish farms\n🔹 **Research**: A*STAR institutes study stem cells and cancer cells\n🔹 **Microscopy**: Science Centre Singapore has electron microscopes"
    },

    "photosynthesis": {
        "addition": "\n\n**Photosynthesis in Singapore:**\n\n**Tropical plants adapt to:**\n🔹 High sunlight intensity year-round\n🔹 High rainfall (average 2,340mm per year)\n🔹 Consistent warm temperatures\n\n**Singapore examples:**\n🔹 **Mangroves at Sungei Buloh**: Photosynthesize in brackish water\n🔹 **Rain trees along roads**: Provide shade while photosynthesizing\n🔹 **Gardens by the Bay Supertrees**: Vertical gardens maximize photosynthesis\n🔹 **Orchids**: Adapt to low light in rainforest understory"
    },

    "food-chains": {
        "addition": "\n\n**Singapore Ecosystems:**\n\n**Mangrove ecosystem (Sungei Buloh):**\nAlgae → Mudskipper → Heron → Python\n\n**Coral reef (Sisters' Islands Marine Park):**\nPhytoplankton → Zooplankton → Small fish → Grouper → Shark\n\n**Forest (Bukit Timah Nature Reserve):**\nLeaves → Caterpillar → Spider → Lizard → Snake → Hawk\n\n**Urban ecosystem:**\nPlants → Grasshopper → House gecko → Cat → (decomposers)"
    },

    "adaptations": {
        "addition": "\n\n**Tropical Adaptations in Singapore:**\n\n**Plants:**\n🔹 **Drip-tip leaves**: Rain trees have pointed leaves for water runoff\n🔹 **Aerial roots**: Mangroves breathe through roots above water\n🔹 **Waxy leaves**: Orchids prevent water loss in hot weather\n\n**Animals:**\n🔹 **Otters**: Webbed feet for swimming in Singapore River\n🔹 **Hornbills**: Large beak to reach fruits in tall trees\n🔹 **Geckos**: Sticky toe pads to climb walls in HDB flats\n🔹 **Macaques**: Omnivorous diet adapts to urban environment"
    },

    "respiration": {
        "addition": "\n\n**Respiration in Daily Life:**\n\n🔹 **Exercise**: Students running at school track use more oxygen\n🔹 **Food digestion**: Body breaks down chicken rice for energy through respiration\n🔹 **Bread making**: Yeast respires anaerobically, producing CO₂ bubbles\n🔹 **Sports**: Athletes at Singapore Sports Hub train to improve aerobic capacity"
    },

    "ecology-human-impact": {
        "addition": "\n\n**Environmental Issues in Singapore:**\n\n**Challenges:**\n🔹 **Limited land**: High population density (8,000 people/km²)\n🔹 **Waste management**: 6.1 million tonnes waste/year\n🔹 **Biodiversity loss**: Habitat destruction from urban development\n🔹 **Climate change**: Rising sea levels threaten low-lying areas\n\n**Solutions:**\n🔹 **Recycling**: Blue bins, e-waste collection points\n🔹 **Nature reserves**: Bukit Timah, Central Catchment protected\n🔹 **Green buildings**: Skyrise greenery, vertical farms\n🔹 **NEWater**: Sustainable water recycling\n🔹 **Public transport**: MRT expansion reduces carbon emissions"
    }
}

def enhance_section_content(section_id, current_content):
    """Add Singapore context to section content"""
    # Check if already enhanced
    if 'Singapore' in current_content and len(current_content) > 300:
        return current_content

    # Find matching enhancement
    for key, enhancement in SINGAPORE_ENHANCEMENTS.items():
        if key.lower() in section_id.lower():
            return current_content + enhancement['addition']

    return current_content


def expand_minimal_sections(chapter_title, section):
    """Expand minimal sections with more detailed content"""
    section_id = section.get('id', '')
    title = section.get('title', '')
    content = section.get('content', '')

    # Skip if already substantial
    if len(content) > 300:
        return content

    # Expand based on topic
    expansions = {
        "laboratory-safety": """**Laboratory Safety Rules:**

Safety in the science lab protects you and others from harm.

**Essential rules:**

1. **Eye protection**: Always wear safety goggles when handling chemicals
2. **Hair and clothing**: Tie back long hair, remove loose jewelry
3. **No food or drink**: Never eat or drink in the laboratory
4. **Follow instructions**: Read procedures carefully before starting
5. **Clean up**: Wash hands after experiments, clean equipment
6. **Report accidents**: Tell teacher immediately about spills or injuries

**Singapore school labs:**

🔹 Fire extinguishers and emergency showers available
🔹 First aid kits in every science room
🔹 Fume cupboards for dangerous chemical experiments
🔹 Safety signs and evacuation routes clearly marked""",

        "si-base-units": content if len(content) > 200 else content + """

**Common SI units in Singapore:**

🔹 **Length**: Meters (m) - MRT track lengths, swimming pool size
🔹 **Mass**: Kilograms (kg) - Body weight, food portions
🔹 **Time**: Seconds (s) - Race timing at Singapore Sports Hub
🔹 **Temperature**: Kelvin/Celsius (K/°C) - Weather reports use °C
🔹 **Current**: Amperes (A) - Electrical appliances rated in A

**Practical examples:**
- Height of Singapore Flyer: 165 m
- Mass of durian: ~2 kg
- Temperature: 27°C average""",

        "cell": content if len(content) > 200 else content + """

**Cell Structure:**

**Animal cells have:**
- Cell membrane (controls what enters/exits)
- Cytoplasm (jelly-like substance)
- Nucleus (controls cell activities, contains DNA)
- Mitochondria (energy production)

**Plant cells also have:**
- Cell wall (rigid support structure)
- Chloroplasts (photosynthesis, contains chlorophyll)
- Vacuole (storage of water and nutrients)

**Size:** Most cells are 10-100 micrometers (need microscope to see)"""
    }

    # Check for matching expansion
    for key, expansion in expansions.items():
        if key in section_id:
            return expansion

    return content


def main():
    content_file = "src/data/content.json"
    backup_file = f"src/data/content-backup-science-{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    print("="*70)
    print("ENHANCING SCIENCE WITH SINGAPORE CONTEXT")
    print("="*70)

    # Read content
    print("\nReading content.json...")
    with open(content_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Backup
    print(f"Creating backup: {backup_file}")
    with open(backup_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Find science subject
    science = next(s for s in data['subjects'] if s['id'] == 'science')

    sections_enhanced = 0
    sections_expanded = 0

    for chapter in science['chapters']:
        for section in chapter.get('sections', []):
            section_id = section.get('id', '')
            original_content = section.get('content', '')
            original_len = len(original_content)

            # Try to expand minimal sections
            expanded = expand_minimal_sections(chapter['title'], section)
            if len(expanded) > len(original_content):
                section['content'] = expanded
                sections_expanded += 1
                print(f"📝 Expanded: {chapter['title']} - {section.get('title', 'Untitled')}")
                continue

            # Try to add Singapore context
            enhanced = enhance_section_content(section_id, original_content)
            if len(enhanced) > original_len:
                section['content'] = enhanced
                sections_enhanced += 1
                print(f"🇸🇬 Added context: {chapter['title']} - {section.get('title', 'Untitled')}")

    # Save
    print(f"\nSaving enhanced content...")
    with open(content_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("\n" + "="*70)
    print("✅ SCIENCE ENHANCEMENT COMPLETE")
    print("="*70)
    print(f"Sections with Singapore context added: {sections_enhanced}")
    print(f"Minimal sections expanded: {sections_expanded}")
    print(f"Total enhancements: {sections_enhanced + sections_expanded}")
    print(f"\nBackup saved: {backup_file}")


if __name__ == '__main__':
    main()
