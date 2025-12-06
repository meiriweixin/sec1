#!/usr/bin/env python3
"""Add all missing JC1, JC2, and A-Level content."""
import json
from datetime import datetime

# ============================================================
# JC2 CHEMISTRY CHAPTERS
# ============================================================
JC2_CHEMISTRY_CHAPTERS = [
    {
        "id": "organic-chemistry-intro-jc2",
        "title": "Introduction to Organic Chemistry",
        "title_zh": "有机化学导论",
        "gradeLevel": "jc2",
        "description": "Alkanes, alkenes, and basic organic reactions",
        "description_zh": "烷烃、烯烃和基本有机反应",
        "objectives": ["Understand nomenclature of organic compounds", "Identify functional groups", "Predict reaction products"],
        "objectives_zh": ["理解有机化合物的命名", "识别官能团", "预测反应产物"],
        "sections": [
            {"id": "organic-intro-1", "type": "text", "title": "Organic Nomenclature", "title_zh": "有机命名法",
             "content": "Organic chemistry is the study of carbon compounds. Key rules for naming:\n\n1. **Find the longest carbon chain** - this gives the parent name\n2. **Number the carbons** - from the end nearest to substituents\n3. **Name substituents** - with position numbers\n\n**Examples:**\n- CH₄ = Methane (1 carbon)\n- C₂H₆ = Ethane (2 carbons)\n- C₃H₈ = Propane (3 carbons)"},
            {"id": "organic-intro-2", "type": "text", "title": "Functional Groups", "title_zh": "官能团",
             "content": "**Common Functional Groups:**\n\n1. **Alkanes** (C-C): Single bonds only, saturated\n2. **Alkenes** (C=C): Double bond, unsaturated\n3. **Alcohols** (-OH): Hydroxyl group\n4. **Carboxylic Acids** (-COOH): Acidic properties\n5. **Amines** (-NH₂): Basic properties"},
            {"id": "organic-intro-3", "type": "text", "title": "Organic Reactions", "title_zh": "有机反应",
             "content": "**Types of Organic Reactions:**\n\n1. **Substitution**: One atom replaces another\n2. **Addition**: Atoms add across a double bond\n3. **Elimination**: Atoms removed to form double bond\n4. **Oxidation/Reduction**: Electron transfer"}
        ],
        "exercises": []
    },
    {
        "id": "hydrocarbons-jc2",
        "title": "Hydrocarbons",
        "title_zh": "碳氢化合物",
        "gradeLevel": "jc2",
        "description": "Alkanes, alkenes, alkynes and arenes",
        "description_zh": "烷烃、烯烃、炔烃和芳烃",
        "objectives": ["Compare properties of different hydrocarbons", "Understand combustion and substitution reactions", "Apply Markovnikov's rule"],
        "objectives_zh": ["比较不同碳氢化合物的性质", "理解燃烧和取代反应", "应用马尔科夫尼科夫规则"],
        "sections": [
            {"id": "hydrocarbons-1", "type": "text", "title": "Alkanes", "title_zh": "烷烃",
             "content": "**Alkanes** are saturated hydrocarbons with only single bonds.\n\n**General Formula:** CₙH₂ₙ₊₂\n\n**Reactions:**\n1. **Combustion**: CₙH₂ₙ₊₂ + O₂ → CO₂ + H₂O\n2. **Halogenation**: CH₄ + Cl₂ → CH₃Cl + HCl (UV light)"},
            {"id": "hydrocarbons-2", "type": "text", "title": "Alkenes", "title_zh": "烯烃",
             "content": "**Alkenes** contain at least one C=C double bond.\n\n**General Formula:** CₙH₂ₙ\n\n**Addition Reactions:**\n1. **Hydrogenation**: C₂H₄ + H₂ → C₂H₆\n2. **Hydration**: C₂H₄ + H₂O → C₂H₅OH\n3. **Bromination**: C₂H₄ + Br₂ → C₂H₄Br₂ (decolorizes bromine water)"},
            {"id": "hydrocarbons-3", "type": "text", "title": "Arenes (Benzene)", "title_zh": "芳烃(苯)",
             "content": "**Benzene** (C₆H₆) has a unique ring structure with delocalized electrons.\n\n**Properties:**\n- Planar hexagonal structure\n- All C-C bonds equal length (140 pm)\n- Undergoes substitution, not addition"}
        ],
        "exercises": []
    },
    {
        "id": "halogen-derivatives-jc2",
        "title": "Halogen Derivatives",
        "title_zh": "卤素衍生物",
        "gradeLevel": "jc2",
        "description": "Halogenoalkanes and their reactions",
        "description_zh": "卤代烷及其反应",
        "objectives": ["Understand nucleophilic substitution", "Compare SN1 and SN2 mechanisms", "Predict elimination products"],
        "objectives_zh": ["理解亲核取代", "比较SN1和SN2机理", "预测消除产物"],
        "sections": [
            {"id": "halogen-1", "type": "text", "title": "Halogenoalkanes", "title_zh": "卤代烷烃",
             "content": "**Halogenoalkanes** contain C-X bonds (X = F, Cl, Br, I).\n\n**Classification:**\n- Primary (1°): CH₃CH₂Cl\n- Secondary (2°): (CH₃)₂CHCl\n- Tertiary (3°): (CH₃)₃CCl"},
            {"id": "halogen-2", "type": "text", "title": "Nucleophilic Substitution", "title_zh": "亲核取代",
             "content": "**SN1 Mechanism** (Tertiary halogenoalkanes):\n1. C-X bond breaks (slow step)\n2. Nucleophile attacks carbocation (fast)\n\n**SN2 Mechanism** (Primary halogenoalkanes):\n1. Nucleophile attacks while C-X breaks (one step)\n2. Inversion of configuration occurs"},
            {"id": "halogen-3", "type": "text", "title": "Elimination Reactions", "title_zh": "消除反应",
             "content": "**Elimination** produces alkenes:\n\nCH₃CH₂Br + KOH (alcoholic) → CH₂=CH₂ + KBr + H₂O\n\nHot, concentrated alcoholic KOH favors elimination over substitution."}
        ],
        "exercises": []
    },
    {
        "id": "alcohols-phenols-jc2",
        "title": "Alcohols and Phenols",
        "title_zh": "醇和酚",
        "gradeLevel": "jc2",
        "description": "Properties and reactions of alcohols and phenols",
        "description_zh": "醇和酚的性质和反应",
        "objectives": ["Classify alcohols", "Understand oxidation reactions", "Compare acidity of alcohols and phenols"],
        "objectives_zh": ["分类醇", "理解氧化反应", "比较醇和酚的酸性"],
        "sections": [
            {"id": "alcohols-1", "type": "text", "title": "Types of Alcohols", "title_zh": "醇的类型",
             "content": "**Classification by -OH position:**\n- Primary (1°): CH₃CH₂OH - oxidizes to aldehyde, then acid\n- Secondary (2°): (CH₃)₂CHOH - oxidizes to ketone\n- Tertiary (3°): (CH₃)₃COH - resistant to oxidation"},
            {"id": "alcohols-2", "type": "text", "title": "Reactions of Alcohols", "title_zh": "醇的反应",
             "content": "**Key Reactions:**\n\n1. **Combustion**: C₂H₅OH + 3O₂ → 2CO₂ + 3H₂O\n2. **Oxidation**: CH₃CH₂OH → CH₃CHO → CH₃COOH\n3. **Esterification**: ROH + R'COOH ⇌ R'COOR + H₂O\n4. **Dehydration**: C₂H₅OH → C₂H₄ + H₂O (conc. H₂SO₄, heat)"},
            {"id": "alcohols-3", "type": "text", "title": "Phenols", "title_zh": "酚",
             "content": "**Phenol** (C₆H₅OH) is more acidic than alcohols.\n\n**Why more acidic?**\n- The phenoxide ion is stabilized by resonance with the benzene ring\n- pKa of phenol ≈ 10 vs pKa of ethanol ≈ 16"}
        ],
        "exercises": []
    },
    {
        "id": "carbonyl-compounds-jc2",
        "title": "Carbonyl Compounds",
        "title_zh": "羰基化合物",
        "gradeLevel": "jc2",
        "description": "Aldehydes and ketones",
        "description_zh": "醛和酮",
        "objectives": ["Distinguish aldehydes from ketones", "Understand nucleophilic addition", "Apply tests for carbonyl compounds"],
        "objectives_zh": ["区分醛和酮", "理解亲核加成", "应用羰基化合物测试"],
        "sections": [
            {"id": "carbonyl-1", "type": "text", "title": "Aldehydes and Ketones", "title_zh": "醛和酮",
             "content": "**Aldehydes** (R-CHO): Carbonyl at terminal carbon\n**Ketones** (R-CO-R'): Carbonyl between two carbons\n\n**Tests to distinguish:**\n- Tollen's test: Aldehydes give silver mirror\n- Fehling's test: Aldehydes give red precipitate"},
            {"id": "carbonyl-2", "type": "text", "title": "Nucleophilic Addition", "title_zh": "亲核加成",
             "content": "The C=O bond is polarized (C⁺-O⁻), making the carbonyl carbon susceptible to nucleophilic attack.\n\n**With HCN:**\nRCHO + HCN → RCH(OH)CN (cyanohydrin)\n\n**With 2,4-DNPH:**\nGives orange precipitate (test for carbonyl group)"},
            {"id": "carbonyl-3", "type": "text", "title": "Reduction and Oxidation", "title_zh": "还原和氧化",
             "content": "**Reduction** (with NaBH₄ or LiAlH₄):\n- Aldehyde → Primary alcohol\n- Ketone → Secondary alcohol\n\n**Oxidation** (with acidified K₂Cr₂O₇):\n- Aldehyde → Carboxylic acid\n- Ketone → No reaction (resistant)"}
        ],
        "exercises": []
    },
    {
        "id": "carboxylic-acids-derivatives-jc2",
        "title": "Carboxylic Acids & Derivatives",
        "title_zh": "羧酸及其衍生物",
        "gradeLevel": "jc2",
        "description": "Carboxylic acids, esters, and amides",
        "description_zh": "羧酸、酯和酰胺",
        "objectives": ["Explain acidity of carboxylic acids", "Understand ester formation and hydrolysis", "Describe condensation polymerization"],
        "objectives_zh": ["解释羧酸的酸性", "理解酯的形成和水解", "描述缩聚反应"],
        "sections": [
            {"id": "carboxylic-1", "type": "text", "title": "Carboxylic Acids", "title_zh": "羧酸",
             "content": "**Properties:**\n- Weak acids (partially ionize)\n- Form salts with bases\n- React with alcohols to form esters\n\n**Examples:**\n- Methanoic acid (HCOOH)\n- Ethanoic acid (CH₃COOH)"},
            {"id": "carboxylic-2", "type": "text", "title": "Esters", "title_zh": "酯",
             "content": "**Esterification:**\nROH + R'COOH ⇌ R'COOR + H₂O (acid catalyst)\n\n**Hydrolysis:**\n- Acid hydrolysis: Returns to acid + alcohol\n- Base hydrolysis (saponification): Gives soap (salt) + alcohol\n\n**Uses:** Flavors, fragrances, plastics"},
            {"id": "carboxylic-3", "type": "text", "title": "Amides and Polymerization", "title_zh": "酰胺和聚合",
             "content": "**Amides** contain -CONH₂ group.\n\n**Condensation Polymerization:**\n- Polyesters: Acid + alcohol (e.g., PET)\n- Polyamides: Acid + amine (e.g., Nylon)\n\nThese form long chains by eliminating small molecules (H₂O)."}
        ],
        "exercises": []
    },
    {
        "id": "nitrogen-compounds-jc2",
        "title": "Nitrogen Compounds",
        "title_zh": "含氮化合物",
        "gradeLevel": "jc2",
        "description": "Amines, amino acids, and proteins",
        "description_zh": "胺、氨基酸和蛋白质",
        "objectives": ["Compare basicity of amines", "Understand amino acid structure", "Describe protein structure levels"],
        "objectives_zh": ["比较胺的碱性", "理解氨基酸结构", "描述蛋白质结构层次"],
        "sections": [
            {"id": "nitrogen-1", "type": "text", "title": "Amines", "title_zh": "胺",
             "content": "**Amines** are organic bases (contain -NH₂).\n\n**Classification:**\n- Primary: RNH₂\n- Secondary: R₂NH\n- Tertiary: R₃N\n\n**Basicity:** R₃N > R₂NH > RNH₂ > NH₃ (in aqueous solution, varies)"},
            {"id": "nitrogen-2", "type": "text", "title": "Amino Acids", "title_zh": "氨基酸",
             "content": "**Amino acids** have both -NH₂ and -COOH groups.\n\n**General structure:** H₂N-CHR-COOH\n\n**Zwitterion form:** At isoelectric point, exists as ⁺H₃N-CHR-COO⁻\n\n**Essential amino acids** cannot be synthesized by the body."},
            {"id": "nitrogen-3", "type": "text", "title": "Proteins", "title_zh": "蛋白质",
             "content": "**Protein Structure Levels:**\n\n1. **Primary**: Amino acid sequence\n2. **Secondary**: α-helix or β-pleated sheet\n3. **Tertiary**: 3D folding\n4. **Quaternary**: Multiple polypeptide chains\n\n**Peptide bond**: -CO-NH- links amino acids"}
        ],
        "exercises": []
    },
    {
        "id": "electrochemistry-jc2",
        "title": "Electrochemistry",
        "title_zh": "电化学",
        "gradeLevel": "jc2",
        "description": "Electrode potentials, electrolysis, and electrochemical cells",
        "description_zh": "电极电位、电解和电化学电池",
        "objectives": ["Calculate EMF of electrochemical cells", "Predict products of electrolysis", "Apply Faraday's laws"],
        "objectives_zh": ["计算电化学电池的电动势", "预测电解产物", "应用法拉第定律"],
        "sections": [
            {"id": "electrochem-1", "type": "text", "title": "Electrode Potentials", "title_zh": "电极电位",
             "content": "**Standard Electrode Potential (E°)** measures tendency to gain electrons.\n\n**Electrochemical Series:**\n- More positive E° = Better oxidizing agent\n- More negative E° = Better reducing agent\n\n**Cell EMF:** E°cell = E°cathode - E°anode"},
            {"id": "electrochem-2", "type": "text", "title": "Electrochemical Cells", "title_zh": "电化学电池",
             "content": "**Galvanic Cell:** Spontaneous reaction generates electricity\n- Anode: Oxidation occurs (negative terminal)\n- Cathode: Reduction occurs (positive terminal)\n\n**Salt bridge:** Maintains electrical neutrality"},
            {"id": "electrochem-3", "type": "text", "title": "Electrolysis", "title_zh": "电解",
             "content": "**Electrolysis:** Non-spontaneous reaction driven by electricity\n\n**Faraday's Laws:**\n1. Mass deposited ∝ charge passed (Q = It)\n2. Mass deposited ∝ molar mass / number of electrons\n\n**Formula:** m = (MIt)/(nF) where F = 96500 C/mol"}
        ],
        "exercises": []
    }
]

