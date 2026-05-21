import json
import os

unity_db = r'c:\Users\rowan\Desktop\ev\evaluate\database\senior_unity\games.json'

levels = [
    "Introduction to Unity & Bolt Scripting",
    "Flappy Bird Game Mechanics",
    "C# Programming Fundamentals",
    "Sunny Land 2D Platformer Adventure",
    "RPG 3D Game Design & Physics",
    "RPG 3D Combat, Audio & Publishing"
]

topics = [
    ["Game Engine Basics", "Console & Debug.Log", "Unity Editor Windows", "Asset Store Magic"],
    ["Physics & Rigidbody 2D", "Jumping & Velocity", "Prefabs & Instantiate", "Collision Detection"],
    ["C# Variables & Syntax", "If Conditions", "Loops (For/While)", "Classes & Objects"],
    ["Tilemaps & Level Design", "Input Management", "Cinemachine Cameras", "Enemy AI Patrol"],
    ["3D Coordinate Systems", "Materials & Textures", "Character Controller", "NavMesh Pathfinding"],
    ["Awake vs Start", "Static Variables", "Health & UI Sliders", "WebGL Publishing"]
]

games_json = {
    "course_id": "senior_unity",
    "course_title": "Unity Game Development",
    "course_subtitle": "Master 2D and 3D game design using Unity Engine and C#!",
    "xp_total": 2400,
    "mascot_img": "./assets/megaminds_mascot.png",
    "stations": []
}

station_id = 1
for level_index, level_name in enumerate(levels):
    level_topics = topics[level_index]
    for topic_index, topic in enumerate(level_topics):
        s_title = f"Level {level_index+1} Session {topic_index+1}: {topic}"
        print_code = f'Debug.Log("Activated {topic}!");'
        
        story_html = f"<h3>?? Welcome, future game developer!</h3>Let's dive into <b>{s_title}</b>!<br><br><b>?? Key Points:</b><ul><li>?? <b>{topic}</b>: Mastering Unity engine techniques!</li></ul><b>? Objectives:</b><ul><li>?? Understand C# integration</li><li>?? Apply game logic</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>?? <b>Project:</b> {topic} simulation</div>"
        
        station = {
            "id": station_id,
            "badge_icon": "???",
            "badge_title": f"{topic} Medal",
            "title": f"Station {station_id}: {s_title}",
            "desc": f"Interactive {topic} activities",
            "story": story_html,
            "simple": f"Imagine {topic} is like designing the rules for your favorite board game!",
            "hint": f"Type: <code>{print_code}</code>",
            "challenge": f"Print: <code>{print_code}</code>",
            "starter_code": f"// Activate {topic}\nusing UnityEngine;\n\npublic class SessionSimulator : MonoBehaviour {{\n    void Start() {{\n        // Write code here\n    }}\n}}",
            "pills": [{"label": "Activate", "code": print_code}],
            "validation_rules": {"required_output_text": f"Activated {topic}!", "required_canvas": False},
            "homework": {
                "title": f"?? Magic Home Challenge: {topic}",
                "desc": f"Practice {topic} at home in your Unity project!",
                "code": f"// Home Challenge: {topic}\n// Write your creative solution here!",
                "starter_code": f"// Home Challenge: {topic}\n// Write your creative solution here!"
            }
        }
        games_json['stations'].append(station)
        station_id += 1

with open(unity_db, 'w', encoding='utf-8') as f:
    json.dump(games_json, f, ensure_ascii=False, indent=2)

print("Unity games.json generated accurately with 24 sessions based on syllabus!")
