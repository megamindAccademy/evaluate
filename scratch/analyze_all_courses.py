import os
import json

db_dir = r"c:\Users\rowan\Desktop\ev\evaluate\database"
report = []

for course_id in os.listdir(db_dir):
    course_path = os.path.join(db_dir, course_id)
    if not os.path.isdir(course_path):
        continue
    
    games_file = os.path.join(course_path, "games.json")
    if not os.path.exists(games_file):
        continue
        
    try:
        with open(games_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            stations = data.get("stations", [])
            
            placeholders = 0
            station_info = []
            for st in stations:
                title = st.get("title", "")
                val_rules = st.get("validation_rules", {})
                req_text = val_rules.get("required_output_text", "")
                
                is_placeholder = "Core Concepts" in title or "Activated Session" in req_text or "activated successfully" in req_text
                if is_placeholder:
                    placeholders += 1
                
                station_info.append({
                    "id": st.get("id"),
                    "title": title,
                    "required_text": req_text,
                    "is_placeholder": is_placeholder
                })
                
            report.append({
                "course_id": course_id,
                "title": data.get("course_title", ""),
                "total_stations": len(stations),
                "placeholders": placeholders,
                "stations": station_info
            })
    except Exception as e:
        print(f"Error reading {course_id}: {e}")

# Save report
with open(os.path.join(db_dir, "../scratch/courses_analysis.json"), "w", encoding="utf-8") as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print(f"Analysis complete! Found {len(report)} courses.")