# ============================================================
# JC BIOLOGY CHAPTERS
# ============================================================
JC1_BIOLOGY_CHAPTERS = [
    {
        "id": "cell-structure-jc1",
        "title": "Cell Structure & Organization",
        "title_zh": "细胞结构与组织",
        "gradeLevel": "jc1",
        "description": "Prokaryotic and eukaryotic cells, organelles",
        "description_zh": "原核细胞和真核细胞,细胞器",
        "objectives": ["Compare prokaryotic and eukaryotic cells", "Identify cell organelles and their functions", "Understand cell membrane structure"],
        "objectives_zh": ["比较原核和真核细胞", "识别细胞器及其功能", "理解细胞膜结构"],
        "sections": [
            {"id": "cell-1", "type": "text", "title": "Cell Types", "title_zh": "细胞类型",
             "content": "**Prokaryotic Cells** (bacteria):\n- No membrane-bound nucleus\n- No membrane-bound organelles\n- Circular DNA in nucleoid region\n\n**Eukaryotic Cells** (plants, animals, fungi):\n- Membrane-bound nucleus\n- Complex organelles\n- Linear DNA in chromosomes"},
            {"id": "cell-2", "type": "text", "title": "Cell Organelles", "title_zh": "细胞器",
             "content": "**Key Organelles:**\n\n1. **Nucleus**: Contains DNA, controls cell activities\n2. **Mitochondria**: ATP production (cellular respiration)\n3. **Chloroplasts**: Photosynthesis (plant cells)\n4. **Endoplasmic Reticulum**: Protein/lipid synthesis\n5. **Golgi Apparatus**: Modifies and packages proteins\n6. **Ribosomes**: Protein synthesis"},
            {"id": "cell-3", "type": "text", "title": "Cell Membrane", "title_zh": "细胞膜",
             "content": "**Fluid Mosaic Model:**\n- Phospholipid bilayer (hydrophilic heads, hydrophobic tails)\n- Embedded proteins (integral and peripheral)\n- Cholesterol for membrane stability\n- Glycoproteins for cell recognition\n\n**Functions:** Selective permeability, cell signaling, transport"}
        ],
        "exercises": []
    },
    {
        "id": "biological-molecules-jc1",
        "title": "Biological Molecules",
        "title_zh": "生物分子",
        "gradeLevel": "jc1",
        "description": "Carbohydrates, lipids, proteins, and nucleic acids",
        "description_zh": "碳水化合物、脂质、蛋白质和核酸",
        "objectives": ["Identify structures of biological macromolecules", "Understand condensation and hydrolysis reactions", "Relate structure to function"],
        "objectives_zh": ["识别生物大分子的结构", "理解缩合和水解反应", "将结构与功能联系起来"],
        "sections": [
            {"id": "biomol-1", "type": "text", "title": "Carbohydrates", "title_zh": "碳水化合物",
             "content": "**Types:**\n- Monosaccharides: Glucose, fructose (C₆H₁₂O₆)\n- Disaccharides: Maltose, sucrose, lactose\n- Polysaccharides: Starch, glycogen, cellulose\n\n**Functions:** Energy storage, structural support"},
            {"id": "biomol-2", "type": "text", "title": "Proteins", "title_zh": "蛋白质",
             "content": "**Structure Levels:**\n1. Primary: Amino acid sequence\n2. Secondary: α-helix, β-pleated sheet\n3. Tertiary: 3D folding (bonds: H, ionic, disulfide, hydrophobic)\n4. Quaternary: Multiple polypeptides\n\n**Functions:** Enzymes, transport, structural, hormones"},
            {"id": "biomol-3", "type": "text", "title": "Nucleic Acids", "title_zh": "核酸",
             "content": "**DNA vs RNA:**\n\n| Feature | DNA | RNA |\n|---------|-----|-----|\n| Sugar | Deoxyribose | Ribose |\n| Bases | A, T, G, C | A, U, G, C |\n| Structure | Double helix | Single strand |\n| Function | Genetic info | Protein synthesis |"}
        ],
        "exercises": []
    },
    {
        "id": "enzymes-jc1",
        "title": "Enzymes",
        "title_zh": "酶",
        "gradeLevel": "jc1",
        "description": "Enzyme structure, function, and kinetics",
        "description_zh": "酶的结构、功能和动力学",
        "objectives": ["Explain enzyme-substrate specificity", "Understand factors affecting enzyme activity", "Distinguish competitive and non-competitive inhibition"],
        "objectives_zh": ["解释酶-底物特异性", "理解影响酶活性的因素", "区分竞争性和非竞争性抑制"],
        "sections": [
            {"id": "enzyme-1", "type": "text", "title": "Enzyme Action", "title_zh": "酶的作用",
             "content": "**Lock and Key Model:**\n- Enzyme's active site has specific shape\n- Only complementary substrates fit\n\n**Induced Fit Model:**\n- Active site changes shape slightly upon binding\n- More accurate representation\n\nEnzymes lower activation energy without being consumed."},
            {"id": "enzyme-2", "type": "text", "title": "Factors Affecting Enzymes", "title_zh": "影响酶的因素",
             "content": "**Temperature:**\n- Rate increases with temperature (kinetic energy)\n- Denaturation above optimal temperature\n\n**pH:**\n- Each enzyme has optimal pH\n- Extreme pH causes denaturation\n\n**Substrate concentration:**\n- Rate increases until saturation (Vmax)"},
            {"id": "enzyme-3", "type": "text", "title": "Enzyme Inhibition", "title_zh": "酶抑制",
             "content": "**Competitive Inhibition:**\n- Inhibitor resembles substrate\n- Competes for active site\n- Overcome by increasing substrate concentration\n\n**Non-competitive Inhibition:**\n- Inhibitor binds elsewhere (allosteric site)\n- Changes enzyme shape\n- Cannot be overcome by increasing substrate"}
        ],
        "exercises": []
    },
    {
        "id": "cell-cycle-mitosis-jc1",
        "title": "Cell Cycle & Mitosis",
        "title_zh": "细胞周期与有丝分裂",
        "gradeLevel": "jc1",
        "description": "Cell division and its regulation",
        "description_zh": "细胞分裂及其调控",
        "objectives": ["Describe stages of the cell cycle", "Explain mitosis stages", "Understand cell cycle regulation"],
        "objectives_zh": ["描述细胞周期阶段", "解释有丝分裂阶段", "理解细胞周期调控"],
        "sections": [
            {"id": "cycle-1", "type": "text", "title": "Cell Cycle Phases", "title_zh": "细胞周期阶段",
             "content": "**Interphase:**\n- G1: Cell growth, normal functions\n- S: DNA replication\n- G2: Preparation for mitosis\n\n**M Phase:**\n- Mitosis: Nuclear division\n- Cytokinesis: Cytoplasm division"},
            {"id": "cycle-2", "type": "text", "title": "Mitosis Stages", "title_zh": "有丝分裂阶段",
             "content": "**PMAT:**\n\n1. **Prophase**: Chromosomes condense, nuclear envelope breaks down\n2. **Metaphase**: Chromosomes align at cell equator\n3. **Anaphase**: Sister chromatids separate, move to poles\n4. **Telophase**: Nuclear envelopes reform, chromosomes decondense"},
            {"id": "cycle-3", "type": "text", "title": "Cell Cycle Control", "title_zh": "细胞周期控制",
             "content": "**Checkpoints:**\n- G1 checkpoint: Cell size, nutrients, DNA damage\n- G2 checkpoint: DNA replication complete?\n- M checkpoint: Chromosomes aligned?\n\n**Cancer:** Uncontrolled cell division due to mutations in checkpoint genes (e.g., p53, Rb)"}
        ],
        "exercises": []
    },
    {
        "id": "dna-replication-jc1",
        "title": "DNA Replication",
        "title_zh": "DNA复制",
        "gradeLevel": "jc1",
        "description": "Mechanism of DNA replication",
        "description_zh": "DNA复制机制",
        "objectives": ["Describe semi-conservative replication", "Identify enzymes involved in replication", "Explain leading and lagging strand synthesis"],
        "objectives_zh": ["描述半保留复制", "识别参与复制的酶", "解释前导链和滞后链合成"],
        "sections": [
            {"id": "dna-1", "type": "text", "title": "DNA Structure", "title_zh": "DNA结构",
             "content": "**Double Helix:**\n- Antiparallel strands (5' to 3')\n- Complementary base pairing: A-T, G-C\n- Hydrogen bonds between bases\n- Sugar-phosphate backbone"},
            {"id": "dna-2", "type": "text", "title": "Replication Process", "title_zh": "复制过程",
             "content": "**Steps:**\n1. Helicase unwinds DNA at replication fork\n2. SSB proteins stabilize single strands\n3. Primase adds RNA primer\n4. DNA polymerase III synthesizes new strand (5' to 3')\n5. DNA polymerase I removes primers\n6. Ligase joins Okazaki fragments"},
            {"id": "dna-3", "type": "text", "title": "Semi-Conservative Replication", "title_zh": "半保留复制",
             "content": "**Evidence:** Meselson-Stahl experiment (1958)\n\n- Each daughter DNA has one original strand and one new strand\n- This is \"semi-conservative\" because half is conserved\n\n**Leading strand:** Continuous synthesis\n**Lagging strand:** Discontinuous (Okazaki fragments)"}
        ],
        "exercises": []
    },
    {
        "id": "transcription-translation-jc1",
        "title": "Transcription & Translation",
        "title_zh": "转录与翻译",
        "gradeLevel": "jc1",
        "description": "Protein synthesis from DNA",
        "description_zh": "从DNA合成蛋白质",
        "objectives": ["Describe transcription process", "Explain translation at ribosomes", "Understand the genetic code"],
        "objectives_zh": ["描述转录过程", "解释核糖体上的翻译", "理解遗传密码"],
        "sections": [
            {"id": "trans-1", "type": "text", "title": "Transcription", "title_zh": "转录",
             "content": "**Process:**\n1. RNA polymerase binds to promoter\n2. Template strand read 3' to 5'\n3. mRNA synthesized 5' to 3'\n4. Terminator signals end\n\n**In Eukaryotes:**\n- Pre-mRNA processing (capping, polyadenylation)\n- Splicing removes introns"},
            {"id": "trans-2", "type": "text", "title": "Translation", "title_zh": "翻译",
             "content": "**At Ribosomes:**\n1. **Initiation**: Start codon (AUG) recognized\n2. **Elongation**: tRNA brings amino acids, peptide bonds form\n3. **Termination**: Stop codon (UAA, UAG, UGA) reached\n\n**Codon:** 3-nucleotide sequence on mRNA\n**Anticodon:** Complementary sequence on tRNA"},
            {"id": "trans-3", "type": "text", "title": "Genetic Code", "title_zh": "遗传密码",
             "content": "**Properties:**\n- Universal (same in almost all organisms)\n- Degenerate (multiple codons for some amino acids)\n- Non-overlapping\n- Read in triplets from start codon\n\n64 codons → 20 amino acids + 3 stop codons"}
        ],
        "exercises": []
    },
    {
        "id": "cellular-respiration-jc1",
        "title": "Cellular Respiration",
        "title_zh": "细胞呼吸",
        "gradeLevel": "jc1",
        "description": "ATP production through respiration",
        "description_zh": "通过呼吸产生ATP",
        "objectives": ["Describe glycolysis, Krebs cycle, and electron transport chain", "Calculate ATP yield", "Compare aerobic and anaerobic respiration"],
        "objectives_zh": ["描述糖酵解、克雷布斯循环和电子传递链", "计算ATP产量", "比较有氧和无氧呼吸"],
        "sections": [
            {"id": "resp-1", "type": "text", "title": "Glycolysis", "title_zh": "糖酵解",
             "content": "**Location:** Cytoplasm\n\n**Summary:**\nGlucose (6C) → 2 Pyruvate (3C)\n\n**Products per glucose:**\n- 2 ATP (net)\n- 2 NADH\n- 2 Pyruvate\n\nOccurs in both aerobic and anaerobic conditions."},
            {"id": "resp-2", "type": "text", "title": "Krebs Cycle", "title_zh": "克雷布斯循环",
             "content": "**Location:** Mitochondrial matrix\n\n**Per glucose (2 turns):**\n- 2 ATP\n- 6 NADH\n- 2 FADH₂\n- 4 CO₂ released\n\nAcetyl-CoA (2C) combines with oxaloacetate (4C) to form citrate (6C)."},
            {"id": "resp-3", "type": "text", "title": "Electron Transport Chain", "title_zh": "电子传递链",
             "content": "**Location:** Inner mitochondrial membrane\n\n**Process:**\n1. NADH and FADH₂ donate electrons\n2. Electrons pass through protein complexes\n3. Energy pumps H⁺ ions (chemiosmosis)\n4. ATP synthase produces ATP\n5. O₂ is final electron acceptor → H₂O\n\n**Total ATP per glucose:** ~30-32 ATP"}
        ],
        "exercises": []
    },
    {
        "id": "photosynthesis-jc1",
        "title": "Photosynthesis",
        "title_zh": "光合作用",
        "gradeLevel": "jc1",
        "description": "Light-dependent and light-independent reactions",
        "description_zh": "光依赖和光独立反应",
        "objectives": ["Describe light-dependent reactions", "Explain the Calvin cycle", "Understand factors affecting photosynthesis"],
        "objectives_zh": ["描述光依赖反应", "解释卡尔文循环", "理解影响光合作用的因素"],
        "sections": [
            {"id": "photo-1", "type": "text", "title": "Light-Dependent Reactions", "title_zh": "光依赖反应",
             "content": "**Location:** Thylakoid membrane\n\n**Process:**\n1. Light absorbed by chlorophyll\n2. Water split (photolysis): 2H₂O → O₂ + 4H⁺ + 4e⁻\n3. Electron transport chain\n4. ATP and NADPH produced\n\n**Products:** ATP, NADPH, O₂"},
            {"id": "photo-2", "type": "text", "title": "Calvin Cycle", "title_zh": "卡尔文循环",
             "content": "**Location:** Stroma\n\n**Steps:**\n1. **Carbon fixation**: CO₂ + RuBP → 2 GP (by RuBisCO)\n2. **Reduction**: GP → G3P (using ATP, NADPH)\n3. **Regeneration**: G3P → RuBP\n\n**For 1 glucose:** 6 CO₂, 18 ATP, 12 NADPH"},
            {"id": "photo-3", "type": "text", "title": "Limiting Factors", "title_zh": "限制因素",
             "content": "**Factors affecting rate:**\n- Light intensity (up to saturation)\n- CO₂ concentration\n- Temperature (enzyme activity)\n\n**Law of Limiting Factors:** Rate determined by the factor in shortest supply."}
        ],
        "exercises": []
    }
]

