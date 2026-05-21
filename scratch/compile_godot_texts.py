import os

txt_dir = r"c:\Users\rowan\Desktop\ev\evaluate\scratch\godot_pdf_text"
output_file = r"c:\Users\rowan\Desktop\ev\evaluate\scratch\compiled_godot_curriculum.txt"

# Get all files and group them by session number
files_by_session = {i: [] for i in range(1, 13)}

for fname in os.listdir(txt_dir):
    fpath = os.path.join(txt_dir, fname)
    if not fname.endswith(".txt"):
        continue
    
    # Extract session number
    # Names are like: SESSION_01_SLIDE_session1.txt, SESSION_01_TG_TG__session_1.txt, SESSION_11_SLIDE_session_11.txt, etc.
    parts = fname.split("_")
    try:
        sess_num = int(parts[1])
        files_by_session[sess_num].append(fname)
    except (IndexError, ValueError):
        print(f"Could not parse session number from {fname}")

with open(output_file, "w", encoding="utf-8") as out:
    for sess in range(1, 13):
        out.write(f"\n================================================================================\n")
        out.write(f"SESSION {sess} CONTENT DUMP\n")
        out.write(f"================================================================================\n")
        
        # Sort so that SLIDE usually comes before TG
        sorted_files = sorted(files_by_session[sess], key=lambda x: ("SLIDE" not in x, x))
        for fname in sorted_files:
            out.write(f"\n--- FILE: {fname} ---\n")
            fpath = os.path.join(txt_dir, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                out.write(f.read())
            out.write("\n")

print(f"Successfully compiled all sessions into {output_file}!")
