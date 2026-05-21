import os
import json
import re

db_path = 'database'

# Mascots and their descriptions/emojis
mascots = {
    'senior_csharp': ('Leo the Coding Lion 🦁', 'Leo', '🦁'),
    'senior_flutter': ('Dash the Bluebird 🐦', 'Dash', '🐦'),
    'senior_react_native': ('Pixel the Smart Dog 🐶', 'Pixel', '🐶'),
    'senior_cyber_security': ('Shieldy the Tech Turtle 🐢', 'Shieldy', '🐢'),
    'senior_network_hacking': ('Detective Owl 🦉', 'Detective Owl', '🦉'),
    'senior_ui_ux': ('Bella the Panda Artist 🐼', 'Bella', '🐼'),
    'senior_laravel_web': ('Robo-Elephant 🐘', 'Robo-Elephant', '🐘'),
    'senior_laravel_mobile': ('Artisan Beaver 🦫', 'Artisan Beaver', '🦫'),
    'senior_mit_app': ('Milo the Mobile Monkey 🐵', 'Milo', '🐵'),
    'senior_python_problem_solving': ('Py-Python 🐍', 'Py-Python', '🐍')
}

# Pre-designed progression paths for csharp, flutter, react_native (which have 0 recap sessions)
csharp_sessions = [
    ("Welcome to C# & Visual Studio", "Introduction to game engines, IDE setup, and running your first desktop window.", ["Setup IDE", "Run Hello World"], "print('Welcome to C#!')"),
    ("Variables & Smart Data Types", "Learn int, float, string, and bool to store game scores and usernames.", ["Create variables", "Understand datatypes"], "score = 100\nprint(score)"),
    ("Arithmetic & Comparisons", "Add, subtract, and compare variables to control game elements.", ["Math operators", "Compare values"], "print(50 * 2)"),
    ("Smart Conditionals (If-Else)", "Write smart branches to decide if a player wins or loses based on points.", ["If statements", "Else branches"], "if score >= 50:\n    print('Pass')"),
    ("Switch Cases for Decisions", "Clean up nested conditions with clean, multi-choice switch cases.", ["Switch syntax", "Break statements"], "print('Choice A')"),
    ("While Loops & Conditions", "Repeat coding instructions until a magic condition becomes true.", ["While loops", "Loop safety"], "print('Repeating...')"),
    ("For Loops & Dynamic Grids", "Count and build perfect repeating rows and grids with For loops.", ["For loops", "Counters"], "for i in range(5):\n    print('Grid Cell')"),
    ("Storing Lists inside Arrays", "Store groups of gold coins and enemy names inside structured arrays.", ["Array structures", "Indexes"], "print('Array of size 5')"),
    ("Methods & Fun Functions", "Write reusable blocks of code that take parameters and return results.", ["Method parameters", "Return types"], "print('Function active')"),
    ("Classes & Object-Oriented C#", "Understand Object-Oriented Programming (OOP) classes and real instances.", ["OOP Classes", "Instances"], "print('Class Instance')"),
    ("Constructors & Object Creation", "Initialize your classes instantly using constructor methods.", ["Constructors", "Arguments"], "print('Object created')"),
    ("Inheritance & Smart Subclasses", "Derive child classes from parents to inherit special game behaviors.", ["Base classes", "Inherited fields"], "print('Child Inherited')"),
    ("Encapsulation & Access Modifiers", "Protect class fields using public and private keywords.", ["Access modifiers", "Getters/Setters"], "print('Encapsulation OK')"),
    ("Exception Handling (Try-Catch)", "Catch and resolve unexpected coding errors safely without crashing.", ["Try-catch blocks", "Exceptions"], "print('Error Handled')"),
    ("Lists & Dynamic Generics", "Use dynamic List structures that shrink and grow automatically.", ["List generic type", "Add/Remove methods"], "print('List active')"),
    ("Intro to Windows Forms UI", "Design graphic window frames and add buttons and text areas.", ["Form controls", "UI design"], "print('Form Loaded')"),
    ("Windows Forms Advanced Layouts", "Position and align text controls, background colors, and labels.", ["Layout layouts", "Padding/margins"], "print('Layout configured')"),
    ("Events & Event Handlers", "Capture mouse clicks and button pressed actions to trigger code.", ["Event handlers", "Delegate triggers"], "print('Event triggered')"),
    ("Building a Calculator App", "Assemble a functional calculator using forms, variables, and math.", ["Form arithmetic", "State updates"], "print('Calculator active')"),
    ("Database & Data Persistence", "Connect C# apps to local databases to save player progress.", ["Local DB connection", "SQL commands"], "print('DB connected')"),
    ("Reading & Writing Files", "Save player highscores permanently into text files on the disk.", ["StreamReader", "StreamWriter"], "print('File saved')"),
    ("Building a Tic-Tac-Toe Game", "Design a two-player grid board with victory validation algorithms.", ["Grid validation", "Turn management"], "print('Winner validated')"),
    ("Game Architecture in C#", "Master standard loops, physics updates, and game structure.", ["Game loops", "Delta timing"], "print('Engine started')"),
    ("Mega Desktop Graduation Project", "Assemble the final desktop hero app with UI, databases, and logic.", ["Final integration", "Polishing"], "print('Graduation complete')")
]