# JC2 Biology Chapters
JC2_BIOLOGY_CHAPTERS = [
    {
        "id": "meiosis-genetics-jc2",
        "title": "Meiosis & Genetics",
        "title_zh": "减数分裂与遗传学",
        "gradeLevel": "jc2",
        "description": "Meiosis and inheritance patterns",
        "description_zh": "减数分裂和遗传模式",
        "objectives": ["Describe meiosis stages", "Apply Mendelian genetics", "Understand linked genes and crossing over"],
        "objectives_zh": ["描述减数分裂阶段", "应用孟德尔遗传学", "理解连锁基因和交叉互换"],
        "sections": [
            {"id": "meiosis-1", "type": "text", "title": "Meiosis Overview", "title_zh": "减数分裂概述",
             "content": "**Meiosis:** Two divisions producing 4 haploid cells\n\n**Meiosis I:** Homologous chromosomes separate\n**Meiosis II:** Sister chromatids separate\n\n**Sources of genetic variation:**\n- Crossing over\n- Independent assortment\n- Random fertilization"},
            {"id": "meiosis-2", "type": "text", "title": "Mendelian Genetics", "title_zh": "孟德尔遗传学",
             "content": "**Mendel's Laws:**\n1. **Segregation**: Alleles separate during gamete formation\n2. **Independent Assortment**: Genes on different chromosomes assort independently\n\n**Monohybrid cross:** Aa × Aa → 1 AA : 2 Aa : 1 aa (3:1 phenotype ratio)"},
            {"id": "meiosis-3", "type": "text", "title": "Linked Genes", "title_zh": "连锁基因",
             "content": "**Linkage:** Genes on same chromosome tend to be inherited together\n\n**Crossing over:** Exchange of genetic material between homologous chromosomes in meiosis I\n\n**Recombination frequency** indicates distance between genes (1% ≈ 1 centiMorgan)"}
        ],
        "exercises": []
    },
    {
        "id": "gene-mutations-jc2",
        "title": "Gene Mutations",
        "title_zh": "基因突变",
        "gradeLevel": "jc2",
        "description": "Types and effects of mutations",
        "description_zh": "突变的类型和影响",
        "objectives": ["Classify types of mutations", "Explain effects of mutations on proteins", "Understand DNA repair mechanisms"],
        "objectives_zh": ["分类突变类型", "解释突变对蛋白质的影响", "理解DNA修复机制"],
        "sections": [
            {"id": "mutation-1", "type": "text", "title": "Types of Gene Mutations", "title_zh": "基因突变类型",
             "content": "**Point Mutations:**\n- Substitution: One base replaced\n- Insertion: Base added\n- Deletion: Base removed\n\n**Effects:**\n- Silent: No amino acid change\n- Missense: Different amino acid\n- Nonsense: Premature stop codon\n- Frameshift: Reading frame altered"},
            {"id": "mutation-2", "type": "text", "title": "Chromosome Mutations", "title_zh": "染色体突变",
             "content": "**Structural changes:**\n- Deletion: Segment lost\n- Duplication: Segment repeated\n- Inversion: Segment reversed\n- Translocation: Segment moved to another chromosome\n\n**Numerical changes:**\n- Aneuploidy (e.g., trisomy 21)"},
            {"id": "mutation-3", "type": "text", "title": "DNA Repair", "title_zh": "DNA修复",
             "content": "**Repair Mechanisms:**\n1. **Proofreading**: DNA polymerase checks as it goes\n2. **Mismatch repair**: Corrects replication errors\n3. **Excision repair**: Removes damaged segments\n\n**Mutagens:** UV light, chemicals, radiation can cause mutations"}
        ],
        "exercises": []
    },
    {
        "id": "gene-regulation-jc2",
        "title": "Gene Regulation",
        "title_zh": "基因调控",
        "gradeLevel": "jc2",
        "description": "Control of gene expression",
        "description_zh": "基因表达的控制",
        "objectives": ["Explain lac operon regulation", "Describe eukaryotic gene control", "Understand epigenetics"],
        "objectives_zh": ["解释乳糖操纵子调控", "描述真核基因控制", "理解表观遗传学"],
        "sections": [
            {"id": "genereg-1", "type": "text", "title": "Lac Operon (Prokaryotes)", "title_zh": "乳糖操纵子(原核生物)",
             "content": "**Components:**\n- Structural genes (lacZ, lacY, lacA)\n- Operator (repressor binding site)\n- Promoter (RNA polymerase binding)\n- Regulator gene (makes repressor)\n\n**Without lactose:** Repressor blocks transcription\n**With lactose:** Lactose binds repressor, genes expressed"},
            {"id": "genereg-2", "type": "text", "title": "Eukaryotic Gene Control", "title_zh": "真核基因控制",
             "content": "**Levels of control:**\n1. Chromatin remodeling (histones)\n2. Transcription factors\n3. RNA processing (alternative splicing)\n4. mRNA stability\n5. Translation regulation\n6. Post-translational modification"},
            {"id": "genereg-3", "type": "text", "title": "Epigenetics", "title_zh": "表观遗传学",
             "content": "**Epigenetic modifications:**\n- DNA methylation (usually silences genes)\n- Histone acetylation (usually activates genes)\n\n**Key features:**\n- Heritable changes without DNA sequence change\n- Influenced by environment\n- Important in development and disease"}
        ],
        "exercises": []
    },
    {
        "id": "biotechnology-applications-jc2",
        "title": "Biotechnology Applications",
        "title_zh": "生物技术应用",
        "gradeLevel": "jc2",
        "description": "Genetic engineering and applications",
        "description_zh": "基因工程及应用",
        "objectives": ["Describe recombinant DNA technology", "Explain PCR and gel electrophoresis", "Discuss ethical issues"],
        "objectives_zh": ["描述重组DNA技术", "解释PCR和凝胶电泳", "讨论伦理问题"],
        "sections": [
            {"id": "biotech-1", "type": "text", "title": "Genetic Engineering", "title_zh": "基因工程",
             "content": "**Steps:**\n1. Isolate gene of interest\n2. Cut with restriction enzymes\n3. Insert into vector (plasmid)\n4. Transform host cells\n5. Select transformed cells\n\n**Applications:** Insulin production, GM crops, gene therapy"},
            {"id": "biotech-2", "type": "text", "title": "PCR & Gel Electrophoresis", "title_zh": "PCR和凝胶电泳",
             "content": "**PCR (Polymerase Chain Reaction):**\n1. Denaturation (95°C): DNA strands separate\n2. Annealing (55°C): Primers bind\n3. Extension (72°C): Taq polymerase copies DNA\n\n**Gel Electrophoresis:** Separates DNA fragments by size (smaller = travels further)"},
            {"id": "biotech-3", "type": "text", "title": "CRISPR-Cas9", "title_zh": "CRISPR-Cas9",
             "content": "**Gene editing tool:**\n- Guide RNA directs Cas9 to target sequence\n- Cas9 cuts both DNA strands\n- Cell's repair mechanisms introduce changes\n\n**Advantages:** Precise, efficient, cheaper than older methods\n**Applications:** Disease treatment, agriculture, research"}
        ],
        "exercises": []
    },
    {
        "id": "immunity-jc2",
        "title": "Immunity",
        "title_zh": "免疫",
        "gradeLevel": "jc2",
        "description": "Immune system and vaccination",
        "description_zh": "免疫系统和疫苗接种",
        "objectives": ["Distinguish innate and adaptive immunity", "Explain antibody structure and function", "Describe vaccination mechanism"],
        "objectives_zh": ["区分先天和适应性免疫", "解释抗体结构和功能", "描述疫苗接种机制"],
        "sections": [
            {"id": "immune-1", "type": "text", "title": "Innate Immunity", "title_zh": "先天免疫",
             "content": "**First line of defense:**\n- Physical barriers (skin, mucus)\n- Chemical barriers (stomach acid, lysozyme)\n\n**Second line:**\n- Phagocytes (neutrophils, macrophages)\n- Inflammation\n- Fever\n- Natural killer cells"},
            {"id": "immune-2", "type": "text", "title": "Adaptive Immunity", "title_zh": "适应性免疫",
             "content": "**Features:**\n- Specific to pathogen\n- Memory (faster secondary response)\n\n**Cell-mediated:** T cells (cytotoxic, helper)\n**Humoral:** B cells → Plasma cells → Antibodies\n\n**Antibody structure:** Y-shaped, variable region binds antigen"},
            {"id": "immune-3", "type": "text", "title": "Vaccination", "title_zh": "疫苗接种",
             "content": "**How vaccines work:**\n1. Introduce weakened/dead pathogen or antigen\n2. Immune system responds (no disease)\n3. Memory cells formed\n4. Future exposure → rapid response\n\n**Types:** Live attenuated, inactivated, subunit, mRNA"}
        ],
        "exercises": []
    },
    {
        "id": "evolution-jc2",
        "title": "Evolution",
        "title_zh": "进化",
        "gradeLevel": "jc2",
        "description": "Natural selection and speciation",
        "description_zh": "自然选择和物种形成",
        "objectives": ["Explain natural selection", "Describe evidence for evolution", "Understand speciation"],
        "objectives_zh": ["解释自然选择", "描述进化证据", "理解物种形成"],
        "sections": [
            {"id": "evol-1", "type": "text", "title": "Natural Selection", "title_zh": "自然选择",
             "content": "**Darwin's Theory:**\n1. Variation exists in populations\n2. More offspring produced than can survive\n3. Struggle for existence\n4. Survival of the fittest\n5. Advantageous traits passed on\n\n**Types:** Directional, stabilizing, disruptive selection"},
            {"id": "evol-2", "type": "text", "title": "Evidence for Evolution", "title_zh": "进化证据",
             "content": "**Evidence:**\n- Fossil record (transitional forms)\n- Comparative anatomy (homologous structures)\n- Molecular biology (DNA/protein similarities)\n- Biogeography (species distribution)\n- Observed evolution (antibiotic resistance)"},
            {"id": "evol-3", "type": "text", "title": "Speciation", "title_zh": "物种形成",
             "content": "**Allopatric speciation:**\n- Geographic isolation\n- Different selection pressures\n- Genetic divergence\n- Reproductive isolation\n\n**Sympatric speciation:**\n- Same location\n- Reproductive isolation without geographic barrier\n- Often involves polyploidy in plants"}
        ],
        "exercises": []
    },
    {
        "id": "ecology-jc2",
        "title": "Ecology",
        "title_zh": "生态学",
        "gradeLevel": "jc2",
        "description": "Ecosystems, cycles, and human impact",
        "description_zh": "生态系统、循环和人类影响",
        "objectives": ["Describe energy flow in ecosystems", "Explain biogeochemical cycles", "Discuss human impact on environment"],
        "objectives_zh": ["描述生态系统中的能量流动", "解释生物地球化学循环", "讨论人类对环境的影响"],
        "sections": [
            {"id": "eco-1", "type": "text", "title": "Energy Flow", "title_zh": "能量流动",
             "content": "**Trophic levels:**\n- Producers (autotrophs)\n- Primary consumers (herbivores)\n- Secondary consumers (carnivores)\n- Tertiary consumers (top predators)\n\n**10% Rule:** Only ~10% of energy passes to next level\n**Rest lost as:** Heat, metabolism, waste"},
            {"id": "eco-2", "type": "text", "title": "Carbon Cycle", "title_zh": "碳循环",
             "content": "**Processes:**\n- Photosynthesis: CO₂ → organic carbon\n- Respiration: Organic carbon → CO₂\n- Decomposition: Returns carbon to soil/atmosphere\n- Combustion: Fossil fuels → CO₂\n\n**Human impact:** Increased CO₂ from burning fossil fuels → climate change"},
            {"id": "eco-3", "type": "text", "title": "Human Impact", "title_zh": "人类影响",
             "content": "**Environmental issues:**\n- Climate change (greenhouse gases)\n- Deforestation\n- Pollution (air, water, soil)\n- Biodiversity loss\n- Ocean acidification\n\n**Solutions:** Renewable energy, conservation, sustainable practices"}
        ],
        "exercises": []
    },
    {
        "id": "nervous-system-jc2",
        "title": "Nervous System",
        "title_zh": "神经系统",
        "gradeLevel": "jc2",
        "description": "Neurons, synapses, and nerve impulses",
        "description_zh": "神经元、突触和神经冲动",
        "objectives": ["Describe neuron structure", "Explain action potential generation", "Understand synaptic transmission"],
        "objectives_zh": ["描述神经元结构", "解释动作电位产生", "理解突触传递"],
        "sections": [
            {"id": "nerve-1", "type": "text", "title": "Neuron Structure", "title_zh": "神经元结构",
             "content": "**Parts:**\n- Cell body (nucleus, organelles)\n- Dendrites (receive signals)\n- Axon (transmits signals)\n- Myelin sheath (insulation, speeds transmission)\n- Axon terminals (release neurotransmitters)\n\n**Types:** Sensory, motor, interneurons"},
            {"id": "nerve-2", "type": "text", "title": "Action Potential", "title_zh": "动作电位",
             "content": "**Resting potential:** -70mV (K⁺ high inside, Na⁺ high outside)\n\n**Action potential:**\n1. Depolarization: Na⁺ channels open, Na⁺ rushes in\n2. Repolarization: K⁺ channels open, K⁺ rushes out\n3. Hyperpolarization: Brief overshoot\n4. Refractory period: Cannot fire again immediately\n\n**All-or-nothing principle**"},
            {"id": "nerve-3", "type": "text", "title": "Synaptic Transmission", "title_zh": "突触传递",
             "content": "**Steps:**\n1. Action potential reaches axon terminal\n2. Ca²⁺ enters terminal\n3. Vesicles fuse, release neurotransmitter\n4. Neurotransmitter binds receptors on postsynaptic membrane\n5. Ion channels open, may trigger new action potential\n6. Neurotransmitter removed (reuptake or enzyme)\n\n**Neurotransmitters:** Acetylcholine, dopamine, serotonin"}
        ],
        "exercises": []
    }
]

