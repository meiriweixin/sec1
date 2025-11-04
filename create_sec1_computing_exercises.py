"""
Create exercises for Secondary 1 Computing chapters
Foundation level - accessible but rigorous
"""

import json

# Load chapters
with open('chapters/computing-sec1-chapters.json', 'r', encoding='utf-8') as f:
    chapters = json.load(f)

exercise_data = {
    "digital-devices-sec1": [
        ("Which component is the brain of the computer?", ["CPU", "RAM", "Hard Drive", "Motherboard"], 0, "mcq"),
        ("RAM stores data:", "temporarily while computer is on", None, "short"),
        ("Which is an input device?", ["Monitor", "Printer", "Keyboard", "Speakers"], 2, "mcq"),
        ("Which is both input AND output?", ["Keyboard", "Mouse", "Touchscreen", "Printer"], 2, "mcq"),
        ("Storage device that permanently saves files:", ["RAM", "CPU", "Hard Drive/SSD", "Monitor"], 2, "mcq"),

        ("Input-Process-Output cycle: When you type in Word and save, which is the OUTPUT?", ["Typing on keyboard", "CPU processing", "File saved to storage", "Opening Word"], 2, "mcq"),
        ("Singapore student downloads 500MB video. Which component stores it permanently?", ["RAM (temporary)", "Hard Drive/SSD (permanent)", "CPU", "Motherboard"], 1, "mcq"),
        ("16GB RAM vs 8GB RAM. Advantage of 16GB:", "can run more programs simultaneously", None, "short"),
        ("Which device is NOT a computer?", ["Desktop", "Smartphone", "Calculator watch", "Electric kettle"], 3, "mcq"),
        ("Embedded system example:", ["Laptop", "Tablet", "ATM machine", "Desktop"], 2, "mcq"),

        ("Singapore Singpass app requires smartphone with camera (input), display (output), and:", ["Internet connection for processing", "Printer", "Scanner", "USB port"], 0, "mcq"),
        ("SSD vs Hard Drive: SSD advantage is:", ["Faster, no moving parts, more durable", "Cheaper only", "Larger capacity only", "Makes noise"], 0, "mcq"),
        ("Computer with 8GB RAM and 256GB SSD. How much data lost when powered off?", "Data in RAM (8GB) lost, SSD data remains", None, "short"),
        ("Motherboard function:", ["Connects all computer components", "Processes data", "Stores files", "Displays images"], 0, "mcq"),
        ("Singapore EZ-Link card reader: Input device reads card, output device:", ["Displays fare deducted", "Prints receipt", "Makes sound", "All of the above"], 3, "mcq")
    ],

    "intro-algorithms-sec1": [
        ("Algorithm is:", ["Step-by-step instructions", "Programming language", "Type of computer", "A software"], 0, "mcq"),
        ("Good algorithm must be:", "clear, ordered, and finite", None, "short"),
        ("Pattern: 3, 6, 9, 12. Next number:", ["13", "14", "15", "16"], 2, "mcq"),
        ("Decomposition means:", ["Breaking problem into smaller parts", "Putting parts together", "Ignoring details", "Solving quickly"], 0, "mcq"),
        ("Abstraction focuses on:", ["Important information only", "All details", "Unimportant things", "Random data"], 0, "mcq"),

        ("Algorithm to make Milo: Step 3 should be:", ["Drink immediately", "Pour hot water", "Buy Milo tin", "Wash cup"], 1, "mcq"),
        ("Sequence 2, 4, 8, 16. Pattern rule:", ["Multiply by 2", "Add 2", "Divide by 2", "Add 4"], 0, "mcq"),
        ("Singapore postal code pattern: First 2 digits represent:", "district/sector", None, "short"),
        ("To solve Go to Sentosa, decompose into steps. Which is NOT needed?", ["Check MRT route", "Take MRT to HarbourFront", "Buy new shoes", "Board Sentosa Express"], 2, "mcq"),
        ("MRT map uses abstraction by:", ["Showing only stations and lines, not exact distances", "Showing every street", "Showing building heights", "Showing weather"], 0, "mcq"),

        ("Algorithm: 1) Input number, 2) Multiply by 2, 3) Add 5, 4) Output. For input 10, output:", ["25", "15", "20", "30"], 0, "mcq"),
        ("Pattern recognition: Singapore bus 14, 14A, 14e. What do they share?", ["Same main route, different variations", "All go to same final stop", "Same bus company only", "Random numbers"], 0, "mcq"),
        ("Which is NOT a characteristic of good algorithm?", "ambiguous steps", None, "short"),
        ("Decompose planning class party into smaller tasks. Which makes sense?", ["Assign food, decorations, games to different groups", "One person does everything", "Do everything at once", "Start without planning"], 0, "mcq"),
        ("Abstraction example in Singapore context:", ["NRIC shows important ID info, not full family tree", "Passport shows all personal history", "Report card shows every single test", "Bank statement shows future predictions"], 0, "mcq")
    ],

    "block-programming-sec1": [
        ("Block programming uses:", ["Visual colorful blocks", "Only text code", "Math equations", "Binary code"], 0, "mcq"),
        ("Popular block programming tool by MIT:", "Scratch", None, "short"),
        ("Blocks execute in what order?", ["Top to bottom", "Bottom to top", "Random order", "Left to right"], 0, "mcq"),
        ("Repeat 5 block will run code inside:", ["5 times", "1 time", "10 times", "Forever"], 0, "mcq"),
        ("If-Then block is used for:", ["Making decisions", "Repeating", "Starting program", "Ending program"], 0, "mcq"),

        ("Code: Move 10 steps, Turn 90 degrees, Move 10 steps. Sprite moves:", ["L-shape", "Square", "Circle", "Straight line"], 0, "mcq"),
        ("Repeat 4: Move 50, Turn 90. This draws:", ["Square", "Triangle", "Circle", "Line"], 0, "mcq"),
        ("Forever loop continues:", "until program stopped", None, "short"),
        ("If temperature > 30 Then Say Hot. For temperature = 25, what happens?", ["Nothing (condition false)", "Says Hot", "Error", "Repeats"], 0, "mcq"),
        ("Advantage of loops over repeating code:", ["Less code, easier to change", "More code", "Slower", "More errors"], 0, "mcq"),

        ("Singapore flag: Background red, Draw crescent and stars. If steps reversed (stars before background):", ["Stars hidden behind red background", "No difference", "Error", "Faster"], 0, "mcq"),
        ("Code: Repeat Until touching edge: Move 5. This creates:", ["Sprite moves until hits wall", "Infinite loop", "No movement", "One move only"], 0, "mcq"),
        ("If score > 50 Then Say Pass, Else Say Fail. For score = 50:", "Say Fail", None, "short"),
        ("To make sprite dance (move left-right repeatedly), use:", ["Forever loop with movement", "One move command", "If statement only", "Turn only"], 0, "mcq"),
        ("Debugging means:", ["Finding and fixing errors in code", "Writing new code", "Deleting program", "Running code"], 0, "mcq")
    ],

    "digital-data-sec1": [
        ("Computers understand only:", ["0 and 1 (binary)", "English", "All languages", "Math"], 0, "mcq"),
        ("1 byte equals:", "8 bits", None, "short"),
        ("File extension .docx represents:", ["Word document", "Image", "Video", "Audio"], 0, "mcq"),
        ("Image file extension:", [".jpg", ".mp3", ".docx", ".exe"], 0, "mcq"),
        ("1000 bytes equals:", ["1 KB", "1 MB", "1 GB", "1 TB"], 0, "mcq"),

        ("Singapore government forms often use which format?", [".pdf", ".exe", ".mp3", ".gif"], 0, "mcq"),
        (".mp4 file is:", ["Video", "Audio", "Document", "Image"], 0, "mcq"),
        ("Compressed file format:", ".zip", None, "short"),
        ("Good folder structure for student:", ["School/Math/Homework", "Everything in one folder", "Random names", "No folders"], 0, "mcq"),
        ("Path C:/Users/Student/Documents/Essay.docx. Essay.docx is in:", ["Documents folder", "Users folder", "C drive root", "Student folder"], 0, "mcq"),

        ("Photo = 5MB, Movie = 2GB. How many photos equal movie size?", ["About 400 photos", "10 photos", "2 photos", "5000 photos"], 0, "mcq"),
        ("Typical smartphone storage:", ["64-256 GB", "1-5 MB", "500 KB", "10 TB"], 0, "mcq"),
        ("Binary for decimal 5:", "101", None, "short"),
        ("To reduce file size for email attachment:", ["Compress to .zip", "Rename file", "Copy file", "Print file"], 0, "mcq"),
        ("Cloud storage advantage:", ["Access files anywhere with internet", "Faster computer", "Better graphics", "Free unlimited storage"], 0, "mcq")
    ],

    "internet-safety-sec1": [
        ("Internet is:", ["Worldwide network of connected computers", "One big computer", "Only for games", "Singapore network only"], 0, "mcq"),
        ("DNS translates:", "website names to IP addresses", None, "short"),
        ("Strong password should have:", ["8+ characters, letters, numbers, symbols", "Just your name", "1234", "Your birthday"], 0, "mcq"),
        ("IP address is like:", ["Postal code for computer", "Person name", "Website content", "Password"], 0, "mcq"),
        ("Phishing is:", ["Fake messages to steal info", "Catching fish online", "Valid email", "Gaming"], 0, "mcq"),

        ("Someone asks for your NRIC online. You should:", ["Not share it", "Share freely", "Post publicly", "Email it"], 0, "mcq"),
        ("Cyberbullying victim should:", ["Tell adult/teacher", "Ignore forever", "Respond angrily", "Delete account"], 0, "mcq"),
        ("Website scamalert.sg is for:", "reporting scams in Singapore", None, "short"),
        ("Email: You won free iPhone! Click here! This is likely:", ["Scam/phishing", "Real prize", "Official Apple", "School email"], 0, "mcq"),
        ("Digital footprint means:", ["Trail of data you leave online", "Foot measurement", "App icon", "Website design"], 0, "mcq"),

        ("Singapore student posts embarrassing photo. It can:", ["Stay online permanently", "Disappear next day", "Only you can see", "Teachers cannot find"], 0, "mcq"),
        ("Before posting online, ask yourself:", ["Would I want teachers/parents to see this?", "Is it funny?", "Will it go viral?", "Is it long?"], 0, "mcq"),
        ("Malware protection:", "use antivirus and avoid untrusted downloads", None, "short"),
        ("Privacy setting on social media should be:", ["Set to private/friends only", "Public for everyone", "No settings needed", "Default is fine"], 0, "mcq"),
        ("Received suspicious link from stranger. You should:", ["Do not click, report/delete", "Click to see", "Forward to friends", "Save for later"], 0, "mcq")
    ],

    "productivity-tools-sec1": [
        ("Word processor example:", ["Microsoft Word", "Excel", "PowerPoint", "Chrome"], 0, "mcq"),
        ("To make text bold in Word:", "select text and click Bold button", None, "short"),
        ("Presentation software:", ["PowerPoint", "Word", "Excel", "Notepad"], 0, "mcq"),
        ("Spreadsheet cell A1 means:", ["Column A, Row 1", "Row A, Column 1", "First alphabet", "Random code"], 0, "mcq"),
        ("Formula in Excel starts with:", ["=", "+", "*", "#"], 0, "mcq"),

        ("Good presentation rule: Max words per slide:", ["About 30-36 (6x6 rule)", "Unlimited", "5 words total", "200 words"], 0, "mcq"),
        ("Google Docs advantage over Word:", ["Multiple people can edit simultaneously", "Only one person at a time", "Needs installation", "Works offline only"], 0, "mcq"),
        ("In Excel, =SUM(A1:A5) calculates:", "total of cells A1 to A5", None, "short"),
        ("To export document for submission (cannot be edited):", ["Save as PDF", "Keep as .docx", "Print only", "Email link"], 0, "mcq"),
        ("Singapore student group project. Best collaboration tool:", ["Google Workspace", "Individual Word files", "Paper notes", "Phone calls only"], 0, "mcq"),

        ("Presentation tip: Use images because:", ["Visual information easier to remember", "Fill space", "Look fancy", "Required always"], 0, "mcq"),
        ("Spreadsheet to track pocket money. Column for remaining money uses:", ["Formula: Received minus Spent", "Just type number", "Copy from internet", "Random guess"], 0, "mcq"),
        ("Bar chart vs Pie chart. Pie chart best for:", "showing parts of a whole", None, "short"),
        ("Collaborating online: Best practice is:", ["Communicate clearly and complete your part on time", "Wait for others", "Ignore messages", "Work alone"], 0, "mcq"),
        ("Singapore schools use which platform for online learning?", ["Google Classroom or Microsoft Teams", "Facebook", "WhatsApp only", "YouTube only"], 0, "mcq")
    ]
}

