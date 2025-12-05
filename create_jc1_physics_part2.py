#!/usr/bin/env python3
"""
Creates JC 1 Physics chapters 3-5 (Dynamics, Forces, Work/Energy/Power)
"""

import json

jc1_physics_chapters_part2 = [
    {
        "id": "dynamics-jc1-physics",
        "title": "Dynamics",
        "title_zh": "动力学",
        "gradeLevel": "jc1",
        "description": "Newton's laws of motion, linear momentum, and impulse",
        "description_zh": "牛顿运动定律、线性动量和冲量",
        "tag": "Physics",
        "tag_zh": "物理",
        "objectives": [
            "Apply Newton's three laws of motion to solve problems",
            "Understand and calculate linear momentum and impulse",
            "Apply conservation of momentum to collision problems",
            "Analyze forces using free-body diagrams"
        ],
        "objectives_zh": [
            "应用牛顿三大运动定律解决问题",
            "理解并计算线性动量和冲量",
            "将动量守恒应用于碰撞问题",
            "使用自由体图分析力"
        ],
        "sections": [
            {
                "id": "newtons-laws",
                "type": "text",
                "title": "Newton's Laws of Motion",
                "title_zh": "牛顿运动定律",
                "content": """**Newton's First Law (Law of Inertia):**

An object at rest stays at rest, and an object in motion continues with constant velocity, unless acted upon by a net external force.

**Inertia** is the tendency of an object to resist changes in its state of motion. **Mass** is the measure of inertia.

**Example: MRT Train at Jurong East**

When an MRT train starts moving from Jurong East station, passengers feel a backward force. This is because:
- The train accelerates forward
- Passengers' bodies tend to stay at rest (inertia)
- Passengers feel pushed backward relative to the train

**Newton's Second Law:**

The net force on an object is equal to the rate of change of its momentum:
$$F_{\\text{net}} = \\frac{dp}{dt} = ma$$

Where:
- $F$ = net force (N)
- $m$ = mass (kg)
- $a$ = acceleration (m/s²)

**Example: Port of Singapore Crane**

A container crane at PSA lifts a **20-ton (20,000 kg) container** with upward acceleration of **0.5 m/s²**. Find the tension in the cable.

**Free-body diagram:**
- Upward: Tension $T$
- Downward: Weight $W = mg = 20,000 \\times 9.81 = 196,200$ N

Applying Newton's second law:
$$T - W = ma$$
$$T = ma + W = 20,000(0.5) + 196,200 = 206,200 \\text{ N}$$

The cable tension is **206.2 kN**.

**Newton's Third Law:**

For every action, there is an equal and opposite reaction.

Important: Action-reaction pairs:
- Act on **different objects**
- Are of the **same type** of force
- Are **equal in magnitude** and **opposite in direction**

**Example: Singapore Airlines A380 Takeoff**

When an A380 takes off from Changi Airport:
- **Action**: Engines push exhaust gases backward
- **Reaction**: Exhaust gases push plane forward (thrust)

The thrust force accelerates the 560-ton aircraft to takeoff speed (~280 km/h) in about 45 seconds on a 3,000 m runway.

**Example: HDB Lift System**

In an HDB lift:
- **Action**: Person pushes down on lift floor with force $F$
- **Reaction**: Lift floor pushes up on person with force $F$

If the lift accelerates upward at $a = 2 \\text{ m/s}^2$ and a person has mass $m = 70$ kg:

Normal force from floor:
$$N = m(g + a) = 70(9.81 + 2) = 826.7 \\text{ N}$$

The person feels **heavier** during upward acceleration.

**Free-Body Diagrams:**

Steps to draw a free-body diagram:
1. Choose the object to analyze
2. Draw all forces acting ON that object
3. Label forces with type and magnitude
4. Choose coordinate system
5. Resolve forces into components

**Example: Helix Bridge Pedestrian**

A 60 kg person walks across Helix Bridge against a 20 N wind force while experiencing 500 N friction from the ground.

**Forces on person:**
- Weight: $W = 60 \\times 9.81 = 588.6$ N (downward)
- Normal force: $N = 588.6$ N (upward)
- Wind: $F_{\\text{wind}} = 20$ N (backward)
- Friction: $F_f = 500$ N (forward)

Net horizontal force = $500 - 20 = 480$ N forward."""
            },
            {
                "id": "momentum-impulse",
                "type": "text",
                "title": "Linear Momentum and Impulse",
                "title_zh": "线性动量和冲量",
                "content": """**Linear Momentum:**

Momentum is the product of mass and velocity:
$$\\vec{p} = m\\vec{v}$$

Unit: kg m/s or N s

**Example: Loaded vs Empty Truck on PIE**

Two identical trucks traveling at 60 km/h (16.7 m/s) on PIE:
- **Empty truck** (5,000 kg): $p = 5,000 \\times 16.7 = 83,500$ kg m/s
- **Loaded truck** (15,000 kg): $p = 15,000 \\times 16.7 = 250,500$ kg m/s

The loaded truck has **3 times more momentum** and is much harder to stop.

**Impulse:**

Impulse is the change in momentum:
$$\\text{Impulse} = \\Delta p = F \\Delta t$$

Or, impulse equals force multiplied by time:
$$J = F \\Delta t = m\\Delta v$$

Unit: N s (newton-second)

**Impulse-Momentum Theorem:**
$$F\\Delta t = m(v - u)$$

**Example: SAF Combat Training Fall**

An NSF soldier (mass 70 kg) jumps from a 2 m platform during training. When landing:

Velocity on impact: $v = \\sqrt{2gh} = \\sqrt{2 \\times 9.81 \\times 2} = 6.26$ m/s

If he **lands stiffly** (stops in 0.1 s):
$$F = \\frac{m\\Delta v}{\\Delta t} = \\frac{70 \\times 6.26}{0.1} = 4,382 \\text{ N}$$

If he **bends knees** (stops in 0.5 s):
$$F = \\frac{70 \\times 6.26}{0.5} = 876 \\text{ N}$$

**Bending knees increases contact time**, dramatically reducing impact force.

**Force-Time Graphs:**

Area under a force-time graph = Impulse

**Example: Singapore Grand Prix Crash Barrier**

When a race car hits a crash barrier at Turn 10:
- Initial momentum: $p_i = 800 \\text{ kg} \\times 50 \\text{ m/s} = 40,000$ kg m/s
- Final momentum: $p_f = 0$ kg m/s
- Impulse needed: $J = 40,000$ N s

If barrier has:
- **Hard wall**: Stops car in 0.2 s → $F = \\frac{40,000}{0.2} = 200,000$ N = 200 kN
- **SAFER barrier**: Stops car in 1.0 s → $F = \\frac{40,000}{1.0} = 40,000$ N = 40 kN

SAFER barriers increase collision time, reducing peak force by **5 times**.

**Conservation of Momentum:**

In an isolated system (no external forces), **total momentum before = total momentum after**:
$$\\sum p_{\\text{before}} = \\sum p_{\\text{after}}$$

**Example: SBS Bus Collision on Orchard Road**

Two buses collide and stick together:
- **Bus A**: 12,000 kg at 8 m/s (moving right)
- **Bus B**: 10,000 kg at -5 m/s (moving left)

Total momentum before:
$$p_{\\text{total}} = (12,000)(8) + (10,000)(-5) = 96,000 - 50,000 = 46,000 \\text{ kg m/s}$$

After collision (stuck together, mass = 22,000 kg):
$$v = \\frac{p_{\\text{total}}}{m_{\\text{total}}} = \\frac{46,000}{22,000} = 2.09 \\text{ m/s}$$

Both buses move together at **2.09 m/s to the right** after collision."""
            },
            {
                "id": "collisions",
                "type": "text",
                "title": "Elastic and Inelastic Collisions",
                "title_zh": "弹性和非弹性碰撞",
                "content": """**Types of Collisions:**

1. **Elastic Collision**
   - Momentum conserved ✓
   - Kinetic energy conserved ✓
   - Objects bounce apart

2. **Inelastic Collision**
   - Momentum conserved ✓
   - Kinetic energy NOT conserved ✗
   - Some KE converted to heat/sound/deformation

3. **Perfectly Inelastic Collision**
   - Momentum conserved ✓
   - Maximum KE lost
   - Objects stick together after collision

**Elastic Collision Formula:**

For two objects with masses $m_1$ and $m_2$:

**Before:** velocities $u_1$ and $u_2$
**After:** velocities $v_1$ and $v_2$

Conservation of momentum:
$$m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2$$

Conservation of KE:
$$\\frac{1}{2}m_1 u_1^2 + \\frac{1}{2}m_2 u_2^2 = \\frac{1}{2}m_1 v_1^2 + \\frac{1}{2}m_2 v_2^2$$

**Special case** (one object initially at rest, $u_2 = 0$):
$$v_1 = \\frac{m_1 - m_2}{m_1 + m_2}u_1$$
$$v_2 = \\frac{2m_1}{m_1 + m_2}u_1$$

**Example: Singapore Snooker Championship**

White ball (0.17 kg) moving at 2 m/s hits stationary red ball (0.17 kg) head-on.

Since $m_1 = m_2$:
- White ball velocity after: $v_1 = 0$ m/s (stops)
- Red ball velocity after: $v_2 = 2$ m/s (moves with original speed)

**The white ball stops and the red ball moves off** - characteristic of equal-mass elastic collision.

**Coefficient of Restitution ($e$):**

Measures how "bouncy" a collision is:
$$e = \\frac{\\text{relative speed after}}{\\text{relative speed before}} = \\frac{v_2 - v_1}{u_1 - u_2}$$

- $e = 1$: Perfectly elastic
- $0 < e < 1$: Inelastic
- $e = 0$: Perfectly inelastic (stick together)

**Example: Basketball Drop at OCBC Arena**

A basketball (mass 0.62 kg) is dropped from height $h_1 = 2.0$ m and rebounds to $h_2 = 1.5$ m.

Speed just before hitting ground:
$$v_1 = \\sqrt{2gh_1} = \\sqrt{2 \\times 9.81 \\times 2.0} = 6.26 \\text{ m/s}$$

Speed just after leaving ground:
$$v_2 = \\sqrt{2gh_2} = \\sqrt{2 \\times 9.81 \\times 1.5} = 5.42 \\text{ m/s}$$

Coefficient of restitution:
$$e = \\frac{v_2}{v_1} = \\frac{5.42}{6.26} = 0.87$$

**Energy Loss in Collisions:**

$$\\text{KE lost} = \\text{KE}_{\\text{before}} - \\text{KE}_{\\text{after}}$$

**Example: Car Accident on ECP**

Two cars collide and stick together (perfectly inelastic):
- **Car A**: 1,200 kg at 25 m/s
- **Car B**: 1,500 kg at 0 m/s (stationary)

**Momentum conservation:**
$$1,200(25) + 1,500(0) = (1,200 + 1,500)v$$
$$v = \\frac{30,000}{2,700} = 11.1 \\text{ m/s}$$

**KE before:**
$$KE_i = \\frac{1}{2}(1,200)(25)^2 = 375,000 \\text{ J}$$

**KE after:**
$$KE_f = \\frac{1}{2}(2,700)(11.1)^2 = 166,700 \\text{ J}$$

**Energy lost:**
$$\\Delta KE = 375,000 - 166,700 = 208,300 \\text{ J} = 208.3 \\text{ kJ}$$

This energy is converted to **deformation, heat, and sound** during the crash."""
            }
        ],
        "exercises": []
    },
    {
        "id": "forces-jc1-physics",
        "title": "Forces",
        "title_zh": "力",
        "gradeLevel": "jc1",
        "description": "Friction, circular motion, gravitational and elastic forces",
        "description_zh": "摩擦力、圆周运动、重力和弹性力",
        "tag": "Physics",
        "tag_zh": "物理",
        "objectives": [
            "Analyze friction forces in static and kinetic scenarios",
            "Apply concepts of circular motion including centripetal force",
            "Understand gravitational force and its applications",
            "Apply Hooke's Law to elastic deformation problems"
        ],
        "objectives_zh": [
            "分析静摩擦和动摩擦情况",
            "应用圆周运动概念,包括向心力",
            "理解重力及其应用",
            "将胡克定律应用于弹性形变问题"
        ],
        "sections": [
            {
                "id": "friction",
                "type": "text",
                "title": "Friction",
                "title_zh": "摩擦力",
                "content": """**Friction** is a force that opposes relative motion between surfaces in contact.

**Types of Friction:**

1. **Static friction** ($F_s$): Prevents motion from starting
   - Maximum value: $F_{s,\\text{max}} = \\mu_s N$
   - Acts up to maximum value, then object starts moving

2. **Kinetic (dynamic) friction** ($F_k$): Opposes ongoing motion
   - $F_k = \\mu_k N$
   - Usually $\\mu_k < \\mu_s$ (easier to keep moving than to start)

Where:
- $\\mu$ = coefficient of friction (dimensionless)
- $N$ = normal reaction force (N)

**Example: Pushing HDB Furniture**

Moving a 50 kg sofa across HDB living room tiles:
- $\\mu_s = 0.6$ (static)
- $\\mu_k = 0.4$ (kinetic)
- Normal force: $N = mg = 50 \\times 9.81 = 490.5$ N

**Maximum static friction:**
$$F_{s,\\text{max}} = 0.6 \\times 490.5 = 294.3 \\text{ N}$$

Need force > 294.3 N to start moving the sofa.

Once moving, **kinetic friction:**
$$F_k = 0.4 \\times 490.5 = 196.2 \\text{ N}$$

Only need 196.2 N to keep it moving (easier than starting).

**Example: Car Braking on Wet Singapore Roads**

A car (mass 1,500 kg) brakes on wet asphalt ($\\mu_k = 0.4$) at 80 km/h (22.2 m/s).

**Maximum friction force:**
$$F_k = \\mu_k N = 0.4 \\times 1,500 \\times 9.81 = 5,886 \\text{ N}$$

**Deceleration:**
$$a = \\frac{F_k}{m} = \\frac{5,886}{1,500} = 3.92 \\text{ m/s}^2$$

**Stopping distance:**
$$s = \\frac{v^2}{2a} = \\frac{(22.2)^2}{2 \\times 3.92} = 62.9 \\text{ m}$$

On **dry roads** ($\\mu_k = 0.7$), stopping distance would be only **35.9 m** - nearly half!

**Applications:**
- **Anti-lock braking (ABS)**: Maintains static friction (higher than kinetic)
- **Tire treads**: Channel water away to maintain grip
- **Road surface**: Porous asphalt on expressways increases friction"""
            },
            {
                "id": "circular-motion",
                "type": "text",
                "title": "Circular Motion",
                "title_zh": "圆周运动",
                "content": """**Circular motion** requires a centripetal force directed toward the center of the circle.

**Key Quantities:**

**Angular displacement** ($\\theta$): Angle swept (radians)
$$s = r\\theta$$

**Angular velocity** ($\\omega$): Rate of change of angle
$$\\omega = \\frac{\\theta}{t} = \\frac{2\\pi}{T}$$

Where $T$ = period (time for one revolution)

**Linear velocity** ($v$):
$$v = r\\omega = \\frac{2\\pi r}{T}$$

**Centripetal acceleration** ($a_c$):
$$a_c = \\frac{v^2}{r} = r\\omega^2$$

Direction: Always toward center

**Centripetal force** ($F_c$):
$$F_c = ma_c = \\frac{mv^2}{r} = mr\\omega^2$$

**Example: Singapore Flyer**

The Singapore Flyer has:
- Diameter: 150 m → radius $r = 75$ m
- Period: $T = 30$ min = 1,800 s

**Angular velocity:**
$$\\omega = \\frac{2\\pi}{1,800} = 0.00349 \\text{ rad/s}$$

**Linear velocity:**
$$v = r\\omega = 75 \\times 0.00349 = 0.26 \\text{ m/s}$$

**Centripetal acceleration:**
$$a_c = \\frac{v^2}{r} = \\frac{(0.26)^2}{75} = 0.0009 \\text{ m/s}^2$$

This is only **0.009% of Earth's gravity** - barely noticeable!

**Example: F1 Singapore GP Turn 10**

A race car (mass 800 kg) takes Turn 10 (radius 15 m) at 120 km/h (33.3 m/s).

**Centripetal acceleration:**
$$a_c = \\frac{v^2}{r} = \\frac{(33.3)^2}{15} = 74.0 \\text{ m/s}^2 = 7.5g$$

**Centripetal force needed:**
$$F_c = ma_c = 800 \\times 74.0 = 59,200 \\text{ N}$$

This force is provided by **friction** between tires and road. If road is wet and friction is insufficient, car skids outward.

**Maximum safe speed:**

If coefficient of friction is $\\mu = 1.5$ (racing slicks on dry asphalt):
$$F_c = F_{\\text{friction}} = \\mu mg$$
$$\\frac{mv^2}{r} = \\mu mg$$
$$v_{\\text{max}} = \\sqrt{\\mu gr} = \\sqrt{1.5 \\times 9.81 \\times 15} = 14.9 \\text{ m/s} = 54 \\text{ km/h}$$

Wait - this doesn't match! The difference is **downforce** from aerodynamics, which increases the effective normal force beyond just $mg$.

**Example: Conical Pendulum at Gardens by the Bay**

A decorative light (mass 0.5 kg) swings in a horizontal circle of radius 1.2 m, with string making 30° to vertical.

**Forces:**
- **Tension** $T$ in string (at 30° to vertical)
- **Weight** $W = mg = 0.5 \\times 9.81 = 4.905$ N (downward)

**Vertical equilibrium:**
$$T \\cos 30° = mg$$
$$T = \\frac{4.905}{\\cos 30°} = \\frac{4.905}{0.866} = 5.66 \\text{ N}$$

**Horizontal component provides centripetal force:**
$$F_c = T \\sin 30° = 5.66 \\times 0.5 = 2.83 \\text{ N}$$

**Speed:**
$$F_c = \\frac{mv^2}{r}$$
$$v = \\sqrt{\\frac{F_c \\cdot r}{m}} = \\sqrt{\\frac{2.83 \\times 1.2}{0.5}} = 2.61 \\text{ m/s}$$"""
            },
            {
                "id": "gravity-hookes-law",
                "type": "text",
                "title": "Gravitational and Elastic Forces",
                "title_zh": "重力和弹性力",
                "content": """**Gravitational Force:**

Newton's Law of Universal Gravitation:
$$F = \\frac{Gm_1m_2}{r^2}$$

Where:
- $G = 6.67 \\times 10^{-11}$ N m²/kg² (gravitational constant)
- $m_1, m_2$ = masses (kg)
- $r$ = distance between centers (m)

**Weight** is gravitational force on object near Earth's surface:
$$W = mg$$

where $g = 9.81$ m/s² (varies slightly with location)

**Example: Singapore Satellite at CRISP**

The Centre for Remote Imaging, Sensing and Processing tracks satellites. A 500 kg satellite orbits at altitude $h = 500$ km above Singapore.

Earth's mass: $M = 5.97 \\times 10^{24}$ kg
Earth's radius: $R = 6.37 \\times 10^6$ m
Orbital radius: $r = R + h = 6.87 \\times 10^6$ m

**Gravitational force:**
$$F = \\frac{GMm}{r^2} = \\frac{6.67 \\times 10^{-11} \\times 5.97 \\times 10^{24} \\times 500}{(6.87 \\times 10^6)^2}$$
$$F = 4,220 \\text{ N}$$

This provides the centripetal force for circular orbit.

**Orbital speed:**
$$\\frac{mv^2}{r} = \\frac{GMm}{r^2}$$
$$v = \\sqrt{\\frac{GM}{r}} = \\sqrt{\\frac{6.67 \\times 10^{-11} \\times 5.97 \\times 10^{24}}{6.87 \\times 10^6}} = 7,610 \\text{ m/s}$$

**Period:**
$$T = \\frac{2\\pi r}{v} = \\frac{2\\pi \\times 6.87 \\times 10^6}{7,610} = 5,680 \\text{ s} = 94.7 \\text{ min}$$

**Gravitational Field Strength:**

$$g = \\frac{F}{m} = \\frac{GM}{r^2}$$

At Earth's surface ($r = R$):
$$g = \\frac{6.67 \\times 10^{-11} \\times 5.97 \\times 10^{24}}{(6.37 \\times 10^6)^2} = 9.81 \\text{ m/s}^2$$

**Hooke's Law:**

For elastic materials, **extension is proportional to applied force**:
$$F = kx$$

Where:
- $F$ = applied force (N)
- $k$ = spring constant (N/m) - measure of stiffness
- $x$ = extension from natural length (m)

**Elastic Limit:** Maximum force before permanent deformation

**Example: Esplanade Bridge Suspension Cables**

A suspension cable on Esplanade Bridge has spring constant $k = 5.0 \\times 10^6$ N/m.

When supporting a section weighing 50,000 N, extension is:
$$x = \\frac{F}{k} = \\frac{50,000}{5.0 \\times 10^6} = 0.010 \\text{ m} = 1.0 \\text{ cm}$$

**Elastic Potential Energy:**

Energy stored in stretched/compressed spring:
$$E_p = \\frac{1}{2}kx^2$$

**Example: Singapore Indoor Stadium Sprung Floor**

The basketball court floor has spring constant $k = 2.0 \\times 10^5$ N/m per square meter. When a 100 kg player lands, compressing floor by 2 cm:

**Energy stored:**
$$E_p = \\frac{1}{2}kx^2 = \\frac{1}{2}(2.0 \\times 10^5)(0.02)^2 = 40 \\text{ J}$$

This energy is returned to the player, reducing impact and injury risk.

**Series and Parallel Springs:**

**Springs in series** (total extension adds):
$$\\frac{1}{k_{\\text{total}}} = \\frac{1}{k_1} + \\frac{1}{k_2}$$

**Springs in parallel** (forces add):
$$k_{\\text{total}} = k_1 + k_2$$

**Example: HDB Lift Shock Absorbers**

Lift has 4 identical springs (each $k = 10,000$ N/m) in parallel at bottom.

**Total stiffness:**
$$k_{\\text{total}} = 4 \\times 10,000 = 40,000 \\text{ N/m}$$

If lift falls 0.5 m before springs engage:
$$v = \\sqrt{2gh} = \\sqrt{2 \\times 9.81 \\times 0.5} = 3.13 \\text{ m/s}$$

Maximum compression when all KE → EPE:
$$\\frac{1}{2}mv^2 = \\frac{1}{2}kx^2$$

For 1,000 kg lift:
$$x = v\\sqrt{\\frac{m}{k}} = 3.13\\sqrt{\\frac{1,000}{40,000}} = 0.49 \\text{ m}$$"""
            }
        ],
        "exercises": []
    },
    {
        "id": "work-energy-power-jc1-physics",
        "title": "Work, Energy, and Power",
        "title_zh": "功、能量和功率",
        "gradeLevel": "jc1",
        "description": "Work done by forces, energy conservation, and power",
        "description_zh": "力所做的功、能量守恒和功率",
        "tag": "Physics",
        "tag_zh": "物理",
        "objectives": [
            "Calculate work done by constant and variable forces",
            "Apply the principle of conservation of energy",
            "Distinguish between different forms of energy",
            "Calculate power and efficiency in energy conversions"
        ],
        "objectives_zh": [
            "计算恒力和变力所做的功",
            "应用能量守恒原理",
            "区分不同形式的能量",
            "计算能量转换中的功率和效率"
        ],
        "sections": [
            {
                "id": "work-energy",
                "type": "text",
                "title": "Work and Energy",
                "title_zh": "功和能量",
                "content": """**Work** is done when a force causes displacement in the direction of the force.

**Work done by constant force:**
$$W = F s \\cos \\theta$$

Where:
- $W$ = work done (J, joules)
- $F$ = force (N)
- $s$ = displacement (m)
- $\\theta$ = angle between force and displacement

**Special cases:**
- $\\theta = 0°$: $W = Fs$ (force parallel to motion, maximum work)
- $\\theta = 90°$: $W = 0$ (force perpendicular to motion, no work)
- $\\theta = 180°$: $W = -Fs$ (force opposes motion, negative work)

**Example: Pushing Cart at NTUC FairPrice**

Pushing a shopping cart (force $F = 50$ N at $30°$ below horizontal) for distance $s = 20$ m:

$$W = Fs \\cos 30° = 50 \\times 20 \\times 0.866 = 866 \\text{ J}$$

**Example: Carrying Groceries Horizontally**

Carrying 10 kg of groceries ($F_{\\text{up}} = 98.1$ N) horizontally for 100 m:

$$W = Fs \\cos 90° = 98.1 \\times 100 \\times 0 = 0 \\text{ J}$$

**No work is done** because force is perpendicular to displacement!

**Work Done by Variable Force:**

When force varies with position:
$$W = \\int F \\, ds = \\text{area under } F\\text{-}s \\text{ graph}$$

**Example: Stretching Resistance Band (Gardens by the Bay Outdoor Gym)**

For a resistance band with $F = kx$ where $k = 200$ N/m, work to stretch from 0 to 0.5 m:

$$W = \\int_0^{0.5} kx \\, dx = \\frac{1}{2}k x^2 \\Big|_0^{0.5} = \\frac{1}{2}(200)(0.5)^2 = 25 \\text{ J}$$

**Kinetic Energy:**

Energy possessed by moving object:
$$KE = \\frac{1}{2}mv^2$$

**Work-Energy Theorem:**
$$W_{\\text{net}} = \\Delta KE = \\frac{1}{2}m v^2 - \\frac{1}{2}m u^2$$

**Example: MRT Train Acceleration**

An MRT train (mass 100,000 kg) accelerates from rest to 20 m/s:

$$\\Delta KE = \\frac{1}{2}(100,000)(20)^2 - 0 = 20,000,000 \\text{ J} = 20 \\text{ MJ}$$

This is the work done by the motors.

**Potential Energy:**

**Gravitational PE:**
$$PE = mgh$$

Where $h$ = height above reference level

**Example: Marina Bay Sands SkyPark Elevator**

Lifting 15 people (total 1,000 kg) to SkyPark at height 200 m:

$$PE = mgh = 1,000 \\times 9.81 \\times 200 = 1,962,000 \\text{ J} = 1.96 \\text{ MJ}$$

**Elastic PE** (stored in springs):
$$PE = \\frac{1}{2}kx^2$$

**Conservation of Energy:**

In isolated system:
$$\\text{Total Energy} = KE + PE + \\text{other forms} = \\text{constant}$$

For mechanical energy only:
$$KE_i + PE_i = KE_f + PE_f$$

**Example: Singapore Cable Car**

A cable car (mass 5,000 kg) descends from Mount Faber (105 m) to Sentosa (15 m), starting from rest.

**Energy at top:**
$$E_i = PE_i = mgh_i = 5,000 \\times 9.81 \\times 105 = 5,150,250 \\text{ J}$$

**Energy at bottom** (if frictionless):
$$E_f = KE_f + PE_f = \\frac{1}{2}mv^2 + mgh_f$$

$$5,150,250 = \\frac{1}{2}(5,000)v^2 + 5,000(9.81)(15)$$
$$5,150,250 = 2,500v^2 + 735,750$$
$$v = \\sqrt{\\frac{4,414,500}{2,500}} = 42.0 \\text{ m/s}$$

In reality, brakes control descent and convert PE to heat."""
            },
            {
                "id": "power-efficiency",
                "type": "text",
                "title": "Power and Efficiency",
                "title_zh": "功率和效率",
                "content": """**Power** is the rate of doing work or transferring energy:
$$P = \\frac{W}{t} = \\frac{E}{t}$$

Unit: Watt (W) = J/s

**Alternative formula** for power when force causes velocity:
$$P = Fv$$

**Example: NEWater Pump at Bedok**

A pump lifts 1,000 kg of water per second through height 50 m.

**Work per second:**
$$P = \\frac{mgh}{t} = \\frac{1,000 \\times 9.81 \\times 50}{1} = 490,500 \\text{ W} = 490.5 \\text{ kW}$$

**Example: Singapore Airlines A380 Engines**

Each Rolls-Royce engine produces thrust $F = 320$ kN at cruising speed $v = 250$ m/s (900 km/h).

**Power per engine:**
$$P = Fv = 320,000 \\times 250 = 80,000,000 \\text{ W} = 80 \\text{ MW}$$

With 4 engines: **Total power = 320 MW**

**Efficiency:**

Ratio of useful energy output to total energy input:
$$\\eta = \\frac{\\text{useful energy output}}{\\text{total energy input}} \\times 100\\%$$

Or in terms of power:
$$\\eta = \\frac{\\text{useful power output}}{\\text{total power input}} \\times 100\\%$$

**Example: Solar Panels at HDB Rooftop (Yuhua Estate)**

Solar panel specifications:
- Input: Solar radiation = 1,000 W/m² (Singapore average)
- Panel area: 100 m² → Total input = 100,000 W
- Output: Electrical power = 20,000 W

**Efficiency:**
$$\\eta = \\frac{20,000}{100,000} \\times 100\\% = 20\\%$$

Typical solar panels in Singapore are 15-22% efficient.

**Energy Losses:**

Main sources of energy waste:
1. **Friction** → Heat (tires on road, bearings)
2. **Air resistance** → Heat, sound
3. **Electrical resistance** → Heat (wires, transformers)
4. **Imperfect energy conversion** → Various forms

**Example: Tuas Power Station**

**Coal-fired power station:**
- Input: Chemical energy in coal = 1,000 MJ
- Heat engine efficiency: 40%
- Electrical generator efficiency: 95%

**Electricity produced:**
$$E_{\\text{out}} = 1,000 \\times 0.40 \\times 0.95 = 380 \\text{ MJ}$$

**Overall efficiency:**
$$\\eta = \\frac{380}{1,000} \\times 100\\% = 38\\%$$

**Energy wasted:**
- 600 MJ lost as heat in combustion and turbines
- 20 MJ lost in generator

**Example: Electric Car in Singapore (Tesla)**

Battery stores 100 kWh = $100 \\times 3.6 \\times 10^6$ J = 360 MJ

**Powertrain efficiency:** 85%
**Useful energy:** $360 \\times 0.85 = 306$ MJ

Compare to petrol car:
- Petrol tank: 50 L = $50 \\times 34.2$ MJ = 1,710 MJ
- Engine efficiency: 25%
- Useful energy: $1,710 \\times 0.25 = 428$ MJ

Electric car is more efficient per unit energy, but petrol has higher energy density.

**Power Dissipation:**

Energy lost per unit time. For example, friction force $F_f$ opposing motion at speed $v$:
$$P_{\\text{dissipated}} = F_f v$$

**Example: Cyclist on East Coast Park Connector**

Cyclist maintains 10 m/s against air resistance $F_d = 30$ N.

**Power needed:**
$$P = F_d v = 30 \\times 10 = 300 \\text{ W}$$

If cyclist pedals at 100 W, they decelerate (insufficient power to overcome drag)."""
            },
            {
                "id": "energy-applications",
                "type": "text",
                "title": "Energy Applications in Singapore",
                "title_zh": "新加坡的能量应用",
                "content": """**Marina Barrage Hydroelectric Potential:**

Marina Barrage can store water at height 2.5 m above sea level.

**Reservoir volume:** ~$2.9 \\times 10^6$ m³
**Mass of water:** $\\rho V = 1,000 \\times 2.9 \\times 10^6 = 2.9 \\times 10^9$ kg

**Potential energy:**
$$PE = mgh = 2.9 \\times 10^9 \\times 9.81 \\times 2.5 = 7.1 \\times 10^{10} \\text{ J} = 71 \\text{ GJ}$$

If released over 1 hour through turbines (80% efficiency):
$$P = \\frac{0.8 \\times 71 \\times 10^9}{3,600} = 15.8 \\text{ MW}$$

This could power ~10,000 HDB flats for 1 hour.

**Singapore MRT Regenerative Braking:**

When trains brake, kinetic energy is converted back to electricity.

Train mass: 100,000 kg
Speed: 20 m/s → 0 m/s

**KE recovered:**
$$KE = \\frac{1}{2}mv^2 = \\frac{1}{2}(100,000)(20)^2 = 20 \\text{ MJ}$$

With 75% efficiency:
$$E_{\\text{recovered}} = 0.75 \\times 20 = 15 \\text{ MJ}$$

**Annual savings** (millions of braking events):
- Each train brakes ~1,000 times/day
- 250 trains in fleet
- Annual braking: $1,000 \\times 250 \\times 365 = 91.25$ million events
- Energy saved: $15 \\times 10^6 \\times 91.25 \\times 10^6 = 1.37 \\times 10^{15}$ J = **380 GWh/year**

**NEWater Production Energy:**

Reverse osmosis requires high pressure to push water through membranes.

**Energy per cubic meter:** ~1.5 kWh/m³ = 5.4 MJ/m³

**Daily NEWater production:** ~430,000 m³
**Daily energy:** $430,000 \\times 1.5 = 645,000$ kWh = **645 MWh**

**Annual energy:** $645 \\times 365 = 235,425$ MWh = **235 GWh**

PUB uses energy recovery devices to reduce consumption by 30%.

**Sentosa Luge Gravitational Energy:**

Skyride lifts riders up 150 m, then luge coasts down.

**Rider + luge mass:** 80 kg
**PE at top:**
$$PE = mgh = 80 \\times 9.81 \\times 150 = 117,720 \\text{ J} \\approx 118 \\text{ kJ}$$

This PE converts to KE during descent. With friction and braking:
$$v_{\\text{max}} = \\sqrt{2gh_{\\text{eff}}} = \\sqrt{2 \\times 9.81 \\times 50} \\approx 31 \\text{ m/s}$$

Actual max speed controlled to ~10 m/s for safety.

**Kinetic Energy in Singapore Traffic:**

During evening rush hour on CTE:
- ~50,000 vehicles
- Average mass: 1,500 kg
- Average speed: 60 km/h = 16.7 m/s

**Total KE:**
$$KE_{\\text{total}} = 50,000 \\times \\frac{1}{2}(1,500)(16.7)^2 = 10.4 \\text{ GJ}$$

When all vehicles brake (converting KE to heat):
$$P_{\\text{heat}} = \\frac{10.4 \\times 10^9}{300 \\text{ s}} = 34.8 \\text{ MW}$$

This heat contributes to urban heat island effect.

**Energy Consumption Comparison:**

| Activity | Energy (MJ) | Equivalent |
|----------|-------------|------------|
| Climb 62 floors (Tanjong Pagar Centre) | 0.12 | 1 banana |
| Swim 2.4 km (OCBC Aquatic Centre) | 4.2 | 1 chicken rice |
| Cycle 40 km (Pulau Ubin) | 3.6 | 3 kaya toast |
| Run full marathon | 12.6 | 3 plates nasi lemak |
| Daily HDB aircon (8 hr) | 28.8 | 20 bowls laksa |

**Power Requirements in Singapore:**

- **Average home:** 400 W
- **HDB flat (4-room):** 800 W
- **Condo unit:** 1,500 W
- **NTUC FairPrice outlet:** 150 kW
- **MRT station:** 2-5 MW
- **Data center:** 10-50 MW
- **Singapore peak demand:** ~7,000 MW (7 GW)"""
            }
        ],
        "exercises": []
    }
]

print("Creating JC 1 Physics chapters (Part 2: Chapters 3-5)...")
print(f"Total chapters in this batch: {len(jc1_physics_chapters_part2)}")

# Save to JSON file
with open('chapters/jc1_physics_chapters_part2.json', 'w', encoding='utf-8') as f:
    json.dump(jc1_physics_chapters_part2, f, ensure_ascii=False, indent=2)

print("✓ Created chapters/jc1_physics_chapters_part2.json")
print("\nChapters created:")
for i, ch in enumerate(jc1_physics_chapters_part2, 3):
    section_count = len(ch['sections'])
    print(f"  {i}. {ch['title']} - {section_count} sections")

print("\nNext: Create final 3 chapters (Current, DC Circuits, Waves)")