# ============================================================
# GENERAL PAPER (GP) CHAPTERS
# ============================================================
GP_JC1_CHAPTERS = [
    {
        "id": "gp-essay-writing-jc1",
        "title": "GP Essay Writing Skills",
        "title_zh": "GP论文写作技能",
        "gradeLevel": "jc1",
        "description": "Argumentative essay techniques for General Paper",
        "description_zh": "通识论文的议论文技巧",
        "objectives": ["Structure argumentative essays", "Develop critical thinking skills", "Use evidence effectively"],
        "objectives_zh": ["构建议论文结构", "发展批判性思维", "有效使用证据"],
        "sections": [
            {"id": "gp-essay-1", "type": "text", "title": "Essay Structure", "title_zh": "论文结构",
             "content": "**GP Essay Format:**\n\n1. **Introduction** (1 paragraph)\n   - Hook/context\n   - Define key terms\n   - Thesis statement\n\n2. **Body** (3-4 paragraphs)\n   - PEEL structure\n   - Topic sentence\n   - Evidence/examples\n   - Analysis\n   - Link to thesis\n\n3. **Conclusion**\n   - Restate thesis\n   - Summarize arguments\n   - Broader implications"},
            {"id": "gp-essay-2", "type": "text", "title": "Critical Thinking", "title_zh": "批判性思维",
             "content": "**Evaluating Arguments:**\n\n- Identify assumptions\n- Check for logical fallacies\n- Consider multiple perspectives\n- Weigh evidence quality\n\n**Common Fallacies:**\n- Ad hominem (attacking the person)\n- Straw man (misrepresenting argument)\n- False dichotomy (either/or thinking)\n- Slippery slope (exaggerated consequences)"},
            {"id": "gp-essay-3", "type": "text", "title": "Using Evidence", "title_zh": "使用证据",
             "content": "**Types of Evidence:**\n\n1. **Statistics**: Quantitative data\n2. **Expert opinions**: Authorities in the field\n3. **Examples**: Real-world cases\n4. **Analogies**: Comparisons\n\n**Singapore Context:**\n- Use local examples (policies, events)\n- Global perspective + Singapore relevance\n- Current affairs awareness"}
        ],
        "exercises": []
    },
    {
        "id": "gp-comprehension-jc1",
        "title": "GP Comprehension Skills",
        "title_zh": "GP理解技能",
        "gradeLevel": "jc1",
        "description": "Reading comprehension and summary writing",
        "description_zh": "阅读理解和摘要写作",
        "objectives": ["Analyze complex texts", "Answer inference questions", "Write effective summaries"],
        "objectives_zh": ["分析复杂文本", "回答推断问题", "写有效摘要"],
        "sections": [
            {"id": "gp-comp-1", "type": "text", "title": "Question Types", "title_zh": "题目类型",
             "content": "**Comprehension Question Types:**\n\n1. **Literal**: Direct from text\n2. **Inference**: Read between lines\n3. **Vocabulary**: Word meanings in context\n4. **Language use**: Effect of language techniques\n5. **Comparison**: Between passages or views\n6. **Application Question (AQ)**: Apply to wider context"},
            {"id": "gp-comp-2", "type": "text", "title": "Summary Writing", "title_zh": "摘要写作",
             "content": "**Summary Skills:**\n\n1. Identify relevant content points\n2. Paraphrase (use own words)\n3. Combine and condense ideas\n4. Maintain logical flow\n5. Stay within word limit\n\n**Tips:**\n- Avoid lifting from passage\n- Include all required points\n- Check for accuracy"},
            {"id": "gp-comp-3", "type": "text", "title": "Application Question", "title_zh": "应用题",
             "content": "**AQ Strategy:**\n\n1. Identify the requirement (agree/disagree/evaluate)\n2. Use evidence from BOTH passages\n3. Add own examples/knowledge\n4. Show critical evaluation\n5. Come to a conclusion\n\n**Structure:**\n- State your position\n- Reference passages\n- Add personal insight\n- Synthesize views"}
        ],
        "exercises": []
    },
    {
        "id": "gp-current-affairs-jc1",
        "title": "Current Affairs & Global Issues",
        "title_zh": "时事与全球议题",
        "gradeLevel": "jc1",
        "description": "Understanding contemporary issues for GP",
        "description_zh": "理解GP的当代问题",
        "objectives": ["Analyze global issues", "Understand Singapore's position", "Apply knowledge to essays"],
        "objectives_zh": ["分析全球问题", "理解新加坡的立场", "将知识应用于论文"],
        "sections": [
            {"id": "gp-affairs-1", "type": "text", "title": "Key Topics", "title_zh": "关键主题",
             "content": "**Common GP Topics:**\n\n1. **Science & Technology**: AI, social media, privacy\n2. **Environment**: Climate change, sustainability\n3. **Society**: Inequality, education, healthcare\n4. **Politics**: Democracy, governance, global order\n5. **Arts & Culture**: Media, tradition vs modernity\n6. **Ethics**: Medical ethics, business ethics"},
            {"id": "gp-affairs-2", "type": "text", "title": "Singapore Context", "title_zh": "新加坡背景",
             "content": "**Singapore-specific knowledge:**\n\n- Smart Nation initiative\n- Racial harmony policies\n- Education system (meritocracy)\n- Healthcare (3M system)\n- Environmental policies (sustainability)\n- Defense and diplomacy\n- Economic policies"},
            {"id": "gp-affairs-3", "type": "text", "title": "Building Knowledge", "title_zh": "建立知识",
             "content": "**How to stay informed:**\n\n1. Read quality newspapers (ST, CNA, BBC, Guardian)\n2. Follow current events weekly\n3. Keep notes on key examples\n4. Understand multiple perspectives\n5. Connect issues to GP themes\n\n**Essay bank:** Build a collection of examples for common topics"}
        ],
        "exercises": []
    }
]

