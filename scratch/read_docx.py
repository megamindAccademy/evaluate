import zipfile
import xml.etree.ElementTree as ET

docx_path = r"C:\Users\rowan\OneDrive\Megaminds curriculum\AGES (10-16)\Programming\Game Development\unity\GameDevelop.docx"

try:
    with zipfile.ZipFile(docx_path) as docx:
        xml_content = docx.read('word/document.xml')
        root = ET.fromstring(xml_content)
        
        # Word XML namespaces
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        
        paragraphs = []
        for paragraph in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            texts = [node.text for node in paragraph.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text]
            if texts:
                paragraphs.append("".join(texts))
                
        full_text = "\n".join(paragraphs)
        print("Successfully read GameDevelop.docx!")
        print("\n--- CONTENT ---")
        print(full_text[:4000]) # First 4000 chars
        print("--- END OF PREVIEW ---")
        
        with open("scratch/unity_docx_content.txt", "w", encoding="utf-8") as out:
            out.write(full_text)
            
except Exception as e:
    print("Error reading docx:", e)
