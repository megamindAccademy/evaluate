import os

txt_dir = r"c:\Users\rowan\Desktop\ev\evaluate\scratch\godot_pdf_text"
summary_file = r"c:\Users\rowan\Desktop\ev\evaluate\scratch\godot_syllabus_summary.txt"

files = sorted(os.listdir(txt_dir))

with open(summary_file, "w", encoding="utf-8") as out:
    for file in files:
        if "SLIDE" in file:
            sess_name = file.split("_")[0] + "_" + file.split("_")[1]
            out.write(f"\n=========================================\n")
            out.write(f"FILE: {file}\n")
            out.write(f"=========================================\n")
            
            fpath = os.path.join(txt_dir, file)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Extract first few lines or page headings
            lines = [line.strip() for line in content.split("\n") if line.strip()]
            
            # Print first 30 lines
            out.write("\n".join(lines[:40]))
            out.write("\n...\n")

print("Generated syllabus summary!")
