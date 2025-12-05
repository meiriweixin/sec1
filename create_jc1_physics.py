#!/usr/bin/env python3
"""
Creates JC 1 Physics chapters with comprehensive lesson content.
Following the same successful pattern as JC Mathematics.
"""

import json

jc1_physics_chapters = [
    {
        "id": "measurement-jc1-physics",
        "title": "Measurement",
        "title_zh": "测量",
        "gradeLevel": "jc1",
        "description": "Physical quantities, units, errors, and uncertainties",
        "description_zh": "物理量、单位、误差和不确定性",
        "tag": "Physics",
        "tag_zh": "物理",
        "objectives": [
            "Understand base and derived quantities and their SI units",
            "Perform unit conversions and dimensional analysis",
            "Analyze errors, uncertainties, and significant figures in measurements"
        ],
        "objectives_zh": [
            "理解基本量和导出量及其国际单位",
            "进行单位换算和量纲分析",
            "分析测量中的误差、不确定性和有效数字"
        ],
        "sections": [
            {
                "id": "physical-quantities-units",
                "type": "text",
                "title": "Physical Quantities and SI Units",
                "title_zh": "物理量和国际单位",
                "content": """**Physical quantities** are properties that can be measured, such as length, mass, time, and temperature. In physics, we use the **International System of Units (SI)** to ensure consistency worldwide.

**Base Quantities and SI Units:**

1. **Length** - meter (m)
2. **Mass** - kilogram (kg)
3. **Time** - second (s)
4. **Electric current** - ampere (A)
5. **Temperature** - kelvin (K)
6. **Amount of substance** - mole (mol)
7. **Luminous intensity** - candela (cd)

**Derived Quantities:**

Derived quantities are combinations of base quantities:
- **Velocity** = displacement / time → m/s or m s⁻¹
- **Acceleration** = velocity / time → m/s² or m s⁻²
- **Force** = mass × acceleration → kg m s⁻² (newton, N)
- **Energy** = force × distance → kg m² s⁻² (joule, J)
- **Power** = energy / time → kg m² s⁻³ (watt, W)

**Example: Singapore MRT System**

The Downtown Line (DTL) from Bukit Panjang to Expo is approximately **42 km** long. If a train completes this journey in **70 minutes**, we can calculate:

- Distance: $s = 42 \\text{ km} = 42,000 \\text{ m}$
- Time: $t = 70 \\text{ min} = 4,200 \\text{ s}$
- Average velocity: $v = \\frac{s}{t} = \\frac{42,000}{4,200} = 10 \\text{ m/s}$

This demonstrates how derived quantities (velocity) come from base quantities (length and time).

**Prefixes:**

Common SI prefixes used in Singapore measurements:
- **Giga (G)** = 10⁹ → Singapore's power consumption: ~50 GW peak
- **Mega (M)** = 10⁶ → Changi Airport passengers: ~5.5 million/month
- **Kilo (k)** = 10³ → MRT fare distances in km
- **Milli (m)** = 10⁻³ → Rainfall in mm (Singapore average: 2,340 mm/year)
- **Micro (μ)** = 10⁻⁶ → Particulate matter PM2.5 (air quality)
- **Nano (n)** = 10⁻⁹ → Semiconductor manufacturing (GlobalFoundries: 7 nm chips)

**Homogeneity of Equations:**

Physical equations must be dimensionally consistent. For example, in the equation $s = ut + \\frac{1}{2}at^2$:
- Left side: [L] (length)
- Right side: [LT⁻¹][T] + [LT⁻²][T²] = [L] + [L] = [L] ✓

This principle helps verify equations and detect errors."""
            },
            {
                "id": "scalars-vectors",
                "type": "text",
                "title": "Scalars and Vectors",
                "title_zh": "标量和矢量",
                "content": """**Scalar quantities** have magnitude only, while **vector quantities** have both magnitude and direction.

**Scalars:**
- Distance, speed, mass, time, energy, temperature
- Can be added algebraically: 5 kg + 3 kg = 8 kg

**Vectors:**
- Displacement, velocity, acceleration, force, momentum
- Must consider direction when adding

**Vector Addition:**

Two methods for adding vectors:
1. **Parallelogram method** - Draw vectors head-to-tail
2. **Component method** - Resolve into x and y components

**Example: Singapore Cable Car System**

A cable car travels from Mount Faber to Sentosa. If the horizontal distance is **1,650 m** and the vertical drop is **150 m**, the total displacement is:

$$d = \\sqrt{(1650)^2 + (150)^2} = \\sqrt{2,722,500 + 22,500} = 1,657 \\text{ m}$$

The angle below horizontal:
$$\\theta = \\tan^{-1}\\left(\\frac{150}{1650}\\right) = 5.2°$$

The displacement is **1,657 m at 5.2° below horizontal**, not just 1,800 m total distance traveled.

**Vector Resolution:**

For a vector $\\vec{F}$ at angle $\\theta$ from horizontal:
- Horizontal component: $F_x = F \\cos \\theta$
- Vertical component: $F_y = F \\sin \\theta$

**Example: F1 Singapore Grand Prix**

When a race car rounds Turn 7 (Singapore Sling) at **200 km/h (55.6 m/s)** on a banking angle of **10°**, the velocity components are:
- Parallel to track: $v_{\\parallel} = 55.6 \\cos 10° = 54.7 \\text{ m/s}$
- Perpendicular to track: $v_{\\perp} = 55.6 \\sin 10° = 9.7 \\text{ m/s}$

**Vector Subtraction:**

To subtract vector $\\vec{B}$ from $\\vec{A}$, add the negative of $\\vec{B}$:
$$\\vec{A} - \\vec{B} = \\vec{A} + (-\\vec{B})$$

This is useful for finding **displacement** when you know initial and final position vectors."""
            },
            {
                "id": "errors-uncertainties",
                "type": "text",
                "title": "Errors and Uncertainties",
                "title_zh": "误差和不确定性",
                "content": """**Errors** are the differences between measured and true values. **Uncertainties** quantify the range within which the true value likely lies.

**Types of Errors:**

1. **Systematic Errors** - Consistent bias in one direction
   - **Zero error**: Instrument doesn't read zero when it should
   - **Calibration error**: Instrument poorly calibrated
   - **Example**: A vernier caliper with +0.02 mm zero error will consistently read 0.02 mm too high
   - **Singapore context**: NEWater quality sensors require monthly calibration to avoid systematic errors

2. **Random Errors** - Unpredictable variations
   - Reading errors from parallax
   - Fluctuations in experimental conditions
   - **Example**: Timing a swinging pendulum manually causes random variations ±0.1 s
   - **Minimized by**: Taking multiple readings and averaging

**Accuracy vs Precision:**

- **Accuracy**: How close measurements are to the true value
- **Precision**: How close measurements are to each other

**Example: Singapore Weather Station**

A weather station at Changi measures temperature. If the true temperature is 30.0°C:
- **Accurate and precise**: Readings of 29.9, 30.0, 30.1°C (close to true value and each other)
- **Precise but inaccurate**: Readings of 32.0, 32.1, 32.0°C (close to each other but wrong)
- **Accurate but imprecise**: Readings of 28.0, 30.0, 32.0°C (average is correct but spread out)

**Uncertainty Calculation:**

For a single measurement with instrument resolution $\\Delta x$:
$$\\text{Absolute uncertainty} = \\frac{\\Delta x}{2}$$

For example, a ruler with 1 mm divisions has absolute uncertainty ±0.5 mm.

**Percentage Uncertainty:**
$$\\text{Percentage uncertainty} = \\frac{\\text{absolute uncertainty}}{\\text{measured value}} \\times 100\\%$$

**Example: Measuring HDB Flat Dimensions**

Measuring a room length of 5.2 m with a tape measure (±0.001 m resolution):
- Absolute uncertainty = ±0.0005 m
- Percentage uncertainty = $\\frac{0.0005}{5.2} \\times 100\\% = 0.01\\%$

**Combining Uncertainties:**

When **adding or subtracting**, add absolute uncertainties:
$$\\text{If } z = x + y, \\text{ then } \\Delta z = \\Delta x + \\Delta y$$

When **multiplying or dividing**, add percentage uncertainties:
$$\\text{If } z = x \\times y, \\text{ then } \\frac{\\Delta z}{z} = \\frac{\\Delta x}{x} + \\frac{\\Delta y}{y}$$

When **raising to a power**:
$$\\text{If } z = x^n, \\text{ then } \\frac{\\Delta z}{z} = n \\times \\frac{\\Delta x}{x}$$

**Significant Figures:**

Rules for significant figures:
1. All non-zero digits are significant
2. Zeros between non-zero digits are significant
3. Leading zeros are NOT significant
4. Trailing zeros after decimal point ARE significant

**Example: Singapore Reservoir Capacity**

Marina Reservoir capacity = 2,900,000 m³ (2 significant figures)
Written in scientific notation: $2.9 \\times 10^6 \\text{ m}^3$

**PUB water quality standards**: pH = 7.0 ± 0.5 (2 significant figures, shows uncertainty)

**Recording Results:**

Always record results as: **measured value ± absolute uncertainty**

Example: Length of Helix Bridge = $280 \\text{ m} ± 2 \\text{ m}$

This means the true length is between 278 m and 282 m."""
            }
        ],
        "exercises": []
    },
    {
        "id": "kinematics-jc1-physics",
        "title": "Kinematics",
        "title_zh": "运动学",
        "gradeLevel": "jc1",
        "description": "Motion in one and two dimensions, including displacement, velocity, and acceleration",
        "description_zh": "一维和二维运动,包括位移、速度和加速度",
        "tag": "Physics",
        "tag_zh": "物理",
        "objectives": [
            "Define and distinguish displacement, velocity, and acceleration",
            "Apply equations of motion to solve kinematics problems",
            "Analyze motion using displacement-time and velocity-time graphs",
            "Solve projectile motion problems in two dimensions"
        ],
        "objectives_zh": [
            "定义并区分位移、速度和加速度",
            "应用运动方程解决运动学问题",
            "使用位移-时间和速度-时间图分析运动",
            "解决二维抛体运动问题"
        ],
        "sections": [
            {
                "id": "displacement-velocity-acceleration",
                "type": "text",
                "title": "Displacement, Velocity, and Acceleration",
                "title_zh": "位移、速度和加速度",
                "content": """**Kinematics** is the study of motion without considering the forces that cause it.

**Displacement ($s$)**:
- Vector quantity representing change in position
- Displacement ≠ Distance (displacement considers direction)
- Unit: meter (m)

**Example: Circle Line MRT**

A train traveling from Serangoon → Paya Lebar → Dakota → Serangoon completes a loop:
- **Distance traveled**: ~15 km (along the track)
- **Displacement**: 0 m (returns to starting point)

**Velocity ($v$)**:
- Rate of change of displacement
- $v = \\frac{\\Delta s}{\\Delta t}$ (average velocity)
- $v = \\frac{ds}{dt}$ (instantaneous velocity)
- Unit: m/s or m s⁻¹

**Speed vs Velocity:**
- **Speed** is scalar (magnitude only)
- **Velocity** is vector (magnitude and direction)

**Example: Singapore Marathon**

42.195 km marathon from Orchard Road → Gardens by the Bay → return:
- **Average speed** = $\\frac{42,195 \\text{ m}}{\\text{time}}$
- **Average velocity** = Much lower (net displacement is small as route loops back)

**Acceleration ($a$)**:
- Rate of change of velocity
- $a = \\frac{\\Delta v}{\\Delta t}$ (average acceleration)
- $a = \\frac{dv}{dt}$ (instantaneous acceleration)
- Unit: m/s² or m s⁻²

**Example: MRT Train Acceleration**

When an MRT train accelerates from Bishan station:
- Initial velocity: $u = 0 \\text{ m/s}$ (at rest)
- Final velocity: $v = 20 \\text{ m/s}$ (after 10 seconds)
- Acceleration: $a = \\frac{20 - 0}{10} = 2 \\text{ m/s}^2$

**Deceleration** (negative acceleration):
When the same train brakes approaching the next station:
- Initial velocity: $u = 20 \\text{ m/s}$
- Final velocity: $v = 0 \\text{ m/s}$ (stops in 8 seconds)
- Acceleration: $a = \\frac{0 - 20}{8} = -2.5 \\text{ m/s}^2$

**Uniform Acceleration:**

When acceleration is constant, we have **equations of motion**:

1. $v = u + at$
2. $s = ut + \\frac{1}{2}at^2$
3. $v^2 = u^2 + 2as$
4. $s = \\frac{1}{2}(u + v)t$

Where:
- $u$ = initial velocity
- $v$ = final velocity
- $a$ = acceleration
- $s$ = displacement
- $t$ = time

**Example: Sentosa Express Monorail**

The monorail accelerates uniformly from Sentosa Station ($u = 0$) at $a = 1.5 \\text{ m/s}^2$ for $t = 6 \\text{ s}$. Find the displacement.

Using $s = ut + \\frac{1}{2}at^2$:
$$s = 0(6) + \\frac{1}{2}(1.5)(6)^2 = 0 + 0.5(1.5)(36) = 27 \\text{ m}$$

The monorail travels 27 meters during acceleration."""
            },
            {
                "id": "graphical-analysis",
                "type": "text",
                "title": "Graphical Analysis of Motion",
                "title_zh": "运动的图解分析",
                "content": """**Displacement-Time Graphs:**

The **gradient** of a displacement-time graph gives **velocity**:
$$v = \\frac{\\Delta s}{\\Delta t} = \\text{gradient of } s\\text{-}t \\text{ graph}$$

**Example: Marina Bay Sands SkyPark Elevator**

An elevator ascends 200 m to the SkyPark in 60 seconds:
- Graph shows straight line from (0, 0) to (60, 200)
- Gradient = $\\frac{200}{60} = 3.33 \\text{ m/s}$ (constant upward velocity)

**Velocity-Time Graphs:**

Two key features:
1. **Gradient** gives **acceleration**: $a = \\frac{\\Delta v}{\\Delta t}$
2. **Area under curve** gives **displacement**: $s = \\int v \\, dt$

**Example: Singapore Grand Prix Lap**

A race car accelerates from pit lane:
- Stage 1 (0-5 s): Linear increase from 0 to 50 m/s → $a = \\frac{50}{5} = 10 \\text{ m/s}^2$
- Stage 2 (5-20 s): Constant 50 m/s → $a = 0 \\text{ m/s}^2$
- Stage 3 (20-25 s): Linear decrease to 20 m/s → $a = \\frac{20-50}{5} = -6 \\text{ m/s}^2$

**Displacement** = Area under v-t graph:
- Stage 1: $\\frac{1}{2}(5)(50) = 125 \\text{ m}$
- Stage 2: $(15)(50) = 750 \\text{ m}$
- Stage 3: $\\frac{1}{2}(5)(50+20) = 175 \\text{ m}$
- **Total**: $125 + 750 + 175 = 1,050 \\text{ m}$

**Acceleration-Time Graphs:**

- **Area under curve** gives **change in velocity**: $\\Delta v = \\int a \\, dt$

**Motion Graph Relationships:**

| Graph Type | Gradient | Area Under Curve |
|------------|----------|------------------|
| $s$-$t$ | Velocity ($v$) | N/A |
| $v$-$t$ | Acceleration ($a$) | Displacement ($s$) |
| $a$-$t$ | Rate of change of $a$ | Change in velocity ($\\Delta v$) |

**Example: Lift in CapitaGreen Tower**

An express lift in CapitaGreen (40 floors) has this velocity profile:
- 0-2 s: Accelerates at 2 m/s² (gradient = +2)
- 2-15 s: Constant 6 m/s (gradient = 0)
- 15-17 s: Decelerates at -3 m/s² (gradient = -3)

**Displacement calculation:**
- Phase 1: $s_1 = \\frac{1}{2}(2)(2 \\times 2) = 4 \\text{ m}$
- Phase 2: $s_2 = (15-2)(6) = 78 \\text{ m}$
- Phase 3: $s_3 = \\frac{1}{2}(2)(6+0) = 6 \\text{ m}$
- **Total height**: $4 + 78 + 6 = 88 \\text{ m}$ (approximately 22 floors)"""
            },
            {
                "id": "projectile-motion",
                "type": "text",
                "title": "Projectile Motion",
                "title_zh": "抛体运动",
                "content": """**Projectile motion** involves motion in two dimensions under the influence of gravity, with:
- **Horizontal motion**: Constant velocity (no acceleration)
- **Vertical motion**: Constant acceleration due to gravity ($g = 9.81 \\text{ m/s}^2$ downward)

**Key Principles:**

1. **Independence of horizontal and vertical motion**
2. **Horizontal velocity is constant**: $v_x = u \\cos \\theta$
3. **Vertical motion follows equations of motion** with $a = -g$

**Equations for Projectile Motion:**

Initial velocity $u$ at angle $\\theta$ from horizontal:
- **Horizontal component**: $u_x = u \\cos \\theta$
- **Vertical component**: $u_y = u \\sin \\theta$

**Horizontal displacement** (range):
$$R = u_x t = (u \\cos \\theta) t$$

**Vertical displacement**:
$$y = u_y t - \\frac{1}{2}gt^2 = (u \\sin \\theta) t - \\frac{1}{2}gt^2$$

**Maximum height** (when $v_y = 0$):
$$H = \\frac{u^2 \\sin^2 \\theta}{2g}$$

**Time of flight** (returns to same level):
$$T = \\frac{2u \\sin \\theta}{g}$$

**Example: Gardens by the Bay Water Fountain**

A fountain in Gardens by the Bay shoots water at $u = 15 \\text{ m/s}$ at $\\theta = 60°$ from horizontal. Find the maximum height and range.

**Maximum height:**
$$H = \\frac{(15)^2 \\sin^2 60°}{2(9.81)} = \\frac{225 \\times 0.75}{19.62} = 8.6 \\text{ m}$$

**Time of flight:**
$$T = \\frac{2(15) \\sin 60°}{9.81} = \\frac{30 \\times 0.866}{9.81} = 2.65 \\text{ s}$$

**Range:**
$$R = (15 \\cos 60°)(2.65) = (15 \\times 0.5)(2.65) = 19.9 \\text{ m}$$

**Example: Singapore Flyer Water View**

A tourist drops a coin from the Singapore Flyer at height $h = 165 \\text{ m}$ while the capsule is moving horizontally at $v_x = 0.26 \\text{ m/s}$ (circumference 540 m / revolution time 2,100 s).

**Time to hit ground:**
Using $h = \\frac{1}{2}gt^2$:
$$165 = \\frac{1}{2}(9.81)t^2$$
$$t = \\sqrt{\\frac{2 \\times 165}{9.81}} = \\sqrt{33.64} = 5.8 \\text{ s}$$

**Horizontal distance traveled:**
$$x = v_x t = 0.26 \\times 5.8 = 1.5 \\text{ m}$$

The coin lands 1.5 m away from directly below the drop point.

**Trajectory Equation:**

Eliminating time from the parametric equations:
$$y = x \\tan \\theta - \\frac{gx^2}{2u^2 \\cos^2 \\theta}$$

This is a **parabola**, the characteristic shape of projectile motion.

**Example: ArtScience Museum Water Feature**

Water is projected horizontally at $v_0 = 8 \\text{ m/s}$ from height $h = 5 \\text{ m}$.

**Time to fall:**
$$t = \\sqrt{\\frac{2h}{g}} = \\sqrt{\\frac{2 \\times 5}{9.81}} = 1.01 \\text{ s}$$

**Horizontal range:**
$$R = v_0 t = 8 \\times 1.01 = 8.1 \\text{ m}$$"""
            }
        ],
        "exercises": []
    }
]

# Note: Due to length constraints, I'm creating first 2 chapters here
# Additional 6 chapters (Dynamics, Forces, Work/Energy/Power, Current, DC Circuits, Waves)
# will be created in a follow-up script

print("Creating JC 1 Physics chapters (Part 1: Chapters 1-2)...")
print(f"Total chapters in this batch: {len(jc1_physics_chapters)}")

# Save to JSON file
with open('chapters/jc1_physics_chapters_part1.json', 'w', encoding='utf-8') as f:
    json.dump(jc1_physics_chapters, f, ensure_ascii=False, indent=2)

print("✓ Created chapters/jc1_physics_chapters_part1.json")
print("\nChapters created:")
for i, ch in enumerate(jc1_physics_chapters, 1):
    section_count = len(ch['sections'])
    print(f"  {i}. {ch['title']} - {section_count} sections")

print("\nNext: Create remaining 6 chapters (Dynamics through Waves)")
