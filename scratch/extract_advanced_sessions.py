with open("godot_curriculum_details.txt", "r", encoding="utf-8") as f:
    text = f.read()

files = text.split("================================================================================")

for f in files:
    if not f.strip():
        continue
    
    header_lines = [l.strip() for l in f.split("\n") if l.strip()]
    if not header_lines:
        continue
    
    fname = header_lines[0].replace("FILE: ", "").strip()
    
    # We are interested in sessions 5 to 12
    # File names are like: SESSION_05_SLIDE_session5.txt, etc.
    session_num = None
    parts = fname.split("_")
    try:
        session_num = int(parts[1])
    except (IndexError, ValueError):
        continue
        
    if session_num >= 5:
        print(f"\n=========================================\n{fname}\n=========================================")
        # Print a few key lines from each page in this file
        pages = f.split("--- Page ")
        for p in pages[1:]:
            plines = [l.strip() for l in p.split("\n") if l.strip()]
            if not plines:
                continue
            p_num = plines[0].split(" ---")[0].strip()
            
            non_trivial = []
            for l in plines[1:]:
                if "All rights reserved" in l or l.replace(".", "").strip().isdigit():
                    continue
                non_trivial.append(l)
                
            if non_trivial:
                print(f"  Page {p_num}: {'; '.join(non_trivial[:4])}")
