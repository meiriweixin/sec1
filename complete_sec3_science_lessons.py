#!/usr/bin/env python3
"""
Complete lesson content for remaining 8 Sec 3 Science chapters.
Covers: Electrolysis, Inheritance & Genetics, Polymers & Recycling, Pressure in Fluids,
Quantitative Chemistry, Reproduction & Cell Division, Salts & Neutralization, Turning Effects of Forces
"""

import json
from datetime import datetime

# Lesson content for remaining 8 chapters
LESSON_CONTENT = {
    "electrolysis": [
        {
            "id": "what-is-electrolysis",
            "title": "What is Electrolysis?",
            "title_zh": "什么是电解？",
            "type": "text",
            "content": """**Electrolysis** is the chemical decomposition of a substance by passing an electric current through it.

**Key requirements for electrolysis:**

1. **Electrolyte**: Ionic compound in molten state or aqueous solution
2. **Electrodes**: Two conductors (usually carbon or platinum)
3. **Power source**: Battery or DC power supply
4. **Complete circuit**: Allows electrons to flow

**How electrolysis works:**

**At the cathode (negative electrode):**
🔹 Positive ions (cations) are attracted
🔹 Cations gain electrons (reduction)
🔹 Example: Cu²⁺ + 2e⁻ → Cu

**At the anode (positive electrode):**
🔹 Negative ions (anions) are attracted
🔹 Anions lose electrons (oxidation)
🔹 Example: 2Cl⁻ → Cl₂ + 2e⁻

**Remember:** OIL RIG
- **Oxidation Is Loss** (of electrons)
- **Reduction Is Gain** (of electrons)

**Electrolysis of molten lead(II) bromide:**

**At cathode:** Pb²⁺ + 2e⁻ → Pb (grey metal deposited)
**At anode:** 2Br⁻ → Br₂ + 2e⁻ (brown fumes released)

**Industrial applications in Singapore:**

🔹 **Electroplating**: Gold/silver coating on jewelry (Mustafa Centre)
🔹 **Metal extraction**: Aluminum production from bauxite ore
🔹 **Chlor-alkali industry**: Producing chlorine for water treatment (PUB uses chlorine in tap water)
🔹 **Copper purification**: Refining copper for electrical wiring""",
            "content_zh": """**电解**是通过电流通过物质进行化学分解。

**电解的关键要求：**

1. **电解质**：熔融状态或水溶液中的离子化合物
2. **电极**：两个导体（通常是碳或铂）
3. **电源**：电池或直流电源
4. **完整电路**：允许电子流动

**电解如何工作：**

**在阴极（负极）：**
🔹 正离子（阳离子）被吸引
🔹 阳离子获得电子（还原）
🔹 例子：Cu²⁺ + 2e⁻ → Cu

**在阳极（正极）：**
🔹 负离子（阴离子）被吸引
🔹 阴离子失去电子（氧化）
🔹 例子：2Cl⁻ → Cl₂ + 2e⁻

**记住：** OIL RIG
- **氧化是失去**（电子）
- **还原是获得**（电子）

**熔融溴化铅的电解：**

**在阴极：** Pb²⁺ + 2e⁻ → Pb（灰色金属沉积）
**在阳极：** 2Br⁻ → Br₂ + 2e⁻（释放棕色烟雾）

**新加坡的工业应用：**

🔹 **电镀**：珠宝上的金/银涂层（Mustafa Centre）
🔹 **金属提取**：从铝土矿生产铝
🔹 **氯碱工业**：生产用于水处理的氯（PUB在自来水中使用氯）
🔹 **铜提纯**：精炼铜用于电线"""
        },
        {
            "id": "electrolysis-aqueous-solutions",
            "title": "Electrolysis of Aqueous Solutions",
            "title_zh": "水溶液的电解",
            "type": "text",
            "content": """**Electrolysis of aqueous solutions** is more complex than molten compounds because water molecules (H₂O) can also be discharged at the electrodes.

**Competing reactions at electrodes:**

**At the cathode** (reduction occurs):
- Metal ion OR hydrogen ions (H⁺) from water can be reduced
- **Reactivity series determines which is reduced:**
  - If metal is **less reactive than hydrogen** (e.g., Cu, Ag): Metal is deposited
  - If metal is **more reactive than hydrogen** (e.g., Na, K, Ca, Mg, Al, Zn): Hydrogen gas is released

**At the anode** (oxidation occurs):
- Non-metal ion OR hydroxide ions (OH⁻) from water can be oxidized
- **Concentration determines priority:**
  - **Concentrated solution**: Halide ions (Cl⁻, Br⁻, I⁻) are discharged
  - **Dilute solution**: OH⁻ ions are discharged, producing oxygen gas

**Example 1: Electrolysis of dilute sulfuric acid (H₂SO₄)**

**At cathode:** 2H⁺ + 2e⁻ → H₂ (hydrogen gas)
**At anode:** 4OH⁻ → 2H₂O + O₂ + 4e⁻ (oxygen gas)

**Overall:** Water is decomposed into hydrogen and oxygen (2:1 volume ratio)

**Example 2: Electrolysis of concentrated sodium chloride (NaCl) solution**

**At cathode:** 2H⁺ + 2e⁻ → H₂ (hydrogen gas, Na⁺ too reactive)
**At anode:** 2Cl⁻ → Cl₂ + 2e⁻ (chlorine gas, Cl⁻ preferentially discharged)

**Example 3: Electrolysis of copper(II) sulfate (CuSO₄) with copper electrodes**

**At cathode:** Cu²⁺ + 2e⁻ → Cu (copper deposits, cathode gains mass)
**At anode:** Cu → Cu²⁺ + 2e⁻ (copper dissolves, anode loses mass)

**Result:** Copper transfers from anode to cathode (electroplating/purification)

**Singapore application - Electroplating:**

Many local industries use electroplating:
🔹 **Jewelry shops**: Gold-plating cheaper metals
🔹 **Electronics manufacturing**: Tin-plating circuit boards
🔹 **Automotive parts**: Chrome-plating for corrosion resistance""",
            "content_zh": """**水溶液的电解**比熔融化合物更复杂，因为水分子（H₂O）也可以在电极处放电。

**电极处的竞争反应：**

**在阴极**（发生还原）：
- 金属离子或来自水的氢离子（H⁺）可以被还原
- **活性系列决定哪个被还原：**
  - 如果金属**活性低于氢**（例如Cu、Ag）：金属沉积
  - 如果金属**活性高于氢**（例如Na、K、Ca、Mg、Al、Zn）：释放氢气

**在阳极**（发生氧化）：
- 非金属离子或来自水的氢氧根离子（OH⁻）可以被氧化
- **浓度决定优先级：**
  - **浓溶液**：卤化物离子（Cl⁻、Br⁻、I⁻）被放电
  - **稀溶液**：OH⁻离子被放电，产生氧气

**例子1：稀硫酸（H₂SO₄）的电解**

**在阴极：** 2H⁺ + 2e⁻ → H₂（氢气）
**在阳极：** 4OH⁻ → 2H₂O + O₂ + 4e⁻（氧气）

**总体：** 水被分解成氢气和氧气（2:1体积比）

**例子2：浓氯化钠（NaCl）溶液的电解**

**在阴极：** 2H⁺ + 2e⁻ → H₂（氢气，Na⁺太活泼）
**在阳极：** 2Cl⁻ → Cl₂ + 2e⁻（氯气，Cl⁻优先放电）

**例子3：硫酸铜（CuSO₄）与铜电极的电解**

**在阴极：** Cu²⁺ + 2e⁻ → Cu（铜沉积，阴极增重）
**在阳极：** Cu → Cu²⁺ + 2e⁻（铜溶解，阳极减重）

**结果：** 铜从阳极转移到阴极（电镀/提纯）

**新加坡应用 - 电镀：**

许多本地行业使用电镀：
🔹 **珠宝店**：镀金较便宜的金属
🔹 **电子制造**：电路板镀锡
🔹 **汽车零件**：镀铬以防腐蚀"""
        },
        {
            "id": "industrial-electrolysis",
            "title": "Industrial Applications of Electrolysis",
            "title_zh": "电解的工业应用",
            "type": "text",
            "content": """**Electrolysis** has many important industrial applications worldwide and in Singapore.

**1. Extraction of reactive metals**

**Aluminum extraction from bauxite ore:**
- Ore purified to aluminum oxide (Al₂O₃), melted at 2000°C
- Cryolite added to lower melting point to 900°C
- **At cathode:** Al³⁺ + 3e⁻ → Al (molten aluminum sinks to bottom)
- **At anode:** 2O²⁻ → O₂ + 4e⁻ (oxygen reacts with carbon anode, needs replacement)
- Uses enormous amounts of electricity

**2. Purification of copper**

- **Impure copper anode** dissolves: Cu → Cu²⁺ + 2e⁻
- **Pure copper cathode** receives copper: Cu²⁺ + 2e⁻ → Cu
- Impurities (Ag, Au, Pt) fall to bottom as "anode sludge" (valuable!)
- Singapore imports refined copper for electrical wiring

**3. Electroplating**

**Process:**
1. Object to be plated is made the cathode
2. Plating metal is made the anode
3. Electrolyte contains ions of plating metal
4. Metal transfers from anode to object

**Benefits:**
✅ Improves appearance (shiny finish)
✅ Prevents corrosion (protective layer)
✅ Reduces cost (thin layer of expensive metal on cheap base)

**Examples:**
- Gold-plated jewelry
- Chrome-plated car parts
- Silver-plated cutlery
- Tin-plated food cans

**4. Chlor-alkali industry**

**Electrolysis of concentrated sodium chloride solution:**
- **At cathode:** Hydrogen gas produced
- **At anode:** Chlorine gas produced
- **Remaining solution:** Sodium hydroxide (NaOH)

**Products and uses:**
🔹 **Chlorine (Cl₂)**: Water disinfection (PUB treats tap water), bleach, PVC plastic
🔹 **Hydrogen (H₂)**: Fuel, ammonia production for fertilizers
🔹 **Sodium hydroxide (NaOH)**: Soap making, paper production, chemical industry

**Singapore context:**

🔹 **Water treatment**: PUB uses chlorine to disinfect tap water and NEWater
🔹 **Electronics manufacturing**: High-purity copper for circuit boards
🔹 **Chemical industry**: Jurong Island produces industrial chemicals
🔹 **Jewelry industry**: Electroplating at Little India shops and Mustafa Centre

**Environmental considerations:**

⚠️ High energy consumption (especially aluminum extraction)
⚠️ Greenhouse gas emissions from electricity generation
✅ Recycling metals reduces need for extraction
✅ Using renewable energy sources for electricity""",
            "content_zh": """**电解**在全球和新加坡有许多重要的工业应用。

**1. 提取活性金属**

**从铝土矿中提取铝：**
- 矿石纯化为氧化铝（Al₂O₃），在2000°C下熔化
- 添加冰晶石以将熔点降低至900°C
- **在阴极：** Al³⁺ + 3e⁻ → Al（熔融铝沉到底部）
- **在阳极：** 2O²⁻ → O₂ + 4e⁻（氧气与碳阳极反应，需要更换）
- 使用大量电力

**2. 铜的提纯**

- **不纯铜阳极**溶解：Cu → Cu²⁺ + 2e⁻
- **纯铜阴极**接收铜：Cu²⁺ + 2e⁻ → Cu
- 杂质（Ag、Au、Pt）落到底部作为"阳极泥"（有价值！）
- 新加坡进口精炼铜用于电线

**3. 电镀**

**过程：**
1. 要镀的物体作为阴极
2. 镀层金属作为阳极
3. 电解质含有镀层金属的离子
4. 金属从阳极转移到物体

**好处：**
✅ 改善外观（光亮表面）
✅ 防止腐蚀（保护层）
✅ 降低成本（在便宜基材上镀薄层昂贵金属）

**例子：**
- 镀金珠宝
- 镀铬汽车零件
- 镀银餐具
- 镀锡食品罐

**4. 氯碱工业**

**浓氯化钠溶液的电解：**
- **在阴极：** 产生氢气
- **在阳极：** 产生氯气
- **剩余溶液：** 氢氧化钠（NaOH）

**产品和用途：**
🔹 **氯气（Cl₂）**：水消毒（PUB处理自来水）、漂白剂、PVC塑料
🔹 **氢气（H₂）**：燃料、肥料用氨生产
🔹 **氢氧化钠（NaOH）**：肥皂制作、造纸、化学工业

**新加坡背景：**

🔹 **水处理**：PUB使用氯消毒自来水和新生水
🔹 **电子制造**：电路板用高纯度铜
🔹 **化学工业**：裕廊岛生产工业化学品
🔹 **珠宝业**：小印度商店和Mustafa Centre电镀

**环境考虑：**

⚠️ 高能耗（特别是铝提取）
⚠️ 发电产生的温室气体排放
✅ 回收金属减少提取需求
✅ 使用可再生能源发电"""
        }
    ],

    "inheritance-genetics": [
        {
            "id": "dna-genes-chromosomes",
            "title": "DNA, Genes, and Chromosomes",
            "title_zh": "DNA、基因和染色体",
            "type": "text",
            "content": """**Genetics** is the study of how characteristics are passed from parents to offspring through genes.

**Key genetic structures:**

**1. DNA (Deoxyribonucleic Acid)**
- **Structure**: Double helix, like a twisted ladder
- **Components**: Sugar-phosphate backbone, nitrogenous bases (A, T, G, C)
- **Base pairing**: A pairs with T, G pairs with C
- **Function**: Stores genetic information

**2. Genes**
- **Definition**: Section of DNA that codes for a specific protein
- **Function**: Determines specific characteristics (eye color, blood type, height)
- **Location**: Found on chromosomes
- **Alleles**: Different versions of the same gene (e.g., brown eye allele vs. blue eye allele)

**3. Chromosomes**
- **Structure**: Long thread of coiled DNA + proteins
- **Number in humans**: 46 chromosomes (23 pairs)
- **Types**: 22 pairs of autosomes + 1 pair of sex chromosomes (XX female, XY male)
- **Inheritance**: 23 from mother, 23 from father

**Genetic terminology:**

🔹 **Genotype**: Genetic makeup (e.g., TT, Tt, tt)
🔹 **Phenotype**: Physical appearance (e.g., tall or short)
🔹 **Dominant allele**: Expressed when present (represented by capital letter, e.g., T)
🔹 **Recessive allele**: Only expressed when paired together (lowercase letter, e.g., t)
🔹 **Homozygous**: Two identical alleles (TT or tt)
🔹 **Heterozygous**: Two different alleles (Tt)

**Example: Pea plant height**
- T = tall (dominant)
- t = short (recessive)

**Genotypes and phenotypes:**
- TT = tall plant (homozygous dominant)
- Tt = tall plant (heterozygous)
- tt = short plant (homozygous recessive)

**Singapore genetic diversity:**

Singapore's multicultural population shows genetic variation:
🔹 **Eye color**: Most Asians have brown eyes (dominant allele)
🔹 **Lactose intolerance**: Common in Asian populations (genetic variation)
🔹 **Blood types**: A, B, AB, O distributed across ethnic groups
🔹 **Genetic research**: Singapore Genome Project studies Asian genetic variations""",
            "content_zh": """**遗传学**是研究特征如何通过基因从父母传递给后代的学科。

**关键遗传结构：**

**1. DNA（脱氧核糖核酸）**
- **结构**：双螺旋，像扭曲的梯子
- **组成部分**：糖-磷酸骨架，含氮碱基（A、T、G、C）
- **碱基配对**：A与T配对，G与C配对
- **功能**：储存遗传信息

**2. 基因**
- **定义**：编码特定蛋白质的DNA片段
- **功能**：决定特定特征（眼睛颜色、血型、身高）
- **位置**：在染色体上发现
- **等位基因**：同一基因的不同版本（例如，棕色眼睛等位基因vs.蓝色眼睛等位基因）

**3. 染色体**
- **结构**：盘绕的DNA长线+蛋白质
- **人类数量**：46条染色体（23对）
- **类型**：22对常染色体+1对性染色体（XX女性，XY男性）
- **遗传**：23条来自母亲，23条来自父亲

**遗传术语：**

🔹 **基因型**：遗传组成（例如TT、Tt、tt）
🔹 **表型**：物理外观（例如高或矮）
🔹 **显性等位基因**：存在时表达（用大写字母表示，例如T）
🔹 **隐性等位基因**：只有成对时才表达（小写字母，例如t）
🔹 **纯合子**：两个相同的等位基因（TT或tt）
🔹 **杂合子**：两个不同的等位基因（Tt）

**例子：豌豆植物高度**
- T = 高（显性）
- t = 矮（隐性）

**基因型和表型：**
- TT = 高植物（纯合显性）
- Tt = 高植物（杂合）
- tt = 矮植物（纯合隐性）

**新加坡遗传多样性：**

新加坡的多元文化人口显示遗传变异：
🔹 **眼睛颜色**：大多数亚洲人有棕色眼睛（显性等位基因）
🔹 **乳糖不耐受**：在亚洲人群中常见（遗传变异）
🔹 **血型**：A、B、AB、O分布在各族群中
🔹 **遗传研究**：新加坡基因组计划研究亚洲遗传变异"""
        },
        {
            "id": "mendelian-inheritance",
            "title": "Mendelian Inheritance and Punnett Squares",
            "title_zh": "孟德尔遗传与庞尼特方格",
            "type": "text",
            "content": """**Gregor Mendel** (1822-1884) discovered the basic principles of inheritance through pea plant experiments.

**Mendel's Laws:**

**1. Law of Segregation**
- Each parent has two alleles for each gene
- Alleles separate during gamete (sex cell) formation
- Each gamete receives only one allele

**2. Law of Independent Assortment**
- Genes for different traits are inherited independently
- Example: Gene for height doesn't affect gene for flower color

**Punnett Square** - Tool to predict offspring genotypes

**Monohybrid cross** (one trait):

**Example: Pea plant height**
- Parents: Tt (heterozygous tall) × Tt (heterozygous tall)

```
Punnett Square:
        T    t
    T  TT   Tt
    t  Tt   tt
```

**Results:**
- **Genotype ratio**: 1 TT : 2 Tt : 1 tt
- **Phenotype ratio**: 3 tall : 1 short (75% tall, 25% short)

**Types of crosses:**

**1. Homozygous dominant × Homozygous recessive**
- Parents: TT × tt
- Offspring: 100% Tt (all tall, heterozygous)

**2. Heterozygous × Heterozygous**
- Parents: Tt × Tt
- Offspring: 3 tall : 1 short

**3. Heterozygous × Homozygous recessive**
- Parents: Tt × tt
- Offspring: 1 Tt : 1 tt (50% tall, 50% short)

**Real-world applications:**

**Plant breeding:**
🔹 Farmers select plants with desirable traits (high yield, disease resistance)
🔹 Cross-pollinate to combine traits
🔹 Singapore's urban farms use selective breeding for vegetables

**Animal breeding:**
🔹 Breed livestock for meat quality, milk production
🔹 Dog breeders select for specific coat colors, sizes

**Human genetics:**
🔹 Genetic counseling predicts probability of inherited diseases
🔹 Understanding family history of conditions (e.g., sickle cell anemia, cystic fibrosis)

**Singapore examples:**

**Blood type inheritance:**
- A and B are co-dominant, O is recessive
- Parents with type A (I^A I^O) and type B (I^B I^O) can have children with types:
  - A (I^A I^A or I^A I^O)
  - B (I^B I^B or I^B I^O)
  - AB (I^A I^B)
  - O (I^O I^O)

This is why blood donation centers (Health Sciences Authority) need diverse donors!""",
            "content_zh": """**格雷戈尔·孟德尔**（1822-1884）通过豌豆植物实验发现了遗传的基本原理。

**孟德尔定律：**

**1. 分离定律**
- 每个亲本对每个基因有两个等位基因
- 等位基因在配子（性细胞）形成期间分离
- 每个配子只接收一个等位基因

**2. 独立分配定律**
- 不同性状的基因独立遗传
- 例子：高度基因不影响花色基因

**庞尼特方格** - 预测后代基因型的工具

**单性状杂交**（一个性状）：

**例子：豌豆植物高度**
- 亲本：Tt（杂合高）× Tt（杂合高）

```
庞尼特方格：
        T    t
    T  TT   Tt
    t  Tt   tt
```

**结果：**
- **基因型比率**：1 TT：2 Tt：1 tt
- **表型比率**：3高：1矮（75%高，25%矮）

**杂交类型：**

**1. 纯合显性×纯合隐性**
- 亲本：TT × tt
- 后代：100% Tt（全部高，杂合）

**2. 杂合×杂合**
- 亲本：Tt × Tt
- 后代：3高：1矮

**3. 杂合×纯合隐性**
- 亲本：Tt × tt
- 后代：1 Tt：1 tt（50%高，50%矮）

**实际应用：**

**植物育种：**
🔹 农民选择具有理想性状的植物（高产量、抗病性）
🔹 杂交以结合性状
🔹 新加坡的城市农场使用选择性育种种植蔬菜

**动物育种：**
🔹 繁殖牲畜以获得肉质、产奶量
🔹 狗繁殖者选择特定毛色、大小

**人类遗传学：**
🔹 遗传咨询预测遗传疾病的概率
🔹 了解疾病的家族史（例如镰状细胞性贫血、囊性纤维化）

**新加坡例子：**

**血型遗传：**
- A和B是共显性，O是隐性
- A型（I^A I^O）和B型（I^B I^O）的父母可以有以下血型的孩子：
  - A型（I^A I^A或I^A I^O）
  - B型（I^B I^B或I^B I^O）
  - AB型（I^A I^B）
  - O型（I^O I^O）

这就是为什么献血中心（卫生科学局）需要多样化的献血者！"""
        },
        {
            "id": "genetic-variation-mutations",
            "title": "Genetic Variation and Mutations",
            "title_zh": "遗传变异与突变",
            "type": "text",
            "content": """**Genetic variation** is the difference in DNA sequences between individuals, making each person unique (except identical twins).

**Sources of genetic variation:**

**1. Sexual reproduction**
- **Meiosis**: Process producing sex cells (gametes)
- **Random fertilization**: Any sperm can fertilize any egg
- **Crossing over**: Chromosomes exchange segments during meiosis
- **Independent assortment**: Chromosomes randomly distributed to gametes
- **Result**: Each offspring is genetically unique

**2. Mutations**
- **Definition**: Random changes in DNA sequence
- **Causes**: Radiation, chemicals, errors during DNA replication
- **Types**: Gene mutations, chromosome mutations

**Types of mutations:**

**Gene mutations** (affect single genes):

**1. Substitution** - One base replaced by another
- Example: Sickle cell disease (GAG → GTG in hemoglobin gene)
- Effect: Abnormal hemoglobin protein, crescent-shaped red blood cells

**2. Insertion** - Extra base added
- Effect: Reading frame shifts, usually harmful

**3. Deletion** - Base removed
- Effect: Reading frame shifts, usually harmful

**Chromosome mutations** (affect whole chromosomes):

**1. Deletion** - Segment of chromosome lost
**2. Duplication** - Segment repeated
**3. Inversion** - Segment reversed
**4. Translocation** - Segment moved to different chromosome

**Effects of mutations:**

**Harmful mutations:**
⚠️ **Sickle cell disease**: Abnormal hemoglobin, painful episodes
⚠️ **Cystic fibrosis**: Thick mucus in lungs and digestive system
⚠️ **Down syndrome**: Extra chromosome 21, developmental delays

**Neutral mutations:**
🔹 No noticeable effect on organism
🔹 Most mutations are neutral

**Beneficial mutations:**
✅ **Lactose tolerance**: Ability to digest milk in adulthood (evolutionary advantage)
✅ **Antibiotic resistance in bacteria**: Allows survival (though harmful to humans!)
✅ **Pesticide resistance in insects**: Allows survival

**Importance of genetic variation:**

✅ **Evolution**: Raw material for natural selection
✅ **Disease resistance**: Some individuals survive epidemics
✅ **Adaptation**: Populations can adapt to environmental changes
✅ **Agriculture**: Selective breeding requires genetic variation

**Genetic diseases in Singapore:**

**Thalassemia screening:**
🔹 Common inherited blood disorder in Asian populations
🔹 Mandatory screening for couples in Singapore
🔹 Genetic counseling available at KKH, SGH

**Glucose-6-phosphate dehydrogenase (G6PD) deficiency:**
🔹 Common in males of Asian, African, Mediterranean descent
🔹 Newborn screening in Singapore
🔹 Avoid certain foods (fava beans) and medications

**Genetic testing services:**
🔹 Available at National University Hospital
🔹 Pre-marital screening programs
🔹 Prenatal genetic testing (amniocentesis, chorionic villus sampling)""",
            "content_zh": """**遗传变异**是个体之间DNA序列的差异，使每个人独特（除了同卵双胞胎）。

**遗传变异的来源：**

**1. 有性生殖**
- **减数分裂**：产生性细胞（配子）的过程
- **随机受精**：任何精子都可以使任何卵子受精
- **交叉互换**：染色体在减数分裂期间交换片段
- **独立分配**：染色体随机分配到配子
- **结果**：每个后代在遗传上都是独特的

**2. 突变**
- **定义**：DNA序列的随机变化
- **原因**：辐射、化学物质、DNA复制期间的错误
- **类型**：基因突变、染色体突变

**突变类型：**

**基因突变**（影响单个基因）：

**1. 替换** - 一个碱基被另一个替换
- 例子：镰状细胞病（血红蛋白基因中GAG → GTG）
- 效果：异常血红蛋白，新月形红细胞

**2. 插入** - 添加额外碱基
- 效果：阅读框移位，通常有害

**3. 删除** - 碱基被移除
- 效果：阅读框移位，通常有害

**染色体突变**（影响整条染色体）：

**1. 删除** - 染色体片段丢失
**2. 重复** - 片段重复
**3. 倒位** - 片段颠倒
**4. 易位** - 片段移动到不同染色体

**突变的影响：**

**有害突变：**
⚠️ **镰状细胞病**：异常血红蛋白，疼痛发作
⚠️ **囊性纤维化**：肺和消化系统中的粘稠粘液
⚠️ **唐氏综合症**：额外的21号染色体，发育迟缓

**中性突变：**
🔹 对生物体没有明显影响
🔹 大多数突变是中性的

**有益突变：**
✅ **乳糖耐受性**：成年后消化牛奶的能力（进化优势）
✅ **细菌的抗生素抗性**：允许生存（尽管对人类有害！）
✅ **昆虫的农药抗性**：允许生存

**遗传变异的重要性：**

✅ **进化**：自然选择的原材料
✅ **抗病性**：一些个体在流行病中幸存
✅ **适应**：种群可以适应环境变化
✅ **农业**：选择性育种需要遗传变异

**新加坡的遗传疾病：**

**地中海贫血筛查：**
🔹 亚洲人群中常见的遗传性血液疾病
🔹 新加坡夫妇强制筛查
🔹 KKH、SGH提供遗传咨询

**葡萄糖-6-磷酸脱氢酶（G6PD）缺乏症：**
🔹 在亚洲、非洲、地中海血统的男性中常见
🔹 新加坡新生儿筛查
🔹 避免某些食物（蚕豆）和药物

**基因检测服务：**
🔹 国立大学医院提供
🔹 婚前筛查计划
🔹 产前基因检测（羊膜穿刺术、绒毛膜绒毛取样）"""
        }
    ],

    "polymers-recycling": [
        {
            "id": "introduction-polymers",
            "title": "Introduction to Polymers",
            "title_zh": "聚合物简介",
            "type": "text",
            "content": """**Polymers** are large molecules made up of many small repeating units called monomers.

**Structure:**
- **Monomer**: Small molecule that joins to form polymer
- **Polymer**: Long chain of monomers linked together
- **Polymerization**: Chemical reaction joining monomers

**Types of polymers:**

**1. Natural polymers** (found in nature):
🔹 **Proteins**: Made from amino acid monomers (silk, wool, hair)
🔹 **Starch**: Made from glucose monomers (rice, potatoes)
🔹 **Cellulose**: Made from glucose monomers (cotton, wood, paper)
🔹 **DNA/RNA**: Made from nucleotide monomers
🔹 **Natural rubber**: Made from isoprene monomers (latex from rubber trees)

**2. Synthetic polymers** (human-made):
🔹 **Plastics**: Polyethylene (plastic bags), polypropylene (food containers)
🔹 **Nylon**: Clothing, ropes, carpets
🔹 **PVC (polyvinyl chloride)**: Pipes, window frames, flooring
🔹 **Polystyrene**: Foam cups, packaging materials
🔹 **PET (polyethylene terephthalate)**: Drink bottles, clothing fibers

**Properties of polymers:**

**Advantages:**
✅ **Lightweight**: Easy to transport and handle
✅ **Durable**: Resistant to corrosion, long-lasting
✅ **Waterproof**: Don't absorb water
✅ **Flexible or rigid**: Can be molded into different shapes
✅ **Cheap to produce**: Lower cost than metals or glass
✅ **Insulator**: Don't conduct electricity or heat well

**Disadvantages:**
⚠️ **Non-biodegradable**: Take hundreds of years to decompose
⚠️ **Flammable**: Burn easily, produce toxic fumes
⚠️ **From fossil fuels**: Made from non-renewable crude oil
⚠️ **Pollution**: Accumulate in environment, harm wildlife

**Common plastic codes in Singapore:**

**1. PET (1)** - Water bottles, soft drink bottles
**2. HDPE (2)** - Milk jugs, shampoo bottles
**3. PVC (3)** - Pipes, window frames
**4. LDPE (4)** - Plastic bags, squeeze bottles
**5. PP (5)** - Food containers, bottle caps
**6. PS (6)** - Foam cups, food trays
**7. Others** - Mixed plastics, CDs

**Singapore examples:**

🔹 **HDB buildings**: PVC pipes for plumbing
🔹 **Food packaging**: Polypropylene containers at hawker centers
🔹 **Drink bottles**: PET bottles at supermarkets (FairPrice, Giant, Sheng Siong)
🔹 **MRT seats**: Synthetic polymer fabrics for durability""",
            "content_zh": """**聚合物**是由许多称为单体的小重复单元组成的大分子。

**结构：**
- **单体**：连接形成聚合物的小分子
- **聚合物**：连接在一起的单体长链
- **聚合反应**：连接单体的化学反应

**聚合物类型：**

**1. 天然聚合物**（在自然界中发现）：
🔹 **蛋白质**：由氨基酸单体组成（丝绸、羊毛、头发）
🔹 **淀粉**：由葡萄糖单体组成（米、土豆）
🔹 **纤维素**：由葡萄糖单体组成（棉花、木材、纸）
🔹 **DNA/RNA**：由核苷酸单体组成
🔹 **天然橡胶**：由异戊二烯单体组成（橡胶树的乳胶）

**2. 合成聚合物**（人造）：
🔹 **塑料**：聚乙烯（塑料袋）、聚丙烯（食品容器）
🔹 **尼龙**：服装、绳索、地毯
🔹 **PVC（聚氯乙烯）**：管道、窗框、地板
🔹 **聚苯乙烯**：泡沫杯、包装材料
🔹 **PET（聚对苯二甲酸乙二醇酯）**：饮料瓶、服装纤维

**聚合物的性质：**

**优点：**
✅ **轻便**：易于运输和处理
✅ **耐用**：耐腐蚀、持久
✅ **防水**：不吸水
✅ **灵活或刚性**：可以塑造成不同形状
✅ **生产成本低**：比金属或玻璃成本更低
✅ **绝缘体**：不导电或导热

**缺点：**
⚠️ **不可生物降解**：需要数百年才能分解
⚠️ **易燃**：容易燃烧，产生有毒烟雾
⚠️ **来自化石燃料**：由不可再生的原油制成
⚠️ **污染**：在环境中积累，伤害野生动物

**新加坡常见塑料代码：**

**1. PET (1)** - 水瓶、软饮料瓶
**2. HDPE (2)** - 牛奶壶、洗发水瓶
**3. PVC (3)** - 管道、窗框
**4. LDPE (4)** - 塑料袋、挤压瓶
**5. PP (5)** - 食品容器、瓶盖
**6. PS (6)** - 泡沫杯、食品托盘
**7. 其他** - 混合塑料、CD

**新加坡例子：**

🔹 **组屋**：PVC管道用于管道系统
🔹 **食品包装**：小贩中心的聚丙烯容器
🔹 **饮料瓶**：超市的PET瓶（职总、巨人、昇菘）
🔹 **地铁座位**：合成聚合物织物，耐用"""
        },
        {
            "id": "plastic-pollution-impact",
            "title": "Plastic Pollution and Environmental Impact",
            "title_zh": "塑料污染与环境影响",
            "type": "text",
            "content": """**Plastic pollution** is one of the most serious environmental problems facing the world today.

**The problem:**

**Global plastic production:**
- 400+ million tonnes produced annually worldwide
- Only 9% is recycled
- 12% is incinerated
- 79% ends up in landfills or environment

**Why is plastic pollution harmful?**

**1. Non-biodegradable**
- Takes 450+ years to decompose
- Breaks into microplastics (< 5mm), never fully disappears
- Accumulates in environment over time

**2. Marine pollution**
- 8 million tonnes enter oceans annually
- Forms "garbage patches" (Great Pacific Garbage Patch = 1.6 million km²)
- Fish, turtles, seabirds mistake plastic for food
- Entanglement in plastic debris (fishing nets, six-pack rings)

**3. Microplastics**
- Found in food chain (fish, salt, drinking water)
- Present in human blood and organs
- Health effects still being studied
- Cannot be filtered out easily

**4. Toxic chemicals**
- Plastics contain additives (phthalates, BPA)
- Leach into food, water, soil
- Disrupt hormones, affect reproduction

**5. Greenhouse gas emissions**
- Production from fossil fuels releases CO₂
- Incineration releases CO₂ and toxic fumes
- Decomposition releases methane

**Singapore's plastic problem:**

**Waste statistics:**
🔹 **1.76 million tonnes plastic waste** generated in 2022
🔹 **Only 6% recycled** (very low!)
🔹 **Rest incinerated** at waste-to-energy plants
🔹 **Ash sent to Pulau Semakau** offshore landfill (limited capacity)

**Sources of plastic waste:**
- Packaging (food delivery, online shopping)
- Single-use plastics (bags, straws, utensils)
- Beverage bottles and cans
- Styrofoam food containers

**Marine pollution around Singapore:**
- Plastic debris washes up on beaches (East Coast Park, Sentosa)
- Harms marine life in Johor Straits
- Microplastics found in fish sold at wet markets

**Common single-use plastics in Singapore:**

⚠️ **Plastic bags**: Supermarkets, shops (FairPrice, NTUC)
⚠️ **Straws and cutlery**: Hawker centers, food courts
⚠️ **Food containers**: Takeaway packaging, bubble tea cups
⚠️ **Bubble wrap**: Online shopping deliveries (Lazada, Shopee)
⚠️ **Styrofoam boxes**: Wet market meat, fish packaging

**Impact on wildlife:**

🔹 **Sea turtles**: Mistake plastic bags for jellyfish, choke
🔹 **Seabirds**: Fill stomachs with plastic, starve
🔹 **Fish**: Ingest microplastics, bioaccumulation in food chain
🔹 **Coral reefs**: Plastic debris smothers coral (Sisters' Islands Marine Park)

**Solutions discussed:**

✅ Reduce single-use plastics
✅ Reusable bags, bottles, containers
✅ Proper recycling in blue bins
✅ Support plastic-free initiatives
✅ Choose products with less packaging

(Detailed solutions in next section: Recycling & Sustainability)""",
            "content_zh": """**塑料污染**是当今世界面临的最严重环境问题之一。

**问题：**

**全球塑料生产：**
- 全球每年生产4亿+吨
- 只有9%被回收
- 12%被焚烧
- 79%最终进入垃圾填埋场或环境

**为什么塑料污染有害？**

**1. 不可生物降解**
- 需要450+年才能分解
- 分解成微塑料（<5mm），永远不会完全消失
- 随时间在环境中积累

**2. 海洋污染**
- 每年800万吨进入海洋
- 形成"垃圾带"（大太平洋垃圾带=160万km²）
- 鱼、海龟、海鸟误将塑料当食物
- 被塑料碎片缠住（渔网、六包环）

**3. 微塑料**
- 在食物链中发现（鱼、盐、饮用水）
- 存在于人类血液和器官中
- 健康影响仍在研究中
- 无法轻易过滤

**4. 有毒化学物质**
- 塑料含有添加剂（邻苯二甲酸盐、BPA）
- 渗入食物、水、土壤
- 扰乱激素，影响生殖

**5. 温室气体排放**
- 从化石燃料生产释放CO₂
- 焚烧释放CO₂和有毒烟雾
- 分解释放甲烷

**新加坡的塑料问题：**

**废物统计：**
🔹 **2022年产生176万吨塑料废物**
🔹 **仅6%被回收**（非常低！）
🔹 **其余焚烧**在垃圾焚化厂
🔹 **灰烬送往实马高岛**离岸垃圾填埋场（容量有限）

**塑料废物来源：**
- 包装（外卖、网购）
- 一次性塑料（袋、吸管、餐具）
- 饮料瓶罐
- 泡沫塑料食品容器

**新加坡周围的海洋污染：**
- 塑料碎片冲上海滩（东海岸公园、圣淘沙）
- 伤害柔佛海峡的海洋生物
- 在湿巴刹出售的鱼中发现微塑料

**新加坡常见的一次性塑料：**

⚠️ **塑料袋**：超市、商店（职总、NTUC）
⚠️ **吸管和餐具**：小贩中心、食阁
⚠️ **食品容器**：外卖包装、珍珠奶茶杯
⚠️ **气泡膜**：网购送货（Lazada、Shopee）
⚠️ **泡沫塑料盒**：湿巴刹肉、鱼包装

**对野生动物的影响：**

🔹 **海龟**：误将塑料袋当作水母，窒息
🔹 **海鸟**：用塑料填满胃，饿死
🔹 **鱼**：摄入微塑料，食物链中的生物累积
🔹 **珊瑚礁**：塑料碎片窒息珊瑚（姐妹岛海洋公园）

**讨论的解决方案：**

✅ 减少一次性塑料
✅ 可重复使用的袋子、瓶子、容器
✅ 在蓝色回收箱中正确回收
✅ 支持无塑料倡议
✅ 选择包装较少的产品

（详细解决方案见下一节：回收与可持续性）"""
        },
        {
            "id": "recycling-sustainability",
            "title": "Recycling and Sustainable Solutions",
            "title_zh": "回收与可持续解决方案",
            "type": "text",
            "content": """**Recycling** is the process of collecting and processing materials to make new products, reducing waste and conserving resources.

**Why recycle plastics?**

✅ **Conserves resources**: Saves crude oil (raw material for plastics)
✅ **Saves energy**: Recycling uses less energy than making new plastic
✅ **Reduces waste**: Less plastic in landfills and incinerators
✅ **Protects environment**: Less pollution, less harm to wildlife
✅ **Economic benefits**: Creates jobs, saves money on raw materials

**Plastic recycling process:**

**Step 1: Collection**
- Separate plastics into blue recycling bins
- Check plastic code (1-7) on bottom of container
- Remove food residue, rinse clean

**Step 2: Sorting**
- Plastics sorted by type (PET, HDPE, PP, etc.)
- Manual and automated sorting at recycling facilities
- Contaminated plastics removed

**Step 3: Shredding**
- Plastics shredded into small flakes
- Easier to process and melt

**Step 4: Washing**
- Remove labels, adhesives, dirt
- Clean plastic flakes ready for processing

**Step 5: Melting and pelletizing**
- Plastic flakes melted and formed into pellets
- Pellets used as raw material for new products

**Step 6: Manufacturing**
- Pellets made into new products:
  - Clothing (fleece jackets from PET bottles)
  - Furniture (park benches from recycled plastic)
  - Containers (new bottles, food containers)
  - Building materials (plastic lumber, tiles)

**Singapore's recycling initiatives:**

**National Recycling Programme:**
🔹 **Blue recycling bins**: In HDB estates, condominiums, landed properties
🔹 **Collection schedule**: Weekly or fortnightly pickup
🔹 **Accepted items**: Paper, plastic, metal, glass

**What can be recycled:**
✅ Plastic bottles (PET #1)
✅ Detergent bottles (HDPE #2)
✅ Food containers (PP #5)
✅ Milk jugs, shampoo bottles
✅ Plastic bags (clean and dry)

**What CANNOT be recycled:**
❌ Styrofoam (polystyrene foam)
❌ Food-contaminated plastic
❌ Plastic straws, cutlery (too small)
❌ Disposable diapers
❌ Crisp packets, candy wrappers

**Sustainable alternatives to single-use plastics:**

**At hawker centers and food courts:**
🔹 **Bring own containers**: For takeaway food (some hawkers give discounts!)
🔹 **Refuse plastic bags**: Dine in or bring reusable bags
🔹 **Use metal straws**: Or skip straws entirely

**At supermarkets:**
🔹 **Reusable shopping bags**: Bring own bags (FairPrice, Giant, Cold Storage)
🔹 **Buy loose produce**: Avoid pre-packaged fruits/vegetables
🔹 **Choose products with less packaging**: Bulk buying reduces waste

**For drinks:**
🔹 **Reusable water bottles**: Refill at water fountains (MRT stations, malls)
🔹 **Bring own cup**: For coffee/tea (some cafes give discounts)
🔹 **Glass bottles**: Choose glass over plastic when possible

**Government initiatives:**

**Extended Producer Responsibility (EPR) for e-waste:**
- Manufacturers responsible for collecting and recycling products
- Coming soon for packaging waste

**Disposable carrier bag charge:**
- Supermarkets charge for plastic bags (encourage reusable bags)

**Zero Waste Masterplan:**
- Goal: 70% recycling rate by 2030
- Reduce waste sent to Pulau Semakau landfill
- Extend landfill lifespan beyond 2035

**What YOU can do:**

**Reduce:**
🔹 Say no to single-use plastics
🔹 Choose products with minimal packaging
🔹 Buy only what you need

**Reuse:**
🔹 Use reusable bags, bottles, containers
🔹 Repair broken items instead of replacing
🔹 Donate or sell unwanted items

**Recycle:**
🔹 Clean and sort recyclables properly
🔹 Check plastic codes before recycling
🔹 Participate in recycling programs

**Singapore success stories:**

🔹 **Bring Your Own (BYO) movement**: Many cafes encourage reusable cups
🔹 **Plastic-free initiatives**: Some supermarkets offer paper bags
🔹 **Recycling bins at MRT stations**: Easy access to recycling
🔹 **Second-hand markets**: Carousell, flea markets reduce waste

Every Singaporean's small actions add up to big environmental impact!""",
            "content_zh": """**回收**是收集和处理材料以制造新产品的过程，减少废物并节约资源。

**为什么回收塑料？**

✅ **节约资源**：节省原油（塑料的原材料）
✅ **节能**：回收使用的能量少于制造新塑料
✅ **减少废物**：垃圾填埋场和焚化炉中的塑料更少
✅ **保护环境**：减少污染，减少对野生动物的伤害
✅ **经济效益**：创造就业，节省原材料成本

**塑料回收过程：**

**步骤1：收集**
- 将塑料分类到蓝色回收箱
- 检查容器底部的塑料代码（1-7）
- 去除食物残渣，冲洗干净

**步骤2：分类**
- 按类型分类塑料（PET、HDPE、PP等）
- 在回收设施进行手动和自动分类
- 去除受污染的塑料

**步骤3：粉碎**
- 塑料粉碎成小薄片
- 更容易处理和熔化

**步骤4：清洗**
- 去除标签、粘合剂、污垢
- 清洁塑料薄片准备处理

**步骤5：熔化和造粒**
- 塑料薄片熔化并形成颗粒
- 颗粒用作新产品的原材料

**步骤6：制造**
- 颗粒制成新产品：
  - 服装（PET瓶制成的羊毛夹克）
  - 家具（回收塑料制成的公园长椅）
  - 容器（新瓶子、食品容器）
  - 建筑材料（塑料木材、瓷砖）

**新加坡的回收倡议：**

**国家回收计划：**
🔹 **蓝色回收箱**：在组屋区、公寓、独立式住宅
🔹 **收集时间表**：每周或每两周收集一次
🔹 **接受的物品**：纸、塑料、金属、玻璃

**可以回收的物品：**
✅ 塑料瓶（PET #1）
✅ 洗涤剂瓶（HDPE #2）
✅ 食品容器（PP #5）
✅ 牛奶壶、洗发水瓶
✅ 塑料袋（清洁干燥）

**不能回收的物品：**
❌ 泡沫塑料（聚苯乙烯泡沫）
❌ 受食物污染的塑料
❌ 塑料吸管、餐具（太小）
❌ 一次性尿布
❌ 薯片包装、糖果包装

**一次性塑料的可持续替代品：**

**在小贩中心和食阁：**
🔹 **自带容器**：外卖食物（一些小贩给折扣！）
🔹 **拒绝塑料袋**：堂食或自带可重复使用的袋子
🔹 **使用金属吸管**：或完全不用吸管

**在超市：**
🔹 **可重复使用的购物袋**：自带袋子（职总、巨人、冷藏）
🔹 **购买散装农产品**：避免预包装水果/蔬菜
🔹 **选择包装较少的产品**：批量购买减少废物

**对于饮料：**
🔹 **可重复使用的水瓶**：在饮水机处续杯（地铁站、商场）
🔹 **自带杯子**：喝咖啡/茶（一些咖啡馆给折扣）
🔹 **玻璃瓶**：尽可能选择玻璃而不是塑料

**政府倡议：**

**电子废物的生产者延伸责任（EPR）：**
- 制造商负责收集和回收产品
- 包装废物即将推出

**一次性手提袋收费：**
- 超市收取塑料袋费用（鼓励可重复使用的袋子）

**零废物总体规划：**
- 目标：到2030年回收率达到70%
- 减少送往实马高岛垃圾填埋场的废物
- 延长垃圾填埋场寿命至2035年之后

**你可以做什么：**

**减少：**
🔹 拒绝一次性塑料
🔹 选择包装最少的产品
🔹 只买你需要的东西

**重复使用：**
🔹 使用可重复使用的袋子、瓶子、容器
🔹 修理破损物品而不是更换
🔹 捐赠或出售不需要的物品

**回收：**
🔹 正确清洁和分类可回收物
🔹 回收前检查塑料代码
🔹 参与回收计划

**新加坡成功案例：**

🔹 **自带（BYO）运动**：许多咖啡馆鼓励可重复使用的杯子
🔹 **无塑料倡议**：一些超市提供纸袋
🔹 **地铁站的回收箱**：方便回收
🔹 **二手市场**：旋转拍卖、跳蚤市场减少废物

每个新加坡人的小行动加起来就是巨大的环境影响！"""
        }
    ]
}

# Continue with remaining 5 chapters in next script...

def main():
    content_file = "src/data/content.json"
    backup_file = f"src/data/content-backup-sec3-complete-{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    print("="*70)
    print("ADDING REMAINING SEC 3 SCIENCE LESSONS")
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

    chapters_updated = 0
    sections_added = 0

    for chapter in science['chapters']:
        chapter_id = chapter['id']

        if chapter_id in LESSON_CONTENT:
            # Add sections to this chapter
            new_sections = LESSON_CONTENT[chapter_id]
            chapter['sections'] = new_sections
            chapters_updated += 1
            sections_added += len(new_sections)
            print(f"✓ Added {len(new_sections)} sections to: {chapter['title']}")

    # Save
    print(f"\nSaving updated content...")
    with open(content_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("\n" + "="*70)
    print("✅ LESSON CONTENT ADDED")
    print("="*70)
    print(f"Chapters updated: {chapters_updated}")
    print(f"Sections added: {sections_added}")
    print(f"\nBackup saved: {backup_file}")
    print("\nNote: 3 more chapters covered. Continue with final 5 chapters.")

if __name__ == '__main__':
    main()
