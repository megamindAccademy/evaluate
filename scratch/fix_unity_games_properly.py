import os
import json
import re

db_path = 'database'
course_id = 'senior_unity'
mascot_name = 'Unity Unicorn 🦄'
mascot_short = 'Unity Unicorn'
mascot_emoji = '🦄'

unity_sessions = [
    # Level 1: Introduction to Unity & Bolt Scripting
    ("Game Engine Basics", 
     "Discover the core architecture of game engines and how Unity coordinates sprites, physics, and gameplay.",
     ["Understand Game Engines", "Navigate Unity Workspace"], 
     "Game Engine Basics activated successfully!",
     "building the magical gates of your dream game playground before adding the players and trees!"),
     
    ("Console & Debug.Log", 
     "Learn how to communicate with your game engine and log messages in the console to track bugs and flow.",
     ["Locate Console Window", "Write your first Debug.Log statement"], 
     "Console & Debug.Log activated successfully!",
     "sending secret walkie-talkie messages from your running player back to the developer desk!"),
     
    ("Unity Editor Windows", 
     "Master the layout by exploring the Scene View, Game View, Hierarchy, Project, and Inspector panels.",
     ["Explore Editor Layout", "Inspect GameObjects & Components"], 
     "Unity Editor Windows activated successfully!",
     "arranging your magical artist studio with drawers for brushes, canvas for painting, and preview screens!"),
     
    ("Asset Store Magic", 
     "Learn how to fetch beautiful art packages, sprites, and animations from the Unity Asset Store to style your worlds.",
     ["Search Asset Store", "Import Packages into Project"], 
     "Asset Store Magic activated successfully!",
     "visiting a huge free toy store where you can grab any sprite, sound, or block to use in your game!"),
     
    # Level 2: Flappy Bird Game Mechanics
    ("Physics & Rigidbody 2D", 
     "Understand rigidbodies, gravity scales, and dynamic mass in 2D systems to simulate realistic weight.",
     ["Apply Rigidbody 2D", "Configure gravity and mass"], 
     "Physics & Rigidbody 2D activated successfully!",
     "blowing a puff of wind that pulls game blocks down to the ground using real-world gravity!"),
     
    ("Jumping & Velocity", 
     "Write code controls to push players upward and manage vertical velocity loops.",
     ["Control Jump Triggers", "Apply upward velocity forces"], 
     "Jumping & Velocity activated successfully!",
     "attaching a small spring to your player's shoes that launches them high when you tap space!"),
     
    ("Prefabs & Instantiate", 
     "Master template cloning using Prefabs to dynamically spawn repeating obstacles and collectible coins.",
     ["Create Prefab templates", "Instantiate new clones programmatically"], 
     "Prefabs & Instantiate activated successfully!",
     "having a magical cookie cutter that lets you stamp out endless yummy game obstacle clones instantly!"),
     
    ("Collision Detection", 
     "Detect intersections using Colliders and triggers to react when players collect gems or crash into walls.",
     ["Configure Colliders & Triggers", "Intercept overlap callback events"], 
     "Collision Detection activated successfully!",
     "wrapping an invisible bubble around your hero that pops and rings a bell whenever they touch a coin!"),
     
    # Level 3: C# Programming Fundamentals
    ("C# Variables & Syntax", 
     "Dive into variables like int, float, string, and bool to keep track of scores and health.",
     ["Learn C# variable syntax", "Store scores and player names"], 
     "C# Variables & Syntax activated successfully!",
     "writing on small sticky labels to track player life, score points, and usernames!"),
     
    ("If Conditions", 
     "Empower your scripts to make smart choices using branch statements and logical operators.",
     ["Write If-Else branches", "Use logic comparisons"], 
     "If Conditions activated successfully!",
     "creating paths. If player has 3 keys, unlock the gold chest. Else, say 'Keep searching!'"),
     
    ("Loops (For/While)", 
     "Repeat coding blocks automatically to generate grid levels, trees, and maps without rewriting lines.",
     ["Write For loops", "Build Repeating grids"], 
     "Loops (For/While) activated successfully!",
     "a music loop playing your favorite song on repeat until you press the stop button!"),
     
    ("Classes & Objects", 
     "Understand Object-Oriented C# classes, class components, and MonoBehaviour instances.",
     ["Learn OOP structure", "Manage GameObject scripts"], 
     "Classes & Objects activated successfully!",
     "using a blue blueprint to build many physical sports cars, each with distinct paint colors!"),
     
    # Level 4: Sunny Land 2D Platformer Adventure
    ("Tilemaps & Level Design", 
     "Design complex, pixel-perfect 2D levels by drawing tiles directly onto a dynamic Tilemap Grid.",
     ["Setup Grid and Tilemaps", "Paint layouts using Tile Palettes"], 
     "Tilemaps & Level Design activated successfully!",
     "using a magic paintbrush to paint bricks, ladders, and grass platforms onto the game screen!"),
     
    ("Input Management", 
     "Capture keystrokes, gamepad taps, and mouse clicks smoothly to steer player animations.",
     ["Configure Input settings", "Translate inputs to movement"], 
     "Input Management activated successfully!",
     "linking your keyboard arrows directly to the character's feet so they walk when you tap!"),
     
    ("Cinemachine Cameras", 
     "Create professional, smooth-scrolling smart cameras that lock onto moving characters.",
     ["Install Cinemachine packages", "Configure Virtual Cameras and tracking"], 
     "Cinemachine Cameras activated successfully!",
     "hiring a professional camera operator who flies behind your hero and keeps them in perfect focus!"),
     
    ("Enemy AI Patrol", 
     "Build patrol sequences that steer enemy movements back and forth between navigation targets.",
     ["Define Waypoint targets", "Steer enemy transforms automatically"], 
     "Enemy AI Patrol activated successfully!",
     "placing two small signposts that tell the enemy soldier to march from Point A to Point B and back!"),
     
    # Level 5: RPG 3D Game Design & Physics
    ("3D Coordinate Systems", 
     "Navigate three-dimensional spaces using X, Y, and Z vector coordinates for rotation and position.",
     ["Understand Vector3 structures", "Manipulate 3D transforms"], 
     "3D Coordinate Systems activated successfully!",
     "adding depth to your drawing! Moving forward, backward, left, right, and high up in the sky!"),
     
    ("Materials & Textures", 
     "Dress plain 3D models with colorful materials, custom textures, and shaders.",
     ["Apply Materials to Meshes", "Tweak specular, metallic, and smooth sliders"], 
     "Materials & Textures activated successfully!",
     "wrapping plain gray clay statues in beautiful colorful gift-wrap paper to look like gold or stone!"),
     
    ("Character Controller", 
     "Build solid 3D player movement controllers that slide down hills and climb steps smoothly.",
     ["Add Character Controller components", "Write 3D motion script parameters"], 
     "Character Controller activated successfully!",
     "stepping inside a robust astronaut suit that moves perfectly over rocky space craters!"),
     
    ("NavMesh Pathfinding", 
     "Configure AI agents that navigate around complex obstacles using baked NavMesh pathfinding grids.",
     ["Bake NavMesh surfaces", "Define NavMesh Agent destinations"], 
     "NavMesh Pathfinding activated successfully!",
     "giving your pet robot a smart map of the living room so it walks around chairs instead of hitting them!"),
     
    # Level 6: RPG 3D Combat, Audio & Publishing
    ("Awake vs Start", 
     "Master initialization life cycle functions to run state setup before regular updates begin.",
     ["Understand Awake call timing", "Initialize components inside Start"], 
     "Awake vs Start activated successfully!",
     "waking up and putting on your shoes (Awake) before you step outside and start playing (Start)!"),
     
    ("Static Variables", 
     "Maintain global persistent variables like scores and levels across different levels and scenes.",
     ["Declare static variables", "Access values globally across scripts"], 
     "Static Variables activated successfully!",
     "a large scoreboard in the clouds that keeps your points safe even when you travel to different lands!"),
     
    ("Health & UI Sliders", 
     "Draw interactive health bar sliders on screens and link them to variables.",
     ["Design Canvas UI components", "Link script values to UI Slider components"], 
     "Health & UI Sliders activated successfully!",
     "putting a glowing progress bar on your hero's forehead that shrinks when they stub their toe!"),
     
    ("WebGL Publishing", 
     "Compile, compress, and publish your final game so it loads directly inside web browsers.",
     ["Configure WebGL platform targets", "Export, test, and publish HTML builds"], 
     "WebGL Publishing activated successfully!",
     "packing your final game into a magic link that you can text to all your friends to play online!")
]

