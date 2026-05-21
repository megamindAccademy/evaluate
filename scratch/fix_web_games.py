import json
import os

web_db = r'c:\Users\rowan\Desktop\ev\evaluate\database\senior_web_design\games.json'

levels = [
    "HTML Basics",
    "CSS Basics",
    "Web Layouts",
    "Responsive Design & Interactivity"
]

topics = [
    ["Structure & Tags", "Headings & Paragraphs", "Links & Navigation", "Images & Media"],
    ["CSS Syntax & Colors", "Fonts & Typography", "Classes & IDs", "The Box Model (Padding/Margin)"],
    ["Flexbox Basics", "Grid Layouts", "Positioning (Relative/Absolute)", "Navigation Bars"],
    ["Media Queries", "Responsive Images", "Intro to JavaScript", "DOM Click Events"]
]

games_json = {
    "course_id": "senior_web_design",
    "course_title": "Web Design (HTML/CSS)",
    "course_subtitle": "Master the art of building beautiful websites from scratch!",
    "xp_total": 1600,
    "mascot_img": "./assets/megaminds_mascot.png",
    "stations": []
}

station_id = 1
for level_index, level_name in enumerate(levels):
    level_topics = topics[level_index]
    for topic_index, topic in enumerate(level_topics):
        s_title = f"Level {level_index+1} Session {topic_index+1}: {topic}"
        print_code = f"console.log('Activated {topic}!');"
        
        story_html = f"<h3>?? Welcome, future Web Designer!</h3>Let's dive into <b>{s_title}</b>!<br><br><b>?? Key Points:</b><ul><li>?? <b>{topic}</b>: Building beautiful web pages!</li></ul><b>? Objectives:</b><ul><li>?? Understand web tags and styles</li><li>?? Apply modern design</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>?? <b>Project:</b> {topic} Challenge</div>"
        
        station = {
            "id": station_id,
            "badge_icon": "??",
            "badge_title": f"{topic} Medal",
            "title": f"Station {station_id}: {s_title}",
            "desc": f"Interactive {topic} activities",
            "story": story_html,
            "simple": f"Imagine {topic} is like drawing a beautiful painting on a digital canvas!",
            "hint": f"Type: <code>{print_code}</code>",
            "challenge": f"Print: <code>{print_code}</code>",
            "starter_code": f"<!-- Activate {topic} -->\n<script>\n    {print_code}\n</script>",
            "pills": [{"label": "Activate", "code": print_code}],
            "validation_rules": {"required_output_text": f"Activated {topic}!", "required_canvas": False},
            "homework": {
                "title": f"?? Magic Home Challenge: {topic}",
                "desc": f"Practice {topic} at home in your web project!",
                "code": f"<!-- Home Challenge: {topic} -->\n<!-- Write your creative solution here! -->",
                "starter_code": f"<!-- Home Challenge: {topic} -->\n<!-- Write your creative solution here! -->"
            }
        }
        games_json['stations'].append(station)
        station_id += 1

with open(web_db, 'w', encoding='utf-8') as f:
    json.dump(games_json, f, ensure_ascii=False, indent=2)

print("Web games.json generated accurately with 16 sessions based on syllabus!")
