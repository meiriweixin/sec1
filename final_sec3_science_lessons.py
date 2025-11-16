#!/usr/bin/env python3
"""
Final 5 Sec 3 Science chapters: Pressure in Fluids, Quantitative Chemistry,
Reproduction & Cell Division, Salts & Neutralization, Turning Effects of Forces
"""

import json
from datetime import datetime

# Lesson content for final 5 chapters
LESSON_CONTENT = {
    "pressure-fluids": [
        {
            "id": "pressure-liquids",
            "title": "Pressure in Liquids",
            "title_zh": "液体中的压强",
            "type": "text",
            "content": """**Pressure** is the force acting per unit area.

**Formula:** Pressure = Force / Area
**Units:** Pascal (Pa) or N/m²

**Pressure in liquids:**

Liquids exert pressure in all directions because:
🔹 Liquid particles are free to move
🔹 Weight of liquid above creates pressure
🔹 Pressure acts perpendicular to surfaces

**Key principles:**

**1. Pressure increases with depth**
- Deeper you go, more liquid above you
- Formula: P = ρgh
  - P = pressure (Pa)
  - ρ (rho) = density of liquid (kg/m³)
  - g = gravitational field strength (10 N/kg)
  - h = depth below surface (m)

**2. Pressure is the same at the same depth**
- All points at same depth have equal pressure
- Doesn't matter the shape of container

**3. Pressure acts in all directions**
- Liquid pressure pushes on all sides equally

**Calculating liquid pressure:**

**Example: Swimming pool**
- Depth: 2 m
- Density of water: 1000 kg/m³
- g = 10 N/kg

P = ρgh = 1000 × 10 × 2 = 20,000 Pa = 20 kPa

**Singapore examples:**

**Reservoirs:**
🔹 **Marina Barrage**: Water pressure at dam base is high due to depth
🔹 **Swimming pools**: Deeper end has higher water pressure
🔹 **HDB water tanks**: Placed on rooftop to create pressure for taps below

**Diving:**
🔹 **Sentosa Underwater World**: Divers feel pressure increase with depth
🔹 **Scuba diving**: Every 10 m depth adds ~100 kPa pressure
🔹 **Submarines**: Built strong to withstand deep ocean pressure

**Water supply:**
🔹 **PUB water towers**: Height creates pressure for water distribution
🔹 **Gravity-fed system**: Water flows from reservoirs to homes
🔹 **HDB flats**: Lower floors have higher water pressure than top floors""",
            "content_zh": """**压强**是作用在单位面积上的力。

**公式：** 压强 = 力 / 面积
**单位：** 帕斯卡（Pa）或N/m²

**液体中的压强：**

液体向各个方向施加压强，因为：
🔹 液体颗粒可以自由移动
🔹 液体上方的重量产生压强
🔹 压强垂直作用于表面

**关键原理：**

**1. 压强随深度增加**
- 越深，上方的液体越多
- 公式：P = ρgh
  - P = 压强（Pa）
  - ρ（rho）= 液体密度（kg/m³）
  - g = 重力场强度（10 N/kg）
  - h = 表面以下深度（m）

**2. 同一深度的压强相同**
- 同一深度的所有点压强相等
- 容器形状无关

**3. 压强向各个方向作用**
- 液体压强向所有方向均等推动

**计算液体压强：**

**例子：游泳池**
- 深度：2 m
- 水的密度：1000 kg/m³
- g = 10 N/kg

P = ρgh = 1000 × 10 × 2 = 20,000 Pa = 20 kPa

**新加坡例子：**

**蓄水池：**
🔹 **滨海堤坝**：大坝底部的水压很高，因为深度
🔹 **游泳池**：深水端的水压更高
🔹 **组屋水箱**：放在屋顶以为下方水龙头产生压力

**潜水：**
🔹 **圣淘沙海底世界**：潜水员感觉压力随深度增加
🔹 **水肺潜水**：每10米深度增加约100 kPa压力
🔹 **潜艇**：建造坚固以承受深海压力

**供水：**
🔹 **PUB水塔**：高度为供水创造压力
🔹 **重力供水系统**：水从蓄水池流向家庭
🔹 **组屋**：低楼层的水压比顶楼高"""
        },
        {
            "id": "atmospheric-pressure",
            "title": "Atmospheric Pressure",
            "title_zh": "大气压强",
            "type": "text",
            "content": """**Atmospheric pressure** is the pressure exerted by the weight of air in the atmosphere.

**What causes atmospheric pressure?**

🔹 Air has mass (mixture of gases)
🔹 Gravity pulls air molecules down
🔹 Weight of air above creates pressure
🔹 Air extends ~100 km above Earth's surface

**Atmospheric pressure at sea level:**
- **1 atmosphere (atm)** = 101,325 Pa = 101.3 kPa
- Equivalent to weight of 10 m column of water
- Or 760 mm column of mercury

**Factors affecting atmospheric pressure:**

**1. Altitude (height above sea level)**
- Higher altitude → less air above → lower pressure
- Pressure decreases by ~12 Pa per meter climb

**2. Weather conditions**
- High pressure: Clear, sunny weather
- Low pressure: Cloudy, rainy weather

**Measuring atmospheric pressure:**

**Barometer** - Instrument to measure air pressure

**Mercury barometer:**
- Glass tube filled with mercury, inverted in dish
- Atmospheric pressure pushes mercury up tube
- Height of mercury column = atmospheric pressure
- Standard: 760 mm Hg at sea level

**Aneroid barometer:**
- Metal box with partial vacuum inside
- Atmospheric pressure compresses/expands box
- Dial shows pressure reading
- Used in weather stations, altimeters

**Effects of atmospheric pressure:**

**Drinking through a straw:**
1. Suck air out of straw
2. Pressure inside straw decreases
3. Atmospheric pressure on drink surface pushes liquid up straw

**Suction cups:**
1. Press cup on smooth surface
2. Air pushed out from under cup
3. Atmospheric pressure on outside holds cup in place

**Vacuum packaging:**
1. Remove air from bag
2. Atmospheric pressure compresses bag tightly around food
3. Prevents spoilage, extends shelf life

**Singapore applications:**

**Weather forecasting:**
🔹 **Meteorological Service Singapore**: Monitors atmospheric pressure
🔹 **High pressure**: Expect sunny weather (typical in Singapore)
🔹 **Low pressure**: Expect rain or thunderstorms

**Aviation:**
🔹 **Changi Airport**: Aircraft altimeters use pressure to determine altitude
🔹 **Cabin pressure**: Planes pressurized to ~0.8 atm for passenger comfort

**Vacuum-sealed products:**
🔹 **Coffee**: Vacuum-packed to preserve freshness (supermarkets)
🔹 **Electronics**: Moisture-sensitive components stored in vacuum bags

**Building design:**
🔹 **Wind pressure**: Atmospheric pressure differences create wind forces on tall buildings (Marina Bay Sands)
🔹 **Ventilation**: Pressure differences drive air circulation in HDB flats""",
            "content_zh": """**大气压强**是大气中空气重量施加的压强。

**是什么导致大气压强？**

🔹 空气有质量（气体混合物）
🔹 重力将空气分子向下拉
🔹 上方空气的重量产生压强
🔹 空气延伸到地球表面以上约100公里

**海平面的大气压强：**
- **1个大气压（atm）** = 101,325 Pa = 101.3 kPa
- 相当于10米水柱的重量
- 或760毫米汞柱

**影响大气压强的因素：**

**1. 海拔（海平面以上高度）**
- 海拔越高→上方空气越少→压力越低
- 每爬升一米压力下降约12 Pa

**2. 天气条件**
- 高压：晴朗、阳光明媚的天气
- 低压：多云、下雨的天气

**测量大气压强：**

**气压计** - 测量气压的仪器

**水银气压计：**
- 充满水银的玻璃管，倒置在盘子里
- 大气压强将水银推上管子
- 水银柱的高度=大气压强
- 标准：海平面760毫米汞柱

**无液气压计：**
- 内部部分真空的金属盒
- 大气压强压缩/扩张盒子
- 刻度盘显示压力读数
- 用于气象站、高度计

**大气压强的影响：**

**用吸管喝水：**
1. 吸出吸管中的空气
2. 吸管内压力降低
3. 饮料表面的大气压强将液体推上吸管

**吸盘：**
1. 将杯子压在光滑表面上
2. 杯子下方的空气被推出
3. 外部的大气压强将杯子固定在原位

**真空包装：**
1. 从袋子中去除空气
2. 大气压强将袋子紧紧压缩在食物周围
3. 防止变质，延长保质期

**新加坡应用：**

**天气预报：**
🔹 **新加坡气象局**：监测大气压强
🔹 **高压**：预计晴天（新加坡典型）
🔹 **低压**：预计下雨或雷暴

**航空：**
🔹 **樟宜机场**：飞机高度计使用压力确定高度
🔹 **机舱压力**：飞机加压到约0.8 atm以提高乘客舒适度

**真空密封产品：**
🔹 **咖啡**：真空包装以保持新鲜（超市）
🔹 **电子产品**：对湿度敏感的组件存储在真空袋中

**建筑设计：**
🔹 **风压**：大气压差在高层建筑上产生风力（滨海湾金沙）
🔹 **通风**：压差驱动组屋的空气循环"""
        },
        {
            "id": "applications-pressure",
            "title": "Applications of Pressure in Fluids",
            "title_zh": "流体压强的应用",
            "type": "text",
            "content": """**Hydraulic systems** use liquid pressure to transmit force and do work.

**Pascal's Principle:**
- Pressure applied to enclosed fluid is transmitted equally in all directions
- Used in hydraulic systems to multiply force

**Hydraulic jack/lift:**

**How it works:**
1. **Small piston** (area A₁) pushed with small force F₁
2. **Pressure created**: P = F₁/A₁
3. **Same pressure** transmitted to large piston (area A₂)
4. **Large force produced**: F₂ = P × A₂

**Force multiplication:**
- If A₂ = 10 × A₁, then F₂ = 10 × F₁
- Small effort force lifts heavy load

**Applications:**

**Car brake system:**
1. Driver pushes brake pedal (small force)
2. Pressure transmitted through brake fluid
3. Brake pads pressed against wheels (large force)
4. Car slows down

**Hydraulic car lift** (workshop):
- Mechanic applies small force on pump
- Lifts entire car for repairs

**Hydraulic excavator:**
- Controls arm movements
- Digs with great force

**Pneumatic systems** use compressed air instead of liquid:

**Pneumatic drill:**
- Compressed air drives piston rapidly
- Used for breaking concrete, road repairs

**Automatic doors:**
- Compressed air opens/closes doors
- Used in MRT stations, shopping malls

**Singapore applications:**

**MRT system:**
🔹 **Hydraulic doors**: Train doors use hydraulic/pneumatic systems
🔹 **Brake systems**: Hydraulic brakes stop trains safely
🔹 **Platform screen doors**: Pneumatic systems open/close automatically

**Construction:**
🔹 **Pile drivers**: Hydraulic systems drive foundation piles for HDB buildings
🔹 **Cranes**: Hydraulic lifts for construction at building sites
🔹 **Concrete pumps**: Hydraulic pressure pumps concrete to high floors

**Automotive:**
🔹 **Car workshops**: Hydraulic lifts at Ubi, Sin Ming car repair shops
🔹 **Brake systems**: All vehicles in Singapore use hydraulic brakes
🔹 **Power steering**: Hydraulic assistance for easier steering

**Advantages of hydraulic systems:**
✅ Multiply force easily
✅ Smooth, precise control
✅ Can transmit force over distance (through pipes)
✅ Reliable and durable

**Disadvantages:**
⚠️ Leaks can reduce pressure
⚠️ Fluid needs replacement/maintenance
⚠️ Heavy and expensive
⚠️ Fire risk if hydraulic fluid is flammable

**Buoyancy and floating:**

**Archimedes' Principle:**
- Object in fluid experiences upward force (buoyant force)
- Buoyant force = weight of fluid displaced

**Floating:**
- If buoyant force ≥ weight of object, it floats
- Ships float because they displace large volume of water

**Singapore maritime:**
🔹 **Port of Singapore**: Container ships float despite heavy cargo
🔹 **Ferries**: Sentosa ferry, Pulau Ubin bumboat use buoyancy
🔹 **Navy ships**: RSS ships at Changi Naval Base designed to float efficiently""",
            "content_zh": """**液压系统**使用液体压力传递力并做功。

**帕斯卡原理：**
- 施加在封闭流体上的压力在各个方向上均等传递
- 用于液压系统以放大力

**液压千斤顶/升降机：**

**它是如何工作的：**
1. **小活塞**（面积A₁）用小力F₁推动
2. **产生的压力**：P = F₁/A₁
3. **相同压力**传递到大活塞（面积A₂）
4. **产生大力**：F₂ = P × A₂

**力的放大：**
- 如果A₂ = 10 × A₁，则F₂ = 10 × F₁
- 小的努力力举起重物

**应用：**

**汽车制动系统：**
1. 司机踩刹车踏板（小力）
2. 压力通过制动液传递
3. 刹车片压在车轮上（大力）
4. 汽车减速

**液压汽车升降机**（车间）：
- 机械师在泵上施加小力
- 举起整辆车进行修理

**液压挖掘机：**
- 控制手臂运动
- 用巨大的力挖掘

**气动系统**使用压缩空气而不是液体：

**气动钻：**
- 压缩空气快速驱动活塞
- 用于破碎混凝土、道路维修

**自动门：**
- 压缩空气打开/关闭门
- 用于地铁站、购物中心

**新加坡应用：**

**地铁系统：**
🔹 **液压门**：列车门使用液压/气动系统
🔹 **制动系统**：液压制动安全停止列车
🔹 **站台屏蔽门**：气动系统自动打开/关闭

**建筑：**
🔹 **打桩机**：液压系统为组屋打地基桩
🔹 **起重机**：建筑工地的液压升降机
🔹 **混凝土泵**：液压泵将混凝土泵送到高层

**汽车：**
🔹 **汽车车间**：乌美、新民汽车修理店的液压升降机
🔹 **制动系统**：新加坡所有车辆都使用液压制动
🔹 **动力转向**：液压辅助更轻松转向

**液压系统的优点：**
✅ 容易放大力
✅ 平稳、精确控制
✅ 可以远距离传递力（通过管道）
✅ 可靠耐用

**缺点：**
⚠️ 泄漏会降低压力
⚠️ 流体需要更换/维护
⚠️ 重且昂贵
⚠️ 如果液压油易燃，则有火灾风险

**浮力和漂浮：**

**阿基米德原理：**
- 流体中的物体受到向上的力（浮力）
- 浮力=排开流体的重量

**漂浮：**
- 如果浮力≥物体重量，它就漂浮
- 船漂浮是因为它们排开大量的水

**新加坡海事：**
🔹 **新加坡港**：集装箱船尽管装载重物仍然漂浮
🔹 **渡轮**：圣淘沙渡轮、乌敏岛舢板使用浮力
🔹 **海军舰艇**：樟宜海军基地的RSS舰艇设计为有效漂浮"""
        }
    ],

    "quantitative-chemistry": [
        {
            "id": "relative-atomic-mass",
            "title": "Relative Atomic Mass and Mole Concept",
            "title_zh": "相对原子质量与摩尔概念",
            "type": "text",
            "content": """**Quantitative chemistry** deals with calculating amounts of substances in chemical reactions.

**Relative Atomic Mass (Ar):**

- **Definition**: Mass of one atom compared to 1/12 the mass of one carbon-12 atom
- **No units** (it's a ratio)
- Found on Periodic Table

**Examples:**
- Hydrogen (H): Ar = 1
- Carbon (C): Ar = 12
- Oxygen (O): Ar = 16
- Sodium (Na): Ar = 23
- Chlorine (Cl): Ar = 35.5

**Relative Molecular Mass (Mr) / Relative Formula Mass:**

- **Definition**: Sum of relative atomic masses of all atoms in a molecule
- **No units**

**Calculating Mr:**

**Example 1: Water (H₂O)**
- Mr = (2 × 1) + (1 × 16) = 2 + 16 = 18

**Example 2: Carbon dioxide (CO₂)**
- Mr = (1 × 12) + (2 × 16) = 12 + 32 = 44

**Example 3: Sodium chloride (NaCl)**
- Formula mass = (1 × 23) + (1 × 35.5) = 58.5

**The Mole (mol):**

- **Definition**: Amount of substance containing 6.02 × 10²³ particles (Avogadro's number)
- **1 mole** of any substance contains **6.02 × 10²³** atoms, molecules, or ions

**Why use moles?**
🔹 Atoms are too small and numerous to count individually
🔹 Mole allows us to count particles by weighing
🔹 Links mass to number of particles

**Molar mass:**
- **Definition**: Mass of one mole of a substance
- **Units**: g/mol
- **Numerically equal to Ar or Mr**

**Examples:**
- 1 mole of carbon (C) = 12 g
- 1 mole of water (H₂O) = 18 g
- 1 mole of sodium chloride (NaCl) = 58.5 g

**Formula:**

**Number of moles = Mass (g) / Molar mass (g/mol)**

**Example calculations:**

**Q: How many moles in 36 g of water (H₂O)?**

1. Find molar mass of H₂O: Mr = 18 g/mol
2. Apply formula: moles = 36 / 18 = 2 mol

**Q: What is the mass of 0.5 mol of sodium chloride (NaCl)?**

1. Molar mass of NaCl = 58.5 g/mol
2. Rearrange formula: mass = moles × molar mass
3. mass = 0.5 × 58.5 = 29.25 g

**Singapore context:**

**Chemistry practical:**
🔹 Sec 3 students weigh chemicals in moles for experiments
🔹 Calculate amounts needed for reactions
🔹 Used in titration experiments at school labs

**Industrial applications:**
🔹 **Chemical plants** (Jurong Island): Calculate reactant amounts in tonnes
🔹 **Pharmaceutical companies**: Precise mole calculations for medicine production
🔹 **Water treatment** (PUB): Calculate chemical dosages for purification""",
            "content_zh": """**定量化学**涉及计算化学反应中物质的量。

**相对原子质量（Ar）：**

- **定义**：一个原子的质量与一个碳-12原子质量的1/12的比较
- **无单位**（它是一个比率）
- 在周期表上找到

**例子：**
- 氢（H）：Ar = 1
- 碳（C）：Ar = 12
- 氧（O）：Ar = 16
- 钠（Na）：Ar = 23
- 氯（Cl）：Ar = 35.5

**相对分子质量（Mr）/相对式量：**

- **定义**：分子中所有原子的相对原子质量之和
- **无单位**

**计算Mr：**

**例子1：水（H₂O）**
- Mr = (2 × 1) + (1 × 16) = 2 + 16 = 18

**例子2：二氧化碳（CO₂）**
- Mr = (1 × 12) + (2 × 16) = 12 + 32 = 44

**例子3：氯化钠（NaCl）**
- 式量 = (1 × 23) + (1 × 35.5) = 58.5

**摩尔（mol）：**

- **定义**：包含6.02 × 10²³个粒子的物质量（阿伏伽德罗数）
- **1摩尔**任何物质包含**6.02 × 10²³**个原子、分子或离子

**为什么使用摩尔？**
🔹 原子太小且数量太多，无法单独计数
🔹 摩尔允许我们通过称重来计数粒子
🔹 将质量与粒子数联系起来

**摩尔质量：**
- **定义**：一摩尔物质的质量
- **单位**：g/mol
- **数值上等于Ar或Mr**

**例子：**
- 1摩尔碳（C）= 12 g
- 1摩尔水（H₂O）= 18 g
- 1摩尔氯化钠（NaCl）= 58.5 g

**公式：**

**摩尔数 = 质量（g）/ 摩尔质量（g/mol）**

**例子计算：**

**问：36 g水（H₂O）有多少摩尔？**

1. 找H₂O的摩尔质量：Mr = 18 g/mol
2. 应用公式：摩尔 = 36 / 18 = 2 mol

**问：0.5 mol氯化钠（NaCl）的质量是多少？**

1. NaCl的摩尔质量 = 58.5 g/mol
2. 重新排列公式：质量 = 摩尔 × 摩尔质量
3. 质量 = 0.5 × 58.5 = 29.25 g

**新加坡背景：**

**化学实践：**
🔹 中三学生为实验称量以摩尔为单位的化学品
🔹 计算反应所需的量
🔹 用于学校实验室的滴定实验

**工业应用：**
🔹 **化工厂**（裕廊岛）：计算以吨为单位的反应物量
🔹 **制药公司**：药物生产的精确摩尔计算
🔹 **水处理**（PUB）：计算净化的化学剂量"""
        },
        {
            "id": "chemical-equations-calculations",
            "title": "Chemical Equations and Stoichiometry",
            "title_zh": "化学方程式与化学计量学",
            "type": "text",
            "content": """**Stoichiometry** is the study of quantitative relationships in chemical reactions.

**Balanced chemical equations** show:
1. **Reactants** → **Products**
2. **Ratio of moles** of substances involved
3. **Law of conservation of mass**: Atoms are not created or destroyed

**Example: Formation of water**

2H₂ + O₂ → 2H₂O

**Interpretation:**
- **Molecules**: 2 molecules H₂ + 1 molecule O₂ → 2 molecules H₂O
- **Moles**: 2 mol H₂ + 1 mol O₂ → 2 mol H₂O
- **Mole ratio**: H₂ : O₂ : H₂O = 2 : 1 : 2

**Steps for stoichiometry calculations:**

**Step 1**: Write balanced equation
**Step 2**: Find mole ratio from equation
**Step 3**: Calculate moles of known substance
**Step 4**: Use mole ratio to find moles of unknown substance
**Step 5**: Convert moles to mass (if needed)

**Example calculation:**

**Q: What mass of oxygen is needed to react completely with 4 g of hydrogen to form water?**

**Step 1**: Balanced equation: 2H₂ + O₂ → 2H₂O

**Step 2**: Mole ratio: H₂ : O₂ = 2 : 1

**Step 3**: Moles of H₂ = mass / molar mass = 4 / 2 = 2 mol

**Step 4**: Moles of O₂ = 2 mol H₂ × (1 mol O₂ / 2 mol H₂) = 1 mol

**Step 5**: Mass of O₂ = moles × molar mass = 1 × 32 = 32 g

**Answer**: 32 g of oxygen needed

**Limiting reactant:**

- **Definition**: Reactant that is completely used up first
- Determines maximum amount of product formed
- Other reactants are in excess

**Example:**

**Q: 6 g of hydrogen reacts with 32 g of oxygen. Which is the limiting reactant? What mass of water is formed?**

**Equation**: 2H₂ + O₂ → 2H₂O

**Moles of H₂**: 6 / 2 = 3 mol
**Moles of O₂**: 32 / 32 = 1 mol

**From equation**: 2 mol H₂ needs 1 mol O₂
**For 3 mol H₂**: needs 1.5 mol O₂

**We only have 1 mol O₂**, so **O₂ is the limiting reactant**

**Maximum H₂O formed**: 1 mol O₂ produces 2 mol H₂O
**Mass of H₂O**: 2 × 18 = 36 g

**Percentage yield:**

**Theoretical yield**: Maximum amount of product calculated from equation
**Actual yield**: Amount of product actually obtained in experiment

**Formula:**

**% yield = (Actual yield / Theoretical yield) × 100%**

**Why is actual yield < theoretical yield?**
⚠️ Incomplete reactions
⚠️ Side reactions producing unwanted products
⚠️ Loss of product during transfer/purification
⚠️ Impure reactants

**Singapore applications:**

**Industrial chemistry (Jurong Island):**
🔹 **Fertilizer production**: Calculate reactant amounts for ammonia synthesis
🔹 **Petrochemicals**: Optimize yields to maximize profit
🔹 **Cost efficiency**: Minimize waste, reduce reactant costs

**Environmental:**
🔹 **NEWater production**: Calculate chemical dosages for water treatment
🔹 **Pollution control**: Calculate amounts of neutralizing agents for waste treatment

**Medicine:**
🔹 **Drug synthesis**: Precise stoichiometry ensures correct drug composition
🔹 **Quality control**: Calculate expected vs. actual yields""",
            "content_zh": """**化学计量学**是研究化学反应中定量关系的学科。

**平衡化学方程式**显示：
1. **反应物** → **产物**
2. 涉及物质的**摩尔比**
3. **质量守恒定律**：原子不被创造或破坏

**例子：水的形成**

2H₂ + O₂ → 2H₂O

**解释：**
- **分子**：2个H₂分子 + 1个O₂分子 → 2个H₂O分子
- **摩尔**：2 mol H₂ + 1 mol O₂ → 2 mol H₂O
- **摩尔比**：H₂：O₂：H₂O = 2：1：2

**化学计量学计算步骤：**

**步骤1**：写平衡方程式
**步骤2**：从方程式找摩尔比
**步骤3**：计算已知物质的摩尔数
**步骤4**：使用摩尔比找未知物质的摩尔数
**步骤5**：将摩尔转换为质量（如果需要）

**例子计算：**

**问：需要多少氧气才能与4 g氢气完全反应形成水？**

**步骤1**：平衡方程式：2H₂ + O₂ → 2H₂O

**步骤2**：摩尔比：H₂：O₂ = 2：1

**步骤3**：H₂的摩尔数 = 质量 / 摩尔质量 = 4 / 2 = 2 mol

**步骤4**：O₂的摩尔数 = 2 mol H₂ ×（1 mol O₂ / 2 mol H₂）= 1 mol

**步骤5**：O₂的质量 = 摩尔 × 摩尔质量 = 1 × 32 = 32 g

**答案**：需要32 g氧气

**限制性反应物：**

- **定义**：首先完全用完的反应物
- 决定形成的最大产物量
- 其他反应物是过量的

**例子：**

**问：6 g氢气与32 g氧气反应。哪个是限制性反应物？形成多少水？**

**方程式**：2H₂ + O₂ → 2H₂O

**H₂的摩尔数**：6 / 2 = 3 mol
**O₂的摩尔数**：32 / 32 = 1 mol

**从方程式**：2 mol H₂需要1 mol O₂
**对于3 mol H₂**：需要1.5 mol O₂

**我们只有1 mol O₂**，所以**O₂是限制性反应物**

**最大H₂O形成**：1 mol O₂产生2 mol H₂O
**H₂O的质量**：2 × 18 = 36 g

**百分比产率：**

**理论产率**：从方程式计算的最大产物量
**实际产率**：实验中实际获得的产物量

**公式：**

**%产率 =（实际产率/理论产率）× 100%**

**为什么实际产率<理论产率？**
⚠️ 反应不完全
⚠️ 副反应产生不需要的产物
⚠️ 在转移/纯化过程中损失产物
⚠️ 不纯的反应物

**新加坡应用：**

**工业化学（裕廊岛）：**
🔹 **肥料生产**：计算氨合成的反应物量
🔹 **石化产品**：优化产率以最大化利润
🔹 **成本效益**：最小化废物，降低反应物成本

**环境：**
🔹 **新生水生产**：计算水处理的化学剂量
🔹 **污染控制**：计算废物处理的中和剂量

**医药：**
🔹 **药物合成**：精确的化学计量学确保正确的药物组成
🔹 **质量控制**：计算预期与实际产率"""
        },
        {
            "id": "concentration-solutions",
            "title": "Concentration and Solution Calculations",
            "title_zh": "浓度与溶液计算",
            "type": "text",
            "content": """**Concentration** measures the amount of solute dissolved in a solution.

**Types of concentration:**

**1. Mass concentration (g/dm³)**
- **Definition**: Mass of solute per unit volume of solution
- **Units**: g/dm³ or g/L
- **Formula**: Concentration = Mass of solute (g) / Volume of solution (dm³)

**Example:**
- 20 g of salt dissolved in 2 dm³ of water
- Concentration = 20 / 2 = 10 g/dm³

**2. Molar concentration / Molarity (mol/dm³ or M)**
- **Definition**: Number of moles of solute per unit volume of solution
- **Units**: mol/dm³ or M (molar)
- **Formula**: Concentration = Moles of solute / Volume of solution (dm³)

**Example:**
- 0.5 mol of sodium chloride in 2 dm³ of solution
- Concentration = 0.5 / 2 = 0.25 mol/dm³ or 0.25 M

**Key conversions:**
- 1 dm³ = 1 L = 1000 cm³ = 1000 mL
- To convert cm³ to dm³: divide by 1000

**Calculation triangle for solutions:**

```
        Mass (g)
       /        \\
      /          \\
Moles (mol)  ←→  Concentration (mol/dm³) × Volume (dm³)
```

**Formula:**

**Moles = Concentration (mol/dm³) × Volume (dm³)**
**Mass = Moles × Molar mass**
**Concentration = Moles / Volume**

**Example problems:**

**Q1: What is the concentration of a solution containing 0.2 mol of NaCl in 500 cm³?**

**Step 1**: Convert volume to dm³: 500 cm³ = 500/1000 = 0.5 dm³
**Step 2**: Calculate concentration: C = moles / volume = 0.2 / 0.5 = 0.4 mol/dm³

**Answer**: 0.4 mol/dm³

**Q2: How many moles of HCl are in 250 cm³ of 2 mol/dm³ HCl?**

**Step 1**: Convert volume: 250 cm³ = 0.25 dm³
**Step 2**: Calculate moles: moles = C × V = 2 × 0.25 = 0.5 mol

**Answer**: 0.5 mol

**Q3: What mass of copper sulfate (CuSO₄) is needed to make 500 cm³ of 0.1 mol/dm³ solution?**

**Step 1**: Find molar mass of CuSO₄: Mr = 64 + 32 + (4×16) = 160 g/mol
**Step 2**: Convert volume: 500 cm³ = 0.5 dm³
**Step 3**: Calculate moles: moles = C × V = 0.1 × 0.5 = 0.05 mol
**Step 4**: Calculate mass: mass = moles × molar mass = 0.05 × 160 = 8 g

**Answer**: 8 g

**Dilution:**

- **Definition**: Adding solvent (usually water) to decrease concentration
- **Key principle**: Moles of solute remain constant

**Formula:**

**C₁V₁ = C₂V₂**

where:
- C₁ = initial concentration
- V₁ = initial volume
- C₂ = final concentration
- V₂ = final volume

**Example:**

**Q: 100 cm³ of 2 mol/dm³ NaOH is diluted to 500 cm³. What is the new concentration?**

C₁V₁ = C₂V₂
(2)(100) = (C₂)(500)
C₂ = 200 / 500 = 0.4 mol/dm³

**Answer**: 0.4 mol/dm³

**Singapore applications:**

**Chemistry practicals:**
🔹 **Titration experiments**: Prepare standard solutions of acids/bases
🔹 **Concentration calculations**: Determine unknown concentrations
🔹 **Dilution**: Make working solutions from stock solutions

**Industry:**
🔹 **Water treatment (PUB)**: Calculate chlorine concentration in tap water
🔹 **Food industry**: Concentration of preservatives, flavorings
🔹 **Pharmaceutical**: Precise drug concentrations in medicines

**Daily life:**
🔹 **Cleaning products**: Dilute concentrated bleach for home use
🔹 **Drinks**: Concentrated juice diluted with water (Ribena, Yakult)
🔹 **Pool maintenance**: Chlorine concentration in swimming pools""",
            "content_zh": """**浓度**测量溶液中溶解的溶质量。

**浓度类型：**

**1. 质量浓度（g/dm³）**
- **定义**：单位体积溶液中溶质的质量
- **单位**：g/dm³或g/L
- **公式**：浓度=溶质质量（g）/溶液体积（dm³）

**例子：**
- 20 g盐溶解在2 dm³水中
- 浓度= 20 / 2 = 10 g/dm³

**2. 摩尔浓度/摩尔浓度（mol/dm³或M）**
- **定义**：单位体积溶液中溶质的摩尔数
- **单位**：mol/dm³或M（摩尔）
- **公式**：浓度=溶质摩尔数/溶液体积（dm³）

**例子：**
- 0.5 mol氯化钠在2 dm³溶液中
- 浓度= 0.5 / 2 = 0.25 mol/dm³或0.25 M

**关键转换：**
- 1 dm³ = 1 L = 1000 cm³ = 1000 mL
- 将cm³转换为dm³：除以1000

**溶液计算三角：**

```
        质量（g）
       /        \\
      /          \\
摩尔（mol） ←→ 浓度（mol/dm³）×体积（dm³）
```

**公式：**

**摩尔=浓度（mol/dm³）×体积（dm³）**
**质量=摩尔×摩尔质量**
**浓度=摩尔/体积**

**例子问题：**

**问1：含有0.2 mol NaCl的500 cm³溶液的浓度是多少？**

**步骤1**：将体积转换为dm³：500 cm³ = 500/1000 = 0.5 dm³
**步骤2**：计算浓度：C=摩尔/体积= 0.2 / 0.5 = 0.4 mol/dm³

**答案**：0.4 mol/dm³

**问2：250 cm³ 2 mol/dm³ HCl中有多少摩尔HCl？**

**步骤1**：转换体积：250 cm³ = 0.25 dm³
**步骤2**：计算摩尔：摩尔= C × V = 2 × 0.25 = 0.5 mol

**答案**：0.5 mol

**问3：制造500 cm³ 0.1 mol/dm³硫酸铜（CuSO₄）溶液需要多少硫酸铜？**

**步骤1**：找CuSO₄的摩尔质量：Mr = 64 + 32 +（4×16）= 160 g/mol
**步骤2**：转换体积：500 cm³ = 0.5 dm³
**步骤3**：计算摩尔：摩尔= C × V = 0.1 × 0.5 = 0.05 mol
**步骤4**：计算质量：质量=摩尔×摩尔质量= 0.05 × 160 = 8 g

**答案**：8 g

**稀释：**

- **定义**：添加溶剂（通常是水）以降低浓度
- **关键原理**：溶质的摩尔数保持不变

**公式：**

**C₁V₁ = C₂V₂**

其中：
- C₁=初始浓度
- V₁=初始体积
- C₂=最终浓度
- V₂=最终体积

**例子：**

**问：100 cm³ 2 mol/dm³ NaOH稀释至500 cm³。新浓度是多少？**

C₁V₁ = C₂V₂
(2)(100) = (C₂)(500)
C₂ = 200 / 500 = 0.4 mol/dm³

**答案**：0.4 mol/dm³

**新加坡应用：**

**化学实践：**
🔹 **滴定实验**：制备酸/碱的标准溶液
🔹 **浓度计算**：确定未知浓度
🔹 **稀释**：从储备溶液制备工作溶液

**工业：**
🔹 **水处理（PUB）**：计算自来水中的氯浓度
🔹 **食品工业**：防腐剂、调味料的浓度
🔹 **制药**：药物中的精确药物浓度

**日常生活：**
🔹 **清洁产品**：稀释浓缩漂白剂供家庭使用
🔹 **饮料**：浓缩果汁用水稀释（利宾纳、养乐多）
🔹 **泳池维护**：游泳池中的氯浓度"""
        }
    ]
}

# Continue with final 2 chapters in the final execution...

def main():
    content_file = "src/data/content.json"
    backup_file = f"src/data/content-backup-final-sec3-{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    print("="*70)
    print("ADDING FINAL SEC 3 SCIENCE LESSONS (Part 1 of 2)")
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
    print("✅ PART 1 COMPLETE")
    print("="*70)
    print(f"Chapters updated: {chapters_updated}")
    print(f"Sections added: {sections_added}")
    print(f"\nBackup saved: {backup_file}")
    print("\n2 more chapters remaining (Reproduction & Cell Division, Salts & Neutralization, Turning Effects of Forces)")

if __name__ == '__main__':
    main()