stations = []
for idx, (title, desc, targets, verify_phrase, analogy) in enumerate(unity_sessions):
    s_num = idx + 1
    
    # Get appropriate emoji
    badge_emoji = "🚀"
    t_lower = title.lower()
    if any(k in t_lower for k in ["engine", "workspace", "editor", "window"]):
        badge_emoji = "🎮"
    elif any(k in t_lower for k in ["console", "debug", "log", "variable", "syntax", "if", "loop", "class"]):
        badge_emoji = "💻"
    elif any(k in t_lower for k in ["physics", "rigidbody", "velocity", "coordinate", "vector3"]):
        badge_emoji = "⚡"
    elif any(k in t_lower for k in ["prefab", "instantiate", "collision", "collider"]):
        badge_emoji = "📦"
    elif any(k in t_lower for k in ["asset", "material", "texture"]):
        badge_emoji = "🎨"
    elif any(k in t_lower for k in ["tilemap", "camera", "patrol", "pathfinding", "navmesh"]):
        badge_emoji = "🗺️"
    elif any(k in t_lower for k in ["publish", "webgl", "graduation"]):
        badge_emoji = "🏆"
        
    points_html = "<b>🎯 Key Points Covered in this Session:</b><ul>"
    points_html += f"<li>{mascot_emoji} <b>{title}</b>: {desc}</li>"
    points_html += "</ul>"
    
    targets_html = "<b>⛳ Session Objectives:</b><ul>"
    for t in targets:
        targets_html += f"<li>🎯 {t}</li>"
    targets_html += "</ul>"
    
    project_html = f"<div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 8px; margin-top: 10px;'>🏆 <b>DIY Session Project:</b> {title} Practical Simulator</div>"
    
    story_html = f"<h3>{mascot_emoji} Hello, future coding hero!</h3>" \
                 f"I am your friend <b>{mascot_short}</b>, and today I will accompany you on an exciting coding adventure to explore <b>{title}</b>! 🌟<br><br>" \
                 f"{points_html}" \
                 f"{targets_html}" \
                 f"{project_html}<br>" \
                 f"<p>Let's run the terminal verify code below to unlock this station's secret medal! You've got this! 🌟🚀</p>"
                 
    simple_explanation = f"Imagine {title} is like {analogy}"
    
    hint_text = f"Type in the editor: <code>print(\"{verify_phrase}\")</code> and press Run!"
    challenge_text = f"Print the exact activation message: <code>{verify_phrase}</code> to unlock the {title} medal!"
    
    station = {
        "id": s_num,
        "badge_icon": badge_emoji,
        "badge_title": f"{title} Medal",
        "title": f"Station {s_num}: {title}",
        "desc": desc,
        "story": story_html,
        "simple": simple_explanation,
        "hint": hint_text,
        "challenge": challenge_text,
        "starter_code": f"// Simulate {title} activation:\n",
        "pills": [
            {
                "label": f"Activate {title}",
                "code": f"print(\"{verify_phrase}\")"
            }
        ],
        "validation_rules": {
            "required_output_text": verify_phrase,
            "required_canvas": False
        },
        "homework": {
            "title": f"🏠 Magic Home Challenge: {title} Builder",
            "desc": f"Great work! At home, practice creating a custom script or model simulating '{title}' using the starter template below!",
            "code": f"// Home Challenge: {topic_name if 'topic_name' in locals() else title} Simulator\n# Write your creative solution here!",
            "starter_code": f"// Home Challenge: {topic_name if 'topic_name' in locals() else title} Simulator\n# Write your creative solution here!"
        }
    }
    stations.append(station)