flutter_sessions = [
    ("Welcome to Flutter & Mobile Dev", "Set up Dart, install Flutter SDK, and boot the virtual phone simulator.", ["Flutter install", "SDK setup"], "print('Flutter Ready!')"),
    ("Dart Syntax & Variables", "Store player progress and app names inside Dart data type containers.", ["Dart variables", "Main function"], "name = 'Rowan'\nprint(name)"),
    ("Dart Classes & Subclasses", "Design reusable components using Dart classes and properties.", ["Dart OOP", "Class constructs"], "print('Dart Class')"),
    ("Stateless vs Stateful Widgets", "Learn the building blocks of mobile screens and widgets that change dynamically.", ["Stateless widgets", "Stateful widgets"], "print('Widgets active')"),
    ("Layouts with Columns & Rows", "Structure mobile components vertically (Column) and horizontally (Row).", ["Column layout", "Row positioning"], "print('Layout active')"),
    ("Scrolling Lists with ListView", "Load dynamic list rows that scroll smoothly without screen lag.", ["ListView builders", "Card elements"], "print('List scrolling')"),
    ("Forms & TextField Inputs", "Create secure login and checkout form fields that collect inputs.", ["TextField", "Form validation"], "print('Form submitted')"),
    ("Navigation & App Screens", "Teleport users between different screens using standard Navigator routes.", ["MaterialPageRoute", "Navigator push"], "print('Screen loaded')"),
    ("State Management Basics", "Sync and refresh data across multiple widget screens automatically.", ["State variables", "setState updates"], "print('State updated')"),
    ("Fetching API Data online", "Connect your app to the cloud to fetch real-time weather or post data.", ["HTTP client", "JSON decoding"], "print('API loaded')"),
    ("Local Storage Preferences", "Save user login states and themes locally inside phone memory.", ["Shared Preferences", "Save key/value"], "print('Preferences saved')"),
    ("Mega Flutter Graduation Project", "Deploy a complete dynamic mobile app with beautiful responsive screens.", ["App assembly", "Export apk"], "print('Flutter app active')")
]

react_native_sessions = [
    ("Welcome to React Native & Expo", "Initialize React Native, install Expo Go, and preview code on your phone.", ["Expo setup", "App component"], "print('Expo active!')"),
    ("JS ES6 Essentials & Logic", "Learn arrow functions, destructured variables, and smart arrays.", ["ES6 variables", "Arrow methods"], "user = 'Pixel'\nprint(user)"),
    ("View, Text & Image Components", "Display custom texts, visual panels, and photos on mobile interfaces.", ["View element", "Text & Image"], "print('Component rendered')"),
    ("Flexbox Mobile Grid Styling", "Position cards and stretch headers responsively using CSS Flexbox layout.", ["Flex direction", "Align items"], "print('Flexbox active')"),
    ("Stateful Hooks with useState", "Update values and change scores instantly when the user taps elements.", ["useState hook", "State changes"], "print('State changed')"),
    ("FlatList Scrolling Components", "Render extremely large grids and rows of products efficiently.", ["FlatList render", "Key extractor"], "print('FlatList loaded')"),
    ("TextInputs & Button Triggers", "Create secure input fields and interactive primary buttons.", ["TextInput focus", "Button onPress"], "print('Input saved')"),
    ("React Navigation Screens", "Build multi-screen apps with bottom tabs and sliding drawer menus.", ["NavigationContainer", "Stack navigator"], "print('Tab active')"),
    ("Fetching Online Web Data", "Make live asynchronous web requests to read API data in JSON format.", ["Fetch API", "Async await"], "print('Fetch success')"),
    ("AsyncStorage Local Database", "Save items permanently inside the phone's local storage database.", ["AsyncStorage set", "AsyncStorage get"], "print('Storage active')"),
    ("Native Features & Cameras", "Unlock phone cameras, alert dialogs, and GPS location coordinates.", ["Native sensors", "Permissions"], "print('Camera active')"),
    ("Mega React Native Graduation Project", "Compile and polish a gorgeous mobile social application for pets.", ["App compilation", "Final polishing"], "print('Social App active')")
]