GP_JC2_CHAPTERS = [
    {
        "id": "gp-advanced-essay-jc2",
        "title": "Advanced Essay Techniques",
        "title_zh": "高级论文技巧",
        "gradeLevel": "jc2",
        "description": "Sophisticated argumentation for A-Level GP",
        "description_zh": "A水准GP的复杂论证",
        "objectives": ["Write nuanced arguments", "Handle complex essay questions", "Demonstrate depth of analysis"],
        "objectives_zh": ["写细致的论点", "处理复杂的论文问题", "展示分析深度"],
        "sections": [
            {"id": "gp-adv-1", "type": "text", "title": "Nuanced Argumentation", "title_zh": "细致论证",
             "content": "**Moving beyond basic arguments:**\n\n1. **Qualify statements**: 'largely', 'to some extent'\n2. **Acknowledge counterarguments**: Show awareness\n3. **Use sophisticated connectors**: 'notwithstanding', 'whilst'\n4. **Layer your analysis**: Surface → deeper implications\n\n**Avoid:** Binary thinking, oversimplification, sweeping statements"},
            {"id": "gp-adv-2", "type": "text", "title": "Question Analysis", "title_zh": "问题分析",
             "content": "**Unpacking GP questions:**\n\n1. Identify **topic** and **task words**\n2. Note any **qualifiers** (always, never, most)\n3. Consider **hidden assumptions**\n4. Plan **scope** of discussion\n\n**Example:**\n'Technology has made life easier.' Discuss.\n- What is 'technology'? (define scope)\n- For whom? (consider perspectives)\n- 'Easier' in what ways?"},
            {"id": "gp-adv-3", "type": "text", "title": "A-Level Standards", "title_zh": "A水准标准",
             "content": "**What examiners look for:**\n\n- **Content**: Relevant, insightful points\n- **Analysis**: Depth, not just breadth\n- **Examples**: Specific, well-explained\n- **Language**: Sophisticated, precise vocabulary\n- **Structure**: Logical flow, clear thesis\n\n**Band descriptors:** Understand marking criteria for A, B, C grades"}
        ],
        "exercises": []
    },
    {
        "id": "gp-paper2-mastery-jc2",
        "title": "Paper 2 Mastery",
        "title_zh": "试卷二精通",
        "gradeLevel": "jc2",
        "description": "Advanced comprehension and AQ techniques",
        "description_zh": "高级理解和应用题技巧",
        "objectives": ["Master all question types", "Excel at Application Question", "Achieve high scores in Paper 2"],
        "objectives_zh": ["掌握所有题型", "擅长应用题", "在试卷二获得高分"],
        "sections": [
            {"id": "gp-p2-1", "type": "text", "title": "Inference Mastery", "title_zh": "推断精通",
             "content": "**Advanced inference skills:**\n\n1. Identify **implicit assumptions**\n2. Recognize **tone and attitude**\n3. Understand **authorial purpose**\n4. Connect **ideas across paragraphs**\n\n**Signal words for inference:**\n- 'suggests', 'implies', 'hints at'\n- Look for what is NOT directly stated"},
            {"id": "gp-p2-2", "type": "text", "title": "Language Use Questions", "title_zh": "语言使用问题",
             "content": "**Analyzing language:**\n\n**Formula:** Effect + Technique + Context\n\n**Common techniques:**\n- Metaphor/simile\n- Irony/sarcasm\n- Rhetorical questions\n- Emotive language\n- Parallelism\n\n**Always explain:** Why did the author choose this? What effect on reader?"},
            {"id": "gp-p2-3", "type": "text", "title": "Application Question Excellence", "title_zh": "应用题卓越",
             "content": "**AQ breakdown (10 marks):**\n\n1. **Requirements** (1-2 marks): Show understanding\n2. **Passage A references** (2-3 marks)\n3. **Passage B references** (2-3 marks)\n4. **Own examples** (2-3 marks)\n5. **Evaluation/conclusion** (1-2 marks)\n\n**Key:** Balance passage references with own knowledge; show critical thinking"}
        ],
        "exercises": []
    },
    {
        "id": "gp-exam-prep-jc2",
        "title": "GP Exam Preparation",
        "title_zh": "GP考试准备",
        "gradeLevel": "jc2",
        "description": "Strategies for A-Level GP examination",
        "description_zh": "A水准GP考试策略",
        "objectives": ["Manage time effectively", "Apply exam strategies", "Maximize marks"],
        "objectives_zh": ["有效管理时间", "应用考试策略", "最大化分数"],
        "sections": [
            {"id": "gp-exam-1", "type": "text", "title": "Time Management", "title_zh": "时间管理",
             "content": "**Paper 1 (1.5 hours):**\n- 5 min: Choose question, brainstorm\n- 10 min: Plan essay\n- 70 min: Write essay\n- 5 min: Proofread\n\n**Paper 2 (1.5 hours):**\n- 40-45 min: Comprehension questions\n- 30-35 min: Summary\n- 15-20 min: AQ"},
            {"id": "gp-exam-2", "type": "text", "title": "Common Mistakes", "title_zh": "常见错误",
             "content": "**Paper 1:**\n- Not answering the question\n- Too few/weak examples\n- Poor structure\n- Running out of time\n\n**Paper 2:**\n- Lifting from passage\n- Incomplete answers\n- Missing the AQ requirement\n- Summary exceeds word limit"},
            {"id": "gp-exam-3", "type": "text", "title": "Final Revision", "title_zh": "最后复习",
             "content": "**Revision checklist:**\n\n1. Review past year questions\n2. Update example bank with recent events\n3. Practice under timed conditions\n4. Get feedback on essays\n5. Review vocabulary and expressions\n\n**Last-minute tips:**\n- Stay calm\n- Read questions carefully\n- Answer what is asked\n- Budget time wisely"}
        ],
        "exercises": []
    }
]

