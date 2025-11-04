"""
Enhance Secondary 2 Math exercises to match Singapore MOE rigor
Replaces simple questions with more challenging, multi-step problems
Aligned with Singapore's problem-solving emphasis
"""

import json

# Load existing chapters
with open('chapters/math-sec2-chapters.json', 'r', encoding='utf-8') as f:
    chapters = json.load(f)

# Enhanced exercise data - more rigorous, multi-step problems
enhanced_exercises = {
    "linear-equations-two-variables-sec2": [
        # Easy (Q1-5): Foundation building
        ("Solve simultaneously: x + y = 10, x - y = 2", ["x=6, y=4", "x=4, y=6", "x=8, y=2", "x=5, y=5"], 0, "mcq"),
        ("At a hawker center, 3 bowls of laksa and 2 cups of kopi cost $15. If 1 laksa costs $1 more than 1 kopi, find the cost of 1 laksa.", ["$3.50", "$3", "$4", "$2.50"], 0, "mcq"),
        ("Using substitution: y = 3x - 2, 2x + y = 8. Find x.", "2", None, "short"),
        ("2 adults and 3 children pay $44 for Zoo tickets. 1 adult and 2 children pay $26. Find adult ticket price.", ["$14", "$12", "$16", "$10"], 0, "mcq"),
        ("Solve by elimination: 3x + 2y = 16, 3x - y = 7", ["x=3, y=3.5", "x=4, y=2", "x=2, y=5", "x=5, y=0.5"], 0, "mcq"),

        # Medium (Q6-10): Application and reasoning
        ("A rectangle's perimeter is 40cm. If length is 4cm more than twice the width, find the dimensions.", ["Length=14cm, Width=6cm", "Length=16cm, Width=4cm", "Length=12cm, Width=8cm", "Length=18cm, Width=2cm"], 0, "mcq"),
        ("The sum of two numbers is 45. If one number is 3 more than twice the other, what is the larger number?", "31", None, "short"),
        ("At Sentosa, family ticket costs $x and child ticket $y. Equation 1: 2x + 3y = 140. Equation 2: x + 2y = 80. If you buy 5 family tickets, how much do you pay?", ["$100", "$150", "$200", "$125"], 0, "mcq"),
        ("Solve: 4x - 3y = 5, 8x - 6y = 10. What can you conclude?", ["Infinite solutions (same line)", "No solution", "One unique solution", "Two solutions"], 0, "mcq"),
        ("A school bought pens at $x each and pencils at $y each. Total for 50 pens and 30 pencils: $85. Total for 30 pens and 50 pencils: $95. Find x - y.", ["$0.25", "-$0.25", "$0.50", "$0"], 1, "mcq"),

        # Hard (Q11-15): Complex problem-solving
        ("MRT charges base fare $0.77 plus $0.08 per km. Bus charges $0.50 plus $0.10 per km. At what distance do both cost the same?", ["1.35 km", "2.7 km", "1 km", "3 km"], 0, "mcq"),
        ("A boat travels 30km downstream in 2h, and 18km upstream in 3h. If current speed is y km/h and boat speed in still water is x km/h, find x.", "12", None, "short"),
        ("Sarah has $2 and $5 notes totaling $56. She has 16 notes in total. How many $5 notes does she have?", ["8", "9", "7", "10"], 0, "mcq"),
        ("Two pipes can fill a pool: Pipe A fills in x hours, Pipe B in y hours. Together they fill in 6 hours. If A is twice as fast as B, find x.", ["9", "12", "8", "10"], 0, "mcq"),
        ("In a number, tens digit is x and units digit is y. The number is 27 more than the number with reversed digits. Also, x + y = 9. Find the original number.", ["63", "72", "54", "81"], 0, "mcq")
    ],

    "algebraic-manipulation-sec2": [
        # Easy
        ("Expand and simplify: (x + 5)(x - 3)", ["x² + 2x - 15", "x² - 15", "x² + 8x - 15", "x² - 8x - 15"], 0, "mcq"),
        ("Factorize completely: 2x² + 8x", ["2x(x + 4)", "x(2x + 8)", "2(x² + 4x)", "(2x)(x + 4)"], 0, "mcq"),
        ("Expand: (2x - 3)²", "4x² - 12x + 9", None, "short"),
        ("Factorize: x² - 7x + 12", ["(x - 3)(x - 4)", "(x - 2)(x - 6)", "(x - 1)(x - 12)", "(x + 3)(x + 4)"], 0, "mcq"),
        ("Simplify: 3(2x - 1) - 2(x + 4)", ["4x - 11", "4x - 5", "6x - 11", "4x + 5"], 0, "mcq"),

        # Medium
        ("Gardens by the Bay flower bed: length (2x+3)m, width (x+4)m. Find area in expanded form.", ["2x² + 11x + 12", "2x² + 8x + 12", "2x² + 7x + 12", "3x² + 11x + 12"], 0, "mcq"),
        ("Factorize: 3x² - 27", ["3(x - 3)(x + 3)", "3(x² - 9)", "(3x - 9)(x + 3)", "3x(x - 9)"], 0, "mcq"),
        ("Expand and simplify: (x + 2)(x - 5) + (x + 3)(x - 1)", "2x² - 2x - 13", None, "short"),
        ("If (x + a)² = x² + 10x + 25, find a.", ["5", "10", "25", "-5"], 0, "mcq"),
        ("Factorize: 4x² - 9y²", ["(2x - 3y)(2x + 3y)", "(4x - 9y)(x + y)", "4(x - y)(x + y)", "(2x)² - (3y)²"], 0, "mcq"),

        # Hard
        ("HDB flat area formula: A = (x + 5)(x + 8) - x². Simplify to find A in terms of x.", ["13x + 40", "x² + 13x + 40", "13x", "40"], 0, "mcq"),
        ("Expand: (2x + 1)(x - 3)(x + 2)", "2x³ - 5x² - 7x - 6", None, "short"),
        ("If x² - y² = 20 and x - y = 4, find x + y.", ["5", "4", "10", "16"], 0, "mcq"),
        ("Factorize completely: 12x² - 27", ["3(2x - 3)(2x + 3)", "3(4x² - 9)", "12(x - 3)(x + 3)", "(6x - 9)(2x + 3)"], 0, "mcq"),
        ("Swimming pool: volume V = x(x + 4)(2x - 1). When expanded, coefficient of x² term is:", ["7", "8", "6", "9"], 0, "mcq")
    ],

    "quadratic-expressions-sec2": [
        # Easy
        ("Which is NOT a quadratic expression?", ["3x + 5", "x² - 1", "2x² + x", "-x²"], 0, "mcq"),
        ("Factorize: x² + 9x + 20", ["(x + 4)(x + 5)", "(x + 2)(x + 10)", "(x + 1)(x + 20)", "(x + 9)(x + 20)"], 0, "mcq"),
        ("In 5x² - 3x + 7, what is the constant term?", "7", None, "short"),
        ("Expand: (x - 7)²", ["x² - 14x + 49", "x² + 49", "x² - 7x + 49", "x² - 14x"], 0, "mcq"),
        ("Factorize: x² - 25", ["(x - 5)(x + 5)", "(x - 25)(x + 1)", "x(x - 25)", "(x - 5)²"], 0, "mcq"),

        # Medium
        ("Factorize: 2x² + 11x + 12", ["(2x + 3)(x + 4)", "(2x + 4)(x + 3)", "(x + 3)(x + 4)", "2(x² + 11x + 12)"], 0, "mcq"),
        ("A square has side (x + 3)cm. If area is 64 cm², find x.", ["5", "8", "11", "4"], 0, "mcq"),
        ("Expand: (3x + 2)² - 4", "9x² + 12x", None, "short"),
        ("If x² + bx + 36 = (x + 6)², find b.", ["12", "6", "36", "18"], 0, "mcq"),
        ("Factorize: x² - 2x - 15", ["(x - 5)(x + 3)", "(x - 3)(x + 5)", "(x - 15)(x + 1)", "(x - 1)(x + 15)"], 0, "mcq"),

        # Hard
        ("HDB carpark lot: Area = (3x² + 14x - 5) m². Which are possible dimensions?", ["(3x - 1)(x + 5)", "(3x + 1)(x - 5)", "(x + 5)(3x + 1)", "(3x + 5)(x - 1)"], 0, "mcq"),
        ("If x² - 6x + k is a perfect square, find k.", ["9", "6", "12", "36"], 0, "mcq"),
        ("Factorize: 6x² - x - 2", "(3x - 2)(2x + 1)", None, "short"),
        ("Rectangle area: (2x² + 5x - 3). If width is (2x - 1), find length.", ["x + 3", "x - 3", "2x + 3", "x + 2"], 0, "mcq"),
        ("Expand: (x + a)(x - a) + (x + b)(x + b). If result is 2x² + 6x + 9, find b.", ["3", "9", "6", "-3"], 0, "mcq")
    ],

    "functions-graphs-sec2": [
        # Easy
        ("For y = 3x - 4, find gradient.", "3", None, "short"),
        ("Which point lies on line y = 2x + 1?", ["(3, 7)", "(3, 6)", "(2, 6)", "(4, 7)"], 0, "mcq"),
        ("Y-intercept of y = -2x + 5:", ["5", "-2", "0", "2.5"], 0, "mcq"),
        ("Line y = -3 is:", ["horizontal", "vertical", "diagonal rising", "diagonal falling"], 0, "mcq"),
        ("If f(x) = 3x - 2, find f(4).", ["10", "14", "12", "8"], 0, "mcq"),

        # Medium
        ("MRT fare: F = 0.83 + 0.072d (d = distance in km). What is fare increase per km?", ["$0.072", "$0.83", "$0.902", "$0.10"], 0, "mcq"),
        ("Line passing through (2,5) and (4,11) has gradient:", ["3", "2", "6", "1.5"], 0, "mcq"),
        ("Perpendicular to y = 4x + 1 has gradient:", ["-1/4", "4", "-4", "1/4"], 0, "mcq"),
        ("If f(x) = 2x + k and f(3) = 11, find k.", "5", None, "short"),
        ("Two lines y = 2x + 3 and y = 2x - 1 are:", ["parallel", "perpendicular", "intersecting", "same line"], 0, "mcq"),

        # Hard
        ("Taxi fare: Basic $3.20, then $0.22 per 400m. Express as F = mx + c for distance x km.", ["F = 0.55x + 3.20", "F = 0.22x + 3.20", "F = 220x + 3.20", "F = 0.55x"], 0, "mcq"),
        ("Line passes through (1, 5) and has gradient -2. Find y-intercept.", ["7", "5", "3", "-2"], 0, "mcq"),
        ("If f(x) = ax + b, f(2) = 7 and f(5) = 16, find a.", "3", None, "short"),
        ("Two lines 2x + 3y = 12 and kx - 2y = 8 are perpendicular. Find k.", ["3", "-3", "2", "4"], 0, "mcq"),
        ("Water tank drains at constant rate. After 5min: 120L, after 12min: 78L. When empty?", ["20 min", "15 min", "25 min", "18 min"], 0, "mcq")
    ],

    "inequalities-sec2": [
        # Easy
        ("Solve: 2x + 5 > 13", ["x > 4", "x < 4", "x ≥ 4", "x ≤ 4"], 0, "mcq"),
        ("Solve: 5 - x ≤ 2", "x ≥ 3", None, "short"),
        ("Which satisfies x ≤ -2?", ["-3", "-2", "0", "1"], 0, "mcq"),
        ("Solve: 3x - 7 < 8", ["x < 5", "x > 5", "x ≤ 5", "x = 5"], 0, "mcq"),
        ("'More than 10' expressed as:", ["x > 10", "x ≥ 10", "x < 10", "x ≤ 10"], 0, "mcq"),

        # Medium
        ("Solve: 2(3x - 1) ≥ 4x + 6", ["x ≥ 4", "x ≤ 4", "x > 4", "x = 4"], 0, "mcq"),
        ("MRT can carry maximum 1800 passengers. Express as inequality (p = passengers).", ["p ≤ 1800", "p < 1800", "p ≥ 1800", "p = 1800"], 0, "mcq"),
        ("Solve: -3x + 5 > 14", "x < -3", None, "short"),
        ("If 2x + 3 < 11, largest integer value of x:", ["3", "4", "5", "2"], 0, "mcq"),
        ("Solve: 4 < 2x + 1 ≤ 9", ["1.5 < x ≤ 4", "2 < x ≤ 5", "3 < x ≤ 8", "1 < x ≤ 3"], 0, "mcq"),

        # Hard
        ("Student needs average ≥ 75 for 5 tests. First 4 scores: 72, 80, 68, 78. Minimum for test 5?", ["77", "75", "80", "70"], 0, "mcq"),
        ("Rental: $50 + $8 per hour. Budget ≤ $130. Maximum hours?", ["10", "9", "11", "8"], 0, "mcq"),
        ("Solve: 3(x - 2) - 2(x + 1) ≥ 5", "x ≥ 13", None, "short"),
        ("x must satisfy both x + 5 > 12 AND 2x - 3 < 21. Find range.", ["7 < x < 12", "7 ≤ x ≤ 12", "x > 7", "x < 12"], 0, "mcq"),
        ("Phone plan: $30 + $0.10 per min. Other plan: $20 + $0.15 per min. First plan cheaper when minutes x:", ["x > 200", "x < 200", "x ≥ 200", "x ≤ 200"], 0, "mcq")
    ],

    "indices-sec2": [
        # Easy
        ("Simplify: a⁴ × a³", "a⁷", None, "short"),
        ("What is 7⁰?", ["1", "0", "7", "undefined"], 0, "mcq"),
        ("Simplify: (m²)⁵", ["m¹⁰", "m⁷", "m³²", "2m⁵"], 0, "mcq"),
        ("Evaluate: 2⁵", ["32", "10", "25", "64"], 0, "mcq"),
        ("Simplify: x⁸ ÷ x³", ["x⁵", "x¹¹", "x²⁴", "x"], 0, "mcq"),

        # Medium
        ("Simplify: (3x²y)³", ["27x⁶y³", "9x⁶y³", "3x⁶y³", "27x⁵y³"], 0, "mcq"),
        ("Bacteria doubles every hour. After 6 hours, multiplied by:", ["64", "12", "36", "128"], 0, "mcq"),
        ("Express 1/(8x³) using negative indices:", "8⁻¹x⁻³", None, "short"),
        ("Simplify: (2⁴ × 2³) ÷ 2⁵", ["4", "2", "8", "16"], 0, "mcq"),
        ("If 3ˣ = 27, find x.", ["3", "9", "27", "2"], 0, "mcq"),

        # Hard
        ("Singapore population grows 2% annually. After n years, multiplied by (1.02)ⁿ. After 10 years, factor is approximately:", ["1.22", "1.20", "2.0", "1.10"], 0, "mcq"),
        ("Simplify: (x²y³)⁴ ÷ (x³y²)²", ["x²y⁸", "x⁸y¹²", "x⁸y⁸", "y⁸"], 0, "mcq"),
        ("If 2ˣ × 4ʸ = 128, and x = y, find x.", "3", None, "short"),
        ("Evaluate: (27)^(2/3)", ["9", "18", "3", "27"], 0, "mcq"),
        ("Simplify: (8a⁶b³) ÷ (2a²b)", ["4a⁴b²", "4a³b²", "6a⁴b²", "4a⁸b⁴"], 0, "mcq")
    ],

    "congruence-similarity-sec2": [
        # Easy
        ("Two triangles with all sides equal are:", ["congruent", "similar", "neither", "both"], 0, "mcq"),
        ("Which is a valid congruence test?", ["SAS", "AAA", "SSA", "AA"], 0, "mcq"),
        ("Similar triangles have:", "same angles", None, "short"),
        ("If △ABC ≅ △DEF by SSS, and AB = 5cm, then DE =", ["5cm", "10cm", "2.5cm", "cannot determine"], 0, "mcq"),
        ("Scale factor 3 means area multiplied by:", ["9", "3", "6", "27"], 0, "mcq"),

        # Medium
        ("Two triangles: sides 6,8,10 and 9,12,15. They are:", ["similar with scale 2:3", "congruent", "similar with scale 3:2", "neither"], 0, "mcq"),
        ("In △ABC, ∠A=50°, ∠B=60°. In △DEF, ∠D=50°, ∠E=60°, ∠F=70°. Triangles are:", ["similar (AAA)", "congruent", "neither", "similar (SAS)"], 0, "mcq"),
        ("If triangles are similar with scale 1:4, perimeter ratio is:", "1:4", None, "short"),
        ("MRT map scale 1:10000. Two stations 3cm apart on map. Actual distance:", ["300m", "3000m", "30m", "3m"], 0, "mcq"),
        ("Triangle PQR ≅ Triangle XYZ. If PQ=7, QR=9, PR=11, find XZ.", ["11", "7", "9", "27"], 0, "mcq"),

        # Hard
        ("HDB floor plan scale 1:50. Room area on plan is 24 cm². Actual room area:", ["60 m²", "12 m²", "120 m²", "6 m²"], 0, "mcq"),
        ("Two similar triangles have areas 16 cm² and 64 cm². If smaller has perimeter 20cm, larger has perimeter:", ["40cm", "80cm", "60cm", "30cm"], 0, "mcq"),
        ("Prove △ABC ≅ △DEF. Given: AB=DE, AC=DF, BC=EF. Which test?", "SSS", None, "short"),
        ("Shadow problem: 1.5m pole casts 2m shadow. How tall is tree casting 8m shadow?", ["6m", "10.67m", "12m", "5.33m"], 0, "mcq"),
        ("If two similar triangles have sides ratio 3:5, their volumes ratio (if extended to pyramids) would be:", ["27:125", "3:5", "9:25", "6:10"], 0, "mcq")
    ],

    "pythagoras-theorem-sec2": [
        # Easy
        ("Right triangle: legs 6, 8. Hypotenuse:", "10", None, "short"),
        ("Which forms right triangle?", ["8,15,17", "4,5,6", "7,8,9", "10,11,12"], 0, "mcq"),
        ("If c²=a²+b², c is the:", ["hypotenuse", "shorter leg", "longer leg", "base"], 0, "mcq"),
        ("Find missing side: a=5, c=13, b=?", ["12", "8", "18", "14"], 0, "mcq"),
        ("Diagonal of square side 5cm:", ["5√2 cm", "10cm", "25cm", "5cm"], 0, "mcq"),

        # Medium
        ("Ladder 10m long leans against wall, base 6m from wall. How high up wall?", ["8m", "4m", "16m", "7m"], 0, "mcq"),
        ("Rectangle 9cm by 12cm. Diagonal length:", ["15cm", "21cm", "18cm", "10.5cm"], 0, "mcq"),
        ("Is triangle with sides 7, 24, 25 a right triangle?", "yes", None, "short"),
        ("HDB room floor is 4m by 3m. Cable from one corner to opposite corner:", ["5m", "7m", "12m", "3.5m"], 0, "mcq"),
        ("Isosceles right triangle has legs x. If hypotenuse is 10√2, find x.", ["10", "20", "5√2", "14.14"], 0, "mcq"),

        # Hard
        ("Gardens by the Bay pathway: Walk 120m north, then 160m east. Direct distance from start:", ["200m", "280m", "140m", "180m"], 0, "mcq"),
        ("Equilateral triangle side 6cm. Find height.", ["3√3 cm", "6√3 cm", "3cm", "6cm"], 0, "mcq"),
        ("Ship sails 15km east then 20km north. How far from starting point?", "25 km", None, "short"),
        ("Rectangular box: 6cm × 8cm × 24cm. Length of longest diagonal:", ["26cm", "30cm", "25cm", "28cm"], 0, "mcq"),
        ("Coordinate geometry: Distance from (2,3) to (8,11):", ["10", "14", "6", "8"], 0, "mcq")
    ],

    "circle-properties-sec2": [
        # Easy
        ("Circumference formula (diameter d):", "πd", None, "short"),
        ("Area of circle radius 10cm (use π=3.14):", ["314 cm²", "628 cm²", "62.8 cm²", "31.4 cm²"], 0, "mcq"),
        ("If diameter = 14cm, radius =", ["7cm", "28cm", "14cm", "3.5cm"], 0, "mcq"),
        ("Angle in semicircle is always:", ["90°", "180°", "45°", "60°"], 0, "mcq"),
        ("Radius of circle with circumference 44cm (π=22/7):", ["7cm", "14cm", "22cm", "11cm"], 0, "mcq"),

        # Medium
        ("Singapore Flyer radius 75m. One complete rotation distance:", ["150π m", "75π m", "225π m", "300π m"], 0, "mcq"),
        ("Circle area 154 cm² (π=22/7). Find radius.", ["7cm", "14cm", "49cm", "11cm"], 0, "mcq"),
        ("Arc length: radius 7cm, angle 60°. Arc length (π=22/7):", "7.33 cm", None, "short"),
        ("Sector area: r=10cm, angle=90°. Area (π=3.14):", ["78.5 cm²", "314 cm²", "157 cm²", "39.25 cm²"], 0, "mcq"),
        ("Tangent to circle makes what angle with radius at contact point?", ["90°", "180°", "45°", "0°"], 0, "mcq"),

        # Hard
        ("Circular pond radius 7m surrounded by path width 2m. Path area (π=22/7):", ["176 m²", "154 m²", "254 m²", "78 m²"], 0, "mcq"),
        ("Two circles touch externally. Radii 5cm and 3cm. Distance between centers:", ["8cm", "5cm", "2cm", "15cm"], 0, "mcq"),
        ("Wheel diameter 70cm. How many revolutions to travel 110m? (π=22/7)", "50", None, "short"),
        ("Annulus (ring): outer radius 10cm, inner radius 6cm. Area (π=3.14):", ["200.96 cm²", "314 cm²", "113.04 cm²", "87.92 cm²"], 0, "mcq"),
        ("Arc AB subtends 120° at center. Radius 6cm. Find length of chord AB (π=22/7):", ["6√3 cm", "12cm", "6cm", "4π cm"], 0, "mcq")
    ],

    "mensuration-2d-sec2": [
        # Easy
        ("Rectangle: length 12m, width 5m. Area:", "60 m²", None, "short"),
        ("Triangle: base 8cm, height 5cm. Area:", ["20 cm²", "40 cm²", "13 cm²", "10 cm²"], 0, "mcq"),
        ("Square perimeter 36cm. Side length:", ["9cm", "36cm", "18cm", "4cm"], 0, "mcq"),
        ("Parallelogram: base 10m, height 6m. Area:", ["60 m²", "16 m²", "30 m²", "100 m²"], 0, "mcq"),
        ("Trapezium: parallel sides 8,12; height 5. Area:", ["50", "100", "60", "40"], 0, "mcq"),

        # Medium
        ("HDB room: 5m × 4m. Tiles are 25cm × 25cm. How many tiles needed?", ["320", "80", "160", "640"], 0, "mcq"),
        ("Rhombus: diagonals 12cm and 16cm. Area:", ["96 cm²", "192 cm²", "28 cm²", "48 cm²"], 0, "mcq"),
        ("Path around rectangular garden 20m × 15m. Path width 2m. Path area:", "156 m²", None, "short"),
        ("Composite: rectangle 10×8 with semicircle on 8cm side. Total area (π=3.14):", ["105.12 cm²", "80 cm²", "130.24 cm²", "100 cm²"], 0, "mcq"),
        ("Triangle ABC: base 10cm. If area is 60 cm², find height.", ["12cm", "6cm", "120cm", "5cm"], 0, "mcq"),

        # Hard
        ("School hall: 30m × 20m. Stage at one end 30m × 5m. Remaining floor area for chairs:", ["500 m²", "600 m²", "450 m²", "550 m²"], 0, "mcq"),
        ("Circular garden radius 14m. Square path around it. If path width 3m, find path area (π=22/7):", ["708 m²", "616 m²", "924 m²", "308 m²"], 0, "mcq"),
        ("Painting walls of room 6m × 4m × 3m high. One door 2m × 1m, two windows each 1.5m × 1m. Paintable area:", "54 m²", None, "short"),
        ("Equilateral triangle side 10cm. Area (use √3=1.732):", ["43.3 cm²", "50 cm²", "86.6 cm²", "25 cm²"], 0, "mcq"),
        ("Regular hexagon side 6cm. Area (hexagon = 6 equilateral triangles, √3=1.732):", ["93.5 cm²", "187 cm²", "108 cm²", "156 cm²"], 0, "mcq")
    ],

    "mensuration-3d-sec2": [
        # Easy
        ("Cube edge 4cm. Volume:", "64 cm³", None, "short"),
        ("Cuboid: 5cm × 3cm × 2cm. Volume:", ["30 cm³", "10 cm³", "15 cm³", "60 cm³"], 0, "mcq"),
        ("Cube edge 3cm. Surface area:", ["54 cm²", "27 cm²", "18 cm²", "9 cm²"], 0, "mcq"),
        ("Cylinder: radius 7cm, height 10cm. Volume (π=22/7):", ["1540 cm³", "440 cm³", "770 cm³", "220 cm³"], 0, "mcq"),
        ("Triangular prism: base area 20 cm², length 15cm. Volume:", ["300 cm³", "35 cm³", "150 cm³", "200 cm³"], 0, "mcq"),

        # Medium
        ("HDB water tank: cylinder radius 3m, height 8m. Capacity in liters (π=3.14, 1m³=1000L):", ["226080 L", "75360 L", "24 L", "226 L"], 0, "mcq"),
        ("Cuboid surface area: 4cm × 5cm × 6cm:", ["148 cm²", "120 cm²", "74 cm²", "180 cm²"], 0, "mcq"),
        ("If cube edge triples, volume multiplied by:", "27", None, "short"),
        ("Cylinder: curved surface area only. r=7cm, h=15cm (π=22/7):", ["660 cm²", "330 cm²", "154 cm²", "462 cm²"], 0, "mcq"),
        ("Cone: radius 6cm, height 8cm. Volume (π=3.14):", ["301.44 cm³", "904.32 cm³", "150.72 cm³", "452.16 cm³"], 0, "mcq"),

        # Hard
        ("Swimming pool: 25m × 10m × 2m deep. Water fills to 1.8m. Volume of water:", ["450 m³", "500 m³", "250 m³", "900 m³"], 0, "mcq"),
        ("Sphere radius 21cm. Surface area (π=22/7):", ["5544 cm²", "2772 cm²", "1386 cm²", "11088 cm²"], 0, "mcq"),
        ("Cylindrical tank diameter 2.8m, height 5m. Paint cost $8/m². Total paint cost for curved surface only (π=22/7):", "352", None, "short"),
        ("Pyramid: square base 10m × 10m, height 12m. Volume:", ["400 m³", "1200 m³", "100 m³", "800 m³"], 0, "mcq"),
        ("Hemisphere radius 7cm on top of cylinder radius 7cm height 10cm. Total volume (π=22/7):", ["2257.33 cm³", "1540 cm³", "718.67 cm³", "3080 cm³"], 0, "mcq")
    ],

    "data-analysis-sec2": [
        # Easy
        ("Data: 12, 15, 18, 15, 20. Find mode.", "15", None, "short"),
        ("Mean of 4, 6, 8, 10, 12:", ["8", "10", "6", "40"], 0, "mcq"),
        ("Median of 3, 7, 5, 9, 11:", ["7", "5", "9", "6"], 0, "mcq"),
        ("Range of 25, 30, 35, 40, 45:", ["20", "45", "25", "35"], 0, "mcq"),
        ("Data: 2, 2, 3, 4, 4, 4, 5. Mode:", ["4", "3", "2", "5"], 0, "mcq"),

        # Medium
        ("Test scores: 65, 70, 75, 80, 95. Which best represents typical score?", ["Median (75)", "Mean (77)", "Mode", "Range"], 0, "mcq"),
        ("Singapore temperature (°C): 28, 30, 32, 29, 31, 30, 29. Find mean.", ["29.86", "30", "31", "28"], 0, "mcq"),
        ("Data: 10, 12, 14, x, 18, 20. If mean is 15, find x.", "16", None, "short"),
        ("Which graph best shows trend over time?", ["Line graph", "Bar chart", "Pie chart", "Pictogram"], 0, "mcq"),
        ("Five numbers have mean 20. Sum of the five numbers:", ["100", "20", "5", "25"], 0, "mcq"),

        # Hard
        ("Class test: 8 students average 72, another 12 students average 68. Overall class average:", ["69.6", "70", "68", "72"], 0, "mcq"),
        ("Box plot shows: Q1=40, Q2=55, Q3=70. Interquartile range:", ["30", "55", "15", "40"], 0, "mcq"),
        ("MRT ridership (millions): Mon 2.1, Tue 2.3, Wed 2.2, Thu 2.4, Fri 2.5. Standard deviation approximately:", "0.14", None, "short"),
        ("Frequency table: 5 appears 3 times, 10 appears 2 times, 15 appears 5 times. Median:", ["15", "10", "12.5", "11"], 0, "mcq"),
        ("Two data sets: A has mean 50, SD 5. B has mean 50, SD 12. Which is more consistent?", ["A", "B", "Same", "Cannot tell"], 0, "mcq")
    ],

    "probability-sec2": [
        # Easy
        ("Fair die rolled. P(6):", "1/6", None, "short"),
        ("Coin flipped. P(tails):", ["1/2", "1", "0", "2/3"], 0, "mcq"),
        ("Bag: 4 red, 6 blue balls. P(blue):", ["3/5", "2/5", "1/2", "6/10"], 0, "mcq"),
        ("P(certain event):", ["1", "0", "1/2", "100"], 0, "mcq"),
        ("If P(A) = 0.7, find P(not A).", ["0.3", "0.7", "1", "0"], 0, "mcq"),

        # Medium
        ("Two dice rolled. P(sum = 7):", ["1/6", "1/12", "1/36", "7/36"], 0, "mcq"),
        ("Singapore 4D: 10,000 numbers. P(winning with 2 specific numbers):", ["1/5000", "2/10000", "1/10000", "2/5000"], 0, "mcq"),
        ("Spinner: sectors 1,2,2,3,3,3,4,4. P(odd number):", "1/2", None, "short"),
        ("Card drawn from 52 cards. P(heart or king):", ["4/13", "1/4", "17/52", "1/13"], 0, "mcq"),
        ("Two coins flipped. P(at least 1 head):", ["3/4", "1/2", "1/4", "1"], 0, "mcq"),

        # Hard
        ("Bag: 5 red, 3 blue balls. Draw 2 without replacement. P(both red):", ["5/14", "25/64", "10/28", "1/4"], 0, "mcq"),
        ("Weather: P(rain Mon)=0.3, P(rain Tue)=0.4. If independent, P(rain both days):", ["0.12", "0.7", "0.35", "0.24"], 0, "mcq"),
        ("Box: 60% chocolates, 40% candies. Of chocolates, 30% are dark. P(dark chocolate):", "0.18", None, "short"),
        ("Three children born. P(exactly 2 girls)?", ["3/8", "1/2", "1/4", "1/8"], 0, "mcq"),
        ("Lottery: 1st draw from 50 numbers, 2nd from remaining 49. P(specific 2 numbers in order):", ["1/2450", "1/50", "2/50", "1/49"], 0, "mcq")
    ],

    "sets-venn-diagrams-sec2": [
        # Easy
        ("A = {2,4,6}, B = {4,6,8}. Find A ∩ B.", "{4,6}", None, "short"),
        ("Empty set symbol:", ["∅", "0", "{ }", "null"], 0, "mcq"),
        ("A ∪ B means:", ["union (all elements)", "intersection", "difference", "complement"], 0, "mcq"),
        ("If A = {1,2} and B = {2,3}, A ∪ B =", ["{1,2,3}", "{2}", "{1,3}", "{1,2,2,3}"], 0, "mcq"),
        ("n({5,10,15,20}) =", ["4", "50", "20", "5"], 0, "mcq"),

        # Medium
        ("U = {1-10}, A = {2,4,6,8}, B = {3,6,9}. Find A ∩ B.", ["{6}", "{}", "{2,3,4,6,8,9}", "{2,4,8}"], 0, "mcq"),
        ("Students: 25 study Math, 18 study Science, 10 study both. How many study at least one?", ["33", "43", "35", "25"], 0, "mcq"),
        ("If U = {1-8}, A = {1,3,5,7}, find A'.", "{2,4,6,8}", None, "short"),
        ("A - B means:", ["elements in A but not B", "all elements", "elements in B but not A", "intersection"], 0, "mcq"),
        ("n(A ∪ B) = 50, n(A) = 30, n(B) = 35. Find n(A ∩ B).", ["15", "50", "85", "5"], 0, "mcq"),

        # Hard
        ("Class: 30 students. 18 play soccer, 15 play basketball, 8 play neither. How many play both?", ["11", "3", "7", "22"], 0, "mcq"),
        ("Survey: 100 people. 60 like tea, 50 like coffee, 20 like both. How many like neither?", ["10", "30", "40", "90"], 0, "mcq"),
        ("If A ⊂ B and B ⊂ C, then A ⊂ C. This demonstrates:", "transitivity", None, "short"),
        ("n(A ∪ B ∪ C) = 100, n(A)=40, n(B)=50, n(C)=45, n(A∩B)=15, n(B∩C)=20, n(A∩C)=10, n(A∩B∩C)=5. Verify using formula.", ["Correct", "Incorrect", "Need more info", "Cannot verify"], 0, "mcq"),
        ("Venn diagram: Region outside all sets but inside U represents:", ["(A ∪ B ∪ C)'", "A' ∩ B' ∩ C'", "Elements in none of the sets", "All of the above"], 3, "mcq")
    ]
}

