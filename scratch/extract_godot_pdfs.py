import os
from pypdf import PdfReader

godot_dir = r"C:\Users\rowan\OneDrive\Megaminds curriculum\AGES (10-16)\Programming\Game Development\godot"
out_dir = r"c:\Users\rowan\Desktop\ev\evaluate\scratch\godot_pdf_text"
os.makedirs(out_dir, exist_ok=True)

# Scan through SESSION_01 to SESSION_12
for i in range(1, 13):
    sess_dir_name = f"SESSION_{i:02d}"
    sess_path = os.path.join(godot_dir, sess_dir_name)
    if not os.path.exists(sess_path):
        print(f"Directory {sess_dir_name} not found!")
        continue
    
    print(f"Scanning {sess_dir_name}...")
    
    # We will search for all PDFs recursively inside this session directory
    for root, dirs, files in os.walk(sess_path):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                print(f"  Found PDF: {pdf_path}")
                try:
                    reader = PdfReader(pdf_path)
                    text_content = []
                    for page_idx, page in enumerate(reader.pages, 1):
                        text = page.extract_text()
                        text_content.append(f"=== Page {page_idx} ===\n{text}\n")
                    
                    # Clean filename for output
                    clean_name = f"{sess_dir_name}_{os.path.basename(root)}_{file.replace('.pdf', '')}.txt"
                    # Replace spaces and special characters
                    clean_name = clean_name.replace(" ", "_").replace("(", "").replace(")", "")
                    out_path = os.path.join(out_dir, clean_name)
                    
                    with open(out_path, "w", encoding="utf-8") as f:
                        f.write("".join(text_content))
                    print(f"    Extracted to {clean_name}")
                except Exception as e:
                    print(f"    Error extracting {file}: {e}")