def get_badge_emoji(title):
    t = title.lower()
    if any(k in t for k in ["setup", "install", "welcome", "introduction", "pillar"]):
        return "🚀"
    if any(k in t for k in ["variable", "datatype", "syntax", "operator", "math", "logic", "condition", "if", "loop", "method", "class", "oop", "code", "problem"]):
        return "💻"
    if any(k in t for k in ["layout", "ui", "ux", "design", "screen", "widget", "flexbox", "column", "row", "card"]):
        return "📱"
    if any(k in t for k in ["sound", "audio", "music", "play"]):
        return "🔊"
    if any(k in t for k in ["db", "database", "save", "local", "preference", "storage", "file", "migration", "seed"]):
        return "💾"
    if any(k in t for k in ["cyber", "security", "hacking", "firewall", "sandbox", "malware", "key", "crypt"]):
        return "🛡️"
    if any(k in t for k in ["project", "pong", "calculator", "shop", "graduation", "culmination", "mega"]):
        return "🏆"
    return "🎯"

def clean_title(title):
    cleaned = "".join(c for c in title if ord(c) < 0xFFFF)
    cleaned = re.sub(r'^(Session\s+\d+:\s*|💡\s*Session\s+\d+:\s*|✨\s*Session\s+\d+:\s*|🚀\s*Session\s+\d+:\s*|🎯\s*Session\s+\d+:\s*)', '', cleaned, flags=re.IGNORECASE)
    return cleaned.strip()

