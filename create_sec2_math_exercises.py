"""
Add detailed exercises to Secondary 2 Math chapters
15 exercises per chapter (5 easy, 5 medium, 5 hard)
Includes Singapore context where applicable
"""

import json

# Load existing chapters
with open('chapters/math-sec2-chapters.json', 'r', encoding='utf-8') as f:
    chapters = json.load(f)

# Exercise data for all 14 chapters
exercise_data = {
    # ALGEBRA CHAPTERS (1-6)

    "linear-equations-two-variables-sec2": [
        ("At a Singapore hawker center, 2 plates of chicken rice and 3 drinks cost $12. If 1 plate costs $2 more than a drink, what is the price of each?", ["Chicken rice: $4.50, Drink: $2.50", "Chicken rice: $4, Drink: $2", "Chicken rice: $5, Drink: $3", "Chicken rice: $4.50, Drink: $1.50"], 0, "mcq"),
        ("Solve: x + y = 8, x - y = 2", ["x=5, y=3", "x=3, y=5", "x=6, y=2", "x=4, y=4"], 0, "mcq"),
        ("Using substitution method, solve: y = 2x, x + y = 9", "x=3, y=6", None, "short"),
        ("2 MRT tickets and 3 bus tickets cost $10. 1 MRT ticket and 2 bus tickets cost $6. Find the cost of 1 MRT ticket.", ["$2.50", "$2", "$3", "$1.50"], 1, "mcq"),
        ("Solve by elimination: 2x + 3y = 13, x + 3y = 10", ["x=3, y=2.33", "x=2, y=3", "x=3, y=2", "x=4, y=1"], 0, "mcq"),
        ("A student bought 3 pens and 2 pencils for $8. Another bought 2 pens and 1 pencil for $5. How much is 1 pen?", ["$2", "$1.50", "$3", "$2.50"], 0, "mcq"),
        ("Graphically, simultaneous equations with one solution have lines that:", ["intersect at one point", "are parallel", "are the same line", "never meet"], 0, "mcq"),
        ("Solve: 3x - 2y = 4, 2x + y = 5", "x=2, y=1", None, "short"),
        ("If 2x + y = 7 and x - y = 2, find the value of x + y.", ["5", "6", "4", "3"], 0, "mcq"),
        ("Which method is best for: y = 3x - 1, 2x + y = 9?", ["Substitution", "Elimination", "Graphing", "All equal"], 0, "mcq"),
        ("A rectangle's perimeter is 30m. Length is 3m more than width. Find dimensions.", ["Length: 9m, Width: 6m", "Length: 10m, Width: 5m", "Length: 8m, Width: 7m", "Length: 12m, Width: 3m"], 0, "mcq"),
        ("Solve: 4x - 3y = 5, 2x - 3y = 1", ["x=2, y=1", "x=1, y=2", "x=3, y=7/3", "x=2, y=2"], 0, "mcq"),
        ("If simultaneous equations have no solution, their graphs are:", ["parallel lines", "intersecting lines", "the same line", "perpendicular lines"], 0, "mcq"),
        ("At Sentosa, family tickets cost $x and child tickets $y. 2 family + 3 child = $150. 1 family + 2 child = $85. Find x.", ["$45", "$40", "$50", "$35"], 0, "mcq"),
        ("Solve: 5x + 2y = 20, 3x - 2y = 4", ["x=3, y=2.5", "x=2, y=5", "x=4, y=0", "x=2.5, y=3"], 0, "mcq")
    ],

    "algebraic-manipulation-sec2": [
        ("Expand: (x + 3)(x + 5)", ["x² + 8x + 15", "x² + 15", "x² + 8x", "x² + 5x + 15"], 0, "mcq"),
        ("Factorize: x² + 7x + 12", ["(x + 3)(x + 4)", "(x + 2)(x + 6)", "(x + 1)(x + 12)", "(x + 3)(x + 5)"], 0, "mcq"),
        ("Expand: 3(2x - 5)", "6x - 15", None, "short"),
        ("Simplify: (2x + 3) - (x - 4)", ["x + 7", "x - 1", "3x + 7", "x + 1"], 0, "mcq"),
        ("Factorize: 4x + 8", ["4(x + 2)", "2(2x + 4)", "x(4 + 8)", "4x(1 + 2)"], 0, "mcq"),
        ("Expand: (x - 2)(x + 2)", ["x² - 4", "x² + 4", "x² - 2x - 4", "x²"], 0, "mcq"),
        ("Factorize: x² - 9", ["(x - 3)(x + 3)", "(x - 9)(x + 1)", "x(x - 9)", "(x - 3)²"], 0, "mcq"),
        ("Expand and simplify: 2(x + 3) + 3(x - 1)", "5x + 3", None, "short"),
        ("Factorize: x² + 5x", ["x(x + 5)", "(x + 1)(x + 5)", "x(5)", "5x(x + 1)"], 0, "mcq"),
        ("Expand: (2x + 1)(x - 3)", ["2x² - 5x - 3", "2x² - 6x - 3", "2x² + x - 3", "2x² - 3"], 0, "mcq"),
        ("Factorize completely: 3x² + 6x", ["3x(x + 2)", "x(3x + 6)", "3(x² + 2x)", "(3x)(x + 2)"], 0, "mcq"),
        ("Expand: (x + 4)²", ["x² + 8x + 16", "x² + 16", "x² + 4x + 16", "x² + 8x"], 0, "mcq"),
        ("Factorize: x² - 6x + 9", ["(x - 3)²", "(x - 3)(x + 3)", "(x - 9)(x + 1)", "x(x - 6) + 9"], 0, "mcq"),
        ("At Gardens by the Bay, a rectangular garden has area (x² + 7x + 12) m². What are possible dimensions?", ["(x + 3)m × (x + 4)m", "(x + 2)m × (x + 6)m", "(x + 1)m × (x + 12)m", "x m × (x + 7)m"], 0, "mcq"),
        ("Expand: (3x - 2)(2x + 5)", ["6x² + 11x - 10", "6x² - 10", "6x² + 15x - 10", "6x² - 4x - 10"], 0, "mcq")
    ],

    "quadratic-expressions-sec2": [
        ("Which is a quadratic expression?", ["x² + 3x + 2", "3x + 2", "x³ + x", "5"], 0, "mcq"),
        ("What is the coefficient of x² in 3x² - 5x + 7?", "3", None, "short"),
        ("Factorize: x² + 6x + 8", ["(x + 2)(x + 4)", "(x + 1)(x + 8)", "(x + 3)(x + 5)", "(x + 4)²"], 0, "mcq"),
        ("The constant term in 2x² - 3x + 5 is:", ["5", "2", "-3", "0"], 0, "mcq"),
        ("Factorize: x² - 5x + 6", ["(x - 2)(x - 3)", "(x - 1)(x - 6)", "(x + 2)(x + 3)", "(x - 5)(x + 1)"], 0, "mcq"),
        ("Expand: (x + 3)² - 4", ["x² + 6x + 5", "x² + 6x + 13", "x² + 3x + 5", "x² + 9"], 0, "mcq"),
        ("Factorize: x² - 16", ["(x - 4)(x + 4)", "(x - 8)(x + 2)", "(x - 16)(x + 1)", "x(x - 16)"], 0, "mcq"),
        ("What is the coefficient of x in x² - 7x + 10?", "-7", None, "short"),
        ("Factorize: 2x² + 7x + 3", ["(2x + 1)(x + 3)", "(2x + 3)(x + 1)", "(x + 1)(x + 3)", "2(x² + 7x + 3)"], 0, "mcq"),
        ("Expand: (x - 5)²", ["x² - 10x + 25", "x² + 25", "x² - 5x + 25", "x² - 10x"], 0, "mcq"),
        ("HDB flat area formula: A = x² + 12x + 35. Factorized form?", ["(x + 5)(x + 7)", "(x + 1)(x + 35)", "(x + 12)(x + 35)", "x(x + 12) + 35"], 0, "mcq"),
        ("Factorize: x² + x - 12", ["(x + 4)(x - 3)", "(x + 3)(x - 4)", "(x + 6)(x - 2)", "(x + 1)(x - 12)"], 0, "mcq"),
        ("The general form of a quadratic expression is:", ["ax² + bx + c", "ax + b", "ax³ + bx² + c", "a + bx + cx²"], 0, "mcq"),
        ("Factorize: 3x² - 12", ["3(x - 2)(x + 2)", "3(x² - 4)", "(3x - 6)(x + 2)", "3x(x - 4)"], 0, "mcq"),
        ("Expand: (2x + 3)(2x - 3)", ["4x² - 9", "4x² + 9", "4x² - 12x - 9", "2x² - 9"], 0, "mcq")
    ],

    "functions-graphs-sec2": [
        ("In y = 2x + 3, what is the gradient?", "2", None, "short"),
        ("Which point lies on y = x + 1?", ["(2, 3)", "(2, 4)", "(1, 3)", "(0, 2)"], 0, "mcq"),
        ("The y-intercept of y = 3x - 5 is:", ["-5", "3", "5", "0"], 0, "mcq"),
        ("Graph of y = 5 is a:", ["horizontal line", "vertical line", "diagonal line", "curve"], 0, "mcq"),
        ("If f(x) = 2x + 1, find f(3).", "7", None, "short"),
        ("Line parallel to y = 4x + 2 has gradient:", ["4", "2", "-4", "1/4"], 0, "mcq"),
        ("Singapore MRT Green Line fare: F = 0.8x + 0.77 (x = distance in km). What is the base fare?", ["$0.77", "$0.80", "$1.57", "$1"], 0, "mcq"),
        ("In y = mx + c, what does m represent?", ["gradient", "y-intercept", "x-intercept", "constant"], 0, "mcq"),
        ("Which is steeper: y = 3x + 1 or y = 2x + 5?", ["y = 3x + 1", "y = 2x + 5", "same", "cannot tell"], 0, "mcq"),
        ("Graph of x = -2 is a:", ["vertical line", "horizontal line", "diagonal line", "curve"], 0, "mcq"),
        ("If f(x) = x² - 1, find f(2).", "3", None, "short"),
        ("Two lines intersect if they have:", ["different gradients", "same gradient", "same y-intercept", "no relationship"], 0, "mcq"),
        ("Line perpendicular to y = 2x has gradient:", ["-1/2", "2", "-2", "1/2"], 0, "mcq"),
        ("In function notation, f(0) gives:", ["y-intercept", "x-intercept", "gradient", "maximum"], 0, "mcq"),
        ("Which line passes through origin?", ["y = 3x", "y = 3x + 1", "y = 3", "x = 0"], 0, "mcq")
    ],

    "linear-inequalities-sec2": [
        ("Solve: x + 3 > 7", ["x > 4", "x < 4", "x ≥ 4", "x ≤ 4"], 0, "mcq"),
        ("Solve: 2x ≤ 10", "x ≤ 5", None, "short"),
        ("Which value satisfies x < 3?", ["2", "3", "4", "3.5"], 0, "mcq"),
        ("Solve: x - 5 ≥ 2", ["x ≥ 7", "x ≤ 7", "x > 7", "x = 7"], 0, "mcq"),
        ("Solve: 3x < 12", ["x < 4", "x > 4", "x ≤ 4", "x = 4"], 0, "mcq"),
        ("When dividing inequality by negative number:", ["reverse the sign", "keep the sign", "add to both sides", "multiply both sides"], 0, "mcq"),
        ("Solve: -2x > 6", ["x < -3", "x > -3", "x < 3", "x > 3"], 0, "mcq"),
        ("Solve: 5x + 2 ≤ 17", "x ≤ 3", None, "short"),
        ("Which represents 'at least 5'?", ["x ≥ 5", "x > 5", "x ≤ 5", "x < 5"], 0, "mcq"),
        ("Solve: 4 - x < 1", ["x > 3", "x < 3", "x ≥ 3", "x = 3"], 0, "mcq"),
        ("Bus can carry at most 50 people: x ___", ["x ≤ 50", "x < 50", "x ≥ 50", "x = 50"], 0, "mcq"),
        ("Solve: 2x + 3 > 11", ["x > 4", "x < 4", "x ≥ 4", "x = 4"], 0, "mcq"),
        ("Temperature in Singapore stays above 20°C. Represent as:", ["T > 20", "T < 20", "T = 20", "T ≥ 20"], 0, "mcq"),
        ("Solve: 3(x - 2) ≥ 9", ["x ≥ 5", "x ≤ 5", "x > 5", "x = 5"], 0, "mcq"),
        ("Which is NOT a solution to x ≤ 4?", ["5", "4", "3", "0"], 0, "mcq")
    ],

    "indices-sec2": [
        ("Simplify: x³ × x²", ["x⁵", "x⁶", "x", "x⁹"], 0, "mcq"),
        ("What is x⁰?", "1", None, "short"),
        ("Simplify: (x²)³", ["x⁶", "x⁵", "x⁸", "x⁹"], 0, "mcq"),
        ("2³ × 2² = ", ["2⁵", "2⁶", "2", "4⁵"], 0, "mcq"),
        ("Simplify: x⁵ ÷ x²", ["x³", "x⁷", "x¹⁰", "x"], 0, "mcq"),
        ("What is 5²?", "25", None, "short"),
        ("Simplify: (2x)³", ["8x³", "2x³", "6x³", "x³"], 0, "mcq"),
        ("2⁻² = ", ["1/4", "4", "-4", "1/2"], 0, "mcq"),
        ("Simplify: (x³)⁰", ["1", "0", "x³", "x"], 0, "mcq"),
        ("3⁴ ÷ 3² = ", ["3²", "3⁶", "3⁸", "9"], 0, "mcq"),
        ("Singapore population doubles every x years. After 3x years, multiplied by:", ["8", "6", "9", "3"], 0, "mcq"),
        ("Simplify: x² × x³ ÷ x", ["x⁴", "x⁶", "x⁵", "x"], 0, "mcq"),
        ("What is √(x²)?", ["x", "x²", "2x", "x/2"], 0, "mcq"),
        ("Simplify: (3²)²", ["81", "36", "12", "64"], 0, "mcq"),
        ("Express 1/x² using negative index:", ["x⁻²", "-x²", "x⁻¹", "-2x"], 0, "mcq")
    ],

    # GEOMETRY CHAPTERS (7-11)

    "congruence-similarity-sec2": [
        ("Two triangles are congruent if:", ["all corresponding sides and angles equal", "same shape only", "same size only", "same color"], 0, "mcq"),
        ("Which is NOT a congruence test?", ["AAA", "SSS", "SAS", "RHS"], 0, "mcq"),
        ("Similar triangles have:", ["same shape, different size", "same size, different shape", "same size and shape", "no relationship"], 0, "mcq"),
        ("If triangles ABC ≅ DEF, then BC =", ["EF", "DE", "DF", "AB"], 0, "mcq"),
        ("SSS congruence means:", "all three sides equal", None, "short"),
        ("Scale factor 2 means new shape is:", ["2× larger", "2× smaller", "half size", "same"], 0, "mcq"),
        ("Two triangles with sides 3,4,5 and 6,8,10 are:", ["similar", "congruent", "neither", "both"], 0, "mcq"),
        ("RHS congruence applies to:", ["right-angled triangles", "all triangles", "equilateral triangles", "isosceles triangles"], 0, "mcq"),
        ("If scale factor is 1/3, area multiplied by:", ["1/9", "1/3", "3", "9"], 0, "mcq"),
        ("Which proves congruence: 2 sides and included angle?", ["SAS", "SSS", "ASA", "AAA"], 0, "mcq"),
        ("Singapore MRT map uses similar triangles for route planning. If actual distance ratio is 3:5, what is true?", ["corresponding angles equal", "triangles are congruent", "all sides equal", "no relationship"], 0, "mcq"),
        ("ASA congruence requires:", ["2 angles and included side", "3 angles", "3 sides", "1 angle 2 sides"], 0, "mcq"),
        ("Corresponding sides of similar triangles are:", ["proportional", "equal", "different", "perpendicular"], 0, "mcq"),
        ("If triangle areas ratio is 4:9, sides ratio is:", ["2:3", "4:9", "16:81", "1:2"], 0, "mcq"),
        ("What does ≅ symbol mean?", "congruent", None, "short")
    ],

    "pythagoras-theorem-sec2": [
        ("In right triangle, if a=3, b=4, then c=", "5", None, "short"),
        ("Pythagoras theorem: c² = ", ["a² + b²", "a + b", "a² - b²", "ab"], 0, "mcq"),
        ("Find hypotenuse if legs are 5 and 12:", ["13", "17", "7", "10"], 0, "mcq"),
        ("Which can form right triangle?", ["3,4,5", "2,3,4", "1,2,3", "5,6,7"], 0, "mcq"),
        ("If c=10, a=6, find b:", ["8", "4", "16", "14"], 0, "mcq"),
        ("Longest side of right triangle is:", ["hypotenuse", "base", "height", "leg"], 0, "mcq"),
        ("A ladder 13m long reaches 12m up wall. How far is base from wall?", ["5m", "1m", "25m", "7m"], 0, "mcq"),
        ("Which set forms right triangle?", ["5,12,13", "6,7,8", "4,5,6", "7,8,9"], 0, "mcq"),
        ("If square on hypotenuse is 100 cm², hypotenuse length:", ["10cm", "100cm", "50cm", "25cm"], 0, "mcq"),
        ("Diagonal of rectangle with sides 6cm and 8cm:", ["10cm", "14cm", "12cm", "7cm"], 0, "mcq"),
        ("HDB flat room is 3m by 4m. Diagonal distance:", ["5m", "7m", "12m", "3.5m"], 0, "mcq"),
        ("In 3-4-5 triangle, which is hypotenuse?", ["5", "4", "3", "cannot tell"], 0, "mcq"),
        ("If legs are equal (x each) and hypotenuse is 10:", ["x = 5√2", "x = 5", "x = 10", "x = 7.07"], 0, "mcq"),
        ("Distance between points (0,0) and (3,4):", ["5", "7", "12", "1"], 0, "mcq"),
        ("Converse of Pythagoras: if a² + b² = c², triangle is:", ["right-angled", "equilateral", "isosceles", "obtuse"], 0, "mcq")
    ],

    "circle-properties-sec2": [
        ("What is π approximately?", "3.14", None, "short"),
        ("Circumference formula:", ["2πr", "πr²", "πd", "2r"], 0, "mcq"),
        ("Area of circle:", ["πr²", "2πr", "πd", "r²"], 0, "mcq"),
        ("Diameter is ___ radius:", ["2×", "3×", "1/2×", "same"], 0, "mcq"),
        ("Angle in semicircle is:", ["90°", "180°", "45°", "60°"], 0, "mcq"),
        ("Radius of circle with circumference 20π:", ["10", "20", "40", "5"], 0, "mcq"),
        ("Line from center perpendicular to chord:", ["bisects the chord", "parallel to chord", "extends the chord", "has no special property"], 0, "mcq"),
        ("Area of circle with radius 7cm (use π=22/7):", ["154 cm²", "44 cm²", "49 cm²", "308 cm²"], 0, "mcq"),
        ("Singapore Flyer diameter is 150m. Circumference:", ["150π m", "75π m", "300π m", "150 m"], 0, "mcq"),
        ("Two radii form:", ["an isosceles triangle with chord", "equilateral triangle", "right triangle", "no triangle"], 0, "mcq"),
        ("If diameter doubles, area:", ["× 4", "× 2", "× 8", "stays same"], 0, "mcq"),
        ("Tangent to circle is:", ["perpendicular to radius at point of contact", "parallel to radius", "passes through center", "bisects radius"], 0, "mcq"),
        ("Arc is:", ["part of circumference", "part of diameter", "part of radius", "line through center"], 0, "mcq"),
        ("Chord is:", ["line joining two points on circle", "line from center", "half diameter", "tangent line"], 0, "mcq"),
        ("Longest chord of circle is:", ["diameter", "radius", "arc", "tangent"], 0, "mcq")
    ],

    "mensuration-2d-sec2": [
        ("Area of rectangle 5m × 8m:", "40 m²", None, "short"),
        ("Perimeter of square with side 6cm:", ["24cm", "36cm", "12cm", "18cm"], 0, "mcq"),
        ("Area of triangle: base 10cm, height 6cm:", ["30 cm²", "60 cm²", "16 cm²", "20 cm²"], 0, "mcq"),
        ("Area of parallelogram: base 8m, height 5m:", ["40 m²", "13 m²", "80 m²", "20 m²"], 0, "mcq"),
        ("Perimeter of rectangle 7cm by 3cm:", ["20cm", "21cm", "10cm", "14cm"], 0, "mcq"),
        ("Area of trapezium: parallel sides 6,10; height 4:", ["32", "40", "64", "16"], 0, "mcq"),
        ("HDB flat living room: 6m × 4m. Flooring tiles needed (area)?", ["24 m²", "20 m²", "10 m²", "48 m²"], 0, "mcq"),
        ("Perimeter of triangle with sides 3,4,5:", ["12", "6", "15", "7.5"], 0, "mcq"),
        ("Area of square with perimeter 40cm:", ["100 cm²", "40 cm²", "160 cm²", "20 cm²"], 0, "mcq"),
        ("Garden 12m × 8m needs fencing. Total length:", ["40m", "96m", "20m", "48m"], 0, "mcq"),
        ("Area of rhombus: diagonals 8cm and 6cm:", ["24 cm²", "48 cm²", "14 cm²", "28 cm²"], 0, "mcq"),
        ("Composite shape: rectangle 10×6 with triangle (base 10, height 4) on top. Total area:", ["80", "60", "100", "74"], 0, "mcq"),
        ("Circle radius 7cm, area (π = 22/7):", ["154 cm²", "44 cm²", "308 cm²", "22 cm²"], 0, "mcq"),
        ("Rectangle area 48 cm², width 6cm. Length:", ["8cm", "42cm", "54cm", "4cm"], 0, "mcq"),
        ("Triangle base doubles, area:", ["× 2", "× 4", "× 1/2", "stays same"], 0, "mcq")
    ],

    "mensuration-3d-sec2": [
        ("Volume of cube with edge 3cm:", "27 cm³", None, "short"),
        ("Surface area of cube edge 2cm:", ["24 cm²", "8 cm²", "12 cm²", "16 cm²"], 0, "mcq"),
        ("Volume of cuboid 4×3×5:", ["60", "12", "47", "20"], 0, "mcq"),
        ("Volume of cylinder: radius 3cm, height 10cm (π=3.14):", ["282.6 cm³", "94.2 cm³", "30 cm³", "565.2 cm³"], 0, "mcq"),
        ("Volume of prism: base area 20 cm², height 8cm:", ["160 cm³", "28 cm³", "40 cm³", "80 cm³"], 0, "mcq"),
        ("Surface area of cuboid 3×4×5:", ["94", "60", "47", "120"], 0, "mcq"),
        ("HDB water tank: cylinder radius 2m, height 5m. Volume (π=3.14):", ["62.8 m³", "31.4 m³", "20 m³", "125.6 m³"], 0, "mcq"),
        ("Curved surface area of cylinder: r=7cm, h=10cm (π=22/7):", ["440 cm²", "154 cm²", "220 cm²", "308 cm²"], 0, "mcq"),
        ("If cube edge doubles, volume:", ["× 8", "× 2", "× 4", "× 6"], 0, "mcq"),
        ("Volume of triangular prism: base triangle area 15 cm², length 12cm:", ["180 cm³", "27 cm³", "90 cm³", "60 cm³"], 0, "mcq"),
        ("Total surface area of cylinder includes:", ["2 circles + curved surface", "curved surface only", "1 circle + curved surface", "2 circles only"], 0, "mcq"),
        ("Box 10cm × 8cm × 6cm. Volume:", ["480 cm³", "24 cm³", "240 cm³", "960 cm³"], 0, "mcq"),
        ("Cylinder volume formula:", ["πr²h", "2πrh", "πrh", "πr²"], 0, "mcq"),
        ("Cone volume: 1/3 × base area × height. If r=3, h=4, V (π=3.14):", ["37.68", "113.04", "12", "75.36"], 0, "mcq"),
        ("Singapore Sports Hub dome covers volume. Which 3D shape?", ["hemisphere", "cube", "cylinder", "cone"], 0, "mcq")
    ],

    # STATISTICS CHAPTERS (12-14)

    "data-analysis-sec2": [
        ("Mean of 2,4,6,8,10:", "6", None, "short"),
        ("Median of 3,5,7,9,11:", ["7", "5", "9", "6"], 0, "mcq"),
        ("Mode of 2,3,3,4,5,5,5,6:", ["5", "3", "4", "no mode"], 0, "mcq"),
        ("Range of 10,15,20,25,30:", ["20", "30", "10", "5"], 0, "mcq"),
        ("Mean of 5,10,15:", ["10", "15", "5", "30"], 0, "mcq"),
        ("Best measure for data with outliers:", ["median", "mean", "mode", "range"], 0, "mcq"),
        ("Singapore MRT ridership (millions): 5,6,6,7,8. Mode:", ["6", "7", "5", "8"], 0, "mcq"),
        ("If all values increase by 3, mean:", ["increases by 3", "stays same", "triples", "doubles"], 0, "mcq"),
        ("Median of 2,4,6,8:", ["5", "4", "6", "4.5"], 0, "mcq"),
        ("Which shows spread of data?", ["range", "mean", "mode", "median"], 0, "mcq"),
        ("Frequency table: value 5 appears 4 times, value 10 appears 2 times. Mean:", ["6.67", "7.5", "5", "10"], 0, "mcq"),
        ("Bar chart best for:", ["comparing categories", "showing trends over time", "showing parts of whole", "correlation"], 0, "mcq"),
        ("Pie chart shows:", ["parts of a whole", "trends", "correlation", "frequency"], 0, "mcq"),
        ("Line graph best for:", ["trends over time", "comparing categories", "parts of whole", "single values"], 0, "mcq"),
        ("Stem-and-leaf plot preserves:", ["individual data values", "only mean", "only median", "only mode"], 0, "mcq")
    ],

    "probability-sec2": [
        ("Probability of certain event:", "1", None, "short"),
        ("Probability of impossible event:", ["0", "1", "0.5", "-1"], 0, "mcq"),
        ("Fair coin flip, P(heads):", ["1/2", "1", "0", "2"], 0, "mcq"),
        ("Die roll, P(even number):", ["1/2", "1/3", "1/6", "2/3"], 0, "mcq"),
        ("Probability range:", ["0 to 1", "-1 to 1", "0 to 100", "any number"], 0, "mcq"),
        ("P(not A) = ", ["1 - P(A)", "P(A)", "1 + P(A)", "2P(A)"], 0, "mcq"),
        ("Singapore 4D lottery: 10,000 numbers. P(specific number):", ["1/10000", "1/1000", "1/100", "1/4"], 0, "mcq"),
        ("Bag: 3 red, 2 blue balls. P(red):", ["3/5", "2/5", "1/2", "3/2"], 0, "mcq"),
        ("Two coins flipped, P(both heads):", ["1/4", "1/2", "1/3", "2/4"], 0, "mcq"),
        ("Die rolled twice, P(both 6):", ["1/36", "1/6", "2/6", "1/12"], 0, "mcq"),
        ("If P(rain) = 0.3, P(no rain):", ["0.7", "0.3", "1", "0"], 0, "mcq"),
        ("Deck of cards (52), P(ace):", ["1/13", "4/52", "1/4", "1/52"], 0, "mcq"),
        ("For independent events A and B, P(A and B) = ", ["P(A) × P(B)", "P(A) + P(B)", "P(A) - P(B)", "P(A)/P(B)"], 0, "mcq"),
        ("Spinner: 1,2,2,3,3,3. P(3):", ["1/2", "1/3", "1/6", "3/6"], 0, "mcq"),
        ("If all outcomes equally likely:", ["use total number of outcomes", "multiply probabilities", "add all values", "cannot calculate"], 0, "mcq")
    ],

    "sets-venn-diagrams-sec2": [
        ("Symbol for 'element of':", "∈", None, "short"),
        ("Empty set symbol:", ["∅ or {}", "0", "[ ]", "null"], 0, "mcq"),
        ("A ∪ B means:", ["union (all elements)", "intersection", "difference", "complement"], 0, "mcq"),
        ("A ∩ B means:", ["intersection (common elements)", "union", "difference", "complement"], 0, "mcq"),
        ("If A = {1,2,3} and B = {2,3,4}, A ∩ B = ", ["{2,3}", "{1,2,3,4}", "{1,4}", "{1}"], 0, "mcq"),
        ("If A = {1,2} and B = {3,4}, A ∪ B = ", ["{1,2,3,4}", "{}", "{2,3}", "{1,4}"], 0, "mcq"),
        ("n(A) means:", ["number of elements in A", "name of set A", "A is null", "A is subset"], 0, "mcq"),
        ("If A ⊂ B, then:", ["all elements of A are in B", "A and B are equal", "B is subset of A", "A and B have no common elements"], 0, "mcq"),
        ("Singapore students: 30 study Math, 20 study Science, 10 study both. How many study at least one?", ["40", "50", "30", "20"], 0, "mcq"),
        ("Complement of A (A'):", ["elements NOT in A", "elements in A", "all elements", "empty set"], 0, "mcq"),
        ("If universal set U = {1,2,3,4,5} and A = {1,2}, then A' = ", ["{3,4,5}", "{1,2}", "{1,2,3,4,5}", "{}"], 0, "mcq"),
        ("A - B means:", ["elements in A but not in B", "union", "intersection", "all elements"], 0, "mcq"),
        ("Venn diagram: overlapping region shows:", ["A ∩ B", "A ∪ B", "A'", "B'"], 0, "mcq"),
        ("If A and B have no common elements:", ["A ∩ B = ∅", "A ∪ B = ∅", "A = B", "A ⊂ B"], 0, "mcq"),
        ("Roster form: listing elements in:", ["curly braces { }", "square brackets [ ]", "parentheses ( )", "angle brackets < >"], 0, "mcq")
    ]
}

