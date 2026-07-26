import os
from pypdf import PdfReader

pdf_dir = r"C:\Users\rowan\OneDrive\Megaminds curriculum\AGES (10-16)\Programming\Python\AI & Machine Learning"
out_dir = r"c:\Users\rowan\Desktop\ev\evaluate\artifacts\ai_pdf_text"
os.makedirs(out_dir, exist_ok=True)

# Find all session PDFs
pdf_files = []
levels = ["New-Level1", "New-Level2", "New-Level3"]
for level in levels:
    level_path = os.path.join(pdf_dir, level)
    if not os.path.exists(level_path):
        continue
    for session in sorted(os.listdir(level_path)):
        sess_path = os.path.join(level_path, session)
        if not os.path.isdir(sess_path):
            continue
        summary_path = os.path.join(sess_path, "Summary")
        if not os.path.exists(summary_path):
            continue
        for file in os.listdir(summary_path):
            if file.lower().endswith(".pdf"):
                full_pdf = os.path.join(summary_path, file)
                pdf_files.append((level, session, file, full_pdf))

print(f"Found {len(pdf_files)} PDFs.")

for idx, (lvl, sess, fname, fpath) in enumerate(pdf_files, 1):
    try:
        reader = PdfReader(fpath)
        text_content = []
        for p_idx, page in enumerate(reader.pages, 1):
            text = page.extract_text()
            text_content.append(f"--- Page {p_idx} ---\n{text}\n")
        
        out_name = f"session_{idx}_{lvl}_{sess}.txt"
        out_path = os.path.join(out_dir, out_name)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("".join(text_content))
        print(f"Extracted: {out_name}")
    except Exception as e:
        print(f"Error extracting {fname}: {e}")