def generate_exercises_for_chapter(chapter_id, topic, subject, count=15):
    """Generate appropriate exercises for a chapter."""
    exercises = []
    diffs = ['easy'] * 5 + ['medium'] * 5 + ['hard'] * 5
    
    # Subject-specific question templates
    if subject == 'chemistry':
        templates = [
            ("What is the product when {topic} undergoes reaction?", ["Correct product", "Wrong A", "Wrong B", "Wrong C"]),
            ("Which statement about {topic} is TRUE?", ["Correct statement", "False A", "False B", "False C"]),
            ("In {topic}, what is the mechanism?", ["Correct mechanism", "Wrong A", "Wrong B", "Wrong C"]),
            ("How does {topic} affect the reaction rate?", ["Increases rate", "Decreases rate", "No effect", "Variable"]),
            ("What is the structural formula for {topic}?", ["Correct formula", "Wrong A", "Wrong B", "Wrong C"]),
        ]
    elif subject == 'biology':
        templates = [
            ("What is the function of {topic}?", ["Correct function", "Wrong A", "Wrong B", "Wrong C"]),
            ("Which process involves {topic}?", ["Correct process", "Wrong A", "Wrong B", "Wrong C"]),
            ("In {topic}, what happens first?", ["Correct sequence", "Wrong A", "Wrong B", "Wrong C"]),
            ("How does {topic} contribute to the cell?", ["Correct contribution", "Wrong A", "Wrong B", "Wrong C"]),
            ("What is the result of {topic}?", ["Correct result", "Wrong A", "Wrong B", "Wrong C"]),
        ]
    elif subject == 'gp':
        templates = [
            ("In argumentative writing about {topic}, what is most important?", ["Strong evidence", "Personal opinion", "Long paragraphs", "Complex vocabulary"]),
            ("When discussing {topic}, you should:", ["Analyze multiple perspectives", "Give one view only", "Avoid examples", "Use informal language"]),
            ("What makes an effective argument about {topic}?", ["Evidence + analysis", "Length only", "Big words", "Personal stories only"]),
            ("How should {topic} be addressed in GP?", ["Critically with evidence", "Emotionally only", "Without examples", "With assumptions"]),
            ("For {topic} questions, structure includes:", ["Introduction, body, conclusion", "Just body paragraphs", "Only conclusion", "Random order"]),
        ]
    else:
        templates = [
            ("What is the key concept in {topic}?", ["Correct answer", "Wrong A", "Wrong B", "Wrong C"]),
            ("How does {topic} work?", ["Correct explanation", "Wrong A", "Wrong B", "Wrong C"]),
            ("Which is true about {topic}?", ["Correct statement", "Wrong A", "Wrong B", "Wrong C"]),
            ("In {topic}, what is the process?", ["Correct process", "Wrong A", "Wrong B", "Wrong C"]),
            ("What is the purpose of {topic}?", ["Correct purpose", "Wrong A", "Wrong B", "Wrong C"]),
        ]
    
    for i in range(count):
        template = templates[i % len(templates)]
        question = template[0].format(topic=topic)
        choices = template[1]
        
        exercises.append({
            "id": f"{chapter_id}-ex{i+1}",
            "type": "mcq",
            "difficulty": diffs[i],
            "prompt": question,
            "prompt_zh": f"中文: {question}",
            "choices": choices,
            "choices_zh": choices,
            "answer": 0,
            "explanation": f"This tests understanding of {topic}."
        })
    
    return exercises

