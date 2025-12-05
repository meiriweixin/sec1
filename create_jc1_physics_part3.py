#!/usr/bin/env python3
"""
Creates final JC 1 Physics chapters 6-8 (Current of Electricity, DC Circuits, Waves)
"""

import json

jc1_physics_chapters_part3 = [
    {
        "id": "current-electricity-jc1-physics",
        "title": "Current of Electricity",
        "title_zh": "电流",
        "gradeLevel": "jc1",
        "description": "Electric current, potential difference, resistance, and electrical power",
        "description_zh": "电流、电位差、电阻和电功率",
        "tag": "Physics",
        "tag_zh": "物理",
        "objectives": [
            "Define electric current, charge, and potential difference",
            "Apply Ohm's Law to calculate resistance",
            "Understand resistivity and factors affecting resistance",
            "Calculate electrical power and energy"
        ],
        "objectives_zh": [
            "定义电流、电荷和电位差",
            "应用欧姆定律计算电阻",
            "理解电阻率和影响电阻的因素",
            "计算电功率和电能"
        ],
        "sections": [
            {
                "id": "current-charge",
                "type": "text",
                "title": "Electric Current and Charge",
                "title_zh": "电流和电荷",
                "content": """**Electric charge** is a fundamental property of matter, measured in coulombs (C).

**Elementary charges:**
- Electron charge: $e = -1.6 \\times 10^{-19}$ C
- Proton charge: $e = +1.6 \\times 10^{-19}$ C

**Electric current** is the rate of flow of charge:
$$I = \\frac{Q}{t}$$

Where:
- $I$ = current (amperes, A)
- $Q$ = charge (coulombs, C)
- $t$ = time (seconds, s)

**1 ampere = 1 coulomb per second**

**Example: HDB Electrical Meter**

A typical HDB 4-room flat uses 600 kWh per month. If operated at 230 V, what is the average current?

**Energy:** $E = 600 \\text{ kWh} = 600 \\times 3.6 \\times 10^6 = 2.16 \\times 10^9$ J

**Time:** 30 days = $30 \\times 24 \\times 3,600 = 2,592,000$ s

**Average power:**
$$P = \\frac{E}{t} = \\frac{2.16 \\times 10^9}{2,592,000} = 833 \\text{ W}$$

**Average current:**
$$I = \\frac{P}{V} = \\frac{833}{230} = 3.6 \\text{ A}$$

**Charge Flow:**

Number of electrons flowing per second:
$$n = \\frac{I}{e} = \\frac{\\text{current}}{\\text{electron charge}}$$

**Example: Singapore Power Grid Cable**

A power cable carries 100 A. How many electrons pass through per second?

$$n = \\frac{100}{1.6 \\times 10^{-19}} = 6.25 \\times 10^{20} \\text{ electrons/s}$$

That's over 600 billion trillion electrons every second!

**Conventional Current vs Electron Flow:**

- **Conventional current**: Flows from positive (+) to negative (−)
- **Electron flow**: Flows from negative (−) to positive (+)

We use conventional current (historical convention from before electrons were discovered).

**Drift Velocity:**

In a conductor, electrons drift slowly in the direction opposite to conventional current:
$$I = nAve$$

Where:
- $n$ = number density of charge carriers (electrons/m³)
- $A$ = cross-sectional area (m²)
- $v$ = drift velocity (m/s)
- $e$ = electron charge (C)

**Example: Copper Wire in HDB Wall**

A 2.5 mm² copper wire carries 10 A.
- Copper has $n = 8.5 \\times 10^{28}$ electrons/m³
- Area: $A = 2.5 \\times 10^{-6}$ m²

**Drift velocity:**
$$v = \\frac{I}{nAe} = \\frac{10}{8.5 \\times 10^{28} \\times 2.5 \\times 10^{-6} \\times 1.6 \\times 10^{-19}}$$
$$v = 2.9 \\times 10^{-4} \\text{ m/s} = 0.29 \\text{ mm/s}$$

Electrons drift extremely slowly (~1 meter per hour), but electric signals travel at nearly the speed of light!

**Potential Difference (Voltage):**

**Potential difference** between two points is the work done per unit charge in moving charge between those points:
$$V = \\frac{W}{Q}$$

Unit: volt (V) = joule per coulomb (J/C)

**Example: 12V Car Battery in Singapore Taxi**

When 5 C of charge flows through the battery:
$$W = VQ = 12 \\times 5 = 60 \\text{ J}$$

The battery does 60 J of work to move 5 C of charge."""
            },
            {
                "id": "resistance-ohms-law",
                "type": "text",
                "title": "Resistance and Ohm's Law",
                "title_zh": "电阻和欧姆定律",
                "content": """**Resistance** is the opposition to current flow in a conductor.

**Ohm's Law:**

For ohmic conductors (resistance constant):
$$V = IR$$

Where:
- $V$ = potential difference (volts, V)
- $I$ = current (amperes, A)
- $R$ = resistance (ohms, Ω)

**Example: LED Street Light on Orchard Road**

An LED street light operates at 24 V and draws 2 A.

**Resistance:**
$$R = \\frac{V}{I} = \\frac{24}{2} = 12 \\text{ Ω}$$

**Ohmic vs Non-ohmic Conductors:**

**Ohmic:**
- Resistance constant (V-I graph is straight line through origin)
- Examples: Metal wires at constant temperature

**Non-ohmic:**
- Resistance varies with voltage/current
- Examples: Filament bulbs (resistance increases with temperature), diodes, thermistors

**I-V Characteristics:**

**Example: MRT Station Halogen Bulb**

At low voltages (cold filament): $R = 10$ Ω
At operating voltage 12 V (hot filament): $R = 48$ Ω

When first switched on:
$$I = \\frac{12}{10} = 1.2 \\text{ A}$$ (high inrush current)

At steady state:
$$I = \\frac{12}{48} = 0.25 \\text{ A}$$ (normal operating current)

This is why bulbs often fail when switched on (high current stress).

**Resistivity:**

Resistance depends on material properties and dimensions:
$$R = \\frac{\\rho L}{A}$$

Where:
- $\\rho$ = resistivity (Ω·m)
- $L$ = length (m)
- $A$ = cross-sectional area (m²)

**Resistivity values:**
- Copper: $\\rho = 1.7 \\times 10^{-8}$ Ω·m (good conductor)
- Silicon: $\\rho \\approx 10^3$ Ω·m (semiconductor)
- Glass: $\\rho > 10^{10}$ Ω·m (insulator)

**Example: Underground Cable from Senoko to City**

Power transmission cable (copper):
- Length: $L = 20,000$ m (20 km)
- Diameter: 50 mm → Area: $A = \\pi (0.025)^2 = 1.96 \\times 10^{-3}$ m²

**Resistance:**
$$R = \\frac{1.7 \\times 10^{-8} \\times 20,000}{1.96 \\times 10^{-3}} = 0.17 \\text{ Ω}$$

If carrying 500 A:
$$V_{\\text{drop}} = IR = 500 \\times 0.17 = 85 \\text{ V}$$

This voltage drop represents wasted energy, which is why high-voltage transmission is used.

**Temperature Effect on Resistance:**

For metals, resistance increases with temperature:
$$R_T = R_0(1 + \\alpha \\Delta T)$$

Where $\\alpha$ = temperature coefficient

**Example: NEWater Plant Heating Element**

A heating element has resistance 50 Ω at 20°C. For copper, $\\alpha = 0.004$ /°C.

At operating temperature 100°C:
$$R_{100} = 50(1 + 0.004 \\times 80) = 50(1.32) = 66 \\text{ Ω}$$

Resistance increases by 32% when hot.

**Semiconductors** (thermistors) have **negative** temperature coefficient:
- Resistance decreases as temperature increases
- Used in temperature sensors

**Example: HDB Aircon Thermistor**

Thermistor in aircon thermostat:
- At 25°C: $R = 10,000$ Ω
- At 30°C: $R = 6,000$ Ω

As room warms, resistance drops, triggering compressor."""
            },
            {
                "id": "electrical-power",
                "type": "text",
                "title": "Electrical Power and Energy",
                "title_zh": "电功率和电能",
                "content": """**Electrical Power** is the rate of electrical energy transfer:
$$P = VI = I^2R = \\frac{V^2}{R}$$

Unit: Watt (W) = J/s

**Example: Common Singapore Appliances**

| Appliance | Voltage | Current | Power |
|-----------|---------|---------|-------|
| LED bulb | 230 V | 0.04 A | 9 W |
| Ceiling fan | 230 V | 0.3 A | 69 W |
| Aircon (1.5 HP) | 230 V | 6.5 A | 1,500 W |
| Washing machine | 230 V | 2.2 A | 500 W |
| Water heater | 230 V | 13 A | 3,000 W |

**Power Calculation:**

**Example: HDB Kitchen Electric Stove**

An electric stove draws 13 A at 230 V.

**Power:**
$$P = VI = 230 \\times 13 = 2,990 \\text{ W} \\approx 3 \\text{ kW}$$

**Resistance:**
$$R = \\frac{V}{I} = \\frac{230}{13} = 17.7 \\text{ Ω}$$

**Alternative power calculation:**
$$P = I^2R = 13^2 \\times 17.7 = 2,993 \\text{ W}$$ ✓

**Electrical Energy:**

Energy consumed over time:
$$E = Pt = VIt = I^2Rt$$

Unit: Joule (J) or kilowatt-hour (kWh)

**1 kWh = 1,000 W × 3,600 s = 3.6 MJ**

**Example: Monthly HDB Electricity Bill**

Appliance usage:
- **Aircon**: 1.5 kW × 8 hours/day × 30 days = 360 kWh
- **Fridge**: 0.15 kW × 24 hours/day × 30 days = 108 kWh
- **Lighting**: 0.1 kW × 6 hours/day × 30 days = 18 kWh
- **Others**: 114 kWh

**Total:** 600 kWh/month

At $0.30/kWh: **Bill = $180**

**Power Dissipation in Transmission:**

Power lost as heat in transmission lines:
$$P_{\\text{loss}} = I^2R$$

**Example: Why High-Voltage Transmission?**

Transmitting 10 MW over cable with resistance 0.5 Ω:

**Low voltage (10 kV):**
- Current: $I = \\frac{P}{V} = \\frac{10,000,000}{10,000} = 1,000$ A
- Power loss: $P_{\\text{loss}} = I^2R = 1,000^2 \\times 0.5 = 500,000$ W = **500 kW** (5% loss)

**High voltage (400 kV):**
- Current: $I = \\frac{10,000,000}{400,000} = 25$ A
- Power loss: $P_{\\text{loss}} = 25^2 \\times 0.5 = 312.5$ W = **0.3 kW** (0.003% loss)

Singapore's national grid uses 400 kV transmission for minimal losses.

**Heating Effect (Joule's Law):**

Energy converted to heat in a resistor:
$$E = I^2Rt = \\frac{V^2}{R}t$$

**Example: Water Heater at OCBC Aquatic Centre**

Pool shower heater (3 kW, 230 V) heats 50 L of water from 28°C to 38°C.

**Energy needed:**
$$E = mc\\Delta T = 50 \\times 4,200 \\times 10 = 2,100,000 \\text{ J} = 2.1 \\text{ MJ}$$

**Time required:**
$$t = \\frac{E}{P} = \\frac{2.1 \\times 10^6}{3,000} = 700 \\text{ s} = 11.7 \\text{ min}$$

**Efficiency:**

$$\\eta = \\frac{\\text{useful energy output}}{\\text{total electrical energy input}} \\times 100\\%$$

**Example: LED vs Incandescent Bulb**

Both produce same light output (800 lumens):

**Incandescent (60 W):**
- Input: 60 W
- Light output: 12 W
- Heat waste: 48 W
- Efficiency: $\\frac{12}{60} \\times 100\\% = 20\\%$

**LED (9 W):**
- Input: 9 W
- Light output: 7 W
- Heat waste: 2 W
- Efficiency: $\\frac{7}{9} \\times 100\\% = 78\\%$

**Over 10,000 hours of use:**
- Incandescent: 600 kWh ($180)
- LED: 90 kWh ($27)
- **Savings: $153**

This is why NEA promotes LED lighting in Singapore."""
            }
        ],
        "exercises": []
    },
    {
        "id": "dc-circuits-jc1-physics",
        "title": "DC Circuits",
        "title_zh": "直流电路",
        "gradeLevel": "jc1",
        "description": "Series and parallel circuits, Kirchhoff's laws, and potential dividers",
        "description_zh": "串联和并联电路、基尔霍夫定律和分压器",
        "tag": "Physics",
        "tag_zh": "物理",
        "objectives": [
            "Analyze series and parallel resistor combinations",
            "Apply Kirchhoff's current and voltage laws",
            "Design and analyze potential divider circuits",
            "Understand internal resistance and terminal voltage"
        ],
        "objectives_zh": [
            "分析串联和并联电阻组合",
            "应用基尔霍夫电流和电压定律",
            "设计和分析分压电路",
            "理解内阻和端电压"
        ],
        "sections": [
            {
                "id": "series-parallel",
                "type": "text",
                "title": "Series and Parallel Circuits",
                "title_zh": "串联和并联电路",
                "content": """**Series Circuits:**

Components connected in a single loop - same current flows through all.

**Key properties:**
1. **Current is same** everywhere: $I = I_1 = I_2 = I_3$
2. **Voltages add:** $V_{\\text{total}} = V_1 + V_2 + V_3$
3. **Resistances add:** $R_{\\text{total}} = R_1 + R_2 + R_3$

**Example: Christmas Lights on Orchard Road**

Old-style series Christmas lights have 50 bulbs (each 4.6 V, 4.6 Ω) connected in series across 230 V.

**Total resistance:**
$$R_{\\text{total}} = 50 \\times 4.6 = 230 \\text{ Ω}$$

**Current:**
$$I = \\frac{V}{R} = \\frac{230}{230} = 1 \\text{ A}$$

**Voltage across each bulb:**
$$V_{\\text{bulb}} = IR = 1 \\times 4.6 = 4.6 \\text{ V}$$ ✓

**Problem:** If one bulb fails (open circuit), **all lights go out** (series circuit broken).

Modern LED strings use parallel sections to avoid this.

**Parallel Circuits:**

Components connected across same two points - same voltage across all.

**Key properties:**
1. **Voltage is same** across all: $V = V_1 = V_2 = V_3$
2. **Currents add:** $I_{\\text{total}} = I_1 + I_2 + I_3$
3. **Reciprocals of resistances add:** $\\frac{1}{R_{\\text{total}}} = \\frac{1}{R_1} + \\frac{1}{R_2} + \\frac{1}{R_3}$

**Example: HDB Living Room Electrical Outlets**

Three appliances plugged into 230 V outlets (parallel):
- TV: 100 W → $I_1 = \\frac{100}{230} = 0.43$ A
- Aircon: 1,500 W → $I_2 = \\frac{1,500}{230} = 6.52$ A
- Fan: 70 W → $I_3 = \\frac{70}{230} = 0.30$ A

**Total current from wall:**
$$I_{\\text{total}} = 0.43 + 6.52 + 0.30 = 7.25 \\text{ A}$$

Circuit breaker rated at 13 A - safe ✓

**Combined Series-Parallel:**

**Example: Traffic Light Circuit at Orchard Road Junction**

Red, yellow, green LEDs in parallel (each 20 Ω), with a 10 Ω series resistor, powered by 12 V battery.

**Parallel LEDs:**
$$\\frac{1}{R_p} = \\frac{1}{20} + \\frac{1}{20} + \\frac{1}{20} = \\frac{3}{20}$$
$$R_p = \\frac{20}{3} = 6.67 \\text{ Ω}$$

**Total circuit resistance:**
$$R_{\\text{total}} = R_s + R_p = 10 + 6.67 = 16.67 \\text{ Ω}$$

**Total current:**
$$I_{\\text{total}} = \\frac{12}{16.67} = 0.72 \\text{ A}$$

**Voltage across LEDs:**
$$V_{\\text{LEDs}} = I_{\\text{total}} \\times R_p = 0.72 \\times 6.67 = 4.8 \\text{ V}$$

**Current through each LED:**
$$I_{\\text{LED}} = \\frac{4.8}{20} = 0.24 \\text{ A}$$

**Two identical resistors in parallel:**

Special case: $R_{\\text{total}} = \\frac{R}{2}$

**Example: NEWater Plant Redundant Pump Motors**

Two identical 10 Ω motors in parallel provide redundancy:
$$R_{\\text{total}} = \\frac{10}{2} = 5 \\text{ Ω}$$

If one fails, other continues working (though with different current)."""
            },
            {
                "id": "kirchhoffs-laws",
                "type": "text",
                "title": "Kirchhoff's Laws",
                "title_zh": "基尔霍夫定律",
                "content": """**Kirchhoff's Current Law (KCL):**

At any junction, **total current in = total current out**
$$\\sum I_{\\text{in}} = \\sum I_{\\text{out}}$$

Based on **conservation of charge**.

**Example: Marina Bay MRT Interchange**

Current distribution in a circuit junction:
- Current into junction: $I_1 = 5$ A, $I_2 = 3$ A
- Current out: $I_3 = 2$ A, $I_4 = ?$

**By KCL:**
$$I_1 + I_2 = I_3 + I_4$$
$$5 + 3 = 2 + I_4$$
$$I_4 = 6 \\text{ A}$$

**Kirchhoff's Voltage Law (KVL):**

Around any closed loop, **sum of EMFs = sum of voltage drops**
$$\\sum \\mathcal{E} = \\sum IR$$

Based on **conservation of energy**.

**Example: Simple Circuit with Battery and Resistors**

12 V battery with three resistors in series: $R_1 = 3$ Ω, $R_2 = 5$ Ω, $R_3 = 4$ Ω.

**Total resistance:**
$$R_{\\text{total}} = 3 + 5 + 4 = 12 \\text{ Ω}$$

**Current:**
$$I = \\frac{12}{12} = 1 \\text{ A}$$

**Voltage drops:**
- $V_1 = IR_1 = 1 \\times 3 = 3$ V
- $V_2 = IR_2 = 1 \\times 5 = 5$ V
- $V_3 = IR_3 = 1 \\times 4 = 4$ V

**Check KVL:**
$$\\mathcal{E} = V_1 + V_2 + V_3$$
$$12 = 3 + 5 + 4$$ ✓

**Example: Complex Circuit - Changi Airport Runway Lighting**

Two-loop circuit with batteries and resistors:

**Loop 1:** 10 V battery, $R_1 = 2$ Ω, $R_2 = 3$ Ω
**Loop 2:** 6 V battery, $R_2 = 3$ Ω (shared), $R_3 = 1$ Ω

Let $I_1$ = current in loop 1, $I_2$ = current in loop 2.

**KVL for Loop 1:**
$$10 = I_1 R_1 + (I_1 - I_2)R_2$$
$$10 = 2I_1 + 3(I_1 - I_2)$$
$$10 = 5I_1 - 3I_2$$ ... (1)

**KVL for Loop 2:**
$$6 = I_2 R_3 + (I_2 - I_1)R_2$$
$$6 = I_2 + 3(I_2 - I_1)$$
$$6 = 4I_2 - 3I_1$$ ... (2)

Solving simultaneously:
From (1): $I_1 = \\frac{10 + 3I_2}{5}$

Substitute into (2):
$$6 = 4I_2 - 3\\left(\\frac{10 + 3I_2}{5}\\right)$$
$$30 = 20I_2 - 30 - 9I_2$$
$$I_2 = \\frac{60}{11} = 5.45 \\text{ A}$$

$$I_1 = \\frac{10 + 3(5.45)}{5} = 5.27 \\text{ A}$$

**Practical Application: HDB Distribution Board**

Kirchhoff's laws used to analyze current distribution in:
- Multi-circuit distribution boards
- Backup power systems
- Solar panel arrays with battery storage

**Wheatstone Bridge Circuit:**

Used for precision resistance measurement:

Four resistors arranged in diamond:
- $R_1$ and $R_2$ in one arm
- $R_3$ and $R_x$ (unknown) in other arm

**Balanced condition** (no current through center meter):
$$\\frac{R_1}{R_2} = \\frac{R_3}{R_x}$$

$$R_x = \\frac{R_2 R_3}{R_1}$$

**Example: Strain Gauge on Helix Bridge**

Strain gauges change resistance under stress. In a Wheatstone bridge:
- $R_1 = R_2 = R_3 = 120$ Ω
- $R_x$ = strain gauge

At balance: $R_x = 120$ Ω (no strain)

Under load: $R_x = 120.5$ Ω
$$\\Delta R = 0.5 \\text{ Ω}$$

This tiny change is detected and converted to strain measurement."""
            },
            {
                "id": "potential-divider-internal-resistance",
                "type": "text",
                "title": "Potential Dividers and Internal Resistance",
                "title_zh": "分压器和内阻",
                "content": """**Potential Divider (Voltage Divider):**

Two resistors in series divide the voltage proportionally:
$$V_{\\text{out}} = \\frac{R_2}{R_1 + R_2} \\times V_{\\text{in}}$$

**Example: Temperature Sensor for HDB Aircon**

Thermistor ($R_T$) in series with fixed resistor ($R_F = 10$ kΩ) across 5 V supply.

At 25°C: $R_T = 10$ kΩ
$$V_{\\text{out}} = \\frac{10,000}{10,000 + 10,000} \\times 5 = 2.5 \\text{ V}$$

At 30°C: $R_T = 6$ kΩ (resistance drops as temp rises)
$$V_{\\text{out}} = \\frac{6,000}{6,000 + 10,000} \\times 5 = 1.875 \\text{ V}$$

Microcontroller reads voltage and converts to temperature.

**Variable Potential Divider (Potentiometer):**

Used for **volume control, dimmer switches, position sensors**.

**Example: Singapore Flyer Motor Speed Control**

A potentiometer controls voltage to DC motor:
- Total resistance: 100 Ω
- Input: 12 V
- Wiper position: 30% from bottom

**Output voltage:**
$$V_{\\text{out}} = 0.30 \\times 12 = 3.6 \\text{ V}$$

Motor runs at reduced speed.

**Light-Dependent Resistor (LDR) Circuit:**

**Example: Orchard Road Street Light Auto-Control**

LDR ($R_L$) in series with fixed resistor ($R_F = 20$ kΩ) across 9 V.

**Bright daylight:** $R_L = 1$ kΩ
$$V_{\\text{out}} = \\frac{20,000}{1,000 + 20,000} \\times 9 = 8.57 \\text{ V}$$ (high - lights OFF)

**Dark night:** $R_L = 200$ kΩ
$$V_{\\text{out}} = \\frac{20,000}{200,000 + 20,000} \\times 9 = 0.82 \\text{ V}$$ (low - lights ON)

**Internal Resistance:**

Real batteries have internal resistance $r$, which causes voltage drop when current flows.

**Terminal voltage:**
$$V = \\mathcal{E} - Ir$$

Where:
- $\\mathcal{E}$ = EMF (electromotive force - voltage with no load)
- $I$ = current
- $r$ = internal resistance

**Example: Old Car Battery (Singapore Taxi)**

12 V battery with internal resistance 0.5 Ω.

**No load** (engine off, no current):
$$V = \\mathcal{E} = 12 \\text{ V}$$

**Starting engine** (draws 100 A):
$$V = 12 - 100(0.5) = 12 - 50 = -38 \\text{ V}$$

Wait - that's impossible! This means internal resistance has increased (battery degraded). Healthy battery: $r \\approx 0.01$ Ω.

**Realistic healthy battery:**
$$V = 12 - 100(0.01) = 11 \\text{ V}$$

Voltage drops to 11 V during cranking (lights dim).

**Power Dissipation in Internal Resistance:**

$$P_{\\text{internal}} = I^2 r$$

This is **wasted energy** heating the battery.

**Maximum Power Transfer:**

Power delivered to external load $R$ is maximum when:
$$R = r$$

**Example: Solar Panel with Battery Storage**

Solar panel: $\\mathcal{E} = 18$ V, $r = 2$ Ω

**Short circuit** ($R = 0$):
$$I = \\frac{\\mathcal{E}}{r} = \\frac{18}{2} = 9 \\text{ A}$$
$$P_{\\text{load}} = 0 \\text{ W}$$ (no external resistor)

**Open circuit** ($R = \\infty$):
$$I = 0 \\text{ A}$$
$$P_{\\text{load}} = 0 \\text{ W}$$ (no current)

**Matched load** ($R = r = 2$ Ω):
$$I = \\frac{18}{2 + 2} = 4.5 \\text{ A}$$
$$P_{\\text{load}} = I^2 R = (4.5)^2 \\times 2 = 40.5 \\text{ W}$$ (maximum!)

**Efficiency:**
$$\\eta = \\frac{R}{R + r} \\times 100\\%$$

At matched load:
$$\\eta = \\frac{2}{2 + 2} \\times 100\\% = 50\\%$$

Only 50% efficient at maximum power transfer! For higher efficiency, use $R >> r$.

**Example: NEWater Plant Battery Backup**

Backup battery system: $\\mathcal{E} = 48$ V, $r = 0.1$ Ω

Powers 4 kW pump ($R = 0.576$ Ω):

**Current:**
$$I = \\frac{48}{0.1 + 0.576} = 71 \\text{ A}$$

**Power to pump:**
$$P_{\\text{pump}} = I^2 R = 71^2 \\times 0.576 = 2,904 \\text{ W}$$ (< 4 kW!)

Battery can't supply full 4 kW due to internal resistance."""
            }
        ],
        "exercises": []
    },
    {
        "id": "waves-jc1-physics",
        "title": "Waves",
        "title_zh": "波",
        "gradeLevel": "jc1",
        "description": "Wave properties, electromagnetic spectrum, and wave phenomena",
        "description_zh": "波的性质、电磁波谱和波动现象",
        "tag": "Physics",
        "tag_zh": "物理",
        "objectives": [
            "Distinguish between transverse and longitudinal waves",
            "Define and calculate wave properties (frequency, wavelength, speed)",
            "Understand the electromagnetic spectrum and its applications",
            "Explain superposition, interference, and diffraction"
        ],
        "objectives_zh": [
            "区分横波和纵波",
            "定义和计算波的性质（频率、波长、速度）",
            "理解电磁波谱及其应用",
            "解释叠加、干涉和衍射"
        ],
        "sections": [
            {
                "id": "wave-properties",
                "type": "text",
                "title": "Wave Properties and Types",
                "title_zh": "波的性质和类型",
                "content": """**Waves** transfer energy without transferring matter.

**Types of Waves:**

**1. Transverse Waves**
- Oscillations perpendicular to direction of energy transfer
- Examples: Light, radio waves, water waves, waves on strings

**2. Longitudinal Waves**
- Oscillations parallel to direction of energy transfer
- Examples: Sound waves, ultrasound, seismic P-waves

**Example: Waves on Singapore Cable Car Cable**

When wind hits cable car cable, **transverse waves** propagate along cable:
- Cable vibrates up and down (perpendicular)
- Wave energy travels along cable (horizontal)

**Wave Parameters:**

**Amplitude ($A$):** Maximum displacement from equilibrium (m)

**Wavelength ($\\lambda$):** Distance between successive crests or troughs (m)

**Period ($T$):** Time for one complete oscillation (s)

**Frequency ($f$):** Number of oscillations per second (Hz)
$$f = \\frac{1}{T}$$

**Wave speed ($v$):** Distance traveled per unit time
$$v = f\\lambda = \\frac{\\lambda}{T}$$

**Example: Marina Bay Water Waves**

Waves approaching Marina Barrage:
- Wavelength: $\\lambda = 15$ m
- Frequency: $f = 0.2$ Hz (one wave every 5 seconds)

**Wave speed:**
$$v = f\\lambda = 0.2 \\times 15 = 3 \\text{ m/s}$$

**Phase and Phase Difference:**

**Phase** describes position in wave cycle (measured in radians or degrees).

**Phase difference** between two points:
$$\\Delta \\phi = \\frac{2\\pi \\Delta x}{\\lambda}$$

Where $\\Delta x$ = distance between points

**Example: WiFi@SG Interference**

Two WiFi routers (2.4 GHz) in HDB flat:
- Wavelength: $\\lambda = \\frac{c}{f} = \\frac{3 \\times 10^8}{2.4 \\times 10^9} = 0.125$ m = 12.5 cm

At point 25 cm from one router and 18.75 cm from other:
- Path difference: $\\Delta x = 25 - 18.75 = 6.25$ cm = 0.0625 m

**Phase difference:**
$$\\Delta \\phi = \\frac{2\\pi \\times 0.0625}{0.125} = \\pi \\text{ radians} = 180°$$

**Destructive interference** - weak signal!

**Energy in Waves:**

Wave intensity (power per unit area):
$$I \\propto A^2 f^2$$

Intensity decreases with distance (spreading):
$$I \\propto \\frac{1}{r^2}$$

**Example: Sound from Singapore Grand Prix**

Race car engine produces 140 dB at 10 m distance. At 100 m:

$$I_{100} = I_{10} \\times \\left(\\frac{10}{100}\\right)^2 = \\frac{I_{10}}{100}$$

Sound intensity reduces to 1% (much quieter for spectators in grandstand).

**Doppler Effect:**

Frequency changes when source or observer moves:
$$f' = f \\frac{v \\pm v_o}{v \\mp v_s}$$

Where:
- $v$ = wave speed
- $v_o$ = observer velocity (+ approaching, - receding)
- $v_s$ = source velocity (- approaching, + receding)

**Example: Ambulance Siren on ECP**

Ambulance siren: $f = 1,000$ Hz, traveling at $v_s = 30$ m/s
Sound speed: $v = 340$ m/s

**Approaching stationary observer:**
$$f' = 1,000 \\times \\frac{340}{340 - 30} = 1,000 \\times \\frac{340}{310} = 1,097 \\text{ Hz}$$

**Receding:**
$$f' = 1,000 \\times \\frac{340}{340 + 30} = 1,000 \\times \\frac{340}{370} = 919 \\text{ Hz}$$

Pitch drops from 1,097 Hz to 919 Hz as ambulance passes."""
            },
            {
                "id": "electromagnetic-spectrum",
                "type": "text",
                "title": "Electromagnetic Spectrum",
                "title_zh": "电磁波谱",
                "content": """**Electromagnetic (EM) waves** are transverse waves that:
- Travel at speed of light: $c = 3.0 \\times 10^8$ m/s (in vacuum)
- Don't require a medium (can travel through vacuum)
- All satisfy: $c = f\\lambda$

**The Electromagnetic Spectrum:**

| Type | Wavelength | Frequency | Singapore Applications |
|------|------------|-----------|------------------------|
| **Radio** | > 1 mm | < 300 GHz | MediaCorp broadcast, WiFi@SG |
| **Microwave** | 1 mm - 1 m | 300 MHz - 300 GHz | 5G networks, airport radar |
| **Infrared** | 700 nm - 1 mm | 300 GHz - 430 THz | Night vision cameras, thermal imaging |
| **Visible** | 400-700 nm | 430-750 THz | Gardens by the Bay lighting |
| **Ultraviolet** | 10-400 nm | 750 THz - 30 PHz | Water sterilization (NEWater) |
| **X-rays** | 0.01-10 nm | 30 PHz - 30 EHz | Medical imaging (SGH, NUH) |
| **Gamma** | < 0.01 nm | > 30 EHz | Cancer treatment (NCCS) |

**Radio Waves:**

**Example: MediaCorp Radio Stations**

- **FM 93.3**: $f = 93.3$ MHz = $93.3 \\times 10^6$ Hz
$$\\lambda = \\frac{c}{f} = \\frac{3 \\times 10^8}{93.3 \\times 10^6} = 3.22 \\text{ m}$$

- **AM 938**: $f = 938$ kHz = $938 \\times 10^3$ Hz
$$\\lambda = \\frac{3 \\times 10^8}{938 \\times 10^3} = 320 \\text{ m}$$

AM has longer wavelength → better diffraction around buildings → wider coverage.

**Microwaves:**

**Example: 5G Network in Singapore**

5G frequencies: 3.5 GHz and 26 GHz (mmWave)

**At 3.5 GHz:**
$$\\lambda = \\frac{3 \\times 10^8}{3.5 \\times 10^9} = 0.086 \\text{ m} = 8.6 \\text{ cm}$$

**At 26 GHz:**
$$\\lambda = \\frac{3 \\times 10^8}{26 \\times 10^9} = 0.012 \\text{ m} = 1.2 \\text{ cm}$$

Higher frequency → shorter wavelength → more directional → need more base stations.

**Example: Changi Airport Weather Radar**

Aircraft weather radar: 9.4 GHz (X-band)
$$\\lambda = \\frac{3 \\times 10^8}{9.4 \\times 10^9} = 3.2 \\text{ cm}$$

Can detect raindrops and turbulence.

**Infrared:**

**Example: Singapore Fever Screening (Thermal Cameras)**

Thermal cameras detect infrared radiation (8-14 μm) emitted by human body:
- Normal body temp (37°C): Peak IR at ~10 μm
- Fever detection (>37.5°C): Increased IR emission

**Visible Light:**

Wavelength range: 400 nm (violet) to 700 nm (red)

**Example: Gardens by the Bay Supertree LED Lighting**

RGB LEDs:
- Red: $\\lambda \\approx 630$ nm → $f = \\frac{3 \\times 10^8}{630 \\times 10^{-9}} = 4.76 \\times 10^{14}$ Hz
- Green: $\\lambda \\approx 520$ nm → $f = 5.77 \\times 10^{14}$ Hz
- Blue: $\\lambda \\approx 470$ nm → $f = 6.38 \\times 10^{14}$ Hz

**Ultraviolet:**

**Example: NEWater UV Disinfection**

UV-C light (254 nm) kills bacteria and viruses:
$$f = \\frac{3 \\times 10^8}{254 \\times 10^{-9}} = 1.18 \\times 10^{15}$ Hz = 1.18 PHz$$

High frequency → high energy → breaks DNA bonds in microorganisms.

**X-rays:**

**Example: Changi Airport Baggage Scanners**

X-ray scanners use ~100 keV x-rays:
- Wavelength: $\\lambda \\approx 0.01$ nm
- Penetrate luggage but absorbed differently by materials
- Organic materials (explosives) vs metals appear different

**Example: Singapore General Hospital CT Scan**

Medical x-rays (40-120 keV):
- Absorbed by bones (calcium) → appear white
- Pass through soft tissue → appear darker
- 3D reconstruction from multiple angles

**Gamma Rays:**

**Example: National Cancer Centre Singapore (NCCS)**

Gamma knife radiotherapy uses cobalt-60 gamma rays:
- Wavelength: < 0.001 nm
- Very high energy → destroys cancer cells
- Precisely focused on tumor"""
            },
            {
                "id": "wave-phenomena",
                "type": "text",
                "title": "Superposition, Interference, and Diffraction",
                "title_zh": "叠加、干涉和衍射",
                "content": """**Principle of Superposition:**

When two or more waves meet, the resultant displacement is the **vector sum** of individual displacements.

$$y_{\\text{resultant}} = y_1 + y_2 + y_3 + ...$$

**Interference:**

Two types based on phase relationship:

**1. Constructive Interference** (waves in phase)
- Crests meet crests, troughs meet troughs
- Amplitude increases: $A_{\\text{max}} = A_1 + A_2$
- Path difference = $n\\lambda$ (where $n = 0, 1, 2, ...$)

**2. Destructive Interference** (waves out of phase)
- Crests meet troughs
- Amplitude decreases: $A_{\\text{min}} = |A_1 - A_2|$
- Path difference = $(n + \\frac{1}{2})\\lambda$

**Example: Esplanade Concert Hall Acoustics**

Two speakers 8 m apart, emitting 500 Hz sound (wavelength 0.68 m).

Point P is 10 m from speaker A and 11.36 m from speaker B.

**Path difference:**
$$\\Delta x = 11.36 - 10 = 1.36 \\text{ m}$$

$$\\frac{\\Delta x}{\\lambda} = \\frac{1.36}{0.68} = 2$$

Path difference = $2\\lambda$ → **Constructive interference** (loud)

Point Q is 10 m from A and 10.34 m from B:
$$\\Delta x = 0.34 \\text{ m} = 0.5\\lambda$$

Path difference = $\\frac{\\lambda}{2}$ → **Destructive interference** (quiet)

This creates **dead spots** in concert halls if not properly designed.

**Standing Waves:**

Formed when two identical waves traveling in opposite directions interfere:
- **Nodes**: Points of zero amplitude (destructive interference)
- **Antinodes**: Points of maximum amplitude (constructive interference)

**Example: Guitar String at Esplanade**

String length $L = 0.65$ m, fundamental frequency 330 Hz (note E):

**Fundamental mode** ($n = 1$):
$$\\lambda_1 = 2L = 2 \\times 0.65 = 1.3 \\text{ m}$$

**Wave speed:**
$$v = f\\lambda = 330 \\times 1.3 = 429 \\text{ m/s}$$

**Higher harmonics:**
- 2nd harmonic: $\\lambda_2 = L = 0.65$ m, $f_2 = 660$ Hz
- 3rd harmonic: $\\lambda_3 = \\frac{2L}{3} = 0.43$ m, $f_3 = 990$ Hz

**Diffraction:**

Spreading of waves when passing through an opening or around obstacles.

**Amount of diffraction depends on:**
$$\\text{Diffraction} \\propto \\frac{\\lambda}{\\text{gap width}}$$

**Example: Singapore Lighthouse (Raffles Lighthouse)**

Lighthouse beam (visible light, $\\lambda \\approx 500$ nm) through 0.5 m opening:
$$\\frac{\\lambda}{a} = \\frac{500 \\times 10^{-9}}{0.5} = 10^{-6}$$

Negligible diffraction → narrow, well-defined beam.

**Example: Sound Around HDB Block**

Low-frequency sound (100 Hz, $\\lambda = 3.4$ m) vs high-frequency (5 kHz, $\\lambda = 6.8$ cm) around building corner.

**Low frequency:**
$$\\frac{\\lambda}{a} = \\frac{3.4}{10} = 0.34$$ (significant diffraction - easily heard around corner)

**High frequency:**
$$\\frac{\\lambda}{a} = \\frac{0.068}{10} = 0.0068$$ (little diffraction - blocked by building)

This is why **bass sounds travel around obstacles** better than treble.

**Single-Slit Diffraction:**

Central maximum width:
$$\\theta \\approx \\frac{\\lambda}{a}$$ (for small angles)

**Example: Laser Pointer at Singapore Science Centre**

Red laser ($\\lambda = 650$ nm) through 0.1 mm slit:
$$\\theta = \\frac{650 \\times 10^{-9}}{0.1 \\times 10^{-3}} = 0.0065 \\text{ radians} = 0.37°$$

At distance 10 m:
$$\\text{width} = 2 \\times 10 \\times \\tan(0.37°) = 0.13 \\text{ m} = 13 \\text{ cm}$$

Laser spreads to 13 cm diameter.

**Double-Slit Interference:**

Bright fringes occur where:
$$d \\sin \\theta = n\\lambda$$

Where:
- $d$ = slit separation
- $\\theta$ = angle to bright fringe
- $n$ = order (0, 1, 2, ...)

**Fringe separation:**
$$\\Delta y = \\frac{\\lambda D}{d}$$

Where $D$ = distance to screen

**Example: Fiber Optic Cable Testing (SingTel)**

Testing fiber optic cable with laser ($\\lambda = 1,550$ nm):
- Two fibers 0.125 mm apart ($d$)
- Screen 2 m away ($D$)

**Fringe spacing:**
$$\\Delta y = \\frac{1,550 \\times 10^{-9} \\times 2}{0.125 \\times 10^{-3}} = 0.0248 \\text{ m} = 2.48 \\text{ cm}$$

**Polarization:**

Transverse waves can be **polarized** (oscillations in specific plane).
Longitudinal waves (sound) **cannot** be polarized.

**Example: Singapore Airlines Cockpit Windows**

Polarized filters reduce glare:
- Sunlight reflects off clouds → partially polarized
- Polarizing filter blocks this component
- Reduces eye strain for pilots

**Example: 3D Cinema at Cathay Cineplex**

Uses polarized light:
- Left-eye image: Vertically polarized
- Right-eye image: Horizontally polarized
- Polarizing glasses separate images → 3D effect

**Applications in Singapore:**

| Phenomenon | Application |
|------------|-------------|
| Interference | WiFi optimization, noise-canceling headphones |
| Diffraction | Antenna design, ultrasound imaging |
| Standing waves | Musical instruments, microwave ovens |
| Polarization | Sunglasses, LCD screens, stress analysis |
| Doppler | Speed cameras on expressways, medical ultrasound |"""
            }
        ],
        "exercises": []
    }
]

print("Creating JC 1 Physics chapters (Part 3: Chapters 6-8)...")
print(f"Total chapters in this batch: {len(jc1_physics_chapters_part3)}")

# Save to JSON file
with open('chapters/jc1_physics_chapters_part3.json', 'w', encoding='utf-8') as f:
    json.dump(jc1_physics_chapters_part3, f, ensure_ascii=False, indent=2)

print("✓ Created chapters/jc1_physics_chapters_part3.json")
print("\nChapters created:")
for i, ch in enumerate(jc1_physics_chapters_part3, 6):
    section_count = len(ch['sections'])
    print(f"  {i}. {ch['title']} - {section_count} sections")

print("\nAll 8 JC 1 Physics chapters complete!")
print("Next: Combine all parts into single file")