print("Creating exercises for Sec 1 Computing...\n")

for chapter in chapters:
    ch_id = chapter["id"]
    if ch_id in exercise_data:
        exercises = []
        for q_num, q_data in enumerate(exercise_data[ch_id], 1):
            difficulty = "easy" if q_num <= 5 else ("medium" if q_num <= 10 else "hard")
            prompt, choices_or_answer, answer_or_none, q_type = q_data

            if q_type == "short":
                exercise = {
                    "id": f"{ch_id.replace('-sec1', '')}-q{q_num}",
                    "type": "short",
                    "difficulty": difficulty,
                    "prompt": prompt,
                    "prompt_zh": f"[{chapter['title']} - 问题 {q_num}]",
                    "answer": choices_or_answer,
                    "validator": "exact",
                    "hint": "Think about the key concept and Singapore examples.",
                    "hint_zh": "考虑关键概念和新加坡例子。"
                }
            else:
                exercise = {
                    "id": f"{ch_id.replace('-sec1', '')}-q{q_num}",
                    "type": "mcq",
                    "difficulty": difficulty,
                    "prompt": prompt,
                    "prompt_zh": f"[{chapter['title']} - 问题 {q_num}]",
                    "choices": choices_or_answer,
                    "answer": answer_or_none,
                    "hint": "Consider how technology works in daily life.",
                    "hint_zh": "考虑技术在日常生活中的应用。"
                }
            exercises.append(exercise)

        chapter["exercises"] = exercises
        print(f"✓ {chapter['title']}: {len(exercises)} exercises")

# Save
with open('chapters/computing-sec1-chapters.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, indent=2, ensure_ascii=False)

print(f"\n✅ Sec 1 Computing exercises complete!")
print(f"📊 Total: {sum(len(ch['exercises']) for ch in chapters)} exercises")
