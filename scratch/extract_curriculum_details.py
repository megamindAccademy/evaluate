import re

with open("compiled_godot_curriculum.txt", "r", encoding="utf-8") as f:
    text = f.read()

sessions = text.split("================================================================================")

with open("godot_curriculum_structured.txt", "w", encoding="utf-8") as out:
    for s in sessions:
        if "SESSION" not in s or "CONTENT DUMP" not in s:
            continue
        
        title_match = re.search(r"SESSION (\d+) CONTENT DUMP", s)
        if not title_match:
            continue
        
        sess_num = int(title_match.group(1))
        out.write(f"\n=========================================\n")
        out.write(f"SESSION {sess_num}\n")
        out.write(f"=========================================\n")
        
        files = s.split("--- FILE: ")
        for file_block in files[1:]:
            lines = file_block.split("\n")
            fname = lines[0].replace("---", "").strip()
            out.write(f"\n  File: {fname}\n")
            
            # Print unique lines that contain key terms (like ready, process, node, scene, movement, operator, canvas, etc.)
            content = "\n".join(lines[1:])
            pages = content.split("=== Page ")
            for p in pages[1:]:
                plines = [l.strip() for l in p.split("\n") if l.strip()]
                if not plines:
                    continue
                p_num = plines[0].split(" ===")[0].strip()
                
                # Gather lines
                important = []
                for l in plines[1:]:
                    if "All rights reserved" in l or l.isdigit() or l == ".":
                        continue
                    if len(l) < 3:
                        continue
                    # Skip typical slides footer
                    if "Game Development with" in l or "Godot Engine" in l:
                        continue
                    important.append(l)
                
                if important:
                    out.write(f"    Page {p_num}: {'; '.join(important[:8])}\n")

print("Created godot_curriculum_structured.txt!")