games_data = {
    "course_id": course_id,
    "course_title": "Unity Game Development",
    "course_subtitle": f"Welcome, future legend! Embark on a spectacular coding adventure in Unity Game Development. Meet {mascot_short}, solve fun challenges, and build outstanding systems! 🎮✨",
    "xp_total": len(stations) * 100,
    "mascot_img": "./assets/megaminds_mascot.png",
    "stations": stations
}

# Ensure destination exists
os.makedirs(os.path.join(db_path, course_id), exist_ok=True)

# Write games.json
games_file = os.path.join(db_path, course_id, 'games.json')
with open(games_file, 'w', encoding='utf-8') as f:
    json.dump(games_data, f, indent=2, ensure_ascii=False)

# Write recap.json
recap_file = os.path.join(db_path, course_id, 'recap.json')
recap_json_data = {
    "course_id": course_id,
    "recaps": [
        {
            "id": idx + 1,
            "title": f"{title} Recap",
            "sections": [
                {
                    "heading": "🌟 Core Concept",
                    "text": desc
                },
                {
                    "heading": "🚀 Golden Takeaway",
                    "text": f"Always remember: {desc} Experiment and design beautiful Unity features with {badge_emoji}!"
                }
            ]
        } for idx, (title, desc, _, _, _) in enumerate(unity_sessions)
    ]
}

with open(recap_file, 'w', encoding='utf-8') as f:
    json.dump(recap_json_data, f, indent=2, ensure_ascii=False)

print("Successfully generated high-quality, placeholder-free games.json and recap.json for senior_unity!")
