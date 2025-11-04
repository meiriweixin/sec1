"""
Create Secondary 2 Computing chapters
Aligned with Singapore MOE Computing syllabus for Sec 2
"""

import json

sec2_computing_chapters = [
    {
        "id": "algorithms-flowcharts-sec2",
        "gradeLevel": "sec2",
        "title": "Algorithms & Flowcharts",
        "title_zh": "算法与流程图",
        "description": "Algorithm design, flowcharts, pseudocode, and problem-solving strategies",
        "description_zh": "算法设计、流程图、伪代码和解决问题的策略",
        "tag": "Computational Thinking",
        "tag_zh": "计算思维",
        "objectives": [
            "Design algorithms to solve problems",
            "Create and interpret flowcharts",
            "Write pseudocode for common tasks",
            "Analyze algorithm efficiency"
        ],
        "objectives_zh": [
            "设计解决问题的算法",
            "创建和解释流程图",
            "为常见任务编写伪代码",
            "分析算法效率"
        ],
        "sections": [
            {
                "id": "what-are-algorithms",
                "type": "text",
                "title": "What are Algorithms?",
                "title_zh": "什么是算法？",
                "content": "An algorithm is a step-by-step procedure to solve a problem. Like a recipe for cooking or directions to a destination. In computing, algorithms tell computers exactly what to do. Example: Singapore MRT route planning - finding shortest path from Jurong East to Changi Airport involves an algorithm that considers all possible routes and selects the optimal one."
            },
            {
                "id": "flowchart-symbols",
                "type": "text",
                "title": "Flowchart Symbols",
                "title_zh": "流程图符号",
                "content": "Flowcharts use standard symbols: Oval (Start/End), Rectangle (Process/Action), Diamond (Decision/Question), Parallelogram (Input/Output), Arrow (Flow direction). Example: ATM withdrawal flowchart - Check PIN → Verify balance → Decision: Sufficient funds? → If Yes: Dispense cash, If No: Display error."
            },
            {
                "id": "pseudocode",
                "type": "text",
                "title": "Pseudocode Basics",
                "title_zh": "伪代码基础",
                "content": "Pseudocode is plain language description of algorithm steps, between human language and programming code. Uses keywords like IF, THEN, ELSE, WHILE, FOR, INPUT, OUTPUT. Example for finding max of 3 numbers: INPUT num1, num2, num3 / IF num1 > num2 AND num1 > num3 THEN max = num1 / ELSE IF num2 > num3 THEN max = num2 / ELSE max = num3 / OUTPUT max"
            },
            {
                "id": "algorithm-efficiency",
                "type": "text",
                "title": "Algorithm Efficiency",
                "title_zh": "算法效率",
                "content": "Efficient algorithms use fewer steps and resources. Linear search checks each item one-by-one (slow for large lists). Binary search divides search space in half each step (much faster for sorted lists). Example: Finding contact in phone with 1000 entries - Linear: up to 1000 checks, Binary: max 10 checks. Singapore government systems process millions of transactions daily, efficiency is critical."
            }
        ],
        "exercises": []
    },

    {
        "id": "python-basics-sec2",
        "gradeLevel": "sec2",
        "title": "Python Programming Basics",
        "title_zh": "Python编程基础",
        "description": "Introduction to Python programming - variables, data types, input/output, basic operations",
        "description_zh": "Python编程入门 - 变量、数据类型、输入输出、基本操作",
        "tag": "Programming",
        "tag_zh": "编程",
        "objectives": [
            "Write simple Python programs",
            "Use variables and data types correctly",
            "Perform input/output operations",
            "Apply arithmetic and comparison operators"
        ],
        "objectives_zh": [
            "编写简单的Python程序",
            "正确使用变量和数据类型",
            "执行输入输出操作",
            "应用算术和比较运算符"
        ],
        "sections": [
            {
                "id": "python-intro",
                "type": "text",
                "title": "Introduction to Python",
                "title_zh": "Python简介",
                "content": "Python is a beginner-friendly programming language used worldwide. Created by Guido van Rossum in 1991. Used by Google, NASA, Singapore government agencies. Easy to read: print('Hello Singapore!') displays text. Python is interpreted - runs line by line. Case-sensitive: 'Name' and 'name' are different."
            },
            {
                "id": "variables-data-types",
                "type": "text",
                "title": "Variables & Data Types",
                "title_zh": "变量与数据类型",
                "content": "Variables store data: age = 13, name = 'Ali', height = 1.65. Data types: int (whole numbers), float (decimals), str (text in quotes), bool (True/False). Python auto-detects type. Example: price = 5.50 (float), quantity = 3 (int), total = price * quantity (result: 16.5). Singapore context: gst_rate = 0.09, total_with_gst = price * (1 + gst_rate)"
            },
            {
                "id": "input-output",
                "type": "text",
                "title": "Input and Output",
                "title_zh": "输入与输出",
                "content": "output: print() displays information. print('Welcome!') or print(age). Input: input() gets user data as string. name = input('Enter your name: '). Convert to number: age = int(input('Enter age: ')). Example program: Calculate MRT fare - distance = float(input('Distance in km: ')) / fare = 0.77 + (distance * 0.08) / print('Fare: $' + str(fare))"
            },
            {
                "id": "operators",
                "type": "text",
                "title": "Operators in Python",
                "title_zh": "Python运算符",
                "content": "Arithmetic: + - * / (division) // (integer division) % (remainder) ** (power). Example: 17 % 5 = 2 (remainder). Comparison: == (equal) != (not equal) > < >= <=. Returns True/False. Example: age >= 13 checks if teenager. Logical: and, or, not. Example: if age >= 13 and age <= 19 then teenager. Singapore PSLE score calculation uses these operators."
            }
        ],
        "exercises": []
    },

    {
        "id": "selection-iteration-sec2",
        "gradeLevel": "sec2",
        "title": "Selection & Iteration",
        "title_zh": "选择与迭代",
        "description": "Control structures - if/else statements, loops (for and while), nested structures",
        "description_zh": "控制结构 - if/else语句、循环（for和while）、嵌套结构",
        "tag": "Programming",
        "tag_zh": "编程",
        "objectives": [
            "Implement conditional statements (if/elif/else)",
            "Use for loops for definite iteration",
            "Use while loops for indefinite iteration",
            "Apply nested control structures"
        ],
        "objectives_zh": [
            "实现条件语句（if/elif/else）",
            "使用for循环进行确定迭代",
            "使用while循环进行不确定迭代",
            "应用嵌套控制结构"
        ],
        "sections": [
            {
                "id": "if-statements",
                "type": "text",
                "title": "If Statements",
                "title_zh": "If语句",
                "content": "if statement makes decisions: if condition: do something. Use indentation (4 spaces). Example: if age >= 18: print('Can vote'). elif (else if) for multiple conditions: if score >= 75: grade = 'A' / elif score >= 60: grade = 'B' / else: grade = 'C'. Singapore O-Level grading uses multiple conditions."
            },
            {
                "id": "for-loops",
                "type": "text",
                "title": "For Loops",
                "title_zh": "For循环",
                "content": "for loop repeats known number of times. range(n) generates 0 to n-1. Example: for i in range(5): print(i) outputs 0,1,2,3,4. range(start, stop, step): range(1, 10, 2) gives 1,3,5,7,9. Calculate total: total = 0 / for i in range(1, 6): total = total + i / Result: 15. Used in Singapore bus arrival times app to check next 5 buses."
            },
            {
                "id": "while-loops",
                "type": "text",
                "title": "While Loops",
                "title_zh": "While循环",
                "content": "while loop repeats while condition is True. Example: count = 1 / while count <= 5: print(count) / count = count + 1. Use when repetitions unknown. ATM PIN validation: attempts = 0 / while attempts < 3: pin = input('Enter PIN: ') / if pin == '1234': break / attempts = attempts + 1 / else: print('Card blocked'). Important: ensure loop eventually ends (no infinite loops)."
            },
            {
                "id": "nested-structures",
                "type": "text",
                "title": "Nested Structures",
                "title_zh": "嵌套结构",
                "content": "Loops and if statements can be nested (one inside another). Example: Print multiplication table: for row in range(1, 4): / for col in range(1, 4): / product = row * col / print(product, end=' ') / print(). Singapore class seating arrangement uses nested loops to assign seats by row and column."
            }
        ],
        "exercises": []
    },

    {
        "id": "data-structures-sec2",
        "gradeLevel": "sec2",
        "title": "Lists & Strings",
        "title_zh": "列表与字符串",
        "description": "Working with lists (arrays) and string manipulation in Python",
        "description_zh": "在Python中使用列表（数组）和字符串操作",
        "tag": "Programming",
        "tag_zh": "编程",
        "objectives": [
            "Create and manipulate lists",
            "Access list elements using indices",
            "Perform string operations and methods",
            "Iterate through lists and strings"
        ],
        "objectives_zh": [
            "创建和操作列表",
            "使用索引访问列表元素",
            "执行字符串操作和方法",
            "遍历列表和字符串"
        ],
        "sections": [
            {
                "id": "lists-basics",
                "type": "text",
                "title": "Lists in Python",
                "title_zh": "Python列表",
                "content": "List stores multiple values: students = ['Ali', 'Bala', 'Chen']. Access by index (starts at 0): students[0] is 'Ali'. Negative index from end: students[-1] is 'Chen'. Length: len(students) = 3. Add: students.append('Devi'). Remove: students.remove('Ali'). Example: Singapore MRT stations list - stations = ['Jurong East', 'Clementi', 'Buona Vista', 'Outram Park']."
            },
            {
                "id": "list-operations",
                "type": "text",
                "title": "List Operations",
                "title_zh": "列表操作",
                "content": "Slicing: numbers[1:4] gets elements at index 1,2,3. numbers[:3] first 3 elements. numbers[2:] from index 2 to end. Concatenate: list1 + list2. Repeat: [0] * 5 creates [0,0,0,0,0]. Check membership: if 'Ali' in students. Sort: numbers.sort() arranges in order. Reverse: numbers.reverse(). Used in Singapore e-commerce sites to manage shopping cart items."
            },
            {
                "id": "strings",
                "type": "text",
                "title": "String Manipulation",
                "title_zh": "字符串操作",
                "content": "Strings are sequences of characters. Access like lists: name = 'Singapore' / name[0] is 'S'. Length: len(name) = 9. Methods: upper(), lower(), strip(), split(), replace(). Example: message = '  Hello World  ' / message.strip() removes spaces = 'Hello World' / message.split() creates ['Hello', 'World']. Check substring: if 'ore' in name (True). Used in Singapore NRIC validation."
            },
            {
                "id": "iterating-collections",
                "type": "text",
                "title": "Iterating Through Collections",
                "title_zh": "遍历集合",
                "content": "Use for loop to process each element. For list: for student in students: print(student). For string: for char in 'Singapore': print(char). With index: for i in range(len(students)): print(i, students[i]). Example: Calculate average - scores = [85, 92, 78, 90] / total = 0 / for score in scores: total = total + score / average = total / len(scores). Singapore temperature monitoring system processes daily readings this way."
            }
        ],
        "exercises": []
    },

    {
        "id": "functions-modules-sec2",
        "gradeLevel": "sec2",
        "title": "Functions & Modules",
        "title_zh": "函数与模块",
        "description": "Creating reusable functions, parameters, return values, and using Python modules",
        "description_zh": "创建可重用函数、参数、返回值和使用Python模块",
        "tag": "Programming",
        "tag_zh": "编程",
        "objectives": [
            "Define and call functions",
            "Use parameters and return values",
            "Understand scope of variables",
            "Import and use Python modules"
        ],
        "objectives_zh": [
            "定义和调用函数",
            "使用参数和返回值",
            "理解变量的作用域",
            "导入和使用Python模块"
        ],
        "sections": [
            {
                "id": "defining-functions",
                "type": "text",
                "title": "Defining Functions",
                "title_zh": "定义函数",
                "content": "Function is reusable block of code. Define with def: def greet(): / print('Hello!'). Call: greet(). With parameters: def greet(name): / print('Hello ' + name + '!'). Multiple parameters: def add(a, b): / result = a + b / return result. Example: Singapore GST calculator - def add_gst(price): / gst = price * 0.09 / total = price + gst / return total"
            },
            {
                "id": "return-values",
                "type": "text",
                "title": "Return Values",
                "title_zh": "返回值",
                "content": "return sends value back to caller. Function stops at return. Example: def max_of_two(a, b): / if a > b: return a / else: return b. Use returned value: largest = max_of_two(10, 15) / print(largest). Can return multiple values as tuple: def min_max(numbers): / return min(numbers), max(numbers). Singapore grade calculator returns grade and points."
            },
            {
                "id": "variable-scope",
                "type": "text",
                "title": "Variable Scope",
                "title_zh": "变量作用域",
                "content": "Local variables exist only inside function. Global variables exist everywhere. Example: total = 0 (global) / def add_score(score): / total = total + score (Error! Can't modify global in function) / Use global keyword or pass as parameter. Best practice: minimize global variables. Example: Singapore point-of-sale system uses local variables in each transaction function for safety."
            },
            {
                "id": "modules",
                "type": "text",
                "title": "Python Modules",
                "title_zh": "Python模块",
                "content": "Module is file containing Python code you can import. Built-in modules: math, random, datetime. Import: import math / math.sqrt(16) = 4.0. Import specific: from random import randint / dice = randint(1, 6). Create own module: Save functions in file 'mytools.py', then import mytools. Singapore apps use datetime module for scheduling: from datetime import datetime / now = datetime.now() / print(now.strftime('%d/%m/%Y %H:%M'))"
            }
        ],
        "exercises": []
    },

    {
        "id": "web-html-css-sec2",
        "gradeLevel": "sec2",
        "title": "Web Development Basics",
        "title_zh": "网页开发基础",
        "description": "HTML structure, CSS styling, and basic web page creation",
        "description_zh": "HTML结构、CSS样式和基本网页创建",
        "tag": "Web Technologies",
        "tag_zh": "网络技术",
        "objectives": [
            "Create HTML web pages with proper structure",
            "Apply CSS styles to HTML elements",
            "Use semantic HTML tags",
            "Design responsive layouts"
        ],
        "objectives_zh": [
            "创建具有正确结构的HTML网页",
            "将CSS样式应用于HTML元素",
            "使用语义化HTML标签",
            "设计响应式布局"
        ],
        "sections": [
            {
                "id": "html-basics",
                "type": "text",
                "title": "HTML Fundamentals",
                "title_zh": "HTML基础",
                "content": "HTML (HyperText Markup Language) structures web content. Uses tags: <tag>content</tag>. Basic structure: <!DOCTYPE html> <html> <head> <title>Page Title</title> </head> <body> <h1>Main Heading</h1> <p>Paragraph text.</p> </body> </html>. Common tags: <h1>-<h6> headings, <p> paragraph, <img> image, <a> link. Singapore government websites use HTML for all pages."
            },
            {
                "id": "semantic-html",
                "type": "text",
                "title": "Semantic HTML",
                "title_zh": "语义化HTML",
                "content": "Semantic tags describe meaning: <header>, <nav>, <main>, <article>, <section>, <aside>, <footer>. Better than generic <div>. Example: Singapore school website - <header> contains logo and menu, <nav> has navigation links, <main> contains main content, <article> for news posts, <footer> for contact info. Benefits: Accessibility (screen readers), SEO (search engines understand structure)."
            },
            {
                "id": "css-basics",
                "type": "text",
                "title": "CSS Styling",
                "title_zh": "CSS样式",
                "content": "CSS (Cascading Style Sheets) makes pages beautiful. Selectors target elements. Inline: <p style='color: red;'>. Internal: <style> p { color: red; } </style>. External (best): <link rel='stylesheet' href='style.css'>. Properties: color, background-color, font-size, margin, padding, border. Example: Singapore flag colors - .red { background-color: #EF3340; } .white { background-color: #FFFFFF; }"
            },
            {
                "id": "css-layout",
                "type": "text",
                "title": "CSS Layout & Responsive Design",
                "title_zh": "CSS布局与响应式设计",
                "content": "Box model: content, padding, border, margin. Display: block (full width), inline (in line), flex (flexible layout). Position: static, relative, absolute, fixed. Responsive design adapts to screen sizes. Media queries: @media (max-width: 600px) { /* mobile styles */ }. Singapore government sites use responsive design for mobile access. Flexbox example: display: flex; justify-content: center; align-items: center;"
            }
        ],
        "exercises": []
    }
]

print(f"📚 Creating {len(sec2_computing_chapters)} Secondary 2 Computing chapters...")
print(f"   Computational Thinking: {sum(1 for ch in sec2_computing_chapters if ch['tag'] == 'Computational Thinking')}")
print(f"   Programming: {sum(1 for ch in sec2_computing_chapters if ch['tag'] == 'Programming')}")
print(f"   Web Technologies: {sum(1 for ch in sec2_computing_chapters if ch['tag'] == 'Web Technologies')}")

# Save
with open('chapters/computing-sec2-chapters.json', 'w', encoding='utf-8') as f:
    json.dump(sec2_computing_chapters, f, indent=2, ensure_ascii=False)

print(f"\n✅ Created {len(sec2_computing_chapters)} chapters")
print(f"📁 Saved to: chapters/computing-sec2-chapters.json")
print(f"\n⚠️ Note: Exercises need to be added separately")
