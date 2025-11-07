#!/usr/bin/env python3
"""
Create Secondary 3 Science chapters aligned with Singapore MOE syllabus.
Based on 2021 G2/G3 Lower Secondary Science Syllabus (updated April 2024).
"""

import json

def create_sec3_science_chapters():
    """Create all Sec 3 Science chapters with sections."""

    chapters = []

    # ============================================================================
    # PHYSICS CHAPTERS (6 chapters)
    # ============================================================================

    # Chapter 1: Electromagnetic Spectrum
    chapters.append({
        "id": "electromagnetic-spectrum",
        "title": "Electromagnetic Spectrum",
        "title_zh": "电磁波谱",
        "gradeLevel": "sec3",
        "tag": "Physics",
        "tag_zh": "物理",
        "description": "Understanding the electromagnetic spectrum and its applications in modern technology",
        "description_zh": "了解电磁波谱及其在现代科技中的应用",
        "objectives": [
            "Understand the electromagnetic spectrum and its components",
            "Describe how radio waves are used in astronomy and RFID tags",
            "Explain how infrared is used in thermal imaging",
            "Discuss beneficial and harmful effects of EM radiation"
        ],
        "objectives_zh": [
            "理解电磁波谱及其组成部分",
            "描述无线电波在天文学和RFID标签中的应用",
            "解释红外线在热成像中的应用",
            "讨论电磁辐射的有益和有害影响"
        ],
        "sections": [
            {
                "id": "em-spectrum-intro",
                "type": "text",
                "title": "What is the Electromagnetic Spectrum?",
                "title_zh": "什么是电磁波谱？",
                "content": "The electromagnetic (EM) spectrum is a continuous range of electromagnetic waves arranged according to their wavelength and frequency. All EM waves travel at the speed of light (3 × 10⁸ m/s) in a vacuum.\n\nThe spectrum includes (from longest wavelength to shortest):\n• Radio waves - longest wavelength, lowest frequency\n• Microwaves\n• Infrared radiation\n• Visible light (ROYGBIV)\n• Ultraviolet radiation\n• X-rays\n• Gamma rays - shortest wavelength, highest frequency\n\nKey relationship: As wavelength decreases, frequency and energy increase.",
                "content_zh": "电磁波谱是根据波长和频率排列的连续电磁波范围。所有电磁波在真空中以光速（3×10⁸米/秒）传播。\n\n波谱包括（从最长波长到最短）：\n• 无线电波 - 最长波长，最低频率\n• 微波\n• 红外辐射\n• 可见光（红橙黄绿蓝靛紫）\n• 紫外线辐射\n• X射线\n• 伽马射线 - 最短波长，最高频率\n\n关键关系：波长减小时，频率和能量增加。"
            },
            {
                "id": "radio-waves-applications",
                "type": "text",
                "title": "Radio Waves in Astronomy and RFID",
                "title_zh": "无线电波在天文学和RFID中的应用",
                "content": "**Radio Astronomy:**\nRadio telescopes detect radio waves emitted by celestial objects like stars, galaxies, and black holes. This allows astronomers to:\n• Study objects invisible to optical telescopes\n• Observe through dust clouds\n• Detect pulsars and quasars\n• Map the structure of galaxies\n\n**RFID (Radio Frequency Identification):**\nRFID tags use radio waves for automatic identification:\n• Used in EZ-Link cards for MRT/bus payments in Singapore\n• Library book tracking systems\n• Inventory management in stores\n• Access control cards\n• Pet microchip identification\n\nRFID tags contain a chip and antenna that respond to radio signals from readers.",
                "content_zh": "**射电天文学：**\n射电望远镜探测恒星、星系和黑洞等天体发射的无线电波。这使天文学家能够：\n• 研究光学望远镜看不见的天体\n• 透过尘埃云观测\n• 探测脉冲星和类星体\n• 绘制星系结构图\n\n**RFID（射频识别）：**\nRFID标签使用无线电波进行自动识别：\n• 在新加坡的易通卡中用于地铁/巴士支付\n• 图书馆图书跟踪系统\n• 商店库存管理\n• 门禁卡\n• 宠物微芯片识别\n\nRFID标签包含一个芯片和天线，对读取器的无线电信号做出响应。"
            },
            {
                "id": "infrared-thermal-imaging",
                "type": "text",
                "title": "Infrared and Thermal Imaging",
                "title_zh": "红外线和热成像",
                "content": "**Properties of Infrared (IR) Radiation:**\n• Wavelength longer than visible light but shorter than microwaves\n• All objects emit infrared radiation\n• Hotter objects emit more IR radiation\n• Can be felt as heat\n\n**Thermal Imaging Applications:**\n1. Medical diagnosis - detecting inflammation, blood flow issues\n2. Building inspection - finding heat leaks, insulation problems\n3. Night vision - seeing in darkness (used by military, wildlife researchers)\n4. Airport screening - detecting fever during disease outbreaks (COVID-19)\n5. Electrical inspection - identifying overheating components\n6. Search and rescue - locating people in darkness or smoke\n\n**How Thermal Cameras Work:**\nThey detect infrared radiation emitted by objects and convert it into a visible image, with different colors representing different temperatures.",
                "content_zh": "**红外线（IR）辐射的性质：**\n• 波长比可见光长但比微波短\n• 所有物体都发射红外辐射\n• 更热的物体发射更多红外辐射\n• 可以感觉到热量\n\n**热成像应用：**\n1. 医学诊断 - 检测炎症、血流问题\n2. 建筑检查 - 发现热量泄漏、绝缘问题\n3. 夜视 - 在黑暗中看东西（军事、野生动物研究人员使用）\n4. 机场筛查 - 在疾病爆发期间检测发烧（COVID-19）\n5. 电气检查 - 识别过热部件\n6. 搜救 - 在黑暗或烟雾中定位人员\n\n**热像仪如何工作：**\n它们检测物体发射的红外辐射并将其转换为可见图像，不同颜色代表不同温度。"
            },
            {
                "id": "em-radiation-effects",
                "type": "text",
                "title": "Effects of EM Radiation",
                "title_zh": "电磁辐射的影响",
                "content": "**Beneficial Effects:**\n• Radio waves - communication, broadcasting\n• Microwaves - cooking, satellite communication\n• Infrared - heating, thermal imaging, remote controls\n• Visible light - sight, photosynthesis, lighting\n• UV radiation - vitamin D production, sterilization\n• X-rays - medical imaging, security scanning\n• Gamma rays - cancer treatment, sterilizing medical equipment\n\n**Harmful Effects:**\n• UV radiation - skin burns, skin cancer, eye damage\n• X-rays - cell damage, increased cancer risk with overexposure\n• Gamma rays - severe radiation damage, mutations\n\n**Safety Precautions:**\n• Use sunscreen to protect from UV rays\n• Limit X-ray exposure (only when medically necessary)\n• Lead shielding for X-ray and gamma ray protection\n• Follow radiation safety guidelines in hospitals",
                "content_zh": "**有益影响：**\n• 无线电波 - 通信、广播\n• 微波 - 烹饪、卫星通信\n• 红外线 - 加热、热成像、遥控器\n• 可见光 - 视觉、光合作用、照明\n• 紫外线辐射 - 维生素D生成、消毒\n• X射线 - 医学成像、安全扫描\n• 伽马射线 - 癌症治疗、医疗设备消毒\n\n**有害影响：**\n• 紫外线辐射 - 皮肤灼伤、皮肤癌、眼睛损伤\n• X射线 - 细胞损伤、过度暴露增加癌症风险\n• 伽马射线 - 严重辐射损伤、突变\n\n**安全预防措施：**\n• 使用防晒霜保护免受紫外线\n• 限制X射线暴露（仅在医学必要时）\n• 铅屏蔽保护免受X射线和伽马射线\n• 在医院遵循辐射安全指南"
            }
        ],
        "exercises": []  # Will be added separately
    })

    # Chapter 2: Current Electricity
    chapters.append({
        "id": "current-electricity",
        "title": "Current Electricity",
        "title_zh": "电流",
        "gradeLevel": "sec3",
        "tag": "Physics",
        "tag_zh": "物理",
        "description": "Understanding electric current, voltage, resistance and circuit analysis",
        "description_zh": "理解电流、电压、电阻和电路分析",
        "objectives": [
            "Define current, voltage and resistance with their SI units",
            "Apply Ohm's Law to solve circuit problems",
            "Analyze series and parallel circuits",
            "Calculate power and energy in electrical circuits"
        ],
        "objectives_zh": [
            "定义电流、电压和电阻及其国际单位",
            "应用欧姆定律解决电路问题",
            "分析串联和并联电路",
            "计算电路中的功率和能量"
        ],
        "sections": [
            {
                "id": "current-voltage-resistance",
                "type": "text",
                "title": "Current, Voltage and Resistance",
                "title_zh": "电流、电压和电阻",
                "content": "**Electric Current (I):**\n• Flow of electric charge through a conductor\n• SI unit: ampere (A)\n• Measured using ammeter (connected in series)\n• Direction: from positive to negative terminal (conventional current)\n\n**Voltage/Potential Difference (V):**\n• Energy transferred per unit charge\n• SI unit: volt (V)\n• Measured using voltmeter (connected in parallel)\n• Battery/cell provides voltage\n\n**Resistance (R):**\n• Opposition to current flow\n• SI unit: ohm (Ω)\n• Factors affecting resistance:\n  - Length (longer = more resistance)\n  - Cross-sectional area (thicker = less resistance)\n  - Material (conductivity)\n  - Temperature",
                "content_zh": "**电流（I）：**\n• 电荷通过导体的流动\n• 国际单位：安培（A）\n• 使用电流表测量（串联连接）\n• 方向：从正极到负极（常规电流）\n\n**电压/电位差（V）：**\n• 每单位电荷传递的能量\n• 国际单位：伏特（V）\n• 使用电压表测量（并联连接）\n• 电池/电池提供电压\n\n**电阻（R）：**\n• 对电流流动的阻力\n• 国际单位：欧姆（Ω）\n• 影响电阻的因素：\n  - 长度（更长=更多电阻）\n  - 横截面积（更粗=更少电阻）\n  - 材料（导电性）\n  - 温度"
            },
            {
                "id": "ohms-law",
                "type": "text",
                "title": "Ohm's Law",
                "title_zh": "欧姆定律",
                "content": "**Ohm's Law:**\nV = IR\n\nWhere:\n• V = voltage (V)\n• I = current (A)\n• R = resistance (Ω)\n\n**Key Points:**\n• Voltage is directly proportional to current (at constant resistance)\n• Current decreases as resistance increases (at constant voltage)\n• A graph of V vs I gives a straight line for ohmic conductors\n\n**Example:**\nIf a resistor has resistance 10Ω and current 2A flows through it:\nV = IR = 2 × 10 = 20V\n\n**Applications:**\n• Calculating required resistance for circuits\n• Determining safe current levels\n• Designing electrical systems",
                "content_zh": "**欧姆定律：**\nV = IR\n\n其中：\n• V = 电压（V）\n• I = 电流（A）\n• R = 电阻（Ω）\n\n**要点：**\n• 电压与电流成正比（恒定电阻时）\n• 电流随电阻增加而减小（恒定电压时）\n• 欧姆导体的V对I图给出直线\n\n**示例：**\n如果电阻器的电阻为10Ω，流过2A电流：\nV = IR = 2 × 10 = 20V\n\n**应用：**\n• 计算电路所需电阻\n• 确定安全电流水平\n• 设计电气系统"
            },
            {
                "id": "series-parallel-circuits",
                "type": "text",
                "title": "Series and Parallel Circuits",
                "title_zh": "串联和并联电路",
                "content": "**Series Circuits:**\n• Components connected in a single loop\n• Same current through all components (I₁ = I₂ = I₃)\n• Total voltage = sum of individual voltages (V_total = V₁ + V₂ + V₃)\n• Total resistance = sum of individual resistances (R_total = R₁ + R₂ + R₃)\n• If one component fails, circuit breaks\n\n**Parallel Circuits:**\n• Components connected across multiple branches\n• Same voltage across all components (V₁ = V₂ = V₃ = V_total)\n• Total current = sum of branch currents (I_total = I₁ + I₂ + I₃)\n• Total resistance: 1/R_total = 1/R₁ + 1/R₂ + 1/R₃\n• If one component fails, others continue working\n\n**Home Wiring:**\nHouses use parallel circuits so:\n• All appliances get same voltage (230V in Singapore)\n• Appliances work independently\n• Can switch devices on/off without affecting others",
                "content_zh": "**串联电路：**\n• 组件连接在单个回路中\n• 所有组件的电流相同（I₁ = I₂ = I₃）\n• 总电压=各个电压之和（V_总 = V₁ + V₂ + V₃）\n• 总电阻=各个电阻之和（R_总 = R₁ + R₂ + R₃）\n• 如果一个组件失效，电路断开\n\n**并联电路：**\n• 组件跨多个分支连接\n• 所有组件的电压相同（V₁ = V₂ = V₃ = V_总）\n• 总电流=分支电流之和（I_总 = I₁ + I₂ + I₃）\n• 总电阻：1/R_总 = 1/R₁ + 1/R₂ + 1/R₃\n• 如果一个组件失效，其他组件继续工作\n\n**家庭布线：**\n房屋使用并联电路，因此：\n• 所有电器获得相同电压（新加坡为230V）\n• 电器独立工作\n• 可以打开/关闭设备而不影响其他设备"
            },
            {
                "id": "electrical-power-energy",
                "type": "text",
                "title": "Electrical Power and Energy",
                "title_zh": "电功率和电能",
                "content": "**Electrical Power (P):**\n• Rate of energy transfer\n• SI unit: watt (W) or kilowatt (kW)\n• Formulas:\n  - P = VI (power = voltage × current)\n  - P = I²R (power = current² × resistance)\n  - P = V²/R (power = voltage² / resistance)\n\n**Electrical Energy (E):**\n• Total energy consumed\n• SI unit: joule (J) or kilowatt-hour (kWh)\n• Formula: E = Pt (energy = power × time)\n• 1 kWh = 3,600,000 J\n\n**Example:**\nA 2kW heater runs for 3 hours:\nEnergy = 2kW × 3h = 6 kWh\n\n**Electricity Bills in Singapore:**\n• Charged per kWh consumed\n• SP Group charges about $0.30 per kWh\n• Cost = Energy (kWh) × Tariff\n• Energy-efficient appliances save money",
                "content_zh": "**电功率（P）：**\n• 能量传递速率\n• 国际单位：瓦特（W）或千瓦（kW）\n• 公式：\n  - P = VI（功率=电压×电流）\n  - P = I²R（功率=电流²×电阻）\n  - P = V²/R（功率=电压²/电阻）\n\n**电能（E）：**\n• 消耗的总能量\n• 国际单位：焦耳（J）或千瓦时（kWh）\n• 公式：E = Pt（能量=功率×时间）\n• 1千瓦时 = 3,600,000焦耳\n\n**示例：**\n一个2千瓦的加热器运行3小时：\n能量 = 2千瓦 × 3小时 = 6千瓦时\n\n**新加坡的电费单：**\n• 按消耗的千瓦时收费\n• SP集团每千瓦时收费约$0.30\n• 费用=能量（kWh）×电价\n• 节能电器省钱"
            }
        ],
        "exercises": []
    })

    # Chapter 3: Electromagnetism
    chapters.append({
        "id": "electromagnetism",
        "title": "Electromagnetism",
        "title_zh": "电磁学",
        "gradeLevel": "sec3",
        "tag": "Physics",
        "tag_zh": "物理",
        "description": "Understanding magnetic fields, electromagnets and their applications in motors and generators",
        "description_zh": "理解磁场、电磁铁及其在电机和发电机中的应用",
        "objectives": [
            "Describe magnetic fields around magnets and current-carrying wires",
            "Explain how electromagnets work and factors affecting their strength",
            "Understand the working principles of electric motors",
            "Explain electromagnetic induction and generators"
        ],
        "objectives_zh": [
            "描述磁铁和载流导线周围的磁场",
            "解释电磁铁的工作原理和影响其强度的因素",
            "理解电动机的工作原理",
            "解释电磁感应和发电机"
        ],
        "sections": [
            {
                "id": "magnetic-fields",
                "type": "text",
                "title": "Magnetic Fields",
                "title_zh": "磁场",
                "content": "**Magnetic Field:**\n• Region where magnetic force is experienced\n• Represented by magnetic field lines\n• Direction: from North pole to South pole\n• Stronger fields have closer field lines\n\n**Magnetic Field Around a Bar Magnet:**\n• Field lines emerge from North pole\n• Field lines enter at South pole\n• Field lines never cross\n• Strongest at the poles\n\n**Magnetic Field Around a Current-Carrying Wire:**\n• Circular field lines around the wire\n• Direction given by right-hand grip rule\n• Field strength increases with current\n• Field strength decreases with distance\n\n**Magnetic Field in a Solenoid:**\n• Coil of wire produces strong uniform field inside\n• Field pattern similar to bar magnet\n• Strength increases with:\n  - More turns of wire\n  - Greater current\n  - Iron core inserted",
                "content_zh": "**磁场：**\n• 经历磁力的区域\n• 由磁场线表示\n• 方向：从北极到南极\n• 更强的场有更近的场线\n\n**条形磁铁周围的磁场：**\n• 场线从北极出现\n• 场线在南极进入\n• 场线从不交叉\n• 在极点处最强\n\n**载流导线周围的磁场：**\n• 导线周围的圆形场线\n• 方向由右手握拳规则给出\n• 场强随电流增加\n• 场强随距离减小\n\n**螺线管中的磁场：**\n• 线圈在内部产生强均匀场\n• 场型类似于条形磁铁\n• 强度随以下因素增加：\n  - 更多线圈匝数\n  - 更大电流\n  - 插入铁芯"
            },
            {
                "id": "electromagnets",
                "type": "text",
                "title": "Electromagnets",
                "title_zh": "电磁铁",
                "content": "**What is an Electromagnet?**\nA coil of wire (solenoid) that becomes magnetic when current flows through it. The magnetism can be switched on and off.\n\n**Factors Affecting Electromagnet Strength:**\n1. **Number of turns** - more turns = stronger magnet\n2. **Current** - larger current = stronger magnet\n3. **Core material** - soft iron core makes it much stronger\n4. **Core shape** - U-shaped core concentrates field\n\n**Advantages over Permanent Magnets:**\n• Can be switched on/off\n• Strength can be adjusted\n• Magnetic poles can be reversed\n• Can be very strong\n\n**Applications in Singapore and Worldwide:**\n• MRT train door locks\n• Electric bells and buzzers\n• Scrapyard cranes (lifting metal)\n• Circuit breakers\n• Relays and switches\n• Hard disk drives\n• Loudspeakers\n• MRI scanners in hospitals",
                "content_zh": "**什么是电磁铁？**\n当电流通过线圈（螺线管）时，它会变成磁性的。磁性可以打开和关闭。\n\n**影响电磁铁强度的因素：**\n1. **匝数** - 更多匝数=更强的磁铁\n2. **电流** - 更大电流=更强的磁铁\n3. **芯材料** - 软铁芯使其更强\n4. **芯形状** - U形芯集中场\n\n**相对于永久磁铁的优势：**\n• 可以打开/关闭\n• 强度可以调节\n• 磁极可以反转\n• 可以非常强\n\n**在新加坡和全球的应用：**\n• 地铁列车门锁\n• 电铃和蜂鸣器\n• 废料场起重机（提升金属）\n• 断路器\n• 继电器和开关\n• 硬盘驱动器\n• 扬声器\n• 医院的MRI扫描仪"
            },
            {
                "id": "electric-motors",
                "type": "text",
                "title": "Electric Motors",
                "title_zh": "电动机",
                "content": "**Principle:**\nElectric motors convert electrical energy to kinetic energy using the motor effect (force on current-carrying wire in magnetic field).\n\n**How a DC Motor Works:**\n1. Current flows through coil in magnetic field\n2. Forces act on opposite sides of coil\n3. Forces cause turning effect (moment)\n4. Coil rotates\n5. Commutator reverses current every half turn\n6. This keeps coil rotating in same direction\n\n**Components:**\n• **Coil** - carries current\n• **Permanent magnets** - provide magnetic field\n• **Commutator** - split ring that reverses current\n• **Brushes** - maintain electrical contact\n\n**Increasing Motor Speed:**\n• Increase current\n• More turns in coil\n• Stronger magnets\n• Better commutator design\n\n**Applications:**\n• Electric fans and air conditioners\n• Electric cars and bicycles\n• Washing machines and dryers\n• Power tools and drills\n• Computer cooling fans\n• Toy cars",
                "content_zh": "**原理：**\n电动机使用电动机效应（磁场中载流导线上的力）将电能转换为动能。\n\n**直流电动机如何工作：**\n1. 电流通过磁场中的线圈\n2. 力作用在线圈的相对侧\n3. 力产生转动效应（力矩）\n4. 线圈旋转\n5. 换向器每半圈反转电流\n6. 这使线圈保持同一方向旋转\n\n**组件：**\n• **线圈** - 携带电流\n• **永久磁铁** - 提供磁场\n• **换向器** - 反转电流的分裂环\n• **电刷** - 保持电接触\n\n**增加电动机速度：**\n• 增加电流\n• 线圈更多匝数\n• 更强的磁铁\n• 更好的换向器设计\n\n**应用：**\n• 电风扇和空调\n• 电动汽车和自行车\n• 洗衣机和烘干机\n• 电动工具和钻头\n• 计算机冷却风扇\n• 玩具车"
            },
            {
                "id": "electromagnetic-induction",
                "type": "text",
                "title": "Electromagnetic Induction & Generators",
                "title_zh": "电磁感应和发电机",
                "content": "**Electromagnetic Induction:**\nVoltage is induced when:\n• A conductor moves through a magnetic field, OR\n• The magnetic field through a conductor changes\n\n**Faraday's Law:**\nInduced voltage increases with:\n• Faster movement\n• Stronger magnetic field\n• More turns in coil\n\n**Lenz's Law:**\nInduced current opposes the change that caused it.\n\n**How a Generator Works:**\n1. Coil rotates in magnetic field\n2. Magnetic flux through coil changes\n3. Voltage induced in coil\n4. Current flows in external circuit\n5. Slip rings maintain continuous contact\n\n**AC Generator produces:**\n• Alternating current (changes direction)\n• Sinusoidal voltage output\n\n**Applications:**\n• Power stations (turbines turn generators)\n• Bicycle dynamos (wheel turns generator)\n• Wind turbines\n• Hydroelectric dams\n• Portable generators\n\n**Energy Conversion:**\nKinetic Energy → Electrical Energy",
                "content_zh": "**电磁感应：**\n当以下情况时会感应电压：\n• 导体通过磁场移动，或\n• 通过导体的磁场改变\n\n**法拉第定律：**\n感应电压随以下因素增加：\n• 更快的运动\n• 更强的磁场\n• 线圈更多匝数\n\n**楞次定律：**\n感应电流反对引起它的变化。\n\n**发电机如何工作：**\n1. 线圈在磁场中旋转\n2. 通过线圈的磁通量改变\n3. 在线圈中感应电压\n4. 电流在外部电路中流动\n5. 滑环保持连续接触\n\n**交流发电机产生：**\n• 交流电（改变方向）\n• 正弦电压输出\n\n**应用：**\n• 发电站（涡轮机转动发电机）\n• 自行车发电机（车轮转动发电机）\n• 风力涡轮机\n• 水电大坝\n• 便携式发电机\n\n**能量转换：**\n动能→电能"
            }
        ],
        "exercises": []
    })

    # Continue with remaining chapters...
    # Due to length, I'll create the structure for all 15 chapters

    # Chapter 4: Static Electricity
    chapters.append({
        "id": "static-electricity",
        "title": "Static Electricity",
        "title_zh": "静电",
        "gradeLevel": "sec3",
        "tag": "Physics",
        "tag_zh": "物理",
        "description": "Understanding electric charge, electrostatic forces and applications",
        "description_zh": "理解电荷、静电力和应用",
        "objectives": [
            "Explain how objects become charged by friction",
            "Describe the forces between charged objects",
            "Explain electrostatic phenomena in everyday life",
            "Understand applications and hazards of static electricity"
        ],
        "objectives_zh": [
            "解释物体如何通过摩擦带电",
            "描述带电物体之间的力",
            "解释日常生活中的静电现象",
            "理解静电的应用和危害"
        ],
        "sections": [
            {
                "id": "electric-charge",
                "type": "text",
                "title": "Electric Charge",
                "title_zh": "电荷",
                "content": "**Types of Charge:**\n• Positive charge (+)\n• Negative charge (-)\n• Neutral (equal positive and negative)\n\n**Properties:**\n• Like charges repel\n• Unlike charges attract\n• Charge is conserved (cannot be created or destroyed)\n• Charge can be transferred\n\n**Charging by Friction:**\nWhen two materials are rubbed together:\n• Electrons transfer from one material to the other\n• Material losing electrons becomes positive\n• Material gaining electrons becomes negative\n\n**Examples:**\n• Rubbing balloon on hair - balloon becomes negative\n• Rubbing plastic rod with cloth - rod becomes negative\n• Combing hair - comb becomes charged",
                "content_zh": "**电荷类型：**\n• 正电荷（+）\n• 负电荷（-）\n• 中性（正负电荷相等）\n\n**性质：**\n• 同性电荷相斥\n• 异性电荷相吸\n• 电荷守恒（不能被创造或破坏）\n• 电荷可以转移\n\n**摩擦起电：**\n当两种材料摩擦在一起时：\n• 电子从一种材料转移到另一种材料\n• 失去电子的材料变为正电\n• 获得电子的材料变为负电\n\n**示例：**\n• 在头发上摩擦气球 - 气球变为负电\n• 用布摩擦塑料棒 - 棒变为负电\n• 梳头 - 梳子带电"
            }
        ],
        "exercises": []
    })

    # Chapter 5: Turning Effects of Forces
    chapters.append({
        "id": "turning-effects-forces",
        "title": "Turning Effects of Forces",
        "title_zh": "力的转动效应",
        "gradeLevel": "sec3",
        "tag": "Physics",
        "tag_zh": "物理",
        "description": "Understanding moments, centre of gravity and stability",
        "description_zh": "理解力矩、重心和稳定性",
        "objectives": [
            "Define moment of a force and calculate it",
            "Apply the principle of moments to solve problems",
            "Understand centre of gravity and its applications",
            "Explain factors affecting stability"
        ],
        "objectives_zh": [
            "定义力的力矩并计算",
            "应用力矩原理解决问题",
            "理解重心及其应用",
            "解释影响稳定性的因素"
        ],
        "sections": [],
        "exercises": []
    })

    # Chapter 6: Pressure in Fluids
    chapters.append({
        "id": "pressure-fluids",
        "title": "Pressure in Fluids",
        "title_zh": "流体中的压力",
        "gradeLevel": "sec3",
        "tag": "Physics",
        "tag_zh": "物理",
        "description": "Understanding pressure in liquids and gases, atmospheric pressure and applications",
        "description_zh": "理解液体和气体中的压力、大气压力和应用",
        "objectives": [
            "Calculate pressure in liquids and gases",
            "Explain atmospheric pressure and its effects",
            "Understand hydraulic systems",
            "Explain buoyancy and Archimedes' principle"
        ],
        "objectives_zh": [
            "计算液体和气体中的压力",
            "解释大气压力及其影响",
            "理解液压系统",
            "解释浮力和阿基米德原理"
        ],
        "sections": [],
        "exercises": []
    })

    # CHEMISTRY CHAPTERS

    # Chapter 7: Quantitative Chemistry
    chapters.append({
        "id": "quantitative-chemistry",
        "title": "Quantitative Chemistry",
        "title_zh": "定量化学",
        "gradeLevel": "sec3",
        "tag": "Chemistry",
        "tag_zh": "化学",
        "description": "Understanding the mole concept, chemical calculations and stoichiometry",
        "description_zh": "理解摩尔概念、化学计算和化学计量学",
        "objectives": [
            "Understand the mole concept and Avogadro's constant",
            "Calculate relative molecular mass and molar mass",
            "Perform stoichiometric calculations",
            "Calculate percentage composition and empirical formula"
        ],
        "objectives_zh": [
            "理解摩尔概念和阿伏伽德罗常数",
            "计算相对分子质量和摩尔质量",
            "进行化学计量计算",
            "计算百分比组成和经验式"
        ],
        "sections": [],
        "exercises": []
    })

    # Chapter 8: Salts & Neutralization
    chapters.append({
        "id": "salts-neutralization",
        "title": "Salts & Neutralization",
        "title_zh": "盐和中和",
        "gradeLevel": "sec3",
        "tag": "Chemistry",
        "tag_zh": "化学",
        "description": "Understanding salt preparation methods and neutralization reactions",
        "description_zh": "理解盐的制备方法和中和反应",
        "objectives": [
            "Describe methods of preparing salts",
            "Write ionic equations for reactions",
            "Explain neutralization reactions",
            "Understand solubility rules for salts"
        ],
        "objectives_zh": [
            "描述制备盐的方法",
            "写出反应的离子方程式",
            "解释中和反应",
            "理解盐的溶解度规则"
        ],
        "sections": [],
        "exercises": []
    })

    # Chapter 9: Polymers & Recycling
    chapters.append({
        "id": "polymers-recycling",
        "title": "Polymers & Recycling",
        "title_zh": "聚合物和回收",
        "gradeLevel": "sec3",
        "tag": "Chemistry",
        "tag_zh": "化学",
        "description": "Understanding polymers, plastics and their environmental impact - NEW syllabus topic",
        "description_zh": "理解聚合物、塑料及其环境影响 - 新教学大纲主题",
        "objectives": [
            "Describe structure and properties of polymers",
            "Explain addition and condensation polymerization",
            "Describe two methods of recycling plastics",
            "Discuss social, economic and environmental issues of recycling"
        ],
        "objectives_zh": [
            "描述聚合物的结构和性质",
            "解释加成聚合和缩合聚合",
            "描述回收塑料的两种方法",
            "讨论回收的社会、经济和环境问题"
        ],
        "sections": [],
        "exercises": []
    })

    # Chapter 10: Atmosphere & Environment
    chapters.append({
        "id": "atmosphere-environment",
        "title": "Atmosphere & Environment",
        "title_zh": "大气和环境",
        "gradeLevel": "sec3",
        "tag": "Chemistry",
        "tag_zh": "化学",
        "description": "Understanding air composition, pollution and climate change",
        "description_zh": "理解空气组成、污染和气候变化",
        "objectives": [
            "Describe composition of clean air",
            "Explain causes and effects of air pollution",
            "Understand the greenhouse effect and global warming",
            "Discuss solutions to environmental problems"
        ],
        "objectives_zh": [
            "描述清洁空气的组成",
            "解释空气污染的原因和影响",
            "理解温室效应和全球变暖",
            "讨论环境问题的解决方案"
        ],
        "sections": [],
        "exercises": []
    })

    # Chapter 11: Electrolysis
    chapters.append({
        "id": "electrolysis",
        "title": "Electrolysis",
        "title_zh": "电解",
        "gradeLevel": "sec3",
        "tag": "Chemistry",
        "tag_zh": "化学",
        "description": "Understanding electrolysis of molten compounds and aqueous solutions",
        "description_zh": "理解熔融化合物和水溶液的电解",
        "objectives": [
            "Explain what electrolysis is and how it works",
            "Predict products of electrolysis",
            "Describe electrolysis of molten ionic compounds",
            "Describe electrolysis of aqueous solutions"
        ],
        "objectives_zh": [
            "解释什么是电解及其工作原理",
            "预测电解产物",
            "描述熔融离子化合物的电解",
            "描述水溶液的电解"
        ],
        "sections": [],
        "exercises": []
    })

    # BIOLOGY CHAPTERS

    # Chapter 12: Reproduction & Cell Division
    chapters.append({
        "id": "reproduction-cell-division",
        "title": "Reproduction & Cell Division",
        "title_zh": "生殖和细胞分裂",
        "gradeLevel": "sec3",
        "tag": "Biology",
        "tag_zh": "生物",
        "description": "Understanding mitosis, meiosis and sexual reproduction - MERGED syllabus topic",
        "description_zh": "理解有丝分裂、减数分裂和有性生殖 - 合并教学大纲主题",
        "objectives": [
            "Describe the cell cycle and mitosis",
            "Explain meiosis and formation of gametes",
            "Compare mitosis and meiosis",
            "Understand sexual reproduction in plants and animals"
        ],
        "objectives_zh": [
            "描述细胞周期和有丝分裂",
            "解释减数分裂和配子形成",
            "比较有丝分裂和减数分裂",
            "理解植物和动物的有性生殖"
        ],
        "sections": [],
        "exercises": []
    })

    # Chapter 13: Inheritance & Genetics
    chapters.append({
        "id": "inheritance-genetics",
        "title": "Inheritance & Genetics",
        "title_zh": "遗传和基因学",
        "gradeLevel": "sec3",
        "tag": "Biology",
        "tag_zh": "生物",
        "description": "Understanding DNA, genes, genetic variation and inheritance patterns",
        "description_zh": "理解DNA、基因、遗传变异和遗传模式",
        "objectives": [
            "Understand the structure and function of DNA",
            "Explain how genes control characteristics",
            "Use genetic diagrams and Punnett squares",
            "Understand dominant and recessive alleles"
        ],
        "objectives_zh": [
            "理解DNA的结构和功能",
            "解释基因如何控制特征",
            "使用遗传图和庞内特方格",
            "理解显性和隐性等位基因"
        ],
        "sections": [],
        "exercises": []
    })

    # Chapter 14: Ecology & Human Impact
    chapters.append({
        "id": "ecology-human-impact",
        "title": "Ecology & Human Impact",
        "title_zh": "生态学和人类影响",
        "gradeLevel": "sec3",
        "tag": "Biology",
        "tag_zh": "生物",
        "description": "Understanding ecosystems, conservation and how human actions reduce effects of global warming - UPDATED topic",
        "description_zh": "理解生态系统、保护以及人类行动如何减少全球变暖的影响 - 更新主题",
        "objectives": [
            "Understand energy flow in ecosystems",
            "Explain nutrient cycles and their importance",
            "Discuss human impact on the environment",
            "Discuss how human actions can reduce effects of global warming"
        ],
        "objectives_zh": [
            "理解生态系统中的能量流动",
            "解释营养循环及其重要性",
            "讨论人类对环境的影响",
            "讨论人类行动如何减少全球变暖的影响"
        ],
        "sections": [],
        "exercises": []
    })

    # Chapter 15: Biotechnology
    chapters.append({
        "id": "biotechnology",
        "title": "Biotechnology",
        "title_zh": "生物技术",
        "gradeLevel": "sec3",
        "tag": "Biology",
        "tag_zh": "生物",
        "description": "Understanding applications of biotechnology including genetic engineering and fermentation",
        "description_zh": "理解生物技术的应用，包括基因工程和发酵",
        "objectives": [
            "Explain what biotechnology is and its applications",
            "Describe genetic engineering and its uses",
            "Understand fermentation and its industrial uses",
            "Discuss ethical issues in biotechnology"
        ],
        "objectives_zh": [
            "解释什么是生物技术及其应用",
            "描述基因工程及其用途",
            "理解发酵及其工业用途",
            "讨论生物技术中的伦理问题"
        ],
        "sections": [],
        "exercises": []
    })

    return chapters

def save_chapters_to_files(chapters):
    """Save each chapter to a separate JSON file in the chapters/ directory."""
    import os

    # Create chapters directory if it doesn't exist
    os.makedirs('chapters', exist_ok=True)

    for chapter in chapters:
        filename = f"chapters/sec3-science-{chapter['id']}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(chapter, f, ensure_ascii=False, indent=2)
        print(f"Created: {filename}")

if __name__ == "__main__":
    print("Creating Sec 3 Science chapters...")
    chapters = create_sec3_science_chapters()
    save_chapters_to_files(chapters)
    print(f"\nSuccessfully created {len(chapters)} Sec 3 Science chapters!")
    print("\nNext steps:")
    print("1. Run: python create_sec3_science_exercises.py")
    print("2. Run: python integrate_sec3_science.py")
