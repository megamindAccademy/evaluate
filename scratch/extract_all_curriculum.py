import os
import re

txt_dir = r"c:\Users\rowan\Desktop\ev\evaluate\scratch\godot_pdf_text"
output_file = r"c:\Users\rowan\Desktop\ev\evaluate\scratch\godot_curriculum_details.txt"

files = sorted(os.listdir(txt_dir))

with open(output_file, "w", encoding="utf-8") as out:
    for fname in files:
        fpath = os.path.join(txt_dir, fname)
        if not fname.endswith(".txt"):
            continue
        
        out.write(f"\n================================================================================\n")
        out.write(f"FILE: {fname}\n")
        out.write(f"================================================================================\n")
        
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        pages = content.split("=== Page ")
        for p in pages:
            if not p.strip():
                continue
            
            lines = p.split("\n")
            p_num = lines[0].split(" ===")[0].strip()
            
            clean_lines = []
            for l in lines[1:]:
                l_str = l.strip()
                if not l_str:
                    continue
                if "All rights reserved" in l_str:
                    continue
                if l_str.isdigit():
                    continue
                clean_lines.append(l_str)
                
            if clean_lines:
                out.write(f"\n--- Page {p_num} ---\n")
                out.write("\n".join(clean_lines))
                out.write("\n")

print("Created godot_curriculum_details.txt successfully!")
