import json
import os
import re
import time
import sys
from deep_translator import GoogleTranslator

sys.stdout.reconfigure(encoding='utf-8')

def translate_text(text, retries=3):
    if not bool(re.search(r'[\u0600-\u06FF]', text)):
        return text
        
    for i in range(retries):
        try:
            translator = GoogleTranslator(source='ar', target='en')
            if len(text) > 4000:
                chunks = [text[j:j+4000] for j in range(0, len(text), 4000)]
                translated_chunks = []
                for chunk in chunks:
                    time.sleep(1)
                    translated_chunks.append(translator.translate(chunk))
                res = "".join(translated_chunks)
            else:
                time.sleep(0.5) # Gentle wait
                res = translator.translate(text)
            
            with open('translation_log.txt', 'a', encoding='utf-8') as f:
                f.write(f"  [+] Translated: {text[:40]}... -> {res[:40]}...\n")
            return res if res else text
        except Exception as e:
            time.sleep(2)
            if i == retries - 1:
                with open('translation_log.txt', 'a', encoding='utf-8') as f:
                    f.write(f"  [-] Error translating after retries: {e} -> Text: {text[:30]}\n")
                return text

def translate_json_obj(obj):
    if isinstance(obj, dict):
        new_dict = {}
        for k, v in obj.items():
            new_dict[k] = translate_json_obj(v)
        return new_dict
    elif isinstance(obj, list):
        return [translate_json_obj(item) for item in obj]
    elif isinstance(obj, str):
        if bool(re.search(r'[\u0600-\u06FF]', obj)):
            return translate_text(obj)
        return obj
    else:
        return obj

def process_directory(directory):
    with open('translation_log.txt', 'a', encoding='utf-8') as f:
        f.write("\n==============================================\n")
        f.write("Resuming robust translation with VERBOSE logging...\n")
        f.write("==============================================\n\n")
        
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if not bool(re.search(r'[\u0600-\u06FF]', content)):
                    continue
                
                with open('translation_log.txt', 'a', encoding='utf-8') as f:
                    f.write(f"\n[FILE] Processing: {file_path}\n")
                    
                try:
                    data = json.loads(content)
                    translated_data = translate_json_obj(data)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(translated_data, f, ensure_ascii=False, indent=2)
                    with open('translation_log.txt', 'a', encoding='utf-8') as f:
                        f.write(f"[SUCCESS] Saved: {file_path}\n")
                except Exception as e:
                    with open('translation_log.txt', 'a', encoding='utf-8') as f:
                        f.write(f"[ERROR] on {file_path}: {e}\n")
                        
    with open('translation_log.txt', 'a', encoding='utf-8') as f:
        f.write("\n✅ Translation fully complete!\n")

if __name__ == "__main__":
    process_directory("database")
