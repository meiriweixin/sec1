#!/usr/bin/env python3
"""
Create JC Chemistry (H2 Level) - Complete 16 Chapters
JC 1: 8 chapters with lessons and exercises
JC 2: 8 chapters with lessons and exercises
Aligned with Singapore-Cambridge GCE A-Level H2 Chemistry syllabus
"""
import json

# JC 1 Chemistry Chapters (8 chapters)
jc1_chemistry = [
    {
        "id": "atomic-structure-jc1-chem",
        "title": "Atomic Structure",
        "title_zh": "原子结构",
        "gradeLevel": "jc1",
        "description": "Electronic configuration, ionization energy, and periodic trends",
        "description_zh": "电子构型、电离能和周期趋势",
        "objectives": [
            "Understand atomic structure and electron arrangement",
            "Explain trends in ionization energy and atomic radius",
            "Apply knowledge of electronic configuration to chemical behavior"
        ],
        "objectives_zh": [
            "理解原子结构和电子排列",
            "解释电离能和原子半径的趋势",
            "应用电子构型知识解释化学行为"
        ],
        "sections": [
            {
                "id": "electron-config",
                "type": "text",
                "title": "Electronic Configuration",
                "title_zh": "电子构型",
                "content": "**Electronic Configuration** describes how electrons are arranged in atoms.\n\n**Key Principles:**\n1. **Aufbau Principle:** Electrons fill orbitals from lowest to highest energy\n2. **Pauli Exclusion Principle:** Maximum 2 electrons per orbital (opposite spins)\n3. **Hund's Rule:** Electrons occupy orbitals singly before pairing\n\n**Orbital Energy Order:**\n1s < 2s < 2p < 3s < 3p < 4s < 3d < 4p < 5s < 4d < 5p\n\n**Singapore Example:**\nSemiconductor manufacturing in Singapore (like GlobalFoundries) relies on understanding electronic configuration of silicon and dopant atoms. Silicon's configuration (1s² 2s² 2p⁶ 3s² 3p²) makes it ideal for electronic devices.\n\n**Writing Configurations:**\n- Nitrogen (Z=7): 1s² 2s² 2p³\n- Iron (Z=26): 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁶\n- Copper (Z=29): 1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹ 3d¹⁰ (exception for stability)\n\n**Ions:**\n- Na⁺: 1s² 2s² 2p⁶ (loses 3s¹ electron)\n- Cl⁻: 1s² 2s² 2p⁶ 3s² 3p⁶ (gains one electron)\n\n**Note:** Transition metals lose 4s electrons before 3d when forming ions."
            },
            {
                "id": "ionization-energy",
                "type": "text",
                "title": "Ionization Energy",
                "title_zh": "电离能",
                "content": "**Ionization Energy (IE)** is the energy required to remove one mole of electrons from one mole of gaseous atoms.\n\n**First Ionization Energy:**\nM(g) → M⁺(g) + e⁻     ΔH = IE₁\n\n**Factors Affecting IE:**\n1. **Nuclear Charge:** Higher Z → stronger attraction → higher IE\n2. **Distance:** Larger radius → weaker attraction → lower IE\n3. **Shielding:** More inner electrons → less attraction → lower IE\n\n**Periodic Trends:**\n- **Across Period:** IE increases (higher Z, similar shielding)\n- **Down Group:** IE decreases (larger radius, more shielding)\n\n**Successive Ionization Energies:**\nIE₁ < IE₂ < IE₃ < ... (removing from increasingly positive ion)\n\n**Large Jumps:** Indicate removal from new shell\nExample: Magnesium\n- IE₁ = 738 kJ/mol (remove 3s¹)\n- IE₂ = 1451 kJ/mol (remove 3s²)\n- IE₃ = 7733 kJ/mol (HUGE JUMP - remove from 2p⁶)\n\n**Singapore Application:**\nMass spectrometry used in Singapore's pharmaceutical industry (like GSK) uses ionization to analyze drug compounds. Understanding IE helps predict fragmentation patterns."
            },
            {
                "id": "periodic-trends",
                "type": "text",
                "title": "Periodic Trends",
                "title_zh": "周期趋势",
                "content": "**Periodic Trends** show how atomic properties vary across the periodic table.\n\n**1. Atomic Radius**\n- **Across Period:** Decreases (higher Z, same shell)\n- **Down Group:** Increases (more shells)\n\n**2. Ionic Radius**\n- **Cations:** Smaller than parent atom (lost electrons)\n- **Anions:** Larger than parent atom (gained electrons, more repulsion)\n- **Isoelectronic Series:** More protons → smaller radius\n  Example: O²⁻ > F⁻ > Na⁺ > Mg²⁺ (all have 10 electrons)\n\n**3. Electronegativity**\n- **Definition:** Ability to attract bonding electrons\n- **Across Period:** Increases (higher Z)\n- **Down Group:** Decreases (larger radius)\n- **Most electronegative:** Fluorine (4.0)\n\n**4. Metallic Character**\n- **Across Period:** Decreases (non-metals on right)\n- **Down Group:** Increases (easier to lose electrons)\n\n**Singapore Context:**\nSingapore's water treatment (NEWater) uses understanding of ionic radii and electronegativity for:\n- **Reverse Osmosis:** Membranes block larger ions\n- **Ion Exchange:** Resins selectively bind ions based on charge and size\n- **Electronegativity:** Predicts bond polarity in treatment chemicals\n\n**Example Comparisons:**\n- Atomic radius: Li < Na < K (down group)\n- Atomic radius: Na > Mg > Al > Si (across period)\n- Electronegativity: F > O > N > C (across period)"
            }
        ],
        "exercises": []
    },

    {
        "id": "chemical-bonding-jc1-chem",
        "title": "Chemical Bonding",
        "title_zh": "化学键",
        "gradeLevel": "jc1",
        "description": "Ionic, covalent, metallic bonding and molecular shapes",
        "description_zh": "离子键、共价键、金属键和分子形状",
        "objectives": [
            "Explain different types of chemical bonding",
            "Predict molecular shapes using VSEPR theory",
            "Relate bonding to physical properties of substances"
        ],
        "objectives_zh": [
            "解释不同类型的化学键",
            "使用VSEPR理论预测分子形状",
            "将键合与物质的物理性质联系起来"
        ],
        "sections": [
            {
                "id": "bonding-types",
                "type": "text",
                "title": "Types of Chemical Bonds",
                "title_zh": "化学键的类型",
                "content": "**Chemical Bonds** form when atoms achieve stable electron configurations.\n\n**1. Ionic Bonding**\n- **Formation:** Transfer of electrons (metal → non-metal)\n- **Example:** Na⁺Cl⁻ (sodium transfers electron to chlorine)\n- **Properties:**\n  - High melting/boiling points\n  - Conduct electricity when molten/aqueous\n  - Brittle (layers slide, like charges repel)\n\n**2. Covalent Bonding**\n- **Formation:** Sharing of electrons (non-metal + non-metal)\n- **Types:**\n  - **Single bond:** H-H (share 2 electrons)\n  - **Double bond:** O=O (share 4 electrons)\n  - **Triple bond:** N≡N (share 6 electrons)\n- **Properties:**\n  - Lower melting points (simple molecular)\n  - Don't conduct electricity\n  - Can be gases, liquids, or solids\n\n**3. Metallic Bonding**\n- **Structure:** \"Sea\" of delocalized electrons around metal cations\n- **Properties:**\n  - Conduct electricity (mobile electrons)\n  - Malleable and ductile (layers slide)\n  - High melting points (strong bonding)\n\n**Singapore Applications:**\n- **Desalination:** Ionic NaCl separated by osmosis at Tuas plant\n- **Petrochemicals:** Covalent compounds processed at Jurong Island\n- **Electronics:** Metallic bonding in solder (Sn-Pb) for circuit boards\n- **Construction:** Steel reinforcement (metallic Fe) in HDB buildings"
            },
            {
                "id": "vsepr-theory",
                "type": "text",
                "title": "VSEPR Theory & Molecular Shapes",
                "title_zh": "VSEPR理论与分子形状",
                "content": "**VSEPR Theory** (Valence Shell Electron Pair Repulsion) predicts molecular shapes.\n\n**Key Principle:** Electron pairs repel to maximize distance apart.\n\n**Common Molecular Shapes:**\n\n**2 Electron Pairs:**\n- **Linear** (180°): CO₂, BeCl₂\n\n**3 Electron Pairs:**\n- **Trigonal Planar** (120°): BF₃, AlCl₃\n- **Bent** (~120°): SO₂ (1 lone pair)\n\n**4 Electron Pairs:**\n- **Tetrahedral** (109.5°): CH₄, CCl₄\n- **Trigonal Pyramidal** (~107°): NH₃ (1 lone pair)\n- **Bent** (~104.5°): H₂O (2 lone pairs)\n\n**5 Electron Pairs:**\n- **Trigonal Bipyramidal** (90°/120°): PCl₅\n\n**6 Electron Pairs:**\n- **Octahedral** (90°): SF₆\n\n**Lone Pair Repulsion:**\nLone pair-Lone pair > Lone pair-Bond pair > Bond pair-Bond pair\n\n**Bond Angles:**\n- CH₄: 109.5° (no lone pairs)\n- NH₃: 107° (1 lone pair compresses)\n- H₂O: 104.5° (2 lone pairs compress more)\n\n**Singapore Example:**\nSingapore's pharmaceutical companies (Novartis, GSK) design drug molecules considering:\n- **Shape:** Determines how drugs bind to receptors\n- **Polarity:** Affects solubility and delivery\n- **Angles:** Critical for biological activity\n\nWater treatment at NEWater plants depends on H₂O's bent shape → polarity → excellent solvent properties."
            },
            {
                "id": "intermolecular-forces",
                "type": "text",
                "title": "Intermolecular Forces",
                "title_zh": "分子间作用力",
                "content": "**Intermolecular Forces** are attractions between molecules (weaker than bonds).\n\n**Types (Weakest to Strongest):**\n\n**1. Van der Waals (Dispersion Forces)**\n- **Cause:** Temporary dipoles from electron movement\n- **Strength:** Increases with molecular size (more electrons)\n- **Examples:** Noble gases, non-polar molecules (CH₄, C₆H₁₄)\n- **Trend:** He < Ne < Ar < Kr (increasing bp)\n\n**2. Permanent Dipole-Dipole**\n- **Requirement:** Polar molecules\n- **Strength:** Stronger than dispersion\n- **Example:** HCl molecules attract (δ⁺H—Clδ⁻ ↔ δ⁺H—Clδ⁻)\n\n**3. Hydrogen Bonding**\n- **Requirements:**\n  - H bonded to N, O, or F\n  - Lone pair on another N, O, or F\n- **Strength:** Strongest intermolecular force\n- **Examples:**\n  - Water (H₂O): High bp (100°C) despite small size\n  - Ammonia (NH₃): Higher bp than PH₃\n  - DNA: Held together by H-bonds\n\n**Effects on Properties:**\n\n**Boiling Point Trends:**\n- **Alkanes:** CH₄ < C₂H₆ < C₃H₈ (increasing dispersion)\n- **Group 16 Hydrides:** H₂S < H₂Se < H₂Te < H₂O (H₂O anomaly due to H-bonding)\n\n**Solubility:**\n- \"Like dissolves like\"\n- Polar solutes in polar solvents (e.g., NaCl in H₂O)\n- Non-polar solutes in non-polar solvents (e.g., oil in hexane)\n\n**Singapore Applications:**\n- **NEWater Treatment:** H-bonding makes water excellent solvent\n- **Petroleum Refining:** Separating hydrocarbons by bp (Jurong Island)\n- **Pharmaceutical Formulation:** Drug solubility depends on polarity\n- **Humidity Control:** H-bonding between water molecules in Singapore's humid air"
            }
        ],
        "exercises": []
    },

    {
        "id": "states-of-matter-jc1-chem",
        "title": "States of Matter",
        "title_zh": "物质状态",
        "gradeLevel": "jc1",
        "description": "Kinetic theory, phase changes, and gas laws",
        "description_zh": "动理论、相变和气体定律",
        "objectives": [
            "Apply kinetic molecular theory to explain properties of matter",
            "Calculate using ideal gas equation and related laws",
            "Explain phase diagrams and phase transitions"
        ],
        "objectives_zh": [
            "应用分子动理论解释物质性质",
            "使用理想气体方程和相关定律进行计算",
            "解释相图和相变"
        ],
        "sections": [
            {
                "id": "gas-laws",
                "type": "text",
                "title": "Gas Laws",
                "title_zh": "气体定律",
                "content": "**Gas Laws** describe relationships between pressure, volume, temperature, and amount of gas.\n\n**1. Boyle's Law** (T, n constant)\nP₁V₁ = P₂V₂\n- Pressure inversely proportional to volume\n\n**2. Charles's Law** (P, n constant)\nV₁/T₁ = V₂/T₂\n- Volume directly proportional to absolute temperature\n\n**3. Gay-Lussac's Law** (V, n constant)\nP₁/T₁ = P₂/T₂\n- Pressure directly proportional to absolute temperature\n\n**4. Avogadro's Law** (P, T constant)\nV₁/n₁ = V₂/n₂\n- Volume directly proportional to moles\n- 1 mole of any gas = 22.4 L at STP\n\n**5. Ideal Gas Equation**\nPV = nRT\n- P = pressure (Pa or atm)\n- V = volume (m³ or L)\n- n = moles\n- R = gas constant (8.31 J/(mol·K) or 0.0821 L·atm/(mol·K))\n- T = temperature (Kelvin)\n\n**6. Combined Gas Law**\nP₁V₁/T₁ = P₂V₂/T₂\n\n**Singapore Applications:**\n- **Scuba Diving:** Sentosa divers experience pressure changes (Boyle's law)\n- **Aircraft Cabins:** Pressurization at Changi Airport (gas laws)\n- **Industrial Gases:** Air Liquide Singapore stores compressed gases\n- **Weather Balloons:** Meteorological Service uses gas expansion\n\n**Example Calculation:**\nCylinder contains 2.0 mol O₂ at 300K and 1.0 atm. Find volume:\nV = nRT/P = (2.0)(0.0821)(300)/1.0 = 49.3 L"
            },
            {
                "id": "kinetic-theory",
                "type": "text",
                "title": "Kinetic Molecular Theory",
                "title_zh": "分子动理论",
                "content": "**Kinetic Molecular Theory (KMT)** explains gas behavior at molecular level.\n\n**Assumptions:**\n1. Gas particles in constant, random motion\n2. Negligible particle volume compared to container\n3. No intermolecular forces\n4. Elastic collisions (no energy lost)\n5. Average kinetic energy ∝ absolute temperature\n\n**Key Relationships:**\n\n**Average Kinetic Energy:**\nKE_avg = (3/2)RT (per mole)\nKE_avg = (3/2)kT (per molecule)\n- k = Boltzmann constant = 1.38×10⁻²³ J/K\n\n**Root Mean Square Speed:**\nu_rms = √(3RT/M)\n- M = molar mass (kg/mol)\n- Higher temperature → faster molecules\n- Lighter molecules → faster at same T\n\n**Maxwell-Boltzmann Distribution:**\n- Range of molecular speeds at given temperature\n- Higher T → broader distribution, higher average speed\n- Some molecules much faster/slower than average\n\n**Real Gases vs Ideal:**\nDeviations occur when:\n1. **High pressure:** Particle volume significant\n2. **Low temperature:** Intermolecular forces matter\n\n**Van der Waals Equation** (real gases):\n(P + an²/V²)(V - nb) = nRT\n- a = accounts for attractions\n- b = accounts for particle volume\n\n**Singapore Applications:**\n- **Air Quality:** NEA monitors molecular speeds affecting pollutant dispersion\n- **Refrigeration:** HDB air conditioners use gas compression/expansion\n- **Chemical Plants:** Jurong Island processes gases at various T and P\n- **Changi Airport:** Aircraft fuel vapor pressure calculations"
            },
            {
                "id": "phase-changes",
                "type": "text",
                "title": "Phase Changes & Diagrams",
                "title_zh": "相变与相图",
                "content": "**Phase Changes** occur when matter transitions between solid, liquid, and gas.\n\n**Types of Phase Changes:**\n1. **Melting/Fusion:** Solid → Liquid (+energy)\n2. **Freezing/Solidification:** Liquid → Solid (-energy)\n3. **Vaporization:** Liquid → Gas (+energy)\n4. **Condensation:** Gas → Liquid (-energy)\n5. **Sublimation:** Solid → Gas (+energy)\n6. **Deposition:** Gas → Solid (-energy)\n\n**Energy Changes:**\n- **Heating:** Q = mcΔT (temperature change)\n- **Phase Change:** Q = nΔH (enthalpy change)\n  - ΔH_fusion (melting)\n  - ΔH_vaporization (boiling)\n\n**Phase Diagrams:**\nShow phases at different T and P\n\n**Key Features:**\n- **Triple Point:** All three phases coexist\n- **Critical Point:** Above this, no distinct liquid/gas phases\n- **Phase Boundaries:** Lines separating regions\n\n**Water Phase Diagram (Unusual):**\n- Solid/liquid boundary has negative slope\n- Ice less dense than liquid (H-bonding structure)\n- Pressure can melt ice (ice skating)\n\n**CO₂ Phase Diagram:**\n- No liquid phase at 1 atm (sublimes)\n- Triple point at 5.1 atm, -57°C\n- Used for dry ice\n\n**Singapore Applications:**\n- **Ice Production:** Food industry uses phase changes\n- **Desalination:** Multi-stage flash evaporation (phase change)\n- **Refrigeration:** AC units in HDB use refrigerant phase changes\n- **Freeze-Drying:** Pharmaceutical companies use sublimation\n- **Dry Ice:** Used in Singapore's food delivery for cold chain\n\n**Vapor Pressure:**\n- Increases with temperature\n- Boiling occurs when vapor pressure = external pressure\n- Singapore's high humidity from high water vapor pressure"
            }
        ],
        "exercises": []
    }
]

# Will continue with remaining 5 JC1 and all 8 JC2 chapters...
# For now, save these 3 chapters

output = {
    "jc1_progress": "3/8 chapters created",
    "jc2_progress": "0/8 chapters created",
    "chapters_ready": jc1_chemistry
}

with open('chapters/jc_chemistry_partial.json', 'w', encoding='utf-8') as f:
    json.dump(jc1_chemistry, f, ensure_ascii=False, indent=2)

print(f"✓ Created {len(jc1_chemistry)} JC1 Chemistry chapters")
print(f"  Chapters: Atomic Structure, Chemical Bonding, States of Matter")
print(f"  Remaining JC1: 5 chapters")
print(f"  Remaining JC2: 8 chapters")
print(f"\nSaved to: chapters/jc_chemistry_partial.json")
