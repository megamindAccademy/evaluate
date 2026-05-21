import os
import json
import re

db_path = 'database'
senior_dirs = [d for d in os.listdir(db_path) if d.startswith('senior_') and d not in ['senior_python', 'senior_ai']]

def get_badge_emoji(title):
    title_lower = title.lower()
    if any(k in title_lower for k in ["setup", "install", "welcome", "introduction"]):
        return "🚀"
    if any(k in title_lower for k in ["ui", "ux", "layout", "screen", "anchor", "margin", "designer", "interface"]):
        return "📱"
    if any(k in title_lower for k in ["code", "script", "gdscript", "variable", "control", "condition", "logic", "function", "array", "list", "loop"]):
        return "💻"
    if any(k in title_lower for k in ["art", "sprite", "graphic", "animate", "animation", "draw", "paint", "canvas"]):
        return "🎨"
    if any(k in title_lower for k in ["sound", "audio", "music", "ping", "hit", "voice"]):
        return "🔊"
    if any(k in title_lower for k in ["physics", "bounce", "collision", "gravity", "force", "ball"]):
        return "⚽"
    if any(k in title_lower for k in ["win", "goal", "score", "game over", "rules", "winner", "result"]):
        return "🏆"
    if any(k in title_lower for k in ["database", "db", "tinydb", "local", "save", "store", "memory", "file"]):
        return "💾"
    if any(k in title_lower for k in ["ai", "assistant", "chatgpt", "teachable", "dall-e", "imagecreator", "bot", "ml"]):
        return "🤖"
    if any(k in title_lower for k in ["cyber", "security", "hacking", "network", "encryp", "decryp", "attack", "defen", "ip", "port", "nmap", "ssh", "exploit"]):
        return "🛡️"
    return "🎯"

def get_clean_title(title):
    # Remove any characters outside BMP (which filters out standard emojis)
    cleaned = "".join(c for c in title if ord(c) < 0xFFFF)
    cleaned = re.sub(r'^(Session\s+\d+:\s*|💡\s*Session\s+\d+:\s*|✨\s*Session\s+\d+:\s*|🚀\s*Session\s+\d+:\s*|🎯\s*Session\s+\d+:\s*)', '', cleaned, flags=re.IGNORECASE)
    return cleaned.strip()