print("Enhancing exercises to match Singapore MOE rigor...\n")

# Update chapters with enhanced exercises
for chapter in chapters:
    chapter_id = chapter["id"]
    if chapter_id in enhanced_exercises:
        exercises = []
        for q_num, q_data in enumerate(enhanced_exercises[chapter_id], 1):
            difficulty = "easy" if q_num <= 5 else ("medium" if q_num <= 10 else "hard")

            prompt, choices_or_answer, answer_or_none, q_type = q_data

            if q_type == "short":
                exercise = {
                    "id": f"{chapter_id.replace('-sec2', '')}-q{q_num}",
                    "type": "short",
                    "difficulty": difficulty,
                    "prompt": prompt,
                    "prompt_zh": f"[{chapter['title']} - 问题 {q_num}]",
                    "answer": choices_or_answer,
                    "validator": "exact",
                    "hint": "Use problem-solving heuristics: understand the problem, devise a plan, carry out the plan, look back.",
                    "hint_zh": "使用解题策略:理解问题,制定计划,执行计划,回顾检查。"
                }
            else:  # mcq
                exercise = {
                    "id": f"{chapter_id.replace('-sec2', '')}-q{q_num}",
                    "type": "mcq",
                    "difficulty": difficulty,
                    "prompt": prompt,
                    "prompt_zh": f"[{chapter['title']} - 问题 {q_num}]",
                    "choices": choices_or_answer,
                    "answer": answer_or_none,
                    "hint": "Apply mathematical reasoning and real-world context to solve.",
                    "hint_zh": "运用数学推理和实际情境来解决。"
                }

            exercises.append(exercise)

        chapter["exercises"] = exercises
        print(f"✓ {chapter['title']}: Enhanced with rigorous MOE-standard exercises")

# Save enhanced chapters
with open('chapters/math-sec2-chapters.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, indent=2, ensure_ascii=False)

print(f"\n✅ All exercises enhanced to Singapore MOE Secondary 2 standards!")
print(f"\n📊 Enhancement features:")
print(f"  • Multi-step problem solving")
print(f"  • Real-world Singapore context")
print(f"  • Heuristic-based questions")
print(f"  • Conceptual understanding focus")
print(f"  • Application and reasoning emphasis")
