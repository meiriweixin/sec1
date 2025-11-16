#!/usr/bin/env python3
"""
Absolute final 3 Sec 3 Science chapters:
- Reproduction & Cell Division
- Salts & Neutralization
- Turning Effects of Forces
"""

import json
from datetime import datetime

# Final lesson content
LESSON_CONTENT = {
    "reproduction-cell-division": [
        {
            "id": "cell-division-mitosis",
            "title": "Cell Division: Mitosis",
            "title_zh": "细胞分裂：有丝分裂",
            "type": "text",
            "content": """**Cell division** is the process by which a parent cell divides into two daughter cells.

**Why cells divide:**

✅ **Growth**: Organisms grow by producing more cells
✅ **Repair**: Replace damaged or dead cells
✅ **Reproduction**: Asexual reproduction in single-celled organisms

**The cell cycle:**

**Interphase** (90% of cell cycle):
- Cell grows in size
- DNA replicates (doubles)
- Organelles (mitochondria, chloroplasts) replicate
- Cell prepares for division

**Mitosis** (10% of cell cycle):
- Nucleus divides
- Chromosomes are separated
- Two identical nuclei formed

**Cytokinesis**:
- Cytoplasm divides
- Cell membrane pinches inward
- Two daughter cells form

**Stages of mitosis:**

**1. Prophase**
- Chromosomes condense (become visible)
- Each chromosome consists of two chromatids joined at centromere
- Nuclear membrane breaks down
- Spindle fibers form

**2. Metaphase**
- Chromosomes line up along equator of cell
- Spindle fibers attach to centromeres

**3. Anaphase**
- Chromatids separate and move to opposite poles
- Pulled by spindle fibers

**4. Telophase**
- Chromatids reach opposite poles
- Nuclear membranes reform around each set
- Chromosomes uncoil
- Spindle fibers disappear

**Result of mitosis:**

🔹 **Two daughter cells** produced
🔹 **Genetically identical** to parent cell and to each other
🔹 **Same number of chromosomes** as parent cell (46 in humans)

**Importance of mitosis:**

**Growth:**
- Baby grows into adult through millions of cell divisions
- Singapore child grows ~5 cm/year during childhood

**Repair:**
- Skin cells replaced every 2-3 weeks
- Cuts and wounds heal through mitosis
- Broken bones repair through new bone cell production

**Asexual reproduction:**
- Bacteria divide by binary fission (similar to mitosis)
- Yeast cells bud off new cells
- Plant cuttings grow new plants (vegetative propagation)

**Singapore examples:**

**Medical:**
🔹 **Cancer**: Uncontrolled cell division (National Cancer Centre Singapore treats with chemotherapy/radiation)
🔹 **Stem cell research**: A*STAR studies how stem cells divide to regenerate tissues
🔹 **Skin grafts**: SGH uses patient's own skin cells (grown through mitosis) for burn victims

**Agriculture:**
🔹 **Urban farms**: Vegetative propagation for growing herbs, vegetables
🔹 **Orchid cultivation**: Singapore's national flower propagated through tissue culture (mitosis)""",
            "content_zh": """**细胞分裂**是亲代细胞分裂成两个子细胞的过程。

**细胞为什么分裂：**

✅ **生长**：生物体通过产生更多细胞来生长
✅ **修复**：替换受损或死亡的细胞
✅ **繁殖**：单细胞生物的无性繁殖

**细胞周期：**

**间期**（细胞周期的90%）：
- 细胞大小增长
- DNA复制（加倍）
- 细胞器（线粒体、叶绿体）复制
- 细胞为分裂做准备

**有丝分裂**（细胞周期的10%）：
- 细胞核分裂
- 染色体分离
- 形成两个相同的细胞核

**胞质分裂**：
- 细胞质分裂
- 细胞膜向内收缩
- 形成两个子细胞

**有丝分裂的阶段：**

**1. 前期**
- 染色体凝缩（变得可见）
- 每条染色体由两条姐妹染色单体在着丝粒处连接
- 核膜破裂
- 纺锤丝形成

**2. 中期**
- 染色体排列在细胞赤道上
- 纺锤丝附着在着丝粒上

**3. 后期**
- 染色单体分离并移向相反的极
- 被纺锤丝拉动

**4. 末期**
- 染色单体到达相反的极
- 核膜在每组周围重新形成
- 染色体解螺旋
- 纺锤丝消失

**有丝分裂的结果：**

🔹 产生**两个子细胞**
🔹 与亲代细胞和彼此**遗传相同**
🔹 与亲代细胞**染色体数量相同**（人类46条）

**有丝分裂的重要性：**

**生长：**
- 婴儿通过数百万次细胞分裂长成成人
- 新加坡儿童在童年期间每年长约5厘米

**修复：**
- 皮肤细胞每2-3周更换一次
- 伤口通过有丝分裂愈合
- 骨折通过新骨细胞产生修复

**无性繁殖：**
- 细菌通过二分裂分裂（类似于有丝分裂）
- 酵母细胞芽出新细胞
- 植物插条长出新植物（营养繁殖）

**新加坡例子：**

**医学：**
🔹 **癌症**：不受控制的细胞分裂（新加坡国家癌症中心用化疗/放疗治疗）
🔹 **干细胞研究**：A*STAR研究干细胞如何分裂以再生组织
🔹 **植皮**：新加坡中央医院使用患者自己的皮肤细胞（通过有丝分裂生长）治疗烧伤受害者

**农业：**
🔹 **城市农场**：通过营养繁殖种植草药、蔬菜
🔹 **兰花栽培**：新加坡国花通过组织培养（有丝分裂）繁殖"""
        },
        {
            "id": "meiosis-sexual-reproduction",
            "title": "Meiosis and Sexual Reproduction",
            "title_zh": "减数分裂与有性生殖",
            "type": "text",
            "content": """**Meiosis** is a special type of cell division that produces sex cells (gametes) for sexual reproduction.

**Comparison: Mitosis vs. Meiosis**

**Mitosis:**
🔹 Produces **2** daughter cells
🔹 Daughter cells are **genetically identical**
🔹 Chromosome number **stays the same** (46 → 46)
🔹 For **growth and repair**

**Meiosis:**
🔹 Produces **4** daughter cells (gametes)
🔹 Daughter cells are **genetically different**
🔹 Chromosome number **halves** (46 → 23)
🔹 For **sexual reproduction**

**Process of meiosis:**

**Before meiosis:**
- DNA replicates (chromosomes double)
- Cell has 46 chromosomes (23 pairs)

**Meiosis I** (first division):
- **Homologous chromosomes** pair up
- **Crossing over** occurs: chromosomes exchange genetic material
- Homologous pairs separate
- Two cells formed, each with 23 chromosomes (still doubled)

**Meiosis II** (second division):
- Sister chromatids separate
- Four cells formed, each with 23 single chromosomes
- These are **gametes** (sex cells)

**Types of gametes:**

**Male gametes**: Sperm cells (spermatozoa)
- Small, mobile (tail for swimming)
- 23 chromosomes
- Millions produced daily

**Female gametes**: Egg cells (ova)
- Large, non-mobile (contains food reserves)
- 23 chromosomes
- One released per month (ovulation)

**Fertilization:**

**Process:**
1. Sperm (23 chromosomes) meets egg (23 chromosomes)
2. Sperm nucleus fuses with egg nucleus
3. **Zygote** formed with 46 chromosomes (23 pairs restored)
4. Zygote divides by mitosis to form embryo

**Why sexual reproduction creates variation:**

**1. Crossing over** during meiosis
- Chromosomes exchange segments
- New combination of genes

**2. Independent assortment**
- Random distribution of chromosomes to gametes
- Each gamete has different combination

**3. Random fertilization**
- Any sperm can fertilize the egg
- Different genetic combinations

**Advantages of sexual reproduction:**

✅ **Genetic variation**: Offspring different from parents
✅ **Adaptation**: Population can adapt to changing environment
✅ **Evolution**: Natural selection acts on variation
✅ **Disease resistance**: Some offspring may resist diseases

**Disadvantages:**

⚠️ Requires two parents (male and female)
⚠️ Takes more time and energy
⚠️ Fewer offspring produced

**Human reproduction in Singapore:**

**Fertility:**
🔹 **Birth rate**: Singapore has low birth rate (~1.1 children per woman)
🔹 **Government incentives**: Baby Bonus, childcare subsidies to encourage births
🔹 **IVF clinics**: KK Women's and Children's Hospital offers fertility treatments

**Sex education:**
🔹 **Schools**: MOE teaches reproduction in Secondary 1-2 Science
🔹 **HPB programs**: Health Promotion Board provides resources
🔹 **Understanding changes**: Puberty, menstrual cycle, responsible behavior

**Genetics:**
🔹 **Inheritance**: Children inherit 23 chromosomes from each parent
🔹 **Genetic diversity**: Singapore's multiracial population shows variation
🔹 **Genetic counseling**: Available at hospitals for couples planning pregnancy""",
            "content_zh": """**减数分裂**是一种特殊的细胞分裂类型，为有性生殖产生性细胞（配子）。

**比较：有丝分裂vs减数分裂**

**有丝分裂：**
🔹 产生**2**个子细胞
🔹 子细胞**遗传相同**
🔹 染色体数量**保持不变**（46 → 46）
🔹 用于**生长和修复**

**减数分裂：**
🔹 产生**4**个子细胞（配子）
🔹 子细胞**遗传不同**
🔹 染色体数量**减半**（46 → 23）
🔹 用于**有性生殖**

**减数分裂过程：**

**减数分裂前：**
- DNA复制（染色体加倍）
- 细胞有46条染色体（23对）

**减数分裂I**（第一次分裂）：
- **同源染色体**配对
- **交叉互换**发生：染色体交换遗传物质
- 同源对分离
- 形成两个细胞，每个有23条染色体（仍然加倍）

**减数分裂II**（第二次分裂）：
- 姐妹染色单体分离
- 形成四个细胞，每个有23条单染色体
- 这些是**配子**（性细胞）

**配子类型：**

**雄配子**：精子细胞
- 小、移动（尾巴用于游泳）
- 23条染色体
- 每天产生数百万

**雌配子**：卵细胞
- 大、不移动（含有食物储备）
- 23条染色体
- 每月释放一个（排卵）

**受精：**

**过程：**
1. 精子（23条染色体）遇到卵子（23条染色体）
2. 精子核与卵子核融合
3. 形成**受精卵**，有46条染色体（恢复23对）
4. 受精卵通过有丝分裂分裂形成胚胎

**为什么有性生殖产生变异：**

**1. 交叉互换**在减数分裂期间
- 染色体交换片段
- 基因的新组合

**2. 独立分配**
- 染色体随机分配到配子
- 每个配子有不同的组合

**3. 随机受精**
- 任何精子都可以使卵子受精
- 不同的遗传组合

**有性生殖的优点：**

✅ **遗传变异**：后代与父母不同
✅ **适应**：种群可以适应变化的环境
✅ **进化**：自然选择作用于变异
✅ **抗病性**：一些后代可能抵抗疾病

**缺点：**

⚠️ 需要两个亲本（雄性和雌性）
⚠️ 需要更多时间和精力
⚠️ 产生的后代更少

**新加坡的人类生殖：**

**生育率：**
🔹 **出生率**：新加坡出生率低（每名妇女约1.1个孩子）
🔹 **政府激励**：婴儿花红、托儿补贴鼓励生育
🔹 **IVF诊所**：竹脚妇幼医院提供生育治疗

**性教育：**
🔹 **学校**：MOE在中一至中二科学课程中教授生殖
🔹 **HPB计划**：健康促进局提供资源
🔹 **了解变化**：青春期、月经周期、负责任行为

**遗传学：**
🔹 **遗传**：孩子从每个亲本继承23条染色体
🔹 **遗传多样性**：新加坡多种族人口显示变异
🔹 **遗传咨询**：医院为计划怀孕的夫妇提供"""
        },
        {
            "id": "human-reproductive-system",
            "title": "Human Reproductive System",
            "title_zh": "人类生殖系统",
            "type": "text",
            "content": """**The reproductive system** enables humans to produce offspring through sexual reproduction.

**Male reproductive system:**

**Key organs and functions:**

**1. Testes** (singular: testis)
- Produce sperm cells (millions daily)
- Produce testosterone hormone
- Located in scrotum (outside body, cooler temperature for sperm production)

**2. Scrotum**
- Sac holding testes
- Keeps testes 2-3°C cooler than body temperature

**3. Sperm ducts** (vas deferens)
- Tubes carrying sperm from testes
- Sperm mixes with fluids from glands

**4. Glands** (prostate, seminal vesicles)
- Secrete fluids that nourish and protect sperm
- Sperm + fluids = semen

**5. Urethra**
- Tube through penis
- Carries semen out during ejaculation

**6. Penis**
- Deposits semen into female reproductive system

**Female reproductive system:**

**Key organs and functions:**

**1. Ovaries** (left and right)
- Produce egg cells (ova)
- Release one egg per month (ovulation)
- Produce estrogen and progesterone hormones

**2. Oviducts** (fallopian tubes)
- Tubes connecting ovaries to uterus
- **Site of fertilization**: Sperm meets egg here
- Cilia and muscle contractions move egg to uterus

**3. Uterus** (womb)
- Muscular organ where embryo develops
- Inner lining (endometrium) thickens each month
- If no fertilization, lining breaks down (menstruation)

**4. Cervix**
- Ring of muscle at uterus entrance
- Produces mucus

**5. Vagina**
- Receives penis during sexual intercourse
- Birth canal during childbirth

**The menstrual cycle** (approximately 28 days):

**Day 1-5: Menstruation**
- Uterus lining breaks down
- Blood and tissue leave through vagina (period)

**Day 6-13: Repair and thickening**
- Uterus lining repairs and thickens
- Egg matures in ovary

**Day 14: Ovulation**
- Mature egg released from ovary
- Egg travels down oviduct
- **Fertile period**: Egg can be fertilized for ~24 hours

**Day 15-28: Maintenance**
- Uterus lining maintained (ready for embryo)
- If no fertilization: progesterone decreases, lining breaks down
- Cycle repeats

**Pregnancy:**

**Fertilization → Implantation → Development:**

1. **Fertilization**: Sperm nucleus fuses with egg nucleus in oviduct
2. **Zygote**: Fertilized egg with 46 chromosomes
3. **Cell division**: Zygote divides by mitosis as it moves to uterus
4. **Implantation** (6-7 days): Embryo embeds in uterus lining
5. **Placenta forms**: Exchange of nutrients, oxygen, waste between mother and fetus
6. **Development** (9 months): Fetus grows and develops

**Functions of placenta:**

✅ **Nutrients**: Glucose, amino acids pass from mother to fetus
✅ **Oxygen**: O₂ diffuses from mother's blood to fetus
✅ **Waste removal**: CO₂, urea pass from fetus to mother
✅ **Protection**: Barrier against some harmful substances
⚠️ **No direct blood contact**: Mother's and fetus's blood don't mix

**Singapore maternal healthcare:**

**Antenatal care:**
🔹 **Regular checkups**: KK Women's and Children's Hospital, NUH, SGH
🔹 **Ultrasound scans**: Monitor fetus development
🔹 **Blood tests**: Check for genetic conditions, infections
🔹 **Maternal support**: Parentcraft classes, breastfeeding support

**Delivery:**
🔹 **Public hospitals**: Subsidized rates for citizens
🔹 **Maternity leave**: 16 weeks for working mothers
🔹 **Baby Bonus**: Government cash gift for newborns

**Family planning:**
🔹 **Contraception**: Available at clinics
🔹 **Education**: HPB provides family planning resources
🔹 **Genetic screening**: Thalassemia, G6PD screening for couples""",
            "content_zh": """**生殖系统**使人类能够通过有性生殖产生后代。

**男性生殖系统：**

**关键器官和功能：**

**1. 睾丸**
- 产生精子细胞（每天数百万）
- 产生睾酮激素
- 位于阴囊中（在身体外部，精子产生需要较低温度）

**2. 阴囊**
- 容纳睾丸的囊
- 使睾丸比体温低2-3°C

**3. 输精管**
- 从睾丸输送精子的管道
- 精子与腺体分泌的液体混合

**4. 腺体**（前列腺、精囊）
- 分泌滋养和保护精子的液体
- 精子+液体=精液

**5. 尿道**
- 穿过阴茎的管道
- 在射精期间输送精液

**6. 阴茎**
- 将精液沉积到女性生殖系统中

**女性生殖系统：**

**关键器官和功能：**

**1. 卵巢**（左右）
- 产生卵细胞
- 每月释放一个卵子（排卵）
- 产生雌激素和孕激素

**2. 输卵管**
- 连接卵巢和子宫的管道
- **受精部位**：精子在这里遇到卵子
- 纤毛和肌肉收缩将卵子移到子宫

**3. 子宫**（子宫）
- 胚胎发育的肌肉器官
- 内膜（子宫内膜）每月增厚
- 如果没有受精，内膜破裂（月经）

**4. 子宫颈**
- 子宫入口的肌肉环
- 产生粘液

**5. 阴道**
- 在性交期间接收阴茎
- 分娩期间的产道

**月经周期**（约28天）：

**第1-5天：月经**
- 子宫内膜破裂
- 血液和组织通过阴道离开（经期）

**第6-13天：修复和增厚**
- 子宫内膜修复和增厚
- 卵子在卵巢中成熟

**第14天：排卵**
- 成熟卵子从卵巢释放
- 卵子沿输卵管移动
- **受孕期**：卵子可以受精约24小时

**第15-28天：维持**
- 子宫内膜维持（为胚胎做好准备）
- 如果没有受精：孕激素减少，内膜破裂
- 周期重复

**怀孕：**

**受精→着床→发育：**

1. **受精**：精子核与输卵管中的卵子核融合
2. **受精卵**：有46条染色体的受精卵
3. **细胞分裂**：受精卵在移动到子宫时通过有丝分裂分裂
4. **着床**（6-7天）：胚胎嵌入子宫内膜
5. **胎盘形成**：母亲和胎儿之间营养、氧气、废物的交换
6. **发育**（9个月）：胎儿生长和发育

**胎盘的功能：**

✅ **营养**：葡萄糖、氨基酸从母亲传递给胎儿
✅ **氧气**：O₂从母亲的血液扩散到胎儿
✅ **废物去除**：CO₂、尿素从胎儿传递给母亲
✅ **保护**：阻挡一些有害物质
⚠️ **没有直接血液接触**：母亲和胎儿的血液不混合

**新加坡孕产妇保健：**

**产前护理：**
🔹 **定期检查**：竹脚妇幼医院、国立大学医院、新加坡中央医院
🔹 **超声波扫描**：监测胎儿发育
🔹 **血液检查**：检查遗传状况、感染
🔹 **孕妇支持**：育儿课程、母乳喂养支持

**分娩：**
🔹 **公立医院**：公民享受补贴费率
🔹 **产假**：在职母亲16周
🔹 **婴儿花红**：政府为新生儿提供现金礼物

**计划生育：**
🔹 **避孕**：诊所提供
🔹 **教育**：HPB提供计划生育资源
🔹 **遗传筛查**：夫妇的地中海贫血、G6PD筛查"""
        }
    ],

    "salts-neutralization": [
        {
            "id": "what-are-salts",
            "title": "Salts and Neutralization Reactions",
            "title_zh": "盐和中和反应",
            "type": "text",
            "content": """**Salts** are ionic compounds formed when an acid reacts with a base.

**What is neutralization?**

**Definition**: Reaction between an acid and a base to produce salt and water only

**General equation:**

**Acid + Base → Salt + Water**

**Ionic equation:**

**H⁺(aq) + OH⁻(aq) → H₂O(l)**

This shows that neutralization is the reaction between hydrogen ions from the acid and hydroxide ions from the base to form water.

**Examples of neutralization:**

**1. Hydrochloric acid + Sodium hydroxide**

HCl + NaOH → NaCl + H₂O
(acid) (base) (salt) (water)

**2. Sulfuric acid + Potassium hydroxide**

H₂SO₄ + 2KOH → K₂SO₄ + 2H₂O

**3. Nitric acid + Calcium hydroxide**

2HNO₃ + Ca(OH)₂ → Ca(NO₃)₂ + 2H₂O

**Naming salts:**

**Salt name = Metal + Non-metal part of acid**

**From the acid:**
- Hydrochloric acid (HCl) → chloride
- Sulfuric acid (H₂SO₄) → sulfate
- Nitric acid (HNO₃) → nitrate
- Ethanoic acid (CH₃COOH) → ethanoate

**From the base:**
- Sodium hydroxide → sodium
- Potassium hydroxide → potassium
- Calcium hydroxide → calcium
- Magnesium hydroxide → magnesium

**Examples:**

HCl + NaOH → **Sodium chloride** + H₂O
H₂SO₄ + MgO → **Magnesium sulfate** + H₂O
HNO₃ + KOH → **Potassium nitrate** + H₂O

**Types of neutralization reactions:**

**1. Acid + Metal oxide**

Acid + Metal oxide → Salt + Water

Example: 2HCl + CuO → CuCl₂ + H₂O

**2. Acid + Metal hydroxide**

Acid + Metal hydroxide → Salt + Water

Example: H₂SO₄ + 2NaOH → Na₂SO₄ + 2H₂O

**3. Acid + Metal carbonate**

Acid + Metal carbonate → Salt + Water + Carbon dioxide

Example: 2HCl + CaCO₃ → CaCl₂ + H₂O + CO₂

**Note**: This produces CO₂ gas (fizzing/effervescence)

**4. Acid + Ammonia**

Acid + Ammonia → Ammonium salt (no water)

Example: HCl + NH₃ → NH₄Cl

**Heat changes in neutralization:**

- Neutralization is **exothermic**: Heat is released
- Temperature of solution increases
- Can be measured with thermometer

**Practical applications in Singapore:**

**Health and medicine:**
🔹 **Antacids**: Neutralize excess stomach acid (gastric reflux)
  - Active ingredient: Magnesium hydroxide, calcium carbonate
  - MgCO₃ + 2HCl → MgCl₂ + H₂O + CO₂

🔹 **Insect stings**:
  - Bee sting (acidic): Apply baking soda paste (sodium bicarbonate - weak base)
  - Wasp sting (alkaline): Apply vinegar (weak acid)

**Agriculture:**
🔹 **Soil treatment**: Add lime (calcium hydroxide) to acidic soil
  - Makes soil suitable for crops
  - Singapore urban farms adjust soil pH

**Environment:**
🔹 **Acid rain neutralization**: Lakes treated with lime
🔹 **Water treatment** (PUB): Adjust pH of water supply

**Industry:**
🔹 **Waste treatment** (Jurong Island): Neutralize acidic/alkaline industrial waste before disposal
🔹 **Chemical spills**: Use appropriate substance to neutralize

**Daily life:**
🔹 **Toothpaste**: Contains bases to neutralize acids from food (prevent tooth decay)
🔹 **Cleaning**: Vinegar (acid) neutralizes alkaline stains; baking soda (base) neutralizes acidic stains""",
            "content_zh": """**盐**是酸与碱反应时形成的离子化合物。

**什么是中和？**

**定义**：酸和碱之间的反应，只产生盐和水

**一般方程式：**

**酸+碱→盐+水**

**离子方程式：**

**H⁺(aq) + OH⁻(aq) → H₂O(l)**

这表明中和是酸的氢离子和碱的氢氧根离子之间的反应形成水。

**中和的例子：**

**1. 盐酸+氢氧化钠**

HCl + NaOH → NaCl + H₂O
（酸）（碱）（盐）（水）

**2. 硫酸+氢氧化钾**

H₂SO₄ + 2KOH → K₂SO₄ + 2H₂O

**3. 硝酸+氢氧化钙**

2HNO₃ + Ca(OH)₂ → Ca(NO₃)₂ + 2H₂O

**命名盐：**

**盐名=金属+酸的非金属部分**

**来自酸：**
- 盐酸（HCl）→氯化物
- 硫酸（H₂SO₄）→硫酸盐
- 硝酸（HNO₃）→硝酸盐
- 乙酸（CH₃COOH）→乙酸盐

**来自碱：**
- 氢氧化钠→钠
- 氢氧化钾→钾
- 氢氧化钙→钙
- 氢氧化镁→镁

**例子：**

HCl + NaOH → **氯化钠** + H₂O
H₂SO₄ + MgO → **硫酸镁** + H₂O
HNO₃ + KOH → **硝酸钾** + H₂O

**中和反应类型：**

**1. 酸+金属氧化物**

酸+金属氧化物→盐+水

例子：2HCl + CuO → CuCl₂ + H₂O

**2. 酸+金属氢氧化物**

酸+金属氢氧化物→盐+水

例子：H₂SO₄ + 2NaOH → Na₂SO₄ + 2H₂O

**3. 酸+金属碳酸盐**

酸+金属碳酸盐→盐+水+二氧化碳

例子：2HCl + CaCO₃ → CaCl₂ + H₂O + CO₂

**注意**：这产生CO₂气体（起泡/沸腾）

**4. 酸+氨**

酸+氨→铵盐（无水）

例子：HCl + NH₃ → NH₄Cl

**中和中的热变化：**

- 中和是**放热**：释放热量
- 溶液温度升高
- 可以用温度计测量

**新加坡的实际应用：**

**健康和医药：**
🔹 **抗酸剂**：中和过量胃酸（胃酸反流）
  - 活性成分：氢氧化镁、碳酸钙
  - MgCO₃ + 2HCl → MgCl₂ + H₂O + CO₂

🔹 **昆虫叮咬**：
  - 蜜蜂叮咬（酸性）：涂抹小苏打糊（碳酸氢钠-弱碱）
  - 黄蜂叮咬（碱性）：涂抹醋（弱酸）

**农业：**
🔹 **土壤处理**：向酸性土壤添加石灰（氢氧化钙）
  - 使土壤适合作物
  - 新加坡城市农场调整土壤pH

**环境：**
🔹 **酸雨中和**：用石灰处理湖泊
🔹 **水处理**（PUB）：调整供水的pH

**工业：**
🔹 **废物处理**（裕廊岛）：在处理前中和酸性/碱性工业废物
🔹 **化学泄漏**：使用适当物质中和

**日常生活：**
🔹 **牙膏**：含有碱以中和食物中的酸（防止蛀牙）
🔹 **清洁**：醋（酸）中和碱性污渍；小苏打（碱）中和酸性污渍"""
        },
        {
            "id": "preparing-salts",
            "title": "Preparing Soluble and Insoluble Salts",
            "title_zh": "制备可溶盐和不溶盐",
            "type": "text",
            "content": """**Preparing salts** in the laboratory involves different methods depending on whether the salt is soluble or insoluble.

**Solubility rules to remember:**

**Soluble salts:**
✅ All sodium, potassium, ammonium salts
✅ All nitrates
✅ Most chlorides (except silver chloride, lead chloride)
✅ Most sulfates (except barium sulfate, calcium sulfate, lead sulfate)

**Insoluble salts:**
❌ Most carbonates (except sodium, potassium, ammonium)
❌ Most hydroxides (except sodium, potassium, calcium)
❌ All sulfides (except Group 1 metals and ammonium)

**Method 1: Preparing soluble salts - Titration method**

**Use when**: Making soluble salt from soluble acid + soluble base

**Steps:**

1. **Titration**: Use indicator to find exact volumes of acid and base that neutralize
2. **Repeat without indicator**: Mix exact volumes found in step 1
3. **Evaporate**: Heat solution gently to evaporate half the water
4. **Crystallize**: Leave to cool, crystals form
5. **Filter and dry**: Collect crystals, pat dry with filter paper

**Example: Preparing sodium chloride**

1. Titrate HCl with NaOH using phenolphthalein indicator
2. Record volumes (e.g., 25 cm³ HCl neutralizes 25 cm³ NaOH)
3. Mix exact volumes without indicator
4. Evaporate, crystallize, filter, dry
5. Obtain white crystals of NaCl

**Method 2: Preparing soluble salts - Excess insoluble base/carbonate**

**Use when**: Making soluble salt from acid + insoluble base/carbonate/metal

**Steps:**

1. **Add excess**: Add insoluble base/carbonate to acid until no more dissolves
2. **Filter**: Remove excess unreacted solid
3. **Evaporate**: Heat filtrate to evaporate half the water
4. **Crystallize**: Leave to cool, crystals form
5. **Filter and dry**: Collect crystals

**Example: Preparing copper(II) sulfate**

1. Add excess copper(II) oxide to warm sulfuric acid
   - H₂SO₄ + CuO → CuSO₄ + H₂O
2. Stir until no more CuO dissolves (solution turns blue)
3. Filter to remove excess CuO
4. Evaporate filtrate until crystals appear on surface
5. Cool, filter, dry → Blue crystals of CuSO₄·5H₂O

**Method 3: Preparing insoluble salts - Precipitation**

**Use when**: Making insoluble salt from two soluble salts

**Steps:**

1. **Mix solutions**: Mix two soluble salt solutions
2. **Precipitate forms**: Insoluble salt forms as solid
3. **Filter**: Collect precipitate on filter paper
4. **Wash**: Rinse with distilled water
5. **Dry**: Pat dry or leave in warm place

**Example: Preparing barium sulfate (white precipitate)**

1. Mix barium chloride solution + sodium sulfate solution
   - BaCl₂(aq) + Na₂SO₄(aq) → BaSO₄(s) + 2NaCl(aq)
2. White precipitate of BaSO₄ forms
3. Filter to collect BaSO₄
4. Wash with distilled water
5. Dry

**Example: Preparing lead(II) iodide (yellow precipitate)**

1. Mix lead(II) nitrate solution + potassium iodide solution
   - Pb(NO₃)₂(aq) + 2KI(aq) → PbI₂(s) + 2KNO₃(aq)
2. Yellow precipitate of PbI₂ forms
3. Filter, wash, dry

**Singapore school laboratory:**

**Safety precautions:**
⚠️ Wear safety goggles
⚠️ Handle acids/bases carefully
⚠️ Wash hands after experiment

**Common experiments in Sec 3:**
🔹 **Preparing copper sulfate**: Demonstrates excess base method
🔹 **Preparing sodium chloride**: Demonstrates titration/crystallization
🔹 **Testing for ions**: Use precipitation to identify ions (barium sulfate test for sulfate ions)

**Industrial salt production:**

**Sodium chloride (table salt):**
🔹 **Sea water evaporation**: Singapore imports sea salt
🔹 **Purification**: Remove impurities for food-grade salt

**Fertilizers:**
🔹 **Ammonium nitrate**: From ammonia + nitric acid
🔹 **Used in agriculture**: Provide nitrogen for plant growth""",
            "content_zh": """**制备盐**在实验室中涉及不同的方法，这取决于盐是可溶的还是不溶的。

**要记住的溶解度规则：**

**可溶盐：**
✅ 所有钠、钾、铵盐
✅ 所有硝酸盐
✅ 大多数氯化物（除氯化银、氯化铅外）
✅ 大多数硫酸盐（除硫酸钡、硫酸钙、硫酸铅外）

**不溶盐：**
❌ 大多数碳酸盐（除钠、钾、铵外）
❌ 大多数氢氧化物（除钠、钾、钙外）
❌ 所有硫化物（除第1族金属和铵外）

**方法1：制备可溶盐-滴定法**

**何时使用**：从可溶酸+可溶碱制备可溶盐

**步骤：**

1. **滴定**：使用指示剂找到中和的酸和碱的确切体积
2. **不使用指示剂重复**：混合步骤1中找到的确切体积
3. **蒸发**：轻轻加热溶液以蒸发一半的水
4. **结晶**：冷却，晶体形成
5. **过滤和干燥**：收集晶体，用滤纸拍干

**例子：制备氯化钠**

1. 使用酚酞指示剂用NaOH滴定HCl
2. 记录体积（例如，25 cm³ HCl中和25 cm³ NaOH）
3. 不使用指示剂混合确切体积
4. 蒸发、结晶、过滤、干燥
5. 获得白色NaCl晶体

**方法2：制备可溶盐-过量不溶碱/碳酸盐**

**何时使用**：从酸+不溶碱/碳酸盐/金属制备可溶盐

**步骤：**

1. **添加过量**：向酸中添加不溶碱/碳酸盐，直到不再溶解
2. **过滤**：去除过量的未反应固体
3. **蒸发**：加热滤液以蒸发一半的水
4. **结晶**：冷却，晶体形成
5. **过滤和干燥**：收集晶体

**例子：制备硫酸铜**

1. 向温暖的硫酸中添加过量的氧化铜
   - H₂SO₄ + CuO → CuSO₄ + H₂O
2. 搅拌直到不再溶解CuO（溶液变蓝）
3. 过滤以去除过量的CuO
4. 蒸发滤液直到表面出现晶体
5. 冷却、过滤、干燥→CuSO₄·5H₂O的蓝色晶体

**方法3：制备不溶盐-沉淀**

**何时使用**：从两种可溶盐制备不溶盐

**步骤：**

1. **混合溶液**：混合两种可溶盐溶液
2. **沉淀形成**：不溶盐形成固体
3. **过滤**：在滤纸上收集沉淀
4. **洗涤**：用蒸馏水冲洗
5. **干燥**：拍干或放在温暖的地方

**例子：制备硫酸钡（白色沉淀）**

1. 混合氯化钡溶液+硫酸钠溶液
   - BaCl₂(aq) + Na₂SO₄(aq) → BaSO₄(s) + 2NaCl(aq)
2. 形成BaSO₄的白色沉淀
3. 过滤收集BaSO₄
4. 用蒸馏水洗涤
5. 干燥

**例子：制备碘化铅（黄色沉淀）**

1. 混合硝酸铅溶液+碘化钾溶液
   - Pb(NO₃)₂(aq) + 2KI(aq) → PbI₂(s) + 2KNO₃(aq)
2. 形成PbI₂的黄色沉淀
3. 过滤、洗涤、干燥

**新加坡学校实验室：**

**安全预防措施：**
⚠️ 戴安全护目镜
⚠️ 小心处理酸/碱
⚠️ 实验后洗手

**中三常见实验：**
🔹 **制备硫酸铜**：演示过量碱法
🔹 **制备氯化钠**：演示滴定/结晶
🔹 **离子测试**：使用沉淀识别离子（硫酸钡测试硫酸根离子）

**工业盐生产：**

**氯化钠（食盐）：**
🔹 **海水蒸发**：新加坡进口海盐
🔹 **纯化**：去除杂质以获得食品级盐

**肥料：**
🔹 **硝酸铵**：来自氨+硝酸
🔹 **用于农业**：为植物生长提供氮"""
        },
        {
            "id": "uses-of-salts",
            "title": "Uses of Common Salts",
            "title_zh": "常见盐的用途",
            "type": "text",
            "content": """**Common salts** have many important applications in industry, agriculture, medicine, and daily life.

**Sodium chloride (NaCl) - Table salt:**

**Uses:**
🔹 **Food preservation**: Prevents bacterial growth in meat, fish
🔹 **Seasoning**: Enhances flavor in cooking
🔹 **De-icing**: Melts ice on roads (lowers freezing point)
🔹 **Chlor-alkali industry**: Produces chlorine, sodium hydroxide, hydrogen

**Singapore context:**
- Used in hawker center cooking
- Imported for food industry
- PUB uses salt in water treatment (chlorine production)

**Calcium carbonate (CaCO₃) - Limestone/chalk:**

**Uses:**
🔹 **Construction**: Making cement and concrete
🔹 **Agriculture**: Neutralizes acidic soil (as lime)
🔹 **Glass making**: Raw material for glass production
🔹 **Antacids**: Neutralizes stomach acid

**Singapore:**
- Imported for construction (HDB buildings, infrastructure)
- Used in cement production

**Ammonium nitrate (NH₄NO₃) - Fertilizer:**

**Uses:**
🔹 **Agriculture**: Provides nitrogen for plant growth
🔹 **Explosives**: Component in mining explosives

**Safety**: Can explode if heated or contaminated

**Singapore:**
- Urban farms use nitrogen fertilizers
- Strict regulations on storage

**Copper(II) sulfate (CuSO₄) - Blue vitriol:**

**Uses:**
🔹 **Fungicide**: Kills fungal diseases on plants
🔹 **Algae control**: Prevents algae growth in pools, ponds
🔹 **Electroplating**: Copper coating of objects

**Singapore:**
- Used in swimming pool maintenance
- Gardens by the Bay uses for plant disease control

**Barium sulfate (BaSO₄):**

**Uses:**
🔹 **X-ray contrast**: Patient drinks "barium meal" before X-ray (opaque to X-rays)
🔹 **Paint**: White pigment

**Singapore hospitals** (SGH, NUH): Use for gastrointestinal X-rays

**Sodium hydrogen carbonate (NaHCO₃) - Baking soda:**

**Uses:**
🔹 **Baking**: Produces CO₂ gas, makes cakes rise
🔹 **Antacid**: Neutralizes excess stomach acid
🔹 **Cleaning**: Mild abrasive, deodorizer
🔹 **Fire extinguisher**: Releases CO₂ when heated

**Singapore:**
- Common in home baking
- Sold at FairPrice, Cold Storage supermarkets

**Silver nitrate (AgNO₃):**

**Uses:**
🔹 **Photography**: Light-sensitive compound (traditional film)
🔹 **Testing for chlorides**: Forms white precipitate with Cl⁻ ions
🔹 **Antiseptic**: Kills bacteria

**Sodium nitrate (NaNO₃):**

**Uses:**
🔹 **Fertilizer**: Provides nitrogen for plants
🔹 **Food preservative**: Curing meat (bacon, ham)
🔹 **Fireworks**: Provides oxygen for combustion

**Magnesium sulfate (MgSO₄) - Epsom salt:**

**Uses:**
🔹 **Medicine**: Laxative, relieves muscle soreness
🔹 **Agriculture**: Provides magnesium for plants

**Calcium sulfate (CaSO₄):**

**Uses:**
🔹 **Plaster of Paris**: Making casts for broken bones
🔹 **Construction**: Plasterboard for walls
🔹 **Tofu making**: Coagulant in soy milk

**Singapore:**
- Hospitals use for bone casts
- Construction industry uses plasterboard
- Tofu shops use for tofu production

**Environmental and health considerations:**

**Advantages:**
✅ Many salts are essential for life (sodium, potassium, calcium salts)
✅ Used in medicine, agriculture, industry
✅ Some are natural and biodegradable

**Concerns:**
⚠️ **Excessive salt intake**: High blood pressure, heart disease (WHO recommends <5g/day)
⚠️ **Fertilizer runoff**: Eutrophication of waterways
⚠️ **Heavy metal salts**: Toxic (lead, mercury salts)
⚠️ **Explosive salts**: Safety hazards (ammonium nitrate)

**Singapore health initiatives:**
🔹 **Healthier Dining Programme**: Reduced-salt options at hawker centers
🔹 **HPB campaigns**: Encourage less salt consumption
🔹 **Food labeling**: Nutrition information shows sodium content""",
            "content_zh": """**常见盐**在工业、农业、医药和日常生活中有许多重要应用。

**氯化钠（NaCl）-食盐：**

**用途：**
🔹 **食品保存**：防止肉、鱼中的细菌生长
🔹 **调味**：增强烹饪中的风味
🔹 **除冰**：融化道路上的冰（降低冰点）
🔹 **氯碱工业**：生产氯、氢氧化钠、氢气

**新加坡背景：**
- 用于小贩中心烹饪
- 为食品工业进口
- PUB在水处理中使用盐（生产氯）

**碳酸钙（CaCO₃）-石灰石/粉笔：**

**用途：**
🔹 **建筑**：制造水泥和混凝土
🔹 **农业**：中和酸性土壤（作为石灰）
🔹 **玻璃制造**：玻璃生产的原材料
🔹 **抗酸剂**：中和胃酸

**新加坡：**
- 为建筑进口（组屋、基础设施）
- 用于水泥生产

**硝酸铵（NH₄NO₃）-肥料：**

**用途：**
🔹 **农业**：为植物生长提供氮
🔹 **炸药**：采矿炸药的成分

**安全**：如果加热或污染可能爆炸

**新加坡：**
- 城市农场使用氮肥
- 严格的储存法规

**硫酸铜（CuSO₄）-蓝矾：**

**用途：**
🔹 **杀菌剂**：杀死植物上的真菌病
🔹 **藻类控制**：防止池塘中的藻类生长
🔹 **电镀**：物体的铜涂层

**新加坡：**
- 用于游泳池维护
- 滨海湾花园用于植物病害控制

**硫酸钡（BaSO₄）：**

**用途：**
🔹 **X射线对比**：患者在X射线前饮用"钡餐"（对X射线不透明）
🔹 **油漆**：白色颜料

**新加坡医院**（新加坡中央医院、国立大学医院）：用于胃肠道X射线

**碳酸氢钠（NaHCO₃）-小苏打：**

**用途：**
🔹 **烘焙**：产生CO₂气体，使蛋糕膨胀
🔹 **抗酸剂**：中和过量胃酸
🔹 **清洁**：温和研磨剂、除臭剂
🔹 **灭火器**：加热时释放CO₂

**新加坡：**
- 家庭烘焙中常见
- 在职总、冷藏超市出售

**硝酸银（AgNO₃）：**

**用途：**
🔹 **摄影**：感光化合物（传统胶片）
🔹 **氯化物测试**：与Cl⁻离子形成白色沉淀
🔹 **防腐剂**：杀死细菌

**硝酸钠（NaNO₃）：**

**用途：**
🔹 **肥料**：为植物提供氮
🔹 **食品防腐剂**：腌肉（培根、火腿）
🔹 **烟花**：为燃烧提供氧气

**硫酸镁（MgSO₄）-泻盐：**

**用途：**
🔹 **医药**：泻药、缓解肌肉酸痛
🔹 **农业**：为植物提供镁

**硫酸钙（CaSO₄）：**

**用途：**
🔹 **巴黎石膏**：为骨折制作石膏
🔹 **建筑**：墙壁石膏板
🔹 **豆腐制作**：豆浆中的凝固剂

**新加坡：**
- 医院用于骨石膏
- 建筑业使用石膏板
- 豆腐店用于豆腐生产

**环境和健康考虑：**

**优点：**
✅ 许多盐对生命至关重要（钠、钾、钙盐）
✅ 用于医药、农业、工业
✅ 有些是天然和可生物降解的

**担忧：**
⚠️ **过量盐摄入**：高血压、心脏病（WHO建议<5g/天）
⚠️ **肥料径流**：水道的富营养化
⚠️ **重金属盐**：有毒（铅、汞盐）
⚠️ **爆炸性盐**：安全隐患（硝酸铵）

**新加坡健康倡议：**
🔹 **健康餐饮计划**：小贩中心的减盐选择
🔹 **HPB宣传活动**：鼓励减少盐摄入
🔹 **食品标签**：营养信息显示钠含量"""
        }
    ],

    "turning-effects-forces": [
        {
            "id": "moments-principle",
            "title": "Moments and Principle of Moments",
            "title_zh": "力矩与力矩原理",
            "type": "text",
            "content": """**Moment** (or torque) is the turning effect of a force about a pivot (fulcrum).

**Formula:**

**Moment = Force × Perpendicular distance from pivot**

**Units**: Newton-meter (N m)

**Key points:**

🔹 Force must act **perpendicular** to distance
🔹 Distance measured from **pivot** to **line of action of force**
🔹 Larger force or larger distance = larger moment

**Example calculation:**

**Q: A 5 N force acts 2 m from a pivot. Calculate the moment.**

Moment = Force × Distance
Moment = 5 × 2 = 10 N m

**Clockwise vs. Anticlockwise moments:**

- **Clockwise moment**: Force turns object clockwise (⟳)
- **Anticlockwise moment**: Force turns object anticlockwise (⟲)

**Principle of Moments:**

**For an object in equilibrium (balanced):**

**Sum of clockwise moments = Sum of anticlockwise moments**

**Example: Balanced seesaw**

```
        Child A (300 N)         Pivot        Child B (?)
        ←─── 2 m ───→           ↑           ←─ 3 m ─→
```

**For balance:**
Clockwise moment = Anticlockwise moment
300 × 2 = Force_B × 3
600 = Force_B × 3
Force_B = 200 N

**Applications of moments:**

**1. Levers**

**Definition**: Simple machine that uses a pivot to multiply force

**Types of levers:**

**Class 1**: Pivot between effort and load
- Examples: Seesaw, scissors, crowbar, pliers

**Class 2**: Load between effort and pivot
- Examples: Wheelbarrow, nutcracker, bottle opener

**Class 3**: Effort between load and pivot
- Examples: Tweezers, fishing rod, human arm

**Mechanical advantage:**

**MA = Load / Effort**

- MA > 1: Lever multiplies force (effort < load)
- MA < 1: Lever multiplies distance (effort > load)

**2. Doors and door handles**

- Handle placed far from hinge (pivot)
- Larger perpendicular distance = smaller force needed
- Push door near hinge → hard to open
- Push door at handle → easy to open

**3. Wrenches and spanners**

- Long handle increases perpendicular distance
- Reduces force needed to turn nut/bolt
- Plumbers use long pipe wrenches for tight fittings

**4. Wheelbarrows**

- Wheel is pivot
- Load between wheel and handles
- Handles far from pivot = less effort needed to lift

**Singapore examples:**

**Playgrounds:**
🔹 **Seesaws**: At HDB playgrounds, children experience moments
🔹 **Balance**: Heavier child sits closer to pivot, lighter child sits farther

**Construction:**
🔹 **Cranes**: Use moments to lift heavy loads (MRT construction, HDB building)
🔹 **Crowbars**: Workers pry open crates at Jurong Port

**Daily life:**
🔹 **Doors**: Condominium doors, HDB unit doors have handles far from hinges
🔹 **Scissors**: Cutting thick cardboard - use handles far from pivot
🔹 **Bottle openers**: Leverage to remove bottle caps

**Problem-solving strategy:**

**Step 1**: Identify the pivot
**Step 2**: Mark all forces and distances
**Step 3**: Calculate clockwise moments
**Step 4**: Calculate anticlockwise moments
**Step 5**: Apply principle of moments (if balanced)

**Example problem:**

**Q: A uniform beam of weight 50 N and length 4 m rests on a pivot at its center. A 30 N weight is placed 1 m from the left end. Where should a 20 N weight be placed to balance the beam?**

**Solution:**

Pivot is at center (2 m from each end)

**Clockwise moments:**
- Beam weight: 0 N m (acts at pivot, distance = 0)
- 30 N weight: 30 × 1 = 30 N m

**Anticlockwise moments:**
- 20 N weight at distance x from pivot: 20x N m

**For balance:**
20x = 30
x = 1.5 m from pivot (on right side)

**Answer**: 1.5 m to the right of the pivot""",
            "content_zh": """**力矩**（或扭矩）是力绕支点（支点）的旋转效应。

**公式：**

**力矩=力×距支点的垂直距离**

**单位**：牛顿米（N m）

**关键点：**

🔹 力必须**垂直**作用于距离
🔹 距离从**支点**到**力的作用线**测量
🔹 更大的力或更大的距离=更大的力矩

**例子计算：**

**问：一个5 N的力作用在距支点2 m处。计算力矩。**

力矩=力×距离
力矩= 5 × 2 = 10 N m

**顺时针vs逆时针力矩：**

- **顺时针力矩**：力使物体顺时针旋转（⟳）
- **逆时针力矩**：力使物体逆时针旋转（⟲）

**力矩原理：**

**对于处于平衡状态的物体（平衡）：**

**顺时针力矩之和=逆时针力矩之和**

**例子：平衡跷跷板**

```
        儿童A（300 N）        支点        儿童B（？）
        ←─── 2 m ───→          ↑          ←─ 3 m ─→
```

**为了平衡：**
顺时针力矩=逆时针力矩
300 × 2 =力_B × 3
600 =力_B × 3
力_B = 200 N

**力矩的应用：**

**1. 杠杆**

**定义**：使用支点放大力的简单机器

**杠杆类型：**

**第1类**：支点在努力和负荷之间
- 例子：跷跷板、剪刀、撬棍、钳子

**第2类**：负荷在努力和支点之间
- 例子：手推车、坚果夹、开瓶器

**第3类**：努力在负荷和支点之间
- 例子：镊子、钓鱼竿、人类手臂

**机械优势：**

**MA =负荷/努力**

- MA > 1：杠杆放大力（努力<负荷）
- MA < 1：杠杆放大距离（努力>负荷）

**2. 门和门把手**

- 把手放在远离铰链（支点）的地方
- 更大的垂直距离=需要更小的力
- 在铰链附近推门→难以打开
- 在把手处推门→容易打开

**3. 扳手和扳手**

- 长手柄增加垂直距离
- 减少旋转螺母/螺栓所需的力
- 管道工使用长管扳手紧固配件

**4. 手推车**

- 轮子是支点
- 负荷在轮子和手柄之间
- 手柄远离支点=需要更少的努力提升

**新加坡例子：**

**游乐场：**
🔹 **跷跷板**：在组屋游乐场，儿童体验力矩
🔹 **平衡**：较重的孩子坐在靠近支点的地方，较轻的孩子坐在更远的地方

**建筑：**
🔹 **起重机**：使用力矩提升重物（地铁建设、组屋建筑）
🔹 **撬棍**：工人在裕廊港撬开板条箱

**日常生活：**
🔹 **门**：公寓门、组屋单元门的把手远离铰链
🔹 **剪刀**：切割厚纸板-使用远离支点的把手
🔹 **开瓶器**：利用杠杆作用去除瓶盖

**解决问题策略：**

**步骤1**：识别支点
**步骤2**：标记所有力和距离
**步骤3**：计算顺时针力矩
**步骤4**：计算逆时针力矩
**步骤5**：应用力矩原理（如果平衡）

**例子问题：**

**问：重量为50 N、长度为4 m的均匀梁在其中心的支点上休息。30 N的重量放在距左端1 m处。应将20 N的重量放在哪里以平衡梁？**

**解决方案：**

支点在中心（距每端2 m）

**顺时针力矩：**
- 梁重量：0 N m（作用在支点，距离= 0）
- 30 N重量：30 × 1 = 30 N m

**逆时针力矩：**
- 距支点距离x处的20 N重量：20x N m

**为了平衡：**
20x = 30
x = 1.5 m从支点（在右侧）

**答案**：距支点右侧1.5 m"""
        },
        {
            "id": "center-of-gravity",
            "title": "Center of Gravity and Stability",
            "title_zh": "重心与稳定性",
            "type": "text",
            "content": """**Center of gravity (CG)** is the point where the entire weight of an object appears to act.

**Key properties:**

🔹 Every object has a center of gravity
🔹 CG may be inside or outside the object
🔹 For uniform, symmetrical objects, CG is at geometric center
🔹 Weight acts downwards from CG

**Finding center of gravity experimentally:**

**For irregular flat objects (cardboard):**

1. **Suspend** object from one point, let it hang freely
2. **Draw vertical line** downwards from suspension point (use plumb line)
3. **Repeat** from different suspension point
4. **CG is where lines intersect**

**Center of gravity for different shapes:**

**Regular shapes:**
- **Uniform rod**: Middle point
- **Rectangle**: Center (where diagonals meet)
- **Circle**: Center
- **Triangle**: Intersection of medians
- **Ring**: Center (outside the material!)

**Stability:**

**Definition**: Ability of an object to return to its original position after being tilted

**Three states:**

**1. Stable equilibrium**
- Object returns to original position when tilted
- CG rises when tilted
- CG is low, base is wide
- Example: Table, chair

**2. Unstable equilibrium**
- Object topples over when tilted
- CG falls when tilted
- CG is high, base is narrow
- Example: Pencil balanced on point

**3. Neutral equilibrium**
- Object remains in new position when tilted
- CG stays at same height
- Example: Ball on flat surface

**Factors affecting stability:**

**1. Height of center of gravity**
- **Lower CG** = **more stable**
- Racing cars have low CG for stability at high speeds
- Double-decker buses have low CG despite height

**2. Width of base**
- **Wider base** = **more stable**
- Wide stance when standing
- Four-legged tables more stable than three-legged

**3. Line of action of weight**
- Object is stable if **vertical line from CG falls within base**
- Object topples if **vertical line from CG falls outside base**

**Applications for stability:**

**Vehicles:**
🔹 **Racing cars**: Low, wide design for high-speed cornering
🔹 **SUVs**: Higher CG, risk of rollover when cornering fast
🔹 **Buses**: Heavy engine at bottom, passengers on top (lower CG)

**Furniture:**
🔹 **Tables**: Wide base prevents tipping
🔹 **Tall cabinets**: Should be secured to wall (unstable if free-standing)

**Sports:**
🔹 **Wrestling/Judo**: Wrestlers lower CG by bending knees (harder to push over)
🔹 **High jump**: Athletes arch back, CG passes under bar while body goes over

**Singapore applications:**

**MRT trains:**
🔹 **Low floor design**: CG kept low for stability
🔹 **Wide track**: Prevents derailment during turns
🔹 **Passengers should hold on**: Standing raises overall CG

**Buildings:**
🔹 **Tall HDB blocks**: Deep foundations, reinforced concrete (low effective CG)
🔹 **Marina Bay Sands**: Three towers connected at top (distribute weight, lower CG)
🔹 **Singapore Flyer**: Counterweights balance passenger capsules

**Ships:**
🔹 **Container ships** at Singapore Port: Heavy cargo at bottom, lighter on top
🔹 **Cruise ships**: Ballast tanks at bottom for stability
🔹 **Navy ships** (Changi Naval Base): Low CG design for rough seas

**Safety considerations:**

**Preventing toppling:**
⚠️ **Ladders**: Place base farther from wall for stability
⚠️ **Loading trucks**: Heavy items at bottom, distribute weight evenly
⚠️ **Stacking boxes**: Wide base at bottom, narrower on top

**Daily life:**
🔹 **Carrying bags**: Two bags (one each side) more balanced than one
🔹 **Backpacks**: Wear both straps for balanced CG
🔹 **Standing on bus/MRT**: Spread feet wide, lower CG slightly (bend knees)

**Exam tip:**

When analyzing stability problems:
1. Identify position of CG
2. Draw vertical line downwards from CG
3. Check if line falls within or outside base
4. Within base = stable; outside base = topples""",
            "content_zh": """**重心（CG）**是物体整个重量似乎作用的点。

**关键属性：**

🔹 每个物体都有一个重心
🔹 CG可能在物体内部或外部
🔹 对于均匀、对称的物体，CG在几何中心
🔹 重量从CG向下作用

**实验寻找重心：**

**对于不规则平面物体（纸板）：**

1. 从一点**悬挂**物体，让它自由悬挂
2. 从悬挂点向下**画垂直线**（使用铅锤线）
3. 从不同的悬挂点**重复**
4. **CG是线相交的地方**

**不同形状的重心：**

**规则形状：**
- **均匀杆**：中点
- **矩形**：中心（对角线相交处）
- **圆**：中心
- **三角形**：中线的交点
- **环**：中心（在材料外！）

**稳定性：**

**定义**：物体在倾斜后返回其原始位置的能力

**三种状态：**

**1. 稳定平衡**
- 物体在倾斜时返回原始位置
- CG在倾斜时上升
- CG低，底座宽
- 例子：桌子、椅子

**2. 不稳定平衡**
- 物体在倾斜时倾倒
- CG在倾斜时下降
- CG高，底座窄
- 例子：在点上平衡的铅笔

**3. 中性平衡**
- 物体在倾斜时保持在新位置
- CG保持在相同高度
- 例子：平面上的球

**影响稳定性的因素：**

**1. 重心高度**
- **较低的CG** = **更稳定**
- 赛车在高速时有低CG以保持稳定
- 双层巴士尽管很高，但有低CG

**2. 底座宽度**
- **更宽的底座** = **更稳定**
- 站立时宽的姿态
- 四条腿的桌子比三条腿的更稳定

**3. 重量的作用线**
- 如果**从CG的垂直线落在底座内**，物体是稳定的
- 如果**从CG的垂直线落在底座外**，物体倾倒

**稳定性应用：**

**车辆：**
🔹 **赛车**：低矮、宽阔的设计用于高速转弯
🔹 **SUV**：较高的CG，快速转弯时有翻车风险
🔹 **巴士**：引擎在底部，乘客在顶部（较低的CG）

**家具：**
🔹 **桌子**：宽底座防止倾倒
🔹 **高柜**：应固定在墙上（如果独立则不稳定）

**运动：**
🔹 **摔跤/柔道**：摔跤手通过弯曲膝盖降低CG（更难推倒）
🔹 **跳高**：运动员拱背，CG通过杆下而身体越过

**新加坡应用：**

**地铁列车：**
🔹 **低地板设计**：CG保持低以保持稳定
🔹 **宽轨**：防止转弯时脱轨
🔹 **乘客应抓紧**：站立会提高整体CG

**建筑物：**
🔹 **高层组屋**：深基础、钢筋混凝土（有效低CG）
🔹 **滨海湾金沙**：三座塔楼在顶部连接（分配重量、降低CG）
🔹 **新加坡摩天轮**：配重平衡乘客舱

**船舶：**
🔹 **集装箱船**在新加坡港：重货在底部，较轻的在顶部
🔹 **游轮**：底部压载舱以保持稳定
🔹 **海军舰艇**（樟宜海军基地）：低CG设计适用于波涛汹涌的海洋

**安全考虑：**

**防止倾倒：**
⚠️ **梯子**：将底座放在离墙更远的地方以保持稳定
⚠️ **装载卡车**：重物在底部，均匀分配重量
⚠️ **堆放箱子**：底部宽底座，顶部较窄

**日常生活：**
🔹 **携带袋子**：两个袋子（每边一个）比一个更平衡
🔹 **背包**：佩戴两条肩带以平衡CG
🔹 **站在巴士/地铁上**：脚分开，稍微降低CG（弯曲膝盖）

**考试技巧：**

分析稳定性问题时：
1. 识别CG的位置
2. 从CG向下画垂直线
3. 检查线是否落在底座内或外
4. 底座内=稳定；底座外=倾倒"""
        },
        {
            "id": "couples-torque",
            "title": "Couples and Practical Applications",
            "title_zh": "力偶与实际应用",
            "type": "text",
            "content": """**A couple** is a pair of equal and opposite parallel forces acting on an object, but not along the same line.

**Characteristics of a couple:**

🔹 Two forces of **equal magnitude**
🔹 Acting in **opposite directions**
🔹 Forces are **parallel**
🔹 Forces act **along different lines** (not same line of action)

**Effect of a couple:**

- Produces **pure rotation** (turning effect only)
- **No resultant force** (forces cancel out)
- Object does not translate (move linearly)
- Only rotates about center

**Moment of a couple:**

**Formula:**

**Moment = One force × Perpendicular distance between forces**

**Units**: Newton-meter (N m)

**Example:**

Two 5 N forces act 0.4 m apart in opposite directions

Moment of couple = 5 × 0.4 = 2 N m

**Examples of couples:**

**1. Turning a steering wheel**
- Two hands push in opposite directions
- Creates rotational effect
- No net force (car doesn't move up/down)

**2. Turning a tap/faucet**
- Fingers apply forces on opposite sides
- Tap rotates, no linear movement

**3. Winding a clock**
- Fingers turn key with opposing forces
- Key rotates in place

**4. Opening a bottle cap**
- Thumb and fingers apply opposite forces
- Cap rotates and unscrews

**5. Screwdriver**
- Handle turned by opposing forces
- Screw rotates into wood/wall

**6. Pedaling a bicycle**
- Feet push pedals in opposite directions (alternating)
- Crank rotates, chain drives wheel

**Singapore applications:**

**Vehicles:**

**Car steering wheel:**
🔹 **Design**: Larger diameter wheel = larger perpendicular distance
🔹 **Effect**: Less force needed to turn (easier steering)
🔹 **Power steering**: Hydraulic/electric assistance reduces required force

**Bicycle cranks:**
🔹 **Longer pedal arms**: Increase perpendicular distance
🔹 **Mountain bikes**: Longer cranks for better torque climbing hills
🔹 **Park Connector bikes**: Standard crank length for casual cycling

**Construction tools:**

**Wrench/Spanner:**
🔹 **Long handle**: Increases perpendicular distance
🔹 **Ratchet wrench**: One-way rotation for tight spaces
🔹 **Used in**: Car workshops (Ubi, Sin Ming), plumbing, construction

**Combination of moments and couples:**

**Problem: Opening a jar lid**

**Method 1**: Apply single force far from center
- Large perpendicular distance
- But hand might slip

**Method 2**: Apply couple (two opposite forces)
- More stable grip
- Pure rotation
- Lid unscrews smoothly

**Problem-solving with couples:**

**Q: A steering wheel of diameter 40 cm requires a couple of 12 N m to turn. What force must each hand exert?**

**Solution:**

Perpendicular distance = diameter = 40 cm = 0.4 m

Moment of couple = Force × Distance
12 = Force × 0.4
Force = 12 / 0.4 = 30 N

**Answer**: Each hand exerts 30 N

**Comparing single force vs. couple:**

**Single force (moment):**
✅ Simpler to apply
❌ May cause translation as well as rotation
❌ Less stable control

**Couple:**
✅ Pure rotation only
✅ More stable and controlled
✅ Better for precision tasks
❌ Requires two forces

**Daily applications in Singapore:**

**Household:**
🔹 **Taps**: Turn on/off water (HDB flats, condominiums)
🔹 **Door knobs**: Round knobs use couple to open doors
🔹 **Gas stove knobs**: Turn to adjust flame

**Cooking:**
🔹 **Opening jar lids**: Kaya jars, sauce bottles
🔹 **Pepper mill**: Grind pepper with rotating motion
🔹 **Egg beater**: Hand-crank models use couple

**Transportation:**
🔹 **MRT turnstiles**: Rotating barriers use couple mechanism
🔹 **Bicycle repairs**: Using wrenches at bike shops (East Coast, Pulau Ubin)

**Machines:**
🔹 **Valve handles** (water mains): PUB workers turn large valves
🔹 **Industrial machinery**: Jurong Island factories use torque wrenches

**Summary comparison:**

| Concept | Pivot needed? | Forces | Effect |
|---------|---------------|--------|--------|
| **Moment** | Yes | Single force | Rotation + possible translation |
| **Couple** | No | Two equal opposite forces | Pure rotation only |
| **Principle of Moments** | Yes | Multiple forces | Balanced (no rotation) |

**Exam tips:**

When solving couple problems:
1. Check forces are equal and opposite
2. Measure perpendicular distance between force lines
3. Moment = one force × perpendicular distance
4. Direction doesn't matter (couple always rotates same way)""",
            "content_zh": """**力偶**是作用在物体上的一对相等且相反的平行力，但不沿同一条线。

**力偶的特征：**

🔹 两个**大小相等**的力
🔹 作用在**相反方向**
🔹 力是**平行的**
🔹 力沿**不同的线**作用（不是同一条作用线）

**力偶的效果：**

- 产生**纯旋转**（仅旋转效应）
- **没有合力**（力相互抵消）
- 物体不平移（线性移动）
- 只绕中心旋转

**力偶的力矩：**

**公式：**

**力矩=一个力×力之间的垂直距离**

**单位**：牛顿米（N m）

**例子：**

两个5 N的力在相反方向上相距0.4 m

力偶力矩= 5 × 0.4 = 2 N m

**力偶的例子：**

**1. 转动方向盘**
- 两只手向相反方向推
- 产生旋转效应
- 没有净力（汽车不上下移动）

**2. 转动水龙头**
- 手指在相对侧施加力
- 水龙头旋转，无线性运动

**3. 上发条钟**
- 手指用相反的力转动钥匙
- 钥匙在原地旋转

**4. 打开瓶盖**
- 拇指和手指施加相反的力
- 盖子旋转并拧开

**5. 螺丝刀**
- 通过相反的力转动手柄
- 螺丝旋转进入木材/墙壁

**6. 踩自行车踏板**
- 脚向相反方向推踏板（交替）
- 曲柄旋转，链条驱动轮子

**新加坡应用：**

**车辆：**

**汽车方向盘：**
🔹 **设计**：更大直径的轮子=更大的垂直距离
🔹 **效果**：需要更少的力来转动（更容易转向）
🔹 **动力转向**：液压/电动辅助减少所需力

**自行车曲柄：**
🔹 **更长的踏板臂**：增加垂直距离
🔹 **山地车**：更长的曲柄以获得更好的扭矩爬坡
🔹 **公园连道自行车**：标准曲柄长度用于休闲骑行

**建筑工具：**

**扳手/扳手：**
🔹 **长手柄**：增加垂直距离
🔹 **棘轮扳手**：用于狭窄空间的单向旋转
🔹 **用于**：汽车车间（乌美、新民）、管道、建筑

**力矩和力偶的组合：**

**问题：打开罐盖**

**方法1**：在远离中心的地方施加单一力
- 大的垂直距离
- 但手可能滑

**方法2**：施加力偶（两个相反的力）
- 更稳定的抓握
- 纯旋转
- 盖子平稳拧开

**用力偶解决问题：**

**问：直径40 cm的方向盘需要12 N m的力偶来转动。每只手必须施加多少力？**

**解决方案：**

垂直距离=直径= 40 cm = 0.4 m

力偶力矩=力×距离
12 =力× 0.4
力= 12 / 0.4 = 30 N

**答案**：每只手施加30 N

**比较单一力vs力偶：**

**单一力（力矩）：**
✅ 更简单施加
❌ 可能导致平移和旋转
❌ 稳定性较差

**力偶：**
✅ 仅纯旋转
✅ 更稳定和可控
✅ 更适合精密任务
❌ 需要两个力

**新加坡的日常应用：**

**家庭：**
🔹 **水龙头**：打开/关闭水（组屋、公寓）
🔹 **门把手**：圆形把手使用力偶打开门
🔹 **煤气炉旋钮**：转动以调节火焰

**烹饪：**
🔹 **打开罐盖**：咖椰罐、酱汁瓶
🔹 **胡椒磨**：用旋转运动研磨胡椒
🔹 **打蛋器**：手摇模型使用力偶

**交通：**
🔹 **地铁旋转门**：旋转栅栏使用力偶机制
🔹 **自行车修理**：在自行车店使用扳手（东海岸、乌敏岛）

**机器：**
🔹 **阀门手柄**（主水管）：PUB工人转动大阀门
🔹 **工业机械**：裕廊岛工厂使用扭矩扳手

**摘要比较：**

| 概念 | 需要支点？ | 力 | 效果 |
|------|-----------|-----|------|
| **力矩** | 是 | 单一力 | 旋转+可能的平移 |
| **力偶** | 否 | 两个相等相反的力 | 仅纯旋转 |
| **力矩原理** | 是 | 多个力 | 平衡（无旋转） |

**考试技巧：**

解决力偶问题时：
1. 检查力是否相等且相反
2. 测量力线之间的垂直距离
3. 力矩=一个力×垂直距离
4. 方向无关紧要（力偶总是以相同方式旋转）"""
        }
    ]
}

def main():
    content_file = "src/data/content.json"
    backup_file = f"src/data/content-backup-absolute-final-{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    print("="*70)
    print("ABSOLUTE FINAL SEC 3 SCIENCE LESSONS")
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
    print("🎉 ALL SEC 3 SCIENCE LESSONS COMPLETE!")
    print("="*70)
    print(f"Chapters updated in this batch: {chapters_updated}")
    print(f"Sections added in this batch: {sections_added}")
    print(f"\nBackup saved: {backup_file}")
    print("\n✅ All 11 Sec 3 Science chapters now have comprehensive lesson content!")

if __name__ == '__main__':
    main()
