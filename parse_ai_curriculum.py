import os

txt_dir = r"c:\Users\rowan\Desktop\ev\evaluate\artifacts\ai_pdf_text"
output_file = r"c:\Users\rowan\Desktop\ev\evaluate\artifacts\ai_sessions_outline.md"

files = sorted(os.listdir(txt_dir), key=lambda x: int(x.split("_")[1]))

outline = []
outline.append("# Megaminds AI & Machine Learning Course - Full 12-Session Outline\n")
outline.append("This document contains the exact extracted text from the 12 lesson PDFs of the AI & ML course.\n")

for fname in files:
    fpath = os.path.join(txt_dir, fname)
    session_num = fname.split("_")[1]
    
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    outline.append(f"## Session {session_num}: {fname.replace('.txt', '')}\n")
    outline.append("```text")
    outline.append(content)
    outline.append("```\n")

with open(output_file, "w", encoding="utf-8") as out:
    out.write("\n".join(outline))

print(f"Outline written to {output_file}")
