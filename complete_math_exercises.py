import json

# Load current content
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Completing remaining Math chapters...\n")

# Find Math subject and add exercises to remaining chapters
for subject in data['subjects']:
    if subject['id'] == 'math':
        for chapter in subject['chapters']:
            current_count = len(chapter.get('exercises', []))

            # Integers - need 1 more (already done earlier)

            # Triangles & Polygons - need 11 more
            if chapter['id'] == 'triangles-polygons' and current_count < 15:
                chapter['exercises'].extend([
                    {"id": f"tri-ex{i+5}", "type": "mcq", "difficulty": ["easy", "medium", "hard"][(i%3)],
                     "prompt": [
                         "What is the sum of interior angles in a quadrilateral?",
                         "An isosceles triangle has two sides of 5 cm. The perimeter is 17 cm. Find the third side:",
                         "How many sides does a pentagon have?",
                         "What is the sum of exterior angles of any polygon?",
                         "In an equilateral triangle, each angle measures:",
                         "A triangle has angles 40° and 60°. Find the third angle:",
                         "How many diagonals does a hexagon have?",
                         "The sum of interior angles of a polygon is 1080°. How many sides?",
                         "What type of triangle has all sides different?",
                         "A regular pentagon has each interior angle of:",
                         "What is a polygon with 8 sides called?"
                     ][i],
                     "prompt_zh": [
                         "四边形的内角和是多少？",
                         "一个等腰三角形有两条边长5厘米。周长是17厘米。求第三边：",
                         "五边形有多少条边？",
                         "任何多边形的外角和是多少？",
                         "等边三角形中，每个角的度数是：",
                         "一个三角形有两个角分别是40°和60°。求第三个角：",
                         "六边形有多少条对角线？",
                         "一个多边形的内角和是1080°。它有多少条边？",
                         "所有边都不相等的三角形叫什么？",
                         "正五边形的每个内角是：",
                         "8条边的多边形叫什么？"
                     ][i],
                     "choices": [
                         ["360°", "180°", "540°", "720°"],
                         ["7 cm", "12 cm", "10 cm", "8 cm"],
                         ["5", "6", "7", "8"],
                         ["360°", "180°", "540°", "720°"],
                         ["60°", "90°", "45°", "120°"],
                         ["80°", "90°", "100°", "70°"],
                         ["9", "6", "12", "15"],
                         ["6", "8", "10", "12"],
                         ["Scalene", "Isosceles", "Equilateral", "Right"],
                         ["108°", "120°", "90°", "72°"],
                         ["Octagon", "Heptagon", "Hexagon", "Nonagon"]
                     ][i],
                     "choices_zh": [
                         ["360°", "180°", "540°", "720°"],
                         ["7厘米", "12厘米", "10厘米", "8厘米"],
                         ["5", "6", "7", "8"],
                         ["360°", "180°", "540°", "720°"],
                         ["60°", "90°", "45°", "120°"],
                         ["80°", "90°", "100°", "70°"],
                         ["9", "6", "12", "15"],
                         ["6", "8", "10", "12"],
                         ["不等边三角形", "等腰三角形", "等边三角形", "直角三角形"],
                         ["108°", "120°", "90°", "72°"],
                         ["八边形", "七边形", "六边形", "九边形"]
                     ][i],
                     "answer": [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0][i],
                     "explanation": [
                         "Sum of angles in quadrilateral = 360°",
                         "Two equal sides = 10 cm total. Third side = 17 - 10 = 7 cm",
                         "Pentagon has 5 sides",
                         "Sum of exterior angles = 360° for all polygons",
                         "Each angle in equilateral triangle = 180°/3 = 60°",
                         "Sum = 180°. Third angle = 180° - 40° - 60° = 80°",
                         "Formula: n(n-3)/2 = 6(3)/2 = 9 diagonals",
                         "Formula: (n-2)×180 = 1080, so n-2 = 6, n = 8 sides",
                         "Scalene triangle has all sides different",
                         "Each interior angle = (n-2)×180/n = 3×180/5 = 108°",
                         "8-sided polygon is an octagon"
                     ][i],
                     "explanation_zh": [
                         "四边形内角和 = 360°",
                         "两条相等的边 = 10厘米。第三边 = 17 - 10 = 7厘米",
                         "五边形有5条边",
                         "所有多边形的外角和 = 360°",
                         "等边三角形每个角 = 180°/3 = 60°",
                         "和 = 180°。第三个角 = 180° - 40° - 60° = 80°",
                         "公式：n(n-3)/2 = 6(3)/2 = 9条对角线",
                         "公式：(n-2)×180 = 1080，所以n-2 = 6，n = 8条边",
                         "不等边三角形所有边都不相等",
                         "每个内角 = (n-2)×180/n = 3×180/5 = 108°",
                         "8条边的多边形是八边形"
                     ][i]
                     } for i in range(11)
                ])
                print(f"✓ Added 11 exercises to {chapter['title']} (now {len(chapter['exercises'])})")

            # Perimeter & Area - need 11 more
            elif chapter['id'] == 'perimeter-area' and current_count < 15:
                chapter['exercises'].extend([
                    {"id": f"area-ex{i+5}", "type": "mcq", "difficulty": ["easy", "medium", "hard"][(i%3)],
                     "prompt": [
                         "Find the perimeter of a rectangle with length 8 cm and width 5 cm:",
                         "Find the area of a square with side 6 cm:",
                         "A rectangle has area 48 cm² and length 8 cm. Find its width:",
                         "Find the area of a triangle with base 10 cm and height 6 cm:",
                         "A circular garden has radius 7 m. Find its circumference: (π = 22/7)",
                         "Find the area of a circle with radius 14 cm: (π = 22/7)",
                         "A rectangular field is 50 m long and 30 m wide. Find its area:",
                         "Find the perimeter of a square with area 64 cm²:",
                         "A triangle has sides 3 cm, 4 cm, and 5 cm. Find its perimeter:",
                         "Find the area of a parallelogram with base 12 cm and height 5 cm:",
                         "A trapezium has parallel sides 8 cm and 12 cm, height 5 cm. Find area:"
                     ][i],
                     "prompt_zh": [
                         "求长8厘米、宽5厘米的矩形周长：",
                         "求边长6厘米的正方形面积：",
                         "矩形面积48平方厘米，长8厘米。求宽：",
                         "求底边10厘米、高6厘米的三角形面积：",
                         "一个圆形花园半径7米。求周长：(π = 22/7)",
                         "求半径14厘米的圆的面积：(π = 22/7)",
                         "长方形田地长50米、宽30米。求面积：",
                         "求面积64平方厘米的正方形周长：",
                         "三角形三边分别为3厘米、4厘米、5厘米。求周长：",
                         "求底边12厘米、高5厘米的平行四边形面积：",
                         "梯形平行边8厘米和12厘米，高5厘米。求面积："
                     ][i],
                     "choices": [
                         ["26 cm", "40 cm", "13 cm", "80 cm"],
                         ["36 cm²", "24 cm²", "12 cm²", "48 cm²"],
                         ["6 cm", "5 cm", "7 cm", "4 cm"],
                         ["30 cm²", "60 cm²", "15 cm²", "20 cm²"],
                         ["44 m", "22 m", "154 m", "88 m"],
                         ["616 cm²", "308 cm²", "88 cm²", "44 cm²"],
                         ["1500 m²", "160 m", "1600 m²", "80 m²"],
                         ["32 cm", "16 cm", "64 cm", "8 cm"],
                         ["12 cm", "6 cm", "15 cm", "10 cm"],
                         ["60 cm²", "17 cm²", "34 cm²", "30 cm²"],
                         ["50 cm²", "100 cm²", "40 cm²", "60 cm²"]
                     ][i],
                     "choices_zh": [
                         ["26厘米", "40厘米", "13厘米", "80厘米"],
                         ["36平方厘米", "24平方厘米", "12平方厘米", "48平方厘米"],
                         ["6厘米", "5厘米", "7厘米", "4厘米"],
                         ["30平方厘米", "60平方厘米", "15平方厘米", "20平方厘米"],
                         ["44米", "22米", "154米", "88米"],
                         ["616平方厘米", "308平方厘米", "88平方厘米", "44平方厘米"],
                         ["1500平方米", "160米", "1600平方米", "80平方米"],
                         ["32厘米", "16厘米", "64厘米", "8厘米"],
                         ["12厘米", "6厘米", "15厘米", "10厘米"],
                         ["60平方厘米", "17平方厘米", "34平方厘米", "30平方厘米"],
                         ["50平方厘米", "100平方厘米", "40平方厘米", "60平方厘米"]
                     ][i],
                     "answer": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0][i],
                     "explanation": [
                         "Perimeter = 2(length + width) = 2(8 + 5) = 26 cm",
                         "Area = side² = 6² = 36 cm²",
                         "Area = length × width, so 48 = 8 × width, width = 6 cm",
                         "Area = ½ × base × height = ½ × 10 × 6 = 30 cm²",
                         "Circumference = 2πr = 2 × 22/7 × 7 = 44 m",
                         "Area = πr² = 22/7 × 14² = 616 cm²",
                         "Area = length × width = 50 × 30 = 1500 m²",
                         "Side = √64 = 8 cm. Perimeter = 4 × 8 = 32 cm",
                         "Perimeter = 3 + 4 + 5 = 12 cm",
                         "Area = base × height = 12 × 5 = 60 cm²",
                         "Area = ½(a + b)h = ½(8 + 12)×5 = 50 cm²"
                     ][i],
                     "explanation_zh": [
                         "周长 = 2(长 + 宽) = 2(8 + 5) = 26厘米",
                         "面积 = 边² = 6² = 36平方厘米",
                         "面积 = 长 × 宽，所以48 = 8 × 宽，宽 = 6厘米",
                         "面积 = ½ × 底 × 高 = ½ × 10 × 6 = 30平方厘米",
                         "周长 = 2πr = 2 × 22/7 × 7 = 44米",
                         "面积 = πr² = 22/7 × 14² = 616平方厘米",
                         "面积 = 长 × 宽 = 50 × 30 = 1500平方米",
                         "边 = √64 = 8厘米。周长 = 4 × 8 = 32厘米",
                         "周长 = 3 + 4 + 5 = 12厘米",
                         "面积 = 底 × 高 = 12 × 5 = 60平方厘米",
                         "面积 = ½(a + b)h = ½(8 + 12)×5 = 50平方厘米"
                     ][i]
                     } for i in range(11)
                ])
                print(f"✓ Added 11 exercises to {chapter['title']} (now {len(chapter['exercises'])})")

            # Statistics - need 11 more
            elif chapter['id'] == 'statistics' and current_count < 15:
                chapter['exercises'].extend([
                    {"id": f"stat-ex{i+5}", "type": "mcq", "difficulty": ["easy", "medium", "hard"][(i%3)],
                     "prompt": [
                         "Find the mean of: 2, 4, 6, 8, 10",
                         "Find the median of: 3, 7, 2, 9, 5",
                         "Find the mode of: 2, 3, 3, 4, 5, 3, 6",
                         "Find the range of: 10, 15, 8, 20, 12",
                         "The mean of 5 numbers is 12. Their sum is:",
                         "Find the median of: 4, 2, 8, 6",
                         "Which measure is most affected by outliers?",
                         "Data: 5, 5, 5, 5, 100. Find the median:",
                         "Find the mean of: 10, 20, 30",
                         "In a class, 10 students scored 80, 15 scored 70. Find mean:",
                         "Data: 1, 2, 2, 3, 3, 3, 4. What is the mode?"
                     ][i],
                     "prompt_zh": [
                         "求平均数：2, 4, 6, 8, 10",
                         "求中位数：3, 7, 2, 9, 5",
                         "求众数：2, 3, 3, 4, 5, 3, 6",
                         "求全距：10, 15, 8, 20, 12",
                         "5个数的平均数是12。它们的和是：",
                         "求中位数：4, 2, 8, 6",
                         "哪个度量最受极端值影响？",
                         "数据：5, 5, 5, 5, 100。求中位数：",
                         "求平均数：10, 20, 30",
                         "班上10个学生得80分，15个得70分。求平均分：",
                         "数据：1, 2, 2, 3, 3, 3, 4。众数是什么？"
                     ][i],
                     "choices": [
                         ["6", "5", "7", "8"],
                         ["5", "7", "6", "4"],
                         ["3", "2", "4", "6"],
                         ["12", "10", "20", "8"],
                         ["60", "12", "5", "17"],
                         ["5", "4", "6", "7"],
                         ["Mean", "Median", "Mode", "Range"],
                         ["5", "100", "25", "20"],
                         ["20", "30", "15", "10"],
                         ["74", "75", "72", "76"],
                         ["3", "2", "1", "4"]
                     ][i],
                     "choices_zh": [
                         ["6", "5", "7", "8"],
                         ["5", "7", "6", "4"],
                         ["3", "2", "4", "6"],
                         ["12", "10", "20", "8"],
                         ["60", "12", "5", "17"],
                         ["5", "4", "6", "7"],
                         ["平均数", "中位数", "众数", "全距"],
                         ["5", "100", "25", "20"],
                         ["20", "30", "15", "10"],
                         ["74", "75", "72", "76"],
                         ["3", "2", "1", "4"]
                     ][i],
                     "answer": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0][i],
                     "explanation": [
                         "Mean = (2+4+6+8+10)/5 = 30/5 = 6",
                         "Ordered: 2,3,5,7,9. Median = middle = 5",
                         "3 appears most frequently (3 times)",
                         "Range = largest - smallest = 20 - 8 = 12",
                         "Sum = mean × count = 12 × 5 = 60",
                         "Ordered: 2,4,6,8. Median = (4+6)/2 = 5",
                         "Mean is most affected by extreme values (outliers)",
                         "Ordered: 5,5,5,5,100. Median = middle = 5",
                         "Mean = (10+20+30)/3 = 60/3 = 20",
                         "Total = (10×80 + 15×70)/25 = 1850/25 = 74",
                         "3 appears most frequently (3 times)"
                     ][i],
                     "explanation_zh": [
                         "平均数 = (2+4+6+8+10)/5 = 30/5 = 6",
                         "排序：2,3,5,7,9。中位数 = 中间值 = 5",
                         "3出现最多（3次）",
                         "全距 = 最大 - 最小 = 20 - 8 = 12",
                         "和 = 平均数 × 个数 = 12 × 5 = 60",
                         "排序：2,4,6,8。中位数 = (4+6)/2 = 5",
                         "平均数最受极端值影响",
                         "排序：5,5,5,5,100。中位数 = 中间值 = 5",
                         "平均数 = (10+20+30)/3 = 60/3 = 20",
                         "总计 = (10×80 + 15×70)/25 = 1850/25 = 74",
                         "3出现最多（3次）"
                     ][i]
                     } for i in range(11)
                ])
                print(f"✓ Added 11 exercises to {chapter['title']} (now {len(chapter['exercises'])})")

            # Volume & Surface Area - need 10 more
            elif chapter['id'] == 'volume-surface-area' and current_count < 15:
                chapter['exercises'].extend([
                    {"id": f"vol-ex{i+6}", "type": "mcq", "difficulty": ["easy", "medium", "hard"][(i%3)],
                     "prompt": [
                         "Find the volume of a cube with side 3 cm:",
                         "Find the volume of a cuboid: length 5 cm, width 3 cm, height 2 cm:",
                         "A cube has volume 64 cm³. Find its side length:",
                         "Find the surface area of a cube with side 4 cm:",
                         "Find the volume of a cylinder: radius 7 cm, height 10 cm: (π = 22/7)",
                         "Find the total surface area of a cuboid: 6 cm × 4 cm × 3 cm:",
                         "A rectangular water tank is 2m long, 1.5m wide, 1m high. Find capacity in liters:",
                         "Find the curved surface area of cylinder: radius 3.5 cm, height 8 cm: (π = 22/7)",
                         "A cube has surface area 96 cm². Find its side:",
                         "Volume of sphere with radius 3 cm: (π = 22/7, V = 4/3πr³)"
                     ][i],
                     "prompt_zh": [
                         "求边长3厘米的立方体体积：",
                         "求长方体体积：长5厘米、宽3厘米、高2厘米：",
                         "立方体体积64立方厘米。求边长：",
                         "求边长4厘米的立方体表面积：",
                         "求圆柱体积：半径7厘米、高10厘米：(π = 22/7)",
                         "求长方体总表面积：6厘米 × 4厘米 × 3厘米：",
                         "长方体水箱长2米、宽1.5米、高1米。求容量（升）：",
                         "求圆柱侧面积：半径3.5厘米、高8厘米：(π = 22/7)",
                         "立方体表面积96平方厘米。求边长：",
                         "求半径3厘米的球体积：(π = 22/7, V = 4/3πr³)"
                     ][i],
                     "choices": [
                         ["27 cm³", "9 cm³", "18 cm³", "81 cm³"],
                         ["30 cm³", "10 cm³", "60 cm³", "15 cm³"],
                         ["4 cm", "8 cm", "16 cm", "2 cm"],
                         ["96 cm²", "64 cm²", "16 cm²", "24 cm²"],
                         ["1540 cm³", "770 cm³", "154 cm³", "440 cm³"],
                         ["108 cm²", "72 cm²", "144 cm²", "216 cm²"],
                         ["3000 L", "300 L", "30 L", "3 L"],
                         ["176 cm²", "88 cm²", "154 cm²", "220 cm²"],
                         ["4 cm", "16 cm", "24 cm", "8 cm"],
                         ["113 cm³", "226 cm³", "339 cm³", "452 cm³"]
                     ][i],
                     "choices_zh": [
                         ["27立方厘米", "9立方厘米", "18立方厘米", "81立方厘米"],
                         ["30立方厘米", "10立方厘米", "60立方厘米", "15立方厘米"],
                         ["4厘米", "8厘米", "16厘米", "2厘米"],
                         ["96平方厘米", "64平方厘米", "16平方厘米", "24平方厘米"],
                         ["1540立方厘米", "770立方厘米", "154立方厘米", "440立方厘米"],
                         ["108平方厘米", "72平方厘米", "144平方厘米", "216平方厘米"],
                         ["3000升", "300升", "30升", "3升"],
                         ["176平方厘米", "88平方厘米", "154平方厘米", "220平方厘米"],
                         ["4厘米", "16厘米", "24厘米", "8厘米"],
                         ["113立方厘米", "226立方厘米", "339立方厘米", "452立方厘米"]
                     ][i],
                     "answer": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0][i],
                     "explanation": [
                         "Volume = side³ = 3³ = 27 cm³",
                         "Volume = length × width × height = 5 × 3 × 2 = 30 cm³",
                         "side³ = 64, side = ³√64 = 4 cm",
                         "Surface area = 6 × side² = 6 × 4² = 96 cm²",
                         "Volume = πr²h = 22/7 × 7² × 10 = 1540 cm³",
                         "SA = 2(6×4 + 4×3 + 3×6) = 2(24+12+18) = 108 cm²",
                         "Volume = 2×1.5×1 = 3 m³ = 3000 liters",
                         "Curved SA = 2πrh = 2 × 22/7 × 3.5 × 8 = 176 cm²",
                         "6×side² = 96, side² = 16, side = 4 cm",
                         "V = 4/3 × 22/7 × 3³ = 4/3 × 22/7 × 27 ≈ 113 cm³"
                     ][i],
                     "explanation_zh": [
                         "体积 = 边³ = 3³ = 27立方厘米",
                         "体积 = 长 × 宽 × 高 = 5 × 3 × 2 = 30立方厘米",
                         "边³ = 64，边 = ³√64 = 4厘米",
                         "表面积 = 6 × 边² = 6 × 4² = 96平方厘米",
                         "体积 = πr²h = 22/7 × 7² × 10 = 1540立方厘米",
                         "表面积 = 2(6×4 + 4×3 + 3×6) = 2(24+12+18) = 108平方厘米",
                         "体积 = 2×1.5×1 = 3立方米 = 3000升",
                         "侧面积 = 2πrh = 2 × 22/7 × 3.5 × 8 = 176平方厘米",
                         "6×边² = 96，边² = 16，边 = 4厘米",
                         "V = 4/3 × 22/7 × 3³ = 4/3 × 22/7 × 27 ≈ 113立方厘米"
                     ][i]
                     } for i in range(10)
                ])
                print(f"✓ Added 10 exercises to {chapter['title']} (now {len(chapter['exercises'])})")

# Save updated content
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\n✓ All remaining Math exercises added successfully!")