for d in sorted(senior_dirs):
    recap_file = os.path.join(db_path, d, 'recap.json')
    if not os.path.exists(recap_file):
        continue
        
    print(f"Generating games.json for {d}...")
    with open(recap_file, 'r', encoding='utf-8') as f:
        recap = json.load(f)
        
    course_title = recap.get('course_title') or recap.get('course') or d
    
    # Generate interactive subtitle
    course_subtitle = f"Welcome, future legend! Embark on a spectacular coding adventure in {course_title}. " \
                      "Unlock custom medals, solve daily challenges, and program your own digital masterpieces!"
                      
    stations = []
    for idx, session in enumerate(recap.get('sessions', [])):
        s_num = session.get('session_num') or (idx + 1)
        s_title = session.get('session_title') or f"Session {s_num}"
        clean_title = get_clean_title(s_title)
        
        badge_emoji = get_badge_emoji(s_title)
        
        # Build Points Covered list
        points_covered_html = ""
        points = session.get('points', [])
        targets = session.get('targets', [])
        blocks = session.get('blocks', [])
        project = session.get('project', '')
        
        if points:
            points_covered_html += "<b>🎯 Key Points Covered in this Session:</b><ul>"
            for p in points:
                p_title = p.get('title') or p.get('name') or ''
                p_desc = p.get('desc') or p.get('description') or ''
                p_icon = p.get('icon') or "👉"
                points_covered_html += f"<li>{p_icon} <b>{p_title}</b>: {p_desc}</li>"
            points_covered_html += "</ul>"
            
        if targets:
            points_covered_html += "<b>⛳ Session Objectives:</b><ul>"
            for t in targets:
                points_covered_html += f"<li>🎯 {t}</li>"
            points_covered_html += "</ul>"
            
        if blocks:
            points_covered_html += "<b>🧱 Key Coding Blocks & Concepts:</b><ul>"
            for b in blocks:
                points_covered_html += f"<li><code>{b}</code></li>"
            points_covered_html += "</ul>"
            
        if project:
            points_covered_html += f"<div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>DIY Session Project:</b> {project}</div>"
            
        # Compile beautiful child-friendly story
        story_html = f"<h3>👋 Welcome, future coding hero!</h3>" \
                     f"Let's dive into our interactive session for <b>{clean_title}</b>!<br><br>" \
                     f"{points_covered_html}<br>"
                     
        # Extract code or examples from points and format them beautifully in the story
        for p in points:
            p_code = p.get('code') or ''
            p_ex = p.get('example') or ''
            p_title = p.get('title') or p.get('name') or ''
            if p_code:
                story_html += f"<h4>💻 Starter Code Block - {p_title}:</h4>" \
                              f"<pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>{p_code}</code></pre>"
            if p_ex:
                story_html += f"<div style='background: #f0fdf4; border: 1px dashed #bbf7d0; color: #166534; padding: 10px; border-radius: 8px; margin-top: 8px; margin-bottom: 8px;'>💡 <b>Try this Example:</b> {p_ex}</div>"
                
        story_html += "<br><p>Let's run the terminal verify code below to unlock this station's secret medal! You've got this! 🌟🚀</p>"
        
        # Build simplified childlike analogical explanation
        simple_explanation = ""
        if points:
            first_p = points[0]
            simple_explanation = f"Imagine that {first_p.get('title', 'this concept')} is like "
            title_lower = first_p.get('title', '').lower()
            if "setup" in title_lower or "install" in title_lower:
                simple_explanation += "building the magic playground gates before you enter and play with toys!"
            elif "database" in title_lower or "db" in title_lower or "save" in title_lower:
                simple_explanation += "having a digital treasure box where you store all your gold coins safely so they never disappear!"
            elif "physics" in title_lower or "collision" in title_lower or "bounce" in title_lower:
                simple_explanation += "throwing a rubber bouncy ball against the wall and watching it spring back realistically!"
            elif "ui" in title_lower or "layout" in title_lower or "designer" in title_lower:
                simple_explanation += "drawing colorful buttons and stickers on your toy car to make it look incredibly cool!"
            elif "code" in title_lower or "script" in title_lower:
                simple_explanation += "writing a list of secret rules telling your helper robot exactly what to do step-by-step!"
            elif "hacking" in title_lower or "cyber" in title_lower:
                simple_explanation += "acting as a digital detective to find secret clues and keep the digital castle safe from thieves!"
            else:
                simple_explanation += "assembling a set of LEGO blocks where each piece connects to build a spectacular castle!"
        else:
            simple_explanation = "Like building a custom set of puzzle pieces where each block fits perfectly to create a stunning masterpiece!"
            
        # Create unique validation string
        verify_phrase = f"{clean_title} activated successfully!"
        
        hint_text = f"Type in the editor: <code>print(\"{verify_phrase}\")</code> and press Run!"
        challenge_text = f"Print the exact activation message: <code>{verify_phrase}</code> to unlock the {clean_title} medal!"
        
        # Design a custom homework based on session content
        hw_desc = f"Great work! At home, practice creating a custom model or code simulating '{clean_title}'. "
        if points:
            hw_desc += f"Specifically, design a feature demonstrating: '{points[-1].get('title', 'the final concept')}' using the starter template below!"
        else:
            hw_desc += "Design a creative system demonstrating the core ideas covered in today's lesson!"
            
        station = {
            "id": s_num,
            "badge_icon": badge_emoji,
            "badge_title": f"{clean_title} Medal",
            "title": f"Station {s_num}: {clean_title}",
            "desc": session.get('project') or (points[0].get('desc') if points else f"Master the core elements of {clean_title}!"),
            "story": story_html,
            "simple": simple_explanation,
            "hint": hint_text,
            "challenge": challenge_text,
            "starter_code": f"# Simulate {clean_title} activation:\n",
            "pills": [
                {
                    "label": f"Activate {clean_title}",
                    "code": f"print(\"{verify_phrase}\")"
                }
            ],
            "validation_rules": {
                "required_output_text": verify_phrase,
                "required_canvas": False
            },
            "homework": {
                "title": f"🏠 Magic Home Challenge: {clean_title} Builder",
                "desc": hw_desc,
                "code": f"# Home Challenge: {clean_title} Simulator\n# Write your creative solution here!",
                "starter_code": f"# Home Challenge: {clean_title} Simulator\n# Write your creative solution here!"
            }
        }
        stations.append(station)
        
    games_data = {
        "course_id": d,
        "course_title": course_title,
        "course_subtitle": course_subtitle,
        "xp_total": len(stations) * 100,
        "mascot_img": "./assets/megaminds_mascot.png",
        "stations": stations
    }
    
    games_file = os.path.join(db_path, d, 'games.json')
    with open(games_file, 'w', encoding='utf-8') as f:
        json.dump(games_data, f, indent=2, ensure_ascii=False)
        
print("All games.json files generated successfully!")
