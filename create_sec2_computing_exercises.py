"""
Create rigorous exercises for Secondary 2 Computing chapters
Aligned with Singapore MOE Computing standards
Emphasis on problem-solving, code reading, and application
"""

import json

# Load chapters
with open('chapters/computing-sec2-chapters.json', 'r', encoding='utf-8') as f:
    chapters = json.load(f)

# Exercise data for all 6 chapters
exercise_data = {
    "algorithms-flowcharts-sec2": [
        # Easy
        ("An algorithm is:", ["A step-by-step procedure to solve a problem", "A programming language", "A type of computer", "A flowchart only"], 0, "mcq"),
        ("Which flowchart symbol represents a decision?", ["Diamond", "Rectangle", "Oval", "Parallelogram"], 0, "mcq"),
        ("What does an oval symbol represent in a flowchart?", "Start or End", None, "short"),
        ("In pseudocode, which keyword is used for conditional statements?", ["IF", "LOOP", "PRINT", "BEGIN"], 0, "mcq"),
        ("Arrow in flowchart indicates:", ["Flow direction", "Input", "Decision", "Process"], 0, "mcq"),

        # Medium
        ("Algorithm to find largest of 3 numbers. Which is correct pseudocode?", ["IF a>b AND a>c THEN max=a", "IF a>b OR a>c THEN max=a", "max = a + b + c", "IF a==b THEN max=a"], 0, "mcq"),
        ("Singapore ERP gantry charges based on time and vehicle type. Which flowchart symbol determines the charge?", ["Diamond (decision based on time/vehicle)", "Rectangle (process)", "Parallelogram (input)", "Oval (start)"], 0, "mcq"),
        ("Linear search vs binary search. For 1000-item sorted list, maximum comparisons:", "Linear: 1000, Binary: 10", None, "short"),
        ("Pseudocode: count = 0 / WHILE count < 5 / OUTPUT count / count = count + 1. What is output?", ["0,1,2,3,4", "1,2,3,4,5", "0,1,2,3,4,5", "Infinite loop"], 0, "mcq"),
        ("Which is NOT a characteristic of a good algorithm?", ["Ambiguous steps", "Finite steps", "Well-defined inputs/outputs", "Effective"], 0, "mcq"),

        # Hard
        ("Algorithm calculates factorial: INPUT n / factorial = 1 / FOR i = 1 TO n / factorial = factorial * i / OUTPUT factorial. For n=5, output:", ["120", "15", "25", "5"], 0, "mcq"),
        ("Singapore MRT route finder uses which algorithm type to find shortest path between stations?", ["Graph traversal (Dijkstra's algorithm)", "Linear search", "Bubble sort", "Sequential processing"], 0, "mcq"),
        ("Bubble sort algorithm: Worst-case time complexity for n items:", "O(n²)", None, "short"),
        ("Flowchart for Singapore NRIC check digit validation requires:", ["Multiple decision points for modulo operations", "Single input only", "No decisions needed", "Output only"], 0, "mcq"),
        ("Algorithm efficiency: Processing 1 million records. Which grows slowest? O(n) vs O(n²) vs O(log n):", ["O(log n)", "O(n)", "O(n²)", "All same"], 0, "mcq")
    ],

    "python-basics-sec2": [
        # Easy
        ("Which is valid Python variable name?", ["student_age", "2nd_student", "class", "my-name"], 0, "mcq"),
        ("Data type of: price = 5.50:", "float", None, "short"),
        ("print(10 + 5 * 2) outputs:", ["20", "30", "10", "15"], 0, "mcq"),
        ("To get user input as integer:", ["int(input())", "input()", "get()", "scan()"], 0, "mcq"),
        ("17 % 5 equals:", ["2", "3", "5", "0"], 0, "mcq"),

        # Medium
        ("Code: x = '5' / y = 3 / z = x + y. Result?", ["Error (cannot add string and int)", "8", "'53'", "5"], 0, "mcq"),
        ("Singapore GST calculation: price = 100 / gst = price * 0.09 / total = price + gst. Value of total:", ["109.0", "100.09", "9.0", "109"], 0, "mcq"),
        ("What does this output? name = 'Singapore' / print(name[0] + name[-1])", "Se", None, "short"),
        ("Code: x = 10 / x = x + 5 / x = x * 2 / print(x). Output:", ["30", "20", "25", "15"], 0, "mcq"),
        ("Which operator checks if two values are equal?", ["==", "=", "!=", ">="], 0, "mcq"),

        # Hard
        ("Code: distance = float(input()) / if distance <= 3.2: fare = 0.92 / else: fare = 0.92 + (distance - 3.2) * 0.16 / print(round(fare, 2)). For input 5.0, output:", ["1.21", "0.92", "1.76", "0.80"], 0, "mcq"),
        ("Expression evaluation: 10 + 5 * 2 ** 3 / 5. Result:", ["18.0", "120.0", "10.0", "50.0"], 0, "mcq"),
        ("Type conversion: int(5.9) + int('7') equals:", "12", None, "short"),
        ("Singapore temperature converter: c = float(input()) / f = c * 9/5 + 32 / print(f'C: {c}, F: {f}'). For input 30, which outputs?", ["C: 30.0, F: 86.0", "C: 30, F: 86", "Error", "C: 86.0, F: 30.0"], 0, "mcq"),
        ("Logical expression: age = 14 / Result of: age >= 13 and age < 20:", ["True", "False", "Error", "None"], 0, "mcq")
    ],

    "selection-iteration-sec2": [
        # Easy
        ("if score >= 75: / grade = 'A' / else: / grade = 'B'. If score = 80, grade is:", "A", None, "short"),
        ("range(5) produces:", ["0,1,2,3,4", "1,2,3,4,5", "0,1,2,3,4,5", "1,2,3,4"], 0, "mcq"),
        ("While loop continues while condition is:", ["True", "False", "1", "0"], 0, "mcq"),
        ("for i in range(2, 8, 2): / print(i). Output:", ["2,4,6", "2,4,6,8", "0,2,4,6", "2,3,4,5,6,7"], 0, "mcq"),
        ("Code: x = 10 / if x > 5: / print('Big'). Output:", ["Big", "Nothing", "Error", "5"], 0, "mcq"),

        # Medium
        ("Singapore O-Level grading: if score >= 75: grade = 'A1' / elif score >= 70: grade = 'A2' / elif score >= 65: grade = 'B3' / else: grade = 'B4'. For score = 72, grade:", ["A2", "A1", "B3", "B4"], 0, "mcq"),
        ("count = 0 / total = 0 / while count < 4: / total = total + count / count = count + 1 / print(total). Output:", ["6", "10", "0", "4"], 0, "mcq"),
        ("for i in range(1, 4): / for j in range(1, 3): / print(i * j, end=' '). Output:", "1 2 2 4 3 6", None, "short"),
        ("Code validates Singapore NRIC: nric = input() / if len(nric) == 9 and nric[0] in 'STFG': / print('Valid'). For input 'S1234567D', output:", ["Valid", "Invalid", "Error", "Nothing"], 0, "mcq"),
        ("Infinite loop occurs when:", ["Condition never becomes False", "Condition is False", "Loop runs once", "No condition"], 0, "mcq"),

        # Hard
        ("num = int(input()) / total = 0 / for i in range(1, num+1): / if num % i == 0: / total = total + 1 / print(total). For input 12, output (count of divisors):", ["6", "12", "4", "3"], 0, "mcq"),
        ("Singapore bus arrival: buses = [5, 12, 18] / for time in buses: / if time <= 10: / print(f'Bus in {time} min') / break / else: / print('Wait for next'). Output:", ["Bus in 5 min", "Bus in 12 min", "Wait for next", "Bus in 5 min, Bus in 12 min"], 0, "mcq"),
        ("n = 5 / for i in range(1, n+1): / print('*' * i). Number of stars printed:", "15", None, "short"),
        ("PIN validation (3 attempts): attempts = 0 / while attempts < 3: / pin = input() / if pin == '1234': / print('Success') / break / attempts += 1 / else: / print('Locked'). What triggers 'Locked'?", ["3 wrong attempts without break", "First wrong attempt", "Any wrong attempt", "Never triggers"], 0, "mcq"),
        ("Nested loop: for r in range(3): / for c in range(4): / print('#', end='') / print(). Total '#' symbols:", ["12", "7", "3", "4"], 0, "mcq")
    ],

    "data-structures-sec2": [
        # Easy
        ("stations = ['Bishan', 'Ang Mo Kio', 'Yio Chu Kang'] / stations[1] is:", "Ang Mo Kio", None, "short"),
        ("len([10, 20, 30, 40]) returns:", ["4", "100", "10", "3"], 0, "mcq"),
        ("numbers = [5, 2, 8, 1] / numbers.append(10) / print(numbers[-1]). Output:", ["10", "1", "8", "5"], 0, "mcq"),
        ("'Singapore'[4] returns:", ["p", "a", "g", "o"], 0, "mcq"),
        ("'Hello' + 'World' equals:", ["HelloWorld", "Hello World", "Error", "helloworld"], 0, "mcq"),

        # Medium
        ("scores = [85, 92, 78, 90] / print(max(scores) - min(scores)). Output:", ["14", "345", "85", "78"], 0, "mcq"),
        ("Singapore postal codes: codes = ['238880', '018956'] / codes[0][:3] returns:", ["238", "880", "238880", "023"], 0, "mcq"),
        ("fruits = ['apple', 'banana', 'cherry'] / fruits[1:3] returns:", "['banana', 'cherry']", None, "short"),
        ("message = '  Singapore  ' / message.strip().upper() equals:", ["SINGAPORE", "'Singapore'", "singapore", "Error"], 0, "mcq"),
        ("numbers = [1, 2, 3] / numbers * 2 produces:", ["[1,2,3,1,2,3]", "[2,4,6]", "Error", "[1,2,3,2]"], 0, "mcq"),

        # Hard
        ("temps = [28, 32, 30, 29, 31] / count = 0 / for t in temps: / if t > 30: count += 1 / print(count). Output (days above 30°C):", ["2", "3", "5", "1"], 0, "mcq"),
        ("Singapore MRT lines: lines = ['Red', 'Green', 'Purple'] / lines.insert(1, 'Blue') / lines.remove('Green') / print(lines). Output:", ["['Red','Blue','Purple']", "['Blue','Red','Purple']", "['Red','Purple']", "Error"], 0, "mcq"),
        ("nric = 'S1234567D' / nric[1:8] extracts:", "1234567", None, "short"),
        ("sentence = 'Singapore is a city' / words = sentence.split() / print(len(words)). Output:", ["4", "19", "3", "5"], 0, "mcq"),
        ("List comprehension: [x*2 for x in range(5)] produces:", ["[0,2,4,6,8]", "[0,1,2,3,4]", "[2,4,6,8,10]", "[1,2,3,4,5]"], 0, "mcq")
    ],

    "functions-modules-sec2": [
        # Easy
        ("def greet(): / print('Hello') / greet(). What does this do?", "Prints Hello", None, "short"),
        ("def add(a, b): / return a + b / result = add(5, 3). Value of result:", ["8", "5", "3", "None"], 0, "mcq"),
        ("Function definition starts with keyword:", ["def", "func", "function", "define"], 0, "mcq"),
        ("return statement:", ["Sends value back to caller and exits function", "Prints value", "Loops back", "Continues function"], 0, "mcq"),
        ("import math / math.sqrt(16) returns:", ["4.0", "16", "8", "2"], 0, "mcq"),

        # Medium
        ("def calculate_gst(price): / gst = price * 0.09 / total = price + gst / return total / result = calculate_gst(100). Value of result:", ["109.0", "9.0", "100", "Error"], 0, "mcq"),
        ("def max_of_three(a, b, c): / if a>=b and a>=c: return a / elif b>=c: return b / else: return c / print(max_of_three(5,12,8)). Output:", ["12", "5", "8", "Error"], 0, "mcq"),
        ("from random import randint / dice = randint(1, 6). Value range of dice:", "1 to 6 inclusive", None, "short"),
        ("def is_even(n): / return n % 2 == 0 / print(is_even(7)). Output:", ["False", "True", "0", "7"], 0, "mcq"),
        ("Variable defined inside function is:", ["Local to that function", "Global", "Available everywhere", "Permanent"], 0, "mcq"),

        # Hard
        ("Singapore temp converter: def to_fahrenheit(celsius): / return celsius * 9/5 + 32 / def to_celsius(fahr): / return (fahr - 32) * 5/9 / print(to_celsius(to_fahrenheit(30))). Output:", ["30.0", "86.0", "Error", "-1.11"], 0, "mcq"),
        ("def factorial(n): / if n == 0: return 1 / else: return n * factorial(n-1) / factorial(4) returns:", ["24", "4", "10", "Infinite"], 0, "mcq"),
        ("def process(nums): / result = [] / for n in nums: / if n > 10: result.append(n) / return result / process([5,15,8,20]). Output:", "[15, 20]", None, "short"),
        ("import datetime / now = datetime.datetime.now() / print(now.hour). This prints:", ["Current hour (0-23)", "Current minute", "Current day", "Error"], 0, "mcq"),
        ("Function with default parameter: def greet(name='Guest'): / return f'Hello {name}' / greet() + greet('Ali') equals:", ["Hello GuestHello Ali", "Hello Ali", "Error", "Hello Guest"], 0, "mcq")
    ],

    "web-html-css-sec2": [
        # Easy
        ("HTML stands for:", ["HyperText Markup Language", "High Tech Modern Language", "Home Tool Markup Language", "Hyperlinks and Text Markup Language"], 0, "mcq"),
        ("Which tag creates a paragraph?", "<p>", None, "short"),
        ("<h1> to <h6> tags represent:", ["Headings (h1 largest)", "Links", "Images", "Lists"], 0, "mcq"),
        ("CSS stands for:", ["Cascading Style Sheets", "Computer Style Sheets", "Creative Style System", "Colorful Style Sheets"], 0, "mcq"),
        ("<img src='flag.jpg' alt='Singapore flag'> . 'alt' attribute provides:", ["Alternative text if image fails to load", "Image size", "Image style", "Link destination"], 0, "mcq"),

        # Medium
        ("Semantic HTML: Which tag best contains navigation links?", ["<nav>", "<div>", "<span>", "<header>"], 0, "mcq"),
        ("CSS: p { color: red; } . This is an example of:", ["Element selector", "Class selector", "ID selector", "Inline style"], 0, "mcq"),
        ("Singapore school website structure: <header>, <nav>, <main>, <footer>. Which contains main content?", "<main>", None, "short"),
        ("<a href='https://moe.gov.sg'>MOE</a> . This creates:", ["Clickable link to MOE website", "Image", "Heading", "Paragraph"], 0, "mcq"),
        ("CSS box model order from inside out:", ["Content, Padding, Border, Margin", "Margin, Border, Padding, Content", "Border, Margin, Padding, Content", "Content, Border, Padding, Margin"], 0, "mcq"),

        # Hard
        ("HTML: <div class='card'><h2>Title</h2><p>Text</p></div> / CSS: .card { background: white; padding: 20px; } . Padding adds space:", ["Inside element between content and border", "Outside element beyond border", "Between elements", "Around text only"], 0, "mcq"),
        ("Responsive design: @media (max-width: 600px) { .menu { display: none; } } . This hides menu when:", ["Screen width ≤ 600px (mobile)", "Screen width > 600px", "Always", "Never"], 0, "mcq"),
        ("CSS specificity: #id vs .class vs element. Most specific:", "#id", None, "short"),
        ("Flexbox: .container { display: flex; justify-content: space-between; } . This distributes child elements:", ["With equal space between them", "Centered", "Left-aligned", "Stacked vertically"], 0, "mcq"),
        ("Singapore government website uses: <header><img src='logo.png' alt='Gov.sg'><nav><a href='/'>Home</a></nav></header> . Best practice shown:", ["Semantic tags, alt text, proper structure", "Only images", "No styling", "Complex code"], 0, "mcq")
    ]
}

print("Creating exercises for all 6 Computing chapters...\n")

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
                    "hint": "Trace through the code step by step or think about the concept carefully.",
                    "hint_zh": "逐步追踪代码或仔细思考概念。"
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
                    "hint": "Read the question carefully and consider Singapore context where applicable.",
                    "hint_zh": "仔细阅读问题,并在适用时考虑新加坡背景。"
                }

            exercises.append(exercise)

        chapter["exercises"] = exercises
        print(f"✓ {chapter['title']}: {len(exercises)} exercises created")

# Save
with open('chapters/computing-sec2-chapters.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, indent=2, ensure_ascii=False)

print(f"\n✅ All 6 Computing chapters completed with exercises!")
print(f"📊 Total exercises: {sum(len(ch['exercises']) for ch in chapters)}")
print(f"\n📊 Enhancement features:")
print(f"  • Code reading and tracing")
print(f"  • Algorithm analysis")
print(f"  • Singapore context (MRT, NRIC, GST)")
print(f"  • Problem-solving emphasis")
print(f"  • Practical programming scenarios")