print("Updating exercises for all 14 Math chapters...\n")

for chapter in chapters:
    chapter_id = chapter["id"]
    if chapter_id in exercise_data:
        exercises = []
        for q_num, q_data in enumerate(exercise_data[chapter_id], 1):
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
                    "hint": "Review the section notes.",
                    "hint_zh": "查看章节注释。"
                }
            elif q_type == "multi":
                exercise = {
                    "id": f"{chapter_id.replace('-sec2', '')}-q{q_num}",
                    "type": "multi",
                    "difficulty": difficulty,
                    "prompt": prompt,
                    "prompt_zh": f"[{chapter['title']} - 问题 {q_num}]",
                    "choices": choices_or_answer,
                    "answers": answer_or_none,
                    "hint": "Select all correct answers.",
                    "hint_zh": "选择所有正确答案。"
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
                    "hint": "Think about the key concepts.",
                    "hint_zh": "想想关键概念。"
                }

            exercises.append(exercise)

        chapter["exercises"] = exercises
        print(f"✓ {chapter['title']}: {len(exercises)} exercises added")

# Save
with open('chapters/math-sec2-chapters.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, indent=2, ensure_ascii=False)

print(f"\n✅ All 14 Math chapters updated successfully!")
print(f"📊 Total exercises: {sum(len(ch['exercises']) for ch in chapters)}")
