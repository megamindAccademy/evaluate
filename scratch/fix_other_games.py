import json
import os

db_path = r'c:\Users\rowan\Desktop\ev\evaluate\database'

courses = [
    ("senior_flutter", "Flutter Mobile Development", "dart", 12),
    ("senior_react_native", "React Native Mobile Dev", "javascript", 12),
    ("senior_godot", "Godot Game Development", "gdscript", 12),
    ("senior_csharp", "C# Application Dev", "csharp", 24)
]

for course_id, title, lang, num_sessions in courses:
    games_json = {
        "course_id": course_id,
        "course_title": title,
        "course_subtitle": f"Master {title}!",
        "xp_total": num_sessions * 100,
        "mascot_img": "./assets/megaminds_mascot.png",
        "stations": []
    }
    
    for i in range(1, num_sessions + 1):
        s_title = f"Session {i}: Core Concepts"
        if lang == 'dart':
            print_code = f"print('Activated Session {i}!');"
            starter = f"// Activate Session {i}\nvoid main() {{\n  {print_code}\n}}"
        elif lang == 'javascript':
            print_code = f"console.log('Activated Session {i}!');"
            starter = f"// Activate Session {i}\n{print_code}"
        elif lang == 'gdscript':
            print_code = f'print("Activated Session {i}!")'
            starter = f"extends Node\n\nfunc _ready():\n    {print_code}"
        else:
            print_code = f'Console.WriteLine("Activated Session {i}!");'
            starter = f"using System;\n\nclass Program {{\n    static void Main() {{\n        {print_code}\n    }}\n}}"

        story_html = f"<h3>?? Welcome, future legend!</h3>Let's dive into <b>{s_title}</b>!<br><br><b>?? Key Points:</b><ul><li>?? Mastering {title} techniques!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>?? <b>Project:</b> Interactive Session {i}</div>"
        
        station = {
            "id": i,
            "badge_icon": "??",
            "badge_title": f"Session {i} Medal",
            "title": f"Station {i}: {s_title}",
            "desc": f"Interactive {s_title}",
            "story": story_html,
            "simple": f"Imagine {s_title} is like designing a beautiful machine!",
            "hint": f"Type: <code>{print_code}</code>",
            "challenge": f"Print: <code>{print_code}</code>",
            "starter_code": starter,
            "pills": [{"label": "Activate", "code": print_code}],
            "validation_rules": {"required_output_text": f"Activated Session {i}!", "required_canvas": False},
            "homework": {
                "title": f"?? Magic Home Challenge: Session {i}",
                "desc": f"Practice Session {i} at home!",
                "code": f"// Home Challenge: Session {i}",
                "starter_code": f"// Home Challenge: Session {i}"
            }
        }
        games_json['stations'].append(station)

    # Write games
    db_folder = os.path.join(db_path, course_id)
    if not os.path.exists(db_folder): os.makedirs(db_folder)
    with open(os.path.join(db_folder, 'games.json'), 'w', encoding='utf-8') as f:
        json.dump(games_json, f, ensure_ascii=False, indent=2)

    # Write recaps
    recaps = [{"id": i, "title": f"Session {i} Recap", "sections": [{"heading": "?? Core Concept", "text": "Great job!"}]} for i in range(1, num_sessions + 1)]
    with open(os.path.join(db_folder, 'recap.json'), 'w', encoding='utf-8') as f:
        json.dump({"course_id": course_id, "recaps": recaps}, f, ensure_ascii=False, indent=2)

print("All other courses generated cleanly!")
