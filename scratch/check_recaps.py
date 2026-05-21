import os
import json

db_path = 'database'
senior_dirs = [d for d in os.listdir(db_path) if d.startswith('senior_') and d not in ['senior_python', 'senior_ai']]

for d in sorted(senior_dirs):
    recap_file = os.path.join(db_path, d, 'recap.json')
    if os.path.exists(recap_file):
        with open(recap_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            course_title = data.get('course_title') or data.get('course') or d
            sessions = data.get('sessions', [])
            num_sessions = len(sessions)
            print(f"Course: {d} | Title: {course_title} | Sessions: {num_sessions}")
            if num_sessions > 0:
                print(f"  Session 1 Keys: {list(sessions[0].keys())}")
