import os
import json
import glob

db_path = r'c:\Users\rowan\Desktop\ev\evaluate\database'
onedrive_path = r'C:\Users\rowan\OneDrive\Megaminds curriculum\AGES (10-16)\Programming'

# Define courses and their actual directories in OneDrive
courses_map = {
    'senior_csharp': {
        'path': os.path.join(onedrive_path, 'Desktop Application', 'C#'),
        'type': 'csharp',
        'levels': True
    },
    'senior_unity': {
        'path': os.path.join(onedrive_path, 'Game Development', 'Unity'),
        'type': 'unity',
        'levels': True
    },
    'senior_web_design': {
        'path': os.path.join(onedrive_path, 'Web Development', 'Web Design'),
        'type': 'html',
        'levels': True
    }
}

def count_sessions(course_info):
    if not os.path.exists(course_info['path']):
        return 12 # fallback
    
    count = 0
    if course_info['levels']:
        for level in os.listdir(course_info['path']):
            level_path = os.path.join(course_info['path'], level)
            if os.path.isdir(level_path) and 'level' in level.lower():
                sessions = [d for d in os.listdir(level_path) if 'session' in d.lower()]
                count += len(sessions)
    else:
        sessions = [d for d in os.listdir(course_info['path']) if 'session' in d.lower() and os.path.isdir(os.path.join(course_info['path'], d))]
        count = len(sessions)
    
    return max(1, count)

def get_language_snippets(lang, title):
    if lang == 'html':
        print_code = f"console.log('{title} activated successfully!');"
        starter = f"<!-- Activate {title} -->\n<script>\n  {print_code}\n</script>"
        hw_starter = f"<!-- Home Challenge: {title} -->\n<!-- Write your creative solution here! -->"
        block = "<code>html_tags</code>, <code>css_properties</code>, <code>javascript</code>"
    elif lang == 'csharp' or lang == 'unity':
        print_code = f'Debug.Log("{title} activated successfully!");'
        starter = f"// Activate {title}\nusing UnityEngine;\n\npublic class SessionSimulator : MonoBehaviour {{\n    void Start() {{\n        {print_code}\n    }}\n}}"
        hw_starter = f"// Home Challenge: {title}\n// Write your creative solution here!"
        block = "<code>MonoBehaviour</code>, <code>Start()</code>, <code>Update()</code>"
    else:
        print_code = f'print("{title} activated successfully!")'
        starter = f"# Activate {title}\n{print_code}"
        hw_starter = f"# Home Challenge: {title}\n# Write your creative solution here!"
        block = "<code>variables</code>, <code>functions</code>, <code>loops</code>"
    return print_code, starter, hw_starter, block

def generate_games(course_id, course_info):
    db_folder = os.path.join(db_path, course_id)
    if not os.path.exists(db_folder): return
    
    num_sessions = count_sessions(course_info)
    print(f"Generating {num_sessions} sessions for {course_id}...")
    
    # Read existing to preserve title/subtitle if possible
    games_file = os.path.join(db_folder, 'games.json')
    try:
        with open(games_file, 'r', encoding='utf-8') as f:
            existing = json.load(f)
            course_title = existing.get('course_title', course_id.replace('_', ' ').title())
            course_subtitle = existing.get('course_subtitle', 'Welcome to the course!')
    except:
        course_title = course_id.replace('_', ' ').title()
        course_subtitle = 'Welcome to the course!'

    stations = []
    for i in range(1, num_sessions + 1):
        s_title = f"Session {i}"
        print_code, starter, hw_starter, block = get_language_snippets(course_info['type'], s_title)
        
        # HTML tag escaping simulation in text
        story_html = f"<h3>?? Welcome, future coding hero!</h3>Let's dive into our interactive session for <b>{s_title}</b>!<br><br><b>?? Key Points Covered in this Session:</b><ul><li>?? <b>Core Concepts</b>: Building amazing projects and writing clean code!</li></ul><b>? Session Objectives:</b><ul><li>?? Master the syntax</li><li>?? Create interactive elements</li></ul><b>?? Key Coding Blocks:</b><ul><li>{block}</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>?? <b>DIY Session Project:</b> Interactive Challenge</div><br><p>Let's run the terminal verify code below to unlock this station's secret medal! You've got this! ????</p>"
        
        station = {
            "id": i,
            "badge_icon": "??" if course_info['type'] != 'html' else "??",
            "badge_title": f"{s_title} Medal",
            "title": f"Station {i}: {s_title}",
            "desc": f"Interactive {s_title} activities",
            "story": story_html,
            "simple": f"Imagine that learning this is like assembling LEGO blocks to build a spectacular castle!",
            "hint": f"Type in the editor: <code>{print_code.replace('<', '&lt;').replace('>', '&gt;')}</code> and press Run!",
            "challenge": f"Print the exact activation message: <code>{print_code.replace('<', '&lt;').replace('>', '&gt;')}</code> to unlock the medal!",
            "starter_code": starter,
            "pills": [
                {
                    "label": f"Activate {s_title}",
                    "code": print_code
                }
            ],
            "validation_rules": {
                "required_output_text": f"{s_title} activated successfully!",
                "required_canvas": False
            },
            "homework": {
                "title": f"?? Magic Home Challenge: {s_title}",
                "desc": f"Great work! At home, practice creating a custom model or code simulating '{s_title}'. Use the starter template below!",
                "code": hw_starter,
                "starter_code": hw_starter
            }
        }
        stations.append(station)
        
    games_json = {
        "course_id": course_id,
        "course_title": course_title,
        "course_subtitle": course_subtitle,
        "xp_total": num_sessions * 100,
        "mascot_img": "./assets/megaminds_mascot.png",
        "stations": stations
    }
    
    with open(games_file, 'w', encoding='utf-8') as f:
        json.dump(games_json, f, ensure_ascii=False, indent=2)

def generate_recaps(course_id, course_info):
    db_folder = os.path.join(db_path, course_id)
    if not os.path.exists(db_folder): return
    num_sessions = count_sessions(course_info)
    
    recap_file = os.path.join(db_folder, 'recap.json')
    recaps = []
    for i in range(1, num_sessions + 1):
        recaps.append({
            "id": i,
            "title": f"Session {i} Recap",
            "sections": [
                {
                    "heading": "?? Core Concept",
                    "text": f"In Session {i}, we learned how to build robust systems and write clean code."
                },
                {
                    "heading": "?? Key Takeaway",
                    "text": "Practice makes perfect! Experiment with different variables and structures."
                }
            ]
        })
        
    recap_json = {
        "course_id": course_id,
        "recaps": recaps
    }
    
    with open(recap_file, 'w', encoding='utf-8') as f:
        json.dump(recap_json, f, ensure_ascii=False, indent=2)

for cid, info in courses_map.items():
    generate_games(cid, info)
    generate_recaps(cid, info)

print('All curriculums updated successfully!')
