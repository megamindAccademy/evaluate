import os

txt_dir = r"c:\Users\rowan\Desktop\ev\evaluate\artifacts\ai_pdf_text"
output_file = r"c:\Users\rowan\Desktop\ev\evaluate\artifacts\all_sessions_summary.txt"

files = sorted(os.listdir(txt_dir), key=lambda x: int(x.split("_")[1]))

with open(output_file, "w", encoding="utf-8") as out:
    for fname in files:
        fpath = os.path.join(txt_dir, fname)
        out.write(f"\n========================================================================\n")
        out.write(f"FILE: {fname}\n")
        out.write(f"========================================================================\n")
        with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            out.write(content)
            
print(f"Combined summary written to {output_file}")