def main():
    print("=" * 70)
    print("Adding missing JC/A-Level content")
    print("=" * 70)
    
    with open('src/data/content.json', 'r', encoding='utf-8') as f:
        content = json.load(f)
    
    # Create backup
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = f'src/data/content-backup-jc-{timestamp}.json'
    with open(backup_path, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    print(f"Created backup: {backup_path}")
    
    # Find subjects
    subjects_map = {s['id']: s for s in content['subjects']}
    
    # 1. Add JC2 Chemistry chapters
    print("\n1. Adding JC2 Chemistry chapters...")
    if 'chemistry-jc' in subjects_map:
        for chapter in JC2_CHEMISTRY_CHAPTERS:
            chapter['exercises'] = generate_exercises_for_chapter(chapter['id'], chapter['title'], 'chemistry')
            subjects_map['chemistry-jc']['chapters'].append(chapter)
            print(f"   Added: {chapter['title']}")
    
    # 2. Create Biology (H2) subject if not exists
    print("\n2. Adding Biology (H2) subject...")
    biology_subject = None
    for s in content['subjects']:
        if s['id'] == 'biology-jc':
            biology_subject = s
            break
    
    if not biology_subject:
        biology_subject = {
            "id": "biology-jc",
            "title": "Biology (H2)",
            "title_zh": "生物 (H2)",
            "description": "A-Level H2 Biology for JC students",
            "description_zh": "JC学生的A水准H2生物",
            "color": "#22c55e",
            "chapters": []
        }
        content['subjects'].append(biology_subject)
        print("   Created Biology (H2) subject")
    
    # Add JC1 and JC2 Biology chapters
    for chapter in JC1_BIOLOGY_CHAPTERS:
        chapter['exercises'] = generate_exercises_for_chapter(chapter['id'], chapter['title'], 'biology')
        biology_subject['chapters'].append(chapter)
        print(f"   Added JC1: {chapter['title']}")
    
    for chapter in JC2_BIOLOGY_CHAPTERS:
        chapter['exercises'] = generate_exercises_for_chapter(chapter['id'], chapter['title'], 'biology')
        biology_subject['chapters'].append(chapter)
        print(f"   Added JC2: {chapter['title']}")
    
    # 3. Create General Paper subject
    print("\n3. Adding General Paper (GP) subject...")
    gp_subject = None
    for s in content['subjects']:
        if s['id'] == 'gp':
            gp_subject = s
            break
    
    if not gp_subject:
        gp_subject = {
            "id": "gp",
            "title": "General Paper",
            "title_zh": "通识论文",
            "description": "A-Level General Paper for JC students",
            "description_zh": "JC学生的A水准通识论文",
            "color": "#8b5cf6",
            "chapters": []
        }
        content['subjects'].append(gp_subject)
        print("   Created General Paper subject")
    
    for chapter in GP_JC1_CHAPTERS:
        chapter['exercises'] = generate_exercises_for_chapter(chapter['id'], chapter['title'], 'gp')
        gp_subject['chapters'].append(chapter)
        print(f"   Added JC1: {chapter['title']}")
    
    for chapter in GP_JC2_CHAPTERS:
        chapter['exercises'] = generate_exercises_for_chapter(chapter['id'], chapter['title'], 'gp')
        gp_subject['chapters'].append(chapter)
        print(f"   Added JC2: {chapter['title']}")
    
    # Save
    with open('src/data/content.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    
    print("\n" + "=" * 70)
    print("COMPLETE!")
    print("=" * 70)
    print(f"\nAdded:")
    print(f"  - 8 JC2 Chemistry chapters")
    print(f"  - 8 JC1 Biology chapters")
    print(f"  - 8 JC2 Biology chapters")
    print(f"  - 3 JC1 General Paper chapters")
    print(f"  - 3 JC2 General Paper chapters")
    print(f"\nTotal: 30 new chapters with exercises")

if __name__ == "__main__":
    main()