for course_id, (mascot_fullname, mascot_name, mascot_emoji) in mascots.items():
    recap_file = os.path.join(db_path, course_id, 'recap.json')
    print(f"Processing course: {course_id}...")
    
    # 1. Determine Sessions Data
    sessions_data = []
    course_title_name = course_id.replace('senior_', '').replace('_', ' ').title()
    if course_id == 'senior_csharp':
        course_title_name = "C# Desktop Application Development"
        for idx, (title, desc, targets, verify_code) in enumerate(csharp_sessions):
            sessions_data.append({
                "session_num": idx + 1,
                "session_title": title,
                "desc": desc,
                "targets": targets,
                "verify_code": verify_code,
                "points": [{"title": title, "desc": desc, "example": verify_code}]
            })
    elif course_id == 'senior_flutter':
        course_title_name = "Flutter & Dart Mobile Development"
        for idx, (title, desc, targets, verify_code) in enumerate(flutter_sessions):
            sessions_data.append({
                "session_num": idx + 1,
                "session_title": title,
                "desc": desc,
                "targets": targets,
                "verify_code": verify_code,
                "points": [{"title": title, "desc": desc, "example": verify_code}]
            })
    elif course_id == 'senior_react_native':
        course_title_name = "React Native Mobile App Development"
        for idx, (title, desc, targets, verify_code) in enumerate(react_native_sessions):
            sessions_data.append({
                "session_num": idx + 1,
                "session_title": title,
                "desc": desc,
                "targets": targets,
                "verify_code": verify_code,
                "points": [{"title": title, "desc": desc, "example": verify_code}]
            })
    else:
        # Load from recap.json
        if not os.path.exists(recap_file):
            print(f"Warning: recap.json not found for {course_id}!")
            continue
            
        with open(recap_file, 'r', encoding='utf-8') as f:
            recap = json.load(f)
            
        course_title_name = recap.get('course_title') or recap.get('course') or course_title_name
        
        for idx, s in enumerate(recap.get('sessions', [])):
            s_num = s.get('session_num') or (idx + 1)
            s_title = s.get('session_title') or f"Session {s_num}"
            s_title_clean = clean_title(s_title)
            
            # Extract points
            points = s.get('points', [])
            points_formatted = []
            for p in points:
                p_title = p.get('title') or p.get('name') or s_title_clean
                p_desc = p.get('desc') or p.get('description') or "Learn all concepts taught in this session."
                p_ex = p.get('example') or ""
                points_formatted.append({"title": p_title, "desc": p_desc, "example": p_ex})
                
            targets = s.get('targets', [f"Master the core rules of {s_title_clean}", "Complete hands-on simulator tasks"])
            project = s.get('project') or f"{s_title_clean} Practical Challenge"
            
            # Generate verification phrase
            verify_phrase = f"{s_title_clean} activated successfully!"
            verify_code = f"print('{verify_phrase}')"
            
            sessions_data.append({
                "session_num": s_num,
                "session_title": s_title_clean,
                "desc": f"Master {s_title_clean} concepts and boost your developer XP!",
                "targets": targets,
                "project": project,
                "points": points_formatted,
                "verify_code": verify_code
            })
            
    # 2. Compile Stations
    stations = []
    for s in sessions_data:
        s_num = s["session_num"]
        title_clean = clean_title(s["session_title"])
        badge_emoji = get_badge_emoji(title_clean)
        
        # Build Point details HTML
        points_html = "<b>🎯 Key Points Covered in this Session:</b><ul>"
        for p in s["points"]:
            points_html += f"<li>{mascot_emoji} <b>{p['title']}</b>: {p['desc']}</li>"
        points_html += "</ul>"
        
        targets_html = "<b>⛳ Session Objectives:</b><ul>"
        for t in s.get("targets", ["Learn basic concepts", "Execute hands-on labs"]):
            targets_html += f"<li>🎯 {t}</li>"
        targets_html += "</ul>"
        
        project_html = ""
        if s.get("project"):
            project_html = f"<div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 8px; margin-top: 10px;'>🏆 <b>DIY Session Project:</b> {s['project']}</div>"
            
        story_html = f"<h3>{mascot_emoji} Hello, future coding hero!</h3>" \
                     f"I am your friend <b>{mascot_name}</b>, and today I will accompany you on an exciting coding adventure to explore <b>{title_clean}</b>! 🌟<br><br>" \
                     f"{points_html}" \
                     f"{targets_html}" \
                     f"{project_html}<br>" \
                     f"<p>Let's run the terminal verify code below to unlock this station's secret medal! You've got this! 🌟🚀</p>"
                     
        # Simpler analogies
        simple_explanation = f"Imagine {title_clean} is like "
        t_lower = title_clean.lower()
        if "setup" in t_lower or "install" in t_lower or "welcome" in t_lower:
            simple_explanation += "building the magic playground gates before you enter and play with toys!"
        elif "variable" in t_lower or "datatype" in t_lower:
            simple_explanation += "having smart boxes in your bedroom where you keep toys, labeled perfectly so they never get lost!"
        elif "operator" in t_lower or "math" in t_lower:
            simple_explanation += "using a digital calculator that instantly doubles your points or speeds up your running hero!"
        elif "condition" in t_lower or "if" in t_lower:
            simple_explanation += "a traffic light. If the light is green, your hero walks. Else, your hero stands still!"
        elif "loop" in t_lower:
            simple_explanation += "a music box that keeps playing your favorite sweet song over and over until you close the lid!"
        elif "db" in t_lower or "database" in t_lower or "storage" in t_lower or "save" in t_lower:
            simple_explanation += "a digital treasure box that safely stores your achievements so they remain even when you restart the computer!"
        elif "layout" in t_lower or "ui" in t_lower or "ux" in t_lower or "view" in t_lower:
            simple_explanation += "drawing beautiful rooms, buttons, and stickers on a white canvas to make your application look spectacular!"
        elif "cyber" in t_lower or "security" in t_lower or "hacking" in t_lower:
            simple_explanation += "acting as a cyber detective who checks door locks and protects the magical castle from intruders!"
        else:
            simple_explanation += "assembling perfect Lego pieces that connect together to build a grand castle!"
            
        verify_code = s["verify_code"]
        # Extract verification phrase
        if "print('" in verify_code:
            verify_phrase = verify_code.split("print('")[1].split("')")[0]
        elif "print(\"" in verify_code:
            verify_phrase = verify_code.split("print(\"")[1].split("\")")[0]
        else:
            verify_phrase = f"{title_clean} activated successfully!"
            
        hint_text = f"Type in the editor: <code>print(\"{verify_phrase}\")</code> and press Run!"
        challenge_text = f"Print the exact activation message: <code>{verify_phrase}</code> to unlock the {title_clean} medal!"
        
        # Determine language comment starter based on course
        lang_comment = "#"
        if course_id in ["senior_csharp"]:
            lang_comment = "//"
        elif course_id in ["senior_laravel_web", "senior_laravel_mobile"]:
            lang_comment = "// PHP"
            
        station = {
            "id": s_num,
            "badge_icon": badge_emoji,
            "badge_title": f"{title_clean} Medal",
            "title": f"Station {s_num}: {title_clean}",
            "desc": s["desc"],
            "story": story_html,
            "simple": simple_explanation,
            "hint": hint_text,
            "challenge": challenge_text,
            "starter_code": f"{lang_comment} Simulate {title_clean} activation:\n",
            "pills": [
                {
                    "label": f"Activate {title_clean}",
                    "code": f"print(\"{verify_phrase}\")"
                }
            ],
            "validation_rules": {
                "required_output_text": verify_phrase,
                "required_canvas": False
            },
            "homework": {
                "title": f"🏠 Magic Home Challenge: {title_clean} Builder",
                "desc": f"Great work! At home, practice creating a custom script or model simulating '{title_clean}' using the starter template below!",
                "code": f"{lang_comment} Home Challenge: {title_clean} Simulator\n# Write your creative solution here!",
                "starter_code": f"{lang_comment} Home Challenge: {title_clean} Simulator\n# Write your creative solution here!"
            }
        }
        stations.append(station)
        
    games_data = {
        "course_id": course_id,
        "course_title": course_title_name,
        "course_subtitle": f"Welcome, future legend! Embark on a spectacular coding adventure in {course_title_name}. " \
                          f"Meet {mascot_name}, solve fun challenges, and build outstanding systems! 🎮✨",
        "xp_total": len(stations) * 100,
        "mascot_img": "./assets/megaminds_mascot.png",
        "stations": stations
    }
    
    games_file = os.path.join(db_path, course_id, 'games.json')
    with open(games_file, 'w', encoding='utf-8') as f:
        json.dump(games_data, f, indent=2, ensure_ascii=False)
        
    # Write matching recap.json for C#, Flutter, and React Native (to ensure consistency across the database)
    if course_id in ['senior_csharp', 'senior_flutter', 'senior_react_native']:
        recap_json_data = {
            "course_id": course_id,
            "recaps": [
                {
                    "id": s["session_num"],
                    "title": f"{s['session_title']} Recap",
                    "sections": [
                        {
                            "heading": "🌟 Core Concept",
                            "text": s["desc"]
                        },
                        {
                            "heading": "🚀 Golden Takeaway",
                            "text": f"Always remember: {s['desc']} Experiment and design beautiful features with {mascot_emoji}!"
                        }
                    ]
                } for s in sessions_data
            ]
        }
        with open(recap_file, 'w', encoding='utf-8') as f:
            json.dump(recap_json_data, f, indent=2, ensure_ascii=False)
            
print("All games.json and recap.json files generated successfully for Category B courses!")

# 3. Replace the placeholder validation rule in senior_web_design_advanced (Station 9)
swda_games_path = os.path.join(db_path, 'senior_web_design_advanced', 'games.json')
if os.path.exists(swda_games_path):
    print("Fixing Station 9 in senior_web_design_advanced...")
    with open(swda_games_path, 'r', encoding='utf-8') as f:
        swda_data = json.load(f)
        
    for station in swda_data.get('stations', []):
        if station.get('id') == 9:
            station['validation_rules']['required_output_text'] = "Rowan"
            print("Successfully updated validation rule for Station 9 to check for 'Rowan'.")
            
    with open(swda_games_path, 'w', encoding='utf-8') as f:
        json.dump(swda_data, f, indent=2, ensure_ascii=False)

print("Compilation and fixes complete!")
