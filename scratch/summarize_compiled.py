import re

with open("compiled_godot_curriculum.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split by SESSION X CONTENT DUMP
sessions = text.split("================================================================================")

for s in sessions:
    if "SESSION" not in s or "CONTENT DUMP" not in s:
        continue
    
    title_match = re.search(r"SESSION (\d+) CONTENT DUMP", s)
    if not title_match:
        continue
    
    sess_num = int(title_match.group(1))
    print(f"\n=========================================\nSESSION {sess_num}\n=========================================")
    
    # Split by files inside this session
    files = s.split("--- FILE: ")
    for file_block in files[1:]: # Skip the first element which is the header
        lines = file_block.split("\n")
        fname = lines[0].replace("---", "").strip()
        print(f"\n  File: {fname}")
        
        # Collect key info
        content = "\n".join(lines[1:])
        pages = content.split("=== Page ")
        for p in pages[1:]:
            plines = [l.strip() for l in p.split("\n") if l.strip()]
            if not plines:
                continue
            p_num = plines[0].split(" ===")[0].strip()
            
            # Print important lines (excluding All rights reserved and numbers)
            clean_lines = []
            for l in plines[1:]:
                if "All rights reserved" in l or l.replace(".", "").strip().isdigit():
                    continue
                clean_lines.append(l)
            
            if clean_lines:
                print(f"    Page {p_num}: {', '.join(clean_lines[:5])}")
